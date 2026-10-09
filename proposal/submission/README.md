# HALA PISA RDI 2026 — LaTeX Submission Package

## Files

| File | Purpose |
|------|---------|
| `hala_pisa_rdi_2026.tex` | Main submission document (~2 pages, two-column) |
| `ASSUMPTIONS_AND_GATES.md` | Candidate models, costs, data-flow, milestones, dependencies |
| `hala_pisa_rdi_2026.pdf` | Compiled PDF (optional, not committed by default) |

## Build

Requires a standard LaTeX distribution with the following packages (common
in TeX Live):

- `geometry`, `booktabs`, `graphicx`, `xcolor`, `hyperref`, `needspace`,
  `titlesec`, `microtype`, `mathpazo`, `amsmath`, `caption`, `float`

Compile with `pdflatex` (2 passes recommended for cross-references):

```bash
pdflatex hala_pisa_rdi_2026.tex
pdflatex hala_pisa_rdi_2026.tex   # second pass for labels
```

**Note:** GitHub Actions remain disabled; all compilation must be local.

## Source references

The proposal synthesises content from:

- `proposal/TWO_PAGE_SUBMISSION_DRAFT_2026.md` — draft content
- `research/PISA_RDI_CONVERSATIONAL_ASSESSMENT_EXTENSION.md` — conversational
  scoring theory, 6 observational codes
- `research/PROTOCOL_V1.md` — original T2 learning estimand (referenced as
  separate study, not merged)
- `proposal/OFFICIAL_CALL_REQUIREMENTS_AUDIT_2026.md` — OECD call requirements
  crosswalk
- `research/reviews/PI_ADVERSARIAL_SYNTHETIC_ANNOTATION.md` — annotation
  system limits
- PR #12 — synthetic annotation pipeline

Template formatting adapted from `Unpeeragogy-An-Evidence-Grounded-Audit-Protocol-v0.2.tex`.

## Submission checklist

- [ ] Verify all four OECD call sections covered (solution+models, collaboration,
      IP, privacy/security)
- [ ] Confirm 70/30 scoring criteria addressed inline
- [ ] Verify no secrets, proprietary data, or Restricted Use PDF in repo
- [ ] Confirm independent researcher eligibility with OECD
- [ ] Confirm 2026 deadline with OECD (PDF shows 2024, live listing 2026)
- [ ] Owner approval before sending to EDU.PisaInnovation@oecd.org