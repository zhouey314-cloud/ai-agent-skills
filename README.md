# Portable Agent Skills

**Reusable, inspectable AI work patterns — from an ambiguous request to evidence, review and handoff.**

[![CI](https://github.com/zhouey314-cloud/ai-agent-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/zhouey314-cloud/ai-agent-skills/actions/workflows/ci.yml)

![Architecture of the ten-skill collection](docs/images/architecture.svg)

**Status:** `LOCAL_RUNNABLE` contract kit. Ten independent, clean-room skills with copyable installation and offline structural checks. Examples are fictional and `synthetic_unverified`; no provider-backed model-quality result or customer adoption is claimed.

[Case study](docs/case-study.md) · [Synthetic walkthroughs](examples/README.md) · [Contribute](CONTRIBUTING.md)

## 30-second overview

| Need | Start with | Output |
|---|---|---|
| Scope a vague request | [requirement-clarifier](skills/requirement-clarifier/SKILL.md) | Acceptance checks and open decisions |
| Write only supported claims | [evidence-content](skills/evidence-content/SKILL.md) + [content-qa](skills/content-qa/SKILL.md) | Draft, source map and release findings |
| Design a gated process | [workflow-planner](skills/workflow-planner/SKILL.md) | States, approvals, retries and failure paths |
| Evaluate changed AI behavior | [eval-engineering-lite](skills/eval-engineering-lite/SKILL.md) | Baseline, cases and release decision |

Each skill includes purpose, trigger, inputs, outputs, workflow, failure handling, a synthetic example, test scope and limitations. Skills are prompts/workflows, not a privileged executable service: reading a skill does not grant credentials, tool access or permission to publish.

## Quick start

Requirements: Python 3.10+ for validation; no package install, API key or provider is needed to read/use the skills.

```bash
git clone https://github.com/zhouey314-cloud/ai-agent-skills.git
cd ai-agent-skills
python3 tests/validate.py
python3 evals/run.py
```

Expected local evidence: `SKILL_CONTRACT_PASS count=10 model_quality=NOT_RUN` and `FIXTURE_SCHEMA_PASS`. These validate structure and case provenance, **not** the quality of a model's answers.

To try one skill, ask your agent to read `skills/requirement-clarifier/SKILL.md` and provide an ambiguous request with its known constraints. Inspect the returned acceptance criteria and open decisions yourself before acting on them. See [three synthetic walkthroughs](examples/README.md).

## Install one skill

Copy one directory, not the whole collection, into an agent's skill root. Review the file before installation and choose a non-colliding name. For Codex:

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skills/requirement-clarifier "$HOME/.codex/skills/requirement-clarifier"
```

For Claude Code, replace `$HOME/.codex/skills` with `$HOME/.claude/skills`. Alternatively, reference a `SKILL.md` directly from an `AGENTS.md` or `CLAUDE.md`; the host determines how and when it invokes it. There is no automatic installer or guaranteed cross-host trigger behavior.

## Collection

- **Define:** [requirement-clarifier](skills/requirement-clarifier/SKILL.md), [workflow-planner](skills/workflow-planner/SKILL.md)
- **Use evidence:** [faq-builder](skills/faq-builder/SKILL.md), [research-synthesizer](skills/research-synthesizer/SKILL.md), [evidence-content](skills/evidence-content/SKILL.md), [content-qa](skills/content-qa/SKILL.md)
- **Evaluate/repair:** [eval-engineering-lite](skills/eval-engineering-lite/SKILL.md), [failure-analyzer](skills/failure-analyzer/SKILL.md)
- **Hand off:** [meeting-to-actions](skills/meeting-to-actions/SKILL.md), [project-handoff](skills/project-handoff/SKILL.md)

The ten workflows are deliberately small; they do not claim to cover every RAG, CRM, video or publishing task. Add a new skill only when a distinct, tested workflow is needed.

## Architecture and design decisions

```text
User-provided task and authorized sources
  → single-purpose SKILL.md (input/output contract + failure path)
  → agent draft / analysis
  → deterministic contract checks where possible
  → human review for business truth, privacy and external actions
```

The skill files are portable Markdown with YAML frontmatter. The offline validator is independent of any model or agent host. A separate [eval specification](evals/PROJECT_EVAL_SPEC.md) records what remains unmeasured. This keeps copy/install simple and makes failures visible instead of treating fluent text as proof.

## Tests / Eval

- `python3 tests/validate.py`: checks ten skill files have nonempty contracts, multiple workflow steps and explicit example/test boundaries.
- `python3 evals/run.py`: checks synthetic case IDs, provenance and constraints. It does not call a model.
- GitHub Actions runs both commands on push/PR.

**Baseline before V2:** ten files passed the old four-heading check. **V2 gate:** expanded structural checks and synthetic case validation must pass; human-reviewed provider performance remains `NOT_RUN`. See [eval spec](evals/PROJECT_EVAL_SPEC.md) for acceptance and blocked evidence.

## Security, privacy and evidence boundary

These skills contain no company GEO prompts, customer knowledge, private voices, internal fields or proprietary workflows. Never paste a credential, private document or unapproved third-party material into a public example. Skills should ask for a human decision when ownership or high-impact communication is unresolved. `synthetic_unverified` means an example illustrates the contract only.

## Contribute / roadmap

See [CONTRIBUTING.md](CONTRIBUTING.md) for the skill contract, example provenance, tests and PR checklist; [CHANGELOG.md](CHANGELOG.md) tracks changes. The next meaningful step is independent human review of real outputs for a small opt-in task set, then regression cases for observed failures—not adding empty skill directories.

MIT licensed; see [LICENSE](LICENSE). [Ethan Zhou's portfolio](https://zhouey314-cloud.github.io/projects.html).
