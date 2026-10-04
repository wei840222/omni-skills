---
name: taste
description: >
  Calibrate aesthetic judgment from human feedback and evaluate subjective creative work
  across design, writing, and generation prompts. Use when reviewing whether something
  "looks right" or "sounds right"; when the user corrects an aesthetic call and wants the
  pattern stored; when establishing domain taste preferences; when separating personal
  preference from craft quality; or when prompting for distinctive creative output instead
  of committee averages. Not for quantified layout systems (design), brand strategy
  (branding), conversion copy (copywriting), multi-format voice drafting (writing),
  component libraries (ui), or type/color system engineering (typography, color).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"👅"}'
  related-skills: '{"design":"Quantified hierarchy, spacing, type, and color rules for visual artifacts.","writing":"Multi-format prose drafting and voice matching rather than taste calibration.","copywriting":"Persuasive marketing and conversion copy rather than aesthetic judgment loops.","art":"Art-making practice and critique beyond taste model calibration.","branding":"Brand positioning and identity systems rather than per-user taste learning.","ui":"Interface component patterns and interaction states.","typography":"Deep type systems, optical sizes, and print settings.","color":"Full color systems, tokens, and cross-surface validation."}'
---

# Taste

Build and apply a **user-specific taste model**. Treat every aesthetic opinion as provisional until the human validates or corrects it. Prefer calibrated judgment over generic “good design” slogans.

## State location

Taste state may exist in `<workspace>/taste/`, `<workspace>/memory/taste/`, or `~/taste/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/taste/`, `<workspace>/memory/taste/`, `~/taste/`.
3. If multiple candidates exist, use the highest-precedence one only. Do not merge lower-precedence directories; tell the user that multiple copies were detected.
4. If none exists and state must be created, default to `<workspace>/taste/`.
5. If the host cannot supply `<workspace>`, do not impersonate it with the current working directory. An existing `~/taste/` may be read; if it also does not exist, ask the user or host to specify a state root before creating data.
6. Once selected, `<state_root>` stays fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill.

### State tree

| Path | Purpose |
|---|---|
| `<state_root>/corrections/` | One note per correction (optional subdirs by domain: `visual/`, `writing/`, …) |
| `<state_root>/preferences/` | Stated aesthetic preferences by domain |
| `<state_root>/patterns/` | Extracted reusable rules from accumulated corrections |
| `<state_root>/calibration.md` | Confidence and accuracy notes per domain |

## When to use

- Review design, layout, typography, color, or visual composition for taste quality
- Review prose, voice, or copy for aesthetic fit (not grammar-only polish)
- Process a human correction to an aesthetic judgment and store the pattern
- Establish or update domain preferences (“more whitespace”, “punchy not salesy”)
- Separate “I like this” from “this is well made”
- Steer generative prompts away from committee-average output

Hand off when the job is really:

- spacing/type/color execution systems → `design`
- brand strategy and identity systems → `branding`
- conversion/sales copy → `copywriting`
- multi-format personal voice drafting → `writing`
- UI components and states → `ui`
- deep type or color engineering → `typography` / `color`
- art practice beyond calibration → `art`

## Quick workflow

1. **Classify the ask** — evaluation, correction/learning, preference capture, or generation steering.
2. **Resolve state** — select `<state_root>`; read `calibration.md` and any matching preference/pattern notes when they exist.
3. **Load only needed references** — see Progressive disclosure.
4. **Judge with reasons** — name hierarchy, restraint, specificity, or voice signals; mark confidence honestly.
5. **Calibrate** — ask one precise question when uncertain or when the user may disagree.
6. **On correction** — acknowledge without defense; extract a pattern; verify; write correction + pattern + calibration update under `<state_root>/`.
7. **Deliver** — assessment or revised direction first; learning updates second.

## Progressive disclosure

| Resource | Load when |
|---|---|
| `references/learning.md` | Corrections, calibration questions, confidence tracking, long-term taste model |
| `references/visual.md` | Layout, hierarchy, type, color, AI-design failure modes |
| `references/writing.md` | Prose rhythm, edit tests, LLM writing clichés |
| `references/development.md` | How taste is trained (volume, near-misses, preference vs quality) |
| `references/antipatterns.md` | More-is-better, impressive-equals-good, safe-average, trend traps |
| `references/prompting.md` | Identity anchoring, negative space, rejection criteria for generation |
| `references/sources.md` | Verified external standards used for Gate 6 claims |

## Core rules

1. **Student stance** — The human’s corrections are training data. Update the model; do not defend the prior call.
2. **Provisional judgments** — State the call, the signals used, and confidence. Unvalidated taste stays labeled provisional.
3. **Preference ≠ quality** — Support both “I dislike this but it is excellent” and “I enjoy this but it is mediocre” when evidence warrants it.
4. **One primary hierarchy** — Visual and prose judgments name a single rank-1 focus; competing foci are a defect unless intentional tension is earned.
5. **Restraint before decoration** — Prefer fewer elements, colors, typefaces, and intensifiers; decoration must earn its place.
6. **Correct can still be dead** — Rule-compliant work that lacks conviction, tension, or specificity fails the taste bar.
7. **Calibrate to domain noise** — Design craft is relatively stable; fashion/music trend layers need lower confidence until user patterns exist (SEP aesthetic judgment: subjective response + claim of broader validity; anomalousness of taste laws).
8. **First impressions are fast** — Visual trust forms in a fraction of a second; hierarchy and calm scanning paths matter before ornament (NN/g first-impressions and aesthetic-usability research).
9. **Write learning to state** — Durable corrections, preferences, and patterns live under `<state_root>/`, never inside the skill package.
10. **Boundary honesty** — When the user needs a full design system, brand platform, or conversion brief, route to the related skill instead of stretching taste.

## Output shape

For evaluations:

1. Verdict (works / weak / split preference-vs-quality)
2. Two to five concrete signals (hierarchy, space, type, voice, cliché load)
3. One calibration question when confidence is low or user taste is unknown
4. Optional state write plan (`corrections/`, `patterns/`, `calibration.md`)

For corrections:

1. Restate the gap in the user’s terms
2. Pattern hypothesis in “In [context], prefer [X] over [Y] because [reason]”
3. Confirm application scope
4. Persist under `<state_root>/`
