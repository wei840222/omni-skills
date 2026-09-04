---
name: london
description: Plan London visits, moves, study, tech work, or startup decisions with neighborhood, transport, cost, safety, and local guidance. Use for London-specific choices; verify live fares, prices, availability, visas, and safety conditions before decisive advice.
metadata:
  openclaw: '{"emoji":"🇬🇧"}'
  related-skills: '{"travel":"Plans multi-destination trips beyond London-specific routing.","travel-planning":"Completes travel planning and reservations after a London choice is made.","uk":"Provides UK-wide context outside London-specific decisions."}'
---

This skill is stateless and does not store local configuration or persistent user state. Treat dated package figures as planning estimates, not live quotes. For fares, prices, availability, visa or immigration rules, venue access, or same-day safety decisions, read `references/current-information.md` and verify the authoritative source before giving decisive advice.

## When to Use

Use for London-specific travel, relocation, study, work, startup, neighborhood, transit, safety, food, or itinerary decisions. Establish the user's purpose, dates, budget, party, access needs, and commute when relevant. For multi-destination planning, use `travel`; for UK-wide context beyond London, use `uk`; for reservation completion, use `travel-planning` after the London choice is made.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Planning & sources** | | |
| Current information & official sources | `references/current-information.md` | Before a decisive fare, booking, immigration, payment, venue, or safety answer |
| Core planning rules | `references/core-rules.md` | When matching advice to role, timeline, safety, weather, transit, or neighborhood needs |
| Traps & misconceptions | `references/london-traps.md` | When discussing tourist traps, scams, or common misconceptions |
| **Visitors** | | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` | Attraction choice, access, or priority |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` | 1-, 3-, or 7-day itinerary |
| Where to stay | `references/visitor-lodging.md` | Hotel area or lodging choice |
| Tips & day trips | `references/visitor-tips.md` | Visitor logistics or day trip |
| **Neighborhoods** | | |
| Quick comparison | `references/neighborhoods-index.md` | Area overview |
| Central (Zone 1) | `references/neighborhoods-central.md` | Central London area choice |
| East London | `references/neighborhoods-east.md` | East London area choice |
| South London | `references/neighborhoods-south.md` | South London area choice |
| West London | `references/neighborhoods-west.md` | West London area choice |
| North London | `references/neighborhoods-north.md` | North London area choice |
| Choosing guide | `references/neighborhoods-choosing.md` | Area tradeoff or shortlist |
| **Food** | | |
| Overview & restaurants | `references/food-overview.md` | Dining recommendations |
| British classics | `references/food-traditional.md` | Traditional British food |
| Markets | `references/food-markets.md` | Food market |
| Best areas | `references/food-areas.md` | Cuisine or food district |
| Pubs | `references/food-pubs.md` | Pub culture or pub choice |
| Dietary & tips | `references/food-practical.md` | Dietary needs, booking, or tipping |
| **Practical** | | |
| Moving & settling | `references/resident.md` | Relocation or settling |
| Transport | `references/transport.md` | Transport, airport transfer, or fares |
| Cost of living | `references/cost.md` | Budget, rent, or living cost |
| Safety | `references/safety.md` | Safety or late-night route |
| Weather | `references/climate.md` | Weather or packing |
| Local services | `references/local.md` | NHS, banking, utilities, or council service |
| **Career** | | |
| Tech industry | `references/tech.md` | Tech job, employer, or work base |
| Students | `references/student.md` | Study, student housing, or student life |
| Startups | `references/startup.md` | Startup, founder, or company setup |

## Plan the Answer

1. Identify the user's role, timeline, budget, location, and any accessibility or late-night constraints.
2. Load the matching topical reference from the table above.
3. Load `references/core-rules.md` for cross-cutting planning guidance and `references/london-traps.md` for scam or tourist-trap questions.
4. Before an answer depends on a mutable fare, price, availability, visa rule, venue policy, or safety condition, load `references/current-information.md`, verify its listed official source, and distinguish verified facts from dated estimates.

## Practical Guardrails

- Base neighborhood and hotel advice on a real commute, transfer tolerance, and late-night return path—not a borough label alone.
- Treat neighborhood character, restaurant listings, fare tables, rent bands, salary bands, and public-service details as dated planning material until checked at the relevant official source.
- Use official operator, government, health, venue, and local-authority sources for unstable operational details. When verification is unavailable, provide the durable decision framework and state the freshness gap.
- Complete bookings, payments, immigration submissions, or other third-party actions only after explicit user instruction.
