# Darwin evaluation (Gate 8)

**Evaluation date:** 2026-10-03
**Package:** `skills/hype`
**Final score:** **84 / 100** (threshold ≥ 80)
**Method:** Structural dry-run over final `SKILL.md`, `references/trading-features.md`, `references/sources.md`, and three recorded full_test `actual` strings in `test-prompts.json`. No live trading, wallet connect, or fund movement during scoring.

## Dimension scores

| Dimension | Score | Notes |
|---|---:|---|
| Frontmatter quality | 6.5/7 | Imperative triggers + negative scope; `metadata.version`; related-skills to existing slugs |
| Workflow clarity | 10/12 | Goal → route/margin confirm → load reference → auth before signed steps |
| Failure mode encoding | 9/12 | Deposit visibility, liquidation order error, fee misconception, rate limits covered |
| Checkpoint design | 5.5/6 | Explicit authorization before deposits/orders/staking; time-sensitive verify note |
| Executable specificity | 15/18 | Concrete thresholds (100k partial, 2/3 MM, 7-day unstake, tiered max lev) with source backing |
| Resource integration | 4/4 | Conditional load of trading-features + sources |
| Overall architecture | 10/12 | Stateless entry + progressive disclosure; no clawic residue |
| Measured performance | 20/23 | Three full_test actuals match expected behavior and corrected domain facts |
| Counter-examples and blacklists | 4/6 | Near-miss routing to binance/ethereum/invest/aave |
| **Total** | **84/100** | pass |

## Full-test provenance

Executed as skill-conditioned answers against the repaired package text (not Jules' obsolete oracle):

1. Deposit how-to — route-dependent USDC/Unit paths; rejects Arbitrum-only claim.
2. Liquidation order + “partial always” myth — book-first, conditional partial, backstop; sizing remedies.
3. Fee revenue-share myth — HLP / assistance fund burn / deployers; staking discounts ≠ fee share.

All three `pass: true` with expected/actual alignment in `test-prompts.json`.

## Iteration notes

- Prior Jules patch failed Gate 8 on obsolete deposit oracle and missing execution evidence.
- This pass rewrote oracles from official docs, recorded real actuals, and kept safety/auth checkpoints while scoring ≥ 80.
