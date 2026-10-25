---
name: austin
description: "Provide practical Austin, Texas guidance for visitors, relocators, and tech workers. Use when researching Austin neighborhoods, housing costs, heat/allergy risks, transit, or local regulations; not for legal or tax advice."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🤠","requires":{"config":["<state_root>/austin/"]}}'
---

Persistent Austin context lives under `<state_root>/austin/` (see State location). One-off visitor questions stay stateless.

## When to Use

User needs Austin-specific guidance that generic U.S. or even generic Texas advice usually misses: visiting vs relocating, neighborhood fit, housing cost shock, car-centric transit, extreme summer heat and cedar fever, BBQ/music culture, tech salaries, Texas LLC basics, or work-visa context tied to Austin employers.

## State location

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/austin/`, `<workspace>/memory/austin/`, `~/austin/`.
3. If multiple candidates exist, keep the highest-priority one, leave others independent, and tell the user which location was selected.
4. If none exists and state must be created, default to `<workspace>/austin/` and create `memory.md` on first need.

Use the selected `<state_root>` for every state path in this skill. Skill resources stay under `references/`; never treat the literal string `<state_root>` as a filesystem path.

```text
<state_root>/austin/
└── memory.md     # User context, timeline, budget, neighborhoods, open loops
```

- Preferred path: `<state_root>/austin/`.
- If the directory does not exist and the user wants continuity, read `references/setup.md`, explain the planned local storage in plain language, and ask for confirmation before creating files. Use `references/memory-template.md` for structure.
- Before creating or changing local files under `<state_root>/austin/`, explain the planned write and ask for confirmation.

## Setup

On first persistent-memory use, read `references/setup.md`. Answer the user's question first; configuration is optional and organic.

## When to Load References

| Topic | When to load | File |
|-------|--------------|------|
| Setup guide | First persistent-memory use | `references/setup.md` |
| Memory template | Creating or updating user context | `references/memory-template.md` |
| Sources | Unstable cost, legal, transit, or employer claims | `references/sources.md` |
| Attractions | Must-see vs skip lists | `references/visitor-attractions.md` |
| Itineraries | 1 / 3 / 7 day plans | `references/visitor-itineraries.md` |
| Lodging | Where to stay | `references/visitor-lodging.md` |
| Visitor tips | Day trips, food strategy, common mistakes | `references/visitor-tips.md` |
| Neighborhood index | Quick area comparison | `references/neighborhoods-index.md` |
| Central Austin | Downtown, East Side, South Congress | `references/neighborhoods-central.md` |
| North Austin | Domain, Arboretum, Cedar Park | `references/neighborhoods-north.md` |
| South Austin | Zilker, Barton Hills, Bouldin | `references/neighborhoods-south.md` |
| East & Southeast | Mueller, Manor, Del Valle | `references/neighborhoods-east.md` |
| West & Hill Country | Westlake, Lakeway, Bee Cave | `references/neighborhoods-west.md` |
| Choosing guide | Matching lifestyle to area | `references/neighborhoods-choosing.md` |
| Food overview | Dining scene orientation | `references/food-overview.md` |
| BBQ | Brisket lines, alternatives, order strategy | `references/food-bbq.md` |
| Tex-Mex | Breakfast tacos and Mexican | `references/food-mexican.md` |
| Food trucks | Trailer parks and late options | `references/food-trucks.md` |
| International / fine dining | Non-Tex-Mex destinations | `references/food-international.md` |
| Food areas | Best corridors for dining | `references/food-areas.md` |
| Food practical | Hours, tipping, dietary | `references/food-practical.md` |
| Live music | Everyday venue scene | `references/music-live.md` |
| SXSW | Mid-March festival chaos | `references/music-sxsw.md` |
| Festivals | ACL and major events | `references/music-festivals.md` |
| Venues by genre | Targeted show hunting | `references/music-venues.md` |
| Moving & settling | Resident admin sequence | `references/resident.md` |
| Transport | Car vs CapMetro / MetroRail / rideshare | `references/transport.md` |
| Cost of living | Rent, homes, tax offset | `references/cost.md` |
| Safety & laws | Marijuana, open carry, tenant norms | `references/safety.md` |
| Climate | Heat, ice, cedar fever | `references/climate.md` |
| Local services | Utilities, DMV, taxes | `references/local.md` |
| Tech industry | Employers and salary bands | `references/tech.md` |
| Business / LLC | Texas entity basics | `references/business.md` |
| Visas | Sponsorship reality checks | `references/visas.md` |
| Startups | VC and founder scene | `references/startup.md` |
| Culture | Local norms and communication | `references/culture.md` |
| Healthcare | Access and insurance shape | `references/healthcare.md` |
| Education | Schools and UT Austin | `references/education.md` |
| Outdoors | Trails, water, heat-safe plans | `references/outdoors.md` |
| Driving | Ownership and inspection | `references/driving.md` |

## Core Operating Loop

1. **Identify context first** — tourist, relocator, tech worker, remote worker, entrepreneur, student; short visit vs move vs already local.
2. **Answer immediately** — load only the references needed for the ask; do not force a setup ritual.
3. **Surface Austin-specific traps early** — heat, housing competition, I-35, Franklin lines, SXSW pricing, cedar fever, property-tax shock.
4. **Separate stable culture from unstable numbers** — cite `references/sources.md` and prefer official portals when cost, law, transit, or employer facts may have moved.
5. **Stay inside scope** — this skill advises; it does not file taxes, practice law, sponsor visas, or provide clinical care.

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, relocator, tech worker, remote worker, entrepreneur, student
- **Timeline**: Short visit, planning to move, already there, comparing Austin vs other cities
- Load the matching auxiliary file for depth

### 2. The Tech Migration Hub
Austin became a major U.S. tech destination. Key factors agents should keep in view:
- **No state income tax**: Draw for high earners (often framed as CA savings of roughly 10–13%)
- **Major HQs / large campuses**: Tesla, Oracle, Charles Schwab, Dell; Apple, Google, Meta, Amazon presence
- **Startup ecosystem**: Large regional VC presence; not Bay Area scale
- **Remote-work friendly**: Many CA/NYC companies keep Austin offices
See `references/tech.md` and `references/visas.md`.

### 3. Cultural Context
Austin is Texas's liberal island but still fundamentally Texan:
- **Keep Austin Weird**: Local support for indie businesses
- **Music identity**: "Live Music Capital of the World" is taken seriously
- **Tex-Mex is daily culture**: Breakfast tacos are a ritual
- **Outdoor culture**: Running, biking, kayaking are defaults when heat allows
- **Casual dress**: Tech casual everywhere; full suits are rare
See `references/culture.md`.

### 4. Weather Reality
- **Subtropical climate**: Mild winters, brutally hot summers
- **Best seasons**: Spring (Mar–May) and Fall (Oct–Nov) — roughly 20–28C
- **Summer (Jun–Sep)**: Extreme heat (often 38–42C); shift outdoors to morning/evening
- **Winter (Dec–Feb)**: Mild (5–18C) with occasional ice storms
- **Allergy capital framing**: Cedar fever (Dec–Feb), oak (Mar–Apr) hit newcomers hard
See `references/climate.md`.

### 5. Current Data Snapshot (verify before high-stakes use)

| Item | Indicative range | Notes |
|------|------------------|-------|
| 1BR rent (central) | $1,800–2,500/month | Confirm with current listings |
| 1BR rent (suburbs) | $1,300–1,800/month | Suburbs vary widely |
| Median home price | $550,000+ | Market moves; re-check sources |
| Senior SWE salary | $180,000–280,000/year | Total comp varies by employer |
| Junior SWE salary | $90,000–130,000/year | Band, not offer |
| Gas price | $2.80–3.20/gallon | Local pump variance |
| BBQ plate | $18–28 | Line time is the real cost at famous spots |
| Breakfast taco | $3–5 | Everyday baseline |
| Rideshare to airport | $25–40 | Surge during events |

Treat the table as orientation, not a live feed. Prefer `references/sources.md` + current portals for decisions.

### 6. Cost Reality
Austin is no longer "cheap college town":
- **Housing**: Multi-year price jump; competition still common in desirable areas
- **No income tax**: Offset by high property taxes (~2.1% of assessed value is a useful planning heuristic)
- **Food & entertainment**: Reasonable for a tech hub
- **Car required**: Transit exists; a car is near-essential for most lifestyles
- **Healthcare**: Private insurance required; costs vary widely
- **Savings vs CA**: Often still real, but the gap narrowed

### 7. Transit Reality
Austin is car-centric compared with coastal transit cities:
- **Car**: Near-essential for most lifestyles
- **CapMetro buses**: Exist with limited coverage
- **MetroRail**: One primary commuter-oriented line, limited hours
- **Rideshare**: Uber/Lyft widely available
- **Biking**: Stronger in central corridors
- **E-scooters**: Common downtown for short hops
- **I-35 traffic**: Plan around it; short distances can become long waits
See `references/transport.md`.

### 8. Neighborhood Matching

| Profile | Best starting areas |
|---------|---------------------|
| Young tech workers | East Austin, Downtown, South Lamar |
| Families | Circle C, Steiner Ranch, Cedar Park |
| Remote workers | South Congress, Zilker, Mueller |
| Budget-conscious | Round Rock, Pflugerville, Manor |
| Luxury seekers | Westlake, Tarrytown, Lake Austin |
| Music lovers | East 6th, Red River, South Congress |
| Outdoor enthusiasts | Barton Hills, Zilker, Bee Cave |
| Students / young professionals | West Campus, North Loop, Hyde Park |

## The Austin Transformation

- **Pre-2010**: Affordable college town with a strong music scene
- **2010–2015**: Tech presence grows; "Silicon Hills" sticks
- **2015–2020**: COTA / F1 era; growth accelerates
- **2020–2021**: Pandemic migration; Tesla and Oracle HQ moves amplify attention
- **2021–2023**: Housing pressure and traffic pain; "old Austin" mourning becomes common talk
- **2023–present**: Growth cooling in places, affordability still strained, infrastructure catching up

The city a visitor meets today is not the Austin of five years earlier.

## Austin-Specific Traps

- **Summer underestimation** — 40C+ heat is a safety issue. Prefer indoor or water plans Jun–Sep.
- **Franklin BBQ line** — 3–4 hour waits are normal. Arrive near 8am, order ahead when available, or choose strong alternatives.
- **SXSW chaos** — Avoid downtown mid-March unless attending. Hotels spike.
- **Cedar fever** — Not "just a cold." Dec–Feb allergies can floor newcomers.
- **"Central Austin" rent labels** — Marketing often stretches "central."
- **I-35 commute** — 10 miles can become 45+ minutes at rush hour.
- **No-zoning myths** — Austin has zoning; it is just different from CA/NY expectations.
- **"Austin's changed" locals** — The complaint is often accurate; stay humble.
- **Property tax shock** — Plan ~2.1% of assessed value annually as a starting heuristic.
- **Water restrictions** — Summer drought rules are real.

## Legal Awareness

Informational only — not legal advice:
- **Marijuana**: Still illegal under Texas law; real enforcement happens.
- **Open carry**: Handgun open carry rules exist for eligible adults; confirm current statute before advising action.
- **Alcohol**: Bars generally close at 2am; public drinking restricted; some Sunday quirks remain.
- **Employment**: At-will baseline; non-competes can matter but are not unlimited.
- **Tenant rights**: Comparatively landlord-friendly; lease text usually controls.
- **Vehicle inspection**: Annual inspection plus registration.
- **No state income tax**: Property and sales taxes still bite.

See `references/safety.md`. For statewide process detail, chain `texas`.

## The Housing Reality (2026)

- **Price explosion**: Median home narrative from ~$300K (2019-era talk) to $550K+ planning band
- **Competition**: Multiple offers, cash buyers, waived contingencies still appear in hot pockets
- **Rent pressure**: Desirable corridors saw large multi-year jumps
- **California factor**: Remote CA salaries can outbid local incomes
- **Local sentiment**: Newcomer resentment is part of the social context
- **As a newcomer**: Lead with curiosity, not "I just left California" flex

Re-check live listing and appraisal sources before money moves.

## Language & Communication

- **English dominant**
- **Spanish useful**: Large Hispanic community; appreciated in many contexts
- **Texas phrases**: "Y'all" is normal; "bless your heart" is not always kind
- **Direct + friendly**: Small talk with strangers is common

## Hard Boundaries

- Do **not** invent live listing prices, visa approvals, medical diagnoses, or court outcomes.
- Do **not** hard-code `~/.austin/`, Clawic paths, or machine-specific homes in instructions.
- Do **not** treat this skill as a lawyer, CPA, immigration attorney, or clinician.
- Prefer official Texas / City of Austin / CapMetro / employer primary sources when stakes are high (`references/sources.md`).
- If the user needs statewide Texas logistics outside Austin color, hand off to `texas`.
