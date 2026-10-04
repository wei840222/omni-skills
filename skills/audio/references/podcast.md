# Podcast post-production workflow

Use this when the user wants an episode master, not show branding or marketing calendars
(those belong in the `podcast` skill).

## Pre-flight (recording advice only when asked)

- Quiet room; monitor on headphones
- Mic about a fist from the mouth; leave headroom (peaks nearer **−12 dBFS** than 0)
- Capture **44.1 kHz or 48 kHz**, 16- or 24-bit WAV/FLAC when possible
- Keep a raw backup before any destructive filter

## Post-production pipeline

### 1. Backup raw

```bash
cp raw_episode.wav raw_episode_backup.wav
```

### 2. Inspect

```bash
ffprobe -v quiet -print_format json -show_format -show_streams raw_episode.wav
```

### 3. Light cleanup (only as needed)

```bash
# Speech band focus
ffmpeg -i raw_episode.wav -af "highpass=f=80,lowpass=f=12000" cleaned.wav

# Persistent broadband noise (tune nf; verify consonants)
ffmpeg -i raw_episode.wav -af "afftdn=nf=-20" cleaned.wav
```

### 4. Silence / dead air (optional)

```bash
ffmpeg -i cleaned.wav -af "silenceremove=stop_periods=-1:stop_duration=1:stop_threshold=-40dB" trimmed.wav
```

Re-listen: aggressive thresholds eat breaths and punchlines.

### 5. Loudness

Default cross-platform podcast target for this skill: **I=−16 LUFS, TP=−1.5 dBTP, LRA≈11**.

```bash
ffmpeg -i trimmed.wav -af "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json" -f null - 2> measure.json
# Apply measured_* on second pass (see references/loudness.md and references/commands.md)

# Or:
ffmpeg-normalize trimmed.wav -o normalized.wav -t -16 -tp -1.5
```

If the user prioritizes Spotify music-style loudness for a hybrid show, use **−14 / −1**
and say so in the delivery note.

### 6. Gentle compression (optional, before or coordinated with loudnorm)

```bash
ffmpeg -i normalized.wav -af "acompressor=threshold=-20dB:ratio=3:attack=5:release=100" even.wav
```

Prefer compressing *then* final loudnorm measure when levels move a lot.

### 7. Intro / outro concat

```bash
printf "file 'intro.wav'\nfile 'even.wav'\nfile 'outro.wav'\n" > episode.txt
ffmpeg -f concat -safe 0 -i episode.txt -c copy episode_final.wav
```

Re-encode if codecs differ.

### 8. Distribution encode

Apple Podcasts for Creators documents:

- **RSS**: MP3 or AAC; AAC often better quality at the same bitrate; MP4/M4A packaging
  preferred over ADTS for AAC seeking/streaming.
- **Bitrate ballpark (RSS AAC/MP3)**: stereo 44.1/48 kHz often **128–256 kbps**; mono lower.
- **Connect masters**: WAV/FLAC/MP3 with stated PCM/FLAC sample-rate floors.

Practical defaults:

```bash
# Widely compatible RSS MP3
ffmpeg -i episode_final.wav -c:a libmp3lame -b:a 128k -ar 44100 episode.mp3

# Higher quality MP3
ffmpeg -i episode_final.wav -c:a libmp3lame -b:a 192k -ar 44100 episode_hq.mp3

# AAC in M4A (good for Apple-centric feeds)
ffmpeg -i episode_final.wav -c:a aac -b:a 160k -ar 44100 episode.m4a

# Tags
ffmpeg -i episode.mp3 \
  -metadata title="Episode 42: Topic" \
  -metadata artist="Podcast Name" \
  -metadata album="Season 2" \
  -c copy episode_tagged.mp3
```

### 9. Transcript (optional local)

```bash
ffmpeg -i episode.mp3 -ar 16000 -ac 1 -c:a pcm_s16le episode_whisper.wav
whisper episode_whisper.wav --model medium --output_format all
```

For diarized meeting products, hand off to `speech-to-text-transcription`.

### 10. Social highlight + audiogram (optional)

```bash
ffmpeg -i episode.mp3 -ss 15:30 -t 60 \
  -af "afade=t=in:d=1,afade=t=out:st=59:d=1" highlight.mp3

ffmpeg -i highlight.mp3 -filter_complex \
  "[0:a]showwaves=s=1080x1920:mode=cline:colors=white[wave];color=c=black:s=1080x1920[bg];[bg][wave]overlay" \
  -c:v libx264 -c:a aac audiogram.mp4
```

## Publish checklist

- [ ] Integrated loudness near chosen target (measure with `loudnorm` summary/json)
- [ ] True peak under chosen ceiling
- [ ] No obvious clipping/distortion on headphones
- [ ] Intro/outro attached if required
- [ ] Title/artist/album (or show) metadata present
- [ ] File plays in a second player
- [ ] Size acceptable for host limits
- [ ] Format matches host (MP3 vs M4A) per Apple/RSS notes above

## Platform export cheat sheet

| Destination | Container | Starting point |
|-------------|-----------|----------------|
| Generic RSS | MP3 128–192 kbps 44.1 kHz | Safest compatibility |
| Apple-centric RSS | AAC in MP4/M4A 128–256 kbps class | Per Apple bitrate tables |
| Spotify for Podcasters upload | Follow current host UI; master still −16 or −14 per intent | Loudness separate from host form |
| YouTube (needs video) | AAC 192+ kbps on a video file | Use `video` skill for full packaging |

## Batch raw episodes

```bash
for raw in raw_*.wav; do
  name="${raw#raw_}"
  name="${name%.wav}"
  ffmpeg -i "$raw" \
    -af "highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11" \
    -c:a libmp3lame -b:a 128k \
    "processed_${name}.mp3"
done
```

For release masters, expand to explicit two-pass loudnorm instead of single-pass batch.
