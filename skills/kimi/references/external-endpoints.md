## External Endpoints

Use only the official Moonshot API surface required for the current task.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://api.moonshot.ai/v1/models | Auth header only | Discover live Kimi models |
| https://api.moonshot.ai/v1/chat/completions | Prompt messages and options | Kimi chat, reasoning, coding, and structured-output requests |

No other data is sent externally.