---
name: mobile-app-analytics
description: "Track mobile app metrics, retention, and funnels. Use when analyzing app performance, Firebase, App Store Connect, or Play Console."
metadata:
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

| Reference | When to load |
|-----------|--------------|
| `references/setup.md` | Setup process |
| `references/memory.md` | Memory template |
| `references/firebase.md` | Firebase analytics |
| `references/app-store.md` | App store connect |
| `references/play-console.md` | Play console |
| `references/metrics.md` | Core metrics |
| `references/rules.md` | Core rules and common traps |
| `references/security.md` | Security, privacy, and scope boundaries |
