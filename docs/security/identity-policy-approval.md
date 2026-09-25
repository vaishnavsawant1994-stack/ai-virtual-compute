# Identity, Permission, and Approval Model

## Identity

Every request resolves an authenticated `client` and effective `principal` within a tenant/security context. Supported principal kinds are human, AI system, agent, service, application, and automation.

The API does not accept caller-supplied canonical principal, tenant, owner, administrator, or approval identities.

## Authorization decision input

- authenticated principal/client and tenant;
- requested action and canonical resource;
- requested capabilities and duration;
- resource ownership and classification metadata;
- current lease/session/device state;
- network, credential, quota, budget, and emergency context;
- authoritative approval records.

## Decision result

`ALLOW`, `DENY`, or `REQUIRE_APPROVAL`, plus bounded capabilities, constraints, reason codes, policy version, decision ID, and expiry. Downstream components consume the bound decision; they do not reinterpret a UI boolean such as `approved=true`.

## Approval binding

Approvals bind approving actor, requester, action, target, risk scope, constraints, issue time, expiry, and policy version. They are single-use where the action requires it and cannot be replayed for a different resource or stronger capability.

## Administrative separation

Agents benefiting from a lease, quota, or budget cannot grant or raise it. Emergency-stop release and persistent-state promotion require distinct administrative authority.
