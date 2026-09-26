---
name: meeting-to-actions
description: Extract decisions and owner-tagged actions from a supplied transcript without inventing deadlines or sending assignments.
---

# Meeting to Actions

## Purpose

Create a reviewable meeting follow-up from transcript evidence.

## When to Use

Use when the user supplies a transcript or notes and wants action items, not an automatic outbound message.

## Inputs

`transcript`, `participants[]`, `meeting_date`, optional `language`.

## Outputs

`summary`, `decisions[]`, `actions: [{task,owner,due,evidence_quote,confidence}]`, `unknowns[]`.

## Workflow

1. Mark inaudible or contradictory transcript spans instead of smoothing them away.
2. Extract only commitments or requests tied to a quoted span.
3. Keep owner and due date `unknown` unless stated or clearly resolved in the transcript.
4. Separate decisions from proposals and disagreements.
5. Return a draft for human confirmation before any assignment is sent.

## Failure Handling

If attribution is ambiguous, mark the owner `unknown`; if the transcript is incomplete, flag missing context. Never send or schedule automatically.

## Example

`synthetic_unverified`: “Alex will review the sample draft” yields owner Alex and due date unknown.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

Transcription errors can propagate; the original recording or participant confirmation may be required.
