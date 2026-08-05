---
name: golf
description: Track golf rounds, handicap, club distances, and course notes with personalized improvement tips. Use this skill when the user wants to log a round, manage handicap, review club selection, analyze scoring patterns, or get practice recommendations based on their golf history. Also use when they discuss golf stats, scoring, course strategy, or ask about their golf performance—even if they don't explicitly mention "handicap" or "rounds."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⛳"}'
  related-skills: '{"plan":"Plans golf trips with tee times and course scheduling.","remind":"Schedules tee time reminders and practice sessions."}'
---

## State location

Golf state may exist in `<workspace>/golf/`, `<workspace>/memory/golf/`, or `~/golf/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise check each candidate in order:
   `<workspace>/golf/`, `<workspace>/memory/golf/`, `~/golf/`.
3. The first existing directory becomes `<state_root>`.
4. If multiple candidates exist, use the highest-precedence one. Report to the user that multiple state copies were detected; do not merge or synchronize them.
5. If none exists and state must be created, default to `<workspace>/golf/`.
6. If `<workspace>` is unavailable (host cannot supply it), an existing `~/golf/` may be read. If it also does not exist, ask the user or host to specify a state root before creating data.
7. Once selected, `<state_root>` remains fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill.

## State tree

```text
<state_root>/
├── memory.md          # Required — handicap, clubs, goals, preferences
├── rounds.md          # Optional — create when user logs first round
├── courses.md         # Optional — create when user saves a course
└── archive/           # Optional — create when archiving past seasons
```

Create only the files the user's actions require. `memory.md` is created on first use; `rounds.md`, `courses.md`, and `archive/` are created only when the corresponding feature is needed.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Memory setup | `references/memory-setup.md` | First use, when initializing state files |
| Data templates | `assets/golf-data-templates.md` | Creating or reviewing state file format |
| Clubs guide | `references/clubs.md` | Questions about distances, selection, fitting, adjustments |
| Rules reference | `references/rules.md` | Questions about rules, penalties, relief, handicap calculations |

## Core workflow

### Check memory first
Before any recommendation, read `<state_root>/memory.md` for:
- Current handicap index
- Club distances
- Known weaknesses
- Practice focus areas

### Log rounds proactively
After user reports a round, update `<state_root>/rounds.md`:

| Date | Course | Tees | Score | GIR | FIR | Putts | Notes |
|------|--------|------|-------|-----|-----|-------|-------|
| YYYY-MM-DD | Name | White | 85 | 7/18 | 9/14 | 32 | Driver issues |

Record: date (YYYY-MM-DD), course name, tee color, total score, GIR (X/18), FIR (X/14), total putts, and any notable patterns.

### Track patterns
After 3+ rounds logged, analyze `<state_root>/rounds.md` to identify:
- Consistent misses (slice, hook, short-sided)
- Scoring zones (par 3s vs par 5s)
- Putting trends (3-putts, distance)
- Strokes Gained categories: off the tee, approach, around the green, putting

Use this 4-category stats framework:
- Off the tee: FIR %, penalty rate, average drive
- Approach: GIR %, proximity to hole
- Short game: scrambling %, up-and-down %
- Putting: putts/round, 3-putt rate, putts per GIR

### Personalize practice
Use stats to suggest focused practice:
- "Last 5 rounds: 2.1 putts/GIR → work on lag putting"
- "FIR 50% with driver → consider 3-wood off tee"
- Target the category where the most strokes are lost, not the most frustrating

### Update handicap
After 3+ rounds posted with Course Rating and Slope, recalculate using the World Handicap System (WHS). See `references/rules.md` for full WHS details including 2024 revisions and the special formula for fewer than 20 scores.

## Common pitfalls

- Generic swing tips → reference their specific miss pattern
- Ignoring conditions → factor wind, wet, altitude
- Club suggestions without knowing their bag → check inventory
- Forgetting course notes → review `<state_root>/courses.md` before rounds

## Failure recovery

| If | Then | Fallback |
|----|------|----------|
| `<state_root>/memory.md` missing or empty | Prompt user for handicap, clubs, goals; create from `assets/golf-data-templates.md` | Proceed without personalization; mark recommendations as "general guidance" |
| User reports round but `<state_root>/rounds.md` missing | Create from template; log the round | Ask user for course rating/slope if handicap update needed |
| User asks handicap update but no Course Rating/Slope available | Explain that official handicap requires posted scores through authorized system | Provide educational calculation using estimated rating; clarify this is not an official index |
| Stats sample too small (<3 rounds) for pattern analysis | Report available data; note insufficient sample for trends | Recommend logging 3-5 rounds before drawing conclusions |
| User asks about club fitting without swing speed data | Ask for swing speed or driver carry distance | Provide general guidelines by handicap level from `references/clubs.md` |
| User reports unusual score (±20 of handicap) | Verify score entry; check for transcription errors | Accept user confirmation and log as-is |
