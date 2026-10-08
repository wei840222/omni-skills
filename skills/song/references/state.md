# Storage and preferences

Resolve `<state_root>` from `SKILL.md` before any read or write. Outside that resolver section, every runtime path uses `<state_root>/...`.

## Tree

```text
<state_root>/
├── drafting/                   # Active song drafts
│   └── {song-name}/
│       ├── current.md          # Read this first for the active draft
│       ├── versions/           # v001.md, v002.md, ...
│       ├── notes.md            # Ideas, inspiration, fragments
│       └── prompts.md          # AI generator prompts tried
├── released/                   # Finished songs the user marked complete
│   └── {song-name}/
│       ├── final.md            # Final lyrics + chords
│       └── meta.md             # Genre, key, BPM, notes
└── preferences.md              # User style preferences
```

| Path | Role | Creation condition |
| --- | --- | --- |
| `<state_root>/preferences.md` | Genre, rhyme, vocabulary, themes, liked progressions, exclusions | Create when the user wants continuity across songs |
| `<state_root>/drafting/{song-name}/current.md` | Active draft snapshot | Create when a named draft begins |
| `<state_root>/drafting/{song-name}/versions/vNNN.md` | Immutable history copies | Create before each material rewrite of `current.md` |
| `<state_root>/drafting/{song-name}/notes.md` | Fragments and inspiration | Create when loose ideas appear |
| `<state_root>/drafting/{song-name}/prompts.md` | Generator prompts already tried | Create when AI prompts are iterated |
| `<state_root>/released/{song-name}/final.md` | User-accepted final lyric/chord sheet | Create only when the user marks the song released |
| `<state_root>/released/{song-name}/meta.md` | Genre, key, BPM, release notes | Create with the released package |

Optional children are created only when needed. Do not pre-expand empty trees.

## Version rule

Before a material edit of an active draft:

1. Copy `current.md` into `versions/` with the next `vNNN` index.
2. Edit the new working copy.
3. Replace `current.md` with the updated draft.

Keep prior versions readable so the user can roll back a lyric or form choice.

## Learning user preferences

Track in `<state_root>/preferences.md` when the user opts into continuity:

- genres they gravitate toward
- rhyme strictness (tight vs loose)
- vocabulary style (poetic vs conversational)
- themes that resonate
- progressions they liked
- patterns to exclude (overused clichés they rejected)

Update after each song based on their feedback. Leave the file untouched when the user wants a one-off draft with no memory.
