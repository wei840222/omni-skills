---
name: website
description: Build and harden fast, accessible, SEO-friendly websites with modern HTML/CSS architecture, Core Web Vitals, mobile-first layout, and launch checks. Use when the user wants to create a site, audit web performance, fix accessibility gaps, structure semantic markup, ship Open Graph/sitemap basics, or review pre-launch readiness. Not for deep ranking strategy (`seo`), pure stylesheet debugging (`css`), markup-only form/ARIA deep dives (`html`), icon implementation (`icons`), or image-asset pipelines (`image`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"seo":"Organic ranking strategy, Search Console recovery, keyword research, and schema beyond basic launch tags.","html":"Deep semantic markup, forms, dialogs, and sanitization details.","css":"Cascade, layout bugs, container queries, and stylesheet architecture.","frontend":"React/Next/Tailwind UI systems and component polish.","icons":"Accessible SVG icon patterns and touch targets.","image":"Format choice, compression, and responsive image delivery.","typography":"Measure, leading, and type-scale decisions that feed site readability."}'
---

## State location

This skill is **stateless**. It does not store local configuration, caches, or persistent project data. Skill resources live under `references/`; never invent a filesystem state root for this package.

## When to use

- User wants to build or restructure a marketing, brochure, or content website
- Performance, accessibility, mobile layout, or semantic HTML review
- Pre-launch checklist: favicon, OG tags, sitemap, 404, forms, uptime
- Core Web Vitals coaching (LCP, CLS, INP) without a full SEO campaign
- Route away when the ask is pure ranking strategy (`seo`), React app architecture (`frontend`), stylesheet debugging only (`css`), or image-file optimization only (`image`)

## Operating loop

1. **Clarify surface** — static page, multi-page site, or app shell; keep advice proportional.
2. **Preserve working content** — prefer progressive enhancement; core content must work without JS.
3. **Load depth on demand** — use the quick reference table; open only the needed reference file.
4. **Ship measurable fixes** — name the metric or a11y failure, the change, and how to re-check (Lighthouse, axe, keyboard).
5. **Hand off specialists** — ranking recovery → `seo`; complex CSS bugs → `css`; icon-only controls → `icons`; heavy media pipelines → `image`.

## Quick reference

| Need | Action | Load |
|---|---|---|
| LCP / CLS / INP, fonts, third-party scripts | Apply CWV and performance rules | `references/performance.md` |
| Semantic landmarks, headings, buttons vs links | Fix document structure | `references/html-structure.md` |
| Contrast, labels, keyboard, alt text | Accessibility pass | `references/accessibility.md` |
| Viewport, touch targets, 320px width | Mobile-first layout | `references/mobile.md` |
| Cascade, units, Flex/Grid, print | CSS patterns | `references/css-patterns.md` |
| Favicon, OG, sitemap, 404, forms, uptime | Launch checklist | `references/launch.md` |
| Verifiable sources | Cite standards | `references/sources.md` |

## Core rules (always on)

### Performance

- Track Core Web Vitals: **LCP**, **CLS**, **INP** (not FID).
- Images are the top LCP risk — prefer WebP/AVIF, lazy-load below-the-fold, set explicit `width`/`height` (or CSS aspect-ratio) to prevent layout shift.
- Inline critical CSS; defer non-critical stylesheets.
- Third-party scripts: `async`/`defer`, audit regularly; delay non-essential widgets until interaction when possible.
- Fonts: `font-display: swap`, preload only the critical face; subset when payload is large.
- Measure with Lighthouse in a clean profile; extensions skew lab scores.

### Mobile first

- Write base styles for small screens; add complexity with `min-width` media queries.
- Touch targets ≥ **44×44 CSS px** (padding may expand the hit area).
- Test real devices; DevTools throttling misses device jank.
- Horizontal scroll at **320px** width is a release blocker.
- Require `<meta name="viewport" content="width=device-width, initial-scale=1">`.

### Accessibility

- Every meaningful `<img>` needs descriptive `alt`; decorative images use `alt=""`.
- Body text contrast ≥ **4.5:1**; large text ≥ 3:1.
- Form controls need associated `<label>` elements — placeholders are not labels.
- Full keyboard path: Tab/Shift+Tab, Enter/Space, Escape for dismissible UI; visible focus.
- Heading levels stay sequential (do not skip for styling).

### HTML structure

- One `<h1>` per page as the page title.
- Prefer landmarks: `<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`.
- `<button>` for in-page actions; `<a href>` for navigation — avoid clickable `<div>`.
- `target="_blank"` links include `rel="noopener noreferrer"`.
- Validate markup; broken HTML causes unpredictable a11y trees.

### CSS patterns

- Prefer fixing specificity over `!important`.
- Prefer relative units (`rem`, `em`, `%`, `svh`) for text and spacing that should scale.
- Define design tokens with CSS custom properties.
- Flexbox for 1D; Grid for 2D — pick the tool that matches the layout axis.
- Content must remain readable if CSS fails to load (progressive enhancement).

### Common mistakes

- Ship a real favicon to stop noisy icon 404 logs
- Set `<html lang="…">` so screen readers use the right pronunciation
- Use `https://` (or scheme-relative) links on HTTPS sites to avoid mixed content
- Keep core content available without JavaScript (progressive enhancement)
- Add `@media print` for receipts/articles people actually print

### Before launch

- Forms actually submit end-to-end
- Custom 404 that helps recovery
- Open Graph / Twitter card previews verified
- Sitemap submitted (Search Console / equivalent)
- Uptime monitoring on the production origin

## Progressive disclosure

Keep this file as the always-on checklist. Load reference files only when the user needs depth, examples, or source citations beyond the rules above.
