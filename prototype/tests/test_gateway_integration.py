import json
import os
import socket
import tempfile
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from prototype.separated_assessment.service import Service
from prototype.separated_assessment import gateway


class GatewayIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.sockpath = str(Path(cls.temp.name) / "assessor.sock")
        cls.assessor = Service(cls.sockpath)
        cls.assessor_thread = threading.Thread(target=cls.assessor.serve_forever, daemon=True)
        cls.assessor_thread.start()
        gateway.ASSESSOR_SOCKET = cls.sockpath
        cls.front = ThreadingHTTPServer(("127.0.0.1", 0), gateway.Handler)
        cls.front_thread = threading.Thread(target=cls.front.serve_forever, daemon=True)
        cls.front_thread.start()
        cls.base = "http://127.0.0.1:" + str(cls.front.server_address[1])

    @classmethod
    def tearDownClass(cls):
        cls.front.shutdown()
        cls.front.server_close()
        cls.front_thread.join(timeout=3)
        cls.assessor.shutdown()
        cls.assessor.server_close()
        cls.assessor_thread.join(timeout=3)
        cls.temp.cleanup()

    def setUp(self):
        with gateway.LOCK:
            gateway.SESSIONS.clear()

    def post(self, route, obj):
        req = Request(self.base + route, data=json.dumps(obj).encode(),
                      headers={"Content-Type": "application/json"})
        with urlopen(req, timeout=5) as response:
            return json.loads(response.read())

    def test_all_three_arms_end_to_end(self):
        for arm in "ABC":
            with self.subTest(arm=arm):
                current = self.post("/api/start", {"arm": arm})
                token = current["token"]
                self.assertEqual(current["stage"], "T0")
                self.assertIn("question", current)
                current = self.post("/api/submit", {"token": token, "stage": "T0", "answer": "synthetic"})
                self.assertEqual(current["stage"], "T1")
                self.assertNotIn("question", current)
                current = self.post("/api/submit", {"token": token, "stage": "T1",
                                                       "answer": "This causes a change"})
                if arm == "C":
                    self.assertEqual(current["branch"], "causal-claim")
                    self.assertEqual(current["provider"], "deterministic_scripted_mock")
                current = self.post("/api/submit", {"token": token, "stage": "T1", "answer": ""})
                self.assertEqual(current["stage"], "T2")
                for stage, expected in (("T2", "T3"), ("T3", "T4"), ("T4", "DONE")):
                    current = self.post("/api/submit", {"token": token, "stage": stage,
                                                         "answer": "hypothetical response"})
                    self.assertEqual(current["stage"], expected)
                self.assertTrue(current["complete"])
                self.assertTrue(self.post("/api/end", {"token": token})["deleted"])

    def test_out_of_sequence_and_old_token_rejected(self):
        current = self.post("/api/start", {"arm": "C"})
        token = current["token"]
        with self.assertRaises(HTTPError) as err:
            self.post("/api/submit", {"token": token, "stage": "T3", "answer": "test"})
        self.assertEqual(err.exception.code, 400)
        self.assertTrue(self.post("/api/end", {"token": token})["deleted"])
        with self.assertRaises(HTTPError):
            self.post("/api/submit", {"token": token, "stage": "T0", "answer": "test"})

    def test_browser_never_receives_future_item(self):
        current = self.post("/api/start", {"arm": "B"})
        from prototype.separated_assessment.private_items import ITEMS
        for stage in ("T2", "T3", "T4"):
            self.assertNotIn(ITEMS[stage], json.dumps(current))
        current = self.post("/api/submit", {"token": current["token"],
                                            "stage": "T0", "answer": "baseline"})
        for stage in ("T2", "T3", "T4"):
            self.assertNotIn(ITEMS[stage], json.dumps(current))

    def test_tutor_code_no_private_item_import(self):
        source = Path(gateway.__file__).read_text()
        self.assertNotIn("from .private_items import", source)
        self.assertNotIn("import private_items", source)

    def test_unknown_arm_and_missing_capability(self):
        with self.assertRaises(HTTPError):
            self.post("/api/start", {"arm": "invalid"})
        with self.assertRaises(HTTPError):
            self.post("/api/submit", {"token": "bad", "stage": "T0", "answer": "x"})

    def test_health_and_same_origin_no_caching(self):
        with urlopen(self.base + "/api/health") as res:
            status = json.loads(res.read())
            self.assertEqual(status["mode"], "separate_assessor_fixture")
            self.assertEqual(res.headers["Cache-Control"], "no-store")


if __name__ == "__main__":
    unittest.main()
