# Kanban Data Templates

## Memory Template (`memory.md`)

```markdown
# Kanban Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | never_ask

## Integration
- Activation mode: always | explicit-only | selected-projects
- Default board mode: workspace-local | home-shared
- Default lane model: basic | custom

## Context
- Stable preferences learned from user behavior
- Planning cadence and review style

## Notes
- Operational reminders safe to persist

---
*Updated: YYYY-MM-DD*
```

## Index Template (`index.md`)

```markdown
# Kanban Index

## Projects
| project_id | aliases | workspace_root | board_mode | board_path | rules_path | log_path | last_used |
|------------|---------|----------------|------------|------------|------------|----------|-----------|
| api-core | backend, core-api | /abs/path/api-core | workspace-local | /abs/path/api-core/.kanban/board.md | /abs/path/api-core/.kanban/rules.md | /abs/path/api-core/.kanban/log.md | YYYY-MM-DD |
| marketing | growth | - | home-shared | <state_root>/projects/marketing/board.md | <state_root>/projects/marketing/rules.md | <state_root>/projects/marketing/log.md | YYYY-MM-DD |

## Resolution Order
1. exact workspace_root match
2. alias match from user message
3. explicit project_id in request
4. fallback to last_used project with confirmation
```

## Board Template (`board.md`)

```markdown
# {Project Name} Kanban Board

## Meta
project_id: {project-id}
board_version: 1.0
updated: YYYY-MM-DD HH:MM
lane_model: custom | basic

## Lanes
- backlog
- ready
- in-progress
- blocked
- review
- done

## Cards
| id | title | state | priority | owner | due | depends_on | updated |
|----|-------|-------|----------|-------|-----|------------|---------|
| KB-001 | Define API scope | backlog | P1 | unassigned | - | - | YYYY-MM-DD |

## WIP Limits
- in-progress: 3
- review: 5

## Rules Snapshot
- Use `rules.md` as source of truth for state mapping and custom policies.

## Notes
- Optional short notes for this board only.
```

## Rules Template (`rules.md`)

```markdown
# {Project Name} Kanban Rules

## State Mapping
| lane_label | canonical_state |
|------------|-----------------|
| backlog | backlog |
| ready | ready |
| in-progress | in-progress |
| blocked | blocked |
| review | review |
| done | done |

## Prioritization
1. blocked dependency with highest downstream impact
2. ready cards with P0/P1
3. due-date pressure
4. age in queue

## Policies
- Create card IDs with `KB-<number>` and do not reuse IDs.
- Any done move must include completion evidence in `log.md`.
- Ensure blocked cards are not moved unless blocker is resolved.
```

## Log Template (`log.md`)

```markdown
# {Project Name} Kanban Log

| timestamp | action | card_id | from_state | to_state | actor | note |
|-----------|--------|---------|------------|----------|-------|------|
| YYYY-MM-DD HH:MM | create | KB-001 | - | backlog | agent | initial setup |
```
