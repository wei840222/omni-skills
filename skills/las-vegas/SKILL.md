---
name: las-vegas
description: >
  Provide Las Vegas guidance for visitors, residents, remote workers, and
  entrepreneurs. Trigger on questions about Vegas travel, relocation, costs,
  or neighborhoods.
metadata:
  openclaw: '{"emoji":"\ud83c\udfb0","os":["linux","darwin","win32"],"displayName":"Las Vegas"}'
  related-skills: '{"business": "Apply proven business frameworks to validate startup ideas, define strategic priorities, track unit economics, and manage irreversible decisions", "dubai": "Provide practical guidance on Dubai for visitors, residents, tech workers, and entrepreneurs", "money": "Guide debt-payoff order, emergency-fund sizing, saving rates, affordability, and financial shocks", "travel": "Maintain a traveler standing system for wishlist destinations, passport and visa readiness, Schengen-style day counts, shared bookings, points expiry, trip budgets, disruption claims, and post-trip debriefs"}'
---

## When to Use

Trigger on user queries regarding Las Vegas travel, relocation, remote work, business setup, tax benefits, or local living conditions.

## Architecture

State is managed in `<state_root>/`. If uninitialized, read `references/setup.md`. Reference `assets/memory-template.md` for structure.

```
<state_root>/
├── memory.md     # Context, preferences, type (visitor vs resident)
└── notes/        # Working notes
```

## Progressive Disclosure

Load relevant files from `references/` based on user context before answering:

**Setup & Context:**
- Initial interaction: Load `references/setup.md`
- Context gathering: Update `<state_root>/memory.md`

**Visitors & Travel:**
- Load `references/visitor-attractions.md`, `references/visitor-itineraries.md`, `references/visitor-lodging.md`, `references/visitor-shows.md`, or `references/visitor-tips.md` based on query.

**Neighborhoods & Relocation:**
- Quick comparison: Load `references/neighborhoods-index.md`
- Deep dives: Load `references/neighborhoods-choosing.md`, `references/neighborhoods-affordable.md`, or specific area files (`strip`, `downtown`, `summerlin`, `henderson`).

**Food & Dining:**
- Load `references/food-overview.md`, `references/food-areas.md`, `references/food-celebrity.md`, `references/food-local.md`, or `references/food-practical.md`.

**Practical Living:**
- Moving logistics: Load `references/resident.md`
- Costs & jobs: Load `references/cost.md`, `references/tech.md`, `references/startup.md`, `references/remote-work.md`, `references/hospitality.md`
- Daily life: Load `references/climate.md`, `references/safety.md`, `references/transport.md`, `references/driving.md`, `references/local.md`, `references/healthcare.md`, `references/education.md`, `references/outdoors.md`, `references/culture.md`, `references/lifestyle.md`

## Core Directives

1. **Identify Persona:** Determine if the user is a visitor, resident, remote worker, or potential mover before giving advice.
2. **Consult References:** Always load the appropriate `references/*.md` file before generating detailed recommendations. Las Vegas knowledge changes quickly (costs, laws, climate realities).
3. **Ground Facts:** For costs, tax/residency, climate hazards, transit, and official visitor claims, prefer `references/sources.md` and the cited official URLs over memory.
