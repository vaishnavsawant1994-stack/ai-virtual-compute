# Stage-0 Product Requirements

Status: **normative draft**

Scope: independent virtual-compute platform; Personal AI integration excluded.

## Functional requirements

| ID | Requirement | Stage owner |
|---|---|---|
| FR-001 | Accept authenticated capability-based resource requests. | 1-3 |
| FR-002 | Select the smallest safe resource satisfying all required capabilities. | 3 |
| FR-003 | Keep device, session, and lease as separate authoritative entities. | 1-2 |
| FR-004 | Validate every lifecycle transition server-side. | 1 |
| FR-005 | Support discoverable, provider-specific capabilities. | 1 |
| FR-006 | Issue scoped, revocable, expiring leases. | 2 |
| FR-007 | Attribute every privileged operation to a principal and client. | 2 |
| FR-008 | Enforce permission, approval, quota, budget, and emergency policy server-side. | 2-3 |
| FR-009 | Support human watch, takeover, pause, return, stop, suspend, and destroy semantics. | 11 |
| FR-010 | Audit security-significant requests, decisions, transitions, and exports. | 1-12 |
| FR-011 | Support ephemeral and persistent resources without flag-only promotion. | 1, 5, 7 |
| FR-012 | Support versioned, immutable, integrity-verifiable golden images. | 4-9 |
| FR-013 | Support ownership-checked snapshots and retention. | 5-9 |
| FR-014 | Separate temporary, persistent, and canonical platform-managed storage. | 7 |
| FR-015 | Enforce network profiles below the guest/client layer. | 4, 7 |
| FR-016 | Broker temporary, scoped credentials without exposing the full secret store. | 7 |
| FR-017 | Enforce automatic expiry and cleanup for temporary resources. | 1-4 |
| FR-018 | Quarantine suspicious resources distinctly from suspension. | 1-4 |
| FR-019 | Emergency stop blocks provisioning and revokes active control independently of agents. | 2 |
| FR-020 | Tolerate provider, host, network, agent, storage, and credential failures safely. | 1-12 |
| FR-021 | Allow independent Python, TypeScript, CLI, REST, WebSocket, and agent-tool clients. | 10 |
| FR-022 | Preserve a provider abstraction capable of future remote physical-device adapters. | 0-1 |
| FR-023 | Keep device lifecycle expiry independent from lease expiry; a persistent device may survive sequential temporary leases. | 0-2 |
| FR-024 | Bind devices, sessions, leases, snapshots, and audit events to canonical tenant context without trusting caller tenant claims. | 0-2 |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR-001 | Deny by default when authority, policy, capability, or lifecycle evidence is absent. |
| NFR-002 | Make operations idempotent or explicitly non-idempotent with safe retry semantics. |
| NFR-003 | Preserve tenant isolation across API, storage, network, snapshot, credential, and provider layers. |
| NFR-004 | Never rely on a guest or model voluntarily enforcing a security boundary. |
| NFR-005 | Record structured, tamper-evident audit evidence without default full-screen recording. |
| NFR-006 | Version public contracts and avoid leaking replaceable provider details. |
| NFR-007 | Refuse unsafe allocation under capacity, quota, budget, storage, or provider-health pressure. |
| NFR-008 | Provide deterministic tests using FakeDeviceProvider before real-provider integration. |
| NFR-009 | Exceptional lifecycle states must be reachable and denial/failure/E-stop paths must not strand resources. |

## Explicit V1 exclusions

- Reimplementation of Personal AI physical-device control.
- Unrestricted host/hypervisor access for agents.
- Production claims for any unqualified provider.
- Automatic persistent promotion by mutable metadata alone.
- iOS simulator claims equivalent to physical iPhone hardware.
