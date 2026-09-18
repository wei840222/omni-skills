# Memory Template - Decide

Create `<state_root>/memory.md` with this structure:

```markdown
# Decide Memory

## Status
status: ongoing
version: 1.0.1
last: YYYY-MM-DD
integration: pending | complete | paused | never_ask

## Activation Rules
- When this skill should step in for consequential branching choices
- Which decision families always deserve a deliberate review

## Always Ask
- Decision categories requiring explicit fresh approval before becoming autonomous
- High-stakes exceptions and no-go areas

## Required Components
- The minimum context needed before a major decision can be reused
- Signals that make the context incomplete

## Confirmed Defaults
- Component patterns the user explicitly approved as defaults
- The choice that should be proposed or applied when the pattern fully matches

## Domain Overrides
- Project-, client-, or domain-specific rules that beat the generic default

## Notes
- Durable decision guidance
- Warnings about overgeneralization
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Decision model still evolving | Ask often and keep logging |
| `complete` | Stable decision baseline exists | Reuse only clearly validated patterns |
| `paused` | User wants less setup friction | Ask only when a real branching choice appears |
| `never_ask` | User does not want setup prompts | Keep setup closed unless requested |

## Local Files to Initialize

```bash
mkdir -p <state_root>/domains
touch <state_root>/{memory.md,decisions.md}
```

## Template for `decisions.md`

```markdown
# Decision Log

- YYYY-MM-DD: [domain] question
  - Components: client=__, surface=__, project=__, constraints=__
  - Options: option A | option B | option C
  - Chosen: __
  - Why: __
  - Confidence: missing | partial | close | validated | confirmed-default
  - Outcome: accepted | corrected | pending
```

## Rules

- Keep durable decision policy in `<state_root>/memory.md`.
- Keep individual decision records in `<state_root>/decisions.md`.
- Keep domain-specific component models and exceptions in `<state_root>/domains/`.
- Persist only safe, non-sensitive context placeholders (e.g., `<api_key_hidden>`).
