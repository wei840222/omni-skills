# Sources — YouTube Video Transcript

Domain facts used in this skill. Re-check version-sensitive rows before asserting new defaults.

## yt-dlp (extractor CLI)

- **Project / install / usage** — canonical CLI for local metadata and subtitle download without third-party transcript proxies.  
  https://github.com/yt-dlp/yt-dlp
- **Subtitle options** (same README destination anchors as published by the project): `--list-subs`, `--write-subs`, `--write-auto-subs`, `--sub-langs`, `--sub-format`, `--convert-subs`, `--skip-download`.  
  https://github.com/yt-dlp/yt-dlp#subtitle-options
- **Local verification (this refactor host, 2026-10-02):** `yt-dlp 2026.08.19` exposes `--write-subs` / `--write-auto-subs` (not the legacy singular `--write-sub` as the primary flag), plus `--cookies`, `--cookies-from-browser`, `--sleep-interval`, `--max-sleep-interval`, `--write-info-json`.

## YouTube captions product behavior

- **Add subtitles & captions** — creators can upload captions or use auto-captions; availability varies by video and language.  
  https://support.google.com/youtube/answer/2734796
- **YouTube Data API Captions resource** — captions are a first-class YouTube concept (list/insert/download via API with OAuth). This skill prefers the local `yt-dlp` path and does not require API keys for the default flow.  
  https://developers.google.com/youtube/v3/docs/captions

## Operational implications captured in skill rules

| Claim | Class | Handling |
|-------|-------|----------|
| Manual captions usually outrank ASR quality | stable-domain | Prefer `--write-subs` before `--write-auto-subs` |
| Auto captions often lack reliable punctuation/casing | stable-domain | Label auto tracks; allow user verification via timestamps |
| Not every video has captions | platform-specific | Explicit empty-track failure path |
| Some videos need cookies for age/region gates | platform-specific | User-provided cookies only; no proxy service |
| Batch extraction should pace requests | version/ops | `--sleep-interval` / `--max-sleep-interval` |
| Deep links use second offsets | stable-domain | `&t=SECONDS` / `start=SECONDS` |

## Out of scope sources

- Third-party paid transcript SaaS and anonymous subtitle proxy sites — intentionally excluded for privacy and integrity.
- Whisper/FFmpeg local re-transcription of downloaded audio — belongs to `video-captions` / `ffmpeg` when host captions are missing and the user opts into media download + ASR.
