# Sources

Cite these pages when repeating a ratio, a draft-spec claim, or a color-space rule. Re-measure any hex pair; do not copy a ratio from memory.

## WCAG 2.2 contrast and use of color

- W3C, WCAG 2.2 Recommendation — normative criteria index: https://www.w3.org/TR/WCAG22/
- Understanding SC 1.4.3 Contrast (Minimum), Level AA — 4.5:1 normal text, 3:1 large text: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- Understanding SC 1.4.6 Contrast (Enhanced), Level AAA — 7:1 normal text, 4.5:1 large text: https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html
- Understanding SC 1.4.11 Non-text Contrast, Level AA — 3:1 for UI components and meaningful graphics: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- Understanding SC 1.4.1 Use of Color, Level A — color is not the only visual means of conveying information: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html

## APCA / WCAG 3 draft contrast research

- W3C WCAG 3.0 Working Draft — exploratory next-generation guidance (not a drop-in legal replacement for WCAG 2.x): https://www.w3.org/TR/wcag-3.0/
- W3C Silver Visual Contrast of Text subgroup notes (APCA research context): https://www.w3.org/WAI/GL/task-forces/silver/wiki/Visual_Contrast_of_Text_Subgroup
- Myndex SAPC-APCA reference implementation and documentation: https://github.com/Myndex/SAPC-APCA

## Color spaces and tokens

- CSS Color Module Level 4 — `oklab` / `oklch` and modern color functions: https://www.w3.org/TR/css-color-4/
- OKLCH color picker and perceptual lightness explainer: https://oklch.com/
- Design Tokens Community Group, DTCG format draft — portable token file shape: https://www.designtokens.org/tr/drafts/format/

## Worked contrast check (this refactor)

Relative-luminance formula from WCAG 2.x against sRGB hex pairs (independent recompute, 2026-10-07):

| Background | Foreground | Approx. contrast ratio | AA body text (4.5:1) |
|------------|------------|------------------------|----------------------|
| `#F3F4F6`  | `#9CA3AF`  | ~2.31:1                | Fail                 |
| `#F3F4F6`  | `#4B5563`  | ~6.87:1                | Pass                 |
