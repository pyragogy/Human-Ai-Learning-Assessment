# HALA repository maintenance report — 2026-10-09

## Purpose

Consolidate reviewed changes and historical issues without conflating an executable **synthetic local demonstrator** with a secure live student assessment or validated psychometric instrument.

## Repository state after cleanup

- **Open pull requests:** 0. Synthetic annotation PR #12 reviewed by PI (reported 66/66 local tests at reviewed head), squash-merged onto `main` earlier.
- **Historical reviews closed with dispositions:** issues #5, #6, #7, #8, #9, #10 and #11. Some intermediate issues were closed as superseded; closing them does not represent completion of every related security/science gate.
- **Gates retained open:** #1 OECD eligibility/application confirmation; #2 assessment learning measurement validity; #3 synthetic demonstrator/field security umbrella; #4 psychometrics/ethics and collaboration; #13 Linux user isolation, process recovery and newly added launcher smoke verification; #14 PI LaTeX OECD proposal.
- **GitHub Actions:** disabled as explicitly requested by owner. No workflow YAML exists; tests are run on the local/VPS Python runtime.
- **Privacy:** private repository, no real learners, no public ports, no external AI provider.

## Recommended local demo

```bash
python -m prototype.separated_assessment.launch_local
```

Open `http://127.0.0.1:8766` on the same machine, or use SSH forwarding. Launcher creates one temporary Unix socket directory and a fresh development-only shared secret for gateway and assessor, then shuts down both subprocesses on exit. **Same user by design**; OS-level separation, security hardening, consent and production readiness are not established. Live startup/shutdown **still requires PI's VPS smoke confirmation** (issue #13).

## Manual checks (without GitHub Actions)

```bash
python -m unittest discover -s prototype/tests -v
python -m compileall -q prototype
python prototype/analyse.py prototype/fixtures/synthetic_scores.csv
```

The latest previous full suite result available is **66/66 as reported by PI at PR #12 reviewed commit**. Maintenance changes and new launcher have **not yet been independently executed end-to-end**, so this report does not assert a newly passing suite.

## OECD submission: verified requirements and remaining gates

The owner-provided four-page call asks for **approximately two pages** covering (1) proposed AI-mediated assessment solution including *specific AI models*, task/scoring scope, (2) OECD collaboration/inputs, (3) IP and third-party rights, (4) data privacy/security and prevention of participant data being reused to train AI models. Evaluation weighting: **70%** technical/relevance/security, **30%** scaling/provider dependencies/costs. Cooperation is **unpaid**.

The call does **not prescribe LaTeX or an exact file extension**, but provides `EDU.PisaInnovation@oecd.org` as submission destination. Source PDF shows **2024** as closing year while contemporaneous OECD 2026 announcement says **26 October 2026**. Request written clarification and do not silently alter the source.

PI has an authoring assignment in [issue #14](https://github.com/pyragogy/human-ai-learning-assessment/issues/14) to prepare an English LaTeX source, build reproducible approximately two-page PDF, evidence/assumptions list and a PR for owner approval. **No application has been sent, no IP commitment authorized.**

## Scientific distinction

- Original `research/PROTOCOL_V1.md`: longitudinal independent **learning** after AI assistance (prospective T2 endpoint).
- `research/PISA_RDI_CONVERSATIONAL_ASSESSMENT_EXTENSION.md`: whether student–AI **interaction** can produce interpretable evidence of proficiency. The synthetic annotator returns `proficiency_score = null`; none of its codes is validated. No silent protocol substitution.

## Explicitly NOT complete

Real LLM integration, data-protection approvals, real participant studies, adolescent safeguarding, blinded human psychometric studies, cross-language invariance, OS-user separation, signed audit anchoring and OECD acceptance/eligibility verification remain future gates.
