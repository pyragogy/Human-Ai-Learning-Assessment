# Evidence note — Fütterer et al., epistemological audit of early ChatGPT meta-analyses

**Recorded:** 2026-10-19  
**Status:** External scientific literature, author-supplied preprint PDF examined; **not peer reviewed**, not independent validation of HALA.  
**Scope:** Methodological relevance to HALA-P01; no change to preregistration status, protocol, analysis plan or efficacy claims.

## Source and provenance

Fütterer, T., Peltzer, N., Gerjets, P., Meurers, D., Tate, T., Warschauer, M., Emslander, V., Bardach, L., Hattie, J., Sailer, M., & Kuhn, J. *A Critical Epistemological Audit of Early Evidence Syntheses in Generative AI Educational Research: A Systematic Review and Meta-Analysis*. Preprint (author manuscript, supplied October 2026). **Year/publication venue/DOI of the manuscript not independently verified**; do not present as peer-reviewed.

Source-declared public research materials:
- Preregistration: https://doi.org/10.17605/OSF.IO/RKCE4
- Data, code, coding manual and supplements: https://doi.org/10.5281/zenodo.23296556
- OSF materials: https://osf.io/hqtvw/?view_only=b4d561c23c7444ccb7c99361cfd26887

These links are reported by the manuscript; the supporting materials were **not independently inspected** for this note.

## Research question and methods (manuscript pp. 3, 16–26)

The authors audit five early meta-analyses of ChatGPT's educational effects and reconstruct their underlying primary evidence. They distinguish **observed task performance**, **human–AI hybrid performance when AI is available at assessment**, and **learning** as a relatively durable change in independently available knowledge or competence. They further distinguish constructs (e.g., knowledge, motivation) from assessment methods. Their reconstructed corpus comprises 87 unique primary studies; the main quantitative analysis uses 198 effect sizes from 75 studies after deduplication and outlier exclusions. Meta-analytic models and bias/sensitivity analyses are exploratory.

## Relevant findings (reported results, not independently replicated)

1. **Construct mismatch** (manuscript pp. 32–34, 46–48): Under a strict classification, 55/69 classifiable studies (79.7%) measured only performance, 8/69 (11.6%) only learning, and 6/69 (8.7%) both. Alternative coding definitions retained a performance-only majority (71.0–82.6%). These percentages must **not** be described as fractions of all 87 studies.
2. **Hybrid output ≠ individual competence** (pp. 13–14, 47–48): A high-quality artifact made with ChatGPT may establish what the combined system accomplished, but cannot alone demonstrate that the learner can reproduce or transfer that competence unaided. AI-supported performance remains a legitimate *different* outcome.
3. **Overall effect is not a stable “learning effect”** (pp. 3–4, 38–41, 50–51): Conventional pooled estimate g = 0.83 (95% CI [0.68, 0.97]), but very high heterogeneity (I² = 94.06%) and wide 95% prediction interval [−0.75, 2.41]. Estimates are attenuated under small-study/selection sensitivity methods (PET g = 0.10; Bayesian model-averaged estimate approximately 0.01). These methods have assumptions, and neither null nor positive educational effects are decisively established.
4. **Quality-filtered learning subset is small** (pp. 38–39, 48): Strict learning outcomes yielded 13 effect sizes from 11 primary studies (g = 1.00); requiring at least five of eight prespecified quality criteria left **four** studies (g = 0.45, 95% CI [−0.26, 1.16]), too few for confident generalization.
5. **Dependence and reproducibility** (pp. 27–31, 45–46): 45/87 unique primary studies recurred in two or more meta-analyses. None of the five audited syntheses was preregistered or released its analysis code; the audit reports that one included meta-analysis was later retracted. Five syntheses are not five independent replications.
6. **No demonstrated significant performance–learning effect difference** (pp. 47–48): The authors report g = 0.91 for performance and g = 0.80 for learning, with no statistically significant difference. The key concern is **invalid inference across distinct constructs**, not an empirically established advantage of one outcome category.

## Implications for HALA (interpretations / design checks, **not** results from Fütterer et al.)

| Source concern | Existing HALA proposal | Proposed evidence gate |
| --- | --- | --- |
| Assisted output conflated with learning | A/B/C conditions; independent baseline and post-session test | Preserve whether AI was accessible at each measurement; report assisted production separately from independent competence |
| Weak inference about durability | Planned unfamiliar transfer tasks and delayed retention at 7–14 days | Record fixed time windows and completion status; do not label the synthetic same-session demo as retention |
| Underspecified AI “treatment” | B explanatory tutor vs C critical collaborator | Freeze and log model/prompt, support policy, task, interaction traces, exposure and actual intervention fidelity; verify differences do not simply reflect more time or feedback |
| Construct/method confounding | Measurement blueprint and EQI proposal | Operationalize construct-to-item mapping, independent anchors, parallel form comparability, scorer blinding and inter-rater reliability; retain EQI as unvalidated |
| Small samples/selection/overlap | HALA not yet run with participants | Preregister estimands, exclusions, missing-data and analysis plan before collection; report precision, attrition and distinct primary evidence |
| Hybrid agency may be valuable in itself | Separate study of learner outcomes from conversational signals | Do not describe hybrid performance as inherently inferior; if studied, label it as a separate construct |

**Potential discriminating test:** compare B (explanatory tutor) vs C (critical AI collaborator) on *independent* baseline-adjusted post-test performance as specified in the current protocol, with independent transfer and delayed retention as additional outcomes. This is **a proposed falsifiable comparison**, not evidence of superiority or proof of learning gains.

### Boundaries and unresolved questions

- The audit covers a historically bounded first wave of **ChatGPT** studies, searched in March 2025; it is not an exhaustive review of all contemporary genAI interventions.
- The audit is a **preprint** and its classification decisions include judgment; its authors examine alternate operationalizations.
- A delayed test alone does not establish construct validity. Timing, assessor independence, item equivalence and genuine competence must all be evaluated.
- HALA has **no participants, calibration, validated measurement instrument, or demonstrated treatment effect**. The manuscript strengthens the *problem rationale*, not the scientific validation of HALA.
- Follow-up before any external citation: validate bibliographic record and access source materials; compare construct definitions and outcome coding; check the most recent published version.

**Disposition:** Add as an external evidence-gap and methods reference; do not alter HALA-P01, archived OECD submission, or existing claims of project status.
