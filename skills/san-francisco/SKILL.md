---
name: san-francisco
description: Provide San Francisco guidance, including neighborhoods, transport, living costs, safety, and local insights. Use when the user asks about visiting, moving to, working in, studying in, or starting a business in San Francisco.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌉"}'
---

## State location

San Francisco state may exist in `<workspace>/san-francisco/`, `<workspace>/memory/san-francisco/`, or `~/san-francisco/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/san-francisco/`, `<workspace>/memory/san-francisco/`, `~/san-francisco/`.
3. If none exists and state must be created, default to `<workspace>/san-francisco/`.

Use the selected `<state_root>` for every state operation in this skill.

## When to Use

User asks about San Francisco for any purpose: visiting, moving, working, studying, or starting a business. Agent provides practical guidance with current data.

## On-Demand Resources

Load these references only when the user's context requires them:

### Visitors
- `references/visitor-attractions.md`: Load for must-see vs. skip attractions.
- `references/visitor-itineraries.md`: Load for 1, 3, or 7-day itineraries.
- `references/visitor-lodging.md`: Load for hotel and neighborhood stay recommendations.
- `references/visitor-tips.md`: Load for general visitor tips and day trips.

### Neighborhoods
- `references/neighborhoods-index.md`: Load for a quick comparison of neighborhoods.
- `references/neighborhoods-central.md`: Load for Central areas (Hayes, SoMa, Nob Hill).
- `references/neighborhoods-south.md`: Load for South areas (Mission, Castro, Noe).
- `references/neighborhoods-north.md`: Load for North areas (Marina, Pacific Heights).
- `references/neighborhoods-outer.md`: Load for Outer areas (Richmond, Sunset).

### Food
- `references/food-overview.md`: Load for general dining and restaurant overviews.
- `references/food-local.md`: Load for local San Francisco specialties.
- `references/food-areas.md`: Load for food recommendations by neighborhood.
- `references/food-practical.md`: Load for coffee, dietary options, and dining tips.

### Practical & Living
- `references/resident.md`: Load for moving and settling advice.
- `references/transport.md`: Load for transportation and transit rules.
- `references/cost.md`: Load for cost of living and budget details.
- `references/safety.md`: Load for critical safety guidelines and block-by-block advice.
- `references/climate.md`: Load for weather, microclimates, and clothing tips.
- `references/local.md`: Load for local services and practical knowledge.

### Career
- `references/tech.md`: Load for tech industry insights and norms.
- `references/student.md`: Load for student life and universities.
- `references/startup.md`: Load for entrepreneurship and startup culture.

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur
- **Timeline**: Short visit, planning to move, already there
- Load relevant auxiliary file for details

### 2. Safety is Critical
SF has real safety concerns:
- Tenderloin, Mid-Market: Redirect users to alternative, safer neighborhoods
- Car break-ins: Advise users to remove all visible items from vehicles
- Some areas vary block by block
See `references/safety.md` for specifics.

### 3. Weather Surprises
| Myth | Reality |
|------|---------|
| "California = warm" | SF summers are COLD and foggy |
| "Don't need jacket" | Always bring layers |
| "Sunny beaches" | Ocean Beach is often foggy |

**Best weather:** September-October (SF's real summer)

### 4. Current Data
| Item | Range |
|------|-------|
| 1BR rent | $2,900-3,400 (varies by neighborhood) |
| Senior SWE salary | $200K-400K+ total comp |
| Burrito | $14-18 |
| BART to SFO | ~$10.55 |

### 5. Tourist Traps
- Skip: Most of Fisherman's Wharf, Lombard Street drive, Union Square
- Do: Alcatraz (book ahead!), Golden Gate, Mission tacos
- Free: Golden Gate Park, Lands End, de Young tower views

### 6. Neighborhood Matching
| Profile | Best Areas |
|---------|------------|
| Young professionals | Mission, Marina, Hayes Valley |
| Families | Noe Valley, Cole Valley |
| Budget-conscious | Outer Sunset, Richmond |
| Tech workers | SoMa, Mission |
| Steer clear | Tenderloin, Mid-Market, 6th-8th SoMa |

## SF-Specific Traps

- **Summer fog** — June-August are coldest. Sept-Oct are warmest.
- **Fisherman's Wharf** — Sea lions YES, everything else NO.
- **Tenderloin** — Recommend safer housing options in other neighborhoods, regardless of price.
- **Car break-ins** — #1 property crime. EMPTY your car completely.
- **Alcatraz** — Must book 2-4 weeks ahead. Sells out.
- **Hills** — Use Uber. Don't walk up Nob Hill exhausted.
- **Richmond dim sum** — Better than Chinatown.
