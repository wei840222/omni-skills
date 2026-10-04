---
name: audio
description: >
  Process local audio and video soundtracks with FFmpeg: inspect streams, convert
  formats, trim/merge, clean noise, normalize loudness, extract stems, prepare
  podcast masters, and hand off local transcription. Use when the user provides a
  local media path and asks to convert, enhance, normalize, denoise, extract audio,
  separate stems, export for a platform, or run a podcast post-production pass.
  Not for curating listening history (music), full show planning/marketing (podcast),
  deep caption/diarization products (speech-to-text-transcription / video-captions),
  YouTube host-subtitle fetch (youtube-video-transcript), or raw codec deep-dives
  without a user media file (ffmpeg).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔊","requires":{"bins":["ffmpeg","ffprobe"]}}'
  related-skills: '{"ffmpeg":"Lower-level codec, filter, and encoding details when the task is pure FFmpeg craft rather than an end-to-end audio deliverable.","music":"Personal listening memory, playlists, and concert logs rather than file processing.","podcast":"Show concept, scripting, publishing, and promotion around episodes this skill masters.","speech-to-text-transcription":"Dedicated transcription, diarization, and subtitle products when speech-to-text is the primary goal.","video":"Full video packaging, reframing, and platform video delivery beyond soundtrack work.","video-captions":"Caption styling and burn-in when captions are the main request.","youtube-video-transcript":"Fetch existing YouTube subtitles instead of processing a local file."}'
---

# Audio

Transform **user-provided local audio/video files** with local tools. Prefer `ffmpeg` /
`ffprobe` for inspect → process → verify. Optional tools unlock advanced steps only when
installed: Whisper (transcription), Demucs (stem separation), SoX / `ffmpeg-normalize`
(extra cleanup or two-pass loudness helpers).

This skill is **stateless**. Keep user media and outputs outside `skills/audio/`; write
results next to the source or to a path the user names. Skip inventing a persistent
config tree.

## When to use

- Convert, trim, merge, resample, or re-encode audio
- Extract audio from video; adjust channels, volume, tempo, fades
- Denoise voice, remove silence, compress/EQ lightly for speech
- Loudness-normalize for podcasts, streaming, or broadcast targets
- Podcast post-production chain (cleanup → loudness → export → tags)
- Stem separation (vocals/drums/bass/other) when Demucs is available
- Prepare audio for local Whisper / hand off heavy STT work

Hand off when the job is really:

- listening history / playlists → `music`
- show strategy, scripts, distribution calendar → `podcast`
- meeting/interview STT as the product → `speech-to-text-transcription`
- caption burn-in / styling as the product → `video-captions`
- YouTube page transcripts → `youtube-video-transcript`
- full video delivery package → `video`
- FFmpeg flag encyclopedia without a concrete media goal → `ffmpeg`

## Requirements

**Required**

- `ffmpeg` and `ffprobe`

**Optional (feature-gated)**

- `whisper` (`pip install openai-whisper`) — local transcription
- `demucs` (`pip install -U demucs`) — stem separation
- `ffmpeg-normalize` — convenient two-pass loudness CLI
- `sox` — extra restoration filters when FFmpeg is insufficient

If an optional binary is missing, complete the FFmpeg path that still works, then state
what the missing tool would add and how to install it. Use cloud STT/APIs only after the
user explicitly chooses that path.

## Quick workflow

1. **Confirm input** — Resolve the user path; ask for a valid path when the file is missing.
2. **Analyze** — `ffprobe` codec, sample rate, channels, duration, bitrate.
3. **Clarify goal** — Target format, platform loudness, speech vs music, output path.
4. **Load references** — Open only the rows needed in the table below.
5. **Process** — Prefer non-destructive copies of masters; chain filters deliberately.
6. **Verify** — Output exists; re-probe streams; for loudness jobs print integrated LUFS /
   true peak; spot-check playback when practical.
7. **Deliver** — Return output path(s), commands run, and any limits (missing optional tools).

## Progressive disclosure

| Resource | Load when |
|---|---|
| `references/quick-reference.md` | Map a short user ask to the default action, format, or quality preset |
| `references/commands.md` | Need concrete FFmpeg/Demucs/SoX command patterns |
| `references/loudness.md` | Platform LUFS/TP targets, measurement, two-pass `loudnorm` |
| `references/podcast.md` | End-to-end podcast post-production and export checklist |
| `references/transcription.md` | Local Whisper prep, models, subtitles, diarization handoff |
| `references/sources.md` | Primary URLs behind loudness, Apple delivery, Whisper, Demucs, FFmpeg claims |

## Core rules

1. **Local first** — Run processing on the user’s machine with local binaries unless they
   explicitly request a cloud API.
2. **Inspect before mutate** — Always `ffprobe` (or equivalent) before re-encoding.
3. **Preserve a master** — Keep the original; write a new output path by default.
4. **Match the job to loudness intent** — Music streaming masters often target about
   **-14 LUFS** with true peak **≤ -1 dBTP** (Spotify artist guidance). Podcasts commonly
   ship near **-16 LUFS** integrated with true peak **≤ -1.0 to -1.5 dBTP** as a
   cross-platform compromise. Broadcast follows **EBU R128 (-23 LUFS)** or regional
   LKFS rules when the user names broadcast delivery. Measure against rows listed in
   `references/loudness.md` rather than guessed platform numbers.
5. **Prefer integrated loudness over peak-only gains** — Use `loudnorm` (ideally two-pass)
   or `ffmpeg-normalize`; peak maximize alone is not a substitute for LUFS targets.
6. **Speech cleanup is light-touch** — Start with highpass ~80 Hz and gentle denoise; heavy
   gates destroy consonants.
7. **Optional tools are gates, not assumptions** — Detect `whisper` / `demucs` before
   promising stems or transcripts.
8. **Transcription depth** — Simple local transcript/subtitles can stay here; speaker-heavy
   or productized STT belongs in `speech-to-text-transcription`.
9. **No promotional residue** — Keep outputs free of skill-catalog marketing links.

## Output contract

Unless the user asks otherwise, return:

1. **Output path(s)** created
2. **Key probes** — before/after codec, rate, channels, duration; loudness summary when relevant
3. **Commands** actually run (copy-pasteable)
4. **Limits** — missing optional tools, unverified playback, or platform rules that still need a human check

## Failure modes

| Symptom | Response |
|---|---|
| Path missing or unreadable | Ask for a valid local path before processing |
| `ffmpeg`/`ffprobe` missing | Report the install need and pause processing |
| Optional tool missing mid-flow | Finish FFmpeg-capable steps; document the gap |
| Loudness target unnamed | Default podcast-safe **-16 LUFS / TP -1.5**; music-only asks default **Spotify -14 / TP -1** and say so |
| User wants cloud STT | Confirm consent first; prefer `speech-to-text-transcription` for provider workflows |
| Request is show branding/SEO only | Hand off to `podcast` |
| Request is YouTube page captions | Hand off to `youtube-video-transcript` |
| Filter errors / empty output | Keep the original; report stderr; retry with a simpler filter chain |
