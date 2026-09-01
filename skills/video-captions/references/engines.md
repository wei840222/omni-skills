# Transcription Engines — Video Captions

## Local Engines (No Data Leaves Machine)

### OpenAI Whisper

**Best for:** General use, offline, privacy-sensitive

```bash
# Installation
pip install openai-whisper

# Models (quality vs speed)
# tiny    → fastest, lowest quality
# base    → fast, decent quality  
# small   → balanced
# medium  → good quality
# large-v3 → best quality, slow
# turbo   → excellent quality, fast (RECOMMENDED)

whisper video.mp4 --model turbo --output_format srt
```

| Model | VRAM | Speed | Quality |
|-------|------|-------|---------|
| tiny | 1GB | 32x | Basic |
| base | 1GB | 16x | Decent |
| small | 2GB | 6x | Good |
| medium | 5GB | 2x | Very good |
| large-v3 | 10GB | 1x | Excellent |
| turbo | 6GB | 8x | Excellent |

### MLX Whisper (Apple Silicon)

**Best for:** Mac M1/M2/M3, native acceleration

```bash
# Installation
pip install mlx-whisper

# Usage (same API as whisper)
mlx_whisper video.mp4 --model mlx-community/whisper-turbo
```

### whisper-timestamped

**Best for:** Word-level timestamps, karaoke effects

```bash
# Installation
pip install whisper-timestamped

# Usage
whisper_timestamped video.mp4 --model large-v3 --output_format srt

# With VAD (Voice Activity Detection) - reduces hallucinations
whisper_timestamped video.mp4 --vad silero --accurate
```

**Advantages:**
- Word-level timestamps via DTW alignment
- Confidence scores per word
- VAD pre-processing option
- Better segment boundary detection

### stable-ts

**Best for:** Improved timestamp accuracy, refinement

```bash
# Installation
pip install stable-ts

# Usage
stable-ts video.mp4 --model turbo -o video.srt

# Refine existing SRT
stable-ts video.mp4 --refine video.srt -o video_refined.srt
```

---

## Cloud APIs (Higher Accuracy, Costs Money)

### AssemblyAI

**Best for:** managed transcription and speaker diarization after the user explicitly selects AssemblyAI and approves sending the media.

Consult the current AssemblyAI documentation before selecting its current API or SDK workflow; configure `ASSEMBLYAI_API_KEY` as a user-provided secret rather than placing it in command history.

### Deepgram

**Best for:** managed pre-recorded or real-time transcription after the user explicitly selects Deepgram and approves sending the media.

Consult the current Deepgram pre-recorded audio documentation before constructing a request; configure `DEEPGRAM_API_KEY` as a user-provided secret rather than embedding it in an example request.

---

## Engine Decision Matrix

| Priority | Recommended Engine |
|----------|-------------------|
| Privacy/Offline | Whisper local (turbo) |
| Best accuracy | AssemblyAI |
| Speed | Deepgram Nova-2 |
| Word timestamps | whisper-timestamped |
| Apple Silicon | MLX Whisper |
| Budget | Whisper local |
| Real-time | Deepgram streaming |
| Speaker ID | AssemblyAI or pyannote+Whisper |

---

## Language Support

Whisper supports 99 languages. Common codes:
- `en` English
- `es` Spanish
- `zh` Chinese (Mandarin)
- `ja` Japanese
- `ko` Korean
- `de` German
- `fr` French
- `pt` Portuguese
- `ar` Arabic
- `hi` Hindi

Auto-detection works well for single-language content. Specify `--language` for:
- Code-switching (multiple languages)
- Low-resource languages
- Accented speech
