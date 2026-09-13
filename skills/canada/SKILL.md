---
name: canada
description: Plan Canadian travel with concrete regional recommendations, city guides,
  nature-route logistics, and practical timing. Use when choosing East vs West focus,
  Banff/Jasper shuttle plans, city food bases, or season tradeoffs across provinces.
  Not for multi-country trip systems (`travel`), deeper cuisine workflows (`food`),
  or English/French writing production (`english` / `french`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🍁"}'
  related-skills: '{"travel":"Multi-destination trip systems and general travel memory beyond Canada-only routing.","food":"Deeper cuisine workflows beyond Canadian regional food pointers.","english":"English writing and register rather than Canada logistics.","french":"French writing and register, especially for Quebec service context."}'
---

## Setup

If `<state_root>/canada/` doesn't exist or is empty, read `references/setup.md` and start naturally.

## When to Use

User planning a trip to Canada or asking for local insights: what to eat, which regions to prioritize, what to skip, season tradeoffs, and practical logistics.

## Architecture

Memory lives in `<state_root>/canada/`. See `references/memory-template.md` for structure.

```
<state_root>/canada/
└── memory.md     # Trip context
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Cities & Regions** | | |
| Toronto complete guide | `references/toronto.md` | Load for toronto complete guide |
| Vancouver complete guide | `references/vancouver.md` | Load for vancouver complete guide |
| Montreal complete guide | `references/montreal.md` | Load for montreal complete guide |
| Banff & Jasper complete guide | `references/banff-jasper.md` | Load for banff & jasper complete guide |
| **Planning** | | |
| Sample itineraries | `references/itineraries.md` | Load for sample itineraries |
| Where to stay by style | `references/accommodation.md` | Load for where to stay by style |
| Useful apps | `references/apps.md` | Load for useful apps |
| **Food & Drink** | | |
| Regional dishes and restaurants | `references/food-guide.md` | Load for regional dishes and restaurants |
| Wine regions and tastings | `references/wine.md` | Load for wine regions and tastings |
| **Experiences** | | |
| Signature experiences | `references/experiences.md` | Load for signature experiences |
| Beaches and lake towns | `references/beaches.md` | Load for beaches and lake towns |
| Hikes and safety by season | `references/hiking.md` | Load for hikes and safety by season |
| Nightlife by city | `references/nightlife.md` | Load for nightlife by city |
| **Reference** | | |
| Provinces and regional differences | `references/regions.md` | Load for provinces and regional differences |
| Culture, etiquette, expectations | `references/culture.md` | Load for culture, etiquette, expectations |
| Traveling with children | `references/with-kids.md` | Load for traveling with children |
| **Practical** | | |
| Intercity transport | `references/transport.md` | Load for intercity transport |
| Phone and internet | `references/telecoms.md` | Load for phone and internet |
| Emergencies and safety | `references/emergencies.md` | Load for emergencies and safety |
| Research anchors / official sources | `references/sources.md` | Verify entry, park, transport, or seasonal claims |

## Core Rules

### 1. Specific Over Generic
Use concrete guidance like: "start in St. Lawrence Market before 10:30, then walk to Distillery District after lunch when crowds thin, and skip CN Tower at sunset unless you prebook a timed slot."

### 2. Local Perspective
What locals actually do, not brochure advice:
- Toronto food courts in major landmarks are expensive and average; better meals are often one block away
- Vancouver's Capilano Suspension Bridge is polished but pricey; Lynn Canyon is free and quieter
- Montreal downtown chain brunch spots are crowded; neighborhood bakeries are better value and faster
- Banff town can feel overrun in peak summer; sunrise starts and shuttle-first planning matter

### 3. Regional Differences

| Region | Key difference |
|--------|----------------|
| Ontario | Big-city pace, museum and food density, easy road trips |
| Quebec | French-first culture, stronger local identity, distinct food scene |
| British Columbia | Ocean + mountain access, outdoor focus, high accommodation costs |
| Alberta Rockies | Nature-first itineraries, weather shifts fast, shuttle logistics crucial |
| Atlantic Canada | Coastal towns, seafood focus, slower pace, weather variability |
| North (Yukon/NWT/Nunavut) | Extreme distances, northern lights potential, higher costs |

### 4. Timing is Everything
- Peak summer in major parks: book accommodation and shuttles months ahead
- Fall foliage: late September to mid October in many areas, but dates vary by province
- Winter city trips: easier prices, fewer crowds, but daylight is short
- Long weekends: highway and airport congestion spikes
- Shoulder seasons: often best value for urban + nature combinations

### 5. Flag Tourist Traps
Flag these specific tourist traps:
- Any restaurant with giant wait and mostly social-media hype near main attractions
- Last-minute Banff parking attempts in July and August
- Paying premium prices for generic airport transfer options without checking rail or bus alternatives
- Underestimating drive times in mountain areas because map distance looks short

### 6. Match Trip Style

| Traveler | Focus on |
|----------|----------|
| Foodie | `references/food-guide.md`, `references/montreal.md`, `references/toronto.md` |
| Nature | `references/banff-jasper.md`, `references/hiking.md`, `references/experiences.md` |
| Family | `references/with-kids.md`, `references/accommodation.md`, `references/itineraries.md` |
| City break | `references/toronto.md`, `references/montreal.md`, `references/nightlife.md` |
| Scenic road trip | `references/itineraries.md`, `references/transport.md`, `references/hiking.md` |
| Wine trip | `references/wine.md`, `references/regions.md` |

## Common Traps

- Treating Canada like one compact destination. Distances are huge.
- Trying to combine too many provinces in one short trip.
- Booking Rockies logistics too late in peak season.
- Assuming weather stability in mountain regions.
- Ignoring bilingual context in Quebec service interactions.
- Expecting cheap data plans without checking eSIM or prepaid options first.
- Relying on rideshare in remote areas where coverage is inconsistent.
- Missing travel insurance for trips with outdoor activities.

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/canada/`

**This skill does NOT:** Access files outside `<state_root>/canada/` or make network requests.

## State location

This skill is stateful.
The skill maintains user preferences and memory at the following paths (in order of precedence):
1. `<state_root>/canada/` (Workspace state)
2. `~/.config/agentskills/canada/` (Global state fallback)

If no state directory exists, it will create `<state_root>/canada/` upon first execution.
