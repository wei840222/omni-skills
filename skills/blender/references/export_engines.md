# Export for Game Engines

## Format choice

- FBX or glTF for Unity/Unreal pipelines.
- Prefer glTF/GLB for web and many real-time runtimes that already speak glTF.
- Apply or bake what the destination cannot evaluate (modifiers, shape keys policy, custom normals).

## Transforms and axis

- Apply object rotation/scale before export when the consumer expects identity transforms on the mesh object.
- Unity FBX common baseline: Forward `-Z`, Up `Y`; enable apply-scalings options such as `FBX All` when Unity imports exaggerated or sheared scale.
- Unreal FBX often expects a different forward/up pairing than Unity — set export axis explicitly for the target engine instead of reusing Unity presets blindly.
- Keep character origins at feet/base unless the engine prefab contract says otherwise.

## Textures and materials

- Embed textures or export a predictable sidecar folder; do not mix both conventions in one handoff.
- Confirm materials are assigned to faces before export.
- After import, validate facing, scale units, and animation orientation in the engine before further content work.

## Failure checks

- Model faces the wrong way → re-export with destination forward/up and applied rotation.
- Animation looks sheared → applied non-uniform scale or mismatched axis; fix in Blender, do not only rotate in-engine.
- Missing textures → packaging mode mismatch or unassigned materials.
