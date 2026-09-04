# CRM Metrics

Measure leading indicators before lagging vanity totals. Prefer numbers derived from closed history over the tool's seeded win rates.

## The six numbers

| Metric | How to compute | Why it matters |
|---|---|---|
| Stage conversion | closed-won ÷ entered, per stage, over a fixed window | Replaces fake default probabilities |
| Cycle length | median days from Lead/Qualified entry to Closed-won | Spots process drag, not just volume |
| Slippage | count of close-date moves per open deal | Two slips = qualification failure |
| Source quality | won rate and cycle length by source | Stops overfunding dead channels |
| Velocity | won value in period ÷ average cycle days | Combines volume and speed |
| Next-step coverage | open deals with a future next-step date ÷ open deals | Predicts which "pipeline" is fiction |

## Forecast rules

1. Weight open value by **measured** stage conversion, with an as-of date on the rates.
2. Apply a slippage adjustment: deals that already moved their close date twice leave the commit forecast.
3. Below roughly 20 closed deals in the period, prefer deal-by-deal commit / best-case / pipeline calls over weighted averages (`references/experts.md`).
4. Never back-date stage entry to shorten cycle length; that corrupts every conversion number downstream.

## Review cadence

On `review_day` (default Monday), produce:

- Stalled list (`stall_days`)
- Overdue follow-ups (`stale_days`, contacts without open deals)
- Forecast with as-of conversion rates
- One sentence on what changed since last review
