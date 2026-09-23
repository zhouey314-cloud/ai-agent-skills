# Requirement Clarifier

Convert an ambiguous request into an agreed, testable scope. Ask only for a choice that materially changes the result. Do not invent business rules.

## Input schema

`request: string`, `known_constraints: string[]`, `stakeholders: string[]`.

## Output schema

`goal`, `in_scope`, `out_of_scope`, `acceptance_criteria`, `open_decisions`, `assumptions`.

## Example

`synthetic_unverified`: “Build a sample FAQ” → acceptance: five cited answers and a no-answer path; open decision: approved source set.

## Failure modes

Inventing requirements, asking every optional question, omitting acceptance criteria.
