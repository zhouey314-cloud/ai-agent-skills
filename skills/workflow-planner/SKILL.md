---
name: workflow-planner
description: Design stateful agent or human workflows with gates, retries and failure paths before implementation.
---

# Workflow Planner

## Purpose

Make workflow behavior inspectable before code or automation is deployed.

## When to Use

Use when a task spans multiple actors, tools, approvals or irreversible steps.

## Inputs

`goal`, `actors[]`, `inputs[]`, `external_systems[]`, `failure_risks[]`.

## Outputs

`states[]`, `transitions[]`, `human_gates[]`, `failure_states[]`, `verification[]`.

## Workflow

1. Identify the initial, success, rejection and blocked states.
2. Write every transition with actor, precondition, data change and idempotency rule.
3. Place a human gate before irreversible publication, payment or high-impact decisions.
4. Specify timeout, retry budget, compensation and escalation for external failures.
5. Check reachability and create one normal, one failure and one unauthorized-path test.

## Failure Handling

If a state has no safe recovery or ownership, flag it `UNRESOLVED` instead of hiding the gap. Never define auto-publish as a default.

## Example

`synthetic_unverified`: draft → review → approved; missing source → blocked; no auto-publish.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

A diagram does not verify the runtime; implement transition tests before release.
