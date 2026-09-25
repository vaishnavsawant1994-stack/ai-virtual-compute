#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    failures: list[str] = []

    for path in sorted((ROOT / "contracts").rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{path.relative_to(ROOT)}: {exc}")

    tests = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"],
        cwd=ROOT,
        check=False,
    )
    if tests.returncode:
        failures.append("unit/contract suite failed")

    if failures:
        print("STAGE-0 QUALIFICATION: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    contract_count = len(list((ROOT / "contracts").rglob("*.json")))
    print(f"STAGE-0 QUALIFICATION: PASS ({contract_count} JSON contract documents)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
