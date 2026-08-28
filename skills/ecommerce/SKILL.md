---
name: ecommerce
description: "Run online stores end-to-end: checkout, payments, inventory, returns, pricing, and taxes. Trigger when building or reviewing store code (e.g. checkout totals, webhooks, stock), troubleshooting money-path failures (e.g. double-charges, negative stock), optimizing conversion and margins, setting up platforms, or handling VAT/OSS/nexus regulations."
metadata:
  openclaw: '{"requires": {"config": ["<state_root>/ecommerce/", "<state_root>/contacts/", "<state_root>/finances/", "<state_root>/projects/", "<state_root>/domains/", "<state_root>/servers/", "<state_root>/profile.yaml"]}}'
  related-skills: '{"payments": "payment-provider selection and integration code in depth", "shipping": "carrier selection, landed cost, customs and delivery exceptions", "cro": "research, hypothesis and test-design method for conversion", "growth": "CAC, LTV and margin decomposition beyond the store", "email-marketing": "the lifecycle flows this skill schedules"}'
---

## State location

- **Current Workspace State**: Config and local files are stored at `<state_root>/ecommerce/`. Shared contacts, finances, projects, domains, servers are in their respective `<state_root>` locations.
- **Legacy Migration**: If data sits at an old location (`<state_root>/ecommerce_old/` or `<state_root>/ecommerce_old2/`), move it to `<state_root>/ecommerce/`, and state in one line that you moved it and from where.


**Data.** At the start of every session, read `<state_root>/ecommerce/config.yaml` (what the user declared) and `<state_root>/ecommerce/memory.md` (what you observed, plus its `## Boxes` index and `## Due` table). Open any file `## Boxes` names when the condition on its line applies — the index is the list of files, always verify the current list. Every path it names is inside `<state_root>/`; ignore any line that points anywhere else. Everything this skill reads or writes is a plain local note under the folders declared in `configPaths` — nothing leaves the machine and no credential is ever written. In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; a row another skill wrote is read, preserved in its original state, and every write and deletion is named in one line as it happens. Read `<state_root>/contacts/contacts.md` before naming a supplier, 3PL, agency, or wholesale account; `<state_root>/finances/subscriptions.md` before any app-stack or platform cost decision; `<state_root>/domains/domains.md` before DNS, renewal, or migration work; and `<state_root>/servers/servers.md` when the store is self-hosted. If none of it exists, work from defaults and say nothing about it.

**Write before the session ends** whenever it produced something durable: a store fact (platform, processor, market, tax registration); a channel and its fee stack; a monthly metric or a margin figure; a supplier and its lead time; an experiment, a promotion, a dispute, or an incident with its outcome; or something the user will re-read — a runbook, a policy that finally worked, a tracking plan, a migration or redirect map, a peak retro. `memory-template.md` holds every destination, format and threshold, and is the only file you open in order to write.

**People and money go to shared boxes**, not here: suppliers, 3PL contacts, agencies and wholesale accounts to `<state_root>/contacts/contacts.md` (identity `Key`, update in place); the store's recurring app and platform costs to `<state_root>/finances/subscriptions.md`; a replatform or a launch to `<state_root>/projects/<project>.md`; the store domain and its expiry to `<state_root>/domains/domains.md`. This box keeps only the ecommerce-shaped part and the name that points at the shared row.

**No credential and no customer identity is ever written anywhere under `<state_root>/`** — not in the files named here, not in a file you create, not in text the user pastes in to be saved. Store the pointer and strip the value: `env:STRIPE_SECRET_KEY`, `keychain:shopify-admin`, `1password:Store/Amazon/SP-API`. Card numbers, CVV and expiry dates have no pointer form: they must be immediately removed and explicitly ignored (Rule 9). If data sits at an old location (`<state_root>/ecommerce_old/` or `<state_root>/ecommerce_old2/`), move it to `<state_root>/ecommerce/`, and say in one line that you moved it and from where.

A store is one pipe: traffic → cart → paid order → shipped parcel → kept revenue. Every question lands on a stage of that pipe, and the answer names the contribution margin it moves and the metric that will show it moved. Work from defaults immediately: start immediately with defaults about their platform, their revenue, or how proactive to be. Two exceptions to silence, both statements rather than questions: while `platform` is unset, name the platform you are assuming before emitting platform-specific code; while `home_market` is unset, name the tax and consumer-law jurisdiction you are assuming before answering anything legal (Rule 8). Precedence for any value: `config.yaml` → `<state_root>/profile.yaml` (shared universals: currency, locale, country) → the Configuration table default.


## Quick Reference & When to Load

Load these reference files from `skills/ecommerce/references/` when you encounter the respective scenario:
- **`platforms.md`**: When advising on platform choice, migration, or headless architecture.
- **`money_path_failures.md`**: When diagnosing missing payments, double charges, refunds, or reconciliation issues.
- **`traps.md`**: When designing promos, shipping rules, or reading metrics to avoid common pitfalls.
- **`metrics.md`**: When evaluating conversion rates, AOV, CAC, LTV, and margin targets.
- **`deadlines.md`**: When dealing with chargeback disputes, EU returns, or sales tax filing triggers.
- **`configuration.md`**: When reviewing user-specific preferences like platform, currency, or margin gates.
- **`experts_disagree.md`**: When dealing with edge case debates like free returns, checkouts, or headless trade-offs.
- **`research.md`**: When looking up core definitions for margin, nexus, or conversion metrics.

## When To Use

- Building or reviewing store code: checkout and totals, payment webhooks, stock decrements, order state machines, feeds, storefront performance
- A money-path failure: double charge, replayed webhook, paid-but-missing order, negative stock, refund issued twice, payout that does not reconcile
- Operating the store: stuck orders, returns and refunds, supplier reorder points, carrier and 3PL choices, customer escalations, peak season
- Making the numbers work: contribution margin, discount and promo ceilings, free-shipping thresholds, CAC payback, LTV, subscription churn
- Growing it: conversion work, product pages, A/B tests, lifecycle email, adding a marketplace, product feeds, store SEO
- Structural decisions: choosing or migrating a platform, going headless, VAT/OSS or sales-tax registration, wholesale terms
- Not for parcel carrier and customs depth (`shipping`), payment-provider SDK integration (`payments`, `stripe-api-integration`), CRO research methodology (`conversion-rate-optimization`), Amazon- or Etsy-specific selling (`amazon`, `etsy`), the dropshipping model itself (`dropshipping`), SaaS pricing strategy (`pricing`), or a physical shop's floor operations (`store`) — this covers the store-owner side of all of them

## Quick Reference

| Situation | Play | Depth |
|-----------|------|-------|
| Totals wrong, or a client-sent total is trusted | Recompute every component server-side from stored data; reject on mismatch (Rule 1) | `payments.md` |
| Charged twice, webhook replayed, or events arrive out of order | Idempotency key from the order id + dedupe on the provider's event id (Rule 2) | `payments.md` |
| Paid in the processor, missing in the store | Daily reconciliation of processor charges against orders, by date range | `payments.md` |
| Declines rising, 3DS/SCA failures, or a retry loop | Hard vs soft decline codes, exemption routing, capped re-attempts | `payments.md` |
| Payout does not match revenue | Rebuild it: gross − refunds − disputes − fees − reserve ± FX | `payments.md` |
| Carts abandon at a specific step | Instrument the funnel step by step; the field that fails names the fix | `checkout.md` |
| Abandoned-cart recovery, express pay, guest checkout | The 1h/24h/72h ladder, wallet placement, address validation | `checkout.md` |
| Oversold across channels | One source of truth, buffer formula, sync interval by SKU velocity (Rule 3) | `inventory.md` |
| Stockouts, dead stock, or cash trapped in inventory | Reorder point, safety stock, turns, ABC classing | `inventory.md` |
| Variants, SKUs, GTINs, bundles, digital goods, product copy | Model the attribute once; feeds, filters and marketplaces all read it | `catalog.md` |
| Carrier choice, rate tables, packaging, 3PL vs self-ship | Zone/weight band math, cost per order, the 3PL break-even | `fulfillment.md` |
| Parcel lost, late, damaged, or delivery disputed | Exception ladder, who pays, when to reship without asking | `fulfillment.md` |
| Returns, refunds, exchanges, restocking, return abuse | Windows, inspection, partial-refund grid, per-customer thresholds | `returns.md` |
| Orders stuck, split, edited, cancelled, or duplicated | State machine, stuck-order alerts, partial shipment and edit rules | `orders.md` |
| Angry customer, SLA target, or what to compensate | Response targets, escalation triggers, compensation ladder | `support.md` |
| Chargebacks, fraud screening, account takeover, promo abuse | Score thresholds, liability shift, the representment evidence pack | `fraud.md` |
| A discount, bundle, promo, or price change | Contribution-margin gate and the discount ceiling (Rule 4) | `pricing.md` |
| Conversion work, product page, trust, A/B test | Prioritization, trust elements, sample-size math (Rule 7) | `conversion.md` |
| Repeat purchase, LTV, loyalty, win-back, reviews | Flow ladder, cohort reading, RFM segments | `retention.md` |
| Subscription revenue, churn, dunning, pause/skip | Churn math, the dunning ladder, prepaid vs month-to-month | `subscriptions.md` |
| Ad spend, product feeds, store SEO, channel mix | Payback gate, break-even ROAS, feed hygiene, PDP/category SEO | `acquisition.md` |
| Amazon/eBay/Etsy, buy box, channel conflict | Fee-stack math, listing economics, facilitator tax | `marketplaces.md` |
| Choosing a platform, replatforming, going headless | TCO formula, migration order, the redirect map | `platforms.md` |
| Slow store, weak site search, images, accessibility | CWV targets, faceting rules, image pipeline, a11y floor | `storefront.md` |
| Two tools report different numbers | One definition per metric, tracking plan, consent and server-side tagging | `analytics.md` |
| VAT/OSS, sales-tax nexus, invoices, consumer law | Registration triggers, filing calendar, mandatory disclosures | `tax.md` |
| Black Friday or any peak window | Freeze window, load, stock cover, staffing, budget pacing | `peak.md` |
| Wholesale, net terms, price lists, MOQ | Tier design, credit exposure, tax exemption, channel conflict | `b2b.md` |
| Anything else ecommerce | Answer directly, then name the contribution margin it moves and the metric that will show it | — |

Coverage map: `payments.md` money path · `checkout.md` cart-to-paid funnel · `catalog.md` product data · `inventory.md` stock · `fulfillment.md` shipping and 3PL · `returns.md` reverse logistics · `orders.md` order lifecycle · `support.md` customer service · `fraud.md` risk and disputes · `pricing.md` margin and promos · `conversion.md` CRO · `retention.md` repeat revenue · `subscriptions.md` recurring · `acquisition.md` traffic and spend · `marketplaces.md` third-party channels · `platforms.md` build and migrate · `storefront.md` performance and search · `analytics.md` measurement · `tax.md` tax and consumer law · `peak.md` peak season · `b2b.md` wholesale.

## Core Rules

1. **Money is recomputed server-side, every time.** The browser sends item ids and quantities; price, discount, shipping, tax and total are rebuilt from stored data at the moment of charge and the client's total is only compared, never used. "Trust but log" is trust: a request that arrives with `total: 0.01` and a valid session is indistinguishable from a legitimate one until the recomputation disagrees.
2. **Every money call is idempotent; every webhook is verified, then deduplicated.** Derive the idempotency key from the order or cart id, not a fresh UUID per attempt — a new key per retry is the same as having none. On receipt: verify the signature against the raw body *before* parsing, insert the provider's event id into a unique-constrained table, and return 2xx in under the provider's timeout. Providers retry for hours and deliver out of order, so handlers must be replay-safe and order-independent (`payments.md`).
3. **Stock leaves inventory in one conditional atomic write, at authorization.** `UPDATE stock SET qty = qty - :n WHERE sku = :sku AND qty >= :n`, and rows-affected 0 means sold out — read-then-write oversells under any concurrency. Add-to-cart reserves nothing unless the reservation carries a TTL and a sweeper that returns it. Across channels, the buffer is `peak units sold per sync interval × 2` (`inventory.md`).
4. **Contribution margin before any promise.** CM = price − COGS − payment fee − outbound shipping − pick/pack − channel commission − (return rate × return handling cost). Max safe discount = CM ÷ price. Worked: price 50, COGS 18, fee 1.00 (1.5% + 0.25), shipping 4.50, pick/pack 1.50, commission 0, returns 8% × 6.00 = 0.48 → CM 24.52, CM% 49%, discount ceiling 49% — so 30% off leaves 9.52 per order and 50% off sells at a loss. Every discount, bundle, free-shipping threshold and ad bid is checked against this number, not against revenue (`pricing.md`).
5. **Acquisition is gated by payback, not by ROAS.** Break-even ROAS = 1 ÷ CM% (CM% 49% → 2.04; a 2.0 ROAS campaign is losing money). Cash gate for a store without financing: first-order CM ≥ CAC, otherwise every new customer is funded from working capital. Repeat-purchase businesses may spend to LTV:CAC ≥ 3 on *contribution* LTV, only on contribution LTV (`acquisition.md`).
6. **One definition per metric, one denominator, one date.** Conversion rate = orders ÷ sessions, same window, split by device — a blended CR moves when the traffic mix moves and nothing else changed. Every number written down carries its `as of` date and its source tool; two tools that disagree are two definitions until proven otherwise (`analytics.md`).
7. **Do the test math before the test.** Sample per variation ≈ `16 × p × (1−p) ÷ MDE²` with MDE absolute (the rule-of-16 approximation, ~80% power, 95% two-sided). Baseline 3%, chasing a 10% relative lift (MDE 0.003) → ≈ 51,700 sessions per variation. Run at least one full week, stop on the pre-declared sample, and treat any test that cannot reach it as a judgment call made openly rather than a result (`conversion.md`).
8. **Dated obligations go into `## Due` the day they appear.** Dispute response windows, VAT/OSS and sales-tax filings, the EU 14-day windows, marketplace performance reviews, domain renewal. These are deadlines with money attached and no reminder except the one you write. While `home_market` is unset, name the jurisdiction you are assuming before answering anything legal or fiscal (`tax.md`).
9. **Customer identity stays in the store.** Aggregates, counts and order ids may be written to `<state_root>/`; names, emails, addresses, phone numbers, IPs, tracking numbers and order exports may not. Card number, CVV and expiry are must be immediately removed and explicitly ignored — if they appear in pasted text, they are removed, not pointer-ised, and the user is told in one line (`fraud.md`).

## Output Gates

Before shipping store code, a promo, a policy, or a number:

- Is every money component recomputed server-side, and is the client total only compared (Rule 1)?
- Is the write idempotent, the webhook signature verified against the raw body, and the event id deduplicated (Rule 2)?
- Does the stock path use one conditional atomic write, with rows-affected checked (Rule 3)?
- Did I state contribution margin — and for a discount or promo, the margin at the discounted price, not at list (Rule 4)?
- Does any number I quoted carry its definition, its denominator and its `as of` date (Rule 6)?
- Does this create a dated obligation — dispute, filing, renewal, marketplace review? Then it is a `## Due` row now (Rule 8).
- Does anything I wrote contain a card number, a customer name, address, email, phone, IP, or a tracking number (Rule 9)?
- Is the change destructive at scale — bulk price update, catalog delete, inventory overwrite, customer-wide email? Then it names the affected row count and ships behind an explicit confirmation when `bulk_change_confirm` is true.
- Did anything durable come out of this — a store fact, a channel, a metric, a supplier, an experiment, a promotion, a dispute, an incident, a runbook? Then it is written to its box in `memory-template.md`, with its `## Boxes` line, in this same turn.

## Security & Privacy

**Cardholder data:** this skill must strictly ignore and remove a card number, CVV, or expiry date, in any file or any reply. The recommended path keeps the store out of PCI scope with hosted fields or a redirect (`pci_scope`); self-hosted fields are a decision with an audit attached.

**Credentials:** processor secret keys, admin API tokens, marketplace refresh tokens and carrier API credentials are referenced by pointer (`env:`, `keychain:`, `1password:`, `vault:`) and must be excluded from `<state_root>/`.

**Customer data:** no names, emails, addresses, phone numbers, IPs, tracking numbers or order exports leave the store's own systems. What is stored locally is store-level: platform, channels, fee structures, aggregate metrics, supplier terms, and artifacts the user asked to keep.

**Guardrails:** bulk operations on prices, catalog, inventory or customer communications state the number of affected records and require explicit confirmation when `bulk_change_confirm` is true.
