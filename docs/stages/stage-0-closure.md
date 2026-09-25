# Stage 0 Closure Checklist

Stage 0 remains **IN PROGRESS** until every item is reviewed and exact-head qualification is green.

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
- [ ] Contract qualification green on exact pushed commit.
- [x] Stage-0 pull request opened.
- [ ] Stage-0 pull request reviewed against the repaired exact head.
- [ ] Stage-0 closure evidence committed.

## Gate to Stage 1

Do not implement a real provider. Stage 1 may begin only after the open Stage-0 items are completed. Its first provider is `FakeDeviceProvider`.
