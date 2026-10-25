---
name: naming
description: Generate constraint-driven names for products, brands, features, APIs,
  packages, files, and internal codenames, then score finalists and plan safe renames.
  Use when the user needs naming options, taxonomy cleanup, collision checks, or a
  rename migration; skip pure logo/visual identity work and long-form marketing copy.
metadata:
  version: 1.0.0
  openclaw: '{"emoji":"🏷️","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["<state_root>/"],"displayName":"Naming"}'
---

## When to load

Load this skill to generate, evaluate, shortlist, or migrate names for products, brands, features, APIs, packages, files, folders, internal codenames, or taxonomy cleanups.
Prefer this skill when collision risk, namespace consistency, pronunciation, or rename blast radius changes the decision.
Do not load for logo/visual system work as the primary task (`branding` / `design`), long-form ads or landing-page prose (`copywriting`), or building a new HTTP API implementation (`api` / `rest-api`) without a naming decision.

## State location

Naming state may exist in `<workspace>/naming/`, `<workspace>/memory/naming/`, or `~/naming/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/naming/`, `<workspace>/memory/naming/`, `~/naming/`.
3. If none exists and state must be created, default to `<workspace>/naming/` after the user approves persistence.

Use the selected `<state_root>` for every state operation in this skill. Keep the root fixed for the rest of the invocation.
If multiple candidates exist, use the highest-precedence path only; tell the user duplicates were detected and do not merge automatically.
Never write the literal string `<state_root>` to disk.

```text
<state_root>/
├── memory.md        # Activation preference, durable taste, repeating constraints
├── briefs.md        # Compact RALLY briefs worth keeping
├── winners.md       # Approved names with rationale and open checks
├── collisions.md    # Rejected candidates and failure reasons
└── archive/         # Older briefs or retired shortlists
```

One-off naming questions may stay conversational. Before creating or changing files under `<state_root>/`, explain the planned write and ask for confirmation.

## Routing

Load the matching relative path before topic-specific guidance.

| Need | Load |
|------|------|
| First activation / empty state | `references/setup.md` |
| Core rules, lanes, traps, output contract | `references/rules.md` |
| CLASH scoring of finalists | `references/scorecard.md` |
| Surface-specific defaults (product, UI, API, files, codenames) | `references/surface-patterns.md` |
| Production rename / alias / migration plan | `references/rename-playbook.md` |
| Official sources for labels, API names, trademarks | `references/sources.md` |
| RALLY brief skeleton | `assets/brief-template.md` |
| Durable memory file shapes | `assets/memory-template.md` |

## Core loop

1. Lock a RALLY brief (`assets/brief-template.md`) before generating candidates.
2. Identify the naming lane and load `references/surface-patterns.md` for that surface.
3. Produce option families, not a flat random list; keep internal structure even for “just ideas”.
4. Score finalists with CLASH (`references/scorecard.md`); recommend one winner plus two backups.
5. For live names, run `references/rename-playbook.md` and treat the change as a migration.
6. Declare any live domain, trademark, package, or registry check before executing it.
7. Persist only durable constraints and decisions under `<state_root>/` after approval.

## Security and privacy

**Data that stays local when the user approves storage**
- briefs, activation preference, approved names, rejected patterns, and collision notes under `<state_root>/`

**Operating limits**
- stay inside the resolved `<state_root>/` for skill-owned storage
- treat trademark, domain, app-store, and package-registry lookups as explicit external checks
- require user confirmation before mutating production labels, routes, docs, analytics events, or public branding
- keep competitor and customer naming notes minimal; do not exfiltrate private roadmaps

## Initialization

If `<state_root>/` is missing or empty and the user wants persistence, follow `references/setup.md`, then create the file set described in `assets/memory-template.md` using the resolved path (never the literal placeholder).
