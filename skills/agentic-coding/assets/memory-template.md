# Memory Template - Agentic Coding

Create files under the resolved `<state_root>/` only after State location
resolution and user consent for durable writes. Never write the literal string
`<state_root>` to disk.

## memory.md Template

Create `<state_root>/memory.md` with this structure:

```markdown
# Agentic Coding Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending

## Working Context
<!-- Active repositories and stacks -->
<!-- Typical task types and risk profile -->

## Contract Preferences
<!-- How this user defines objective, constraints, and non-goals -->
<!-- Preferred acceptance style: tests, logs, screenshots, benchmarks -->

## Validation Patterns
<!-- Commands and checks that are trusted in this workspace -->
<!-- What counts as enough evidence before handoff -->

## Repeated Traps
<!-- Recurring failure modes worth preventing early -->

## Notes
<!-- Stable operational observations only -->

---
*Updated: YYYY-MM-DD*
```

## contracts.md Template

Create `<state_root>/contracts.md`:

```markdown
# Active Contracts

## YYYY-MM-DD - [Task Name]
Objective: ...
Acceptance: ...
Non-goals: ...
Constraints: ...
Status: drafted | active | verified | blocked
```

## evidence.md Template

Create `<state_root>/evidence.md`:

```markdown
# Validation Evidence

## YYYY-MM-DD - [Task Name]
Before: [failing test/log/reproduction]
After: [passing test/log/reproduction]
Residual risk: [low/medium/high + why]
```

## handoffs.md Template

Create `<state_root>/handoffs.md`:

```markdown
# Handoffs

## YYYY-MM-DD - [Task Name]
Changes: ...
Files touched: ...
Validation run: ...
Rollback: ...
Next action: ...
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Default | Keep collecting patterns |
| `complete` | Context is stable | Use memory mostly for refresh |
| `paused` | User wants minimal process | Keep only essential checks |
| `opt_out_ask` | User rejected integration prompts | Maintain current workflow silently |
