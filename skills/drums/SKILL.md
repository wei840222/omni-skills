---
name: drums
description: Provide drum practice strategies, technique correction, groove development, rudiment progression, and session logging. Use when the user is learning drums, asks for practice plans, kit setup, fill/tempo fixes, rudiment goals, or progress tracking. Route listening discovery to `music`, piano practice to `piano`, and guitar practice to `acoustic-guitar` or `electric-guitar`.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🥁"}'
  related-skills: '{"music":"Track listening history, playlists, and concerts rather than drum practice technique.","piano":"Keyboard practice plans and technique instead of drum kit work.","acoustic-guitar":"Acoustic guitar practice and repertoire instead of drums.","electric-guitar":"Electric guitar practice and gear instead of drums.","habits":"Design the recurring practice habit once the drum routine itself is clear."}'
---

## When to load

Load this skill for drum-kit practice coaching, technique diagnosis, rudiment tempo goals, groove-vs-chops decisions, electronic vs acoustic kit setup, hearing protection, and logging sessions under the drums workspace.

Do not load as the primary skill for general music discovery, piano/guitar practice, or whole-life habit design without a drum-specific ask.

## State location

Resolve `<state_root>` before reading or writing drum practice data:

1. Use a host- or user-configured drums-state path when one is explicitly supplied.
2. Otherwise use the first existing directory in this order: `<workspace>/drums/`, `<workspace>/memory/drums/`, then `~/drums/`.
3. If none exists and the user asks to persist practice data, create `<workspace>/drums/`.

Use only the selected `<state_root>` for this invocation. Do not hardcode absolute paths or write the literal string `<state_root>` to disk. If more than one candidate exists, use the highest-precedence directory and report the conflict; keep the directories separate rather than merging or moving data.

```text
<state_root>/
├── repertoire.md      # Songs learned and in progress
├── sessions/
│   └── YYYY-MM.md     # Monthly practice logs
├── rudiments.md       # Tempo tracking per rudiment
└── goals.md           # Short and long-term goals
```

## Core behavior

- On first interaction that needs persistence, create the workspace tree under the resolved `<state_root>/`.
- After practice, offer to log the session; load `references/progress.md` before writing logs or updating repertoire/rudiments/goals.
- Load `references/technique.md` before diagnosing form, fills, kit setup, or level-specific mistakes.
- Load `references/sources.md` when explaining why a practice default exists (motor learning, hearing safety, rudiment vocabulary).
- Before advising, ask kit type (acoustic vs electronic), level/context, and goals (rock, jazz, session, hobby).
- Prioritize groove, timing stability with a click, weak-hand development, dynamics/ghost notes, and hearing protection.
- Surface progress proactively from logs (for example, "Paradiddles 90 last month — push to 100?").

## Progressive disclosure

| Resource | When to load |
|----------|--------------|
| `references/technique.md` | Form errors, rudiment priority, groove vs chops, troubleshooting, electronic kits, hearing |
| `references/progress.md` | Workspace layout, repertoire/session/rudiment/goal formats, logging triggers |
| `references/sources.md` | Pedagogy and safety sources behind defaults |

## Safety

- Hearing damage is permanent — default to hearing protection around **-15 dB** attenuation for practice and live volume.
- Stop and reassess grip/posture when wrists, forearms, or shoulders hurt; do not push through pain for tempo gains.
