# PISA-RDI conversational assessment extension — scientific separation of estimands

**Date:** 2026-10-08
**Status:** Call-specific prospective research design; unvalidated and not preregistered.
**Source:** PI's [independent agent review #11](https://github.com/pyragogy/human-ai-learning-assessment/issues/11) and the four-page OECD AI-Mediated Assessment call, supplied by project owner and marked Restricted Use.

## Non-retroactive protocol policy

**Do not overwrite `research/PROTOCOL_V1.md` or its original T2-based estimand.** The original HALA study asks whether learners independently retain and transfer competence after different types of AI assistance. Its baseline-adjusted T2 C-versus-B contrast is a proposed *learning* efficacy estimand.

The OECD PISA-RDI call asks a distinct measurement-validity question: whether **student–AI conversational interactions** can yield interpretable, comparable proficiency evidence. A separate protocol extension is appropriate. Both studies can share infrastructure and conceptual constructs, but not silently exchange endpoints or claim that the conversation score is the same as independent learning gain.

## Extension RDI-P01 — proposed conversational construct

**Unit of observation:** one task-specific learner–AI exchange and final learner-produced artifact; eventually multiple tasks/persons/models/languages to investigate reliability and generalisability.

**Target construct:** evidence-based reasoning and appropriate epistemic action *under AI-mediated assessment conditions*. Distinguish this observable collaborative competence from unaided knowledge, generic AI fluency and model-generated output quality.

**Candidate primary measurement research question:** Can a blinded, behaviorally anchored rating of student turns and revisions yield a score that is sufficiently stable across raters, tasks, interaction policies and language conditions, with interpretable relations to pre-specified external independent anchors?

**Not a confirmed primary efficacy endpoint.** No scoring algorithm, validated scale, item equivalence, participant sample or psychometric evidence yet exists.

## Prototype task family — PROPOSED, not implemented

1. **Causal claim:** evaluate a proposed cause-and-effect relationship, identify alternatives and suggest discriminating evidence.
2. **Source credibility:** test AI-produced claims against supplied evidence and justify whether to trust or revise them.
3. **Revision and uncertainty:** draft a tentative recommendation, interrogate a counterexample and document evidence-led revision.

Tasks need age-appropriate language and controlled, safe source materials; an expert review must confirm curriculum relevance and construct representation before any adolescent pilot.

## Candidate observational coding manual — draft

| Code | Observable learner behavior | Quality criterion | Contamination/confound |
|---|---|---|---|
| EVIDENCE_REQUEST | Student explicitly requests source, observation or grounds | Relevant to disputed claim and actionable | Can be prompted verbatim by AI |
| COMPETING_CAUSE | Student proposes a plausible rival explanation | Explains same pattern without asserting unsupported certainty | AI may supply competing explanation |
| DISCRIMINATING_TEST | Student designs a comparison to distinguish hypotheses | Test separates alternatives and notes a limitation | May reflect instruction not competence |
| SOURCE_APPRAISAL | Student weighs credibility/relevance of evidence | Identifies specific strengths, weaknesses or missing provenance | Vocabulary/reading burden |
| JUSTIFIED_REVISION | Student revises conclusion in light of evidence | Revision trace links evidence to changed confidence/position | Could be AI-authored revision |
| CALIBRATED_UNCERTAINTY | Student differentiates unknowns from supported conclusions | Confidence proportional to available evidence | Mere hedging or verbose style |

**Separate observation from proficiency:** presence of a code is not automatically a valid score. A student can ask for a source without evaluating it. Rater guidance must separate learner-originated behavior from AI suggestions, account for prompted vs spontaneous actions, and avoid rewarding verbosity.

## Proposed validation programme (all future)

- Co-design explicit task and rubric versions, predeclare score aggregation and failure conditions.
- Blind independent expert coding; evaluate agreement and disagreement mechanisms (ordinal weighted kappa or suitable generalizability designs where justified by sampling design).
- Study facets: learner, task, rater, AI model/prompt, language, exposure duration and generated assistance.
- Use separate unaided anchor tasks to test convergent/discriminant relations and incremental measurement value, **without redefining T2 as the call-specific primary score**.
- Examine differential item functioning / language invariance only with appropriately designed multilingual empirical samples.
- Explicitly test AI contamination: could the model manufacture the target evidence while learner contributes little?
- No computed reliability, construct validity, causal effect or PISA comparability claims until empirical evidence permits them.

## Engineering boundary and current readiness

HALA has a synthetic A/B/C flow, deterministic limited C-branch, a Unix-socket assessor demonstration, application-secret authentication and 58 automated tests reported by PI on the audited commit. No sustained real AI conversation, operational process scoring, blinded expert data, psychometric calibration, adolescent ethics approval or securely deployed distinct OS identities. The user-supplied OECD call requests specific AI models, IP position, collaboration plan, privacy/non-training safeguards and provider-cost feasibility, to be addressed in the application, not declared implemented.

## Programme boundary

Keep `research/PROTOCOL_V1.md` as the original longitudinal **learning** study. Treat this RDI-P01 document as a **separate call-specific assessment measurement extension**. Any future consolidated study must publicly version new hypotheses, measures and estimands *before data collection*, never merge them retroactively.

**Human-scientific signoff:** pending formal approval before conducting research; documentation of research options is not a participant-study authorization.
