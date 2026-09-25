# Emergency Stop Model

## Scopes

- platform;
- tenant;
- client/principal;
- provider/host;
- device/session.

## Activation order

1. Persist an authoritative stop decision and audit correlation.
2. Block matching new provisioning and session creation.
3. Revoke matching active leases.
4. Revoke matching temporary credentials and control channels.
5. Isolate networking according to stop policy.
6. Freeze, suspend, quarantine, or destroy resources according to evidence-preservation policy.
7. Reconcile provider outcomes and record exceptions.

## Recovery

Emergency-stop release is a separate authorized action. It never silently restores old leases or temporary credentials. Resources are re-evaluated before resumption.
