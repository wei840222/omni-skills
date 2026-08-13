---
name: influencer
description: Create, manage, and scale AI-generated virtual influencers. Define consistent characters, generate multi-platform content, and execute monetization workflows. Use when the user wants to launch or operate a virtual influencer persona.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⭐"}'
---

## State location

Influencer state may exist in `<workspace>/influencer/`, `<workspace>/memory/influencer/`, or `~/influencer/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/influencer/`, `<workspace>/memory/influencer/`, `~/influencer/`.
3. If multiple candidate directories exist, use the highest-priority one, keep the others independent, and tell the user which location was selected.
4. If none exists and the user asks to save influencer state, default to `<workspace>/influencer/`.

Use the selected `<state_root>` for every state operation in this skill. Treat legacy locations as migration sources only: propose a copy, validation, cutover, and rollback plan before any migration; do not move or delete existing state automatically.

## Workspace Structure

Each influencer lives in a dedicated folder:
```
<state_root>/
├── {persona-slug}/
│   ├── identity.md        # Name, niche, voice, personality
│   ├── reference/         # Base images for consistency
│   │   ├── face-ref-1.png
│   │   └── style-guide.md
│   ├── content/
│   │   ├── photos/        # Generated images by date
│   │   └── videos/        # Generated videos by date
│   ├── captions.md        # Caption templates, hashtags
│   ├── schedule.md        # Posting schedule
│   └── analytics.md       # Performance tracking
└── tools.md               # Configured generation tools
```

## Consent and publication boundary

Drafting personas, captions, schedules, and local state is reversible. Before creating a paid provider account, uploading source media, training or cloning a voice, signing a brand agreement, scheduling content, or publishing to a platform, show the target, data that will leave the workspace, cost or contractual commitment, and request explicit confirmation. Use only fully synthetic identities or source media, likenesses, and voices for which the user has documented rights and consent.

---

## Quick Reference

| Task | Load |
|------|------|
| Create new persona (identity, niche, aesthetics) | `references/persona.md` |
| Generate consistent photos | `references/image-gen.md` |
| Generate videos (talking head, lifestyle) | `references/video-gen.md` |
| Voice and audio (TTS, voice cloning) | `references/voice.md` |
| Content strategy and captions | `references/content.md` |
| Platform optimization (IG, TikTok, YT) | `references/platforms.md` |
| Monetization (brand deals, affiliates) | `references/monetization.md` |
| Legal and disclosure requirements | `references/compliance.md` |

---

## Persona Creation Checklist

Before generating any content:
- Define niche (fitness, lifestyle, tech, fashion, etc.)
- Create identity document (name, age, location, backstory)
- Generate 5-10 reference images for face consistency
- Define visual style (lighting, colors, settings)
- Create voice profile (if using TTS/videos)
- Draft personality guidelines for captions

---

## Character Consistency Rules

Maintaining the same face/body across all content is CRITICAL.

**For photos:**
1. Generate base reference set first (5-10 images, multiple angles)
2. Use IP-Adapter or InstantID for every generation
3. Same seed + similar prompt structure = more consistency
4. Quality check EVERY image before posting

**For videos:**
1. Use face-swap on real footage OR
2. Generate with character LoRA if trained OR
3. Talking head tools (HeyGen, D-ID) with reference image

---

## Content Generation Flow

1. **Plan** — Check `<state_root>/{persona-slug}/schedule.md` for what's needed today
2. **Generate** — Use appropriate tool (see `references/image-gen.md` or `references/video-gen.md`)
3. **Review** — Verify character consistency, quality
4. **Caption** — Write engaging copy matching persona voice
5. **Schedule** — Queue for optimal posting time
6. **Track** — Log in `<state_root>/{persona-slug}/analytics.md` after posting

---

## Common Patterns

| User says | Agent does |
|-----------|------------|
| "Create new influencer" | Draft the persona creation flow; create local state only when the user asks to save it |
| "Generate photos for today" | Check schedule, generate with consistency refs |
| "Make a TikTok video" | Generate 9:16 video with talking head or lifestyle footage |
| "Write captions for these" | Draft captions matching persona voice + niche hashtags |
| "How is she performing?" | Summarize analytics.md, suggest improvements |
| "Add brand deal content" | Draft sponsored content and disclosure; request confirmation before any external send or post |

---

## Tool Configuration

Store active tools in `<state_root>/tools.md`:

```markdown
## Active Tools
- Image: Nano Banana Pro (Gemini)
- Video: Kling / Runway
- Voice: ElevenLabs (voice_id: xxx)
- Lip Sync: HeyGen
```

Update when switching providers. All generation scripts read from here.
