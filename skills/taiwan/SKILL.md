---
name: taiwan
description: >
  Design Taiwan itineraries with HSR/TRA routing, city-specific food, weather
  backups, and tourist-trap avoidance. Load when planning Taiwan trips, choosing
  bases (Taipei/Taichung/Tainan/Kaohsiung), or asking about night markets, tea,
  hot springs, east-coast logistics, or family pacing. Not for mainland China
  or Japan-only travel plans.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji": "🇹🇼", "requires": {"config": ["<state_root>/taiwan/"]}}'
  related-skills: '{"travel": "general multi-country trip structure beyond Taiwan-specific logistics", "food": "dish-level cuisine guidance when the ask is food, not itinerary routing", "chinese": "language and phrase help beyond Taiwan trip planning", "photography": "shot planning and gear when the trip goal is photo-first"}'
---


## When to load

Load this skill when the user asks to plan a trip to Taiwan, requests advice on Taiwanese cities (Taipei, Taichung, Tainan, Kaohsiung), needs HSR/TRA transit routing, or wants specific local food recommendations (night markets, regional specialties).

## Architecture

Memory lives in `<state_root>/taiwan/`. If `<state_root>/taiwan/` doesn't exist or is empty, read `references/setup.md` and start naturally. See `assets/memory-template.md` for structure.

```text
<state_root>/taiwan/
└── memory.md     # Trip context
```

## Quick Reference

| Topic | File |
|-------|------|
| **Cities** | |
| Taipei neighborhoods, rhythm, day trips | `references/taipei.md` |
| Taichung pacing, design, central hub strategy | `references/taichung.md` |
| Tainan food-first old-town planning | `references/tainan.md` |
| Kaohsiung harbor districts and southern base logic | `references/kaohsiung.md` |
| **Planning** | |
| First-timer and repeat-visitor routes | `references/itineraries.md` |
| Best base by budget and trip style | `references/accommodation.md` |
| Rail, maps, taxi, bike, and booking apps | `references/apps.md` |
| **Food & Drink** | |
| Regional dishes, breakfasts, night markets | `references/food-guide.md` |
| Tea regions, what to buy, how to order | `references/tea.md` |
| **Activities** | |
| Hot springs, scenic rides, cultural wins | `references/experiences.md` |
| Best beaches, islands, and swim realities | `references/beaches.md` |
| Easy urban hikes to alpine planning logic | `references/hiking.md` |
| Night markets, bars, music, late-night rhythm | `references/nightlife.md` |
| **Reference** | |
| North, central, south, east, islands breakdown | `references/regions.md` |
| Etiquette, payment reality, timing, temple manners | `references/culture.md` |
| Family travel pacing and kid-friendly structure | `references/with-kids.md` |
| **Practical** | |
| HSR, TRA, airport access, buses, driving | `references/transport.md` |
| SIMs, eSIMs, LINE, payment and data habits | `references/telecoms.md` |
| Emergency numbers, typhoon, earthquake, clinics | `references/emergencies.md` |

## Core Rules

### 1. Choose the Corridor Before the Wishlist
State "Use the west coast HSR spine for Taipei-Taichung-Tainan-Kaohsiung, and only add the east coast if you have extra days and weather flexibility."

### 2. Match the Base to the Trip
Taiwan is compact, but sleeping in the wrong place wastes the trip:
- Taipei for first-timers, museums, nightlife, and easy transit
- Taichung for a softer pace, cafes, and central Taiwan branching
- Tainan for food and history, not for a rushed checklist
- Kaohsiung for winter sun, harbor walks, and southern side trips

### 3. Transport Strategy Beats Distance Math
Use the right rail layer:
- HSR for long west-coast jumps
- TRA for east coast, local hops, and smaller cities
- MRT, YouBike, taxi, and walking for the last mile
- Car only when the plan is rural, alpine, or island-heavy

### 4. Timing Changes the Whole Experience
- Lunar New Year, long weekends, and major festivals reshape availability and crowd levels
- Summer means heat, humidity, and typhoon risk
- Winter is best for southern cities and many hot-spring trips
- Rain can destroy mountain or coast plans fast, so always give a backup

### 5. Taiwan Rewards Specific Food Advice
State which city, which neighborhood, and what it is good for:
- Taipei for breadth and late convenience
- Tainan for breakfast, snacks, and old-school specialties
- Taichung for cafes and dessert stops
- Kaohsiung for duck rice, seafood, and easygoing evening eating

### 6. Call Out the Real Friction Points
Be explicit about what visitors routinely miss:
- Cash still matters at small stalls and local shops
- The biggest night market is not always the best one
- East coast and mountain plans need weather checks
- A scenic place that looks close on the map may still be a half-day move

### 7. Match the Traveler

| Traveler | Focus on |
|----------|----------|
| First-timer | `references/taipei.md`, `references/itineraries.md`, `references/transport.md`, `references/food-guide.md` |
| Food-first | `references/tainan.md`, `references/food-guide.md`, `references/tea.md`, `references/culture.md` |
| Relaxed repeat visitor | `references/taichung.md`, `references/regions.md`, `references/experiences.md` |
| Southern sun | `references/kaohsiung.md`, `references/beaches.md`, `references/nightlife.md` |
| Family | `references/with-kids.md`, `references/accommodation.md`, `references/transport.md` |

## Common Traps

- Trying to do Taipei, Sun Moon Lake, Tainan, Kaohsiung, and the east coast in one short trip
- Assuming every famous night market is worth the detour
- Booking east-coast or mountain days with zero weather backup
- Treating Taipei and Tainan like the same speed of city
- Relying on cards only, then getting stuck at cash-first spots
- Assuming rail solves the last mile everywhere
- Planning alpine or beach days without checking current conditions

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/taiwan/`

**This skill does NOT:** Access files outside `<state_root>/taiwan/` or make network requests.
