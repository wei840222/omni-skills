# Monitor Analysis

Resolve `<state_root>` as SKILL.md specifies, and bind its actual path to `state_root`. Read the optional `<state_root>/logs/{name}/YYYY-MM.jsonl` files only after they contain observed results. A missing log means unavailable evidence, not 100% availability. Use the user-confirmed name and reporting period rather than the example path below.

Expected record fields are `ts` (UTC), `status` (`ok`, `fail`, `unknown`), and optional nonnegative numeric `latency_ms` in milliseconds. Retain transport diagnostics separately. Validate input JSONL and report malformed records; repair requires an explicit data-recovery decision.

## Sampled Availability

This is the percentage of **known sampled checks** that succeeded, not time-weighted uptime or a contractual SLA. Report unknown observations and known-sample count alongside it. Missed scheduler runs are not present in this count and must be reported from scheduler evidence separately.

```bash
jq -s '
  map(select(.status == "ok" or .status == "fail")) as $known |
  ($known | length) as $n |
  {
    known_samples: $n,
    unknown_samples: (map(select(.status == "unknown")) | length),
    sampled_availability_percent:
      (if $n == 0 then null
       else (($known | map(select(.status == "ok")) | length) / $n * 100)
       end)
  }
' "$state_root/logs/http-api-prod/2024-03.jsonl"
```

A null result means no known samples. Unequal intervals, missing data and maintenance exclusions need an explicit time-based method before reporting uptime.

## Latency Statistics

Filter to measured nonnegative numeric values. This example uses the explicit empirical index `floor((n-1)*q)` for percentiles; document the estimator and sample count when comparing periods.

```bash
jq -s '
  [.[].latency_ms | select(type == "number" and . >= 0)] | sort |
  length as $n |
  if $n == 0 then
    {samples: 0, p50: null, p95: null, p99: null, avg: null}
  else
    {
      samples: $n,
      p50: .[(($n - 1) * 0.50 | floor)],
      p95: .[(($n - 1) * 0.95 | floor)],
      p99: .[(($n - 1) * 0.99 | floor)],
      avg: (add / $n)
    }
  end
' "$state_root/logs/http-api-prod/2024-03.jsonl"
```

Latency sample eligibility (all completed HTTP responses or successful responses only) is a user-defined reporting policy; use the same policy and estimator across comparisons. Empty, singleton and missing-latency samples are valid analysis cases rather than division/index errors.

## Patterns and Trends

- Group failures by hour or weekday using an explicit reporting timezone. Summarize observed patterns such as morning failures or weekend latency without inferring causes.
- Compare equivalent periods and the same monitor/predicate. Identify user-confirmed maintenance windows separately.
- The original suggested P95 rise threshold of **20%** is an optional policy, not a benchmark. Obtain authorization before scheduling a trend alert. A zero/missing prior P95 cannot support a percentage increase; report absolute values instead.
- Request the required sample minimum when the user needs actionable trend alerts. Sparse samples and changed intervals lower confidence.

## Weekly Summary

Use `assets/weekly-summary.md` directly listed in SKILL.md. Replace every illustrative date, monitor and figure with observed log evidence. Label availability as sampled; distinguish known checks, unknown checks, missed runs and notification delivery gaps. Report sampled incident durations and specify the percentile estimator.

## Suggested Monitors

Offer related checks only as suggestions: website → API health, API → certificate expiry, production → staging. A suggestion is not consent to create a definition, execute a new check or schedule a job.

## Source

- jq array filtering, sorting, numeric operations and indexing: https://jqlang.org/manual/

Sample eligibility, percentile estimator, 20% threshold and reporting conventions above are declared package policy, not jq defaults or external service guarantees.
