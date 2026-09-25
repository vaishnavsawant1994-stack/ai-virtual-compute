# Threat Model and Trust Boundaries

## Protected assets

- host and hypervisor integrity;
- tenant and client isolation;
- platform identity, policy, and approval authority;
- leases, budgets, quotas, and lifecycle truth;
- credentials and private network access;
- images, snapshots, volumes, exported artifacts, and audit evidence;
- provider availability and paid-resource spend.

## Threat actors

- malicious or compromised client;
- prompt-injected or malfunctioning agent;
- hostile workload inside a guest;
- compromised image, provider, host, or dependency;
- cross-tenant attacker;
- authorized user exceeding intended authority;
- external attacker exploiting an API or control channel.

## Trust boundaries

| Boundary | Crossing data | Required controls |
|---|---|---|
| Client -> API | identity token, request, idempotency key | authentication, schema validation, rate limit, request correlation |
| API -> Policy | verified context, target, action | canonical context only; deny on ambiguity; decision audit |
| Policy -> Resolver/Scheduler | bounded allow/approval result | decision binding, expiry, quota and budget reservation |
| Control plane -> Provider | normalized operation | mutual authentication, allowlisted operation, timeout, idempotency |
| Provider -> Guest | boot/control/storage/network | isolation outside guest, resource limits, measured image |
| Guest -> Network | packets/DNS | profile enforcement, deny private/platform ranges, egress logging |
| Guest -> Storage | mounts/import/export | ownership, malware/content policy, path isolation, audit |
| Control plane -> Credential broker | credential request | scoped authorization, short TTL, target binding, revocation |
| Human takeover -> Session | control-mode change | strong authentication, priority arbitration, audit |
| Tenant -> Tenant | shared infrastructure | namespace, row, storage, network, cache, snapshot isolation |

## Principal threats and mitigations

| Threat | Required mitigation |
|---|---|
| Client forges owner/admin context | derive authority only from authenticated server-side context |
| Client assigns lifecycle state | accept commands, never arbitrary state; validate transition table |
| Lease replay or use after expiry | audience/device/session binding, short expiry, revocation check |
| Cross-tenant IDOR | authority-aware lookup; never fetch by opaque ID before tenant constraint |
| Guest escapes or reaches host/LAN | provider isolation, network deny rules, host hardening, sandbox qualification |
| Agent raises budget/quota | separate administrative permission and immutable beneficiary boundary |
| Snapshot leaks credentials | snapshot policy, credential non-persistence, scan and ownership checks |
| Ephemeral resource becomes persistent | promotion workflow, inspection, approval, immutable snapshot/image |
| Provider lies about capability/health | registry admission, attestation where possible, active health probes |
| Race creates duplicate/ghost resource | idempotency keys, reservations, compare-and-swap/transactions, reconciliation |
| Emergency stop is ignored | control-plane enforcement, lease/credential revocation, provider isolation |
| Audit disabled or rewritten | append-only store, integrity chaining/signing, separated permission |

## Assumptions requiring later proof

- Provider isolation mechanisms are stage-specific and unproven at Stage 0.
- Secure wipe semantics vary by storage provider and must be qualified.
- Apple, Windows, GPU, and cloud providers depend on licensing and suitable infrastructure.
- Physical-device providers are future extensions and are not a V1 implementation commitment.
