# Darwin evaluation

**Evaluation date:** 2026-08-08
**Final score:** **82.6 / 100** mean across three independent judges (median `83.1`; range `80.8`–`83.9`). All three judged the skill as a pass.

## Reproducible evidence

Each judge was a separate read-only Hermes one-shot process. It loaded the final `SKILL.md`, `references/current-market-verification.md`, and the two real `full_test` outputs in `test-prompts.json`; the run scope contained file reads and omitted live market lookups, wallet calls, and file edits.

```bash
env -u HERMES_KANBAN_TASK -u HERMES_KANBAN_WORKSPACE \
  -u HERMES_KANBAN_BRANCH -u HERMES_KANBAN_DB -u HERMES_KANBAN_BOARD \
  hermes --safe-mode -z '<read the three files; independently score frontmatter(7), workflow(12), failure modes(12), checkpoints(6), specificity(18), resources(4), architecture(12), measured performance(23), and blacklist(6); return JSON scores and total>'
```

| Judge | Total | Verdict | Main shortfall identified |
|---|---:|---|---|
| alpha | 83.1 | pass | Distributed anti-pattern guidance |
| beta | 80.8 | pass | Decision gates use non-interrupting evidence gates; anti-pattern guidance is distributed |
| gamma | 83.9 | pass | Recovery branches and anti-pattern guidance could be more explicit |

Mean dimension scores (`0`–`10`): frontmatter `9.33`, workflow `8.00`, failure modes `7.33`, checkpoints `5.00`, specificity `8.67`, resources `10.00`, architecture `9.00`, measured performance `9.33`, blacklist `4.67`.

## Retained Darwin change

The final skill adds compact **Decision gates** and **Evidence foundation** sections. They make the conditions for quantified analysis, transaction planning, and near-liquidation reasoning explicit while preserving portable, non-interrupting guidance. The package expresses checkpoint behavior as positive evidence gates, reducing unnecessary cognitive-load markers.

## Full-test evidence

`test-prompts.json` contains the actual outputs from two final-skill Hermes one-shot executions:

1. A collateral-withdrawal request with `HF = 1.35`; the response requested an exact market and live simulation, then compared lower-risk repayment, smaller-withdrawal, and collateral options.
2. A GHO cross-chain request close to liquidation; the response separated the Ethereum debt and collateral from token movement, then identified the live state and repayment path to verify.

Both outputs meet their recorded expected behavior. They are qualitative skill tests; live verified context supplies financial advice, market data, and transaction simulation.
