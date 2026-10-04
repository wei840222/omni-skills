# Loudness targets and measurement

Facts below are tied to primary sources listed in `references/sources.md`. Platform
apps still apply their own playback processing; mastering tips optimize *upload*
masters, not a guarantee of identical app output on every device.

## Spotify (music) — verified artist guidance

Spotify adjusts playback toward **-14 dB LUFS** (ITU-R BS.1770 family). Masters tip:

| Guidance | Value |
|----------|-------|
| Integrated loudness target | **−14 LUFS** |
| True Peak | **Below −1 dBTP** (prefer for lossy encodes) |
| If louder than −14 LUFS | Keep True Peak **below −2 dBTP** to reduce transcoder distortion |
| Album vs shuffle | Album context can share gain; playlists/shuffle may normalize per track |
| Premium user modes | Loud ≈ −11, Normal ≈ −14, Quiet ≈ −19 LUFS (playback), not master targets |

Spotify measures on upload but applies gain at **playback**; it does not rewrite the
uploaded master. Web player / some third-party devices may skip normalization.

## Podcasts and speech

Apple’s public **Podcasts for Creators — Audio requirements** document focuses on
**format, sample rate, and bitrate** (Connect: WAV/FLAC/MP3; RSS: MP3 or AAC with
recommended rate tables). It does **not** publish a single official LUFS number in that
article. Practical cross-platform speech masters therefore use a documented compromise:

| Intent | Integrated | True Peak | Notes |
|--------|------------|-----------|-------|
| Cross-platform podcast default | **−16 LUFS** | **−1.5 dBTP** (≤ −1.0 OK if measured clean) | Safe shared target used in this skill |
| Spotify-aligned speech/music hybrid | **−14 LUFS** | ≤ −1 dBTP | When user prioritizes Spotify music-style loudness |
| “Quiet” / accessibility leaning | **−18 to −19 LUFS** | ≤ −1 dBTP | Softer; say so when chosen |
| Broadcast Europe | **−23 LUFS** (EBU R128) | typically −1 dBTP class | Only when user names broadcast/EBU |
| US TV-style | **−24 LKFS** (ATSC A/85 family) | regional TP rules | Only when user names broadcast/ATSC |

Phrase Apple guidance accurately: “Apple documents file/codec requirements; this skill’s
podcast default is −16 LUFS for consistent multi-host delivery,” rather than calling −16
an Apple statute.

## Music streaming (approximate ecosystem)

| Platform / context | Practical master target | Notes |
|--------------------|-------------------------|-------|
| Spotify | −14 LUFS, TP ≤ −1 (≤ −2 if hot) | Primary-sourced above |
| Apple Music Sound Check | Playback feature; master still keep sane TP | Cite an Apple mastering page before stating a single public LUFS law |
| YouTube / social reels | Often ballpark −14 LUFS speech+music hybrids | Prefer measure-after; platform processing varies |
| Amazon / Tidal / Deezer | Commonly near −14 to −15 LUFS in industry charts | Treat third-party charts as unverified unless cited in sources.md |

When the user names a store without a primary URL in `sources.md`, master to **−14 LUFS /
TP −1**, label the assumption, and offer to re-target after they confirm.

## Broadcast standards (names only until user confirms region)

| Standard | Target | Region focus |
|----------|--------|--------------|
| EBU R128 | −23 LUFS | Europe broadcast/streaming loudness alignment |
| ATSC A/85 | −24 LKFS | US television loudness practices |
| ARIB TR-B32 | −24 LKFS class | Japan broadcast practices |

Load official PDFs when the deliverable is true broadcast compliance; this skill’s
default consumer/podcast path does not silently switch to −23.

## FFmpeg `loudnorm` behavior (verified locally / docs)

FFmpeg filter `loudnorm` implements EBU R128-style normalization.

| Option | Role | Filter default |
|--------|------|----------------|
| `I` | Integrated loudness target | **−24** LUFS |
| `TP` | Max true peak | **−2** dBTP |
| `LRA` | Loudness range target | **7** |
| `linear` | Prefer linear gain when possible | `true` |
| `print_format` | `none` / `json` / `summary` | `none` |
| `measured_*` | Second-pass inputs from first measure | required for best finals |

**Always override `I`/`TP` for podcasts (−16 / −1.5) or Spotify-oriented music (−14 / −1).**
Leaving defaults yields broadcast-ish −24 masters, which sound quiet on mobile podcast apps.

### Recommended measure → apply loop

```bash
ffmpeg -i input.wav -af "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json" -f null - 2> measure.json
# Parse input_i, input_tp, input_lra, input_thresh, target_offset
ffmpeg -i input.wav -af "loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=...:measured_TP=...:measured_LRA=...:measured_thresh=...:offset=...:linear=true" out.wav
```

Optional helper:

```bash
ffmpeg-normalize input.wav -o out.wav -t -16 -tp -1.5
```

### LRA guidance

| Content | Comfortable LRA ballpark |
|---------|--------------------------|
| Spoken podcast | ~5–11 LU |
| Dynamic music | ~8–15+ LU |

Forcing very low LRA flattens performance; only compress hard when the user wants “radio
evenness.”

## LUFS vocabulary

- **LUFS / LKFS** — integrated perceived loudness (BS.1770 family). Closer to 0 = louder.
- **True Peak (dBTP)** — estimated inter-sample peak; keep below 0; leave headroom for lossy encode.
- **LRA** — loudness range; variation over time.

## Common mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Master at −8 LUFS “for loudness wars” | Platforms turn it down; adds distortion risk | Target platform table |
| Only peak-normalize to 0 dBFS | Uneven speech; clips after lossy encode | LUFS + TP headroom |
| Forget FFmpeg default I=−24 | Podcast sounds too quiet | Set I/TP explicitly |
| Invent Apple LUFS as law | Not in Apple audio-requirements article | Use format specs + stated skill default |
| Skip measure pass on finals | Drift from target | Two-pass or `ffmpeg-normalize` |

## Verify after encode

```bash
ffmpeg -i output.mp3 -af "loudnorm=print_format=summary" -f null -
```

Confirm integrated loudness near the target and true peak within the chosen ceiling.
