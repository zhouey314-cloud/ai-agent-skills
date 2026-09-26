"""Offline structural validation for portable skills; not a model-quality eval."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED = [
    "Purpose", "When to Use", "Inputs", "Outputs", "Workflow",
    "Failure Handling", "Example", "Tests", "Limitations",
]


def validate_skill(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path}: missing YAML frontmatter"
    frontmatter = text.split("---", 2)[1]
    assert re.search(r"(?m)^name: " + re.escape(path.parent.name) + r"$", frontmatter), path
    match = re.search(r"(?m)^description: (.+)$", frontmatter)
    assert match and len(match.group(1)) >= 40, f"{path}: description too short"
    for heading in REQUIRED:
        section = re.search(
            rf"(?ms)^## {re.escape(heading)}\n\n(.+?)(?=^## |\Z)", text
        )
        assert section and section.group(1).strip(), f"{path}: empty {heading}"
    assert "synthetic_unverified" in text, f"{path}: example provenance absent"
    assert "not model-quality evidence" in text, f"{path}: test boundary absent"
    steps = re.findall(r"(?m)^\d+\. ", text)
    assert len(steps) >= 3, f"{path}: workflow too thin"


def main() -> None:
    paths = sorted(SKILLS.glob("*/SKILL.md"))
    assert paths, "No skills found"
    assert len(paths) == 10, f"Unexpected skill count: {len(paths)}"
    for path in paths:
        validate_skill(path)
    print(f"SKILL_CONTRACT_PASS count={len(paths)} model_quality=NOT_RUN")


if __name__ == "__main__":
    main()
