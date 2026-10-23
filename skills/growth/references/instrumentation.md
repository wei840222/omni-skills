# Instrumentation and definitions

## Definition contract

Every stored rate must declare:

1. **Numerator / denominator**
2. **Window** (e.g., 7-day)
3. **Cohort anchor** (prefer permanent first-touch dating; conversion-dated cohorts rewrite history)

Example: "conversion 12%" → *signups ÷ unique visitors, 7-day window, cohort by first touch*.

## Tracking plan

Ship events **with** the feature. Retroactive events cannot backfill the cohort that first used it.

Include: event names, properties, identity stitching, server vs client, and ownership. Align examples to `analytics_stack` when set (`ga4`, `amplitude`, `mixpanel`, `posthog`, `warehouse`, or `none`).

## Privacy

Apply `privacy_regime` (`none` / `gdpr` / `ccpa` / `both`) to consent, retargeting, and messaging opt-in. Do not invent lawful bases.

## Metric registry

Keep durable definitions in a growth artifact (for example `<state_root>/growth/artifacts/metric-definitions.md`) and index it from `memory.md` `## Boxes`.
