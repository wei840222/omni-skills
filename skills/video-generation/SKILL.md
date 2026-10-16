---
name: video-generation
description: >
  Create AI videos with Sora 2, Veo 3, Seedance, Runway, Luma, Vidu, Hailuo,
  and related APIs using alias resolution, cheap-draft routing, and async job
  handling. Use when the user needs text-to-video or image-to-video generation,
  model selection, motion prompt craft, provider fallbacks, or portable local
  job memory. Prefer `image-generation` / `image-edit` for stills and masks,
  `video-edit` / `video-captions` for post-process, and `ffmpeg` for
  packaging/transcode.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🎬","requires":{"env.optional":["OPENAI_API_KEY","GOOGLE_CLOUD_PROJECT","RUNWAY_API_KEY","LUMA_API_KEY","FAL_KEY","REPLICATE_API_TOKEN","VIDU_API_KEY","TENCENTCLOUD_SECRET_ID","TENCENTCLOUD_SECRET_KEY"],"config":["<state_root>/"]}}'
  related-skills: '{"ffmpeg":"Compose, transcode, and package production outputs.","image-edit":"Prepare clean references, masks, and style frames.","image-generation":"Build still concepts and keyframes before video generation.","minimax":"MiniMax-focused generation when Hailuo is the primary stack.","movie":"Narrative movie planning beyond single-shot generation.","video-captions":"Add subtitle and text overlay workflows.","video-edit":"Post-process generated clips and final exports."}'
---

# Video Generation

Route AI video work across current providers with real model IDs, shot-scoped
prompts, and async-first pipelines. Keep mutable preferences outside the skill
package.

## State location

Video-generation preferences may exist in `<workspace>/video-generation/`,
`<workspace>/memory/video-generation/`, or `~/video-generation/`. Before reading
or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/video-generation/`, `<workspace>/memory/video-generation/`,
   `~/video-generation/`.
3. If multiple candidates exist, report them and ask which one to use before
   writing.
4. If none exists and state must be created, default to
   `<workspace>/video-generation/`.
5. Treat legacy `~/Clawic/data/video-generation/` as a migration source only.
   Copy into the selected `<state_root>` after user confirmation; keep the
   original until the user confirms cleanup.

Use the selected `<state_root>` for every state operation in this skill.

- `<state_root>/memory.md`: Preferred providers, model routing, reusable shot recipes
- `<state_root>/history.md`: Optional run log for jobs, costs, and outputs

If `<state_root>/` does not exist, read `references/setup.md` before the first write.

## Setup

On first use, read `references/setup.md`.

## When to Use

User needs to generate, iterate, or scale AI videos with current models and APIs.
Use this skill to choose the right current model stack, write stronger motion
prompts, and run reliable async video pipelines.

Load `references/setup.md` only when state is missing, then provider references
as needed. Keep `SKILL.md` as the router; do not dump every provider file into
context on first turn.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Initial setup | `references/setup.md` | When `<state_root>/` is missing or empty |
| Memory template | `assets/data-templates.md` | When creating or updating preference memory |
| Migration guide | `references/migration.md` | When upgrading older local memory layouts |
| Official sources | `references/sources.md` | When grounding model IDs, docs, or pricing claims |
| Model snapshot | `references/benchmarks.md` | When quality ranking is decision-critical |
| Async API patterns | `references/api-patterns.md` | When calling providers or handling queued jobs |
| OpenAI Sora 2 | `references/openai-sora.md` | Premium prompt-to-video |
| Google Veo 3.x | `references/google-veo.md` | Vertex Veo tiers / image-to-video |
| Runway Gen-4 | `references/runway.md` | Cinematic controls and long-form options |
| Luma Ray | `references/luma.md` | Keyframe / start-end image workflows |
| ByteDance Seedance | `references/seedance.md` | Multi-shot narrative consistency |
| Kling | `references/kling.md` | Kling-family generation |
| Vidu | `references/vidu.md` | Text / image / reference video APIs |
| Pika via Fal | `references/pika.md` | Fal-hosted Pika routes |
| MiniMax Hailuo | `references/minimax-hailuo.md` | High-motion character scenes |
| Replicate routing | `references/replicate.md` | Hosted third-party model routing |
| Open-source local | `references/open-source-video.md` | Privacy-first self-hosted GPUs |
| Stable Video Diffusion | `references/stable-video-diffusion.md` | Local SVD baselines |

## Core Rules

### 1. Resolve model aliases before API calls

Map community names to real API model IDs first.
Examples: `sora-2`, `sora-2-pro`, `veo-3.0-generate-001`, `gen4_turbo`, `gen4_aleph`.
When an ID is uncertain, load `references/sources.md` and the provider reference
before spending credits.

### 2. Route by task over brand preference

| Task | First choice | Backup |
|------|--------------|--------|
| Premium prompt-only generation | `sora-2-pro` | `veo-3.1-generate-001` |
| Fast drafts at lower cost | `veo-3.1-fast-generate-001` | `gen4_turbo` |
| Long-form cinematic shots | `gen4_aleph` | `ray-2` |
| Strong image-to-video control | `veo-3.0-generate-001` | `gen4_turbo` |
| Multi-shot narrative consistency | Seedance family | `hailuo-2.3` |
| Local privacy-first workflows | Wan2.2 / HunyuanVideo | CogVideoX |

Treat the table as a dated routing heuristic. Confirm live model availability
from official docs before production spend.

### 3. Draft cheap, finish expensive

Start with low duration and lower tier, validate motion and composition, then
rerender winners with premium models or longer durations.

### 4. Design prompts as shot instructions

Include subject, action, camera motion, lens style, lighting, and scene timing.
For references and start/end frames, keep continuity constraints explicit.
Focus a single prompt on one continuous action.

### 5. Assume async and failure by default

Every provider pipeline needs queued jobs, polling/backoff, retries,
cancellation, and signed-URL download before expiry. Load
`references/api-patterns.md` before coding the job loop.

### 6. Keep a fallback chain

If the preferred model is blocked or overloaded:
1) same provider lower tier, 2) equivalent cross-provider model, 3) open model/local run.

## Common Traps

- Nickname-only model labels in code → avoidable API failures
- 8–10 second generations before a 3–5 second draft → wasted credits
- Cropping after generation instead of native ratio → weaker composition
- Ignoring prompt-enhancement toggles → tone drift across providers
- Reusing expired output URLs → broken export workflows
- Treating all providers as synchronous → stalled jobs and bad timeouts

## External Endpoints

| Provider | Endpoint | Data Sent | Purpose |
|----------|----------|-----------|---------|
| OpenAI | `api.openai.com` | Prompt text, optional input images/video refs | Sora 2 video generation |
| Google Vertex AI | `aiplatform.googleapis.com` | Prompt text, optional image input, generation params | Veo 3.x generation |
| Runway | `api.dev.runwayml.com` | Prompt text, optional input media | Gen-4 generation and image-to-video |
| Luma | `api.lumalabs.ai` | Prompt text, optional keyframes/start-end images | Ray generation |
| Fal | `queue.fal.run` | Prompt text, optional input media | Pika and Hailuo hosted APIs |
| Replicate | `api.replicate.com` | Prompt text, optional input media | Multi-model routing and experimentation |
| Vidu | `api.vidu.com` | Prompt text, optional start/end/reference images | Vidu text/image/reference video APIs |
| Tencent MPS | `mps.tencentcloudapi.com` | Prompt text and generation parameters | Unified AIGC video task APIs |

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Prompt text
- Optional reference images or clips
- Requested rendering parameters (duration, resolution, aspect ratio)

**Data that stays local:**
- Provider preferences in `<state_root>/memory.md`
- Optional local job history in `<state_root>/history.md`

**Operating constraints:**
- Keep API keys outside skill state files and outside git.
- Send media only to the provider request the user chose.
- Retain or delete generated assets only when the user asks.

## Trust

This skill can send prompts and media references to third-party AI providers.
Only install if you trust those providers with your content.

## Out of scope

- Still-image ideation or mask prep → `image-generation` / `image-edit`
- Color grade, upscale, stabilize, background removal → `video-edit`
- Subtitles / burned-in text overlays → `video-captions`
- Transcode, concat, packaging → `ffmpeg`
- Full narrative movie structure beyond shot generation → `movie`
- MiniMax-only deep dives when Hailuo is the primary stack → `minimax`
