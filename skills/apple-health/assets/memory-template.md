# Memory Template — Apple Health

Static format for `<state_root>/memory.md`:

```markdown
# Apple Health Memory

## Status
status: ongoing
version: 1.0.1
last: YYYY-MM-DD
integration: pending
mode: csv-export

## Integration Snapshot
client: unknown
mcp_server: @neiltron/apple-health-mcp
health_data_dir: not_set
last_export_date: unknown
freshness: unknown

## User Intent
<!-- What they want from Apple Health data -->
<!-- Examples: sleep trends, resting heart rate baseline, workout consistency -->

## Constraints
<!-- Privacy constraints, reporting preferences, no-go topics -->

## Notes
<!-- Query caveats, unit normalization choices, schema oddities -->

---
*Updated: YYYY-MM-DD*
```

## Integration-note template

Static format for `<state_root>/integrations.md`:

```markdown
# Apple Health Integrations

## Active Client
- Client: [name]
- Config file: [path]
- Validation: pass | fail
- Last checked: YYYY-MM-DD

## MCP Command
- command: npx
- args: ["-y", "@neiltron/apple-health-mcp"]
- HEALTH_DATA_DIR: /absolute/path

## Known Issues
- [Issue]: [Fix]
```

## Query-note template

Static format for `<state_root>/query-log.md`:

```markdown
# Apple Health Query Log

## YYYY-MM-DD
- Goal:
- Query/report used:
- Date window:
- Result summary:
- Caveats:
```
