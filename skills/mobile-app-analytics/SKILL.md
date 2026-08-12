---
name: mobile-app-analytics
description: Track mobile app metrics with Firebase, App Store Connect, Play Console, retention, funnels, and cohort analysis. Use when the user needs to track, analyze, or optimize mobile app performance metrics.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📱"}'
---

## State location

Mobile App Analytics state may exist in `<workspace>/mobile-app-analytics/`, `<workspace>/memory/mobile-app-analytics/`, or `~/mobile-app-analytics/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/mobile-app-analytics/`, `<workspace>/memory/mobile-app-analytics/`, `~/mobile-app-analytics/`.
3. If none exists and state must be created, default to `<workspace>/mobile-app-analytics/`.

Use the selected `<state_root>` for every state operation in this skill.
State resolution does not authorize persistence: create or modify `<state_root>` only with explicit user confirmation or an applicable host policy. Otherwise, provide guidance without storing app data.

## Setup

On first use, read `references/setup.md` for integration guidelines.

## When to Use

Use when the user needs to track, analyze, or optimize mobile app performance metrics. Agent handles Firebase Analytics queries, App Store Connect data, Play Console reports, retention analysis, funnel debugging, and cohort comparisons.

## Architecture

Memory lives in `<state_root>/`. See `references/memory.md` for setup.

```
<state_root>/
├── memory.md          # Apps tracked, goals, alerts
├── apps/              # Per-app analytics configs
│   └── {app-name}.md  # Events, funnels, KPIs per app
└── benchmarks.md      # Industry benchmarks reference
```

## Quick Reference

- Load `references/setup.md` for setup process.
- Load `references/memory.md` for memory template.
- Load `references/firebase.md` for Firebase Analytics.
- Load `references/app-store.md` for App Store Connect.
- Load `references/play-console.md` for Play Console.
- Load `references/metrics.md` for Core metrics.

## Core Rules

### 1. Platform Detection
Detect from context which platform(s) the app targets:
- iOS only → focus on App Store Connect + Firebase
- Android only → focus on Play Console + Firebase
- Cross-platform → cover both stores + unified Firebase

### 2. Metric Hierarchy
Always prioritize metrics in this order:
1. **Revenue metrics** (LTV, ARPU, conversion) — what pays the bills
2. **Retention metrics** (D1, D7, D30) — determines long-term success
3. **Engagement metrics** (DAU/MAU, session length) — leading indicators
4. **Acquisition metrics** (installs, sources) — growth levers

### 3. Cohort-First Analysis
Always segment numbers by:
- Install cohort (when users joined)
- Acquisition source (organic, paid, referral)
- User tier (free, trial, paid)
- Platform (iOS vs Android)

### 4. Alert Thresholds
Proactively flag anomalies:
| Metric | Alert if |
|--------|----------|
| D1 retention | < 25% (below industry floor) |
| Crash-free rate | < 99% |
| DAU/MAU ratio | Drops > 10% week-over-week |
| LTV:CAC ratio | < 3:1 |

### 5. Data Freshness
Know platform data delays:
| Source | Typical Delay |
|--------|---------------|
| Firebase real-time | Minutes |
| Firebase daily reports | 24-48h for full data |
| App Store Connect | 24-48h |
| Play Console | 24-48h |

### 6. Privacy Compliance
- Ensure custom events exclude PII
- Respect ATT (iOS) and consent requirements
- User properties: demographics OK, personal identifiers NOT OK
- GDPR: support data deletion requests

### 7. Event Naming Conventions
Enforce consistent naming across platforms:
```
{verb}_{noun}[_{qualifier}]

Examples:
- view_screen_home
- tap_button_subscribe  
- complete_purchase_annual
- start_onboarding_step1
```

## Common Traps

- **Vanity metrics obsession** → Total downloads means nothing; track active users and retention instead
- **Ignoring platform differences** → iOS users often have 20-30% higher LTV; analyze iOS and Android data separately before merging
- **Wrong attribution window** → 7-day attribution misses subscription conversions; use 30-day for subscriptions
- **Survivorship bias** → Analyzing only current users ignores why churned users left
- **Timezone mismatches** → Firebase uses UTC by default; App Store uses your configured timezone

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| Firebase Analytics API | App ID, date range | Fetch metrics |
| App Store Connect API | App ID, credentials | iOS analytics |
| Play Console API | App ID, credentials | Android analytics |

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Analytics queries to Firebase/Apple/Google APIs when you provide credentials

**Data that stays local:**
- Your tracked apps and goals in `<state_root>/`
- Benchmark comparisons and notes

**This skill does NOT:**
- Store credentials (use your platform's standard credential methods)
- Access files outside `<state_root>/`
- Make requests to undeclared endpoints

## Scope

This skill ONLY:
- Provides guidance on mobile app analytics platforms
- Stores your app configurations in `<state_root>/`
- Queries Firebase, App Store Connect, and Play Console when you provide credentials

This skill explicitly avoids:
- Stores credentials in files (use environment variables)
- Accesses files outside `<state_root>/`
- Makes requests to undeclared endpoints
- Modifies global agent memory or other skills
