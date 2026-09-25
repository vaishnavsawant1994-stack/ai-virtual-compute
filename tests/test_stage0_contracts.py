from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts"


class Stage0ContractTests(unittest.TestCase):
    def test_all_json_documents_parse(self) -> None:
        documents = sorted(CONTRACTS.rglob("*.json"))
        self.assertGreaterEqual(len(documents), 8)
        for path in documents:
            with self.subTest(path=path.relative_to(ROOT)):
                json.loads(path.read_text(encoding="utf-8"))

    def test_schemas_have_versioned_identity(self) -> None:
        schemas = sorted(CONTRACTS.rglob("*.schema.json"))
        self.assertGreaterEqual(len(schemas), 7)
        for path in schemas:
            with self.subTest(path=path.relative_to(ROOT)):
                schema = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
                self.assertIn("v1", schema["$id"])
                self.assertTrue(schema["title"])
                self.assertEqual(schema["type"], "object")

    def test_ephemeral_capability_request_requires_ttl(self) -> None:
        schema = json.loads(
            (CONTRACTS / "capabilities/capability-v1.schema.json").read_text(encoding="utf-8")
        )
        rule = schema["allOf"][0]
        self.assertEqual(rule["if"]["properties"]["persistence"]["const"], "ephemeral")
        self.assertIn("ttl_seconds", rule["then"]["required"])

    def test_lease_is_bounded_to_actor_device_and_session(self) -> None:
        schema = json.loads(
            (CONTRACTS / "device-api/lease-v1.schema.json").read_text(encoding="utf-8")
        )
        required = set(schema["required"])
        self.assertTrue(
            {
                "tenant_id", "principal_id", "client_id", "device_id", "session_id",
                "capabilities", "issued_at", "expires_at", "state", "policy_context_id",
            }.issubset(required)
        )
        self.assertEqual(
            set(schema["properties"]["state"]["enum"]),
            {"issued", "active", "expired", "revoked"},
        )

    def test_public_device_contract_does_not_leak_provider_identifiers(self) -> None:
        schema = json.loads(
            (CONTRACTS / "device-api/device-v1.schema.json").read_text(encoding="utf-8")
        )
        forbidden = {"provider_id", "provider_resource_id", "host_id", "hypervisor_id"}
        self.assertTrue(forbidden.isdisjoint(schema["properties"]))


if __name__ == "__main__":
    unittest.main()
