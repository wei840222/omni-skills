---
name: ffmpeg
description: Process video and audio streams using correct FFmpeg codecs, filters,
  and encoding settings. Use when the user wants to convert media formats, trim clips,
  extract audio, scale/crop video, or normalize loudness.
metadata:
  version: 1.0.1
  openclaw: '{"emoji": "🎬", "requires": {"bins": ["ffmpeg"]}}'
  related-skills: '{"bash": "Execute FFmpeg scripts and automate batch processing.",
    "powershell": "Execute FFmpeg commands on Windows systems."}'
---

## Input Seeking (Major Difference)

- `-ss` BEFORE `-i`: fast seek, may be inaccurate—starts from nearest keyframe
- `-ss` AFTER `-i`: frame-accurate but slow—decodes from start
- Combine both: `-ss 00:30:00 -i input.mp4 -ss 00:00:05`—fast seek then accurate trim
- For cutting, add `-avoid_negative_ts make_zero` to fix timestamp issues

## Stream Selection

- Default: first video + first audio—review this default to ensure it meets requirements
- Explicit selection: `-map 0:v:0 -map 0:a:1`—first video, second audio
- All streams of type: `-map 0:a`—all audio streams
- Copy specific: `-map 0 -c copy`—all streams, no re-encoding
- Exclude: `-map 0 -map -0:s`—all except subtitles

## Encoding Quality

- CRF (Constant Rate Factor): lower = better quality, larger file—18-23 typical for H.264
- `-preset`: ultrafast to veryslow—slower = smaller file at same quality
- Two-pass for target bitrate: first pass analyzes, second pass encodes
- `-crf` and `-b:v` mutually exclusive—use one or the other

## Container vs Codec

- Container (MP4, MKV, WebM): wrapper format holding streams
- Codec (H.264, VP9, AAC): compression algorithm for stream
- Codecs require specific compatible containers—H.264 in MP4/MKV, not WebM; VP9 in WebM/MKV, not MP4
- Copy codec to new container: `-c copy`—fast, no quality loss

## Filter Syntax

- Simple: `-vf "scale=1280:720"`—single filter chain
- Complex: `-filter_complex "[0:v]scale=1280:720[scaled]"`—named outputs for routing
- Chain filters: `-vf "scale=1280:720,fps=30"`—comma-separated
- Filter order matters—scale before crop gives different result than crop before scale

## Common Filters

- Scale: `scale=1280:720` or `scale=-1:720` for auto-width maintaining aspect
- Crop: `crop=640:480:100:50`—width:height:x:y from top-left
- FPS: `fps=30`—change framerate
- Trim: `trim=start=10:end=20,setpts=PTS-STARTPTS`—setpts resets timestamps
- Overlay: `overlay=10:10`—position from top-left

## Audio Processing

- Sample rate: `-ar 48000`—standard for video
- Channels: `-ac 2`—stereo
- Audio codec: `-c:a aac -b:a 192k`—AAC at 192kbps
- Normalize: `-filter:a loudnorm`—EBU R128 loudness normalization
- Extract audio: `-vn -c:a copy output.m4a`—no video, copy audio

## Concatenation

- Same codec/params: concat demuxer—`-f concat -safe 0 -i list.txt -c copy`
- Different formats: concat filter—`-filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1"`
- list.txt format: `file 'video1.mp4'` per line—escape special characters
- Different resolutions: scale/pad to match before concat filter

## Subtitles

- Burn-in (hardcode): `-vf "subtitles=subs.srt"`—these are permanent in the video stream
- Mux as stream: `-c:s mov_text` (MP4) or `-c:s srt` (MKV)—user toggleable
- From input: `-map 0:s`—include subtitle streams
- Extract: `-map 0:s:0 subs.srt`—first subtitle to file

## Hardware Acceleration

- Decode: `-hwaccel cuda` or `-hwaccel videotoolbox` (macOS)
- Encode: `-c:v h264_nvenc` (NVIDIA), `-c:v h264_videotoolbox` (macOS)
- Speed benefits depend on video length and setup overhead; gains usually appear on long videos
- Quality may differ—software encoding often produces better quality

## Common Mistakes

- Remember to use `-c copy` when copying streams to avoid slow, lossy re-encoding
- `-ss` after `-i` for long videos—takes forever seeking
- Audio desync after cutting—use `-async 1` or `-af aresample=async=1`
- Filter on stream copy—filters require re-encoding; `-c copy` + `-vf` = error
- Output extension requires explicit codec selection (e.g. `-c:v libx264`) because defaults differ from expectations
