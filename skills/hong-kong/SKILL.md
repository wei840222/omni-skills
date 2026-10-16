---
name: hong-kong
description: >
  Navigate Hong Kong for visitors, residents, tech workers, students, and
  entrepreneurs: neighborhoods, MTR/Octopus, housing costs, visas, typhoon
  timing, food areas, and Greater Bay Area day-trip logistics. Use for Hong
  Kong stay, move, commute, or work-base decisions. Prefer `travel` /
  `travel-planning` for multi-city trip systems, `booking` after a base is
  chosen, `expat` for full cross-border move tracking, `macau` / `china` /
  `taiwan` / `singapore` for peer city routing, and `flight` for air-segment
  details. Not for inventing nationality-specific visa outcomes or quoting
  fares/rents as guaranteed without a live official or listing check.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇭🇰"}'
  related-skills: '{"booking":"Lodging or reservation completion after a Hong Kong neighborhood base is chosen.","china":"Mainland China routing when the trip or move crosses the Shenzhen/Guangzhou border.","expat":"Cross-border move project tracking beyond Hong Kong neighborhood and settling advice.","flight":"Air-segment planning into or out of HKG when flights are the main question.","macau":"Peer SAR guide for ferry/HZMB day trips and Macau-specific districts.","singapore":"Peer dense Asian city-state guide for comparative relocation framing.","taiwan":"Peer Traditional Chinese destination when comparing HK with Taiwan bases.","travel":"Standing multi-destination travel records when Hong Kong is one stop among several.","travel-planning":"Day-by-day multi-city itineraries when the trip leaves Hong Kong."}'
---

## State location

Hong Kong continuity state may exist in `<workspace>/hong-kong/`,
`<workspace>/memory/hong-kong/`, or `~/hong-kong/`. Before reading or writing
state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/hong-kong/`, `<workspace>/memory/hong-kong/`, `~/hong-kong/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/hong-kong/` when `<workspace>` is available; otherwise ask for a
   state root before creating data.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. Create
or update `<state_root>/memory.md` only when the user wants context kept across
sessions. Legacy `~/Clawic/data/hong-kong/` is a migration source only—keep it
out of active lookup; move only with explicit user consent (copy, validate,
cutover). Scripts and shell examples must receive the resolved filesystem path;
never write the literal string `<state_root>` to disk.

Research notes and official source URLs live in `references/sources.md`
(progressive disclosure).

## When to use

Use for **Hong Kong (HKSAR)** decisions: visit length and neighborhood base,
relocation fit, MTR/bus/ferry/Octopus routing, cost bands, safety street-smarts,
tech/work base, visas and residency *orientation*, food areas, typhoon planning,
schools, healthcare orientation, driving tradeoffs, and Greater Bay Area day
trips (Shenzhen / Macau).

Do **not** use this skill as the sole source for a multi-country standing travel
system (`travel`), generic multi-city day packing (`travel-planning`), a full
move project board (`expat`), Macau district planning (`macau`), or mainland
China procedures (`china`).

Classify the user first: visitor, planning-to-move, already-resident, tech/remote
worker, student, or entrepreneur. Ask only for the next missing detail that
changes the recommendation (dates/month, budget currency, passport, kids,
Cantonese/Mandarin/English comfort, quiet vs nightlife priority).

## Reference routing

Load the smallest set that answers the current question. Prefer
`references/sources.md` before booking-critical fare, entry, residency, or
typhoon-risk claims.

| Topic | File | When to load |
| --- | --- | --- |
| Continuity setup | `references/setup.md` | User wants persistent Hong Kong context or empty `<state_root>/` |
| Memory structure | `assets/memory-template.md` | Creating/updating `<state_root>/memory.md` after consent |
| Official source map | `references/sources.md` | Before booking-critical fares, entry rules, residency, or agency claims |
| Visitor attractions | `references/visitor-attractions.md` | Must-see vs skip lists |
| Visitor itineraries | `references/visitor-itineraries.md` | 1/3/7-day frames |
| Visitor lodging | `references/visitor-lodging.md` | Hotel/Airbnb neighborhood fit for short stays |
| Visitor tips | `references/visitor-tips.md` | Day trips, packing, practical visitor traps |
| Neighborhoods index | `references/neighborhoods-index.md` | Quick neighborhood comparison |
| Central / Mid-Levels / SoHo | `references/neighborhoods-central.md` | Island CBD and hillside bases |
| Causeway Bay / Wan Chai | `references/neighborhoods-causeway.md` | East Island bases |
| TST / Mong Kok / West Kowloon | `references/neighborhoods-kowloon.md` | Kowloon bases |
| New Territories | `references/neighborhoods-newterritories.md` | Sha Tin, Tai Po, Tuen Mun, Tsuen Wan |
| Choosing guide | `references/neighborhoods-choosing.md` | Profile → neighborhood matching |
| Food overview | `references/food-overview.md` | Dining scene and meal timing |
| Cantonese / dim sum | `references/food-local.md` | Local specialties |
| International dining | `references/food-international.md` | Non-local restaurants |
| Food areas | `references/food-areas.md` | Where to eat by district |
| Dietary / practical | `references/food-practical.md` | Dietary constraints and alcohol norms |
| Moving / settling | `references/resident.md` | Move-in, utilities, admin orientation |
| Transport | `references/transport.md` | MTR, buses, ferries, taxis, Octopus |
| Cost of living | `references/cost.md` | Rent and monthly budget orientation |
| Safety | `references/safety.md` | Street safety and legal framing |
| Climate / typhoons | `references/climate.md` | Seasonal and signal planning |
| Local services | `references/local.md` | Banks, SIM, payments |
| Tech / salaries | `references/tech.md` | Local tech scene orientation |
| Company setup / tax | `references/business.md` | Company and tax orientation |
| Entry / residency paths | `references/visas.md` | Employment, TTPS, QMAS, Working Holiday orientation |
| Startups / funding | `references/startup.md` | Startup and GBA context |
| Culture | `references/culture.md` | Etiquette and language reality |
| Healthcare | `references/healthcare.md` | Hospitals and insurance orientation |
| Schools | `references/education.md` | Schools and universities |
| Expat lifestyle | `references/lifestyle.md` | Social and lifestyle fit |
| Driving | `references/driving.md` | Car ownership and parking tradeoffs |

## Core rules

1. **Identify context first** — role, timeline, month, budget currency, passport,
   and language comfort before locking a neighborhood or itinerary.
2. **Transit-first city** — plan around MTR + Octopus before suggesting a car.
   Read `references/transport.md`; verify live fares/service changes with MTR or
   Octopus before treating a figure as current.
3. **Housing size and cost are planning constraints** — treat small flats and
   high rents as defaults, not exceptions. Use `references/cost.md` and
   `references/neighborhoods-choosing.md` for orientation, then check live
   listings before budgeting.
4. **Typhoons change the day** — May–September humidity and typhoon signals can
   cancel outdoor plans; T8+ means stay indoors. See `references/climate.md`.
5. **Visa claims are orientation only** — employment, TTPS, QMAS, investment,
   and Working Holiday rules depend on nationality and current ImmD text. Read
   `references/visas.md`, then re-check the matching ImmD page before advising
   an application. Do not invent eligibility.
6. **Greater Bay Area is adjacent, not identical** — Shenzhen and Macau day trips
   need separate entry rules (`china`, `macau`). Confirm border mode and passport
   pathway before stacking same-day crossings.
7. **Prefer official sources for fragile facts** — ImmD, MTR, Octopus, labour,
   and tourism hubs in `references/sources.md` beat memory or forum numbers.

## Output gates

- Ask for the next missing constraint before locking lodging or visa advice.

- State which references were loaded.
- Separate orientation from live-verified booking facts.
- When a visa, fare, rent, or fee is material, point to the official URL and say
  what still needs a live check.
- Keep passport numbers, ID card numbers, and credentials out of
  `<state_root>/memory.md`.
