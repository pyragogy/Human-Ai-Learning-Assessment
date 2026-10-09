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

## Browser demonstrator (synthetic only)

From repository root (Linux/macOS, Python 3.10+):

```bash
python -m prototype.separated_assessment.launch_local
```

Visit `http://127.0.0.1:8766` locally; on a remote VPS, use an SSH tunnel. This starts two same-OS-user Python processes with a temporary development credential. It is not independent OS-account isolation. Arm C is a scripted mock; T4 happens in the same session. No live models or real learner data.

The older `prototype/webdemo/server.py` (port 8765) is a legacy single-process comparison path, **not** the recommended process-separated demo. The `conversation_annotation.py` module illustrates heuristic coding limitations and always returns a null proficiency score.

**GitHub Actions is intentionally disabled** by the owner. The commands above and the unit tests run manually, with no hosted runner billing.

## Next engineering stage
Consent flow, secure event ingestion, locked intervention scripts, task delivery, blinded rubrics, export provenance, participant withdrawal, and a real ethics review. Do not log raw student conversations in Git.
