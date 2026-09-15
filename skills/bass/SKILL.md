---
name: bass
description: Provide bass guitar practice strategies, groove development, technique
  correction, and session progress tracking. Use when the user is learning bass,
  improving rhythm/pocket, fixing slap or fingerstyle technique, or logging practice.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji": "🎸"}'
  related-skills:
    music: skills/music
---

## When to load references

- `references/progress.md`: Load before logging practice, updating repertoire, technique notes, or goals.
- `references/sources.md`: Load for pedagogy and groove-source notes behind practice defaults.

## Core Behavior

- Create `<state_root>/bass/` as workspace on first interaction.
- After practice sessions, offer to log progress.
- Before suggesting grooves or slap work, check current repertoire and technique notes when available.
- Load `references/progress.md` before writing repertoire, sessions, technique, or goals files.

## Before Advising

- Ask style — rock vs funk vs jazz vs metal differ hugely
- Ask technique — fingers vs pick vs slap
- Ask gear — active vs passive, 4 vs 5 string

## Practice Defaults

| Default | Why |
|---------|-----|
| Always use a metronome / click | Bass carries time; unguided tempo drift becomes band-time drift |
| Leave space; rests are groove | Constant note density flattens pocket and fights the kick |
| Mute unused strings | String noise ruins recordings and live clarity |
| Feel volume more than force | Bass is felt; excess pluck volume often muddies the mix |

## Technique Defaults

| Default | Why |
|---------|-----|
| Lighter pluck, let amp work | Harder attack often dirties tone before it adds punch |
| Minimum fretting pressure | Excess tension slows shifts and invites injury |
| Floating thumb on 5-string when needed | Anchored thumb can block low-B access and mute duty |
| Vary dynamics deliberately | Flat dynamics make lines feel lifeless |

## Mistakes by Level

**Beginners:** Racing the drummer, failing to lock with kick, no muting

**Intermediate:** Overplaying, ignoring roots, slap without groove

**Advanced:** Too busy for the song, neglecting simple supportive lines

## Groove Fundamentals

| Concept | Why |
|---------|-----|
| Lock with kick drum | Creates the pocket and rhythmic foundation of the song |
| Ghost notes | Adds percussive feel and syncopation without cluttering harmony |
| Note length | Staccato vs legato defines feel more than note choice |
| Dynamics | Quiet-to-loud range creates emotional contour |

## Fretboard Knowledge

- Learn note names, not only visual shapes — say names while playing
- Prefer arpeggios/chord tones over scale runs for song support
- Know the same line in multiple positions

## Troubleshooting

- "Struggling to sit in mix" → EQ: cut competing mids or boost useful low-mids
- "Lines boring" → ghost notes, vary note length, widen dynamics
- "Can't lock with drums" → practice to kick only
- "Slap weak" → strike through the string for power instead of bouncing off

## Slap Basics

- Thumb through the string (Victor Wooten-style power) rather than bounce-only motion
- Muting with fretting hand and right-hand palm is ~50% of clean slap tone
- Prioritize groove and metronome timing before speed or flashy fills

## Gear

Tone starts in the hands — setup and technique matter more than brand chasing.

## Progress Tracking

Log to `<state_root>/bass/`: songs, techniques, groove exercises. Use `references/progress.md` formats.

## What to Surface

- "Slap logged — want ghost-note drills?" / "5 rock songs — try a funk pocket next?"
