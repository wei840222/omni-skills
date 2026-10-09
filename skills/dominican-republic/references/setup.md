# Setup - Dominican Republic Travel Guide

Read this when `<state_root>/` does not exist or is empty. Resolve `<state_root>`
using the **State location** section in `SKILL.md` before following this guide.
Initialize `<state_root>/memory.md` from `references/memory-template.md` only
when durable trip context must persist.

## First Contact

Answer the immediate Dominican Republic question first, then capture only the facts that change the route:
- Travel window or exact dates
- Resort-heavy, beach-hopping, city, food, remote-work, family, surf, or mixed priorities
- Preferred water type: calm swim water, snorkeling, boat days, or surf and wind
- Tolerance for long road transfers, intercity buses, and rental-car driving
- Budget band and stay style: all-inclusive, boutique, apartment, villa, or mixed
- Whether nightlife, off-resort dining, or independent exploration matters

## What To Save

Keep durable facts in `<state_root>/memory.md`:
- Confirmed coast or base under consideration
- Resort-first vs independent-travel bias
- Family setup, mobility needs, and beach safety needs
- Flight airports and transfer sensitivity
- Water, nightlife, food, and pace priorities
- Open questions such as "Punta Cana vs Samana" or "resort vs boutique hotel"

## Returning Users

Read `<state_root>/memory.md`, reuse what is still valid, and ask only what changed:
- Dates
- Base choice
- Bookings already fixed
- Car, driver, or bus decisions
- Weather or season concerns

## Quick Start Prompts

**"I want an easy beach vacation."**
- Ask whether the user wants an all-inclusive resort, adults-only setup, or family ease.
- Then use `references/punta-cana-and-bavaro.md`, `references/beaches.md`, `references/accommodation.md`, and `references/transport-domestic.md`.

**"I want the more local side of the country."**
- Ask whether the user wants city, beach town, or mountain energy.
- Then use `references/regions.md`, `references/santo-domingo.md`, `references/samana-and-las-terrenas.md`, `references/jarabacoa-and-constanza.md`, and `references/food-guide.md`.

**"I need a full Dominican Republic route."**
- Ask total days, arrival airport, resort vs independent style, and whether the user is comfortable changing bases.
- Then use `references/regions.md`, `references/itineraries.md`, `references/transport-domestic.md`, `references/budget-and-costs.md`, and `references/payments-and-money.md`.

## Important Notes

- Dominican Republic trip quality depends more on choosing the right coast than on packing in more stops.
- East-coast resort ease, north-coast wind, Samana nature, and Santo Domingo city logic are different products.
- The safest planning move is fewer transfers, clearer water-fit, and better weather margin.
- Avoid writing credentials or full identity documents into skill state.
