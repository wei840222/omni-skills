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
| Attractions (must-see vs skip) | `references/visitor-attractions.md` | User asks about attractions (must-see vs skip) |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` | User asks about itineraries (1/3/7 days) |
| Where to stay | `references/visitor-lodging.md` | User asks about where to stay |
| Tips & day trips | `references/visitor-tips.md` | User asks about tips & day trips |
| **Neighborhoods** | | |
| Quick comparison | `references/neighborhoods-index.md` | User asks about quick comparison |
| Central (Zone 1) | `references/neighborhoods-central.md` | User asks about central (zone 1) |
| East London | `references/neighborhoods-east.md` | User asks about east london |
| South London | `references/neighborhoods-south.md` | User asks about south london |
| West London | `references/neighborhoods-west.md` | User asks about west london |
| North London | `references/neighborhoods-north.md` | User asks about north london |
| Choosing guide | `references/neighborhoods-choosing.md` | User asks about choosing guide |
| **Food** | | |
| Overview & restaurants | `references/food-overview.md` | User asks about overview & restaurants |
| British classics | `references/food-traditional.md` | User asks about british classics |
| Markets | `references/food-markets.md` | User asks about markets |
| Best areas | `references/food-areas.md` | User asks about best areas |
| Pubs | `references/food-pubs.md` | User asks about pubs |
| Dietary & tips | `references/food-practical.md` | User asks about dietary & tips |
| **Practical** | | |
| Moving & settling | `references/resident.md` | User asks about moving & settling |
| Transport | `references/transport.md` | User asks about transport |
| Cost of living | `references/cost.md` | User asks about cost of living |
| Safety | `references/safety.md` | User asks about safety |
| Weather | `references/climate.md` | User asks about weather |
| Local services | `references/local.md` | User asks about local services |
| **Career** | | |
| Tech industry | `references/tech.md` | User asks about tech industry |
| Students | `references/student.md` | User asks about students |
| Startups | `references/startup.md` | User asks about startups |

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
