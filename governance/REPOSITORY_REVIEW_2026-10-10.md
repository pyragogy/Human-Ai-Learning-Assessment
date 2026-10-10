# HALA pre-publication repository review — 2026-10-10

## Decision
**REVISE before changing visibility.** Repository remains private. This is an authoring-agent review, not independent scientific certification.
Reviewed working head: `5cceae9267153100cc4e49b5b18f640ced8467f1`; main: `e1bf115b86dbee290cc610e743f9affdac52d3e9`.
The owner confirms submission on 9 October 2026. No OECD receipt, eligibility decision or endorsement is evidenced.

## Scope and evidence
- 76 files at working head (75 text/source files plus archived PDF).
- All eight branch tips enumerated. 153 distinct commits and 150 trees reached through commit listings; 165 distinct blobs inventoried. Main history exhausted at page 2 (124 commits). Branch listings use up to 100 ancestors; their shared ancestry was covered by main history.
- 20 issue/PR bodies and available top-level comments read: 57 discussion entries. Inline reviews, attachments, Actions logs/artifacts, releases, external caches and unreachable/deleted refs are **not** exhaustively covered. This is not a forensic guarantee.
- Pattern checks for private keys, GitHub tokens, provider tokens, AWS access IDs and quoted credential assignments found no verified live credential. Eight candidate blob hits were reviewed: shell variable references and explicitly synthetic test credentials.
- Historical workflow existed and was removed; no workflow in current working tree. Account-level Actions settings are not readable through this connector. No Actions configuration changed.
- Two historical/current proposal PDFs identified. Historical PDF at commit `47f3b842322aaca17cd4b938e5cd40eb25b40a77` is HALA's own earlier two-page draft, not the Restricted Use OECD call. It contains the founder's named project email. Owner should explicitly accept visibility of this email and past discussions.
- Archived final PDF: 116918 bytes, two A4 pages, no JavaScript or embedded form according to pdfinfo; both pages rendered and inspected. No clipping/overlap observed. SHA256 `8a027cba8e6abc83356df8205a8063009a4591749bc88302f6138032efa77c08`. Preserve bytes; original preview hash discrepancy remains recorded.
- Current local Markdown file links checked with PDF present. Internal file paths resolve; remote URLs and Markdown heading anchors not exhaustively verified.

## Verification
Commands run from a connector-materialized source snapshot, not a full git clone:
```sh
python -m unittest discover -s prototype/tests -v
python -m compileall -q prototype
python prototype/analyse.py prototype/fixtures/synthetic_scores.csv
```
Unittest: **60 tests run, 3 errors**. Two Unix-socket tests fail on socket creation and gateway integration setUpClass also fails with `PermissionError: [Errno 1] Operation not permitted`. This environment denies AF_UNIX creation. Do not relabel these as passing or remove the tests. Full suite and launcher smoke test require a normal Linux/macOS environment/VPS.
Compileall and synthetic CLI: PASS. CLI labels output descriptive/synthetic, not empirical effects. Prior PI 66/66 remains historical agent-reported evidence at its own pinned SHA.

## Findings and closure
| ID | Severity | Finding / evidence | Disposition / closure |
|---|---|---|---|
| PUB-01 | BLOCK for licensed release | No repository license. Submission describes private unlicensed background. | Owner selects license; confirm ownership and exclusions. Do not retroactively rewrite submitted PDF. |
| PUB-02 | HIGH | Main lacks submitted final version/PDF and review synthesis; #18/#19/#20 remain open. | Integrate reviewed stack deliberately after owner adjudication; verify final main tree. No merge in this audit. |
| PUB-03 | MEDIUM | Submission README says #14 open although it is now closed; unchecked old pre-send checklist remains visible. | Add current checklist and clearly date historical authoring statements. |
| PUB-04 | MEDIUM | Root README status inserted inside hero HTML block; assignment row describes pre-send state. | Move status to ordinary Markdown; update assignment description. |
| PUB-05 | MEDIUM | Public-release gate requires green CI despite owner-disabled Actions. | Use pinned local/VPS checks; keep Actions disabled. |
| PUB-06 | HIGH for pilot, not public synthetic code | Same-user worker/gateway, no deployed OS identity isolation or live model. | Prominent limitations retained. Issue #13 and human-study gates stay open; release code does not authorize deployment. |
| PUB-07 | MEDIUM | Independent academic/psychometric review absent. Regex annotation is lexical, English-specific and bypassable with keyword salads. | Disclose; publish as synthetic heuristic, not validated coding or authorship detector. |
| PUB-08 | MEDIUM | Bibliographic leads and product/cost statements are dated, not all reverified in this audit. | Preserve dated status and explicit unverified literature register; no blanket bibliography certification. |
| PUB-09 | MEDIUM | Publishing visibility exposes old correspondence drafts, project email and discussion history. | Owner reviews disclosure scope; no participant records or Restricted Use call identified in inspected material, with scope limits above. |
| PUB-10 | MEDIUM | Proposed watermark could be mistaken for proof of copied origin or infringement. | Use explicit provenance/citation/hashes; no invisible markers, copyright traps or altered submitted PDF. |

## Scientific review summary
Original T2 learning study and call-specific conversational proficiency extension remain distinct. Assisted response is not automatically contamination: its interpretation depends on the construct. Cognitive origin stays unknown. No calibrated proficiency scores, educational efficacy, recruited institution, ethical approval or OECD partnership is demonstrated.
The synthetic score fixture must never be used as a real gain analysis: task equating and human scoring remain open. No methodological endpoint or scoring implementation changed here.

## Residual release decisions
1. Choose code/document licenses and confirm rightsholder/excluded third-party materials.
2. Owner adjudicates integration of the submission stack and this audit patch.
3. Full socket suite + launcher smoke on supported host, or expressly disclose unverified checks for a source-only release.
4. Confirm publication scope includes past issue/PR discussions and founder project contact.
5. Approve exact publication commit and actual visibility change after the above; no blog publication is part of this patch.

## Provenance
CITATION.cff and governance/PROVENANCE_AND_LICENSING.md provide transparent attribution and license options. A file-hash manifest verifies exact bytes only; edits, excerpts and paraphrases will not retain the hashes. Timestamps, Git history and citation records support provenance but do not alone prove infringement.
