# ADR-0001: Capability-Based Independent Control Plane

Status: **Accepted for Stage 0**

## Context

Clients need computers without depending on a particular hypervisor, emulator, cloud, or operating system. Agents cannot be allowed to select privileged infrastructure or become an authorization source.

## Decision

- Maintain an independent control plane with generic principals and clients.
- Accept declarative capability requests.
- Resolve the smallest safe eligible resource.
- Hide replaceable provider details behind `ComputeProvider`.
- Keep device, session, and lease separate.
- Make leases scoped, revocable, expiring, and auditable.
- Begin implementation with FakeDeviceProvider.

## Consequences

- More contract and policy work precedes real-device demos.
- Providers can evolve without rewriting public clients.
- Personal AI can integrate later through the same authenticated API as other clients.
- Provider-specific features require explicit, discoverable capabilities rather than API leakage.
