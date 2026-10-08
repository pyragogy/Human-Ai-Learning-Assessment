"""Synthetic fixture regression tests; not psychometric validity tests."""
import json
import unittest
from pathlib import Path

from prototype.conversation_annotation import annotate, PATTERNS

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "pi_prompted_coffee.json"


class SyntheticAnnotationTests(unittest.TestCase):
    def test_scaffolded_fixture_exposes_naive_score_failure(self):
        data = json.loads(FIXTURE.read_text())
        self.assertTrue(data["synthetic_only"])
        result = annotate(data["transcript"])
        observed = {x for row in result["learner_turns"] for x in row["observed_codes"]}
        self.assertEqual(observed, set(PATTERNS))
        self.assertGreaterEqual(result["naive_code_count"], 6)
        self.assertGreaterEqual(
            sum(row["elicitation"] == "potential_ai_scaffold" for row in result["learner_turns"]), 5
        )
        self.assertIsNone(result["proficiency_score"])
        self.assertTrue(all(row["learner_origin"] == "indeterminate" for row in result["learner_turns"]))

    def test_unprompted_observable_action_not_assumed_to_be_proficiency(self):
        turns = [
            {"speaker": "learner", "text": "I need evidence before accepting this claim.",
             "turn_number": 1},
            {"speaker": "ai", "text": "Understood.", "turn_number": 2},
            {"speaker": "learner", "text": "Another possible cause is prior knowledge.",
             "turn_number": 3},
        ]
        result = annotate(turns)
        self.assertEqual(result["learner_turns"][0]["elicitation"], "no_ai_antecedent")
        self.assertIn("EVIDENCE_REQUEST", result["learner_turns"][0]["observed_codes"])
        self.assertEqual(result["learner_turns"][1]["elicitation"], "preceded_by_ai")
        self.assertIsNone(result["proficiency_score"])

    def test_echo_is_only_a_flag_not_an_automatic_grade(self):
        turns = [
            {"speaker": "ai", "text": "The reliable evidence requires more reliable evidence.",
             "turn_number": 1},
            {"speaker": "learner", "text": "Reliable evidence requires more reliable evidence.",
             "turn_number": 2},
        ]
        result = annotate(turns)
        self.assertTrue(result["learner_turns"][0]["lexical_echo_flag"])
        self.assertIsNone(result["proficiency_score"])

    def test_bad_inputs_fail_closed(self):
        invalid = [
            {},
            [{"speaker": "ai", "text": "test"}],
            [{"speaker": "ai", "text": "test", "turn_number": 3}],
            [{"speaker": "unknown", "text": "test", "turn_number": 1}],
            [{"speaker": "ai", "text": "test", "turn_number": 1},
             {"speaker": "ai", "text": "test", "turn_number": 2}],
            [{"speaker": "ai", "text": "x" * 4001, "turn_number": 1}],
        ]
        for value in invalid:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    annotate(value)


if __name__ == "__main__":
    unittest.main()
