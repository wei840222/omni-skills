---
name: buy
description: >
  Research purchases end-to-end, compare sold-price comps, detect scam signals,
  time deals, and coach buyer-side negotiation scripts across consumer and B2B
  categories. Use when the user asks should-I-buy, is-this-a-good-deal, compare
  prices, spot scams, negotiate a purchase, or audit subscriptions before cancel.
  Prefer `shopping` for product-recommendation framing, `price` for pure
  price-history / sale-legitimacy timing, `negotiate` for live counterparty
  autonomy with hard limits, `home-buying` for primary-residence purchases,
  store skills (`amazon`, `walmart`, `marketplace`) for retailer-specific ops,
  and `money` / `expenses` / `subscriptions` once the buy decision becomes
  cashflow or recurring tracking.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛒"}'
  related-skills: '{"shopping":"Product recommendation and buy-vs-wait framing when the hard part is choosing what to buy rather than executing acquisition research.","price":"Price-history, dynamic-pricing, and sale-legitimacy analysis when the ask is timing rather than full purchase workflow.","negotiate":"Live counterparty negotiation with mandatory limits and approval gates; buy covers buyer research and script coaching before/around that.","home-buying":"Primary-residence purchase system with listings, offers, and closing; buy covers general purchase research outside that pipeline.","amazon":"Amazon listing, tracking, and account workflows after a general buy decision.","walmart":"Walmart basket, pickup, substitution, and restock flows.","marketplace":"Cross-platform listing, fee, and sold-price ops beyond a single retailer.","money":"Household cash-flow and affordability sequencing beyond one purchase.","expenses":"Capture spend after the buy decision.","subscriptions":"Recurring-charge inventory and renewal tracking when the ask is portfolio audit rather than one-off negotiation.","sell":"Seller listing and intake when the user is on the sell side."}'
---

This skill is stateless and does not store local configuration or persistent user state.

## When to load

Load for buyer-side acquisition help:

- "should I buy", "is this worth it", "is this a good deal"
- compare prices / sold comps / walk-away pricing
- scam or too-good-to-be-true checks
- negotiation scripts for retail, used goods, bills, SaaS, or cars
- subscription cancel / retention leverage before routing to `subscriptions`

Do **not** prefer this skill when:

- the user mainly wants a product recommendation shortlist → `shopping`
- the ask is only price history or "is this sale real?" → `price`
- a live counterparty thread needs autonomy limits / approval gates → `negotiate`
- the purchase is a primary home → `home-buying`
- the work is Amazon / Walmart / marketplace mechanics → those store skills

## Before acting

Clarify, in order:

1. Hard budget vs flexible ceiling
2. Timeline (urgent vs can wait for a sale cycle)
3. Quality / risk tolerance
4. Category (electronics, vehicle, real estate, services, B2B/SaaS, subscriptions)
5. Walk-away price (create one if missing)

## Core flow

1. **Identify** — product, service, or B2B software; constraints and non-goals
2. **Research** — category sources in `references/sources.md`
3. **Evaluate** — sold comps vs listings, red flags, timing
4. **Recommend** — buy / wait / walk with reasons and total cost
5. **Support** — negotiation scripts from `references/tactics.md` when useful

## Quick deal check

When asked "is this a good deal?":

- Compare to recent **sold** prices, not active listings alone
- Check ~3-month price trend — falling favors wait; stable/rising favors buy if the need is real
- Scan red flags below
- Separate sticker price from out-the-door / total cost (tax, fees, shipping, warranty, subscriptions)

**Red flags that usually kill the deal:**

- Price far below market without a documented reason → treat as scam risk
- Seller avoids written communication or insists on off-platform chat only
- Payment via wire / crypto / gift cards only
- "Sale" price still above the recent average
- Pressure timers, "someone else is coming", or refusal of independent inspection (vehicles / contractors)

## Decision framework

| Question | If no |
|----------|-------|
| Do I need this (not just want)? | Wait ~30 days unless urgent |
| Have I researched alternatives? | Research first |
| Is price at/below verified market? | Negotiate or walk |
| Do I have a walk-away price? | Set one before talking numbers |

All yes → proceed toward buy / negotiate.

## Negotiation basics

**Retail / services:**
> "I found this for $X at [competitor]. Can you match?"

**Used goods:**
> "Similar items sold for $X. Would you take that?"

**Bills (internet, insurance):**
> "I've been a customer X years. What can you do to keep me?"

Advanced tactics and category scripts: `references/tactics.md`.

## Category guidance

Pricing data, negotiation norms, and red flags differ by category. Load `references/categories.md` for:

- Electronics & tech
- Vehicles
- Real estate
- Services (contractors, professionals)
- B2B / SaaS
- Subscriptions

For a primary-residence purchase pipeline, hand off to `home-buying`.

## Subscription audit

When asked to review subscriptions:

1. List each with cost + last-use date
2. Flag unused (60+ days), overpriced, or redundant items
3. Provide cancellation / retention talking points
4. Calculate total savings

If the user wants ongoing inventory or renewal reminders, continue in `subscriptions`.

## Output rules

- Lead with verdict: **buy / wait / walk** (or negotiate) plus 2–4 evidence bullets
- Cite which comps or sources were checked; mark unverified claims explicitly
- Prefer sold / completed prices over asking prices
- For vehicles and contractors, require independent inspection language before any "buy" verdict
- Never invent KBB/Edmunds/Keepa numbers; look them up or say the check is still needed
- Do not place orders, send money, or message sellers unless the user explicitly authorizes that action in-session
