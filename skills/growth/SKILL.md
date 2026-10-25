---
name: growth
description: >
  Run growth as a system: name the constrained funnel stage in absolute units,
  choose compounding loops, and size channel/experiment programs. Use when growth
  stalls, CAC/payback/LTV:CAC must be defended, signups rise but activation or
  retention does not, or when designing referral, lifecycle, north-star, or
  forecast models. Not for page-level CRO (`cro`), deep churn cohorts
  (`retention`), CGO org leadership (`cgo`), or SaaS MRR taxonomy (`saas`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📈","requires":{"config":["<state_root>/growth/","<state_root>/finances/","<state_root>/projects/","<state_root>/contacts/","<state_root>/profile.yaml"]}}'
---

# Growth

Advise-mode skill for **systemic growth diagnosis and planning**: find the constrained stage, prove lift in absolute units, gate paid spend on retention, and pick loops/channels with kill numbers. It reads and writes plain local notes under `<state_root>/` only.

## State location

Growth state may exist in `<workspace>/growth/`, `<workspace>/memory/growth/`, or `~/growth/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/growth/`, `<workspace>/memory/growth/`, `~/growth/`.
3. If none exists and state must be created, default to `<workspace>/growth/`.

Use the selected `<state_root>` for every state operation in this skill.

## When to load

- Growth is flat, decelerating, or a target was missed and nobody can name the broken stage
- Choosing, scaling, or killing acquisition channels with CAC / payback / LTV:CAC
- Signups grow but activation, retention, or paid conversion does not
- Designing a growth loop, referral program, lifecycle map, north-star, or bottom-up forecast
- Marketplace liquidity, app install funnels, ecommerce repeat purchase, or self-serve vs sales motion
- Out of scope: single-test statistics and page CRO (`cro`); deep churn cohort craft (`retention`); CGO role/org design (`cgo`); pure SaaS MRR taxonomy (`saas`)

## Data and state

At session start, read `<state_root>/growth/config.yaml` and `<state_root>/growth/memory.md` (including `## Boxes` and `## Due`). Open files named by `## Boxes` only when their condition applies; every path must stay under `<state_root>/`. Read `<state_root>/finances/budget.md` before proposing spend and `<state_root>/projects/` before treating a launch as new. If none exist, work from defaults and do not narrate the missing files.

**Write before the session ends** when something durable was produced (funnel/retention number with as-of date; channel start/scale/kill with CAC and payback; experiment readout; loop identified; metric definition; target/forecast; paid budget; agency/person involved; or a reusable artifact). Destinations and formats live in `references/memory-template.md`.

**Shared boxes:** paid spend → `<state_root>/finances/budget.md`; growth tooling → `<state_root>/finances/subscriptions.md`; launches → `<state_root>/projects/<project>.md`; people → `<state_root>/contacts/contacts.md` (one row per `Key`). Growth numbers stay in `<state_root>/growth/`.

**Never write credentials under `<state_root>/`.** Store pointers only (`env:…`, `keychain:…`, `1password:…`). Aggregate raw user exports; drop PII rows. If data sits at `~/growth/` or `~/clawic/growth/`, move it to `<state_root>/growth/` and say so in one line.

## Quick Reference

| Situation | Play | Depth |
|-----------|------|-------|
| Flat growth / missed number | Equation → absolute lift → one constraint | `references/diagnosis.md` |
| Channel choice / paid scale | Portfolio, CAC, payback, kill numbers | `references/acquisition.md` |
| Need a compounding mechanism | Loop selection and cycle time | `references/loops.md` |
| Definitions disagree / no events | Denominator, window, cohort anchor, tracking plan | `references/instrumentation.md` |
| Memory destinations / shared boxes | Write protocol and templates | `references/memory-template.md` |
| Cite or re-verify Gate 6 facts | Research anchors | `references/sources.md` |

Load **at most one** deep `references/` file per step (progressive disclosure).

## Core Rules

1. **Work the constraint in absolute units.** `lift = upstream_volume × (achievable_rate − current_rate) × downstream_conversion × value_per_conversion`. Rank stages by lift, not by the ugliest percentage (`references/diagnosis.md`).
2. **Retention gates spend.** Do not step-change paid spend until the cohort curve flattens on two consecutive cohorts at the product's natural frequency; pre-PMF prefer Sean Ellis ≥40% "very disappointed" before buying traffic (`references/diagnosis.md`, route depth to `retention`).
3. **A rate needs denominator, window, and cohort anchor.** Write the definition once and reuse it (`references/instrumentation.md`).
4. **Payback decides scale; LTV:CAC decides existence.** `payback_months = CAC ÷ (monthly ARPA × gross_margin)`. Scale only when payback ≤ `target_cac_payback_months` **and** it holds after a 2× spend increase (`references/acquisition.md`).
5. **One named loop with cycle time.** Output = f(step conversion, **cycle time**); campaigns are not loops (`references/loops.md`).
6. **Two or three live channel tests**, each with a pre-committed kill number and kill date (`references/acquisition.md`).
7. **Pre-register metric, horizon, and sample size** before shipping a test; do not stop early on peeking (`references/acquisition.md` experiments notes).
8. **Segment before concluding** (source, plan, platform, geo, new vs existing) to avoid Simpson effects.
9. **Ship the event with the feature**, never after (`references/instrumentation.md`).

## Growth equation (select the row)

| Model | Equation | Usual break |
|---|---|---|
| Self-serve SaaS | visitors × signup% × activation% × paid-conversion% × (1 ÷ churn) × ARPA | Activation, then paid conversion |
| Sales-assisted B2B | leads × MQL% × SQL% × win% × ACV × (1 + expansion) | SQL definition / win rate |
| Marketplace | (supply × listing quality) ∩ (demand × intent) → match% × take_rate × frequency | Constrained side |
| Ecommerce | sessions × conversion% × AOV × contribution_margin% × repeat_rate | Repeat rate |
| Consumer app | installs × open% × D1 × D7 × D30 × sessions/user × monetization/session | Install-to-value gap |
| Content/media | content × traffic/content × subscribe% × engagement × ad or sub RPM | Traffic-per-unit decay |

## Stage gates

| Stage | Signal | Do | Defer |
|---|---|---|---|
| pre-pmf | Curve → 0; Sean Ellis <40% | Talk to churned users; change product; hand-deliver value | Hiring growth, buying traffic, referral programs |
| early | Curve flattens for one segment; one manual channel works | Instrument; define the loop; make the channel repeatable | Channels 3–4; automate unproven hand work |
| growth | Payback on ≥1 channel survives 2× spend | Scale that channel; run experiments; close the loop | Reorg around unproven channels |
| scale | Multi-channel; CAC drifting up | Portfolio, incrementality, expansion, new segments | Treating plateau as a pure tactics bug |

## Output gates

Before delivering a recommendation:

- Named constraint with absolute lift units?
- Definitions include denominator, window, cohort anchor?
- Spend gated on retention evidence and 2× payback survival?
- Each test has metric, horizon, sample size, kill number?
- Loop vs campaign labeled?
- Durable outputs written per `references/memory-template.md`?

## Configuration

Store overrides in `<state_root>/growth/config.yaml`. Defaults: `business_model=saas`, `motion=self-serve`, `stage=early`, `north_star=none`, `target_cac_payback_months=12`, `monthly_paid_budget=0`, `analytics_stack=none`, `experiment_confidence=95`, `reporting_cadence=weekly`, `privacy_regime=none`. Precedence: `config.yaml` → `<state_root>/profile.yaml` → defaults.

## Mode

**Advise by default** — produce the model, number, and decision. Draft artifacts (experiment brief, tracking plan, lifecycle map) only when asked. Start from defaults; prefer stating assumptions over opening with inventory questions about stage, stack, or budget.
