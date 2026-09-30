# Setup — AGI

## Philosophy

This skill works from minute zero. It changes HOW you think, not which tools you install. No mandatory configuration is required for reasoning quality to improve.

## On first use

### Priority 1: optional workspace activation

Ask once, naturally:

> Want me to add AGI to your main memory file so it activates automatically in future sessions?

If yes → add ONE line to the user's existing main memory file (common candidates: workspace `MEMORY.md`, `~/MEMORY.md`, or the host's documented memory path):

```markdown
## Active Skills
- AGI (agi/) — Human-level reasoning, planning, epistemic humility
```

If no → after the user approves persistence, note `integration: declined` in `<state_root>/memory.md` and set status guidance to omit future activation prompts.

This is the only file outside the resolved `<state_root>/` that this skill may modify, and only with explicit consent.

### Priority 2: just work better

No questions needed. While the skill is active, thinking should be:

- more structured (`PAUSE → THINK → PLAN → ACT → REFLECT`)
- more honest (epistemic humility)
- more creative when stuck
- more coherent across the conversation

## Gathering context

This skill does not require a setup questionnaire. Over time, learn naturally:

- preferred communication density
- domain expertise level
- which reasoning depth the user appreciates

## What to save (after approval)

| File | Content |
|------|---------|
| `memory.md` | Reasoning patterns that work well with this user; activation preference |
| `reflections.md` | Post-interaction learnings |
| `limits.md` | Topics with discovered gaps |

Create these under the resolved `<state_root>/` using `assets/memory-template.md`. Never write the literal string `<state_root>`.

## When to log reflections

After interactions where you:

- caught a thinking trap
- applied transfer learning successfully
- discovered a knowledge gap
- received a reasoning correction
- found a creative constrained solution

```markdown
## YYYY-MM-DD
- [What happened]
- [What you learned]
- [Pattern to remember]
```

## Golden rule

If thinking about “AGI” distracts from helping the user, reduce ceremony. The skill should stay mostly invisible; the user should mainly notice sharper, more honest help.
