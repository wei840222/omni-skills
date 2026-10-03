---
name: ui
description: >
  Design clear, consistent product UI with hierarchy, type, color, spacing,
  alignment, component states, icons, imagery, responsive layout, dark mode,
  motion, and design tokens. Use when building or reviewing screens, components,
  design systems for product interfaces, fixing cluttered/inaccessible layouts,
  or applying visual polish before handoff. Prefer `design` for broader visual
  critique across slides/posters/email, `typography` for deep type systems,
  `color` for palette/token science, `animate` for motion implementation,
  `figma` for in-file canvas mechanics, and `ux` for heuristics/flow evaluation
  when visual craft is not the main ask.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎨"}'
  related-skills: '{"animate":"Product motion systems, reduced-motion, and transition tokens when animation is primary.","color":"Palette construction, contrast math, and color-space decisions beyond UI defaults.","css":"Implementation syntax for layout, tokens, and states in web CSS.","design":"Broader visual critique across UI and non-UI artifacts when taste leads.","design-system":"Token architecture and component library governance this skill applies inside screens.","figma":"Figma auto-layout, variables, and Dev Mode mechanics inside the design file.","frontend":"Front-end architecture around the UI patterns this skill specifies.","typography":"Deep measure, leading, optical size, and type-scale craft.","ux":"Nielsen heuristics, cognitive load, and flow evaluation beyond visual craft."}'
---

# UI

Stateless product-interface craft rules. This skill does not store local configuration or persistent user state.

## When to use

- Designing or reviewing **product UI**: screens, components, forms, dashboards, mobile/web app chrome
- Fixing clutter, weak hierarchy, inconsistent spacing, low contrast, missing states, or weak affordances
- Specifying responsive behavior, dark mode, motion defaults, icons/imagery, or design tokens for interfaces
- Not the first choice for pure visual taste across posters/slides (`design`), pure type systems (`typography`), pure color science (`color`), Figma file mechanics (`figma`), motion implementation stacks (`animate`), or heuristic UX audits without visual craft (`ux`)

## Core rules (always on)

1. **One focal point** — Size, color, and weight establish rank; primary action is the most prominent control.
2. **Group by proximity** — Related elements share tighter gaps; groups get more space between them than items within.
3. **Grid and align** — Prefer an 8px (or 4px dense) base grid; share edges on invisible lines; use optical alignment when math centers look wrong.
4. **Type discipline** — At most 2–3 families; clear steps title > heading > body > caption; body line-height ~1.4–1.6; measure ~45–75 characters; left-align body.
5. **Color with meaning** — One dominant brand/primary; semantic red/green/yellow reserved; neutrals carry most UI; never rely on color alone.
6. **Touch and focus** — Interactive targets ≥44×44 CSS px equivalent on touch; visible focus for keyboard; disabled looks disabled.
7. **States are designed** — Default, hover, active, focus, disabled, loading, error — each intentional, not accidental.
8. **Motion serves meaning** — 150–300ms transitions; ease-out enter / ease-in exit; honor `prefers-reduced-motion`.
9. **Tokens over magic numbers** — Colors, spacing, type, radii, elevation as semantic tokens so theme/dark mode swap values once.

## Quick reference

| Situation | Play |
|---|---|
| Screen feels cluttered | Delete decoration first; increase between-group gaps; one primary action |
| Nothing stands out | Rank content 1–3; style only rank 1 as prominent |
| Text hard to read | Check contrast (≥4.5:1 body), measure 45–75ch, line-height 1.4–1.6 |
| Error shown only in red | Add icon + text; keep red as reinforcement, not sole cue |
| Buttons look inert | Strengthen affordance (shape, contrast, label); keep disabled truly muted |
| Touch misses | Grow hit area to ≥44px; icon visual can stay ~24px |
| Dark mode looks harsh | Do not invert; redesign elevation with lighter surfaces; re-check every state |
| Inconsistent cards/spacing | Snap to spacing scale 4/8/16/24/32/48; same relationship → same gap |
| Animation feels random | Align duration/easing; skip pure decoration under reduced motion |
| Theme drift | Move raw values into semantic tokens (`color-error`, `space-md`) |

## Progressive disclosure

Load references only when the task needs depth beyond Core rules and Quick reference.

| Load when | File |
|---|---|
| Implementing or reviewing full guideline checklist (hierarchy, type, color, spacing, alignment, states, icons, imagery, responsive, dark mode, motion, tokens, common mistakes) | `references/design-guidelines.md` |
| Verifying contrast, target size, focus, tokens, or reduced-motion claims against Gate 6 sources | `references/sources.md` |

## Safety and boundaries

- Do not invent brand/legal/accessibility compliance claims without checking product requirements and cited sources.
- Accessibility numbers (contrast, target size) follow WCAG/platform guidance in `references/sources.md`; flag when a host cannot measure contrast live.
- Prefer progressive enhancement and reduced-motion paths over decorative motion that blocks tasks.
- Keep secrets, real user PII, and production tokens out of examples; use placeholders only.
