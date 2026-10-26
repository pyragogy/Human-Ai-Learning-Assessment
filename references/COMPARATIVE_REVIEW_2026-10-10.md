# HALA in the literature: evidence, distinctions and a practical research path

**Date:** 10 October 2026  
**Status:** AI-assisted research synthesis; independent scientific review and owner adjudication pending  
**Repository baseline:** `11553d1e3ea2930bbff67c7db33148d825d768d3`  
**Purpose:** position an early personal research project and choose useful next work. This document proposes options; it does not amend the study protocol, adopt an endpoint or authorize participants.

## What this review changes

HALA's broad question already has substantial prior work. Its possible contribution needs to be more specific: an inspectable method for separating the quality of an AI-supported answer, evidence of a learner's reasoning during assistance, and what the learner can demonstrate independently afterwards.

That is a proposed position, not an established novelty claim. The selected studies neither validate HALA nor make it unnecessary. They show why a useful contribution must go beyond a persuasive concept or a functioning chatbot.

The most productive next output is a small assessment package: explicit claims, carefully specified tasks, anchored rubrics, assistance records and reproducible synthetic counterexamples. A qualified external reader should be able to identify what it would measure, where it fails and what evidence would justify the next step.

## Scope and method

A focused search on 10 October 2026 followed the owner-supplied PISA publication and expanded to generative-AI learning trials, unaided assessment, delayed outcomes, critical thinking, evidence-centered design and conversational assessment. Representative queries included “generative AI without guardrails harm learning”, “AI tutoring active learning randomized”, “2026 randomized generative AI self-regulated learning”, “AI tutoring delayed assessment mastery”, and “evidence-centered design assessment”.

Primary publishers, research institutions, author manuscripts and author data/code repositories were prioritized. Secondary summaries were discovery aids only. Ten bibliographic records were selected for direct relevance to HALA's learning study or its separate conversational-measurement extension. A correction to R02 was also checked. The selection deliberately includes positive, null and negative results.

This is **not** an exhaustive or systematic review: no registered search, complete database export, duplicate screening, formal risk-of-bias instrument or meta-analysis. Heterogeneous outcomes and interventions should not be pooled into one “AI effect”. Full supplementary analyses, raw-data reproducibility and publication-bias assessment remain outside this pass. Source access limits are recorded below; a publisher abstract cannot support a detailed methodological audit.

### Access and traceability

| Source | Material actually consulted | Evidence type / constraint |
| :--- | :--- | :--- |
| R01 | OECD publication metadata; relevant chapter, Box I.3.2, Table I.3.2 | Population assessment with questionnaire profiles; the cited figures are attitudes |
| R02 | Publisher main article, design and results, data-availability statement; correction notice | Published field experiment; supplementary allocation details not independently reproduced |
| R03 | Publisher/PMC indexed article sections, abstract, results excerpts and metadata | Published randomized study; full methods and supplements were not consistently retrievable |
| R04 | Publisher full HTML, design, outcomes, attrition, limitations and data availability | Published RCT; no raw-data reproduction |
| R05 | Author manuscript HTML, version 2, including methods and appendices | Preprint version used; not treated here as a verified journal publication |
| R06 | NBER publisher abstract and metadata | Working paper; full PDF retrieval failed, methodological claims limited to abstract |
| R07 | Microsoft Research publication page and abstract | Published survey; full paper not audited |
| R08 | ETS record and publisher abstract | Foundational design report; full PDF retrieval failed |
| R09 | ETS record and publisher abstract | Foundational validity argument; full text not audited |
| R10 | OECD chapters 6 and 10 | Design/framework chapters; not a new LLM efficacy trial |

All links and complete citations are in [the reference index](README.md) and [BibTeX](sources.bib). Section and table locators below make findings challengeable without reproducing third-party text.

## Empirical comparison

| Study | Design and population | What was measured / observed | Boundary relevant to HALA |
| :--- | :--- | :--- | :--- |
| **R01 · OECD PISA** | Large-scale observational assessment; selected student-questionnaire profiles | Scientific/source-checking beliefs and associations with achievement | Not a randomized AI intervention or a behavioral audit of AI fact-checking |
| **R02 · Bastani et al.** | Nearly 1,000 high-school learners in Turkey; classroom-level allocation to no AI, GPT Base or safeguarded GPT Tutor | Assisted practice improved; subsequent unassisted exam performance was lower for GPT Base, while GPT Tutor was statistically indistinguishable from control | Immediate, context-specific outcomes; safeguard package does not isolate HALA's critical collaboration |
| **R03 · Kestin et al.** | Randomized undergraduate physics study, N=194, purpose-built AI tutor versus active classroom learning | Higher post-test performance with the AI tutoring package | Different learning setting and pedagogical package; no durable-retention claim justified by the sections accessed |
| **R04 · Fütterer et al.** | Individual randomization, 371 students in grades 7–9; utility-value prompts, cognitive-strategy prompts or standard ChatGPT | No significant intervention advantage over control on domain knowledge, effort or elaboration-based strategy use | Immediate outcomes; 35% pre/post attrition; null findings do not establish equivalence |
| **R05 · Tutor CoPilot** | Tutor-level randomization; manuscript reports 1,787 identified students and 782 tutors at launch | About 4 percentage points higher exit-ticket mastery with AI-assisted human tutors | AI supports the tutor, not the learner directly; exit-ticket success is not demonstrated delayed retention |
| **R06 · Oreopoulos et al.** | Abstract reports randomized field experiment with >6,000 middle-school students; AI/CAL and mastery conditions | One-week assessment; encouraging gains concentrated on practiced material under mastery, described as marginally significant | Preliminary working paper; broad transfer, uncertainty estimates and full methods not audited |
| **R07 · Lee et al.** | Survey of 319 knowledge workers with 936 examples | Greater confidence in AI associated with lower reported critical-thinking effort | Self-report and association; not causal evidence of skill loss or a student learning test |

**R02 numerical anchor:** publisher Table 1 reports normalized practice differences of +0.137 (GPT Base) and +0.361 (GPT Tutor), and unassisted exam differences of −0.054 and −0.004, respectively. The latter tutor estimate was not significant. These are study-specific estimates, not HALA effect-size assumptions. The August 2025 correction concerns an author's affiliation, not the reported learning results.

**R04 is a particularly useful challenge:** the cognitive-strategy condition included elaboration, self-correction and Socratic questions, yet this did not establish superior knowledge outcomes. Its limitations include substantial attrition and no delayed follow-up. Source locators: Intervention Conditions, Table 1 and Limitations.

**R05 coding anchor:** the manuscript distinguishes strategy detection from outcomes, with classifiers trained on human-checked labels and reported F1 varying by code. Its headline sample figures are rounded; manuscript participant counts vary by assignment and analytic stage. Use the full flow, not “900 tutors” as an analytic denominator.

## What the assessment literature contributes

**R08 · Evidence-centered design.** Mislevy, Almond and Lukas organize assessment around claims about learners, tasks that elicit evidence and models that connect observations to those claims. For HALA, a code such as “requested a source” needs an explicit warrant: why does this observation support the intended interpretation, and what alternative explanation could defeat it? A keyword match alone supplies neither that warrant nor a calibrated scale.

**R09 · Validity of interpretation and use.** Kane's argument-based approach requires justification of the inferences and uses proposed for scores. HALA should distinguish a limited descriptive coding use from high-stakes proficiency assessment. Reliable coding would be one component of the case, not sufficient evidence for broad educational conclusions.

**R10 · OECD complex assessments and intelligent tutors.** Chapter 6 (Piacentini) connects claims, evidence, tasks and measurement models, illustrated through Learning in the Digital World. Chapter 10 (Hu, Shubeck and Sabatini) considers adaptive assessment with intelligent tutors. Learning during assessment and dependence on support are existing measurement problems. Those frameworks are relevant prior art; they do not demonstrate that an unrestricted LLM conversation yields comparable proficiency scores.

## Position HALA around two separate questions

The repository already separates these questions in [P01](../research/PROTOCOL_V1.md) and the [conversational extension](../research/PISA_RDI_CONVERSATIONAL_ASSESSMENT_EXTENSION.md). Keep that separation.

| Question | Intended evidence | Current HALA status | What would challenge the proposal |
| :--- | :--- | :--- | :--- |
| **Learning:** does C outperform explanatory tutor B? | Baseline-adjusted independent T2; separate transfer T3 and retention T4 at 7–14 days | Proposed future comparison; no learners or results | Defensible trial finds no meaningful advantage or harm |
| **Measurement:** what can dialogue reveal under AI assistance? | Anchored human ratings across tasks and assistance policies, linked to external independent anchors | Draft behavioral codes; no calibrated proficiency scale | Ratings mainly track AI help, verbosity or task/model changes |
| **Engineering:** can the instrumentation preserve the intended conditions? | Reproducible synthetic cases, access and event checks | Scripted demonstrator; supported-host verification still pending | Assessment leaks, timestamps or stage controls fail |

P01 proposes individual randomization for a future efficacy study. The earlier conversational claim that HALA necessarily randomizes classes was incorrect. Classroom allocation is a design choice requiring its own justification, sample-size implications and versioned amendment; R02's allocation does not dictate HALA's.

Likewise, EQI is a candidate idea, not the locked dependent variable. P01's independent endpoint needs a defensible rubric and form comparability. Neither scaling a rubric to 0–100 nor finding rater agreement alone establishes comparability, construct validity or fairness.

## Recommended route: produce useful evidence in manageable steps

The following are **recommendations for adjudication**, not newly adopted protocol requirements. No sample size, psychometric cutoff or recruitment authorization is invented.

| Priority | Concrete output | Implicit lead / dependencies | Closure criterion before moving on |
| :--- | :--- | :--- | :--- |
| **1 · Define one claim** | One-page construct map for causal/evidence reasoning; examples of supported and unsupported inferences | Owner with an external assessment reader | Reviewer can identify target competence, intended use and competing explanations; owner records decisions |
| **2 · Build an assessment package** | A small set of matched tasks, analytic scoring anchors and scoring instructions; private future test items kept separate | Domain educator and measurement reviewer, neither secured; depends on 1 | Content and accessibility reviewed; form-comparability plan documented; unresolved issues explicit |
| **3 · Break the rubric synthetically** | Cases where AI supplies all reasoning, learner echoes it, uses fluent but empty language, or makes a justified short revision | Owner/developer using synthetic fixtures; depends on 2 | Each case has expected interpretation and a falsifier; no automatic proficiency or authorship claims |
| **4 · Verify software on a supported host** | Pinned test logs plus launcher and stage-boundary checks | Owner/developer; tracked in issue #3 | Socket and gateway checks reproduced; known security limits retained; same-session T4 labeled as a demo |
| **5 · Seek a narrow external critique** | Review packet with construct map, tasks, rubric, counterexamples and questions | Owner recruits a qualified human reviewer; depends on 1–3 | Dated critique, conflict disclosure and response log; unresolved objections remain open |
| **6 · Adult feasibility pilot** | Approved, preregistered feasibility plan; scorer agreement, missingness, timing, fidelity and delayed follow-up | Owner plus suitable research/ethics partner; depends on measurement, safety and ethics decisions | Predeclared feasibility thresholds met or redesign documented; no efficacy claim from a small pilot |
| **7 · Future efficacy trial** | Separate frozen P01-E protocol, analysis plan and power justification | Research partner and independent assessors; depends on 6 | Enough interpretable data for the prespecified C-versus-B comparison, including nulls and harms |

A good first reviewer request is specific: “Do these tasks and anchors support this interpretation of independent evidence reasoning, and where do they fail?” That is more tractable than asking someone to endorse HALA as a whole.

### An option before recruiting our own participants

R02 links an [author data/code repository](https://github.com/obastani/GenAICanHarmLearning). R04 links [materials/data](https://doi.org/10.17605/OSF.IO/Y6KFS) and its [preregistration](https://doi.org/10.17605/OSF.IO/VBSQ4). These are candidates for a separate reproducibility or secondary-measurement project.

First inspect permissions, documentation, participant protections and available variables. In this pass only R02's repository listing and data dictionary were read; no learner records were downloaded or copied to HALA. Public availability is not a blanket reuse license.

An authorized secondary analysis could test whether a bounded dialogue code adds information beyond task, baseline and assistance condition. Separate people/classes between development and evaluation, account for repeated observations, and avoid selecting the code because it predicts the same held-out outcome used to evaluate it. Correlation would still not show that the code causes learning, establishes learner authorship, or generalizes from mathematics to HALA's proposed reasoning domain.

If reuse is unsuitable, the synthetic assessment package remains a useful standalone contribution. Synthetic evidence can expose logical failures and software defects; it cannot supply learner validity coefficients.

## Decisions worth making next

1. **Focus:** prioritize the independent-learning study or the conversational-measurement extension for the next small deliverable. Preserve both protocols, but avoid trying to solve both at once.
2. **Scope:** select one reasoning domain and intended use. Prefer a defensible limited interpretation over a broad intelligence or learning score.
3. **Resources:** choose synthetic design work plus external critique, or an authorized secondary analysis, before committing to participant recruitment.
4. **Intervention:** specify what B and C actually do, including answer-giving rules, curriculum, time and permitted assistance. “Critical” cannot be just a system-prompt label.
5. **Failure:** predeclare what would make us revise or abandon the rubric or intervention.

My recommendation is to start with the assessment package and seek criticism of it. It would give a potential collaborator something concrete to inspect and could help others even if the efficacy hypothesis fails.

## Open questions and review checklist

- Can human raters distinguish evidence appraisal from polished repetition of AI suggestions?
- Do task forms support baseline adjustment without assuming equating?
- Does a change of model, language or hint policy alter score meaning?
- Is C's extra dialogue educationally useful or simply more time and effort?
- Can follow-up be completed safely and with interpretable missingness?
- Which recommendation here would an external specialist reject, and why?

The proposed positioning would be weakened by closer prior work with the same task/rubric/assistance design; the suggested direction would be weakened if tasks cannot elicit independently interpretable evidence. Those are reasons to revise the project, not hide inconvenient results.

**Independent challenge pending:** this synthesis was authored with AI assistance and has not been certified by its author. Owner adjudication and external human scientific review remain separate. Nothing here changes the archived submission PDF or supplies OECD receipt, endorsement, ethics approval or empirical validation.

