---
name: research-synthesizer
description: Compare provided sources, distinguish fact from inference, and surface dated conflicts in a research answer.
---

# Research Synthesizer

## Purpose

Produce a synthesis with traceable citations and explicit disagreement.

## When to Use

Use when multiple documents or links disagree or when freshness matters.

## Inputs

`question`, `sources: [{id,title,url,date,excerpt}]`, `as_of_date`.

## Outputs

`findings: [{claim,citations,confidence}]`, `conflicts[]`, `gaps[]`, `inferences[]`.

## Workflow

1. Inventory source dates and whether each is primary or secondary.
2. Extract relevant claims and quote only short supporting spans.
3. Group agreement, disagreement and missing evidence separately.
4. Label inferences as inferences and avoid resolving conflicts without evidence.
5. Return a concise synthesis with citations and a freshness caveat.

## Failure Handling

A broken citation or stale source blocks a current-fact claim. If sources conflict, report the conflict instead of selecting a convenient answer.

## Example

`synthetic_unverified`: two fictional guides disagree on a deadline; the output reports the conflict.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

No live browsing is implied by this skill; it can only analyze sources actually supplied or retrieved with authorized tools.
