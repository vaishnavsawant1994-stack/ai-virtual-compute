# Security Policy

## Security boundary

The control plane, policy engine, lease authority, credential broker, provider isolation, network enforcement, and audit recorder are security boundaries. Models, agents, clients, user interfaces, and guest operating systems are not.

## Never-supported authority

An ordinary client or agent must never receive:

- hypervisor or host root access;
- unrestricted platform database or secret-store access;
- access to another tenant's resources;
- authority to disable audit or emergency controls;
- authority to raise its own permissions, quota, or budget;
- authority to bypass policy, approval, lifecycle, or lease expiry.

## Reporting

Do not disclose suspected vulnerabilities in a public issue. Use GitHub's private vulnerability-reporting feature when enabled, or contact the repository owner privately.

## Current maturity

The project is pre-production. Stage-0 contracts are not evidence that a provider is secure. No real workload should be entrusted to this repository until the applicable provider and Stage 12 have been qualified.
