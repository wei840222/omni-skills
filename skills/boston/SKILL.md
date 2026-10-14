---
name: boston
description: >
  Navigate Boston for visitors, residents, tech workers, students, and
  entrepreneurs: neighborhoods, MBTA/transport, costs, safety, visas, food,
  climate, and local services. Use for Greater Boston stay, move, commute, or
  work-base decisions. Prefer `united-states` for multi-city US routing,
  `travel`/`travel-planning` for generic trip systems, and `expat` for full
  cross-border move project tracking.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🦞"}'
  related-skills: '{"united-states":"Country-level multi-city US routing when Boston is only one stop.","booking":"Lodging search and reservation completion after a neighborhood base is chosen.","expat":"Cross-border move project tracking beyond Boston neighborhood and settling advice.","travel":"Standing multi-destination travel records when Boston is one city among several.","travel-planning":"Day-by-day multi-city itineraries when the trip leaves Boston.","dubai":"Peer city-guide pattern for another dense metro when comparing city skills."}'
---

## State location

Boston continuity state may exist in `<workspace>/boston/`, `<workspace>/memory/boston/`, or `~/boston/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/boston/`, `<workspace>/memory/boston/`, `~/boston/`.
3. If several candidate directories exist, use only the highest-precedence one and report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create `<workspace>/boston/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/boston/` only; otherwise ask for a state root before creating data.

Research notes and official source URLs live in `references/sources.md` (progressive disclosure).

Expanded domain rules, seasons, costs orientation, and local pitfalls live in `references/domain.md` (progressive disclosure).

## When to Use

Load this skill when the user asks about **Boston / Greater Boston** for visiting, moving, working, studying, or starting a business. Prefer progressive disclosure: answer from this file first, then open only the topic files needed.

For multi-city US trips, load `united-states` as the routing parent. Hand generic multi-destination trip systems to `travel` / `travel-planning`. Hand full cross-border move project tracking to `expat`.

## Quick Reference

| Topic | File |
|-------|------|
| **Visitors** | |
| Domain Knowledge | `references/domain.md` |
| Official sources | `references/sources.md` |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` |
| Where to stay | `references/visitor-lodging.md` |
| Tips & day trips | `references/visitor-tips.md` |
| **Neighborhoods** | |
| Quick comparison | `references/neighborhoods-index.md` |
| Downtown, Back Bay, Beacon Hill | `references/neighborhoods-downtown.md` |
| Cambridge, Somerville | `references/neighborhoods-cambridge.md` |
| South End, Jamaica Plain, Roxbury | `references/neighborhoods-south.md` |
| North End, Charlestown, East Boston | `references/neighborhoods-north.md` |
| Choosing guide | `references/neighborhoods-choosing.md` |
| **Food** | |
| Overview & dining scene | `references/food-overview.md` |
| Seafood & New England classics | `references/food-seafood.md` |
| North End Italian & ethnic | `references/food-ethnic.md` |
| Best areas for dining | `references/food-areas.md` |
| Dietary, alcohol, practical | `references/food-practical.md` |
| **Practical** | |
| Moving & settling | `references/resident.md` |
| Transport (T, buses, bikes) | `references/transport.md` |
| Cost of living | `references/cost.md` |
| Safety | `references/safety.md` |
| Weather & seasonal tips | `references/climate.md` |
| Local services (banking, utilities) | `references/local.md` |
| **Career** | |
| Tech industry & salaries | `references/tech.md` |
| Business & legal | `references/business.md` |
| Startups & funding | `references/startup.md` |
| Visas & work permits | `references/visas.md` |
| **Lifestyle** | |
| Culture & customs | `references/culture.md` |
| Healthcare & hospitals | `references/healthcare.md` |
| Universities & education | `references/education.md` |
| Expat & social life | `references/lifestyle.md` |
| Driving & car ownership | `references/driving.md` |

## Related Skills

- `united-states` — multi-city US routing when Boston is one stop
- `travel` / `travel-planning` — generic trip systems and multi-city itineraries
- `expat` — full cross-border move project tracking
- `booking` — lodging search after a neighborhood base is chosen
- `dubai` — peer city-guide pattern for dense-metro comparisons
