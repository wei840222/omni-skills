# Core Rules

### 1. Lock the delivery profile first

Choose one profile before coding:

- **Browser Instant** — no-build HTML/CSS/JS, fastest iteration and sharing
- **Browser Structured** — TypeScript or bundler workflow with modular architecture
- **Engine Path** — Unity, Unreal, or Godot when editor tooling and content scale justify it

Stick to one profile per milestone unless the user explicitly requests migration.

### 2. Start from a vertical slice, not a full game plan

Always build a playable loop in this order:

1. input
2. movement
3. objective
4. fail state
5. restart

A complete five-minute loop beats ten untested systems.

### 3. Treat browser performance as a product requirement

For browser-first games, define budgets before adding content:

- frame target and frame-time budget
- draw calls and shader complexity budget
- texture and audio memory budget
- mobile fallback quality tier

If a feature breaks the budget, simplify first and optimize second. Prefer time-based animation (`requestAnimationFrame` delta) over frame-count physics.

### 4. Separate deterministic core logic from presentation

Keep rules deterministic and testable:

- game state transitions
- hit and scoring logic
- progression and economy math

Render, VFX, and animation observe state; they do not own truth.

### 5. Use progressive complexity

System order for agent-driven delivery:

1. loop and controls
2. feedback and readability
3. enemy or puzzle variation
4. progression layer
5. social or online features

Only unlock the next layer after the previous one is playable and measured.

### 6. Make playtesting continuous

Each milestone must include:

- test objective
- expected player behavior
- observed friction
- one concrete balancing action

Do not accept a feature batch without a playtest note under `<state_root>/playtest-log.md`.

### 7. Preserve reusable project knowledge

Update local memory after major decisions:

- concept changes
- preference updates
- architecture pivots
- launch risks

This lets later sessions continue without repeating discovery.
