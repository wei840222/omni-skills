---
name: singapore
description: Guide users on visiting, living, working, or doing business in Singapore using current practical data and legal awareness.
metadata:
  openclaw: '{"emoji":"🦁","os":["linux","darwin","win32"],"displayName":"Singapore"}'
  related-skills: '{"travel-planning":"For flight/hotel bookings beyond the skill scope","expat":"For general expatriate advice"}'
---

## Quick Reference

**Trigger:** Use this skill when the user asks about visiting, moving to, working in, studying in, or starting a business in Singapore.
**Action:** Provide practical, current guidance tailored to their specific role and timeline.

| Topic | File | When to load |
|-------|------|--------------|

| Topic | File |
|-------|------|
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

### 3. Visa Categories
Employment requires proper visa sponsorship:
- **EP (Employment Pass)**: S$5,600+ salary (increases to S$6,200 for financial services), COMPASS framework (40 points)
- **S Pass**: S$3,300+ salary, quota-limited
- **Dependent Pass**: Requires S$6,000+ sponsor salary
- **PR pathway**: Typically 2-5 years with stable employment
See `references/visas.md` for current requirements (Feb 2026).

### 4. Weather Reality
Singapore is tropical year-round:
- **Temperature**: 27-32°C constant, no seasons
- **Humidity**: 80%+ average — acclimatization takes 2-4 weeks
- **Rain**: Afternoon thunderstorms common, carry umbrella always
- **Monsoons**: NE (Dec-Mar), SW (Jun-Sep) — affects outdoor activities
See `references/climate.md` for monthly breakdown.

### 5. Current Data (Feb 2026)

| Item | Range |
|------|-------|
| 1BR rent (CBD) | S$3,000-5,000/month |
| 1BR rent (suburbs) | S$2,000-3,500/month |
| HDB room rental | S$800-1,500/month |
| Senior SWE salary | S$12,000-20,000/month |
| MRT monthly pass | S$128 (adult) |
| Hawker meal | S$4-8 |
| Restaurant dinner | S$30-100/person |
| International school | S$30,000-55,000/year |

### 6. Cost Reality
Singapore is expensive but tax-efficient:
- **No capital gains tax, no inheritance tax**
- **Income tax**: 0-24% progressive (most pay 7-15%)
- **Housing**: 30-50% of budget typical for expats
- **COE (car permit)**: S$100,000-150,000 for 10 years — most don't drive
- **Hidden costs**: Agent fees (1 month rent), security deposits (2 months)
- **Hawker centres**: Affordable meals (S$4-8) offset restaurant costs

### 7. Transit Excellence
Unlike most cities, Singapore has world-class public transport:
- **MRT**: 6 lines, 140+ stations, S$1-2.50 per trip
- **Buses**: Extensive network, same EZ-Link/SimplyGo card
- **Grab**: Primary ride-hailing, S$8-25 for most trips
- **No car needed**: 90%+ of residents don't own cars
See `references/transport.md` for complete guide.

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

## Singapore-Specific Traps

- **Chewing gum ban** — Importing gum for personal use is illegal. Ensure you arrive without it.
- **Drug laws** — Zero tolerance. Death penalty for trafficking. Even trace amounts = prison.
- **Vandalism** — Criminal offense including caning. Keep public surfaces clean.
- **Jaywalking** — S$50 fine within 50m of crossing. Police do enforce.
- **Smoking** — Banned in most public areas. S$200+ fines.
- **Littering** — S$300 first offense, S$1,000+ repeat. Very enforced.
- **Public intoxication** — Liquor control areas 10:30pm-7am in some zones.
- **LGBTQ+** — 377A repealed (2022) but limited protections. Discretion advised.
- **Criticism of government** — Defamation laws strict. Maintain a respectful public stance regarding the government.
- **Photography** — Only take photos in permitted tourist or public areas, avoiding government or military sites.
- **Overstaying visa** — Criminal offense, caning possible. Depart before your visa expires.

## Legal Awareness

Key laws every visitor/resident must know:
- **Drugs**: Zero tolerance. Death penalty for 15g heroin, 500g cannabis.
- **Weapons**: Strictly prohibited including pocket knives.
- **Alcohol**: Legal at 18+, retail sales end 10:30pm.
- **Public order**: Unlicensed gatherings >1 person in public can be illegal.
- **Internet**: VPNs legal but bypassing government blocks is not.
- **Employment**: Working without valid pass = deportation + ban.

See `references/safety.md` for comprehensive legal guidance.

## State location

Singapore visitor planning requires storing user preferences (visa status, dietary needs, role). Store this state in:

1. `<state_root>/singapore/preferences.json`

Do not use absolute paths.

## State location

Singapore visitor planning requires storing user preferences (visa status, dietary needs, role). Store this state in:

1. `<state_root>/singapore/preferences.json`

Do not use absolute paths.
