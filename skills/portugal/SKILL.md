---
name: portugal
description: >
  Plan Portugal trips with local-leaning food, region, and logistics advice for
  Lisbon, Porto, Algarve, Douro, Alentejo, Azores, and Madeira. Use when choosing
  neighborhoods, itineraries, trains/cards, fado, beaches, wine routes, or
  tourist-trap avoidance. Not for multi-country trip systems (`travel`), deep
  cuisine technique (`food`), or Portuguese language production (`portuguese`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇵🇹"}'
  related-skills: '{"travel":"Multi-country itineraries and general travel memory beyond Portugal-only routing.","food":"Deeper cuisine workflows beyond Portuguese food pointers.","portuguese":"Portuguese language production and register rather than trip logistics."}'
---

# Portugal

Local-leaning trip planning for a small but regionally diverse country: neighborhood and region choice beat brochure slogans, meal timing matters, and tourist-trap patterns are predictable once you name them.

## State location

Resolve `<state_root>` before any preference read/write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory:
   `<workspace>/portugal/`,
   `<workspace>/memory/portugal/`,
   `~/portugal/`.
3. If none exist and the user asked to persist data, create
   `<workspace>/portugal/`.

| Path | Required? | Role |
|------|-----------|------|
| `<state_root>/memory.md` | optional | Trip style, season, region preferences, history |

Do not treat the literal string `<state_root>` as a filesystem path. Skill resources stay under `references/` and `assets/`. Host-shared memory such as workspace `MEMORY.md` is outside `<state_root>` and needs separate consent.

Template: `assets/memory-template.md`.

## Setup

If `<state_root>` is missing or empty, read `references/setup.md` and start naturally. Ask month, duration, regions, travel style, diet, and group before locking a multi-city plan.

## When to load

Load when the user is planning a **Portugal** trip or needs local logistics:

- Lisbon / Porto / Sintra / Algarve / Douro / Alentejo / Azores / Madeira bases
- neighborhood choice, fado, pastéis, francesinha, wine routes
- CP trains, Rede Expressos, metro/tram cards, car-vs-transit tradeoffs
- beaches, hiking, nightlife, family pacing
- tourist-trap avoidance and realistic timing (lunch, dinner, August, Sundays)

Route away when the ask is mainly:

- multi-country routing systems → `travel`
- restaurant technique or deep cuisine systems → `food`
- Portuguese writing/production → `portuguese`

## Quick reference

| Need | Load |
|------|------|
| Core rules, traps, security | `references/rules.md` |
| Regions at a glance | `references/regions.md` |
| Lisbon | `references/lisbon.md` |
| Porto | `references/porto.md` |
| Sintra day trip | `references/sintra.md` |
| Algarve | `references/algarve.md` |
| Sample plans | `references/itineraries.md` |
| Stays | `references/accommodation.md` |
| Apps | `references/apps.md` |
| Food | `references/food-guide.md` |
| Wine | `references/wine.md` |
| Experiences | `references/experiences.md` |
| Beaches | `references/beaches.md` |
| Hiking | `references/hiking.md` |
| Nightlife | `references/nightlife.md` |
| Culture / fado | `references/culture.md` |
| With kids | `references/with-kids.md` |
| Transport | `references/transport.md` |
| Telecoms | `references/telecoms.md` |
| Emergencies | `references/emergencies.md` |
| Official sources | `references/sources.md` |
| First-run setup | `references/setup.md` |

## Core rules (summary)

1. **Specific over generic** — name venues, streets, cards, and routes.
2. **Local perspective** — separate ritual queues from better everyday options.
3. **Region first** — Lisboa, Porto, Algarve, Alentejo, Douro, islands behave differently.
4. **Timing** — late dinners, long lunches, August coastal demand, Sunday closures.
5. **Name traps** — waterfront menus, hawker fado, pickpocket hot spots, car-in-center pain.
6. **Match style** — foodie vs beach vs wine vs family load different reference sets.

Full detail: `references/rules.md`.

## Default answer shape

1. Clarify month, nights, regions, style, diet/kids if missing.
2. Recommend a base + day-trip logic (not a generic “visit everything” list).
3. Load the matching reference files before detailed claims.
4. Flag one likely tourist trap and one practical timing constraint.
5. Offer optional consent to store preferences under `<state_root>/memory.md`.
6. Point to `references/sources.md` / `references/apps.md` for live fares, hours, and disruptions.

## Security and privacy

- Trip memory stays in `<state_root>` only after consent.
- No network requests from this skill; no files outside `<state_root>`.
- Do not invent live weather, queue length, seat inventory, or current fares—send the user to official sources to confirm.
