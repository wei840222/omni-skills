# Local transcription helpers

This skill covers **audio prep** and **light local Whisper** runs. When transcription,
diarization, provider choice, or transcript libraries are the primary product, prefer
`speech-to-text-transcription`.

## Tool map

| Tool | Role | Gate |
|------|------|------|
| FFmpeg | Extract/convert/clean before STT | Required |
| OpenAI Whisper (local) | Offline transcription + basic subtitles | Optional `whisper` CLI |
| Whisper.cpp | Lower-memory local port | Optional external binary |
| WhisperX / pyannote | Local diarization stacks | Optional; often need HF tokens |
| AssemblyAI / Deepgram / cloud STT | Hosted APIs | **Only with explicit user consent** |

## Install Whisper (optional)

```bash
pip install -U openai-whisper
# If build issues: install rust/setuptools-rust per upstream README
```

Upstream documents models (sizes approximate):

| Model | Parameters | Relative speed | VRAM ballpark |
|-------|------------|----------------|---------------|
| tiny | 39 M | fastest | ~1 GB |
| base | 74 M | fast | ~1 GB |
| small | 244 M | medium | ~2 GB |
| medium | 769 M | slower | ~5 GB |
| large | 1550 M | slowest | ~10 GB |
| turbo | optimized large-v3 class | faster large | ~6 GB class |

English-only `.en` variants can help tiny/base on English speech. **`turbo` is strong for
English transcription but is not trained for translation** — use multilingual
`medium`/`large` for translate-to-English tasks (upstream README).

Default recommendation for this skill: **`medium`** when quality matters and RAM allows;
**`base`/`small`** for quick drafts; **`turbo`** when installed and English-only speed matters.

## Prepare audio

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le whisper_ready.wav
# Optional light cleanup first
ffmpeg -i input.mp3 -af "highpass=f=80,lowpass=f=8000" -ar 16000 -ac 1 cleaned.wav
```

## Basic Whisper commands

```bash
whisper audio.mp3 --model medium
whisper audio.mp3 --model medium --language en
whisper audio.mp3 --model medium --output_format srt
whisper audio.mp3 --model medium --output_format all
whisper japanese.wav --model medium --language Japanese --task translate
whisper audio.mp3 --model medium --initial_prompt "Hosts Alice and Bob discuss MLOps"
```

Outputs may include `.txt`, `.srt`, `.vtt`, `.json`, `.tsv` depending on flags.

## Subtitle formats (shape)

**SRT**

```text
1
00:00:01,000 --> 00:00:04,500
First line.
```

**VTT**

```text
WEBVTT

00:00:01.000 --> 00:00:04.500
First line.
```

Convert:

```bash
ffmpeg -i subtitles.srt subtitles.vtt
ffmpeg -i subtitles.vtt subtitles.srt
```

## Diarization

Vanilla Whisper does not label speakers. Options:

1. Hand off to `speech-to-text-transcription` for provider/local diarization workflows
2. WhisperX / pyannote stacks when the user accepts those installs and token requirements
3. Explicit cloud APIs only after the user opts in

## Burn-in (when user wants burned captions on a video)

```bash
ffmpeg -i video.mp4 -vf "subtitles=captions.srt" output.mp4
```

For caption-centric styling products, prefer `video-captions`.

## Quality tips

1. Clean and normalize quiet speech before STT
2. Pass `--language` when known
3. Use larger models for noisy/overlapping speech
4. Supply `--initial_prompt` for names/jargon
5. Split multi-hour files before STT (see speech-to-text skill for long-form policy)

## Common issues

| Issue | Likely cause | Fix |
|-------|--------------|-----|
| Wrong language | Auto-detect miss | `--language` |
| Loopy hallucinations | Silence/noise | Trim silence, denoise, larger model |
| Missing words | Too quiet | Loudnorm / level speech first |
| No speakers labeled | Expected | Diarization tool or other skill |
| Translate ignored on turbo | Model limit | Multilingual medium/large |
