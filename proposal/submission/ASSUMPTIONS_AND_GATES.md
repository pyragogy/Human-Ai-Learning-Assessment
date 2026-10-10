# HALA submission — assumptions and gates

## Current status — 2026-10-10
The owner confirmed that the OECD PISA proposal was submitted on **2026-10-09**. Awaiting OECD response; no receipt, eligibility confirmation, selection or endorsement is documented here.

The recovered final-named PDF is archived at [hala_pisa_rdi_2026_final_gaps.pdf](hala_pisa_rdi_2026_final_gaps.pdf).
SHA256: `8a027cba8e6abc83356df8205a8063009a4591749bc88302f6138032efa77c08`.
This differs from the authoring preview digest recorded below (`571cfc54…`). The recovered file is not regenerated or altered; byte identity with the actual email attachment has not been independently established. Preserve this distinction until the sent attachment or its digest is checked.

Pre-dispatch statements below describe the 9 October authoring checkpoint and are historical. Sending does not close scientific review, OECD eligibility/call clarification, contractual IP, or pre-pilot safeguards. The repository stays private; public release and a blog post remain undecided. No fresh email, merge, licence grant, paid service or Actions change is authorised by this status update.

Date: 2026-10-09. Supporting working document, not an authorised contract or pilot.
The two-page LaTeX source is the current proposal. No model/provider is selected.

## Candidate models and current-source checks
Only two specific candidates are needed to make the proposal concrete; neither is a purchasing commitment. Other models remain eligible after an equivalent evidence review.

| Candidate | Verified public status on 2026-10-09 | Training / retention feasibility | Unresolved acceptance gate |
|---|---|---|---|
| Mistral Large 4, API alias `mistral-large-4`, documentation v26.10 | Public preview announced 2026-10-06. Announcement says weights forthcoming later in October; no currently usable self-hosted package or immutable snapshot is asserted. | API training opt-out and ZDR are separate settings. Documentation permits requesting ZDR for supported stateless paid API calls; approval is discretionary. Feedback/sharing routes need exclusion. | Verify preview-specific rights, approved API endpoint, opt-out, DPA, hosting/transfers, subprocessors and deletion. A mutable alias alone fails a reproducibility gate: obtain an acceptable version guarantee or use another model. |
| OpenAI GPT-4o, `gpt-4o-2024-08-06` | Listed snapshot in current official model documentation; account access not tested. | API data are not used for training by default unless sharing is enabled. Abuse monitoring can retain content; ZDR is an eligibility/configuration gate, not an automatic property of the model. | Recheck availability, account access, regional processing, endpoint retention, training/sharing configuration and contractual protections before pilot. |

EU hosting is a candidate-selection preference, not a GDPR certificate. No provider contract, commercial account upgrade, live API call or paid infrastructure is authorised by this package. Self-hosting remains an option only after an exact weight revision, rights, realistic GPU capacity, operations and egress controls are verified.

### Dated indicative inference tariffs (not session estimates)
USD per million text tokens; read on 2026-10-09, recheck before any budget decision. No workload, free tier, cache hit rate, VAT, region surcharge or discount duration is assumed.

| Candidate | Uncached input | Cached input | Output | Source / caution |
|---|---:|---:|---:|---|
| Mistral Large 4 | $1.36 | $0.14 | $4.18 | Model card's displayed undiscounted prices; page also shows temporary launch prices $0.68 / $0.07 / $2.09. Do not budget recurring delivery from a launch promotion. |
| GPT-4o | $2.50 | $1.25 | $10.00 | Current model card, standard text pricing; exact account, endpoint and snapshot tariff must be reconfirmed. |

These are published indicative tariffs, not fabricated performance measurements or an offer to provide services. No per-session cost is defensible until the task workload is measured.

```text
C_inference = (N_uncached * P_uncached
             + N_cached * P_cached + N_output * P_output) / 1_000_000
C_programme = C_inference + C_hosting + C_storage_network
            + C_rater_adjudication + C_translation_adaptation
            + C_psychometrics + C_security_privacy + C_operations
```

Count full conversation history, retries and auxiliary calls. Cache/reasoning/tool charges and region/tier differences must follow the chosen service's actual billing rules. For self-hosting, replace hosted inference charges with all-in compute and utilisation costs; do not double count the same infrastructure. Compare latency, peak concurrency, failure rates and language coverage using a versioned synthetic workload. Pricing is only one factor: no valid scaling claim follows from cheap tokens.

### Version and provider-dependence gate
Before each evaluative phase, freeze model revision, prompts, decoding, tools/retrieval, annotation manual and analysis plan. Preserve actual outputs, since a version/seed does not ensure deterministic API replay. Export versioned traces and metadata in provider-independent form. Withdrawal/forced updates pause assessment and trigger a new comparability review; never silently mix versions or replace a failed provider mid-assessment.

## Construct, task and annotation gates
The call-specific study asks about proficiency evidence during interaction. Unaided proficiency and AI-supported collaborative proficiency are separate candidate constructs. The original T2 learning estimand in `research/PROTOCOL_V1.md` is unchanged.

Proposed design: agent role × assistance level × task, adapted language versions, unaided anchors with order/reactivity checks, calibrated raters and student-level clustering. Agreement metrics, variance-component models, differential functioning, sample/precision rationale and construct-specific retain/revise/reject thresholds must be justified and preregistered before pilot collection. No universal agent-variance threshold is adopted.

The worked PDF rubric and proposed contextual fields are manual specifications, not claims of implemented scoring:
- `behaviour_code=COMPETING_CAUSE`: plausible rival explanation for the same pattern, without unwarranted certainty;
- `support_context=AI-suggested`: keep actual preceding AI turn and support level;
- `code_status=insufficient_evidence`: short assent supplies too little evidence for that code; it is not an ability zero;
- `learner_origin=indeterminate`: cognitive origin is unknown even when behavioural evidence is sufficient.
Lexical echo is descriptive possible uptake, never proof of copying, originality or absence of support. The existing regex fixture is heuristic and emits no proficiency score.

## Data flow, age-15 safeguarding and security
Current software is synthetic only, with no live LLM integration or participant access. Two-process separation is not deployed OS-identity isolation or security certification. Earlier agent reports of tests are software evidence, not independent security/psychometric approval.

| Stage of proposed pilot flow | Minimum controls before use |
|---|---|
| Partner-held identity/permissions register | Separate identity keys, institution-controlled access, documented lawful basis, ethics determination, age-appropriate assent and guardian permissions where applicable. |
| Browser to approved gateway | Random session identifier (not a claim of anonymisation), encrypted transport, data minimisation, prohibited personal disclosures and safe interaction policy. |
| Gateway to approved model endpoint / self-hosted service | Only approved task context, pseudonymised dialogue and required synthetic materials; no identity keys or withheld unaided items. Review free-text reidentification risk. Contractual training exclusion, sharing/feedback disabled, approved retention and transfers. |
| Protected trace store and human ratings | Encryption, access roles, separate identity linkage, versioned provenance, appropriate rater access, audit logs and incident-response responsibility. |
| Research exports and deletion | Raw traces stay out of Git. Retention schedule and withdrawal/deletion procedures agreed before collection and tested across logs, backups and processors. Release only disclosure-reviewed anonymised aggregates or synthetic fixtures. |

Pseudonymisation is not anonymisation. No invented 12-month retention commitment remains. Complete a DPIA and agree controller/processor roles, applicable GDPR/partner rules, hosting jurisdiction, subprocessors and cross-border safeguards before a student pilot. No training/fine-tuning on collected student data, including through feedback or optional data sharing. Self-hosting alone does not enforce egress or remove administrator/logging risks. Isolate withheld anchor items and scoring service from AI context; test prompt injection, leakage, unsafe content, timeouts and fail-closed behaviour before participants.

## IP and licensing gates
- Background: existing independently developed task concepts, code and documentation. Private repository has no explicit repository licence.
- Foreground: co-developed specifications, rubrics and designs. Ownership, research/evaluation rights, reuse, publication and confidentiality require written agreement before joint work.
- Third-party: inventory libraries, model/API or weight licences, synthetic-card provenance and generated-content rights. Access to an API does not grant unrestricted sublicensing rights.
No current OECD licence, permissive repository licence, institutional affiliation or provider agreement is asserted or granted.

## Three bounded work packages and dependencies
No FTE, fixed schedule, recurring meetings, paid review or service availability is promised. Durations and resource allocation remain joint scoping decisions.

| Work package | HALA proposed output | Required OECD/partner input | Acceptance evidence |
|---|---|---|---|
| P1: construct and estimand agreement | Blueprints, construct map, proposed inference/falsifier rules | Competencies, delivery constraints, psychometric guidance | Agreed constructs, responsibilities and provisional analysis plan |
| P2: tasks, prompts and observation instrument | Three task specs, prompt registry, manual, synthetic/adversarial traces | Curriculum/accessibility, translation and safeguarding requirements | Versioned package with explicit negative cases and reproducible checks |
| P3: instrument review and pilot readiness | Rater-calibration/reliability plan; data-flow/threat model, provider comparison, full-cost worksheet and dependency register | Actual assessment/language specialists, educational partner, ethics, privacy, recruitment and resources | Justified criteria/preregistration before collection, approved safeguards/IP/roles and feasible budget; otherwise no pilot or empirical reliability report |

Cooperation is unpaid. No fieldwork funding, adolescent cohort, reviewer or institution is secured. Synthetic authoring and pilot readiness are different deliverables; failure to secure partners does not become a fictitious deployment commitment.

## External dispatch gates (separate from manuscript quality)
1. OECD clarification of independent natural-person eligibility.
2. Confirm operative call/deadline and acceptable route despite the supplied PDF's 2024 date. The public OECD listing was rechecked on 2026-10-09 and shows 26 October 2026, 23:59 Paris. This does not itself resolve the PDF discrepancy.
3. Owner confirms proposer identity/contact, bounded capacity, legal/IP posture and final outgoing PDF; no extra affiliation is assumed.
4. Any external email, agreement, financing or filing requires the owner's explicit authorisation. This work sends none, merges nothing and leaves issue #14 open.
No fixed provider choice is needed to describe specific candidates; contractual controls and final selection remain pre-pilot gates, not invented current capabilities.

## Public sources checked on 2026-10-09
- OECD listing: https://www.oecd.org/en/about/calls-for-tenders.html
- Mistral announcement: https://mistral.ai/it/news/mistral-large-4/
- Mistral model card / prices: https://docs.mistral.ai/models/mistral-large-4-0
- Mistral training opt-out: https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training
- Mistral ZDR: https://docs.mistral.ai/admin/monitor-comply/zero-data-retention
- OpenAI model / snapshot / prices: https://developers.openai.com/api/docs/models/gpt-4o
- OpenAI data controls: https://developers.openai.com/api/docs/guides/your-data
- OECD (2017), PISA 2015 Assessment and Analytical Framework: https://doi.org/10.1787/9789264281820-en
- OECD controlled-agent explanation: https://www.oecd.org/en/topics/sub-issues/student-problem-solving-skills/pisa-2015-collaborative-problem-solving.html
- OECD (2026), PISA 2025 Assessment and Analytical Framework: https://doi.org/10.1787/86c36975-en
- Poehner & Lantolf (2005), Dynamic assessment in the language classroom: https://doi.org/10.1191/1362168805lr166oa ; institutional record https://pure.psu.edu/en/publications/dynamic-assessment-in-the-language-classroom/
Primary public sources establish product/method facts, not HALA suitability, legal approval or validity. The restricted OECD call is not included.
