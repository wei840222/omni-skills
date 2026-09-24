---
name: thailand
description: Manage, plan, and optimize travel, relocation, remote work, or business
  setup in Thailand. Use when the user requests information on Thai regions, visas,
  living costs, or local practicalities.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🇹🇭"}'
  related-skills: '{"travel-planning": "Structures and tracks complex multi-region
    itineraries within Thailand.", "expat": "Broader transition planning for long-term
    international relocation."}'
---
## State location

Thailand state may exist in `<workspace>/thailand/`, `<workspace>/memory/thailand/`, or `~/thailand/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/thailand/`, `<workspace>/memory/thailand/`, `~/thailand/`.
3. If none exists and state must be created, default to `<workspace>/thailand/`.

Use the selected `<state_root>` for every state operation in this skill.

## Trigger Instructions

Load specific references based on the user's intent:

- **Setup & Baseline**: Load `references/setup.md` first if `<state_root>` is empty.
- **Regions & Choosing a Base**: Load `references/regions-index.md` or `references/regions-choosing.md`. For specific regions, load `references/regions-bangkok.md`, `references/regions-chiang-mai.md`, `references/regions-islands.md`, `references/regions-north.md`, or `references/regions-phuket.md`.
- **Visas & Legal**: Load `references/visas.md`.
- **Cost of Living**: Load `references/cost.md`.
- **Housing & Setup**: Load `references/resident.md` or `references/nomad.md`.
- **Food & Dining**: Load `references/food-overview.md` to begin. Specifics live in `references/food-areas.md`, `references/food-international.md`, `references/food-practical.md`, `references/food-street.md`, and `references/food-thai.md`.
- **Transport**: Load `references/transport.md`.
- **Culture & Language**: Load `references/culture.md` or `references/language.md`.
- **Lifestyle & Nightlife**: Load `references/lifestyle.md` or `references/nightlife.md`.
- **Healthcare & Safety**: Load `references/healthcare.md` or `references/safety.md`.
- **Business & Teaching**: Load `references/business.md` or `references/teaching.md`.
- **Tech & Connectivity**: Load `references/tech.md`.
- **Visitors**: Load `references/visitor-tips.md`, `references/visitor-attractions.md`, `references/visitor-itineraries.md`, or `references/visitor-lodging.md`.
- **Climate**: Load `references/climate.md`.
- **Memory Template**: Use `assets/memory-template.md` to structure `<state_root>/memory.md`.

Maintain focused execution by loading only the necessary files for the immediate request.
