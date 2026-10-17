---
name: chile
description: >
  Plan Chile itineraries with macro-region routing, entry and SAG compliance,
  domestic transport, park reservations, and extreme weather or altitude
  constraints. Use when choosing Atacama vs lakes vs Patagonia vs Rapa Nui,
  checking Permanencia Transitoria / FUI rules, or pricing flight-heavy versus
  bus/road logistics. Prefer `travel` for multi-country standing systems,
  `spanish` for language help, and `food` for deep restaurant planning after the
  route is set.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇨🇱"}'
  related-skills: '{"food":"Deeper restaurant and cuisine planning once the Chile route and base cities are fixed.","spanish":"Language support for bookings, menus, and practical on-the-ground interactions.","travel":"General multi-country trip system, wishlist, and disruption handling outside Chile-specific routing."}'
---

## Setup

If `<state_root>/` doesn't exist or is empty, read `references/setup.md` and start naturally.

## When to Use

User is planning a Chile trip and needs more than generic sightseeing advice: which macro-region to choose, how to route huge distances, what to reserve early, and how to handle entry, SAG declaration, weather, transport, and safety on the ground.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure.

```
<state_root>/
└── memory.md     # Trip context and evolving constraints
```

## Quick Reference

Use this map to load only the Chile subtopic that changes the decision in front of you.

| Topic | File |
|-------|------|
| **Entry and Compliance** | |
| Entry pathway, tourist stay, Rapa Nui rules | `references/entry-and-documents.md` |
| SAG declaration, customs, restricted items | `references/customs-and-biosecurity.md` |
| **Planning Backbone** | |
| Macro-regions and route logic | `references/regions.md` |
| Sample itineraries (5-21 days) | `references/itineraries.md` |
| Domestic flights, buses, airport moves | `references/transport-domestic.md` |
| Self-drive and road-trip reality | `references/road-trips-and-driving.md` |
| National parks, reservations, permits | `references/national-parks.md` |
| Climate and seasonality | `references/weather-and-seasonality.md` |
| Budget, cards, cash, and tipping | `references/budget-and-payments.md` |
| Apps, eSIM, and connectivity | `references/telecoms-and-apps.md` |
| **Major Regions and Bases** | |
| Santiago and central base strategy | `references/santiago.md` |
| Valparaiso and Vina del Mar strategy | `references/valparaiso-and-vina.md` |
| San Pedro de Atacama and the north | `references/atacama.md` |
| Puerto Varas, Chiloe, and the lake district | `references/lake-district-and-chiloe.md` |
| Puerto Natales, Punta Arenas, and Torres | `references/patagonia-and-torres-del-paine.md` |
| Aysen and Carretera Austral | `references/carretera-austral-and-aysen.md` |
| Rapa Nui entry and visit design | `references/rapa-nui.md` |
| **Lifestyle and Execution** | |
| Food, markets, seafood, and wine | `references/food-and-wine.md` |
| Nightlife and evening strategy | `references/nightlife.md` |
| Traveling with children | `references/family-travel.md` |
| Accessibility planning | `references/accessibility.md` |
| **Safety and Verification** | |
| Emergencies, protests, earthquakes, alerts | `references/safety-and-emergencies.md` |
| Official source map | `assets/sources.md` |

## Core Rules

### 1. Route by Latitude, By Geography
Chile is long, transfer-heavy, and season-sensitive. For short trips, lock one macro-region plus Santiago/central coast at most.

### 2. Solve Entry and SAG First
Before building routes, confirm the traveler's entry pathway in `references/entry-and-documents.md` and declaration obligations in `references/customs-and-biosecurity.md`. Chile is strict about undeclared animal and plant products.

### 3. Treat Atacama Altitude and Patagonia Weather as Trip-Shaping
Use `references/atacama.md`, `references/patagonia-and-torres-del-paine.md`, and `references/weather-and-seasonality.md` before promising ambitious days. Altitude, wind, rain, park closures, and ferry timing can break a pretty itinerary.

### 4. Always Offer Two Logistics Models
For each plan provide:
- A faster flight-heavy version
- A slower bus/road-heavy version

Explain the tradeoff in cost, scenery, fatigue, reservation pressure, and weather resilience.

### 5. Price the Full Chain, Not the Headline Fare
Budget using complete Chile trip math: domestic flights, Calama/Puerto Natales transfers, park tickets, refugios or tours, baggage, tolls, and card-vs-cash friction in smaller towns.

### 6. Flag Incompatible Combos Early
Call out mistakes before the user books:
- Atacama plus Torres del Paine in a short trip
- Carretera Austral in bad season without slack
- Rapa Nui planned without the extra entry requirements
- Dense city stays in Valparaiso hill areas without mobility review

### 7. Deliver Operational Plans
Output should include:
- Best base or base pair
- Day-by-day flow with transfer windows
- Reservation deadlines and risk points
- Weather and altitude notes
- Backup plan for delays, strikes, or closures

## Execution Targets

- Treat Chile as a north-south corridor rather than a compact destination.
- Focus on 1-2 regions for short trips rather than attempting Atacama, lakes, and Patagonia together.
- Account for Calama, Puerto Natales, and ferry transfer overhead in planning.
- Schedule lower altitude acclimatization days in San Pedro before attempting high-altitude excursions.
- Secure Torres del Paine reservations months in advance for high season travel.
- Plan for variable card acceptance, mobile signal, and transport frequency outside major cities.

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/`

**This skill does NOT:** Access files outside `<state_root>/` or make network requests.
