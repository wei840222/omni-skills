---
name: daily-news-digest
description: >
  Fetch and compile personalized news briefings from specified sources, filter
  topics, and schedule automated delivery. Use for morning/evening digests, RSS
  and public-API aggregation, topic include/exclude lists, format selection
  (brief/standard/deep-dive/audio), and OpenClaw cron delivery.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📰"}'
  related-skills: '{"news":"Personalized news with ongoing preference learning when the ask is continuous feed tuning rather than a scheduled digest.","summarizer":"Single-article or long-form summarization after a digest story is selected.","podcast":"Audio show discovery when the user wants podcasts instead of a text/voice news briefing.","schedule":"Calendar and scheduling primitives when delivery timing needs calendar coordination beyond digest cron.","digest":"General multi-source content digests outside the daily news briefing loop."}'
---

## When to load

Load this skill when the user requests daily news briefings, multi-source news summaries (RSS, Hacker News, Reddit, Brave Search), topic filtering, preferred formats, voice briefings, or scheduled automated news delivery.

Prefer `news` for continuous preference-learning feeds, `summarizer` for one-article deep reads, `podcast` for show discovery, and `digest` for non-news multi-source rollups.

## State location

Resolve `<state_root>` in this order:

1. `<workspace>/.agents/state` when a local workspace is active
2. `$XDG_DATA_HOME` when set
3. `~/.local/share` on Linux/macOS defaults

If the user or host configuration explicitly defines a state root, that path takes precedence. Resolve once per invocation and keep it fixed.

Skill state lives under `<state_root>/daily-news-digest/`. Create the directory when the first persistent write is required. Prefer portable `<state_root>` paths; never hard-code host-specific roots such as `~/Clawic/data/daily-news-digest/`.

```text
<state_root>/daily-news-digest/
|-- memory.md           # Preferences + delivery schedule + learned interests
|-- sources.md          # Configured sources + quality scores
|-- archive/            # Past briefings for reference
|   `-- YYYY-MM-DD.md
`-- cache/              # Temporary fetch cache (auto-cleaned)
```

## Setup

On first use, read `references/setup.md`. Learn activation mode, topics, sources, geography, format, and delivery schedule through conversation, then persist under the resolved state root.

## Quick reference

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` |
| Memory template | `references/memory-template.md` |
| Source configuration | `references/sources.md` |
| Briefing formats | `references/formats.md` |
| Scheduling guide | `references/scheduling.md` |

## Core rules

1. **Multi-source aggregation** — Combine RSS, Brave Search, and public APIs (Hacker News, Reddit JSON). If one source fails, continue with the others and keep partial service.
2. **Intelligent deduplication** — Treat headline similarity >70% as the same story; keep the most detailed version; note covering outlets; present each story once.
3. **Priority scoring** — Rank by user topic match (+40), multi-outlet coverage (+25), breaking/trending (+20), trusted source (+15), recency last 6h (+10)—not recency alone.
4. **Respect preferences** — Read memory before fetching: include/exclude topics, preferred/blocked outlets, geography emphasis, schedule. On conflict, ask once.
5. **Format adaptation** — Brief (3–5 headlines), Standard default (8–12 stories), Deep Dive, Audio (TTS), or Archive markdown under `archive/`.
6. **Time-aware delivery** — Morning forward-looking; midday breaking focus; evening missed-story recap; weekend lighter tone.
7. **Interactive deep-dive** — End briefings with “Reply with any story number to dive deeper.” On a number: fetch fuller content, summarize with context, show related stories, offer the article link.
8. **Scheduled delivery** — Use OpenClaw cron for automated briefings; track delivery history in memory and skip duplicate sends for the same window.
9. **Source quality tracking** — Score accuracy, paywall frequency, ad density, freshness, and user feedback in `sources.md`; deprioritize low-quality sources over time.
10. **Graceful degradation** — Log source failures, continue with remaining sources, and mention unavailable sources only when the gap is material.

## Operating loop

1. **Load preferences** — Read `<state_root>/daily-news-digest/memory.md` (and sources.md).
2. **Fetch** — Pull configured sources per `references/sources.md`.
3. **Normalize** — Dedup, score, filter by preferences and age (>24h only when requested).
4. **Render** — Apply format + time-of-day tone from `references/formats.md`.
5. **Deliver** — On-demand reply or cron channel delivery; offer deep-dive numbers.
6. **Persist** — Update delivery history, quality scores, and optional archive entries.

## Failure modes

| Failure | Detection | Recovery |
|---|---|---|
| Source outage | Fetch error / empty payload | Log, continue with other sources, note gap only if material |
| Paywall | Content truncated or login wall | Warn user, prefer alternate outlet covering same story |
| Overwhelming volume | Too many unique stories | Default Standard 8–12; keep Brief on “quick update” |
| Stale stories | Age >24h | Skip unless user asks for backlog/archive |
| Duplicate delivery | Same schedule window already sent | Skip; record in memory delivery history |
| Preference conflict | Include and exclude collide | Ask one clarifying question before fetching |

## Common traps

- Defaulting to every story → stay on Standard/Brief bounds
- Ignoring story age → filter >24h unless requested
- Surprising paywalls → detect, warn, offer alternate source
- Missing local news → capture geography on first setup
- Skipping dedup → always dedup before present
- Silent total failure → never fail the whole briefing on one dead source

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| RSS feed URLs | None (GET) | Headlines |
| Brave Search API | Query text | Trending/breaking |
| Hacker News API | None (GET) | Tech news |
| Reddit JSON API | None (GET) | Public subreddit feeds |
| ElevenLabs TTS (optional) | Briefing text | Voice synthesis |

**Credential handling:** Brave Search and ElevenLabs credentials come from OpenClaw platform configuration. RSS, Hacker News, and Reddit public APIs need no auth. Scheduled deliveries use OpenClaw channel integrations.

## Security and privacy

**Leaves the machine:** search queries to Brave; briefing text to TTS when voice is enabled.

**Stays local:** preferences, archives, source quality scores under `<state_root>/daily-news-digest/`; no telemetry.

**This skill does not:** share reading habits with third parties; store credentials in plain text; access files outside the resolved state root; modify itself or other skills.

**Trust:** enable voice synthesis only when the user accepts sending briefing text to the configured TTS provider.

## Related skills

- `news` — personalized news with learning
- `summarizer` — article summarization
- `podcast` — audio content discovery
- `schedule` — calendar and scheduling
- `digest` — general content digests
