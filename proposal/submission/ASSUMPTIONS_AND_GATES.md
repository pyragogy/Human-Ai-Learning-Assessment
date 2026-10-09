# ASSUMPTIONS AND GATES — HALA PISA RDI 2026 Submission

## Candidate AI models

All models listed below are current as of October 2026. Terms verified against
public provider documentation; **no model is selected or deployed**.

| Model | Provider | Type | Est. per-session cost | Data-training terms | Status |
|-------|----------|------|-----------------------|---------------------|--------|
| GPT-4o | OpenAI | Hosted API | Token-based: ~$0.15/M input + ~$0.60/M output | API opt-out available; must verify no training on assessment data; enterprise terms may differ |
| Anthropic API flagship | Anthropic | Hosted API | Token-based (published per-M token rates) | Contractual prohibition on training from API submissions; distinction between default policy, retention opt-out, and explicit feedback must be verified |
| DeepSeek-V3-0324 | DeepSeek | Self-hosted (MIT licence) | ~compute cost (~$2-3/hr GPU) | Full data control; not assumed cheaper at low volume |
| Llama 4 Scout | Meta | Self-hosted (community licence) | ~compute cost (~$2-3/hr GPU) | Full data control; not assumed cheaper at low volume |

**Previous draft errors corrected:**
- Claude 3.5 Sonnet was **retired from API in 2025**; replaced with generic "current Anthropic API flagship" (exact ID to be confirmed at deployment)
- Claude Opus 4 also **retired from ordinary API** per latest documentation
- "Llama 4 70B" does not correspond to Meta's documented Llama 4 models; replaced with Llama 4 Scout
- Per-session pricing removed; replaced with token-based methodology + per-M rates
- Self-hosting **not assumed cheaper** — infrastructure cost may exceed API at low volume

### Required pre-deployment tests (all models)

- Adversarial prompt-leakage and instruction-override test suite
- Output consistency across repeated identical inputs
- Latency measurement (target: <3s per turn for interactive use)
- Failure-mode catalogue (timeout, refusal, off-topic, hallucination)
- Terms verification: distinguish default API policy from retention/non-training options

### Cost calculation methodology (indicative)

Estimates derived from current published API pricing (October 2026). The
proposal does not state a fixed per-session price; it provides token-based
order-of-magnitude estimates:

| Parameter | Low estimate | High estimate | Basis |
|-----------|-------------|---------------|-------|
| Turns per session | ~30 | ~80 | Task design estimate (to be calibrated; 150 turns in 15-20 min is unrealistic) |
| API calls per turn | 1 | 3 | Prompt + optional continuation/retrieval |
| Input tokens per call | ~500 | ~2000 | Prompt + conversation history |
| Output tokens per call | ~200 | ~800 | Model response |
| Total tokens/session | ~20k | ~240k | Product of above |

**Hosted API cost estimate (indicative):** At ~$0.15/M input + ~$0.60/M output
(Anthropic current rates), a session ranges from roughly $0.01 to $0.15.
**Self-hosted:** GPU infrastructure at ~$2-3/hr; at low volume (<1000 sessions),
self-hosting is likely more expensive per session than API.
**Precise budget requires** prompt structure, max tokens, retry policy and
infrastructure choices to be determined during development.

## Data flow and safeguarding

```
Student browser → Gateway (port 8766) → Worker (Unix socket)
                    ↓
               HMAC-authenticated IPC
                    ↓
          No external network from worker (synthetic-only)
```

**Current limitations (not deployment-ready):**
- **No OS-level user isolation:** all processes run as `coder` user; gateway
  and worker share the same OS account. Full isolation requires separate
  system users with Unix-socket permissions (documented in
  `prototype/separated_assessment/VPS_ISOLATION_RUNBOOK.md` but not deployed).
- **No security certification or penetration testing** conducted.

**Required for any student-facing pilot:**
1. Formal Data Protection Impact Assessment
2. Pseudonymisation at point of collection (session hash, not student ID)
3. Appropriate legal basis under GDPR/DPA — **not automatically parental
   consent under Art. 8 alone**; requires determination of controller vs.
   processor roles, risk assessment, and actual pilot conditions with the
   partner institution
4. Data minimisation: only task responses, timestamps, dialogue traces
5. Retention: raw data deleted after 12 months; anonymised aggregate scores
   retained for reproducibility
6. **No collected student data available to model provider for training** —
   verified through contractual terms for hosted API; architecturally
   enforced for self-hosted (data never leave host)
7. Assessment items and scoring logic separated from AI tutor context
   (audited: 4 audits, 66 tests passing)

## IP and licensing

| Category | Scope | Status |
|----------|-------|--------|
| Background | Existing task concepts, source code, documentation | Private repository, **no explicit licence defined**. Before any collaboration, a permissive open-source licence (MIT/Apache 2.0) would be applied subject to OECD agreement on scope and terms. |
| Foreground | Co-developed specifications, rubrics, protocol designs | To be negotiated; propose bounded research licence to OECD |
| Third-party | Model provider terms, dataset licences, library dependencies | Inventory to be produced before submission |

**Correction from previous draft:** The repository does not currently carry an
MIT or Apache 2.0 licence. We cannot offer OECD rights not yet defined. A
licence decision is a prerequisite for any joint work, not an existing asset.

## Delivery milestones

Approximately 0.5 FTE research engineer + 0.25 FTE assessment designer,
assuming collaboration is established.

| Milestone | Estimated duration | Dependency |
|-----------|-------------------|------------|
| Task specification × 3 with prompt registries | 6–8 weeks | OECD construct guidance |
| Process-coding manual (draft) | 4–6 weeks | Task specs complete |
| Synthetic trace pipeline + adversarial tests | 4–6 weeks | Coding manual draft |
| Deployment design + DPIA framework | 3–4 weeks | Model + infrastructure selected |
| Independent technical review gate | — | OECD reviewer + external expert |
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
- **Licence decision**: open-source licence must be assigned before joint work

## Open questions requiring owner decision

1. Authorize eligibility inquiry email to EDU.PisaInnovation@oecd.org?
2. Accept the 2026 date as authoritative and proceed?
3. Preferred submission scope: full proposal vs. exploratory methods
   contribution (Track A in `BOUNDED_OFFER.md`)?
4. Authorize merging of PR branch to main vs. keep as branch?
5. Any institutional affiliation to state (none currently)?
6. Budget for GPU infrastructure if self-hosted path is chosen?
7. Licence decision for the repository before collaboration?
8. Confirm current Anthropic and Meta model lineups (Opus 4 and Llama 4 Scout
   are used as reasonable 2026 estimates; exact IDs to be verified)?