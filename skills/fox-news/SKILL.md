---
name: fox-news
description: >
  Monitor Fox News sections and breaking updates with official RSS routes,
  event live-page follow-through, and optional outside verification. Use when
  the user wants Fox-owned headlines, section sweeps, Fox-first briefings, or
  clip/article packaging that keeps reporting and opinion separate. Prefer
  `news` for multi-outlet personalized briefings, `hacker-news` for HN API
  work, `apple-news` for News.app/Shortcuts on macOS, `digest` for recurring
  curated digests, and `summarizer` to compress one already-chosen article.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🦊","requires":{"bins":["curl"],"anyBins":["python3","python"]}}'
  related-skills: '{"news":"Personalized multi-outlet briefings once the ask is broader than Fox-owned surfaces.","hacker-news":"Live Hacker News API/search rather than Fox RSS or section pages.","apple-news":"macOS News.app and Apple News Shortcuts instead of Fox web/RSS workflows.","digest":"Recurring curated digests across many sources when Fox is only one input.","summarizer":"Compress one known Fox article or transcript after the source is already chosen.","scrape":"Extract structured content from a single Fox URL when the briefing needs a primary document."}'
---

# Fox News Monitor

Fox-owned **section routing, RSS sweeps, and event live-page follow-through**. Keep reporting, video/clips, and opinion on separate surfaces. Treat outside corroboration as an explicitly labeled follow-up block only.

## When to load

Load when the user wants:

- Fox News section monitoring or Fox-owned headline sweeps
- Fox-first briefings with optional outside verification
- event live-page updates, clips, or article packaging from Fox properties

Prefer other skills when the ask is mainly:

- multi-outlet personalized briefings → `news`
- Hacker News API/search → `hacker-news`
- Apple News.app / Shortcuts → `apple-news`
- recurring multi-source digests → `digest`
- one known article to shorten → `summarizer`

## State location

Optional preferences and run notes may live under `<workspace>/fox-news/`, `<workspace>/memory/fox-news/`, or `~/fox-news/`. `<workspace>` is the host/runtime workspace root, never the shell cwd.

Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/fox-news/`, `<workspace>/memory/fox-news/`, `~/fox-news/`.
3. If multiple candidates exist, keep the highest-precedence one only, report the conflict, and leave other copies unchanged.
4. If none exists and persistent state must be created, describe the write, obtain confirmation, then default to `<workspace>/fox-news/`.
5. Keep the resolved `<state_root>` fixed for the invocation. Never write the literal string `<state_root>` to disk.

```text
<state_root>/
├── memory.md    # Activation scope, preferred sections, balance defaults
├── sources.md   # Approved Fox surfaces and section notes
├── runs.md      # Fetch timestamps, live-event notes, follow-up history
└── briefs/      # Saved briefings only when the user asks to archive them
```

If older notes exist at `~/Clawic/data/fox-news/`, migrate them into the resolved `<state_root>/` on first write and say in one line that you moved them and from where. Seed new memory from `assets/memory-template.md`.

## Workflow

1. Confirm the request is Fox-specific and map it to **one** primary surface before fetching.
2. Load `references/feed-map.md` for the matching RSS/page route; use RSS for deterministic headline capture and page routes for section context or event live pages.
3. Load `references/workflow-patterns.md` for the matching pattern (section sweep, breaking follow-through, opinion/video, multi-link, app/device).
4. Load `references/briefing-formats.md` when shaping the reply; keep surface labels and timestamps on every freshness claim.
5. If the user wants analysis, controversy review, or credibility checking, keep the Fox block first and add outside corroboration as a separate labeled block.
6. Load `references/troubleshooting.md` when RSS is empty/stale, a stream is gated, opinion leaks into news, or a story feels one-sided.
7. Persist only durable preferences under `<state_root>/` after consent; skip full article bodies unless the user asks to archive a brief.

## Progressive disclosure

| File | Load when |
|---|---|
| `references/feed-map.md` | Choosing RSS feeds, section pages, or event live-page routing |
| `references/workflow-patterns.md` | Running a section sweep, live follow-through, opinion/video, or multi-link flow |
| `references/briefing-formats.md` | Formatting quick scans, standard briefings, balanced follow-up, or live updates |
| `references/troubleshooting.md` | Recovering from empty feeds, gated streams, mixed surfaces, or contested claims |
| `references/sources.md` | Citing or refreshing official Fox surface evidence |
| `assets/memory-template.md` | Creating `<state_root>/memory.md` on first persist |

## Core rules

1. **One surface first** — homepage/latest, section feed/page, event live page, video, or opinion — before widening.
2. **Label the surface type** before summarizing; keep opinion and video out of straight-news briefings unless requested.
3. **Timestamp freshness claims**; mark older items as recap/background instead of breaking.
4. **Fox-owned sources first**; outside checks stay in a separate follow-up block.
5. **Preview high-volume work** and require confirmation before opening multiple articles, clips, or rolling updates.
6. **Stay on public surfaces** — if live TV / Fox Nation / provider login appears, state the boundary and fall back to public headlines, clips, or articles.
7. **Persist reusable preferences only** under the resolved `<state_root>/`.

## Security boundary

May leave the machine: HTTP requests to Fox News pages/RSS and optional on-site search terms the user asked for, plus user-requested outside follow-up URLs.

Stays local: activation scope, preferred sections, briefing defaults, fetch history, and archived briefs under `<state_root>/`.

Out of scope: collecting Fox/TV-provider/Fox Nation credentials, bypassing gates or paywalls, auto-posting to social platforms, and reading files outside `<state_root>/` (except host-owned paths the user explicitly names for migration).
