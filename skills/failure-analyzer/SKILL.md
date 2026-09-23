# Failure Analyzer

Classify observed failures using logs and reproduction evidence, then propose the smallest next experiment.

## Input schema

`expected`, `observed`, `logs`, `reproduction_steps`, `recent_changes`.

## Output schema

`symptom`, `likely_causes`, `evidence`, `unknowns`, `next_experiment`, `regression_case`.

## Example

`synthetic_unverified`: fictional retrieval failure has zero matching chunks → test chunking and access filters before editing prompts.

## Failure modes

Guessing root cause, hiding unknowns, changing benchmarks to pass.
