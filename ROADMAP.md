# HALA roadmap and operational gates — 9 October 2026

## Current, reproducible software state

- **Synthetic two-process demonstrator:** worker + browser gateway over authenticated Unix socket, loopback-only. Start using `python -m prototype.separated_assessment.launch_local`. Same-UID fixture, **not** secure multi-user field deployment.
- **Three mock conditions:** A non-AI, B scripted explanation, C deterministic branching. No real model or empirical student data.
- **Synthetic adversarial conversation annotator:** merged [PR #12](https://github.com/pyragogy/human-ai-learning-assessment/pull/12); never returns a proficiency grade. PI reported 66/66 tests passing on the PR's reviewed head SHA; the launcher has not yet received its own independently documented live smoke test.
- **CI:** GitHub Actions intentionally disabled. Run unit tests manually on local machine/VPS, without paid GitHub runners.
- **Research:** original learning/retention protocol distinct from [PISA-RDI conversational measurement extension](research/PISA_RDI_CONVERSATIONAL_ASSESSMENT_EXTENSION.md); both unvalidated.

## Priority 0 — OECD response (target 26 October 2026)

The supplied four-page OECD call requests an approximately **two-page proposal**, explaining the solution, **specific proposed AI models**, collaboration commitments and OECD inputs, background/foreground IP and third-party rights, privacy/security including controls preventing data use for model training.

**Document integrity:** the uploaded call PDF says 26 Oct **2024**, while OECD's 2026 listing gives **26 Oct 2026**; seek written confirmation of the authoritative deadline and applicant eligibility. Neither a LaTeX template nor a mandatory file extension is specified in the provided text. Author in LaTeX; submit a reviewed readable PDF by the instructed email route unless OECD clarifies otherwise.

Actions:
1. PI drafts `proposal/submission/hala_pisa_rdi_2026.tex` and `proposal/submission/README.md` in a dedicated branch and submits a PR (no automatic merge).
2. Identify **named candidate models** with version, deployment assumptions, data terms, rough per-session cost/latency and provider-independent fallback; clearly mark unselected options.
3. Add a **bounded task/scoring example**, evaluator challenge, psychometric validation plan, role-specific resource and security boundaries. No invented partner commitments.
4. The human owner approves naming/legal position, no-pay/external funding assumptions, any IP licence grant and whether/when to send. Do not email without explicit approval.

## Priority 1 — Synthetic integration robustness

- PI independently smoke-tests `prototype.separated_assessment.launch_local` on Linux VPS through SSH port forward and confirms shutdown cleanup; code currently newly added and not independently smoke-tested.
- Improve worker session failure handling, health verification, error surfacing and OS access-denial testing under separate service identities **only with operator approval**.
- Track methodological counterexamples and maintain a null automatic proficiency score until empirical evidence exists.

## Priority 2 — Ethics-gated research

- Secure actual educational/psychometric specialists and study partners.
- Validate tasks, scorer agreement, fairness, languages and real learner protections; no minors recruited before proper approvals.
- Only then investigate whether conversational interactions yield comparable proficiency evidence and whether unaided transfer/retention anchors correlate with it.

## Closure policy

An issue may be closed when **its defined audit/engineering handoff** is complete with links to resulting evidence. Scientific, security, partner and eligibility gates remain open until independently satisfied. Closed historical audits are not a claim of completed overall research.
