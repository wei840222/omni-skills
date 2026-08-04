# Model Selection and Routing

## Current Production Models (2026)

### Text Models

| Model ID | Speed (T/sec) | Input $/1M | Output $/1M | Context | Max Output | Best For |
|----------|---------------|------------|-------------|---------|------------|----------|
| `llama-3.1-8b-instant` | 560 | $0.05 | $0.08 | 131K | 131K | Fast interactive chat, low-cost tasks |
| `llama-3.3-70b-versatile` | 280 | $0.59 | $0.79 | 131K | 32K | High-accuracy reasoning, complex tasks |
| `openai/gpt-oss-120b` | 500 | $0.15 | $0.60 | 131K | 65K | Strong reasoning, structured output (strict mode) |
| `openai/gpt-oss-20b` | 1000 | $0.075 | $0.30 | 131K | 65K | Fast structured output (strict mode), tool calling |
| `qwen/qwen3.6-27b` | 500 | $0.60 | $3.00 | 131K | 16K | High-quality output, specialized tasks |

### Speech Models

| Model ID | Speed | Price | Max File | Best For |
|----------|-------|-------|----------|----------|
| `whisper-large-v3` | 217x realtime | $0.111/hour | 100 MB | High-accuracy transcription |
| `whisper-large-v3-turbo` | 228x realtime | $0.04/hour | - | Cost-effective bulk transcription |

### Agentic Systems

| System ID | Speed | Context | Max Output | Capabilities |
|-----------|-------|---------|------------|--------------|
| `groq/compound` | 450 | 131K | 8K | Web search, code execution |
| `groq/compound-mini` | 450 | 131K | 8K | Lightweight agentic tasks |

## Routing Strategy

Select models by workload profile, not by a single default:

| Workload | Primary Goal | Routing Guidance |
|----------|--------------|------------------|
| Interactive chat | Lowest latency | `llama-3.1-8b-instant` (560 T/sec, $0.05/$0.08) |
| Agent reasoning | Higher reliability | `openai/gpt-oss-120b` (500 T/sec, $0.15/$0.60) |
| Structured output | Schema compliance | `openai/gpt-oss-20b` or `openai/gpt-oss-120b` (strict mode) |
| Summarization | Throughput | Batch requests, cap context to 32K |
| Transcription | Accuracy + speed | `whisper-large-v3-turbo` for bulk, `whisper-large-v3` for critical |
| Agentic workflows | Tool use | `groq/compound` for web search + code execution |

## Practical Selection Loop

1. Fetch live model list from `/models` to verify availability.
2. Keep a short candidate set per workload (2-3 models).
3. Run the same prompt across candidates with identical parameters.
4. Compare latency (time-to-first-token, tokens/sec), output quality, and failure rate.
5. Save winner + fallback in `<state_root>/memory.md`.

## Fallback Policy

Use a primary model and one fallback per workload:
- If timeout or repeated `5xx`, switch to fallback immediately.
- If `429`, retry with exponential backoff first, then fallback.
- Log the switch reason and timestamp to `<state_root>/logs/` for routing improvement.

Example fallback chains:
- Fast chat: `llama-3.1-8b-instant` → `openai/gpt-oss-20b`
- Reasoning: `openai/gpt-oss-120b` → `llama-3.3-70b-versatile`
- Transcription: `whisper-large-v3-turbo` → `whisper-large-v3`

## Prompt Sizing Rules

- Keep system prompts compact and explicit (< 500 tokens when possible).
- Split long context into summarized chunks if exceeding 64K tokens.
- Avoid unnecessary history replay in every request; use conversation ID or summary.
- Use deterministic settings (`temperature: 0`) when output must be parsed.
- For structured output, prefer `response_format.json_schema` over prompt-based JSON instructions.

## Rate Limits (Developer Plan)

| Model | RPM | RPD | TPM |
|-------|-----|-----|-----|
| `llama-3.1-8b-instant` | 30 | 14.4K | 6K |
| `llama-3.3-70b-versatile` | 30 | 1K | 12K |
| `openai/gpt-oss-120b` | 30 | 1K | 8K |
| `openai/gpt-oss-20b` | 30 | 1K | 8K |
| `whisper-large-v3` | 20 | 2K | - (7.2K ASH) |

Check response headers for real-time usage:
- `x-ratelimit-remaining-requests`: remaining requests today
- `x-ratelimit-remaining-tokens`: remaining tokens per minute
- `retry-after`: seconds to wait on 429

## Production Checklist

- Primary and fallback model IDs are valid now (verify with `/models`).
- Retry policy is capped (max 3 attempts) and observable (log each retry).
- Output parsing fails closed (reject malformed JSON, don't guess).
- P95 latency and error rate are tracked per route in `<state_root>/experiments/`.
- Rate limit headers are monitored; backoff triggers at 80% TPM usage.
- Structured output uses `strict: true` when schema compliance is critical.
