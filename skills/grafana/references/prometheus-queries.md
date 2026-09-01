# Prometheus Queries

- Use a range vector with `rate()`, for example `rate(requests_total[5m])`.
- `rate()` for counters, `deriv()` for gauges — rate handles counter resets
- Prefer `$__rate_interval` to adapt the rate window to the scrape interval and dashboard range.
- Labels in legend: `{{label}}` — multiple: `{{instance}} - {{job}}`
- Regex filter: `metric{label=~"val1|val2"}` — `!~` for negative match
