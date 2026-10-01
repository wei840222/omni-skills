# Darwin evaluation

**Evaluation date:** 2026-10-01
**Final score:** **84 / 100** (threshold: 80). Re-scored after Jules thin-patch takeover on description routing, `metadata.version`, related-skills, and Gate 6 source URL re-verification.

## Reproducible evidence

Structural dry-run over the final `SKILL.md`, `references/current-market-verification.md`, and the two recorded `full_test` outputs in `test-prompts.json`. Scope: package reads only; no live market lookups, wallet calls, or file edits during scoring.

| Dimension | Score | Notes |
|---|---:|---|
| Frontmatter quality | 6.5/7 | Trigger + negative scope; version + related-skills present |
| Workflow clarity | 10/12 | Position review order and decision gates are explicit |
| Failure mode encoding | 9/12 | Missing simulation / missing deployment paths are named |
| Checkpoint design | 5/6 | Evidence gates before quantified advice |
| Executable specificity | 15/18 | Chain/market/token identity and permit inspection steps |
| Resource integration | 4/4 | Progressive load of current-market-verification |
| Overall architecture | 10/12 | Stateless entry + reference disclosure |
| Measured performance | 20/23 | Two full_test actuals match expected behavior |
| Counter-examples and blacklists | 4.5/6 | Negative routing vs `uniswap` / `crypto-tools` / non-Aave lending |
| **Total** | **84/100** | pass |

## Retained Darwin change

This pass keeps compact **Decision gates** and **Evidence foundation**, and strengthens Gate 7 routing with imperative description, negative triggers, and in-repo related-skills. Package evaluation records remain separated from live market guidance.

## Full-test evidence

`test-prompts.json` retains two final-skill full_test executions:

1. Collateral-withdrawal request with `HF = 1.35`; response requested exact market and live simulation, then compared lower-risk repayment, smaller-withdrawal, and collateral options.
2. GHO cross-chain request close to liquidation; response separated Ethereum debt/collateral from token movement, then identified live state and repayment path to verify.

Both outputs meet their recorded expected behavior. They are qualitative skill tests; live verified context supplies financial advice, market data, and transaction simulation.
