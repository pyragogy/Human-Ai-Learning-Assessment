# ASSUMPTIONS AND GATES — HALA PISA RDI 2026 Submission

## Candidate AI models

All models listed below have public terms compatible with research use and
non-training of submitted data, verified October 2026.

| Model | Provider | Type | Est. per-session cost | Data-training terms |
|-------|----------|------|-----------------------|-------------------|
| Claude 3.5 Sonnet (Oct 2026) | Anthropic | Hosted API | $0.03--0.08 | Contractual prohibition on training from API submissions (confirmed in Anthropic commercial terms) |
| GPT-4o mini (Oct 2026) | OpenAI | Hosted API | $0.01--0.03 | API opt-out available; must verify no training on assessment data |
| DeepSeek-V3-0324 | DeepSeek | Self-hosted (MIT licence) | ~$0.01 (compute only) | Full data control; local deployment |
| Llama 4 70B (quantised) | Meta | Self-hosted (community licence) | ~$0.02 (compute only) | Full data control; local deployment |

**Recommended primary model:** Claude 3.5 Sonnet with contractual non-training
guarantee and established evaluation performance.

**Fallback strategy:** Self-hosted DeepSeek-V3 or Llama 4 on EU-based
infrastructure (Hetzner or equivalent), ensuring data never leaves the
deployment jurisdiction.

**Risk:** Anthropic and OpenAI API terms may change; self-hosted alternatives
require GPU infrastructure (estimated $1.50–3.00/hour for 70B-class models).

### Required pre-deployment tests

- Adversarial prompt-leakage and instruction-override test suite
- Output consistency across repeated inputs
- Latency measurement (target: <3s per turn)
- Failure-mode catalogue (timeout, refusal, off-topic, hallucination)

## Data flow and safeguarding

```
Student browser → Gateway (port 8766) → Worker (Unix socket)
                    ↓
               HMAC-authenticated IPC
                    ↓
          No external network from worker
                    ↓
          Synthetic-only → no real data collected
```

**For any future student-facing pilot:**

1. Formal Data Protection Impact Assessment
2. Pseudonymisation at point of collection (student ID → session hash)
3. Consent workflow (parental/guardian for minors, per GDPR Art. 8 + DPA)
4. Data minimisation: only task responses, timestamps, dialogue traces
5. Retention schedule: raw data deleted after 12 months; anonymised
   aggregate scores retained for reproducibility
6. No collected data available to model provider (contractual +
   architectural enforcement)
7. Assessment items and scoring logic separated from AI tutor context
   (verified by independent audit: 4 audits, 66 tests passing)
8. No formal security certification or penetration testing conducted

## IP and licensing

| Category | Scope | Licence |
|----------|-------|---------|
| Background | Existing methods, task concepts, source code, documentation | Open-source (MIT / Apache 2.0) |
| Foreground | Co-developed specifications, rubrics, protocol designs | To be negotiated; propose bounded research licence to OECD |
| Third-party | Model provider terms, dataset licences, library dependencies | Inventory in submission; no rights conflicts anticipated |

## Delivery milestones

Assuming 0.5 FTE research engineer + 0.25 FTE assessment designer:

| Milestone | Estimated duration | Dependency |
|-----------|-------------------|------------|
| Task specification × 3 | 6–8 weeks | OECD construct guidance |
| Prompt registry + versioning | 2–4 weeks | Model selection confirmed |
| Coding manual + rubric draft | 4–6 weeks | Task specs complete |
| Synthetic trace pipeline | 4–6 weeks | Coding manual draft |
| Deployment design + DPIA | 3–4 weeks | Model and infrastructure selected |
| Technical review gate | — | OECD reviewer + independent expert |
| Psychometric review gate | — | Psychometric collaborator (not secured) |

## Explicit partnership dependencies

- **OECD confirmation**: eligibility of independent researcher, 2026 deadline,
  submission format, IP requirements
- **Educational partner**: school access, ethics approval, pilot recruitment
  (not secured; no commitment)
- **Psychometric collaborator**: scoring validation, equating, DIF analysis
  (not secured; no commitment)
- **GPU infrastructure**: for self-hosted model fallback (not procured;
  estimated €150–300/month)

## Open questions requiring owner decision

1. Authorize eligibility inquiry email to EDU.PisaInnovation@oecd.org?
2. Accept the 2026 date as authoritative and proceed?
3. Preferred submission scope: full proposal vs. exploratory methods
   contribution (Track A in `BOUNDED_OFFER.md`)?
4. Authorize merging of this PR branch to main?
5. Any institutional affiliation to state (none currently)?
6. Budget for GPU infrastructure if self-hosted path is chosen?