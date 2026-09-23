# FAQ Builder

Build questions and answers only from supplied approved material. Mark unsupported questions as unanswered.

## Input schema

`source_docs: [{id,text}]`, `audience: string`, `questions: string[]`.

## Output schema

`faq: [{question,answer,citation_ids,status}]`, `unanswered: string[]`.

## Example

`synthetic_unverified`: fictional guide states support 09:00–17:00 → answer cites guide ID; pricing without source → unanswered.

## Failure modes

Unsupported policies, invented prices, citations to irrelevant text, leaking private sources.
