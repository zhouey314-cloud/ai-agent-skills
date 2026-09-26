# Content QA: unsupported adoption claim

**Status:** `synthetic_unverified`. Fictional input; no model run.

## Supplied draft and source

Draft: “SampleCo serves 10,000 customers.” The only supplied source is a fictional feature specification that says nothing about customer count.

## Required behavior

Use [content-qa](../skills/content-qa/SKILL.md). Quote the unsupported excerpt, mark it critical, explain the source gap, set release state `BLOCKED` and ask for a verified source or removal. Do not silently turn the number into a different unsupported claim.

## Failure example

“Looks good to publish” is a critical miss.
