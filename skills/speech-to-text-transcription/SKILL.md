---
name: speech-to-text-transcription
description: Transcribe local audio, video, and downloaded recordings into text, speaker-labeled segments, or subtitle files. Use when a user asks to transcribe a voice memo, meeting, interview, podcast, lecture, or video.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎤","requires":{"bins":["ffmpeg"]}}'
  related-skills: '{"audio":"General audio processing.","ffmpeg":"Video and audio conversion.","podcast":"Podcast creation and editing."}'
---


## State location

Transcription state may exist in `<workspace>/speech-to-text-transcription/`, `<workspace>/memory/speech-to-text-transcription/`, or `~/speech-to-text-transcription/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/speech-to-text-transcription/`, `<workspace>/memory/speech-to-text-transcription/`, `~/speech-to-text-transcription/`.
3. If none exists and state must be created, default to `<workspace>/speech-to-text-transcription/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, read `references/setup.md` only to learn the user’s workflow and explicit preferences. Keep the first transcription focused on the requested file; save a preference only when the user expresses it or asks to retain it.

## When to Use

Use this skill for local files, downloaded URLs, voice memos, podcasts, interviews, meetings, lectures, and videos that need transcription, timestamps, subtitles, or speaker labels.

## Workflow

1. Confirm the input is accessible and identify its format, duration, size, language, and whether speaker labels or subtitles are required.
2. Choose local Whisper for private/offline work; select a cloud provider only after the user explicitly chooses the data transfer.
3. For files over 25 MB or recordings longer than two hours, split the input first; preserve order and merge the resulting transcript segments with timestamps.
4. Run the transcription, verify the output is complete and readable, then offer the requested format and any summary or action-item extraction.

If the input cannot be read or its format is unsupported, use `ffmpeg` to extract or convert the audio, then repeat step 1. If a cloud request fails, report the provider error without exposing credentials and offer local Whisper or a retry after the user decides.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure. Read `references/provider-guidance.md` before selecting or updating a cloud-provider command.

```
<state_root>/
├── memory.md        # Provider preferences, defaults
├── transcripts/     # Saved transcriptions
└── temp/            # Processing workspace
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| Provider-specific commands and limits | `references/provider-guidance.md` |

## Core Rules

### 1. Detect File Type First
Before transcription, identify the input:
- Local file path → verify exists, check format
- URL → download to temp, then process
- Meeting recording → likely needs speaker diarization
- Voice memo → usually single speaker, shorter

### 2. Choose Provider Based on Context
| Scenario | Best Provider | Why |
|----------|---------------|-----|
| Quick local transcription | Whisper (local) | No API key, free, private |
| Current OpenAI transcription | OpenAI Audio API | Use the documented `gpt-transcribe` request |
| Speaker identification | OpenAI diarization or AssemblyAI | Use a provider that returns speaker labels |
| Real-time/streaming | Deepgram | Low latency |
| Long content (>2 hours) | Split + batch | Avoid timeouts |

### 3. Handle Long Audio
For files over 25 MB or recordings longer than two hours:
1. Split the audio into ordered chunks with ffmpeg.
2. Process each chunk using the chosen provider or local Whisper.
3. Merge transcript segments in order while preserving timestamps.
4. Check the joined result for gaps or duplicated boundary text before delivery.

### 4. Preserve Context
After transcription:
- Ask if user wants the transcript saved
- Suggest filename based on content
- Offer to extract action items or summary

### 5. Output Formats
Default to plain text. Offer alternatives:
- `.txt` — clean text, no timestamps
- `.srt` / `.vtt` — subtitles with timing
- `.json` — structured with word-level timing
- `.md` — formatted with speaker labels

## Common Traps

- **Match the provider to the requested output** → use a diarization-capable provider for speaker labels and local Whisper for offline/private transcription.
- **Prepare large files first** → split recordings over 25 MB or two hours before sending chunks for transcription.
- **Improve noisy audio before transcription** → apply appropriate ffmpeg preprocessing when noise affects intelligibility.
- **Confirm language expectations** → provide a language hint for mixed-language or uncertain recordings when the chosen provider supports it.
- **Preserve speaker context** → request diarization whenever speaker attribution is required.

## Requirements

**Required:** ffmpeg (for audio processing)

**Optional API keys (only if using cloud providers):**
- `OPENAI_API_KEY` — for OpenAI Whisper API
- `ASSEMBLYAI_API_KEY` — for AssemblyAI (speaker diarization)
- `DEEPGRAM_API_KEY` — for Deepgram (real-time)

Local Whisper works without any API keys.

## Provider Quick Reference

### Local Whisper (No API Key)
```bash
# Install
pip install openai-whisper

# Basic transcription
whisper audio.mp3 --model base --output_format txt

# With timestamps
whisper audio.mp3 --model medium --output_format srt
```

Models: `tiny` (fast) → `base` → `small` → `medium` → `large` (accurate)

### OpenAI Whisper API
```bash
curl -X POST https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@audio.mp3" \
  -F model="gpt-transcribe"
```

### AssemblyAI (Speaker Diarization)
```bash
# Upload
curl -X POST https://api.assemblyai.com/v2/upload \
  -H "Authorization: $ASSEMBLYAI_API_KEY" \
  --data-binary @audio.mp3

# Transcribe with speakers
curl -X POST https://api.assemblyai.com/v2/transcript \
  -H "Authorization: $ASSEMBLYAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"audio_url": "URL", "speaker_labels": true}'
```

## Audio Preprocessing

### Extract Audio from Video
```bash
ffmpeg -i video.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 audio.wav
```

### Reduce Noise
```bash
ffmpeg -i noisy.wav -af "afftdn=nf=-25" clean.wav
```

### Split Long Audio
```bash
# Split into 10-minute chunks
ffmpeg -i long.mp3 -f segment -segment_time 600 -c copy chunk_%03d.mp3
```

## Security & Privacy

**Data that stays local:**
- Transcripts in <state_root>/transcripts/
- Local Whisper processes entirely on-device

**Data that leaves your machine (if using APIs):**
- Audio file sent to chosen provider (OpenAI, AssemblyAI, Deepgram)
- Transcript returned and stored locally

**Credential and upload handling:**
- Read cloud-provider API keys only from environment variables or an approved secret store.
- Obtain explicit user confirmation before sending any audio to a cloud provider.
- Explain that a provider may retain uploaded data under its own policy; consult its current documentation when retention requirements matter.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| api.openai.com/v1/audio | Audio file | Whisper API transcription |
| api.assemblyai.com/v2 | Audio file | AssemblyAI transcription |
| api.deepgram.com/v1 | Audio stream | Deepgram transcription |

Only called when user explicitly chooses cloud provider. Local Whisper sends nothing.

## Trust

By using cloud transcription providers, audio data is sent to OpenAI, AssemblyAI, or Deepgram. Only install if you trust these services with your audio. For sensitive content, use local Whisper.
