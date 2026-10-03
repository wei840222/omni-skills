---
name: gratitude
description: Track daily gratitude, discover patterns, and build a positive reflection practice. Use when the user expresses gratitude, wants to log a good moment, or asks for help reflecting on the positive aspects of their day.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🙏"}'
  related-skills: '{"habits":"Integrates gratitude logging into trackable daily routines.","journal":"Captures longer-form personal reflections beyond short gratitude entries.","reflection":"Provides structured frameworks for deeper personal review and insight."}'
---

## State location

Gratitude state may exist in `<workspace>/gratitude/`, `<workspace>/memory/gratitude/`, or `~/gratitude/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/gratitude/`, `<workspace>/memory/gratitude/`, `~/gratitude/`.
3. If none exists and state must be created, default to `<workspace>/gratitude/`.

Use the selected `<state_root>` for every state operation in this skill.

## Core Behavior
- Help user log what they're grateful for.
- Surface patterns and insights over time.
- Help identify gratitude when they're stuck.

## File Structure

- `<state_root>/log/YYYY/MM/DD.md`: Daily entries.
- `<state_root>/patterns.md`: Aggregated themes and insights.
- `<state_root>/favorites.md`: Standout entries for hard days.
- `<state_root>/practice.md`: User preferences for frequency and style.

## Instructions

- **Capturing Entries**: When the user wants to log gratitude, or if they need prompts to find something they are grateful for, read `references/capture.md`.
- **Reviewing Insights**: To summarize past entries or surface meaningful patterns during check-ins, read `references/reflection.md`.
- **Data Formatting**: Use `assets/data-templates.md` when creating or updating any file in `<state_root>`.
