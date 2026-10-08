"""Fixed mock learning experiences. Contains NO assessment items.

No LLM calls are performed. This boundary is illustrative, not hardened.
"""
LESSONS = {
    "A": {
        "title": "Independent learning materials",
        "turns": [
            "A correlation is a relationship observed between variables. It does not by itself show that one variable causes the other. Hidden factors, reverse causation and selection effects can explain an association.",
            "Self-check: Before concluding causation, ask whether people were randomly assigned, whether alternative explanations exist, and what evidence would challenge the proposed claim.",
        ],
    },
    "B": {
        "title": "Explanatory AI tutor — scripted mock",
        "turns": [
            "Tutor: Correlation tells us two things vary together. Causation means changing one actually influences the other. An observation alone often cannot distinguish these.",
            "Tutor: Consider a third variable that influences both. Experiments and carefully controlled comparisons can strengthen a causal argument, though each has limitations.",
        ],
    },
    "C": {
        "title": "Critical AI collaborator — scripted mock",
        "turns": [
            "Collaborator: State your initial causal hypothesis. What evidence would convince you? What observation could prove your explanation wrong?",
            "Collaborator: Now argue against your own hypothesis. Identify a hidden variable and propose an independent test. Which part of your claim remains uncertain?",
        ],
    },
}
