"""HALA adaptive *mock* critical collaborator.

A deterministic branching fixture, not an LLM, therapeutic tool, human tutor,
pedagogically validated instrument, or evidence of actual student learning.
Does not import the assessment bank or access test items.
"""
import hashlib

POLICY = (
    "HALA C synthetic critical-collaboration policy v0.3a: ask for a falsifier, "
    "consider alternatives, verify evidence, revise uncertainty."
)
POLICY_SHA256 = hashlib.sha256(POLICY.encode("utf-8")).hexdigest()


def respond_to_claim(claim):
    """Return one of three predeclared critical prompts based on learner wording."""
    if not isinstance(claim, str):
        raise ValueError("Claim must be text")
    text = claim.casefold()
    if any(term in text for term in ("cause", "because", "leads to", "effect")):
        mode = "causal-claim"
        message = (
            "You have advanced a possible causal explanation. What observation "
            "would disconfirm it? Give a competing explanation and describe "
            "what evidence could distinguish the two."
        )
    elif any(term in text for term in ("not sure", "uncertain", "don't know", "maybe")):
        mode = "uncertainty"
        message = (
            "You have expressed uncertainty. Which assumption is least secure? "
            "Name a testable hypothesis and one piece of evidence that would "
            "change your confidence."
        )
    else:
        mode = "other-claim"
        message = (
            "I cannot yet identify a testable causal claim in that statement. "
            "Restate it as a falsifiable hypothesis, then propose a plausible "
            "alternative and an independent way to check it."
        )
    return {"mode": mode, "message": message, "policy_sha256": POLICY_SHA256,
            "provider": "deterministic_scripted_mock", "synthetic_only": True}
