# FFmpeg and companion command patterns

All paths are examples. Substitute the user-provided input/output paths. Prefer writing
a new output file; keep the original master.

## Inspect

```bash
ffprobe -v quiet -print_format json -show_format -show_streams input.mp3

ffprobe -v error -show_entries stream=codec_name,sample_rate,channels,bit_rate:format=duration,bit_rate \
  -of default=noprint_wrappers=1 input.mp3
```

## Format conversion

```bash
# MP3 VBR (good default share quality)
ffmpeg -i input.wav -c:a libmp3lame -q:a 2 output.mp3

# MP3 CBR
ffmpeg -i input.wav -c:a libmp3lame -b:a 192k output.mp3

# AAC in M4A
ffmpeg -i input.wav -c:a aac -b:a 192k output.m4a

# FLAC lossless
ffmpeg -i input.wav -c:a flac output.flac

# WAV PCM 16-bit
ffmpeg -i input.mp3 -c:a pcm_s16le output.wav

# Opus
ffmpeg -i input.wav -c:a libopus -b:a 128k output.opus
```

## Extract audio from video

```bash
# Copy audio bitstream when compatible
ffmpeg -i video.mp4 -vn -c:a copy audio.m4a

# Re-encode to MP3
ffmpeg -i video.mp4 -vn -c:a libmp3lame -q:a 2 audio.mp3

# Edit-friendly WAV
ffmpeg -i video.mp4 -vn -c:a pcm_s16le -ar 44100 audio.wav
```

## Trim / cut

```bash
# Stream copy window (fast; cut points follow keyframes for some codecs)
ffmpeg -i input.mp3 -ss 00:00:30 -to 00:02:00 -c copy output.mp3

# First 60 seconds
ffmpeg -i input.mp3 -t 60 -c copy output.mp3

# Drop opening 10 seconds
ffmpeg -i input.mp3 -ss 10 -c copy output.mp3
```

When filters are applied, place `-ss` to balance speed vs accuracy (see `ffmpeg` skill for
seek semantics) and re-encode audio.

## Merge multiple files

```bash
printf "file 'clip1.mp3'\nfile 'clip2.mp3'\nfile 'clip3.mp3'\n" > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp3
```

Clips should share codec parameters for `-c copy`. Otherwise re-encode the concat output.

## Volume and loudness

```bash
# Linear gain
ffmpeg -i input.mp3 -af "volume=1.5" output.mp3
ffmpeg -i input.mp3 -af "volume=-3dB" output.mp3

# Measure only (no output file)
ffmpeg -i input.mp3 -af "loudnorm=print_format=summary" -f null -

# Single-pass loudnorm (good preview; prefer two-pass for finals)
ffmpeg -i input.mp3 -af "loudnorm=I=-16:TP=-1.5:LRA=11" output.mp3

# Two-pass loudnorm (measure → apply measured_* + linear)
ffmpeg -i input.mp3 -af "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json" -f null - 2> measure.json
# Read input_i, input_tp, input_lra, input_thresh, target_offset from JSON, then:
ffmpeg -i input.mp3 -af "loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=<input_i>:measured_TP=<input_tp>:measured_LRA=<input_lra>:measured_thresh=<input_thresh>:offset=<target_offset>:linear=true" output.mp3

# Helper CLI when installed
ffmpeg-normalize input.mp3 -o output.mp3 -t -16 -tp -1.5
```

Default `loudnorm` targets in FFmpeg are **I=-24, TP=-2, LRA=7** (broadcast-oriented).
Override `I`/`TP`/`LRA` for podcasts or streaming. See `references/loudness.md`.

## Noise reduction and voice cleanup

```bash
# Rumble / hiss trim for speech
ffmpeg -i input.mp3 -af "highpass=f=80,lowpass=f=8000" output.mp3

# FFT denoise (tune nf carefully; too aggressive dulls consonants)
ffmpeg -i input.mp3 -af "afftdn=nf=-25" output.mp3

# Non-local means denoise
ffmpeg -i input.mp3 -af "anlmdn" output.mp3
```

SoX (optional) can help stubborn broadband noise; only use when installed and FFmpeg
denoise is insufficient.

## Speed / tempo

```bash
# Pitch-preserving tempo (each atempo in 0.5–2.0)
ffmpeg -i input.mp3 -af "atempo=1.5" output.mp3
ffmpeg -i input.mp3 -af "atempo=0.75" output.mp3
ffmpeg -i input.mp3 -af "atempo=2.0,atempo=2.0" output.mp3   # 4×

# Rate change that also shifts pitch
ffmpeg -i input.mp3 -af "asetrate=44100*1.5,aresample=44100" output.mp3
```

## Fade in / out

```bash
ffmpeg -i input.mp3 -af "afade=t=in:st=0:d=3" output.mp3

duration=$(ffprobe -v error -show_entries format=duration -of csv=p=0 input.mp3)
# Portable start time without bc:
python3 - <<'PY' 
import os
d=float(os.environ["D"]); print(max(d-3,0))
PY
# Or compute st for afade out, then:
ffmpeg -i input.mp3 -af "afade=t=out:st=${START}:d=3" output.mp3
```

## Silence removal

```bash
ffmpeg -i input.mp3 -af "silenceremove=stop_periods=-1:stop_duration=0.5:stop_threshold=-50dB" output.mp3
ffmpeg -i input.mp3 -af "silenceremove=start_periods=1:start_threshold=-50dB" output.mp3
```

Thresholds are content-dependent; verify speech is not chopped.

## Channels and sample rate

```bash
ffmpeg -i input.mp3 -ac 1 output.mp3
ffmpeg -i input.mp3 -ac 2 output.mp3
ffmpeg -i input.mp3 -af "pan=mono|c0=FL" output.mp3
ffmpeg -i input.mp3 -ar 44100 output.mp3
ffmpeg -i input.mp3 -ar 48000 output.mp3
# Whisper prep
ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le whisper_ready.wav
```

## Dynamics and EQ (light)

```bash
ffmpeg -i input.mp3 -af "acompressor=threshold=-20dB:ratio=4:attack=5:release=50" output.mp3
ffmpeg -i input.mp3 -af "alimiter=limit=0.9" output.mp3
ffmpeg -i input.mp3 -af "acompressor=threshold=-20dB:ratio=3:attack=5:release=100,loudnorm=I=-16:TP=-1.5:LRA=11" output.mp3

ffmpeg -i input.mp3 -af "bass=g=5" output.mp3
ffmpeg -i input.mp3 -af "treble=g=3" output.mp3
ffmpeg -i input.mp3 -af "equalizer=f=3500:t=q:w=1:g=3" output.mp3
ffmpeg -i input.mp3 -af "equalizer=f=7000:t=q:w=2:g=-4" output.mp3
```

## Metadata

```bash
ffmpeg -i input.mp3 \
  -metadata title="Episode 42" \
  -metadata artist="Show Name" \
  -metadata album="Season 2" \
  -c copy tagged.mp3
```

## Ringtone-style clip

```bash
ffmpeg -i song.mp3 -ss 60 -t 30 \
  -af "afade=t=in:st=0:d=1,afade=t=out:st=29:d=1" \
  -c:a libmp3lame -b:a 192k ringtone.mp3

ffmpeg -i song.mp3 -ss 60 -t 30 \
  -af "afade=t=in:st=0:d=1,afade=t=out:st=29:d=1" \
  -c:a aac -b:a 192k ringtone.m4r
```

## Batch patterns

```bash
for f in *.wav; do
  ffmpeg -i "$f" -c:a libmp3lame -q:a 2 "${f%.wav}.mp3"
done

for f in *.mp3; do
  ffmpeg -i "$f" -af "loudnorm=I=-16:TP=-1.5:LRA=11" "normalized_$f"
done
```

## Stem separation (Demucs, optional)

```bash
python3 -m pip install -U demucs
# Default Hybrid Transformer model separates drums, bass, vocals, other
demucs -n htdemucs track.mp3
# Vocals vs accompaniment
demucs -n htdemucs --two-stems=vocals track.mp3
```

Outputs land under `separated/<model>/<track>/` as WAV stems (see Demucs README). GPU
RAM limits may require `--segment`.

## Recovery habits

- On failure, keep the original; delete only partial outputs the user agrees are junk.
- Simplify the filter graph; re-encode step-by-step to isolate the failing filter.
- Re-probe after each major stage on long podcasts before the next expensive pass.
- When a long chain fails, rerun inspect → single-filter → verify before restoring the full graph.
