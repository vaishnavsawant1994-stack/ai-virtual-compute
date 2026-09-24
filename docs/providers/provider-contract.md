# ComputeProvider Contract v1

Providers translate normalized control-plane operations into backend-specific operations. They do not authenticate clients, grant permissions, approve risks, or issue leases.

## Required operations

| Operation | Semantics |
|---|---|
| `capabilities` | Return versioned supported capabilities and limits. |
| `allocate` | Reserve/create a resource using an idempotency key and normalized spec. |
| `boot` | Move an allocated resource toward provider-ready state. |
| `status` | Return observed provider state without mutating canonical lifecycle directly. |
| `connect` | Return a short-lived, scoped control/data channel descriptor. |
| `control` | Execute a supported normalized GUI/app/file/device operation. |
| `snapshot` | Create a provider snapshot after control-plane authorization. |
| `restore` | Restore an ownership-validated snapshot. |
| `suspend` | Stop execution while preserving allowed state. |
| `resume` | Resume a suspended resource. |
| `reset` | Reset resource state according to declared semantics. |
| `destroy` | Idempotently make the resource unavailable and start deletion. |
| `health` | Return provider/host health and capacity observations. |

## Behavioral requirements

- All mutating calls accept `operation_id` and `idempotency_key`.
- Timeouts produce an unknown outcome until reconciled; they do not justify blind retry.
- Provider identifiers are opaque and remain internal.
- Capability discovery is versioned and cannot silently broaden an active lease.
- Errors map to the public error taxonomy without leaking secrets or host topology.
- Destruction is idempotent; already-absent is a successful terminal condition.
- Provider observations are reconciled by the lifecycle manager.
- Provider adapters emit correlation data for audit without accepting audit authority.

The machine-readable request/response envelope is in `contracts/provider/provider-v1.schema.json`.
