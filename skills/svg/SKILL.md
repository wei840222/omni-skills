---
name: svg
description: >
  Create, review, and optimize SVG markup with correct viewBox scaling,
  accessibility, currentColor theming, embedding choices, and SVGO-safe
  configs. Use when writing or fixing inline icons/charts, exported Figma/
  Illustrator SVG, screen-reader titles, CSS color inheritance, sprite
  `<use>` patterns, or when optimization strips viewBox/title. Prefer
  `icons` for product icon systems, `css` for page layout/cascade, `html`
  for document semantics, `image` for raster formats, and `figma` for
  canvas export mechanics.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📐"}'
  related-skills: '{"icons":"Product UI icon systems, sizing, and performance once SVG primitives are correct.","css":"Page layout, cascade, and stylesheet architecture around SVG presentation.","html":"Document semantics, embeds, and non-SVG accessibility patterns.","design":"Visual hierarchy and multi-surface design critique beyond SVG markup.","figma":"Figma export, vectors, and Dev Mode handoff that produce SVG assets.","image":"Raster formats (WebP/AVIF/PNG) rather than vector SVG markup."}'
---

# SVG

Author and harden **vector SVG** for the web: scaling, a11y, theming, embedding, and safe optimization. Keep optional preferences under portable `<state_root>`; the skill package stays read-only.

## State location

SVG preferences may exist in `<workspace>/svg/`, `<workspace>/memory/svg/`, or `~/svg/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/svg/`, `<workspace>/memory/svg/`, `~/svg/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and preferences must be created, default to `<workspace>/svg/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/svg/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Never treat the literal string `<state_root>` as a filesystem path. Never write learned preferences into `SKILL.md`.

Default preference file: `<state_root>/memory.md` (create on first authorized write). Load `references/state.md` for the template sections.

## Workflow

1. Classify the ask: new icon/chart, export cleanup, a11y fix, theming, embedding choice, or SVGO pass.
2. Resolve `<state_root>` only when preferences or prior defaults matter; otherwise stay stateless.
3. Apply the minimum viable SVG defaults below, then load only the matching reference.
4. Verify the output still has `viewBox` (and `title`/`role` when informative) after any optimize step; if missing, restore them before shipping.
5. Hand off sibling work: product icon systems → `icons`; layout/CSS architecture → `css`; document semantics → `html`; Figma canvas issues → `figma`; raster delivery → `image`.

| Need | Load |
| --- | --- |
| Defaults, checklist, common traps | `references/domain.md` |
| viewBox, units, preserveAspectRatio, export offsets | `references/viewbox.md` |
| Informative vs decorative, title/desc, ID collision | `references/accessibility.md` |
| Inline / img / sprite / object trade-offs | `references/embedding.md` |
| currentColor, hardcoded fills, multi-color tokens | `references/styling.md` |
| SVGO overrides, size checks, icon-count strategy | `references/optimization.md` |
| Preference template under `<state_root>` | `references/state.md` |
| Verified specs and fragile claims | `references/sources.md` |

## Minimum viable SVG

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img">
  <title>Close</title>
  <path d="M18 6L6 18M6 6l12 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>
```

- Prefer `viewBox` for scaling; drop fixed `width`/`height` when the container should own size.
- Informative graphics: `role="img"` plus a first-child `<title>` (or `aria-labelledby`); decorative: `aria-hidden="true"` and `focusable="false"`.
- Themeable icons: inherit with `currentColor` and keep path fills free of hard-coded hex when theming is required.
- External `.svg` files keep the SVG namespace; inline HTML5 SVG may omit it but keeping it is safe.
- After SVGO, re-check that `viewBox` and accessibility titles survived.

## Failure branches

| Condition | Action |
| --- | --- |
| Missing `viewBox` after export/optimize | Restore `viewBox="min-x min-y width height"`; re-run optimize with `removeViewBox: false` |
| Screen reader announces filename or nothing | Switch informative SVG to `role="img"` + `<title>`; for `<img src>`, set meaningful `alt` |
| CSS color does not affect icon | Use inline SVG (or careful sprite), remove hard-coded `fill`/`style` on paths |
| Duplicate `id` across inline icons | Namespace title/clip IDs per instance |
| Optimize removed title/desc | Override `removeTitle` / `removeDesc` (and related) in SVGO config, then re-verify |
| User wants raster compression only | Hand off to `image` |

## Safety defaults

- Treat untrusted SVG as markup: sanitize script/event handlers before embedding third-party paths.
- Do not invent browser support matrices or SVGO plugin defaults from memory; re-check `references/sources.md` when claims are version-sensitive.
- Keep preference writes inside `<state_root>/` with consent; never commit runtime memory into the package.
- Load at most one deep reference per step; keep always-on defaults in this file only.
