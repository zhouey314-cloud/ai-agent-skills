# Eval Engineering Lite

Define a small repeatable evaluation before claiming an AI behavior improvement. Keep test and model quality separate.

## Input schema

`journey`, `risk_level`, `cases: [{input,expected,provenance}]`, `baseline`.

## Output schema

`rubric`, `results`, `regressions`, `failure_taxonomy`, `release_gate`.

## Example

`synthetic_unverified`: two fictional RAG cases validate fixture shape; model quality remains NOT_RUN without a provider.

## Failure modes

AI grading its own invented ground truth, deleting hard cases, treating valid JSON as answer quality.
