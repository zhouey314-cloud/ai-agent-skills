# Research Synthesizer

Compare supplied sources and separate facts, disagreements and inferences. Prefer primary evidence where available.

## Input schema

`question`, `sources: [{title,url,date,excerpt}]`, `as_of_date`.

## Output schema

`findings: [{claim,citations,confidence}]`, `conflicts`, `gaps`, `inferences`.

## Example

`synthetic_unverified`: two fictional guides disagree on a deadline → report conflict, do not choose a winner without evidence.

## Failure modes

Broken citations, stale facts treated as current, inference described as source text.
