---
name: groq-api
description: Use when building, integrating, or debugging Groq API chat completions, structured JSON output, tool calling, or speech transcription. Handles request shaping, model routing (Llama 3.1/3.3, GPT-OSS, Whisper), rate limit management, and production retry patterns. Activate for Groq inference tasks even if user doesn't explicitly mention "Groq API."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⚡","requires":{"bins":["curl","jq"],"env":["GROQ_API_KEY"]}}'
  related-skills: '{"api":"Provides reusable REST auth and error-handling patterns that complement Groq endpoint usage.","ai":"Landscape check before committing to a specific Groq model or provider.","fine-tuning":"Adaptation path when Groq prompting alone is insufficient.","langchain":"Orchestration layer for multi-step Groq-backed pipelines.","models":"Cross-provider model comparison when Groq is one of several options."}'
---

## State location

Groq API state may exist in `<workspace>/groq-api/`, `<workspace>/memory/groq-api/`, or `~/groq-api/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/groq-api/`, `<workspace>/memory/groq-api/`, `~/groq-api/`.
3. If none exists and state must be created, default to `<workspace>/groq-api/`.

Use the selected `<state_root>` for every state operation in this skill.

```text
<state_root>/
├── memory.md           # Status, activation preference, defaults
├── requests/           # Reusable payload snippets
├── logs/               # Optional debug snapshots
└── experiments/        # Prompt/model A-B notes
```

## Setup

On first use, read `references/setup.md` for activation preferences, credential verification, and default workflow setup.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | First use or when `<state_root>` doesn't exist |
| Memory template | `references/memory.md` | Creating or updating `<state_root>/memory.md` |
| Request patterns | `references/api-patterns.md` | Building chat, structured output, or transcription requests |
| Model routing | `references/model-selection.md` | Choosing models, setting up fallback chains, checking rate limits |
| Failures and recovery | `references/troubleshooting.md` | On 401, 404, 429, 5xx, JSON parse failures, or transcription quality issues |

## Core Workflow

### 1. Verify Auth (mandatory first step)

Verify auth before any API call. Confirm `/models` returns a valid model ID before proceeding.

```bash
curl -s https://api.groq.com/openai/v1/models \
  -H "Authorization: Bearer $GROQ_API_KEY" | jq '.data[0].id'
```

If this fails with 401:
- Check without printing it: `: "${GROQ_API_KEY:?Set GROQ_API_KEY in the environment}"`
- Remove trailing spaces or quotes
- Verify key is active at https://console.groq.com/keys

### 2. Start Minimal, Then Add Complexity

Begin with a small deterministic payload:
- Use `temperature: 0` for structured output
- Keep system prompt < 500 tokens
- Test with one message before adding history

Add complexity only after baseline call succeeds.

### 3. Route by Task

Default routing (change only if task requires):
- Fast interactive chat: `llama-3.1-8b-instant` (560 T/sec, $0.05/$0.08)
- High-accuracy reasoning: `openai/gpt-oss-120b` (500 T/sec, $0.15/$0.60)
- Structured JSON output: `openai/gpt-oss-20b` with `strict: true`
- Speech transcription: `whisper-large-v3-turbo` ($0.04/hour)

Verify model availability before switching models. Run `/models` to confirm target ID exists. Query model IDs at runtime rather than hardcoding — they change without notice.

### 4. Design for Failure

If 429 rate limit:
1. Read `retry-after` header
2. Exponential backoff: 1s -> 2s -> 4s (max 3 attempts)
3. Switch to fallback model if still rate-limited
4. Log switch to `<state_root>/logs/`

If 5xx server error:
1. Retry capped attempts (max 3)
2. Shorten payload
3. Fail over to fallback immediately
4. If persistent (> 5 min), reduce request rate

If JSON parse fails:
1. For strict mode: verify model supports it (`openai/gpt-oss-20b` or `openai/gpt-oss-120b`)
2. Ensure all fields in `required`, objects have `additionalProperties: false`
3. Fall back to `response_format.json_object` with explicit schema in system prompt

### 5. Validate Output Before Acting

Validate output before downstream actions. If output feeds code execution or data writes, parse and validate first.

If output feeds code execution or data writes:
- Parse JSON before using (never trust raw text)
- Validate against schema
- Reject malformed output early with clear error message

### 6. Speech is a separate path

Speech uploads have different failure modes:
- Validate input format (mp3, wav, m4a, flac, ogg, webm)
- Check file size (max 100 MB)
- Split long audio into < 25 MB segments
- For critical transcription: use `whisper-large-v3` (accuracy)
- For bulk processing: use `whisper-large-v3-turbo` (speed)

### 7. Keep Secrets Scoped

- Store `GROQ_API_KEY` only in environment variables
- Sanitize request logs (no full prompts unless user explicitly asks)
- State goes to `<state_root>/`, not skill package

## Gotchas

- Model IDs are case-sensitive and versioned: Use exact IDs from `/models` (e.g., `llama-3.1-8b-instant`, not `llama-3.1-8b`)
- Structured output strict mode requires all fields: Every property must be in `required` array, objects need `additionalProperties: false`
- Rate limits are per-organization, not per-user: Hitting TPM limit blocks entire org, not just your key
- Whisper has 10-second minimum billing: Short audio clips still billed as 10 seconds
- Cached tokens don't count toward rate limits: Use prompt caching to reduce TPM usage
- Preview models can disappear without warning: Use production models for anything beyond testing
- 429 `retry-after` is in seconds: Use seconds for backoff calculations

## Best Practices

- Query current model IDs from `/models` at runtime instead of copying from old examples
- Truncate prompts to reasonable length to avoid latency spikes and timeouts
- Implement exponential backoff for 429 responses to handle rate limits gracefully
- Use the correct endpoint for each payload type (chat vs. transcription)
- Parse and validate free-form text before using it in automation
- Query model IDs at runtime; models get deprecated without notice
- Verify model support for strict mode before using it; unsupported models fall back to best-effort silently
- Store API keys in environment variables, not in `<state_root>/memory.md`

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://api.groq.com/openai/v1/models | API credential; no prompt or audio payload | Discover available models |
| https://api.groq.com/openai/v1/chat/completions | Prompt messages and options | Chat completions |
| https://api.groq.com/openai/v1/audio/transcriptions | Audio file and params | Speech-to-text |

No other data is sent externally.

## Security & Privacy

Data that leaves your machine:
- Prompt content sent to Groq inference endpoints
- Audio content sent to Groq transcription endpoint when requested

Data that stays local:
- Workflow preferences in `<state_root>/memory.md`
- Optional debug notes in `<state_root>/logs/`

This skill does NOT:
- Store `GROQ_API_KEY` in project files
- Access files outside `<state_root>/` for persistence
- Call undeclared third-party endpoints
- Modify itself or other skills

## Trust

By using this skill, prompts and optional audio content are sent to Groq.
Only install if you trust Groq with that data.
