---
name: song
description: >
  Write original songs with guided discovery, structure, lyrics, chord progressions,
  melody contours, and AI music-generator prompts (Suno/Udio-style tags). Use when
  the user wants to compose, finish a hook, draft verses/chorus/bridge, pick a form
  (verse-chorus, AABA), or prepare generation prompts. Not for curating listening
  history (`music`), end-to-end AI audio generation workflows (`music-generation` /
  `suno`), local audio file processing (`audio`), or long-form prose craft (`writing`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎵"}'
  related-skills: '{"music":"Track discoveries, playlists, and concerts rather than compose.","music-generation":"Run multi-provider AI generation once composition intent is clear.","suno":"Suno-specific generation, credits, and delivery when the user targets that product.","audio":"Process local audio/video files with FFmpeg rather than write songs.","writing":"General prose voice craft outside lyric meter and song form."}'
---

# Song

Pre-production songwriting skill for **lyrics, form, harmony suggestions, and generator prompts**. It keeps optional drafts and taste preferences under portable `<state_root>` only; the skill package stays read-only.

## State location

Song drafts and preferences may exist in `<workspace>/song/`, `<workspace>/memory/song/`, or `~/song/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/song/`, `<workspace>/memory/song/`, `~/song/`.
3. If none exists and state must be created, default to `<workspace>/song/`.

Use the selected `<state_root>` for every state operation in this skill. If more than one candidate exists, keep the highest-precedence directory, report the conflict, and leave the others untouched. Do not invent listening history or finished songs the user did not confirm.

## When to load

- original lyrics, hooks, verses, chorus, bridge, or full song drafts
- form/structure choices (verse-chorus, AABA, strophic, freeform)
- mood-matched chord progressions and simple contour notes
- Suno/Udio-style section tags and style prompts for later generation
- learning the user's songwriting preferences across sessions

Hand off when a sibling owns the job:

| Job | Skill |
| --- | --- |
| Save albums/playlists/concerts | `music` |
| Multi-provider AI generation end-to-end | `music-generation` |
| Suno plan, credits, API/browser delivery | `suno` |
| Convert/normalize local audio files | `audio` |
| Non-lyric prose voice rewrite | `writing` |

## Core path

1. **Resolve state** — load `<state_root>/preferences.md` when present before inventing a new voice.
2. **Discovery** — mood, genre, theme, reference vibe, vocal perspective, tempo feel (`references/phases.md`).
3. **Structure** — pick a form and section lengths before long lyric dumps (`references/structure.md`).
4. **Lyrics** — section by section; check rhyme, meter, and emotional arc (`references/lyrics.md`).
5. **Harmony** — suggest progressions that match mood/genre; keep theory practical (`references/harmony.md`).
6. **Polish** — singability, hook strength, flow; offer iteration instead of declaring a song finished.
7. **Generate prompts** — only when the user wants AI audio; prepare tags via `references/prompts.md`, then hand off delivery to `music-generation` / `suno` if they need provider execution.

## Progressive disclosure

| Need | Load |
| --- | --- |
| Draft tree, versioning, preferences | `references/state.md` |
| Six-step process summary | `references/process.md` |
| Phase questions and section goals | `references/phases.md` |
| Lyric craft and emotional techniques | `references/lyrics.md` |
| Chord progressions by mood | `references/harmony.md` |
| Song form patterns and transitions | `references/structure.md` |
| Suno/Udio section and style tags | `references/prompts.md` |
| Verified sources and fragile claims | `references/sources.md` |

## Safety defaults

- Focus on **pre-production** (words, form, harmony, prompts); leave DAW mixing and mastering out of scope unless the user only needs a short practical note.
- Treat drafts, preferences, and unfinished lyrics as private state under `<state_root>/`.
- Suggest alternatives; keep the user's voice primary.
- Offer iteration; frame songs as improvable drafts rather than final seals.
- Re-check `references/sources.md` before restating product limits, generator feature matrices, or third-party pricing.
