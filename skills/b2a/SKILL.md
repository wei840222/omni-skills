---
name: b2a
description: Design products and services for AI agents as buyers. Use when making
  offerings agent-discoverable, exposing machine-readable catalogs and pricing,
  supporting autonomous purchasing or replenishment, or competing on structured
  data instead of human marketing.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🤖"}'
---

## When to Use

Use when the user is building or adapting products/services so **AI agents** can discover, compare, trial, purchase, or reorder without a human UI:

- Expose catalogs, pricing, inventory, SLAs, and capabilities as structured APIs
- Design for autonomous purchasing, zero-click replenishment, or agent payment rails
- Compete when buyers rank cold structured data instead of storytelling
- Not for generic human ecommerce ops alone (`ecommerce`), list-price strategy alone (`pricing`), or low-level third-party API client debugging alone (`api`)

## Quick Reference

| Topic | File | Load when |
|-------|------|-----------|
| Technical implementation | `references/infrastructure.md` | Protocols, OpenAPI/MCP shapes, auth, errors, versioning |
| Agent discovery | `references/discovery.md` | Registries, capability metadata, ranking signals |
| Retail / ecommerce | `references/retail.md` | Catalog attributes, inventory feeds, auto-reorder lock-in |
| Sources | `references/sources.md` | Verify domain claims against primary URLs |

## The Paradigm Shift

| B2C/B2B | B2A |
|---------|-----|
| Humans browse, compare, feel | Agents query, parse, decide |
| Emotional storytelling wins | Structured data wins |
| UX optimized for eyes | APIs optimized for parsing |
| Brand = trust + emotion | Brand = verified track record |
| Loyalty = relationship | Loyalty = switching cost |
| Marketing = persuasion | Marketing = engineering |

## Core Rules

### 1. Machine-Readable First
- Products must be structured objects, not prose descriptions
- JSON-LD, Schema.org, OpenAPI with typed fields
- If an agent has to "interpret" text to extract price/specs, you lose
- Normalize units: `shipping_days_max: 2`, not "fast shipping"

### 2. Comparability Is Everything
Agents compare ruthlessly. Win by being comparable:
- Standardized attributes across your catalog
- Same fields as competitors (`price_currency`, `availability_stock`)
- SLAs with concrete numbers, not promises
- "Better" must be objectively measurable

### 3. Discovery ≠ SEO
Agents use structural queries instead of Google. They query registries and APIs:
- Publish in skill stores / capability directories
- `/.well-known/ai-plugin.json` or MCP tools
- Metadata must declare capabilities, not market them
- Ranking comes from structured capability indexes, not keyword SEO

### 4. Trust Is Verified, Not Told
Agents require verifiable proof rather than claims. They verify:
- Uptime/latency/SLA history via API, not badges
- Reviews from other agents (programmatic reputation)
- Certifications as queryable data, not PDF downloads
- Track record > marketing copy

### 5. Zero-Friction Trial or Death
Agents test immediately instead of "considering":
- Onboarding < 1 API call when possible
- Sandbox with rate limits, not "talk to sales"
- Must work correctly on first attempt
- Errors must be machine-readable JSON, not HTML pages

### 6. Payments for Agents
The agent needs to transact autonomously:
- Agent payment toolkits / pre-authorized budgets
- Programmatic receipts and confirmations
- Escrow patterns when counterparties are unknown
- Hand off provider-specific integration depth to `payments` / `stripe-api-integration`

### 7. Metrics That Matter

| Metric | What It Measures |
|--------|-----------------|
| Agent Conversion Rate | % queries → purchase |
| Decision Latency | Time from first query to commit |
| Comparison Survival | % times reaching final shortlist |
| Repeat Agent Retention | % agents that return |
| API Error Rate | Failures causing agent to discard |

Traditional metrics (page views, bounce rate) are weak proxies for agent buyers.

## Common Traps

| Trap | Why It Fails |
|------|--------------|
| Pretty website, no API | Agents only parse your API |
| "Contact us for pricing" | Agents need programmatic pricing |
| Marketing copy in descriptions | Agents parse data, skip prose |
| HTML error pages | Agents need JSON errors |
| Manual onboarding | Agents will not wait |
| Trust badges instead of APIs | Unverifiable = untrusted |
| Optimizing for humans first | Delays agent-readiness |

## Honest Limitations

What an AI helping you with B2A cannot do:
- **Create track record** — you still have to deliver measurable uptime and fulfillment
- **Know internal rankings** — how closed agent platforms rank skills can be opaque
- **Predict every agent heuristic** — each buyer agent may weight fields differently
- **Guarantee discovery** — registry placement and ranking can include private deals
- **Prevent competitor gaming** — false structured claims remain a real risk; verify

## Readiness Checklist

```
□ Products exposed via structured API (not scraping required)
□ Pricing programmatically queryable
□ Inventory/availability real-time
□ Authentication supports client_credentials (not interactive)
□ Errors return JSON with semantic codes
□ Onboarding works in a small number of API calls
□ Payment rails support autonomous agents
□ SLA metrics exposed via API
□ Listed in relevant skill registries
```
