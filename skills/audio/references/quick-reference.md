# Quick reference

Load this file to map a short user request to a default action. For full command
blocks, continue to `references/commands.md`. For LUFS tables, use
`references/loudness.md`.

## Common requests → actions

| User says | Agent does |
|-----------|------------|
| Convert to MP3 | `libmp3lame` VBR `-q:a 2` (~190 kbps) or CBR `-b:a 192k` |
| Convert to M4A/AAC | `aac` / `libfdk_aac` if available, often `-b:a 192k` |
| Extract audio from video | `-vn` then copy or re-encode |
| Remove background rumble/hiss | `highpass=f=80`, optional `lowpass=f=8000`, then `afftdn` if needed |
| Normalize for podcast | Two-pass `loudnorm` toward **I=-16:TP=-1.5:LRA=11** (or measure first) |
| Normalize for Spotify music | Target about **-14 LUFS**, true peak **≤ -1 dBTP** (≤ -2 dBTP if hotter than -14) |
| Transcribe this | Prep 16 kHz mono WAV → local `whisper`; deep STT → `speech-to-text-transcription` |
| Separate vocals/instruments | `demucs` default `htdemucs` (optional install) |
| Make it smaller | Lower bitrate (`-b:a 128k` / `96k`) or Opus |
| Speed up 1.5× without pitch shift | `atempo=1.5` (chain for factors outside 0.5–2.0) |
| Trim / cut | Prefer stream copy when codec allows; re-encode when filters needed |
| Merge clips | `concat` demuxer with a `list.txt` of `file '…'` lines |

## Format quick reference

| Format | Use case | Notes |
|--------|----------|-------|
| WAV / AIFF | Edit master | Uncompressed PCM |
| FLAC | Archive | Lossless compressed |
| MP3 | Universal share / many RSS hosts | Lossy; wide player support |
| AAC in M4A/MP4 | Apple ecosystem, efficient lossy | Apple Podcasts RSS prefers AAC when practical |
| Opus (Ogg/WebM) | Efficient speech/music online | Excellent low-bitrate efficiency |
| M4R | iPhone ringtone container | AAC payload, short duration |

## Quality defaults

| Context | Default |
|---------|---------|
| Podcast loudness | **-16 LUFS** integrated, true peak **≈ -1.5 dBTP**, LRA often ~7–11 |
| Music streaming master (Spotify-oriented) | **≈ -14 LUFS**, true peak **≤ -1 dBTP** |
| Broadcast (Europe) | **EBU R128 −23 LUFS** when user names broadcast |
| MP3 encode | VBR `-q:a 2` or CBR `192k` speech/music share; `128k` when size-bound |
| Sample rate | **44.1 kHz** music/podcast share; **48 kHz** when matching video; **16 kHz mono** Whisper prep |
| Voice cleanup starter | `highpass=f=80` before heavier denoise |

## Decision hints

1. If the user names a platform, load `references/loudness.md` and match that row.
2. If both music and speech exist, ask which loudness intent wins before mastering.
3. If the file is video and the user only needs sound, extract audio early to save CPU.
4. If transcription quality is poor, clean and normalize speech *before* Whisper.
5. Prefer measuring loudness (`loudnorm=print_format=json` or `summary`) before one-shot guess encodes on finals.
