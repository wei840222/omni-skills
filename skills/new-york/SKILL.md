---
name: new-york
description: Guide New York State living, moving, work, taxes, housing, winter risk, transit, and statewide trips. Use when region choice, DMV, school districts, cost reality, or visitor routing matters; not for NYC-only itineraries that belong in `new-york-city`.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🍎"}'
---

## State location

New York State continuity state may exist in `<workspace>/new-york/`, `<workspace>/memory/new-york/`, or `~/new-york/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/new-york/`, `<workspace>/memory/new-york/`, `~/new-york/`.
3. If several candidate directories exist, use only the highest-precedence one and report the separate copies.
4. If none exists and the user explicitly wants continuity, create `<workspace>/new-york/` by default. If the host cannot provide `<workspace>`, request a state root before creating state.

Use the selected `<state_root>` for every state operation in this invocation. Resolve existing locations before creation; preserve separate copies unless the user requests a migration.

## When to use

Use this skill for New York State decisions that generic U.S. advice gets wrong: choosing a region, moving in, licensing and vehicles, taxes, housing and insurance, winter readiness, healthcare access, school planning, business setup, or statewide trip design.

Classify the user's mode first—visitor, future resident, current resident, or business operator—then anchor advice to region, metro, county, ZIP, and school district when those variables change the answer. For NYC-only borough itineraries, airports, and neighborhood bases, prefer `new-york-city`.

## Reference routing

| Topic | Read | When to load |
|---|---|---|
| Continuity setup and consent | `references/setup.md` | The user wants persistent New York context or `<state_root>/` needs initialization |
| Memory structure | `references/memory-template.md` | Creating or updating `<state_root>/memory.md` after consent |
| Regions and corridor tradeoffs | `references/regions.md` | Recommending a metro, corridor, or statewide place to live |
| Moving and settling | `references/moving-and-settling.md` | Planning relocation deadlines, documents, and first-week sequence |
| DMV and vehicles | `references/new-york-dmv-and-vehicles.md` | License exchange, registration, REAL ID, inspection, or car ownership |
| Housing and insurance | `references/housing-and-insurance.md` | Renting, buying, flood/snow exposure, or insurance pressure |
| Utilities and bills | `references/utilities-and-bills.md` | Electricity, heating, internet, and recurring service setup |
| Costs and taxes | `references/costs-and-taxes.md` | Salary reality, property tax, tolls, or total-cost comparisons |
| Weather and preparedness | `references/weather-and-preparedness.md` | Winter storms, floods, heat, outages, or emergency readiness |
| Laws and safety | `references/laws-and-safety.md` | Practical legal, scam, and safety boundaries |
| Family and schools | `references/family-and-schools.md` | School districts, childcare, or family-location logic |
| Healthcare coverage | `references/healthcare-and-coverage.md` | Marketplace coverage, care access, or insurance choice |
| Work and business | `references/work-and-business.md` | Jobs, startups, permits, or business location tradeoffs |
| Transit and commutes | `references/transit-and-commutes.md` | Rail, bus, driving, and commute design across regions |
| Road trips and visiting | `references/road-trips-and-visiting.md` | Statewide parks, corridors, and visit strategy |
| Visitor tips and etiquette | `references/visitor-tips.md` | First-time visitor mistakes and etiquette |
| Current statewide updates | `references/2026-updates.md` | Recent congestion pricing, tax, climate, or housing changes |
| Official sources | `references/sources.md` | Unstable rules that need official verification |
| Domain knowledge snapshot | `references/domain-knowledge.md` | Sourced statewide facts and verification notes |

## Core workflow

1. **Classify before advising.** Identify visitor / mover / resident / business mode, then the region or metro that actually changes the recommendation. Ask only for the next missing detail that materially changes the answer.
2. **Separate statewide rules from local reality.** Label which guidance is statewide and which must be verified by county, school district, utility, transit agency, or municipality. NYC, Long Island, Hudson Valley, Capital Region, Western New York, Central New York, Finger Lakes, Southern Tier, and North Country are different operating environments.
3. **Optimize for total cost and risk, not brochure copy.** Include state income tax, local property tax, tolls, heating, parking, insurance, commute cost, flood/snow exposure, and winter readiness before calling a place cheap or worth it.
4. **Deliver sequence.** For administrative topics, answer as do-this-today / this-week / later. For relocation and regional questions, show why one corridor fits better than another.
5. **Verify mutable details.** For DMV, taxes, school boundaries, health-plan options, utility rules, congestion pricing, and seasonal access, read `references/sources.md` and confirm with the official source. If verification is blocked, keep the durable framework and mark the mutable fact as unverified.
6. **Persist only with consent.** For continuity, read `references/setup.md`, resolve `<state_root>`, explain the intended scope, then use `references/memory-template.md`. Keep credentials, SSNs, payment details, and full street addresses out of `<state_root>/` unless the user explicitly directs otherwise.

## Practical guardrails

- Never treat New York as "NYC plus upstate." Region, commute corridor, school district, winter driving, and property-tax reality usually dominate the answer.
- Prefer official state or local portals for compliance steps; send ZIP, county, district, or region context only when the user asks for location-specific help.
- Complete government forms, bookings, or submissions only after explicit user instruction.
- If weather, floodplain, lake-effect snow, or outage risk matters, lead with readiness and fallback plans rather than scenery.
- Keep `new-york` for statewide and multi-region decisions; hand NYC-only borough itineraries to `new-york-city`.
