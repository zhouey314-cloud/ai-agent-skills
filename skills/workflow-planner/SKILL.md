# Workflow Planner

Turn a goal into a stateful workflow with owners, gates, retries and external dependencies.

## Input schema

`goal`, `actors`, `inputs`, `external_systems`, `failure_risks`.

## Output schema

`states`, `transitions`, `human_gates`, `failure_states`, `verification`.

## Example

`synthetic_unverified`: draft → review → approved; missing source → blocked; no auto-publish.

## Failure modes

Unreachable states, no retry budget, hidden irreversible actions.
