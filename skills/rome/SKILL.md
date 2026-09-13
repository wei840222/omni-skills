---
name: rome
description: Provide practical Rome guidance for visitors, expats, digital nomads, students, retirees, and founders—neighborhoods, transport, costs, visas, food, safety, and lifestyle. Use when the user asks about Rome-specific decisions; verify live fares, rents, visas, tickets, and safety conditions before decisive advice. Not a substitute for multi-city Italy routing (`italy`/`travel`) or Italian-language writing (`italian`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏛️","requires":{"config":["<state_root>/rome/"]}}'
  related-skills: '{"italy":"Italy-wide destinations and multi-city routing beyond Rome-only depth.","travel":"Multi-destination trip systems and general travel memory.","italian":"Natural Italian writing and register rather than Rome logistics.","europe":"Cross-border EU mobility context beyond Rome.","booking":"Lodging and reservation execution after a Rome base is chosen.","career":"Broader career decisions after Rome tech or job context is set.","startup":"Founder workflows after Rome startup landscape is scoped.","food":"Deeper food-system workflows beyond Roman dining guidance.","dubai":"Expat-destination comparison when weighing Rome against other hubs."}'
---

## State location

Persistent Rome context lives under `<state_root>/rome/` (see `references/memory-template.md`). One-off visitor questions can stay effectively stateless.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/rome/`, `<workspace>/memory/rome/`, `~/rome/`.
3. If none exists and state must be created, default to `<workspace>/rome/`.

Use the selected `<state_root>` for every state operation in this skill.

```
<state_root>/rome/
└── memory.md     # User context and preferences
```

On first use with durable context, read `references/setup.md` for optional workspace integration. Answer the user's question first; setup is never blocking.

## When to Use

User asks about Rome for visiting, relocating, working remotely, studying, retiring, or starting a business. Establish role, timeline, budget, party, language level, and neighborhood constraints first, then load only the needed reference files. For multi-city Italy trips prefer `italy`/`travel`; for Italian-language drafting prefer `italian`.

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
| Historic Center (Centro Storico, Trastevere, Campo de' Fiori) | `references/neighborhoods-historic.md` |
| Trendy & Creative (San Lorenzo, Pigneto, Ostiense) | `references/neighborhoods-trendy.md` |
| Upscale (Parioli, Prati, Aventino) | `references/neighborhoods-upscale.md` |
| Residential (Testaccio, San Giovanni, Monteverde) | `references/neighborhoods-residential.md` |
| Outer & Suburbs (EUR, Garbatella, Ostia) | `references/neighborhoods-outer.md` |
| Choosing guide | `references/neighborhoods-choosing.md` |
| **Food** | |
| Overview & dining scene | `references/food-overview.md` |
| Roman cuisine essentials | `references/food-roman.md` |
| Traditional Roman dishes | `references/food-local.md` |
| International cuisine | `references/food-international.md` |
| Pizza & street food | `references/food-pizza.md` |
| Coffee & aperitivo culture | `references/food-coffee.md` |
| Best areas for dining | `references/food-areas.md` |
| Practical (tipping, hours, reservations) | `references/food-practical.md` |
| **Practical** | |
| Moving & settling | `references/resident.md` |
| Transport (metro, buses, trams) | `references/transport.md` |
| Cost of living | `references/cost.md` |
| Safety & laws | `references/safety.md` |
| Weather & seasonal tips | `references/climate.md` |
| Local services (codice fiscale, healthcare, SIM) | `references/local.md` |
| **Career** | |
| Tech scene & remote work | `references/tech.md` |
| Business setup & freelancing | `references/business.md` |
| Visas (Elective Residence, Digital Nomad, EU) | `references/visas.md` |
| Startups & innovation | `references/startup.md` |
| **Lifestyle** | |
| Culture & customs | `references/culture.md` |
| Healthcare (SSN) | `references/healthcare.md` |
| Schools & universities | `references/education.md` |
| Expat lifestyle & social | `references/lifestyle.md` |
| Driving & car ownership | `references/driving.md` |
| Parks, beaches & outdoors | `references/outdoors.md` |
| **Sources** | |
| Official portals & verification | `references/sources.md` |

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, expat, digital nomad, student, retiree, entrepreneur
- **Timeline**: Short visit, planning to move, already there
- Load relevant auxiliary file for details

### 2. The Eternal City Reality
Rome is not a modern efficient city — it's a living museum with ancient infrastructure:
- **Bureaucracy**: Italian bureaucracy is legendary. Patience required.
- **Pace**: Things move slowly. "Piano piano" (slowly, slowly) is the motto.
- **Chaos**: Traffic, noise, crowds are constant. Embrace it.
- **Beauty**: 3,000 years of history at every corner. Worth the chaos.
See `references/culture.md` for detailed guidance.

### 3. Visa & Residency Options
Key pathways for non-EU citizens:
- **Elective Residence Visa**: Passive income route (no work permitted)
- **Digital Nomad Visa**: New in 2024, remote workers
- **Student Visa**: Universities and language schools
- **Self-Employment Visa**: Freelancers and entrepreneurs
- **EU Citizens**: Free movement, just register with comune
See `references/visas.md` for current requirements and processes.

### 4. Weather Reality
- **Mediterranean climate**: Hot dry summers, mild wet winters
- **Best seasons**: Spring (Apr-May) and Fall (Sep-Oct) — 18-25C, fewer tourists
- **Summer (Jun-Aug)**: Very hot (35C+), extremely crowded, locals flee
- **Winter (Dec-Feb)**: Mild (8-15C), rainy, but Rome is beautiful
- **August**: Many businesses close. Romans leave for Ferragosto.
See `references/climate.md` for monthly breakdown.

### 5. Current Data (Feb 2026)

| Item | Range |
|------|-------|
| 1BR rent (center) | EUR 1,200-1,800/month |
| 1BR rent (periphery) | EUR 700-1,000/month |
| Average salary | EUR 1,500-2,000/month net |
| Senior developer salary | EUR 2,500-4,000/month net |
| Metro single ticket | EUR 1.50 |
| 24h transport pass | EUR 7.00 |
| Espresso at bar | EUR 1.20-1.50 |
| Pizza al taglio slice | EUR 2.50-4.00 |
| Restaurant meal | EUR 15-25 |

### 6. Cost Reality
Rome is moderate by Western European standards:
- **Housing**: Expensive in center, reasonable in outer neighborhoods
- **Food**: Eating out affordable, groceries reasonable
- **Transport**: Excellent public transit, cheap
- **Healthcare**: Public (SSN) is free/cheap for residents
- **Hidden costs**: Bureaucracy fees, furniture (unfurnished common), utilities

### 7. Transit Excellence
Rome has good public transport despite the chaos:
- **Metro**: 3 lines (A, B, C), covers main areas
- **Buses**: Extensive ATAC network, can be chaotic
- **Trams**: Several lines, scenic
- **Regional trains**: To Ostia beach, Fiumicino, suburbs
- **Walking**: Historic center is very walkable
See `references/transport.md` for complete guide.

### 8. Neighborhood Matching

| Profile | Best Areas |
|---------|------------|
| First-time visitor | Centro Storico, Trastevere |
| Budget traveler | Termini area, San Lorenzo |
| Expat families | Parioli, Monteverde, EUR |
| Digital nomads | Trastevere, Testaccio, Pigneto |
| Students | San Lorenzo, Pigneto, Garbatella |
| Retirees | Prati, Aventino, Trastevere |
| Short-term luxury | Campo de' Fiori, Piazza Navona area |

## The Rome Experience

Understanding Rome requires accepting its contradictions:
- **Ancient + Modern**: 3,000 years coexist, often uneasily
- **Beautiful + Chaotic**: Stunning beauty amid traffic and crowds
- **Frustrating + Rewarding**: Bureaucracy is painful, dolce vita is real
- **Touristy + Authentic**: Both exist, sometimes in same street

The city rewards patience and curiosity. Embrace the experience instead of trying to optimize Rome.

## Rome-Specific Traps

- **August shutdown** — Half the city closes for Ferragosto. Plan around it.
- **Termini area hotels** — Convenient but sketchy at night. Not the best area.
- **Restaurant tourist menus** — Fixed price "menu turistico" is usually bad. Skip these options.
- **Gladiator photos** — They'll demand money. Walk away without engaging.
- **Taxi scams** — Use official white taxis only, insist on meter.
- **Pickpockets** — Crowded metro, tourist sites. Keep valuables secure.
- **Siesta hours** — Many shops close 13:00-16:00. Adapt.
- **Sunday closures** — Many things closed, especially outside center.
- **Fountains are drinking water** — The "nasoni" — use them!
- **Dress codes at churches** — Covered shoulders and knees required.

## Legal Awareness

Key laws visitors/residents must know:
- **Drinking**: Legal at 18. Public drinking generally tolerated in piazzas.
- **Smoking**: Banned in enclosed public spaces, some outdoor areas.
- **Monuments**: Sitting on Spanish Steps is fined. Eat only in designated dining areas away from fountains.
- **Driving ZTL**: Limited traffic zones — big fines if you enter without permit.
- **Cannabis**: Decriminalized for small amounts, but still illegal.
- **Tax residency**: 183+ days = tax resident. 7% flat tax for retirees available.
- **Receipts**: Businesses must give receipts; you can be fined for not taking one.

See `references/safety.md` for comprehensive legal guidance.

## The Housing Reality (2026)

Housing in Rome:
- **Center**: Expensive, often old buildings, character but issues
- **Semi-center**: Better value, good transport links
- **Outer areas**: Most affordable, requires car or long commute
- **Furnished vs unfurnished**: Unfurnished very common (you buy everything)
- **Contracts**: Typically 4+4 year standard contracts
- **Deposits**: Usually 2-3 months rent
- **Competition**: Good apartments go fast, especially near center

## Language

- **Italian essential**: Less English than Northern Europe
- **Romanesco**: Local dialect, colorful expressions
- **Gestures**: Italians communicate with hands — learn them
- **Bureaucracy in Italian**: Almost always, bring translator if needed
- **Learning Italian**: Greatly improves quality of life and integration
- **English improving**: Younger generation, tourist areas, but verify beforehand

## Related Skills

Route adjacent work instead of stretching this package:

- `italy` — Italy-wide destinations and multi-city routing
- `travel` — Multi-destination trip systems
- `italian` — Natural Italian writing and register
- `europe` — Broader EU mobility context
- `booking` — Reservation execution after a Rome base is chosen
- `career` / `startup` / `food` / `dubai` — adjacent career, founder, dining, or destination-comparison depth
