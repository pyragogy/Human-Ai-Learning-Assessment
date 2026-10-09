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
            sum(row["known_scaffold_pattern"] for row in result["learner_turns"]), 5
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
        self.assertFalse(result["learner_turns"][0]["preceded_by_ai"])
        self.assertIn("EVIDENCE_REQUEST", result["learner_turns"][0]["observed_codes"])
        self.assertTrue(result["learner_turns"][1]["preceded_by_ai"])
        self.assertFalse(result["learner_turns"][1]["known_scaffold_pattern"])
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

    def test_pi_undetected_paraphrases_are_explicitly_unknown(self):
        for prompt in ("Got any sources to back that up?",
                       "Think about what might cause that instead.",
                       "And how could you check which cause is right?"):
            with self.subTest(prompt=prompt):
                rows = annotate([
                    {"speaker": "ai", "text": prompt, "turn_number": 1},
                    {"speaker": "learner", "text": "Could you provide evidence for this claim?",
                     "turn_number": 2},
                ])["learner_turns"]
                self.assertTrue(rows[0]["preceded_by_ai"])
                self.assertFalse(rows[0]["known_scaffold_pattern"])
                self.assertIsNone(rows[0]["proficiency_score"])

    def test_single_word_and_keyword_salad_do_not_establish_reasoning(self):
        lone = annotate([{"speaker": "learner", "text": "Evidence.", "turn_number": 1}])
        self.assertEqual(lone["naive_code_count"], 0)
        salad = annotate([
            {"speaker": "learner",
             "text": "Evidence source alternative test revise uncertain",
             "turn_number": 1},
        ])
        self.assertGreater(salad["naive_code_count"], 0)
        self.assertTrue(salad["heuristic_annotation_only"])
        self.assertIsNone(salad["proficiency_score"])

    def test_learner_extends_ai_framing_without_automatic_echo_label(self):
        result = annotate([
            {"speaker": "ai", "text": "The experiment controlled for confounding variables",
             "turn_number": 1},
            {"speaker": "learner",
             "text": "The experiment controlled for confounding variables and also measured outcomes",
             "turn_number": 2},
        ])
        self.assertGreater(result["learner_turns"][0]["lexical_overlap_ratio"], 0.5)
        self.assertFalse(result["learner_turns"][0]["lexical_echo_flag"])
        self.assertIsNone(result["proficiency_score"])

    def test_arm_c_scaffolding_is_observation_not_penalty(self):
        result = annotate([
            {"speaker": "ai", "text": "What evidence would challenge your argument?",
             "turn_number": 1},
            {"speaker": "learner", "text": "Evidence about the control group would help.",
             "turn_number": 2},
        ])
        row = result["learner_turns"][0]
        self.assertTrue(row["known_scaffold_pattern"])
        self.assertTrue(row["preceded_by_ai"])
        self.assertNotIn("penalty", row)
        self.assertIsNone(row["proficiency_score"])

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
