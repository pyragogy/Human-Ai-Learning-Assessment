# PI VPS audit — findings intake and independent triage

**Document ID:** HALA-REV-001  
**Date:** 2026-10-08  
**Status:** reviewer report received; technical triage proposed; **human adjudication pending**  
**Source:** [Issue #5 comment #6063811936](https://github.com/pyragogy/human-ai-learning-assessment/issues/5#issuecomment-6063811936)  
**Audited commit:** `0fe031e` (different from latest `main`).  
**Reviewer:** PI, a separately operated AI agent on the project owner's VPS; not a human/academic peer reviewer.

## Evidence received, not independently re-executed in this intake

PI reports Python 3.13.5 / Linux, 34 unit tests passing, compilation succeeding, scripted journey output, local HTTP health check and full A/B/C journeys reaching DONE. Reported reproduction verdict: PASS as a *synthetic-only demonstration*. Scientific-product verdict: REVISE for v0.3; no claim of human learning or efficacy.

The review contains reproducible commands and file-level allegations, but this intake **does not assert that the development assistant independently replayed the VPS experiments**. Independent execution and/or CI on the corrective commit is a later verification gate.

## Findings proposed for owner decision

| ID | Source finding | Triage | Proposed response | Gate |
|---|---|---|---|---|
| HALA-REV-001 | Session-cap lockout at 100, no expiration | Confirmable code-level limitation, MEDIUM local availability risk | Session TTL, bounded eviction or explicit cleanup; separate local threat model and regression tests | Human accepts scope before patch |
| HALA-REV-002 | Restart leaves orphan sessions and answers in RAM | Confirmable code-level limitation, LOW privacy/availability risk | Server-side DELETE/abort session endpoint with protected token and frontend call; TTL fallback | Human accepts scope before patch |
| HALA-REV-003 | Teaching and assessment share server process | Architectural boundary missing, HIGH *for real research*, not a defect against v0.2's declared scope | Separate services with distinct privileges, sealed item bank, unidirectional receipts and threat-model tests | Blocks any human-study claim |
| HALA-REV-004 | Arm C is fixed two-turn script rather than interaction | Confirmed by implementation; HIGH for research representation | Provider-neutral interactive engine, versioned prompts, branching challenge/verification and recorded configuration; scripted offline fallback | Blocks efficacy-demo claims |
| HALA-REV-005 | Tutor exercise overlaps skills probed by T2/T3 | **Risk, not proven item leakage**: content validity requires alignment with taught construct; bias arises from exact item exposure/differential preparation | Matched curricula, safeguarded unseen items, construct blueprint, equivalent treatment dose and expert psychometric review | Requires evidence before classifying as contamination |
| HALA-REV-006 | Client sends current stage | **Correction to review interpretation:** server validates stage against stored state and rejects out-of-order submissions; current trust is not unconditional | Retain state-machine tests; do not classify as an existing bypass without reproduction | No change unless exploit reproduced |
| HALA-REV-007 | Missing Origin/CSRF controls | Context-dependent, LOW in strict loopback-only JSON dev mode; revisit for authentication/exposure | Explicit local-only scope; add Origin/Host validation or CSRF gate before any shared deployment | Blocks public remote deployment |
| HALA-REV-008 | UI accessibility partially assessed | Positive keyboard/ARIA observations; no independent accessibility audit | Keyboard, focus, contrast and assistive-tech test matrix | Before any participant use |

## Reconciliation with the human–AI collaboration protocol

- **Build:** development assistant created v0.2 and disclosed synthetic limitations.
- **Challenge:** PI reported defects, reproduction attempts and a v0.3 proposal in issue #5.
- **Human adjudication:** **PENDING**. Do not silently mark accepted, merged or independently validated.
- **Verify:** **PENDING** for fixes. Proposed verification includes negative unit tests, pinned-commit CI and repeat agent review.

## Proposed next work packages, not yet approved for implementation

1. **V0.2.1 reliability/security:** TTL + explicit session disposal + tests, keeping loopback-only deployment.
2. **V0.3 architecture RFC:** physically separated evaluator and tutor, roles/access matrix and frozen model configuration; *no new real learner data*.
3. **V0.3 intervention prototype:** actual conditional interaction, not scripted two-turn dialogue; scientific contrast and fidelity checks.
4. **V0.3 assessment integrity:** item-pool isolation, pre/post forms, rubric provenance and no unsupported learning-gain visualization.

## Scientific decision

**Accept PI's PASS/REVISE classification as a reviewer conclusion, not as a certification.** The audit demonstrates the value of independent challenge in the engineering workflow through documented findings. It does **not** establish that multi-agent review statistically outperforms other methods, nor that AI collaboration improves human learning.

**Next required action:** project owner prioritises and authorises the corrective work. Link accepted findings to issue(s), commit(s), replay evidence and before/after test status.
