---
name: influencer
description: Create, manage, and scale AI-generated virtual influencers. Define consistent characters, generate multi-platform content, and execute monetization workflows. Use when the user wants to launch or operate a virtual influencer persona.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⭐"}'
---

## State location

Influencer state may exist in `$WORKSPACE/influencer/`, `$WORKSPACE/memory/influencer/`, or `~/influencer/`.
Before reading or writing state, resolve `$STATE_ROOT` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `$WORKSPACE/influencer/`, `$WORKSPACE/memory/influencer/`, `~/influencer/`.
3. If none exists and state must be created, default to `$WORKSPACE/influencer/`.

Use the selected `$STATE_ROOT` for every state operation in this skill.

## Workspace Structure

Each influencer lives in a dedicated folder:
```
$STATE_ROOT/
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

1. **Plan** — Check `$STATE_ROOT/{persona-slug}/schedule.md` for what's needed today
2. **Generate** — Use appropriate tool (see `references/image-gen.md` or `references/video-gen.md`)
3. **Review** — Verify character consistency, quality
4. **Caption** — Write engaging copy matching persona voice
5. **Schedule** — Queue for optimal posting time
6. **Track** — Log in `$STATE_ROOT/{persona-slug}/analytics.md` after posting

---

## Common Patterns

| User says | Agent does |
|-----------|------------|
| "Create new influencer" | Run persona creation flow, set up workspace |
| "Generate photos for today" | Check schedule, generate with consistency refs |
| "Make a TikTok video" | Generate 9:16 video with talking head or lifestyle footage |
| "Write captions for these" | Draft captions matching persona voice + niche hashtags |
| "How is she performing?" | Summarize analytics.md, suggest improvements |
| "Add brand deal content" | Generate sponsored content with disclosure |

---

## Tool Configuration

Store active tools in `$STATE_ROOT/tools.md`:

```markdown
## Active Tools
- Image: Nano Banana Pro (Gemini)
- Video: Kling / Runway
- Voice: ElevenLabs (voice_id: xxx)
- Lip Sync: HeyGen
```

Update when switching providers. All generation scripts read from here.
