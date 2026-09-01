# Core Rules

### 1. Engine Selection by Context

| Scenario | Engine | Why |
|----------|--------|-----|
| Default (recommended) | Whisper local | 100% offline, no data leaves machine |
| Apple Silicon | MLX Whisper | Native acceleration, still local |
| Word timestamps | whisper-timestamped | DTW alignment, still local |

Default: Whisper local (turbo model). Load the `engines.md` reference in this directory before selecting an optional cloud alternative.

### 2. Format Selection by Platform

| Platform | Format | Notes |
|----------|--------|-------|
| YouTube | VTT or SRT | VTT preferred |
| Netflix/Pro | TTML | Strict timing rules |
| Social (TikTok, IG) | Burn-in (ASS) | Embedded in video |
| General | SRT | Universal compatibility |
| Karaoke/effects | ASS | Advanced styling |

Ask user's target platform if not specified.

### 3. Professional Timing Standards

**Netflix-compliant (default):**
- Min duration: 5/6 second (0.833s)
- Max duration: 7 seconds
- Max chars/line: 42
- Max lines: 2
- Gap between subtitles: 2+ frames

**Social media:**
- Shorter segments (2-4 words)
- More frequent breaks
- Centered or dynamic positioning

### 4. Segmentation Rules

Break lines:
- After punctuation marks
- Before conjunctions (and, but, or)
- Before prepositions

Keep these elements together on the same line:
- Article from noun
- Adjective from noun
- First name from last name
- Verb from subject pronoun
- Auxiliary from verb

### 5. Word-Level Timestamps

Use word timestamps for:
- Karaoke-style highlighting
- Precise sync verification
- TikTok/Instagram animated captions
- Quality checking transcript accuracy

For the OpenAI Whisper CLI, enable word timestamps with `--word_timestamps True`; use the word-level output produced by `whisper_timestamped` when that engine is selected.

### 6. Speaker Identification

For multi-speaker content:
- Use diarization (pyannote local, or cloud APIs if configured)
- Format: `[Speaker 1]` or `[Name]` if known
- SDH format: `JOHN: What do you think?`

### 7. Quality Verification

Before delivering:
- Check sync at start, middle, end
- Verify character limits per line
- Confirm speaker labels if multi-speaker
- Test burn-in render quality
