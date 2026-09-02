---
name: video-downloader
description: Download online videos with quality and format controls using yt-dlp for reliable local saves.
metadata:
  openclaw: '{"emoji":"⬇️","requires":{"bins":["yt-dlp","python3"],"install":[{"id":"brew","kind":"brew","formula":"yt-dlp","bins":["yt-dlp"],"label":"Install yt-dlp (Homebrew)"}]},"os":["linux","darwin"]}'
  related-skills: '{"video":"General video processing workflows beyond one-off downloads.","ffmpeg":"Codec conversion and remux tasks after a download.","audio":"Audio cleanup workflows when the user needs post-processing beyond MP3 extraction.","youtube-video-transcript":"Transcript extraction when the user needs text rather than a media file."}'
---

# Video Downloader

Download single videos from user-provided URLs with predictable quality, format, and output paths.

## Setup

On first use, read `references/setup.md` for integration guidelines.

## When to Use

Use this skill when the user asks to download a video or extract audio from a video URL.
It is optimized for one-off downloads with explicit quality and format requirements.

## State location
Memory lives in `<state_root>/`. See `references/memory-template.md` for structure.

```text
<state_root>/
├── memory.md             # Status + user preferences
├── downloads-log.md      # Optional history of completed downloads
└── failed-downloads.md   # Optional retries and failure reasons
```

## Quick Reference

Load only what you need to keep context small during execution.

| Topic | File | When to load |
|-------|------|--------------|
| Setup flow | `references/setup.md` | When `<state_root>/memory.md` is missing or empty |
| Memory template | `references/memory-template.md` | When creating or updating the memory state file |
| Command recipes | `references/commands.md` | When you need explicit `yt-dlp` download settings |
| Core rules | `references/core-rules.md` | When initiating a new download request |
| Common traps | `references/common-traps.md` | When a download fails or behaves unexpectedly |
| Security | `references/security.md` | When handling user privacy concerns or permissions |
| Domain knowledge | `references/domain-knowledge.md` | When you need context on formats or rate limits |
| Download script | `download_video.py` | To execute the download |

## External Endpoints

The downloader only contacts domains implied by the user-provided URL.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| User-provided video host URL domains (via `yt-dlp`) | Requested media URL and standard downloader headers | Fetch metadata and media streams |

No other data is sent externally.

## Trust

By using this skill, requests are sent to the video host domains behind the provided URL.
Only install if you trust those services with your request metadata.
