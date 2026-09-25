# System Architecture

## Layers

1. **Client access** — REST, WebSocket, SDKs, CLI, and agent-tool interfaces.
2. **Identity and security** — authentication, authorization, policy, approval, quotas, budgets, revocation, rate limits, and emergency controls.
3. **Control plane** — resolver, scheduler, registries, lifecycle, sessions, leases, storage, networking, credentials, health, recovery, quarantine, and audit.
4. **Provider layer** — replaceable implementations behind the versioned provider contract.
5. **Compute resources** — isolated browser, container, sandbox, VM, mobile, desktop, GPU, and future remote-device environments.

## Authoritative request path

1. Authenticate the principal and client.
2. Parse and validate the capability request.
3. Evaluate permission, risk, approval, quota, budget, and emergency policy.
4. Resolve candidate device classes and providers.
5. Schedule only onto a healthy host with sufficient reserved capacity.
6. Allocate and boot through a provider operation with an idempotency key.
7. Register authoritative device state.
8. Create a session and issue a scoped lease.
9. Route control operations only after current lease and policy validation.
10. Audit decisions, state transitions, credential use, exports, and cleanup.

## Authority ownership

| Fact | Authoritative owner | Untrusted input |
|---|---|---|
| Authenticated identity | Identity service | Headers or model claims |
| Permission and approval | Policy/approval services | UI state or booleans |
| Device lifecycle | Lifecycle manager | Client-assigned state |
| Provider capability | Provider registry + attestation | Requested capability |
| Host capacity | Scheduler/host registry | Provider advertisement alone |
| Lease validity | Lease manager | Cached client token alone |
| Network isolation | Network controller/provider enforcement | Guest firewall |
| Credential scope | Credential broker | Guest request body |
| Audit outcome | Audit recorder | Client log statement |

## Persistence rule

Ephemeral devices require a device lifecycle expiry. Persistent devices may outlive many access leases according to policy, but all access leases remain temporary and revocable. Lease expiry revokes control and does not destroy a persistent device; device lifecycle expiry initiates cleanup and confirmed destruction for an ephemeral device. Promotion from ephemeral to persistent is a security workflow, not a database flag change.

## Control-plane principle

The control plane should remain small, deterministic, and independent of guest cooperation. Provider adapters may be complex; they cannot inherit policy authority.
