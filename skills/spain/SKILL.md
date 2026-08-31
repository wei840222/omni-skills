---
name: spain
compatibility: 'none'
allowed-tools: null
license: 'none'
description: 'Plans Spain travel with local-level picks: named restaurants, regional rules, timing, booking windows, and tourist-trap avoidance. Use when the user plans or books a trip to Spain, builds an itinerary, or asks about Madrid, Barcelona, Sevilla, Granada, Valencia, Bilbao, Málaga, or San Sebastián, the Balearics or Canaries, tapas, paella, pintxos, wine or flamenco, festivals like San Fermín, Fallas, or Semana Santa, walking the Camino de Santiago, beaches, hiking, AVE trains, driving and car rental, SIM cards, safety and pickpockets, or traveling Spain with kids. Not for learning the Spanish language — that is the spanish skill.'
metadata:
  openclaw: '{"emoji":"🇪🇸","requires":{"config":["<state_root>/"]},"displayName":"Spain"}'
  related-skills: '["travel", "spanish", "madrid", "barcelona", "europe"]'
---


## State location

User preferences and memory live in `<state_root>/`.
- `<state_root>/config.yaml` for structured preferences.
- `<state_root>/memory.md` for conversational trip context.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| budget_level | backpacker \| mid \| high | mid | Selects the accommodation tier (hostel/pensión vs 3-4★ vs parador) and restaurant bracket recommended in every guide |
| dietary | list (vegetarian, vegan, gluten-free, halal) | none | Filters every restaurant pick; routes through Dietary Needs in `references/food-guide.md` |
| travel_pace | packed \| relaxed | relaxed | Packed keeps the day trips in `references/itineraries.md`; relaxed drops them and adds free half-days |
| transport_mode | train \| car \| fly | train | Reorders the mode table in `references/transport.md`; car unlocks white-village, winery, and north-coast routing |

Preference areas to record as the user reveals them:

- **trip context** — dates, regions, group (solo/couple/family/friends), trip style — lives in `references/memory.md` and drives the Match Trip Style table
- **food** — adventurousness (offal, percebes vs safe orders), Michelin interest, drinking habits — affects food-guide and wine picks
- **accommodation style** — hotel vs apartment vs parador vs hostel — affects accommodation.md recommendations
- **booking posture** — lock everything early vs stay spontaneous — affects how hard the Book-Ahead Ladder is pushed
- **crowd tolerance** — iconic sights regardless of crowds vs quieter alternatives — affects Gaudí/Alhambra/beach picks
- **daily rhythm** — early riser vs night owl — affects whether timing advice fights or embraces the late Spanish schedule
- **mobility / accessibility** — step-free needs, elevator-required lodging, stroller or wheelchair access — routes the hill/steps constraints (Albaicín and Alhambra climbs, Sacromonte, cave venues), the no-elevator warning on old-building apartments in `references/accommodation.md`, and metro-with-stroller notes
- **units / locale** — temperature scale (°C vs °F) and home currency for € conversions — affects how temperatures and prices are quoted; default °C and € shown as-is

## When To Use

**Mode: advise.** You counsel the traveler and prepare picks, itineraries, and booking plans for them to act on — you advise and counsel while the user handles booking, payment, and transactions.

- Planning or booking a Spain trip: itinerary, where to stay, what to book how far ahead
- Choosing places: which city, island, beach, hike, winery, festival, or Camino route fits this traveler
- Eating well: named restaurant picks, regional dishes, meal timing, tourist-trap detection
- On-the-ground logistics: AVE trains, driving, SIM/eSIM, money, safety, emergencies, apps
- Sanity-checking advice against regional rules (paella timing, free tapas, pintxos mechanics, languages)
- Not for learning the Spanish language — that's the `spanish` skill

## Quick Reference

To effectively advise the user, load these files based on the context of their query.

| Situation | File | When to load |
|---|---|---|
| **Cities** | | |
| Madrid: eating, museums, neighborhoods | `references/madrid.md` | When discussing Madrid activities or stays. |
| Barcelona: Gaudí, tapas, pickpockets | `references/barcelona.md` | When user mentions Barcelona. |
| Sevilla: heat, Feria, monuments | `references/sevilla.md` | When talking about Seville or Andalusia. |
| Granada: Alhambra tickets, free tapas | `references/granada.md` | When booking Alhambra or visiting Granada. |
| Valencia: paella rules, Fallas | `references/valencia.md` | When discussing Valencia or paella. |
| Bilbao: Guggenheim, Basque coast base | `references/bilbao.md` | For Bilbao or Basque itineraries. |
| Málaga: museums, espetos, Andalusia gateway | `references/malaga.md` | When visiting Malaga or Costa del Sol. |
| San Sebastián: pintxos, Michelin | `references/san-sebastian.md` | When discussing food in San Sebastián. |
| **Planning** | | |
| Building a route, sample itineraries | `references/itineraries.md` | When user is planning a route. |
| Where to stay, prices by city | `references/accommodation.md` | When asked about lodging options. |
| Balearics vs Canaries, which island | `references/islands.md` | When choosing Spanish islands. |
| Apps to install before landing | `references/apps.md` | Before the trip starts. |
| **Food & Drink** | | |
| Regional dishes, markets, dietary needs | `references/food-guide.md` | When giving restaurant or food advice. |
| Wine regions, bodega visits | `references/wine.md` | When user asks about Spanish wine. |
| **Experiences** | | |
| Standout experiences, overrated list | `references/experiences.md` | When looking for activities or avoiding traps. |
| Beach guide by coast | `references/beaches.md` | For coastal trips. |
| Hiking routes and permits | `references/hiking.md` | When user wants to hike. |
| Nightlife by city, LGBTQ+ | `references/nightlife.md` | When asked about going out. |
| Walking the Camino de Santiago | `references/camino.md` | For Camino advice. |
| **Reference** | | |
| Core rules of advising | `references/core-rules.md` | Always, to ensure high quality local advice. |
| Tourist traps | `references/traps.md` | When sanity checking an itinerary. |
| Security and privacy | `references/security-and-privacy.md` | When handling user data. |
| Output gates | `references/output-gates.md` | Before providing final recommendations. |
| Domain Knowledge | `references/domain-knowledge.md` | When asking for broad Spain tourism facts. |
| 17 regions, what changes in each | `references/regions.md` | When planning multi-region trips. |
| Customs, eating times, festivals, phrases | `references/culture.md` | For cultural queries. |
| Traveling with children | `references/with-kids.md` | If traveler is a family. |
| **Practical** | | |
| Trains, flights, driving, city transit | `references/transport.md` | For transit advice. |
| SIM, eSIM, coverage | `references/telecoms.md` | For mobile phone connectivity. |
| Theft, health, 112, heat | `references/emergencies.md` | In case of emergencies or safety questions. |
| Anything else (visas, weather, currency) | Answer inline; log the gap in `<state_root>/memory.md` | If topic is missing. |
