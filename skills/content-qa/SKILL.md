---
name: content-qa
description: Review a draft for evidence, privacy, tone and release risks without silently rewriting disputed statements.
---

# Content QA

## Purpose

Produce an actionable release gate for draft content.

## When to Use

Use before publishing a claim-heavy article, landing page, FAQ or generated answer.

## Inputs

`draft`, `source_docs[]`, `style_rules[]`, `forbidden_claims[]`, optional `audience`.

## Outputs

`findings: [{severity,excerpt,reason,source_id,fix}]`, `release_state`, `required_review[]`.

## Workflow

1. Extract all quantitative, comparative, customer and compliance claims.
2. Trace each claim to the provided source and flag mismatches or missing citations.
3. Check personally identifying information, confidential material, links and channel rules.
4. Score findings as critical, major or minor with exact excerpt and proposed fix.
5. Set `release_state=BLOCKED` on unresolved critical findings; do not publish.

## Failure Handling

If sources are incomplete, report `UNKNOWN_SUPPORT` rather than approving. Disputed language is flagged, never silently softened into apparent approval.

## Example

`synthetic_unverified`: “10,000 customers” without source triggers a critical finding and blocked release.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

This is a review aid, not legal clearance, source authenticity verification or human editorial approval.
