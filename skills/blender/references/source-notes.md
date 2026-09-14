# Source Notes — blender

Research captured during the 2026-09-14 refactor. Prefer primary docs over forum folklore when guidance conflicts.

## Official documentation

- Blender Manual — Applying Object Transformations
  https://docs.blender.org/manual/en/latest/scene_layout/object/editing/apply.html
  Use when deciding whether location/rotation/scale must be applied before export or modifier work.

- Blender Manual — Mesh Normals
  https://docs.blender.org/manual/en/latest/modeling/meshes/structure.html#normals
  Anchors recalculate/flip guidance and why facing affects shading and export.

- Blender Manual — Mesh Operators / Normals menus (recalculate, flip)
  https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/normals.html
  Confirms `Shift+N` recalculate and related normal editing entry points.

- Blender Manual — Modifiers
  https://docs.blender.org/manual/en/latest/modeling/modifiers/index.html
  Modifier stack evaluation order and apply-for-export expectations.

- Blender Manual — UV Editing
  https://docs.blender.org/manual/en/latest/modeling/meshes/uv/index.html
  Seam marking, unwrap, and island hygiene before bake/export.

- Blender Manual — glTF importer/exporter
  https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html
  Web/runtime-oriented export path and material/texture packaging notes.

- Blender Manual — FBX importer/exporter
  https://docs.blender.org/manual/en/latest/addons/import_export/scene_fbx.html
  Axis, scale, and apply-transform related export settings for DCC/engine handoff.

- Blender Python API — Overview
  https://docs.blender.org/api/current/info_overview.html
  Distinguishes context, data, and operator layers.

- Blender Python API — `bpy.ops`
  https://docs.blender.org/api/current/bpy.ops.html
  Operator execution model and why invalid context fails.

- Blender Python API — Context / temp override
  https://docs.blender.org/api/current/bpy.types.Context.html
  Supports explicit overrides for non-UI scripts.

## Engine import baselines

- Unity Manual — Model file formats / FBX
  https://docs.unity3d.com/Manual/3Dformats.html
  Confirms FBX as a primary interchange path into Unity.

- Unity Manual — Importing models
  https://docs.unity3d.com/Manual/ImportingModelFiles.html
  Scale/orientation expectations after DCC export.

- Unreal Engine — FBX Content Pipeline
  https://dev.epicgames.com/documentation/unreal-engine/fbx-content-pipeline
  Engine-side FBX import contract that Blender exports must satisfy.

## Obsolete / removed baseline claims

- Clawic homepage and `_meta.json` owner metadata were promotional/repo-duplicative and removed.
- Nested `metadata.clawdbot` YAML was replaced by string `metadata.openclaw`.
- Broad all-OS filters with no gating effect were dropped.
