# OpenAI Sora 2

**Best for:** premium text-to-video quality and strong prompt adherence.

## Official Models

- `sora-2` — faster exploration / drafts
- `sora-2-pro` — higher fidelity finals

Source: OpenAI video generation guide (developers.openai.com).

## API Path

Use the OpenAI **Videos API** (`/videos`) with async create → poll → download.
Do not invent a Responses-API `"video"` modality path unless current official docs show it.

## Practical Routing

- Use `sora-2-pro` for final hero outputs
- Use `sora-2` for earlier iterations or lower-cost tests
- Keep shot prompts explicit about subject, motion, and camera timing

## Reliability Tips

- Treat jobs as async and poll status for completion
- Keep prompts scoped to one shot objective to reduce drift
- Store response IDs and download outputs immediately before URL expiry
