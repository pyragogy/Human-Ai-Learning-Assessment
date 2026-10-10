# Public release gate — HALA

**Status (2026-10-10):** Owner requested preparation for public release after repository review. Visibility remains private while licensing, review integration and final disclosure decisions are unresolved. See [dated repository review](REPOSITORY_REVIEW_2026-10-10.md).

## R0 — Source and security
- [ ] Run repository-wide secret scanning and review entire git history, including removed files.
- [ ] Confirm that no participant data, private correspondence, token, provider configuration or API key has ever been committed.
- [ ] Review GitHub Actions permissions and dependency pinning; adopt minimum permissions and update policy.
- [ ] Ensure no privileged deployment/action relies on public issue or pull-request input.
- [ ] Include SECURITY.md with a responsible vulnerability reporting route.

## R1 — Evidence and research integrity
- [ ] Review public scientific claims; label hypotheses and explicitly retain the list of bibliographic leads not yet full-text verified. Do not present open literature audits as validation.
- [ ] Confirm that diagrams and README distinguish planned partnerships from established affiliations.
- [ ] Document all generated/illustrative data and methodology assumptions.
- [ ] Obtain independent methods and psychometric critique or conspicuously disclose it has not occurred.
- [ ] Ensure pilot status, non-validation and lack of real learner data are prominent.

## R2 — Licenses and ownership
- [ ] Decide software license and separate license for text/figures; confirm rights for all contributed assets.
- [ ] Review third-party marks, OECD/PISA mentions, illustrations and any embedded citations for attribution and non-endorsement.
- [ ] Decide whether protocol materials should remain under a research-document license and code under an OSI-approved license.
- [ ] Define contribution and conduct rules appropriate for a public project.

## R3 — Reproducibility
- [ ] Pinned local/VPS checks reviewed at publication commit; deterministic mock and negative tests included. GitHub Actions remain disabled. Record environment restrictions rather than claiming unexecuted tests passed.
- [ ] Verify README instructions on clean Python environment with no credentials or network access.
- [ ] Validate diagrams on GitHub, links, alt text and accessible contrast.
- [ ] Include machine-readable release manifest with version, limitations and SHA-256 artifacts.

## R4 — Operational readiness
- [ ] Confirm the owner intends to publish all currently private issues and their discussion history.
- [ ] Review files, commit history and issues for personal contact details before changing visibility.
- [ ] Decide whether the proposal or communications files should be redacted/kept separate.
- [ ] Document contact, maintenance expectations and scope of external collaboration.

## Release decision
**BLOCK until all mandatory gates pass and the owner explicitly chooses public visibility.** A clean CI result alone is not a privacy, compliance or scientific approval.
