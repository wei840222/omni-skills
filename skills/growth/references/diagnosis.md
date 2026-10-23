# Diagnosis — find the constraint

## Absolute lift

Rank every stage by:

`lift = upstream_volume × (achievable_rate − current_rate) × downstream_conversion × value_per_conversion`

A 2% → 4% activation on 10,000 signups beats 30% → 45% on a 300-user segment even when the second percentage looks better.

## Procedure

1. Pick the equation row for the business model (see `SKILL.md`).
2. Fill current rates with explicit denominator, window, and cohort anchor.
3. Estimate an achievable rate that has precedent in-segment (not a fantasy ceiling).
4. Sort stages by absolute lift; name **one** primary constraint.
5. Only then choose a tactic that moves that stage.

## Pre-PMF gate

- If the retention curve slides to zero, treat product change and churn interviews as the work — not channel scale.
- Sean Ellis "very disappointed" ≥40% is a common pre-PMF bar before buying traffic; below that, acquisition amplifies a leak.

## Plateaus and mix shifts

Separate saturation, creative/channel decay, seasonality, and mix shift before killing a channel. Compare like windows (and YoY when the business is seasonal). An aggregate can move opposite every segment when mix changes.

## Numbers that commonly lie

| Number | Failure mode | Prefer |
|---|---|---|
| Signups | Intent without value | Activated users (aha action) |
| Blended CAC | Organic subsidises paid | Paid CAC = paid spend ÷ paid-attributed customers |
| Uncapped LTV | `ARPA × margin ÷ churn` invents a lifetime never observed | Cap planning horizon (often 24–36 months) and state the cap |
| DAU/MAU | Ignores natural frequency | Frequency vs expected frequency for the job |
| Single "70% retention" | Hides curve shape | Cohort curve with flatten week |
| Last-touch attribution | Flatters harvest channels | Hold-out / geo tests when spend allows |
| Stopped-early test lift | Peeking false positives | Pre-registered horizon or sequential method |

## Handoff

- Page is the constrained surface → `cro`
- Cohort/churn depth is the ask → `retention`
- Org/board narrative is the ask → `cgo`
