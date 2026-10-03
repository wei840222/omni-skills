---
name: apple-health
description: Connect agents to Apple Health exports with MCP setup, schema validation, and privacy-safe analysis.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"❤️","requires":{"bins":["node","npx"],"env":["HEALTH_DATA_DIR"]},"install":[{"id":"npm","kind":"npm","package":"@neiltron/apple-health-mcp","bins":["apple-health-mcp"],"label":"Install Apple Health MCP Server (npm)"}]}'
  related-skills: '{"api":"API and MCP integration debugging outside exported-health analysis.","health":"General wellness framing beyond analysis of exported records.","ios":"iPhone export setup and iOS platform troubleshooting.","sleep":"Sleep coaching and interpretation beyond querying recorded sleep.","swift":"HealthKit application implementation rather than terminal export analysis."}'
---

## State location

Before the first state read, query, create, update or delete, resolve `<state_root>` once:

1. Use the user- or host-configured state root when supplied.
2. Otherwise use the first existing directory in this order: `<workspace>/apple-health/`, `<workspace>/memory/apple-health/`, `~/apple-health/`.
3. If multiple candidates exist, use only the highest-precedence one and report the extra copies. Keep other copies unchanged and separate.
4. Complete lookup before creation. If no candidate exists and the user consents to saving health-related notes, create `<workspace>/apple-health/`.
5. `<workspace>` is the host/runtime workspace root, not the shell working directory. If unavailable, read an existing `~/apple-health/`; otherwise obtain an explicit root before creation.
6. Keep this resolved root fixed throughout the invocation. Resolution selects a path; obtain consent before persisting or modifying health information.

Use `<state_root>/memory.md`, `<state_root>/integrations.md`, `<state_root>/query-log.md` and `<state_root>/archive/` as needed. Runtime state and original exports stay outside the skill package and version control. Read-only analysis needs no state creation.
Legacy `~/Clawic/data/apple-health/` is a migration source only. Copy only on an explicit migration request, validate the destination, retain the original for rollback, and obtain separate authorization before deletion.

## Setup

On first use, read `references/setup.md` for integration guidelines.

## When to Use

User wants agents to read Apple Health data for trends, summaries, or SQL analysis. Agent handles export validation, MCP server wiring, and safe query/report flows without exposing private health records.

## Architecture

Memory lives in `<state_root>/`. Read `references/memory.md` before persistent-note updates and `assets/memory-template.md` only when seeding requested notes.

```
<state_root>/
|-- memory.md              # Status, client integration state, latest export path
|-- integrations.md        # Connected MCP clients and validation notes
|-- query-log.md           # Reusable SQL/report prompts and known-good outputs
`-- archive/               # Retired paths and old troubleshooting notes
```

### State children

| Path | Role | Create when |
|---|---|---|
| `<state_root>/memory.md` | Status, integration mode, validated export path and freshness | User first requests retained integration notes |
| `<state_root>/integrations.md` | Client configuration pointers and validation notes | User requests a working integration be remembered |
| `<state_root>/query-log.md` | Reproducible SQL, windows and non-sensitive caveats | User requests a reusable query be saved |
| `<state_root>/archive/` | Retired path pointers or troubleshooting notes | User requests archival of an existing note |

Create each optional child only when needed, after consent; read existing content before updating it. Retain configuration pointers and reproducible queries rather than raw health rows or credentials. There are no shared-memory or external state writes in this skill.

## Quick Reference

Use these files on demand instead of overloading the main instructions.

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` — first use or troubleshooting configuration |
| Persistent-note status and lifecycle | `references/memory.md` — before reading or updating health notes |
| Memory template | `assets/memory-template.md` — only when creating user-requested notes |
| MCP client wiring | `references/mcp-config.md` — before configuring a client |
| Query recipes | `references/query-recipes.md` — after schema discovery when writing SQL |
| Fallback CLI paths | `references/fallback-cli.md` — after startup or native-module failure |

## Core Rules

### 1. Confirm Integration Mode Before Doing Anything
Start by clarifying one of these modes:
- `csv-export` using Apple Health CSV exports and MCP
- `not-now` if user is only planning and does not want setup yet

Never imply direct HealthKit API access from terminal agents. This skill works from exported data.

### 2. Validate Local Export Before MCP Wiring
Require a real export folder before configuration:
- Must exist locally and be readable
- Must include files matching `HKQuantityTypeIdentifier*.csv`, `HKCategoryTypeIdentifier*.csv`, or `HKWorkoutActivityType*.csv`
- Must not be an empty unzip folder

If validation fails, stop and fix data path first.

### 3. Run Runtime Preflight Before MCP Configuration
Before wiring MCP, verify runtime:
- `node -v` should be an LTS line (18, 20, or 22)
- If `npx @neiltron/apple-health-mcp` fails with missing `duckdb.node`, switch to LTS Node and retry
- Confirm `HEALTH_DATA_DIR` is available as an absolute path

Do not continue while runtime is incompatible.

### 4. Configure MCP With Explicit Path and Command
Use the MCP server command from `references/mcp-config.md`:
- Command: `npx`
- Args: `[@neiltron/apple-health-mcp]`
- Env: `HEALTH_DATA_DIR=/absolute/path/to/export`

Never continue with placeholders or relative paths that are not verified.

### 5. Schema First, Then Queries
First run schema discovery (`health_schema`) and map available tables.
Only then run `health_query` or `health_report`.

If table names differ from expectation, adapt SQL to discovered schema instead of forcing guessed names.

### 6. Use Date-Bounded Queries By Default
Every analytical query should include time bounds and clear units.
Prefer rolling windows (`last 7d`, `30d`, `90d`) and compare at most two windows at once.

Avoid unbounded full-history scans unless user explicitly asks.

### 7. Track Data Freshness and Refresh Points
Log last export timestamp in memory and warn when data is stale.
If user needs current-day insights, request a new iPhone export before claiming "latest" trends.

## Common Traps

- Assuming live HealthKit access from CLI agents -> setup fails because only exported data is available
- Using wrong export path in MCP env -> server starts but returns no data
- Running SQL before schema discovery -> queries fail on wrong table names
- Unbounded queries on large exports -> slow analysis and noisy output
- Reporting "today" metrics from stale export -> inaccurate recommendations
- Running MCP package on non-LTS Node -> DuckDB native module errors can break startup

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://registry.npmjs.org | Package install metadata only | Download MCP server package |
| https://raw.githubusercontent.com | Public markdown only | Read validated fallback skill docs |
| https://apps.apple.com | Manual app download traffic | Install CSV export app on iPhone |

No health record rows should be sent externally by default.

## Security & Privacy

Data that leaves your machine:
- Package install requests to npm
- Optional app download traffic from App Store

Data that stays local:
- Apple Health CSV exports
- MCP query outputs and summaries
- Skill memory in `<state_root>/`

This skill does NOT:
- Access iCloud Health data directly
- Bypass Apple permission prompts
- Upload health CSVs unless the user asks for that explicitly

## Trust

By using this skill, you rely on third-party tooling (`@neiltron/apple-health-mcp` and the chosen iPhone export app).
Only install and run if you trust those tools.
