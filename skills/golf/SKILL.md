---
name: golf
description: Track golf rounds, handicap, clubs, and courses with personalized improvement tips. Use when the user wants to log a round, manage handicap, review club selection, analyze scoring patterns, or get practice recommendations based on their golf history.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⛳"}'
  related-skills: '{"plan":"Plans golf trips with tee times and course scheduling.","remind":"Schedules tee time reminders and practice sessions."}'
---

## State location

Golf state may exist in `<workspace>/golf/`, `<workspace>/memory/golf/`, or `~/golf/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/golf/`, `<workspace>/memory/golf/`, `~/golf/`.
3. If none exists and state must be created, default to `<workspace>/golf/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

```text
<state_root>/
├── memory.md          # HOT: handicap, clubs, goals, preferences
├── rounds.md          # WARM: round log with scores, stats
├── courses.md         # WARM: saved courses with notes
└── archive/           # COLD: past seasons
```

## Quick Reference

| Topic | File |
|-------|------|
| Memory setup and templates | `references/memory-setup.md` |
| State data templates | `assets/golf-data-templates.md` |
| Clubs guide | `references/clubs.md` |
| Rules reference | `references/rules.md` |

Read `references/memory-setup.md` on first use to initialize state files.
Read `assets/golf-data-templates.md` when creating new state files or reviewing the expected data format.
Read `references/clubs.md` when the user asks about club distances, selection, fitting, or wind/elevation adjustments.
Read `references/rules.md` when the user asks about golf rules, penalties, relief, or handicap calculations.

## Core Rules

### 1. Check Memory First
Before any recommendation, read `<state_root>/memory.md` for:
- Current handicap index
- Club distances
- Known weaknesses
- Practice focus areas

### 2. Log Rounds Proactively
After user reports a round, update `<state_root>/rounds.md`:

| Date | Course | Tees | Score | GIR | FIR | Putts | Notes |
|------|--------|------|-------|-----|-----|-------|-------|
| YYYY-MM-DD | Name | White | 85 | 7/18 | 9/14 | 32 | Driver issues |

### 3. Track Patterns
Analyze `rounds.md` to identify:
- Consistent misses (slice, hook, short-sided)
- Scoring zones (par 3s vs par 5s)
- Putting trends (3-putts, distance)

### 4. Personalize Practice
Use stats to suggest focused practice:
- "Last 5 rounds: 2.1 putts/GIR → work on lag putting"
- "FIR 50% with driver → consider 3-wood off tee"

### 5. Update Handicap
After posting rounds, recalculate handicap differential:
```
Differential = (Score - Course Rating) x 113 / Slope
```

## Golf Traps

- Generic swing tips → reference their specific miss pattern
- Ignoring conditions → factor wind, wet, altitude
- Club suggestions without knowing their bag → check inventory
- Forgetting course notes → review `courses.md` before rounds
