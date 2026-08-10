# Troubleshooting Guide

## 401 Unauthorized

Symptoms:
- API returns `401`
- `/models` fails immediately

Checks:
1. Confirm without printing it: `: "${GROQ_API_KEY:?Set GROQ_API_KEY in the environment}"`
2. Remove trailing spaces or quotes in env var value
3. Re-run the `/models` check request
4. Verify key is active at https://console.groq.com/keys

Recovery:
```bash
export GROQ_API_KEY="<set-through-your-secret-manager>"
curl -s https://api.groq.com/openai/v1/models -H "Authorization: Bearer $GROQ_API_KEY" | jq '.data[0].id'
```

## 404 or Model Not Found

Symptoms:
- Request accepted but model ID is rejected
- Error: "model not found" or "invalid model"

Checks:
1. Fetch `/models` and copy exact model ID (case-sensitive)
2. Remove stale IDs from saved defaults in `<state_root>/memory.md`
3. Re-test with a minimal payload
4. Verify model is not deprecated (check Groq deprecations page)

Common mistakes:
- Using `llama-3.1-8b` instead of `llama-3.1-8b-instant`
- Using `gpt-oss-120b` instead of `openai/gpt-oss-120b`

## 429 Rate Limited

Symptoms:
- Spikes of `429` under burst traffic
- `retry-after` header present

Checks:
1. Read `retry-after` header for server-suggested wait time
2. Add exponential backoff with jitter (1s, 2s, 4s + random 0-500ms)
3. Reduce parallel requests and prompt size
4. Route overflow to a fallback model
5. Monitor `x-ratelimit-remaining-tokens` header

Developer plan limits (per model):
- Text models: 30 RPM, 1K-14.4K RPD, 6K-12K TPM
- Whisper: 20 RPM, 2K RPD, 7.2K ASH

Recovery pattern:
```bash
if response.status == 429:
    wait = response.headers.get('retry-after', 1)
    sleep(wait)
    retry with fallback model if still rate-limited
```

## 5xx or Timeout

Symptoms:
- Intermittent server errors (500, 502, 503, 504)
- Long-tail latency increases

Checks:
1. Retry capped attempts (max 3) before failing
2. Shorten payload and disable non-essential options
3. Fail over to fallback route and capture error context
4. Check Groq status page for service incidents

Recovery:
- Switch to fallback model immediately on 5xx
- Log error context to `<state_root>/logs/` with timestamp
- If persistent (> 5 minutes), reduce request rate

## JSON Parse Failures

Symptoms:
- Model returns prose when automation expects JSON
- `jq` or JSON parser fails

Checks:
1. Force strict output contract in system message
2. Use low temperature (`temperature: 0`) for deterministic shape
3. Validate parse before executing downstream actions
4. Prefer `response_format.json_schema` with `strict: true` over prompt-based JSON

Strict mode requirements:
- Model: `openai/gpt-oss-20b` or `openai/gpt-oss-120b`
- All fields in `required` array
- `additionalProperties: false` on all objects

Best-effort fallback:
```json
{
  "response_format": {"type": "json_object"},
  "messages": [{"role": "system", "content": "Respond only with valid JSON matching this schema: {...}"}]
}
```

## Transcription Quality Drops

Symptoms:
- Missing words or unstable output
- High word error rate

Checks:
1. Verify input audio format (mp3, wav, m4a, flac, ogg, webm)
2. Check file size (max 100 MB for whisper-large-v3)
3. Split long audio into smaller segments (< 25 MB each)
4. Compare results across `whisper-large-v3` (accuracy) vs `whisper-large-v3-turbo` (speed)
5. Verify audio sample rate (16kHz+ recommended)

Recovery:
- For critical transcription: use `whisper-large-v3`
- For bulk processing: use `whisper-large-v3-turbo` (228x realtime, $0.04/hour)
- Pre-process audio: normalize volume, remove background noise if possible

## Structured Output Schema Errors

Symptoms:
- 400 error with schema validation message
- Model returns valid JSON but doesn't match schema

Checks:
1. Verify model supports structured output (`openai/gpt-oss-20b`, `openai/gpt-oss-120b`)
2. For strict mode: all fields must be in `required`, objects need `additionalProperties: false`
3. Check schema syntax (valid JSON Schema draft-07+)
4. Test with minimal schema first, then add complexity

Common errors:
- Missing `additionalProperties: false` in strict mode
- Optional fields not in `required` array (strict mode requires all fields)
- Using strict mode with unsupported model (falls back to best-effort)

## Model Deprecation

Symptoms:
- Previously working model returns 404
- Warning messages about deprecation

Checks:
1. Fetch current `/models` list
2. Check Groq deprecations page for timeline
3. Update model ID in code and `<state_root>/memory.md`
4. Test with new model before deploying

Migration pattern:
```python
# Old
model = "llama-3.1-8b"  # deprecated

# New
model = "llama-3.1-8b-instant"  # current
```
