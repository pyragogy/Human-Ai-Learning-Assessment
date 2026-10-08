"""HALA synthetic-only boundary contracts.

Fail closed on unknown fields. This is data minimization, not access control.
"""
TUTOR_FIELDS = ("session_ref", "arm", "topic", "turn", "dialogue", "provider", "policy_hash")
RATER_FIELDS = ("response_ref", "item_code", "form_version", "response_text", "packet_version")

def validate_fields(payload, fields):
    if not isinstance(payload, dict):
        raise ValueError("Expected dictionary")
    if set(payload) != set(fields):
        raise ValueError("Unexpected or missing fields")
    return {name: payload[name] for name in fields}

def tutor_packet(payload):
    output = validate_fields(payload, TUTOR_FIELDS)
    if output["arm"] not in ("B", "C"):
        raise ValueError("Only B and C use tutor adapters")
    return output

def rater_packet(payload):
    return validate_fields(payload, RATER_FIELDS)
