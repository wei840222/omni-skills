---
name: bucharest
description: >
  Navigate Bucharest for visitors, residents, tech workers, students, and
  entrepreneurs: neighborhoods (Old Town, Floreasca/Dorobanți, Pipera/Băneasa),
  STB/metro + Bolt routing, cost bands in RON/EUR, EU/Schengen stay orientation,
  Romanian food, climate, and local services. Use for Bucharest stay, move,
  commute, or work-base decisions. Prefer `romania` for multi-city Romania
  routing, `travel`/`travel-planning` for generic trip systems, and `expat` for
  full cross-border move project tracking.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏛️"}'
  related-skills: '{"booking":"Lodging search and reservation completion after a Bucharest neighborhood base is chosen.","dubai":"Peer city-guide pattern for another dense metro when comparing city skills.","expat":"Cross-border move project tracking beyond Bucharest neighborhood and settling advice.","romania":"Country-level multi-city Romania routing when Bucharest is only one stop.","romanian":"Everyday Romanian for menus, bookings, and on-the-ground talk.","toronto":"Peer city-guide pattern with immigration-heavy framing when comparing city skills.","travel":"Standing multi-destination travel records when Bucharest is one city among several.","travel-planning":"Day-by-day multi-city itineraries when the trip leaves Bucharest."}'
---

## State location

Bucharest continuity state may exist in `<workspace>/bucharest/`, `<workspace>/memory/bucharest/`, or `~/bucharest/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/bucharest/`, `<workspace>/memory/bucharest/`, `~/bucharest/`.
3. If several candidate directories exist, use only the highest-precedence one and report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create `<workspace>/bucharest/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/bucharest/` only; otherwise ask for a state root before creating data.

Use the selected `<state_root>` for every state operation in this invocation. Create or update `<state_root>/memory.md` only when the user wants context kept across sessions. Legacy `~/Clawic/data/bucharest/` is a migration source only—keep it out of active lookup; move only with explicit user consent (copy, validate, cutover).

Research notes and official source URLs live in `references/sources.md` (progressive disclosure).

Expanded domain rules, seasons, costs orientation, and local pitfalls live in `references/domain.md` (progressive disclosure).

## When to use

Use for **Bucharest (city + metro area)** decisions: visit length and neighborhood base, relocation fit, metro/STB/ride-hailing routing, cost bands, safety street-smarts, tech/work base, visas and residency *orientation*, Romanian food, climate, schools, healthcare orientation, and driving-in-city tradeoffs.

Do **not** use this skill as the sole source for a multi-city Romania itinerary (`romania`), a multi-country standing travel system (`travel`), generic day packing across cities (`travel-planning`), or a full move project board (`expat`).

Classify the user first: visitor, planning-to-move, already-resident, tech/remote worker, student, or entrepreneur. Ask only for the next missing detail that changes the recommendation (dates/month, budget currency, passport, kids, Romanian/English comfort, Old Town vs north-corridor priority).

## Reference routing

Load the smallest set that answers the current question. Prefer `domain.md` + one topic file before opening the full neighborhood or food set.

| Topic | File | When to load |
| --- | --- | --- |
| Continuity setup | `references/setup.md` | User wants persistent Bucharest context or empty `<state_root>/` |
| Memory structure | `assets/memory-template.md` | Creating/updating `<state_root>/memory.md` after consent |
| Core rules, traps, context | `references/domain.md` | First substantive answer; always for money/season/visa framing |
| Official source map | `references/sources.md` | Before booking-critical fares, entry rules, residency, or agency claims |
| Visitor attractions | `references/visitor-attractions.md` | Must-see vs skip lists |
| Visitor itineraries | `references/visitor-itineraries.md` | 1/3/7-day frames |
| Visitor lodging | `references/visitor-lodging.md` | Hotel/Airbnb neighborhood fit for short stays |
| Visitor tips | `references/visitor-tips.md` | Day trips, packing, practical visitor traps |
| Neighborhoods index | `references/neighborhoods-index.md` | Quick neighborhood comparison |
| Old Town & Center | `references/neighborhoods-center.md` | Historic core / nightlife bases |
| Floreasca & Dorobanți | `references/neighborhoods-north.md` | North professional corridor |
| Pipera & Băneasa | `references/neighborhoods-expat.md` | Expat / family / tech-park bases |
| Emerging & budget areas | `references/neighborhoods-emerging.md` | Titan / Berceni / Drumul Taberei style value bases |
| Choosing guide | `references/neighborhoods-choosing.md` | Profile → neighborhood matching |
| Food overview | `references/food-overview.md` | Dining scene map |
| Romanian cuisine | `references/food-local.md` | Local dishes and markets |
| International / fine dining | `references/food-international.md` | Non-local options |
| Food areas | `references/food-areas.md` | Where to eat by neighborhood |
| Food practical | `references/food-practical.md` | Hours, tipping, delivery |
| Moving & settling | `references/resident.md` | Contracts, utilities, everyday resident life |
| Transport | `references/transport.md` | Metro, STB, Bolt/Uber |
| Cost of living | `references/cost.md` | Rent bands and monthly budgets (ranges, not live quotes) |
| Safety | `references/safety.md` | Street crime patterns and area awareness |
| Climate | `references/climate.md` | Season, heat, winter |
| Local services | `references/local.md` | Banking, SIM, paperwork orientation |
| Tech industry | `references/tech.md` | Salaries, remote work, offices |
| Business setup | `references/business.md` | Company / tax orientation |
| Visas & residency | `references/visas.md` | Tourist stay, work, residency paths (verify passport) |
| Startups | `references/startup.md` | Ecosystem and funding orientation |
| Culture | `references/culture.md` | Customs, Orthodox calendar, tipping |
| Healthcare | `references/healthcare.md` | Public / private orientation |
| Education | `references/education.md` | Schools and universities orientation |
| Lifestyle | `references/lifestyle.md` | Expat social life |
| Driving | `references/driving.md` | Car ownership vs city transit |

## Core workflow

1. **Lock context.** Role, month, length of stay, passport (for entry only), budget currency, language comfort, Old Town vs north/Pipera priority, and whether kids or office commute matter.
2. **Answer the immediate question first.** Then load the smallest reference set from the table—do not dump every file.
3. **Money and paperwork before bookings.** Treat rent bands, metro/STB fares, and visa fees as orientation. Re-open `references/sources.md` and official pages before non-refundable flights, multi-month leases, or residency filings.
4. **Neighborhood from routine, not hype.** Match late-night return path, commute (metro vs Bolt), noise tolerance (Old Town nights), and budget.
5. **Entry is passport-specific.** Tourist stay windows and visa needs vary. Orient with `references/visas.md`, then verify on IGI / MAE / EU pages for that nationality and travel date.
6. **Persist only with consent.** Follow `references/setup.md`; keep passport numbers, bank credentials, and full address dumps out of reusable chat logs and `<state_root>/`.

## Core rules (durable)

1. Identify role and timeline before neighborhood or cost advice.
2. Separate **orientation euro/RON ranges** from **live quotes** for rent, fares, and visa fees.
3. Romania is EU; currency remains **RON** (EUR widely accepted in tourist zones)—quote both when budgeting.
4. Prefer **metro + STB + Bolt/Uber** for city trips; center parking and rush-hour traffic are high-friction.
5. Use **app-based or official taxi stands** for airport and night rides; treat street hailing as high-risk.
6. Winters are cold and summers can spike to heatwave levels—pack and schedule around `climate.md`.
7. Romanian is Latin-based; English is common among younger/tech crowds and uneven elsewhere—lead with Romanian basics when needed via `romanian`.
8. For multi-city Romania trips, hand off routing to `romania` after the Bucharest city block is set.

## Prefer these patterns

- Match Floreasca/Dorobanți for young professionals; Pipera/Băneasa for family/expat/tech-park routines; Old Town for short nightlife-heavy visits; Titan/Berceni/Drumul Taberei for budget bases.
- Quote visa/residency figures only from live official pages (or mark unverified).
- Visit rental listings in person before deposits; Storia / listing sites are search surfaces, not escrow.
- For short culture trips, keep lodging walkable to Old Town / center unless the user wants north quiet.
- Before long rentals, map deposit custom, building fees, and winter heating schedule quirks.
- Verify tourist stay and residency products per passport on government sources listed in `references/sources.md`.

## Safety and privacy

- Advise; do not claim real-time crime maps or guarantee neighborhood safety block-by-block.
- No live network actions, bookings, or government filings without explicit user instruction.
- Keep credentials, passport images, residence-card numbers, and payment secrets out of `<state_root>/`.
- Mark unverified mutable facts clearly when official pages cannot be opened.

## Source freshness

Package orientation was bulk-aligned on 2026-10-16 against the URL map in `references/sources.md`. Before any booking-critical or legal claim, open the matching official page again for the user's passport and travel month.
