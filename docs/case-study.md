# Case Study — Portable Agent Skills

## Problem
Agent workflows are often shared as isolated prompts with no stated inputs, outputs, failure path or evidence boundary, making them hard for another developer to reuse safely.

## Context
This is a self-built clean-room collection of ten small, portable Skill files. It does not include company prompts, customer sources or production adoption data.

## Constraints
No provider credential or agent host is required for the repository's offline checks. A Skill file cannot grant tool permission or prove model quality by itself.

## My Role
Structured the ten public workflows, their contracts and examples; added a repeatable validator, synthetic fixture checks and contribution process.

## Architecture
Each `skills/<name>/SKILL.md` is a standalone Markdown contract with YAML frontmatter. `tests/validate.py` checks structure; `evals/run.py` validates case provenance. Examples are separate from measured model results.

## Key Decisions
Keep each skill single-purpose and fail closed on missing sources, owner decisions or external publishing authority. Mark all fictional examples `synthetic_unverified`.

## Hardest Problem
Avoiding the appearance of rigor from ten uniform files: contract consistency is useful, but it is not evidence that a model follows them in real work.

## Failure/Tradeoff
Portable Markdown is easy to copy, but trigger behavior varies by host and requires human judgment. Provider-backed evaluation and independent ground truth are still missing.

## Testing
Run `python3 tests/validate.py` and `python3 evals/run.py`. Both run without a provider and are included in CI.

## Eval
Baseline before V2: ten skills passed a four-heading structural check. Current fixtures cover three fictional failure scenarios. `MODEL_QUALITY=NOT_RUN`; no pass rate or user outcome is claimed.

## Current Evidence
The repository includes ten nonempty Skill contracts, three synthetic walkthroughs, installation steps, contribution instructions and deterministic CI checks.

## Limitations
No measured agent performance, cross-host trigger guarantee, customer adoption or production use. A human must verify important factual claims and external actions.

## What I Would Do in Production
Gather opted-in user tasks and independently approved expected constraints, run the same cases with a configured provider, capture traces and regressions, and stop on critical privacy or unsupported-claim failures.

## What I Learned
Making failure and provenance explicit is a prerequisite to reusable Skill design, but measured behavior must remain a separate gate.
