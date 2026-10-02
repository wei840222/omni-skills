---
name: etsy
description: >
  Structure Etsy shop growth workflows and listing diagnostics: listing quality
  audits, buyer-intent keyword clusters, margin-safe pricing checks, conversion
  funnel triage, and controlled experiments. Use when reviewing Etsy listings,
  improving search visibility, checking fees/margins before discounts or ads, or
  designing one-variable listing tests. Prefer `ecommerce` for multi-channel store
  ops, `seo` for non-Etsy organic search, `pricing` for general price strategy,
  and `market-research` for broad demand validation outside listing execution.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛍️","requires":{"config":["<state_root>"]}}'
  related-skills: '{"ecommerce":"Multi-channel store operations and conversion foundations beyond Etsy-only listing execution.","seo":"General organic search when the surface is not an Etsy listing.","pricing":"Broader pricing strategy and tradeoffs outside Etsy fee-aware listing checks.","market-research":"Competitive and demand validation before listing-level experiments.","content-marketing":"Messaging frameworks that improve listing clarity when the ask is broader content craft."}'
---

## State location

Etsy shop context may exist in `<workspace>/etsy/`, `<workspace>/memory/etsy/`, or `~/etsy/`.
`<workspace>` means the workspace root provided by the host/runtime, not the shell cwd.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/etsy/`, `<workspace>/memory/etsy/`, `~/etsy/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and persistent state must be created, default to `<workspace>/etsy/` after brief first-write consent.

Use the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Skill package files stay under `references/` and `assets/`; never write learned shop data into `SKILL.md`.

Legacy path `~/Clawic/data/etsy/` is a migration source only. It is outside active lookup. Copy, validate, cut over, and keep a rollback path only after the user chooses migration.

```text
<state_root>/
├── memory.md                 # Stable shop context and operating preferences
├── listing-experiments.md    # Experiment log and outcomes
└── launch-checklists.md      # Reusable pre-launch and post-launch checks
```

## When to load

Load this skill for **Etsy listing and shop growth execution**:

- listing quality reviews (title, photos, offer clarity, description opening)
- search visibility / tag and keyword-cluster work on Etsy listings
- pricing sanity checks that include Etsy + payment fees before discounts or ads
- conversion funnel triage (impressions → clicks → favorites/carts → orders)
- controlled one-variable listing experiments with a defined measurement window

Route away when the primary task is:

- multi-channel ecommerce ops outside Etsy → `ecommerce`
- non-Etsy organic search / technical SEO → `seo`
- general pricing strategy without listing execution → `pricing`
- broad demand or competitor research before a listing plan → `market-research`
- brand/content craft with no listing diagnostic → `content-marketing`

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` is missing or empty, read `references/setup.md` and follow it while still answering the current Etsy question first. Confirm before the first durable write. File shapes: `assets/memory-template.md`.

## When to load references

Keep this file as the router; load the smallest matching reference only.

| Need | File |
|------|------|
| Setup / activation preferences | `references/setup.md` |
| Memory and experiment file templates | `assets/memory-template.md` |
| Core rules and growth traps | `references/core-rules.md` |
| Listing underperformance audit | `references/listing-audit-playbook.md` |
| Fee and policy source URLs (Gate 6) | `references/sources.md` |

## Operating loop

1. **Resolve state** — pick `<state_root>`; load prior shop context only after consent rules in setup.
2. **Lock scope** — category, target buyer, shipping region, production model, current goal.
3. **Diagnose by funnel stage** — visibility → click-through → consideration → conversion before prescribing edits.
4. **Protect margin** — estimate post-fee contribution margin before discounts, ads, or paid boosts.
5. **Change one variable** — define a 7–14 day window unless traffic is high enough for a shorter fair test.
6. **Log outcomes** — write experiment results to `<state_root>/listing-experiments.md` when persistence is allowed.

## Core rules

1. **Lock context before recommendations** — no scoped buyer/category/shipping → no high-confidence edits.
2. **Keyword clusters, not isolated tags** — one primary intent cluster + two supporting clusters mapped across title opening, tags, and description opening without clone phrasing.
3. **Optimize the full listing stack** — title, images, offer clarity, description opening, and shipping promise move together; do not retag over weak photos.
4. **Protect unit economics** — include Etsy fees, payment fees, packaging, shipping, and ad spend before growth tactics.
5. **Controlled experiments** — one major variable per cycle; track views, favorites, carts, conversion, and revenue per visit.
6. **Policy and trust** — no trademarked terms, unverifiable claims, or misleading delivery promises; name compliance risk and give a safer alternative.

## Security & privacy

- **Leaves the machine:** nothing by default from this skill itself.
- **Stays local:** shop context and experiment logs under `<state_root>/` after consent.
- **Does not:** ask for marketplace passwords or payment credentials; post, edit, or publish listings automatically; make undeclared network requests.
- Use placeholders only for shop IDs, API tokens, and private buyer data in examples.

## Scope

**ONLY**

- structure Etsy listing and shop growth workflows
- audit conversion blockers and search-relevance gaps
- recommend measurable experiments with clear success criteria

**NEVER**

- guarantee ranking position or sales outcomes
- invent performance metrics the user did not provide
- execute irreversible marketplace actions without explicit confirmation
