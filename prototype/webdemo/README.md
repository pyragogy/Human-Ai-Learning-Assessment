# HALA legacy single-process research demonstrator (port 8765)

**Status:** legacy local interactive software prototype · scripted content with deterministic C-arm branching · simulated study flow · **not approved for human-subjects research**.

> [!WARNING]
> This is the older single-process demo; **do not use it to assess HALA's process-separated architecture**. Run `python -m prototype.separated_assessment.launch_local` instead for the synthetic two-process worker + gateway (port 8766). Neither is secure for real research participants.

## Start the legacy demo

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
- Inactive sessions expire after 30 minutes; restarting the browser flow requests server-side deletion of previous answers. The live-session cap remains 100.
- **C arm only:** second scripted prompt branches deterministically based on the first claim (causal, uncertainty or other), with a SHA-256 identifier for the mock policy. This is a technical interactivity fixture, not a real model.
- Automated state-machine and localhost HTTP tests. No secrets, provider accounts, model API calls, cookies, database, analytics, or third-party frontend resources.

## Crucial constraints

1. **No real AI is connected.** Arm B texts are fixed mock lessons; arm C has a small deterministic conditional response, not live or generative agent responses.
2. **No learner scores are generated.** Users can type illustrative answers, but no performance or learning inferences are made.
3. **T4 is immediate in the demo.** It is not genuine delayed retention; a study requires a 7–14-day later evaluation.
4. **Not suitable for research with real participants.** No participant informed consent, ethics approval, accessibility audit, signed audit log, deletion interface, regulatory basis or independent measurement validation.
5. **The isolation is structural, not security-grade.** Assessment items and teaching materials are separate modules, and teaching responses exclude future assessments. The same local server can access both, so a production design requires an independent assessment service, separate permissions, and a secure item bank.
6. **Ephemeral is not automatically anonymous.** Text typed into the demo is kept in server RAM until explicit session deletion, 30-minute inactivity expiry or process termination. Do not enter personal or sensitive data. Network/browser security hardening remains incomplete.
7. Public release is blocked on the [release gate](../../governance/PUBLIC_RELEASE_GATE.md).

## Verification

```bash
python -m unittest discover -s prototype/tests -v
python -m compileall -q prototype
python prototype/journey.py > synthetic_journey.json
```

Run these tests locally/on your own VPS. GitHub Actions is disabled to avoid hosted runner usage. The term “independent” describes the intended *measurement condition*, not an independently validated learning assessment.

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

## PI review and v0.3 architecture

The [PI VPS audit](../../research/reviews/PI_VPS_AUDIT_TRIAGE_2026-10-08.md) identified session-lifetime and interactivity weaknesses. The follow-up implements a local session TTL, disposal endpoint and deterministic adaptive mock. A separate-process Unix socket assessment worker and gateway are now **implemented as a synthetic fixture**: [integration guide](../separated_assessment/INTEGRATION.md) and [RFC-003](../../research/architecture/RFC_003_SEALED_ASSESSMENT.md). This **legacy** server still runs the tutor and item bank in the same process and is unsuitable for secrecy-sensitive evaluation. The newer gateway also lacks independently verified distinct-OS-user security.
