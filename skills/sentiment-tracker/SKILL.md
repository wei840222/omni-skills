---
name: sentiment-tracker
description: >
  Monitor brand, product, crypto, and competitor public sentiment across X,
  Reddit, YouTube, Hacker News, TikTok, and news with one-shot reports,
  multi-entity comparison, baseline alerts, and local entity history. Use when
  the user asks what people are saying, wants ongoing mention monitoring, or
  needs relative sentiment between entities. Not for internal app analytics
  (`analytics`), brand identity systems (`branding`), or infrastructure/HTTP
  health checks (`monitor`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📊"}'
  related-skills: '{"analytics":"Web traffic and conversion measurement rather than public social sentiment.","branding":"Brand strategy and identity systems used to interpret perception, not live mention sampling.","monitor":"Recurring HTTP/TLS/process health checks rather than social-opinion tracking."}'
---

## State location

Optional durable sentiment state may exist in
`<workspace>/sentiment-tracker/`, `<workspace>/memory/sentiment-tracker/`, or
`~/sentiment-tracker/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/sentiment-tracker/`, `<workspace>/memory/sentiment-tracker/`, `~/sentiment-tracker/`.
3. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
4. If none exists and durable tracking must be created, default to
   `<workspace>/sentiment-tracker/` only with user consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/sentiment-tracker/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.
Legacy `~/sentiment-analysis/` trees are migration sources only; copy with
explicit authorization, validate, cut over, and keep a rollback copy.

**Data layout**

```text
<state_root>/
├── memory.md                 # Config, entities, preferences
├── entities/                 # One file per tracked entity
│   └── {entity}.md
├── reports/                  # Generated analysis reports
│   └── YYYY-MM-DD-{entity}.md
└── alerts.md                 # Alert history
```

Avoid storing secrets, private account credentials, or non-public post bodies
that the host is not already authorized to read.

## Role

Act as a careful public-opinion analyst: sample multiple platforms, quantify
sentiment with an explicit time window, separate volume from valence, and only
alert on meaningful baseline deviations.

## When to use

- One-shot: "What are people saying about [brand/product/crypto]?"
- Ongoing: "Monitor [entity] and alert me on negative spikes"
- Comparison: "Compare sentiment: [A] vs [B]"
- Theme digests after launches, incidents, or campaigns

Hand off when a sibling owns the job:

| Job | Skill |
| --- | --- |
| Traffic/conversion analytics | `analytics` |
| Brand identity / messaging systems | `branding` |
| HTTP/TLS/process health monitors | `monitor` |

## Setup

On first use, read `references/setup.md` and follow its order: answer the
immediate question first, then offer ongoing tracking, then capture preferences
into `<state_root>/memory.md`.

## Ordered workflow

1. **Clarify entity + window** — name/keywords, platforms if specified, default
   window **last 7 days** unless the user sets 24h / 30d / custom.
2. **Resolve state** — bind `<state_root>` before any write; one-shot answers may
   skip persistence until the user opts into monitoring.
3. **Sample ≥2–3 sources** — prefer complementary bias (e.g. X + Reddit + news).
   Note source mix and sampling limits in the report.
4. **Read posts, not only keywords** — discount sarcasm, meme copy, coordinated
   spam, and PR-filtered headlines when labeling valence.
5. **Quantify** — volume, % positive / negative / neutral, top themes, notable
   posts with platform + engagement context.
6. **Compare baselines** — for monitored entities, load prior entity history
   before claiming a spike or recovery.
7. **Alert only on meaning** — negative share >20% above baseline, viral
   negative (>10× normal engagement), new negative theme, or competitor
   positive spike the user cares about.
8. **Persist when authorized** — update entity file, append report, log alerts;
   keep schedules in `memory.md` and deliver through the user-preferred channel.

Failure branches:

- Too few public hits → report low-confidence / insufficient sample; do not invent percentages.
- Single-platform-only access → state the bias explicitly and avoid strong claims.
- Conflicting state roots → stop writes until the user picks one root.
- Private or authenticated content required → stay on public sampling; request
  an explicit grant before any logged-in path.

## Report shape

```text
📊 Entity: [Name]
🕐 Period: [Date range]
📈 Volume: [N mentions sampled]
😊 Positive: XX% | 😠 Negative: XX% | 😐 Neutral: XX%

Top Themes:
1. [Theme] — N mentions, XX% negative|positive
2. [Theme] — N mentions, XX% negative|positive

Notable Posts:
- "[quote]" — [platform, engagement]
```

Multi-entity comparison:

```text
📊 Sentiment Comparison (Last 7d)

| Entity | Volume | Positive | Negative | Trend |
|--------|--------|----------|----------|-------|
| Brand A | 1240 | 62% | 18% | ↗️ +5% |
| Brand B | 890 | 45% | 32% | ↘️ -8% |
```

## Scheduled monitoring

When the user wants ongoing tracking, prefer host automation the workspace
already exposes (cron / heartbeat / equivalent). Defaults if unspecified:

- Critical entities: daily ~09:00 local
- Regular entities: every 3 days
- Background entities: weekly

Store schedule + alert threshold in `<state_root>/memory.md`. A schedule entry
alone is not proof a job runs—confirm the durable job or say it is pending.

## Source bias cheat-sheet

| Source | Typical bias / use |
| --- | --- |
| X | Real-time, emotional, viral; API limits may force search/manual sampling |
| Reddit | Longer threads, niche subs, often harsher tone |
| YouTube | Product experience in comments; creator framing |
| Hacker News | Tech-skeptical early-adopter lens |
| TikTok | Fast visual trends; younger cohorts |
| News | Official/PR-filtered narratives |

## Common failure modes → recovery

| Trap | Recovery |
| --- | --- |
| Single-source skew | Add 1–2 contrasting platforms before concluding |
| No time window | Restate window; default 7d |
| Volume ≠ positivity | Always pair volume with valence % |
| Keyword-only sarcasm | Read representative posts; mark uncertain labels |
| Alert fatigue | Keep >20% baseline / viral / new-theme gates |

## External data boundaries

| Path | Data | Purpose |
| --- | --- | --- |
| Host web search | Query text | Find public mentions |
| Host web fetch | Public URL requests | Read public pages/posts |

Prefer host-local analysis. Do not invent API keys. Persist only under
`<state_root>/`. Public fetch/search is read-oriented sampling of content the
user already asked to inspect.

## Operating defaults

- Answer the one-shot question before upselling monitoring.
- Cross-reference platforms; state sample size and limits.
- Keep alerts rare and baseline-relative.
- Load `references/memory.md` when creating or reshaping state files.
- Load `references/sources.md` when refreshing method or platform caveats.
- Load `references/setup.md` on first-run onboarding.

## Quick reference

| Topic | File |
| --- | --- |
| First-run onboarding | `references/setup.md` |
| Memory / entity templates | `references/memory.md` |
| Method & platform sources | `references/sources.md` |
