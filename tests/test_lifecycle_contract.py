from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class LifecycleContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lifecycle = json.loads(
            (ROOT / "contracts/lifecycle/lifecycle-v1.json").read_text(encoding="utf-8")
        )

    def test_states_are_unique_and_complete(self) -> None:
        states = self.lifecycle["states"]
        self.assertEqual(len(states), len(set(states)))
        self.assertEqual(self.lifecycle["initial_state"], "REQUESTED")
        self.assertEqual(self.lifecycle["terminal_states"], ["DESTROYED"])
        for required in {"QUARANTINED", "RECOVERING", "FAILED", "DEGRADED"}:
            self.assertIn(required, states)

    def test_every_transition_uses_declared_states(self) -> None:
        states = set(self.lifecycle["states"])
        pairs: set[tuple[str, str]] = set()
        for transition in self.lifecycle["transitions"]:
            self.assertIn(transition["from"], states)
            self.assertIn(transition["to"], states)
            key = (transition["from"], transition["command"])
            self.assertNotIn(key, pairs, f"nondeterministic transition: {key}")
            pairs.add(key)

    def test_destroyed_has_no_outgoing_transition(self) -> None:
        outgoing = [t for t in self.lifecycle["transitions"] if t["from"] == "DESTROYED"]
        self.assertEqual(outgoing, [])

    def test_quarantine_is_not_suspension(self) -> None:
        quarantine_targets = {
            t["to"] for t in self.lifecycle["transitions"] if t["command"] == "quarantine"
        }
        self.assertEqual(quarantine_targets, {"QUARANTINED"})


if __name__ == "__main__":
    unittest.main()
