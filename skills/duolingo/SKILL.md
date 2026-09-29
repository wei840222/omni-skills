---
name: duolingo
description: Run a multi-topic spaced-repetition learning system with daily lesson
  loops and progression tracking.
metadata:
  clawdbot: '{"emoji": "D", "requires": {"bins": [], "config": ["<state_root>/"]},
    "os": ["linux", "darwin", "win32"], "configPaths": ["<state_root>/"], "displayName":
    "Duolingo Learning OS"}'
  openclaw: '{"requires": {"config": ["<state_root>/"]}}'
  related-skills:
  - learning
  - english
  - course
  - retention
  - coach
---
## When to load

Load this skill when the user asks to learn a new subject, practice an existing skill, review a learning topic, or explicitly requests a Duolingo-style lesson.

## Setup

On first use, read `references/setup.md` for routing, filesystem bootstrap, and topic activation.

## Quick Reference

| Topic | File |
|-------|------|
| Setup flow | `references/setup.md` |
| Global memory template | `assets/memory-template.md` |
| Filesystem bootstrap | `references/blueprint.md` |
| Architecture and state structure | `references/architecture.md` |
| Core rules and guidelines | `references/core-rules.md` |
| AGENTS routing rules | `references/activation-routing.md` |
| Lesson runtime loop | `references/lesson-loop.md` |
| XP/hearts/streak economy | `references/progression.md` |
| Multi-topic retention ops | `references/retention-ops.md` |
| Topic namespace templates | `assets/topic-template.md` |
| Weekly health review | `references/launch-scorecard.md` |
| Common traps and anti-patterns | `references/traps.md` |
| Security and privacy constraints | `references/security.md` |
