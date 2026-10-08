# Sources (Gate 6)

Full URLs verified or used while refactoring this skill. Re-check live pages before restating product feature matrices, plan tiers, or third-party pricing.

## Agent Skills format

| Source | URL | Use |
| --- | --- | --- |
| Agent Skills specification | https://agentskills.io/specification | Package format, progressive disclosure, metadata shape |
| Best practices for skill creators | https://agentskills.io/skill-creation/best-practices | Scope and calibration |
| Optimizing skill descriptions | https://agentskills.io/skill-creation/optimizing-descriptions | Trigger-rich descriptions |
| Reference validator (`skills-ref`) | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate` |

## Song form and craft (stable domain)

| Source | URL | Notes |
| --- | --- | --- |
| Wikipedia — Song structure | https://en.wikipedia.org/wiki/Song_structure | Common commercial forms (verse, chorus, bridge, pre-chorus); treat as orientation, not a rigid standard |
| Wikipedia — Thirty-two-bar form (AABA) | https://en.wikipedia.org/wiki/Thirty-two-bar_form | AABA jazz/standard form reference |
| Wikipedia — Strophic form | https://en.wikipedia.org/wiki/Strophic_form | AAA / verse-repeating storytelling forms |
| Open Music Theory — Harmonic function primer | https://viva.pressbooks.pub/openmusictheory/chapter/harmonic-function/ | Practical functional harmony language for non-academic coaching |

## Lyric and prosody practice (stable domain)

| Source | URL | Notes |
| --- | --- | --- |
| Purdue OWL — Literary devices overview | https://owl.purdue.edu/owl/general_writing/creative_writing/index.html | Metaphor/imagery craft transferable to lyrics; keep examples user-owned |
| Soundtrap — Song structure basics (education blog) | https://www.soundtrap.com/learning/blog/song-structure | Accessible section-length intuition; re-check if citing specific bar counts as universal law |

## AI music generators (version-sensitive)

| Source | URL | Notes (refactor-time) |
| --- | --- | --- |
| Suno | https://suno.com/ | Consumer AI song generation; features and plan limits change — re-check before promising stems, commercial rights, or clip length |
| Udio | https://www.udio.com/ | Consumer AI song generation; same caution on rights and feature matrices |
| Stable Audio (Stability) | https://www.stableaudio.com/ | Stronger fit for instrumentals / sound design than full vocal pop workflows |

## Claims discipline

- Bar counts and BPM→duration tables in `structure.md` / `phases.md` are **rules of thumb** at ~120 BPM, not genre law.
- Chord tables in `harmony.md` are pedagogical starting points; voice-leading and key context still matter.
- Generator section tags in `prompts.md` are community/prompt-craft conventions observed across Suno/Udio-style workflows; they are not an official API schema. Prefer live product docs when the user needs provider-accurate behavior.
- Do not invent pricing, commercial-license terms, or model version numbers from memory.
