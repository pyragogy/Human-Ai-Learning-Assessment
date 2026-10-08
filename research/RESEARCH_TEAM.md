# Virtual research team — role charters v0.2

This is a **division of work and adversarial review protocol**, not a claim that independent human experts or autonomous AI agents have been recruited or executed.

| Role | Mandate | Mandatory review question | Deliverable |
| --- | --- | --- | --- |
| PI / Scientific integrator | align construct, study aims, decisions and scope | What is the precise inference we can defend? | decision log |
| Psychometrician | item calibration, reliability, validity, DIF | Does the score actually measure learning? | measurement dossier |
| Causal inference analyst | randomisation, comparison, confounding, missingness | What would happen without the intervention? | estimand / SAP |
| Learning scientist | construct definition, conceptual change, transfer | Has competence been internalised? | learning task blueprint |
| HCI / AI interaction researcher | tutoring scripts, fidelity, process observables | Is there a manipulable, testable mechanism? | intervention manual |
| Privacy / ethics reviewer | consent, minors, GDPR, minimisation | Could the experiment harm or expose learners? | ethics gate |
| Red-team / replication auditor | attack confounds, test leakage, unearned claims | How might our conclusions be false? | adversarial audit |
| Product & reproducibility engineer | event schemas, replay, deterministic scoring | Can an independent team reproduce the pipeline? | versioned prototype |

## Review procedure
Every milestone is reviewed in four passes: (1) construct and outcome, (2) causal identification, (3) privacy and implementation, (4) falsification. A reviewer must state PASS / REVISE / BLOCK, a concrete supporting artifact and an unresolved concern. Conflict is recorded, not silently resolved by majority vote.

## Current state
These are **specified roles** only. No independent psychometrician, ethics board, or human reviewer has signed off. No real participants have been studied. No AI subagents have been launched in the background.

## Gates
G0 documented theory -> G1 defined constructs -> G2 runnable synthetic demonstrator -> G3 ethical authorisation -> G4 approved feasibility pilot -> G5 reliability/validity evidence -> G6 confirmatory replication. Claims must never cross gates by prose alone.
