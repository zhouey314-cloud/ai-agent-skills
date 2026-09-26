---
name: eval-engineering-lite
description: Set up a small repeatable AI evaluation with baseline, provenance and a release decision; use when model or retrieval behavior changes.
---

# Eval Engineering Lite

## Purpose

Separate deterministic test health from probabilistic model quality.

## When to Use

Use when changing prompts, RAG, agents, model configuration or semantic decisions.

## Inputs

`journey`, `risk_level`, `cases: [{id,input,expected,ground_truth_status}]`, `baseline`, optional `traces[]`.

## Outputs

`rubric`, `case_results`, `regressions`, `failure_taxonomy`, `release_gate`.

## Workflow

1. Define success, must-not-happen conditions and critical cases before editing behavior.
2. Preserve the baseline run and case provenance; synthetic cases remain `synthetic_unverified`.
3. Run deterministic schema/rule checks first, then real provider output only if configured.
4. Compare candidate versus baseline on the same cases, including high-risk failures and traces.
5. Classify failures and mark the release `PASS`, `FAIL` or `BLOCKED` with evidence.

## Failure Handling

An unavailable model, missing independent ground truth or failed judge is `BLOCKED`/`NOT_RUN`, never PASS. Do not lower a rubric or erase a hard case to improve a score.

## Example

`synthetic_unverified`: two fictional RAG cases validate fixture shape; without a provider, report `MODEL_QUALITY=NOT_RUN`.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

This lite skill is not a full production eval platform; human-reviewed Golden Sets and domain owners are required for high-risk claims.
