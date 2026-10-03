# Verified sources — Apple Health

Checked 2026-10-03. Source snapshots and HTTP results are held in the workflow's repair audit outside this package. Package requirements were cross-checked with npm version 1.4.5; maintainer main-branch docs describe current behavior and should be rechecked against an installed version before assuming a later capability. No price, account policy or exporter privacy guarantee is inferred.

## Package/runtime/export/privacy (version-sensitive)

- **npm published package metadata** — version 1.4.5, engines Node >=22, executable `apple-health-mcp`: https://registry.npmjs.org/@neiltron/apple-health-mcp/latest
- **Maintainer README** — Simple Health Export CSV layout, native XML unsupported, stdio config, tools, defaults 2048MB/100 cached results, full-history in-memory loads, client/model-provider egress: https://raw.githubusercontent.com/neiltron/apple-health-mcp/main/README.md
- **Maintainer querying guide** — `valueText` category labels, asleep filtering, source/unit separation, schema-discovered workout tables, tool arguments, discarded source timezone offset and misleading output Z: https://raw.githubusercontent.com/neiltron/apple-health-mcp/main/docs/querying.md
- **Maintainer architecture** — import catalog and normalized columns, one analytical statement, query/file safeguards and limits, writable export directory, lack of process isolation, full-history lazy loading and explicit memory failures: https://raw.githubusercontent.com/neiltron/apple-health-mcp/main/docs/architecture.md
- **Maintained project landing page** — recovery/documentation entry point: https://github.com/neiltron/apple-health-mcp

## Skill format (stable standard / version-sensitive validator)

- **Agent Skills document index** — normative documentation discovery: https://agentskills.io/llms.txt
- **Agent Skills specification** — name/description/frontmatter metadata string map, resource directories and root-relative paths: https://agentskills.io/specification.md

## Corrected unsupported guidance

- Node 18/20 guidance replaced by verified engines >=22 for npm 1.4.5; no arbitrary runtime-switch success claimed.
- Memory default changed from 1024 to documented 2048MB.
- Local server is distinguished from MCP client/provider handling; schema sample rows and summaries may leave via that client.
- Sleep excludes awake/in-bed and separates source overlap; category labels and timezone loss are explicit.
- Combined workout table assumptions replaced by schema-discovered activity tables.
- Prior alternative raw skill URLs returned 404. Their claimed validated CLI recovery was replaced with maintained MCP diagnosis and an honest blocked/manual boundary; no speculative substitute installation.
