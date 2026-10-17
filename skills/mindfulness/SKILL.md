---
name: mindfulness
description: >
  Track mindfulness habits, guide short meditation sessions, log progress, and
  recommend adaptive daily routines. Use when the user wants stress reset,
  guided breathing/body-scan practice, habit building for meditation, session
  logging, or weekly routine adjustments. Prefer `health` for broad clinical
  health context, `habits` for generic habit design, `journal` for free-form
  reflection, `coach` for accountability loops, and `sleep` for evening
  wind-down that is not a live mindfulness session.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧘"}'
  related-skills: '{"coach":"Accountability loops and progress reviews around practice adherence.","habits":"Generic habit design and cue-routine-reward framing outside meditation coaching.","health":"Broader health context that can shape mindfulness goals without clinical diagnosis.","journal":"Free-form reflection workflows after sessions rather than structured session logs.","sleep":"Evening wind-down and sleep hygiene when the request is recovery, not live practice."}'
---

# Mindfulness

Coach local mindfulness practice: mode selection, short guided sessions,
structured logs, and one-change-at-a-time routine adjustments. This is coaching
and tracking support, not clinical diagnosis or therapy.

## State location

Mindfulness memory, session logs, plans, and recommendation history are
persistent user state. Resolve `<state_root>` once per invocation before any
read or write:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order:
   `<workspace>/mindfulness/`, `<workspace>/memory/mindfulness/`, then
   `~/mindfulness/`.
3. If more than one candidate exists, use only the highest-precedence directory
   and report the duplicates; do not merge them.
4. If none exists and the user confirms saving state, create
   `<workspace>/mindfulness/`. If `<workspace>` is unavailable, ask for a state
   root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. Keep
skill resources under `references/` and `assets/`; never write the literal
string `<state_root>` to disk.

Suggested layout (create only paths the user confirms):

```text
<state_root>/
├── memory.md
├── logs/sessions.md
├── plans/current.md
├── recommendations.md
├── guides/library.md
└── check-ins/weekly.md
```

Before creating or changing local files, present the planned write and ask for
user confirmation.

## When to use

- Quick stress reset or 1–3 minute breathing space
- Live guided meditation (body scan, open monitoring, short resets)
- Daily/weekly mindfulness habit building with realistic time windows
- Structured session logging and trend-based next-step recommendations
- Activation setup for when this skill should or should not fire

Prefer neighboring skills when the ask is broader health triage (`health`),
generic habit scaffolding (`habits`), free-form journaling (`journal`),
accountability coaching (`coach`), or sleep hygiene (`sleep`).

## Setup

On first use, or when `<state_root>/` is missing or empty, read
`references/setup.md` silently, answer the immediate user need first, then
clarify activation preference and practice depth.

## Quick reference

| Topic | File | Load when |
|-------|------|-----------|
| Setup and activation | `references/setup.md` | First use / empty state / activation unclear |
| Memory structure | `references/memory.md` | Before reading or writing state |
| Data templates | `assets/data-templates.md` | Initializing or extending state files |
| Practice modes | `references/practice-modes.md` | Choosing or switching mode |
| Session log fields | `references/session-log-template.md` | After each session |
| Guided scripts | `references/guided-meditations.md` | Running a live guided practice |
| Recommendation matrix | `references/recommendation-rules.md` | Weekly or adherence-based next step |
| Reflection prompts | `references/reflection-prompts.md` | Closing a session with one prompt |
| Verified sources | `references/sources.md` | Fact claims, crisis framing, research language |

## Core rules

### 1. Identify the active mode before responding

Select one mode from `references/practice-modes.md`:

- `logger` — tracking only
- `guided` — live step-by-step session
- `builder` — gradual routine growth
- `reset` — short downshift during high-stress moments

Keep a single active mode; switch only on explicit user request (except the
temporary `reset` escalation, which returns to the prior mode afterward).

### 2. Match session length to real constraints

Start with the smallest viable session (1–3 minutes when time is tight), then
scale. A completed short session beats an ideal session that never starts.

### 3. Guide sessions with a consistent flow

When running practice from `references/guided-meditations.md`, include:

1. opening cue and intention
2. anchor instruction
3. drift-recovery instruction
4. closing transition plus one-line reflection

Keep language concise and secular unless the user requests a specific tradition.

### 4. Log every session in a structured way

Use `references/session-log-template.md` after each session. Capture duration,
technique, pre/post state, and one short note. Base trend decisions on logs, not
assumptions.

### 5. Recommend one next action at a time

Use `references/recommendation-rules.md` to propose one primary next step plus
one fallback. At weekly review, change exactly one variable (duration, timing,
technique, or frequency) unless the user asks otherwise.

### 6. Keep scope in coaching support

Support self-regulation and practice habits. Do not diagnose mental-health
conditions or present this skill as treatment. If the user reports crisis,
self-harm risk, or severe distress escalation, stop routine coaching and direct
immediate professional or emergency support (see `references/sources.md`).

### 7. Preserve user agency and positive framing

Offer clear options and let the user choose effort level. Treat missed days as
data. Prefer positive targets (“do the 1-minute reset at an existing cue”) over
guilt or perfection framing.

## Common traps

- Starting with long daily targets → early dropout
- Generic meditation advice without mode/context → weak follow-through
- Tracking only streaks, not session quality → misleading progress
- Mixing multiple techniques in one default session → cognitive overload
- Treating mindfulness as a cure-all → safety and trust risk
- Pushing deep introspection during acute stress → higher dysregulation risk

## External endpoints

This skill makes **no** undeclared network requests. It is instruction-only and
local unless the user explicitly asks to export notes.

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

## Security and privacy

- **Leaves the machine:** nothing by default.
- **Stored locally (with confirmation):** session logs, recommendation decisions,
  and routine notes under `<state_root>/`.
- **Does not:** make undeclared network calls; diagnose or treat clinical
  conditions; write memory without confirmation; enforce a single belief system;
  modify its own package files at runtime.

## Trust

Instruction-only mindfulness coaching and tracking. No credentials and no
third-party service access are required.
