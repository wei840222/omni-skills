## Architecture

Memory lives in `<state_root>/`. If `<state_root>/` does not exist, run `references/setup.md`. Use `references/memory-template.md`, `references/watchlist-template.md`, and `references/heartbeat-state.md` as the baseline structures.

Workspace setup may add a minimal discovery router to the workspace `AGENTS.md` and a quiet recurring check to `HEARTBEAT.md`, with recurring behavior routed through `references/heartbeat-rules.md`. Those workspace files are host-owned paths outside `<state_root>` and need explicit approval before writing.

```text
<state_root>/
├── memory.md             # Activation rules, novelty bar, and autonomy boundaries
├── watchlist.md          # Topics worth discovering, why they matter, and heartbeat status
├── heartbeat-state.md    # Last run, last angle used, and no-op markers
├── findings/
│   └── {topic}.md        # Dated log of only the discoveries that were actually new
└── archive/              # Retired topics and frozen logs
```

| Path | Role | Creation condition |
|------|------|--------------------|
| `<state_root>/memory.md` | Stable preferences and activation behavior | Create when persistent discovery is enabled |
| `<state_root>/watchlist.md` | Active, parked, and retired topics | Create when the first durable topic is accepted |
| `<state_root>/heartbeat-state.md` | Last-run markers and lens rotation | Create before the first heartbeat run |
| `<state_root>/findings/{topic}.md` | Dated novelty deltas | Create when the first log-worthy finding appears |
| `<state_root>/archive/` | Retired topics and frozen logs | Create when a topic is retired |
