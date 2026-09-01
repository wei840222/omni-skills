---
name: property-valuation
description: Estimate a residential or commercial property's market-value range from user-provided comparable sales, income, or cost inputs. Use when the user asks for a property estimate, listing-price check, comparable-sales analysis, or cap-rate calculation; use a licensed local appraiser for an appraisal or regulated purpose.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏠"}'
  related-skills: '{"financial-literacy":"Explains the financial concepts and calculations that support property analysis.","house":"Helps with home-management decisions after a valuation.","real-estate-skill":"Covers broader purchase, sale, and transaction decisions beyond a value estimate."}'
---

## State location

Before saving any property context or report, resolve `<state_root>` once for this invocation:

1. Use an explicitly configured state root when the user or host provides one.
2. Otherwise, use the first existing directory in this order: `<workspace>/property-valuation/`, `<workspace>/memory/property-valuation/`, then `~/property-valuation/`.
3. If none exists and the user asks to save state, create `<workspace>/property-valuation/`.

Use the selected `<state_root>` for every state operation. If multiple candidate directories exist, use only the highest-precedence one and tell the user; do not merge copies automatically.

```text
<state_root>/
├── memory.md          # Preferences and market context, when the user elects to save them
└── valuations/        # Saved valuation reports, when requested
```

## Setup

On first use, read `references/setup.md` for onboarding and consent guidance. Read `references/memory-template.md` only when creating or parsing `<state_root>/memory.md`.

## When to Use

Use this skill when the user asks for a value range for a residential or commercial property, provides comparable sales, requests an income-approach or cap-rate calculation, or wants to assess a listing price.

## Core Rules

### 1. State the valuation method

Every estimate must name its method:

- **Comparable sales (comps):** recent similar sales, typically the primary residential method.
- **Income approach:** net operating income (NOI) divided by a market-supported cap rate, typically for income property.
- **Cost approach:** land value plus replacement cost, less depreciation.

Use more than one method when the available data supports it, and explain material differences between results.

### 2. Gather the decision inputs

Before estimating, obtain or clearly mark as unknown: location or neighborhood, property type, living or rentable area, bedrooms and bathrooms when relevant, condition and updates, year built, lot or site information when relevant, valuation date, and the source/date of each comp or income figure. Missing or non-comparable inputs require a wider range and lower confidence.

### 3. Reconcile comparable sales explicitly

For each comp, identify its sale date, proximity, physical differences, and any adjustment supported by local market evidence. Show the direction and rationale for each adjustment; do not present generic percentage adjustments as universal market facts.

### 4. State confidence and market context

Use **high** confidence only with several recent, nearby, well-matched comps; use **medium** when some material adjustments are necessary; use **low** when evidence is sparse, old, geographically distant, or the property is unusual. Note known supply, days-on-market, financing, or condition factors that could shift the range.

### 5. Use income calculations transparently

```text
Property value = NOI / cap rate
NOI = effective gross income - operating expenses
```

State whether each input is actual, trailing, projected, or assumed. Calculate price per square foot or another relevant unit metric as a cross-check, and explain a material divergence from comparable evidence.

## Conditional research

Read `references/research.md` when explaining regulated appraisal scope, selecting lending-oriented comparable-sale evidence, or discussing tax-related valuation. Verify local law and current market evidence before making jurisdiction-specific claims.

## Evidence hygiene

- Prioritize recent, arm's-length comparable sales and explain when older sales are used.
- Compare condition, updates, concessions, financing terms, and location to explain differences among raw sale prices.
- Use automated valuation models and tax assessments as context alongside verified property-specific evidence.
- Keep assessed value separate from market value.

## Security & privacy

- Keep property details, reports, and user preferences in `<state_root>` only when the user asks to save them.
- Use user-provided information for the estimate; do not imply MLS, Zillow, Redfin, or other live-data access when it is unavailable.
- Exclude or redact sensitive financial information that is not necessary for the requested analysis.
- Present the result as an educational estimate, not a licensed appraisal, legal opinion, tax opinion, or lending determination.
