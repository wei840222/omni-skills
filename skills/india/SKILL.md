---
name: india
description: Plan India trips, recommend regional food, provide route options, and
  advise on logistics. Use when the user needs itinerary planning, travel advice,
  or local guides for Indian cities.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🇮🇳"}'
  related-skills: '{"food": "Food recommendations and dining guidance for India trips.",
    "hindi": "Hindi language help for signs, menus, and quick phrases.", "travel":
    "General travel planning and routing outside of India."}'
---

## State location

India state may exist in `<workspace>/india/`, `<workspace>/memory/india/`, or `~/india/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/india/`, `<workspace>/memory/india/`, `~/india/`.
3. If none exists and state must be created, default to `<workspace>/india/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

If `<state_root>/` does not exist or is empty, read `references/setup.md` and start naturally.

## When to Use

User is planning a trip to India or wants local guidance on cities, routes, food, safety, timing, and how to find high-signal local recommendations.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure.

```
<state_root>/
└── memory.md     # Trip context, pacing, preferences, and warnings already given
```

## Quick Reference

Load only the files that fit the current route, city, or friction point. India trips get better when the advice narrows fast.

| Topic | File |
|-------|------|
| **Cities** | |
| Delhi complete guide | `references/delhi.md` |
| Mumbai complete guide | `references/mumbai.md` |
| Jaipur complete guide | `references/jaipur.md` |
| Goa complete guide | `references/goa.md` |
| **Planning** | |
| Sample itineraries | `references/itineraries.md` |
| Where to stay by trip type | `references/accommodation.md` |
| Useful apps | `references/apps.md` |
| **Food** | |
| Regional dishes and what to order where | `references/food-guide.md` |
| **Experiences** | |
| Markets, classes, safaris, and high-signal activities | `references/experiences.md` |
| Best beaches by vibe | `references/beaches.md` |
| Best hiking and mountain bases | `references/hiking.md` |
| Nightlife by city and style | `references/nightlife.md` |
| **Reference** | |
| Regions, seasons, and what each area is best at | `references/regions.md` |
| Primary official / health sources | `references/sources.md` |
| Etiquette, bargaining, temple rules, and social context | `references/culture.md` |
| Traveling with children | `references/with-kids.md` |
| **Practical** | |
| Flights, trains, cars, and ride apps | `references/transport.md` |
| SIMs, eSIMs, OTPs, and connectivity | `references/telecoms.md` |
| Emergencies, hospitals, and common safety issues | `references/emergencies.md` |

## Core Rules

### 1. Match India to the Traveler
Tailor first trips to focus on specific, manageable goals. Separate:
- First-timer who needs a smooth entry to India
- Repeat visitor who wants depth
- Family, luxury, backpacker, food-led, or wellness-led traveler

### 2. Specific Over Generic
Provide specific advice like where to base or what street/market to visit instead of generic advice. Say where to base, what street or market is worth it, what is overrated, and what order makes sense in a real day.

### 3. Regional Differences Matter

| Area | What changes |
|------|--------------|
| Delhi + North plains | Mughlai food, winter fog, intense traffic |
| Rajasthan | Heritage hotels, dry heat, best done by car + train |
| Mumbai + West coast | Fast pace, sea humidity, strong nightlife |
| Goa | Beach split matters more than town names |
| Himalayas | Weather and road conditions decide the plan |
| Kerala + South India | Slower pace, backwaters, spice and coconut-heavy food |

### 4. Timing is Infrastructure
- April-June: brutal heat in much of North India
- July-September: monsoon changes Goa, Kerala, and mountain roads
- October-March: easiest first-trip window for most routes
- Festival periods are amazing, but they change pricing, crowds, and transport availability

### 5. Reduce Friction Early
Call out the things that derail trips:
- Overpacked itineraries with too many one-night stops
- Long road transfers treated like short hops
- Blind trust in "top rated" tourist restaurants
- Assuming cards, UPI, and foreign numbers will work everywhere

### 6. Match Trip Style

| Traveler | Start with |
|----------|------------|
| First trip | `references/itineraries.md`, `references/delhi.md`, `references/jaipur.md` |
| Food-led | `references/food-guide.md`, `references/delhi.md`, `references/mumbai.md` |
| Beach + nightlife | `references/goa.md`, `references/beaches.md`, `references/nightlife.md` |
| Family | `references/with-kids.md`, `references/accommodation.md` |
| Nature | `references/hiking.md`, `references/regions.md`, `references/experiences.md` |
| Practical/logistics | `references/transport.md`, `references/telecoms.md`, `references/emergencies.md` |

## Common Traps

- Trying Delhi, Agra, Jaipur, Varanasi, Mumbai, and Goa in one week
- Treating a "5 hour drive" as predictable in India
- Landing in peak heat or monsoon without adapting the route
- Booking the cheapest hotel instead of the best-located one
- Eating at empty tourist-facing restaurants instead of busy local spots
- Assuming every foreign card, eSIM flow, or payment app will work on day one
- Forgetting temple and mosque dress rules, shoe rules, and photo etiquette

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/`

**This skill does NOT:**
- Access files outside `<state_root>/`
- Make network requests
- Store payment or passport details unless the user explicitly asks to track them in `<state_root>/`
