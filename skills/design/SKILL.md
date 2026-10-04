---
name: design
description: Executes and critiques visual design with quantified rules for hierarchy, spacing, type scale, color, and layout. Use when designing UI screens, landing pages, slides, posters, social graphics, emails, charts, or PDFs; when a design looks cluttered, flat, or hard to read; when choosing fonts or building a palette without a design system; when adapting to dark mode or mobile; or when reviewing generated HTML/CSS before delivery. Do not use for design-token pipelines (design-system) or brand strategy (branding).
metadata:
  version: "1.0.3"
  openclaw: '{"emoji": "🎨"}'
  related-skills: '{"ui": "Provides interface component patterns, interaction states, and platform conventions.", "typography": "Handles deep type work: optical sizes, variable weight axes, and print settings.", "color": "Provides full color systems, tokens, and cross-surface color validation.", "design-system": "Scales one-off decisions into tokens and component libraries."}'
---
## State location

Design state may exist in `<workspace>/design/`, `<workspace>/memory/design/`, or `~/design/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/design/`, `<workspace>/memory/design/`, `~/design/`.
3. If none exists and state must be created, default to `<workspace>/design/`.

Use the selected `<state_root>` for every state operation in this skill.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| type_scale_ratio | number (1.125-1.5) | 1.25 | Regenerates the size ladder in Core Rule 4 (1.25 → 16/20/25/31/39); 1.333 for editorial and marketing pages |
| base_unit | 4 \| 8 (px) | 8 | Every spacing value becomes a multiple of this; 4 for dense pro tools, 8 everywhere else |
| accessibility_target | AA \| AAA | AA | AA floors are 4.5:1 body and 3:1 large text; AAA raises them to 7:1 and 4.5:1 across all checks |
| platform | web \| ios \| android \| print | web | Switches units (px/pt/dp), touch-target minimums (44pt HIG / 48dp Material), and platform conventions in `references/ui-screens.md` and `references/documents.md` |
| brand_file | path | none | Palette, typefaces, and logo rules read from `<state_root>/brand.md`; overrides the derivation procedures in `references/palettes.md` and `references/fonts.md` |

Preference areas to record as the user reveals them:

- **output medium** — HTML/CSS vs image render vs written spec; framework in use (Tailwind, vanilla CSS) — affects what the deliverable looks like
- **aesthetic register** — minimal, dense, editorial, playful — shifts spacing generosity, type choices, and decoration tolerance
- **motion posture** — full motion vs reduced by default — gates Core Rule 8 and all transition suggestions
- **language and script** — RTL layouts mirror scan order; CJK needs looser line-height and no italic emphasis — affects `references/layout.md` and `references/fonts.md` guidance
- **critique style** — ranked punch-list vs annotated walkthrough — affects how `references/critique.md` findings are delivered

## When To Use

- Designing any visual artifact from scratch: UI screens, landing pages, slides, social graphics, posters, emails, PDFs.
- Fixing a design that "looks off" when the user cannot articulate why.
- Choosing typography, spacing, or a palette for a project that has no design system yet.
- Reviewing generated HTML/CSS or rendered images before delivery.
- Not for token pipelines and component libraries (design-system) or brand positioning (branding).

## Quick Reference

| Situation | Play |
|---|---|
| Design looks cluttered | Delete decoration first, then double the gap between groups; use whitespace to organize instead of adding boxes (→ `references/critique.md`) |
| "Looks off," cause unknown | Run gates in order: grayscale, squint, alignment count (→ Output Gates); full symptom chains in `references/critique.md` |
| Everything looks equally important | Rank all content 1-3; style only rank 1 as prominent, demote the rest to body style |
| Picking fonts | One family, weights 400/700; add a second family only to split display vs text roles (→ `references/fonts.md`) |
| Picking colors | 60-30-10 split; one accent hue; neutrals tinted with 2-5% of the accent's saturation (→ `references/palettes.md`) |
| Text hard to read | Check measure 45-75ch, line-height 1.5, contrast 4.5:1 before blaming the typeface |
| Mobile layout | 44pt/48dp touch targets, 16px minimum body (also prevents iOS input zoom), primary actions in bottom thumb zone |
| Slide deck | One idea per slide, 24pt text floor, max 6 lines of text per slide (→ `references/slides.md`) |
| Poster, thumbnail, social post | One-glance artifact: single message, readable at 10% zoom (→ `references/graphics.md`) |
| Form, table, or dashboard | Component-level rules in `references/ui-screens.md` |
| Chart or data display | Zero-baseline bars, direct labels, one hue for magnitude (→ `references/data-viz.md`) |
| HTML email | Tables and inline CSS, 600px body, Outlook renders with Word (→ `references/email.md`) |
| Dark mode requested | Not inversion: lighten surfaces to show elevation, desaturate accents 10-20%, white text at ~87% opacity (Material) (→ `references/dark-mode.md`) |
| Contrast, CVD, motion sensitivity | Floors and non-color encodings in `references/accessibility.md` |
| Print or PDF deliverable | 300 DPI, bleed, CMYK, margins (→ `references/documents.md`) |
| Any other visual task | Apply Core Rules in order 1-7: hierarchy, then spacing, then type, then color |

## Progressive Disclosure

Load specific references based on the current task:
- **Setup & memory**: Load `references/setup.md` on first use or preference capture; `references/memory.md` defines the memory file shape under `<state_root>`.
- **Analysis**: Load `references/critique.md` when diagnosing cluttered or flat designs.
- **Typography & Color**: Load `references/fonts.md` for pairings and `references/palettes.md` for building color systems.
- **Layout & Structure**: Load `references/layout.md` for grids and responsive behavior.
- **Artifact Types**: Load `references/ui-screens.md` (forms/tables), `references/landing-pages.md` (marketing), `references/slides.md` (decks), `references/graphics.md` (posters/social), `references/documents.md` (print/PDF), `references/email.md` (HTML email), or `references/data-viz.md` (charts) depending on the target format.
- **Adaptations & Compliance**: Load `references/dark-mode.md` for theming and `references/accessibility.md` for WCAG contrast and focus checks.

## Core Rules

1. **Hierarchy is a ranking, not a styling pass.** Inventory every element, rank each 1-3 by user importance (1 = must see, 2 = supporting, 3 = metadata). Exactly one rank-1 per view. Check: a grayscale screenshot must reveal the ranking in 3 seconds.
2. **Spend one channel per level step.** Adjacent hierarchy levels differ by one full step in ONE channel: size x1.25, weight +300 (400 to 700), or a clear lightness jump. Three small tweaks read as noise. Example: 18px/600 next to 16px/400 body is two half-steps and ranks poorly; use 20px/400 or 16px/700 instead.
3. **Spacing: base 8, factor 2 between grouping levels.** Scale 4/8/16/24/32/48/64 (multiples of `base_unit`). Between-group gap >= 2x within-group gap: 8px label-to-field, 24px field-to-field, 48px section-to-section. Proximity groups content more cheaply than any border or background box.
4. **Type floors: 16px body, 1.5 line-height, 45-75ch measure.** Bringhurst's 66ch is the target; under 45ch the eye jumps lines, over 75ch it loses the return sweep. Headings tighten to 1.1-1.3. Ratio `type_scale_ratio` = 1.25 gives 16/20/25/31/39 and covers most product work; 1.333 for editorial and marketing pages.
5. **Color: 60-30-10 with contrast floors.** ~60% neutral surface, ~30% secondary, ~10% accent, and the accent marks interactive or state-bearing elements only. WCAG floors: 4.5:1 body text, 3:1 large text (24px+, or 19px bold) and UI component boundaries. Use near-black (#111 to #1a1a1a) on #FFF instead of pure #000; near-black cuts edge vibration.
6. **Every edge answers to a line.** Target <= 3 distinct vertical alignment lines per view; each extra line adds perceived clutter. Center only display text of 1-3 lines; left-align everything longer, because ragged-right gives the eye a fixed return point.
7. **Design in grayscale first.** Layout, hierarchy, and spacing must work with zero color. Add color last to encode meaning (state, action, brand); color used to rescue hierarchy fails for the ~8% of men with color vision deficiency and fails the grayscale gate.
8. **Motion: 150-300ms for UI transitions.** Ease-out on entry, ease-in on exit. Over 400ms reads as lag; under 100ms reads as a glitch. Animate only transform and opacity for smooth playback; honor reduced-motion preferences (`references/accessibility.md`).

## Hierarchy Procedure

1. Content inventory before any styling: list every element the view must contain, including legal text and empty states.
2. Rank each element 1-3. If two elements demand rank 1, split the view or demote one by position (top-left beats bottom-right in LTR scan order).
3. Assign styles top-down from the type scale. Demote rank 3 by lightness (40-60% gray on white), not by shrinking below 13px, where legibility collapses.
4. Place rank 1 in the natural entry point: top-left for documents, visual center for posters and slides.
5. Verify with the Output Gates before delivering.

## Spacing and Layout

- Macro before micro: set page margins and section gaps before touching padding inside components.
- Text content containers: 560-600px max width (keeps measure at 70-75ch at 16px, inside the 45-75ch range). Dashboards run full-width with 24px outer margins.
- Space belongs to what it labels: a heading sits closer to the text below it than to the section above (e.g. 8px below, 32px above). Equal gaps destroy grouping.
- Optical beats mathematical: icons, triangles, and play buttons need a 1-3px shift toward their visual weight to look centered. Grid math and column layouts: `references/layout.md`.
- Whitespace is the grouping mechanism. Filling "empty" corners with decoration deletes the structure the space was providing.

## Type and Color Execution

- Pair typefaces by role contrast (display serif + text sans), never by similarity; two near-identical sans faces read as a rendering mistake. Selection tables and loading: `references/fonts.md`.
- Skip adjacent weights: 400 vs 500 is indistinguishable at body sizes. Use 400/600 or 400/700.
- ALL CAPS only for labels of 1-2 words, with +5-10% letterspacing. Keep lowercase body text tracking at 0; it breaks the word shapes readers scan by.
- Palette derivation: pick the accent hue, build a 9-step lightness ramp from it, then tint neutrals with 2-5% of the accent's saturation. Pure grays next to a saturated accent look dirty. Full procedure: `references/palettes.md`.
- Semantic color is reserved: red for destructive and error, green for success. A red brand needs error states distinguished by a different shade plus an icon; always pair hue with an icon, label, weight, or position.
- One radius scale per artifact (e.g. 4/8/16). Mixed radii on sibling elements is the fastest tell of unreviewed generated UI.

## Output Gates

Run before delivering any visual artifact:

- Grayscale test: desaturated, is the 1-3 ranking still obvious in 3 seconds?
- Squint test: blurred, do exactly the title and the primary action pop?
- Alignment count: <= 3 vertical alignment lines, and every element sits on one?
- Spacing audit: every gap a multiple of the base unit, between-group >= 2x within-group?
- Contrast check: every text/background pair meets its floor (4.5:1 body, 3:1 large/UI)?
- Single rank-1: exactly one primary action or focal point per view?

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Boxes and borders to separate content | Each border is added noise; proximity groups for free | Remove the box, double the between-group gap |
| Shrinking text to fit the space | Below 13px legibility collapses; the content problem remains | Cut content, paginate, or widen the container |
| Centering long text | No fixed return point for the eye, each line restart costs a search | Left-align; center only 1-3 line display text |
| Emphasizing with bold + bigger + colored at once | Burns all channels on one level; nothing is left to mark the true top rank | One channel per level step (→ Core Rule 2) |
| Color as the only state signal | Fails grayscale, print, and ~8% of male users | Encode with icon, weight, or position first; color reinforces |
| Pure gray neutrals beside a saturated accent | Grays pick up a dirty, mismatched cast by contrast | Tint neutrals with 2-5% of the accent hue |
| Filling every empty area | Whitespace was doing the grouping; filling it flattens hierarchy | Leave it; if it feels empty, the content ranking is wrong, not the space |
| Restyling before ranking | Polishing elements in place cements a flat hierarchy | Content inventory and 1-3 ranking first (→ Hierarchy Procedure) |
| Designing only the happy state | Empty, loading, error, and overflow states ship broken | Design the four non-happy states before polishing the happy one (`references/ui-screens.md`) |
| Checking one theme only | A palette tuned in light mode breaks contrast in dark | Run the Output Gates once per theme (`references/dark-mode.md`) |

## Where Experts Disagree

- **Pure black (#000) dark backgrounds.** OLED-first designers use #000 for power and contrast; Material argues #121212 reduces halation and lets shadows exist. Default #121212; go #000 only when the artifact targets OLED media consumption (video, photo feeds).
- **Grid math vs optical judgment.** Systematists snap everything to the 8px grid; typographers override math wherever the eye disagrees (icon centering, display-type spacing). Default: grid for layout; allow optical corrections only at the component level — never the reverse.
- **System fonts vs webfonts.** System stacks cost zero load time and feel native; a webfont earns its bytes only when type IS the brand voice (marketing, editorial). Product UI defaults to a system stack or one variable font.
- **Minimal vs dense.** Consumer surfaces reward whitespace; daily-use pro tools reward density (more data per scroll, `base_unit` 4). The boundary is usage frequency, not taste: daily expert use → dense wins.
