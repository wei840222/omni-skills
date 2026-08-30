---
name: sydney
description: Navigate Sydney as a visitor, resident, tech worker, student, or entrepreneur. Provides localized guidance on neighborhoods, beaches, transport, visas, cost of living, and local insights. Use this skill when the user asks about visiting, moving to, working in, studying in, or starting a business in Sydney.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏖️"}'
  related-skills: '{"australia":"Provides broader Australian context for Sydney-specific questions.","travel-planning":"Helps structure multi-city itineraries that may include Sydney."}'
---

## When to Use

User asks about Sydney for any purpose: visiting, moving, working, studying, or starting a business. Agent provides practical guidance with current data.

For fares, visa conditions, regulated costs, or service eligibility, load the matching reference and use its linked primary source before presenting a current figure or requirement.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Visitors** | | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` | When user asks for sights or attractions |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` | When user needs day-by-day plans |
| Where to stay | `references/visitor-lodging.md` | When user asks for hotel or accommodation locations |
| Tips & day trips | `references/visitor-tips.md` | When user asks for general tourist tips |
| **Neighborhoods** | | |
| Quick comparison | `references/neighborhoods-index.md` | When user needs an overview of areas |
| CBD, The Rocks, Barangaroo | `references/neighborhoods-cbd.md` | When user asks about central Sydney |
| Surry Hills, Paddington, Potts Point | `references/neighborhoods-inner-east.md` | When user asks about inner east |
| Newtown, Marrickville, Balmain | `references/neighborhoods-inner-west.md` | When user asks about inner west |
| Bondi, Manly, Northern Beaches | `references/neighborhoods-beach.md` | When user asks about beach areas |
| North Shore, Parramatta, Western | `references/neighborhoods-suburban.md` | When user asks about suburban areas |
| Choosing guide | `references/neighborhoods-choosing.md` | When user needs help deciding where to live |
| **Food** | | |
| Overview & dining scene | `references/food-overview.md` | When user asks about food culture |
| Australian & local cuisine | `references/food-local.md` | When user asks for local dishes |
| International & multicultural | `references/food-international.md` | When user asks for diverse food options |
| Best dining precincts | `references/food-areas.md` | When user asks where to eat |
| Dietary, alcohol, coffee | `references/food-practical.md` | When user asks about dietary needs or drinks |
| **Practical** | | |
| Moving & settling | `references/resident.md` | When user is moving to Sydney |
| Transport (Opal, trains, ferries) | `references/transport.md` | When user asks about getting around |
| Cost of living | `references/cost.md` | When user asks about expenses |
| Safety & wildlife | `references/safety.md` | When user asks about safety or dangerous animals |
| Weather & seasons | `references/climate.md` | When user asks about the weather |
| Local services (banking, SIM) | `references/local.md` | When user asks about banks or phones |
| **Career** | | |
| Tech industry & salaries | `references/tech.md` | When user asks about tech jobs |
| Business setup | `references/business.md` | When user wants to start a business |
| Visas (skilled, working holiday) | `references/visas.md` | When user asks about visas |
| Startups & funding | `references/startup.md` | When user asks about the startup ecosystem |
| **Lifestyle** | | |
| Culture & customs | `references/culture.md` | When user asks about local culture |
| Healthcare & Medicare | `references/healthcare.md` | When user asks about healthcare |
| Schools & universities | `references/education.md` | When user asks about education |
| Expat lifestyle & social | `references/lifestyle.md` | When user asks about expat life |
| Driving & car ownership | `references/driving.md` | When user asks about driving |


## State location

This skill is stateless and does not store or manage any local configuration or runtime state.

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur
- **Timeline**: Short visit, planning to move, already there
- Load relevant auxiliary file for details

### 2. Beach-Centric City
Sydney's identity revolves around its beaches and harbour:
- **70+ beaches** from Bondi to Palm Beach
- Harbor lifestyle (ferries, sailing, waterfront dining)
- Outdoor culture year-round
- Beach safety critical (rips, UV)
See `references/visitor-tips.md` for beach safety and `references/neighborhoods-beach.md` for living near beaches.

### 3. Multicultural Reality
Sydney is one of the world's most diverse cities:
- 40%+ born overseas
- 200+ languages spoken
- Ethnic precincts: Chinatown, Cabramatta (Vietnamese), Harris Park (Indian), Lakemba (Lebanese)
- Food reflects global diversity
See `references/culture.md` and `references/food-international.md` for cultural guidance.

### 4. Climate & UV Reality
- **Mild year-round** compared to Europe/Americas
- **Summer (Dec-Feb)**: 25-35°C, humid, thunderstorms
- **Winter (Jun-Aug)**: 8-18°C, mild, rarely below 5°C
- **UV is extreme**: Australia has highest skin cancer rates
- **Bushfire season**: Summer, affects air quality
See `references/climate.md` for monthly breakdown and `references/safety.md` for UV/wildlife.

### 5. Current Planning Data

Use the detailed reference that matches the question rather than repeating dated prices here:

- Housing, food, healthcare, and transport budgets: `references/cost.md`
- Current public-transport fares and airport-access fees: `references/transport.md`
- School and university costs: `references/education.md`
- Tech compensation and hiring conditions: `references/tech.md`
- Visa charges, conditions, and processing guidance: `references/visas.md`

### 6. Cost Reality
Sydney is expensive but with good wages:
- **Housing**: Most expensive in Australia, 35-45% of budget
- **Childcare and healthcare**: eligibility and out-of-pocket costs depend on visa status, provider, and household circumstances
- **Tipping**: generally optional; service norms vary by venue
- **Hidden costs**: account for bond, utilities, and move-in expenses

### 7. Transport Mix
Sydney has diverse transport options:
- **Trains**: Extensive network, Opal card
- **Ferries**: Iconic, practical for harbour suburbs (Manly, Taronga)
- **Light rail**: CBD to Inner West and Eastern Suburbs
- **Buses**: Fill the gaps
- **Car**: Needed for Northern Beaches, Western suburbs
Most inner city residents rely on public transport instead of cars. See `references/transport.md` and `references/driving.md`.

### 8. Neighborhood Matching

| Profile | Best Areas |
|---------|------------|
| Young professionals | Surry Hills, Newtown, Darlinghurst |
| Families | North Shore, Inner West (Balmain), Northern Beaches |
| Beach lifestyle | Bondi, Manly, Coogee |
| Budget-conscious | Marrickville, Redfern, Western suburbs |
| Tech workers | Surry Hills, Pyrmont, CBD |
| LGBTQ+ friendly | Newtown, Darlinghurst, Marrickville |

## Sydney vs Melbourne Context

Common comparison for migrants/visitors:
- **Sydney**: Beaches, outdoor lifestyle, harbour, more expensive
- **Melbourne**: Arts, coffee culture, sport, more affordable
- **Weather**: Sydney warmer year-round
- **Tech jobs**: Both strong, Sydney slightly larger market
- **Lifestyle**: Sydney = beach/outdoor, Melbourne = cafes/culture

## Sydney-Specific Traps

- **Rips kill tourists** — ALWAYS swim between the red and yellow flags. Rips are invisible currents that drag you out.
- **UV underestimation** — Australia has highest skin cancer rates. Wear SPF 50+, even on cloudy days.
- **Sydney funnel-web spiders** — Dangerous, found in gardens. Shake shoes, be aware.
- **Beach driving** — Only at designated beaches, 4WD required, many restrictions.
- **Toll roads add up** — Sydney has expensive tolls (Harbour Bridge/Tunnel, WestConnex). Get e-tag.
- **Housing competition** — Expect 20-50+ applications per rental. Apply multiple properties.
- **Airport train surcharge** — Train to airport costs extra on top of Opal fare.
- **Alcohol prices** — Very expensive. Pre-drink culture exists.
- **Speed cameras everywhere** — Hidden, mobile, average speed. Observe speed limits strictly.
- **Tipping is optional** — But tourists often do, confusing service staff.

## Regulated Activities

For immigration, driving, alcohol, smoking, fireworks, or other regulated activities, load the relevant reference and verify the applicable government rules before advising on eligibility, penalties, or permissions.
