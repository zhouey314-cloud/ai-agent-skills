# Content QA

Check a draft for factual support, tone, scope, privacy and channel constraints. Flag, do not silently rewrite, disputed statements.

## Input schema

`draft`, `source_docs`, `style_rules`, `forbidden_claims`.

## Output schema

`findings: [{severity,excerpt,reason,source_id}]`, `release_state`, `required_review`.

## Example

`synthetic_unverified`: “10,000 customers” without source → critical finding and blocked release.

## Failure modes

Calling unsupported claims safe, auto-publishing, missing personal data.
