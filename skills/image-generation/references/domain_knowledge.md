# AI Image Generation Domain Knowledge

## Sources
- **OpenAI Images API** — current GPT Image generation and editing surface — https://platform.openai.com/docs/guides/image-generation
- **OpenAI model docs: GPT Image** — official model identifiers and capabilities — https://platform.openai.com/docs/models/gpt-image-1
- **Google Gemini image generation** — Gemini native image generation/editing guidance — https://ai.google.dev/gemini-api/docs/image-generation
- **Google Imagen on Vertex AI** — Imagen generation models and request patterns — https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview
- **Black Forest Labs FLUX** — provider docs for FLUX generation SKUs — https://docs.bfl.ai/
- **Artificial intelligence visual art (Wikipedia)** — architecture overview for GANs, diffusion, and autoregressive image models — https://en.wikipedia.org/wiki/AI_art

## Fundamentals
- **Generative Models:** Modern image skills mainly route through diffusion systems (Stable Diffusion, Midjourney, DALL·E-lineage, Imagen, FLUX) and multimodal transformers that condition pixels on text or reference images.
- **Diffusion Models:** Dominant architecture for high-quality text-to-image synthesis. Models learn to reverse a noise process, guided by text embeddings and optional image conditioning.
- **Prompt Engineering:** Structure subject, style, composition, lighting, and constraints so the selected model can follow the request without relying on outdated DALL·E-only prompt folklore.

## Recent Advancements (2025-2026)
- Coherent text rendering and multi-turn editing matter as much as first-pass generation quality.
- Provider SKUs rename quickly; resolve community labels such as "Nano Banana" or "FLUX 2 Pro" to the current official model ID before spending on retries.
- Cost-aware workflows draft on cheaper variants, then finalize only the chosen candidate on a higher-tier model.
