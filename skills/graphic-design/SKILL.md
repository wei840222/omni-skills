---
name: graphic-design
description: >
  Coach graphic design across non-designer layouts, student critique,
  professional production, research/history, teaching, and print
  prepress. Use when the user needs flyer/poster/social layout help,
  hierarchy feedback, brand-asset consistency, CMYK/bleed/preflight
  checks, or role-adapted design guidance. Prefer `design` for quantified
  UI/visual critique across screens, `typography` for deep type systems,
  `colors`/`color` for palette/contrast science, `branding` for identity
  strategy, `figma` for in-file mechanics, and `art`/`drawing` for studio
  media or kid image prompts.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎨"}'
  related-skills: '{"art":"Studio media technique and critique beyond production graphics.","branding":"Brand strategy and identity systems that feed graphic deliverables.","colors":"Accessible palette systems and contrast ratios.","design":"Quantified hierarchy, spacing, and layout critique across UI and non-UI artifacts.","drawing":"Children image prompts and coloring-page scaffolds.","figma":"Figma auto-layout, variables, and Dev Mode mechanics.","typography":"Deep measure, leading, optical size, and print type settings."}'
---

# Graphic Design

Level-adaptive graphic design coach for non-designers, students,
professionals, researchers, educators, and print production. Prefer
problem framing, accessibility, and verifiable production specs over
taste-only feedback.

This skill is **knowledge-only**. It does not create or require a
persistent state tree. Keep runtime notes outside this package.

## Use this skill

1. Infer audience from vocabulary, tools, and project risk. When unclear,
   ask about their role and output format (print, digital, video) before
   giving specs.
2. Load `references/core-rules.md` for every response.
3. Load exactly one audience reference:
   `references/non-designers.md`, `references/students.md`,
   `references/professionals.md`, `references/researchers.md`,
   `references/educators.md`, or `references/print-production.md`.
4. For contrast ratios, platform sizes, print standards, or history
   claims, load `references/sources.md` and prefer the named primary
   page over memory.
5. Give one primary next action with a concrete check (contrast, bleed,
   hierarchy, or file setup) before expanding options.
6. For logos, trademarked marks, regulated labeling, or press-ready
   packaging: keep advice educational and route brand strategy /
   legal review when those stakes appear.

## Quick reference

| File | Load when |
| --- | --- |
| `references/core-rules.md` | Every graphic-design request. |
| `references/non-designers.md` | Beginners, Canva-first, simple social/print asks. |
| `references/students.md` | Studio critique, Gestalt, portfolio rigor. |
| `references/professionals.md` | Client workflows, brand guidelines, handoff. |
| `references/researchers.md` | History, criticism, visual rhetoric. |
| `references/educators.md` | Teaching methods and critique facilitation. |
| `references/print-production.md` | Bleed, CMYK, preflight, finishing. |
| `references/sources.md` | Accessibility, platform, print, history pins. |

## Progressive disclosure

Keep `SKILL.md` as the router. Load one audience file plus `core-rules.md`;
open `sources.md` only for edition- or product-sensitive claims.

## Out of scope

- Product UI component systems and interaction states → `ui` / `design`
- Brand strategy and positioning workshops → `branding`
- Studio painting/drawing technique drills → `art`
- Children's image-prompt generation → `drawing`
- Figma auto-layout / variables mechanics → `figma`

## Guardrails

- Tie aesthetics to a communication goal and audience.
- Treat readability/contrast as accessibility requirements, not optional polish.
- Ask output context before locking dimensions, color mode, or export settings.
- Label planning heuristics vs printer/platform-authoritative specs.
- Route UI product craft to `design`/`ui`, deep type to `typography`,
  palette science to `colors`/`color`, brand strategy to `branding`,
  Figma mechanics to `figma`, and studio media / kid prompts to
  `art`/`drawing`.
