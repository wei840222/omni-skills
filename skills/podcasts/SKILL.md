---
name: podcasts
description: Track, summarize, and manage podcasts. Use when the user follows shows,
  needs time-constrained episode briefings, wants backlog catch-up plans, extracts
  learning notes, tracks VIP guests across platforms, or works with YouTube podcast
  channels and clips. Not for music library curation (`music`), original songwriting
  (`song`), AI music generation (`music-generation`), or raw audio file processing
  (`audio`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎙️"}'
  related-skills: '{"audio": "Process or convert audio files rather than manage show subscriptions and briefings.", "journal": "Capture reflective listening notes beyond structured podcast state.", "music": "Curate personal music discoveries, playlists, and concerts rather than podcast episode workflows.", "music-generation": "Generate AI music with style prompts rather than manage podcast listening.", "song": "Write original lyrics or melody rather than track podcast episodes."}'
---

## State location

Resolve `<state_root>` once per invocation before reading or writing podcast data:

1. Use an explicitly configured podcast-state path when the host or user supplies one.
2. Otherwise use the first existing directory in this order: `<workspace>/podcasts/`, `<workspace>/memory/podcasts/`, then `~/podcasts/`.
3. If none exists and the user asks to persist podcast data, create `<workspace>/podcasts/`.
4. If more than one candidate exists, keep the highest-precedence directory, leave others independent, and tell the user which location was selected.

Use only the selected `<state_root>` for this invocation. Do not hardcode absolute paths. Never treat the literal string `<state_root>` as a filesystem path. Skill resources stay under `references/`.

## When to Use

- User follows shows, asks what is new, or wants an episode briefing without listening
- Limited time → prioritize queue, essential timestamps, skip vs listen
- Learning mode: extract frameworks, citations, and applied insights across episodes
- Guest or topic alerts across subscriptions and unsubscribed shows
- YouTube podcast channels, clips, chapter markers, and cross-platform guest tours
- Not for music taste CRM (`music`), composing (`song`), generative audio prompts (`music-generation`), or file-level audio tooling (`audio`)

## Quick Reference

| Topic | File | Load when |
|-------|------|-----------|
| Episode briefings & digests | `references/briefings.md` | Summaries, time-boxed listening, weekly digests |
| Discovery & backlog | `references/discovery.md` | New shows, VIP guests, topic alerts, catch-up plans |
| Learning extraction | `references/learning.md` | Notes by topic, spaced resurfacing, applied insights |
| YouTube video podcasts | `references/youtube.md` | Channels, clips, chapters, title/thumbnail parsing |
| Domain sources | `references/sources.md` | Verify claims against primary podcast/RSS/transcript docs |

## Core Behavior

- User names a show → add to `<state_root>/subscriptions.md` and watch for new episodes
- "What's new?" → summarize recent subscribed episodes; offer briefings before full listens
- Briefing request → load `references/briefings.md`; produce TL;DR, key points, quotes, actions, skip/listen
- Time constraint → compare duration vs available time; propose essential segments with timestamps
- Guest watch → scan appearances beyond subscriptions; recommend the single best episode when tours repeat
- Finished episode → mark progress in queue/knowledge files under `<state_root>/`
- Backlog overwhelm → load `references/discovery.md`; build a bankruptcy/catch-up plan

## File Structure

```text
<state_root>/
├── subscriptions.md    # Shows followed
├── queue.md            # Episodes to listen / in progress
├── briefings/          # Generated summaries by show
├── knowledge.md        # Extracted insights (learning mode)
└── guests.md           # VIP guest watchlist
```

Initialize missing directories or starter files inside the selected `<state_root>` only when the user needs persistence.

## Quick Commands

| User says | Agent does |
|-----------|------------|
| "I follow Lex Fridman" | Add to `<state_root>/subscriptions.md` |
| "Summarize latest Huberman" | Load `references/briefings.md`; write briefing under `briefings/` |
| "What should I listen to?" | Prioritize `queue.md` by available time |
| "Did Naval appear anywhere?" | Check guest watchlist + recent appearances |
| "I finished episode X" | Mark complete; update progress / knowledge |
| "Too many episodes" | Catch-up plan with skips and essential segments |
| "Follow JRE clips" | Load `references/youtube.md`; track clips channel |

## Operating Rules

1. **Disclose transcript quality** — official transcripts first; label auto-captions/Whisper as error-prone.
2. **Portable state only** — all durable data under resolved `<state_root>`; never `~/Clawic/...` or clawic.com paths.
3. **Progressive disclosure** — keep this entry thin; load one reference file per task.
4. **One best appearance** — on guest tours, prefer the deepest unique angle over every rehash.
5. **No invented episodes** — if feed/title/date is unknown, say so and ask one clarifying question.
6. **Privacy** — treat listening history and notes as private local state.

## Failure Modes

| Failure | Recovery |
|---------|----------|
| Multiple `<state_root>` candidates | Keep highest precedence; report conflict; do not merge |
| Missing show identity | Ask once for show name / feed / platform before writing state |
| No transcript available | Brief from title/description/chapters only; mark confidence low |
| Conflicting expert advice | Record both sides under learning notes; do not force a false consensus |
| YouTube clickbait title | Parse guest/topic from description or trusted metadata before alerting |

## Out of Scope

- Clinical advice derived from health podcasts (summarize claims; do not prescribe)
- Paying for or bypassing paid podcast paywalls
- Mass-downloading copyrighted audio without user-owned access
