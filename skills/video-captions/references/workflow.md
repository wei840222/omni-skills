# Workflow

### Basic Transcription
```bash
# Auto-detect language, output SRT
whisper video.mp4 --model turbo --output_format srt

# Specify language
whisper video.mp4 --model turbo --language es --output_format srt

# Multiple formats
whisper video.mp4 --model turbo --output_format all
```

### Word-Level Timestamps
```bash
# Using whisper-timestamped
whisper_timestamped video.mp4 --model large-v3 --output_format srt

# With VAD pre-processing (reduces hallucinations)
whisper_timestamped video.mp4 --vad silero:3.1 --accurate
```

### Styled Subtitles (ASS)

Before burn-in, verify that the installed FFmpeg build includes the `subtitles` filter (and therefore libass support):

```bash
ffmpeg -hide_banner -filters | grep -w subtitles
```

If this command prints no `subtitles` filter, use an FFmpeg build compiled with `--enable-libass` or deliver the SRT/ASS file without burn-in.

```bash
# Generate SRT first, then convert with style
ffmpeg -i video.mp4 -vf "subtitles=video.srt:force_style='FontName=Arial,FontSize=24,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Shadow=1,Alignment=2'" output.mp4
```

### Burn-In for Social Media

Apply the same `subtitles` filter preflight before running these commands.

```bash
# TikTok/Instagram style (centered, bold)
ffmpeg -i video.mp4 -vf "subtitles=video.srt:force_style='FontName=Montserrat-Bold,FontSize=32,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=3,Shadow=0,Alignment=10,MarginV=50'" output.mp4

# Netflix style (bottom, clean)
ffmpeg -i video.mp4 -vf "subtitles=video.srt:force_style='FontName=Netflix Sans,FontSize=48,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Shadow=1,Alignment=2'" output.mp4
```

### Translation
```bash
# Transcribe + translate to English
whisper video.mp4 --model turbo --task translate --output_format srt
```

### Format Conversion
```bash
# SRT to VTT
ffmpeg -i video.srt video.vtt

# SRT to ASS (for styling)
ffmpeg -i video.srt video.ass
```
