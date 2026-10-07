---
name: game-development
description: >
  Design and ship browser-playable games from no-build Three.js prototypes to
  modular TypeScript builds, with vertical-slice workflows, performance budgets,
  playtest loops, and optional multiplayer/live-ops plans. Use when the user
  wants a playable browser game, endless runner/arena/puzzle/platformer slice,
  Three.js no-build prototype, game architecture split (core vs presentation),
  asset budgets, save/recovery design, or launch/balance checklists. Not for
  pure Three.js scene hygiene without gameplay (`threejs`), language-only JS/TS
  debugging (`javascript`, `typescript`), or engine-editor deep dives that are
  already covered by `unity` / `unreal-engine`.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🕹️","requires":{"bins":["node","python3"]}}'
  related-skills: '{"threejs":"WebGL scene setup, disposal, responsive canvas, and GPU hygiene once gameplay needs 3D rendering.","javascript":"Browser/Node language edges for game scripts outside architecture choices.","typescript":"Typed modular game codebases and bundler/tsconfig work for Browser Structured delivery.","unity":"Editor-heavy engine path when browser delivery is no longer the right profile.","unreal-engine":"High-fidelity C++/replication engine path when advanced rendering or netcode demands it."}'
---

# Game Development

Ship a **playable loop** first. Lock one delivery profile, build input → movement → objective → fail → restart, then expand systems only after playtest evidence.

## State location

Game-development state may exist in `<workspace>/game-development/`, `<workspace>/memory/game-development/`, or `~/game-development/`.
`<workspace>` is the host/runtime workspace root (from host config), not the shell cwd alone.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/game-development/`, `<workspace>/memory/game-development/`, `~/game-development/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and durable notes must be saved, propose `<workspace>/game-development/` (or an explicit path if no workspace is available) and obtain named consent before creating it.
5. Legacy paths `~/Clawic/data/game-development/` and bare copies outside the selected root are migration sources only. Copy into the selected layout only after the user names the destination; leave legacy trees untouched unless the user asks to remove them.

Use the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Skill package files stay under `references/` and `assets/`; never write learned data into `SKILL.md`.

### State tree (after resolution)

```text
<state_root>/
├── memory.md              # Status, snapshot, budgets, risks
├── concept-briefs.md      # Fantasy, audience, pillars
├── user-preferences.md    # Taste and non-negotiables
├── system-decisions.md    # Architecture tradeoffs
├── playtest-log.md        # Findings and balance actions
├── roadmap.md             # Milestones and blockers
└── release-notes.md       # Player-visible changes
```

On first use, read `references/setup.md`. Create files from `assets/memory-template.md` only after consent.

## When to use

- Instant browser games (especially no-build Three.js HTML/JS)
- Vertical slices: endless runner, arena, puzzle, platformer, idle, tactical
- Choosing Browser Instant vs Browser Structured vs Engine Path
- Performance budgets, asset pipelines, save/recovery, multiplayer escalation
- Playtest, balance, and launch gates

Prefer `threejs` for pure scene/renderer hygiene, `javascript`/`typescript` for language-only failures, and `unity`/`unreal-engine` when the user already committed to those editors.

## Session workflow

1. **Resolve state** — run the State location procedure if continuity matters.
2. **Lock delivery profile** — Browser Instant, Browser Structured, or Engine Path (`references/core-rules.md`). Do not mix profiles in one milestone unless the user asks to migrate.
3. **Define the five-step slice** — input, movement, objective, fail state, restart.
4. **Set budgets before content** — frame time, draw calls, texture/audio memory, mobile fallback (`references/browser-threejs-fast-path.md`, `references/content-pipeline.md`).
5. **Separate simulation from presentation** — deterministic rules own truth; render/VFX observe (`references/systems-and-state.md`, `references/architecture.md`).
6. **Playtest every milestone** — objective, expected behavior, friction, one balance action (`references/qa-balance-launch.md`).
7. **Escalate carefully** — multiplayer/live-ops only after single-player loop quality (`references/multiplayer-and-live-ops.md`).

## Quick reference

| Topic | File |
|-------|------|
| First activation / consent setup | `references/setup.md` |
| Memory and file templates | `assets/memory-template.md` |
| Core delivery rules | `references/core-rules.md` |
| Genre → loop mapping | `references/game-types-and-loops.md` |
| No-build Three.js path | `references/browser-threejs-fast-path.md` |
| Folder blueprints | `references/project-structure-blueprints.md` |
| Systems and save/recovery | `references/systems-and-state.md` |
| Architecture overview | `references/architecture.md` |
| Asset/content pipeline | `references/content-pipeline.md` |
| Multiplayer and live ops | `references/multiplayer-and-live-ops.md` |
| QA / balance / launch | `references/qa-balance-launch.md` |
| Runtime requirements | `references/requirements.md` |
| Data stored under state | `references/data-storage.md` |
| Common traps | `references/common-traps.md` |
| Security and privacy | `references/security-privacy.md` |

Load only the smallest file needed for the current step.

## Requirements (summary)

- Local preview scripts: `node`
- Optional offline asset helpers: `python3`
- Browser targets for instant path: Chromium, Firefox, or Safari family

Prefer static local workflows first. Add backends only when the user needs authority, persistence, or commerce (`references/requirements.md`).

## Safety

- Keep concept notes, preferences, and playtest logs under the resolved `<state_root>/`.
- Push source, CDN uploads, or telemetry only when the user explicitly requests it.
- Do not force paid APIs or external services for simple browser prototypes.
- Do not claim launch readiness without at least one complete playtest cycle and budget evidence (`references/security-privacy.md`).
