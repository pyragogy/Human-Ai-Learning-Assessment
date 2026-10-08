"""Structural checks for the HALA synthetic research event log.

This is a *validator for a scripted fixture*, not a live security boundary.
Errors fail closed. The hash chain alone cannot authenticate a rewritten log.
"""
from collections import Counter

from journey import ARMS, ITEMS, VERSION, isolated, verify

STAGES = ("T0", "T1", "T2", "T3", "T4")
ASSESSMENT_CHANNELS = {"assessment", "fixture_response"}
EXPECTED_ASSESSMENT_ORDER = tuple(
    (stage, channel, ITEMS[stage][0])
    for stage in ("T0", "T2", "T3", "T4")
    for channel in ("assessment", "fixture_response")
)


class IntegrityError(ValueError):
    pass


def validate_journey(log, arm):
    """Validate sequence, schema and isolation for exactly one synthetic run."""
    if arm not in ARMS:
        raise IntegrityError("unknown arm")
    if not isinstance(log, list) or not log:
        raise IntegrityError("empty or non-list event log")
    if not verify(log):
        raise IntegrityError("hash chain invalid")
    if not isolated(log):
        raise IntegrityError("teaching-assessment isolation failed")

    ordered = []
    previous_stage = -1
    for row in log:
        required = {"participant_id", "arm", "stage", "channel",
                    "message", "item_id", "version"}
        if not required.issubset(row):
            raise IntegrityError("required field absent")
        if row["participant_id"] != "SYNTH-" + arm:
            raise IntegrityError("unexpected participant id")
        if row["arm"] != arm or row["version"] != VERSION:
            raise IntegrityError("arm or protocol version mismatch")
        if row["stage"] not in STAGES:
            raise IntegrityError("unknown study stage")
        pos = STAGES.index(row["stage"])
        if pos < previous_stage:
            raise IntegrityError("stage order reversed")
        previous_stage = pos

        channel = row["channel"]
        if row["stage"] == "T1":
            if channel != "lesson" or row["item_id"] is not None:
                raise IntegrityError("teaching boundary violated")
        elif channel not in ASSESSMENT_CHANNELS:
            raise IntegrityError("assessment boundary violated")
        else:
            if row["item_id"] != ITEMS[row["stage"]][0]:
                raise IntegrityError("assessment item/stage mismatch")
            ordered.append((row["stage"], channel, row["item_id"]))
            if channel == "assessment" and row["message"] != ITEMS[row["stage"]][1]:
                raise IntegrityError("assessment prompt mismatch")
    if tuple(ordered) != EXPECTED_ASSESSMENT_ORDER:
        raise IntegrityError("missing, duplicate, or out-of-order assessment event")
    if sum(1 for row in log if row["stage"] == "T1") != 2:
        raise IntegrityError("unexpected lesson event count")
    return {
        "arm": arm,
        "events": len(log),
        "stages": dict(Counter(row["stage"] for row in log)),
        "chain_valid": True,
        "fixture_isolation_valid": True,
        "validity_scope": "scripted_synthetic_fixture_only",
    }
