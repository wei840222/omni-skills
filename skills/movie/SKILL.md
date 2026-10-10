---
name: movie
description: >
  Produce AI-assisted short films and commercial spots end-to-end: style bible,
  character sheets, shot lists, generation prompts, continuity checks, assembly,
  and polish. Use when the user wants a film/project workflow from script to
  final cut, multi-shot continuity, or production logging. Prefer
  `video-generation` for single-clip API calls, `video-edit`/`ffmpeg` for
  isolated transforms, `image-generation` for stills only, `video-captions` for
  subtitles alone, and `prompting` for generic prompt debugging outside film craft.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎬"}'
  related-skills: '{"video-generation":"Single-clip or API-centric generation once the shot is already specified.","video-edit":"Clip-level AI edit transforms outside full production logging.","ffmpeg":"Exact encode/concat/crop/LUT shell operations.","image-generation":"Still storyboard or character-sheet frames without motion.","video-captions":"Transcription, timing, styling, and burn-in only.","prompting":"Cross-model prompt failure diagnosis outside movie production structure."}'
---

# Movie

Own **AI film production workflows**: style bible, character continuity, shot lists, generation routing, assembly, and project logs—from concept through final cut—not one-off clip APIs.

## State location

Movie project trees may exist in `<workspace>/movies/`, `<workspace>/memory/movies/`, or `~/movies/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/movies/`, `<workspace>/memory/movies/`, `~/movies/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and state must be created, default to `<workspace>/movies/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/movies/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Do not treat the literal string `<state_root>` as a filesystem path. Do not write API keys, account cookies, or paid-provider credentials into project files. Do not write learned preferences into `SKILL.md`.

Default project layout (create on first authorized write):

```text
<state_root>/<project>/
├── script.md           # Source screenplay or treatment
├── style-bible.md      # Visual rules, references, palette
├── characters/         # Reference images per character
├── shots/              # Generated clips organized by scene
├── timeline.md         # Edit assembly order
└── status.md           # What's done, what needs work
```

If older project files exist only under a legacy path outside the candidate roots, offer a one-time migrate into the resolved `<state_root>/` and say in one line what moved; do not keep marketplace homepage links.

## Core behavior

- Establish style bible, character sheets, and shot list **before** bulk generation.
- Route tools by shot need; keep continuity higher priority than speed.
- Log prompts, takes, and failures under the project tree.
- Start with rough animatics; polish only approved shots.
- Defer single-clip provider minutiae to `video-generation`, encode math to `ffmpeg`, stills to `image-generation`, captions-only to `video-captions`.

## When the user starts or continues a film

1. Resolve `<state_root>` and identify or create `<state_root>/<project>/`.
2. Confirm whether a script/treatment, style bible, and character refs already exist.
3. If any foundation piece is missing, build it before new generation (see `references/domain.md`).
4. Break scenes into a shot list (`references/preproduction.md`) with duration and framing notes.
5. For each shot, select a generation path using `references/tools.md` **and** re-open vendor docs linked in `references/sources.md` before stating product limits, durations, or pricing.
6. Write prompts with locked style keywords (`references/generation.md`); attach character references.
7. After each take: continuity check vs refs, log outcome under `shots/`, reject broken continuity and re-generate.
8. Assemble with `timeline.md`; use `references/postproduction.md` for color/sound, `ffmpeg` skill for exact filters when needed.
9. Commercial cuts/localization → `references/commercial.md`. Experimental transitions → `references/experimental.md`.

## Failure and safety

- Missing style bible or character sheets: stop bulk generation; create foundations first.
- Continuity break (wardrobe, lighting, face): reject the take; re-generate with refs attached rather than “fix in post” as the default.
- Vendor capability/price/duration claims: treat model cards as time-sensitive; open `references/sources.md` URLs instead of inventing numbers.
- Secrets: never paste API keys into `script.md`, prompts logs shared externally, or git-tracked skill files.
- Scope pressure (feature-length): plan iteration counts honestly; do not promise hundreds of final shots in one pass.
- Tool outage or blocked host: record the blocker in `status.md` and offer a smaller offline path (storyboard stills, shot-list only).

## Progressive disclosure

Depth on demand—load only the reference required for the current step.

| Need | Load |
| --- | --- |
| Core workflow, checklists, critical rules | `references/domain.md` |
| Script breakdown and shot lists | `references/preproduction.md` |
| Prompt patterns by shot type | `references/generation.md` |
| Assembly, color, sound | `references/postproduction.md` |
| Model/tool routing heuristics | `references/tools.md` |
| Commercial versions and formats | `references/commercial.md` |
| Experimental transitions | `references/experimental.md` |
| Verified vendor and craft URLs | `references/sources.md` |
