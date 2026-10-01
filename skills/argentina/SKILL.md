---
name: argentina
description: >
  Plan an Argentina trip by macro-region, entry path, money strategy, season,
  and domestic transport. Use for Buenos Aires, Mendoza, Iguazu, Patagonia
  Lakes, South Patagonia, Ushuaia, Salta/Jujuy, Peninsula Valdes, or Atlantic
  coast routing with practical logistics. Not for filing a visa, booking
  flights, or stating a nationality-specific entry rule without checking the
  official source for that passport and travel date.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇦🇷"}'
  related-skills: '{"booking":"Keep hotel, flight, and excursion reservation hygiene after the Argentina route is chosen.","car-rental":"Decide when a self-drive segment in wine country, lakes, or the north actually helps.","food":"Extend regional meal planning beyond the Argentina food playbook.","spanish":"Support menus, bookings, and on-the-ground Spanish once the route is set.","travel":"Build a multi-country itinerary when Argentina is only one stop."}'
---

## State location

Argentina trip state may exist in `<workspace>/argentina/`, `<workspace>/memory/argentina/`, or `~/argentina/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/argentina/`, `<workspace>/memory/argentina/`, `~/argentina/`.
3. If none exists and the user wants planning context kept, create `<workspace>/argentina/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/argentina/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants trip context kept across sessions. Legacy `~/Clawic/data/argentina/` is a migration source only. Keep it out of the active lookup order, and move it only when the user asks.

## When to load

Load this skill for an Argentina trip plan, itinerary, entry/money strategy, domestic transport choice, regional routing, park access, or seasonal safety question. Identify passport, dates/month, region cluster, and pace before locking a route.

Read `references/sources.md` before repeating a visa duration, cash/card rule, park tariff, border-hop requirement, or emergency number. Re-check the official page for that nationality and travel date before the user books a non-refundable flight or pays a visa fee.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/setup.md` |
| Visa, stay window, minor paperwork | `references/entry-and-documents.md` |
| Customs, cash limits, food at borders | `references/customs-and-border.md` |
| Cards, cash, exchange, VAT, tips | `references/money-payments-and-exchange.md` |
| Macro-region selection | `references/regions.md` |
| Sample 7–21 day frames | `references/itineraries.md` |
| Lodging strategy | `references/accommodation.md` |
| Budget layers and cost traps | `references/budget-and-costs.md` |
| Flights, buses, trains, buffers | `references/transport-domestic.md` |
| Self-drive and mountain roads | `references/road-trips-and-driving.md` |
| Parks, permits, tickets | `references/national-parks-and-nature.md` |
| Chile/Brazil/Uruguay side trips | `references/border-hops-and-neighbor-countries.md` |
| Buenos Aires | `references/buenos-aires.md` |
| Mendoza / wine country | `references/mendoza-and-wine-country.md` |
| Iguazu / Misiones | `references/iguazu-and-misiones.md` |
| Patagonia Lakes | `references/patagonia-lakes.md` |
| South Patagonia | `references/patagonia-south.md` |
| Ushuaia / Tierra del Fuego | `references/ushuaia-and-tierra-del-fuego.md` |
| Salta / Jujuy | `references/salta-and-jujuy.md` |
| Peninsula Valdes / Puerto Madryn | `references/peninsula-valdes-and-puerto-madryn.md` |
| Cordoba / central | `references/cordoba-and-central-argentina.md` |
| Atlantic coast / Mar del Plata | `references/atlantic-coast-and-mar-del-plata.md` |
| Food, nightlife, family, access | `references/food-guide.md`, `references/nightlife.md`, `references/family-travel.md`, `references/accessibility.md` |
| Safety and season | `references/safety-and-emergencies.md`, `references/weather-and-seasonality.md` |
| Connectivity and apps | `references/telecoms-and-apps.md` |
| Official source map | `references/sources.md` |
| Persisted trip context | `assets/memory-template.md` |

## Core rules

1. Route by macro-region, not map fantasy: for short trips, one anchor cluster plus at most one contrast region.
2. Lock entry path and money strategy before non-refundable flights or long-haul lodging.
3. Ask for month first: Argentina changes sharply by season and latitude.
4. Treat Patagonia as multiple products: Lake District, South Patagonia, and Ushuaia need separate segment plans.
5. Always offer two transport models for multi-region routes (flight-heavy vs bus/road-heavy) with tradeoffs.
6. Budget with friction: transfers, park tickets, excursion timing, and card/cash execution—not headline meal prices alone.
7. Deliver action plans: base-city logic, day flow, booking deadlines, weather fallback, and a safety note for the chosen region.

## Operating plan

Answer the immediate question first. When the user wants a route, return:

- Base-city logic and the cluster being chosen
- Day flow with transfer windows
- Reservation deadlines
- Weather or transport backup
- Safety note for the chosen region
- Money execution note (card vs ARS cash friction)

For an empty state file, follow `references/setup.md` and copy the structure from `assets/memory-template.md` into `<state_root>/memory.md` only after the user wants memory kept.

## Common traps

- Compressing Iguazu, Mendoza, and Patagonia into one short loop.
- Applying one visa pathway to every passport.
- Treating old dual-exchange-rate blog posts as current payment truth without checking sources near departure.
- Planning South Patagonia and Ushuaia as one rushed two-night add-on.
- Defaulting to a rental car inside dense Buenos Aires.
- Ignoring agricultural customs limits on Chile/Argentina land borders.
- Booking parks and boats without a weather-flex block in shoulder or winter months.

## Source freshness

Domain claims in this package were last bulk-checked against the URLs in `references/sources.md` (see file header). Before any booking-critical statement, open the matching official page again for the user's passport and travel month.
