# PI adversarial synthetic annotation — developer research fixture

**Status:** proposed experimental code awaiting PI review. Do not merge without review.

This fixture originated from PI's scientific challenge in GitHub issue #11: an AI can ask a learner all six epistemic-process questions and produce an apparently complete rubric trace without establishing independent learner proficiency.

## Files

- `prototype/conversation_annotation.py`: deterministic rule-based annotation over ordered AI/learner turns.
- `prototype/fixtures/pi_prompted_coffee.json`: 14-turn coffee/exam synthetic prompt-heavy transcript.
- `prototype/tests/test_conversation_annotation.py`: regression test confirms all six naive codes can appear alongside high AI-scaffold exposure, without emitting any proficiency grade.

## Fields and permitted interpretation

- `observed_codes`: heuristic keyword detections, **not** validated behavioral coding.
- `elicitation`: whether the immediately preceding AI text matched a simple prompt pattern; this is a descriptive *risk tag*, not a trustworthy causal attribution.
- `lexical_echo_flag`: overlap in surface tokens; false positives and false negatives are expected.
- `learner_origin`: explicitly `indeterminate`.
- `proficiency_score`: always `null`, including adversarial and positive comparison fixtures.

The synthetic transcript does **not** show that a learner's actual competence is zero. It demonstrates why naive presence-based coding cannot be equated with a competence estimate. An independently reasoned answer can be prompted; unsolicited answers can also be wrong. Arm C intrinsically solicits critical thinking, so penalising prompted behavior automatically would bias between intervention conditions.

## Falsification aim and limitations

**Demonstrated if tests pass:** a deterministic instrument can expose a counterexample to naive code-presence grading and retain AI-turn context for later expert review.

**Not demonstrated:** construct validity, reliable human ratings, cross-lingual equivalence, true learner-origin identification, authorship detection, or a justified decision threshold. No human-subject data are used.

## PI review questions

1. Can a learner generate all six tags even with superficial or meaningless answers? If yes, keep this as a negative example rather than claiming a robust classifier.
2. Can prompting styles with and without obvious question wording evade the `elicitation` pattern? Identify at least two such failure cases.
3. Can a copied AI sentence evade the lexical overlap flag, or can independently constructed arguments trigger a false positive?
4. Are the data fields sufficiently explicit to support a future *human* coding study without encouraging automatic proficiency scoring?
5. Do not merge before the designated reviewer gate. No live model, adolescent cohort, public data, or deployment.

Run: `python -m unittest discover -s prototype/tests -v`.
