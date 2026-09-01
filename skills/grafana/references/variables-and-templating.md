# Variables and Templating

- Multi-value variable needs `$__all` in regex — or only first value used
- `${var:csv}` for comma-separated — `${var:pipe}` for pipe-separated in regex
- Variable in query: `$var` or `${var}` — different escaping per data source
- `$__interval` auto-adjusts to time range — use for aggregation window
- Chained variables: child depends on parent — set "Refresh" to "On time range change"

## Query Variables

Use the variable format that matches the query context: `${var:pipe}` is appropriate for a regex alternation, while `${var:csv}` is appropriate where a comma-separated value list is expected. If an interpolation result is surprising, inspect the rendered query with Grafana's query inspector and select the documented format option explicitly.

Source: [Grafana variables documentation](https://grafana.com/docs/grafana/latest/dashboards/variables/).
