---
name: unity
description: >
  Avoid common Unity MonoBehaviour pitfalls: lifecycle ordering, GetComponent
  caching, FixedUpdate physics timing, UnityEngine.Object fake null, coroutines,
  pooling, serialization, and ScriptableObject data. Use when writing or
  reviewing Unity C# gameplay scripts, diagnosing Destroy/null surprises, or
  tuning component/physics performance. Out of scope: Blender mesh export
  (`blender`), Unreal C++/replication (`unreal-engine`), and browser Three.js
  game slices (`game-development`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎮"}'
  related-skills: '{"blender": "Mesh cleanup and FBX/glTF export before Unity import.", "csharp": "General C# null/async/LINQ discipline outside UnityEngine.Object semantics.", "game-development": "Browser playable loops and Three.js delivery when Unity Editor is not the target.", "unreal-engine": "Unreal C++ GC, actor lifecycle, and replication instead of Unity MonoBehaviour."}'
---

This skill is stateless knowledge guidance. It does not store local configuration or persistent user state.

## Safety posture

- Treat Editor-only APIs (`DestroyImmediate`, Play Mode ScriptableObject edits) as unsafe for player builds unless the user explicitly asks for Editor tooling.
- Prefer read-only diagnosis first. For destructive scene/prefab edits or mass refactors, restate the exact change and wait for explicit authorization.
- Verify lifecycle, physics, and null claims against current Unity Manual / Scripting API for the project's Unity version before irreversible refactors.

## Workflow

1. Identify the failure class: lifecycle order, component lookup cost, physics timing, fake null / Destroy delay, coroutine lifetime, pooling, serialization, or ScriptableObject mutation.
2. Confirm whether the code runs in Play Mode, Edit Mode, FixedUpdate, or a disabled MonoBehaviour.
3. Load only the matching reference below, then answer with the affirmative pattern and a recovery check.
4. For project-wide cleanup (mass Find/GetComponent, Destroy patterns), restate scope and wait for authorization.

## Load references

| Reference | Load when |
|---|---|
| `references/runtime-pitfalls.md` | Lifecycle, GetComponent, FixedUpdate, fake null, Destroy delay, coroutines, pooling, serialization, ScriptableObjects, or common mistakes. |
| `references/sources.md` | Need primary Unity Manual/API URLs or Gate 6 provenance. |

## Route adjacent asks

- Blender transform/normal/export before import → `blender`
- Unreal GC / Actor lifecycle / replication → `unreal-engine`
- Browser Three.js playable slice → `game-development`
- Generic C# null/async/LINQ without UnityEngine.Object → `csharp`
