import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from journey import ARMS, ITEMS, artifact, chain, isolated, run, verify


class JourneyTests(unittest.TestCase):
    def test_all_arms_and_stages(self):
        for arm in ARMS:
            rows = run(arm)
            self.assertEqual({r["stage"] for r in rows}, {"T0", "T1", "T2", "T3", "T4"})
            self.assertTrue(verify(rows))
            self.assertTrue(isolated(rows))

    def test_deterministic(self):
        self.assertEqual(artifact(), artifact())

    def test_tampering_detected(self):
        log = run("C")
        log[2]["message"] = "tampered"
        self.assertFalse(verify(log))

    def test_reordering_detected(self):
        log = run("B")
        log[2], log[3] = log[3], log[2]
        self.assertFalse(verify(log))

    def test_leakage_detected_even_with_valid_hashes(self):
        log = run("C")
        rows = [{k: v for k, v in row.items()
                 if k not in {"sequence", "previous_hash", "hash"}} for row in log]
        rows[2]["message"] += " " + ITEMS["T2"][1]
        injected = chain(rows)
        self.assertTrue(verify(injected))
        self.assertFalse(isolated(injected))

    def test_invalid_arm(self):
        with self.assertRaises(ValueError):
            run("D")

    def test_no_lessons_during_independent_assessment(self):
        for arm in ARMS:
            for row in run(arm):
                if row["stage"] != "T1":
                    self.assertNotEqual(row["channel"], "lesson")

    def test_artifact_disclaims_human_evidence(self):
        output = artifact()
        self.assertIn("SYNTHETIC", output["provenance"])
        self.assertIn("human learning", output["prohibited_claims"])

if __name__ == "__main__":
    unittest.main()
