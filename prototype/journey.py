"""Synthetic-only HALA study journey. NOT evidence of human learning."""
import hashlib
import json

VERSION = "synthetic-journey-v0.1"
ARMS = {"A": "non_ai", "B": "explanatory_mock", "C": "critical_mock"}
ITEMS = {"T0": ("E1", "Is correlation causation? Explain."),
         "T2": ("E2", "Consider confounding in a new example."),
         "T3": ("E3", "Find an alternative explanation in a new domain."),
         "T4": ("E4", "Evaluate uncertainty in a new causal claim.")}
LESSONS = {"A": ["Printed primer on causal reasoning", "Printed self-check"],
           "B": ["Mock tutor explains confounding", "Mock tutor asks comprehension question"],
           "C": ["Mock collaborator elicits learner hypothesis",
                 "Mock collaborator asks for counterargument and source verification"]}

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))

def chain(events):
    out, previous = [], "GENESIS"
    for i, event in enumerate(events):
        row = dict(sequence=i, previous_hash=previous, **event)
        row["hash"] = hashlib.sha256(canonical(row).encode()).hexdigest()
        out.append(row)
        previous = row["hash"]
    return out

def verify(log):
    previous = "GENESIS"
    for i, row in enumerate(log):
        if row["sequence"] != i or row["previous_hash"] != previous:
            return False
        value = {k: v for k, v in row.items() if k != "hash"}
        if hashlib.sha256(canonical(value).encode()).hexdigest() != row["hash"]:
            return False
        previous = row["hash"]
    return True

def isolated(log):
    protected = [(code, prompt) for stage, (code, prompt) in ITEMS.items() if stage != "T0"]
    for row in log:
        if row["stage"] == "T1":
            if row["channel"] != "lesson" or row["item_id"] is not None:
                return False
            if any(code in row["message"] or prompt in row["message"] for code, prompt in protected):
                return False
        elif row["channel"] == "lesson":
            return False
    return True

def run(arm):
    if arm not in ARMS:
        raise ValueError("Unknown study arm")
    events = []
    def put(stage, channel, message, item_id=None):
        events.append(dict(participant_id="SYNTH-"+arm, arm=arm, stage=stage,
                           channel=channel, message=message, item_id=item_id,
                           version=VERSION))
    code, prompt = ITEMS["T0"]
    put("T0", "assessment", prompt, code)
    put("T0", "fixture_response", "Invented baseline response", code)
    for lesson in LESSONS[arm]:
        put("T1", "lesson", lesson)
    for stage in ("T2", "T3", "T4"):
        code, prompt = ITEMS[stage]
        put(stage, "assessment", prompt, code)
        put(stage, "fixture_response", "Invented "+stage+" response", code)
    log = chain(events)
    assert verify(log) and isolated(log)
    return log

def artifact():
    return dict(provenance="SYNTHETIC: no human subjects and no real AI",
                allowed_claims=["reproducible fixture", "basic pipeline checks"],
                prohibited_claims=["educational efficacy", "human learning",
                                   "psychometric validity"],
                runs={arm: run(arm) for arm in sorted(ARMS)})

if __name__ == "__main__":
    print(json.dumps(artifact(), indent=2))
