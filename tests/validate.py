"""Offline structural validation for portable skills; not a model-quality eval."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED = [
    "Purpose", "When to Use", "Inputs", "Outputs", "Workflow",
    "Failure Handling", "Example", "Tests", "Limitations",
]


def require(condition, message) -> None:
    if not condition:
        raise ValueError(message)


def validate_skill(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    require(text.startswith("---\n"), f"{path}: missing YAML frontmatter")
    frontmatter = text.split("---", 2)[1]
    require(re.search(r"(?m)^name: " + re.escape(path.parent.name) + r"$", frontmatter), path)
    match = re.search(r"(?m)^description: (.+)$", frontmatter)
    require(match and len(match.group(1)) >= 40, f"{path}: description too short")
    for heading in REQUIRED:
        section = re.search(
            rf"(?ms)^## {re.escape(heading)}\n\n(.+?)(?=^## |\Z)", text
        )
        require(section and section.group(1).strip(), f"{path}: empty {heading}")
    require("synthetic_unverified" in text, f"{path}: example provenance absent")
    require("not model-quality evidence" in text, f"{path}: test boundary absent")
    steps = re.findall(r"(?m)^\d+\. ", text)
    require(len(steps) >= 3, f"{path}: workflow too thin")


def main() -> None:
    paths = sorted(SKILLS.glob("*/SKILL.md"))
    require(paths, "No skills found")
    require(len(paths) == 10, f"Unexpected skill count: {len(paths)}")
    for path in paths:
        validate_skill(path)
    print(f"SKILL_CONTRACT_PASS count={len(paths)} model_quality=NOT_RUN")


if __name__ == "__main__":
    main()
