# PI adversarial synthetic annotation — developer research fixture

**Status:** revised on PR #12 in response to PI review; independent recheck pending. Do not merge before review.

This fixture originated from PI's scientific challenge in GitHub issue #11: an AI can ask a learner all six epistemic-process questions and produce an apparently complete rubric trace without establishing independent learner proficiency.

## Files

- `prototype/conversation_annotation.py`: deterministic rule-based annotation over ordered AI/learner turns.
- `prototype/fixtures/pi_prompted_coffee.json`: 14-turn coffee/exam synthetic prompt-heavy transcript.
- `prototype/tests/test_conversation_annotation.py`: regression test confirms all six naive codes can appear alongside high AI-scaffold exposure, without emitting any proficiency grade.

## Fields and permitted interpretation

- `observed_codes`: heuristic keyword detections, **not** validated behavioral coding.
- `known_scaffold_pattern`: Boolean matching only a small list of AI prompting phrases. **False does not mean no scaffolding**; PI demonstrated paraphrase evasion.
- `preceded_by_ai`: whether an AI turn immediately precedes the learner turn, independent of keyword matching.
- `lexical_overlap_ratio`: descriptive token overlap with preceding AI turn.
- `lexical_echo_flag`: a conservative signal for short/high-overlap turns; suppressed when learner uses more distinct tokens than the AI. **This does not certify productive learning, originality, or absence of copied content.**
- `observed_codes`: pattern hits are suppressed for fewer than three substantive tokens, but longer keyword salads still produce tags; they are never considered verified reasoning.
- `learner_origin`: explicitly `indeterminate`.
- `proficiency_score`: always `null`, including adversarial and positive comparison fixtures.

The synthetic transcript does **not** show that a learner's actual competence is zero. It demonstrates why naive presence-based coding cannot be equated with a competence estimate. An independently reasoned answer can be prompted; unsolicited answers can also be wrong. Arm C intrinsically solicits critical thinking, so penalising prompted behavior automatically would bias between intervention conditions.

## PI PR #12 review disposition (2026-10-09)

- **F12-1 HIGH:** Accepted. Rather than claiming robust prompt classification through ever more regexes, renamed to `known_scaffold_pattern` and added `preceded_by_ai` separately. Tests demonstrate undetected paraphrases still exist; absence of match is not evidence of no scaffolding.
- **F12-2 MEDIUM:** Accepted as a conservative rule: do not flag a longer distinct-token expansion as echo. Lexical echo retains false positives/negatives and is not an authorship detector.
- **F12-3 MEDIUM:** One-word responses no longer trigger candidate codes (minimum 3 substantive tokens). A keyword salad still triggers codes; a synthetic regex cannot establish semantic reasoning, so we deliberately test and document that limitation.
- **F12-4 LOW:** Answer-in-question remains unsupported, documented for future human annotation.
- **B12-1:** No automatic learner authorship or internal cognition detection is justified; blinded human rating also has limitations.
- **B12-3:** Added an arm-C-like test ensuring prompted behavior does not yield a penalty or proficiency score.

**Research integrity:** `proficiency_score` remains `null` on every path. No scoring validity or actual student proficiency is established.

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
