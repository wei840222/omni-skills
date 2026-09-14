---
name: miami
description: Navigate Miami as a visitor, resident, tech worker, student, or entrepreneur.
  Use when the user asks about Miami neighborhoods, beaches, costs, safety, local
  insights, or travel plans. Verify live fares, rents, insurance, and hurricane
  conditions before decisive advice.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌴"}'
---
## Load Instructions

When a user asks about Miami (visiting, moving, working, studying, or starting a business), identify their context (tourist, resident, tech worker, etc.) and load the relevant files from `references/` for specific practical guidance.

## Quick Reference

| Topic | File |
|-------|------|
| **Visitors** | |
| Attractions & beaches | `references/visitor-attractions.md` |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` |
| Where to stay | `references/visitor-lodging.md` |
| Tips & day trips | `references/visitor-tips.md` |
| **Neighborhoods** | |
| Quick comparison | `references/neighborhoods-index.md` |
| Downtown & Brickell | `references/neighborhoods-downtown.md` |
| Miami Beach | `references/neighborhoods-beach.md` |
| Wynwood & Design District | `references/neighborhoods-wynwood.md` |
| Coral Gables & Coconut Grove | `references/neighborhoods-coral.md` |
| North (Aventura, Sunny Isles) | `references/neighborhoods-north.md` |
| Choosing guide | `references/neighborhoods-choosing.md` |
| **Food** | |
| Overview & dining scene | `references/food-overview.md` |
| Cuban cuisine & Little Havana | `references/food-cuban.md` |
| Latin American flavors | `references/food-latin.md` |
| Seafood | `references/food-seafood.md` |
| Best dining areas | `references/food-areas.md` |
| Dietary & tips | `references/food-practical.md` |
| **Practical** | |
| Moving & settling | `references/resident.md` |
| Transport | `references/transport.md` |
| Cost of living | `references/cost.md` |
| Safety | `references/safety.md` |
| Weather & hurricanes | `references/climate.md` |
| Local services | `references/local.md` |
| **Sources** | |
| Official sources | `references/sources.md` |
| **Career** | |
| Tech industry | `references/tech.md` |
| Students | `references/student.md` |
| Startups | `references/startup.md` |

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur
- **Timeline**: Short visit, planning to move, already there
- Load relevant auxiliary file for details

### 2. Safety Context
Miami is generally safe in tourist/residential areas. Main concerns:
- Car break-ins (always hide valuables)
- Petty theft in tourist areas
- Stick to well-lit, populated neighborhoods at night
See `references/safety.md` for area-specific guidance.

### 3. Weather Reality
- Hot and humid year-round (avg 77°F/25°C)
- Hurricane season: June 1 - November 30
- Rainy season: May-October (afternoon thunderstorms)
- Best months: November-April (dry, pleasant)
See `references/climate.md` for hurricane prep.

### 4. Current Data
| Item | Range |
|------|-------|
| 1BR rent | $2,200-3,500 (Brickell/Beach) |
| Senior SWE salary | $120K-180K (no state tax) |
| Student budget | $1,800-2,500/month |
| Car insurance | $200-400/month (FL crisis) |

### 5. Tourist Traps
- Prefer: Little Havana, Wynwood Walls, Key Biscayne, Coral Gables
- Lower-value tourist defaults: Ocean Drive dining, Bayside Marketplace, chain restaurants
- Free: South Beach (early morning), Wynwood street art, Brickell City Centre

### 6. Car Is Essential
- Miami is NOT walkable (unlike NYC/London)
- Public transit limited (Metrorail, Metromover downtown only)
- Brightline train to Fort Lauderdale/West Palm useful
- Uber/Lyft expensive for daily use
- Budget for car + parking + insurance

### 7. Neighborhood Matching
| Profile | Best Areas |
|---------|------------|
| Young professionals | Brickell, Edgewater, Midtown |
| Families | Coral Gables, Coconut Grove, Pinecrest |
| Beach lifestyle | Miami Beach, Surfside, Key Biscayne |
| Budget-conscious | Doral, Kendall, Hialeah |
| Tech workers | Wynwood, Brickell, Design District |

## Miami-Specific Traps

- **"Beach party 24/7"** — South Beach is tourists. Locals rarely go.
- **"No need for a car"** — Treat Miami as car-dependent for normal daily life.
- **"Cheap alternative to NYC"** — Rent is now comparable, with lower salaries.
- **Ocean Drive** — Tourist trap. Walk to Lincoln Road or Española Way.
- **Hurricane ignorance** — Know your evacuation zone. Get supplies early.
- **Car insurance shock** — Florida has highest rates in US. Budget $3-4K/year.
- **Condo fees** — Post-Surfside reforms mean high assessments. Ask about reserves.
