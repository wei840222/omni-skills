# Sources - Game Development

Verified full URLs used for this refactor. Re-check before changing version-sensitive claims.

## Agent Skills format

- Agent Skills specification — https://agentskills.io/specification.md
- Skill creation best practices — https://agentskills.io/skill-creation/best-practices.md
- Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions.md
- Evaluating skill output quality — https://agentskills.io/skill-creation/evaluating-skills.md
- skills-ref validator package — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Three.js / browser realtime

- Three.js fundamentals — https://threejs.org/manual/#en/fundamentals
- Responsive design — https://threejs.org/manual/#en/responsive
- Cleanup / disposal overview — https://threejs.org/manual/#en/cleanup
- How to dispose of objects — https://threejs.org/docs/#manual/en/introduction/How-to-dispose-of-objects
- Rendering on demand — https://threejs.org/manual/#en/rendering-on-demand
- Debugging JavaScript — https://threejs.org/manual/#en/debugging-javascript

## Web games / animation timing

- MDN: Building a basic demo with Three.js — https://developer.mozilla.org/en-US/docs/Games/Techniques/3D_on_the_web/Building_up_a_basic_demo_with_Three.js
- MDN: Games introduction — https://developer.mozilla.org/en-US/docs/Games/Introduction
- MDN: Anatomy of a video game — https://developer.mozilla.org/en-US/docs/Games/Anatomy
- MDN: `window.requestAnimationFrame` — https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame
- web.dev: Optimize JavaScript execution — https://web.dev/articles/optimize-javascript-execution
- web.dev: OffscreenCanvas — https://web.dev/articles/offscreen-canvas

## Domain guidance retained from package intent

- Vertical slice order (input → movement → objective → fail → restart) before systems sprawl.
- Separate deterministic simulation state from presentation observers.
- Multiplayer/live-ops only after single-player loop quality is measured.
