# Research Sources — Arbitrage

Gate 6 pins. Prefer these primary documents over model memory for formulas, market structure, and compliance language. Re-check dated pages when quoting numbers.

## Agent Skills packaging

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- skills-ref validator (PyPI / agentskills CLI) — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Market structure and probability

- CME Group — Understanding basis (futures vs cash) — https://www.cmegroup.com/education/courses/introduction-to-futures/understanding-the-basis.html
- Cboe — Options pricing concepts hub — https://www.cboe.com/tradable_products/options/
- Polymarket docs — resolution and trading overview — https://docs.polymarket.com/
- Kalshi API / markets documentation — https://trading-api.readme.io/reference/getting-started

## Odds and surebet math

- Wikipedia — Dutch book theorem (completeness check for complementary outcomes) — https://en.wikipedia.org/wiki/Dutch_book
- Wikipedia — Arbitrage — https://en.wikipedia.org/wiki/Arbitrage
- Decimal odds conversion: implied probability = 1 / decimal_odds (standard bookmaking identity; verify venue commission before netting)

## Crypto venue friction (fees, funding, transfers)

- Binance Support — Spot trading fee schedule — https://www.binance.com/en/fee/schedule
- Binance Support — Withdrawal fees and networks (verify live) — https://www.binance.com/en/fee/cryptoFee
- Deribit help — Funding and perpetual mechanics overview — https://insights.deribit.com/
- Ethereum.org — Gas and transaction fees — https://ethereum.org/en/developers/docs/gas/

## Retail / operational mismatch

- FTC — Business guidance on advertising and pricing claims (US) — https://www.ftc.gov/business-guidance/advertising-marketing
- Incoterms overview (ICC) — shipping risk allocation vocabulary — https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/

## Disclaimers posture

- SEC investor education hub — https://www.sec.gov/investor
- CFTC customer protection — https://www.cftc.gov/ConsumerProtection/index.htm

## Notes for maintainers

- Fee tables and withdrawal latencies change without notice; always prefer user-supplied live venue screens or official fee pages at analysis time.
- Prediction-market resolution text is venue-specific; never assume two similarly named markets share void or overtime rules.
- Sportsbook palpable-error and max-payout rules are operator-specific; capture them in `<state_root>/venue-notes.md` when the user provides them.
