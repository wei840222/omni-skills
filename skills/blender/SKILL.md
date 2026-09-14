---
name: blender
description: >
  Apply Blender transforms, fix normals, order modifiers, unwrap UVs, set
  origins, and export FBX/glTF for Unity, Unreal, or web. Use for mesh cleanup,
  game-engine export orientation/scale, common modeling mistakes, and bpy
  context/operator scripting.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧊"}'
  related-skills: '{"unity":"Engine-side lifecycle, components, and import behavior after Blender export.","unreal-engine":"Unreal C++ and asset constraints after FBX/glTF handoff.","drawing":"2D illustration and coloring workflows outside 3D mesh authoring.","art":"Broader art direction when the task is critique or style, not Blender ops.","design":"Visual direction before locking a 3D modeling or export workflow."}'
---

## When to Use

Use this skill when the work is inside Blender or preparing a Blender asset for another runtime:

- apply/reset transforms before export or modifiers
- diagnose flipped normals, bad shading, or origin/pivot issues
- order and apply modifiers for game-engine geometry
- mark UV seams and avoid overlapping islands
- choose FBX vs glTF and correct axis/scale for Unity, Unreal, or web
- write or debug `bpy` scripts that fail on context/mode

Prefer `unity` or `unreal-engine` once the asset has left Blender and the problem is engine-side. Prefer `drawing` / `art` / `design` for 2D illustration or art direction without mesh authoring.

## State location

This skill is stateless. It does not create local configuration, caches, or memory files. Do not invent a Blender state directory unless the user explicitly asks to persist project notes outside this skill.

## Core workflow

1. Confirm Object vs Edit mode before transforming or selecting.
2. Apply rotation/scale when the asset will leave Blender or when modifiers need uniform scale.
3. Recalculate normals and inspect Face Orientation before shading or export.
4. Order modifiers deliberately; apply them when the destination cannot evaluate Blender modifier stacks.
5. Mark seams in hidden areas, unwrap, and check for UV overlap before bake/export.
6. Set the origin for the intended pivot (often feet/base for characters).
7. Export with destination axis/scale rules; embed or pack textures to match the consumer.
8. For automation, set or override `bpy` context before calling operators.

## Transforms

- Apply scale before export — `Ctrl+A` → Scale, or objects deform in game engines.
- Apply rotation for correct orientation — especially for rigged models.
- Non-uniform scale breaks modifiers — apply scale before Mirror, Bevel, and similar ops.
- Reset transforms: `Alt+G` / `Alt+R` / `Alt+S` for location, rotation, scale defaults.

## Object vs Edit Mode

- Object mode transforms the whole object; Edit mode transforms geometry only.
- Modifiers are managed in Object mode; Edit mode shows the base mesh.
- Selection scope differs: Object selects whole objects; Edit selects vertices/edges/faces.
- `Tab` toggles modes; most operators are mode-specific.

## Normals

- Flipped normals produce invisible faces — `Shift+N` recalculates outside.
- Check Viewport Overlays → Face Orientation — blue outside is correct, red is flipped.
- `Ctrl+Shift+N` flips inside — useful for interior scenes.
- Smooth-shading artifacts often start as bad normals — recalculate first.

## Modifiers

- Order matters — Mirror before Subdivision; Bevel before Mirror is a common safe pattern.
- Apply modifiers for export when game engines need evaluated geometry rather than Blender modifier stacks.
- Array + Curve deformation issues — apply Array first, then Curve.
- Keep Subdivision preview and render levels aligned for consistent export expectation.

## UV Unwrapping

- Mark seams where the texture can split — `Ctrl+E` → Mark Seam.
- Prefer seams in hidden areas — under arms, behind ears, and hard model edges.
- `U` → Unwrap after marking; Smart UV Project is a fallback, not the default craft path.
- Check UV overlap — overlapping islands cause bake and texture issues.

## Origin Point

- Origin controls rotation/scale pivot — right-click → Set Origin.
- Origin to Geometry centers the pivot; Origin to 3D Cursor places it precisely.
- For game-engine import, character origins often belong at feet/base.

## Common Mistakes

- `Alt+D` creates a linked duplicate — use `Shift+D` for an independent copy.
- Delete removes geometry; Dissolve merges in Edit mode.
- Proportional editing left on silently affects nearby vertices — check the header.
- High Subdivision levels on dense meshes can freeze Blender — start at Levels 1.
- Materials not assigned to faces will not export as expected.

## Progressive disclosure

| Need | Reference |
|------|-----------|
| FBX/glTF destination rules, axis, scale, textures | `references/export_engines.md` |
| `bpy.context` / `bpy.data` / `bpy.ops` context overrides | `references/python_api.md` |
| Source-backed export and API notes | `references/source-notes.md` |

Load only the reference that matches the current bottleneck.
