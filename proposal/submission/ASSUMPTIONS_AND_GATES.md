# ASSUMPTIONS AND GATES — HALA PISA RDI 2026 Submission

## Model-selection gate — explicitly deferred until collaboration

**Owner decision, 9 October 2026:** no AI model, provider, hosted service or GPU deployment has been selected. The final model choice is a **prospective, joint research-design decision**, not an implementation commitment hidden in the proposal.

| Candidate for future evaluation | Deployment option | What must be checked before any evaluative pilot |
|---|---|---|
| OpenAI GPT-4o, snapshot `gpt-4o-2024-08-06` | Hosted API | Continued availability of snapshot, provider retention/training terms, region, exact tariffs, language performance and safety |
| Anthropic Claude API model (exact version not yet selected) | Hosted API | Verified model ID and commercial availability, no-training and retention terms, tariff, stability and language performance |
| DeepSeek-V3 family | Self-hosted | Specific weights and licence, GPU requirements, jurisdiction, measured throughput and full total cost |
| Meta Llama 4 Scout | Self-hosted | Exact weights/license, GPU requirements, language/equity tests and full total cost |

**Nothing in this table asserts current contractual rights, confirmed pricing, model availability or suitability.** Vendor selection may change as products evolve.

### Pre-registration model stability

After exploratory benchmarking and **before data collection**, record immutable model identifiers/snapshots where possible, prompt and decoding version, tools/retrieval corpus, service terms, region, retention controls and cost basis. Use the **same locked experimental exposure** within each pre-specified arm/phase. Forced provider updates trigger a documented interruption or new phase and sensitivity review, not a silent swap.

### Cost model (no unsupported prices)

Use measured token volumes and a dated price sheet:

```text
C_session = (N_input * P_input + N_output * P_output) / 1_000_000
            + C_compute + C_storage + C_network + C_oversight
```

`N_input` and `N_output` must include every model call, full prior context, retries, auxiliary checking and tool response tokens. `P_input`/`P_output` are prices per million tokens from the chosen provider and tier, not assumed constants. For self-hosting model the all-in compute/operations cost and utilisation instead of invented per-token economics. Record peak concurrency and geography. **No per-session numerical cost is supportable yet** because task design, model/version, provider and prompts have not been locked.

### Pre-pilot acceptance criteria

- Prompt leakage, instruction override and age-appropriate safety checks;
- Multilingual accessibility, cross-country comparability and low-resource language failure analysis;
- Availability/latency under realistic concurrent load and a documented failure fallback;
- Written exclusion of participant data from model training;
- Verified provider-specific conditions for retention, transfers, logging, subprocessors and deletion;
- Pilot approval from actual educational/psychometric and privacy partners, none secured.

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
| Background | Existing task concepts, source code, documentation | Private repository, **no explicit licence defined**. Any licensing change requires an explicit decision by the project owner, followed by negotiation of scope and terms with the OECD. |
| Foreground | Co-developed specifications, rubrics, protocol designs | To be negotiated; propose bounded research licence to OECD |
| Third-party | Model provider terms, dataset licences, library dependencies | Inventory to be verified and disclosed before signing a collaboration agreement; disclose known third-party dependencies in proposal |

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
- **GPU infrastructure**: only if self-hosting is selected; no budget or supplier assumed
- **Licence decision**: scope and terms are an explicit owner/partner negotiation, not a promised permissive release

## Open questions requiring owner decision

1. Authorize eligibility inquiry email to EDU.PisaInnovation@oecd.org?
2. Accept the 2026 date as authoritative and proceed?
3. Preferred submission scope: full proposal vs. exploratory methods
   contribution (Track A in `BOUNDED_OFFER.md`)?
4. Authorize merging of PR branch to main vs. keep as branch?
5. Any institutional affiliation to state (none currently)?
6. Budget for GPU infrastructure if self-hosted path is chosen?
7. Licence decision for the repository before collaboration?
8. Verify available snapshots, terms, language performance and real costs during post-acceptance model selection.