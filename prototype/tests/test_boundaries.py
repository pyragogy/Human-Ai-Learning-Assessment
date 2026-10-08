import json
import os
import socket
import stat
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from prototype.boundaries import tutor_packet, rater_packet
from prototype.separated_assessment.service import AssessmentStore, Service, CAP_TTL


class ContractTests(unittest.TestCase):
    def test_tutor_payload_allowlist(self):
        packet = dict(session_ref="synthetic-1", arm="C", topic="causal",
                      turn=0, dialogue=[], provider="mock", policy_hash="abc")
        self.assertEqual(tutor_packet(packet), packet)
        for unsafe in ("baseline_score", "assessment_item", "rubric_key", "response_text"):
            with self.subTest(field=unsafe):
                with self.assertRaises(ValueError):
                    tutor_packet({**packet, unsafe: "MUST NOT PASS"})

    def test_blind_rater_packet(self):
        packet = dict(response_ref="masked-1", item_code="T2",
                      form_version="fixture", response_text="Synthetic text",
                      packet_version="1")
        self.assertEqual(rater_packet(packet), packet)
        for unsafe in ("arm", "provider", "tutor_transcript", "participant_id"):
            with self.subTest(field=unsafe):
                with self.assertRaises(ValueError):
                    rater_packet({**packet, unsafe: "LEAK"})


class AssessmentStoreTests(unittest.TestCase):
    def setUp(self):
        self.now = [1000.0]
        self.store = AssessmentStore(clock=lambda: self.now[0])
        self.session = self.store.handle({"op": "start"})["session"]

    def issue(self):
        return self.store.handle({"op": "issue", "session": self.session})

    def test_stage_specific_item_and_replay(self):
        expected = ("T0", "T2", "T3", "T4")
        for stage in expected:
            issued = self.issue()
            self.assertEqual(issued["stage"], stage)
            response = self.store.handle({"op": "item", "capability": issued["capability"]})
            self.assertEqual(response["stage"], stage)
            self.assertNotIn("T2", str(response) if stage == "T0" else "")
            completed = self.store.handle({"op": "complete", "capability": issued["capability"]})
            self.assertEqual(completed["stage"], stage)
            with self.assertRaises(ValueError):
                self.store.handle({"op": "item", "capability": issued["capability"]})
            with self.assertRaises(ValueError):
                self.store.handle({"op": "complete", "capability": issued["capability"]})
        with self.assertRaises(ValueError):
            self.issue()

    def test_expired_capability_denied(self):
        issued = self.issue()
        self.now[0] += CAP_TTL + 1
        with self.assertRaises(ValueError):
            self.store.handle({"op": "item", "capability": issued["capability"]})
        with self.assertRaises(ValueError):
            self.store.handle({"op": "complete", "capability": issued["capability"]})

    def test_issuing_new_capability_revokes_old_one(self):
        old = self.issue()
        new = self.issue()
        with self.assertRaises(ValueError):
            self.store.handle({"op": "item", "capability": old["capability"]})
        self.assertEqual(self.store.handle({"op": "item", "capability": new["capability"]})["stage"], "T0")

    def test_worker_session_expiry_and_capacity(self):
        from prototype.separated_assessment.service import SESSION_TTL, MAX_SESSIONS
        for _ in range(MAX_SESSIONS - 1):
            self.store.handle({"op": "start"})
        with self.assertRaisesRegex(ValueError, "capacity"):
            self.store.handle({"op": "start"})
        self.now[0] += SESSION_TTL + 1
        self.assertEqual(len(self.store.sessions), MAX_SESSIONS)
        created = self.store.handle({"op": "start"})
        self.assertEqual(created["stage"], "T0")
        self.assertEqual(len(self.store.sessions), 1)

    def test_worker_end_revokes_capabilities(self):
        issued = self.issue()
        self.assertTrue(self.store.handle({"op": "end", "session": self.session})["deleted"])
        with self.assertRaises(ValueError):
            self.store.handle({"op": "item", "capability": issued["capability"]})
        with self.assertRaises(ValueError):
            self.issue()

    def test_rejects_invalid_commands(self):
        for command in ({}, {"op": "issue", "session": "forged"},
                        {"op": "item", "capability": "forged"},
                        {"op": "complete", "capability": "forged"},
                        {"op": "tutor", "session": self.session}):
            with self.subTest(command=command):
                with self.assertRaises(ValueError):
                    self.store.handle(command)


class SocketTests(unittest.TestCase):
    def test_socket_rejects_unauthenticated_and_wrong_secret(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "assessor.sock")
            secret = "synthetic-authentication-secret-for-tests"
            server = Service(path, secret=secret)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                for command in ({"op": "start"}, {"op": "start", "auth": "wrong"}):
                    with self.subTest(command=command):
                        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                            sock.connect(path)
                            sock.sendall(json.dumps(command).encode() + b"\\n")
                            response = b""
                            while not response.endswith(b"\\n"):
                                response += sock.recv(1024)
                        obj = json.loads(response)
                        self.assertFalse(obj["ok"])
                        self.assertIn("Unauthorized", obj["error"])
                self.assertEqual(len(server.store.sessions), 0)
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=3)

    def test_worker_requires_nonempty_secret(self):
        with tempfile.TemporaryDirectory() as directory:
            for secret in (None, "", "weak"):
                with self.subTest(secret=secret):
                    with self.assertRaises(ValueError):
                        Service(os.path.join(directory, "assessor.sock"), secret=secret)

    def test_unix_socket_round_trip_and_permissions(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "assessor.sock")
            server = Service(path, secret="unit-test-access-secret-for-synthetic-fixture")
            os.chmod(path, 0o600)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                self.assertEqual(stat.S_IMODE(os.stat(path).st_mode), 0o600)
                with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                    sock.connect(path)
                    sock.sendall(json.dumps({"op":"start", "auth":"unit-test-access-secret-for-synthetic-fixture"}).encode() + b"\n")
                    answer = b""
                    while not answer.endswith(b"\n"):
                        answer += sock.recv(1024)
                payload = json.loads(answer)
                self.assertTrue(payload["ok"])
                self.assertEqual(payload["result"]["stage"], "T0")
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=3)


if __name__ == "__main__":
    unittest.main()
