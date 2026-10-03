# Runtime failure recovery — Apple Health

Load after startup/native-module failure. Preserve the exact error, selected package version, Node version and client command. Recover the failing layer rather than silently changing ingest tools.

| Trigger | First action | If still blocked |
|---|---|---|
| Node engine mismatch | Compare `node -v` with verified package engines (1.4.5: >=22); use an already approved compatible runtime | Report the required runtime change; obtain authorization before installing/changing it |
| Missing `duckdb.node` or native load error | Confirm Node/platform/package compatibility and the client's actual executable path; perform one authorized retry through that client | Retain logs, consult maintainer docs/issues; report integration blocked rather than assuming an arbitrary Node switch fixes it |
| No catalog tables | Verify the absolute export directory, readable HK CSV files and supported Simple Health Export CSV shape | Request the correct CSV export; native XML is not a supported substitute |
| Unknown table/column | Repeat authorized schema discovery and adapt SQL to observed names/units/labels | Record schema mismatch; report no analysis until a query succeeds |
| Memory load error | Explain full-history loading and 2048MB documented default; measure approved host capacity | Use a smaller user-approved export or authorized limit adjustment; preserve source files |
| Client/provider egress unacceptable | Leave health tools unused, including schema sample rows | Offer an explicitly approved local-only analysis path; state it is not the verified MCP setup |

## Alternative CLI boundary

The former healthkit-sync/apple-watch raw-document links returned HTTP 404 during the audit. Their advertised CLI commands are not a verified recovery path and have been removed. No guessed replacement package or live sync is invoked.

Use the maintained MCP documentation at https://github.com/neiltron/apple-health-mcp and the full source records in `references/sources.md`. If MCP remains unavailable, report the precise blocker. Manual inspection of supported local CSVs is an option only after the user authorizes its tool/data path; it does not count as a successful MCP setup. Apply the same source overlap, time, units, freshness and privacy rules to any alternate analysis.
