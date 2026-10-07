# GIF Sources (verified defaults)

Record of primary sources used to ground this skill. Re-check live docs before asserting version-specific API fields or legal thresholds.

## Agent Skills format

- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices)
- [Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)

## FFmpeg / encoding

- [FFmpeg filters documentation (palettegen)](https://ffmpeg.org/ffmpeg-filters.html#palettegen)
- [FFmpeg filters documentation (paletteuse)](https://ffmpeg.org/ffmpeg-filters.html#paletteuse)
- Practical default retained from domain practice: fps 8–12, width 320–480, always palettegen+paletteuse for full-color sources.

## Optimization tooling

- [Gifsicle home](https://www.lcdf.org/gifsicle/) — optional post-optimizer; `-O3` and lossy modes are tool features, not a guarantee of a fixed size ratio on every input.

## Provider APIs

- [Giphy API endpoints](https://developers.giphy.com/docs/api/endpoint/#search) — search requires an API key; response includes multiple image renditions under each GIF object.
- [Tenor API endpoints](https://developers.google.com/tenor/guides/endpoints) — v2 search via `https://tenor.googleapis.com/v2/search` with `key` query param.

## Accessibility

- [WCAG 2.2 Understanding: Pause, Stop, Hide (2.2.2)](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- [WCAG 2.2 Understanding: Three Flashes or Below Threshold (2.3.1)](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)
- [MDN: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)

## Delivery guidance (stable domain)

- Muted autoplay looping `<video>` is widely used as a lighter web alternative to large animated GIFs; exact size savings vary by content—measure the actual encode rather than citing a fixed percentage as a guarantee for every asset.
