# Memory Template — Paperclip

Create `<state_root>/memory.md` only after consent:

```markdown
# Paperclip Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending | done | declined

## Environment
<!-- API base, PAPERCLIP_HOME / --data-dir, local_trusted vs authenticated -->

## Company Scope
<!-- Active companies, goals, key projects, operators -->

## Adapter Defaults
<!-- Preferred runtimes, host vs Docker notes, wake patterns -->

## OpenClaw Notes
<!-- Gateway URL scheme (ws/wss), hostname caveats, invite/pairing status -->

## Notes
<!-- Repeated blockers, successful command shapes (no secrets), preferences -->
```

Optional companions under the same `<state_root>/`:

| File | Purpose |
|------|---------|
| `companies.md` | Company names, goals, status snapshots |
| `commands.md` | Reused CLI/API snippets that worked |
| `notes.md` | Open questions, blockers, migration notes |

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning the setup | Add context when it reduces future friction |
| `complete` | Stable enough to operate | Reuse stored defaults before asking |
| `paused` | User wants no setup discussion now | Work with current facts only |
| `never_ask` | User opted out of setup prompts | Ask only if explicitly requested |

## Key principles

- Keep secrets out of memory files (tokens, private keys, raw provider keys).
- Store environment facts and operating preferences, not credentials.
- Record adapter type keys (`claude_local`, `openclaw_gateway`, …) not marketing names only.
- Update `last` whenever the skill is used meaningfully.
