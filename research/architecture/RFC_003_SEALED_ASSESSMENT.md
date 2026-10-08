# RFC-003 — HALA v0.3: independent assessment and interactive tutor

**Version:** 0.1 | **Date:** 2026-10-08 | **Status:** architecture proposal, NOT deployed or approved for participant research  
**Inputs:** [PI audit, issue #5](https://github.com/pyragogy/human-ai-learning-assessment/issues/5); [PI triage](../reviews/PI_VPS_AUDIT_TRIAGE_2026-10-08.md); [HALA P01 protocol](../PROTOCOL_V1.md)  
**Human decision:** direction approved in conversation; implementation and eventual human research have separate gates.

## Non-negotiable purpose

The hypothesis concerns human learners' *independently demonstrated* competence, not the quality of AI-generated answers. The intervention tutor must not be able to retrieve, infer from API access, or alter the assessment items, scores, rubric keys or evaluator decisions.

## Trust boundaries

```text
                  [CLIENT: research journey UI]
                   /                       \
      delegated session capability      assessment capability
                /                             \
    [TUTOR SERVICE / MODEL]           [ASSESSMENT SERVICE]
     Prompt policy, adapter             item bank, test forms
     model logs, process codes          response capture, rater export
                |                             |
         tutor-only store             assessment-only store
                |                             |
       minimal stage receipt <---- [ORCHESTRATOR / ENROLMENT]
             (no item text, answers or scoring keys)
```

**Important:** separate Python files or routes inside a single process are *not* a sealed evaluation boundary. Production requires distinct processes/containers with separately restricted network reachability, role-scoped credentials and stores, preferably isolated infrastructure. An independent service also requires adversarial network testing, not merely a process name.

## Contracts — conceptual, not implemented

| Boundary | Input | Output | Forbidden fields |
|---|---|---|---|
| Orchestrator → Tutor | opaque session ID, A/B/C arm, allowed topic/level, model policy version, non-test learning history | permitted study exercise, stage receipt | test item text, scoring rubrics, candidate correct answers |
| Orchestrator → Assessment | short-lived stage-scoped capability, independent condition, sealed form version | exercise delivery direct to client and opaque completion receipt | tutoring transcript, tutor model context |
| Assessment → Evaluator | pseudonymous response reference, assessment form, masked scoring packet | coded ratings, uncertainty and adjudication trail | arm allocation, tutor identity, AI-generated rationale |
| Evaluator → Analysis | masked scored outcomes with provenance, optional predeclared covariates | research export after appropriate permissions | participant reidentification secrets |

The user interface must not download *future* protected items. If the same client can call both APIs, browser access needs scoped capabilities, strong response caching protections and no prefetch. Do not pretend the learner cannot voluntarily share a test item with an AI; intervention conditions and auditing must address that residual contamination risk.

## Real tutor interactivity

Provider-neutral adapter contract:

```python
class TutorProvider(Protocol):
    def generate(self, *, policy_version: str, messages: list[dict], settings: dict) -> str: ...
```

- **A:** matched materials, with no chat model.
- **B:** explanation and bounded feedback; no intentionally adversarial questioning.
- **C:** ask learner for claim, elicit competing hypothesis, request evidence, challenge counterexample, invite revision and calibrated uncertainty. The next response must depend on learner input; two static turns do not count as interaction.
- Use the same learning domain, estimated time and practice opportunity, and prespecified fidelity coding, so C's extra turns are not automatically confounded with extra instruction.
- Pin model identifier/revision (as available), provider, temperature, prompt hash, date, allowed tool calls, policy template, and failures. Model versions may change outside our control: document rather than claim exact reproducibility.

## Safety-first implementation ladder

**v0.3a (no live API keys):** provider interface + local deterministic **branching** collaborator, event provenance, branch-counterexample tests; all text fictional. Proves interaction plumbing only.

**v0.3b (local dev, opt-in by owner):** live model adapter with credential isolation and explicit "not for personal data" gate, replay traces and prompt provenance. Keep assessment entirely disconnected from tutor model.

**v0.3c (field-ready architecture, not field authorization):** isolated assessment container/service, signed receipts, dedicated IAM/rate limits, immutable event store, informed-consent workflow, data retention, deletion, comprehensive threat tests. Requires independent security/ethics review.

**Human-subject studies:** separate research ethics determination and data processing authorization, calibrated items, sufficient sample size, independent raters and pre-registration before confirmatory claims.

## Required failure injection and acceptance tests

1. A tutor credential attempting to call assessment API is denied, and failure logged.
2. A tutor process cannot import or access assessment bank at filesystem/network level.
3. A test stage cannot be skipped or replayed; expired stage capabilities fail closed.
4. AI changes model/prompt mid-session → provenance change flagged, not silently accepted.
5. Assessment exports exclude arm and tutor details for scorers.
6. Transcript contains an item → explicit contamination incident, affected outcomes reviewed.
7. Participant-data mode unavailable unless ethics, consent, lawful basis, and appropriate safeguards are actually configured and independently verified.
8. No technical passing test is reported as evidence for learning improvement.

## Research design concern raised by PI

Alignment between taught *construct* and measured construct is necessary for learning tests. Unfair leakage consists of disclosing specific test forms/answers or tailoring only one condition to those items, not teaching students to evaluate confounding per se. Build parallel independent forms and blinded review.

## Non-goals for v0.3a

No grade/score claims; no psychometric measurement, PISA compatibility, learner trials, model superiority claims, secure remote hosting or authorization to turn the repository public.

## Adjudication and sign-off

- Human owner: prioritization and release decision.
- Development assistant: changes + tests, cannot self-certify.
- PI: review at pinned commit, propose falsifiers and negative tests.
- External experts: not yet recruited; no simulated sign-off.

**Proposed next implementation:** v0.3a local, deterministic *adaptive* text engine (no real LLM) and provenance-aware interaction tests, developed as an independent module; field-grade separation remains a later gate.
