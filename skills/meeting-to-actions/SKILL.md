# Meeting to Actions

Extract action items from a supplied transcript. Keep owner and deadline unknown when not spoken; require human confirmation before sending.

## Input schema

`transcript`, `participants`, `meeting_date`.

## Output schema

`summary`, `decisions`, `actions: [{task,owner,due,evidence_quote}]`, `unknowns`.

## Example

`synthetic_unverified`: “Alex will review the sample draft” → action owner Alex; due date unknown.

## Failure modes

Fabricated commitments, omitted disagreement, automatic outbound assignment.
