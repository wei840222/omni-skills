---
name: milan
description: >
  Guide visitors, residents, students, and professionals through Milan neighborhoods,
  transport (metro/tram/ZTL/Area C), costs, visas and permits, food areas, tech salaries,
  startups, healthcare, and lodging. Use when the user asks about Milan travel, relocation,
  living costs, Duomo/Last Supper planning, Ferragosto closures, or working in Italy's
  business hub. Not for generic Italy itineraries without Milan focus (`travel`), pure
  Italian language practice (`italian`), or non-Milan expat admin (`expat`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇮🇹"}'
  related-skills: '{"travel":"Broader multi-city trip logistics when Milan is only one stop.","expat":"General relocation mindset and admin priorities outside Milan-specific districts.","food":"Personalized restaurant research when city context is already set.","italian":"Language help for bureaucracy and daily phrases.","business":"Company operations beyond Milan company-setup notes."}'
---

This skill is stateless and does not store local configuration or persistent user state. Keep itineraries, rental notes, visa checklists, and personal documents in ordinary user files outside the skill package.

## When to Use

User asks about Milan for any purpose: visiting, moving, studying, working, or launching a company. Agent gives practical, current, neighborhood-level guidance.

## Quick Reference

| Topic | File |
|-------|------|
| **Visitors** | |
| Attractions and what to skip | `references/visitor-attractions.md` |
| Itineraries (1, 3, 7 days) | `references/visitor-itineraries.md` |
| Where to stay | `references/visitor-lodging.md` |
| Practical tips and day trips | `references/visitor-tips.md` |
| **Neighborhoods** | |
| Quick comparison | `references/neighborhoods-index.md` |
| Historic and central zones | `references/neighborhoods-central.md` |
| Trendy and social zones | `references/neighborhoods-trendy.md` |
| Business and modern districts | `references/neighborhoods-business.md` |
| Family and value districts | `references/neighborhoods-suburban.md` |
| Choosing framework | `references/neighborhoods-choosing.md` |
| **Food** | |
| Dining scene overview | `references/food-overview.md` |
| Milan and Lombardy classics | `references/food-local.md` |
| International and fine dining | `references/food-international.md` |
| Best areas for food | `references/food-areas.md` |
| Dietary, timing, booking rules | `references/food-practical.md` |
| **Practical** | |
| Moving and settling | `references/resident.md` |
| Metro, trams, trains, airports | `references/transport.md` |
| Cost of living | `references/cost.md` |
| Safety and legal basics | `references/safety.md` |
| Weather and seasons | `references/climate.md` |
| SIM, banking, local apps | `references/local.md` |
| **Career and Business** | |
| Tech market and salaries | `references/tech.md` |
| Company setup and taxes | `references/business.md` |
| Visas and permits | `references/visas.md` |
| Startup ecosystem | `references/startup.md` |
| **Lifestyle** | |
| Culture and social norms | `references/culture.md` |
| Healthcare and insurance | `references/healthcare.md` |
| Schools and universities | `references/education.md` |
| Day to day life and social scene | `references/lifestyle.md` |
| Driving and ZTL rules | `references/driving.md` |

## Load Order

1. Classify the user (visitor / resident / student / worker / founder).
2. Open the matching Quick Reference row before drafting advice.
3. Cross-check traps (Area C, Ferragosto, ticket validation) when plans involve driving, August travel, or transit fines.
4. For legal status or company setup, prefer the official sources listed in the loaded reference file over memory.

## Core Rules

### 1. Identify User Profile First
- Role: tourist, resident, student, employee, founder, family.
- Time horizon: weekend trip, relocation plan, already in Milan.
- Load the matching file before giving recommendations.

### 2. Milan Is Neighborhood-Driven
The city changes block by block. Price, safety, noise, and lifestyle vary heavily by district. Always require district context before answering housing or nightlife questions.

### 3. Public Transport Works, Cars Are Constrained
Metro, tram, and rail are strong for daily movement. Central driving is limited by ZTL and Area C rules. For most newcomers, public transport plus walking is faster and cheaper.

### 4. Budget Reality
Load `references/cost.md` for current typical ranges on rent, transport passes, and dining costs.

### 5. Timing Culture Matters
- Lunch and dinner times are later than in many US cities.
- Monday can be closure day for museums and some restaurants.
- August has reduced activity due to Ferragosto holidays.
Use seasonal and weekly timing before planning.

### 6. Bureaucracy Requires Lead Time
Residence registration, tax code, rental contracts, and permits take planning. Always give a sequence, not just a checklist.

### 7. Tourism Peaks Affect Everything
Design Week, Fashion Week, and major football matches move prices quickly. Mention event calendars when user asks about lodging, dining, or transport.

### 8. Compare Milan Inside Italy
Milan is faster, more expensive, and more international than most Italian cities. For users comparing Rome, Venice, or Florence, highlight concrete trade-offs.

## Milan-Specific Recovery Checks

Before finalizing advice, load `references/safety.md` and `references/visitor-tips.md` and confirm:
- Area C / ZTL plans use the correct permit or choose metro/tram instead of assuming normal parking.
- August (Ferragosto) itineraries re-check venue hours and booking lead times.
- Transit plans include ticket validation and a strike/service-notice check.
- Housing picks near Navigli/Isola nightlife include noise expectations up front.

## Legal Awareness

- Ticket validation is mandatory on public transport; fines are common for mistakes.
- Driving in restricted traffic zones without permit leads to automatic penalties.
- Short-term rental rules and tourist taxes differ by property type and municipality requirements.
- Carry valid ID and residence documents if staying long term.
- Work and study status must match visa or permit conditions.

See `references/safety.md` and `references/visas.md` for details.
