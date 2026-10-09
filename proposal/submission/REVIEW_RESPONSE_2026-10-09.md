# Focused final-gap pass — response to reviewers A/B
Date: 2026-10-09. Authoring/verification record, not scientific certification.

## Version and scope
- Issue #14 instructions and named research/call files were read, together with governance and merged PR #12.
- Main baseline: `e1bf115b86dbee290cc610e743f9affdac52d3e9`; local build confirmed three pages.
- Review synthesis: PR #18, `755637a98811c13e5bb3d3b9ce3e3f3a02ad3073`. A/B are AI opinions, not human peer review or OECD scoring.
- During this task the owner supplied a newer two-page PDF. Its text corresponds to the proposal source on PR #19, `25b7f74b968e87456f4ac32a8a160badf2c8cd4a`.
- The final patch is based on that PR #19 source and preserves its style, three work packages, contact `info@pyragogy.org` and two-page format. It changes four submission-package files only. No prototype, original T2 endpoint, workflow, licence or source-call PDF changes.
- This is a stacked follow-up PR targeting the PR #19 branch; it does not merge PR #19 or PR #18. Human review must decide the integration order.

## Real remaining findings on PR #19
| Finding | Evidence at pinned baseline | Minimal repair / possible falsifier |
|---|---|---|
| F1: unaided definition includes an AI | “unaided” defined with generic interaction management | Define unaided with no-AI probes; reviewer can falsify the issue if protocol establishes that generic management is literally non-assistance. Do not assume it here. |
| F2: example's support provenance is incomplete | Quoted AI turn contains no “evening use”, but commentary says it does | Put evening use in the actual quoted AI turn and use a concrete rival explanation. |
| F3: assisted construct conflicts with rejection rule | “those that track prompting are discarded” despite construct-relevant responsiveness | Reject unsupported interpretations rather than every prompted observation; no universal agent-variance cutoff. |
| F4: preregistration timing and nesting | Before data analysis; turns within tasks/sessions omit explicit student clustering | Move to before collection, include student clustering, support-context-aware ratings and precision/uncertainty rationale. |
| F5: added prior art lacks corresponding precise citations | Footnote cites neither PISA 2015 nor dynamic assessment | Add verified OECD 2017 and Poehner/Lantolf 2005 references/DOIs. |
| F6: claimed implementation/capacity exceeds evidence | “Each turn is annotated”; reliability report; unfunded Packages 1–2 | Label manual/schema prospective, make report conditional on approved calibration data and specialist capacity, make workload jointly scoped. |
| F7: supporting assumptions drift | No Mistral row; 0.5/0.25 FTE; fixed durations; 12-month retention; self-hosted training exclusion treated as automatic | Align candidates/three packages; remove unsupported commitments; separate training, retention, pseudonymisation and egress gates. |
| F8: remaining compliance/reproducibility gaps | README unchecked generic crosswalk and incomplete package list | Add exact build/inspection steps and four-section / 70–30 table, with human/admin gates left open. |

Findings are author-observed document inconsistencies, not empirical study outcomes.

## Reviewer-response matrix
Locations refer to the revised two-page PDF unless an auxiliary file is named.

| A / B point | Disposition | Reason and location |
|---|---|---|
| A: distinguish constructs; B: clarify scoring scope | Accepted | p1 “Two candidate constructs”, updated subtitle, no-AI external anchors; original T2 study explicitly separate. |
| A: PISA 2015 / dynamic assessment; B: precise sources | Accepted | p1 opening/footnote; three verified references with title/year/DOI. |
| A: factorial/reliability/variance design; B: operational pilot specification | Accepted prospectively | p1 “Experimental skeleton”: policy × assistance × task/language, student clustering, actual output/version logs, rater calibration, precision and pre-collection decisions. |
| A: agent variance can dominate; B: validity assurance | Qualified, not universally adopted | p1 “Measurement development”: agent effects judged against intended construct. Unsupported unaided inference rejected; replicable assisted response may remain meaningful. A universal variance-ratio cutoff is rejected. |
| A: illustrative reliability cutoffs/sample planning; B: concrete capacity | Numerical commitments deferred | Thresholds, sample and raters co-designed/preregistered before collection; no arbitrary N, alpha, FTE or timeline. Assumptions P1–P3. |
| A: origin/code ambiguity; B: scoring example | Accepted with distinction | p1 “Observation and provenance”/worked task: cognitive origin remains indeterminate; coding sufficiency separate; actual evening-use prompt included; echo is possible uptake, not copying. |
| A: multilingual comparability; B: scale | Accepted as future tests | p1 adapted language versions/differential functioning; p2 cost/concurrency/latency/provider review; no validated international deployment. |
| A/B: bounded OECD collaboration | Accepted with capacity correction | p2 Packages 1–3; partner/ethics/resource dependencies, unpaid cooperation, calibration report contingent on actual data. No recruitment authority assumed. |
| A/B: privacy, model/provider/IP | Accepted prospectively | p2 models/privacy/IP plus assumptions: precise candidates, preview/version risks, separate training/retention controls, no IP grant, youth safeguards and pseudonymised-data caveat. |
| A/B: full cost and readable length | Accepted | p2 cost prose; dated actual tariffs and all-in formula in assumptions; two A4 pages at original 10pt and margins. |
| B: private evidence inaccessible; A: could not inspect repo | Accepted limitation | p2 readiness: controlled repository access on request; reviewer reports are not repository/security certification. |
| A/B: eligibility and date conflict | Deferred external gates | README/assumptions: live listing reconfirmed 2026; no written resolution of supplied 2024 date, no inferred eligibility or filing. |

A/B disagreement is preserved: scaffold dependence is not inherently invalid; `learner_origin` and coding sufficiency are different; arbitrary numerical thresholds are not inherited. Reviewer B's 66/100 is an opinion, not an OECD forecast.

## Local verification
Linux environment; pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian), two pdfLaTeX passes; Poppler rendering/text/font inspection.
- **2 A4 pages**, 595.276 × 841.89 pt, 10pt single-column body; margins preserved from PR #19 (1.7cm sides, 1.4cm top, 1.3cm bottom).
- Log: **no warnings, no overfull/underfull boxes**.
- Both rendered pages inspected; no clipped text, overlap or broken glyphs. Footer/page numbers and footnote inspected.
- Searchable extraction checked for constructs, manual fields, task, three packages and model IDs; fonts embedded. Courier replaces bitmap monospace without changing body size.
- Source SHA256: `dda00269e1ccba8548454e9d0297002f7a20f51b5e02255e9a53ea3662a9db1a`.
- Reviewed PDF SHA256: `571cfc540c1952b5eb73841d596b7c2f856b8c07f5c24a479fa969f12b7edcc0`.
- README contains reproduction commands and call crosswalk. PDF is a local preview, not committed.
- No code changes; prototype tests were not rerun as evidence for a document-only patch. Earlier PR #12 test reports are not represented as fresh tests or validity evidence.
- No workflow files in the inspected baseline tree; no runs returned for main's pinned commit. Account-level workflow settings were not readable through the available connector. No Actions setting was changed, workflow added, job run or retried.
- Changed content checked: no secrets, real student traces, Restricted Use PDF or fictitious results. This is not a forensic secret audit of the whole repository.
- Exact method/product references and indicative tariffs were checked against primary sources, listed in assumptions. No account/API access or contractual entitlement was tested.

## Decision
**Technical rendering gate: PASS. Manuscript: ready for separate reviewer/human adjudication after these focused corrections.**
The author cannot certify scientific validity or its own final output. A reviewer should pin the eventual follow-up PR head, reproduce the README build, challenge F1–F8 and identify a falsifier for any remaining substantive claim.

**External submission: NOT APPROVED / NOT SENT.**
Remaining decisions: independent-person eligibility, conflicting call-year clarification, proposer/capacity/IP posture and final owner-approved outgoing PDF. No email, merge, public release, provider contract, paid service or Actions reactivation occurred. Issue #14 remains open.
