# Contributing

Thank you for improving this clean-room collection. A useful contribution must solve a distinct task, not add a placeholder folder.

## Before opening a PR

1. Confirm you own or may redistribute every instruction, example and asset. Do not submit company/customer prompts, private documents, real voices, secrets or scraped private material.
2. Make one skill directory with a `SKILL.md` whose frontmatter name equals its directory name. Include Purpose, When to Use, Inputs, Outputs, Workflow, Failure Handling, Example, Tests and Limitations.
3. Give an example with source/provenance and a failure path. Mark fictional material `synthetic_unverified`.
4. Add a deterministic structural test where possible. If changing model behavior, preserve a baseline and add independently reviewed cases; a synthetic fixture is not evidence of model quality.
5. Run `python3 tests/validate.py` and `python3 evals/run.py`. Show exact outputs, limitations and any blocked provider in the PR.

## Review checklist

- Is the trigger description specific, and does it avoid stealing adjacent tasks?
- Can a newcomer supply inputs and inspect outputs without secret credentials?
- Does the workflow stop at ownership, privacy, high-impact or publishing gates?
- Is each factual claim supported, and is third-party attribution retained?
- Does the test/eval claim match what was actually run?

Use the issue templates for a reproducible bug or a proposed workflow. Maintain backwards compatibility of published skill names where possible; document changes in [CHANGELOG.md](CHANGELOG.md). MIT licensing applies only to material you have authority to contribute.
