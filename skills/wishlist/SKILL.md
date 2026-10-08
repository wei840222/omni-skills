---
name: wishlist
description: >
  Capture wants, track target prices, prioritize purchases, and log bought items
  in a local wishlist. Use when the user says they want something, asks what to
  buy next, wants price alerts or deal timing for saved items, reviews stale
  wants, or records a purchase from the list. Not for gift ideas for other people
  (`gifts`), one-shot buy-vs-wait advice without a saved list (`shopping` /
  `price`), checkout execution (`buy`), or household budget math (`money` /
  `expenses`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⭐"}'
  related-skills: '{"shopping":"Product research and buy-vs-wait once a wishlist item is ready for a purchase decision.","price":"Fair-value and sale-legitimacy checks when the question is the price itself, not list hygiene.","buy":"Checkout, order placement, and scam checks after the user decides to purchase a saved item.","gifts":"Gift ideas and occasion tracking for other people rather than the user own wants list.","money":"Affordability, cash-flow timing, and budget ceilings before committing a must-have spend.","expenses":"Post-purchase spend logging after an item moves to purchased.","remind":"Calendar nudges for sale windows or review dates once the list decision is set."}'
---

## When to use

Load for **personal want capture and purchase timing**:

- "I want … / add this to my wishlist"
- "What should I buy next?" / priority surfacing
- Price check or alert against saved targets
- Monthly relevance review of stale items
- Move a bought item into the purchased log

Hand off when a sibling owns the job:

| Job | Skill |
|-----|-------|
| Gift ideas for someone else | `gifts` |
| One-shot product pick without list state | `shopping` |
| Sale legitimacy / fair value only | `price` |
| Place the order / negotiate checkout | `buy` |
| Can I afford this / debt vs save | `money` |
| Log the spend after purchase | `expenses` |
| Timed nudge without list mutation | `remind` |

## State location

Wishlist state may exist in `<workspace>/wishlist/`, `<workspace>/memory/wishlist/`, or `~/wishlist/`. `<workspace>` means the workspace root provided by the host/runtime, not the shell CWD.

Before any state read or write, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/wishlist/`, `<workspace>/memory/wishlist/`, `~/wishlist/`.
3. If none exists and the user asks to save durable wishlist data, create `<workspace>/wishlist/` only after consent.
4. If multiple candidates exist, use only the highest-precedence path, report the duplicates, and leave the others untouched.

Use the selected `<state_root>` for every state operation in this skill. Create only the resolved filesystem path; the placeholder name `<state_root>` is documentation-only.

Legacy path `~/Clawic/data/wishlist/` is a migration source only. Propose copy, validation, cutover, and rollback; do not move or delete automatically.

## Setup

After resolving `<state_root>`, if `<state_root>/settings.md` is missing, read `references/setup.md`. Confirm before the first write to `<state_root>`.

## Primary workflow

Execute in order. Stop early only when a step already blocks progress.

1. **Intent** — Classify: capture, prioritize, price-check, review, or purchase-log.
2. **Resolve state** — Select `<state_root>`; load `settings.md` when present.
3. **Route detail** — Load only the reference that owns the current pain:

| Bottleneck | Load |
|------------|------|
| Paths, schemas, indexes | `references/state.md` |
| Capture, priority, purchase flow | `references/domain.md` |
| First-run activation | `references/setup.md` |
| Verified consumer guidance | `references/sources.md` |

4. **Capture with friction** — For a new want, ask priority, target price/budget, and at least one product link when missing; write `items/{slug}.md` and update priority/category indexes.
5. **Decide with evidence** — Before recommending buy-now, compare current price to target and history; surface must-have items under target first.
6. **Confirm before external impact** — Draft only for purchase, cart, or payment actions; place an order or spend only with explicit current-task authorization.
7. **Write durable notes** — After consent, update the item file, indexes, `price-alerts.md`, and `purchased.md` as applicable.

## Operating rules

- Check the wishlist before suggesting an impulsive purchase of something already tracked.
- Keep card numbers, CVVs, bank logins, and full payment tokens out of every state file; retain at most last-four, nickname, or a secret pointer.
- Treat retailer countdown timers and "only N left" copy as weak urgency signals; evaluate the item at regular price first.
- Prefer ranges and observed prices; leave market averages blank when not measured.
- Review must-have and want items at least monthly: still relevant, still needed, still the right target?

## Progressive enhancement

1. Capture name + priority.
2. Add target price and links.
3. Enable price checks / alerts from `settings.md`.
4. Monthly relevance review; move bought items to `purchased.md`.
