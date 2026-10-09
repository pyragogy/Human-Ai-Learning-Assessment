# Decision ledger

| Date | ID | Decision | Basis | Revisit trigger |
|---|---|---|---|---|
| 2026-10-08 | D-001 | Prefer independent learning performance (T2) over AI-assisted output (T1) as target outcome | construct attribution problem | evidence changes |
| 2026-10-08 | D-002 | Specify three instructional arms A/B/C but primary prospective contrast C vs B | isolate critical collaboration beyond generic tutoring | study feasibility |
| 2026-10-08 | D-003 | Separate feasibility (P01-F) from future randomized efficacy (P01-E) | avoid unsupported causal claims | after feasibility |
| 2026-10-08 | D-004 | Treat calibration and scoring validity as blocking dependencies, not optional polish | credible interpretation of longitudinal scores | psychometric review |
| 2026-10-08 | D-005 | No claims of outside review, preregistration or OECD endorsement | evidence-first publication ethics | independent evidence documented |

| 2026-10-08 | D-006 | Adopt documented human–AI build/challenge/human-adjudication/verification workflow with agent self-approval prohibited | [Collaboration protocol](../governance/HUMAN_AI_RESEARCH_COLLABORATION.md); [PI audit issue #5](https://github.com/pyragogy/human-ai-learning-assessment/issues/5) | actual PI evidence or external methodological critique |

## Operational dispositions — 2026-10-09

These are **project-maintenance records**, not protocol amendments or external scientific approvals:

| ID | Action / recorded decision | Evidence and limitations |
|---|---|---|
| O-001 | Owner requested disabling GitHub Actions after account-level billing/spending block; continue testing locally/VPS only | Workflow removed from `main`; 66 passing tests independently reported by PI at reviewed PR #12 head; new launcher not yet VPS-smoke-tested |
| O-002 | Merge PR #12 after PI adversarial findings addressed and local tests reported | [PR #12](https://github.com/pyragogy/human-ai-learning-assessment/pull/12) — syntactic annotation, **no** proficiency score |
| O-003 | Preserve original `PROTOCOL_V1.md` learning outcome and maintain distinct PISA conversational measurement extension | [Extension](PISA_RDI_CONVERSATIONAL_ASSESSMENT_EXTENSION.md) — call-specific construct remains unvalidated |
| O-004 | Close historical review issues #5–#11 with evidence pointers; do **not** close scientific/OS-isolation gates | Open gates #1–#4 and #13; PI LaTeX submission drafting issue #14 |
| O-005 | Build proposed OECD 2026 submission from versioned LaTeX source and provide a two-page PDF for owner approval | Format from the owner-supplied four-page call: *approximately two pages*, no mandatory LaTeX/PDF extension specified. No IP commitment or email authorized. |

Every amendment must identify impacted outcomes and whether data collection had begun. Changes made after reviewing outcomes require explicit exploratory labeling.
