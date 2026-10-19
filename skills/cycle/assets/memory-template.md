# Cycle memory setup

Create a resolved `<state_root>/` tree only after the user consents to durable
cycle notes. Never write into the skill package. Never recreate
`~/Clawic/data/cycle/`.

## Initial structure

```bash
mkdir -p "<state_root>/{cycles,runs}"
touch "<state_root>/memory.md"
```

Treat `<state_root>` as the path resolved by `SKILL.md` State location rules.
Do not expand the placeholder literally.

## memory.md template

```markdown
# Cycle Memory

## Preferences
<!-- tools, tone, phase naming conventions -->

## Patterns
<!-- what worked across runs -->

## Boundaries
<!-- out-of-scope actions and failure patterns to sidestep -->

## Named cycles
<!-- links or short pointers into cycles/<name>/ -->
```
