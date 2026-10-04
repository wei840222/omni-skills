---
name: indonesia
description: >
  Plan an Indonesia trip by island cluster, entry path, weather and sea conditions,
  and transfer realism. Use for Bali, Nusa islands, Java (Jakarta, Yogyakarta,
  Bromo/Ijen), Lombok/Gilis, Komodo/Flores, or Sumatra routing with practical
  on-the-ground logistics. Not for inventing a nationality-specific visa outcome,
  fixing same-day boat-to-flight connections, or treating map distance as travel time.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇮🇩"}'
  related-skills: '{"travel":"Multi-country or multi-region itineraries when Indonesia is only one stop.","booking":"Hotel, flight, ferry, and excursion reservation hygiene after the Indonesia route is chosen.","food":"Broader meal planning beyond the Indonesia food playbook.","esim":"Connectivity and eSIM setup once island bases are set.","indonesian":"Bahasa Indonesia support for menus, bookings, and on-the-ground phrases."}'
---

## State location

Indonesia trip state may exist in `<workspace>/indonesia/`, `<workspace>/memory/indonesia/`, or `~/indonesia/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/indonesia/`, `<workspace>/memory/indonesia/`, `~/indonesia/`.
3. If none exists and the user wants planning context kept, create `<workspace>/indonesia/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/indonesia/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants trip context kept across sessions. Legacy `~/Clawic/data/indonesia/` is a migration source only. Keep it out of the active lookup order, and move it only when the user asks.

### State tree

| Path | Purpose |
| --- | --- |
| `<state_root>/memory.md` | Trip context, activation preference, and evolving constraints |

## When to load

Load this skill for an Indonesia trip plan, island choice, entry/visa pathway check, domestic transport tradeoff, weather or sea-condition planning, family/accessibility pacing, or destination playbook across Bali, Java, Lombok, Komodo/Flores, or Sumatra.

Identify passport nationality, travel month, trip length, primary goal, and boat/flight tolerance before locking a multi-island route.

Read `references/sources.md` before repeating a visa duration, VOA eligibility, Bali levy rule, customs process, park fee, volcano alert, or emergency number. Re-check the official page for that passport and travel date before the user books a non-refundable flight or pays a visa fee.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/setup.md` |
| Visa, VOA, onward proof, stay limits | `references/entry-and-documents.md` |
| Customs, arrival hour, first transfers | `references/customs-and-arrival.md` |
| Island choice and route strategy | `references/regions.md` |
| Sample itinerary frames | `references/itineraries.md` |
| Lodging strategy | `references/accommodation.md` |
| Budget layers and cost traps | `references/budget-and-costs.md` |
| Cards, cash, payment norms | `references/payments-and-money.md` |
| Flights, trains, ferries, boats | `references/transport-domestic.md` |
| Scooter, driver, road risk | `references/road-trips-and-driving.md` |
| Bali and Nusa islands | `references/bali-and-nusa-islands.md` |
| Jakarta and West Java | `references/jakarta-and-west-java.md` |
| Yogyakarta and Central Java | `references/yogyakarta-and-central-java.md` |
| East Java, Bromo, Ijen | `references/east-java-and-bromo-ijen.md` |
| Lombok and Gili islands | `references/lombok-and-gili-islands.md` |
| Komodo and Flores | `references/komodo-and-flores.md` |
| Sumatra and Bukit Lawang | `references/sumatra-and-bukit-lawang.md` |
| Food, nightlife, family, access | `references/food-guide.md`, `references/nightlife.md`, `references/family-travel.md`, `references/accessibility.md` |
| Safety and season | `references/safety-and-emergencies.md`, `references/weather-and-seasonality.md` |
| Connectivity and apps | `references/telecoms-and-apps.md` |
| Official source map | `references/sources.md` |
| Persisted trip context template | `assets/memory-template.md` |
| Evaluation harness only | `test-prompts.json` |

## Near-miss handoffs

- Multi-country SEA routing beyond Indonesia → `travel`
- Reservation holds after the route is chosen → `booking`
- Bahasa phrasing for menus and local booking → `indonesian`
- eSIM/connectivity setup → `esim`

## Core rules

1. Route by island cluster and transfer friction, not postcard count. For most travelers, keep one main cluster per week (Bali±Nusa/Lombok, Java backbone, Flores/Komodo, or Sumatra).
2. Clear entry path first: passport route, onward proof, and Bali levy assumptions before non-refundable long-haul tickets.
3. Match the island to the user's real objective (first-trip ease, surf, diving, temples, volcanoes, family pacing, remote nature)—not hype alone.
4. Make every plan season- and sea-aware before locking boat days, dive trips, volcano starts, or beach-heavy routes.
5. Prefer driver or rides over scooters unless the user explicitly accepts wet-road and traffic risk.
6. Budget with friction: domestic flights, boats, park fees, cash pockets, and buffer days—not headline hotel rates alone.
7. Deliver action plans: base logic, day flow with transfer windows, booking deadlines, weather fallback, and a safety note for the chosen cluster.

## Operating plan

Answer the immediate question first. When the user wants a route, return:

- Base-island logic and the cluster being chosen
- Day flow with realistic transfer windows
- Reservation deadlines (visa/levy checks, parks, boats, domestic flights)
- Weather or sea-condition backup
- Safety note for the chosen cluster
- Money and connectivity first-day plan

For an empty state file, follow `references/setup.md` and copy the structure from `assets/memory-template.md` into `<state_root>/memory.md` only after the user wants memory kept.

## Prefer these checks

- Compress island lists when the calendar only supports one or two clusters.
- Re-check nationality-specific entry rules instead of reusing another traveler's pathway.
- Treat same-day boat-to-international-flight connections as fragile; return the day before.
- Separate Bali levy and customs steps from immigration when advising arrival hour.
- Plan family and accessibility routes with fewer stairs, night hikes, and rough-road scooters.

## Source freshness

Domain claims in this package were last bulk-checked against the URLs in `references/sources.md` (see file header). Before any booking-critical statement, open the matching official page again for the user's passport and travel month.
