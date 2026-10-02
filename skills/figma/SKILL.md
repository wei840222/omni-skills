---
name: figma
description: >
  Build and debug Figma auto layout, components, variants, variables, modes,
  libraries, prototypes, and Dev Mode handoff. Use when fixing unresponsive
  frames, clipping text, lagging variant sets, broken library updates,
  theming/dark-mode transitions, blurry vectors, or slow files, or when
  scripting via plugins, REST API, or Dev Mode MCP. Prefer `design` for visual
  judgment, and keep token pipelines into platform code outside this skill.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎨","requires":{"config":["<state_root>"]}}'
  related-skills: '{"design":"Visual design judgment outside Figma file mechanics.","design-system":"Token and component architecture governing the file this skill implements.","ui":"Broader UI product patterns beyond Figma-specific mechanics.","vibe-design":"Exploratory visual direction when the ask is taste rather than file structure."}'
---

# Figma

Agent guidance for **in-file Figma mechanics**: auto layout, components/variants, variables/modes, libraries, Dev Mode handoff surfaces, plugins, and REST automation. Canvas work is **advise** (named panels, fields, shortcuts in click order); API/plugin work is **act-as**.

## State location

Figma preferences may exist in `<workspace>/figma/`, `<workspace>/memory/figma/`, or `~/figma/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/figma/`, `<workspace>/memory/figma/`, `~/figma/`.
3. If none exists and state must be created, default to `<workspace>/figma/`.

Use the selected `<state_root>` for every state operation in this skill.
Do not treat the literal string `<state_root>` as a filesystem path.
See `setup.md` on first use and `assets/memory-template.md` for the file format.
If older absolute paths still hold data, move them into the resolved `<state_root>/` and state the move in one line.

## When To Use

- Building or restructuring a file: auto layout, component sets, variables and modes, library architecture
- Debugging a file: a frame that will not resize, clipped text, a laggy variant set, a file that takes a minute to open
- Preparing handoff: Dev Mode annotations, Code Connect, Ready-for-dev scope, the sad-path states engineers otherwise invent
- Theming and tokens inside Figma: dark mode, brand and density modes, alias chains, plan-gated mode limits
- Automating: plugins, the REST API, the Dev Mode MCP server, bulk renames, unused-component audits
- Prefer `design` / `vibe-design` for visual judgment and taste; prefer `design-system` / `ui` for broader system or product UI work outside Figma file mechanics. Token pipelines that leave Figma into platform code, and external redline/spec review rituals, stay out of scope here. Dev Mode annotations, Code Connect, and Ready-for-dev scope stay in scope because they are built inside the file.

Mode: **act-as** through the API and plugin surfaces, **advise** on the canvas. Figma has no CLI, so canvas work is delivered as named panel fields and shortcuts the user executes, in click order (`shortcuts.md`); anything scriptable is delivered as plugin code or REST calls.

## Quick Reference

| Situation | Play |
|---|---|
| A frame won't grow or shrink | Fill child inside a Hug parent on the same axis — the size is undefined and Figma freezes it. Fix the outermost container first, then work inward (→ Sizing Modes) |
| Text clips, wraps wrong, or shows an unexpected ellipsis | Text node is Fixed size, or Max lines is set; switch to Auto height and let the parent Hug → `text.md` |
| Engineers say "it breaks on resize" | Absolute positioning where auto layout belongs; the screenshot was fine, the tree was not → `auto-layout.md` |
| Dark mode, brand themes, or density variants needed | One tree, a second mode on the color collection, every fill bound to a semantic alias → `variables.md` |
| A variant set lags when edited, or nobody can find a variant | Past the combinatorial ceiling; move uncoupled axes to boolean, text, and instance-swap properties (→ Component Property Types) → `components.md` |
| A library update broke consuming files | Review per component, review per component individually; use versioning for breaking changes rather than editing the main directly → `libraries.md` |
| Handoff churn: engineers rebuild instead of reusing | Components have no code identity — map them with Code Connect and annotate what code cannot infer → `dev-mode.md` |
| Prototype motion crossfades instead of moving | Smart Animate found no name-and-hierarchy match across the two frames → `prototyping.md` |
| Icons look blurry, misaligned, or export at the wrong size | Stroke alignment plus off-pixel bounds; export from a fixed keyline frame → `vectors.md` |
| Assets needed at @2x/@3x, mdpi→xxxhdpi, or as clean SVG | Export settings and density presets per platform → `export.md` |
| The file takes forever to open or edit | Rank the causes: raster images, vector node count, effects, layer count, fonts → `performance.md` |
| The same edit has to happen on 50 layers | 10+ repetitions justifies a plugin; read-only audits belong on the REST API → `plugins.md` |
| A pipeline needs the file's structure, tokens, or renders | Targeted node fetches, not whole-file pulls; webhook on library publish → `rest-api.md` |
| A feature seems missing from the UI | Plan gate, not a bug — modes, branching, Dev Mode, analytics and the Variables API are all tiered → `collaboration.md` |
| Contrast, focus order, or touch targets need speccing | Annotate what the visual layer cannot carry → `accessibility.md` |
| Speccing for iOS, Android, or a foldable | Densities, safe areas, system UI and touch minimums differ from web → `mobile.md` |
| Inherited a messy file, or importing from Sketch/XD | Inventory before editing; freeze a named version first → `audit.md` |
| A workshop, flow diagram, deck, site, or generated draft is the deliverable | FigJam, Slides and the newer publishing and generative surfaces are separate editors with their own object models and seat gates → `surfaces.md` |
| The fix is a canvas operation the user has to perform | Deliver panel, section, field and key in click order — always specify the exact click path → `shortcuts.md` |
| Anything else | Rebuild the smallest failing case in a fresh file with two frames. If it behaves there, the bug is this file's structure, not Figma |

## References

- Load `references/core-rules.md` to understand sizing modes, component properties, token layers, and core rules.

- Load `references/auto-layout.md` for sizing engine
- Load `references/components.md` for sets and properties
- Load `references/variables.md` for tokens and modes
- Load `references/libraries.md` for publishing and versioning
- Load `references/dev-mode.md` for handoff and Code Connect
- Load `references/prototyping.md` for flows and motion
- Load `references/text.md` for type mechanics
- Load `references/vectors.md` for icons and paths
- Load `references/export.md` for assets and densities
- Load `references/performance.md` for file health
- Load `references/plugins.md` for choosing and writing plugins
- Load `references/rest-api.md` for automation
- Load `references/collaboration.md` for plans, permissions, review
- Load `references/accessibility.md` for speccing a11y
- Load `references/mobile.md` for platform rules
- Load `references/audit.md` for rescuing a file
- Load `references/surfaces.md` for FigJam, Slides and the newer editors
- Load `references/shortcuts.md` for shortcuts, panel paths and click order.
- Load `references/best-practices.md` when setting up configurations, reviewing output gates, or encountering traps and expert disagreements.
- Load `references/sources.md` before asserting plan limits, API surface names, or accessibility thresholds that may drift.
