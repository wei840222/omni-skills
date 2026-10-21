# Memory Template — Learn State

Copy structures on first write. Keep entries compact — keywords and dates, not prose.

## `<state_root>/memory.md`

```markdown
# Learn Memory

## Boxes
- projects/<name>.md — when a build-to-learn project is active
- contacts/contacts.md — mentor/tutor/language partner rows owned by this skill
- finances/subscriptions.md — paid course/subscription rows owned by this skill

## Due
| When | What | Why |
|------|------|-----|
| YYYY-MM-DD | plan review | plan_review_weeks |
| YYYY-MM-DD | retention re-test: <topic> | mastery ladder |

## Topics
| Topic | Level | Evidence date | Notes |
|-------|-------|---------------|-------|
| … | recall | YYYY-MM-DD | …

## Error Log
| Date | Item/topic | Conf | Misconception | Next drill |
|------|------------|------|---------------|------------|
| YYYY-MM-DD | … | 4 | … | …

## Sessions
| Date | Minutes | Production artifact | Success rate note |
|------|---------|---------------------|-------------------|
| YYYY-MM-DD | 45 | … | 17/20 |
```

## `<state_root>/config.yaml`

```yaml
weekly_hours: 5
session_minutes: 45
daily_review_limit: 20
retention_target: 0.90
hint_policy: after-attempt
sr_tool: this-skill
practice_bias: balanced
plan_review_weeks: 4
```

## Shared-box write protocol

- One entity, one home; reference by name from learn memory.
- Update/delete only rows this skill wrote (match identity key).
- Name every write and deletion in one line during the session.
- Never store credential values—pointers only.
