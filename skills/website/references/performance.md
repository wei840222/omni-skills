# Performance and Core Web Vitals

Load when optimizing load speed, lab/field metrics, fonts, scripts, or LCP candidates.

## Metrics that matter

| Metric | What it measures | Practical target mindset |
|---|---|---|
| **LCP** | Largest contentful paint | Optimize hero image/text; reduce TTFB and render-blocking work |
| **CLS** | Layout shift | Reserve space for media/ads/embeds; avoid late font swaps without fallback metrics |
| **INP** | Interaction to next paint | Keep event handlers short; break long tasks; defer non-critical work |

FID is legacy; prefer INP for interaction responsiveness.

## Image delivery

- Serve modern formats (AVIF/WebP) with sensible fallbacks.
- Lazy-load below-the-fold images (`loading="lazy"`); keep the LCP image eager and high-priority when needed (`fetchpriority="high"` on the hero only).
- Always pair intrinsic dimensions or CSS `aspect-ratio` with responsive `srcset`/`sizes`.
- Compress to the display size; do not ship 4000px assets into a 400px slot.
- For deeper format/compression pipelines, hand off to `image`.

## CSS and fonts

- Inline a small critical CSS bundle for above-the-fold content; defer the rest.
- Avoid huge unused frameworks on content sites; purge or split by route.
- Preload one critical font file max; use `font-display: swap` or optional for non-brand text.
- Prefer system or variable fonts when brand allows — fewer requests, less CLS from late swaps.

## JavaScript and third parties

- Default to less JS. Static or server-rendered HTML first.
- Mark analytics/chat/A-B tags `async` or `defer`; load chat widgets after idle or first interaction when business allows.
- Audit third parties in coverage/network panels; remove dead tags.
- Long tasks (>50ms) on interaction paths are INP risks — split work or move off the critical path.

## Measurement workflow

1. Lab: Lighthouse (mobile + desktop) in a clean browser profile.
2. Field: CrUX / RUM when available; lab-only green is not production proof.
3. Re-test after each change set; one variable at a time for regressions.
4. Document the before/after metric the user cares about (LCP ms, CLS score, INP ms).
