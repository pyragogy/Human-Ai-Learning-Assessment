# HALA-P01 — Research protocol v1.0 (pre-participant; not registered)

**Version/date:** 1.0 / 2026-10-08. **Status:** design draft, internally reviewed for completeness; NOT ethically approved, preregistered, piloted, or externally peer reviewed. **Sponsor/institution:** independent Pyragogy initiative. **PI:** Fabrizio Terzi (proposed; formal roles to confirm). This protocol is not an OECD-sponsored study.

## 1. Rationale and objective
AI-assisted output quality is not evidence of student learning. HALA examines whether dialogic critical interaction with an AI (C) yields **independently demonstrated** learning relative to an explanatory AI tutor (B), and whether process data can help explain variation without being confused for an endpoint.

## 2. Two distinct studies — DO NOT CONFLATE
**P01-F feasibility:** consenting adults (18+), one learning domain, synthetic-first instrumentation then human participants only following appropriate ethics determination. Objective: feasibility, acceptability, adherence, data completeness, item comprehensibility, scorer agreement, safety and implementation fidelity. No confirmatory claims about efficacy. Sample size determined by precision of feasibility metrics and resources, documented *before recruitment*; no arbitrary “powerful” N.

**P01-E efficacy (future, conditional):** individually randomized 3-arm, parallel-group study. Preregister estimands/analysis and power calculation before recruitment; lock all instruments and prompts; use blinded assessors for independently authored responses. A pilot may lead to redesign. P01-E needs its **own dated protocol** and ethical approval; this document does not authorize P01-E.

## 3. Intended learning domain and outcomes
Candidate domain: causal reasoning/evaluation of evidence (see assessment/ITEM_BLUEPRINT.md). This is provisional, not asserted as educationally representative. Draft constructs: conceptual accuracy, evidence evaluation, justified inference. Transfer across contexts and delayed retention are secondary. All forms must be reviewed for curriculum relevance, difficulty and language accessibility.

**Primary intended P01-E contrast:** C vs B, baseline-adjusted independent T2 score. T2 is scored by masked human raters with predefined analytic rubric, not by interaction model. Arm A provides a secondary comparator. T3 transfer and T4 retention secondary; T1 assisted quality and interaction codes exploratory only.

**Hard constraint:** T0/T2 scores are not assumed interval-equivalent or equated. Quantitative gain analyses remain blocked until parallel-form comparability is established. A transformed 0–100 rubric score is not calibration.

## 4. Allocation and isolation
Recruitment and eligibility must be set before allocation; assess baseline T0 **before random assignment**, or conceal assignment rigorously if earlier. For P01-E: centralized computer-generated concealed allocation; stratification factors limited and preregistered; document sequence generation, seed custody and audit trail. Participants and tutors cannot be blinded, but independent human raters can. Measure prior knowledge, AI literacy and familiarity with task as baseline factors. Monitor cross-arm contamination.

Arm A: non-AI self-directed materials and structured exercises.
Arm B: explanatory tutor giving bounded feedback.
Arm C: critical dialogic AI prompting hypotheses, counterarguments and verification.
Equalize intended learning time, curriculum, difficulty and opportunity to practice. Acknowledge unavoidable conversational-dose differences; record turns, time and requests and analyze as process/descriptive data, not selectively adjust primary treatment effect for mediators.

## 5. Participant journey
**Consent / eligibility → T0** protected independent test → allocation → **T1** teaching with matched learning objective → **T2** protected independent post-test → **T3** independent new-domain transfer task → **T4** independent delayed retention 7–14 days later. Log exact delay. T2/T3/T4 items must be withheld from AI prompts, training materials and researchers conducting interventions wherever feasible. Equal testing conditions. No repeated identical prompts without counterbalancing.

## 6. Protocol integrity and learning evidence
Instrument blueprint and scorer anchors finalized before participants. Dual masked scoring on a prespecified portion, with adjudication rules and uncertainty estimates; evaluate rater agreement appropriate to ordinal items (weighted kappa or ICC only if its assumptions fit). Investigate floor/ceiling, item functioning, fairness, differential attrition and subgroup comparability when adequately powered. Do not claim invariance from small pilot samples. Process codes must be independently specified and measured, with no circular definition in terms of post-test outcome.

## 7. Safety, data rights and governance
Adults only for first feasibility. No recruitment, personal data or intervention trial without documented local ethics determination and GDPR lawful-basis review. Consent must cover capture and potential model-provider processing of interactions. Minimize dialogue logging; pseudonymize, encrypt, set retention limits and allow withdrawals per applicable approvals. Keep participant records, transcript content, credentials and reidentification keys **out of Git**. For 15-year-old PISA-like populations, obtain separate school/institutional review, parental/guardian permissions as applicable, age-specific safeguarding, language/accessibility review and additional privacy controls.

## 8. Analysis and dissemination
P01-F: descriptive feasibility proportions with uncertainty, participant flow, missingness by stage/arm, rater agreement, implementation fidelity, deviations and qualitative acceptability. Any between-arm learning figures strictly exploratory.
P01-E (future): pre-specify baseline-adjusted ITT ANCOVA, missing-data sensitivity and multiplicity strategy in a frozen SAP prior to seeing outcomes; avoid per-protocol cherry-picking. Report all prespecified results, nulls, harms, protocol deviations and funding conflicts. Public release only of consented deidentified data if disclosure controls allow; otherwise code, metadata and synthetic fixtures.

## 9. Decision and failure gates
**BLOCK:** ethics absent; assessment items leak to AI; unequal curriculum/time unaddressed; no validated/defensible independent endpoint; scoring cannot be blinded; missingness prevents credible inference; no safe data architecture.
**No effectiveness claim** before a sufficiently powered, preregistered, independently assessed trial with interpretable uncertainty. Rejection of hypothesis C>B is reportable scientific information.

## 10. Reporting and external standards
Adapt SPIRIT 2025 protocol completeness and CONSORT 2025 reporting transparency as appropriate to educational intervention studies (not a claim that this is a clinical trial); AERA/APA/NCME *Standards for Educational and Psychological Testing* for score interpretation, validity, reliability and fairness; WWC education evidence design briefs for attrition, baseline equivalence and confounding; OSF preregistration guidance. Sources and applicability in research/METHOD_STANDARDS.md.

## 11. Mandatory unresolved items before human recruitment
- [ ] Eligible population/site and independently verified access
- [ ] Complete curriculum and culturally appropriate task forms
- [ ] Scorer manual, anchors and training plan
- [ ] Feasibility N rationale, decision thresholds, and participant flow
- [ ] Ethics authorization/determination and lawful data process
- [ ] Version-locked tutor and critical collaborator
- [ ] Event schema, access controls, retention schedule, deletion tests
- [ ] External psychometric and education research review
- [ ] Register protocol *before* outcome data; publish deviations with dates

**Interpretive rule:** A polished protocol is a plan, not evidence.
