---
name: barcelona
description: Provide practical Barcelona guidance for visitors, relocators, tech workers, students, and founders—neighborhoods, transport, costs, safety, Catalan/Spanish context, food, and lifestyle. Use when the user asks about Barcelona-specific decisions; verify live fares, rents, tickets, and safety conditions before decisive advice. Not a substitute for Spain-wide multi-city routing (`spain`/`travel`), Catalan-language writing (`catalan`), or Madrid-only depth (`madrid`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏖️","requires":{"config":["<state_root>/barcelona/"]}}'
  related-skills: '{"spain":"Spain-wide destinations, regional routing, and multi-city itineraries beyond Barcelona-only depth.","travel":"General multi-destination trip systems and travel memory.","catalan":"Natural Catalan writing and register rather than Barcelona logistics.","madrid":"Compare or switch to Madrid-specific neighborhood, cost, and lifestyle depth.","europe":"Cross-border EU mobility context beyond Barcelona.","booking":"Lodging and reservation execution after a Barcelona base is chosen.","career":"Broader career decisions after Barcelona tech or job context is set.","startup":"Founder workflows after Barcelona startup landscape is scoped.","food":"Deeper food-system workflows beyond Catalan dining guidance."}'
---

## State location

Persistent Barcelona context lives under `<state_root>/barcelona/` (see `references/memory-template.md`). One-off visitor questions can stay effectively stateless.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/barcelona/`, `<workspace>/memory/barcelona/`, `~/barcelona/`.
3. If none exists and state must be created, default to `<workspace>/barcelona/`.

Use the selected `<state_root>` for every state operation in this skill.

```text
<state_root>/barcelona/
└── memory.md     # User context and preferences
```

On first use with durable context, read `references/setup.md` for optional workspace integration. Answer the user's question first; setup is never blocking.

## When to Use

User asks about Barcelona for visiting, relocating, working remotely, studying, or starting a business. Establish role, timeline, budget, party, language level, and neighborhood constraints first, then load only the needed reference files. For multi-city Spain trips prefer `spain`/`travel`; for Catalan-language drafting prefer `catalan`; for Madrid-only depth prefer `madrid`.

Treat dated package figures as planning estimates. Before booking, immigration, payment, or same-day safety decisions, open the matching reference and verify the official source in `references/sources.md`.

## Auxiliary knowledge (Progressive Disclosure)

Only load these files when the user explicitly requests topics requiring them. When they do, load the file using the paths below.

| Topic | File |
|-------|------|
| **Visitors** | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` |
| Where to stay | `references/visitor-lodging.md` |
| Tips & day trips | `references/visitor-tips.md` |
| **Neighborhoods** | |
| Quick comparison | `references/neighborhoods-index.md` |
| Central (Gòtic, Raval, Born) | `references/neighborhoods-central.md` |
| Uptown (Eixample, Gràcia) | `references/neighborhoods-uptown.md` |
| Beach (Barceloneta, Poblenou) | `references/neighborhoods-beach.md` |
| Outer (Sant Andreu, Horta) | `references/neighborhoods-outer.md` |
| Choosing guide | `references/neighborhoods-choosing.md` |
| **Food** | |
| Overview & restaurants | `references/food-overview.md` |
| Traditional Catalan | `references/food-traditional.md` |
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
| **Sources** | |
| Official portals & verification | `references/sources.md` |

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur
- **Timeline**: Short visit, planning to move, already there
- Load relevant auxiliary file for details

### 2. Safety Context
Barcelona is generally safe for a major European city but has a high pickpocketing rate for tourists. Main concerns:
- Pickpocketing (Las Ramblas, metro, beaches, Barri Gòtic)
- Phone snatching (tourists with phones visible)
- Apartment scams (online rentals)
- Beach theft (leaving belongings unattended)
See `references/safety.md` for area-specific guidance. Verify current safety notices via `references/sources.md` before same-day advice.

### 3. Weather Expectations
- Mediterranean climate — mild winters, hot summers
- Summer: Hot (28-32°C) with humidity
- Winter: Mild (10-15°C), rarely below 5°C
- Best months: May-June, September-October
- Beach season: June-September (water warm enough)
See `references/climate.md` for monthly detail.

### 4. Current Data (Feb 2026)

| Item | Range |
|------|-------|
| 1BR rent | €1,200-1,800 (central), €900-1,400 (outer) |
| Senior SWE salary | €50K-80K total comp |
| Student budget | €1,000-1,400/month |
| T-usual (monthly pass) | €22.80 (Zone 1) |

Treat these as planning estimates only; re-check TMB/ATM and housing listings before booking or budgeting decisions.

### 5. Tourist-Trap Avoidance
- Prefer side-street dining over Las Ramblas restaurant rows and Barceloneta beachfront tourist menus
- Favor El Born, Gràcia's Plaça del Sol, and Poblenou for more local texture
- Keep belongings secured throughout Ciutat Vella
- Free or low-cost high-value options: Park Güell free zone, beaches, Bunkers del Carmel sunset
- Book Sagrada Família timed entry online to avoid multi-hour queues

### 6. Transit Over Driving
- Metro + bus + FGC covers most trips
- T-Casual (10 trips) for visitors; T-usual for residents
- Bicing for eligible residents
- ZBE (Low Emission Zone) makes casual driving complicated
See `references/transport.md`.

### 7. Neighborhood Matching

| Profile | Best Areas |
|---------|------------|
| Young professionals | Gràcia, Poblenou, Sant Antoni |
| Families | Sarrià, Les Corts, Horta |
| Budget-conscious | Sant Andreu, Nou Barris, Sants |
| Tech workers | Poblenou (22@), Eixample, Gràcia |
| Beach lifestyle | Barceloneta, Poblenou, Vila Olímpica |

## Language Context

### Catalan vs Spanish (Castellano)

Barcelona is bilingual. Understanding this is essential:

| Situation | Language Used |
|-----------|---------------|
| Street signs | Catalan |
| Official documents | Catalan (with Spanish option) |
| Daily conversation | Both (depends on person) |
| Service industry | Spanish common, Catalan appreciated |
| Schools | Catalan primary |
| Business | Both, leaning Spanish in multinationals |

**Practical advice:**
- Speaking Spanish is fine — most locals are bilingual
- Learning basic Catalan phrases is appreciated and shows respect
- Locals will often switch to Spanish if you're struggling
- Keep an open mind about political opinions based on language preference
- Catalonia has strong regional identity — be aware but neutral
- For drafting Catalan text itself, hand off to `catalan`

### Basic Catalan Phrases

| Catalan | Spanish | English |
|---------|---------|---------|
| Bon dia | Buenos días | Good morning |
| Gràcies | Gracias | Thank you |
| Si us plau | Por favor | Please |
| Adéu | Adiós | Goodbye |
| Quant costa? | ¿Cuánto cuesta? | How much? |

## Barcelona-Specific Traps

- **Las Ramblas dining** — Tourist-priced menus; walk into side streets instead.
- **Barceloneta beachfront** — Often overpriced for the quality; walk toward Poblenou for better value.
- **"Free" walking tours** — Expect tip pressure around €15-20; decide tip intentionally.
- **Sagrada Família without booking** — 2+ hour queues are common; book online.
- **Airport taxi** — Expect roughly €40-45 on meter; confirm meter use.
- **Pickpockets** — High tourist targeting; keep phones and bags secured.
- **Fake accommodation** — Prefer verified platforms and in-person viewing before large payments.
- **Beach belongings** — Keep valuables with you; unattended bags are common targets.
- **Assuming everyone speaks English** — Start with "Perdona" or "Hola".

## Setup

On first durable use, read `references/setup.md`. Never block the first answer on setup.

## Sources

Official and primary verification links live in `references/sources.md`. Prefer those over secondary blogs when fares, tickets, residence procedures, or safety conditions change.
