---
name: reverse-engineering
description: Reverse engineer undocumented systems. Map interfaces, test hypotheses,
  and create evidence-backed behavioral models.
metadata:
  openclaw: '{"emoji": "🧩", "requires": {"bins": []}}'
---

## When to load

Load this skill when asked to analyze opaque, undocumented, legacy, or broken systems (binaries, APIs, file formats, protocols). Use progressive disclosure to load specific `references/` guides on demand rather than loading all documentation upfront.

## Architecture

Memory lives in `<state_root>/reverse-engineering/`. If `<state_root>/reverse-engineering/` does not exist, run `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/reverse-engineering/
├── memory.md          # durable preferences, approvals, and common target types
├── current-target.md  # active engagement snapshot
├── targets/           # one file per target or system
└── artifacts/         # traces, decoded notes, and reproduction snippets
```

## Quick Reference

Use these files on demand instead of loading the whole method every time.

| Topic | File |
|-------|------|
| Setup guide | `references/setup.md` |
| Memory template | `references/memory-template.md` |
| TRACE protocol | `references/protocol.md` |
| Confidence model | `references/evidence-ladder.md` |
| Surface mapping | `references/interface-map.md` |
| Deliverable templates | `references/deliverables.md` |
| Safety boundaries | `references/boundaries.md` |

## Requirements

- Authorized access to the target, samples, and environment being analyzed
- A clear statement of whether the target is production, staging, or an offline copy
- Explicit user approval before any invasive, destructive, or credential-bearing step

## Core Rules

### 1. Bound the job before probing
- Name the target, desired outcome, available artifacts, and operational boundary first.
- Ask what is allowed: read-only inspection, replay, instrumentation, decompilation, fuzzing, or patching.
- If the boundary is unclear, default to the safest read-only path.
- Before the first persistent write, state what will be stored locally and ask for permission.

### 2. Run the TRACE loop from `references/protocol.md`
- Triage the target.
- Record observable behavior.
- Abstract hypotheses.
- Challenge each hypothesis with the smallest useful test.
- Explain the result in user-facing language.

### 3. Separate evidence, inference, and guess
- Tag every claim using the ladder in `references/evidence-ladder.md`.
- Keep "observed" distinct from "likely" or "possible."
- When certainty is low, say what would raise confidence instead of pretending to know.

### 4. Map surfaces before internals
- Build the interface inventory from `references/interface-map.md` before writing an implementation story.
- Start from inputs, outputs, states, side effects, and trust boundaries.
- Reverse engineering is faster when the outer contract is stable before diving deeper.

### 5. Prefer minimal, reproducible probes
- Use the smallest sample, trace, packet, call, or binary slice that can prove or disprove a hypothesis.
- Keep every probe replayable and attributable.
- If a result cannot be reproduced, it is a clue, not a conclusion.

### 6. Deliver models, not raw notes
- Every session should end with concrete outputs from `references/deliverables.md`: target brief, interface map, hypothesis ledger, reproduction note, and remaining unknowns.
- Optimize for what the user can act on next: debug, reimplement, migrate, document, or secure.
- Good reverse engineering compresses complexity without hiding uncertainty.

## Common Traps

These failures usually waste the most time or create false confidence.

| Trap | Why It Fails | Better Move |
|------|--------------|-------------|
| Jumping straight to decompilation | You lose the external contract and context | Start with behavior, interfaces, and captured artifacts |
| Treating logs as truth | Logs reflect one code path and one viewpoint | Cross-check with traces, outputs, and controlled inputs |
| Reverse engineering the whole system | Scope explodes and confidence drops | Pick one question, one layer, and one target surface |
| Confusing correlation with mechanism | Similar timings or names can mislead | Design a falsifiable probe before concluding |
| Keeping findings in loose notes | Knowledge becomes untestable and unreusable | Convert findings into deliverables with evidence tags |
| Poking live systems casually | You create risk and destroy signal | Prefer offline copies, captures, and explicit approvals |

## Security & Privacy

**Data that leaves your machine:**
- Nothing by default.
- Only user-approved samples or public documentation if the task explicitly requires external lookup.

**Data that stays local:**
- Preferences and engagement notes in `<state_root>/reverse-engineering/`
- Captured traces, decoded notes, and reproduction snippets kept in the workspace or the local reverse-engineering folder

**Restricted Actions:**
- Protect credentials, require authorization, and maintain visible activity
- Restrict execution to safe environments and require approval for exploit chains
- Base all claims on verified evidence
- Keep sensitive data strictly within the documented local folder
- Confirm with the user before creating durable local memory

## Related Skills
- `analysis` — structure ambiguous problems and turn raw evidence into decisions
- `api` — reason about endpoints, payloads, contracts, and integration behavior
- `architecture` — model system boundaries, components, and data flow once the target is understood
- `bash` — build small inspection and replay loops for traces, logs, and artifacts
- `cybersecurity` — evaluate trust boundaries, attack surface, and safe handling of sensitive targets
