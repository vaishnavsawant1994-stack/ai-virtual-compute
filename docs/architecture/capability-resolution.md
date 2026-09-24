# Capability Resolution and Scheduling

Capabilities are authoritative; device classes are extensible selection hints.

## Resolution order

The resolver prefers the smallest safe eligible environment, normally:

1. lightweight command execution;
2. browser workspace;
3. container;
4. high-isolation sandbox;
5. full virtual machine/desktop;
6. virtual mobile device;
7. specialized GPU/cloud resource.

An earlier class is not selected unless it satisfies every required capability and policy constraint.

## Eligibility filters

- policy and tenant allowlist;
- required capability and version;
- persistence, TTL, image, architecture, and OS constraints;
- network and credential profile compatibility;
- provider and host health;
- quota, rate, budget, and cost constraints;
- isolation/risk class;
- available reservable capacity.

## Scheduling guarantees

Capacity is reserved atomically before allocation. Failed/expired reservations are reclaimed. The scheduler refuses new work when health or storage pressure makes a safe allocation uncertain. Cost optimization never outranks isolation or policy.
