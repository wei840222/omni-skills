# MCP configuration — Apple Health

Use a trusted MCP-compatible client with local stdio transport. Obtain setup/package-execution consent and establish the health-data client/provider boundary in SKILL.md first.

Merge this entry into the client's actual existing configuration; preserve other entries and a rollback copy. The example path must be replaced with a verified, readable absolute directory:

```json
{
  "mcpServers": {
    "apple-health": {
      "command": "npx",
      "args": ["-y", "@neiltron/apple-health-mcp"],
      "env": {
        "HEALTH_DATA_DIR": "/absolute/path/to/health-export"
      }
    }
  }
}
```

`-y` accepts npm acquisition prompts after user authorization; it is not consent by itself. For reproducible operation, verify a package version and use `@neiltron/apple-health-mcp@<VERIFIED_VERSION>` rather than guessing a version. Client config/env paths differ; use that client's current docs. A configured `HEALTH_DATA_DIR` inside the server environment need not be a global shell variable.

## Runtime and integration checks

- Published npm version 1.4.5 declares Node >=22. Verify `node -v` and the selected package engines; Node 18/20 are incompatible with that requirement.
- Validate the absolute directory and supported nonempty Simple Health Export CSV layout; native `export.xml` is unsupported.
- After authorization, client discovery of `health_schema`, `health_query` and `health_report` proves tool registration. At least one schema table plus one successful bounded query proves usable integration; process startup alone does not.
- On native-module or startup failure, use `references/fallback-cli.md` with the original error preserved.

## Optional server environment

| Variable | Documented default | Effect |
|---|---|---|
| `MAX_MEMORY_MB` | `2048` | DuckDB memory limit in MB |
| `CACHE_SIZE` | `100` | Maximum cached query-result count |

Each touched table loads its full CSV history into process memory even for bounded SQL. A load over the memory limit returns an error; the server disables temporary spill storage. Increase memory only for a measured need within host capacity and with authorization, or provide a narrower approved export. Restart rebuilds the in-memory database; persistent incremental import is not current behavior.

Source/version boundary: defaults and requirements were checked on 2026-10-03 against the sources in `references/sources.md`; verify again when changing versions.
