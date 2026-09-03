---
name: creativity
description: "Generate creative options and brainstorm across a safe→stretch→wild spectrum while calibrating to the user's taste. Use when the user asks for ideas, creative directions, naming options, campaign concepts, or taste-calibrated brainstorming; not for prompt debugging (`prompting`), business-idea validation (`business-ideas`), or design-system deliverables (`designer`)."
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🎨"}'
  related-skills: '{"prompting":"Diagnose and iterate prompts when the blocker is instruction quality rather than idea generation.","brainstorm":"Fast unstructured idea dumps when taste calibration and technique rotation are not needed.","writing":"Draft or rewrite prose after a creative direction is chosen.","business-ideas":"Startup and side-project ideation with market-validation framing.","designer":"Design artifacts and systems after creative direction is locked."}'
---

## When to Use

User asks for ideas, brainstorming, creative options, campaign concepts, naming directions, or taste-calibrated alternatives. Agent generates a Safe → Stretch → Wild spectrum, rotates techniques, and updates learned preferences after feedback.

Use `prompting` when the failure is prompt structure or model behavior. Use `business-ideas` for startup/market validation. Use `designer` when the deliverable is a design system or artifact, not the idea set itself.

## Quick Reference

| Area | File | When to load |
|------|------|--------------|
| Creative techniques | `references/techniques.md` | When rotating methods or the user asks for a specific technique |
| Preferences template | `references/preferences-template.md` | When seeding `<state_root>/preferences.md` for the first time |
| Research sources | `references/sources.md` | When citing technique origins or refreshing domain knowledge |

## State location

Creativity taste state may exist in `<workspace>/creativity/`, `<workspace>/memory/creativity/`, or `~/creativity/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured state path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/creativity/`, `<workspace>/memory/creativity/`, then `~/creativity/`.
3. If no candidate exists and the user wants preferences saved, create `<workspace>/creativity/`.

Use the selected `<state_root>` for every state operation in this invocation. If several candidate directories exist, use only the highest-precedence one and tell the user that separate copies were detected; do not merge them automatically.

Durable taste lives at `<state_root>/preferences.md`. If that file is missing, copy `references/preferences-template.md` into `<state_root>/preferences.md` before the first write. Skill package resources stay under `references/`; never write runtime preferences into the skill tree.

## Core Principle

Creativity is controlled divergence. Learn the user's taste, then explore within and beyond those boundaries intentionally.

Before generating ideas, load `<state_root>/preferences.md` when it exists. When instructed to use a specific technique or when seeking varied output, load `references/techniques.md`. Update preferences after receiving feedback.

## The Creative Process

```text
1. DIVERGE  — Generate many options, suspend judgment
2. FILTER   — Apply preferences from <state_root>/preferences.md
3. PRESENT  — Show range: safe → stretch → wild
4. LEARN    — Record reaction in <state_root>/preferences.md
5. REFINE   — Iterate based on feedback
```

## Output Spectrum

Always present options across a range:

```text
🎨 Creative options for [goal]:

Safe (familiar territory):
→ [Option aligned with known preferences]

Stretch (new but grounded):
→ [Option that pushes slightly beyond comfort]

Wild (high risk, high reward):
→ [Option that breaks conventions]

Which direction feels right?
```

## Taste Dimensions

| Dimension | Spectrum |
|-----------|----------|
| Tone | Serious ←→ Playful |
| Density | Minimal ←→ Rich |
| Novelty | Classic ←→ Avant-garde |
| Structure | Rigid ←→ Fluid |
| Abstraction | Concrete ←→ Conceptual |
| Energy | Calm ←→ Intense |
| Polish | Raw ←→ Refined |

## Learning Signals

| Signal | Action |
|--------|--------|
| "Love it" / "Perfect" | Record in `<state_root>/preferences.md`: this direction works |
| "Interesting but..." | Note what worked and what did not |
| Silence / moves on | Assume miss; try a different vector |
| "Too X" / "Not enough Y" | Adjust the matching dimension in `<state_root>/preferences.md` |
| Chooses from options | Record which spectrum end was picked |

## Calibration

Periodically confirm the taste model:

```text
🎨 Quick calibration

I've noticed you tend toward [observed pattern].
Should I keep leaning that direction, mix it up, or shift?
```

## Required Execution Patterns

| Standard Action | Requirement |
|-----------------|-------------|
| Idea generation | Always provide a spectrum of options (Safe, Stretch, Wild) |
| Risk distribution | Include stretch and wild options alongside safe ones |
| Negative signals | Update `<state_root>/preferences.md` when ideas are rejected |
| Technique selection | Rotate techniques systematically (`references/techniques.md`) |
| State writes | Resolve `<state_root>` once, then write only under that root |
