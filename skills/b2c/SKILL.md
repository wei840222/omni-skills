---
name: b2c
description: >
  Design consumer product strategy with validated demand, monetization choice,
  activation/retention kill metrics, CAC/LTV/payback denominators, and growth
  loops. Use for B2C apps, freemium/trial paywalls, consumer SaaS, casual games,
  and unit-economics reviews. Not for enterprise B2B deal qualification (`b2b`)
  or CRM/API plumbing.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📱"}'
  related-skills: '{"b2b":"Enterprise deal qualification when the customer is a buying committee rather than end consumers.","growth":"Channel experiment execution after B2C stage and loop choices are set.","pricing":"Deep price research once the monetization model is chosen.","retention":"Deep cohort retention diagnostics after stage priorities point at habit.","saas":"Broader SaaS ops once consumer-specific economics are framed.","product":"General product discovery adjacent to consumer monetization and loops."}'
---

## When to use

Load for consumer (B2C) product and growth judgment: demand validation, monetization/paywall, activation/retention, unit economics, growth loops, stage priorities.

## Scope

Knowledge-only coaching. No persistent analytics state, billing config, or ad-account credentials. Ask for measured inputs; do not invent cohort rates, spend, or revenue.

## Primary workflow

1. Classify the ask (demand, monetization, activation/retention, economics, loop/channel, stage).
2. Inventory known facts (category, stage, model, D1/D7/D30 or M6, conversion definition, ARPU, spend, **new paying customers**, payback policy). Label unknowns.
3. Load the reference that owns the bottleneck:

| Bottleneck | Load |
|------------|------|
| Monetization / paywall | `references/monetization.md` |
| CAC / LTV / payback | `references/economics.md` |
| Growth loops / channels | `references/growth.md` |
| Retention / conversion bands | `references/benchmarks.md` |

4. Apply core rules below.
5. Output recommendation, missing inputs, kill metric, and next measurement.

## Core framework

### Stage-aware priorities
| Stage | Focus | Key signal |
|-------|-------|------------|
| Pre-PMF | Activation + Retention | Weak habit / retention vs category → fix product before scale |
| Post-PMF | Acquisition + Conversion | CAC payback vs funding posture |
| Scaling | LTV optimization + Loops | LTV:CAC on **contribution** basis |

### The 30-second rule
Consumer products win or lose in the first session surface:
1. Is there a hook? (emotional trigger, curiosity, benefit)
2. How many taps to value? (target: ≤3)
3. Is signup deferred until after value shown when feasible?

### Critical metrics
- **Activation**: % reaching named aha moment in first session
- **Retention**: D1/D7/D30 and M6 when available, by acquisition cohort
- **Monetization**: Conversion rate, ARPU, payback period
- **Referral**: K-factor, organic vs paid ratio
- **CAC**: fully loaded spend / **new paying customers** (CPI separate if only installs)
- **LTV/payback**: state revenue vs contribution-margin basis

## Anti-patterns → preferred moves
1. **Building for power users** → design the casual-majority default path
2. **Generous freemium that fully solves the job** → natural limits or trial
3. **Vanity MAU** → define “active,” then report retention on that event
4. **B2B-long onboarding for consumers** → show value fast
5. **Ignoring emotions** → pair benefit with felt hook early
6. **Late paywall after free habit** → gate after aha at a natural limit
7. **Scaling ads before retention shape is known** → fix activation/retention first
8. **CAC from installs + LTV from payers** → align denominators

## Decision support
1. Validate demand first (real complaints / willingness to pay)
2. Design monetization model early (model before fine price)
3. Define activation moment in observable events
4. Plan at least one compounding growth loop
5. Set kill metrics before scaling spend

## Reference routing

| Topic | File |
|-------|------|
| Monetization models & paywall design | `references/monetization.md` |
| Unit economics (CAC, LTV, payback) | `references/economics.md` |
| Growth loops & acquisition channels | `references/growth.md` |
| Retention benchmarks by category | `references/benchmarks.md` |
