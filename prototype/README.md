# Minimal reproducible demonstrator

**Purpose:** illustrate an auditable event-and-score pipeline on synthetic data only. This is **not** an AI tutor, psychometric instrument, experiment, or production-ready system.

## Run
Requires Python 3.10+ standard library only.

```sh
python -m unittest discover -s prototype/tests -v
python prototype/analyse.py prototype/fixtures/synthetic_scores.csv
```

Output is descriptive statistics for independent stages, missingness, and changes from baseline. No p-values, causal effects or learner diagnoses. Synthetic fixtures are deliberately artificial, and are not evidence for an educational benefit.

## Input contract
CSV columns: participant_id, arm (A/B/C), stage (T0/T1/T2/T3/T4), score (0–100), independent (true/false). T1 is assisted for B/C and must **never** be used in an independent learning-gain calculation. Unique (participant_id,stage), one arm per participant, bounded scores, and independent flags for T0/T2/T3/T4 are checked. Missing follow-up data remains missing and is reported without imputation.

## Next engineering stage
Consent flow, secure event ingestion, locked intervention scripts, task delivery, blinded rubrics, export provenance, participant withdrawal, and a real ethics review. Do not log raw student conversations in Git.
