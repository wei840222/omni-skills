---
name: tokyo
description: "Navigate Tokyo for tourism, residency, tech work, or studying. Use when the user asks about Tokyo neighborhoods, transport, living costs, safety, local culture, or itineraries; verify live fares, rents, visas, and disaster status before decisive advice."
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🗼"}'
  related-skills: '{"travel":"Multi-destination trip planning beyond Tokyo-specific routing.","booking":"Accommodation comparisons and reservation completion after a Tokyo stay is selected.","japan":"Japan-wide travel and regional context outside Greater Tokyo.","japanese":"Natural Japanese language help for deeper local integration."}'
---

This skill is stateless and does not store local configuration or persistent user state. For live fares, rents, visa eligibility, lodging availability, or weather/disaster-dependent plans, load the matching reference and verify the official source in `references/sources.md` before treating a figure as current.

## When to Use

Use when the user asks about Tokyo for visiting, moving, working, studying, or starting a business. Give practical guidance with dated planning ranges, then verify mutable facts at official sources before booking, immigration, payment, or same-day safety decisions.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Visitors** | | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` | When user wants to know what to see or skip |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` | When user needs a daily schedule |
| Where to stay | `references/visitor-lodging.md` | When user is picking a hotel area |
| Tips & day trips | `references/visitor-tips.md` | When user asks for excursions or general tourist advice |
| **Neighborhoods** | | |
| Quick comparison | `references/neighborhoods-index.md` | When user needs an overview of areas |
| Central (Minato, Shibuya, Shinjuku) | `references/neighborhoods-central.md` | When user asks about central hubs |
| Residential (Meguro, Setagaya) | `references/neighborhoods-residential.md` | When user asks about living outside the center |
| East (Asakusa, Ueno, Sumida) | `references/neighborhoods-east.md` | When user asks about the older/eastern side |
| Outer (Kichijoji, Nerima) | `references/neighborhoods-outer.md` | When user asks about suburban areas |
| Choosing guide | `references/neighborhoods-choosing.md` | When user doesn't know which neighborhood fits them |
| **Food** | | |
| Overview & dining culture | `references/food-overview.md` | When user asks about general dining |
| Traditional (sushi, ramen, etc.) | `references/food-traditional.md` | When user asks for classic Japanese foods |
| Markets & depachika | `references/food-markets.md` | When user asks about street food or markets |
| Best areas by cuisine | `references/food-areas.md` | When user wants to know where to find specific foods |
| Etiquette & practical tips | `references/food-practical.md` | When user asks about reservations, tipping, or manners |
| **Practical** | | |
| Moving & settling | `references/resident.md` | When user is relocating |
| Transport (JR, Metro, IC cards) | `references/transport.md` | When user asks how to get around |
| Cost of living | `references/cost.md` | When user asks about rent or expenses |
| Safety | `references/safety.md` | When user asks about crime or disasters |
| Weather & seasons | `references/climate.md` | When user asks when to visit or about weather |
| Local services | `references/local.md` | When user needs gyms, doctors, etc. |
| **Culture** | | |
| Etiquette & customs | `references/culture.md` | When user asks about behavioral norms |
| **Career** | | |
| Tech industry | `references/tech.md` | When user is looking for tech jobs |
| Students | `references/student.md` | When user is studying abroad |
| Startups | `references/startup.md` | When user is starting a business |
| **Sources** | | |
| Official / primary sources | `references/sources.md` | Before quoting live fares, rents, visas, or disaster status |

## Core Rules

### 1. Identify User Context First
- **Role**: Tourist, resident, tech worker, student, entrepreneur
- **Timeline**: Short visit, planning to move, already there
- **Japanese level**: None, basic, conversational, fluent
- Load relevant auxiliary file for details

### 2. Safety Context
Tokyo is one of the world's safest major cities. Main concerns are minor:
- Petty theft in crowded tourist areas (Shibuya, Asakusa, Akihabara)
- Drink spiking in Roppongi/Kabukicho nightlife districts
- Overcharging scams at some hostess/host clubs
- Natural disasters (earthquakes, typhoons)
See `references/safety.md` for detailed guidance.

### 3. Weather Expectations
- Four distinct seasons
- Summer (Jun-Sep): Hot, humid (30-35°C), rainy season in June
- Winter (Dec-Feb): Cold, dry (5-10°C), rarely snows
- Best months: March-May (cherry blossoms), October-November (autumn leaves)
- Typhoon season: August-October
See `references/climate.md` for monthly breakdown.

### 4. Current Data (Sep 2026)

| Item | Range |
|------|-------|
| 1K/1R rent (studio) | ¥105,000-145,000 (central), ¥75,000-110,000 (outer) |
| 1LDK rent | ¥155,000-250,000 |
| Senior SWE salary | ¥8M-14M/year |
| Student budget | ¥170,000-230,000/month |
| Suica/Pasmo fare | ¥200-300/ride |
| Monthly transit pass | ¥8,000-15,000 |

### 5. Tourist Traps
- Skip: Overpriced tourist ramen in Shibuya crossing area
- Do: Standing sushi near Tsukiji/Toyosu, local izakaya in Yurakucho
- Watch: Roppongi "free drink" touts (lead to overcharging scams)
- Free: Meiji Shrine, Imperial Palace East Gardens, Senso-ji Temple
- Golden Gai bars welcome foreigners but have ¥500-1000 cover charges

### 6. Transit System
Tokyo has the most complex transit system in the world:
- **JR Lines**: Yamanote loop, Chuo, Sobu (green Suica card)
- **Tokyo Metro**: 9 lines (private, accepts Suica)
- **Toei Subway**: 4 lines (city-operated, accepts Suica)
- **Private railways**: Tokyu, Odakyu, Keio, etc.
- **IC cards**: Suica/Pasmo interchangeable, use everywhere
See `references/transport.md` for full guide.

### 7. Neighborhood Matching

| Profile | Best Areas |
|---------|------------|
| Young professionals | Shibuya, Nakameguro, Ebisu |
| Families | Setagaya, Meguro, Kichijoji |
| Budget-conscious | Nerima, Adachi, Edogawa |
| Tech workers | Shibuya, Roppongi, Shinagawa |
| Traditional vibes | Asakusa, Yanaka, Kagurazaka |
| Nightlife seekers | Shinjuku, Roppongi, Shibuya |

## Language Context

### Japanese Language Reality

Unlike many global cities, English proficiency is limited:

| Situation | English Support |
|-----------|-----------------|
| Tourist attractions | Good signage, staff varies |
| Restaurants | Menus sometimes, conversation rare |
| Train stations | Excellent signage |
| Daily life | Very limited |
| Business | Depends on company |
| Medical | Limited, bring translator |

**Practical advice:**
- Learn basic Japanese phrases
- Google Translate camera mode works well for menus
- Download offline Japanese in Google Translate
- Major chains (Starbucks, McDonald's) have English menus
- Hospital/clinic visits often need interpreter

### Essential Phrases

| Japanese | Romaji | English |
|----------|--------|---------|
| すみません | Sumimasen | Excuse me / Sorry |
| ありがとうございます | Arigatou gozaimasu | Thank you |
| お会計お願いします | Okaikei onegaishimasu | Check please |
| これください | Kore kudasai | This please |
| 英語メニューありますか | Eigo menu arimasu ka | English menu? |
| いくらですか | Ikura desu ka | How much? |

## Tokyo-Specific Traps

- **Roppongi touts** — "Free drinks" lead to ¥50,000+ bills. Ignore street touts and walk past them.
- **Kabukicho host/hostess clubs** — Can run ¥100,000+ per visit. Visit only when accompanied by trusted locals.
- **Fake monks** — Aggressive "donation" requests near Asakusa. Authentic monks wait for visitors at temples.
- **Rush hour** (7:30-9:30am) — Trains packed 200%+ capacity. Travel before 7:30am or after 9:30am.
- **Airport taxi** — ¥20,000+ to central Tokyo. Use Limousine Bus (¥3,200) or train (¥1,200-2,500).
- **"No foreigners" signs** — Some establishments cater exclusively to Japanese speakers. Move on to the many welcoming international venues.
- **Cash is king** — Many places are cash-only. Carry ¥10,000-20,000.
- **Tipping** — Pay the exact bill amount. Tipping is not practiced and will cause confusion.
- **Walking while eating** — Culturally inappropriate except at festivals.
- **Talking on trains** — Keep conversations quiet; phone calls are prohibited.

## Visa & Residency Quick Reference

| Purpose | Visa Type | Duration |
|---------|-----------|----------|
| Tourism | Visa-free (most Western countries) | 90 days |
| Working | Work visa (sponsored) | 1-5 years |
| Tech/Startup | Engineer/HSP visa | 1-5 years |
| Student | Student visa | Duration of program |
| Digital nomad | No specific visa (use tourist) | 90 days max |

**Note**: Japan has no digital nomad visa. Remote workers typically use tourist visa (no local employment allowed) or need proper work visa sponsorship.
