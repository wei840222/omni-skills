---
name: google-fonts
description: "Load and optimize Google Fonts: display=swap, preconnect, exact weights, variable fonts, subsetting, proven pairings, and GDPR-aware self-hosting. Use when choosing or wiring web fonts from Google Fonts, reviewing font performance, or deciding whether to self-host. Not for general typographic measure/leading (typography) or CSS layout systems (css)."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔤"}'
  related-skills: '{"typography":"Measure, leading, tracking, and optical scale once the font files are chosen.","css":"@font-face, font-display, and CSS delivery details around the selected fonts.","branding":"Brand voice and visual identity that constrain font choice."}'
---

## State location

This skill is stateless and does not store local configuration or persistent user state.

## When to Use

- Loading Google Fonts with performance-safe HTML/CSS snippets
- Choosing weights, variable axes, subsets, or proven pairings
- Deciding whether CDN Google Fonts or self-hosting is appropriate for privacy

Redirect measure/leading/tracking questions to `typography`. Redirect pure CSS layout or `@font-face` mechanics without Google Fonts selection concerns to `css`.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Loading Mistakes | `references/loading-mistakes.md` | When optimizing Google Fonts loading code and CSS links |
| Variable Fonts | `references/variable-fonts.md` | When selecting multiple weights and aiming to reduce payload size |
| Subsetting | `references/subsetting.md` | When loading fonts for non-English languages or specific character subsets |
| Proven Pairings | `references/font-pairings.md` | When designing typography and selecting combinations of fonts |
| Font Selection | `references/font-selection.md` | When deciding which font family to use for reading, UI, or headings |
| Common Mistakes | `references/common-mistakes.md` | When verifying typography implementation and reviewing font usage |
| Self-Hosting | `references/self-hosting.md` | When addressing privacy regulations (GDPR) or local hosting needs |
| Domain Knowledge | `references/domain-knowledge.md` | When needing fundamental context on web typography and font formats |
