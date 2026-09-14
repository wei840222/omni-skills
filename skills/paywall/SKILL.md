---
name: paywall
description: >
  Design and review high-converting paywalls for mobile (iOS/Android) and web.
  Use for subscription screens, pricing pages, free-trial flows, placement strategy,
  pricing display, copy, layout patterns, and A/B testing priorities. Skip general UI
  design that is not about monetization or conversion.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔓"}'
  related-skills: '{"in-app-purchases":"Implement store billing, entitlements, and restore flows after paywall UX is decided.","pricing":"Broader pricing strategy and packaging outside a single paywall screen."}'
---

## When to load

Load this skill when tasked with designing, reviewing, or optimizing a paywall, subscription screen, pricing page, or free trial flow. Skip loading this for general UI design unrelated to monetization.

## Platform Differences

| Aspect | Mobile (iOS/Android) | Web (SaaS) |
|--------|----------------------|------------|
| Context | Full-screen takeover | Pricing page or modal |
| Timing | Onboarding, contextual, campaigns | Landing page, upgrade prompts |
| Billing | App Store / Play Store | Stripe, Paddle, etc. |
| Trials | Store-managed | Self-managed |
| Testing | Remote config, A/B tools | Standard web A/B |

**Load `<state_root>/skills/paywall/references/mobile.md`** for iOS/Android specifics.
**Load `<state_root>/skills/paywall/references/web.md`** for SaaS pricing pages.

## Placement Strategy

| Type | When | Conversion share |
|------|------|------------------|
| Onboarding | After install, during setup | 40-60% of trials |
| Contextual | User hits premium feature | 20-30% |
| Upgrade button | Persistent in UI | 10-20% |
| Campaign | Push, email, in-app trigger | 5-15% |

**Rule:** Always have an onboarding paywall. Most conversions happen when motivation is highest.

**Load `<state_root>/skills/paywall/references/placement.md`** for timing and trigger strategies.

## Core Layout Elements

Every high-converting paywall includes:

1. **Value proposition** — What they get (benefits, not features)
2. **Plan options** — Usually 2-3, with one highlighted
3. **Price display** — Clear, with anchoring if applicable
4. **CTA** — Single action, prominent
5. **Trust signals** — Trial terms, cancel anytime, reviews

**Load `<state_root>/skills/paywall/references/layout.md`** for design patterns and examples.

## Pricing Display

| Pattern | Effect |
|---------|--------|
| Monthly equivalent | "Just $4.99/mo" for yearly |
| Savings badge | "Save 50%" on annual |
| Decoy plan | Makes target plan look better |
| Price anchoring | Show "was $X" or compare to alternatives |

**Default selection matters.** Pre-select the plan you want users to buy.

**Load `<state_root>/skills/paywall/references/pricing.md`** for plan structures and psychology.

## Copy Rules

- **Benefits over features.** "Unlimited exports" -> "Never hit a limit"
- **Specific outcomes.** "Save 4 hours/week" beats "Save time"
- **Risk reversal.** "Cancel anytime" near CTA
- **Social proof.** "Join 50,000+ subscribers"

**Load `<state_root>/skills/paywall/references/copy.md`** for formulas by paywall type.

## Testing Priority

Test in this order (highest impact first):

1. **Price points** — Test every 6-12 months minimum
2. **Plan presentation** — Which plan is default, how many shown
3. **Layout** — Full redesigns, section order
4. **Copy** — Headlines, benefit framing
5. **Timing** — When paywall appears

**Rule:** Always A/B test paywall changes. Even "obvious" improvements can backfire.

**Load `<state_root>/skills/paywall/references/testing.md`** for metrics, sample sizes, and experiment design.

## Red Flags

Required protections:
- No onboarding paywall -> Add one
- Only monthly plan -> Add annual option
- Cluttered with options -> Simplify to 2-3 plans
- No trial/guarantee -> Add risk reversal
- Can't test remotely -> Implement remote config

## Research anchors

**Load `<state_root>/skills/paywall/references/sources.md`** for store policy and monetization research URLs used in this refactor.
