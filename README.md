# AI Virtual Compute

AI Virtual Compute is an independent, capability-based control plane for securely provisioning and operating virtual computers and virtual devices for humans, AI systems, agents, applications, and automation.

> Give AI systems computers when they need computers, without giving them uncontrolled infrastructure.

## Current status

**0/12 stages complete — Stage 0 (Architecture & Contracts) in progress.**

This repository currently contains the authoritative Stage-0 architecture and public contract foundation. It deliberately does **not** integrate a real hypervisor, Android emulator, Windows VM, Apple simulator, GPU, cloud provider, or Personal AI.

## Project boundary

- This is a new, independent platform.
- Personal AI is a future API client, not a privileged internal component.
- Clients request capabilities; the platform selects the smallest safe provider.
- Models and agents are clients of the runtime, never the security boundary.
- Access is granted through scoped, revocable, expiring leases.
- Runtime-owned lifecycle state cannot be assigned by a client.

## Architecture

```text
Human / AI / Agent / Application
              |
Authenticated Compute API
              |
Policy + Permissions + Approval + Budget
              |
Capability Resolver -> Scheduler -> Provider
              |
Secure Virtual Resource
              |
Session + Lease + Controlled Execution
              |
Output / Snapshot / Suspend / Destroy + Audit
```

The normative documents are:

- [Product requirements](docs/architecture/product-requirements.md)
- [System architecture](docs/architecture/system-architecture.md)
- [Domain model](docs/architecture/domain-model.md)
- [Threat model and trust boundaries](docs/security/threat-model.md)
- [Security invariants](docs/security/security-invariants.md)
- [Provider contract](docs/providers/provider-contract.md)
- [API v1](docs/api/api-v1.md)
- [Testing strategy](docs/testing/testing-strategy.md)
- [Stage-0 closure checklist](docs/stages/stage-0-closure.md)

Machine-readable contracts live under [`contracts/`](contracts/).

## Stage model

| Stage | Scope |
|---|---|
| 0 | Architecture and contracts |
| 1 | Control plane and FakeDeviceProvider |
| 2 | Identity, policy, approvals, quotas, and leases |
| 3 | Capability resolver and scheduler |
| 4 | Secure sandbox |
| 5 | Linux and virtual desktop |
| 6 | Android |
| 7 | Storage, network, and credentials |
| 8 | Windows and expanded desktop |
| 9 | Apple, GPU, and cloud providers |
| 10 | SDKs, CLI, and multi-agent compute |
| 11 | Device Center and human UX |
| 12 | Whole-system security, reliability, and production qualification |

## Validate Stage 0

Requires Python 3.11 or newer and uses only the standard library:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/qualify_stage0.py
```

## Development rule

Every stage follows:

`PLAN -> IMPLEMENT -> UNIT -> INTEGRATION -> SECURITY -> FAILURE -> REGRESSION -> DIFF -> EXACT HEAD -> EVIDENCE -> CLOSE`

No stage is complete merely because code was written.

## License

No open-source license has been granted yet. All rights are reserved until the owner selects a license.
