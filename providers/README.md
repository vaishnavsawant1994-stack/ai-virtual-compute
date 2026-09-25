# Providers

Provider implementations conform to the normalized `ComputeProvider` contract and remain subordinate to control-plane policy, lifecycle, lease, budget, and emergency authority.

Stage 1 starts with `fake/`. Real sandbox, Linux, Windows, Android, Apple, and GPU providers are stage-gated and must not be represented as implemented before qualification.
