---
name: prom
description: Diagnose cardinality explosions, write efficient PromQL, configure alerts,
  and manage Prometheus TSDB performance. Use when resolving monitoring issues, debugging
  missing metrics, or optimizing Prometheus storage and scrape configs.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🎉"}'
---

## Cardinality Explosions

- Every unique label combination creates a new time series — `user_id` as label kills Prometheus
- Remove high-cardinality labels: user IDs, email addresses, request IDs, timestamps, UUIDs
- Check cardinality: `prometheus_tsdb_head_series` metric — above 1M series needs attention
- Use histograms for latency, instead of per-request labels — buckets are fixed cardinality
- Relabeling can drop dangerous labels before ingestion: `labeldrop` in scrape config

## Histogram vs Summary

- Histograms: use for SLOs, aggregatable across instances, buckets defined upfront
- Summaries: use when you need exact percentiles, cannot aggregate across instances
- Histogram bucket boundaries must be defined before data arrives — wrong buckets = wrong percentiles
- Default buckets (.005, .01, .025, .05, .1, .25, .5, 1, 2.5, 5, 10) assume HTTP latency — adjust for your use case


## Native Histograms
- Native histograms (experimental/beta) use high-resolution buckets dynamically, solving the upfront bucket definition problem.
- Enable via `--enable-feature=native-histograms`.
- Use native histograms when you cannot predict latency distribution or need to aggregate without losing precision.

## Rate and Increase

- `rate()` requires range selector at least 4x scrape interval — `rate(metric[1m])` with 30s scrape misses data
- `rate()` is per-second, `increase()` is total over range — distinguish them carefully
- Counter resets on restart — `rate()` handles this, raw delta lacks this handling
- `irate()` uses only last two samples — too spiky for alerting, use `rate()` for alerts

## Alerting Mistakes

- Alert on symptoms, instead of causes — "high latency" instead of "high CPU"
- `for` clause prevents flapping: `for: 5m` means condition must hold 5 minutes before firing
- Missing `for` clause = fires immediately on first match = noisy
- Alerts need `runbook_url` label — on-call needs to know what to do, beyond simply recognizing a failure
- Test alerts with `promtool check rules` — syntax errors discovered at 3am are bad

## PromQL Traps

- `and` is intersection by labels, rather than boolean AND — results must have matching label sets
- `or` fills in missing series, leaves values unchanged without boolean OR
- `{}` without metric name is expensive — scans all metrics
- `offset` goes back in time: `metric offset 1h` is value from 1 hour ago
- Comparison operators filter series: `http_requests > 100` drops series below 100, returns the filtered numeric values

## Scrape Configuration

- `honor_labels: true` trusts source labels — use only when source is authoritative (e.g., Pushgateway)
- `scrape_timeout` must be less than `scrape_interval` — otherwise overlapping scrapes
- Static configs require a restart to reload — use file_sd or service discovery for dynamic targets
- TLS verification disabled (`insecure_skip_verify`) should be temporary, must be removed before production

## Pushgateway Pitfalls

- Pushgateway is for batch jobs, rather than services — services should expose /metrics
- Metrics persist until deleted — stale metrics from dead jobs confuse dashboards
- Add job and instance labels to distinguish sources — default grouping hides failures
- Delete metrics when job completes: `curl -X DELETE http://pushgateway/metrics/job/myjob`

## Recording Rules

- Pre-compute expensive queries: `record: job:request_duration_seconds:rate5m`
- Naming convention: `level:metric:operations` — helps identify what rules produce
- Recording rules update every evaluation interval — incorporating a slight execution delay
- Reduce cardinality with recording rules: aggregate away labels you can omit from alerting

## Federation and Remote Write

- Federation for pulling from other Prometheus — use sparingly, adds latency
- Remote write for long-term storage — Prometheus local storage is meant for short-term retention
- Remote write can buffer during outages — but buffer is finite, data loss on extended outages
- Prometheus is not highly available by default — run two instances scraping same targets

## Common Operational Issues

- TSDB corruption on unclean shutdown — use `--storage.tsdb.wal-compression` and monitor disk space
- Memory grows with series count — each series costs ~3KB RAM
- Compaction pauses during high load — leave 40% disk headroom
- Scrape targets stuck "Unknown" — check network, firewall, target actually exposing /metrics

## Label Best Practices

- Use labels for dimensions you'll filter/aggregate by — environment, service, instance
- Keep label values low-cardinality — tens or hundreds, instead of thousands
- Consistent naming: `snake_case`, prefix with domain: `http_requests_total`, `node_cpu_seconds_total`
- `le` label is reserved for histogram buckets — reserve strictly for bucket definition
