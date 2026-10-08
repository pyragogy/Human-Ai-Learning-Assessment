# HALA Research Demonstrator v0.2

**Status:** local interactive software prototype · scripted content · simulated study flow · **not approved for human-subjects research**.

## Start in under one minute

Requires Python 3.10+ (standard library, no dependencies or API keys).

```bash
python prototype/webdemo/server.py
# Open http://127.0.0.1:8765
```

Stop with `Ctrl+C`. The application binds **only to 127.0.0.1**, never to a public network interface.

## What is implemented

- Responsive research UI in English with experimental condition A (fixed non-AI), B (mock explanatory tutor), or C (mock critical collaborator).
- A deliberately constrained five-stage journey: T0 independent baseline → T1 scripted teaching → T2 independent post-test → T3 transfer → T4 demonstration of retention stage.
- *Server-side* assessment item bank in `assessment.py`; mock teaching content in `teaching.py`.
- Session tokens using `secrets.token_urlsafe`, in-memory phase state, maximum response length, content-length restriction, and no response echoing.
- Automated state-machine and localhost HTTP tests. No secrets, provider accounts, model API calls, cookies, database, analytics, or third-party frontend resources.

## Crucial constraints

1. **No real AI is connected.** Arm B/C texts are authored mock teaching materials, not live or generative agent responses.
2. **No learner scores are generated.** Users can type illustrative answers, but no performance or learning inferences are made.
3. **T4 is immediate in the demo.** It is not genuine delayed retention; a study requires a 7–14-day later evaluation.
4. **Not suitable for research with real participants.** No participant informed consent, ethics approval, accessibility audit, signed audit log, deletion interface, regulatory basis or independent measurement validation.
5. **The isolation is structural, not security-grade.** Assessment items and teaching materials are separate modules, and teaching responses exclude future assessments. The same local server can access both, so a production design requires an independent assessment service, separate permissions, and a secure item bank.
6. **Ephemeral is not automatically anonymous.** Text typed into the demo is kept in server RAM until process termination; do not enter personal or sensitive data. Starting another browser session does not erase previous in-memory server sessions.
7. Public release is blocked on the [release gate](../../governance/PUBLIC_RELEASE_GATE.md).

## Verification

```bash
python -m unittest discover -s prototype/tests -v
python -m compileall -q prototype
python prototype/journey.py > synthetic_journey.json
```

CI executes these tests. The term “independent” describes the intended *measurement condition*, not an independently validated learning assessment.

## Architecture (development only)

```text
Browser UI (HTML/CSS/JS)
       |
       | JSON over loopback HTTP
       v
Local state machine (server.py)
     /                      \
Mock tutor materials         Assessment item bank
(teaching.py)                (assessment.py)
     |                              |
     +--------- phase control ------+
                (T0→T4)

No model provider. No real participant store. No external services.
```

For a field study, the teaching process should **never** have read access to sealed assessment items, and human assessor blinding must be specified and enforced.

## Future milestone (v0.3)

A genuinely independent assessment service, consent-gated storage, versioned interventions, researcher exports, role-specific access controls, and separate scoring workflow. Each step remains conditional on methodological and ethical review.
