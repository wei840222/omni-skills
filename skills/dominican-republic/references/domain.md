# Dominican Republic Skill Domain

## State location

Resolve `<state_root>` using the **State location** section in `SKILL.md` before any state read or write. Dominican Republic trip state lives under the selected `<state_root>/`.

## When to Use

- Planning a Dominican Republic trip beyond generic resort marketing
- Choosing which coast or base fits calm water, surf, city depth, or independent travel
- Confirming e-ticket, entry, passport, and visa-check paths before non-refundable bookings
- Handling domestic transport, night-driving risk, weather timing, and practical safety
- Not for standing multi-destination travel systems (`travel`), multi-country itineraries (`travel-planning`), or Spanish composition (`spanish`)

## Architecture

Memory lives in `<state_root>/`. If `<state_root>/` does not exist or is empty, run `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/
└── memory.md     # Trip context, route logic, and evolving constraints
```

## Data Storage

- `<state_root>/memory.md` stores durable trip context, route decisions, and constraints for future Dominican Republic planning.
- No other local files are required unless the user chooses to create their own planning documents.
- Avoid storing credentials, full passport numbers, payment details, or third-party private data in skill state.

## Quick Reference

Use this map to load only the decision module that changes the plan in front of you.

| Topic | File | Load when |
|-------|------|-----------|
| Regions and coast fit | `references/regions.md` | Choosing base coast or multi-base route |
| Beaches and water fit | `references/beaches.md` | Calm swim, surf, snorkel, or boat days |
| Entry and documents | `references/entry-and-documents.md` | E-ticket, visa path, passport checks |
| Domestic transport | `references/transport-domestic.md` | Airports, transfers, buses, domestic hops |
| Road trips and driving | `references/road-trips-and-driving.md` | Rental car, night driving, toll roads |
| Safety and emergencies | `references/safety-and-emergencies.md` | 911, beach flags, theft, storm buffer |
| Weather and seasonality | `references/weather-and-seasonality.md` | Hurricane season, heat, rain timing |
| Budget and costs | `references/budget-and-costs.md` | Stay style and daily spend bands |
| Payments and money | `references/payments-and-money.md` | Cards, cash, tips, ATMs |
| Accommodation styles | `references/accommodation.md` | Resort, boutique, apartment, villa |
| Punta Cana / Bavaro | `references/punta-cana-and-bavaro.md` | East-coast resort ease |
| Bayahibe / La Romana | `references/bayahibe-and-la-romana.md` | Calm Caribbean water, lighter AI density |
| Samana / Las Terrenas | `references/samana-and-las-terrenas.md` | Independent beach-town base |
| Puerto Plata / Cabarete / Sosua | `references/puerto-plata-cabarete-and-sosua.md` | North-coast wind and surf |
| Santo Domingo | `references/santo-domingo.md` | City culture overnight, not beach filler |
| Jarabacoa / Constanza | `references/jarabacoa-and-constanza.md` | Highlands and cooler climate |
| Itineraries | `references/itineraries.md` | Sample day patterns and base changes |
| Experiences | `references/experiences.md` | Tours, boats, nature days |
| Food guide | `references/food-guide.md` | Local dining beyond resort buffet |
| Nightlife | `references/nightlife.md` | Evening plans by region |
| Family travel | `references/family-travel.md` | Kids, mobility, beach safety |
| Culture | `references/culture.md` | Local norms and etiquette |
| Telecoms and apps | `references/telecoms-and-apps.md` | SIM, rideshare, delivery apps |
| Setup | `references/setup.md` | First use or empty state |
| Memory template | `references/memory-template.md` | Creating or reshaping memory.md |
| Sources | `references/sources.md` | Official URLs to re-check |

## Core Rules

1. Choose the coast before packing stops. East-coast resort ease, north-coast wind, Samana nature, and Santo Domingo city logic are different products.
2. Prefer fewer transfers and clearer water-fit over ambitious multi-base routes for first-time or low-tolerance travelers.
3. Treat commercial-flight e-ticket completion as a travel-day task; verify nationality-specific visa rules before non-refundable purchases.
4. Default against night self-driving after long flights; prefer professional transfers or an initial hotel night.
5. Load only the reference files needed for the current decision; keep answers execution-oriented and source-checkable.

## Progressive Disclosure

- Start from this file plus `references/regions.md` or the single topic the user asked about.
- Open destination files only after the coast or trip style is in play.
- Open `references/sources.md` when quoting entry, safety, or official destination claims that may change.

## Failure Modes

- Overselling Punta Cana all-inclusives when the user wants calm independent beaches or city depth
- Treating Santo Domingo as a same-day beach side trip from far east-coast resorts
- Ignoring night-driving, transfer time, and hurricane-season buffer
- Inventing visa or e-ticket rules without checking official sources for the traveler's nationality
