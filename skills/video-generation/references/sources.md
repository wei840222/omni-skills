# Official Sources — Video Generation

Dated routing snapshot for Gate 6. Prefer these primary docs over community aliases.
Verified reachable over HTTPS on 2026-10-16 unless noted.

## Format authority

- Agent Skills specification — https://agentskills.io/specification

## OpenAI Sora

- Video generation guide — https://developers.openai.com/api/docs/guides/video-generation
- Note: older `platform.openai.com/docs/models/sora` returned HTTP 404 during this pass; use the developers.openai.com video guide and live model picker for exact IDs (`sora-2`, `sora-2-pro`).

## Google Veo (Vertex / Gemini Enterprise Agent Platform)

- Video models overview — https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/overview
- Generate videos from text — https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-text
- Veo 3.1 generate model card — https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate
- Historical Vertex AI video overview redirects into the same docs host.

## Runway

- API reference home — https://docs.dev.runwayml.com/api/
- Docs site root — https://docs.dev.runwayml.com/

## Luma

- Video generation docs — https://docs.lumalabs.ai/docs/video-generation

## Fal / Pika / Hailuo hosts

- Fal model explore — https://fal.ai/explore
- Example MiniMax Video-01 on Fal — https://fal.ai/models/fal-ai/minimax/video-01

## MiniMax

- Video generation document — https://platform.minimaxi.com/document/video_generation

## Seedance / ByteDance ModelArk

- BytePlus ModelArk Seedance docs — https://docs.byteplus.com/en/docs/ModelArk/seedance

## Replicate

- Replicate docs — https://replicate.com/docs

## Vidu

- Product home — https://www.vidu.com/
- Treat consumer marketing pages as discovery; confirm API host and model IDs in the authenticated developer console before production spend.

## Freshness caveats

- Model IDs, duration caps, and pricing change frequently. Re-check the linked official page before locking a production route.
- Community nicknames (`Nano Banana`, `Gen-4 Turbo` marketing labels, etc.) are aliases only until mapped to a documented API ID.
- Bot-mitigation / geo walls may return 403 to plain curl for some vendor consoles; record the gap and use authenticated docs when needed.
