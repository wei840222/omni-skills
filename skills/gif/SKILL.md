---
name: gif
description: >
  Search, create, optimize, and ship accessible GIFs with FFmpeg palettegen,
  optional gifsicle compression, and Giphy/Tenor lookups. Use when converting
  video clips to GIF, choosing GIF vs MP4/WebM, searching reaction GIFs, or
  applying WCAG pause/reduced-motion/alt-text rules. Not for general video
  packaging (`video`), raw codec deep-dives (`ffmpeg`), or static image export
  (`image`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎞️","requires":{"bins":["ffmpeg"]}}'
  related-skills: '{"ffmpeg":"Lower-level codec, filter, and encoding details when palette or seek flags need precise FFmpeg control.","image":"Static image format, compression, and delivery decisions when the artifact is not an animated GIF.","video":"Platform packaging, trim/convert pipelines, and non-GIF delivery when MP4/WebM is the better output."}'
---

## When to use

Use when the primary artifact is an animated GIF or a short looping clip that must stay GIF-compatible: create from video, optimize size/colors, search Giphy/Tenor, or enforce accessibility before shipping.

Prefer sibling skills when the job is broader:

- `video` for platform delivery limits, multi-step packaging, or MP4/WebM-first exports
- `ffmpeg` for raw codec/filter expertise beyond GIF recipes
- `image` for still-frame, screenshot, or non-animated web assets

## Requirements

**Required for creation:**

- `ffmpeg` — video → GIF with palettegen/paletteuse

**Optional:**

- `gifsicle` — post-optimization (often 30–50% smaller)
- `ffprobe` — inspect source duration/resolution before convert
- `GIPHY_API_KEY` — Giphy search API
- `TENOR_API_KEY` — Tenor search API

Never print full API keys in logs, commits, or chat. Use env vars and redacted examples only.

## Critical rules

1. Prefer short clips (typically ≤5–8s) at 8–12 fps and 320–480px width unless the user requires more.
2. Always use a palette pipeline (`palettegen` + `paletteuse`); bare GIF encode washes out colors.
3. Prefer MP4/WebM loop embeds for web delivery when the audience can play video; GIF is for chat, email, or forced-GIF surfaces.
4. Inspect source with `ffprobe` when available before encoding (duration, resolution, rotation).
5. Apply accessibility before delivery: pause control for long loops, `prefers-reduced-motion` static fallback, descriptive alt text, no >3 flashes/second.
6. Process only user-provided files or URLs; upload private media to third-party APIs only with explicit consent.
7. After encode, verify output exists, duration/frame sanity, and approximate size before claiming success.

## Fast path

1. Clarify goal: search existing GIF, create from video, optimize an existing GIF, or accessibility review.
2. If creating: confirm input path, start time, duration, max width, and size budget.
3. Load only the matching reference from the table below—do not preload every file.
4. Run the smallest safe command path; optimize with gifsicle when installed.
5. Validate output + accessibility notes; offer MP4/WebM alternative when GIF is oversized.

## When to load references

| Need | File |
|------|------|
| FFmpeg create, palette, gifsicle, size traps | `references/creation-and-optimization.md` |
| Giphy/Tenor/Imgur search and API shapes | `references/sources-and-apis.md` |
| WCAG pause, reduced motion, alt, seizure risk | `references/accessibility.md` |
| Normative URLs and verified defaults | `references/sources.md` |

## Decision defaults

| Situation | Default | Why |
|-----------|---------|-----|
| Chat/reaction GIF | 320–480w, 8–12 fps, ≤5s | Keeps files small on mobile |
| Demo/UI loop | 480w, 10 fps, pause control if >5s | Readable UI without huge payloads |
| Web hero animation | Prefer muted loop MP4/WebM | Often 80–90% smaller than GIF |
| Washed-out colors | Rebuild with palettegen/paletteuse | GIF needs an explicit palette |
| Still oversized after encode | gifsicle `-O3 --lossy` + fewer colors | Secondary compression pass |

## Boundaries

- Do not invent API keys, paid plan limits, or provider pricing.
- Do not treat search result URLs as free-to-redistribute assets; respect provider and creator terms.
- Do not claim gifsicle ran if the binary is missing; skip and report.
- Do not substitute shell cwd for a host workspace path when writing outputs; use the path the user named.
