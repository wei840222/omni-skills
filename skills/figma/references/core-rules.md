# Figma Core Rules

## Core Rules

1. **Fill by default; Fixed only for genuinely fixed dimensions.** Every typed px is a future bug report. Fixed is right for icon frames, avatars, and rail widths; everything else is Fill with min/max clamps. A Fill child in a Hug parent on the same axis has no defined size — resolve sizing outside-in, always outside-in.
2. **Bind components exclusively to semantic tokens.** The chain is `component/button/bg` → `semantic/bg/accent` → `primitive/blue/500` → raw value. Bind the button straight to `blue/500` and retheming becomes a find-and-replace across every instance in every file; with the chain it is one value edit at the bottom.
3. **Cap the variant set; move the rest to properties.** `total variants = product of every axis kept as a variant`; a property costs 1, not a multiplier. A button set carrying four states, three sizes, three emphases, a leading icon and a trailing icon is 4 × 3 × 3 × 2 × 2 = 144 variants — unusable to browse and slow to edit. Above roughly 40-60 variants, convert every axis with no visual coupling — the two icon toggles here — into boolean, text, or instance-swap properties: 4 × 3 × 3 = 36 variants plus 2 boolean properties covers the same 144 combinations. State, size and emphasis stay variants because a designer compares them in the dropdown (→ Component Property Types). If the coupled axes alone still exceed the ceiling, split the set (`Button` and `Icon Button`), split the set instead of deleting an axis.
4. **Version breaking library changes; always version breaking library changes by duplicating.** Duplicate to `Button v2`, migrate consumers file by file, then deprecate the original by prefixing its name with `_` (hides it from the assets panel without unpublishing and breaking live instances). An in-place restructure delivers the breakage to every consuming file in the same second.
5. **Name for the picker and the codebase, not the layer list.** `Button / Primary / Large` nests in the assets menu; `Frame 47` reaches engineers verbatim through Dev Mode and the REST API and ships as `frame-47`. Batch-rename with `Cmd/Ctrl + R` before marking anything Ready for dev.
6. **Build the sad paths before the prototype.** Empty, loading, error, disabled, longest-string, missing-image. A happy-path file transfers the missing states to the engineer, who invents them under deadline — and that invention is what users hit most often.
7. **Publish from a library file; consume everywhere else.** Mains living in the file where they are used get edited by accident and have no version boundary. One foundations library (variables) plus one component library per product surface; a single mega-library makes every linked file pay the load cost and every edit org-wide.
8. **Resolve the plan gate before promising a mechanism.** Mode count per collection, branching, Dev Mode seats, library analytics and the Variables REST API are all tiered (`collaboration.md`). Architecting brand × theme × density as 12 modes on a plan capped at 4 wastes the whole token structure; check `figma_plan` first.
9. **Audit responsiveness by dragging, not by looking.** Grab the frame edge and sweep the full width range the design must survive, then paste the longest realistic string. Static canvas hides clipped text, overlap, and fixed-width overflow — the three defects that reach production most often.


## Sizing Modes

| Mode | Means | Right for | Breaks when |
|---|---|---|---|
| Fill | Take the parent's available space on this axis | Cards, rows, text containers, anything responsive | The parent Hugs on the same axis: nothing to fill, size undefined |
| Hug | Shrink to fit children or text content | Buttons, chips, badges, any wrapper of text | A Fill child sits inside: the same circular dependency, from the other side |
| Fixed | The px you typed | Icon frames, avatars, sidebar rails, fixed-height app bars | Content grows past it — Figma never scrolls. With `Clip content` on it is cut off; off (the default on new frames) it spills silently over siblings |

- Responsive without breakpoints: Fill width plus `min-width` and `max-width` on the same layer. A 320/1200 clamp inside a Fill parent centers and holds across the entire viewport range — one layer instead of a breakpoint frame per size.
- `Wrap` on a horizontal Fill row replaces every nested chip-row hack, and turns gap into separate horizontal and vertical gaps.
- `Space between` with a single child left-aligns it (looks like a bug, is the rule). Two-item rows that must sit flush use `Packed` plus a Fill spacer.
- Absolute position pulls a child out of flow while keeping it parented (badges, overlays, FABs) — and it stops contributing to a Hug parent's size, which is why absolutely-positioned badges get clipped.
- Constraints (Left, Right, Scale, Center) only act inside a fixed-size frame with manual layout, or on an absolutely-positioned child. Tuning constraints inside an auto layout frame is tuning a dead control.


## Component Property Types

| Property | Cost | Right for | Trap |
|---|---|---|---|
| Variant | Multiplies the set | Axes a designer compares side by side: state, size, emphasis | Two concerns fused into one value (`Primary-Large`); value names that drift between sibling sets |
| Boolean | 1 per property | An optional sublayer: leading icon, badge, helper text | Pointing it at a layer another property also targets |
| Instance swap | 1 per property | An interchangeable child: icon set, avatar, nested card | An unbounded swap list — set preferred values |
| Text | 1 per property | Label, count, placeholder | Exposing copy that should come from a string variable |

Test for the split: an axis belongs in variants only if someone would pick it from the variant dropdown while comparing options. Everything else is a property. Property mechanics — preferred values, panel order, exposed nested instances, the `.slot` pattern — are in `components.md`.


## Token Layers

- Three layers, one direction: `primitive` (raw scale values, no meaning) → `semantic` (`bg/surface`, `text/muted`, `border/danger`) → `component` (only where a component genuinely deviates). Components bind to semantic; semantic aliases primitive.
- A semantic token with exactly one consumer that never differs across modes is noise — inline the primitive and add the token when a second consumer or a second mode appears.
- Modes retheme a whole tree in one switch: bind every fill to a mode-bound variable, then set the mode on the top frame. Child frames inherit the parent frame's mode unless explicitly overridden.
- Number variables bind to padding, gap, corner radius and stroke weight, so a spacing scale change propagates without touching layouts. Boolean variables bind to layer visibility and component boolean properties.
- Styles are not dead: gradients, effects, text and grid styles still cover what raw color and number variables do not. A style can itself reference a variable, which is the bridge during migration.
