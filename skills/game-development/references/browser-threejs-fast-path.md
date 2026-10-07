# Browser Three.js Fast Path (No Build)

Use this path when users want a playable 3D game quickly from static files.

## Minimal delivery model

- `index.html` bootstraps canvas and UI overlay
- `styles.css` handles HUD and responsive layout
- `main.js` initializes scene, camera, renderer, and loop
- optional `assets/` for textures, models, and audio

CDN Three.js is acceptable for prototypes; pin a versioned URL when sharing builds.

## Recommended development sequence

1. Scene and camera calibration (responsive canvas; cap `devicePixelRatio`)
2. Player movement and input handling (time-delta based)
3. Basic collision proxies and fail condition
4. Score/progress logic in pure modules
5. Restart flow and HUD readability
6. Performance pass for desktop and mobile
7. Dispose geometries, materials, textures, and controls on scene teardown

## Performance guardrails

- Cap pixel ratio to avoid mobile GPU overload (Three.js responsive guidance).
- Keep draw calls bounded with instancing and merged static meshes.
- Dispose GPU resources on scene transitions (Three.js cleanup / dispose guides).
- Prefer rendering on demand when the scene is static; use a continuous loop only while gameplay needs it.
- Avoid expensive post-processing until the core loop is validated.

## Game feel checklist

- Input delay under one frame for movement and actions
- Clear camera framing during high-action moments
- High-contrast feedback for hit, damage, and success
- Restart and retry path under three interactions

## Upgrade path to structured builds

Move to a bundled workflow only when needed:

- codebase exceeds manageable single-file complexity
- shared systems require module boundaries
- automated tests and content pipeline justify tooling overhead

For most prototype-to-playable browser games, no-build remains the fastest delivery path.
