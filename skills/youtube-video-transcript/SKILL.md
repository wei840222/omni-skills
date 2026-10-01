---
name: youtube-video-transcript
description: >
  Fetch and format YouTube video transcripts with precise timestamp navigation,
  chapter detection, quote extraction, and local cache-with-consent. Use when
  the user shares a YouTube URL and asks to read, summarize, search, quote, or
  export that video's spoken content. Not for generating/burning captions onto
  a local media file (`video-captions`), general FFmpeg media processing
  (`ffmpeg`), or summarizing text the user already has (`summarizer`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📺","requires":{"bins":["yt-dlp"]},"install":[{"id":"brew","kind":"brew","formula":"yt-dlp","bins":["yt-dlp"],"label":"Install yt-dlp (Homebrew)"},{"id":"pip","kind":"pip","package":"yt-dlp","bins":["yt-dlp"],"label":"Install yt-dlp (pip)"}]}'
  related-skills: '{"summarizer":"Compress an already-extracted transcript or other text source once you have plain text.","video-captions":"Generate or burn captions for a local video file rather than fetch YouTube host subtitles.","ffmpeg":"Lower-level media convert/trim/extract when the request is not YouTube transcript work.","video":"General video tasks outside YouTube subtitle extraction.","extract-pdf-text":"Extract text from PDFs/scans before summarization; different source type."}'
---

# YouTube Video Transcript

Extract YouTube subtitles locally with `yt-dlp`, keep timestamps for navigation, prefer human-uploaded tracks over auto-generated ones, and only cache under a portable `<state_root>` after the user consents.

## State location

Resolve `<state_root>` before any preference or cache read/write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory:
   `<workspace>/youtube-video-transcript/`,
   `<workspace>/memory/youtube-video-transcript/`,
   `~/youtube-video-transcript/`.
3. If none exist and the user asked to persist data, create
   `<workspace>/youtube-video-transcript/`.

| Path | Required? | Role |
|------|-----------|------|
| `<state_root>/memory.md` | optional | Format/summary preferences and recent video index |
| `<state_root>/videos/{video_id}.md` | optional | Cached transcript per video (consent required) |
| `<state_root>/exports/` | optional | User-requested export files |
| `<state_root>/research/{topic}/` | optional | Multi-video research folders the user asked to keep |

Do not treat the literal string `<state_root>` as a filesystem path. Skill resources stay under `references/` and `assets/`. Never store cookies, credentials, or browser profiles inside `<state_root>`.

Template: `assets/memory-template.md`.

## When to load

Trigger on YouTube-URL + transcript intent. Load this skill when the user:

- shares a YouTube watch/youtu.be/shorts URL and wants the spoken content as text
- asks what someone said about a topic and needs timestamps or deep links
- wants quotes with context for research or content reuse
- wants chapter-oriented reading, SRT/VTT/Markdown export, or a consented local cache

Route away when the ask is mainly:

- caption generation or burn-in for a local file → `video-captions`
- codec/trim/scale/audio extract without YouTube subtitles → `ffmpeg` / `video`
- summarizing text already on hand → `summarizer`

## Quick reference

| Need | Load |
|------|------|
| Install check, first-run order, consent prompts | `references/setup.md` |
| Metadata → list-subs → extract → format pipeline | `references/workflow.md` |
| Search, chapters, exports, batch, recovery | `references/patterns.md` |
| yt-dlp flags, YouTube caption facts, sources | `references/sources.md` |
| Preference / cache file shapes | `assets/memory-template.md` |

## Core rules

1. **Metadata before extraction.** Run `yt-dlp -j "URL"` first for title, duration, chapters, and id. Do not extract blind.
2. **List tracks, then choose.** Run `yt-dlp --list-subs "URL"`. Prefer human-uploaded (`--write-subs`) over auto (`--write-auto-subs`). Report which language and whether the track was manual or automatic.
3. **Timestamps stay attached.** Keep `[HH:MM:SS]` or `[MM:SS]` on every segment through display, search, quote, and export (except an explicit plain-text strip request).
4. **Cache only with consent.** After the first useful extraction, ask once. Yes → write under `<state_root>/videos/`. No → show once and do not cache. Always name the path written.
5. **Quality transparency.** Manual → "official/uploaded subtitles". Auto → "auto-generated (may have errors)". None → say so and stop; do not invent dialogue.
6. **Local only.** No third-party transcript proxies. Optional `--cookies` / `--cookies-from-browser` only when the user supplies their own file or browser profile for age/region locks; never request passwords.
7. **Deep links for hits.** When returning search/quote hits, include `https://youtube.com/watch?v=ID&t=SECONDS` (integer seconds).

## Default pipeline

```bash
yt-dlp -j "VIDEO_URL"                 # metadata + chapters
yt-dlp --list-subs "VIDEO_URL"        # available tracks
# prefer manual, then auto; skip media download
yt-dlp --skip-download --write-subs --sub-langs LANG --sub-format vtt/best "VIDEO_URL"
# fallback:
yt-dlp --skip-download --write-auto-subs --sub-langs LANG --sub-format vtt/best "VIDEO_URL"
```

Convert VTT/SRV to Markdown segments with timestamps, optionally group by official chapters (`jq '.chapters'` on the `-j` JSON), then answer the user request (full read, summary, search, quote, export).

## Security and privacy

- Keep transcripts and preferences local, and write them only after consent.
- Leave cookies, `cookies.txt`, and auth headers out of the skill tree and git; accept only user-supplied cookie inputs at runtime.
- On geo/age restrictions, report the blocker and continue only with user-supplied `--cookies` / `--cookies-from-browser` when offered—no proxy path.
- Before any cache write, redact live secrets if a transcript contains them and say that redaction happened.

## Common traps

| Trap | Prevention |
|------|------------|
| Extract without `-j` / `--list-subs` | Always metadata + list first |
| Treat auto as manual quality | Label auto; prefer uploaded tracks |
| Strip timestamps during cleanup | Preserve through every transform |
| Cache without asking | Ask after first extraction |
| Legacy `--write-sub` flag | Current yt-dlp uses `--write-subs` / `--write-auto-subs` |
