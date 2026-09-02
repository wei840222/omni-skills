---
name: madeira
description: Navigate Madeira as visitor, digital nomad, or resident with neighborhoods, levadas, costs, visas, and local insights for the Atlantic island.
metadata:
  openclaw: '{"emoji":"🌴"}'
  related-skills: '{"dubai":"City-level Atlantic/Gulf visitor and resident guidance that Madeira can hand off to for UAE comparisons.","travel":"Standing travel records, visas, and multi-destination planning beyond one island.","portuguese":"Natural Portuguese language help for deeper local integration.","health":"Wellness and safety boundaries when Madeira healthcare or hiking risks come up."}'
---

## When to Use

Use when the user asks about Madeira as a visitor, digital nomad, retiree, or resident: neighborhoods and zones, levadas and mountains, costs, visas/tax residency, transport, food, or local practicalities. For live fares, visa eligibility, tax status, lodging availability, or weather-dependent hiking decisions, load the matching reference and verify the official source before treating a figure as current.

## Quick Reference

| Topic | When to load | File |
|-------|--------------|------|
| **Visitors** | | |
| Specific Traps | Load when planning trips or identifying issues | `references/traps.md` |
| Attractions (must-see vs skip) | Load when discussing attractions (must-see vs skip) | `references/visitor-attractions.md` |
| Itineraries (3/5/7 days) | Load when discussing itineraries (3/5/7 days) | `references/visitor-itineraries.md` |
| Where to stay | Load when discussing where to stay | `references/visitor-lodging.md` |
| Tips & day trips | Load when discussing tips & day trips | `references/visitor-tips.md` |
| **Zones** | | |
| Quick comparison | Load when discussing quick comparison | `references/zones-index.md` |
| Funchal (center, old town, hotel zone) | Load when discussing funchal (center, old town, hotel zone) | `references/zones-funchal.md` |
| Caniço, Santa Cruz, Machico (east) | Load when discussing caniço, santa cruz, machico (east) | `references/zones-east.md` |
| Câmara de Lobos, Ribeira Brava (west) | Load when discussing câmara de lobos, ribeira brava (west) | `references/zones-west.md` |
| Porto Moniz, São Vicente (north) | Load when discussing porto moniz, são vicente (north) | `references/zones-north.md` |
| Choosing guide | Load when discussing choosing guide | `references/zones-choosing.md` |
| **Food** | | |
| Cultural Context | Load when discussing culture or habits | `references/culture.md` |
| Overview & dining scene | Load when discussing overview & dining scene | `references/food-overview.md` |
| Local cuisine & specialties | Load when discussing local cuisine & specialties | `references/food-local.md` |
| Restaurants & recommendations | Load when discussing restaurants & recommendations | `references/food-restaurants.md` |
| Wine & poncha | Load when discussing wine & poncha | `references/food-drinks.md` |
| Markets & groceries | Load when discussing markets & groceries | `references/food-practical.md` |
| **Nature** | | |
| Levadas (best walks by difficulty) | Load when discussing levadas (best walks by difficulty) | `references/nature-levadas.md` |
| Mountains (Pico Ruivo, Pico Areeiro) | Load when discussing mountains (pico ruivo, pico areeiro) | `references/nature-mountains.md` |
| Beaches & natural pools | Load when discussing beaches & natural pools | `references/nature-beaches.md` |
| Gardens & parks | Load when discussing gardens & parks | `references/nature-gardens.md` |
| **Practical** | | |
| Moving & settling | Load when discussing moving & settling | `references/resident.md` |
| Transport (bus, car rental, taxis) | Load when discussing transport (bus, car rental, taxis) | `references/transport.md` |
| Cost of living | Load when discussing cost of living | `references/cost.md` |
| Safety & healthcare | Load when discussing safety & healthcare | `references/safety.md` |
| Weather & microclimates | Load when discussing weather & microclimates | `references/climate.md` |
| Local services (banking, SIM) | Load when discussing local services (banking, sim) | `references/local.md` |
| **Digital Nomads** | | |
| Nomad guide & community | Load when discussing nomad guide & community | `references/nomad.md` |
| Coworking spaces | Load when discussing coworking spaces | `references/nomad-coworking.md` |
| Internet & connectivity | Load when discussing internet & connectivity | `references/nomad-internet.md` |
| **Visas & Legal** | | |
| EU citizens | Load when discussing eu citizens | `references/visas-eu.md` |
| Non-EU & digital nomad visa | Load when discussing non-eu & digital nomad visa | `references/visas-non-eu.md` |
| NHR tax regime | Load when discussing nhr tax regime | `references/visas-tax.md` |

## State location

This is a stateless skill. It does not store or read local configuration state.

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, digital nomad, retiree, EU citizen, long-term resident
- **Timeline**: Short visit, winter escape, permanent move
- **Interests**: Hiking, beaches, remote work, retirement
- Load relevant auxiliary file for details

### 2. Island Geography
Madeira is a small volcanic island (~740 km²) with dramatic terrain:
- **South coast**: Sunnier, warmer, where most people live (Funchal, Caniço)
- **North coast**: Wilder, wetter, more dramatic scenery (São Vicente, Porto Moniz)
- **Mountains**: Central spine reaching 1,862m (Pico Ruivo) — often cloudy
- **Driving times**: Funchal to Porto Moniz ~1.5h, Funchal to Santana ~1h

### 3. Climate Reality (Eternal Spring)
- **Year-round mild**: 17-25°C most of the year
- **No extreme seasons**: Maintains moderate temperatures (sea level)
- **Microclimates**: North vs south, coast vs mountains dramatically different
- **Rain patterns**: More rain Nov-Feb, but brief showers common year-round
- **Mountain weather**: Can be 15°C colder than coast, often foggy
See `references/climate.md` for monthly breakdown.

### 4. Current Data (Feb 2026)

| Item | Range |
|------|-------|
| 1BR rent (Funchal center) | €700-1,000/month |
| 1BR rent (outside Funchal) | €500-750/month |
| Remote worker salary (typical) | €2,500-5,000/month |
| Bus monthly pass | €35 (Funchal), €45 (regional) |
| Restaurant meal | €8-15 (local), €20-40 (upscale) |
| Coffee + pastry | €2-3 |
| Supermarket (monthly, single) | €200-300 |

### 5. Cost Reality
Madeira is affordable by Western European standards:
- **Housing**: Biggest expense, prices rose 2020-2024 but stabilizing
- **Food**: Very affordable eating local; imported goods pricier
- **Healthcare**: Portuguese public system available to residents
- **Car**: Useful but optional in Funchal (good bus network)
- **Flights**: Budget airlines connect to Lisbon, Porto, UK, Germany

### 6. Transport Options
Unlike mainland cities, Madeira has specific transport patterns:
- **Buses (Horários do Funchal)**: Good coverage, €1.95 per ride
- **Car rental**: Essential for exploring; €20-40/day
- **Taxis**: Fixed rates to popular destinations
- **No trains, no metro**: Island is small enough not to need them
- **Airport**: 20min from Funchal; famous challenging approach
See `references/transport.md` for detailed guidance.

### 7. Digital Nomad Hub
Madeira actively courts remote workers:
- **Digital Nomad Village** (Ponta do Sol): Purpose-built community with fast wifi
- **Coworking**: Multiple spaces in Funchal with good internet
- **Community**: Active nomad meetups, especially winter months
- **Connectivity**: Fiber widely available, 4G/5G coverage good
- **D7 Visa**: Portugal's passive income/remote work visa
See `references/nomad.md` for comprehensive guide.

### 8. Zone Matching

| Profile | Best Areas |
|---------|------------|
| Digital nomads | Ponta do Sol, Funchal center, Caniço |
| Beach lovers | Caniço, Machico, Porto Moniz (pools) |
| Hikers | Santana, Ribeira Brava, anywhere with levada access |
| Nightlife/urban | Funchal old town, hotel zone |
| Quiet/nature | North coast (São Vicente, Porto Moniz) |
| Budget-conscious | Machico, Santa Cruz, Câmara de Lobos |
| Families | Funchal suburbs, Caniço |

## EU vs Non-EU Context

Critical distinction for anyone considering Madeira:
- **EU citizens**: Can live and work freely, just need to register after 3 months
- **Non-EU citizens**: Need visa (D7 for passive income, Digital Nomad Visa, work visa)
- **NHR tax regime**: 10-year special tax status for new residents (being phased out for new applicants)
- **Golden Visa**: Investment-based residency (real estate route ended 2023)

See `references/visas-eu.md` and `references/visas-non-eu.md` for detailed requirements.

## Best Times to Visit

| Season | Weather | Crowds | Best For |
|--------|---------|--------|----------|
| **Dec-Feb** | Mild (17-20°C), some rain | Low (except holidays) | Nomads, budget travelers |
| **Mar-May** | Warm (18-22°C), flowers | Medium | Hiking, Flower Festival |
| **Jun-Aug** | Hot (22-26°C), dry | High | Beaches, festivals |
| **Sep-Nov** | Warm (20-24°C), harvest | Medium | Wine harvest, mild crowds |

Year-round destination, but each season has different character.
