# PI follow-up audit — reception and decision intake

**Date:** 2026-10-08  
**Status:** Received and triaged; architectural decisions still require explicit acceptance.  
**Reviewer:** PI (AI agent operating from owner-controlled VPS).  
**Source:** [Issue #6 comment](https://github.com/pyragogy/human-ai-learning-assessment/issues/6#issuecomment-6064298243)  
**Audited commit:** `6b402ab` (not necessarily current main).  
**Review evidence status:** reviewer-reported checks; follow-up agent report, not external human scientific peer review.

## Reported verified results
- 41 automated tests passed under PI's environment.
- Session inactivity expiry and explicit `/api/end` deletion behaved as expected.
- Arm C branched across three synthetic input classes with prompt hash in the mock output; arm A/B stayed static.
- No future item text found in the T1 API payloads or static browser bundle PI inspected.
- No live LLM, human participant data, real delayed retention or human-learning outcomes.

## Critical reading of PI's findings

1. **Do not overstate fixes.** The report's statement that *all* prior medium-severity issues are resolved should be narrowed to the operational session fixes; same-process assessment/tutor separation and research validity remain open by design.
2. **Race-condition note requires a realistic threat model.** A legitimate delete request carrying the same unguessable token can invalidate a concurrent submit; that is normal cancellation semantics, not a random token collision. Concurrent submit-vs-delete ordering merits a deterministic test rather than claims of exploitable collision.
3. **AI contamination indicators are not proof of AI use.** Clipboard paste, focus loss, writing time and apparent LLM-likeness are ambiguous and potentially discriminatory. Any instrumentation requires advance disclosure, consent, minimal data capture, fairness analysis, and must not be treated as a decisive cheating detector.
4. **Process isolation needs real permissions.** Merely splitting code into two Python modules or processes does not suffice if the tutor can reach the assessment bank through the same privileges/network.
5. **A branching scripted response is not a Socratic dialogue or an educational effect.** Human-learning claims remain entirely prohibited.

## Architecture decisions proposed for human adjudication

| Decision | Proposed default | Constraint / verification |
|---|---|---|
| IPC | Unix-domain socket or loopback HTTP behind private process isolation for local dev; hardened authenticated service boundaries for deployment | Different process identities, ACLs; tutor has no access to evaluator endpoint, code or item bank |
| Orchestrator audit | Append-only capability issuance events plus signed/verified assessment-stage receipts | Check verifier uses public key inaccessible to tutor/orchestrator; test tampering and replay |
| Browser stage access | Orchestrator-mediated proxy with short-lived one-stage authorization; no future-item prefetch | Backend enforces role, stage and expiry; don't mistake proxy for prevention of learner copying questions |
| External AI contamination | Minimize exposure, counterbalance forms, independent task administration and preregister sensitivity analysis | No automated accusation from focus/paste/AI-detector heuristics; ethics/privacy review for any monitoring |
| Tutor history scope | Only non-test interaction metadata; no T0 scores, sealed items, assessment answers or rubric keys | Validate serialized tutor payloads and test deliberate leakage injection |
| Blinded rating | Withhold arm, model name, tutor transcript and intervention condition from human raters | Audit exports and study rater blinding success empirically |

## Next work sequence
1. Incorporate decisions into RFC-003, showing alternatives and unresolved tradeoffs.
2. Add machine-readable `provider` and `synthetic_only` to adaptive C responses (LOW correction).
3. Write negative multi-session and route-level tests for stage isolation and replay.
4. Prototype a **separate assessment service** with deny-by-default service permissions, then have PI retest it.
5. Only then consider a configured real-model adapter for developer-only use, with zero real participant data.

**Gate:** Synthetic demo PASS (per PI). Research instrument REVISE/BLOCK pending measurement validity, human ethics and secured assessment boundaries. Public release needs separate owner approval and repository history/privacy audit.
