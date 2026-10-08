# HALA local end-to-end separate-process demonstration

**Milestone:** v0.3a integration. **Status:** synthetic-only developer fixture, not a protected research instrument.

Two independent Python processes now run a browser-facing journey orchestrator and an assessment worker. The gateway talks to the worker using a Unix-domain socket, retrieves the *current* item only and does not import the worker's private item bank. The existing `prototype/webdemo/server.py` is a **legacy single-process demo**, preserved for comparison.

## Start (two terminals; Linux/macOS with Unix sockets)

Before starting, configure the *same* high-entropy value in the `HALA_ASSESSOR_SECRET` environment variable for both processes. This value must be at least 32 characters, must **never be committed**, and should be injected through restricted service configuration rather than pasted into shell history. For distinct Linux service accounts, follow [VPS isolation runbook](VPS_ISOLATION_RUNBOOK.md); do not run these simple same-account commands as evidence of OS-level isolation.\n\nIn terminal 1, from the repository root:

```bash
mkdir -p /tmp/hala-assessor-private
chmod 700 /tmp/hala-assessor-private
HALA_ASSESSOR_SECRET="$HALA_ASSESSOR_SECRET" python -m prototype.separated_assessment.service /tmp/hala-assessor-private/assessor.sock
```

In terminal 2, same repository root:

```bash
HALA_ASSESSOR_SOCKET=/tmp/hala-assessor-private/assessor.sock HALA_ASSESSOR_SECRET="$HALA_ASSESSOR_SECRET" python -m prototype.separated_assessment.gateway
```

Open **http://127.0.0.1:8766** on the same machine. For a remote VPS, use `ssh -L 8766:127.0.0.1:8766 user@vps` and then browse to the local loopback URL. No external public port is needed. Exit both processes after testing. All inputs must be fictitious.

Run tests:

```bash
python -m unittest discover -s prototype/tests -v
```

## Supported flow

- Browser `POST /api/start`: gateway creates its own session and a worker-side test sequence.
- Gateway requests a stage-scoped capability, fetches one synthetic assessment item and returns only that item to the browser at T0/T2/T3/T4.
- At T1, the orchestrator handles A/B fixed materials or the branching C mock; the worker has no T1 route.
- `POST /api/submit`: the gateway checks the current stage, consumes a worker capability for assessments, advances stage and requests the next item only as needed.
- `POST /api/end`: removes the gateway session and requests deletion of the corresponding worker session and its capabilities.
- There is **no scoring**, no true delayed retention, no learner inference, no real model provider, and no research data export.

## Threat boundaries — what's missing

This demonstrates **process separation, a shared-secret application check, and stage-gated delivery**, but **not an independently verified OS permission boundary**. Under the same Linux identity, a process that steals the gateway secret can still access the worker. The worker rejects missing/incorrect secrets, uses bounded sessions with inactivity cleanup, and supports explicit end requests. There are no independently signed receipts. It is not safe to connect a live tutor that can access local files, sockets or host tools.

Before any real model integration: distinct service accounts, restricted working directories, minimal socket permissions for the designated orchestrator only, independently authenticated calls, expiry-aware worker session cleanup, capability issuance audit, and deliberate access-denial tests under the tutor account. Before any participant study: ethics, consent, secure retention/deletion, item validity and assessor blinding.

See [RFC-003 Addendum A](../../research/architecture/RFC_003_ADDENDUM_A.md).

**Version policy:** call this `v0.3a-integration`, not `v0.3c secure assessor`.


## Security gate after PI issue #9

The worker now requires a minimum-length shared secret for requests, bounds live worker sessions, applies inactivity expiry and returns size-limited responses. These checks are exercised in CI. The **OS-user separation has not been applied to the owner's VPS**. The dedicated [runbook](VPS_ISOLATION_RUNBOOK.md) provides a proposed deployment design and mandatory negative checks for PI. This remains a synthetic-only research demonstrator, not a validated research instrument.
