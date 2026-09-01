# Variables and Templating

- Multi-value variable needs `$__all` in regex — or only first value used
- `${var:csv}` for comma-separated — `${var:pipe}` for pipe-separated in regex
- Variable in query: `$var` or `${var}` — different escaping per data source
- `$__interval` auto-adjusts to time range — use for aggregation window
- Chained variables: child depends on parent — set "Refresh" to "On time range change"
