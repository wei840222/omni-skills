---
name: video-captions
description: "Generate video captions and subtitles via multi-engine transcription with word-level timing, styling presets, and burn-in capabilities."
metadata:
  openclaw: '{"emoji": "\ud83c\udfac", "requires": {"bins": ["ffmpeg", "whisper"], "env": {"optional": ["ASSEMBLYAI_API_KEY", "DEEPGRAM_API_KEY"]}}, "os": ["linux", "darwin"], "displayName": "Video Captions"}'
  related-skills: '["skills/ffmpeg", "skills/video", "skills/video-edit", "skills/audio"]'
---

## When to Use

Trigger this skill when the user explicitly requests captions, subtitles, or text burn-in for video content. Only trigger when captions are explicitly requested (route general video editing tasks to other skills).

## State location

This skill is completely stateless. It does not store local configuration or persistent state across executions.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Transcription engines | `references/engines.md` | When deciding which transcription tool to use. |
| Output formats | `references/formats.md` | When selecting the correct format for a platform. |
| Styling presets | `references/styling.md` | When generating styled subtitles (ASS/burn-in). |
| Platform requirements | `references/platforms.md` | When targeting a specific platform (YouTube, Netflix, etc.). |
| Core Rules | `references/rules.md` | When creating captions to ensure professional standards. |
| Workflow | `references/workflow.md` | When executing specific commands for transcription or burn-in. |
| Caption Traps | `references/traps.md` | When debugging or avoiding common issues. |
| Common Scenarios | `references/scenarios.md` | When handling end-to-end workflows for specific platforms. |
| External Endpoints | `references/endpoints.md` | When configuring or using cloud APIs. |
| Security & Privacy | `references/security.md` | When evaluating data privacy or API usage. |
| Industry Standards | `references/research.md` | When reviewing styling and timing constraints. |
