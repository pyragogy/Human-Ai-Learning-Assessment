import json
import sys
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "webdemo"))
from assessment import ITEMS
from server import Handler, SESSIONS, LOCK, MAX_SESSIONS, SESSION_TTL_SECONDS, create_session, snapshot, submit, delete_session, purge_expired


class StateMachineTests(unittest.TestCase):
    def setUp(self):
        with LOCK:
            SESSIONS.clear()

    def test_each_arm_reaches_completion_in_order(self):
        for arm in "ABC":
            token = create_session(arm)
            state = SESSIONS[token]
            self.assertEqual(snapshot(state)["stage"], "T0")
            with self.assertRaisesRegex(ValueError, "Stage mismatch"):
                submit(state, "T2", "premature")
            submit(state, "T0", "baseline illustrative answer")
            self.assertEqual(snapshot(state)["stage"], "T1")
            submit(state, "T1", "")
            self.assertEqual(snapshot(state)["stage"], "T1")
            submit(state, "T1", "")
            for phase in ("T2", "T3", "T4"):
                self.assertEqual(snapshot(state)["stage"], phase)
                submit(state, phase, "A hypothetical student answer")
            self.assertEqual(snapshot(state)["stage"], "DONE")
            self.assertEqual(sorted(state["responses"]), ["T0", "T2", "T3", "T4"])

    def test_no_empty_assessment_submissions(self):
        state = SESSIONS[create_session("A")]
        with self.assertRaisesRegex(ValueError, "short answer"):
            submit(state, "T0", "   ")

    def test_invalid_answer_type_and_size(self):
        state = SESSIONS[create_session("B")]
        for value in (1, None, "x" * 4001):
            with self.assertRaises(ValueError):
                submit(state, "T0", value)

    def test_teaching_snapshot_excludes_protected_items(self):
        state = SESSIONS[create_session("C")]
        submit(state, "T0", "some answer")
        payload = json.dumps(snapshot(state))
        for phase in ("T2", "T3", "T4"):
            self.assertNotIn(ITEMS[phase]["scenario"], payload)
            self.assertNotIn(ITEMS[phase]["question"], payload)


    def test_expired_sessions_evicted_at_creation(self):
        token = create_session("A")
        with LOCK:
            SESSIONS[token]["last_seen"] -= SESSION_TTL_SECONDS + 1
        other = create_session("C")
        self.assertNotIn(token, SESSIONS)
        self.assertIn(other, SESSIONS)

    def test_explicit_disposal_removes_answers(self):
        token = create_session("C")
        submit(SESSIONS[token], "T0", "synthetic answer to delete")
        self.assertTrue(delete_session(token))
        self.assertNotIn(token, SESSIONS)
        self.assertFalse(delete_session(token))

    def test_live_session_capacity_is_bounded(self):
        for _ in range(MAX_SESSIONS):
            create_session("B")
        with self.assertRaisesRegex(ValueError, "session limit"):
            create_session("A")

    def test_t4_notice_is_not_real_retention(self):
        state = SESSIONS[create_session("A")]
        submit(state, "T0", "baseline")
        submit(state, "T1", "")
        submit(state, "T1", "")
        submit(state, "T2", "post")
        submit(state, "T3", "transfer")
        self.assertIn("NOT a real", snapshot(state)["notice"])


class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = "http://127.0.0.1:" + str(cls.server.server_address[1])

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def request(self, route, payload=None):
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        headers = {} if body is None else {"Content-Type": "application/json"}
        req = Request(self.base + route, data=body, headers=headers)
        with urlopen(req, timeout=3) as response:
            return json.loads(response.read()), response.headers

    def test_health(self):
        result, headers = self.request("/api/health")
        self.assertTrue(result["synthetic_only"])
        self.assertEqual(headers["Cache-Control"], "no-store")

    def test_serves_frontend(self):
        with urlopen(self.base + "/", timeout=3) as response:
            self.assertIn(b"HALA", response.read())
            self.assertIn("default-src 'none'", response.headers["Content-Security-Policy"])

    def test_http_journey(self):
        started, _ = self.request("/api/start", {"arm": "C"})
        self.assertEqual(started["stage"], "T0")
        token = started["token"]
        next_step, _ = self.request("/api/submit", {"token": token, "stage": "T0", "answer": "draft"})
        self.assertEqual(next_step["stage"], "T1")
        for _ in range(2):
            next_step, _ = self.request("/api/submit", {"token": token, "stage": "T1", "answer": ""})
        self.assertEqual(next_step["stage"], "T2")


    def test_end_endpoint_disposes_session(self):
        started, _ = self.request("/api/start", {"arm": "C"})
        token = started["token"]
        ended, _ = self.request("/api/end", {"token": token})
        self.assertTrue(ended["deleted"])
        with self.assertRaises(HTTPError) as cm:
            self.request("/api/submit", {"token": token, "stage": "T0", "answer": "x"})
        self.assertEqual(cm.exception.code, 400)

    def test_end_missing_session_id_is_rejected(self):
        with self.assertRaises(HTTPError):
            self.request("/api/end", {})

    def test_invalid_arm_http_400(self):
        with self.assertRaises(HTTPError) as cm:
            self.request("/api/start", {"arm": "Z"})
        self.assertEqual(cm.exception.code, 400)

    def test_missing_token_http_400(self):
        with self.assertRaises(HTTPError) as cm:
            self.request("/api/submit", {"stage": "T0", "answer": "test"})
        self.assertEqual(cm.exception.code, 400)


if __name__ == "__main__":
    unittest.main()
