# Darwin evaluation — accountant

Triage-only absolute scoring (paired keep/revert not required for this gate once ≥80). Eval mode: `full_test` via three independent skill-loaded executions recorded verbatim in `test-prompts.json`. The first two tests have no state-write authorization; the setup test authorizes only its named temporary `config.yaml` and `memory.md` files.

## Dimension scores (after Gate 8 structure)

| # | Dimension | Weight | Score /10 | Weighted |
|---|-----------|--------|-----------|----------|
| 1 | Frontmatter quality | 7 | 9 | 6.3 |
| 2 | Workflow clarity | 12 | 9 | 10.8 |
| 3 | Failure mode encoding | 12 | 9 | 10.8 |
| 4 | Checkpoint design | 6 | 9 | 5.4 |
| 5 | Executable specificity | 18 | 8 | 14.4 |
| 6 | Resource integration | 4 | 9 | 3.6 |
| 7 | Overall architecture | 12 | 8 | 9.6 |
| 8 | Measured performance | 23 | 8 | 18.4 |
| 9 | Counter-examples / blacklist | 6 | 9 | 5.4 |
| | **Total** | 100 | | **84.7** |

## Test summary

1. Stripe net deposit vs gross sales → proposed gross-method entries; clearing $0; tax as liability; durable coding rule withheld pending named-write authorization.
2. TB off $90 with locked June + estimated tax → ÷9/÷2 diagnostics; reverse+re-post in open period; escalate if filed figures change.
3. Greenfield sole trader → explicitly authorized temporary state root; only `config.yaml` and `memory.md` created from templates; close/recon cadence and no credential storage.

All three marked `pass: true`, `eval_mode: full_test`.

## Notes for reviewers

- Dim8 evidence is the exact output of independent skill-loaded executions in `test-prompts.json`; prompt 3 also verified the two explicitly authorized temporary files.
- Absolute score is triage-only per Darwin 2.1; paired majority is the keep/revert authority when iterating.
