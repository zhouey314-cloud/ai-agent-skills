---
name: failure-analyzer
description: Diagnose reproducible failures from logs and state evidence, separating observed facts from hypotheses.
---

# Failure Analyzer

## Purpose

Choose the smallest informative next experiment, not a speculative rewrite.

## When to Use

Use when a test, deployment, retrieval or workflow step fails and evidence is available.

## Inputs

`expected`, `observed`, `logs`, `reproduction_steps`, `recent_changes`.

## Outputs

`symptom`, `likely_causes[]`, `evidence[]`, `unknowns[]`, `next_experiment`, `regression_case`.

## Workflow

1. Reproduce the failure and capture exact command, version, environment and symptom.
2. Separate observed facts from possible causes.
3. Rank hypotheses by evidence and choose one discriminating read-only or reversible experiment.
4. Run the smallest test, update the diagnosis and preserve failures as regression cases.
5. Only then propose a fix and re-run the original failing path.

## Failure Handling

If the failure cannot be reproduced, mark cause `UNKNOWN` and specify missing observation. Do not edit baselines to manufacture a pass.

## Example

`synthetic_unverified`: retrieval returns zero matching chunks; inspect chunking and access filters before prompts.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

Logs may omit the causal event; do not claim certainty from correlation alone.
