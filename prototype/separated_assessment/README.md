# HALA independent assessment worker — experimental process prototype

**Status: development fixture only.** This is a *separate-process* Unix-socket assessment service, deliberately **not integrated** into the current webdemo's browser flow. There is no real human data, grading, calibrated form, signed receipt, or field-use authorization.

## What has been built

- `prototype/separated_assessment/service.py`: Unix socket service supporting `start`, `issue`, `item` and `complete`.
- `prototype/separated_assessment/private_items.py`: synthetic assessment item bank, separate from the tutor mock module.
- `prototype/boundaries.py`: explicit allowlists for tutor-facing context and blinded rater packets.
- `prototype/tests/test_boundaries.py`: deterministic negative tests for unknown/expired/replaced capabilities, replay, stage order, packet schema violations and Unix socket round trips.

## Run on Linux, local only

From the repository root:

```bash
mkdir -p /tmp/hala-assessor-private
chmod 700 /tmp/hala-assessor-private
python -m prototype.separated_assessment.service /tmp/hala-assessor-private/assessor.sock
```

The socket file is set to mode 0600. This service is a *standalone test harness*: do not forward it to an external network, add real participant information, or connect a model provider.

## Critical remaining limitations

1. **The existing web UI remains on the older in-process assessment path.** The new worker demonstrates process separation but is not yet the live assessment backend for the web journey. No misleading claim of full HALA isolation is allowed.
2. **Process separation ≠ authorization.** Socket permissions alone are insufficient unless the assessor and tutor run under separate identities, the tutor lacks access to the private directory, and the orchestrator is individually authorized. On the same operating-system account, any process that can connect can request `start` and `issue` and see item text.
3. **Single stage scope, not item secrecy against the browser.** A valid token retrieves the current synthetic item. Issuing another token revokes the former; completing the stage consumes its token. The protocol does not prevent learners sharing content with outside systems.
4. **No signed receipts or immutable event anchoring.** The receipt is a random opaque identifier, not a digital signature; there is no verifiable append-only journal or independent signing identity.
5. **No persisted consent, answers, deletion workflow, rate-limit policy, human-evaluation blinding or audit of child/minor data handling.** None of those can be inferred from successful unit tests.
6. **No production availability assurances.** The fixture store is process-memory only. Restart loses state. The service is intentionally limited to local developer experiments.

## Next gates

- Enforce separate Linux user identities, directory ACL and process sandbox; test tutor access denial from that distinct identity.
- Implement orchestrator-to-worker proxy with session-scoped authorization and replay controls; remove the assessment-item import from the browser-serving process.
- Add independently verifiable signed receipts and tamper-detection tests, plus masked exports.
- Conduct an external expert security/methodology review prior to experiments with human learners.

See [RFC-003](../../research/architecture/RFC_003_SEALED_ASSESSMENT.md) and [PI addendum](../../research/architecture/RFC_003_ADDENDUM_A.md). All findings remain purely technical.
