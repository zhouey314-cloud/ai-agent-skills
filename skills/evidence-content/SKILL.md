# Evidence Content

Draft content from a claim ledger. Separate verified claims from hypotheses and omit unsupported assertions.

## Input schema

`claims: [{text,source_id,verification_state}]`, `audience`, `channel`.

## Output schema

`draft`, `claim_map: [{claim,source_id}]`, `uncertain_claims`, `review_state`.

## Example

`synthetic_unverified`: fictional feature claim cites spec-1; adoption numbers with no source are excluded.

## Failure modes

Fabricated metrics, lost qualifications, channel copy that overstates evidence.
