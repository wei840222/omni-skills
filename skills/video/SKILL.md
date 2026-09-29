---
name: video
description: Process, edit, convert, compress, and optimize videos for platforms with
  ffmpeg. Use when the user needs format conversion, compression, trimming, reframing,
  captions burn-in, GIF export, or platform-specific video delivery.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🎬","requires":{"bins":["ffmpeg","ffprobe"]}}'
  related-skills: '{"ffmpeg":"Lower-level codec, filter, and encoding details when a task needs precise FFmpeg flags beyond this skill.","video-captions":"Dedicated caption transcription, styling, and burn-in when captions are the primary request.","video-edit":"AI enhancement workflows (background removal, color grade, upscale, stabilize) beyond basic FFmpeg transforms.","video-downloader":"Download source media from URLs before local processing."}'
---

## When to load

Load this skill when the user asks to process an existing video file for platform delivery or basic editing with FFmpeg. Prefer `video-captions` for caption-only work, `video-edit` for AI enhancement, and `ffmpeg` when the user needs raw codec/filter expertise without platform packaging.

## Requirements

**Required:**
- `ffmpeg` / `ffprobe` — core video processing

**Optional:**
- `whisper` — local transcription for captions
- `realesrgan` — AI upscaling

## Critical rules

- Clarify target platform, format, duration, and size limit before encoding.
- Inspect the source with `ffprobe` (codec, resolution, duration, audio) before transforming.
- Prefer AAC audio and `-movflags +faststart` for web playback.
- Use H.264 CRF 23 as the default quality; raise CRF (28–32) only when size limits require it.
- Verify duration, file size, and playability before delivery.
- Process only files the user explicitly provides; do not upload to external services unless asked.

## State location

This skill is stateless. Working media and outputs stay in the user workspace; the package does not own a mutable `<state_root>`.

## Progressive disclosure

Load topic files under `references/` only when needed:

- Read `references/platforms.md` for YouTube, TikTok, Instagram, WhatsApp, and other delivery limits.
- Read `references/commands.md` for FFmpeg recipes (trim, convert, crop, merge, GIF, subtitles).
- Read `references/quality.md` for CRF/preset/audio bitrate guidance and common failure fixes.
- Read `references/workflows.md` for multi-step creator, social, educator, and marketer pipelines.

## Execution pattern

1. **Clarify target** — platform, format, size/duration limit
2. **Check source** — `ffprobe` for codec, resolution, duration, audio
3. **Process** — FFmpeg transform for the requested outcome
4. **Verify** — confirm output meets specs
5. **Deliver** — return the file to the user

## Scope

This skill:
- Processes video files the user explicitly provides
- Runs FFmpeg commands on user request
- Does NOT access files without user instruction
- Does NOT upload to external services automatically
