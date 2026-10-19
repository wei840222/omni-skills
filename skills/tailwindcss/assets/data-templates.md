# Memory Template — Tailwind CSS

Create `<state_root>/memory.md` with this structure (only after State location
resolution and consent):

```markdown
# Tailwind CSS Memory

## Status
status: ongoing
last: YYYY-MM-DD

## Context
<!-- Major and integration, framework, monorepo or single app -->
<!-- Design system in play: own tokens, a UI kit, an imported token pipeline -->

## Pain Points
<!-- Issues they have hit: missing styles, cascade fights, upgrade blockers -->

## Preferences
<!-- Banned techniques, token promotion threshold, tolerance for ! and arbitrary values -->
<!-- Explanation depth: mechanism first vs fix only -->

---
*Updated: YYYY-MM-DD*
```

Also create `<state_root>/config.yaml` when preferences must persist, using the
keys from the Configuration table in `SKILL.md` (`tailwind_version`,
`build_integration`, `dark_mode_strategy`, `component_syntax`, `merge_helper`,
`rem_base`, `token_threshold`, `text_direction`, `a11y_target`).

## Status Values

| Value | Meaning |
|-------|---------|
| `ongoing` | Still learning their stack and conventions |
| `complete` | Know their setup and design system well |
