"""Independent assessment item bank for *demo use only*.

Never pass these items to a teaching-model context. The production study will
require a separate service and access-control boundary.
"""
ITEMS = {
    "T0": {
        "title": "Independent baseline",
        "scenario": "A study finds that people who read more books tend to sleep better.",
        "question": "Does this show that reading books causes better sleep? Explain why or why not, and name one alternative explanation.",
    },
    "T2": {
        "title": "Independent post-test",
        "scenario": "An observational report finds that students using a planner receive higher grades.",
        "question": "Can we conclude the planner causes better grades? Explain, name a confounder, and describe a more convincing test.",
    },
    "T3": {
        "title": "Independent transfer",
        "scenario": "Cities with more bicycle lanes report better health outcomes.",
        "question": "Evaluate the causal claim, give a rival explanation, and propose one way to test the proposed cause.",
    },
    "T4": {
        "title": "Retention rehearsal",
        "scenario": "People who regularly attend museums report higher wellbeing.",
        "question": "Explain why this association may not show a causal effect and propose a fairer comparison.",
    },
}
STAGES = ("T0", "T1", "T2", "T3", "T4")
