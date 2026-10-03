# Sources - Apple Maps (macOS)

Verified full URLs used for Gate 6 domain accuracy. Prefer these over model memory.

## Agent Skills format

- Agent Skills specification — frontmatter, progressive disclosure, optional directories via https://agentskills.io/specification
- Agent Skills document index — discovery entry point via https://agentskills.io/llms.txt
- skills-ref validator package — `uvx --from skills-ref agentskills validate` via https://github.com/agentskills/agentskills/tree/main/skills-ref

## Apple Maps URL schemes and parameters

- Apple Map Links (iPhone URL Scheme Reference) — `q`, `near`, `ll`, `z`, `saddr`, `daddr`, `dirflg`, `t` parameter semantics via https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/MapLinks/MapLinks.html
- MapKit documentation hub — related Apple maps platform surface via https://developer.apple.com/documentation/mapkit

## macOS Maps product guidance

- Maps User Guide for Mac — product workflows for search and directions via https://support.apple.com/guide/maps/welcome/mac
- Apple Support map-related article redirect target — supplemental consumer guidance via https://support.apple.com/en-us/105132

## Notes retained from research

- Directions need `daddr`; omitting `saddr` means start from "here".
- `dirflg` values used by this skill: `d` driving, `w` walking, `r` transit.
- Prefer `open -a Maps "https://maps.apple.com/..." ` over browser-only opens or UI scripting.
