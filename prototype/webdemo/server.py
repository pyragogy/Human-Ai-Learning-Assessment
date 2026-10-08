"""HALA Research Demonstrator v0.2 — local, ephemeral scripted study flow.

STANDARD LIBRARY ONLY. Not for real participants, not approved human-subjects
research, not an AI model, not a validated learning assessment.
Start: python prototype/webdemo/server.py
"""
import json
import secrets
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

try:
    from .assessment import ITEMS, STAGES
    from .teaching import LESSONS
except ImportError:
    from assessment import ITEMS, STAGES
    from teaching import LESSONS

HOST = "127.0.0.1"
PORT = 8765
MAX_BODY = 8192
ROOT = Path(__file__).resolve().parent
SESSIONS = {}
LOCK = threading.Lock()
MAX_SESSIONS = 100
MAX_RESPONSE = 4000
SESSION_TTL_SECONDS = 30 * 60


def purge_expired(now=None):
    """Call under LOCK; lazy monotonic expiration, no background worker."""
    if now is None:
        now = time.monotonic()
    for token, state in list(SESSIONS.items()):
        if now - state.get("last_seen", now) >= SESSION_TTL_SECONDS:
            del SESSIONS[token]


def delete_session(token):
    """Remove an active demo session and its unsaved responses."""
    with LOCK:
        purge_expired()
        return SESSIONS.pop(token, None) is not None


def create_session(arm):
    if arm not in LESSONS:
        raise ValueError("Unknown study arm")
    token = secrets.token_urlsafe(24)
    with LOCK:
        purge_expired()
        if len(SESSIONS) >= MAX_SESSIONS:
            raise ValueError("Demo session limit reached; end old sessions or retry after expiry.")
        SESSIONS[token] = {"arm": arm, "index": 0, "responses": {}, "teaching_turn": 0,
                           "last_seen": time.monotonic()}
    return token


def snapshot(state):
    stage = STAGES[state["index"]] if state["index"] < len(STAGES) else "DONE"
    result = {
        "stage": stage,
        "arm": state["arm"],
        "complete": stage == "DONE",
        "disclaimer": "Local scripted demonstration only — do not enter personal data or conduct human research.",
    }
    if stage == "T1":
        lesson = LESSONS[state["arm"]]
        result["title"] = lesson["title"]
        result["lesson"] = lesson["turns"][state["teaching_turn"]]
        result["step"] = state["teaching_turn"] + 1
        result["steps"] = len(lesson["turns"])
    elif stage in ITEMS:
        result["title"] = ITEMS[stage]["title"]
        result["scenario"] = ITEMS[stage]["scenario"]
        result["question"] = ITEMS[stage]["question"]
        if stage == "T4":
            result["notice"] = "Same-session demonstration: this is NOT a real 7–14 day retention measure."
    else:
        result["notice"] = "Finished — demo responses remain only in server RAM until session deletion, expiry or server restart."
        result["submitted_stages"] = sorted(state["responses"])
    return result


def submit(state, stage, answer):
    if state["index"] >= len(STAGES) or stage != STAGES[state["index"]]:
        raise ValueError("Stage mismatch — proceed only in order")
    if not isinstance(answer, str) or len(answer) > MAX_RESPONSE:
        raise ValueError("Response must be text under 4001 characters")
    if stage == "T1":
        state["teaching_turn"] += 1
        if state["teaching_turn"] >= len(LESSONS[state["arm"]]["turns"]):
            state["index"] += 1
    else:
        if not answer.strip():
            raise ValueError("Write a short answer to continue")
        state["responses"][stage] = answer
        state["index"] += 1
    return snapshot(state)


class Handler(BaseHTTPRequestHandler):
    server_version = "HALA-Demo/0.2"

    def log_message(self, format, *args):
        # No request bodies, answers, or tokens in the server log.
        pass

    def common_headers(self, code, mime):
        self.send_response(code)
        self.send_header("Content-Type", mime)
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-Security-Policy",
                         "default-src 'none'; script-src 'self'; style-src 'self'; "
                         "connect-src 'self'; img-src 'self'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()

    def send_json(self, obj, status=200):
        payload = json.dumps(obj).encode("utf-8")
        self.common_headers(status, "application/json; charset=utf-8")
        self.wfile.write(payload)

    def do_GET(self):
        route = urlsplit(self.path).path
        if route == "/":
            path, mime = ROOT / "index.html", "text/html; charset=utf-8"
        elif route == "/app.js":
            path, mime = ROOT / "app.js", "text/javascript; charset=utf-8"
        elif route == "/style.css":
            path, mime = ROOT / "style.css", "text/css; charset=utf-8"
        elif route == "/api/health":
            self.send_json({"status": "ok", "version": "0.2", "synthetic_only": True})
            return
        else:
            self.send_json({"error": "Not found"}, 404)
            return
        self.common_headers(200, mime)
        self.wfile.write(path.read_bytes())

    def do_POST(self):
        route = urlsplit(self.path).path
        if route not in ("/api/start", "/api/submit", "/api/end"):
            self.send_json({"error": "Not found"}, 404)
            return
        if self.headers.get("Content-Type", "").split(";")[0].strip().lower() != "application/json":
            self.send_json({"error": "JSON content-type required"}, 415)
            return
        try:
            size = int(self.headers.get("Content-Length", "-1"))
            if not 0 <= size <= MAX_BODY:
                raise ValueError("Invalid request length")
            obj = json.loads(self.rfile.read(size))
            if not isinstance(obj, dict):
                raise ValueError("Expected JSON object")
            if route == "/api/start":
                arm = obj.get("arm")
                token = create_session(arm)
                with LOCK:
                    response = snapshot(SESSIONS[token])
                response["token"] = token
            else:
                token = obj.get("token")
                if not isinstance(token, str) or not token:
                    raise ValueError("Missing token")
                if route == "/api/end":
                    response = {"deleted": delete_session(token)}
                else:
                    with LOCK:
                        purge_expired()
                        if token not in SESSIONS:
                            raise ValueError("Unknown or expired session")
                        state = SESSIONS[token]
                        response = submit(state, obj.get("stage"), obj.get("answer", ""))
                        state["last_seen"] = time.monotonic()
            self.send_json(response)
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            self.send_json({"error": str(exc)}, 400)


def main():
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"HALA scripted demo: http://{HOST}:{PORT} (local use only)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
