<div align="center">

<img src="assets/hala-hero.svg" alt="HALA — Human–AI Learning Assessment: Measure learning, not just assisted performance" width="100%" />

<br />

[![Research status](https://img.shields.io/badge/research-protocol%20%2B%20prototype-1e3a5f?style=for-the-badge)](research/PROTOCOL.md)
[![Scientific integrity](https://img.shields.io/badge/claims-evidence--first-167d88?style=for-the-badge)](research/ADVERSARIAL_AUDIT.md)
[![Research checks](https://github.com/pyragogy/human-ai-learning-assessment/actions/workflows/research-checks.yml/badge.svg?branch=main)](https://github.com/pyragogy/human-ai-learning-assessment/actions/workflows/research-checks.yml)
[![Stage](https://img.shields.io/badge/validation-not%20yet%20established-986b31?style=for-the-badge)](assessment/MEASUREMENT.md)

**An open-science-oriented research initiative by [Pyragogy](https://pyragogy.org)**

*How do we know what a student has truly learned when artificial intelligence participates in the learning process?*

[**The research question**](#the-question-that-matters) · [**Study design**](#research-design) · [**Measurement**](#what-we-measure) · [**Prototype**](#run-the-reproducible-demonstrator) · [**Research resources**](#research-library) · [**Get involved**](#participation--collaboration)

</div>

---

> [!IMPORTANT]
> **Scientific maturity:** HALA is a research programme **under development**, not a validated educational assessment, proven learning intervention, or deployed PISA assessment. The software currently processes **synthetic data only**. There have been **no learner trials**, no established psychometric validity, and no independent confirmation of educational impact. All claims should be read against these limits.

## The question that matters

Artificial intelligence can help a student produce an excellent answer. But an excellent answer does not necessarily mean that learning occurred.

**HALA — Human–AI Learning Assessment** investigates how to distinguish:

| What we can observe | What we still need to establish |
| :--- | :--- |
| **Assisted performance** — what a learner and AI produce together | **Independent competence** — what the learner can do without the AI |
| **Interaction process** — questions, disagreement, evidence checks and revisions | **Learning mechanisms** — whether those processes contribute to later competence |
| **Immediate improvement** — stronger performance shortly after a session | **Durable learning** — retention and transfer to unfamiliar problems |

**Central hypothesis:** critical, well-structured interaction with AI *may* support deeper and more transferable learning than explanatory assistance alone. HALA is designed to test this claim, **including the possibility that it is false**.

## Our north star

<div align="center">

### Measure the learning that remains when the AI is gone.

**Observe → Operationalise → Compare → Challenge → Replicate**

</div>

No leaderboard disguised as science. No claim that a fluent AI-produced answer demonstrates understanding. No black-box score promoted to psychometric truth.

## Research design

<img src="assets/hala-method.svg" alt="HALA study timeline: independent baseline T0, AI collaborative learning T1, independent post-test T2, transfer T3, delayed retention T4" width="100%" />

We propose a controlled study with **three instructional conditions**:

| Study arm | Instructional experience | Scientific role |
| :--- | :--- | :--- |
| **A — Non-AI comparator** | Standardised learning resources and self-checks | Active comparison condition |
| **B — Explanatory AI tutor** | Supportive explanations and comprehension prompts | Tests assisted instruction |
| **C — Critical AI collaborator** | Hypothesis generation, alternative perspectives, challenges and evidence verification | Tests dialogic, critical collaboration |

All groups require comparable tasks, intended instructional time, assessment conditions and protected independent tests. Randomisation and baseline adjustment are planned for a later adequately designed study.

**T0** independent baseline → **T1** assisted learning → **T2** independent post-test → **T3** novel-problem transfer → **T4** independent delayed retention (7–14 days).

**Primary planned outcome:** baseline-adjusted difference in independently assessed T2 performance between C and B. Transfer, retention and interaction process indicators are secondary/exploratory outcomes. An initial pilot would establish feasibility and measurement properties, **not causal efficacy**.

Read the [full research protocol](research/PROTOCOL.md), [hypotheses and disconfirmation rules](research/HYPOTHESES.md), [statistical analysis plan](research/ESTIMANDS_AND_ANALYSIS.md), and [intervention manual](research/INTERVENTION_MANUAL.md).

## What we measure

| Construct | Core question | Evidence source |
| :--- | :--- | :--- |
| **Conceptual understanding** | Can the learner explain and apply the concept independently? | Blinded rubric-scored tasks |
| **Critical reasoning** | Can the learner recognize poor evidence or mistaken inference? | Justification and error-detection items |
| **Transfer** | Can knowledge be used in a new context? | Independent novel problems |
| **Retention** | Does capability persist after a delay? | Follow-up assessment |
| **Metacognitive calibration** | Does confidence align with demonstrated performance? | Confidence judgments + independent outcomes |
| **Collaborative process** | Does the learner challenge, verify and improve reasoning? | Consented, structured process indicators |

The proposed **Epistemic Quality Index (EQI)** is a theoretical candidate for further operationalisation — **not a validated psychometric instrument**. We will examine item properties, inter-rater agreement, fairness, measurement invariance, construct validity, intervention fidelity and reproducibility before advancing any claims.

Explore the [measurement specification](assessment/MEASUREMENT.md) and [item blueprint](assessment/ITEM_BLUEPRINT.md).

## Run the reproducible demonstrator

The first implementation is an auditable **Python standard-library** data-validation and descriptive-scoring pipeline. It verifies score boundaries, stage independence, consistent assignment, uniqueness and missing follow-up records.

```bash
git clone https://github.com/pyragogy/human-ai-learning-assessment.git
cd human-ai-learning-assessment

# Run the six integrity tests
python -m unittest discover -s prototype/tests -v

# Analyze synthetic example records
python prototype/analyse.py prototype/fixtures/synthetic_scores.csv
```

> [!NOTE]
> This repository is currently **private**. Clone access requires collaborator permission. Example records are fabricated. The script **does not** estimate treatment efficacy, psychometric reliability, or causal effects; AI tutoring, participant onboarding, data protection infrastructure and assessment delivery are not yet implemented.

Continuous checks: [research-checks workflow](.github/workflows/research-checks.yml) · [prototype documentation](prototype/README.md).

## Research maturity — no shortcuts

| Capability | State |
| :--- | :--- |
| Research question and falsifiable hypotheses | **Documented — draft** |
| Arm definitions and study protocol | **Documented — draft** |
| Measurement rubric and item blueprint | **Designed — unvalidated** |
| Synthetic data validation + descriptive pipeline | **Implemented** |
| Automated research-integrity checks | **Implemented** |
| Interactive AI learning environment | **Not implemented** |
| Human-subject ethics authorisation | **Not obtained** |
| Learner pilot and psychometric validation | **Not conducted** |
| Independent replication | **Not conducted** |

See the [adversarial self-audit](research/ADVERSARIAL_AUDIT.md). These are **internal checks**, not a substitute for independent specialist review.

## Research library

| Research artifact | Why it matters |
| :--- | :--- |
| [Research team and review roles](research/RESEARCH_TEAM.md) | Clear accountability and adversarial-review charters; roles **do not imply recruited human reviewers or running autonomous agents** |
| [Protocol](research/PROTOCOL.md) | Study population, comparison conditions, bias controls and outcome definitions |
| [Hypotheses](research/HYPOTHESES.md) | Predictions, limits and falsification criteria |
| [Estimands and analysis](research/ESTIMANDS_AND_ANALYSIS.md) | Primary comparison and statistical decision principles |
| [Intervention manual](research/INTERVENTION_MANUAL.md) | Tutor versus critical-collaborator behaviour |
| [Measurement](assessment/MEASUREMENT.md) | Constructs, scoring and validity requirements |
| [Item blueprint](assessment/ITEM_BLUEPRINT.md) | Example independent assessment tasks |
| [Ethics and data governance](governance/ETHICS.md) | Research oversight, privacy and safeguarding |
| [Adversarial audit](research/ADVERSARIAL_AUDIT.md) | Known threats and blocking issues |
| [Roadmap](ROADMAP.md) | Development stages and evidence gates |
| [OECD call intelligence](proposal/CALL_INTELLIGENCE.md) | Opportunity tracking, not an endorsement or affiliation |
| [Application guide](proposal/APPLICATION_GUIDE.md) | Submission due diligence and open eligibility questions |

## Intellectual foundations

HALA draws research questions from the wider Pyragogy ecosystem. These works provide **conceptual or engineering foundations**, not empirical proof of HALA's outcomes.

- **Fabrizio Terzi (2025)** — [*Cognitive Intraspecific Selection in Education*](https://doi.org/10.5281/zenodo.16962409). Epistemic selection and the evolution of ideas.
- **Fabrizio Terzi (2025)** — [*The Cognitive Rhythm Theory*](https://doi.org/10.5281/zenodo.15480363). Temporal dynamics and human–AI co-creation.
- **UnPeeragogy** — [Research artifact and DOI](https://doi.org/10.5281/zenodo.22309102). Critical collaboration, independent challenge and auditability.
- [Pyragogy](https://pyragogy.org) — the broader human–AI co-learning research initiative.

These sources require separate claim-level review; HALA does not inherit validity from their publication or archival DOI. See the [prior-work provenance register](research/PRIOR_WORK.md).

## Research without a classroom

HALA currently has **no recruited learners, school access or validated human-learning results**. Our near-term deliverable is a rigorous, classroom-independent **assessment method and synthetic technical demonstrator**. The required human studies will need educational and psychometric collaborators, ethical authorisations and recruitment capacity.

- [Classroom-independent research strategy](research/NO_CLASS_RESEARCH_STRATEGY.md)
- [What we can genuinely contribute to a partner](proposal/BOUNDED_OFFER.md)
- [Evidence-backed claim register](research/CLAIM_REGISTER.md)

The technical demonstrator can test system integrity. **It cannot demonstrate that any human has learned.**

## OECD / PISA relevance

An OECD call concerning AI-mediated assessment motivates this work, but **HALA is independent of OECD and PISA**. No institutional partnership, procurement award, endorsement or acceptance is implied. Applicability to international assessment of 15-year-olds would require substantial additional work on curricula, translations, fairness, participant protections and cross-national measurement invariance. Our current feasibility design envisages consenting adults only, contingent on ethical authorisation.

## Participation & collaboration

We welcome rigorous challenges from learning scientists, psychometricians, assessment designers, human–AI interaction researchers, statisticians and privacy specialists.

**Especially useful contributions:** critiques of construct validity, experimental confounds, item calibration, secure assessment isolation, accessibility and replication design.

This project is currently private. Interested collaborators can start at [Pyragogy.org](https://pyragogy.org); repository access is **not** public by default. Project tasks and review checkpoints are tracked in [GitHub Issues](../../issues).

> **Privacy rule:** no identifiable student records, private transcripts, participant identifiers or API credentials in Git. All current examples are synthetic.

---

<div align="center">

**Pyragogy · HALA**

*Human–AI learning deserves evidence, not assumptions.*

[Research](research/PROTOCOL.md) · [Measurement](assessment/MEASUREMENT.md) · [Integrity](research/ADVERSARIAL_AUDIT.md) · [Pyragogy](https://pyragogy.org)

</div>
