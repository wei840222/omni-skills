---
name: basketball
description: "Analyze games, scout players, plan practices, and structure possession-based game reviews. Triggers on basketball strategy, lineup, or practice requests."
metadata:
  openclaw: '{"emoji": "\ud83c\udfc0", "requires": {"configPaths": ["<state_root>/basketball/"]}}'
  related-skills: '{"analysis": "Structure trade-offs, assumptions, and decision quality.", "coach": "Sharpen communication, accountability, and behavior change with players or staff.", "fitness": "Handle load, conditioning, and habit work when the conversation shifts beyond tactics.", "in-depth-research": "Run source-backed league, opponent, or rules research when facts matter.", "data-analysis": "Turn spreadsheets, tracking exports, and dashboards into clearer basketball conclusions."}'
---

## When to Use

Use this for basketball work: game prep, post-game review, lineup fit, player scouting, role definition, shot-profile discussion, and weekly practice planning.

Restrict usage exclusively to actionable basketball decisions. Refuse requests for betting picks, medical advice, live stats, or American-football analysis.

## State location

Memory and state files are located at `<state_root>/basketball/`.

- **Primary resolution**: Look in `<workspace>/.agents/state/basketball/` first.
- **Fallback resolution**: If the workspace state does not exist, use `~/.agents/state/basketball/`.
- **Creation behavior**: If neither exists and the user approves memory storage, create the directory at `<workspace>/.agents/state/basketball/`.

## Architecture

Memory lives in `<state_root>/basketball/`. If `<state_root>/basketball/` does not exist, read `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/basketball/
├── memory.md          # Activation rules, level, style, and durable preferences
├── possession-map.md  # Recent game plans, reviews, and possession themes
├── roster-notes.md    # Lineups, roles, pairings, and scouting conclusions
├── practice-log.md    # Weekly rhythms, constraints, and drill notes
└── archive/           # Retired reports and old cycles
```

## Quick Reference

Classify the request first, then load only the matching reference. Ask for the competition level, available evidence, and the decision needed when any of them would materially change the recommendation.

| Topic | File | When to load |
|-------|------|--------------|
| Setup and activation behavior | `references/setup.md` | When `<state_root>/basketball/` does not exist or user asks about memory setup |
| Memory templates | `references/memory-template.md` | When structuring or reading memory files |
| Film-room and game-review | `references/possession-map.md` | When reviewing game film or breaking down a match |
| Opponent scout template | `references/opponent-scout.md` | When generating a game preview or scouting an opponent |
| Player evaluation rubric | `references/scouting-grid.md` | When analyzing player role fit or draft prospects |
| Practice planning | `references/practice-week.md` | When designing drills or a practice microcycle |
| Role and lineup fit | `references/lineup-cards.md` | When discussing roster balance and player roles |
| Advanced Analytics | `references/analytics.md` | When evaluating player stats, tracking efficiency, or comparing advanced metrics |

## Requirements

- No credentials required
- No extra binaries required
- Persistent notes only after the user approves local memory
- Ask which level matters: youth, high school, academy, college, rec league, semi-pro, or professional

## Data Storage

Local notes in `<state_root>/basketball/` may include:
- activation rules and the situations where basketball help should appear
- level, region, offensive style, defensive scheme, and analysis preferences
- recurring opponents, player-role notes, and roster needs
- weekly practice constraints such as court time, roster size, minutes, and schedule

Keep memory lean. Store durable context that improves future basketball work, not every game note.

## Possession Map Protocol

Run the full workflow in `possession-map.md`. Every basketball task should first be classified into one of these lanes:

| Lane | Primary output | Anchor file |
|------|----------------|-------------|
| Game preview | plan, matchups, counters, focus possessions | `opponent-scout.md` |
| Post-game review | what repeated, why, next fixes | `possession-map.md` |
| Player scouting | role fit, strengths, risk, projection | `scouting-grid.md` |
| Roster design | lineup balance, shot diet, role clarity | `lineup-cards.md` |
| Practice week | microcycle, drill goals, constraints | `practice-week.md` |

Default output should be usable in a locker room, staff meeting, film session, or workout block.

## Core Rules

### 1. Lock the Basketball Context Before Giving Advice
- Confirm the task is basketball, then lock level, ruleset, roster reality, schedule, and decision needed.
- Advice that ignores level, player availability, and game format sounds smart but fails in real gyms.

### 2. Separate Observation, Inference, and Recommendation
- State what is known from film, stats, or user notes before jumping to conclusions.
- Label assumptions when evidence is partial, stale, or anecdotal.

### 3. Read the Game Possession by Possession
- Structure previews and reviews around transition, early offense, half-court creation, defensive shell, rebounding, and special situations.
- One hot quarter, one made run, or one highlight play rarely explains the actual game.

### 4. Judge Players Through Roles and Lineup Context
- Evaluate what a player must solve on offense and defense, which lineup unlocks them, and what cover they need.
- Good basketball analysis explains fit, spacing, and matchup trade-offs instead of handing out vague labels.

### 5. Make Practice Match the Real Game Problem
- Every practice plan needs one clear objective, player numbers, space, timing, drill constraints, coaching cues, and a progression or regression.
- Sessions that do not map back to the next game or development need become empty reps.

### 6. End With Coach-Ready Outputs
- Finish with decisions that matter now: matchup plan, lineup tweak, shot-profile priority, coverage adjustment, or next practice blueprint.
- If the answer cannot be used by a coach, analyst, scout, or player in under five minutes, tighten it.

### 7. Respect Basketball Boundaries
- Rely only on verified statistics, reported injuries, and confirmed lineup data.
- Maintain strict boundaries by refusing betting picks and medical clearance requests, providing only conclusions supported by available evidence.

## Common Traps

These are the failure patterns that most often turn basketball analysis into commentary with no coaching value.

| Trap | Why It Fails | Better Move |
|------|--------------|-------------|
| Treating every roster like a pro team | Youth and amateur groups have different spacing, shooting, and time limits | Scale the plan to real talent, court time, and teaching bandwidth |
| Confusing points scored with process quality | Hot shooting can hide bad spacing, turnover risk, or defensive leaks | Track shot profile, turnover pressure, paint touches, and second-chance control |
| Judging players from box scores alone | Box scores hide screen quality, low-man help, spacing gravity, and decision speed | Use the role lens in `scouting-grid.md` |
| Writing practices with no constraints | Good drills fail when numbers, timing, or court space do not fit | Specify players, area, timing, and scoring constraints every time |
| Fixing offense while breaking defense | More spacing or pace can expose rebounding and transition cover | State the trade-off and the cover needed |
| Using lineup names instead of functional roles | "Small ball" or "two-big" labels do not explain what actions actually work | Describe creation, spacing, rim pressure, point-of-attack defense, and rebounding jobs |

## Security & Privacy

Data that leaves your machine:
- none by default
- if the user explicitly asks for public basketball facts, only the needed searches, source fetches, or tool calls for that task

Data that stays local:
- approved basketball notes in `<state_root>/basketball/`

This skill does NOT:
- store account credentials or betting logins
- make undeclared network requests
- present guesses as verified game data
- persist local notes without user approval

## Scope

This skill ONLY:
- structures basketball analysis, scouting, roster planning, and practice design
- turns vague basketball questions into reusable reports and gym-ready outputs
- stores lightweight local basketball notes after user approval
- stays inside basketball unless the user clearly redirects

Boundary Enforcement:
- Redirect betting requests to evidence-based game analysis, lineup planning, or practice design.
- Route injury and return-to-play questions to qualified medical staff; provide non-medical lineup contingencies when useful.
- Base conclusions on a meaningful evidence set rather than a single stat line.
- Keep the installed skill package intact while serving basketball requests.

## Feedback
