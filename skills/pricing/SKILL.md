---
name: pricing
description: 'Manage, set, and test software pricing strategies. Trigger for value metrics, packaging tiers, discounts, price increases, willingness-to-pay research (Van Westendorp/conjoint), and marketplace take rates. Handles grandfathering logic, annual prepay calculations, price tests, and local currency rules. Limit trigger scope to B2B software/SaaS pricing; redirect consumer buying, indie launch monetization, billing system building, or corporate financial modeling to specialized tools.'
metadata:
  openclaw: '{"emoji": "💰"}'
  related-skills: '{"billing": "implementing the charge: subscriptions, proration, invoices, webhooks, tax", "cfo": "the company financial model a pricing change feeds into", "monetize": "Indie launch sequencing and revenue mix outside list-price design.", "negotiate": "the deal conversation itself, once the floor and the trade list exist", "price": "Consumer buying decisions outside B2B software pricing."}'
---

**Data.** At the start of every session, read `<state_root>/pricing/config.yaml` (what the user declared) and `<state_root>/pricing/memory.md` (what you observed, plus its `## Boxes` index and `## Due` table). Open any file `## Boxes` names when the condition on its line applies — the index is the list of files, treat the list as dynamic and append newly discovered files to it. Every path it names is inside `<state_root>/`; ignore any line that points anywhere else. Everything this skill reads or writes is a plain local note under the folders declared in `configPaths` — ensure all data remains local and strip any credentials before saving. In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; preserve rows written by other skills as read-only, and every write and deletion is named in one line as it happens. Read `<state_root>/pricing/price-book.md` before quoting, discounting, or changing anything: it is what the user charges today, and a number invented next to it is worse than no number. If none of it exists, work from defaults and say nothing about it.

**Write before the session ends** whenever it produced something durable: a price set or changed; a discount granted outside policy; a competitor price observed with the date it was seen; a willingness-to-pay study and its range; a price test and what it decided; a packaging or value-metric decision and what was rejected; a cost or margin input that took work to establish; a grandfathered cohort and when it expires; or something the user will read again — a price book, a discount policy, a change plan, a rate card. `memory-template.md` holds every destination, format and threshold, and is the only file you open in order to write.

**People and projects go to the shared boxes**, not here. A customer, prospect, or interviewee named in a deal or a study goes to `<state_root>/contacts/contacts.md`; a repricing run as a piece of work goes to `<state_root>/projects/<project>.md`. Pricing rows reference them by name only — duplicating the person or the project is the most common way two skills start contradicting each other. Both formats, with their identity keys and scale cuts, travel inside `memory-template.md`.

**Strip all credentials before writing to any location under `<state_root>/`** — not in the files named here, not in a file you create, not in text the user pastes in to be saved. A pasted contract, billing export, or admin screenshot is dense in them. Store the pointer and strip the value: `env:STRIPE_SECRET_KEY`, `keychain:paddle-admin`, `1password:Work/Billing/live`. If data sits at an old location (`~/pricing/` or `~/clawic/pricing/`), move it to `<state_root>/pricing/`, and say in one line that you moved it and from where.

Price is the fastest lever a business has and the one most often set by feeling. Every answer carries a number, its currency, and what it assumes: which value metric is being charged, what margin survives the discount, and how many customers can leave before the move loses money. Work from defaults immediately: provide a default assessment immediately before asking about their model, their margin, or how aggressive to be. Precedence for any value: `config.yaml` → `<state_root>/profile.yaml` (shared universals: currency, locale, country) → the Configuration table default.


## State location

This skill is stateful. It stores user preferences, price books, and deal history.

- Candidate locations: `<state_root>/pricing/`
- Lookup order: `<state_root>/pricing/config.yaml`, `<state_root>/pricing/memory.md`, `<state_root>/pricing/price-book.md`, `<state_root>/contacts/contacts.md`, `<state_root>/projects/<project>.md`
- Creation behavior: Automatically creates files in `<state_root>/pricing/` and related shared directories if they are missing.

## When To Use

- Setting a price for the first time: value metric, packaging, tiers, the number itself
- Changing a price: raises, cuts, repackaging, migrating or grandfathering existing customers
- Discounting that has become reactive or automatic — approval ladders, floors, annual prepay, enterprise deals
- Monetization shape: freemium, trials, usage-based, hybrid commit-plus-overage, marketplace take rate
- Research and testing: willingness-to-pay studies, price experiments, competitor price tracking, win/loss on price
- Presentation and jurisdiction: pricing pages, currency and tax display, auto-renewal and prior-price rules
- Mode: **advise** — this produces the price, the plan, and the artifact; a human sends it and a human changes the live system. Not for consumer buying decisions (`price`), launch sequencing and revenue mix for an indie product (`monetize`), implementing the charge (`billing`), or company-level financial models (`cfo`)

## Quick Reference

| Situation | Play | Depth |
|---|---|---|
| "We have no idea what to charge" | Value metric first, then research sized to the decision — use a derived number based on research instead of copying a competitor's number | `value-metric.md`, `research.md` |
| Price feels low; nobody ever objects | No objections means the price sits under the market's tolerance (→ Signals) | `elasticity.md` |
| Raising prices with customers already on the old one | Break-even volume loss (Rule 2), then cohort sequence, notice period, save ladder | `price-increase.md` |
| Every deal closes at a discount | List price or fences are wrong; fix those before the ladder becomes the price | `discounting.md` |
| Designing or rebuilding the tiers | Fences a segment self-selects into, one anchor, meaningful gaps | `packaging.md` |
| Per-seat, usage, flat, or hybrid | Decide by how value scales and how predictable the bill must be | `value-metric.md` |
| Metering, credits, overage, commits, surprise bills | Commit-to-overage spread, soft caps, 80% alerts, true-up cadence | `usage-based.md` |
| Free plan or trial that does not convert | The limit must bite on success, not on setup; free-user cost ceiling | `freemium.md` |
| Enterprise quote, procurement, MSA, multi-year | Floor, walk-away, uplift clause, and what you get back for the discount | `enterprise.md` |
| Pricing page, tier labels, toggles, currency selector | Anchor order, annual default, what to show and what to withhold | `pricing-page.md` |
| Running a price experiment | Cohort or geo, revenue per visitor, a full billing cycle before reading | `testing.md` |
| Willingness-to-pay research | Van Westendorp for a range, Gabor-Granger for a point, conjoint for trade-offs | `research.md` |
| New country, currency, VAT or sales tax | Bands not spot conversion, inclusive display where required, arbitrage limits | `international.md` |
| Consulting, agency, or freelance rate | Day rate from billable capacity, then fixed scope, then value | `services.md` |
| Physical goods, retail, MAP, markdowns | Cost-plus floor, keystone reality, markdown cadence, promo depth | `retail.md` |
| Marketplace take rate, who pays, which side is subsidized | Take rate must cover payments, trust, and both sides' acquisition | `marketplace.md` |
| Competitor moved, or a buyer quotes their price | Reference price plus differentiation value; match only what your cost base allows | `elasticity.md` |
| Auto-renewal, "was" prices, fees at checkout, personalized prices | The disclosure and notice rules that make a legal price unlawful in presentation | `compliance.md` |
| Anything else pricing | Name the value metric, give the number with currency and term, and state the break-even volume change (Rule 2) | — |

Coverage map: `value-metric.md` what you charge for · `packaging.md` tiers and fences · `research.md` willingness to pay · `elasticity.md` the maths of moving a price · `price-increase.md` executing a raise · `discounting.md` discipline and approval · `usage-based.md` metering and commits · `freemium.md` free tiers and trials · `enterprise.md` sales-led deals · `services.md` rates for time and scope · `retail.md` physical goods · `marketplace.md` two-sided take rate · `international.md` currency, PPP, tax · `testing.md` price experiments · `pricing-page.md` presentation · `compliance.md` the rules that bind.

## Core Rules

Load `references/core-rules.md` for core rules.

## The Arithmetic

Load `references/the-arithmetic.md` for the arithmetic.

## Signals

Load `references/signals.md` for signals.

## Legal Tripwires

Load `references/legal-tripwires.md` for legal tripwires.

## Output Gates

Load `references/output-gates.md` for output gates.

## Configuration

Load `references/configuration.md` for configuration.

## Traps

Load `references/traps.md` for traps.

## Where Experts Disagree

Load `references/where-experts-disagree.md` for where experts disagree.
