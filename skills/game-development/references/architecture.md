# Architecture

Memory and project continuity live under the resolved `<state_root>/`. See `assets/memory-template.md` for status fields and companion templates.

```text
<state_root>/
|-- memory.md              # Current project state, scope, and delivery profile
|-- concept-briefs.md      # Game concepts, target audience, and pillar ideas
|-- user-preferences.md    # User taste, constraints, and style preferences
|-- system-decisions.md    # Technical decisions and tradeoffs
|-- playtest-log.md        # Session findings, issues, and balancing actions
|-- roadmap.md             # Milestones and release checkpoints
`-- release-notes.md       # What changed between iterations
```

## Runtime architecture (game project, not skill state)

Prefer a hard boundary:

- **Domain / simulation** — pure state transitions, scoring, collision resolution, progression math
- **Presentation** — renderer, HUD, audio, VFX that observe emitted events
- **Infrastructure** — input adapters, save I/O, optional telemetry

Keep simulation deterministic and frame-rate independent where possible (fixed timestep or time-delta based movement). See `references/systems-and-state.md` and `references/project-structure-blueprints.md`.
