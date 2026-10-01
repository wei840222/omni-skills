# Performance, SEO basics, and accessibility

Load for Core Web Vitals, image delivery, launch SEO tags, and a11y minimums. Deep ranking → `seo`. Deep image pipelines → `image`.

## Core Web Vitals

| Metric | Practical target mindset | How to improve |
|--------|--------------------------|----------------|
| **LCP** | Largest content paints quickly | Optimize hero image/text, TTFB, reduce render-blocking CSS/JS |
| **INP** | Interactions stay responsive | Break long tasks, defer non-critical JS, keep handlers short |
| **CLS** | Layout stays stable | Explicit image/video dimensions or `aspect-ratio`; reserve ad/embed space |

**FID is legacy.** Prefer **INP** for interaction responsiveness (web.dev Core Web Vitals guidance).

## Image optimization

- Prefer AVIF/WebP with sensible fallbacks; JPEG for photos when needed; PNG mainly for true transparency needs.
- Serve display-sized assets — do not ship 2000px into a 200px slot.
- Lazy-load below-fold images (`loading="lazy"`); keep the LCP candidate eager; consider `fetchpriority="high"` only on the true hero.
- Always include intrinsic `width`/`height` or CSS `aspect-ratio` to protect CLS.
- Framework helpers (e.g. Next.js `<Image>`) help when configured; they are not magic without sizes/domains setup.

## JavaScript and CSS performance

- Mark non-critical scripts `defer` / `async`, or load after hydration/idle.
- Code-split routes and heavy widgets.
- Prefer ES module graphs that tree-shake; avoid mega default imports from barrels.
- Batch DOM reads then writes to limit layout thrashing.
- Inline a small critical CSS path when LCP is CSS-bound; defer the rest.

## SEO essentials (launch hygiene)

- Unique `<title>` per page (~50–60 characters as a practical bound, not a hard law)
- Meta description that earns the click without stuffing
- One clear `<h1>`; sequential heading levels
- Canonical URL when duplicates exist
- Open Graph basics: `og:title`, `og:description`, `og:image`
- `sitemap.xml` + coherent `robots.txt` (do not accidentally `Disallow` important paths)
- Hand off keyword strategy, link building, and recovery work to `seo`

## Accessibility minimums

- Full keyboard path for interactive controls; visible focus (`:focus-visible` ok)
- Text contrast ≥ **4.5:1** normal, ≥ **3:1** large (WCAG reference targets)
- Descriptive `alt` for content images; `alt=""` for decorative
- Every input has an associated `<label>` (placeholders are not labels)
- Use ARIA only when native HTML semantics are insufficient
- Do not skip heading levels for visual style

## Measurement workflow

1. Lab: Lighthouse in a clean profile (extensions skew scores).
2. Field: CrUX / RUM when available — lab green is not production proof.
3. Change one variable set at a time; record before/after LCP, CLS, INP.
4. Re-test mobile and desktop when layout differs.

## Critical rules

- **Images need dimensions** — missing width/height is a common CLS failure.
- **INP not FID** — update stale checklists that still optimize First Input Delay only.

## Common requests

- **"Improve performance"** → Lighthouse + field if possible; fix LCP element, CLS space, long tasks on INP paths; lazy-load below-fold media.
- **"Add SEO"** → titles/descriptions, semantic HTML, OG, sitemap/robots; escalate ranking strategy to `seo`.
