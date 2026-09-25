# Security Invariants

These invariants are normative. A provider or feature that cannot preserve them is ineligible.

1. **Authentication is not authorization.** A valid identity never implies permission for an operation.
2. **Model output is never authority.** Owner/admin/approval state originates only from canonical server-side context.
3. **Deny by default.** Missing or contradictory authority, policy, capability, or lifecycle evidence denies the operation.
4. **Lifecycle is runtime-owned.** Clients request commands; only the lifecycle manager commits validated transitions.
5. **Every control operation requires a current lease.** Lease expiry/revocation is enforced independently of client cooperation.
6. **Leases are bounded.** Every lease binds principal, client, device, session, capabilities, policy context, issue time, and expiry.
7. **Human authority wins.** Human takeover pauses or arbitrates competing AI input before accepting human control.
8. **Providers are not policy authorities.** Provider success cannot override a policy denial, budget limit, or emergency stop.
9. **Guests are untrusted.** Isolation, network, credentials, quotas, cleanup, and audit are enforced externally.
10. **No cross-tenant lookup.** All resource resolution is authority-aware at the data-access boundary.
11. **No self-escalation.** A principal cannot raise its own permission, approval, quota, budget, or lease ceiling.
12. **Credentials are scoped and temporary.** A guest never receives unrestricted vault access.
13. **Ephemeral means expiring.** Ephemeral devices require an expiry; cleanup revokes access before destruction.
14. **Persistent does not mean permanently accessible.** Persistent devices still require temporary leases.
15. **Promotion is a workflow.** Ephemeral state cannot become trusted/persistent by changing a mutable flag.
16. **Quarantine is isolating.** Quarantine revokes control/credentials and restricts networking while preserving authorized evidence.
17. **Emergency stop is independent.** It operates even when models, clients, guests, or providers are malfunctioning.
18. **Significant actions are attributable.** Audit records include actor, client, target, request, decision, time, correlation, and outcome.
19. **Retries are safe.** Provisioning and destructive operations use idempotency or explicit conflict semantics.
20. **Fail closed under pressure.** Capacity, storage, health, quota, budget, and policy uncertainty cannot produce unsafe allocation.
21. **Device lifetime is not lease lifetime.** Lease expiry revokes access; it does not destroy a persistent device. Ephemeral device lifecycle expiry initiates cleanup independently of lease state.
22. **Purpose is not authority.** Client/model-provided purpose, labels, hints, and metadata cannot grant permission, approval, quota, budget, or provider selection authority.
23. **Representations preserve separation.** Device resources do not embed a canonical current session or lease; sessions and leases are separately authorized resources.
