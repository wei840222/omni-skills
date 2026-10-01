---
name: glovo
description: >
  Navigate a live Glovo browser or app session to compare stores, manage carts,
  and reach checkout safely. Use when the user needs Glovo-specific browsing,
  draft-cart help, checkout confirmation, or post-order recovery with their real
  address and session. Prefer `food-delivery` for platform-agnostic ordering
  advice, `shopping` for multi-merchant value comparison, and `maps` when the
  main task is geography rather than Glovo checkout.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛵"}'
  related-skills: '{"food-delivery":"Platform-agnostic ordering preferences and multi-app comparison when the user is not locked to Glovo.","maps":"Delivery geography, area fit, and route realism around the chosen address.","safari":"Control the user real Safari session when Glovo is open there.","applescript":"macOS browser-control snippets when exact Apple Events are required.","shopping":"Fee, promo, and checkout-value comparison beyond a single Glovo cart."}'
---

## When to load

Load this skill when the next step depends on a **real Glovo session**:

- browse stores, categories, ETAs, fees, minimums, or promos inside Glovo
- prepare or edit a draft cart with the user's signed-in account
- reach checkout and confirm a live order only after explicit approval
- recover from missing items, wrong items, courier delay, or payment failure on Glovo

Route away when:

- platform-agnostic ordering advice is enough → `food-delivery`
- multi-merchant value comparison is the main ask → `shopping`
- geography / route realism is the main ask → `maps`

## State location

Candidate locations for persistent state, in order of precedence:

```text
<workspace>/glovo/
<workspace>/memory/glovo/
~/glovo/
```

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/glovo/`, `<workspace>/memory/glovo/`, `~/glovo/`.
3. If multiple candidates exist, keep the highest-priority one, leave others independent, and tell the user which location was selected.
4. If none exists and persistent state must be created, default to `<workspace>/glovo/` with brief consent on first write.

Use the selected `<state_root>` for every state path in this skill. Resolve the placeholder before any filesystem write. Never write the literal string `<state_root>` to disk. Skill resources stay under `references/` and `assets/`. Never write learned data into `SKILL.md`.

```text
<state_root>/
|-- memory.md       # Activation defaults, browser mode, and ordering boundary
|-- addresses.md    # Approved delivery addresses and area caveats
|-- stores.md       # Preferred stores, cuisines, fees, and repeat winners
|-- orders.md       # Recent orders, substitutions, and issue history
`-- incidents.md    # Payment failures, missing items, support outcomes, and fixes
```

## When to load references

Keep this file as the entry point; load the smallest matching reference.

| Need | File |
|------|------|
| First-run activation and safety mode | `references/setup.md` |
| Live browser navigation loop | `references/browser-flow.md` |
| Checkout confirmation checklist | `references/checkout-guardrails.md` |
| Missing item / delay / payment recovery | `references/issue-recovery.md` |
| Memory file schemas | `assets/memory-template.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |

## Requirements

- Prefer a browser session where the user is already signed in to Glovo.
- Browser reading, clicking, typing, or screenshots must use a host-provided automation path the user already approved in the current environment.
- Addresses, payment methods, and credentials stay inside the user's own browser or Glovo app.
- Stay in **planning mode** until the current thread grants explicit browser-control approval.
- If live Glovo access is unavailable, prepare exact browse/checkout steps instead of inventing live state.

## Control modes

Escalate only as far as the user asked:

1. **Browse mode** — inspect home, categories, stores, ETAs, minimums, fees, and promos without changing cart state.
2. **Draft cart mode** — open stores and prepare a candidate cart when the user clearly asked to build an order draft.
3. **Live checkout mode** — review the full summary and place the order only after explicit confirmation in the current conversation.

Treat the live Glovo session as containing real addresses, real payment methods, and real purchase consequences.

## Operating loop

1. **Resolve mode** — browse, draft cart, or live checkout; stay in planning mode until browser control is approved.
2. **Lock address first** — read the active Glovo address/city before treating store cards, ETAs, or fees as meaningful.
3. **Read store state** — confirm name, ETA, minimum, delivery fee, service fee, and promo state before cart edits.
4. **Inspect cart** — if items already exist, clarify preserve / edit / replace before changing anything.
5. **Compare totals** — item subtotal + fees + promo + tip + ETA together; show the tradeoff, not only headline price.
6. **Checkout gate** — before any live order action, summarize store, items, substitutions, address, ETA, fees, total, tip, payment method, and notes; proceed only after explicit current-thread approval.
7. **Verify after every action** — re-read the page or capture a screenshot; observe DOM/page changes rather than assuming clicks worked.
8. **Persist only durable preferences** — addresses labels, favorite stores, substitution habits, recurring issues; never secrets.

## Core rules

### 1. Reuse the real session only when requested

- Prefer the user's already signed-in Glovo browser session when live state matters.
- This skill does not grant browser access by itself; it uses an already-approved host browser-control path.
- Ask before activating tabs, typing, clicking, or capturing screenshots from the daily browsing profile.
- If the user only wants strategy, stay out of the real session and explain the flow.

### 2. Lock the delivery address before comparing stores

- Availability, ETA, fees, and promos depend on the active address.
- If no address is set, solve that first.
- Verify the address Glovo is actively using rather than relying on login status alone.

### 3. Read the store state before touching the cart

- Confirm store name, delivery ETA, minimum order, delivery fee, service fee, and promo state before adding items.
- Re-read the page after every navigation or major action.
- If the cart already contains items, clarify whether to preserve, edit, or replace them.

### 4. Separate drafting from live purchase

- Building a candidate cart is not placing an order.
- Before any live checkout step, summarize store, items, substitutions, address, ETA, fees, total, tip, payment method, and notes.
- Place the final order only after explicit approval in the current thread.

### 5. Compare like for like

- Compare item totals, fees, ETA, minimums, promo eligibility, and substitution risk together.
- A cheaper subtotal can still be worse after fees or slower delivery.
- When optimizing, show the real total and the tradeoff.

### 6. Keep memory about preferences, not secrets

- Save reusable address choices, favorite stores, cuisine habits, substitution preferences, and known problem stores.
- Keep short notes about what worked, what arrived late, and what needed support.
- Store only generic preference data; exclude passwords, payment cards, verification codes, and full receipts.

### 7. Handle post-order issues as their own workflow

- Missing items, wrong items, courier delay, cancellation, and refund paths need their own verification loop.
- Start with the exact order state visible in Glovo before proposing compensation or support steps.
- Record only the durable lesson after resolution.

## Failure patterns → recovery

| Failure | First recovery step |
|---------|---------------------|
| Home/store cards look wrong | Verify active address/city, then refresh the read |
| Wrong tab / wrong cart | Confirm URL/title is Glovo; inspect cart before edits |
| Non-empty unexpected cart | Ask preserve / edit / replace before changing items |
| Promo or total drift | Re-read checkout summary after every fee/promo/tip change |
| Click appears to do nothing | Re-read DOM/page state; retry once with a fresh screenshot |
| Live order risk | Stop at summary; require explicit current-thread confirmation |
| Post-order complaint | Load `references/issue-recovery.md` and verify on-screen order state first |

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| https://glovoapp.com | Addresses, search terms, cart state, checkout data, and account session cookies inside the user's own browser session | Browsing, cart preparation, checkout, and issue handling |
| Glovo app deep links or mobile handoff opened by the user | Store, cart, and checkout intent data | Native app continuation when browser flow is not enough |

No other data leaves the machine unless the user explicitly opens additional payment, map, or support surfaces during the Glovo workflow.

## Security and privacy

**Data that leaves the machine (through the user's Glovo session):**

- addresses and search terms entered into Glovo
- cart and checkout data sent through the user's Glovo session
- support or issue details the user explicitly submits to Glovo

**Data that stays local:**

- optional notes under `<state_root>/` only when the user wants persistent memory
- preferences, address labels, and known-good store patterns approved by the user

**This skill does not:**

- ask for Glovo passwords in chat
- store payment card numbers or one-time verification codes
- place live orders without explicit confirmation in the current thread
- claim a cart or checkout is correct without re-reading the actual Glovo page

## Trust

By using this skill, data is sent to Glovo through the user's own browser or app session. Install and run it only if you trust Glovo with address, cart, payment, and order data.

## Scope

**This skill does:**

- help control Glovo ordering safely through a live browser or app handoff
- structure browse, draft-cart, live-checkout, and issue-recovery workflows
- keep durable notes for addresses, stores, preferences, and recurring issues

**Out of scope:**

- claiming live Glovo state that cannot be verified on screen
- promising stock, ETA, or promo validity without checking the current page
- storing secrets or raw payment data in skill memory files
- modifying its own skill package files
