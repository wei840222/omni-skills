# Blender Python API (bpy)

## Core objects

- `bpy.context` is the current session state: selection, active object, mode, and view layer.
- `bpy.data` is the blend-file datablock collection; look up objects by name regardless of selection.
- `bpy.ops` are operators and require a valid context (mode, active object, selected objects).

## Context rules

- Most mesh/object operators need Object mode first:
  `bpy.ops.object.mode_set(mode='OBJECT')`
- When calling operators from scripts or batch jobs, override context explicitly instead of assuming the UI selection is present:

```python
override = {
    "object": obj,
    "active_object": obj,
    "selected_objects": [obj],
    "selected_editable_objects": [obj],
}
with bpy.context.temp_override(**override):
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
```

- Prefer data-API edits (`obj.location`, mesh datablocks, attributes) when you do not need operator-only behavior.
- Do not treat a failed operator as a data bug until mode and context are verified.

## Common failure modes

- `bpy.ops.*.mode_set` or mesh operators error → wrong mode or empty selection.
- Operator affects the wrong object → active object not set; pass override.
- Script works in UI but fails headless → missing window/area context; use `temp_override` or data API.
