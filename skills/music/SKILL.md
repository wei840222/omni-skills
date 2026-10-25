---
name: music
description: Track and organize music discoveries, favorites, concerts, and playlists. Use when the user shares a song or album to save, asks for music recommendations from their collection, wants a mood or activity playlist, or mentions a concert to log. Route original songwriting to `song`, AI music generation prompts to `music-generation`, and raw audio processing to `audio`.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🎵"}'
---

## State location

Resolve `<state_root>` before reading or writing music data:

1. Use a host- or user-configured music-state path when one is explicitly supplied.
2. Otherwise use the first existing directory in this order: `<workspace>/music/`, `<workspace>/memory/music/`, then `~/music/`.
3. If none exists and the user asks to persist music data, create `<workspace>/music/`.

Use only the selected `<state_root>` for this invocation. Do not hardcode absolute paths. If more than one candidate exists, use the highest-precedence directory and report the conflict; keep the directories separate rather than merging or moving data.

## Quick Reference

| Resource | Description | When to load |
|----------|-------------|--------------|
| `references/domain-knowledge.md` | Mood-regulation, concert-memory, and curation principles with sources. | When recommending, organizing playlists, or explaining why a tracking choice helps. |
| `assets/data-templates.md` | Markdown templates for discovery, favorites, playlists, concerts, collection, and memories. | When creating or updating files under `<state_root>/`. |

## Core Behavior

- **Save Music:** When the user shares a song or album, offer to save it with discovery context (who/where/when), mood or activity fit, and a later rating slot.
- **Recommend Music:** When the user asks for music, inspect `<state_root>/favorites/` and `<state_root>/playlists/` first; recommend inside demonstrated genres and moods.
- **Track Concerts:** When the user mentions a concert, log it in `<state_root>/concerts/upcoming.md` or create an attended note under `<state_root>/concerts/attended/`.
- **Confirm Context:** Ask for the target mood or activity before generating a new playlist when that context is missing.

## File Structure

```text
<state_root>/
├── discover/
│   └── to-listen.md
├── favorites/
│   ├── songs.md
│   ├── albums.md
│   └── artists.md
├── playlists/
│   ├── workout.md
│   ├── focus.md
│   └── road-trip.md
├── concerts/
│   ├── upcoming.md
│   └── attended/
├── collection/
│   └── vinyl.md
└── memories/
    └── YYYY.md
```

## Track Entry Requirements

When logging a new entry, include when known:

- Song/album/artist name
- How discovered (who, where, when)
- Context (mood it fits, activity)
- Rating after listening
- Standout tracks on albums

## Artist Deep Dives

When the user discovers an artist they love:

- Map discography chronologically.
- Note fan-favorite albums.
- Flag essential tracks for sampling.
- Track which albums have been explored vs pending.

## By Mood/Activity Guidelines

- **Workout:** High energy, tempo roughly 120+.
- **Focus:** Instrumental, ambient, lo-fi.
- **Cooking:** Upbeat, familiar favorites.
- **Sad hours:** Cathartic, emotional.
- **Party:** Crowd-pleasers, danceable.
- **Road trip:** Singalongs, classics.

## Surfacing Context

Actively surface saved content when relevant:

- "You saved that album months ago and still have not listened."
- "An artist you like is touring near you."
- "Last time you needed focus music you liked Tycho."
- "This sounds like artists already in your favorites."

## Progressive Enhancement

- **Week 1:** Capture current favorite songs/albums.
- **Ongoing:** Save discoveries with their source.
- **Over time:** Build mood-based playlists and log attended concerts.

## Required Operating Principles

- **Platform Agnostic:** Stay independent of specific streaming platforms unless the user explicitly provides an integration.
- **Respect Preferences:** Recommend only within genres and moods the user has shown interest in.
- **Maintain Simplicity:** Keep organization structures flat and rely on simple markdown lists.
- **No Forced Logging:** Offer to save; do not invent listening history the user did not confirm.
- **Privacy:** Treat music taste, concert plans, and personal notes as private state under `<state_root>/`.

## Failure Modes

- Missing mood/activity for a playlist request → ask one clarifying question before writing a new playlist file.
- Empty or missing `<state_root>` collection → say so, then offer to start with favorites or a discovery queue.
- Conflicting candidate state directories → keep the highest-precedence tree and report the conflict.
- User asks for composition or audio engineering → hand off to `song`, `music-generation`, or `audio`.

## Anti-Patterns

- Do not invent a listening history, rating, or concert attendance the user did not confirm.
- Do not push a streaming-platform signup or paid catalog sync when local markdown tracking is enough.
- Do not dump the entire favorites archive when a single mood-matched suggestion answers the request.
- Do not treat a missing playlist file as failure; offer to create one after confirming context.

