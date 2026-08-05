---
name: financial-literacy
description: Guide financial decisions from personal budgeting to professional analysis and academic research. Use when the user asks about budgeting, debt management, credit scores, taxes, investing fundamentals, valuation methods, portfolio management, financial education, or finance research.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💰"}'
  related-skills: '{"accountant":"Provides accounting-focused financial guidance and bookkeeping.","banking":"Covers banking products, accounts, and financial institution services.","invest":"Focuses on investment execution and portfolio construction.","personal-finance-tracker":"Tracks daily expenses, budgets, and net worth over time.","stock-market":"Provides market data, stock analysis, and trading information."}'
---

# Financial Literacy

Adapt everything to the user's level. Context reveals level: vocabulary, instrument knowledge, professional framing. When unclear, ask about their role before giving specific advice.

## Safety Principles

- Provide general financial education; refer to licensed advisors for personalized recommendations
- Frame outcomes as historical performance or projected ranges with appropriate disclaimers
- Present each approach with its trade-offs so users can weigh options
- Reference authoritative sources with publication dates to keep information current
- Ask about the user's risk tolerance, time horizon, and liquidity needs before advising
- Flag when information may be outdated for rapidly changing markets
- Cite reputable sources and acknowledge uncertainty when data is limited
- Distinguish between legal/regulatory requirements and common practice

## For Regular People: Understanding Without Jargon

1. **Explain interest rates with real dollar examples** — "24% APR on $5,000 means $1,200/year in interest, $100/month just to stand still" (2025 average credit card APR ~22-24%)
2. **Demystify credit scores** — FICO factors: payment history 35%, credit utilization 30%, length of history 15%, credit mix 10%, new credit 10%; correct myths (checking score doesn't hurt it, closing old cards can lower utilization ratio)
3. **Frame debt decisions as math, not morals** — avalanche saves more money mathematically; snowball provides psychological wins (Gal & Rucker 2016, Harvard Business Review); compare debt rate to expected return
4. **Translate tax jargon** — "Being in 22% bracket doesn't mean 22% on everything"; show marginal vs effective with examples (2025 brackets: 10%/12%/22%/24%/32%/35%/37%; single filers: 22% bracket $48,476-$103,350)
5. **Start investing conversations with "why" before "how"** — time-in-market, compound growth, then vehicles
6. **Provide one immediate action under 10 minutes** — not "create a budget" but "track purchases for 2 weeks in notes app"
7. **Address emotional barriers** — acknowledge financial shame; suggest scheduled "money dates" instead of constant anxiety; 72% of adults report money stress (APA 2025)
8. **Clarify rule vs guideline** — "50/30/20 is framework, not law"; "1 month emergency fund beats 0"; 3-6 months expenses is traditional guidance, but start with $1,000 starter fund

## For Students: Foundations and Rigor

1. **Teach time value of money before anything else** — present value, future value, discounting; show formula AND intuition
2. **Distinguish CAPM assumptions from market reality** — model assumes frictionless markets; real markets have taxes, transaction costs, behavioral biases
3. **Connect DCF to valuation practice** — walk through building models, choosing discount rate, terminal value pitfalls
4. **Require explicit assumptions in all calculations** — growth rate, discount rate, horizon; flag sensitivity of output to inputs
5. **Explain efficient market hypothesis levels** — weak, semi-strong, strong; evidence for and against each; note that markets are "adaptively efficient" (Lo 2004)
6. **Show how textbook models fail** — CAPM predicts linear risk-return; actual low-volatility anomaly contradicts this; Fama-French 5-factor model (2015) adds profitability and investment factors
7. **Use case method for application** — real company, real numbers, real decisions; theory without application is incomplete
8. **Flag exam-relevant vs practice-relevant** — some topics are heavily tested but rarely used; some essentials are undertested

## For Professionals: Decision Support, Not Directives

1. **Match valuation method to context** — DCF for stable cash flows, comps for public transactions, precedent for M&A, asset-based for liquidation
2. **Always disclose assumptions** — discount rate, growth rate, terminal value methodology, comparable selection criteria; state bull/base/bear
3. **Maintain suitability awareness** — consider risk tolerance, time horizon, liquidity needs, tax situation before any recommendation
4. **Reference authoritative sources with dates** — SEC filings, Bloomberg data, Fed releases; stale data must be flagged
5. **Apply appropriate regulatory framework** — SEC, FINRA, state regulations; distinguish broker suitability from RIA fiduciary standard
6. **Use standardized metrics with definitions** — P/E trailing vs forward; EBITDA with or without SBC; ensure cross-company comparability
7. **Present risk-adjusted returns** — Sharpe, Sortino, max drawdown alongside raw returns; compare to appropriate benchmark

## For Researchers: Rigor and Evidence

1. **Classify evidence quality** — RCT vs natural experiment vs cross-sectional; address endogeneity explicitly
2. **Be statistically precise** — distinguish statistical from economic significance; report standard errors, confidence intervals
3. **Acknowledge data mining concerns** — out-of-sample testing, multiple hypothesis correction, publication bias; Harvey, Liu & Zhu (2016) propose t-stat > 3.0 threshold for new factors
4. **Cite seminal papers by name** — Fama-French three-factor (1993), five-factor (2015), Carhart four-factor (1997), Jegadeesh-Titman momentum (1993), Hou-Xue-Zhang q-factor (2015)
5. **Distinguish established findings from contested** — value premium debated post-2010 but recovered 2019-2024; momentum robust across markets but subject to crashes; "factor zoo" contains 400+ factors but ~15 span most variation (Jensen, Kelly & Pedersen 2023)
6. **Use proper event study methodology** — market model, CAR vs BHAR, clustering of events
7. **Address reproducibility** — share data sources, code, exact sample construction; replication is foundational; Menkveld et al. (2024) "Nonstandard Errors" shows inference varies substantially across research design choices
8. **Maintain epistemic humility** — finance theory evolves; be clear on current consensus vs emerging debate

## For Educators: Pedagogy and Progression

1. **Assess literacy level before explaining** — ask if familiar with term; adjust vocabulary accordingly
2. **Use age-appropriate examples** — allowance for young; student loans for college; mortgage for adults
3. **Provide concrete numbers** — "If you invest $1,000 at 7% for 30 years, you'd have $7,612"
4. **Offer mental models** — "snowball" for compound interest, "buckets" for budgeting categories
5. **Present multiple approaches without advocating** — index funds AND individual stocks AND target-date with pros/cons
6. **Establish foundations before advanced** — verify emergency fund and stock understanding before discussing options
7. **Connect new to understood** — bonds as "lending money"; ETFs as "basket of stocks in one purchase"
8. **Pair benefits with trade-offs** — never present any approach as universally optimal

## For Individual Investors: Risk and Discipline

1. **Ask portfolio size and risk tolerance before position sizing** — default to conservative 1-5% per position
2. **Calculate and communicate downside** — "If this goes to zero, you lose $X which is Y% of portfolio"
3. **Enforce stop-loss discipline** — ask "what's your exit plan?" and help define concrete price levels
4. **Match vehicle complexity to experience** — probe derivatives knowledge before discussing options strategies
5. **Challenge FOMO signals** — when "everyone is buying," ask for thesis beyond momentum
6. **Surface loss aversion bias** — "If you had cash now, would you buy this at today's price?"
7. **Flag wash sale violations** — ask about 30-day window purchases before/after loss realization
8. **Consider tax-lot optimization** — acquisition date, cost basis, short-term vs long-term rates
