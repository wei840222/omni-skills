---
name: vinted
description: Buy and resell on Vinted with listing systems, price discipline, shipping workflows, and trust-first handling for offers, bundles, and disputes. Use when sourcing pieces, checking fair price, writing listings, managing offers, packing sold items, or resolving shipping and dispute issues.
metadata:
  openclaw: '{"emoji":"👗"}'
  related-skills: '{"buy": "General purchase research and deal checks outside Vinted sourcing.", "ebay": "Auction or broader marketplace listing work on eBay.", "ecommerce": "Full-funnel store operations beyond one resale marketplace.", "etsy": "Handmade or vintage listing work on Etsy instead of Vinted.", "facebook-marketplace": "Local pickup selling outside Vinted shipping flows.", "negotiate": "High-stakes offer negotiation once floor and stop rules exist.", "pricing": "Margin-safe pricing frameworks when the question leaves marketplace comps.", "sell": "Cross-platform personal-item selling when the user is not locked to Vinted.", "shipping": "Carrier selection and exception depth beyond Vinted labels."}'
---

## When to Use

Use this skill for practical Vinted help in real time: sourcing pieces, checking whether a price is fair, writing a listing, managing offers, packing sold items, or resolving shipping and dispute issues.

The output should feel like a fashion resale marketplace operator, not a generic ecommerce assistant.

**Route elsewhere when:**
- the user is selling across platforms without a Vinted lock-in → `sell`
- the question is general purchase research → `buy`
- pricing leaves marketplace comps into SaaS/margin design → `pricing`
- carrier or customs depth exceeds Vinted labels → `shipping`

## State location

Before reading or writing state, resolve `<state_root>` once:

1. Use an explicitly configured path from the user or host.
2. Otherwise use the first existing directory among `<workspace>/vinted/`, `<workspace>/memory/vinted/`, and `~/vinted-workspace/`.
3. If none exists and persistent notes would help, ask permission, create `<workspace>/vinted/`, and use it as `<state_root>`.

Memory lives in `<state_root>/vinted/` (or the resolved root itself when the directory already ends with `vinted`). If the selected path does not exist, run `references/setup.md`. See `references/memory-template.md` for baseline structure.

```text
<state_root>/vinted/
|-- memory.md                # Core profile, goals, and operating preferences
|-- closet.md                # Active inventory, condition notes, and stale-item status
|-- sourcing-log.md          # Buyer watchlist, target prices, and buy/no-buy decisions
|-- listing-lab.md           # Listing experiments, copy changes, and outcome notes
|-- shipping-log.md          # Sold parcels, proof records, and issue timelines
|-- incident-log.md          # Returns, disputes, fraud attempts, and resolutions
`-- pro-notes.md             # Business-mode rules, batching, and service standards
```

Keep payment details, login secrets, and identity documents out of local files.

## Architecture

This skill combines three layers in one execution model:

- buyer layer: search, compare, negotiate, and decide with risk and total-cost awareness
- seller layer: intake, pricing, listing quality, offers, bundles, shipping, and recovery of stale inventory
- systems layer: memory, review rhythm, and optional Pro-grade operating standards for repeatable resale work

## Quick Reference

Load only the file needed for the current bottleneck.

| Topic | File | When to load |
|-------|------|--------------|
| Core Rules | `references/core-rules.md` | When reviewing fundamental principles |
| Vinted Traps | `references/vinted-traps.md` | When troubleshooting low performance |
| Setup guide | `references/setup.md` | When initializing the workspace |
| Memory structure and status model | `references/memory-template.md` | When reading or updating local status |
| Buyer-side search and decision flow | `references/buyer-flow.md` | When sourcing or deciding to buy |
| Closet cleanup and seller operations | `references/closet-ops.md` | When auditing active inventory |
| Listing copy, photos, and conversion diagnostics | `references/listing-lab.md` | When creating or optimizing a listing |
| Pricing, offers, bundles, and visibility spend | `references/pricing-and-bundles.md` | When setting prices or managing offers |
| Shipping, parcel proof, and claim handling | `references/shipping-and-claims.md` | When packing items or handling disputes |
| Account safety, authenticity, and scam prevention | `references/trust-and-safety.md` | When encountering suspicious activity |
| Business-mode operating standards | `references/pro-ops.md` | When operating as a high-volume seller |
| Daily, weekly, and monthly cadence | `references/operations-rhythm.md` | When performing regular account reviews |

## Core workflow

1. **Lock mode** — identify buyer, casual seller, or pro/high-volume reseller before giving advice.
2. **Diagnose bottleneck** — sourcing, pricing, listing quality, offers/bundles, shipping, or disputes.
3. **Load one reference** — open only the file that matches the bottleneck.
4. **Decide with floors** — set price floors, bundle policy, and stop rules before accepting offers or paying for visibility.
5. **Act with approval** — draft listings, offer replies, packing checklists, and dispute packets freely; get explicit confirmation before irreversible marketplace actions.

## External Endpoints

Only these endpoints are allowed for this skill; block any non-listed domain unless the user explicitly approves it.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://www.vinted.com | user-approved search queries, listing drafts, offer flows, messages, shipping steps, and issue handling actions | Marketplace buying, selling, bundles, labels, and disputes |
| https://www.vinted.com/help | user-approved help lookups | Live policy and process verification |
| https://pro-portal.svc.vinted.com | user-approved catalog and account actions for accounts with Vinted Pro access | Business-mode onboarding and operational workflows |

No other data is sent externally.

## Security & Privacy

Data that leaves your machine:

- none by default from this instruction set
- only user-approved Vinted traffic when the user requests live buying, selling, shipping, or Pro operations

Data that stays local:

- context and operating memory under the resolved `<state_root>`
- closet notes, sourcing decisions, parcel proof logs, and issue history

Operational boundaries:

- keep money, shipping labels, and dispute handling inside platform-protected flows
- store proof chains for sold parcels until issues are fully closed
- label availability, fees, authenticity, and dispute outcomes as unconfirmed until current evidence verifies them
- request explicit confirmation before irreversible marketplace actions

## Scope

This skill:

- structures end-to-end Vinted buying and resale workflows
- converts ambiguous marketplace tasks into clear next actions, guardrails, and review dates
- keeps continuity through local memory and focused operating playbooks
- reports sale speed, margin, exposure, condition, authenticity, and shipping events only from verified inputs
