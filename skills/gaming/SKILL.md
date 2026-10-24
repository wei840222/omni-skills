---
name: gaming
description: >
  Recommend games, troubleshoot stuck points, optimize settings, and promote
  healthy gaming habits.
metadata:
  openclaw: '{"emoji": "🎮"}'
  category: 'entertainment'
---

When the user asks for gaming recommendations, help when stuck, settings optimization, or healthy gaming habits, you MUST load the guidance from `<state_root>/skills/gaming/references/guidance.md` before answering.

## State location

Gaming state may exist in `<workspace>/gaming/`, `<workspace>/memory/gaming/`, or `~/gaming/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/gaming/`, `<workspace>/memory/gaming/`, `~/gaming/`.
3. If none exists and state must be created, default to `<workspace>/gaming/`.

Use the selected `<state_root>` for every state operation in this skill.
