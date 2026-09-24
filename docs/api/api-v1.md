# Device API v1

Base path: `/v1`

## Resource requests

`POST /devices` accepts a capability request. The server authenticates the client, evaluates policy, resolves a provider, and returns an operation or a ready device/session/lease representation.

Example:

```json
{
  "purpose": "test web application",
  "capabilities": ["gui", "browser", "internet", "filesystem", "python"],
  "resources": {"memory_mb": 8192},
  "persistence": "ephemeral",
  "ttl_seconds": 3600,
  "network_profile": "normal"
}
```

## Initial endpoints

| Method | Path | Meaning |
|---|---|---|
| POST | `/devices` | Request a device by capability. |
| GET | `/devices/{device_id}` | Read an authority-filtered device representation. |
| POST | `/devices/{device_id}/actions/{action}` | Request validated lifecycle action. |
| POST | `/devices/{device_id}/sessions` | Create an interaction session. |
| POST | `/sessions/{session_id}/leases` | Request a bounded control lease. |
| POST | `/leases/{lease_id}/revoke` | Revoke a lease. |
| POST | `/sessions/{session_id}/control` | Execute a leased normalized control operation. |
| POST | `/devices/{device_id}/snapshots` | Create a policy-authorized snapshot. |
| POST | `/emergency-stop` | Activate an authorized emergency scope. |

## Protocol rules

- Mutating requests require an `Idempotency-Key` unless explicitly documented otherwise.
- All responses include or echo a correlation ID.
- Resource IDs are opaque and never evidence of authorization.
- Clients cannot submit canonical principal, approval result, budget, lifecycle state, or provider ID.
- Long operations return `202 Accepted` with an operation resource.
- Errors conform to `contracts/errors/error-v1.schema.json`.
- Events conform to `contracts/events/event-v1.schema.json`.

Stage 0 freezes shapes and invariants; endpoint implementation begins in Stage 1.
