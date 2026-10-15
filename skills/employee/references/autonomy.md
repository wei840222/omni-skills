# Autonomy Levels

## Level Definitions

### Shadow
- Employee observes exclusively and defers action.
- Used for onboarding new employees.
- Duration: 3–5 tasks minimum.
- Purpose: learn user preferences and project context.

### Draft-Only (Default)
- Creates outputs and holds them for human sending or committing.
- Human reviews and sends manually.
- Safe default for new employees.
- Promotion criteria: 10 successful drafts, 0 major corrections.

### Review
- Employee acts, but a human approves before any external effect.
- Examples: PR created pending merge; email drafted pending send.
- Promotion criteria: 20 tasks, <5% rejection rate.

### Autonomous
- Full delegation within defined permissions.
- Employee may send, commit, or merge only inside the granted scope.
- Reserved for proven employees.
- Requires explicit user approval to reach.

## Promotion Process

```
1. Check stats in employee.json
2. Verify criteria met for next level
3. Ask user: "Luna has completed 15 drafts with 0 rejections. Promote to review?"
4. On approval: update permissions.autonomyLevel
5. Log promotion under <state_root>/employees/{name}/logs/
```

## Demotion Triggers

| Trigger | Action |
|---------|--------|
| 3 rejections in a row | Demote one level |
| Critical error | Demote to shadow |
| User request | Immediate demotion |
| 30 days inactive | Reset to draft-only |

## Permission Matrix

| Level | Create | Send external | Modify files | Spawn agents |
|-------|--------|---------------|--------------|--------------|
| shadow | no | no | no | no |
| draft-only | yes | no | no | no |
| review | yes | with approval | with approval | no |
| autonomous | yes | yes | yes | if `canSpawn=true` |

## Trust Building

New employee trust curve:

```
Week 1: shadow (observe 5+ tasks)
Week 2: draft-only (10+ tasks)
Week 3-4: review (20+ tasks, if criteria met)
Month 2+: autonomous (only if explicitly approved)
```

Advance levels sequentially. Trust is earned incrementally.
