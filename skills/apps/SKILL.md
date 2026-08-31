---
name: apps
description: Recommend, compare, and track iOS or Android apps around a user's platform, budget, privacy, and workflow preferences. Use for mobile app recommendations, app comparisons, or an approved personal app tracker; use mobile-app-analytics for product performance metrics.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📱"}'
  related-skills: '{"mobile-app-analytics":"Analyzes product performance metrics rather than recommending consumer apps."}'
---

## State location

Apps state may exist in `<workspace>/apps/`, `<workspace>/memory/apps/`, or `~/apps/`. `<workspace>` is the workspace root supplied by the host/runtime.

Before any state read, query, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path supplied by the user or host when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/apps/`, `<workspace>/memory/apps/`, `~/apps/`.
3. When no candidate exists and the host supplied `<workspace>`, propose `<workspace>/apps/` as the creation target and obtain named consent before creating it.
4. When no candidate exists and no host workspace is available, ask for an explicit state path before creating state.

When multiple candidate directories exist, use only the first one, tell the user that multiple state directories were found, and keep all other candidates unchanged. Use the selected `<state_root>` for every state operation during the run. Create the resolved directory path itself rather than a literal directory named `<state_root>`.

## Workflow

1. Identify the decision: recommendation, comparison, or approved state update.
2. Gather the minimum decision constraints: platform, primary job, budget or subscription preference, privacy or offline needs, and existing tools.
3. For a saved-preference workflow, resolve `<state_root>` and read only the relevant approved files.
4. Load the one reference that fits the job: `references/categories.md` for discovery, `references/compare.md` for a comparison, or `references/sources.md` for mutable details.
5. Return a bounded recommendation or use-case-specific comparison, then offer a state update only after confirmation.

## When to use

Use for iOS or Android app recommendations, app-to-app comparisons, and an approved personal record of apps the user likes, tries, or plans to evaluate. Gather the platform, use case, budget or subscription preference, privacy or offline needs, and any existing app constraints before narrowing choices.

Use `mobile-app-analytics` instead when the user needs product-performance metrics, funnels, retention, or store-console analysis rather than a consumer app decision.

## Architecture

Persistent preference data lives under the resolved `<state_root>` only after the user approves saving it.

```text
<state_root>/
├── memory.md          # Preferences, platforms, dislikes
├── favorites.md       # Apps the user likes, grouped by category
├── tried.md           # Apps evaluated, with outcomes and reasons
└── wishlist.md        # Apps to evaluate later
```

## Quick reference

| Topic | File | When to load |
|---|---|---|
| State-file templates | `assets/memory-template.md` | Creating or repairing approved local app-tracking files |
| Category guide | `references/categories.md` | Narrowing a recommendation by category |
| Comparison framework | `references/compare.md` | Comparing two or more apps |
| Privacy and source map | `references/sources.md` | Verifying current privacy disclosures, pricing, availability, or terms |

## Scope

This skill recommends and compares apps, explains tradeoffs, and records approved preferences or evaluation notes. Keep installation, store-account management, purchases, subscriptions, and device inventory under the user's control.

## Decision boundaries

- Use current official listings and vendor documentation for mutable details; platform privacy disclosures inform a comparison but are not an independent security audit.
- Treat the user's explicit approval as the write boundary for `<state_root>`; otherwise provide a recommendation without persistence.
- Route product-performance questions about funnels, retention, analytics, or store-console reports to `mobile-app-analytics`.

## Core rules

### 1. Check preferences first

When the user has approved saved preferences, read `<state_root>/memory.md` before recommending. Consider:

- Platform: iOS, Android, or both.
- Pricing preference: free, freemium, paid, or no subscriptions.
- Past dislikes and apps already tried.
- Priorities such as privacy, offline use, export, accessibility, or cross-platform support.

### 2. Recommend for fit

| Signal | Response |
|---|---|
| User asks for the “best” app | Offer up to three options with distinct tradeoffs. |
| Similar apps were tried | Read `<state_root>/tried.md` and avoid repeating rejected choices without explaining what changed. |
| Subscription aversion | Prefer options that meet it; describe any unavoidable recurring cost clearly. |
| A specific workflow is stated | Match the workflow rather than popularity. |

### 3. Explain tradeoffs

For each recommendation, state what it suits, meaningful limitations, pricing model, platform and sync fit, and privacy or data-handling implications when relevant.

### 4. Record only confirmed preferences

With the user's approval, update the resolved state:

| Confirmed event | File |
|---|---|
| Platform or preference stated | `<state_root>/memory.md` |
| App liked | `<state_root>/favorites.md` |
| App tried or rejected | `<state_root>/tried.md` |
| App saved for later evaluation | `<state_root>/wishlist.md` |

### 5. Compare within a decision context

Compare apps serving the same primary job, use the criteria in `references/compare.md`, and name the use case that favors each option rather than declaring a universal winner.

### 6. Be explicit about freshness

Feature availability, prices, subscription terms, store availability, and privacy disclosures can change. Read `references/sources.md`, then verify material current details from the app vendor and relevant store listing before presenting them as facts. When verification is unavailable, label the detail as unverified rather than guessing.

## Common traps

- Treating a popularity ranking as a personal recommendation: anchor the choice to the stated workflow and constraints.
- Repeating a rejected app: check `<state_root>/tried.md` whenever approved history exists.
- Treating current pricing, features, availability, or privacy disclosures as durable: verify them through `references/sources.md` and the current official listing.
- Writing state after conversational context alone: obtain approval and use the resolved `<state_root>`.
- Mixing unrelated app categories in a comparison: compare the same primary job and state which use case favors each option.
