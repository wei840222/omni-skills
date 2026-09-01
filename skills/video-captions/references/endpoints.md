# External Endpoints

**Default: 100% LOCAL processing. No network calls.**

| Endpoint | Data Sent | When Used |
|----------|-----------|-----------|
| Whisper (local) | None (local) | Default — always |
| api.assemblyai.com | Audio file | Only after the user explicitly selects AssemblyAI and approves the transfer |
| api.deepgram.com | Audio file | Only after the user explicitly selects Deepgram and approves the transfer |

Cloud APIs are documented as alternatives. Use a cloud provider only after the user explicitly requests that provider and approves sending the media there; otherwise keep processing local.

## Provider references

- **AssemblyAI documentation** — API authentication and transcription workflow: https://www.assemblyai.com/docs
- **Deepgram pre-recorded audio documentation** — request format and response behavior: https://developers.deepgram.com/docs/pre-recorded-audio
