# Monitoring domain guidance

Practical coverage ladders, checklists, and traps preserved from the pre-refactor
`monitoring` package and aligned with SRE / Prometheus / OTel sources listed in
`sources.md`. Absolute vendor dollars are heuristics — re-check live pricing.

## Coverage tiers

| Level | Tools | Setup time | Best for |
|-------|-------|------------|----------|
| **Minimal** | UptimeRobot, Healthchecks.io | ~15 min | Side projects, MVPs |
| **Standard** | Uptime Kuma, Sentry, basic Grafana | 1–2 hours | Small teams, startups |
| **Professional** | Prometheus, Grafana, Loki, Alertmanager | 1–2 days | Production systems |
| **Enterprise** | Datadog, New Relic, or hardened OSS | Ongoing | Large-scale operations |

Start at the smallest tier that answers the actual failure mode. Jumping
straight to Prometheus for "tell me if the site is down" is a common mistake.

## Three pillars (routing)

| Pillar | Question | Typical tools | Prefer sibling when |
|--------|----------|---------------|---------------------|
| **Metrics** | How is the system performing? | Prometheus, Grafana, Datadog | Deep PromQL / cardinality / SLO → `observability`; product KPIs → `metrics` |
| **Logs** | What happened? | Loki, ELK, CloudWatch | Host journal surgery → `sysadmin` |
| **Traces** | Why is this request slow? | Jaeger, Tempo, Sentry | Full OTel collector design → `observability` |

## Quick start by use case

### "I just want to know if it's down" (Minimal)

- **UptimeRobot (SaaS):** free tier historically ~50 monitors / 5-minute
  intervals; email/Slack/Telegram/webhooks. Verify current free limits live.
- **Uptime Kuma (self-hosted):**

```bash
docker run -d --restart=unless-stopped -p 3001:3001 \
  -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1
```

  HTTP/TCP/DNS/Docker/push monitors; built-in status pages; many notification
  channels.

- **Healthchecks.io** for cron heartbeats (generous free tier historically):

```bash
curl -fsS -m 10 --retry 5 https://hc-ping.com/YOUR-UUID-HERE
curl -fsS -m 10 --retry 5 "https://hc-ping.com/YOUR-UUID-HERE/$?"
```

Outside-in URL checks beat internal-only probes.

### "I need to debug production errors" (Standard APM)

Prefer **Sentry** for most teams (errors + basic performance, strong DX).
Framework wizards (Next.js / Node) are the fast path; keep DSNs pointer-only.

OpenTelemetry is the vendor-neutral instrumentation path when you must export
to multiple backends — deeper collector / sampling guidance lives in
`observability`.

Other APM options (Datadog APM, New Relic, Jaeger, Grafana Tempo) trade cost
and ops burden; treat published per-host prices as verify-live.

### "I want real observability" (Professional OSS)

Typical scrape → store → visualize → page shape:

```text
App /metrics + exporters → Prometheus → Grafana
                              ↓
                         Alertmanager
Logs → Promtail/agents → Loki → Grafana
```

Compose sketch (pin versions at deploy time; examples below are illustrative):

```yaml
services:
  prometheus:
    image: prom/prometheus:v2.50.1
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - ./rules:/etc/prometheus/rules
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.retention.time=30d'
      - '--web.enable-lifecycle'
    ports: ["9090:9090"]
  grafana:
    image: grafana/grafana:10.3.3
    volumes: [grafana_data:/var/lib/grafana]
    environment: [GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASS}]
    ports: ["3000:3000"]
  alertmanager:
    image: prom/alertmanager:v0.27.0
    volumes: [./alertmanager.yml:/etc/alertmanager/alertmanager.yml]
    ports: ["9093:9093"]
  node_exporter:
    image: prom/node-exporter:v1.7.0
    # mount host proc/sys/rootfs per current exporter docs
  loki:
    image: grafana/loki:2.9.0
    ports: ["3100:3100"]
  promtail:
    image: grafana/promtail:2.9.0
    # mount /var/log and container logs read-only
```

Prometheus habits:

- Prefer histograms for aggregatable quantiles; use `rate()` on counters with
  range ≥ 2× scrape interval.
- Avoid unbounded label sets (`user_id`, `request_id`).
- Default scrape ~15s is usually enough; 1s scrapes explode cost/cardinality.
- Set retention explicitly (`--storage.tsdb.retention.time`); forever fills disks.
- Use recording rules for expensive repeated queries.
- Example high-CPU style rule shape (symptom still preferred for pages):

```text
100 - (avg by(instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
```

Grafana dashboard IDs commonly imported for a first pass (verify availability):
Node Exporter Full, and stack-specific boards for the services you actually run.
Deep panel craft belongs in `grafana`.

### "I need to centralize logs"

| Stack | Best for | Trade-off |
|-------|----------|-----------|
| **Loki + Grafana** | Already on Grafana; smaller volumes | Label-first; full-text slower than ELK |
| **ELK** | Complex full-text search, large volumes | Heavy (multi-GB RAM) ops cost |
| **Managed** (Grafana Cloud, CloudWatch, Papertrail, Better Stack) | Less ops | Ingest/retention pricing — verify live |

Structured JSON logs with a request/trace id beat free-form strings. Never plan
infinite retention without a budget.

## What to monitor

### Applications — RED

- **R**ate — requests per second
- **E**rrors — error rate by endpoint
- **D**uration — latency (p50, p95, p99; averages lie)

### Infrastructure — USE

- **U**tilization — CPU, memory, disk
- **S**aturation — queue depth, load average
- **E**rrors — hardware/system errors

Pair with Google SRE golden signals (latency, traffic, errors, saturation) when
designing pages; prefer symptoms that map to user impact.

## Alerting principles (handoff to `alerts`)

| Do | Don't |
|----|-------|
| Alert on symptoms (user impact) | Alert only on causes (CPU high) |
| Include a runbook / next action | Require archaeology to understand |
| Set coherent severity | Make everything P1 |
| Require human action | Page on "interesting" metrics |

**Every alert should require action.** If the response is "ignore it," delete or
demote the alert. Fatigue symptoms: muted channels, dreaded on-call, real pages
lost in noise. Common causes: >~5 noisy pages/person/day, flapping, missing
context. Fixes: raise thresholds, add for/pending windows, inhibit/group, attach
runbooks — detailed routing/webhook playbooks live in `alerts`.

Illustrative severity ladder:

| Severity | Response time | Example |
|----------|---------------|---------|
| P1/Critical | < 15 min | Production down / revenue loss |
| P2/High | < 1 hour | Major feature broken |
| P3/Medium | < 4 hours | Minor feature degraded |
| P4/Low | Next business day | Disk 70%, no user impact yet |

Routing sketch: P1 → phone/PagerDuty escalation; P2 → push + Slack; P3 → Slack;
P4 → email digest.

## Cost comparison (heuristics — verify live)

| Solution | Small (heuristic) | Medium (heuristic) |
|----------|-------------------|--------------------|
| UptimeRobot | Free tier | Low paid plan |
| Uptime Kuma | Small VPS | Small VPS |
| Sentry | Free → entry paid | Growth plan |
| Grafana Cloud | Free tier | Usage-based |
| Datadog | Per-host | Per-host + features |
| Self-hosted OSS | Small VPS | Larger VPS / ops time |

Do not paste stale dollar figures into user-facing advice without a live check
of the vendor page. Prefer ratios and "start free / expect ops time" framing.

## Common mistakes

- Starting with Prometheus/Grafana when Uptime Kuma would suffice
- Dashboards with no alerting
- Too many non-actionable alerts (fatigue)
- Missing runbooks when a page fires
- Monitoring only from inside the network
- Storing logs forever (cost explodes)
- High-cardinality labels (`user_id`, raw URLs)
- Scraping every second "just in case"
- No TSDB / log retention policy
- Skipping recording rules for hot queries
- Putting DSNs or admin passwords in git

## Semantic preservation map

| Original item | Disposition |
|---------------|-------------|
| Complexity / tier table | retained above |
| Three pillars table | retained + sibling routing |
| Quick start four use cases | retained; links → this file |
| RED / USE | retained |
| Alerting Do/Don't + fatigue | retained; deep routing → `alerts` |
| Cost table | retained as verify-live heuristics |
| Common mistakes | retained / strengthened |
| `simple.md` UptimeRobot/Kuma/Healthchecks/Sentry | folded here |
| `apm.md` Sentry/OTel/tool compare | folded; OTel depth → `observability` |
| `prometheus.md` compose + habits | folded; PromQL depth → `observability`/`grafana` |
| `logs.md` Loki/ELK/managed | folded |
| `alerting.md` severities/routing | folded summary; full playbooks → `alerts` |
| Clawic homepage / `_meta.json` / Feedback | removed (Gates 1/5) |
