---
name: project-handoff
description: Package a runnable project with exact tests, risks and next-owner instructions without overstating production readiness.
---

# Project Handoff

## Purpose

Let a new owner reproduce the current status and understand what is not done.

## When to Use

Use before transferring a repo, demo or implementation to another person or team.

## Inputs

`repository`, `run_commands[]`, `test_results[]`, `external_dependencies[]`, `known_limits[]`.

## Outputs

`start_here`, `verification_evidence`, `status`, `manual_steps[]`, `rollback`, `owner_questions[]`.

## Workflow

1. Identify the exact commit and working-tree state.
2. Run or verify documented start/test commands and record outcomes.
3. Separate local, static deployed, external-provider and production evidence.
4. List configuration secrets by name only and explain how the owner supplies them.
5. Provide rollback, limitations and one-page first-run steps.

## Failure Handling

Unknown deployment status is `UNVERIFIED`; unavailable credentials are `BLOCKED`. Never copy secrets into the handoff.

## Example

`synthetic_unverified`: a local demo passes tests but provider is `NOT_CONFIGURED` and live deploy is unverified.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

This package does not replace receiving-team acceptance or operational runbooks.
