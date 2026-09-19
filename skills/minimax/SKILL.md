---
name: minimax
description: Manage MiniMax multimodal generation (text, speech, video). Load when the user requests MiniMax text models (e.g. abab6.5-chat), speech generation, or video/music API jobs.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🎛️", "requires": {"env": ["MINIMAX_API_KEY"], "config": ["<state_root>/"]}, "primaryEnv": "MINIMAX_API_KEY"}'
  related-skills: '{"ai": "Compare MiniMax against other model providers before locking the stack.", "api": "Reuse structured HTTP, retry, and payload-debugging patterns around the MiniMax APIs.", "models": "Choose the right model family and fallback chain for quality, latency, and cost.", "video-generation": "Extend MiniMax video work into broader multi-provider video routing.", "music": "Strengthen prompt and arrangement decisions when the task is specifically music-first."}'
---
## When to Use

Trigger when the user explicitly requests MiniMax text models, voice generation, or media jobs. Load for generic text completion only when MiniMax is the preferred provider.

## State location

MiniMax state may exist in `<workspace>/minimax/`, `<workspace>/memory/minimax/`, or `~/minimax/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/minimax/`, `<workspace>/memory/minimax/`, `~/minimax/`.
3. If none exists and state must be created, default to `<workspace>/minimax/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

Memory lives in `<state_root>/`. If `<state_root>/` does not exist, run `references/setup.md`. See `assets/memory-template.md` for structure.

```text
<state_root>/
|-- memory.md          # Durable context, activation boundaries, and approved defaults
|-- routing.md         # Model and interface choices that worked in practice
|-- text-defaults.md   # Text model pins, SDK compatibility notes, and parsing rules
|-- speech-defaults.md # Voice, format, latency, and consent-sensitive speech notes
|-- media-jobs.md      # Async video or music job patterns, polling, and output handling
|-- mcp-notes.md       # Approved MCP hosts, scopes, and rejection reasons
`-- incidents.md       # Rate limits, failed jobs, bad prompts, and recovery notes
```

## Quick Reference

Load only the file needed for the current blocker.

| Topic | File |
|-------|------|
| Setup guide | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| Model selection and routing | `references/model-routing.md` |
| Native, Anthropic-compatible, and OpenAI-compatible text flows | `references/text-interfaces.md` |
| Speech generation and audio delivery | `references/speech-workflows.md` |
| Video, music, and async media jobs | `references/media-generation.md` |
| MCP boundaries and orchestration choices | `references/mcp-and-orchestration.md` |
| Failure recovery and debugging | `references/troubleshooting.md` |

## Requirements

- `MINIMAX_API_KEY` for direct MiniMax API usage.
- A client surface of choice: raw HTTP, an approved SDK, or an existing Anthropic-compatible or OpenAI-compatible integration.
- Explicit user approval before uploading private media, cloning or imitating a real person's voice, enabling remote MCP servers, or launching long-running paid generation jobs.
- Current model names, compatibility limits, and endpoint behavior must be verified against official MiniMax docs when the task depends on exact product surface.

## Operating Coverage

This skill treats MiniMax as an execution platform, not as a one-line provider swap. It covers:
- text generation through native MiniMax APIs and compatible SDK interfaces
- model routing across current text families such as `abab6.5g-chat`, `abab6.5s-chat`, `abab6.5t-chat`, `abab6.5-chat`, and `abab5.5-chat`
- speech generation with synchronous HTTP and lower-latency endpoint choices
- queued media workflows for video and music where submit, poll, and fetch are separate phases
- MCP-aware workflows where tool access, host trust, and data scope must be explicit
- debugging around ignored parameters, malformed payloads, long queue times, rate limits, and output reproducibility

## Data Storage

Keep only durable MiniMax operating context in `<state_root>/`:
- which modalities the user actually uses: text, speech, video, music, or MCP-backed flows
- approved models, speed tiers, and compatibility interfaces that worked for real tasks
- output defaults such as JSON parsing rules, audio formats, polling intervals, and retry posture
- media safety rules, consent requirements, and budget boundaries the user explicitly approved
- repeated failures such as 401s, ignored params, queue stalls, or bad prompt templates

## Core Rules

### 1. Lock the Modality and Deliverable First
- Start by naming the actual output: structured text, chat reply, narration audio, short video, song draft, or tool-augmented workflow.
- MiniMax is not one surface. The wrong modality choice creates wrong endpoints, wrong latency expectations, and wrong retry logic.

### 2. Choose Native Versus Compatible APIs Deliberately
- Use native MiniMax APIs when you need MiniMax-specific features or exact behavior.
- Use Anthropic-compatible or OpenAI-compatible interfaces only when the surrounding app already depends on those SDKs and the supported subset is good enough.
- Treat compatibility layers as narrower surfaces, not as feature-complete copies.

### 3. Pin the Exact Model Family and Speed Tier
- Choose quality-first, speed-first, or fallback models explicitly instead of saying "use MiniMax."
- Current text routing should start with `abab6.5g-chat` or `abab6.5s-chat`, then step down only if latency, cost, or compatibility requires it.
- Re-check live docs before shipping hardcoded model lists because MiniMax updates its public surface frequently.

### 4. Separate Sync From Async Media Work
- Synchronous text and speech flows can often return in one request.
- Video and music generation usually need submit, poll, timeout, and fetch logic.
- Design asynchronous polling workflows for media jobs that are inherently queued.

### 5. Validate Media Rights, Inputs, and Formats Before Generation
- Confirm the user has rights to upload or transform any voice, lyrics, reference media, or branded assets.
- Validate format, duration, language, and output expectations before generating.
- Bad asset assumptions waste spend faster than bad prompts.

### 6. Make Cost and Trust Boundaries Explicit
- Multimodal runs can send prompts, media, and metadata off machine and can accumulate cost quickly.
- State which endpoint will receive which payload, and pause to require approval before remote MCP or large media uploads unless the user approved that path.
- Require explicit consent for remote execution even when the API supports it.

### 7. Finish With a Reproducible Recipe
- A successful MiniMax run ends with the exact model, interface, key parameters, asset inputs, and polling behavior recorded clearly enough to rerun.
- If the output is fragile, capture the narrowest reproducible payload before changing prompts or models again.

## MiniMax Traps

- Treating every MiniMax feature as available through every SDK shim -> parameters get ignored and debugging starts from a false premise.
- Saying "use the MiniMax model" without pinning family or speed tier -> latency, quality, and cost drift across runs.
- Building media flows as one request and one response -> queued jobs hang or fail without usable recovery.
- Uploading sensitive media before clarifying rights or consent -> the technical workflow succeeds but the usage is unsafe.
- Assuming text defaults work for speech, video, or music -> prompts, payload shape, and validation rules diverge quickly.
- Blaming the model before checking payload schema, queue state, or output fetch logic -> operational bugs get mislabeled as generation quality problems.
- Letting MCP servers touch broad data without host review -> tool convenience becomes a trust leak.

## External Endpoints

Only these endpoint categories are allowed unless the user explicitly approves more:

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://api.minimax.io | prompts, approved media inputs, generation parameters, and polling requests | Native MiniMax text, speech, media, and related API workflows |
| https://api-uw.minimax.io | approved speech payloads and generation parameters | Optional lower-TTFA speech endpoint when the user wants faster first audio |
| https://platform.minimax.io/docs | doc queries only | Verify current models, compatibility notes, and API behavior |
| https://{user-approved-mcp-host} | request payloads required by the approved MCP server | Optional MCP tool access beyond the local machine |

No other data is sent externally unless the user explicitly approves additional hosts or provider routes.

## Security & Privacy

Data that leaves your machine:
- prompts and parameters sent to MiniMax API endpoints
- approved media assets or reference files only for the generation workflow the user requested
- optional MCP payloads only for user-approved MCP hosts
- optional documentation lookups against official MiniMax docs

Data that stays local:
- durable operating notes under `<state_root>/`
- local prompt drafts, routing choices, and incident notes unless the user exports them
- any rejected or unused assets that never get uploaded

This skill does NOT:
- treat compatible SDKs as exact feature matches without verification
- upload private media, voice references, or lyrics without explicit user intent
- enable remote MCP or broad tool access without explicit approval
- claim that every MiniMax modality is synchronous or instantly available
- modify its own skill files

## Trust

By using this skill, prompts and approved media may be sent to MiniMax services, plus any optional user-approved MCP hosts.
Only install if you trust those services with that data.

## Scope

This skill ONLY:
- helps operate MiniMax text, speech, video, music, and MCP-related workflows safely
- routes tasks to the right model family, interface, and job pattern
- keeps durable notes for approved defaults, budget boundaries, and recurring failures

This skill ENSURES:
- MiniMax is treated with precise interface limits in mind
- Voice imitation or media transformation happens only with verified rights and consent
- Local orchestration is kept distinct from remote MCP execution
- Queued media jobs are managed with asynchronous expectations
