# Historical review dossier
This document records pre-submission AI opinions from 9 October 2026. Owner subsequently confirmed submission that day. It is preserved unchanged below, not current dispatch status or scientific certification.

# HALA — Consolidated independent AI pre-submission reviews

**Date:** 9 October 2026 · **Proposal baseline:** `main`, commit `e1bf115` (PDF: three A4 pages).  
**Purpose:** preserve two separate *AI-generated* independent reviews and convert them into a controlled, evidence-based last editorial/scientific revision before an OECD decision. **These are not human peer reviews, OECD evaluations or independent security/psychometric certification.**

## Source reports and review limitations

**Reviewer A — scientific/psychometric review.** Source supplied by project owner: `Testo incollato(9).txt`, *Independent Senior Review: HALA / OECD PISA RDI*. Verdict **GO WITH REQUIRED MINOR REVISIONS** (self-reported confidence ~70%). Reviewer could inspect extracted PDF text but **not** the private repo, rendered document or full OECD call. It verified only selected public references. It notes missing prior art, confusion between unaided and AI-supported competence, and insufficiently operational rejection criteria.

**Reviewer B — OECD selection, compliance and deployment review.** Source supplied by project owner: `Testo incollato(10).txt`, *Independent OECD submission-gate evaluation*, dated 2026-10-09. Verdict **CONDITIONAL GO**; indicative **66/100** (47/70 technical, 19/30 feasibility). It claims to have examined rendered PDF and public OECD call listings, **but could not inspect the private repository**. Its score is reviewer opinion, **not** an OECD score or a validated prediction. It identifies eligibility and call-year discrepancy as pre-send administrative blockers, the three-page length as a high-priority compliance risk, and limited operational specificity.

**Synthesis decision:** **CONDITIONAL GO, substantive revision required; no submission authorization.** The reports support proceeding with HALA as an early-stage, bounded research collaboration offer, not asserting a validated measure or turnkey PISA deployment.

## Cross-review decision matrix

| Priority | Convergent issue | A | B | Consolidated action / acceptance check |
|---|---|---|---|---|
| **P0 scientific** | Target construct: unaided proficiency vs *AI-supported* proficiency | Explicit critical weakness | Pilot/scoring scope insufficient | State **both constructs as analytically distinct**, to be specified jointly with OECD; scaffold-responsiveness may itself be meaningful. Do not frame every agent effect as contamination or promise cognitive authorship detection. |
| **P0 scientific** | Testable study skeleton and decision rules | Factors, G-study, agreement, rejection structure | Pilot design, rater and scoring plan | Add compact experimental skeleton: agent role × assistance level × task, language comparison, unaided anchors, turn nesting and agent-output versioning. Predeclare criteria classes (inter-rater reliability, agent/task effects, probe relationship, linguistic invariance) **before pilot**; final thresholds and sample sizes co-designed, not invented. |
| **P1 literature** | Positioning versus known methods | PISA 2015 CPS, dynamic assessment, ITS, generalizability | OECD links / precise references | Cite the **closest** relevant PISA 2015 Collaborative Problem Solving controlled-agent precedent and dynamic assessment alongside PISA 2025 Learning in the Digital World and Evidence-Centred Design. Explicitly clarify how open-ended LLM dialogue changes the methodological challenge; do not claim first-ever framework. Check exact source citations. |
| **P1 operational** | A bounded, executable OECD offer | Explicit factor design and psychometric partner gap | Deliverable gates, cadence, pilot readiness and unfunded capacity | Show 3–4 bounded work packages: construct/estimand agreement; synthetic tasks and model/prompt policy freeze; manual/provenance/reliability/adversarial tests; pilot-readiness/IP/privacy feasibility gate. Specify **OECD inputs** and **owner-provided outputs**. Do not promise resources, partners, regular meetings or timelines without owner commitment. |
| **P1 comparability** | Language/measurement equivalence | Language-specific rubrics, DIF-style analyses | Explicit international feasibility | Name translation/adaptation and cross-language item/code functioning as proposed tests; multilingual deployment is not already validated. |
| **P1 data governance** | GDPR and youth safeguarding | Article 8 sentence conflates concepts | DPIA, roles, retention, subprocessors, incident response | Simplify to lawful basis, controller/processor assignment, ethical approval/child safeguards, GDPR privacy-by-design, contractual training exclusion, retention/deletion and transfer controls **before student-facing pilot**. No blanket EU-provider = GDPR assertion. |
| **P1 model/costs** | Model dependence and full cost | Mistral preview, GPT-4o current access uncertainty, redundant formula | Full operational costs and provider withdrawal | Keep Mistral Large 4 and other **candidates only**, with preview restrictions; freeze versions **within evaluative phase**. Replace displayed token equation in submission with concise full-cost components (tokens, human coding, translation, security, operations); separate auditable detailed method in assumptions. No invented price/model contract. |
| **P1 submission** | Page count and reviewer accessibility | Only partial PDF inspection | ~2 pages requested; 3 pages risk; private repo inaccessible | Prepare an editorial **two-page alternative** with readable ≥10pt typography and no loss of target-construct/experiment substance, **plus retain a three-page scientific master** if useful. Owner selects final version after call requirements review. Do not imply the private GitHub link proves implementation; offer evidence pack / controlled read-only access on request. |
| **P0 administrative** | Eligibility and 2024/2026 call conflict | Could not assess call | Two pre-send blockers | Verify operative 2026 call and deadline from authoritative 2026-linked call/document; obtain OECD **written** eligibility clarification for natural-person independent researcher; no sending or signing until resolved. |

## Non-convergent or potentially mistaken suggestions — do NOT adopt blindly

1. **Agent variance is not automatically invalidating.** Reviewer A proposes rejecting an indicator when agent-attributable variance exceeds student variance unless theoretically predicted. That ratio is **not a universal validity criterion**: interpretation depends on the construct and factorial design. Preserve scaffold responsiveness when theoretically meaningful and empirically replicable.
2. **`learner_origin = indeterminate` and `undetermined` are not synonyms.** The former explicitly denotes epistemic uncertainty about cognitive origin; the latter may designate a coding decision where behavioural evidence is insufficient. Give distinct formal definitions rather than a global find-and-replace. Similarly, lexical uptake/novelty cannot determine authorship.
3. **Reliability targets** like Krippendorff α≥.67/.80 are illustrative heuristics, not justified universal admission thresholds. Specify a metric-selection and threshold-preregistration process, conditional on code prevalence, rater design and intended stakes.
4. **Exact sample size, rater count, language pair, throughput and FTE** cannot be fabricated. Offer study-design dimensions and conditions for later power/precision planning with OECD.
5. **Private repository and DOI references.** Reviewer A did not independently verify the internal pipeline; Reviewer B could not review repository evidence. Do not claim either external reviewer has certified our code; expose an optional curated, reproducible synthetic evidence pack under controlled access.
6. **Three pages are not proven disqualifying.** The call requests *approximately* two; report the compliance risk faithfully. A polished two-page executive version is preferable if scientific clarity survives, but never make 9pt/shrunken margins the workaround.
7. **GDPR is not established merely by EU hosting.** Likewise a DPIA-ready design is **not** a completed DPIA, and a synthetic prototype does not need a fictional already-approved student-data DPIA.
8. **Reviewer B's numerical score 66/100 is subjective**, not the committee's likely outcome. No decision to submit follows from that number.

## Required amendments to the proposal (PR-level specification)

**A. Scientific opening / closest precedent.** After the expanded introduction, add a compact acknowledgement of **PISA 2015 Collaborative Problem Solving** (controlled computer agents) and **dynamic assessment** (scaffolded performance as evidence). Keep the clear explanation of why generated, adaptive AI prompts complicate validity, and retain OECD PISA 2025 process evidence as an existing achievement.

**B. Specify what is measured.** Distinguish **unaided proficiency** and **AI-supported problem-solving proficiency** as separate candidate constructs. Explain that HALA evaluates which observations warrant which inference; response to scaffolding is not by default a contaminant. OECD co-design will fix the estimand and scoring interpretation for each study arm before collection.

**C. Compact experimental skeleton.** Propose agent policies/roles and scaffolding doses crossed with tasks, language-specific adaptation, student-level analysis (turns clustered within students), counterbalanced independent probes, rater calibration/blinding where feasible, and model-version logging. Specify statistical families as candidates (reliability, variance components, convergence and differential functioning), not validated deliverables. Add a **preregistered decision rule structure**, not invented numeric thresholds.

**D. Worked example / provenance.** Explicitly flag that student's phrase *at night* follows an AI mention of *evening use*: an uptake signal and potential priming, **not proof of copying or origin**. Distinguish `behaviour_code=COMPETING_CAUSE`, `support_context=AI-suggested`, `learner_origin=indeterminate`; define a separate `code_status=insufficient_evidence` for the short assent if needed. Verify that examples of these schema fields are illustrative, not necessarily already implemented.

**E. Co-design offer and scope.** Turn tasks/manual/trace tests/privacy design into 3–4 measurable gates with OECD inputs and acceptance conditions. State operational limitations honestly. Note no pilot involving minors without real partners, ethics, safeguards and financing; do not add an unfunded or recurring commitment without owner approval.

**F. Editorial/compliance.** Remove duplicate disclosures and repeated provider names; use a brief executive lead with the offer, followed immediately by concrete measurement problem. Keep candidate-model selection open, incl. Mistral as preview only. Move cost formula to supporting assumptions; in proposal describe *full* future cost dimensions (model inference, raters/adjudication, translation, psychometrics, operations, security). Exact OECD references: verify year, author, title, DOI; add closest antecedents rather than padding a bibliography. Correct any PDF text-extraction oddities if visible. Prefer exactly 2 well-laid-out pages; retain 3-page source if compression harms science.

**G. External administrative preflight (separate from manuscript editing).** Check latest official 2026 call, individual eligibility, email/address, permitted length and submission date. Request written clarification from OECD **only after owner authorises the inquiry**. No application send, licences, contracts, or public disclosure in this review PR.

## Proposed acceptance checklist for PI

- [ ] Provide a **change-log tied to both source reviews**, explaining each accepted/rejected suggestion with rationale.
- [ ] Show a precise construct statement (unaided vs AI-supported) and no blanket agent-effect contamination rule.
- [ ] Show an experimental design skeleton and predeclared *classes* of decisions without fabricated validity thresholds.
- [ ] Acknowledge PISA 2015 CPS, dynamic assessment and PISA 2025 LDW with checked precise references.
- [ ] Provide a specific answer to 'what does OECD get during the bounded first collaboration phase?'.
- [ ] Clarify `learner_origin` vs coding sufficiency; protect against lexical-echo false inference.
- [ ] GDPR, model, costs and capacity claims remain source-backed and conditional.
- [ ] Run `pdflatex` locally twice; **GitHub Actions remain disabled**. Review real A4 pages, typography, text extraction and page balance; report exact page counts for both versions if produced.
- [ ] No restricted-use OECD document, student data, fictitious financing or paid service commitment is committed.
- [ ] Separate the **scientific/editing GO** from **owner submission GO**; keep issue #14 open for eligibility/date/dispatch.

## Decision/traceability

**Scientific assessment:** both AI reviewers supported the substantive research concept, conditional on improvements. Reviewer A's verdict was *GO WITH REQUIRED MINOR REVISIONS*; Reviewer B's was *CONDITIONAL GO*. This does **not** equate to external human peer-review acceptance.

**Submission state:** **NOT APPROVED / NOT SENT.** Two external administrative unknowns (independent-person eligibility and contradictory 2024 vs 2026 deadlines) require resolution, and the actual two-page-versus-three-page choice is the owner's call. The research programme is a prospective design; the current synthetic pipeline is not a psychometrically validated system.

**Next step:** PI implements a single coherent editorial/scientific revision in a separate PR, references this synthesis, and reports a proposed final GO/NO-GO with precise remaining gates.