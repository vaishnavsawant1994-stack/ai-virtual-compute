# Versioned Contracts

Stage-0 public contracts are JSON Schema draft 2020-12 documents.

- `device-api/` — separate device, session, lease, snapshot, and emergency-stop resources and requests.
- `capabilities/` — normalized capability/resource requests.
- `lifecycle/` — authoritative states and transition data.
- `events/` — structured audit/operation events.
- `errors/` — stable public error taxonomy.
- `provider/` — internal normalized provider-operation envelope.

Breaking changes require a new contract version. Provider-specific identifiers and secrets must not appear in public device representations.
