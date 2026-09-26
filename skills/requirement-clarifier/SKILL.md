---
name: requirement-clarifier
description: Clarify an ambiguous build request into a testable scope when goals, stakeholders, or acceptance criteria are unclear.
---

# Requirement Clarifier

## Purpose

Turn a vague request into a minimal, falsifiable delivery contract without making up business rules.

## When to Use

Use before implementation when the input leaves ownership, success, data source, or irreversible actions ambiguous.

## Inputs

`request`, `known_constraints[]`, `stakeholders[]`, optional `existing_artifacts[]` and `decision_deadline`.

## Outputs

`goal`, `in_scope[]`, `out_of_scope[]`, `acceptance_criteria[]`, `assumptions[]`, `open_decisions[]`, `evidence_needed[]`.

## Workflow

1. Restate the user's desired outcome in one sentence and separate outcome from requested implementation.
2. Extract hard constraints and existing evidence verbatim; label anything inferred as an assumption.
3. Draft at most three acceptance checks that a reviewer can reproduce.
4. Ask only for decisions that materially change scope, risk or external state; continue with reversible work meanwhile.
5. Return the scope contract and mark each open decision with its owner and blocking effect.

## Failure Handling

If the owner of a business rule is unknown, mark `BLOCKED_OWNER_DECISION`; do not invent a default. If source evidence is missing, mark the criterion provisional.

## Example

`synthetic_unverified`: “Build a sample FAQ” becomes five cited answers plus a no-answer path; the approved source set remains an open decision.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

This skill cannot substitute for customer sign-off or legal/product ownership.
