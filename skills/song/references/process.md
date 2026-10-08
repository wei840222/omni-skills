# Process summary

1. **Discovery** — Genre, mood, theme, inspiration. Load `<state_root>/preferences.md` when present (`phases.md`).
2. **Structure** — Choose form (verse-chorus-bridge, AABA, etc.). Define section lengths (`structure.md`).
3. **Lyrics** — Draft section by section. Check rhyme, meter, emotional arc (`lyrics.md`).
4. **Harmony** — Suggest progressions matching mood/genre (`harmony.md`).
5. **Polish** — Review singability, hook strength, flow. Iterate with the user.
6. **Generate** — Prepare AI music prompts with section/style tags when requested (`prompts.md`), then hand off provider execution to `music-generation` or `suno` if the user needs audio delivery.
