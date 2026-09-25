# Stage 0 Closure Checklist

Stage 0 remains **IN PROGRESS** until the closure candidate passes exact-head qualification.

- [x] Independent product boundary documented.
- [x] Product and non-functional requirements defined.
- [x] Layered architecture and authority ownership defined.
- [x] Domain, device, session, and lease separation defined.
- [x] Capability model and device classes defined.
- [x] Lifecycle and transition authority defined.
- [x] Provider interface defined.
- [x] Identity, permission, approval, quota, and budget boundaries defined.
- [x] Threat model and trust boundaries defined.
- [x] Security invariants defined.
- [x] Emergency-stop model defined.
- [x] Cleanup and retention model defined.
- [x] API, event, and error contracts defined.
- [x] Testing and qualification strategy defined.
- [x] Hostile Stage-0 architecture/contract audit completed and findings repaired locally.
- [x] Repaired contract tree qualified on public exact head `ad5e42bb5fe8f8a69f69e885c5a7b343f46b3458` (CI run #68).
- [x] Stage-0 pull request opened.
- [x] External-review unavailability recorded; owner-authorized hostile-audit substitution documented.
- [x] Stage-0 closure evidence committed in this closure candidate.
- [ ] This closure candidate is green on exact-head CI.

## Gate to Stage 1

Do not implement a real provider. Stage 1 may begin only after the open Stage-0 items are completed. Its first provider is `FakeDeviceProvider`.

See [Stage-0 closure evidence](stage-0-closure-evidence-20260925.md) for the exact evidence and review-substitution decision.
