---
name: vancouver
description: Load this skill when the user asks about visiting, moving to, working
  in, or navigating Vancouver. Read the relevant references to answer questions about
  neighborhoods, transit, dining, immigration, or local culture.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🏔️"}'
  related-skills: '{"toronto": "Canada city guide and immigration context", "seattle": "Nearby US city tech and outdoor culture"}'
---
## When to load

User asks about Vancouver for any purpose: visiting, moving, working, studying, or starting a business. Agent provides practical guidance with current data.

**Instructions:** When a user asks about a specific Vancouver topic, load and read the corresponding file in the `references/` directory to gather accurate and contextual guidance before responding.

## Quick Reference

| Topic | File |
|-------|------|
| **Visitors** | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` |
| Where to stay | `references/visitor-lodging.md` |
| Tips & day trips | `references/visitor-tips.md` |
| **Neighborhoods** | |
| Quick comparison | `references/neighborhoods-index.md` |
| Downtown, Yaletown, Coal Harbour | `references/neighborhoods-downtown.md` |
| Kitsilano, Point Grey, West Side | `references/neighborhoods-westside.md` |
| East Van, Commercial Drive, Main St | `references/neighborhoods-eastside.md` |
| North Shore, West Van, Deep Cove | `references/neighborhoods-northshore.md` |
| Burnaby, Richmond, Surrey suburbs | `references/neighborhoods-suburbs.md` |
| Choosing guide | `references/neighborhoods-choosing.md` |
| **Food** | |
| Overview & dining scene | `references/food-overview.md` |
| Asian cuisines (Chinese, Japanese, Korean) | `references/food-asian.md` |
| Local & farm-to-table | `references/food-local.md` |
| International & fine dining | `references/food-international.md` |
| Best areas for dining | `references/food-areas.md` |
| Dietary, craft beer, cannabis | `references/food-practical.md` |
| **Practical** | |
| Moving & settling | `references/resident.md` |
| Transit (SkyTrain, buses, SeaBus) | `references/transport.md` |
| Cost of living | `references/cost.md` |
| Safety & neighborhoods | `references/safety.md` |
| Weather & rain survival | `references/climate.md` |
| Local services (banking, SIM, MSP) | `references/local.md` |
| **Career** | |
| Tech industry & salaries | `references/tech.md` |
| Business setup & incorporation | `references/business.md` |
| Immigration (Express Entry, PNP, work permits) | `references/immigration.md` |
| Startups & funding | `references/startup.md` |
| **Lifestyle** | |
| Culture & customs | `references/culture.md` |
| Healthcare (MSP, clinics) | `references/healthcare.md` |
| Schools & education | `references/education.md` |
| Outdoor lifestyle & activities | `references/lifestyle.md` |
| Driving & car ownership | `references/driving.md` |

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur
- **Timeline**: Short visit, planning to move, already there
- Load relevant auxiliary file for details

### 2. Immigration-Centric Planning
Canada has complex but transparent immigration. Key pathways:
- **Express Entry**: Points-based skilled worker immigration
- **BC PNP**: Provincial nomination (tech pilot is fast-tracked)
- **Work permits**: LMIA-based or LMIA-exempt (IEC, intra-company)
- **Study permits**: Pathway to PR through PGWP
See `references/immigration.md` for current requirements and processing times.

### 3. Weather Reality
Vancouver has Canada's mildest climate but earns its "Raincouver" nickname:
- **Winter (Nov-Mar)**: 5-10°C, grey and rainy. ~170 rainy days/year.
- **Summer (Jun-Sep)**: 20-25°C, sunny and spectacular. Best months.
- **Microlimates**: North Shore wetter, Richmond drier.
See `references/climate.md` for monthly breakdown and survival strategies.

### 4. Housing Crisis Context
Vancouver has the least affordable housing in North America:
- **Average home price**: ~$1.2M CAD (condos ~$750K)
- **1BR rent Downtown**: $2,200-3,000/month
- **Vacancy rate**: ~1% — units go fast
- **Foreign buyer tax**: 20% for non-residents
See `references/cost.md` for current market data and strategies.

### 5. Current Data (Feb 2026)

| Item | Range |
|------|-------|
| 1BR rent (Downtown) | $2,200-3,000/month |
| 1BR rent (East Van) | $1,800-2,400/month |
| Senior SWE salary | $150,000-220,000 CAD/year |
| Monthly transit pass | $102.55-177.75 (zones) |
| Craft beer pint | $8-12 |
| Childcare (infant) | $1,500-2,200/month |

### 6. Cost Reality
Vancouver is expensive but wages are lower than US:
- **Housing**: 40-50% of budget common (crisis level)
- **Childcare**: Among Canada's highest until BC $10/day rollout completes
- **Healthcare**: Free basic coverage (MSP), dental/vision extra
- **Car ownership**: Optional if you live near SkyTrain
- **Hidden costs**: 12% PST+GST on goods, 15% tip expected

### 7. Transit Excellence (For Canada)
Vancouver has strong public transit by Canadian standards:
- **SkyTrain**: Automated metro, 3 lines, clean and frequent
- **Buses**: Extensive network, real-time tracking
- **SeaBus**: Ferry to North Vancouver (12 min)
- **Cycling**: Excellent infrastructure, bike-share available
Most Downtown/inner city residents rely fully on walking or transit. See `references/transport.md`.

### 8. Neighborhood Matching

| Profile | Best Areas |
|---------|------------|
| Young professionals | Yaletown, Mount Pleasant, Gastown |
| Families | North Vancouver, Burnaby, Coquitlam |
| Beach lifestyle | Kitsilano, English Bay, West End |
| Budget-conscious | East Van, New Westminster, Surrey |
| Tech workers | Downtown, Mount Pleasant, Burnaby (near Metrotown) |
| Students | UBC area, Commercial Drive, Burnaby near SFU |
| Outdoors focus | North Vancouver, Squamish (commutable) |

## Tech Industry Context

Vancouver is Canada's third-largest tech hub after Toronto and Montreal:
- **Major employers**: Amazon, Microsoft, Apple, EA, SAP, Slack, Hootsuite
- **Strengths**: Gaming, VFX/film, AI/ML, clean tech
- **US proximity**: Same timezone as Seattle/SF, easy cross-border work
- **BC Tech Pilot**: Expedited PR pathway for tech workers

Salaries are lower than Seattle/SF but:
- Healthcare included
- No state income tax (BC rates apply)
- Better work-life balance culture
- PR pathway for long-term stability

See `references/tech.md` for detailed industry analysis and salary bands.

## Vancouver-Specific Traps

- **Rain depression** — 6 months of grey skies is real. Get a SAD lamp and rainwear.
- **Housing speed** — Good units rent within hours. Have documents ready, apply immediately.
- **Reference requirements** — Landlords want employment letter, credit check, references. Prepare these.
- **Tipping culture** — 18-20% expected everywhere. Budget for it.
- **BC income tax** — Higher than other provinces. Alberta/Ontario may be cheaper net.
- **Car insurance (ICBC)** — Government monopoly, expensive. $2,000-4,000/year typical.
- **Strata restrictions** — Many condos restrict pets, rentals, or Airbnb. Check bylaws.
- **Summer accommodation** — July-August prices spike 2-3x. Book early or visit shoulder season.
- **US border assumptions** — Canadians need ESTA/visa; NEXUS card helps frequent crossers.
- **Ski traffic** — Sea-to-Sky Highway gridlocks winter weekends. Leave early or stay over.

## Legal/Practical Awareness

Key things newcomers should know:
- **Cannabis**: Legal (19+). Dispensaries everywhere. No public smoking near schools.
- **Alcohol**: BC Liquor Stores or licensed private stores only. No corner store beer.
- **Healthcare wait times**: Walk-in clinics have hours-long waits. Register with family doctor ASAP.
- **SIN requirement**: Apply immediately on arrival. Needed for work/banking.
- **Banking**: Big 5 banks (TD, RBC, BMO, Scotiabank, CIBC) plus credit unions.
- **Phone plans**: Expensive by global standards. $50-80/month for decent data.
- **Earthquake zone**: Vancouver is seismically active. Know emergency procedures.
- **Wildlife**: Bears in North Shore suburbs. Coyotes everywhere. Secure garbage.

See `references/safety.md` and `references/local.md` for detailed guidance.

## Related Skills

- `toronto` — Canada's largest city; different vibe with similar immigration pathways
- `seattle` — Closest major US city with comparable tech and outdoor culture
