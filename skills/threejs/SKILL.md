---
name: threejs
description: Generate, debug, and optimize Three.js 3D web scenes. Use when building WebGL/WebXR scenes, configuring cameras, lighting, controls, models, animation loops, responsive canvases, GPU cleanup, or render performance.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎮"}'
---

# Three.js Production Patterns

## Start Here

1. Define the scene, camera, renderer, and intended asset lifecycle before adding objects.
2. Configure a responsive renderer and a time-based animation loop.
3. Dispose of geometry, materials, textures, render targets, and controls when their scene is retired.
4. Inspect `renderer.info` while tuning draw calls, triangles, and texture memory.

## Load on Demand

| Reference | Load when | Covers |
| --- | --- | --- |
| `references/best-practices.md` | Building or debugging scenes, models, controls, resizing, cleanup, or performance | Copyable setup patterns, lifecycle rules, diagnostics, and recovery paths. |
| `references/sources.md` | Verifying Three.js API behavior or updating these practices | Official Three.js documentation and manual sources. |

## Required Checks

- After every resize, update `camera.aspect`, call `camera.updateProjectionMatrix()`, and set the renderer size.
- Use `renderer.setAnimationLoop()` for the renderer-owned animation loop, including WebXR-capable scenes.
- Before removing a scene or loaded asset, traverse it and dispose of each owned GPU resource; retain shared resources until their final consumer is gone.
- For a black, distorted, leaking, or slow scene, follow the corresponding recovery path in `references/best-practices.md` before changing unrelated rendering code.
