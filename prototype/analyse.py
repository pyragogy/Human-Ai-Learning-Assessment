"""HALA synthetic research-data validator and descriptive reporter.

This is not an inferential analysis nor a psychometric model.
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

STAGES = ("T0", "T1", "T2", "T3", "T4")
INDEPENDENT = {"T0", "T2", "T3", "T4"}
ARMS = {"A", "B", "C"}
FIELDS = {"participant_id", "arm", "stage", "score", "independent"}


def load_rows(path):
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not FIELDS.issubset(set(reader.fieldnames)):
            raise ValueError("Missing required columns")
        records = {}
        participant_arm = {}
        for line, row in enumerate(reader, 2):
            pid, arm, stage = row["participant_id"].strip(), row["arm"].strip(), row["stage"].strip()
            if not pid or arm not in ARMS or stage not in STAGES:
                raise ValueError(f"Invalid identity, arm or stage on line {line}")
            try:
                score = float(row["score"])
            except (ValueError, TypeError):
                raise ValueError(f"Invalid score on line {line}") from None
            if not (0 <= score <= 100):
                raise ValueError(f"Out-of-range score on line {line}")
            flag = row["independent"].strip().lower()
            if flag not in {"true", "false"}:
                raise ValueError(f"Invalid independent flag on line {line}")
            if (stage in INDEPENDENT) != (flag == "true") or (stage == "T1" and flag != "false"):
                raise ValueError(f"Stage independence mismatch on line {line}")
            if (pid, stage) in records:
                raise ValueError(f"Duplicate participant-stage on line {line}")
            if pid in participant_arm and participant_arm[pid] != arm:
                raise ValueError(f"Inconsistent arm for {pid}")
            participant_arm[pid] = arm
            records[(pid, stage)] = score
    return records, participant_arm


def report(records, participant_arm):
    result = {"method": "descriptive_only", "arms": {}}
    for arm in sorted(ARMS):
        members = sorted(p for p, a in participant_arm.items() if a == arm)
        stage_stats = {}
        for stage in STAGES:
            vals = [records[(p, stage)] for p in members if (p, stage) in records]
            stage_stats[stage] = {"observed_n": len(vals), "missing_n": len(members) - len(vals),
                                  "mean": round(sum(vals) / len(vals), 3) if vals else None}
        gains = [records[(p, "T2")] - records[(p, "T0")] for p in members
                 if (p, "T0") in records and (p, "T2") in records]
        result["arms"][arm] = {
            "participants": len(members),
            "stages": stage_stats,
            "paired_T2_minus_T0_n": len(gains),
            "paired_T2_minus_T0_mean": round(sum(gains) / len(gains), 3) if gains else None,
        }
    result["warning"] = "Synthetic/demo only. These are not causal effects, real findings or validated scores."
    return result


def main(argv):
    if len(argv) != 2:
        raise SystemExit("Usage: python prototype/analyse.py <scores.csv>")
    try:
        records, participants = load_rows(Path(argv[1]))
        print(json.dumps(report(records, participants), indent=2, sort_keys=True))
    except (OSError, ValueError) as exc:
        print(f"Data validation failed: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main(sys.argv)
