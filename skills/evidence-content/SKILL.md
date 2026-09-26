---
name: evidence-content
description: Draft content from a provenance-tagged claim ledger when factual support and approval boundaries matter.
---

# Evidence Content

## Purpose

Turn approved claims into channel-ready copy while exposing unsupported or provisional claims.

## When to Use

Use for public, sales or technical content where a source map is needed and invented proof would be harmful.

## Inputs

`claims: [{text,source_id,verification_state,scope}]`, `audience`, `channel`, optional `style_rules[]`.

## Outputs

`draft`, `claim_map[]`, `uncertain_claims[]`, `review_state`.

## Workflow

1. Classify each claim as verified, source-limited, hypothetical or unsupported.
2. Exclude unsupported metrics, customer outcomes and authority claims from the draft.
3. Draft for the audience without strengthening the claim beyond its source scope.
4. Map each material statement back to a source ID and retain important qualifications.
5. Run a final contradiction/privacy check and send uncertain claims to a named human reviewer.

## Failure Handling

If a material statement lacks support, remove it or label it explicitly as a hypothesis; set `review_state=BLOCKED` for unapproved high-impact claims.

## Example

`synthetic_unverified`: a fictional feature claim cites spec-1; an adoption number without a source is omitted.

## Tests

Run `python3 tests/validate.py` from the repository root to check this skill's contract and example provenance. This is a structural test, not model-quality evidence.

## Limitations

The skill structures evidence but does not prove a source is authentic, licensed or up to date.
