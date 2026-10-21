"""Validate synthetic fixture contracts. Does not invoke or score an AI model."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATASET = Path(__file__).with_name("cases.jsonl")
REQUIRED = {"id", "skill", "input", "must_include", "ground_truth_status", "source"}


def require(condition, message) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    cases = [json.loads(line) for line in DATASET.read_text(encoding="utf-8").splitlines() if line.strip()]
    require(cases, "empty case set")
    seen = set()
    for case in cases:
        require(REQUIRED <= case.keys(), f"missing fields in {case.get('id', '<no id')}")
        require(case["id"] not in seen, f"duplicate case: {case['id']}")
        seen.add(case["id"])
        require((ROOT / "skills" / case["skill"] / "SKILL.md").is_file(), case["skill"])
        require(case["ground_truth_status"] == "synthetic_unverified", case["id"])
        require(case["source"] == "fictional_example", case["id"])
        require(isinstance(case["must_include"], list) and case["must_include"], case["id"])
    print(f"FIXTURE_SCHEMA_PASS cases={len(cases)} provenance=synthetic_unverified")
    print("MODEL_QUALITY=NOT_RUN provider=offline")


if __name__ == "__main__":
    main()
