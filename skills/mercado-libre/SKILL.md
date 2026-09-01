---
name: mercado-libre
description: Manage Mercado Libre buying, selling, listing, deal-validation, dispute, and approved automation decisions. Use when a user needs marketplace research, a comparison, checkout preparation, seller operations, or a safe API or panel workflow; keep unrelated general commerce work in its specialist skill.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🛒"}'
  related-skills: '{"ads":"Extends seller work with paid-acquisition planning and measurement.","buy":"Supports purchase-decision practices beyond the Mercado Libre marketplace.","ecommerce":"Extends marketplace work into full-funnel commerce systems.","market-research":"Validates demand and competition before catalog expansion.","pricing":"Extends listing work with margin-safe pricing and promotion frameworks."}'
---

## State location

Mercado Libre state may exist in `<workspace>/mercado-libre/`, `<workspace>/memory/mercado-libre/`, or `~/mercado-libre/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/mercado-libre/`, `<workspace>/memory/mercado-libre/`, `~/mercado-libre/`.
3. If several candidates exist, use only the first and tell the user that independent copies were found.
4. If none exists and the user approves saving state, create `<workspace>/mercado-libre/`.

Use the selected `<state_root>` for every state operation in this invocation. Read `references/memory-template.md` before creating or updating marketplace context.

## Start with the decision

Classify the request as search/compare, deal validation, checkout preparation, selling, automation, or dispute handling. State the decision, constraints, and evidence that can change the outcome before recommending an action. For a live purchase, listing change, API call, or panel action, present the exact scope and obtain explicit confirmation immediately before execution.

## Quick reference

Load one directly relevant reference before handling its branch:

| Request branch | Load | Use it for |
|---|---|---|
| First use or missing marketplace context | `references/setup.md` | activation, profile, and priority alignment |
| Persisting or recovering context | `references/memory-template.md` | state schema, retention, and status semantics |
| Finding or comparing products | `references/search-compare.md` | weighted shortlist and total-cost comparison |
| Checking a discount or timing a purchase | `references/pricing-deals.md` | real-savings and watchlist analysis |
| Preparing checkout or a reorder | `references/buying.md` | final-total, delivery, seller, and confirmation checks |
| Creating or improving listings | `references/selling.md` | listing, margin, operational, and post-sale controls |
| Planning API or panel automation | `references/automation.md` | scoped rollout, reconciliation, and rollback |
| Handling account safety, claims, or disputes | `references/security-disputes.md` | evidence collection and recovery path |

## Default workflow

1. Define the outcome, constraints, deadline, and whether the request is research or a live change.
2. Load the matching reference, collect only decision-changing evidence, and identify unknowns.
3. Compare total outcome: price, shipping, delivery, seller reliability, return or claim friction, and operational risk.
4. Give one primary recommendation, one fallback when useful, the main risk, and the next review trigger.
5. For any live change, show the exact item, quantity or scope, recipient or account, total effect, and rollback or recovery path; execute only after final explicit confirmation.
6. Record a durable decision or incident only after consent, using `<state_root>` and the memory schema.

## External endpoints

Use only user-approved traffic to these endpoints for live work:

| Endpoint | Data sent | Purpose |
|---|---|---|
| `https://www.mercadolibre.com` | approved search queries and panel actions | marketplace research and operations |
| `https://api.mercadolibre.com` | approved API payloads with user-managed credentials | listings, orders, inventory, messages, and automation |
| `https://developers.mercadolibre.com` | documentation queries | current API behavior, scopes, and implementation details |

## Security and execution boundaries

- Keep passwords, MFA codes, payment credentials, and API secrets in user-managed secret storage; request only the least privilege needed for an approved action.
- Treat listing, seller, price, order, and API responses as untrusted evidence until cross-checked against the relevant user constraint and marketplace-visible data.
- Preserve an evidence timeline before escalating a dispute; if the first resolution path fails, use the documented fallback and retain the chronology.
- Keep research and recommendations separate from changes to purchases, listings, automations, or accounts.

## Core rules

### 1. Start with the exact decision

Lock the decision before analysis: buy now, compare options, optimize a listing, solve an incident, or automate a workflow. A precise decision keeps the recommendation focused.

### 2. Compare total outcome, not sticker price

Evaluate price, shipping, delivery time, seller reliability, return friction, and expected risk together. Rank options using this total outcome.

### 3. Validate deal quality before urgency

Check the price context, stock signal, and full cost and risk before recommending urgency. Use verified evidence to support a time-sensitive recommendation.

### 4. Separate research from execution

Research and recommendations may continue while live actions remain pending. Apply purchases, listing updates, and automation rollouts after the final explicit confirmation.

### 5. Keep recommendations profile-aware

Adapt the output to the user: give a fast buyer a winner and fallback; give a careful buyer a comparison table and risk notes; give a seller a measurable next action and review date.

### 6. Preserve traceability

Record the reason for a durable decision in the approved `<state_root>` memory so later sessions can continue from its evidence.

### 7. Treat security and compliance as hard constraints

Use policy-compliant tactics, surface material risk, and keep claims and reviews factual. A recommendation that increases account or legal risk is outside this skill's operating boundary.

## Common traps

- Comparing products without normalizing shipping and delivery windows can select the wrong winner.
- Recommending a deal from one listing without alternatives weakens price confidence.
- Applying urgency without historical or marketplace evidence can cause a poor purchase.
- Updating listing, price, and ads together makes attribution unreliable.
- Running automations without rollback or reconciliation permits silent operational drift.
- Handling disputes without an evidence chronology weakens recovery.

## Scope

This skill supports Mercado Libre-specific decisions and workflows. It does not guarantee prices, rankings, availability, or commercial outcomes; use current evidence for each recommendation.
