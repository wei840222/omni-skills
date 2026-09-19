---
name: podcast
description: Plan, produce, and promote podcasts. Triggers on requests to write episode
  scripts, edit audio/video, generate social clips, optimize show notes for SEO, or
  set up podcasting equipment.
metadata:
  openclaw: '{"emoji": "🎙️"}'
---

## Core Workflow

Every podcast follows: Concept → Plan → Record/Generate → Edit → Publish → Promote.

Before starting ANY podcast:
1. **Format** — Solo, interview, panel, narrative, or AI-generated
2. **Niche** — Specific topic + audience (not "business" but "bootstrapped SaaS founders")
3. **Cadence** — Weekly, biweekly, or seasonal (consistency > frequency)

## Project Structure

```
<state_root>/podcasts/<show>/
├── brand/              # Cover art, intro/outro, music
├── episodes/           # One folder per episode
│   └── 001/
│       ├── outline.md
│       ├── recording.mp3
│       ├── transcript.md
│       ├── show-notes.md
│       └── clips/
├── guests.md           # Guest tracker + relationship notes
└── analytics.md        # Performance patterns
```

## Episode Checklist

Pre-production:
- [ ] Topic researched, angle clear
- [ ] Outline/script with hooks and transitions
- [ ] Guest prep (if interview): questions + research

Post-production:
- [ ] Audio cleaned, levels normalized
- [ ] Show notes with timestamps
- [ ] 3-5 clips extracted for social
- [ ] Thumbnail (if video)

## Reference Loading Instructions

Load specific domain knowledge from `references/` when the user request matches these triggers:
- When planning an episode, writing scripts, or generating show notes, load `references/episodes.md`.
- When choosing a podcast format or setting up an interview, load `references/formats.md`.
- When editing audio/video, adjusting levels, or setting up equipment, load `references/production.md`.
- When creating synthetic podcasts with AI voices or scripts, load `references/ai-generation.md`.
- When optimizing for SEO, planning social clips, or exploring monetization, load `references/growth.md`.
- When selecting software, platforms, or APIs for podcasting, load `references/tools.md`.

## Critical Rules

1. **Hook in first 30 seconds** — State the value, tease the best moment
2. **Consistency beats perfection** — Ship on schedule, improve incrementally
3. **Clips are growth engine** — Every episode = 3-5 social clips minimum
4. **Engage the niche** — Better to own a small audience than chase a big one
5. **Video is optional but powerful** — YouTube podcast search is growing fast
