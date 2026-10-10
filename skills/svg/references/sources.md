# Verified sources (Gate 6)

Re-open these pages before restating version-sensitive claims. Retrieval window for this refactor: 2026-10-10.

## SVG geometry and packaging

- **SVG 2 coordinates / viewBox model** — normative coordinate system and viewport mapping via https://www.w3.org/TR/SVG2/coords.html
- **MDN `viewBox`** — authoring notes for min-x/min-y/width/height and scaling via https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/viewBox
- **Agent Skills specification** — package frontmatter and resource layout rules via https://agentskills.io/specification

## Accessibility

- **SVG accessibility techniques (W3C Note)** — text equivalents and structure guidance via https://www.w3.org/TR/SVG-access/
- **WAI Images tutorial** — informative vs decorative image decisions via https://www.w3.org/WAI/tutorials/images/
- **MDN `<title>` (SVG)** — accessible name pattern for graphics via https://developer.mozilla.org/en-US/docs/Web/SVG/Element/title
- **MDN ARIA `img` role** — when to expose a graphic as an image via https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/img_role

## Optimization

- **SVGO repository** — project entry and plugin ecosystem via https://github.com/svg/svgo
- **SVGO preset-default docs** — default plugin bundle behavior; override destructive plugins explicitly and verify output via https://svgo.dev/docs/preset-default/

## Fragile claims

- Do not assert a fixed SVGO plugin default matrix from memory; confirm against the preset-default docs for the installed SVGO major version.
- Browser quirks for external `<use>` CORS and legacy `xlink:href` should be re-checked against current MDN/SVG2 text when advising production sprites.
- Performance timings in older skill drafts are illustrative only; measure on the target page rather than quoting historical ms tables as fact.
