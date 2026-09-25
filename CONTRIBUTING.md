# Contributing

## Change discipline

1. Identify the requirement and affected contract.
2. Document architectural conflicts before changing a frozen decision.
3. Repair root causes rather than weakening tests.
4. Add or update qualification evidence.
5. Run the full Stage-0 suite.
6. Review the exact diff and commit SHA.

## Boundaries

- Do not copy Personal AI code or add client-specific backdoors.
- Do not add a real provider before its stage is authorized.
- Do not expose provider implementation details in public API contracts unless necessary.
- Do not treat client assertions as authorization or lifecycle truth.
- Do not commit secrets, credentials, private keys, VM images, or customer data.

## Contract changes

Breaking public-contract changes require a new version or an explicit migration plan. Schemas must remain syntactically valid JSON and include `$schema`, `$id`, `title`, and `type`.
