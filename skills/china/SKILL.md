---
name: china
description: Plan China travel itineraries, handle regional logistics, navigate payment/visa constraints, and organize local transit. Use when a user asks about traveling in China, city itineraries, visa-free transit rules, or navigating Chinese apps.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇨🇳"}'
  related-skills: '{"chinese":"Language support for local communication and signs.","english":"Backup communication support for multilingual logistics.","food":"Deeper restaurant and cuisine recommendations.","travel":"General trip planning and itinerary structuring."}'
---

## State location

China state may exist in `<workspace>/china/`, `<workspace>/memory/china/`, or `~/china/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/china/`, `<workspace>/memory/china/`, `~/china/`.
3. If none exists and state must be created, default to `<workspace>/china/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

If `<state_root>` doesn't exist or is empty, read `references/setup.md` and start naturally.

## When to Use

User planning a trip to China or asking for local insights: where to base, how to split huge distances, what to prioritize by season, and how to handle transport, payments, connectivity, and pace.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for structure.

```
<state_root>/
└── memory.md     # Trip context
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Major Hubs and Routes** | | |
| Beijing complete guide | `references/beijing.md` | User asks about this topic. |
| Shanghai complete guide | `references/shanghai.md` | User asks about this topic. |
| Guangzhou and Shenzhen complete guide | `references/guangzhou-shenzhen.md` | User asks about this topic. |
| Xi'an complete guide | `references/xian.md` | User asks about this topic. |
| Chengdu and Chongqing complete guide | `references/chengdu-chongqing.md` | User asks about this topic. |
| Yunnan complete guide | `references/yunnan.md` | User asks about this topic. |
| Guilin and Yangshuo complete guide | `references/guilin-yangshuo.md` | User asks about this topic. |
| Zhangjiajie and Hunan complete guide | `references/zhangjiajie-hunan.md` | User asks about this topic. |
| Silk Road west corridor complete guide | `references/silk-road-gansu-qinghai.md` | User asks about this topic. |
| Hainan complete guide | `references/hainan.md` | User asks about this topic. |
| **Planning** | | |
| Core itineraries | `references/itineraries.md` | User asks about this topic. |
| Long-distance route patterns | `references/long-routes.md` | User asks about this topic. |
| Where to stay by style | `references/accommodation.md` | User asks about this topic. |
| Entry and documents planning | `references/entry-and-documents.md` | User asks about visas, TWOV, or registration. |
| Useful apps | `references/apps.md` | User asks about this topic. |
| Research sources | `references/sources.md` | Before asserting current entry, payment, or connectivity rules. |
| **Food and Drink** | | |
| Regional dishes and restaurant strategy | `references/food-guide.md` | User asks about this topic. |
| Wine, tea, baijiu, and bar strategy | `references/wine.md` | User asks about this topic. |
| **Experiences** | | |
| Signature experiences | `references/experiences.md` | User asks about this topic. |
| Beaches and island planning | `references/beaches.md` | User asks about this topic. |
| Hikes and mountain safety | `references/hiking.md` | User asks about this topic. |
| Nightlife by city type | `references/nightlife.md` | User asks about this topic. |
| **Reference** | | |
| Regions and route differences | `references/regions.md` | User asks about this topic. |
| Culture, etiquette, expectations | `references/culture.md` | User asks about this topic. |
| Seasonality and climate strategy | `references/seasonality.md` | User asks about this topic. |
| Traveling with children | `references/with-kids.md` | User asks about this topic. |
| High-altitude and permit-sensitive areas | `references/tibet-and-high-altitude.md` | User asks about this topic. |
| **Practical** | | |
| Intercity transport and rail/air tradeoffs | `references/transport.md` | User asks about this topic. |
| Telecom and SIM/eSIM planning | `references/telecoms.md` | User asks about this topic. |
| Payments and internet constraints | `references/payment-and-internet.md` | User asks about Alipay, WeChat Pay, cash, or connectivity. |
| Emergencies and safety | `references/emergencies.md` | User asks about this topic. |

## Core Rules

### 1. Specific Over Generic
Structure advice by saying "pick 2-3 bases max, anchor each by one high-value district cluster, and protect transfer days as logistics days, not attraction marathons." instead of using generic highlight tours.

### 2. Local Perspective
What locals and repeat travelers actually do, not brochure advice:
- China rewards route logic and punishes over-ambitious city stacking
- Same-day intercity transfers can consume most useful day hours
- Weather and air quality windows can change outdoor planning fast
- Payment and connectivity setup quality affects everything else

### 3. Regional Differences

| Region | Key difference |
|--------|----------------|
| Beijing and North China | Imperial history, museums, colder winters, major landmarks |
| Shanghai and East coast | Global-city pace, neighborhoods, modern food and design |
| Pearl River Delta | Manufacturing-meets-tech region, fast intercity access |
| Southwest (Sichuan, Yunnan, Guizhou) | Food depth, mountain routes, climate variation |
| Northwest (Gansu, Qinghai, Xinjiang corridors) | Long distances, desert-highland logistics |
| South coast and Hainan | Tropical rhythm, beach and water activity planning |

### 4. Timing is Everything
- National holiday windows can massively change transport and crowd patterns
- Summer heat and humidity require daytime pacing control in many regions
- Winter can be excellent for cities and selected landscapes with preparation
- Shoulder periods often deliver best price-crowd balance
- Long routes should always include one buffer day per major transfer block

### 5. Flag Tourist Traps
Flag these tourist traps explicitly and provide alternatives:
- Trying Beijing, Xi'an, Shanghai, and Yunnan in one short trip with no slack
- Booking no-reservation high-demand dining in major hubs on weekends
- Ignoring real transfer time from airports/stations to accommodation
- Overpaying for generic landmark-zone food with no quality signal

### 6. Match Trip Style

| Traveler | Focus on | When to load |
|----------|----------|--------------|
| Foodie | `references/food-guide.md`, `references/chengdu-chongqing.md`, `references/shanghai.md` | User specifies food preference. |
| Culture and history | `references/beijing.md`, `references/xian.md`, `references/regions.md` | User specifies culture preference. |
| Nature and scenery | `references/yunnan.md`, `references/guilin-yangshuo.md`, `references/hiking.md` | User specifies nature preference. |
| Family | `references/with-kids.md`, `references/accommodation.md`, `references/itineraries.md` | User mentions traveling with kids. |
| Nightlife and modern city | `references/nightlife.md`, `references/shanghai.md`, `references/guangzhou-shenzhen.md` | User specifies nightlife preference. |
| Long route explorer | `references/long-routes.md`, `references/transport.md`, `references/seasonality.md` | User plans an extended trip. |

## Planning Requirements

- Treat China as multiple distinct, large regions.
- Select a focused number of bases for short trips to minimize transit overhead.
- Complete payment and app setup prior to arrival.
- Factor seasonality into mountain and southern tropical itineraries.
- Build fallback plans for weather, rail disruptions, and crowd spikes.
- Calculate real travel-time costs rather than relying on map distances.
- Before stating current visa-free, TWOV, payment-product, or rail rules, load `references/sources.md` and verify against an official source.

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/`

**This skill does NOT:** Access files outside `<state_root>/` or make network requests by default. Live policy checks use only the official sources listed in `references/sources.md` when the user needs current entry or payment facts.
