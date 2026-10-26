<div align="center">

<img src="assets/hala-hero.svg" alt="HALA — Open Science. Human–AI Learning Assessment. What stays when the AI is gone?" width="100%" />

**An open research programme about what AI-assisted interaction reveals—and what learners can independently retain.**

[![Version 1.0.0](https://img.shields.io/badge/1.0.0-submission_edition-31566B?style=flat-square&labelColor=253746)](CHANGELOG.md)
[![Research status](https://img.shields.io/badge/research-pre--pilot-8A673D?style=flat-square&labelColor=253746)](#research-status)
[![Code: AGPL-3.0](https://img.shields.io/badge/code-AGPL--3.0-31566B?style=flat-square&labelColor=253746)](LICENSE)
[![Text: CC BY-SA 4.0](https://img.shields.io/badge/text-CC_BY--SA_4.0-31566B?style=flat-square&labelColor=253746)](LICENSING.md)

**[Read the OECD/PISA proposal](proposal/submission/hala_pisa_rdi_2026_final_gaps.pdf) · [Scientific questions](#two-related-research-questions) · [Study design](#research-design) · [Evidence & limitations](#research-status) · [Explore the research](#research-navigation)**

</div>

## Research at a glance

**HALA — Human–AI Learning Assessment** is an independent, open-science research initiative by **Fabrizio Terzi**, developed within [Pyragogy](https://pyragogy.org) with AI assistance.

Its starting point is a measurement problem: **a stronger answer produced with AI does not, by itself, show what the human learner knows, understands or can do independently.** At the same time, meaningful human–AI collaboration may be a competence worth assessing in its own right.

HALA investigates *which evidence can support which inference*, rather than assuming that fluent AI-mediated output establishes learning or proficiency.

> **Research status — pre-pilot.** HALA has research protocols, proposed measurement instruments, synthetic tasks and a software demonstration. It has **no participant data, validated assessment scores, empirical effectiveness results, secured institutional partner or ethics approval**. This repository documents a research proposal, **not** a PISA-endorsed or operational assessment platform.

## Two related research questions

| Research track | Central question | What could count as evidence? |
| :--- | :--- | :--- |
| **HALA-P01 · Independent learning** | After different kinds of AI assistance, what can learners demonstrate *without AI*? | Independent baseline/post-tests, transfer to unfamiliar tasks and delayed retention |
| **RDI-P01 · AI-mediated assessment** | Under what conditions can student–AI dialogue provide defensible evidence of proficiency? | Behaviorally anchored student-turn annotations, documented AI support, inter-rater agreement, generalisability checks and relations to unaided anchors |

**These are separate research questions with different estimands.** A conversation-derived indicator must not be represented as an independent learning gain, and neither is validated today.

The [OECD/PISA proposal](proposal/submission/hala_pisa_rdi_2026_final_gaps.pdf) foregrounds **RDI-P01**. It proposes a bounded programme to test the validity of proficiency inferences from adaptive AI dialogue, including situations where the AI itself offers evidence, prompts or counterexamples.

## Research design

### Track 1 — What remains after AI assistance?

The original [HALA-P01 protocol](research/PROTOCOL_V1.md) proposes three learning conditions:

| Condition | Proposed experience | Intended contrast |
| :--- | :--- | :--- |
| **A · Without AI** | Learning materials and self-checks | Baseline comparison |
| **B · Explanatory AI tutor** | Explanations and guided support | AI explanation |
| **C · Critical AI collaborator** | Questions, counterexamples and challenges to reasoning | Critical dialogue |

<img src="assets/hala-method.svg" width="100%" alt="Proposed independent baseline, intervention, post-test, transfer and delayed retention study design" />

The proposed **primary contrast** compares C versus B on independently completed post-session performance adjusted for baseline. Transfer and retention **7–14 days later** are additional planned outcomes. The hypothesis that C improves independent learning relative to B is **falsifiable and untested**.

### Track 2 — Can dialogue support valid proficiency inference?

The [RDI-P01 extension](research/PISA_RDI_CONVERSATIONAL_ASSESSMENT_EXTENSION.md) proposes three task families—causal reasoning, source appraisal and evidence-based revision—and examines student behavior under specified AI policies and levels of assistance.

Candidate observable behaviors include **requesting evidence**, **proposing competing explanations**, **designing discriminating tests**, **appraising sources**, **justified revision** and **calibrating uncertainty**. Every observation must retain its AI-support context. Presence of a behavioral code does **not** automatically establish proficiency, cognitive authorship or learning.

The proposal calls for blinded rating where feasible, rater calibration, analysis of student/task/agent/language variation, and comparisons against independent unaided tasks. Constructs, decision rules and feasibility constraints must be agreed **before collecting participant data**.

**[Read the two-page scientific proposal](proposal/submission/hala_pisa_rdi_2026_final_gaps.pdf)** · [Measurement approach](assessment/MEASUREMENT.md) · [Candidate task blueprint](assessment/ITEM_BLUEPRINT.md)

## OECD/PISA submission

The original two-page proposal was **sent on 9 October 2026**, as reported by the proposer, for the *AI-Mediated Assessment Solutions for PISA* call. The [archived submission PDF](proposal/submission/hala_pisa_rdi_2026_final_gaps.pdf) is preserved unchanged; [provenance and checksum notes](proposal/submission/README.md) describe the archival record.

The proposed collaboration comprises three bounded work packages: **construct and estimand agreement**, **tasks/prompts and observation instrument**, and **instrument review with a pilot-readiness gate**. It does not presume access to learners, OECD resources, psychometric experts, funding or a commissioned deployment.

**Submission does not imply OECD selection, institutional affiliation, partnership or scientific endorsement.** No acknowledgement of receipt or selection is recorded in the repository's documented submission status.

## Research status

| Available for examination | Not established |
| :--- | :--- |
| Research questions and versioned draft protocols | Independent scientific validation |
| Synthetic task examples and proposed coding rules | Validated, reliable or fair proficiency scores |
| A local Python demonstration with scripted AI behavior | Real participant study or live AI tutoring deployment |
| Proposed independent tests and delayed follow-up | Empirically established learning, transfer or retention effects |
| Documented ethical, privacy and technical safeguards to develop | Ethics approval, GDPR/DPIA completion or production security certification |
| Open code/documentation and an evidence/claim register | Formal research team or OECD partnership |

The proposed **Epistemic Quality Index (EQI)** remains an *unvalidated research concept*. A synthetic same-session demonstration of a retention step **is not evidence of delayed learning**. Research transparency includes documenting failures, negative results and unresolved measurement questions.

The [research evidence note on Fütterer et al.](research/literature/FUETTERER_META_ANALYSIS_EPISTEMOLOGICAL_AUDIT_2026.md) discusses why assisted task performance and independent learning must not be conflated. It provides context for HALA's research question, **not validation of HALA**.

## Research navigation

| For reviewers | Primary materials |
| :--- | :--- |
| **Proposal & scope** | [OECD/PISA submission PDF](proposal/submission/hala_pisa_rdi_2026_final_gaps.pdf) · [Submission provenance](proposal/submission/README.md) |
| **Scientific protocols** | [HALA-P01](research/PROTOCOL_V1.md) · [RDI-P01 extension](research/PISA_RDI_CONVERSATIONAL_ASSESSMENT_EXTENSION.md) |
| **Hypotheses & analysis** | [Hypotheses](research/HYPOTHESES.md) · [Estimands and analysis plan](research/ESTIMANDS_AND_ANALYSIS.md) |
| **Measurement & example materials** | [Measurement](assessment/MEASUREMENT.md) · [Item blueprint](assessment/ITEM_BLUEPRINT.md) · [Assessment kit v0.1](assessment/kit_v0_1/README.md) |
| **Prior evidence & criticism** | [Research references](references/README.md) · [Comparative review](references/COMPARATIVE_REVIEW_2026-10-10.md) · [Prior work](research/PRIOR_WORK.md) · [Claim register](research/CLAIM_REGISTER.md) · [Adversarial audit](research/ADVERSARIAL_AUDIT.md) |
| **Responsible research** | [Ethics](governance/ETHICS.md) · [Security](SECURITY.md) · [Collaboration provenance](governance/HUMAN_AI_RESEARCH_COLLABORATION.md) |
| **Prototype & next steps** | [Prototype guide](prototype/README.md) · [Integration guide](prototype/separated_assessment/INTEGRATION.md) · [Roadmap](ROADMAP.md) |

### Inspect the synthetic prototype

On Linux/macOS with Python 3.10+, from the repository root:

```bash
python -m prototype.separated_assessment.launch_local
```

Then open **http://127.0.0.1:8766**; stop with **Ctrl+C**. For remote access, see the [SSH tunnel instructions](prototype/separated_assessment/INTEGRATION.md). The demonstration uses synthetic data and a scripted AI stand-in. Its processes are not isolated as separate OS identities and its same-session retention step is not a delayed assessment.

Suggested local software checks:

```bash
python -m unittest discover -s prototype/tests -v
python -m compileall -q prototype
python prototype/analyse.py prototype/fixtures/synthetic_scores.csv
```

These commands are provided for reproducibility; **this README revision does not establish that they were rerun successfully**. GitHub Actions is disabled, and previously blocked Unix-socket tests remain documented in [issue #3](../../issues/3) and the [repository review](governance/REPOSITORY_REVIEW_2026-10-10.md).

## Open science & collaboration

The repository is public to invite methodological challenge, replication-oriented critique and potential collaboration. Particularly useful contributions include **psychometrics, learning sciences, evidence-centred design, multilingual assessment, accessibility, privacy/security and reproducibility**.

HALA is open to co-design and comparison with complementary approaches; this is **not** a promise to combine studies or share background/foreground intellectual property without agreement.

[Read the contribution guide](CONTRIBUTING.md) · [Open issues](../../issues) · [Pyragogy](https://pyragogy.org) · **info@pyragogy.org**

Please do not upload identifiable student records, private correspondence, restricted calls for proposals or credentials.

## Licensing, authorship & citation

HALA was initiated by **Fabrizio Terzi** as an independent Pyragogy project with AI-assisted drafting and software development. AI-generated reviews are **not independent expert peer review**; see the [collaboration record](governance/HUMAN_AI_RESEARCH_COLLABORATION.md).

Original repository **code** is licensed under [AGPL-3.0-only](LICENSE); original **text and figures** under [CC BY-SA 4.0](LICENSING.md). Third-party materials retain their respective rights. The archived October 9 proposal preserves its historical IP wording; current repository licences and any future collaboration terms must be considered separately.

Citation metadata: [CITATION.cff](CITATION.cff). Archived submission: [version 1.0.0](https://github.com/pyragogy/Human-Ai-Learning-Assessment/releases/tag/v1.0.0).

---

<div align="center">

**HALA · Pyragogy**  
*What stays when the AI is gone?*

</div>
