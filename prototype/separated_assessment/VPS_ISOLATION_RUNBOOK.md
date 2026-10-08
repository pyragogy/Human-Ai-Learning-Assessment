# HALA VPS isolation deployment design — requires administrator review

**Status:** development-only runbook, not executed on the owner's VPS. No public exposure, no real participants, no approved scientific assessment.  
**Applies to:** `prototype/separated_assessment/service.py` and `gateway.py`.

## Goal and process identities

Use **three** distinct Linux identities:
- `hala-assessor`: owns the separate private-item source tree and the Unix-socket assessment worker.
- `hala-gateway`: runs the browser-facing orchestrator, may connect to assessor through a dedicated narrow IPC group.
- `hala-tutor`: potential future AI runtime account, not in the assessor IPC group; must not have filesystem access to private items, gateway environment or private socket directory.

Run a fourth controlled *operator* identity for maintenance. Never run any component as root in routine operation.

**Caution:** creating users/groups and changing permissions can disrupt existing VPS services. The following is a reference configuration for explicit operator review, not automatically applied.

## IPC identity and permissions

Create dedicated Unix group `hala-ipc`, with members `hala-assessor` and `hala-gateway`, **not** `hala-tutor`. Put the socket in a directory owned by assessor, group `hala-ipc`, mode `0710` (directory traversal for authorized group, no listing). The assessor must create the socket owned by assessor, group `hala-ipc`, mode `0660`, setting `HALA_ASSESSOR_SOCKET_GROUP=hala-ipc`. A `0600` socket cannot be accessed by the separate gateway identity even if it belongs to the same group.

**Separate private code deployments:** the tutor must not have read or execute permission on the directory containing `private_items.py`. A git clone accessible to all service identities defeats isolation even when socket ACLs are correct. A full production deployment should package the tutor without assessment item content.

## Credential provision

The assessor and gateway require the same **high-entropy secret** through `HALA_ASSESSOR_SECRET`, at least 32 characters. Generate it with a cryptographically secure generator and place it in **separately restricted environment files** owned by the administrator, readable only by each corresponding service identity. **Never commit the secret to git**, paste it into issue comments or put it in command arguments that appear in process listings. Reject missing/wrong credentials; tests already cover this.

The shared secret is a *defense-in-depth credential* and is not an alternative to OS isolation. Root, same-uid gateway compromise, an attacker with control of gateway's secrets or privileged access can still impersonate it.

## Example systemd configuration considerations

Assessor service:
- `User=hala-assessor`; `Group=hala-assessor`; `SupplementaryGroups=hala-ipc`.
- Restricted `EnvironmentFile` holding secret and socket-group setting.
- `UMask=0077`, `NoNewPrivileges=yes`, `ProtectSystem=strict`, `PrivateTmp=yes`, scoped write access only to the private socket directory.
- The socket directory must exist, have the permissions stated above, and be reachable via the configured absolute path.

Gateway service:
- `User=hala-gateway`; `Group=hala-gateway`; `SupplementaryGroups=hala-ipc`.
- Matching restricted secret, and `HALA_ASSESSOR_SOCKET` path.
- Browser gateway listens only on `127.0.0.1:8766`. Access using SSH forwarding; no public ingress.
- The gateway code package should exclude private test items, and its service account should lack access to assessor item storage.

Tutor service:
- `User=hala-tutor`; **no** `hala-ipc` supplemental group.
- No common readable secret file, no assessable socket path, and no protected item bank in its filesystem view.
- An external LLM adapter remains **not connected**.

**Note:** this is operational guidance, not a tested systemd unit file. Verify syntax and filesystem behavior on the actual VPS before enabling services.

## Independent checks PI must perform

1. Verify process effective UID/GID and supplementary groups with Linux tooling.
2. Under the **gateway** identity, authenticate and complete a synthetic socket round-trip.
3. Under the **tutor** identity, try to open the Unix socket and read the assessor's private item file; both must fail at OS authorization.
4. With gateway socket access but deliberately wrong/missing secret, `start` must be rejected and must not allocate a session.
5. Try replayed, expired and forged capabilities; verify worker cleanup at expiry and browser end.
6. Confirm neither tutor nor its model subprocess inherits `HALA_ASSESSOR_SECRET` or sees scorer/export material.
7. Verify an assessor restart, gateway restart, and lost socket are handled without exposing internal secrets or accepting stale tokens.
8. Ensure gateway endpoint still delivers only current-stage questions and a scripted C-branch, and warns T4 is same-session only.

**Security gate remains open until these tests are executed under distinct OS identities on the VPS.** Passing the single-user CI cannot certify permission isolation.
