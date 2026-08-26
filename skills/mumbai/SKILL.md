---
name: mumbai
description: Assist users with navigating Mumbai, covering neighborhoods, transport, living costs, visas, and local insights for various user personas.
metadata:
  openclaw: '{"emoji": "\ud83c\udfd9\ufe0f", "requires": {"bins": []}, "os": ["linux", "darwin", "win32"], "displayName": "Mumbai"}'
  related-skills: '{"dubai": "Fellow financial hub, many Mumbai expats there", "travel": "General travel planning and tips", "austin": "Tech hub comparison for relocation decisions"}'
---

## When to Use

User asks about Mumbai for any purpose: visiting, moving, working, studying, or starting a business. Agent provides practical guidance with current data.

## Quick Reference

*Load the appropriate file from the `references/` directory based on the user's need. Only load files if their specific details are required.*

| Topic | File | When to load |
|-------|------|--------------|
| Domain knowledge | `references/domain-knowledge.md` | General background on Mumbai's economy and geography |
| **Visitors** | | |
| Attractions | `references/visitor-attractions.md` | User asks for places to visit |
| Itineraries | `references/visitor-itineraries.md` | User needs a planned schedule (1/3/7 days) |
| Where to stay | `references/visitor-lodging.md` | User asks about hotels or areas to stay for a visit |
| Tips & trips | `references/visitor-tips.md` | User asks for visitor advice or day trips |
| **Neighborhoods** | | |
| Quick comparison| `references/neighborhoods-index.md` | User wants a summary of different areas |
| South Mumbai | `references/neighborhoods-south.md` | User asks about Colaba, Fort, Marine Drive |
| Bandra/West | `references/neighborhoods-bandra.md` | User asks about Bandra or Western Suburbs |
| Powai/Central | `references/neighborhoods-central.md` | User asks about Powai or Central Suburbs |
| Navi Mumbai | `references/neighborhoods-extended.md` | User asks about Navi Mumbai or Thane |
| Choosing guide | `references/neighborhoods-choosing.md` | User needs help picking a neighborhood |
| **Food** | | |
| Dining scene | `references/food-overview.md` | User asks for a general food guide |
| Street food | `references/food-street.md` | User asks about street food |
| Regional Indian | `references/food-regional.md` | User wants regional Indian cuisine |
| International | `references/food-international.md` | User wants international or fine dining |
| Dining areas | `references/food-areas.md` | User asks for best areas to eat |
| Practical tips | `references/food-practical.md` | User asks about dietary needs or dining etiquette |
| **Practical** | | |
| Settling | `references/resident.md` | User is moving to Mumbai |
| Transport | `references/transport.md` | User asks about trains, autos, or metro |
| Cost of living | `references/cost.md` | User asks about expenses |
| Safety & tips | `references/safety.md` | User asks about safety |
| Climate | `references/climate.md` | User asks about weather or monsoon |
| Local services | `references/local.md` | User needs info on banking or SIM cards |
| **Career** | | |
| Tech industry | `references/tech.md` | User asks about tech jobs or salaries |
| Business setup | `references/business.md` | User asks about starting a company |
| Visas | `references/visas.md` | User needs visa information |
| Startups | `references/startup.md` | User asks about the startup ecosystem |
| Entertainment | `references/entertainment.md` | User asks about Bollywood or media |
| **Lifestyle** | | |
| Culture | `references/culture.md` | User asks about local customs |
| Healthcare | `references/healthcare.md` | User asks about hospitals or medical care |
| Education | `references/education.md` | User asks about schools |
| Lifestyle | `references/lifestyle.md` | User asks about expat or local life |
| Driving | `references/driving.md` | User asks about traffic or driving |

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur, NRI returning
- **Timeline**: Short visit, planning to move, already there
- Load relevant auxiliary file for details

### 2. Maximum City Reality
Mumbai is India's financial capital and most populous city:
- 20+ million people in metro area
- Extreme density in island city (South Mumbai)
- Housing is the primary expense and challenge
- "Jugaad" (creative problem-solving) is essential
Load `references/resident.md` for settling guidance.

### 3. Train-Centric Transport
Unlike car-centric cities, Mumbai runs on local trains:
- **Western Line**: Churchgate to Dahanu (suburbs)
- **Central Line**: CST to Kasara/Karjat
- **Harbour Line**: CST to Panvel (Navi Mumbai)
- 7.5 million daily passengers — world's most crowded
- Peak hours (8-11am, 5-9pm) are intense
Load `references/transport.md` for survival guide.

### 4. Monsoon Reality
- **Monsoon (June-September)**: Heavy rainfall, flooding common
- **October-February**: Pleasant, best time to visit
- **March-May**: Hot and humid, pre-monsoon
- Monsoon affects everything: transport, housing (waterlogging), daily life
Load `references/climate.md` for monthly breakdown and monsoon survival.

### 5. Current Data (Feb 2026)

| Item | Range |
|------|-------|
| 1BHK rent (Bandra) | ₹40,000-80,000/month (~$475-950) |
| 1BHK rent (South Mumbai) | ₹50,000-1,50,000/month (~$600-1,800) |
| Senior SWE salary | ₹40-80 LPA (~$48K-96K/year) |
| Local train monthly pass | ₹500-1,500 (~$6-18) |
| Street food meal | ₹50-150 (~$0.60-1.80) |
| Restaurant meal (mid-range) | ₹500-1,500/person (~$6-18) |
| International school fees | ₹5-25 LPA (~$6K-30K/year) |

### 6. Housing Reality
Mumbai has India's most expensive real estate:
- **South Mumbai**: Premium, colonial buildings, sea views, astronomical prices
- **Bandra-Khar-Santacruz**: Hip, expat-friendly, Bollywood crowd
- **Powai**: Tech hub, modern apartments, lake views
- **Navi Mumbai**: Affordable, planned city, longer commute
- **Deposit**: 3-6 months rent (negotiable)
- **Brokerage**: 1-2 months rent
Load the relevant `references/neighborhoods-*.md` for detailed area guides.

### 7. Neighborhood Matching

| Profile | Best Areas |
|---------|------------|
| Young professionals | Bandra, Lower Parel, Andheri |
| Families | Powai, Hiranandani, Thane |
| Heritage/culture lovers | South Mumbai, Fort, Colaba |
| Tech workers | Powai, BKC, Andheri East |
| Budget-conscious | Navi Mumbai, Thane, Malad |
| Bollywood/media | Bandra, Juhu, Versova |
| Sea views | Marine Drive, Worli, Bandra Bandstand |

### 8. Business Environment
- **BKC (Bandra Kurla Complex)**: Financial district, corporate HQs
- **Lower Parel**: Old mills converted to offices, media companies
- **Andheri-Powai corridor**: Tech parks, IT companies
- **Nariman Point**: Traditional business district (declining)
- SEZ benefits available in certain zones
Load `references/business.md` and `references/startup.md` for setup guidance.

## Mumbai-Specific Traps

- **Monsoon underestimation** — July flooding can strand you for hours. Check weather before traveling and plan accordingly.
- **Peak hour trains** — 8-10am and 6-8pm are extremely crowded. Travel outside these hours when possible, or prepare for dense crowds.
- **Housing deposits** — Landlords often ask for 6+ months. Negotiate for a 3-month deposit.
- **Broker fees** — The standard fee is 1 month's rent. Confirm this upfront.
- **Auto/taxi refusals** — Use Uber or Ola for more reliable rides when local drivers refuse destinations.
- **Traffic assumptions** — A 10km journey can take 2 hours. Always add buffer time to your schedule.
- **Water quality** — Drink only filtered or bottled water.
- **Power cuts** — Check for backup power when renting apartments, as cuts occur in some areas.
- **Festival traffic** — Plan for massive congestion during Ganesh Chaturthi and Diwali.
- **Rent vs buy** — Renting is the norm due to extremely high property prices.

## Cultural Context

Mumbai is cosmopolitan but has local customs:
- **Language**: Hindi and Marathi are primary. English widely spoken in business.
- **Festivals**: Ganesh Chaturthi (Sep) is THE Mumbai festival.
- **Dress code**: Liberal by Indian standards but modest in religious sites.
- **Tipping**: 10% in restaurants, small tips to service staff appreciated.
- **Bargaining**: Expected in markets, not in malls/fixed-price shops.
- **Personal space**: Different norms in crowded areas — patience required.
Load `references/culture.md` for detailed guidance.

## Visa Information

For foreigners:
- **e-Visa**: Available for tourism (30/90/180 days)
- **Employment Visa**: Requires job offer, company sponsorship
- **Business Visa**: For business meetings, conferences
- **OCI (Overseas Citizen of India)**: For people of Indian origin — lifetime validity

For NRIs returning:
- No visa needed but tax residency rules apply
- Bank account options (NRE/NRO) important
Load `references/visas.md` for detailed requirements.
