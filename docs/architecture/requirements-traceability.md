# Requirements Traceability

| Requirement range | Normative source | Machine contract / future proof |
|---|---|---|
| FR-001-002 | product requirements; capability resolution | capability schema; Stage 3 tests |
| FR-003-006 | domain model; system architecture | device/lease/lifecycle schemas; Stages 1-2 |
| FR-007-010 | identity policy; audit model | event schema; Stages 1-2 |
| FR-011-014 | persistence model; cleanup | device schema; Stages 5-7 |
| FR-015-016 | threat model; security invariants | Stage 4/7 security tests |
| FR-017-020 | cleanup; emergency stop; threat model | lifecycle/event/error schemas; Stages 1-12 |
| FR-021-022 | system architecture; provider contract | API/provider schemas; Stages 1/10 |
| FR-023 | system architecture; cleanup and retention | device/lease schemas; hostile Stage-0 tests |
| FR-024 | identity policy; persistence model; audit model | device/session/lease/snapshot/event schemas |
| NFR-001-004 | security invariants; threat model | security/adversarial suites |
| NFR-005-008 | audit model; API/provider contracts; testing strategy | contract and exact-head qualification |
| NFR-009 | lifecycle contract; cleanup and emergency stop | hostile lifecycle reachability/cleanup tests |

Traceability is expanded to individual test IDs during each implementation stage. Missing evidence cannot be interpreted as a pass.
