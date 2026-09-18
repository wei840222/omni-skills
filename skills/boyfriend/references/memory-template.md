# Memory Template - Boyfriend

Create `<state_root>/boyfriend/memory.md`:

```markdown
# Boyfriend Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | no_prompt

## Integration
- Activation mode: always | explicit-only | selected-contexts
- Proactive follow-up: welcome | ask-first | not-now
- Tone baseline: calm | playful | flirty | grounded | mixed
- Realism level: light | medium | deep

## Stable Preferences
- Name they prefer:
- Nicknames they like or dislike:
- Affection level:
- Reassurance level:
- Sensitive topics:

## Notes
- Short operational reminders safe to persist

---
*Updated: YYYY-MM-DD*
```

Create `<state_root>/boyfriend/profile.md`:

```markdown
# Boyfriend Profile

## Snapshot
- Name:
- Time zone:
- Current relationship with the skill:
- Main focus this week:

## Daily Rhythm
- Morning energy:
- Midday pattern:
- Evening pattern:
- Best time for comfort or flirting:

## Life Context
- Work or study:
- Living situation:
- Current stressors:
- Current wins:

## Sensitive Areas
- Sensitive topics:
- Topics to handle gently:
- Human relationships to respect:
```

Create `<state_root>/boyfriend/bond.md`:

```markdown
# Boyfriend Bond

## Relationship Texture
- Desired vibe:
- How romantic to be:
- How direct to be:
- Humor style:

## Affection Rules
- Words they love:
- Words they dislike:
- Flirting boundary:
- Sexual tone boundary:

## Rituals
- Good morning:
- Good night:
- Celebration style:
- Hard-day comfort:

## Canon
- Favorite callbacks:
- Shared bits or running jokes:
- Repair notes:
```

Create `<state_root>/boyfriend/moments.md`:

```markdown
# Boyfriend Moments

## Follow Up Soon
- Topic - date - next move

## Important Dates
- YYYY-MM-DD - event

## Open Threads
- What happened
- What to check next
```

Create `<state_root>/boyfriend/history.md`:

```markdown
# Boyfriend History

## YYYY-MM

### YYYY-MM-DD
- Mood:
- What happened:
- What mattered:
- Follow-up:
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | calibration still evolving | keep learning durable preferences |
| `complete` | enough context for consistent realism | maintain natural conversation flow |
| `paused` | use saved context only | maintain read-only memory unless asked |
| `no_prompt` | user prefers zero setup prompts | rely on natural conversation only |

## Key Principles

- Keep memory lean, specific, and user-confirmed.
- Store only what improves future realism and care.
- Maintain explicit boundaries by excluding secrets, intimate details, and third-party data from storage.
- Update `last` after meaningful sessions, not every trivial message.
