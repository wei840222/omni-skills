---
name: uber-eats
description: Navigate Uber Eats in an approved live browser or app handoff to compare merchants, manage carts, and reach checkout safely. Use when the user asks to browse Uber Eats, draft a cart, review a checkout total, resolve an Uber Eats delivery issue, or place an Uber Eats order; use food-delivery for platform-neutral delivery advice.
compatibility: Requires an approved browser or app session for live Uber Eats actions.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🍔","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"applescript":"Builds macOS browser-control snippets when an approved Uber Eats workflow needs Apple Events.","food-delivery":"Provides delivery advice when the user is not committed to Uber Eats.","maps":"Checks delivery geography and route realism for the selected address.","safari":"Controls an approved Safari session when Uber Eats is open there.","shopping":"Compares fees, promotions, and checkout value before purchase."}'
---

## State location

Uber Eats state may exist in `<workspace>/uber-eats/`, `<workspace>/memory/uber-eats/`, or `~/uber-eats/`. `<workspace>` is the workspace root supplied by the host/runtime.

Before any state read, query, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path supplied by the user or host when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/uber-eats/`, `<workspace>/memory/uber-eats/`, `~/uber-eats/`.
3. When multiple candidate directories exist, use only the first, tell the user that separate state locations exist, and leave the other candidates unchanged.
4. When no candidate exists and the user asks to save preferences, propose `<workspace>/uber-eats/` as the creation target and obtain confirmation before creating it.
5. When no candidate exists and the host has not supplied `<workspace>`, ask for an explicit state path before creating state.

Use the selected `<state_root>` for every state operation during the run. Create the resolved directory path rather than the placeholder text.

## When to Use

Use this skill for Uber Eats-specific work involving an approved live session, saved addresses, merchant availability, promotion state, cart contents, grocery or convenience ordering, or post-order troubleshooting. For platform-neutral delivery planning, route to `food-delivery`.

## Architecture

Persistent preferences live in the resolved `<state_root>` only after the user approves saving them. For first-time setup, read `references/setup.md`; use `references/memory-template.md` when creating the initial memory file.

```text
<state_root>/
|-- memory.md       # Activation defaults, session mode, and ordering boundary
|-- addresses.md    # Approved delivery addresses and zone caveats
|-- merchants.md    # Preferred merchants, cuisine notes, and fee patterns
|-- orders.md       # Recent orders, substitutions, and issue history
`-- incidents.md    # Access failures, payment issues, refunds, and support outcomes
```

## Quick Reference

Load only the smallest file needed for the current blocker.

| Topic | File | When to load |
|-------|------|--------------|
| Setup guide | `references/setup.md` | The user has approved persistent preference setup or `<state_root>` is absent. |
| Memory template | `references/memory-template.md` | Creating or repairing approved preference files. |
| Browser and app-handoff flow | `references/browser-flow.md` | An approved live browser or app session needs control. |
| Checkout guardrails | `references/checkout-guardrails.md` | A draft cart may change or checkout is approaching. |
| Access fallback | `references/access-fallbacks.md` | The web session is blocked, blank, or shows access denial. |
| Issue recovery | `references/issue-recovery.md` | An order, payment, address, cancellation, or refund problem needs diagnosis. |
| Platform facts | `references/domain.md` | Verifying mutable delivery, fee, cancellation, or support details. |

## Requirements

- A browser or app session where the user can access Uber Eats is strongly preferred.
- Any browser reading, clicking, typing, or screenshot capture must use a host-provided browser automation path that the user has already approved in the current environment.
- Saved addresses, payment methods, and account credentials should stay inside the user's own Uber Eats browser session or app.
- Explicit approval is required before controlling the user's daily browser session, changing delivery details, editing a non-empty cart, or placing any live order.
- Without explicit current-thread approval for browser control, remain in planning mode and leave the live session untouched.

If Uber Eats web access is blocked or the browser shows `access denied`, use the fallback path and report that the live session cannot be verified.

## Control Modes

This skill supports four levels of intervention:

- **Browse mode**: inspect address, merchant cards, ETAs, fees, promos, and categories without changing cart state.
- **Draft cart mode**: open a merchant and prepare a candidate cart when the user clearly asked for an order draft.
- **Live checkout mode**: review payment, tip, notes, and total before placing the order.
- **Fallback mode**: when web access fails, use a locale route, app handoff, or manual support path instead of brittle blind automation.

Keep browse, draft-cart, and live-purchase actions distinct. A live Uber Eats session has real addresses, real payment methods, and real purchase consequences.

## Data Storage

Persistent local notes in `<state_root>/` are optional. When the user prefers a stateless session, leave state locations unchanged.

When local notes are approved, keep only durable operating context in `<state_root>/`:
- whether the skill may reuse the daily browser profile or should stay read-only
- preferred addresses, neighborhoods, and delivery caveats approved by the user
- favorite merchants, reorder patterns, and substitution preferences
- issue history worth reusing, such as access-denied loops, weak promos, or frequent cancellation friction

Store reusable preferences and operational notes only; keep account passwords, payment card data, one-time verification codes, and sensitive receipt details inside the user's authorized Uber Eats surfaces.

## Core Rules

### 1. Reuse the Real Session Only When the User Actually Wants That
- Prefer the user's already signed-in Uber Eats browser session when live state matters.
- This skill does not grant browser access by itself; it only uses an already-approved browser control path from the host environment.
- Obtain current-thread approval before activating, switching tabs, typing, clicking, or capturing screenshots from the daily browsing profile.
- When the user only wants strategy, explain the flow without opening a real session.

### 2. Lock the Delivery Address Before Comparing Merchants
- Uber Eats ordering starts with sign-in plus a delivery address.
- Merchant availability, ETA, fees, and promos depend on the active address.
- If the address is missing or ambiguous, solve that first before treating merchant cards as meaningful.

### 3. Read the Merchant and Cart State Before Touching Checkout
- Confirm merchant name, ETA, delivery fee, service fee, promo state, and cart contents before adding or editing items.
- Re-read the page after every navigation or major action.
- If the cart already contains items, obtain a preserve, edit, or replace decision before changing it.

### 4. Separate Drafting From Live Purchase
- Building a candidate cart is not the same as placing an order.
- Before any live checkout step, summarize the merchant, items, substitutions, address, ETA, fees, total, tip, payment method, and delivery notes.
- Place the final order only after explicit approval in the current thread.

### 5. Treat Address and Cancellation as High-Risk Boundaries
- Official Uber Eats help says the order flow requires a confirmed delivery address before checkout.
- After an order is placed, treat an address change as a live support question and verify available options with the delivery partner.
- Cancellation may be possible only before the merchant accepts the order or before dispatch; refund eligibility can disappear quickly.

### 6. Prepare a Fallback When the Web Session Misbehaves
- If the browser shows `access denied`, a blank screen, or another blocking page, pause interaction and read `references/access-fallbacks.md`.
- Try a supported locale route or app handoff first.
- If the session remains blocked, provide manual guidance or support recovery and state that checkout cannot proceed in the current session.

### 7. Keep Memory About Preferences, Not Secrets
- Save reusable address choices, favorite merchants, cuisine habits, substitution preferences, and known problem merchants.
- Keep short notes about what worked, what arrived late, and what needed support.
- Keep full payment data, raw support transcripts, and copied personal verification details out of local state.

## Uber Eats Traps

- Set or verify the delivery address before comparing merchants because availability and fees depend on it.
- On an `access denied` or anti-bot page, use the fallback procedure instead of continuing browser actions.
- Read a non-empty cart and obtain a preserve, edit, or replace decision before changing it.
- Compare the subtotal with delivery fee, service fee, tip, and total before recommending a purchase.
- Treat post-order address changes and cancellation eligibility as live support questions; verify the current order page before promising an outcome.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://www.ubereats.com | Addresses, search terms, cart state, checkout data, and account session cookies inside the user's own browser session | Browsing, cart preparation, checkout, and issue handling |
| Uber Eats app deep links or app continuation opened by the user | Merchant, cart, and checkout intent data | Native app continuation when browser flow is blocked or incomplete |
| https://help.uber.com/ubereats | Support requests, issue details, and help navigation opened by the user | Recovery, cancellation, address, and troubleshooting guidance |

No other data should be sent externally unless the user explicitly opens additional payment, map, or support surfaces during the Uber Eats workflow.

## Security & Privacy

**Data that leaves your machine:**
- addresses and search terms entered into Uber Eats
- cart and checkout data sent through the user's Uber Eats session
- support or issue details the user explicitly submits to Uber Eats

**Data that stays local:**
- optional Uber Eats operating notes in `<state_root>/`, only if the user wants persistent memory
- preferences, address labels, and known-good merchant patterns approved by the user

**Safety boundary:**
- Keep Uber account passwords, payment card numbers, and one-time verification codes inside the user's own authorized surfaces.
- Place a live order only after explicit current-thread confirmation.
- Re-read the current Uber Eats page before reporting a cart, address, cancellation, or refund path as available.

## Trust

By using this skill, data is sent to Uber Eats through the user's own browser or app session.
Only install and run it if you trust Uber Eats with your address, cart, payment, and order data.

## Scope

This skill helps control Uber Eats ordering through an approved live browser or app handoff, structures browse, draft-cart, live-checkout, fallback, and issue-recovery workflows, and records approved durable preferences.

**Execution boundary:**
- Verify live Uber Eats state before reporting it.
- Check the current page before making a claim about availability, ETA, promotions, cancellation, or refund outcome.
- Keep secrets and payment data out of local state.
- Treat this skill package as read-only during normal use.
