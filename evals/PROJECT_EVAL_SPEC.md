# Project Eval Spec

## Success contract

A developer can clone the repository, identify the right skill, read its input/output contract, run offline checks, and distinguish a structurally valid prompt from a model that actually performs the task. A skill must surface missing sources, unauthorized external actions and high-impact decisions for human review.

## Users and journeys

- A developer copies one skill into a compatible agent host.
- A user supplies authorized sources and receives a draft or analysis with traceable evidence.
- A reviewer inspects failure cases before publication or handoff.

## Critical failures

Invented customer results, fabricated citations, leaking private information, silent publishing, or treating synthetic examples as human-verified ground truth. The release gate for these is zero known critical failures; this threshold is provisional because no independent model run is included.

## Baseline before Portfolio V2

At `e507788`, `python3 tests/validate.py` reported `SKILL_CONTRACT_PASS count=10`. That was a four-heading structural check, not model behavior. There was no provider run, scored output, human-reviewed Golden Set, latency or cost measurement.

## Current checks

`python3 tests/validate.py` verifies structural contracts. `python3 evals/run.py` verifies case IDs, schema and provenance in `cases.jsonl`. Both are deterministic and must print `MODEL_QUALITY=NOT_RUN`. Cases are `synthetic_unverified`.

## Model-quality gate

`BLOCKED` until an opted-in user supplies or approves tasks, independent expected constraints and a permitted provider run. Save raw outputs and traces, review groundedness, instruction following, unsafe actions and unsupported claims, then compare to the baseline on the same cases. Never let the same model author cases, ground truth and final grade and call it verified.

## Failure taxonomy

Prompt, Retrieval, Knowledge, Tool Selection, Tool Failure, Workflow, Hallucination, Instruction Following, Business Rule, Formatting or Unknown. Add an observed failure to the regression set only after human verification.
