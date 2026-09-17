---
name: suno
description: Generate music and structured lyrics with Suno. Trigger when users request
  to create songs, jingles, anthems, or background tracks, convert lyrics into audio,
  match a specific artist's style, or troubleshoot generation issues like off-genre
  results or cut-off endings.
metadata:
  openclaw: '{"emoji": "🎵"}'
---

This skill stores all persistent data under `<state_root>/suno/` (config, preferences, project tracking, downloaded audio — see `references/setup.md` on first use, `references/memory-template.md` for the memory format). If you have data at an old location (`~/suno/` or `~/clawic/suno/`), move it to `<state_root>/suno/`, and say in one line that you moved it and from where.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/suno/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| default_method | prompts \| api \| browser | prompts | Resolves Core Rule 3's default branch: prompts = craft text for manual pasting; api/browser = deliver audio |
| api_provider | aimusicapi \| evolink | aimusicapi | Which hosted service `references/api.md` examples target and which env var holds the key |
| plan_tier | free \| paid | free | Gates commercial deliverables (Output Gates), credit budgeting in `references/browser.md`, WAV/stems availability in `references/release.md` |
| audio_format | mp3 \| wav | mp3 | Download format in `references/release.md`; wav requires a paid plan |
| lyrics_language | text (language name) | English | Language lyrics are written in; when not English, also named in the style field (`references/lyrics.md`) |

Preference areas to record as the user reveals them:

- **taste** — go-to genres, moods, vocal textures, eras; steers first-draft prompts (stated preference → config; observed reactions → memory.md)
- **workflow** — present-and-pick vs auto-download both clips; how many rerolls before checking in
- **spend posture** — confirm before multi-extend builds or runs beyond a credit threshold
- **conventions** — song/file naming, project folder layout under `<state_root>/suno/`
- **delivery** — where finished audio lands, whether stems are fetched by default

## When to load

Load this skill when tasked with generating or troubleshooting music via Suno. For specific workflows, load the corresponding reference:

- **Music Generation Setup**: Load `references/setup.md`.
- **Crafting Prompts**: Load `references/prompts.md`.
- **Writing/Structuring Lyrics**: Load `references/lyrics.md`.
- **Extending/Stitching Tracks**: Load `references/extend.md`.
- **Covers & Personas**: Load `references/covers.md`.
- **Jingles & Short Audio**: Load `references/jingles.md`.
- **Troubleshooting**: Load `references/debug.md`.
- **Commercial/Release Prep**: Load `references/release.md`.
- **API Generation**: Load `references/api.md`.
- **Browser Automation**: Load `references/browser.md`.

Maintain focus on Suno generation. Route tasks involving editing existing audio to `audio` or `ffmpeg` (use `audio` or `ffmpeg`).

## Quick Reference

| Situation | Play |
|-----------|------|
| First run, no `<state_root>/suno/` | `references/setup.md` |
| Song cuts off mid-phrase | Missing ending cue — `[End]` as final tag (rule 4) |
| Style description got sung | Words were in the lyrics box — sound in style field, words in lyrics field (rule 1) |
| Output generic or off-genre | Front-load genre, 8-12 precise terms, add era + texture → `references/debug.md` |
| "Make it sound like [artist]" | Translate to voice + era + production (rule 6) — names get stripped, credits still spent |
| Great clip that drifts, or song needs >4 min | Extend from the last good timestamp → `references/extend.md` |
| Chorus melody changes every repeat | Paste identical chorus text each time (`references/lyrics.md`) |
| New style for an existing song; consistent voice across songs | Covers and Personas → `references/covers.md` |
| Jingle, podcast intro, loop, birthday song | `references/jingles.md` |
| Stems, WAV, remaster, rights, distribution | `references/release.md` |
| Anything else about generating with Suno | Reproduce with a minimal prompt in simple mode, then re-add one element per run until it breaks (`references/debug.md`) |

Depth on demand: `references/debug.md` symptom→cause chains · `references/prompts.md` style prompt craft · `references/styles.md` tag vocabulary · `references/lyrics.md` structure, delivery, word budget · `references/extend.md` long tracks, crop, stitch · `references/covers.md` covers, personas, uploads · `references/jingles.md` functional audio briefs · `references/release.md` downloads, stems, rights · `references/api.md` hosted APIs · `references/browser.md` suno.com automation · `references/setup.md` first run · `references/memory-template.md` memory format.

## Core Rules

1. **Style field describes; lyrics field gets sung.** Genre words typed into the lyrics box become sung words ("upbeat pop song" turns into the opening line). Sound goes in the style field, words in the lyrics field, structure in `[bracketed]` tags on their own lines.
2. **Each generation is sampling, not drafting.** One run returns two clips from the same prompt — two rolls, not a draft and a revision. When a roll lands, save its exact style string to `<state_root>/suno/memory.md` and reuse it verbatim; rewording a working prompt resets the odds.
3. **Pick the method by situation.**

   | Situation | Method |
   |-----------|--------|
   | Deliver audio files programmatically | Hosted API (`references/api.md`) |
   | No API key, browser tool available | Automate suno.com (`references/browser.md`) |
   | User will paste into suno.com themselves | Craft prompt + lyrics only |
   | Unclear (default) | `default_method` from config; if audio delivery is requested and neither key nor browser exists, ask once and record the answer |

4. **Force endings.** Ensure clips include an ending cue to finish cleanly. Close the lyrics with an `[Outro]` section and `[End]` as the final tag; for instrumentals, `[Fade Out]` then `[End]`.
5. **Long songs are built, not one-shotted.** Generate the strongest opening clip, extend from the last good timestamp (not the raw end), repeat until `[End]`, stitch with Get Whole Song. Target 2-4 minutes; Suno >=3.5 generates 4-minute clips and >=4.5 allows 8-minute songs, but one-shot epics drift in melody and mix. Full workflow and segment planning: `references/extend.md`.
6. **Translate artist names into attributes.** Moderation rejects or strips artist and brand names — and the credits are still spent. Convert with three knobs: voice texture + era + production. "Like Springsteen" → "raspy heartland rock male vocals, 80s arena production, driving piano and saxophone".
7. **API pattern: generate → poll every 5 seconds → download immediately.** Audio URLs expire; generation runs 30-90 seconds. Working code in `references/api.md`.

## Prompt Essentials

Layered formula (full guide: `references/prompts.md`, vocabulary: `references/styles.md`):
```
[genre] [subgenre] [mood] [tempo] [instruments] [vocals] [era/influence]
```
Example: "indie folk melancholic slow acoustic guitar soft female vocals 90s"

- Front-load: earlier terms steer harder in practice — genre first, garnish last.
- Specificity beats quantity: "shoegaze" outsteers "rock, reverb, dreamy, atmospheric".
- Stay within 8-12 style terms (canonical limits: `references/styles.md`).
- Instrumental: set the instrumental toggle AND leave the lyrics box empty; stray text gets sung.

## Output Gates

Before submitting any generation, check:
- No artist, band, or brand names in prompt or lyrics?
- Everything that should not be sung is inside `[brackets]` on its own line?
- Ending cue present (`[End]` last) for a standalone song?
- Style terms 8-12, no contradictions (lo-fi + polished, happy + mournful)?
- Instrumental toggle matches the request — and lyrics box empty if instrumental?
- Song over 4 minutes → full lyrics written and segment plan made before the first run (`references/extend.md`)?
- Commercial deliverable → user confirmed a paid Suno plan at generation time (`references/release.md`)?

## Traps

| Trap | Why it fails | Do instead |
|------|--------------|------------|
| Artist/brand names in prompt | Rejected or stripped by moderation; credits spent | Voice + era + production attributes (rule 6) |
| Free-plan track for commercial use | Rights attach at generation time under the plan then active; free-tier songs are non-commercial under Suno's terms | Confirm paid plan before generating deliverables (`references/release.md`) |
| Regenerating a clip that was 90% right | Discards the roll that worked | Crop the bad part, extend from the last good bar (`references/extend.md`) |
| Lyrics far over 300 words for a 3-minute song | Rushed, half-spoken delivery | Word budget in `references/lyrics.md` |
| Different chorus wording on each repeat | Each variant gets its own melody | Paste identical chorus text every time |
| Negations in the style field ("no drums") | Style terms act as attractors; the noun still pulls | Omit the term, or use Suno's Exclude Styles field |
| Prompting an exact duration ("90 seconds long") | Duration text is treated as style words, not a control | Generate a short structure, then crop to length (`references/jingles.md`) |
| Multi-extend build on an unvalidated idea | Burns a day of credits before you know the core works | Validate the opening clip first; extend only what already lands (`references/extend.md`) |

## Where Experts Disagree

- **Tags vs natural-language prose.** Suno >=4.5 handles prose descriptions as well as comma tags; prose reads better, tags are more reproducible and easier to mutate one term at a time. Default: tags; prose when a mood is easier to describe than to enumerate. Reproducibility needs (albums, clients) → tags.
- **Write lyrics vs let Suno generate them.** Generated lyrics are serviceable but generic — competent rhymes, no specifics. Anything with an emotional stake or a client → write them (`references/lyrics.md`); throwaway background tracks → generated is fine.
- **One-shot vs extend-built long songs.** >=4.5 can one-shot 8 minutes; drift risk rises with length. Boundary: past ~4 minutes, or when any section must be exactly right, build by extending (rule 5).

## Security & Privacy

**Data storage.** This skill creates `<state_root>/suno/` on first use:
- **config.yaml** — Declared preferences (variables above)
- **memory file** — Observed preferences, successful prompts
- **projects folder** — Per-project tracking
- **songs folder** — Downloaded audio (optional)

All data stays local. API keys live in environment variables, keep them strictly out of files.

**This skill does:**
- Generate music via hosted APIs (requires API key from provider)
- Navigate suno.com with browser automation
- Craft optimized prompts for Suno's model
- Write lyrics with proper structure tags
- Track projects and successful patterns locally

**This skill does NOT:**
- Store API keys in plain text files
- Access files outside `<state_root>/suno/`
- Make requests without user direction

**External endpoints.** When using hosted APIs, requests go to:

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| api.aimusicapi.ai | Prompts, lyrics | Music generation |
| api.evolink.ai | Prompts, lyrics | Music generation |
| suno.com | Browser session | Direct platform access |

API keys authenticate requests; prompts and lyrics are sent for processing.

**Guardrails.** By using this skill with APIs, prompts and lyrics are sent to third-party services for music generation. Only use services you trust with your creative content.

## Related Skills
- `audio` — Audio processing and editing
- `video` — Combine music with video content
- `ffmpeg` — Audio format conversion, cropping, cross-fades

## Feedback
