---
name: madrid
description: Provide practical Madrid guidance for visitors, relocators, tech workers,
  students, and founders—neighborhoods, transport, costs, safety, food, and lifestyle.
  Use when the user asks about Madrid-specific decisions; verify live fares, rents,
  tickets, and safety conditions before decisive advice. Not a substitute for Spain-wide
  multi-city routing (`spain`/`travel`) or Barcelona-only depth (`barcelona`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇪🇸","requires":{"config":["<state_root>/madrid/"]}}'
  related-skills: '{"spain":"Spain-wide destinations, regional routing, and multi-city itineraries beyond Madrid-only depth.","travel":"General multi-destination trip systems and travel memory.","barcelona":"Compare or switch to Barcelona-specific neighborhood, cost, and lifestyle depth.","europe":"Cross-border EU mobility context beyond Madrid.","booking":"Lodging and reservation execution after a Madrid base is chosen.","career":"Broader career decisions after Madrid tech or job context is set.","startup":"Founder workflows after Madrid startup landscape is scoped.","food":"Deeper food-system workflows beyond madrileño dining guidance."}'
---

## State location

Persistent Madrid context lives under `<state_root>/madrid/` when the user wants ongoing trip or relocation memory. One-off visitor questions can stay effectively stateless.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/madrid/`, `<workspace>/memory/madrid/`, `~/madrid/`.
3. If none exists and state must be created, default to `<workspace>/madrid/`.

Use the selected `<state_root>` for every state operation in this skill.

```text
<state_root>/madrid/
└── memory.md     # User context and preferences
```

## When to Use

User asks about Madrid for visiting, relocating, working remotely, studying, or starting a business. Establish role, timeline, budget, party, language level, and neighborhood constraints first, then load only the needed reference files. For multi-city Spain trips prefer `spain`/`travel`; for Barcelona-only depth prefer `barcelona`.

Treat dated package figures as planning estimates. Before booking, immigration, payment, or same-day safety decisions, open the matching reference and verify the official source in `references/sources.md`.

## Quick Reference

| Topic | File |
|-------|------|
| **Sources** | |
| Official / primary URLs | `references/sources.md` |
| **Visitors** | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` |
| Where to stay | `references/visitor-lodging.md` |
| Tips & day trips | `references/visitor-tips.md` |
| **Neighborhoods** | |
| Quick comparison | `references/neighborhoods-index.md` |
| Central (Centro, Sol) | `references/neighborhoods-central.md` |
| North (Chamberí, Tetuán) | `references/neighborhoods-north.md` |
| South (Usera, Carabanchel) | `references/neighborhoods-south.md` |
| East (Salamanca, Retiro) | `references/neighborhoods-east.md` |
| Choosing guide | `references/neighborhoods-choosing.md` |
| **Food** | |
| Overview & restaurants | `references/food-overview.md` |
| Traditional madrileño | `references/food-traditional.md` |
| Markets | `references/food-markets.md` |
| Best areas | `references/food-areas.md` |
| Dietary & tips | `references/food-practical.md` |
| **Practical** | |
| Moving & settling | `references/resident.md` |
| Transport | `references/transport.md` |
| Cost of living | `references/cost.md` |
| Safety | `references/safety.md` |
| Weather | `references/climate.md` |
| Local services | `references/local.md` |
| **Career** | |
| Tech industry | `references/tech.md` |
| Students | `references/student.md` |
| Startups | `references/startup.md` |

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur
- **Timeline**: Short visit, planning to move, already there
- Load only the relevant auxiliary file for details

### 2. Safety Context
Madrid is generally very safe. Main concerns:
- Pickpocketing (tourist areas)
- Phone snatching (rare but rising)
- Late-night incidents (specific areas)
See `references/safety.md` for area-specific guidance and verify live advisories when needed.

### 3. Weather Expectations
- Continental climate with extremes
- Summer: very hot (often 35-40°C in July-August)
- Winter: cold but sunny (often 5-10°C)
- Best months: April-June, September-October
- Pack layers for large day/night temperature swings
- Confirm heat or storm alerts via AEMET links in `references/sources.md`

### 4. Current Data (Feb 2026 planning estimates)

| Item | Range |
|------|-------|
| 1BR rent | €1,200-1,800 (central) |
| Senior SWE salary | €50K-80K total comp |
| Student budget | €1,000-1,400/month |
| Metro monthly pass | €54.60 (Zona A regular) / €32.70 (with temporary discounts) — runs 06:00 to 01:30 |

Verify fares on CRTM / Metro de Madrid and rents on live listings before decisive advice.

### 5. Tourist Traps
- Skip: Mercado de San Miguel (overpriced), Botín (tourist trap)
- Do: El Rastro (Sundays), Mercado de San Fernando, rooftop bars
- Free windows: Museo del Prado (last 2h), Reina Sofía free slots, Retiro Park — confirm current hours on museum sites

### 6. Transit Over Driving
- Metro + bus covers most needs
- Multi card or contactless
- BiciMAD for central areas
- Parking + traffic make driving impractical for visitors

### 7. Neighborhood Matching

| Profile | Best Areas |
|---------|------------|
| Young professionals | Malasaña, Lavapiés, La Latina |
| Families | Retiro, Chamberí, Arganzuela |
| Budget-conscious | Tetuán, Usera, Vallecas, Carabanchel |
| Tech workers | Salamanca, Chamartín, Malasaña |

## Madrid-Specific Traps

- **"Siesta culture"** — Modern Madrid works normal hours. Some shops close 2-5pm, but not offices.
- **Mercado de San Miguel** — Beautiful but tourist trap. Prefer Mercado de San Fernando or Antón Martín.
- **Casa Botín** — Claims oldest restaurant. Overpriced; better cocido elsewhere.
- **Plaza Mayor dining** — Expensive, mediocre. Walk to nearby side streets.
- **Taxi to airport** — Fixed €33 from center is the usual rule of thumb; refuse unmetered markups and confirm current official notices.
- **August** — Many locals leave and some businesses close; plan heat and closures explicitly.
