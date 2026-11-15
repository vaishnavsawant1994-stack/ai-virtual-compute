# AI Virtual Compute — Project Handbook

> **Repository:** [vaishnavsawant1994-stack/ai-virtual-compute](https://github.com/vaishnavsawant1994-stack/ai-virtual-compute)  
> **Documentation review:** 15 November 2026 · **Scope:** checked-in source and existing documentation, not a fresh end-to-end certification.

## 1. Purpose and intended audience

**Goal:** Capability-based control plane for provisioning and operating virtual compute/device sessions with explicit security boundaries.

**Who this serves:** Developers building governed computer/device execution for human users and AI agents.

## 2. Product features and expected journeys

1. Define contract-first resource and capability interfaces.
2. Separate provider implementations from control-plane policy.
3. Offer API, CLI, SDK and runtime foundations.
4. Require stage gates before real provisioning and agent actions.

These are described product areas or repository-supported development paths. See the status and limitations below before claiming live feature completeness.

## 3. Technical architecture and project structure

Python >=3.11 project; `api/`, `cli/`, `contracts/`, `providers/`, `runtime/`, `sdk/`, `ui/`, `tests/` and `docs/`. pyproject.toml configures Ruff and pytest. No real hypervisor support should be inferred from provider interfaces.

## 4. Implementation maturity and evidence

README records Stage 0 architecture/contracts as qualified and Stage 1 control-plane/fake-provider work gated by review/authorization. Real device or hypervisor provisioning remains unverified.

**Evidence level:** Repository source, current README and available manifest/structure were inspected. No new unit-test run, database migration, browser acceptance, security penetration test, CI re-run or live deployment is implied by this document. Treat older gate reports as date- and commit-specific records.

## 5. Installation, development and validation

Create a Python 3.11+ virtual environment, install the documented project dependencies, then use repository-specific validation scripts. The pyproject documents pytest test discovery under `tests/`.

Recheck exact commands, package versions and environment variables against the current source. Use disposable credentials and isolated local/test data; never run destructive migrations or seed scripts against an unknown database.

## 6. Security, data and operational boundaries

- Deny capabilities unless granted and scoped.
- Isolate executing code and never treat a simulated provider as real infrastructure.
- Require exact-head review and test evidence before activation.

For production use additionally verify access control, errors, secrets, backup/recovery, monitoring and relevant legal/privacy responsibilities.

## 7. Recommended next milestones

1. Complete outstanding Stage 1 review.
2. Strengthen provider reconciliation, logs and fault isolation.
3. Demonstrate fail-closed policy on an isolated fake provider.
4. Specify acceptance gates before any billable/live provider.

## 8. Source documents and change policy

- [`README.md`](../README.md)
- [`pyproject.toml`](../pyproject.toml)
- [`contracts/`](../contracts/)
- [`docs/`](../docs/)
- [`tests/`](../tests/)

This handbook supplements rather than replaces authoritative specs, security rules and exact-SHA qualification. Update it whenever the application architecture, deployment status, feature contract or project ownership changes.
