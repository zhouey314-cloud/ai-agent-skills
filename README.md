# Portable Agent Skills

Ten self-contained, clean-room skills for Codex, Claude Code and compatible agents. They encode generic work patterns from independently written material; no company GEO prompts, customer knowledge, internal fields or proprietary workflows are included.

![Skill map](docs/images/architecture.svg)

## Use

Copy an individual `skills/<name>/SKILL.md` into your agent's skill directory or reference it from an `AGENTS.md` / `CLAUDE.md`. Read its input and output schemas before running. Examples are fictional and marked `synthetic_unverified`. Skills do not supply credentials or grant tool permissions.

## Collection

`requirement-clarifier`, `faq-builder`, `evidence-content`, `content-qa`, `eval-engineering-lite`, `meeting-to-actions`, `research-synthesizer`, `workflow-planner`, `failure-analyzer`, `project-handoff`.

## Verification, limitations and license

`python3 tests/validate.py` checks all ten skill contracts and examples. It is a structural check, not an eval of model behavior. Real use requires human review, especially for external communication and business claims. MIT.
