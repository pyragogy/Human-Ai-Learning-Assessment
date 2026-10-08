# HALA Human–AI Research Collaboration Protocol

**Document ID:** HALA-GOV-001  
**Version:** 1.0 · 2026-10-08  
**Status:** Adopted as an internal working protocol; effectiveness untested  
**Research lineage:** Pyragogy × UnPeeragogy — critical collaboration, independence gates and auditable decisions  
**First documented application:** [Issue #5 — PI independent VPS audit](https://github.com/pyragogy/human-ai-learning-assessment/issues/5)

> **Our governing rule: No agent approves its own work. Every substantive claim must be challengeable, traceable, and falsifiable.**

## 1. Why we are documenting this

HALA studies whether collaboration with AI can improve *independently demonstrable* human learning. Our development process should therefore itself embody critical human–AI collaboration, with explicit challenges rather than mutual affirmation.

**Observation (8 October 2026):** the project owner reports that a separate agent called **PI**, operating with a clone of HALA on the owner's VPS, read issue #5 and began working on its audit. The research/development assistant drafted the audit assignment and repository changes. This is a **reported operational event**, *not* an independently verified review finding, a completed audit or experimental evidence about multi-agent learning.

**Research opportunity:** record the workflow as an inspectable *development-process case study*, without conflating it with HALA's human-learning outcomes or suggesting that two LLM agents constitute independent human peer review.

## 2. Human authority and delegated roles

| Role | Current function | Authority / constraint |
|---|---|---|
| **Human project owner / research director** | Defines goals, accepts risks, adjudicates trade-offs, authorises release, handles external partnerships | Final decisions and accountability remain human |
| **Development/research AI assistant** | Drafts methodology, implements prototype, maintains decision/evidence logs, proposes fixes | Must disclose uncertainty, evidence and tool limitations; cannot self-certify its work |
| **PI — separate reviewer agent on VPS** | Attempts to reproduce, critique and break the demonstrator; files evidence-backed findings | May report PASS/REVISE/BLOCK opinions with reproduction steps; **not** human independent academic peer review |
| **External human specialists (not yet secured)** | Future psychometric, educational, ethics and causal-methodology challenges | No endorsement, approval or recruited reviewer may be implied |

The role of *reviewer* concerns the job performed; it does **not** certify independence from common models, prompts, training data, project incentives or human direction.

## 3. Review cycle: build → challenge → adjudicate → verify

1. **Build / propose.** Development assistant defines a bounded change, assumptions, affected files, version and acceptance criteria.
2. **Challenge independently.** PI reproduces at a pinned commit on VPS, tests negative cases, identifies false positives, scientific blind spots, UX failures and security issues. PI works without modifying `main` during the initial audit.
3. **Evidence packet.** Every finding names tested SHA, environment, exact repro command/input, expected and actual behaviour, risk, severity, and confidence. Screen captures must exclude secrets and personal information.
4. **Human adjudication.** Owner accepts, revises, defers or rejects each finding, with rationale. Technical agents may recommend but not assign themselves final scientific validity.
5. **Repair in an isolated branch.** Each accepted issue receives a minimal patch and a negative regression test. Cross-cutting scientific choices additionally update protocol, estimand or scoring documentation.
6. **Verify separately.** CI and PI (or a second review pass with disclosed limitations) assess the fix; regressions and unresolved blockers remain visible.
7. **Archive decision.** Record issue/PR, relevant SHA, disposition and evidence level. Publication and actual human-subject deployment have separate gates.

### Scientific independence gate

A reviewer must ask: **What evidence would cause us to reject the proposed improvement, even if its author is confident?** If none exists, the claim remains an opinion or hypothesis, not a verified result.

### Conflict and disagreement protocol

When AI reviewers disagree, preserve *both* arguments, identify discriminating experiments, and escalate unresolved design or risk choices to the human owner. Majority vote among LLMs is **not** validation. The adversarial reviewer is rewarded for high-quality counterexamples, not the number of objections or agreement with the author.

## 4. Required finding schema

```yaml
finding_id: HALA-PI-001
tested_commit: "<exact SHA>"
environment: "<OS / Python / deployment details>"
reviewer: "PI (AI agent), independence not externally verified"
area: "scientific-design | reliability | security | privacy | UX | accessibility"
severity: "BLOCK | HIGH | MEDIUM | LOW"
claim: "<precise observable defect>"
evidence: "<logs/links or test fixture; redact secrets>"
reproduction: "<minimal deterministic steps>"
expected: "<expected result>"
actual: "<observed result>"
possible_falsifier: "<what would show the finding is wrong>"
proposed_fix: "<minimal remedy>"
owner_decision: "pending | accepted | rejected | deferred"
verification: "pending | passed | failed"
```

**Never fabricate a finding or claim PI has completed a test before the evidence is posted.**

## 5. Two different things we must not confuse

| Process property | Evidence that can support it | What it cannot establish |
|---|---|---|
| AI-to-AI challenge improved software quality | Reproducible bug reports, corrected tests, before/after CI, independent replay | Improved student understanding |
| Separate agents produced different critiques | Saved prompts, artefacts, versions and disagreement ledger | Independence in the statistical, institutional or human peer-review sense |
| Human owner chose between competing recommendations | Time-stamped, reasoned decisions and acceptance criteria | Objective educational effectiveness |
| Real participants eventually demonstrate independent transfer/retention | Approved study, defensible measures and sufficient uncertainty analysis | Generalization to all students or countries without additional evidence |

The **Pyragogy/UnPeeragogy workflow itself** can be investigated as a future case study. This would require a separately defined research question, observational protocol, baselines, reproducible outcomes and explicit limitations; one success story does not validate a general hypothesis.

## 6. Case chronology and evidence status

| Date | Event | Source | Status |
|---|---|---|---|
| 2026-10-08 | HALA v0.2 synthetic demonstration developed and CI tested | `prototype/webdemo/` and Actions | Software evidence; not learning evidence |
| 2026-10-08 | PI audit assignment created | [Issue #5](https://github.com/pyragogy/human-ai-learning-assessment/issues/5) | Verifiable assignment |
| 2026-10-08 | Owner reports PI cloned to VPS and began issue #5 review | Owner's report in project discussion | Reported; **findings pending** |
| Pending | PI findings, reproduced counterexamples and priorities | Issue #5 comments / linked review | **Not yet recorded** |
| Pending | Human decisions, fixes and separate re-verification | Issues, PRs and decision ledger | **Not yet recorded** |

## 7. Hard boundaries

- **No human learning claim from simulated data, scripted tutors, CI or peer-agent agreement.**
- **No real learner data in Git**, issue comments or public demo logs.
- No opening the private repo, public deployment or student recruitment without explicit owner approval and applicable review.
- No agent may silently alter the study's outcome hierarchy or equating assumptions.
- No external human specialist endorsement without genuine documented participation.
- Clearly distinguish **AI-agent code review** from **independent scientific peer review**.

## 8. Concrete next steps

- PI posts a version-pinned findings report on issue #5.
- Development assistant triages findings and proposes testable corrections.
- Owner decides prioritisation and whether to authorise any public exposure.
- Produce a short **Collaborative Research Process Report** covering accepted findings, false alarms, disagreement cases, revisions, and unresolved limitations, with GitHub links.
- Decide whether this workflow merits a *separate* formal study instead of treating it as proven.

---

**Working maxim:** *Build carefully. Challenge ruthlessly. Measure independently. Publish limitations.*
