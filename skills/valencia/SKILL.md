---
name: valencia
description: >
  Navigate Valencia for visitors, residents, tech workers, students, and
  entrepreneurs: neighborhoods, metro/EMT/Valenbisi, costs, Digital Nomad/NIE
  orientation, paella lunch culture, Fallas timing, climate, and local services.
  Use for Valencia stay, move, commute, or work-base decisions. Prefer `spain`
  for multi-city Spain routing, `travel`/`travel-planning` for generic trip
  systems, and `expat` for full cross-border move project tracking.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🍊"}'
  related-skills: '{"booking":"Lodging search and reservation completion after a Valencia neighborhood base is chosen.","dubai":"Peer city-guide pattern for another dense metro when comparing city skills.","expat":"Cross-border move project tracking beyond Valencia neighborhood and settling advice.","spain":"Country-level multi-city Spain routing when Valencia is only one stop.","spanish":"Everyday Spanish for menus, bookings, and on-the-ground talk.","travel":"Standing multi-destination travel records when Valencia is one city among several.","travel-planning":"Day-by-day multi-city itineraries when the trip leaves Valencia."}'
---

## State location

Valencia continuity state may exist in `<workspace>/valencia/`, `<workspace>/memory/valencia/`, or `~/valencia/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/valencia/`, `<workspace>/memory/valencia/`, `~/valencia/`.
3. If several candidate directories exist, use only the highest-precedence one and report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create `<workspace>/valencia/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/valencia/` only; otherwise ask for a state root before creating data.

Use the selected `<state_root>` for every state operation in this invocation. Create or update `<state_root>/memory.md` only when the user wants context kept across sessions. Legacy `~/Clawic/data/valencia/` is a migration source only—keep it out of active lookup; move only with explicit user consent (copy, validate, cutover).

Research notes and official source URLs live in `references/sources.md` (progressive disclosure).

Expanded domain rules, seasons, costs orientation, and local pitfalls live in `references/domain.md` (progressive disclosure).

## When to use

Use for **Valencia (city + metro area)** decisions: visit length and neighborhood base, relocation fit, metro/EMT/Valenbisi routing, cost bands, safety street-smarts, tech/work base, visas and residency *orientation*, food (including paella lunch culture), climate, schools, healthcare orientation, and driving-in-city tradeoffs.

Do **not** use this skill as the sole source for a multi-city Spain itinerary (`spain`), a multi-country standing travel system (`travel`), generic day packing across cities (`travel-planning`), or a full move project board (`expat`).

Classify the user first: visitor, planning-to-move, already-resident, tech/remote worker, student, or entrepreneur. Ask only for the next missing detail that changes the recommendation (dates/month, budget currency, passport, kids, Spanish level, beach vs Centro priority).

## Reference routing

Load the smallest set that answers the current question. Prefer `domain.md` + one topic file before opening the full neighborhood or food set.

| Topic | File | When to load |
| --- | --- | --- |
| Continuity setup | `references/setup.md` | User wants persistent Valencia context or empty `<state_root>/` |
| Memory structure | `assets/memory-template.md` | Creating/updating `<state_root>/memory.md` after consent |
| Core rules, traps, context | `references/domain.md` | First substantive answer; always for money/season/visa framing |
| Official source map | `references/sources.md` | Before booking-critical fares, entry rules, residency, or agency claims |
| Visitor attractions | `references/visitor-attractions.md` | Must-see vs skip lists |
| Visitor itineraries | `references/visitor-itineraries.md` | 1/3/7-day frames |
| Visitor lodging | `references/visitor-lodging.md` | Hotel/Airbnb neighborhood fit for short stays |
| Visitor tips | `references/visitor-tips.md` | Day trips, packing, practical visitor traps |
| Neighborhoods index | `references/neighborhoods-index.md` | Quick neighborhood comparison |
| Centro Histórico / Eixample / La Seu | `references/neighborhoods-centro.md` | Historic core bases |
| Ruzafa / Russafa | `references/neighborhoods-ruzafa.md` | Food/nightlife / nomad density |
| Beach / Cabanyal / Malvarrosa | `references/neighborhoods-beach.md` | Seafront bases |
| Patraix / Benimaclet / Campanar | `references/neighborhoods-residential.md` | Residential value bases |
| Choosing guide | `references/neighborhoods-choosing.md` | Profile → neighborhood matching |
| Food overview | `references/food-overview.md` | Dining scene map |
| Local cuisine / paella | `references/food-local.md` | Valencian dishes and lunch timing |
| International / fine dining | `references/food-international.md` | Non-local options |
| Food areas | `references/food-areas.md` | Where to eat by neighborhood |
| Food practical | `references/food-practical.md` | Hours, tipping, reservations |
| Moving & settling | `references/resident.md` | Contracts, utilities, everyday resident life |
| Transport | `references/transport.md` | Metro, EMT, Valenbisi, taxis |
| Cost of living | `references/cost.md` | Rent bands and monthly budgets (ranges, not live quotes) |
| Safety | `references/safety.md` | Street crime patterns and area awareness |
| Climate | `references/climate.md` | Season, heat, Fallas noise |
| Local services | `references/local.md` | Banking, NIE, paperwork orientation |
| Tech industry | `references/tech.md` | Salaries, remote work, offices |
| Business setup | `references/business.md` | Autónomo / company orientation |
| Visas & residency | `references/visas.md` | Tourist stay, Digital Nomad, residency paths (verify passport) |
| Startups | `references/startup.md` | Ecosystem and funding orientation |
| Culture | `references/culture.md` | Customs, timing, Valenciano |
| Healthcare | `references/healthcare.md` | Public / private orientation |
| Education | `references/education.md` | Schools and universities orientation |
| Lifestyle | `references/lifestyle.md` | Expat social life |
| Driving | `references/driving.md` | Car ownership vs city transit |

## Core workflow

1. **Lock context.** Role, month, length of stay, passport (for entry only), budget currency, Spanish comfort, beach vs Centro priority, and whether kids or office commute matter.
2. **Answer the immediate question first.** Then load the smallest reference set from the table—do not dump every file.
3. **Money and paperwork before bookings.** Treat rent bands, metro fares, and visa income floors as orientation. Re-open `references/sources.md` and official pages before non-refundable flights, multi-month leases, or residency filings.
4. **Neighborhood from routine, not hype.** Match late-night return path, commute, noise tolerance (especially Fallas), and budget.
5. **Entry is passport-specific.** Tourist stay windows and visa needs vary. Orient with `references/visas.md`, then verify on Spanish government pages for that nationality and travel date.
6. **Persist only with consent.** Follow `references/setup.md`; keep passport numbers, bank credentials, and full address dumps out of reusable chat logs and `<state_root>/`.

## Core rules (durable)

1. Identify role and timeline before neighborhood or cost advice.
2. Separate **orientation euro ranges** from **live quotes** for rent, fares, and visa fees.
3. Valencians treat **paella as a lunch dish** (roughly 13:00–15:00); tourist restaurants may ignore this—still teach the local pattern.
4. Many shops observe **siesta-style afternoon closures**; plan errands around morning/evening windows and supermarket exceptions.
5. Prefer metro + EMT + Valenbisi + walking for city-only stays; cars are usually a liability in Centro.
6. **Fallas (mid-March)** is loud and booked-out—either embrace the festival or leave town.
7. Spanish works citywide; Valenciano appears on some signage/services—Castilian Spanish remains legally accepted.
8. For multi-city Spain trips, hand off routing to `spain` after the Valencia city block is set.

## Prefer these patterns

- Match Ruzafa for lively walkable food/cafes; Centro for monuments; beach barrios when sea access outranks short Centro walks.
- Quote Digital Nomad / NIE / fare figures only from live official pages (or mark unverified).
- Visit rental listings in person before deposits; Idealista/Fotocasa are search surfaces, not escrow.
- For short culture trips, keep lodging walkable to Centro/Ruzafa unless the user wants beach quiet.
- Before long rentals, map deposit custom, community fees, and August/Fallas service disruptions.
- Verify tourist stay and residency products per passport on government sources listed in `references/sources.md`.

## Safety and privacy

- Advise; do not claim real-time crime maps or guarantee neighborhood safety block-by-block.
- No live network actions, bookings, or government filings without explicit user instruction.
- Keep credentials, passport images, NIE/TIE numbers, and payment secrets out of `<state_root>/`.
- Mark unverified mutable facts clearly when official pages cannot be opened.

## Source freshness

Package orientation was bulk-aligned on 2026-10-16 against the URL map in `references/sources.md`. Before any booking-critical or legal claim, open the matching official page again for the user's passport and travel month.
