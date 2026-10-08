import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from journey import chain, run
from validate import IntegrityError, validate_journey


def resigned(log):
    """Recompute every hash to show structural tests catch more than tampering."""
    return chain([{k: v for k, v in row.items()
                   if k not in {"sequence", "previous_hash", "hash"}}
                  for row in log])


class ValidationTests(unittest.TestCase):
    def test_accepts_all_clean_arms(self):
        for arm in "ABC":
            with self.subTest(arm=arm):
                result = validate_journey(run(arm), arm)
                self.assertTrue(result["chain_valid"])
                self.assertEqual(result["events"], 10)

    def test_missing_posttest_rejected_even_when_resigned(self):
        rows = run("C")
        altered = resigned([r for r in rows if not (
            r["stage"] == "T2" and r["channel"] == "assessment")])
        with self.assertRaises(IntegrityError):
            validate_journey(altered, "C")

    def test_wrong_arm_rejected_even_when_resigned(self):
        rows = run("A")
        rows[1]["arm"] = "C"
        with self.assertRaisesRegex(IntegrityError, "arm or protocol"):
            validate_journey(resigned(rows), "A")

    def test_wrong_item_rejected_even_when_resigned(self):
        rows = run("B")
        rows[4]["item_id"] = "E3"
        with self.assertRaises(IntegrityError):
            validate_journey(resigned(rows), "B")

    def test_wrong_assessment_prompt_rejected_even_when_resigned(self):
        rows = run("C")
        rows[4]["message"] = "A substitute prompt not in the instrument"
        with self.assertRaisesRegex(IntegrityError, "prompt"):
            validate_journey(resigned(rows), "C")

    def test_reordered_stages_rejected_even_when_resigned(self):
        rows = run("B")
        rows[4], rows[6] = rows[6], rows[4]
        with self.assertRaises(IntegrityError):
            validate_journey(resigned(rows), "B")

    def test_missing_lesson_rejected(self):
        rows = run("A")
        with self.assertRaises(IntegrityError):
            validate_journey(resigned(rows[:2] + rows[3:]), "A")

    def test_teaching_stage_item_rejected(self):
        rows = run("C")
        rows[2]["item_id"] = "E2"
        with self.assertRaises(IntegrityError):
            validate_journey(resigned(rows), "C")

    def test_version_change_rejected(self):
        rows = run("C")
        rows[2]["version"] = "undocumented-change"
        with self.assertRaises(IntegrityError):
            validate_journey(resigned(rows), "C")

    def test_empty_and_wrong_arm_rejected(self):
        with self.assertRaises(IntegrityError):
            validate_journey([], "A")
        with self.assertRaises(IntegrityError):
            validate_journey(run("A"), "X")


if __name__ == "__main__":
    unittest.main()
