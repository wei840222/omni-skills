# Implementing cycles as skills

When the user wants the designed cycle packaged as its own skill:

```text
cycle-name/
|-- SKILL.md           # Short entry: triggers, sequence, routing
|-- phases/
|   |-- plan.md
|   |-- execute.md
|   `-- verify.md
|-- assets/            # Templates only
`-- references/        # Domain detail loaded on demand
```

Runtime preferences for that named cycle live under the parent `cycle` skill's
resolved `<state_root>/cycles/<name>/` (or the new skill's own state root if it
is promoted to a first-class skill). Never write runtime state into the package.

## SKILL.md skeleton

```markdown
---
name: example-cycle
description: >
  Run the <domain> cycle from <trigger> to <done artifact>. Use when...
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔁"}'
---

# Example cycle

## Workflow
Plan → Execute → Verify → Deliver

## Phases
- **Plan** — input → scoped plan (gated)
- **Execute** — plan → draft output
- **Verify** — draft → pass/fail evidence
- **Deliver** — verified output → published/handed off (gated)

Load `phases/<name>.md` only for the active phase.
```

## State persistence fields

When consent is given, track under `<state_root>/memory.md`:

- **Preferences** — style, tools, constraints
- **Patterns** — what worked on prior runs
- **Boundaries** — out-of-scope actions and failure patterns to sidestep

Use `assets/memory-template.md` shapes. Do not recreate `~/Clawic/data/cycle/`.
