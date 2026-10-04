# Research sources (Gate 6)

Verified during the 2026-10-05 audio refactor handoff. Prefer these URLs over model
memory when updating loudness, delivery, or tool claims.

## Agent Skills format

- Agent Skills specification — https://agentskills.io/specification
- Optional directories / progressive disclosure — https://agentskills.io/specification#optional-directories
- Agent Skills docs index — https://agentskills.io/llms.txt

## Loudness and measurement

- Spotify for Artists — Loudness normalization on Spotify —
  https://support.spotify.com/us/artists/article/loudness-normalization/
  (−14 dB LUFS playback target; ITU 1770; master tips −14 LUFS and TP below −1 dBTP;
  hotter masters keep TP below −2 dBTP; Premium Loud/Normal/Quiet playback modes;
  normalization at playback, not by rewriting the master; album vs shuffle behavior)
- FFmpeg Filters Documentation — `loudnorm` —
  https://ffmpeg.org/ffmpeg-filters.html#loudnorm
  (EBU R128 loudness normalization filter; parameters I/TP/LRA/measured_*/linear)
- Local `ffmpeg -h filter=loudnorm` on FFmpeg 9.0.2 (handoff host) — defaults
  **I=−24, TP=−2, LRA=7**; confirms option ranges used in commands reference
- EBU R128 publication hub — https://tech.ebu.ch/publications/r128
  (broadcast loudness alignment at −23 LUFS class; use when user names broadcast)

## Podcast / Apple delivery formats

- Apple Podcasts for Creators — Audio requirements —
  https://podcasters.apple.com/support/893-audio-requirements
  (Connect accepts WAV/FLAC/MP3 with sample-rate/bit-depth tables; RSS accepts MP3 or AAC;
  AAC preferred over MP3 at same bitrate; MP4 preferred over ADTS for AAC; bitrate tables
  by mono/stereo and sample rate. **No LUFS mandate in this article** — skill podcast
  default −16 LUFS is a cross-platform engineering choice, not an Apple statute.)

## Transcription

- OpenAI Whisper README — https://github.com/openai/whisper/blob/main/README.md
  (install; model table tiny→large + turbo; English `.en` notes; turbo not for translation;
  CLI examples; language/translate tasks)

## Stem separation

- Facebook Research Demucs README — https://github.com/facebookresearch/demucs/blob/main/README.md
  (`pip install -U demucs`; default Hybrid Transformer **htdemucs**; four stems;
  `--two-stems=vocals`; output layout under `separated/`; GPU segment notes)

## FFmpeg denoise filters (capability check)

- Local `ffmpeg -filters` on handoff host lists `afftdn`, `anlmdn`, `arnndn`, `highpass`,
  `lowpass`, `silenceremove`, `loudnorm`, `dynaudnorm` — command recipes rely only on
  filters present in modern FFmpeg builds; still verify on the user machine before long jobs.

## Corrections vs pre-refactor claims

| Old claim | Treatment |
|-----------|-----------|
| “Apple Podcasts −16 LUFS / −19 LUFS” as hard platform law | Replaced with Apple format requirements + explicit skill default −16 LUFS; removed bogus −19-as-Apple-law quick reference |
| Unverified per-DSP LUFS rows (Tidal/Deezer/etc.) as fact tables | Marked approximate / assumption unless primary URL added |
| FFmpeg loudnorm implied podcast defaults | Document real filter defaults (−24/−2/7) and required overrides |
| Google Podcasts rows | Removed as a hard authority (service retired/changed); use generic RSS guidance |
| Whisper model table without turbo/translate caveats | Updated from current upstream README |
