---
name: self-improving
description: >
  Manage self-reflection, criticism, learning, and self-organizing memory.
  Evaluate own work, catch mistakes, and log improvements permanently. Load
  when the user corrects you, a multi-step task needs post-mortem learning,
  memory patterns must be reviewed/exported/forgotten, or durable execution
  lessons should compound across sessions.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧠","requires":{"config":["<state_root>/self-improving/"]}}'
  related-skills: '{"memory":"Long-term factual continuity and diary context; self-improving owns execution lessons and corrections.","learning":"General learning workflows; self-improving stores durable agent performance rules.","decide":"Consequential choice patterns; self-improving logs how work was executed, not branch decisions.","escalate":"Ask-vs-act thresholds; self-improving records corrections after outcomes."}'
---

## When to load

Load this skill when:

- The user corrects you or rejects output and the lesson should persist.
- A significant multi-step task finishes and needs self-reflection.
- You discover a better approach, outdated assumption, or repeated failure mode.
- The user asks to review, export, forget, or inspect memory patterns.
- Workspace setup needs the standard self-improving steering snippets.

Prefer adjacent skills when they fit better:

- Durable facts, people, dates, and diary continuity → `memory`
- One-off study plans or learning curricula → `learning`
- Architecture/vendor/policy branching decisions → `decide`
- Whether to act now or ask first → `escalate`

## Architecture

Memory lives under `<state_root>/self-improving/` with tiered HOT / WARM / COLD storage.
If the directory does not exist, follow `references/setup.md` before writing state.
Workspace setup should add the standard self-improving steering to workspace
`AGENTS.md`, `SOUL.md`, and `HEARTBEAT.md`, with recurring maintenance routed
through `references/heartbeat-rules.md`.

## State location

Self-improving state may exist in `<workspace>/self-improving/`,
`<workspace>/memory/self-improving/`, or `~/self-improving/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/self-improving/`, `<workspace>/memory/self-improving/`, `~/self-improving/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to `<workspace>/self-improving/`.

Use the selected `<state_root>` for every state operation in this skill.
Never write runtime state into this skill package.
Do not store credentials, financial identifiers, medical diagnoses, biometrics,
third-party private data, or precise home/work routines under `<state_root>/`.

Optional layout:

```text
<state_root>/self-improving/
├── memory.md          # HOT: ≤100 lines, always loaded
├── index.md           # Topic index with line counts
├── heartbeat-state.md # Heartbeat markers and action notes
├── projects/          # Per-project learnings
├── domains/           # Domain-specific lessons (code, writing, comms)
├── archive/           # COLD: decayed patterns
└── corrections.md     # Last 50 corrections log
```

If older data lives at `~/Clawic/data/self-improving/`, migrate it into the
resolved `<state_root>/self-improving/` and state the move in one line.

## Quick Reference

| Topic | File |
|-------|------|
| Setup guide | `references/setup.md` |
| Research sources | `references/sources.md` |
| Heartbeat state template | `references/heartbeat-state.md` |
| Memory template | `assets/memory-template.md` |
| Workspace heartbeat snippet | `references/HEARTBEAT.md` |
| Heartbeat rules | `references/heartbeat-rules.md` |
| Learning mechanics | `references/learning.md` |
| Security boundaries | `references/boundaries.md` |
| Scaling rules | `references/scaling.md` |
| Memory operations | `references/operations.md` |
| Self-reflection log | `references/reflections.md` |
| OpenClaw HEARTBEAT seed | `references/openclaw-heartbeat.md` |

## Core Rules

See `references/learning.md` and `references/operations.md` for full details.

- Log only explicitly confirmed preference signals or corrections.
- Derive durable rules from explicit confirmation, not silence or single anecdotes.
- Use tiered storage (HOT, WARM, COLD) with promotion after repeated confirmed use and demotion on decay.
- Keep namespace isolation and resolve conflicts by specificity: project > domain > global.
- Cite the memory source when a stored lesson changes behavior.
- If context is tight, load only `memory.md` (HOT) and defer deeper tiers.
- Before non-trivial work, read `<state_root>/self-improving/memory.md` and at most three directly related domain/project files.

## Heartbeat maintenance

During workspace heartbeat checks:

1. Read `references/heartbeat-rules.md`.
2. Use `<state_root>/self-improving/heartbeat-state.md` for last-run markers.
3. If no file inside `<state_root>/self-improving/` changed since the last reviewed change, return `HEARTBEAT_OK`.
