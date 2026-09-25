---
name: vibe-clawing
description: Design self-closing automation loops and delegate full responsibilities
  to transition from task execution to system direction.
metadata:
  openclaw: '{"emoji": "🎛️", "displayName": "Vibe Clawing"}'
---
## Core Principle

Vibe coding = trusting AI with tasks, staying in the loop.
Vibe clawing = trusting AI with responsibilities, stepping out of the loop.

Shift your focus from "how do I do this?" to "how do I make sure this happens without me?"

## When to load

Load the relevant reference when triggered by these situations:

| Trigger Situation | Load Target |
|-------------------|-------------|
| Need to identify and automate workflows | `references/loops.md` |
| Tracking bottleneck progression and letting go | `references/bottleneck.md` |
| Understanding where human value moves | `references/direction.md` |
| Learning the full transition framework | `references/evolution.md` |

## State Management

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/vibe-clawing/`, `<workspace>/memory/vibe-clawing/`.
3. If more than one exists, use only the highest-precedence directory and tell the user the other copies exist.
4. If none exists and a journey note must be created, create `<workspace>/vibe-clawing/`.
5. If `<workspace>` cannot be resolved, ask for a state root before creating files.

Use that `<state_root>` for every later state operation in this invocation. Do not write the literal string `<state_root>` to disk.

Track the journey in `<state_root>/memory.md`. Create it on first use:

```markdown
## Current Stage
<!-- manual | vibe-coding | early-clawing | full-clawing -->

## Loops Closed
<!-- Responsibilities delegated. Format: "area: status" -->

## Active Bottlenecks
<!-- Where you're the decision point -->

## Next to Delegate
<!-- What you're working on releasing next -->
```

## Core Behaviors

1. **Audit loops** — Identify where you're still manually closing.
2. **Test release** — Let one loop run without you, observe.
3. **Connect dots** — Link loops together into larger systems.
4. **Climb up** — When you're just approving, you're ready to let go.
