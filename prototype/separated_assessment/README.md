# HALA independent assessment worker — experimental process prototype

**Status: development fixture only.** The separate-process worker is integrated through `gateway.py` on loopback port 8766; the legacy browser server on port 8765 remains single-process. There is no real human data, grading, calibrated form, signed receipt, or field-use authorization.

## What has been built

- `prototype/separated_assessment/service.py`: Unix socket service supporting authenticated `start`, `issue`, `item`, `complete` and `end`.
- `prototype/separated_assessment/private_items.py`: synthetic assessment item bank, separate from the tutor mock module.
- `prototype/boundaries.py`: explicit allowlists for tutor-facing context and blinded rater packets.
- `prototype/tests/test_boundaries.py`: deterministic negative tests for unknown/expired/replaced capabilities, replay, stage order, packet schema violations and Unix socket round trips.

## Recommended local synthetic run

From repository root:

```bash
python -m prototype.separated_assessment.launch_local
```

This starts the worker and gateway with an ephemeral development secret on one local OS account. Browse to `http://127.0.0.1:8766` (or use SSH forwarding on a VPS). It is **not a secure study deployment**. The launcher has not yet been independently smoke-tested on the VPS; see the open security/operations gate.

## Run the assessor alone (advanced developer mode)

From the repository root, after configuring a shared secret (minimum 32 characters) in the environment:

```bash
mkdir -p /tmp/hala-assessor-private
chmod 700 /tmp/hala-assessor-private
HALA_ASSESSOR_SECRET="$HALA_ASSESSOR_SECRET" python -m prototype.separated_assessment.service /tmp/hala-assessor-private/assessor.sock
```

The socket file defaults to mode 0600, or 0660 with `HALA_ASSESSOR_SOCKET_GROUP` set to an explicitly authorized Unix group. This service is a *standalone test harness*: do not forward it to an external network, add real participant information, or connect a model provider.

## Critical remaining limitations

1. **The browser UI can use the gateway on port 8766** for a separate-process synthetic worker. Port 8765 remains a legacy in-process comparison path. No misleading claim of full HALA isolation is allowed.
2. **Process separation and a shared secret do not prove OS isolation.** Socket permissions alone are insufficient unless the assessor and tutor run under separate identities, the tutor lacks access to the private directory, and the orchestrator is individually authorized. On the same account, a process with access to the shared secret can still read items; test distinct service-user isolation on the VPS.
3. **Single stage scope, not item secrecy against the browser.** A valid token retrieves the current synthetic item. Issuing another token revokes the former; completing the stage consumes its token. The protocol does not prevent learners sharing content with outside systems.
4. **No signed receipts or immutable event anchoring.** The receipt is a random opaque identifier, not a digital signature; there is no verifiable append-only journal or independent signing identity.
5. **No persisted consent, answers, deletion workflow, rate-limit policy, human-evaluation blinding or audit of child/minor data handling.** None of those can be inferred from successful unit tests.
6. **No production availability assurances.** The fixture store is process-memory only. Restart loses state. The service is intentionally limited to local developer experiments.

## Next gates

- Enforce separate Linux user identities, directory ACL and process sandbox; test tutor access denial from that distinct identity.
- Independently verify gateway/worker access-denial and stage transitions under distinct Linux service identities; the separate-process gateway already exists.
- Add independently verifiable signed receipts and tamper-detection tests, plus masked exports.
- Conduct an external expert security/methodology review prior to experiments with human learners.

See [RFC-003](../../research/architecture/RFC_003_SEALED_ASSESSMENT.md) and [PI addendum](../../research/architecture/RFC_003_ADDENDUM_A.md). All findings remain purely technical.


## Security gate after PI issue #9

The worker now requires a minimum-length shared secret for requests, bounds live worker sessions, applies inactivity expiry and returns size-limited responses. These checks are exercised in CI. The **OS-user separation has not been applied to the owner's VPS**. The dedicated [runbook](VPS_ISOLATION_RUNBOOK.md) provides a proposed deployment design and mandatory negative checks for PI. This remains a synthetic-only research demonstrator, not a validated research instrument.


## Hosted CI and review

GitHub Actions has been deliberately **disabled by the owner** due to account-billing/spending concerns. Run `python -m unittest discover -s prototype/tests -v` locally or on a private VPS. PI reported 66 passing tests for merged PR #12; that report does not verify the newly added one-command launcher. No public port or real student-data collection is authorised.
