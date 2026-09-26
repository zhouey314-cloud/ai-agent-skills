---
name: faq-builder
description: Build cited FAQs from supplied approved documents, with explicit no-answer behavior when policy or pricing is absent.
---

# FAQ Builder

## Purpose

Produce a traceable FAQ without inventing policies, prices or citations.

## When to Use

Use when a user supplies source documents and needs audience-specific questions answered from those sources.

## Inputs

`source_docs: [{id,text,visibility,approved}]`, `audience`, `questions[]`.

## Outputs

`faq: [{question,answer,citation_ids,status}]`, `unanswered[]`, `source_gaps[]`.

## Workflow

1. Reject or quarantine documents not approved for this audience.
2. For each question, identify exact supporting source spans before drafting the answer.
3. Write only the supported portion; if no span suffices, set status `NO_ANSWER`.
4. Check each citation points to the asserted fact and preserves qualifications.
5. Return unanswered questions as explicit knowledge gaps for human review.

## Failure Handling

Missing or conflicting sources produce `NO_ANSWER` or `CONFLICT`, never a guessed answer. Private source material must not be copied into a public FAQ.

## Example

`synthetic_unverified`: a fictional guide says support is 09:00–17:00, so cite its ID; a pricing question without a source is unanswered.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

Citations are only as trustworthy and current as the supplied documents; there is no independent fact verification.
