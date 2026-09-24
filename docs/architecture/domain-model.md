# Domain Model

| Entity | Purpose | Key relations |
|---|---|---|
| Principal | Human, agent, service, application, or automation identity. | owns clients; requests sessions |
| Client | Authenticated software identity acting for a principal. | bound to permissions and budgets |
| Provider | Adapter implementing the provider contract. | manages devices on hosts |
| Host | Capacity and health boundary. | belongs to a provider |
| Device | Virtual compute resource with authoritative lifecycle. | has sessions, volumes, snapshots |
| DeviceClass | Extensible selection hint, not the capability authority. | declares baseline capabilities |
| Capability | Normalized operation/resource property. | requested, supported, or leased |
| Session | Bounded interaction context between client and device. | uses one active lease at a time |
| Lease | Temporary authorization to control a device. | scoped to principal/client/device |
| Image | Versioned immutable resource template. | instantiates devices |
| Snapshot | Ownership-checked point-in-time device state. | belongs to device/principal |
| Volume | Temporary or persistent storage unit. | attached through mounts |
| NetworkProfile | Enforceable connectivity policy. | assigned to device/session |
| CredentialReference | Opaque reference to broker-managed secret material. | never stores plaintext credential |
| Policy | Server-side rule set. | produces allow/deny/approval result |
| Approval | Authoritative decision for a bounded operation. | references policy, principal, target |
| Quota | Non-financial resource ceiling. | scoped to tenant/client/principal |
| Budget | Financial/cost ceiling. | cannot be raised by beneficiary agent |
| UsageRecord | Metered consumption evidence. | supports quota and budget decisions |
| AuditEvent | Structured immutable security/operation evidence. | correlates request and outcome |
| SecurityEvent | Detection and response evidence. | may trigger quarantine/E-stop |

## Separation invariants

- A device existing does not imply any principal has a valid session.
- A session existing does not imply a valid lease.
- A valid lease does not grant unsupported provider capabilities.
- Ownership does not bypass permission, approval, budget, emergency, or lifecycle policy.
- A provider status observation does not directly mutate canonical state; the lifecycle manager reconciles it.
