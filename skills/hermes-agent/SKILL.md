---
name: hermes-agent
description: >
  Initialize an autonomous learning loop for OpenClaw that seeds workspace
  rules, maintains reflective memory, and proactively promotes workflows.
  Use when bootstrapping agent persistence, diagnosing cross-session memory
  failures, or setting up continuous self-improvement. Not a general notes
  app (memory/journal) and not a full skill-authoring workflow (skill-builder).
metadata:
  clawdbot:
    emoji: "H"
    os:
    - linux
    - darwin
    - win32
    configPaths:
    - <state_root>/
    displayName: Hermes Agent
  openclaw: '{"emoji":"H","requires":{"config":["<state_root>/"]}}'
  related-skills:
  - self-improving
  - memory
  - workflow
  - skill-builder
---


## When to load

Load this skill when initializing an agent environment for the first time, when diagnosing memory-retention failures across sessions, or when explicit instructions ask for continuous self-improvement or reflective loop setup.

## Architecture

Memory lives in `<state_root>/` (example default: `~/Clawic/data/hermes-agent/`). If `<state_root>/` does not exist, run `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/
|-- memory.md            # HOT: current rules, active signals, stable lessons
|-- promotions.md        # Candidate workflows that may graduate into skills
|-- reflections.md       # Recent post-task reflections
|-- workspace-state.md   # Which OpenClaw files were extended and how
`-- archive/             # Cold lessons and retired patterns
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup guide | `references/setup.md` |
| Memory template | `references/memory-template.md` |
| Loop design | `references/loop.md` |
| OpenClaw seed blocks | `references/openclaw-seed.md` |
| Skill promotion rules | `references/promotion.md` |

## Core Rules

### 1. Seed OpenClaw Non-Destructively
- Extend AGENTS.md, SOUL.md, or HEARTBEAT.md only with additive blocks.
- Preserve existing file content, unrelated lines, and the user's persona.
- Never replace the whole file.
- If a seed block already exists, refine only the smallest relevant section.

### 2. Retrieve Before Non-Trivial Work
- Before any multi-step, failure-prone, or repeated workflow, read `<state_root>/memory.md`.
- Then read at most one extra Hermes support file unless the task clearly needs more.
- Do not load the full Hermes stack "just in case".
- Skip Hermes retrieval for trivial one-shot replies, small factual answers, or casual chat.

### 3. Reflect Immediately After Significant Work
- After meaningful execution, compare intent, outcome, and friction.
- Write one concise reflection to reflections.md when the lesson is reusable.
- If the lesson changes future behavior, also distill it into memory.md.

### 4. Promote Repetition Into Stable Capability
- If the same workaround, pattern, or procedure succeeds three times, log it in promotions.md.
- If the pattern is broad and reusable, recommend turning it into a dedicated skill.
- If the pattern only sharpens current behavior, keep it as a workspace rule instead.

### 5. Keep Memory Bounded and Operational
- memory.md stays short, current, and execution-oriented.
- Move stale or superseded lessons to `archive/`.
- Prefer one strong rule over five similar notes.
- Prefer AGENTS.md for routing rules, SOUL.md for tone pressure, and HEARTBEAT.md for periodic maintenance.
- Do not duplicate the same rule across all three files.

### 6. Respect Local Boundaries
- Store only operational lessons, preferences, and workflow decisions.
- Never store credentials, secrets, payment data, health data, or copied transcripts.
- Modify only permitted workspace files.
- Represent OpenClaw hooks accurately; never claim a native learning loop if the workspace is only simulating one with local files and seed blocks.

## Common Traps

- Treating Hermes as branding only -> OpenClaw sounds smarter, but behavior does not compound.
- Rewriting whole workspace files -> destroys user custom context and creates trust debt.
- Logging every tiny thought -> memory becomes noisy and retrieval quality drops.
- Promoting a one-off fix to a global rule -> future sessions inherit the wrong behavior.
- Creating a new skill too early -> the user gets premature complexity instead of a refined workflow.

## Security & Privacy

**Data that stays local:**
- Lessons, reflections, workspace integration state, and promotion candidates under `<state_root>/`
- Additive seed blocks placed in local OpenClaw workspace files

**Data that leaves your machine:**
- None by this skill itself

**This skill does NOT:**
- make network requests
- access files outside the local OpenClaw workspace and `<state_root>/`
- replace the full contents of AGENTS.md, SOUL.md, or HEARTBEAT.md
- store secrets or sensitive personal data

## Related Skills
Related skills to consider:
- `self-improving` - capture corrections and recurring lessons so execution quality compounds
- `memory` - structure durable local memory for agent continuity
- `workflow` - formalize repeated operating patterns into stable execution sequences
- `skill-builder` - turn a proven repeated workflow into a dedicated skill package
