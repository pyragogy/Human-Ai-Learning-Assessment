# RFC-003 Addendum A — PI architecture decisions

**Date:** 2026-10-08. **State:** design proposal for synthetic prototypes; no human-subject approval. Source: [PI issue #6](https://github.com/pyragogy/human-ai-learning-assessment/issues/6).

## Six requirements before v0.3 can be a real research environment

1. **IPC:** use a local Unix-domain socket for a separately executed assessment service. In a deployment, assign tutor and evaluator different operating-system accounts, private storage and independent access controls. Merely using separate Python modules is not isolation.
2. **Orchestrator audit:** keep a verifiable issuance journal, externally anchored digests and assessment receipts authenticated by credentials not held by the tutoring process. A bare hash chain cannot prevent wholesale rewriting.
3. **Client boundary:** proxy only the currently permitted assessment item through the orchestrator. Use expiring, single-stage authorizations and prevent future-item prefetching. These controls cannot prevent a student voluntarily copying visible text.
4. **Contamination and fairness:** draft alternate calibrated item forms and sensitivity analysis. Browser focus, paste, speed and AI-likeness indicators are uncertain, privacy-sensitive signals and must not be used as automatic cheating evidence.
5. **Tutor payload:** explicit allowlist: opaque study reference, arm, approved curriculum topic, T1 dialogue turns, tutor policy hash and provider ID. Exclude all assessment answers, scoring keys, item prompts and T0 results. Any adaptive baseline treatment must be preregistered and balanced.
6. **Blinded assessment:** rater packets may hold only masked response reference, item/form code, text, rubric and scoring instructions. Exclude assignment arm, model, tutor transcript and participant identity. Blindness can still fail from writing style and must be investigated.

## Implementation gates

**G1 — contract tests:** construct tutor and rater packets with strict allowlists and reject unexpected fields. Run deliberate test-item and score-injection failures in CI.

**G2 — process isolation:** independently operated assessment process, separate permissions and access-denial tests. This is NOT implemented in the existing webdemo.

**G3 — agent runtime:** only after G2, introduce a provider-neutral model adapter and a multi-turn critical collaborator; record provider/policy provenance and restrict all external tools.

**G4 — research:** separate ethical authorisation, calibrated measurements and appropriate participant protections. Synthetic technical tests never imply human learning.

**Decision status:** these are proposed development requirements derived from the completed PI audit, not external certifications. The repository remains private.
