---
name: berlin
description: "Guide users on visiting, moving to, or living in Berlin. Use when researching Berlin neighborhood profiles, public transit, housing search strategies, visa pathways, or cost of living."
metadata:
  openclaw: '{"emoji":"🐻"}'
---

## When to Use

User asks about Berlin for any purpose: visiting, moving, working, studying, or starting a business. Agent provides practical guidance with current data.

## Quick Reference

| Topic | File | When to load |
|---|---|---|
| **Domain Knowledge** | | |
| Official sources & statutory references | `references/sources.md` | Authoritative municipal, transit, tenancy, and immigration sources |
| Current facts, Blue Card, fares, CanG | `references/research-sources.md` | Before quoting time-sensitive legal, visa, registration, or fare facts |
| **Visitors** | | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` | When discussing attractions (must-see vs skip) |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` | When discussing itineraries (1/3/7 days) |
| Where to stay | `references/visitor-lodging.md` | When discussing where to stay |
| Tips & day trips | `references/visitor-tips.md` | When discussing tips & day trips |
| **Neighborhoods** | | |
| Quick comparison | `references/neighborhoods-index.md` | When discussing quick comparison |
| Mitte, Prenzlauer Berg | `references/neighborhoods-central.md` | When discussing mitte, prenzlauer berg |
| Kreuzberg, Neukölln | `references/neighborhoods-east.md` | When discussing kreuzberg, neukölln |
| Charlottenburg, Wilmersdorf | `references/neighborhoods-west.md` | When discussing charlottenburg, wilmersdorf |
| Friedrichshain, Lichtenberg | `references/neighborhoods-alt.md` | When discussing friedrichshain, lichtenberg |
| Wedding, Moabit | `references/neighborhoods-north.md` | When discussing wedding, moabit |
| Choosing guide | `references/neighborhoods-choosing.md` | When discussing choosing guide |
| **Food** | | |
| Overview & food culture | `references/food-overview.md` | When discussing overview & food culture |
| German cuisine (currywurst, döner) | `references/food-local.md` | When discussing german cuisine (currywurst, döner) |
| International & fine dining | `references/food-international.md` | When discussing international & fine dining |
| Best areas for dining | `references/food-areas.md` | When discussing best areas for dining |
| Dietary, bars, practical | `references/food-practical.md` | When discussing dietary, bars, practical |
| **Practical** | | |
| Moving & settling | `references/resident.md` | When discussing moving & settling |
| Transport (U-Bahn, S-Bahn, BVG) | `references/transport.md` | When discussing transport (u-bahn, s-bahn, bvg) |
| Cost of living | `references/cost.md` | When discussing cost of living |
| Safety & laws | `references/safety.md` | When discussing safety & laws |
| Weather & seasons | `references/climate.md` | When discussing weather & seasons |
| Local services (banking, Anmeldung) | `references/local.md` | When discussing local services (banking, anmeldung) |
| **Career** | | |
| Tech industry & salaries | `references/tech.md` | When discussing tech industry & salaries |
| Business setup & freelancing | `references/business.md` | When discussing business setup & freelancing |
| Visas (work, freelance, EU Blue Card) | `references/visas.md` | When discussing visas (work, freelance, eu blue card) |
| Startups & funding | `references/startup.md` | When discussing startups & funding |
| **Lifestyle** | | |
| Culture & customs | `references/culture.md` | When discussing culture & customs |
| Healthcare & insurance | `references/healthcare.md` | When discussing healthcare & insurance |
| Schools & education | `references/education.md` | When discussing schools & education |
| Expat lifestyle & social | `references/lifestyle.md` | When discussing expat lifestyle & social |
| Cycling & mobility | `references/cycling.md` | When discussing cycling & mobility |

## Core Rules

### Current-information check

Before quoting a fare, visa threshold, registration rule, or legal permission, load `references/research-sources.md` and use the linked official source. Present planning estimates as estimates, not guarantees.

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur, digital nomad
- **Timeline**: Short visit, planning to move, already there
- Load relevant auxiliary file for details

### 2. City Reality
Berlin is Germany's capital with unique characteristics:
- **Size**: 892 km² — largest city in Germany, sprawling
- **Population**: 3.8 million (diverse, 20%+ foreign-born)
- **Language**: German primary; English widely spoken in tech/tourism
- **Government**: City-state (Bundesland), left-leaning politics

### 3. Visa Categories
Non-EU citizens need proper documentation:
- **EU Blue Card**: The annual salary threshold changes each year. Check `references/research-sources.md` and the official source before quoting the current threshold.
- **Work Visa**: Job offer required, employer sponsorship
- **Freelance Visa (Freiberufler)**: Most unique — self-sponsorship possible with client proof
- **Job Seeker Visa**: 6 months to find employment
- **Student Visa**: Enrolled in German institution
See `references/visas.md` and `references/research-sources.md` for requirements and current thresholds.

### 4. Weather Reality
Berlin has distinct seasons:
- **Summer** (Jun-Aug): 20-30°C, long days (sunrise 5am, sunset 9:30pm)
- **Winter** (Dec-Feb): -5 to 5°C, short days (sunrise 8am, sunset 4pm), grey
- **Spring/Fall**: Transitional, unpredictable
- **Key**: Winter affects mental health — light therapy common among expats
See `references/climate.md` for monthly breakdown.

### 5. Planning estimates (verify before relying on them)

| Item | Range |
|------|-------|
| 1BR rent (central) | €1,200-2,000/month |
| 1BR rent (outer) | €800-1,300/month |
| WG room (shared flat) | €500-900/month |
| Senior SWE salary | €70,000-95,000/year gross |
| BVG monthly pass | Check the current zone-specific fare before quoting |
| Döner kebab | €6-8 |
| Restaurant dinner | €20-50/person |
| Health insurance | €200-400/month (public) |

### 6. Cost Reality
Berlin is cheap for Western Europe:
- **Rent**: Rising fast but still 40-60% cheaper than Munich/London
- **Income tax**: 42% top rate + solidarity surcharge — high but includes healthcare
- **Healthcare**: Mandatory, public or private (choice based on income)
- **Hidden costs**: Rundfunkbeitrag (€18.36/month TV tax), warm rent vs cold rent
- **Deposits**: 3 months rent typical (Kaution)
- **Eating out**: Very affordable compared to other capitals

### 7. Transit Excellence
Berlin has extensive public transit:
- **U-Bahn**: 10 lines, 175 stations, runs until ~1am (24h Fri/Sat)
- **S-Bahn**: Suburban rail, connects outer districts
- **Trams**: Mostly east Berlin
- **Buses**: Extensive night bus network (N-lines)
- **No barriers**: Honor system — but inspectors fine €60 for fare-dodging
See `references/transport.md` for complete guide.

### 8. Neighborhood Matching

| Profile | Best Areas |
|---------|------------|
| Young creatives | Kreuzberg, Neukölln, Friedrichshain |
| Families | Prenzlauer Berg, Charlottenburg, Zehlendorf |
| Budget-conscious | Wedding, Lichtenberg, Marzahn |
| Tech workers | Mitte, Prenzlauer Berg, Kreuzberg |
| Nightlife lovers | Friedrichshain, Kreuzberg, Neukölln |
| Quiet professionals | Wilmersdorf, Schöneberg, Steglitz |

## Food Culture Context

Berlin is Germany's most diverse food city:
- **Street food**: Döner capital of Europe, currywurst origin
- **Markets**: Markthalle Neun (Thursday Street Food), Turkish Market
- **Must-try**: Döner, currywurst, Buletten, Eisbein, Berliner (donut)
- **Michelin**: 2 three-star, 5 two-star, 20+ one-star restaurants
- **Bars**: Späti culture (24h corner shops), craft beer scene
- **Brunch**: Weekend institution, reserve ahead for popular spots

See `references/food-overview.md` for complete guide.

## Berlin-Specific Realities

- **Anmeldung** — Register or re-register within 14 days of moving in; use the official Berlin service page for appointment and document requirements.
- **Schufa** — Credit score system. No Schufa = hard to rent.
- **Housing crisis** — Finding apartments is brutal. Budget 2-3 months search.
- **Cash culture** — Many places still cash-only. Always carry euros.
- **Sunday closures** — Shops closed Sundays. Spätis and some bakeries open.
- **Bureaucracy** — Ausländerbehörde appointments book months ahead.
- **Recycling** — Pfand system for bottles. Yellow/blue/brown/black bins.
- **Noise rules** — Quiet hours 10pm-6am and Sundays. Neighbors will complain.
- **Dog city** — Dogs everywhere, allowed in restaurants/trains.
- **Techno capital** — Berghain, Tresor, clubs are cultural institutions.
- **Bike theft** — Very high. Use two locks, register your bike.

## Legal Awareness

Key laws every visitor/resident must know:
- **Drugs**: Cannabis rules are conditional and changeable; use the Federal Ministry of Health CanG guidance for permissions and restrictions.
- **Jaywalking**: Technically illegal (€5-10 fine), rarely enforced
- **Photography**: GDPR strict — Always obtain consent before photographing people
- **Employment**: Must have work permit BEFORE starting work
- **Insurance**: Health insurance mandatory for all residents
- **Tax**: Must file annual tax return (Steuererklärung)
- **Rental**: Strong tenant protections, but Mietpreisbremse complex

See `references/safety.md` and `references/research-sources.md` for legal guidance and current official sources.
