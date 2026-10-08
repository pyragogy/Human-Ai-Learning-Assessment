"""HALA separate-process assessment fixture service, Linux/Unix sockets only.

Demo-only protocol. Uses opaque single-use stage capabilities. This is a process
boundary, NOT proof of OS-user privilege separation or field-ready security.
"""
import json
import os
import secrets
import socketserver
import time
from pathlib import Path
from .private_items import ITEMS

STAGE_ORDER = ("T0", "T2", "T3", "T4")
CAP_TTL = 180
MAX_LINE = 4096


class AssessmentStore:
    def __init__(self, clock=None):
        self.clock = clock or time.monotonic
        self.sessions = {}
        self.capabilities = {}

    def handle(self, command):
        if not isinstance(command, dict):
            raise ValueError("Invalid command")
        operation = command.get("op")
        if operation == "start":
            session = secrets.token_urlsafe(24)
            self.sessions[session] = 0
            return {"session": session, "stage": "T0", "synthetic_only": True}
        if operation == "issue":
            session = command.get("session")
            if session not in self.sessions:
                raise ValueError("Unknown session")
            index = self.sessions[session]
            if index >= len(STAGE_ORDER):
                raise ValueError("Already complete")
            stage = STAGE_ORDER[index]
            # At most one outstanding capability per session.
            for token, record in list(self.capabilities.items()):
                if record["session"] == session:
                    del self.capabilities[token]
            token = secrets.token_urlsafe(24)
            self.capabilities[token] = {"session": session, "stage": stage,
                                         "expires": self.clock() + CAP_TTL}
            return {"capability": token, "stage": stage, "ttl_seconds": CAP_TTL}
        if operation == "item":
            token = command.get("capability")
            record = self.capabilities.get(token)
            if not record or record["expires"] < self.clock():
                self.capabilities.pop(token, None)
                raise ValueError("Unknown or expired capability")
            # A capability reveals only its single current item.
            return {"stage": record["stage"], "item": ITEMS[record["stage"]],
                    "synthetic_only": True}
        if operation == "complete":
            token = command.get("capability")
            record = self.capabilities.pop(token, None)
            if not record or record["expires"] < self.clock():
                raise ValueError("Unknown or expired capability")
            session, stage = record["session"], record["stage"]
            expected = STAGE_ORDER[self.sessions[session]]
            if expected != stage:
                raise ValueError("Stage mismatch")
            self.sessions[session] += 1
            return {"receipt": secrets.token_urlsafe(18), "stage": stage,
                    "next_stage": STAGE_ORDER[self.sessions[session]]
                    if self.sessions[session] < len(STAGE_ORDER) else "DONE",
                    "synthetic_only": True}
        raise ValueError("Unsupported operation")


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        line = self.rfile.readline(MAX_LINE + 1)
        try:
            if len(line) > MAX_LINE:
                raise ValueError("Request too large")
            command = json.loads(line.decode("utf-8"))
            result = self.server.store.handle(command)
            reply = {"ok": True, "result": result}
        except (ValueError, TypeError, UnicodeDecodeError, KeyError) as exc:
            reply = {"ok": False, "error": str(exc)}
        self.wfile.write((json.dumps(reply) + "\n").encode("utf-8"))


class Service(socketserver.UnixStreamServer):
    def __init__(self, path, store=None):
        self.store = store or AssessmentStore()
        super().__init__(str(path), Handler)


def serve(path):
    """Bind to private socket in a pre-created restricted directory."""
    path = Path(path)
    if path.exists():
        raise RuntimeError("Socket path already exists; remove stale socket manually")
    old_umask = os.umask(0o077)
    try:
        server = Service(path)
        os.chmod(path, 0o600)
    finally:
        os.umask(old_umask)
    try:
        server.serve_forever()
    finally:
        server.server_close()
        path.unlink(missing_ok=True)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python -m prototype.separated_assessment.service /private/dir/hala.sock")
    serve(sys.argv[1])
