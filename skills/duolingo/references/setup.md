# Setup — Duolingo Learning OS

Read this when `<state_root>/` is absent, empty, or the user starts a new Learning OS.

## Priority order

### 1. Confirm activation and optional routing scope

In the first exchanges, name the topics that should auto-activate (examples: english, cooking, math).
If the user wants AGENTS auto-routing, prepare the snippet from `activation-routing.md`.
Show the snippet and ask the user to paste it themselves. Keep the skill fully manual if they decline.

### 2. Confirm learning mode per topic

For each active topic, confirm:

- target outcome
- current level
- session pace (`light`, `normal`, `intense`)

Multiple topics may stay active in parallel.

### 3. Bootstrap filesystem and topic namespaces

Create the resolved `<state_root>/` with:

- global router files
- global memory
- one namespace per active topic

Use `blueprint.md`, `assets/memory-template.md`, and `assets/topic-template.md`.
Never write the literal placeholder `<state_root>` to disk.

### 4. Run placement and first micro-lesson

For each new topic:

- run quick placement (2–5 prompts)
- set starting lessons in `queue.md`
- complete the first loop from `lesson-loop.md`

### 5. Configure daily rotation for multi-topic learning

When multiple topics are active, choose a default rotation:

- same-day stack (topic A then B)
- alternating days
- weighted plan (example: 70% english, 30% cooking)

Store the policy in global memory and apply it automatically.

## What to save

| Save to | Content |
|---------|---------|
| `<state_root>/memory.md` | Global status, active topics, rotation policy, streak summary |
| `<state_root>/router/topics.md` | Canonical topics and trigger phrases |
| `<state_root>/router/agentsmd-snippet.md` | Current AGENTS.md routing snippet |
| `<state_root>/topics/<slug>/profile.md` | Goal, level, constraints |
| `<state_root>/topics/<slug>/curriculum.md` | Skill tree and lesson units |
| `<state_root>/topics/<slug>/queue.md` | Next lessons and review backlog |
| `<state_root>/topics/<slug>/sessions.md` | Session log and results |
| `<state_root>/topics/<slug>/checkpoints.md` | Weekly and milestone checks |

## Guardrails

- Start lessons only after the topic namespace exists.
- Require explicit confirmation before removing or archiving a topic.
- If AGENTS router is enabled, keep `agentsmd-snippet.md` synchronized with `router/topics.md`, then ask the user to update AGENTS.
- Keep lesson loops short; split long explanations into multiple loops.
