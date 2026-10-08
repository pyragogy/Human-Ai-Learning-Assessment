# Intervention manual — version 0.1

## Shared instructional task
Evidence-based causal reasoning. Same curated documents, scope, session duration, access requirements and intended learning outcomes for all arms. T2/T3/T4 secure independent tasks must never be exposed to the teaching agents.

## Arm A: non-AI active comparator
Provide prepared text with examples, self-check questions and worked explanations. Equivalent intended learning time, no AI interaction.

## Arm B: explanatory AI tutor
System instruction (research draft):

> You are an educational tutor in causal reasoning. Help learners understand the difference between association and causation using clear explanations and comprehension checks. Do not provide answers to secure assessment tasks. Offer supportive feedback based only on the teaching material. If uncertain, state uncertainty. Do not fabricate studies or facts.

## Arm C: critical collaborative AI
System instruction (research draft):

> You are a critical learning collaborator, not a grader. Elicit the learner's initial hypothesis before revealing a solution. Ask them for evidence and an alternative explanation. When reasoning is weak, respectfully challenge the specific assumption and invite independent verification. Do not provide unsupported claims as facts. Avoid adversarial pressure, personal judgments, high-stakes topics or deceptive wrong answers. Do not solve any secure assessment item. After each episode prompt the learner to summarize what they would do independently next time.

## Fidelity codes (research candidates)
- HYP: learner independently articulates a hypothesis
- ALT: learner proposes a plausible alternative
- EVID: learner cites interpretable evidence
- CHAL: learner challenges an AI proposition with reasons
- VERIFY: learner checks evidence externally or against a source
- REVISE: learner makes justified rather than merely cosmetic revision
- DEPEND: learner accepts an answer without a reason despite a verification prompt

Two raters should code a masked sample; report agreement and rubric disagreements. Counts are not equivalent to learning, and over-prompting might inflate counts.

## Task scripts and experimental isolation
1. Confirm study consent and arm. Display only approved common learning objectives.
2. T0 conducted with no AI, recorded separately.
3. T1 uses the matched session, with prompt and model version captured.
4. T2/T3 individual tasks occur in isolated mode with no agent available.
5. T4 follow-up independently. Withdrawal controls remain visible.

## Safety and change control
No participant data before ethics authorisation. Avoid relying on any LLM's assertion of truth, stable behavior or model identity. Prompt changes constitute protocol amendments and should be tracked before deployment.
