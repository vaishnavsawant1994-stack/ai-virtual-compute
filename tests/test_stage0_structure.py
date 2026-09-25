from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Stage0StructureTests(unittest.TestCase):
    def test_required_documents_exist_and_are_nonempty(self) -> None:
        required = [
            "README.md",
            "SECURITY.md",
            "docs/architecture/product-requirements.md",
            "docs/architecture/system-architecture.md",
            "docs/architecture/domain-model.md",
            "docs/architecture/persistence-model.md",
            "docs/security/threat-model.md",
            "docs/security/security-invariants.md",
            "docs/security/identity-policy-approval.md",
            "docs/providers/provider-contract.md",
            "docs/api/api-v1.md",
            "docs/testing/testing-strategy.md",
            "docs/stages/stage-0-closure.md",
        ]
        for relative in required:
            with self.subTest(path=relative):
                path = ROOT / relative
                self.assertTrue(path.is_file())
                self.assertGreater(len(path.read_text(encoding="utf-8").strip()), 100)

    def test_personal_ai_is_only_a_future_client(self) -> None:
        architecture = (ROOT / "docs/architecture/system-architecture.md").read_text(
            encoding="utf-8"
        )
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("future API client", readme)
        self.assertNotIn("PersonalAIAgent", architecture)
        self.assertNotIn("JarvisOwner", architecture)


if __name__ == "__main__":
    unittest.main()
