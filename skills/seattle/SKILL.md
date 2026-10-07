---
name: seattle
description: >
  Navigate Seattle for visiting, moving, studying, or working in tech. Use when
  the user asks about Seattle neighborhoods, housing costs, weather myths, food,
  Amazon/Microsoft/Eastside commuting, light rail, or Pacific Northwest travel
  itineraries. Prefer `travel` for multi-city trip logistics, `dubai` for another
  city-guide pattern, and `negotiate` for offer/comp discussions beyond local
  salary ranges.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌲"}'
  related-skills: '{"dubai":"Parallel city-guide pattern for another metro with progressive neighborhood/food routing.","negotiate":"Salary and offer negotiation once Seattle/tech comp ranges are framed.","travel":"Multi-stop trip planning and logistics beyond a single Seattle stay."}'
---

This skill is stateless and does not store local configuration or persistent user state. Keep moving checklists, lease notes, and personal budgets in ordinary user files outside the skill package.

# Seattle

Practical guidance for visiting, moving to, studying in, or working in the Seattle metro (Seattle proper + Eastside). Load references only for the user's role and timeline.

## When to load

- Neighborhood and housing fit (Capitol Hill, SLU, Ballard, Eastside, South Seattle)
- Weather myths vs grey-day reality; packing for visits
- Cost of living, WA tax posture, or transit vs car trade-offs
- Tech hub orientation (Amazon SLU, Microsoft Redmond, other Eastside campuses)
- Short visit itineraries, food, outdoor day trips

Prefer `travel` when the trip spans multiple cities, `negotiate` when the user is bargaining an offer, and other city skills (for example `dubai`) when the request is not about Seattle.

## Quick workflow

1. **Identify context** — tourist, mover, tech worker (Amazon vs Microsoft/Eastside), student, remote, outdoor-focused; timeline short visit vs relocating.
2. **Load one reference lane** — visitor / neighborhoods / food / practical / career from the table below; do not dump every file.
3. **Correct myths early** — rain volume vs grey/SAD; Seattle proper vs Eastside commute pain; Pike Place morning vs noon crowds.
4. **Ground money claims** — treat rents, home prices, and total-comp bands as ranges that drift; prefer `references/cost.md` / `references/tech.md` and `references/sources.md` over inventing a single number.
5. **Match neighborhood to job side of the lake** — Amazon-heavy Seattle proper vs Microsoft/Eastside; flag 520/I-90 bridge traffic.
6. **Verify sticky facts** — tax posture, Link fares, UW tuition bands against URLs in `references/sources.md` when advising decisions.

## Progressive disclosure

| Topic | File |
|-------|------|
| **Visitors** | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` |
| Where to stay | `references/visitor-lodging.md` |
| Tips and day trips | `references/visitor-tips.md` |
| **Neighborhoods** | |
| Quick comparison | `references/neighborhoods-index.md` |
| Downtown and Belltown | `references/neighborhoods-downtown.md` |
| Capitol Hill and Central District | `references/neighborhoods-central.md` |
| Queen Anne and Magnolia | `references/neighborhoods-queen-anne.md` |
| Ballard, Fremont, Wallingford | `references/neighborhoods-north.md` |
| Eastside (Bellevue, Kirkland, Redmond) | `references/neighborhoods-eastside.md` |
| South Seattle | `references/neighborhoods-south.md` |
| **Food** | |
| Overview and dining scene | `references/food-overview.md` |
| Local specialties (seafood, coffee) | `references/food-local.md` |
| International cuisine | `references/food-international.md` |
| Best areas for dining | `references/food-areas.md` |
| Practical (apps, grocery, dietary) | `references/food-practical.md` |
| **Practical** | |
| Moving and settling | `references/resident.md` |
| Transport (car vs transit reality) | `references/transport.md` |
| Cost of living | `references/cost.md` |
| Safety | `references/safety.md` |
| Weather (myth vs reality) | `references/climate.md` |
| Local services | `references/local.md` |
| **Career** | |
| Tech industry and salaries | `references/tech.md` |
| Startups and funding | `references/startup.md` |
| Students | `references/student.md` |
| Remote workers | `references/remote.md` |
| **Sources** | |
| Gate 6 verified URLs | `references/sources.md` |

## Core orientation (keep short)

### Weather reality
Seattle's rain reputation is about **frequency of grey drizzle**, not tropical downpours. Annual liquid totals are often lower than many East Coast/Southeast cities; **overcast days and seasonal affective strain** are the harder part. Locals favor waterproof layers over constant umbrellas. Jul–Sep is typically the dry, outdoor season—book hikes and ferries early.

### Tax posture
Washington **does not currently have an individual state income tax** (WA DOR). Trade-offs show up in retail sales tax and other local costs—do not claim a single citywide sales-tax percent without checking current local rates.

### Lake split
- **Amazon / Seattle proper**: Capitol Hill, SLU, Ballard, and nearby walkable neighborhoods dominate young-tech social maps.
- **Microsoft / many Eastside campuses**: Bellevue, Kirkland, Redmond; living cross-lake without a plan means brutal 520/I-90 time.
- Treat "Seattle" vs "Eastside" as different daily lives, not synonyms.

### Transit snapshot
Link light rail is expanding and is useful for airport and north–south spines; Sound Transit publishes adult Link one-way fares (commonly **$3** adult one-way on Link—confirm passes on the official fares page). Cars remain common for suburbs, Eastside laterals, and outdoor trips. See `references/transport.md`.

### Neighborhood matching (starter)

| Profile | First places to compare |
|---------|-------------------------|
| Young tech (Amazon) | Capitol Hill, South Lake Union, Ballard |
| Young tech (Microsoft/Eastside) | Bellevue, Kirkland, Redmond |
| Families | Eastside, West Seattle, North Seattle |
| Nightlife and culture | Capitol Hill |
| Hip / artsy | Fremont, Ballard |
| Quiet / nature-leaning | Magnolia, Queen Anne |
| Budget-conscious entry | South Seattle, Beacon Hill (verify block-level fit) |

### Money ranges are directional
Use `references/cost.md` and `references/tech.md` for rent/comp bands. In chat, label figures as approximate and time-sensitive (Zillow/home-value indexes and job offers move). Example orientation only: walkable Capitol Hill 1BR often prices above Eastside suburban stock in different ways; senior SWE total comp at large tech is wide and offer-specific.

## Seattle-specific traps

- **"It rains all the time"** — grey/drizzle frequency ≠ constant heavy rain; pack layers.
- **Underestimating the grey** — budget light strategy Oct–Mar if sensitive to low sun.
- **Seattle = Eastside** — bridge traffic and job-side housing matter more than city-brand prestige.
- **Pike Place at noon first** — go early (about 9am) before peak tourist density.
- **Ignoring Bellevue** — Eastside dining and job gravity are real.
- **Summer FOMO** — Jul–Sep outdoor demand spikes; book ahead.
- **Seattle Freeze** — social circles can feel slow to open; plan repeated low-pressure hangs.
- **Car break-ins / package theft** — common enough to warrant empty-car and delivery hygiene (`references/safety.md`).

## Outdoor context

Within roughly 1–3 hours: Mt. Rainier, Olympics, San Juans (ferry), Snoqualmie Falls, Crystal Mountain, North Cascades. REI flagship culture is a lifestyle signal—gear and day-trip planning are first-class topics (`references/visitor-tips.md`).

## Coffee culture

Starbucks origin story is tourist lore; locals often point to third-wave and classic Seattle roasters (Victrola, Elm, Slate, Milstead, Caffe Vita, Espresso Vivace, and many independents). Order plainly; craft expectations are normal.

## Safety boundaries

- Do not invent live rent medians, tax percents, Link pass prices, or UW tuition from memory when the user is making a move/budget decision—open `references/sources.md` and the matching reference file.
- Do not store leases, SSNs, employer offer letters, or travel document scans in the skill package.
- Do not present neighborhood safety as universal; block-level conditions change—pair guidance with official/local reporting habits in `references/safety.md`.

## Non-goals

- Not a full multi-city itinerary engine (`travel`) or generic comp negotiation coach (`negotiate`).
- Not a complete restaurant database; keep discovery in food references and current local sources.
- Do not duplicate long neighborhood essays in `SKILL.md`; route to `references/neighborhoods-index.md` and the neighborhood detail files.
