---
name: romania
description: >
  Plan Romania travel itineraries. Trigger when the user asks about Romanian
  regions, Transylvania bases, Bucharest transit, or local logistics.
metadata:
  openclaw: '{"emoji":"🇷🇴","requires":{"config":["<state_root>/romania/"]}}'
  related-skills: '{"booking": "Hotel reservations, guesthouse lodging, and train booking in Romania.", "europe": "Cross-border transit, Schengen rules, and regional EU travel context.", "family": "Family-friendly itineraries, rural tourism, and child activities.", "food": "Traditional Romanian cuisine, regional wine, and dining etiquette.", "travel": "Carpathian routes, castle itineraries, and transport logistics."}'
---

## Setup

If `<state_root>/romania/` does not exist or is empty, read `references/setup.md` and start naturally.

## When to Use

User is planning a Romania trip and needs help that goes beyond generic Europe advice: route shape, regional differences, local food, mountain and seaside timing, practical logistics, and what is worth skipping.

## State location

Romania state may exist in `<workspace>/romania/`, `<workspace>/memory/romania/`, or `~/romania/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/romania/`, `<workspace>/memory/romania/`, `~/romania/`.
3. If none exists and state must be created, default to `<workspace>/romania/`.

Use the selected `<state_root>` for every state operation in this skill.

Stateful skill. Memory lives in `<state_root>/romania/`. If `<state_root>/romania/` does not exist or is empty, run `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/romania/
└── memory.md     # Trip context, route logic, and evolving constraints
```

## Quick Reference

Use this map to load only the Romania subtopic that changes the decision in front of you.

| Topic | File | When to load |
|-------|------|--------------|
| **Cities** | | |
| Bucharest entry hub and urban strategy | `references/bucharest.md` | User asks about bucharest entry hub and urban strategy |
| Brasov and first Transylvania base | `references/brasov.md` | User asks about brasov and first transylvania base |
| Cluj-Napoca for cafes, festivals, and western access | `references/cluj-napoca.md` | User asks about cluj-napoca for cafes, festivals, and western access |
| Sibiu for slower culture and southern Transylvania | `references/sibiu.md` | User asks about sibiu for slower culture and southern transylvania |
| **Planning** | | |
| Region choice and route logic | `references/regions.md` | User asks about region choice and route logic |
| Sample itineraries for 3-10 days | `references/itineraries.md` | User asks about sample itineraries for 3-10 days |
| Where to stay by trip style | `references/accommodation.md` | User asks about where to stay by trip style |
| Essential travel apps | `references/apps.md` | User asks about essential travel apps |
| **Food and Drink** | | |
| Dishes, markets, and restaurant logic | `references/food-guide.md` | User asks about dishes, markets, and restaurant logic |
| Wine regions, tuica, palinca, and ordering cues | `references/wine.md` | User asks about wine regions, tuica, palinca, and ordering cues |
| **Experiences** | | |
| High-value Romania experiences | `references/experiences.md` | User asks about high-value romania experiences |
| Black Sea coast and Danube Delta choice | `references/black-sea.md` | User asks about black sea coast and danube delta choice |
| Carpathian hiking and mountain safety | `references/carpathians-and-hiking.md` | User asks about carpathian hiking and mountain safety |
| **Reference** | | |
| Culture, etiquette, and language cues | `references/culture.md` | User asks about culture, etiquette, and language cues |
| Family travel and mixed-age planning | `references/with-kids.md` | User asks about family travel and mixed-age planning |
| **Practical** | | |
| Trains, buses, driving, and route tradeoffs | `references/transport.md` | User asks about trains, buses, driving, and route tradeoffs |
| SIMs, data, and roaming | `references/telecoms.md` | User asks about sims, data, and roaming |
| Safety, health, and emergency response | `references/emergencies.md` | User asks about safety, health, and emergency response |
| Setup process | `references/setup.md` | User asks about setup process |
| Memory structure | `references/memory-template.md` | User asks about memory structure |

## Core Rules

### 1. Route by Region, Not by Castle Count
Romania works best when the trip has one dominant shape:
- Bucharest plus Brasov for first-timers
- Southern Transylvania for pretty towns and mountain access
- Cluj plus Apuseni for a younger, western-facing trip
- Black Sea or Danube Delta only in warm-season windows

### 2. Specific Beats Generic
Provide specific base recommendations instead of generic Transylvania advice. Say which base, how many nights, what it unlocks, and what the tradeoff is:
- Brasov for easiest first trip and day trips
- Sibiu for slower old-town rhythm and southern routes
- Cluj for urban energy, festivals, and west-side access

### 3. Evaluate Popular Destinations Realistically
Be explicit when something is popular but weak:
- Bran Castle is an icon, not the best castle experience
- Bucharest Old Town is good for a walk, noisy for sleeping
- Mamaia is for party energy, not the best quiet seaside
- Peles Castle can justify a detour; random "Dracula" branding usually cannot

### 4. Treat Transport and Season as Core Planning Inputs
- Trains are best on some corridors, but not all
- Drives that look short on a map can be slow on mountain roads
- Black Sea logic changes sharply outside June to early September
- Winter mountain plans need backup options for fog, ice, and closures

### 5. Match the Trip Style Early

| Traveler | Best starting files |
|----------|---------------------|
| First-time culture trip | `references/bucharest.md`, `references/brasov.md`, `references/itineraries.md` |
| Food-led trip | `references/food-guide.md`, `references/wine.md`, `references/bucharest.md`, `references/sibiu.md` |
| Nature and hiking | `references/carpathians-and-hiking.md`, `references/regions.md`, `references/brasov.md` |
| Family trip | `references/with-kids.md`, `references/accommodation.md`, `references/black-sea.md` |
| Beach trip | `references/black-sea.md`, `references/transport.md`, `references/accommodation.md` |

### 6. Protect the User From Practical Friction
Always cover the execution details that break Romania trips:
- airport or rail entry point
- cash vs card expectations
- realistic transfer times
- weekday vs weekend crowd patterns
- when local verification is smart for hours, tickets, or weather

## Common Traps

- Treating Bucharest as the whole point of Romania instead of the transport hub
- Trying to combine Bucharest, Brasov, Sibiu, Cluj, the Black Sea, and the Delta in one short trip
- Booking Bran Castle as the centerpiece and skipping stronger town or mountain time
- Assuming every rail leg is efficient because the distance looks short
- Choosing Mamaia for a calm family beach week in peak party season
- Going into bear territory with food, poor timing, or zero trail planning
- Building Black Sea plans in shoulder season and expecting full-summer atmosphere

## Security & Privacy

**Data that stays local:** Trip preferences, route decisions, and saved constraints in `<state_root>/romania/`

**This skill does NOT:** Access files outside `<state_root>/romania/` or make network requests.

**Memory rule:** Keep local trip notes only when the user is actively planning Romania or clearly wants continuity across sessions. For one-off answers, help without creating extra trip memory.
