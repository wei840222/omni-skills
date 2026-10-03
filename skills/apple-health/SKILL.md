---
name: apple-health
description: >
  Connect a trusted MCP client to local Apple Health CSV exports for schema-first
  sleep, heart-rate and workout analysis. Use when validating an export, wiring
  or troubleshooting Apple Health MCP, or querying recorded health trends.
  For setup planning, explain options without changing configuration. Live
  HealthKit/iCloud access, app implementation and personal medical diagnosis
  are outside this export-analysis workflow.
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

Use for recorded Apple Health CSV trends, summaries, SQL analysis, export validation and MCP configuration troubleshooting. Planning-only requests stay in `not-now` mode. For HealthKit app implementation use `swift`; for general wellness without an export use `health`. Private records require the client/provider authorization boundary below before any tool call.

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
| Runtime failure recovery | `references/fallback-cli.md` — after startup or native-module failure |
| Verified domain sources | `references/sources.md` — before asserting package capabilities or current defaults |

## Core Rules

### 1. Confirm Integration Mode Before Doing Anything
Use the user's stated intent; ask only when the integration mode is missing:
- `csv-export` using Apple Health CSV exports and MCP
- `not-now` if user is only planning and does not want setup yet

Terminal agents in this workflow read point-in-time exported data. Live HealthKit and iCloud access are outside this workflow. In `not-now` mode answer planning questions only; configuration and installation wait for an explicit setup request.

### 2. Validate Local Export Before MCP Wiring
Require a real export folder before configuration:
- Must exist locally and be readable
- Must include files matching `HKQuantityTypeIdentifier*.csv`, `HKCategoryTypeIdentifier*.csv`, or `HKWorkoutActivityType*.csv`
- Must contain readable, nonempty CSV data in the Simple Health Export CSV layout, not only an empty unzip directory
- Native Apple Health `export.xml` is unsupported by this MCP package; request the supported CSV layout instead of renaming XML files

If validation fails, identify the missing directory, unreadable file or unsupported layout and repair that input before configuration.

### 3. Run Runtime Preflight Before MCP Configuration
Before wiring MCP, verify runtime:
- `node -v` must satisfy the installed package engines; npm version 1.4.5 requires Node >=22. Use a supported Node release satisfying that range, not Node 18/20
- On a missing `duckdb.node` or native-module failure, verify the Node version, platform and installed package before one bounded retry using `references/fallback-cli.md`; retain the error if it persists
- Confirm `HEALTH_DATA_DIR` is available as an absolute path

Proceed to wiring only after runtime compatibility is verified.

### 4. Configure MCP With Explicit Path and Command
Use the MCP server command from `references/mcp-config.md`:
- Command: `npx`
- Args: `["-y", "@neiltron/apple-health-mcp"]`
- Env: `HEALTH_DATA_DIR=/absolute/path/to/export`

Replace example placeholders with a verified absolute export path. Confirm third-party package execution, client configuration changes and client/provider health-data handling before setup. `-y` accepts npm acquisition prompts; it does not provide user consent. Use local stdio transport, not an exposed network service.

### 5. Schema First, Then Queries
After health-data access and client/provider handling are authorized, run schema discovery (`health_schema`) and map available tables, units and category labels. Schema discovery can itself return sample health rows. Minimize tool output under the client's available controls; if provider egress is unacceptable, keep health tools unused and offer an approved local-only path.
Only then run `health_query` or `health_report`.

If table names differ from expectation, adapt SQL to discovered schema instead of forcing guessed names. Category labels are in `valueText`; quantity values are numeric. Discover workout tables from `commonPatterns.workouts`, including split activity tables.

### 6. Use Date-Bounded Queries By Default
Every analytical query includes an explicit start and exclusive end, and clear units. Inspect `sourceName`, source overlap and units before aggregation; report per-source results until an overlap policy is established.
Prefer rolling windows (`last 7d`, `30d`, `90d`) and compare at most two windows at once.

Use unbounded result queries only when explicitly requested. A bounded SQL predicate still loads the full CSV history for each touched table; it is not a memory or access boundary. On a memory error reduce the approved export scope or adjust the limit explicitly, rather than presenting an empty result as no data.
Sleep sums include asleep labels only, excluding awake/in-bed and checking overlaps within the chosen source. Imported timestamps lose their original timezone offsets; report stored local clock times and state that output `Z` does not recover a UTC instant. Read `references/query-recipes.md` before computing sleep or cross-zone comparisons.

### 7. Track Data Freshness and Refresh Points
Record the last export timestamp in `<state_root>/memory.md` only when persistent-note consent exists; otherwise state freshness in the current reply. If the export timestamp or coverage is unknown, say so rather than inferring freshness from file modification time.
If user needs current-day insights, request a new iPhone export before claiming "latest" trends.

## Common Traps

- Assuming live HealthKit access from CLI agents -> setup fails because only exported data is available
- Using wrong export path in MCP env -> server starts but returns no data
- Running SQL before schema discovery -> queries fail on wrong table names
- Unbounded queries on large exports -> slow analysis and noisy output
- Reporting "today" metrics from stale export -> inaccurate recommendations
- Running Node below the package engines -> verify Node >=22 for version 1.4.5, then inspect native-module errors
- Treating bounded SQL as a bounded import -> touched tables load full exported history
- Summing all sleep rows or multiple devices -> inspect asleep labels and per-source overlap first
- Treating a returned timestamp Z as UTC -> import discarded the source offset; show stored clock time

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://registry.npmjs.org | Package-resolution/download requests | Acquire MCP package and dependencies |
| https://raw.githubusercontent.com | Public-document requests | Read maintainer setup/query/recovery documentation |
| https://apps.apple.com | Manual app download traffic | Install CSV export app on iPhone |
| Client-configured model provider (runtime-dependent endpoint) | Tool results, including possible schema sample rows and health summaries | Client inference, only after informed authorization |

The MCP server itself performs no remote health-data upload; the client/provider boundary is separate and must be checked before even schema discovery.

## Security & Privacy

- Package acquisition and optional iPhone exporter acquisition involve their providers. Confirm those operations explicitly.
- Original exports and opted-in notes under `<state_root>/` remain local unless the user separately authorizes a transfer. Store reproducible query text and minimal freshness/configuration pointers rather than raw health rows.
- MCP results pass to the client and may reach its configured model provider. Local server execution does not guarantee local-only analysis. Establish this data path before schema/query/report calls, and minimize sensitive results.
- This workflow uses exported CSVs; it neither authenticates to iCloud Health nor bypasses Apple permission prompts. Uploading exports needs explicit destination-specific authorization.
- Keep raw-row output for an explicit user request after checking the same egress boundary. Reports summarize recorded data; personal diagnosis and treatment decisions belong to a clinician.
- SQL is one analytical statement. Package query/file restrictions reduce side effects but are not process isolation; the export directory can remain writable. Run only trusted local stdio clients and SQL. Preserve the original export and use OS/process isolation for untrusted SQL.

## Trust

By using this skill, you rely on third-party tooling (`@neiltron/apple-health-mcp` and the chosen iPhone export app).
Install and run only after the user trusts and authorizes those tools. Verify the exact package/version, export path and MCP client; related-skill metadata grants no installation permission.

Read `references/sources.md` when checking version-sensitive package capabilities, privacy boundaries, import semantics or recovery advice.
