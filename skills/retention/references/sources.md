# Retention sources

Load this file when quoting benchmarks, NRR formulas, or churn ranges. Keep the original window and denominator.

## Metric definitions

| Source | URL | Use |
| --- | --- | --- |
| Stripe — Net revenue retention | https://stripe.com/resources/more/net-revenue-retention | NRR/GRR formulas, expansion vs contraction, why NRR can mask logo churn (page last updated 2026-05-07 in retrieved copy) |
| Agent Skills specification | https://agentskills.io/specification | Package format only; not a retention benchmark |

## Benchmarks and churn context

| Source | URL | Window / notes |
| --- | --- | --- |
| Lenny Rachitsky — What is good retention? (with Casey Winters) | https://www.lennysnewsletter.com/p/what-is-good-retention-issue-29 | **2020-06-09**. Expert GOOD/GREAT **6-month user retention** and **12-month NRR** by business type. Not D30. |
| Paddle — SaaS churn rate | https://www.paddle.com/blog/saas-churn-rate | Churn varies by industry, ARPU, contract length, stage; discusses involuntary churn from payment failure; warns against universal averages |

## Intentionally unused / failed lookups this refactor

| URL | Result |
| --- | --- |
| https://mixpanel.com/blog/retention-benchmarks/ | HTTP 404 at repair time — do not cite |
| https://mixpanel.com/blog/product-analytics-benchmarks-report/ | HTTP 404 at repair time — do not cite |
| https://amplitude.com/blog/product-retention | Connection failed in repair environment — do not claim live numbers from it |

## Citation rules

1. Always pair a number with source, date, metric name, and window.
2. Do not relabel 6-month or 12-month comps as D30.
3. Prefer the user’s own cohort math over external bands when data exists.

## Extraction notes (repair)

- Lenny 2020 tables are expert synthesis for **month-6 user retention** and **month-12 NRR**; paid-company denominators appear in some SMB examples in the article body—do not silently convert to D30 free-user comps.
- Stripe NRR example uses beginning recurring revenue ± expansion/contraction/churn for the **same** starting customers.
- Paddle emphasizes definition mismatch (logo vs revenue, monthly vs annual) before any single “good churn %”.
