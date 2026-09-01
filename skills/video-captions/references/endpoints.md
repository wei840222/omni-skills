# External Endpoints

**Default: 100% LOCAL processing. No network calls.**

| Endpoint | Data Sent | When Used |
|----------|-----------|-----------|
| Whisper (local) | None (local) | Default — always |
| api.assemblyai.com | Audio file | Only if user sets ASSEMBLYAI_API_KEY |
| api.deepgram.com | Audio file | Only if user sets DEEPGRAM_API_KEY |

Cloud APIs are **documented as alternatives** and only used when the user explicitly provides API keys and requests cloud processing. By default, all processing stays on your machine.