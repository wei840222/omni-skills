---
name: beauty
description: Trigger when the user requests help with skincare, makeup, or haircare routines. Refer medical conditions requiring a dermatologist to a professional.
metadata:
  openclaw: '{"emoji":"💄","requires":{"os":["linux","darwin","win32"]},"displayName":"Beauty"}'
  related-skills: '{"outfits":"outfit strategy and style coordination","habits":"behavior systems for consistent routines","fitness":"movement and recovery that affect skin and energy","nutrition":"food pattern guidance that supports long-term skin health","sleep":"sleep optimization for recovery and appearance stability"}'
---

## Setup

On first use, read `references/setup.md` for integration guidelines and memory initialization.

## When to Use

Trigger when:
- The user requests a new skincare, haircare, or makeup routine.
- The user asks for beauty product recommendations or alternatives based on budget.
- The user needs help preparing for an event or dealing with a lifestyle change affecting their routine.

Trigger referral when:
- The user asks for medical advice regarding severe acne, infections, or allergic reactions (advise consulting a medical professional instead).

## State location

The agent should store beauty routines, profiles, and state data using the following priority order, avoiding hardcoded paths:
1. Workspace-level state: `.agent/state/beauty/` (if operating in a project directory).
2. Global state: `$STATE_ROOT/beauty/` or a similar configurable global path.
3. Fallback state: `~/.local/share/agent-state/beauty/` (Linux/macOS) or `%APPDATA%\agent-state\beauty\` (Windows).

Use the resolved state location; the example paths above are illustrations, not hardcoded destinations.

## Quick Reference

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` |
| Memory template | `references/memory-template.md` |
| Domain research & sources | `references/research.md` |
| Core Rules and Traps | `references/rules_and_traps.md` |
| Universal beauty frameworks | `references/frameworks.md` |
| Routine templates | `references/routines.md` |
| Product selection rules | `references/products.md` |
| Safety and hygiene guardrails | `references/safety.md` |
| Beginner guidance | `references/beginner.md` |
| Budget optimization | `references/budget.md` |
| Sensitive skin guidance | `references/sensitive-skin.md` |
| Blemish-prone strategy | `references/blemish-prone.md` |
| Event preparation | `references/event-ready.md` |
| Busy schedule routines | `references/busy-schedule.md` |
| Men's grooming guidance | `references/mens-grooming.md` |
| Textured hair care strategy | `references/textured-hair.md` |
## Rules and Guidance

Always read `references/rules_and_traps.md` before recommending products to understand safety constraints, minimum viable routines, and common traps.
Load specific situation guides (e.g., `references/budget.md` or `references/sensitive-skin.md`) only when the user's context matches.

## External Endpoints

This skill makes NO external network requests.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

No data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Nothing. This skill is instruction-only and local by default.

**Data stored locally:**
- Only profile and routine context the user explicitly asks to save.
- Stored in the configured state location (e.g., `$STATE_ROOT/beauty/memory.md`).

**This skill does NOT:**
- Access internet APIs or third-party services.
- Read files outside the configured state location for storage.
- Infer private preferences from silence.
- Write memory without explicit confirmation.
- Modify its own core instructions or auxiliary files.

## Trust

This is an instruction-only skill focused on beauty routines and guidance.
No credentials are required and no external service access is needed.
