# Project Handoff

Package a runnable artifact and a truthful status note for the next owner.

## Input schema

`repository`, `run_commands`, `test_results`, `external_dependencies`, `known_limits`.

## Output schema

`start_here`, `verification_evidence`, `status`, `manual_steps`, `rollback`, `owner_questions`.

## Example

`synthetic_unverified`: a local demo passes unit tests, but provider integration is NOT_CONFIGURED and live deployment is unverified.

## Failure modes

Claiming production success from local tests, omitted secrets boundary, missing rollback.
