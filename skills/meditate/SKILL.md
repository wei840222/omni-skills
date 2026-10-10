---
name: meditate
description: >
  Generate sandboxed idle-time reflections: profile-aware observations and
  questions, adaptive cadence from feedback, and a small local insight queue.
  Use when the agent has idle time between interactions, or the user asks to
  meditate, ruminate, or surface non-actionable insights from recent chat
  patterns. Prefer `reflection` for pre-delivery self-critique and lesson
  logging, `journal` for user-authored entries and reviews, `habits` for
  cue/routine tracking, and `daily-planner` for scheduling blocks. This skill
  produces text-only reflections and never executes actions on the user's behalf.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧘"}'
  related-skills: '{"reflection":"Pre-delivery self-critique and post-mistake lesson capture rather than idle pattern meditation.","journal":"User-authored journaling practice and multi-scale reviews.","habits":"Cue and streak tracking once a meditation cadence is chosen.","daily-planner":"Places protected thinking time into the day schedule.","memory":"Long-term shared memory retrieval outside the meditate state tree."}'
---

# Meditate

Own **idle-time sandboxed meditation**: detect conversation patterns, queue a few text-only observations/questions, adapt cadence from feedback, and keep mutable state out of the skill package.

## State location

Meditate state may exist in `<workspace>/meditate/`, `<workspace>/memory/meditate/`, or `~/meditate/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/meditate/`, `<workspace>/memory/meditate/`, `~/meditate/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and state must be created, default to `<workspace>/meditate/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/meditate/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Do not treat the literal string `<state_root>` as a filesystem path. Do not write secrets, credentials, or raw private dumps into insight files. Do not write learned preferences into `SKILL.md`.

Default layout (create on first authorized write):

```text
<state_root>/
├── profile.md         # Detected profile, rhythm preferences, focus areas
├── topics.md          # Active meditation topics with priority
├── insights.md        # Pending insights queue (max 3)
├── feedback.md        # User reactions and engagement stats
└── archive/           # Presented insights with outcomes
```

If older files exist only under a legacy path outside the candidate roots (for example a vendor data directory), offer a one-time migrate into the resolved `<state_root>/` and say in one line what moved; do not keep marketplace homepage links.

## Core behavior

- **Not for:** delivery QA (`reflection`), authored diary pages (`journal`), streak tracking (`habits`), or placing calendar blocks (`daily-planner`).
- Produce **text-only** observations and questions; frame suggestions as “What if we considered X?” rather than “I’ll do X”.
- Resolve `<state_root>` before any profile/topic/queue read or write.
- Keep at most **3** pending insights; present oldest first; archive after present.
- Adapt frequency from feedback (positive → maintain/increase; silence/negative → reduce).
- Confirm profile and topic preferences through feedback; do not lock a profile without signal.
- Prefer routing to `reflection`, `journal`, `habits`, or `daily-planner` when the user wants critique, authored entries, streaks, or calendar blocks.

## When idle time or a meditation request arrives

1. Resolve `<state_root>` and load `profile.md` / `topics.md` when present (`references/memory-template.md` for templates).
2. Decide whether cadence allows a new insight (`references/domain.md` adaptive rhythm). If over-quota or user asked to pause, skip generation and say so briefly.
3. Classify a working profile from recent shared conversation patterns only (`references/topics.md`); store updates in `<state_root>/profile.md` after confirmation, not speculation alone.
4. Draft 1–2 insights in the standard output format (`references/domain.md`); run the sandbox checklist (`references/sandbox.md`) before presenting.
5. Enqueue under `<state_root>/insights.md` (cap 3). Present oldest pending item first.
6. After user response or measurable silence, update `<state_root>/feedback.md` and topic priorities (`references/feedback.md`).
7. Archive presented items under `<state_root>/archive/` with outcome notes; clear archive entries older than 30 days when touching archive.

## Failure and safety

- Action-shaped request (“give me an action plan”, “run this”, “send that”): keep output as observations/questions only; offer to hand off to a task skill if the user explicitly wants execution.
- Missing `<state_root>` and no host workspace: read-only meditation from current chat context is allowed; ask before creating durable files.
- Multiple candidate roots: use highest precedence only; report siblings; do not merge.
- Personal data in queue: store non-sensitive summaries; omit secrets, credentials, and third-party private content.
- External research during meditation: only with explicit user permission for that turn.
- Sandbox doubt: omit the insight rather than emit commands, scripts, network calls, or file edits outside `<state_root>/`.

## Progressive disclosure

| Topic | Load when | File |
|-------|-----------|------|
| Domain rules, rhythm, output format | Every meditation run | `references/domain.md` |
| Sandbox checklist and output validation | Before presenting any insight | `references/sandbox.md` |
| Profile topic catalogs | Profile detection or topic planning | `references/topics.md` |
| Feedback interpretation and recovery | After user response or silence | `references/feedback.md` |
| State file templates | First setup or empty `<state_root>` | `references/memory-template.md` |
| Research sources | Freshness checks or PR/audit context | `references/sources.md` |
