---
name: singapore
description: Guide users on visiting, living, working, or doing business in Singapore using current practical data and legal awareness.
metadata:
  openclaw: '{"emoji":"🦁"}'
  related-skills: '{"travel-planning":"For flight/hotel bookings beyond the skill scope","expat":"For general expatriate advice"}'
---

## Quick Reference

**Trigger:** Use this skill when the user asks about visiting, moving to, working in, studying in, or starting a business in Singapore.
**Action:** Provide practical guidance tailored to their role and timeline; verify time-sensitive legal, immigration, fare, and price claims with the relevant official source before relying on them.

| Topic | File | When to load |
|-------|------|--------------|
| **Visitors** | | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` | User asks what to see |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` | User needs a day-by-day plan |
| Where to stay | `references/visitor-lodging.md` | User needs hotel recommendations |
| Tips & day trips | `references/visitor-tips.md` | General tourist advice |
| **Neighborhoods** | | |
| Quick comparison | `references/neighborhoods-index.md` | User wants to compare living areas |
| CBD, Marina Bay, Raffles | `references/neighborhoods-central.md` | Specific central area queries |
| Orchard, Newton, River Valley | `references/neighborhoods-orchard.md` | Specific orchard area queries |
| Katong, East Coast, Bedok | `references/neighborhoods-east.md` | Specific east area queries |
| Novena, Toa Payoh, Bishan | `references/neighborhoods-suburbs.md` | Specific suburb queries |
| Holland Village, Clementi, Jurong | `references/neighborhoods-west.md` | Specific west area queries |
| Woodlands, Yishun, Punggol | `references/neighborhoods-north.md` | Specific north area queries |
| Choosing guide | `references/neighborhoods-choosing.md` | User needs help picking a neighborhood |
| **Food** | | |
| Overview & hawker culture | `references/food-overview.md` | General dining questions |
| Local cuisine (chicken rice, laksa) | `references/food-local.md` | User wants local food recommendations |
| International & fine dining | `references/food-international.md` | Non-local food recommendations |
| Michelin stars & speakeasies | `references/food-fine-dining.md` | High-end dining queries |
| Best areas for dining | `references/food-areas.md` | Where to go for food |
| Dietary, alcohol, practical | `references/food-practical.md` | Specific dietary needs |
| **Practical** | | |
| Moving & settling | `references/resident.md` | User is moving to Singapore |
| Transport (MRT, buses, Grab) | `references/transport.md` | Commuting questions |
| Cost of living | `references/cost.md` | Budgeting and expenses |
| Safety & laws | `references/safety.md` | Legal and safety questions |
| Weather & survival tips | `references/climate.md` | Weather and packing advice |
| Local services (banking, SIM) | `references/local.md` | Practical setup queries |
| **Career** | | |
| Tech industry & salaries | `references/tech.md` | Tech job market |
| Business setup & ACRA | `references/business.md` | Starting a company |
| Visas (EP, S Pass, PR) | `references/visas.md` | Immigration and work pass queries |
| Startups & funding | `references/startup.md` | Startup ecosystem |
| **Lifestyle** | | |
| Culture & customs | `references/culture.md` | Social norms |
| Healthcare & insurance | `references/healthcare.md` | Medical queries |
| Schools & education | `references/education.md` | Finding schools |
| Expat lifestyle & social | `references/lifestyle.md` | Social life for expats |
| Driving & COE system | `references/driving.md` | Car ownership queries |

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur
- **Timeline**: Short visit, planning to move, already there
- Load relevant auxiliary file for details

### 2. City-State Reality
Singapore is a city-state with unique characteristics:
- **Size**: 733 km² — everything is accessible within 1 hour by MRT
- **Population**: 5.9 million (74% Chinese, 13% Malay, 9% Indian)
- **Language**: English is primary business language; Singlish widely spoken
- **Government**: Highly efficient, strict laws, low corruption

### 3. Immigration and work passes
Employment and residence eligibility depend on the applicant, employer, sector, age, and current Ministry of Manpower rules. Read `references/visas.md` for the background, then verify the current requirements at the Ministry of Manpower before advising on an application. Do not present salary thresholds, quotas, or timelines as guaranteed outcomes.

### 4. Weather and packing
Singapore is hot and humid year-round, with frequent rain. Read `references/climate.md` for planning context; check an up-to-date forecast for specific travel dates.

### 5. Costs and transport
Housing, fares, food, and car costs change. Use `references/cost.md` and `references/transport.md` for planning context, then verify live prices or service changes with the provider before making a booking or budget decision.

### 6. Business and career
For business formation or employment questions, route to `references/business.md` or `references/tech.md`. Confirm any filing, pass, tax, salary, or licensing requirement with the responsible Singapore authority before treating it as current.

### 7. Food and culture
Singapore’s hawker culture, multilingual setting, and varied neighborhoods shape most visitor and relocation decisions. Read `references/food-overview.md` for food questions and select a neighborhood reference for location-specific advice.

### 8. Neighborhood Matching

| Profile | Best Areas |
|---------|------------|
| Young professionals | Tiong Bahru, Tanjong Pagar, Robertson Quay |
| Families | East Coast, Bukit Timah, Holland Village |
| Budget-conscious | Woodlands, Jurong, Tampines |
| Tech workers | One-north, CBD, Tanjong Pagar |
| Beach lifestyle | East Coast, Katong, Sentosa Cove |
| Food lovers | Tiong Bahru, Jalan Besar, Katong |

## Food Culture Context

Singapore is a UNESCO-recognized hawker food destination:
- **Hawker centres**: 100+ centres, 6,000+ stalls, heritage status
- **Must-try dishes**: Chicken rice, laksa, char kway teow, bak kut teh, chili crab
- **Michelin**: 3 three-star, 7 two-star, 32 one-star restaurants
- **Speakeasies**: Jigger & Pony (#3 Asia), 28 Hong Kong Street
- **Halal**: Widely available, MUIS certification

See `references/food-overview.md` for complete guide.

## Legal and safety awareness

Use `references/safety.md` as background, but verify current rules with an official Singapore government source when the user needs legal, immigration, customs, alcohol, public-order, or controlled-substance advice. Communicate uncertainty clearly and direct the user to qualified legal or immigration advice for consequential decisions.

- Keep controlled substances and unfamiliar packages out of travel plans; Singapore enforces serious drug offences strictly.
- Use marked crossings, follow smoking and alcohol-area rules, and check venue or authority guidance for location-specific restrictions.
- Check customs guidance before carrying regulated goods, including gum products, medicines, vaping products, and food.
- Keep valid immigration status and leave or extend permission before expiry.
- Take photographs only where access and signage permit.

## State location

Only persist travel preferences when the user asks to save them. Resolve `<state_root>` from an explicit user- or host-configured path; if no state root is available, ask for one before creating files. After the user confirms the write, store preferences such as visa status, dietary needs, and role at `<state_root>/singapore/preferences.json`. Keep this state outside the skill package and do not store passport, national-ID, bank, or full visa numbers.
