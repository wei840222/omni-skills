# Setup — Apple Health

Read for first setup or existing-client troubleshooting. Resolve state using SKILL.md before accessing notes; a missing directory is not creation consent.

## 1. Confirm goal and client

Use known intent when supplied: connect now, evaluate options (`not-now`), or troubleshoot. Ask only for missing decisions. Identify the actual MCP-compatible client and configuration location from its current documentation. Planning mode leaves installations and configuration unchanged.

## 2. Confirm the export and privacy boundary

This MCP reads Simple Health Export CSV files, not live HealthKit/iCloud or native `export.xml`.
If no supported export exists, describe the maintainer's supported iPhone CSV export workflow and request the readable unzipped local directory. Installing an exporter, transferring sensitive files or paying for an app requires separate authorization. Validate an actual absolute directory with nonempty HK quantity/category/workout CSVs; preserve the original export.

Before any `health_schema`, `health_query` or `health_report` call, apply SKILL.md Security & Privacy: schema can expose sample rows and client results may reach the model provider. Establish informed authorization or use an approved local-only path instead.

## 3. Verify runtime and configure

Read `references/mcp-config.md`. Check `node -v`, `npx --version` and the exact package engines/version; published version 1.4.5 requires Node >=22. Confirm the export directory rather than inferring it from a parent archive path.
After setup authorization, merge the apple-health entry into the existing client config, preserving unrelated servers and a rollback copy. Replace sample paths before use; use stdio transport. Restart the client only according to its verified procedure.

For missing native modules/startup failure, use the bounded diagnostic path in `references/fallback-cli.md`; package launch alone is not integration verification.

## 4. Verify before analysis

1. Run authorized `health_schema`; confirm at least one catalog table and required columns/units/labels.
2. Run one analytical query from `references/query-recipes.md` adapted to that schema and an explicit finite date window.
3. Confirm the observed result's units, coverage, source and freshness. An error is not a zero-data result.

If verification fails, retain the error and fix the implicated runtime/path/schema layer before reporting trends.

## Optional retained notes

After consent, read `references/memory.md` and use `assets/memory-template.md` only for a needed child:

| Destination | Minimum content |
|---|---|
| `<state_root>/memory.md` | Status, mode, validated export pointer, freshness |
| `<state_root>/integrations.md` | Client/config pointers, verified command/env and checks |
| `<state_root>/query-log.md` | Reproducible SQL, window and unit/source/time caveats |

Keep raw rows and credentials out of retained notes. Current-day claims need a current export; unknown freshness stays unknown. Default output is aggregated recorded-data analysis, not diagnosis.
