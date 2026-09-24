# Audit Model

Audit is structured event evidence rather than continuous default screen recording.

## Minimum event fields

- event ID, type, schema version, time, sequence;
- principal, client, tenant, and optional session/lease;
- request and correlation IDs;
- target resource and action;
- policy/approval decision references;
- outcome and stable reason code;
- selected safe metadata, excluding secrets;
- integrity link/proof and recorder identity.

## Required event families

Resource request, policy and approval decision, allocation, boot, lifecycle transition, session, lease, control action, application install, important file transfer, credential request/use/revocation, network change, snapshot/restore, quarantine, suspension, destruction, emergency stop, and provider/host health.

## Integrity and privacy

Events are append-only through a dedicated authority. Integrity chaining/signing and external retention are production-stage requirements. Sensitive payloads are minimized, redacted, classified, access-controlled, and retained by policy. Audit access itself is audited.
