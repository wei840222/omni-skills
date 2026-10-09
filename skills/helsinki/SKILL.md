---
name: helsinki
description: >
  Navigate Helsinki as a visitor, resident, tech worker, student, or entrepreneur:
  neighborhoods, HSL transport, costs, visas/permits, food, climate, and local life.
  Use when planning a Helsinki trip or move, comparing areas, estimating living costs,
  choosing work/study/startup permit paths, or settling practical Finnish admin.
  Not for multi-country itinerary systems (travel), generic founder coaching (startup),
  or other city bases (dubai and siblings).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇫🇮"}'
  related-skills: '{"dubai":"Parallel Gulf city base when comparing Helsinki vs Dubai living or work.","startup":"Founder operating judgment and multi-function startup orchestration beyond Helsinki base selection.","travel":"Multi-stop itinerary framing when Helsinki is only one city in a larger trip."}'
---

## State location

Optional Helsinki planning context may exist in `<workspace>/helsinki/`, `<workspace>/memory/helsinki/`, or `~/helsinki/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/helsinki/`, `<workspace>/memory/helsinki/`, `~/helsinki/`.
3. If none exists and the user wants preferences kept, create `<workspace>/helsinki/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/helsinki/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants planning context kept across sessions. Host-shared memory such as workspace `MEMORY.md` is outside `<state_root>` and needs separate user consent; do not write passport, application IDs, or payment details there from this skill.

This skill is primarily **routing knowledge**. Durable notes are optional. Do not invent a CRM or visa case file unless the user asks to keep state. Template: `references/memory-template.md`.

## When to load

Load for Helsinki **visitor**, **relocation**, **tech/work**, **study**, or **business** questions:

- trip plans, lodging, attractions, winter survival, day trips
- neighborhood choice, rent ranges, settling-in admin
- HSL/metro/tram/commuter reality (without treating stale fares as live fact)
- non-EU work permits (specialist, EU Blue Card), student or startup paths
- cost of living, healthcare orientation, schools, culture, driving

Route away when the ask is mainly:

- multi-country trip systems → `travel`
- founder coaching / multi-function startup ops beyond city base → `startup`
- another city as the primary base → `dubai` (or that city's skill)

## Critical verification path

Before stating a **visa duration, salary floor, processing fee, student funds floor, HSL fare, tax rate, or legal consequence** as current fact:

1. Open `references/sources.md` for the canonical URL.
2. Re-check the live official page for that nationality, permit type, and date.
3. If the live page cannot be opened, say the claim is unverified and give the URL to check — do not invent a number.

Orientation ranges in this package are for routing only. They are not filing advice.

## Core path

1. Identify **role** (visitor / resident / tech worker / student / entrepreneur) and **timeline** before naming a neighborhood or permit.
2. Load `references/domain.md` for Helsinki traps and EU/Schengen framing; load one leaf file for the active branch.
3. Prefer ranges over false precision. Label time-sensitive money and legal claims as verify-before-money.
4. Respect stored preferences in `<state_root>/memory.md` when present.
5. Default language: English. If the user writes in Finnish, reply in Finnish.

## Quick reference

| Topic | Load when | File |
|-------|-----------|------|
| Domain rules, traps, freshness | Always first for non-trivial asks | `references/domain.md` |
| Official / research links | Before quoting fees, floors, fares | `references/sources.md` |
| First-use / optional memory | Empty state or user wants notes kept | `references/setup.md`, `references/memory-template.md` |
| **Visitors** | | |
| Attractions | Sightseeing priorities | `references/visitor-attractions.md` |
| Itineraries | 1/3/7-day plans | `references/visitor-itineraries.md` |
| Lodging | Where to stay | `references/visitor-lodging.md` |
| Tips / day trips | Practical visitor edges | `references/visitor-tips.md` |
| **Neighborhoods** | | |
| Comparison | Choosing area | `references/neighborhoods-index.md`, `references/neighborhoods-choosing.md` |
| Center | City Center, Kamppi, Punavuori | `references/neighborhoods-center.md` |
| Trendy | Kallio, Vallila, Sörnäinen | `references/neighborhoods-trendy.md` |
| Residential | Töölö, Lauttasaari, Munkkiniemi | `references/neighborhoods-residential.md` |
| Suburban | Espoo, Vantaa, outer | `references/neighborhoods-suburban.md` |
| **Food** | | |
| Overview → leaf | Dining branch | `references/food-overview.md` then matching `references/food-*.md` |
| **Practical** | | |
| Settling | Moving in | `references/resident.md` |
| Transport | Metro/tram/HSL | `references/transport.md` |
| Cost | Budgets / rent orientation | `references/cost.md` |
| Safety / law | Legal lines | `references/safety.md` |
| Climate | Season survival | `references/climate.md` |
| Local admin | Banking, SIM | `references/local.md` |
| Driving | Car ownership | `references/driving.md` |
| **Career** | | |
| Tech / salaries | Work market | `references/tech.md` |
| Business | Company setup | `references/business.md` |
| Visas / permits | Work, Blue Card, study, startup | `references/visas.md` |
| Startups / funding | Ecosystem | `references/startup.md` |
| **Lifestyle** | | |
| Culture | Customs | `references/culture.md` |
| Healthcare | System orientation | `references/healthcare.md` |
| Education | Schools | `references/education.md` |
| Expat social | Community | `references/lifestyle.md` |

## Failure recovery

- Missing role/timeline → ask one clarifying question; default short-visit advice to visitor files, multi-month plans to `resident.md` + `visas.md`.
- Live official page blocked or CAPTCHA → keep package text as orientation only; surface the canonical URL from `references/sources.md`.
- Conflicting package number vs live official page → trust the live page and note the package may be stale.
- User wants durable notes but no writable state root → ask for an authorized path; do not write outside `<state_root>` or host-shared memory without consent.
