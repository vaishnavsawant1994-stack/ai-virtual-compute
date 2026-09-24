# Cleanup and Retention

Every temporary resource records creator, purpose, creation time, expiry, retention policy, policy context, and budget context.

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

Ephemeral devices require `expires_at`/TTL. Persistent devices follow retention policy and may outlive a single device TTL, but their leases always expire.
