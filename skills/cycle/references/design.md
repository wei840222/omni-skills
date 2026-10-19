# Cycle design

Design for reuse. Prefer Shewhart/Deming-style Plan→Do→Check→Act rhythm when
the domain lacks a stronger native sequence; rename phases to domain language.

## Phase contract

Each phase must declare:

- **Name** — verb-led, stable across runs
- **Input** — required artifacts or facts
- **Output** — concrete deliverable
- **Validation** — pass/fail check before handoff
- **Handoff type** — `automatic` | `gated` (needs user) | `conditional`
- **Recovery** — retry same phase, revise inputs, or abort cycle

Keep total phases between 3 and 6. Nested repetition belongs in `loop`, not as
extra top-level phases.

## Design checklist

1. Map the current messy path before inventing an ideal one.
2. Collapse duplicate steps; promote skipped-but-critical steps into gates.
3. Put irreversible actions behind gated handoffs.
4. Define kill criteria (when to abort rather than thrash).
5. Record preferences and boundaries only after consent under `<state_root>/`.

## PDCA mapping (optional scaffold)

| PDCA | Typical cycle role |
|------|--------------------|
| Plan | Scope, constraints, success metrics |
| Do | Execute the primary work |
| Check | Verify against the done-definition |
| Act | Standardize, fix process, or schedule the next run |

Sources for this scaffold: see `references/sources.md`.
