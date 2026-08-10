# Groq API Patterns

## Base URL and Headers

Base URL:
`https://api.groq.com/openai/v1`

Required headers:
- `Authorization: Bearer $GROQ_API_KEY`
- `Content-Type: application/json`

## Health Check

```bash
curl -s https://api.groq.com/openai/v1/models \
  -H "Authorization: Bearer $GROQ_API_KEY" | jq '.data | length'
```

## Chat Completion (minimal)

```bash
curl -s https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.1-8b-instant",
    "messages": [
      {"role":"system","content":"Be concise."},
      {"role":"user","content":"Summarize this in 3 bullets: ..."}
    ],
    "temperature": 0.2
  }' | jq -r '.choices[0].message.content'
```

## Structured JSON Response (Strict Mode)

Use `response_format.json_schema` with `strict: true` for guaranteed schema compliance (supported by `openai/gpt-oss-20b` and `openai/gpt-oss-120b`):

```bash
curl -s https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-oss-20b",
    "messages": [
      {"role":"system","content":"Extract classification data."},
      {"role":"user","content":"Classify: payment failed after update"}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "classification",
        "strict": true,
        "schema": {
          "type": "object",
          "properties": {
            "label": {"type": "string"},
            "confidence": {"type": "number"}
          },
          "required": ["label", "confidence"],
          "additionalProperties": false
        }
      }
    },
    "temperature": 0
  }' | jq -r '.choices[0].message.content' | jq
```

**Schema requirements for strict mode:**
- All fields must be in `required` array
- Objects must set `additionalProperties: false`
- Supported models: `openai/gpt-oss-20b`, `openai/gpt-oss-120b`

For other models, use best-effort mode (`strict: false`) or `response_format.json_object` with explicit schema in system prompt.

## Audio Transcription

```bash
curl -s https://api.groq.com/openai/v1/audio/transcriptions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -F "model=whisper-large-v3-turbo" \
  -F "file=@sample.wav" | jq
```

Supported formats: mp3, wav, m4a, flac, ogg, webm
Max file size: 100 MB (whisper-large-v3)
Billing: minimum 10 seconds per request

## Retry Pattern

Retry on `429` and `5xx` with exponential backoff:
1. Sleep 1s
2. Sleep 2s
3. Sleep 4s
4. Stop and report full context if still failing

Check `retry-after` header on 429 responses for server-suggested wait time.

Monitor rate limit headers:
- `x-ratelimit-remaining-tokens`: backoff at 80% usage
- `x-ratelimit-remaining-requests`: track daily quota
