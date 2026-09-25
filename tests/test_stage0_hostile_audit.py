from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts"


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class HostileStage0AuditTests(unittest.TestCase):
    def test_exceptional_lifecycle_states_are_reachable_from_normal_operation(self) -> None:
        lifecycle = load("contracts/lifecycle/lifecycle-v1.json")
        normal = {
            "REQUESTED", "POLICY_CHECK", "RESOLVING", "ALLOCATING", "BOOTING",
            "READY", "ACTIVE", "IDLE", "SUSPENDING", "SUSPENDED",
        }
        transitions = lifecycle["transitions"]
        for exceptional in {"FAILED", "DEGRADED", "QUARANTINED"}:
            with self.subTest(exceptional=exceptional):
                self.assertTrue(
                    any(t["from"] in normal and t["to"] == exceptional for t in transitions),
                    f"{exceptional} is declared but unreachable from normal operation",
                )

    def test_denial_failure_and_emergency_cleanup_cannot_strand_resources(self) -> None:
        lifecycle = load("contracts/lifecycle/lifecycle-v1.json")
        transitions = {(t["from"], t["command"]): t["to"] for t in lifecycle["transitions"]}
        required = {
            ("REQUESTED", "cancel"): "DESTROYING",
            ("POLICY_CHECK", "policy_denied"): "DESTROYING",
            ("RESOLVING", "resolution_failed"): "FAILED",
            ("ALLOCATING", "allocation_failed"): "FAILED",
            ("BOOTING", "boot_failed"): "FAILED",
            ("ALLOCATING", "destroy"): "DESTROYING",
            ("BOOTING", "destroy"): "DESTROYING",
            ("SUSPENDING", "destroy"): "DESTROYING",
            ("DEGRADED", "destroy"): "DESTROYING",
            ("RECOVERING", "destroy"): "DESTROYING",
        }
        for key, target in required.items():
            with self.subTest(transition=key):
                self.assertEqual(transitions.get(key), target)

    def test_device_contract_preserves_device_session_lease_separation(self) -> None:
        device = load("contracts/device-api/device-v1.schema.json")
        self.assertNotIn("session_id", device["properties"])
        self.assertNotIn("lease_id", device["properties"])

    def test_ephemeral_device_representation_requires_lifecycle_expiry(self) -> None:
        device = load("contracts/device-api/device-v1.schema.json")
        rules = device.get("allOf", [])
        self.assertTrue(
            any(
                rule.get("if", {}).get("properties", {}).get("persistence", {}).get("const")
                == "ephemeral"
                and "lifecycle_expires_at" in rule.get("then", {}).get("required", [])
                for rule in rules
            )
        )

    def test_lease_and_session_are_tenant_bound_and_lease_has_explicit_state(self) -> None:
        lease = load("contracts/device-api/lease-v1.schema.json")
        session = load("contracts/device-api/session-v1.schema.json")
        self.assertTrue({"tenant_id", "state"}.issubset(lease["required"]))
        self.assertIn("expired", lease["properties"]["state"]["enum"])
        self.assertTrue({"tenant_id", "principal_id", "client_id", "device_id"}.issubset(session["required"]))

    def test_snapshot_is_tenant_and_owner_bound(self) -> None:
        snapshot = load("contracts/device-api/snapshot-v1.schema.json")
        self.assertTrue(
            {"tenant_id", "device_id", "owner_principal_id", "retention_expires_at"}.issubset(
                snapshot["required"]
            )
        )

    def test_audit_event_contract_matches_normative_minimum(self) -> None:
        event = load("contracts/events/event-v1.schema.json")
        required = set(event["required"])
        self.assertTrue(
            {"schema_version", "tenant_id", "sequence", "request_id", "target"}.issubset(required)
        )
        self.assertIn("policy_decision_id", event["properties"])

    def test_emergency_stop_has_versioned_scope_and_release_contract(self) -> None:
        emergency = load("contracts/device-api/emergency-stop-v1.schema.json")
        self.assertTrue(
            {
                "emergency_stop_id", "scope", "reason", "activated_at",
                "activated_by_principal_id", "state",
            }.issubset(
                emergency["required"]
            )
        )
        self.assertIn("released", emergency["properties"]["state"]["enum"])
        self.assertTrue(
            any("released_at" in rule.get("then", {}).get("required", []) for rule in emergency["allOf"])
        )

    def test_provider_mutations_require_control_plane_authority_context(self) -> None:
        provider = load("contracts/provider/provider-v1.schema.json")
        rules = provider.get("allOf", [])
        self.assertTrue(
            any("authority_context" in rule.get("then", {}).get("required", []) for rule in rules)
        )

    def test_lifetime_contract_explicitly_separates_devices_and_leases(self) -> None:
        cleanup = (ROOT / "docs/operations/cleanup-retention.md").read_text(encoding="utf-8")
        self.assertIn("Lease expiry does not destroy a persistent device", cleanup)
        self.assertIn("device lifecycle expiry", cleanup)

    def test_user_selected_authority_invariants_are_normative(self) -> None:
        invariants = (ROOT / "docs/security/security-invariants.md").read_text(encoding="utf-8")
        self.assertIn("Client/model-provided purpose", invariants)
        self.assertIn("cannot raise its own permission", invariants)
        self.assertIn("Emergency stop is independent", invariants)
        self.assertIn("No cross-tenant lookup", invariants)

    def test_all_authority_bearing_public_resources_are_tenant_bound(self) -> None:
        for relative in [
            "contracts/device-api/device-v1.schema.json",
            "contracts/device-api/session-v1.schema.json",
            "contracts/device-api/lease-v1.schema.json",
            "contracts/device-api/snapshot-v1.schema.json",
            "contracts/events/event-v1.schema.json",
        ]:
            with self.subTest(contract=relative):
                schema = load(relative)
                self.assertIn("tenant_id", schema["required"])
                self.assertIn("tenant_id", schema["properties"])


if __name__ == "__main__":
    unittest.main()
