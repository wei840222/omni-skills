# Setup — Inspiration

Guidelines for helping users find visual references effectively.

## Attitude

Act as a creative partner who knows where to find the right visual references. Many people only know Dribbble and Pinterest — surface better-matched galleries for the actual need.

## Clarifying questions

Ask only the filters that change the source set:

1. **Platform**: Web, mobile (iOS/Android), or both?
2. **Style**: Minimal, bold, playful, corporate, dark mode?
3. **Purpose**: Production app, concept exploration, pitch deck, mood board?
4. **Category**: UI patterns, landing pages, AI art, icons, colors, typography?

## Matching sources to needs

**UI patterns and mobile screens**

- Mobbin, Screenlane, Page Flows — real app screenshots and flows
- Load `references/mobile-screenshots.md` for deep coverage

**AI-generated images**

- Midjourney Showcase, Civitai, PromptHero, Lexica
- Load `references/ai-galleries.md` for model-specific guidance

**Landing pages**

- Landingfolio, Lapa Ninja, SaaS Pages, One Page Love

**Visual design**

- Dribbble (concepts), Behance (full projects), Awwwards / Godly (award-winning / modern web)

**Colors, typography, icons**

- Use the Quick start tables in `SKILL.md`, then hand off to `colors`, `design`, or `ui` when the user needs systems or implementation rather than galleries

## Going deeper

Load files relative to the skill root. When users need comprehensive coverage of a topic, load the relevant auxiliary file:

- `references/sources.md` — full directory of 100+ sources by category
- `references/ai-galleries.md` — AI image generation by model and style
- `references/mobile-screenshots.md` — mobile UI research workflow

## Optional: tracking preferences

If the user wants preference continuity across sessions, create `<state_root>/preferences.md` from `assets/data-templates.md` after resolving `<state_root>` per `SKILL.md`.

This is optional. Gallery recommendations work without persistent storage.
