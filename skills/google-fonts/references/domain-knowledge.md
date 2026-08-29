## Domain Knowledge: Google Fonts and Web Typography

## What This Skill Covers

Google Fonts is a CDN-backed catalog of open web fonts. This skill focuses on the load path, payload choices, and privacy trade-offs that most often create invisible text, oversized downloads, or GDPR risk when agents wire fonts into pages.

## Stable Domain Facts

- `display=swap` (or equivalent `font-display: swap`) keeps text visible while fonts load.
- Unused static weights and unused subsets increase transfer size without changing rendered glyphs.
- Variable fonts can replace many static weight files with one axis-range file when the family supports it.
- CDN Google Fonts requests go to Google infrastructure and therefore expose visitor IPs; self-hosting keeps font delivery first-party.

## Corrected / Tightened Guidance

- Prefer exact weight lists (`wght@400;600;700`) over "load everything".
- Prefer variable axis ranges (`wght@100..900`) only when the family is marked variable and the design actually needs the range.
- Treat `google-webfonts-helper` as a practical download helper for self-hosting, then serve with first-party `@font-face` + `font-display: swap`.
- Keep pairings practical: one display/heading face + one text face, or a single UI family with weight hierarchy.

## Sources

### Google Fonts delivery
- Get Started with the Google Fonts API — HTML link patterns and basic loading via https://developers.google.com/fonts/docs/getting_started
- CSS API (v2) — axis syntax, multiple families, and modern CSS2 query form via https://developers.google.com/fonts/docs/css2
- Google Fonts privacy FAQ — CDN privacy implications and self-hosting guidance via https://developers.google.com/fonts/faq/privacy

### Variable fonts and helpers
- Google Fonts Knowledge: Variable fonts glossary — axis model and variable badge meaning via https://fonts.google.com/knowledge/glossary/variable_fonts
- google-webfonts-helper — download helper for self-hosted Google Fonts files via https://gwfh.mranftl.com/fonts
