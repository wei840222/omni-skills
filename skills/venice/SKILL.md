---
name: venice
description: Navigate Venice as a visitor or resident using practical guidance on neighborhoods, water transport, costs, local dining, and managing tourist areas.
metadata:
  version: "1.0.0"
  clawdbot: '{"emoji":"🏛️","requires":{"bins":[]},"os":["linux","darwin","win32"],"displayName":"Venice"}'
  related-skills: '{"travel": "General travel planning and logistics", "dubai": "Compare luxury city destination", "toronto": "Compare with another major city skill"}'
---

## State Location

Venice trip state may exist in `<workspace>/venice/`, `<workspace>/memory/venice/`, or `~/venice/`.

Before reading or writing trip state, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/venice/`, `<workspace>/memory/venice/`, `~/venice/`.
3. If none exists and the user requests persistent trip memory, create `<workspace>/venice/`.

Use the selected `<state_root>` for every state operation in this skill. State resolution does not authorize persistence: create or modify state only with explicit user confirmation or an applicable host policy. When creating `memory.md`, copy the structure from `references/memory-template.md`.

## When to Use

User asks about Venice for any purpose: visiting, understanding the city, planning trips, or exploring Venetian culture. Agent provides practical guidance avoiding tourist traps.

## Quick Reference

| Topic | File |
|-------|------|
| **Visitors** | |
| Must-see vs skip | `references/visitor-attractions.md` |
| Itineraries (1/3/5 days) | `references/visitor-itineraries.md` |
| Where to stay by area | `references/visitor-lodging.md` |
| Tips & day trips | `references/visitor-tips.md` |
| **Neighborhoods (Sestieri)** | |
| Quick comparison | `references/neighborhoods-index.md` |
| San Marco & Castello | `references/neighborhoods-sanmarco.md` |
| Dorsoduro & Giudecca | `references/neighborhoods-dorsoduro.md` |
| San Polo & Santa Croce | `references/neighborhoods-sanpolo.md` |
| Cannaregio & Jewish Ghetto | `references/neighborhoods-cannaregio.md` |
| Islands (Murano, Burano, Lido) | `references/neighborhoods-islands.md` |
| Choosing guide | `references/neighborhoods-choosing.md` |
| **Food** | |
| Overview & dining scene | `references/food-overview.md` |
| Venetian cuisine | `references/food-local.md` |
| Cicchetti & bacari culture | `references/food-cicchetti.md` |
| Best areas for dining | `references/food-areas.md` |
| Practical (reservations, tourist traps) | `references/food-practical.md` |
| **Practical** | |
| Transport (vaporetti, water taxis) | `references/transport.md` |
| Cost of living & visiting | `references/cost.md` |
| Safety & scams | `references/safety.md` |
| Weather & acqua alta | `references/climate.md` |
| Local services | `references/local.md` |
| **Culture** | |
| History & context | `references/history.md` |
| Art & museums | `references/art.md` |
| Carnevale & festivals | `references/festivals.md` |
| Venetian customs | `references/culture.md` |
| **Sustainability** | |
| Overtourism & responsible visit | `references/sustainability.md` |
| **Memory** | |
| Trip state template | `references/memory-template.md` |

## Core Rules

### 1. Identify User Context First
- **Role**: Day-tripper, multi-day visitor, art enthusiast, first-timer, returning visitor
- **Season**: High season (Apr-Oct), Carnevale, acqua alta period
- **Mobility**: Venice has 400+ bridges with steps — mobility considerations crucial
Load relevant auxiliary file for details.

### 2. Island City Reality
Venice is 118 small islands connected by 400+ bridges:
- **No cars, bikes, or wheeled transport** in historic center
- **Walking + boats** are the only options
- **Getting lost is inevitable** — and part of the charm
- **Bridges have steps** — no ramps in most places
See `references/transport.md` for navigation strategies.

### 3. Tourist Trap Capital
Venice has more tourist traps per square meter than anywhere in Europe:
- **San Marco pricing**: 2-3x normal prices for everything
- **"Tourist menus"**: Poor quality at premium prices
- **Gondola scams**: Always agree price before boarding
- **Glass "Murano"**: Much sold in Venice is Chinese-made
See `references/food-practical.md` and `references/safety.md` for avoidance strategies.

### 4. Water & Weather
Venice's relationship with water defines daily life:
- **Acqua alta**: Flooding (Oct-Mar), check forecasts, bring boots
- **Humidity**: High year-round, affects comfort and art preservation
- **Fog (nebbia)**: Winter mornings can be atmospheric but disorienting
- **Summer**: Hot, crowded, mosquitoes near canals
See `references/climate.md` for monthly breakdown and preparation.

### 5. Current Data (Feb 2026)

| Item | Range |
|------|-------|
| Vaporetto 75-min ticket | €9.50 |
| Vaporetto 24h pass | €25 |
| Vaporetto 7-day pass | €65 |
| Gondola ride (30 min) | €80-100 daytime, €100-120 evening |
| Water taxi airport | €110-130 |
| Espresso at bar | €1.20-1.50 (standing), €3-6 (seated San Marco) |
| Spritz | €3-4 (bacaro), €12-18 (San Marco terrace) |
| Museum Pass (11 museums) | €40 |
| Day trip entry fee | €5 (peak days, required) |

### 6. Cost Reality
Venice is expensive but manageable with strategy:
- **Accommodation**: 2-3x mainland prices. Mestre as budget alternative.
- **Food**: Eat where locals eat (bacari, away from San Marco)
- **Transport**: Passes pay off quickly (individual tickets expensive)
- **Entry fee**: €5 day-tripper fee on peak days (2024+)
- **Booking fees**: Major sites charge €1-5 booking fees

### 7. Sestiere (Neighborhood) Matching

| Profile | Best Areas |
|---------|------------|
| First-timers wanting central | San Marco (expensive), Castello (better value) |
| Art lovers | Dorsoduro (Accademia, Peggy Guggenheim) |
| Authentic Venice | Cannaregio, Santa Croce |
| Foodies | San Polo (Rialto market area) |
| Nightlife (limited) | Dorsoduro (Campo Santa Margherita) |
| Families | Lido (beach), Giudecca (quiet) |
| Budget-conscious | Mestre (mainland), Cannaregio (less touristy) |

## Timing Context

### High Season (Apr-Oct)
- Crowds peak at San Marco 10am-4pm
- Book accommodations months ahead
- Restaurant reservations essential
- Arrive early (before 9am) or late (after 6pm) for sights

### Shoulder Season (Nov-Mar)
- Acqua alta risk highest Nov-Dec
- Many tourists leave — authentic Venice emerges
- Some restaurants/hotels closed
- Carnevale (Feb) brings temporary crowds

### Best Times
- **Late September**: Warm, fewer crowds, Regata Storica
- **Early November**: Pre-acqua-alta, very few tourists
- **January (non-Carnevale)**: Cheapest, quietest, cold but magical

## Venice-Specific Traps

- **Standing vs sitting prices** — Coffee €1.50 standing, €6+ at table (especially San Marco). Ask "al banco?" for bar price.
- **Restaurant "cover charge"** (coperto) — €2-5/person is normal. Check menu for it.
- **"Menu turistico"** — Fixed menus near San Marco are typically tourist traps. Select alternative local restaurants.
- **Fake Murano glass** — Ask for certificate. If price seems too good, it's Chinese.
- **Gondola overcharging** — Official rate €80/30min. Agree price AND duration before boarding.
- **Wrong vaporetto direction** — San Marco has multiple stops. Check direction on digital signs.
- **Water taxi airport quote** — Should be €110-130 total to city center, not per person.
- **Rialto Bridge shopping** — Overpriced everything. Walk 2 minutes away for real prices.
- **Booking unnecessary tours** — Most churches free. St. Mark's needs timed slot (free), not paid tour.
- **Cruise ship timing** — Check arrivals. 10am-4pm when ships dock is peak chaos.

## Mobility Considerations

Venice is challenging for mobility issues:
- **400+ bridges** with steps (no ramps on most)
- **No wheelchairs** in historic center without careful planning
- **Water buses** (vaporetti) have gaps to board
- **"Accessible" routes exist** but are limited and indirect
- **Strollers**: Possible but exhausting — consider baby carrier

See `references/transport.md` for accessible route information.
