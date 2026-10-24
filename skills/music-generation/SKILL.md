---
name: music-generation
description: Generate AI music with optimized prompts, style control, and production-ready audio output. Trigger when the user wants to create music, background tracks, or sound effects.
metadata:
  openclaw: '{"emoji": "🎵"}'
---

# AI Music Generation

Help users create AI-generated music and audio.

**Rules:**
- Ask what they need: full songs with vocals, instrumentals, background music, or sound effects
- Check provider files: `references/suno.md`, `references/udio.md`, `references/stable-audio.md`, `references/musicgen.md`, `references/mubert.md`, `references/soundraw.md`, `references/riffusion.md`, `references/replicate.md`
- Check `references/prompting.md` for music prompt techniques
- Start with short clips to validate style before full generation

---

## Provider Selection

| Use Case | Recommended | When to load |
|----------|-------------|--------------|
| Full songs with vocals | Suno, Udio | Load `references/suno.md` or `references/udio.md` |
| Instrumentals, background | Stable Audio, MusicGen, Mubert | Load `references/stable-audio.md`, `references/musicgen.md`, or `references/mubert.md` |
| Royalty-free commercial | Soundraw, Mubert | Load `references/soundraw.md` or `references/mubert.md` |
| Classical/orchestral | AIVA, Stable Audio | Load `references/stable-audio.md` |
| Sound effects | Stable Audio, ElevenLabs | Load `references/stable-audio.md` |
| Local/private | MusicGen, Stable Audio Open | Load `references/musicgen.md` or `references/stable-audio.md` |
| Quick testing | Replicate, Riffusion | Load `references/replicate.md` or `references/riffusion.md` |

---

## Prompting Fundamentals

- **Genre first** — "electronic", "jazz", "hip-hop", "orchestral"
- **Mood/energy** — "upbeat", "melancholic", "aggressive", "calm"
- **Instruments** — "piano", "guitar", "synth", "strings"
- **Tempo** — "120 BPM", "slow", "fast-paced"
- **Reference artists** — "in the style of Hans Zimmer" (where supported)

---

## Output Formats

- **WAV** — Uncompressed, highest quality, large files
- **MP3** — Compressed, universal compatibility
- **FLAC** — Lossless compression, good for archival
- **Stems** — Separate tracks (drums, bass, vocals) when available

---

## Common Workflows

### Background Music for Video
1. Determine video length and mood
2. Generate instrumental at matching duration
3. Adjust tempo to match cuts if needed
4. Mix levels appropriately

### Full Song Production
1. Write or generate lyrics
2. Describe musical style in detail
3. Generate multiple variations
4. Select best, extend or edit
5. Export stems if available for mixing

### Sound Design
1. Describe sound effect clearly
2. Specify duration needed
3. Generate variations
4. Layer and process as needed

---

## Licensing Considerations

| Provider | Personal Use | Commercial Use |
|----------|--------------|----------------|
| Suno | ✅ Free tier | Pro plan required |
| Udio | ✅ Free tier | Subscription required |
| Stable Audio | ✅ | License required |
| MusicGen | ✅ | Research license |
| Mubert | ✅ | API license |
| Soundraw | ✅ | Subscription |

**Verify current licensing terms prior to commercial use.**

---

## Quality Tips

- **Be specific** — "acoustic guitar fingerpicking" beats "guitar"
- **Layer generations** — combine outputs for richer sound
- **Use stems** — mix individual elements for control
- **Match context** — consider where audio will be used
- **Iterate** — first generation rarely perfect

---

*Load the matching `references/<provider>.md` file for setup details and API usage.*

## State location

Music Generation state may exist in `<workspace>/music-generation/`, `<workspace>/memory/music-generation/`, or `~/music-generation/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/music-generation/`, `<workspace>/memory/music-generation/`, `~/music-generation/`.
3. If none exists and state must be created, default to `<workspace>/music-generation/`.

Use the selected `<state_root>` for every state operation in this skill.

This skill is knowledge-only and does not store local configuration or session state.
