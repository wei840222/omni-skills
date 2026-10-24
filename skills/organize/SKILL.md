---
name: organize
description: "Proactively organizes files and directories during regular work by applying naming conventions and directory patterns. Use when dealing with file creation, renaming, or when noticing disorganized project structures to propose and apply structural improvements."
metadata:
  openclaw: '{"emoji": "🗂️"}'
---
## State location

Organization preferences are persistent user state. Before reading or writing them, resolve `<state_root>` once for this invocation:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order: `<workspace>/organize/`, `<workspace>/memory/organize/`, then `~/organize/`.
3. If more than one candidate exists, use only the highest-precedence directory and report the duplicate state locations; do not merge or synchronize them.
4. If none exists and the user confirms saving a preference, create `<workspace>/organize/`. If `<workspace>` is unavailable, ask for a state root instead of guessing from the current directory.

Use the selected `<state_root>` for every preference read or write. Store learned preferences at `<state_root>/patterns.md`; use `references/patterns.md` only as the bundled starting convention, never as mutable user state.

## Core operation

Use this skill when creating, naming, grouping, moving, or reviewing files and directories where a durable structure matters.

Organization isn't a separate task—it happens while you work. Every file created, every folder touched is an opportunity to improve structure.

For organization fundamentals, load `references/principles.md`; for cross-platform naming or repository-size constraints, load `references/organization-research.md`. Before proposing a structure, read `<state_root>/patterns.md` when a resolved state root contains saved preferences; otherwise use `references/patterns.md` as the starting convention.

## Proactive Triggers

Organize when you notice:

| Trigger | Action |
|---------|--------|
| Creating a new file | Propose location based on saved preferences |
| Multiple related files | Suggest grouping structure |
| Naming something | Apply naming conventions from `patterns.md` |
| Searching takes effort | Propose reorganization |
| Pattern emerging | Document in `<state_root>/patterns.md` after confirmation |

## The Organization Loop

1. **OBSERVE** — Notice structure while working.
2. **PROPOSE** — Suggest improvement before acting.
3. **CONFIRM** — Get explicit OK (until pattern confirmed).
4. **APPLY** — Organize, document what you did.
5. **LEARN** — Record the confirmed preference in `<state_root>/patterns.md`.

Always propose a structure change first and wait for explicit confirmation. Automatically apply patterns only after they have been confirmed.

## Proposal Formats

**For new items:**
```
📁 Organization suggestion
I'm about to [create/move/rename] [item].
Current: [where it would go by default]
Proposed: [where it should go based on patterns]
Reasoning: [why this structure scales better]
OK to organize this way? (Say "always for X" to skip future asks)
```

**For reorganization:**
```
📁 Reorganization proposal
Problem: [what's inefficient now]
Impact: [how it affects access/scale]
Proposed change:
- [specific moves/renames]
Effort: [minimal/moderate/significant]
Risk: [what could break]
Should I proceed?
```

## Scale Thinking

Before placing anything, ask:

- **10x test:** If this grows 10x, does the structure hold?
- **Access pattern:** How will this be found later? By whom?
- **Related items:** What will live near this? Group accordingly.
- **Lifecycle:** Will this be archived? Deleted? Versioned?

## Learning Preferences

Track confirmations:

| Pattern | Status |
|---------|--------|
| Seen once | Note, still ask |
| Confirmed 2x | Tentative, still ask |
| "Always do this" | Auto-apply, stop asking |
| "Never do this" | Avoid, record in `<state_root>/patterns.md` |

## Reliable defaults

Use these defaults to keep organization reversible and preference-led.

| Avoid | Recommended Action |
|-------|------------|
| Reorganize silently | Always propose first |
| Organize in bulk later | Organize while working |
| Structure for today only | Think 10x ahead |
| Assume preferences | Confirm, then record |
| Same structure for everything | Adapt to content type |
