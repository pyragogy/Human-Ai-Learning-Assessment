"""Loopback browser orchestrator for HALA's separate assessor worker.

Synthetic-only, local integration demonstration. No human-subject use.
The orchestrator does not import protected assessment items.
"""
import json
import os
import secrets
import socket
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from prototype.webdemo.adaptive import respond_to_claim
from prototype.webdemo.teaching import LESSONS

ROOT = Path(__file__).resolve().parents[1] / "webdemo"
ASSESSOR_SOCKET = os.environ.get("HALA_ASSESSOR_SOCKET", "/tmp/hala-assessor-private/assessor.sock")
STAGES = ("T0", "T1", "T2", "T3", "T4")
SESSIONS = {}
LOCK = threading.Lock()
TTL = 30 * 60
MAX_SESSIONS = 100
MAX_RESPONSE = 4000


def worker(command, socket_path=None):
    """Talk to the assessor through a local Unix socket, never from tutor context."""
    destination = socket_path or ASSESSOR_SOCKET
    secret = os.environ.get("HALA_ASSESSOR_SECRET")
    if not secret or len(secret) < 32:
        raise ValueError("HALA_ASSESSOR_SECRET must be configured")
    command = {**command, "auth": secret}
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)
        sock.connect(destination)
        sock.sendall((json.dumps(command) + "\n").encode())
        data = bytearray()
        while not data.endswith(b"\n"):
            chunk = sock.recv(4096)
            if not chunk or len(data) + len(chunk) > 16384:
                raise ValueError("Invalid assessor reply")
            data.extend(chunk)
    response = json.loads(data)
    if not response.get("ok"):
        raise ValueError(response.get("error", "Assessor refused request"))
    return response["result"]


def purge(now=None):
    now = time.monotonic() if now is None else now
    for token, state in list(SESSIONS.items()):
        if now - state["last_seen"] >= TTL:
            SESSIONS.pop(token, None)


def make_session(arm, call=worker):
    if arm not in LESSONS:
        raise ValueError("Unknown arm")
    with LOCK:
        purge()
        if len(SESSIONS) >= MAX_SESSIONS:
            raise ValueError("Session capacity reached")
        remote = call({"op": "start"})
        identifier = secrets.token_urlsafe(24)
        state = {"arm": arm, "stage": "T0", "turn": 0,
                 "worker_session": remote["session"], "capability": None,
                 "last_seen": time.monotonic()}
        SESSIONS[identifier] = state
        try:
            result = snapshot(state, call)
        except Exception:
            SESSIONS.pop(identifier, None)
            raise
        return identifier, result


def snapshot(state, call=worker):
    stage = state["stage"]
    response = {
        "stage": stage, "arm": state["arm"], "complete": stage == "DONE",
        "disclaimer": "SYNTHETIC ONLY: no real learners, no psychometric findings."
    }
    if stage == "T1":
        lesson = LESSONS[state["arm"]]
        response["title"] = lesson["title"]
        if state["arm"] == "C" and state["turn"] == 1:
            reply = respond_to_claim(state.get("claim", ""))
            response.update({"lesson": "Scripted adaptive collaborator: " + reply["message"],
                             "branch": reply["mode"], "mock_policy_sha256": reply["policy_sha256"],
                             "provider": reply["provider"], "synthetic_only": True})
        else:
            response["lesson"] = lesson["turns"][state["turn"]]
        response["step"] = state["turn"] + 1
        response["steps"] = len(lesson["turns"])
        return response
    if stage in ("T0", "T2", "T3", "T4"):
        if state["capability"] is None:
            issued = call({"op": "issue", "session": state["worker_session"]})
            if issued["stage"] != stage:
                raise ValueError("Assessor stage mismatch")
            state["capability"] = issued["capability"]
        item = call({"op": "item", "capability": state["capability"]})
        if item["stage"] != stage:
            raise ValueError("Assessor item mismatch")
        response.update({"title": "Independent " + stage + " assessment",
                         "scenario": "Assessment fixture · " + stage,
                         "question": item["item"], "synthetic_only": True})
        if stage == "T4":
            response["notice"] = "Same-session demonstration: this is NOT a real 7–14 day retention measure."
        return response
    response["submitted_stages"] = ["T0", "T2", "T3", "T4"]
    response["notice"] = "No learning measurements were computed."
    return response


def advance(state, stage, answer, call=worker):
    if stage != state["stage"]:
        raise ValueError("Out-of-sequence stage")
    if not isinstance(answer, str) or len(answer) > MAX_RESPONSE:
        raise ValueError("Invalid response")
    if stage == "T1":
        if state["arm"] == "C" and state["turn"] == 0:
            state["claim"] = answer
        state["turn"] += 1
        if state["turn"] >= len(LESSONS[state["arm"]]["turns"]):
            state["stage"] = "T2"
    elif stage in ("T0", "T2", "T3", "T4"):
        if not answer.strip():
            raise ValueError("An illustrative answer is required")
        if not state["capability"]:
            raise ValueError("No stage capability")
        completed = call({"op": "complete", "capability": state["capability"]})
        if completed["stage"] != stage:
            raise ValueError("Completion receipt mismatch")
        state["capability"] = None
        state["stage"] = {"T0": "T1", "T2": "T3", "T3": "T4", "T4": "DONE"}[stage]
    else:
        raise ValueError("Session finished")
    state["last_seen"] = time.monotonic()
    return snapshot(state, call)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def respond(self, obj, code=200, mime="application/json; charset=utf-8"):
        payload = json.dumps(obj).encode() if not isinstance(obj, bytes) else obj
        self.send_response(code)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        path = urlsplit(self.path).path
        static = {"/": ("index.html", "text/html; charset=utf-8"),
                  "/app.js": ("app.js", "text/javascript; charset=utf-8"),
                  "/style.css": ("style.css", "text/css; charset=utf-8")}
        if path in static:
            filename, mime = static[path]
            return self.respond((ROOT / filename).read_bytes(), mime=mime)
        if path == "/api/health":
            return self.respond({"status": "ok", "mode": "separate_assessor_fixture", "synthetic_only": True})
        self.respond({"error": "Not found"}, 404)

    def do_POST(self):
        path = urlsplit(self.path).path
        if path not in ("/api/start", "/api/submit", "/api/end"):
            return self.respond({"error": "Not found"}, 404)
        if self.headers.get("Content-Type", "").split(";")[0].strip() != "application/json":
            return self.respond({"error": "JSON required"}, 415)
        try:
            size = int(self.headers.get("Content-Length", "-1"))
            if not 0 <= size <= 8192:
                raise ValueError("Invalid request size")
            body = json.loads(self.rfile.read(size))
            if not isinstance(body, dict):
                raise ValueError("Expected JSON object")
            with LOCK:
                purge()
                if path == "/api/start":
                    # make_session takes LOCK itself; release outside this branch below
                    pass
                else:
                    token = body.get("token")
                    if not isinstance(token, str):
                        raise ValueError("Missing session token")
                    if path == "/api/end":
                        return self.respond({"deleted": SESSIONS.pop(token, None) is not None})
                    if token not in SESSIONS:
                        raise ValueError("Unknown or expired session")
                    return self.respond(advance(SESSIONS[token], body.get("stage"), body.get("answer", "")))
            token, response = make_session(body.get("arm"))
            response["token"] = token
            self.respond(response)
        except (ValueError, TypeError, OSError, json.JSONDecodeError) as exc:
            self.respond({"error": str(exc)}, 400)


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 8766), Handler)
    print("HALA with separate assessor: http://127.0.0.1:8766")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
