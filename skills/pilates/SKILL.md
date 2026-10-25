---
name: pilates
description: >
  Plan Pilates sessions, refine form, and track progress with equipment-aware
  modifications and core-focused cues under <state_root>/pilates/. Use when the
  user asks for mat practice, reformer-informed home work, posture drills, core
  routines, form repair, or a weekly Pilates review. Not for general strength
  programming (`fitness`), clinical rehab diagnosis, or pure habit design
  (`habits`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧘","requires":{"config":["<state_root>/pilates/"]}}'
---

## When to load

User wants Pilates support for mat practice, reformer-informed home work, posture and control drills, recovery-minded training, or a consistent core-focused routine.
Agent helps choose the right session mode, build realistic blocks, fix one form issue at a time, and keep safety boundaries visible.

## State location

Pilates state may exist in `<workspace>/pilates/`, `<workspace>/memory/pilates/`, or `~/pilates/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/pilates/`, `<workspace>/memory/pilates/`, `~/pilates/`.
3. If none exists and state must be created, default to `<workspace>/pilates/`.

Use the selected `<state_root>` for every state operation in this skill.

## Quick Reference

Use these files as operating modules. Load the smallest file that matches the current coaching job.

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory structure and templates | `assets/memory-template.md` |
| Mode selection and switching | `references/practice-modes.md` |
| Session blueprints by duration | `references/session-templates.md` |
| Form checks and coaching cues | `references/form-checks.md` |
| Safety boundaries and modifications | `references/safety-modifications.md` |
| Progression rules and weekly review | `references/progression-ladder.md` |
| Personal practice review prompts | `assets/weekly-review-template.md` |
| Detailed operating rules and guidelines | `references/operating-rules.md` |
