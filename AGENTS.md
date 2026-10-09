# Contributor guidance

This is an evidence-first educational measurement project.

- Keep hypotheses, measurements, implementation details and findings explicitly separate.
- Never fabricate data, psychometric coefficients, approvals, quotes or OECD eligibility.
- Use synthetic fixtures for software tests, not real student transcripts.
- Do not claim EQI is validated unless documented validity evidence exists.
- All interventions and scoring versions must be recorded for reproducibility.
- Prefer pull requests and review before changing methodological commitments.
- Protect private information and never include secrets or participant data in the repository.
- Preserve study arm definitions and outcome precedence unless a protocol change is justified and documented.


## Mandatory collaboration and independent challenge

Read [Human–AI Research Collaboration Protocol](governance/HUMAN_AI_RESEARCH_COLLABORATION.md) before contributing to methodological, intervention or assessment changes.

- An authoring agent **cannot certify its own output**. Review feedback needs a pinned SHA, reproducible evidence, possible falsifier and explicit decision.
- PI's **agent-performed** audits and falsification cycles are documented across issues #5–#11 and [merged PR #12](https://github.com/pyragogy/human-ai-learning-assessment/pull/12). PI reported 66 local unit tests passing at the reviewed SHA. This is **not** independent human academic peer review or psychometric validation.
- Document disagreements and negative findings instead of suppressing them. Human owner adjudicates final decisions.
- Protect private data and preserve public-release approval gates.

## Current operational guardrails (October 2026)

- **GitHub Actions intentionally disabled by the owner** after account billing/spending-limit errors. Never reintroduce workflow YAML, cloud runners, automated paid CI or subscriptions without explicit approval; use `python -m unittest discover -s prototype/tests -v` locally or on the VPS.
- Use `python -m prototype.separated_assessment.launch_local` for the synthetic-only two-process development demo. This uses the current account and **does not satisfy Linux identity isolation**. Keep localhost-only and use SSH tunnel for remote viewing.
- The previous `prototype/webdemo/server.py` on port 8765 is a **legacy single-process fixture**; do not claim it has assessment isolation.
- Preserve the original T2 learning-study estimand in `research/PROTOCOL_V1.md`. The call-specific PISA conversational proficiency question is a separate research extension, not a silent protocol change.
- Keep the repository private and the user-supplied OECD call (marked Restricted Use) out of release assets.
- No real human participants or live LLM integration with host tools before approved safety and scientific gates.
- The OECD submission belongs in versioned `proposal/submission/` sources. **LaTeX is an authoring choice, not an OECD requirement**; the user must approve final filing, IP terms, finances and any external email.
