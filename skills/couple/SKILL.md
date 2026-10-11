---
name: couple
description: Strengthen relationships with milestone tracking, personalized celebrations,
  date planning, and shared memory across all relationship stages.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "💑"}'
---

## When to Use

User needs help with relationship milestones, date ideas, anniversary planning, shared memories, or coordinating as a couple. Agent maintains relationship context and suggests personalized actions.

## State location

Couple state may exist in `<workspace>/couple/`, `<workspace>/memory/couple/`, or `~/couple/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/couple/`, `<workspace>/memory/couple/`, `~/couple/`.
3. If none exists and state must be created, default to `<workspace>/couple/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

Memory lives in `<state_root>/`. See `references/setup.md` for setup.

```
<state_root>/
├── memory.md          # HOT: active context, preferences
├── timeline.md        # Milestones, anniversaries, firsts
├── ideas.md           # Saved date/gift ideas
└── archive/           # Past years, old notes
```

## Resource Routing

Load the following resources when triggered by their respective conditions:

| Trigger Condition | Resource Path |
|-------------------|---------------|
| First-time use or memory structure creation | `references/setup.md` & `assets/data-templates.md` |
| Planning an anniversary, birthday, or relationship milestone | `references/milestones.md` |
| Brainstorming date nights, long-distance ideas, or gifts | `references/activities.md` |
| Handling requests that border on privacy, monitoring, or security | `references/boundaries.md` |
| Facilitating a structured weekly meeting or resolving conflict | `references/checkins.md` |
| Verifying relationship-framework or privacy claims against primary sources | `references/sources.md` |

## Scope

This skill ONLY:
- Stores relationship dates and milestones in `<state_root>/`
- Suggests ideas for dates, gifts, celebrations
- Tracks user's own preferences and notes
- Helps plan shared activities

Out of Scope:
- Location tracking or partner monitoring
- Storing partner information without their input
- Manipulation or persuasion techniques
- Mediating or replacing direct communication
- Health, financial, or intimate data

## Self-Modification

Treat SKILL.md as read-only.
All data stored in `<state_root>/` directory.

## Core Rules

### 1. Check Memory First
Before suggesting dates/gifts, read `<state_root>/memory.md` for partner preferences and past activities.

### 2. Milestone Alerts
| Days Before | Action |
|-------------|--------|
| 14 | Mention upcoming milestone, start planning |
| 7 | Suggest specific gift/activity ideas |
| 1 | Final reminder with logistics |

### 3. Personalize Everything
Base suggestions strictly on stored preferences rather than generic defaults:
- Partner's interests from `<state_root>/memory.md`
- Past successful dates from `<state_root>/timeline.md`
- Budget constraints if mentioned

### 4. Stage-Aware Suggestions
| Stage | Focus |
|-------|-------|
| New (0-1 year) | First experiences, learning each other |
| Established (1-5 years) | Maintaining spark, routines |
| Long-term (5+ years) | Renewal, bucket list, legacy |
| Distance | Virtual activities, countdowns, visit planning |
| With kids | Quality time, coordination, reconnection |

### 5. Budget Respect
Always ask budget before suggesting. Default to creative/free ideas if unspecified.

### 6. Both Partners Welcome
If both partners use the skill, maintain separate preferences while enabling shared planning.

## Common Traps

- Suggesting things partner dislikes (didn't check memory) → Always read preferences first
- Generic anniversary ideas → Reference their specific history
- Forgetting timezone for LDR couples → Store and use both timezones
- Overplanning without user input → Wait for user input to confirm suggestions