"""Synthetic conversation annotation harness, NOT a competence scorer.

All annotations are heuristic prompts for blinded human review. No validated
psychometric inference, automatic grades, or claims about learner cognition.
"""
import re

PATTERNS = {
    "EVIDENCE_REQUEST": r"\b(evidence|sources?|data|proof)\b",
    "COMPETING_CAUSE": r"\b(maybe|alternatively|another|other explanation|also study)\b",
    "DISCRIMINATING_TEST": r"\b(compare|control for|randomi[sz]e|experiment|test)\b",
    "SOURCE_APPRAISAL": r"\b(reliable|remember|bias|self.report|trustworthy|credib)\b",
    "JUSTIFIED_REVISION": r"\b(revise|change my mind|instead|because of|now think)\b",
    "CALIBRATED_UNCERTAINTY": r"\b(uncertain|don't know|not sure|might|depends|confidence)\b",
}
SCAFFOLD = r"\b(what evidence|what else|alternative explanation|how would|is .* reliable|would you revise|what.*uncertain|how confident)\b"
TOKEN = re.compile(r"[a-z]{4,}")


def _tokens(text):
    return set(TOKEN.findall(text.lower()))


def annotate(transcript):
    """Return descriptive tags only. Input must alternate AI and learner turns.

    The assistance flag means only that the preceding AI turn may have
    scaffolded the behavior. It does not imply low ability or cheating.
    """
    if not isinstance(transcript, list):
        raise ValueError("Expected transcript list")
    rows = []
    previous = ""
    previous_speaker = None
    for index, turn in enumerate(transcript):
        if not isinstance(turn, dict) or set(turn) != {"speaker", "text", "turn_number"}:
            raise ValueError("Expected speaker, text and turn_number")
        speaker, message = turn["speaker"], turn["text"]
        if speaker not in ("ai", "learner") or not isinstance(message, str):
            raise ValueError("Invalid turn")
        if turn["turn_number"] != index + 1 or (previous_speaker == speaker):
            raise ValueError("Turns must be ordered and alternate speakers")
        if len(message) > 4000:
            raise ValueError("Turn too long")
        if speaker == "learner":
            codes = [code for code, pattern in PATTERNS.items()
                     if re.search(pattern, message, flags=re.I)]
            antecedent = previous if previous_speaker == "ai" else ""
            overlap = _tokens(message) & _tokens(antecedent)
            ratio = len(overlap) / max(1, len(_tokens(message)))
            prompted = bool(re.search(SCAFFOLD, antecedent, flags=re.I))
            rows.append({
                "turn_number": index + 1,
                "observed_codes": codes,
                "elicitation": "potential_ai_scaffold" if prompted else
                               ("preceded_by_ai" if antecedent else "no_ai_antecedent"),
                "lexical_echo_flag": ratio >= 0.5 and len(overlap) >= 2,
                "learner_origin": "indeterminate",
                "proficiency_score": None,
            })
        previous, previous_speaker = message, speaker
    return {
        "synthetic_only": True,
        "heuristic_annotation_only": True,
        "learner_turns": rows,
        "naive_code_count": sum(len(r["observed_codes"]) for r in rows),
        "proficiency_score": None,
    }
