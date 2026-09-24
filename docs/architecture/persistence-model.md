# Persistence Model

Stage 0 defines logical entities; physical migrations begin with implementation stages.

| Table/entity | Minimum security-relevant fields |
|---|---|
| principals | id, tenant_id, kind, status, created_at |
| clients | id, principal_id, tenant_id, auth_binding, status |
| providers | id, type, contract_version, status, trust_metadata |
| hosts | id, provider_id, capacity, reserved_capacity, health |
| devices | id, tenant_id, provider_id, host_id, class, persistence, state, version, expires_at |
| device_capabilities | device_id, capability, constraints |
| device_images | id, version, digest, signature_ref, scan_status, immutable |
| device_sessions | id, tenant_id, device_id, principal_id, client_id, state, timestamps |
| device_leases | id, session_id, principal_id, client_id, scope, issued_at, expires_at, revoked_at |
| device_snapshots | id, tenant_id, device_id, owner_principal_id, digest, retention |
| device_volumes | id, tenant_id, kind, encryption_ref, retention |
| device_mounts | device_id, volume_id, mount_policy |
| network_profiles | id, tenant_id/null, ruleset_version, enforcement_mode |
| credential_references | id, tenant_id, broker_locator, scope, expires_at; no plaintext secret |
| policies | id, version, scope, effect, rules_digest |
| approvals | id, policy_id, actor, target, action, decision, expires_at |
| quotas | id, scope, resource, limit, period |
| budgets | id, scope, currency/unit, limit, period, administrative_owner |
| usage_records | id, scope, resource, quantity, start/end, correlation_id |
| audit_events | id, tenant_id, sequence, event, previous_hash, integrity_proof |
| security_events | id, tenant_id, severity, signal, response, status |
| provider_health | provider_id/host_id, observed_at, state, capacity, evidence |

## Transaction and concurrency rules

- Tenant predicates are part of resource lookup, not post-fetch checks.
- Lifecycle mutations use versioned compare-and-swap or row locking.
- Lease issue, capacity reservation, and quota/budget reservation are atomic from the client's perspective.
- Outbox/event persistence is committed with the state change it describes.
- Unique idempotency scope prevents duplicate provisioning on retry.
- Cleanup records remain until absence and evidence retention requirements are satisfied.
- Sensitive application data and storage keys use envelope encryption; secrets remain in the broker/vault.
