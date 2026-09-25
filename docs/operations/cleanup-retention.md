# Cleanup and Retention

Every temporary resource records creator, purpose, creation time, device lifecycle expiry, retention policy, policy context, and budget context. Purpose is untrusted descriptive input and must never grant authority.

## Device lifetime versus lease lifetime

Device lifetime and lease lifetime are independent clocks.

- Lease expiry does not destroy a persistent device. It revokes that principal/client's control and closes or pauses its session according to policy.
- A persistent device may survive many sequential leases, but no lease becomes permanent merely because the device is persistent.
- An ephemeral device requires an enforceable `lifecycle_expires_at`. Reaching device lifecycle expiry starts cleanup even if a client or agent is still running.
- Lease expiry on an ephemeral device does not by itself prove the device was destroyed; lifecycle cleanup must run and confirm provider absence.
- A persistent device may have a policy-scheduled lifecycle expiry, but omission of that optional expiry never implies permanent access.

## Ordered cleanup

1. Stop accepting new control operations.
2. Preserve explicitly approved outputs.
3. Close or fail active sessions.
4. Revoke leases and temporary credentials.
5. Detach mounts and release network allocations.
6. Wipe/delete temporary state according to provider guarantees.
7. Destroy the environment idempotently.
8. Reconcile absence and record evidence.

Cleanup failures move to a retriable recovery/quarantine workflow; they never mark a resource destroyed merely because a deletion request was sent.

Ephemeral devices require `lifecycle_expires_at`/device TTL. Persistent devices follow retention policy and may outlive many leases, but every lease remains temporary and revocable.
