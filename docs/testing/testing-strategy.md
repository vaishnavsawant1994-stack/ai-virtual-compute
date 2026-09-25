# Testing and Qualification Strategy

## Test layers

- **Contract:** JSON syntax, schema metadata, examples, enums, compatibility.
- **Unit:** domain invariants, transition table, resolver ranking, policy decisions.
- **Integration:** API-control-plane-provider flow using FakeDeviceProvider.
- **Security:** IDOR, forged authority, lease replay/expiry, quota/budget bypass, injection.
- **Adversarial:** races, retries, resource exhaustion, malformed provider behavior.
- **Failure:** timeouts, unknown outcomes, host/provider/storage/network failures, recovery.
- **End-to-end:** authorized capability request through cleanup and audit evidence.
- **Stage-0 hostile contracts:** exceptional-state reachability, non-stranding failure paths, lifetime separation, tenant binding, authority context, audit minimums, and provider-detail non-leakage.

## Stage qualification

Every closure report records repository, branch, exact commit, changed files, commands, pass/fail counts, security findings, known limitations, and remaining risks. Exact-head CI evidence is required after local qualification.

## FakeDeviceProvider role

Stage 1 begins with a deterministic fake provider capable of injected delay, failure, stale state, partial success, and unknown outcomes. It exists to test control-plane correctness, not to simulate provider security.
