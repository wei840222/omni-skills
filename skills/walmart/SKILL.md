---
name: walmart
description: >
  Plan Walmart grocery and household orders with pickup timing, substitutions,
  repeat restocks, and budget-aware cart decisions. Use for weekly stock-ups,
  urgent top-offs, reorder workflows, pickup/delivery coordination, substitution
  policy, order recovery, and pharmacy-adjacent operational planning with strict
  safety limits. Prefer `grocery` for pantry/list logistics across any store,
  `shopping` for general buy-vs-wait product research, `meal-planner` for what to
  cook before the basket, `price` for deal timing outside Walmart flows, and
  `family` / `subscriptions` when the hard part is household coordination or
  recurring non-Walmart renewals.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛒","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"grocery":"Cross-store grocery lists, pantry inventory, and dietary checks; walmart owns Walmart pickup/delivery/substitution/recovery flows.","shopping":"General product research and buy-vs-wait judgment outside a Walmart-specific basket.","meal-planner":"Decide meals and recipes first; walmart turns the resulting staples into a Walmart basket.","price":"Price-history and sale-legitimacy analysis when the ask is deal timing rather than Walmart cart execution.","family":"Multi-member household logistics that may feed a shared Walmart trip.","subscriptions":"Recurring non-Walmart renewals; walmart covers store restock cadence and reorder memory."}'
---

# Walmart

Help the user plan and, only with explicit confirmation, hand off Walmart
grocery/household orders. Prefer stable Walmart account surfaces over guessed
APIs. Keep durable household notes under a resolved `<state_root>` outside this
package. Never write runtime state into the skill tree.

## State location

Walmart planning notes may exist in `<workspace>/walmart/`,
`<workspace>/memory/walmart/`, or `~/walmart/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/walmart/`, `<workspace>/memory/walmart/`, `~/walmart/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable state must be created, default to
   `<workspace>/walmart/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill.
Typical layout (create children only when needed):

```text
<state_root>/
|-- memory.md           # Household profile, store preferences, substitution rules
|-- weekly-cart.md      # Current basket with must-have vs optional items
|-- order-log.md        # Prior orders, missing items, substitution outcomes
|-- exceptions.md       # Allergy, pharmacy, age-restricted, never-substitute rules
`-- archive/            # Past carts and resolved delivery issues
```

If older notes exist only at `~/Clawic/data/walmart/`, propose a
copy/validation/cutover plan and wait for confirmation before any migration.
Never write the literal string `<state_root>` to disk. Create or update state
only after the user opts in. Store operational household rules only—no
passwords, payment data, insurance identifiers, prescription numbers, or
detailed medical history.

## When to use

- Weekly grocery stock-ups and household restocks at Walmart
- Urgent top-offs with a needed-by window
- Reorder from Purchase History / My Items
- Pickup, delivery, or mixed-fulfillment coordination
- Substitution policy for allergy, baby, pet, pharmacy, or brand-sensitive items
- Missing-item, damaged-item, or split-shipment recovery
- Pharmacy-adjacent operational planning (timing / refill workflow routing only)

Prefer adjacent skills when they fit better:

- Pantry inventory / multi-store grocery lists → `grocery`
- General product research outside Walmart → `shopping`
- Decide meals before building the cart → `meal-planner`
- Deal timing / price-history verdicts → `price`
- Multi-member household coordination → `family`
- Recurring non-Walmart renewals → `subscriptions`

## Load order

1. `SKILL.md` state rules and core rules (always)
2. `references/setup.md` + `assets/data-templates.md` on first activation
3. `references/basket-workflows.md` for weekly / urgent / reorder / mixed baskets
4. `references/substitutions-playbook.md` before proposing alternates
5. `references/automation-paths.md` before any apply / browser / seller path
6. `references/order-recovery.md` when the order already failed
7. `references/pharmacy-safety.md` for pharmacy-adjacent asks
8. `references/sources.md` when verifying research provenance

## Operating path

1. Classify trip mode and needed-by window first.
2. Resolve `<state_root>` when durable memory or logging is needed; follow
   `references/setup.md` with explicit approval if missing.
3. Build or adjust the basket by priority (`must-have`, `replaceable`,
   `nice-to-have`) using `references/basket-workflows.md`.
4. Apply substitution policy before checkout suggestions.
5. Warn about split shipping, cold-chain, ID, or pharmacy-only items.
6. For applied workflows, load `references/automation-paths.md`, refresh live
   stock/price/slot state, then require explicit confirmation before mutations.
7. On failures, use `references/order-recovery.md` and update
   `<state_root>/order-log.md` only with consent.

## Quick reference

| Topic | File | Load when |
|-------|------|-----------|
| Setup / activation | `references/setup.md` | Missing state or first use |
| File templates | `assets/data-templates.md` | Seeding memory / cart / log files |
| Basket building | `references/basket-workflows.md` | Weekly, urgent, reorder, mixed trips |
| Automation paths | `references/automation-paths.md` | Browser apply or seller Marketplace work |
| Substitutions | `references/substitutions-playbook.md` | Before proposing alternates |
| Order recovery | `references/order-recovery.md` | Missing, damaged, split, timing failures |
| Pharmacy safety | `references/pharmacy-safety.md` | Refill or pharmacy-adjacent tasks |
| Sources | `references/sources.md` | Verifying research provenance |

## Requirements

- Live ordering or account support needs access to the user's Walmart site or app session
- Browser automation needs a user-approved browser session and, only for apply mode, a user-provided runtime such as Playwright
- Repeat planning needs permission to keep local notes under `<state_root>/`
- Pharmacy-related tasks need explicit confirmation before refill or account-change workflows

Direct the user to enter passwords, payment credentials, insurance details, or
prescription identifiers on Walmart's own surfaces outside chat.

## Automation scope

Use `references/automation-paths.md` before any applied workflow.

- Official Walmart developer APIs documented for US Marketplace partners are
  seller / solution-provider APIs, not a public grocery or pickup API for
  ordinary consumer accounts.
- For consumer workflows, the reliable surface is browser-driven interaction
  with Walmart account flows such as Purchase History, My Items, checkout,
  order edit windows, and live-shopping support.
- Treat consumer automation as user-mediated and confirmation-gated: plan →
  review → apply. Browser tooling is optional for planning-only use.

## Core rules

### 1. Start with trip mode and deadline
- Classify first: weekly stock-up, urgent top-off, reorder, pickup tonight,
  delivery tomorrow, or account recovery.
- Confirm the needed-by window before recommending basket changes; slots,
  substitutions, and shipping splits depend on timing.

### 2. Build the basket by priority, not by aisle
- Structure every basket into `must-have`, `replaceable`, and `nice-to-have`.
- Put food, baby, pet, and cleaning staples first so the order still works if
  inventory changes late.

### 3. Treat substitutions as a policy
- Capture category-specific substitution rules before suggesting alternates.
- Require manual approval for allergy-sensitive, baby, pet, pharmacy, or
  strongly preferred items.

### 4. Optimize for value, waste, and reliability together
- Compare unit value, pack size, spoilage risk, and reorder frequency instead
  of chasing the lowest sticker price.
- Prefer stable household outcomes over a cheaper basket that creates waste or
  extra trips.

### 5. Separate grocery, general merchandise, and pharmacy risk
- Expect mixed baskets to behave differently across pickup, delivery, shipping,
  and refill flows.
- Call out items likely to ship separately, require ID, need cold-chain timing,
  or belong in a pharmacy-only workflow.

### 6. Verify execution conditions before high-impact actions
- Require clear user confirmation before placing orders, changing addresses,
  accepting substitutions, canceling items, or starting refill workflows.
- If live availability, pricing, or delivery windows may have changed, refresh
  that state before the final action.

### 7. Learn only the household rules that improve repeat orders
- Store only approved local notes under `<state_root>/`: store choice, pack
  size preferences, restock cadence, and substitution boundaries.
- Exclude payment data, login secrets, insurance information, and detailed
  medical data from local storage.

### 8. Prefer stable Walmart surfaces for automation
- For repeat ordering, start from Account → Purchase History → Reorder all or
  My Items → Reorder before rebuilding carts manually.
- For live delivery issues, use Chat with Shopper, the order detail view, and
  documented edit windows before ad hoc browsing.

## Common traps

- Treating Walmart like generic shopping search → the user needed a workable
  household basket, not browsing help.
- Optimizing for discounts only → cheaper items that break preferences, timing,
  or substitutions create extra trips.
- Leaving substitution rules vague → allergy, baby, pet, and brand-sensitive
  items fail fast when inventory moves.
- Mixing shipping-only items into an urgent grocery plan without warning → the
  order looks complete but arrives in pieces.
- Offering medication or dosage guidance → pharmacy workflows need operational
  help, not medical advice.
- Claiming a public consumer grocery API → Marketplace APIs are seller-side;
  consumer work stays on account UI / browser flows.
- Pretending stock, pricing, or slot availability is stable → those are live
  conditions that must be refreshed before apply.

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| https://www.walmart.com | Search terms, cart choices, account-selected order details, and order-management actions the user explicitly approves | Browse products, review carts, manage pickup, delivery, shipping, and order support |
| https://www.walmart.com/pharmacy | Refill or pharmacy-account metadata the user explicitly chooses to submit | Pharmacy workflows, pickup status, and refill operations |
| https://developer.walmart.com/us-marketplace | Seller or solution-provider registration metadata and developer documentation activity | Marketplace API docs, scopes, and sandbox guidance |
| https://developer.walmart.com/us-marketplace/reference/tokenapi | Marketplace OAuth / token documentation traffic | Seller-side auth docs for partner integrations |

No other data should be sent externally unless the user explicitly connects
another service. Do not treat `marketplace.walmartapis.com` root URLs as a
public browseable consumer API.

## Security and privacy

Data that leaves the machine:
- only the Walmart requests required for browsing, cart review, order
  management, or pharmacy workflows the user explicitly asked for

Data that stays local:
- household notes and approved workflow preferences under `<state_root>/`
- order recovery history and substitution guardrails

Out of scope:
- place or modify real orders without explicit user confirmation
- save payment credentials, passwords, or prescription identifiers in local memory
- provide medication, dosage, or interaction advice
- accept silent substitutions for sensitive categories
- modify its own skill files

## Trust

This skill relies on Walmart services for live browsing, ordering, and pharmacy
workflows. Only install and run it if you trust Walmart with the order and
account data you choose to use there.
