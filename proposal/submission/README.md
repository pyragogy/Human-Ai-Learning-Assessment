# HALA — two-page OECD PISA proposal
Working package and submission archive. **Owner reports submitted on 2026-10-09; awaiting OECD response.**
Authoring issue [#14](https://github.com/pyragogy/human-ai-learning-assessment/issues/14) was closed on 10 October 2026. OECD clarification remains separate.

## Current status — 2026-10-10
The owner confirmed that the OECD PISA proposal was submitted on **2026-10-09**. Awaiting OECD response; no receipt, eligibility confirmation, selection or endorsement is documented here.

The recovered final-named PDF is archived at [hala_pisa_rdi_2026_final_gaps.pdf](hala_pisa_rdi_2026_final_gaps.pdf).
SHA256: `8a027cba8e6abc83356df8205a8063009a4591749bc88302f6138032efa77c08`.
This differs from the authoring preview digest recorded below (`571cfc54…`). The recovered file is not regenerated or altered; byte identity with the actual email attachment has not been independently established. Preserve this distinction until the sent attachment or its digest is checked.

Pre-dispatch statements below describe the 9 October authoring checkpoint and are historical. Sending does not close scientific review, OECD eligibility/call clarification, contractual IP, or pre-pilot safeguards. The repository stays private; public release and a blog post remain undecided. Licensing was approved on 10 October and the submission stack was integrated into main through PRs #19–#21. The restricted OECD source PDF is excluded.

## Technical clarification — 2026-10-10
The archived PDF describes “HMAC-authenticated IPC”. The implementation actually sends a shared secret over a Unix socket and compares it using `hmac.compare_digest`; it does not implement per-message HMAC signatures. This terminology correction does not alter the submitted PDF. Process separation also does not establish OS-user isolation.

## Files
- `hala_pisa_rdi_2026.tex`: current two-page English proposal.
- `ASSUMPTIONS_AND_GATES.md`: dated model/price sources, design, privacy/IP and resource dependencies.
- `REVIEW_RESPONSE_2026-10-09.md`: response to the two AI reviews consolidated in PR #18, quality findings and remaining review gates.
- Archived final-named PDF: `hala_pisa_rdi_2026_final_gaps.pdf`; provenance and digest caveat above. Authoring preview: generated locally, not committed. No restricted OECD source PDF is included.

## Reproduce locally
From the repository root, using pdfLaTeX (TeX Live 2023 was used for this revision):

```bash
mkdir -p tmp/pdfs
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs proposal/submission/hala_pisa_rdi_2026.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs proposal/submission/hala_pisa_rdi_2026.tex
pdfinfo tmp/pdfs/hala_pisa_rdi_2026.pdf
pdftotext -layout tmp/pdfs/hala_pisa_rdi_2026.pdf tmp/pdfs/extracted.txt
pdftoppm -r 150 -png tmp/pdfs/hala_pisa_rdi_2026.pdf tmp/pdfs/review
```

Required common TeX packages: `inputenc`, `fontenc`, `mathpazo`, `courier`, `microtype`, `geometry`, `xcolor`, `hyperref`, `titlesec`. Poppler provides the three inspection commands. Inspect both PNG pages and the log for warnings/overflows. Expected result: **2 A4 pages**, single column, 10pt body, preserved margins (1.7cm sides, 1.4cm top, 1.3cm bottom). References use standard smaller footnote type; body type/margins were not shrunk to make the document fit. Package versions can affect line wrapping; PDF timestamps/IDs need not match byte-for-byte.

GitHub Actions remain disabled; no workflow changes, remote CI or paid model calls are needed.

## Call and evaluation crosswalk
The call asks for approximately two pages; LaTeX and PDF are internal authoring/delivery choices, not verified mandatory formats. Weights describe OECD criteria, not a predicted HALA score.

| Call requirement / criterion | Location in PDF | Supporting evidence or remaining gate |
|---|---|---|
| 1. Solution, task/scoring scope, specific models | p1 solution; p2 IP/model section | Worked synthetic cards/dialogue and manual rubric; Mistral Large 4 / GPT-4o IDs; final selection and pilot validation pending |
| 2. OECD collaboration and inputs | p2 OECD collaboration | Three bounded work packages; no secured cohort, expert team, FTE or financing |
| 3. Background/foreground IP and third-party rights | p2 IP/model section | Historical submission IP position; repository licenses approved 10 October (see ../../LICENSING.md); bespoke OECD terms remain unresolved |
| 4. Privacy, AI security, no student-data training | p2 privacy/model/cost sections | DPIA, youth protections, roles, minimisation, provider controls and deletion are pre-pilot gates |
| 70%: technical quality and PISA relevance | p1 solution; p2 collaboration | Distinct constructs, prior art, factorial skeleton, unaided anchors, rater/variance/language analysis and preregistered rejection rules |
| 70%: digital/data security | p2 privacy/model/cost sections | Synthetic-only readiness honestly stated; no security certification or deployable isolation claimed |
| 30%: scalability feasibility | p2 collaboration and cost sections | Bounded outputs, explicit unpaid/resource dependencies; concurrency/language/latency tests proposed |
| 30%: provider reliance and cost | p2 privacy/model/cost sections | Version freeze, pause/review on withdrawal, renewed comparability on substitution; full cost drivers and dated indicative tariffs in assumptions |

## Source and review trail
Read before interpreting this package:
- `proposal/OFFICIAL_CALL_REQUIREMENTS_AUDIT_2026.md`, `APPLICATION_GUIDE.md`, `BOUNDED_OFFER.md`;
- `proposal/TWO_PAGE_SUBMISSION_DRAFT_2026.md` (historical drafting input; its proposed biweekly cadence is not a commitment of the current submission);
- `research/PISA_RDI_CONVERSATIONAL_ASSESSMENT_EXTENSION.md` and `PROTOCOL_V1.md` (different studies; original T2 endpoint unchanged);
- `research/reviews/PI_ADVERSARIAL_SYNTHETIC_ANNOTATION.md` and merged PR #12 (heuristic synthetic software, no validated score);
- [PR #18](https://github.com/pyragogy/human-ai-learning-assessment/pull/18), review brief pinned to `755637a98811c13e5bb3d3b9ce3e3f3a02ad3073` (two AI opinions, not human peer review);
- `governance/HUMAN_AI_RESEARCH_COLLABORATION.md`: author cannot certify own work.

Main baseline read: `e1bf115b86dbee290cc610e743f9affdac52d3e9` (three pages). The owner then supplied a newer two-page PDF, matched by the source on [PR #19](https://github.com/pyragogy/human-ai-learning-assessment/pull/19), pinned to `25b7f74b968e87456f4ac32a8a160badf2c8cd4a`. This patch builds on PR #19 rather than replacing its completed revision. Older research/planning files are not silently rewritten.

## Current checklist — 2026-10-10
- [x] Owner confirms submission on 9 October 2026 and identifies the final preview as the sent proposal.
- [x] Final PDF archived unchanged with its actual SHA256.
- [x] Authoring issue #14 closed.
- [ ] OECD receipt/eligibility/call-year clarification documented.
- [x] Owner-authorized submission stack integrated into main (PRs #19–#21).
- [x] License decision: AGPL-3.0-only code; CC-BY-SA-4.0 original text/figures.
- [ ] Independent human scientific review.
- [ ] Final visibility change and GitHub release publication.

## Historical authoring checklist — 2026-10-09
These entries preserve the pre-dispatch checkpoint; they do not override the current status above.
- [x] Four required sections and both weighted criterion groups mapped above.
- [x] Concrete synthetic task/manual rubric; no proficiency/authorship claim.
- [x] Candidate models and dated published tariffs checked against primary sources; no service selected.
- [x] No new source PDF, real student data, licence grant, API calls or workflow files in the patch.
- [x] Local two-pass compilation, A4 page count, extracted text and both rendered pages checked.
- [ ] Separate reviewer rechecks the eventual PR head and human owner adjudicates the scientific changes.
- [ ] OECD confirms independent-person eligibility and resolves the supplied 2024/live 2026 date discrepancy.
- [ ] Owner confirms final identity/contact, realistic capacity, IP/legal posture and outgoing PDF.
- [ ] Owner authorises any email or filing; none is sent by this work.

The public OECD listing was rechecked on 2026-10-09: **26 October 2026, 23:59 Europe/Paris**. No written OECD clarification of the contradictory PDF has been obtained. This is a historical call-check record, not a fresh verification of the deadline. Actions remain disabled.
