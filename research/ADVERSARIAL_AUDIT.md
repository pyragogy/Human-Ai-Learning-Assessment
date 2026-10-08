# Pre-data adversarial audit v0.2

**Status:** structured self-audit, not an independent third-party review.

| Threat | Consequence | Prevention / evidence |
| --- | --- | --- |
| Scoring assisted T1 as learning | confuses performance with competence | primary outcome independent T2; automated exclusion regression test |
| AI model changes during trial | treatment drift | pin versions, record provider and prompt SHA; fidelity sampling |
| Difficulties differ across tests | invalid gain comparison | parallel forms, calibration and anchors |
| Group C gets more time | dose confound | equal allocated time and contact schedule |
| Raters know group assignment | expectancy bias | masked anonymous answer sheets, dual rating |
| Prompt leakage into assessment | invalid outcomes | assessment isolation, never send T2 items to intervention AI |
| Participants withdraw selectively | attrition bias | ITT, missingness transparency, sensitivity analysis |
| Subgroup unfairness | inequitable inference | accessibility and DIF analyses with adequate samples |
| Process coding tautologically predicts outcome | circular construct | independent human-coded process data, distinct blinded outcomes |
| Small synthetic demonstration mistaken for science | public misrepresentation | explicit provenance and status labels throughout |
| Child data processed prematurely | ethics/legal failure | adults-only feasibility until minor protocol and authorisations |

## Blocking concerns
1. No documented recruitment access or ethics approval.
2. No empirical test calibration or inter-rater reliability.
3. No real-world intervention deployment.
4. No confirmed call-specific eligibility/technical annex.
5. No actual independent specialist review.

**Decision:** PASS only for technical/research scoping; BLOCK any claim of validated learning benefit or ready-to-run minor study.
