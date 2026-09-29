---
name: follow
description: Track content from people, topics, and sources with smart filtering and
  tiered alerts. Use when the user wants to monitor accounts, track discussions, query
  archived content, or set up notification rules.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "👀"}'
  related-skills: '{"news": "Personalized multi-source news briefings when the user wants ongoing feed tuning rather than person/topic follow trackers.","daily-news-digest": "Scheduled daily news briefing loops when delivery is a digest cadence instead of per-source follow alerts.","summarizer": "Single-article or long-form summarization after a followed item is selected from the archive.","newsletter": "Newsletter subscribe/send workflows when the source is an owned list rather than external account monitoring.","hacker-news": "Live Hacker News API access when the follow target is HN specifically rather than generic multi-platform tracking.","digest": "General multi-source content digests outside person/topic follow state."}'
---

## State location

Follow state may exist in `<workspace>/follow/`, `<workspace>/memory/follow/`, or `~/follow/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/follow/`, `<workspace>/memory/follow/`, `~/follow/`.
3. If none exists and state must be created, default to `<workspace>/follow/`.

Use the selected `<state_root>` for every state operation in this skill.

```
<state_root>/
├── sources/           # One file per followed entity
│   ├── people/        # @naval.md, @dhh.md
│   ├── topics/        # ai-safety.md, rust.md
│   └── feeds/         # techcrunch.md, hn-frontpage.md
├── archive/           # Captured content by date
│   └── YYYY-MM/
├── alerts.md          # Alert configuration
└── index.md           # Quick status: what's being followed
```

---

## Quick Reference

| When to load | File |
|------|------|
| Add/configure sources | `references/sources.md` |
| Set up filtering rules | `references/filtering.md` |
| Configure alert tiers | `references/alerts.md` |
| Query archived content | `references/querying.md` |
| Platform-specific setup | `references/platforms.md` |

---

## Core Loop

1. **Add source**: User names person/topic/feed → create tracking file
2. **Monitor**: Check sources on schedule (cron) or on-demand
3. **Filter**: Apply relevance rules, skip noise
4. **Store**: Archive what matters (summaries, not full dumps)
5. **Alert**: Notify based on tier (immediate/daily/weekly/passive)
6. **Query**: Answer "what did X say about Y?" from archive

---

## Common Patterns

| User says | Agent does |
|-----------|------------|
| "Follow @naval on Twitter" | Create `sources/people/naval.md`, configure Twitter monitoring |
| "Track AI safety discussions" | Create topic tracker with keywords across multiple sources |
| "What has Competitor X posted this week?" | Query archive, synthesize summary |
| "Alert me immediately when Y happens" | Add to high-priority tier in `<state_root>/alerts.md` |
| "Give me a weekly digest of everything" | Configure weekly summary in alerts |
| "Pause following X" | Archive and mark inactive |

---

## Capture Principles

- **Summaries over full content** — save space, stay legal
- **Links + timestamps always** — retrievable later
- **Context for why it matters** — not just "X posted"
- **Deduplicate across sources** — same news from 5 places = 1 entry
