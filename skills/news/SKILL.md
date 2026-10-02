---
name: news
description: >
  Build personalized news briefings that learn interests, format, and timing.
  Trigger when the user asks for news, morning/evening briefings, topic
  updates, multi-source contested coverage, or profile-driven current-events
  digests. Prefer `summarizer` to condense one known article, `scrape` for a
  single page extract, and `reading` for long-form reading lists instead of
  recurring briefings.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📰","os":["linux","darwin","win32"],"displayName":"News"}'
  related-skills: '{"summarizer":"Condense one known long article once the briefing already has the source.","scrape":"Extract structured content from a single URL when a briefing needs a primary document.","reading":"Maintain reading lists and long-form tracking instead of recurring news digests."}'
---

# News

Personalized **news briefings** with a durable interest profile, freshness discipline, multi-source contested coverage, and local-only memory. This skill does not invent events; it routes verification and sourcing before analysis.

## When to load

Load when the user wants:

- personalized morning/evening/on-demand news briefings
- topic-specific current-events updates tied to a learned profile
- multi-source treatment of contested or high-stakes stories
- iterative preference learning (format, timing, interest mix)

Prefer other skills when the ask is mainly:

- one known article to shorten → `summarizer`
- single-page extraction → `scrape`
- reading list / corpus tracking → `reading`

## State location

News profile and engagement history may live under `<workspace>/news/`, `<workspace>/memory/news/`, or `~/news/`. `<workspace>` is the host/runtime workspace root, never the shell cwd.

Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/news/`, `<workspace>/memory/news/`, `~/news/`.
3. If multiple candidates exist, keep the highest-precedence one only, report the conflict, and leave other copies unchanged.
4. If none exists and persistent state must be created, default to `<workspace>/news/` with brief consent on first write.

Use only the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Keep third-party private data and credentials out of the skill package and out of git.

```text
<state_root>/
├── memory.md       # Profile: interests, mix, format, timing
├── history.md      # Past briefings and engagement signals
└── sources.md      # Trusted sources and known leanings (optional)
```

On activation: load `<state_root>/memory.md` first when it exists. Load `history.md` / `sources.md` only when engagement learning or source bias notes are needed. Seed layout from `assets/memory-template.md` on first create.

## Routing

Keep this file as the progressive-disclosure router; load depth only when needed:

| Need | File |
|------|------|
| Profile build, briefing loop, multi-source rules | `references/core-rules.md` |
| Freshness, overload, generic-category traps | `references/common-traps.md` |
| Local-only data boundaries | `references/security-and-privacy.md` |
| Gate 6 primary sources | `references/sources.md` |
| First-run state tree | `assets/memory-template.md` |

## Operating loop

1. **Resolve state** — Select `<state_root>` once. If `memory.md` is missing, run first-run profile intake before delivering a full briefing.
2. **Read profile** — Interests (specific, not generic), optional mix percentages, format (bullets / narrative / headlines-only), timing preference.
3. **Gather** — Prefer named, time-stamped sources the user trusts. Cap morning briefings at 5–7 items unless the user asks for more.
4. **Structure** — Facts and “when it broke” first; analysis second; cite sources by name. Contested topics need ≥2 independent sources and explicit disagreement notes.
5. **Deliver** — Match the requested format. Flag uncertainty instead of inventing events.
6. **Learn** — After engagement (follow-ups, skips, “more of X”), propose a small profile update and write only with consent for first-time durable state.

## Core rules

1. **Profile before bulk delivery** — On first use, ask for specific interests, optional mix, format, and timing (`references/core-rules.md`).
2. **Memory first** — Read `<state_root>/memory.md` before every briefing when present.
3. **Facts before analysis** — Lead with what happened and when; then why it matters.
4. **Multi-source on contested topics** — At least two sources; note disagreements and known editorial leanings when relevant.
5. **No fabrication** — If unsure an event occurred or a detail is verified, say so and stop short of inventing.
6. **Freshness over volume** — Stale items labeled as fresh destroy trust; prefer fewer current items.
7. **Local memory only** — Preferences and history stay under `<state_root>/` (`references/security-and-privacy.md`).

## Failure modes

| Condition | Response |
|-----------|----------|
| No `<state_root>` / empty profile | Resolve state; run first-run intake; do not dump a generic mega-brief |
| Conflicting candidate state dirs | Highest-precedence only; report conflict |
| Contested topic, only one source handy | Fetch or disclose single-source limit; do not present as settled |
| Uncertain / unverified claim | State uncertainty; omit or mark provisional |
| User refuses memory writes | Deliver briefing; skip durable profile updates |
| Request exceeds 5–7 morning items | Confirm they want volume; otherwise keep the cap |

## Out of scope

- Fabricating headlines, quotes, vote totals, or market moves
- Permanent archival of full article bodies inside the skill package
- Replacing dedicated fact-check desks or legal/compliance review
- Sending profile/history to third-party analytics without explicit user authorization
- Generic “tech/world news” dumps without a learned or stated interest mix
