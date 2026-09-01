# Prometheus Queries

- Use a range vector with `rate()`, for example `rate(requests_total[5m])`.
- `rate()` for counters, `deriv()` for gauges — rate handles counter resets
- `$__rate_interval` over hardcoded — adapts to scrape interval and dashboard range
- Labels in legend: `{{label}}` — multiple: `{{instance}} - {{job}}`
- Regex filter: `metric{label=~"val1|val2"}` — `!~` for negative match
