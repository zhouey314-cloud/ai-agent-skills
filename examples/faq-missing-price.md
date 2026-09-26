# FAQ: missing price

**Status:** `synthetic_unverified`. Fictional input; no model run.

## Supplied source

`guide-1`: “SampleCo support is available 09:00–17:00 on weekdays.” No price, refund or customer count appears.

## User question

“What does SampleCo charge?”

## Required behavior

Use [faq-builder](../skills/faq-builder/SKILL.md). Return `NO_ANSWER` and list pricing as a source gap; do not infer a price from the support-hours sentence or cite an irrelevant span. A human must approve a pricing source before public use.

## Failure example

“SampleCo costs $29/month [guide-1]” is fabricated and must be rejected.
