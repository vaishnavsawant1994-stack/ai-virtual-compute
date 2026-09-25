# Stage-0 Hostile Audit — 2026-09-25

Audited candidate: `0fd33166124dfd521d43b01934797302d75ba38d`  
Audited Git tree: `31edae6c440accbda7d43d18c721afb0d2425e89`  
Disposition: **candidate falsified; repaired local candidate qualified, publication pending**

## Method

The audit compared normative requirements, architecture, threat boundaries, security invariants, JSON contracts, lifecycle reachability, persistence semantics, provider authority, API separation, and existing qualification tests. Findings were converted into executable regression tests before repair.

## Confirmed findings

| ID | Severity | Finding | Repair |
|---|---|---|---|
| S0-A01 | High | `FAILED` and `DEGRADED` were declared but unreachable from ordinary failure/degradation paths. | Added deterministic failure/degradation transitions and reachability tests. |
| S0-A02 | High | Policy denial, cancellation, allocation/boot failure, and E-stop destruction could strand lifecycle states. | Added denial, cancel, failure, destroy, cleanup-failure, and quarantine transitions. |
| S0-A03 | High | Device response embedded one `session_id` and `lease_id`, weakening required entity separation. | Removed embedded IDs; added separate session and tenant-bound lease schemas. |
| S0-A04 | High | Ephemeral TTL was required on a request but not as a non-null lifecycle expiry on the device representation. | Added conditional `lifecycle_expires_at` requirement for ephemeral devices. |
| S0-A05 | High | Device-versus-lease lifetime semantics were descriptive but not explicit enough to prevent lease expiry destroying a persistent VM. | Added normative independent-clock rules and regression tests. |
| S0-A06 | High | Cross-tenant session/lease/snapshot isolation was not machine-represented completely. | Added tenant-bound device, session, lease, snapshot, and audit-event contracts. |
| S0-A07 | Medium | Event schema omitted fields declared mandatory by the normative audit model. | Added schema version, tenant, sequence, request, target, decision references, and integrity chain fields. |
| S0-A08 | High | Provider mutation envelope did not require bounded control-plane authority context. | Added tenant/device/policy binding and mandatory lease binding for connect/control. |
| S0-A09 | High | Emergency Stop had narrative semantics but no versioned resource contract. | Added scoped activation/release state contract; release never restores old leases. |
| S0-A10 | Medium | Existing 11 tests proved syntax/structure but did not falsify the above security invariants. | Added hostile Stage-0 regression suite and expanded qualification count. |

## Invariants re-attacked

- Model/client purpose and metadata remain non-authoritative.
- Providers cannot grant or broaden policy, leases, quota, budget, or lifecycle state.
- Persistent devices may survive multiple temporary leases.
- Ephemeral device lifecycle expiry initiates cleanup independently of lease state.
- IDs are never authorization; tenant scope applies before existence disclosure.
- Emergency Stop and cleanup do not depend on agent or guest cooperation.
- Personal AI remains an ordinary future client and its repository is untouched.

## Local repair qualification

- Full suite: **23/23 passed**.
- Contract parse/qualification: **PASS (12 JSON documents)**.
- Lifecycle graph: **51 deterministic transitions; all 16 states reachable**.
- Diff whitespace/error check: **PASS**.
- Draft 2020-12 meta-schema validation: **not run locally because the optional `jsonschema` package is unavailable**; CI does not currently claim this check.

## Closure status

Stage 0 remains **IN PROGRESS** until the repair candidate is published, passes exact-head CI, receives PR review against that exact head, and has closure evidence committed.
