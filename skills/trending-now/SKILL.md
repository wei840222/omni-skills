---
name: trending-now
description: >
  Monitor topic watchlists with heartbeat cadence, cross-network validation,
  freshness scoring, and concise actionable alerts (or HEARTBEAT_OK). Use when
  the user wants "what's trending", brand/industry/culture spike detection,
  X-plus-community-plus-publisher confirmation, or recurring trend heartbeats.
  Prefer `news` for personalized briefings, `digest` for curated recurring
  digests, `competitor-monitoring` for company dossiers/pricing moves,
  `in-depth-research` when a weak signal needs a deep dive, and `monitoring`
  for uptime/coverage ladders rather than social trend narrative.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📈","requires":{"bins":[],"config":["<state_root>/"]},"os":["darwin","linux","win32"],"displayName":"Trending Now"}'
  related-skills: '{"monitoring":"Uptime/coverage ladders and infra heartbeats once the ask is service health, not social narrative.","news":"Personalized news briefings and interest profiles instead of thresholded trend alerts.","competitor-monitoring":"Competitor dossiers, pricing, and positioning alerts beyond a single trend spike.","in-depth-research":"Expand a weak or contested trend into evidence-backed analysis.","digest":"Recurring curated digests with preference learning instead of score-gated trend heartbeats."}'
---

# Trending Now

Heartbeat-driven **trend monitoring** with progressive disclosure: define topic scope, gather fast + community + validation signals, score freshness/novelty/relevance, and send a short alert only when the threshold is met. Otherwise return exactly `HEARTBEAT_OK`.

## State location

Trend preferences, topics, run history, and alert outcomes may live under
`<workspace>/trending-now/`, `<workspace>/memory/trending-now/`, or
`~/trending-now/`. `<workspace>` is the host/runtime workspace root, never the
shell cwd.

Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/trending-now/`, `<workspace>/memory/trending-now/`,
   `~/trending-now/`.
3. If multiple candidates exist, keep the highest-precedence one only, report
   the conflict, and leave other copies unchanged.
4. If none exists and persistent state must be created, default to
   `<workspace>/trending-now/` after brief consent on first write.

Use only the selected `<state_root>` for every state path in this skill. Never
write the literal string `<state_root>` to disk. Keep credentials and private
account tokens out of the skill package and out of git.

```text
<state_root>/
|-- memory.md    # Activation behavior, scope, and monitoring preferences
|-- topics.md    # Active topics, query variants, and relevance boundaries
|-- runs.md      # Heartbeat run history and change detection summary
`-- alerts.md    # Alerts sent, impact notes, and false-positive log
```

## When to load

Load when the user wants:

- recurring "what is trending" checks for named brands, products, industries, culture, or breaking events
- heartbeat topic watchlists with score thresholds and cooldown
- cross-network confirmation (high-velocity + community + publisher/search)
- concise mobile-ready alerts with one next action

Prefer other skills when the ask is mainly:

- personalized morning/evening news briefing → `news`
- preference-learned recurring digest → `digest`
- competitor pricing/feature dossiers → `competitor-monitoring`
- deep dive on one contested claim → `in-depth-research`
- service uptime / RED-USE coverage ladder → `monitoring`

## Progressive disclosure

| Need | File |
|------|------|
| First-run consent, scope, and state init | `references/setup.md` |
| Discovery → validate → score → decide loop | `references/research-protocol.md` |
| Source families, tiers, and blend rules | `references/source-map.md` |
| Gate 6 primary URLs | `references/sources.md` |
| Production heartbeat contract template | `assets/HEARTBEAT.md` |
| `memory.md` seed structure | `assets/data-templates.md` |
| Alert / escalation / `HEARTBEAT_OK` formats | `assets/message-format.md` |

## Requirements

- Web access for live public-source lookups the user approves.
- User-approved topic, geography, and language scope.
- Timezone and active hours before proactive heartbeat delivery.

Verify trend currency with timestamped evidence from at least two independent
source families before alerting.

## Core rules

### 1. Lock topic scope before monitoring

Each topic needs:

- intent (`brand`, `product`, `industry`, `culture`, or `breaking-event`)
- inclusion / exclusion criteria
- audience and geography boundaries

Without scope, monitoring becomes noisy and low trust. Expand scope mid-cycle
only with explicit user approval.

### 2. Treat `assets/HEARTBEAT.md` as the operating contract

Every cycle follows one contract:

- actionable update → send one structured alert per topic
- no decision-relevant movement → return exactly `HEARTBEAT_OK`

Skip filler summaries when nothing crossed the threshold.

### 3. Require source diversity; treat X as a fast signal only

For each topic, gather evidence from:

- a high-velocity channel (X or equivalent) for narrative emergence
- at least one community source (Reddit, forums, niche communities)
- at least one publisher or search-trend validation source

Single-network spikes are hypotheses, not confirmed trends. Prefer Tier 1
timestamped sources plus at least one supporting Tier 2 source before alert.

### 4. Enforce freshness windows

Classify findings by age (UTC):

- hot: `<= 6` hours
- recent: `<= 24` hours
- stale: `> 24` hours

Escalate only hot or recent signals unless the user explicitly asks for a longer
horizon.

### 5. Score before alerting

Score each candidate 0–100:

- volume shift: 0–25
- cross-source confirmation: 0–25
- novelty versus prior runs: 0–20
- user relevance: 0–20
- action urgency: 0–10

If below the topic threshold, store on the watchlist and do not alert. Prefer
two consecutive threshold hits before escalate unless urgency is critical.
Apply the cooldown in `assets/HEARTBEAT.md` after an alert.

### 6. Ship decision-ready alerts

Every alert includes:

- what changed
- why it matters now
- confidence and main risk
- one concrete next action
- 2–4 source labels or links

Keep length mobile-readable. Avoid sensational language.

### 7. Protect cost and credibility

Start with low-cost checks; deepen only after a preliminary score passes the
deep-verification floor in `assets/HEARTBEAT.md`. Use paid APIs only with
explicit budget approval. Mark uncertain claims instead of overstating certainty.

## Operating loop

1. Resolve `<state_root>` once; load `memory.md` / `topics.md` when present.
2. On first use or empty state, follow `references/setup.md` and seed from
   `assets/data-templates.md` / `assets/HEARTBEAT.md`.
3. Run `references/research-protocol.md` with the blend in
   `references/source-map.md`.
4. Decide alert / watchlist / `HEARTBEAT_OK`; format via
   `assets/message-format.md`.
5. Append run and alert outcomes to `<state_root>/runs.md` and
   `<state_root>/alerts.md` when durable logging is enabled.

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| `https://x.com` | Topic keywords and public post metadata references | Fast narrative and framing shifts |
| `https://www.reddit.com` | Topic keywords and thread metadata references | Community recurrence and depth |
| `https://news.google.com` | Topic keywords and article metadata references | Publisher coverage and recency |
| `https://trends.google.com` | Query terms and interest snapshots | Relative demand momentum |

Send no other external data unless the user explicitly approves additional
sources. Do not access private social accounts or auto-post by default.

## Security and privacy

Leaves the machine:

- topic keywords used for live research
- public source lookups for recency and momentum

Stays local under `<state_root>/`:

- monitoring preferences and topic definitions
- run history, confidence scores, and alert outcomes

This skill does not post to social networks, scrape private accounts by default,
or run undeclared paid APIs without approval.

## Trust

Public internet and social sources can be noisy, amplified, or adversarial.
Install and run only if the user trusts the approved sources and research
services. Re-check primary URLs in `references/sources.md` before locking
time-sensitive claims.

## Execution anchors

- Treat X repost volume as an early signal that still needs cross-family validation.
- Validate across multiple source families before calling a spike a trend.
- Apply strict recency windows so old stories are not shipped as breaking.
- Include one actionable recommendation with every alert.
- Keep the approved topic scope unless the user expands it.
- Anchor conclusions with links and timestamps for later audit.
