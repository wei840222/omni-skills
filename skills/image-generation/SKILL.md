---
name: image-generation
description: "Select and run text-to-image or image-editing workflows across GPT Image, Gemini, FLUX, Imagen, and related providers with alias resolution, cost-aware drafting, and portable local memory."
metadata:
  version: "1.0.3"
  openclaw: '{"emoji":"🎨","requires":{"env":["OPENAI_API_KEY","GEMINI_API_KEY","BFL_API_KEY","GOOGLE_CLOUD_PROJECT","REPLICATE_API_TOKEN","LEONARDO_API_KEY","IDEOGRAM_API_KEY"],"config":["<state_root>/"]}}'
  related-skills: '{"image-edit":"Specialized inpainting, outpainting, and mask workflows","video-generation":"Convert image concepts into video pipelines","colors":"Build palettes for visual consistency across assets","ffmpeg":"Post-process image sequences and exports"}'
---

## When to Use

User needs AI-generated visuals, edits, or consistent image sets.
Use this skill to pick the right model, write stronger prompts, and avoid outdated model choices.

## State location

Image-generation preferences may exist in `<workspace>/image-generation/`, `<workspace>/memory/image-generation/`, or `~/image-generation/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/image-generation/`, `<workspace>/memory/image-generation/`, `~/image-generation/`.
3. If none exists and state must be created, default to `<workspace>/image-generation/`.

Use the selected `<state_root>` for every state operation in this skill.

- `<state_root>/memory.md`: Preferred providers, project context, winning recipes
- `<state_root>/history.md`: Optional generation log

If `<state_root>/` does not exist, read `references/setup.md` before the first write.

## Setup

On first use, read `references/setup.md`.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Initial setup | `references/setup.md` | When `<state_root>/` is missing or empty |
| Memory template | `references/memory-template.md` | When creating or updating preference memory |
| Migration guide | `references/migration.md` | When upgrading older local memory layouts |
| Core rules and traps | `references/core_rules_and_traps.md` | Before choosing a model or spending on drafts |
| Domain knowledge | `references/domain_knowledge.md` | When grounding model-family claims |
| Benchmark snapshots | `references/benchmarks-2026.md` | When quality ranking is decision-critical |
| Prompt techniques | `references/prompting.md` | When drafting or refining prompts |
| API handling | `references/api-patterns.md` | When calling provider APIs or handling errors |
| GPT Image (OpenAI) | `references/gpt-image.md` | Exact text, OpenAI drafts, or GPT Image edits |
| Gemini and Imagen (Google) | `references/gemini.md` | Multi-turn edits or Google image models |
| FLUX (Black Forest Labs) | `references/flux.md` | Consistency-heavy or FLUX-specific work |
| Midjourney | `references/midjourney.md` | Discord-driven Midjourney workflows |
| Leonardo | `references/leonardo.md` | Leonardo generation or editing |
| Ideogram | `references/ideogram.md` | Typography-focused generation |
| Replicate | `references/replicate.md` | Hosted third-party model routing |
| Stable Diffusion | `references/stable-diffusion.md` | Local or open-weight SDXL workflows |

## Core Rules and Common Traps

Load `references/core_rules_and_traps.md` before generating an image to review model selection criteria, alias resolution, cost-saving drafting strategies, and common API errors.

## Security & Privacy

**Data that leaves your machine:**
- Prompt text
- Reference images when editing or style matching

**Data that stays local:**
- Provider preferences in `<state_root>/memory.md`
- Optional local history file

**Operating constraints:**
- Keep API keys outside skill state files and outside git.
- Send files only to the provider request the user chose.
- Retain generated images only when the user explicitly asks to save them.

## External Endpoints

| Provider | Endpoint | Data Sent | Purpose |
|----------|----------|-----------|---------|
| OpenAI | `api.openai.com` | Prompt text, optional input images | GPT Image generation/editing |
| Google Gemini API | `generativelanguage.googleapis.com` | Prompt text, optional input images | Gemini image generation/editing |
| Google Vertex AI | `aiplatform.googleapis.com` | Prompt text, optional input images | Imagen 4 generation |
| Black Forest Labs | `api.bfl.ai` | Prompt text, optional input images | FLUX generation/editing |
| Replicate | `api.replicate.com` | Prompt text, optional input images | Hosted third-party image models |
| Midjourney | `discord.com` | Prompt text | Midjourney generation via Discord workflows |
| Leonardo | `cloud.leonardo.ai` | Prompt text, optional input images | Leonardo generation/editing |
| Ideogram | `api.ideogram.ai` | Prompt text | Typography-focused image generation |

No other data is sent externally.

## Migration

If upgrading from a previous version, read `references/migration.md` before updating local memory structure.

## Trust

This skill may send prompts and reference images to third-party AI providers.
Only install if you trust those providers with your content.
