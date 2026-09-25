# Runtime Boundary

Stage 1 will implement the trusted control-plane modules under this directory: domain, identity, policy, resolver, scheduler, sessions, leases, devices, storage, networking, credentials, audit, health, and recovery.

Runtime modules own canonical state and security decisions. Provider adapters and clients cannot mutate that authority directly.
