# OpenClaw Talk mode

Load this reference when the user wants continuous voice conversation on a supported device, speech playback, interruption behavior, or a realtime Talk session. Talk mode is distinct from carrier telephony; load `references/voice-call.md` for phone numbers and carrier webhooks.

## Choose the voice path

| Goal | Configuration path | Read next |
|---|---|---|
| Device Talk with text-to-speech playback | `talk.provider` plus `talk.providers.<id>` | This reference |
| Browser or mobile realtime conversation | `talk.realtime` | This reference and the selected provider's official documentation |
| Inbound or outbound carrier call | `plugins.entries.voice-call.config` | `references/voice-call.md` |

## Device Talk TTS

Configure the active provider under `talk.provider` and its provider-specific fields under `talk.providers.<id>`. This example selects ElevenLabs for device playback:

```json5
{
  talk: {
    provider: "elevenlabs",
    providers: {
      elevenlabs: {
        voiceId: "<elevenlabs-voice-id>",
        modelId: "eleven_v3",
        outputFormat: "mp3_44100_128",
        apiKey: "<secret-ref-or-provider-secret>",
      },
    },
    speechLocale: "en-US",
    silenceTimeoutMs: 1500,
    interruptOnSpeech: true,
  },
}
```

Use the provider's current voice catalog to select `voiceId`. Keep the API key in the configured secret mechanism when supported. Device defaults vary by platform: Talk uses a device-provided speech locale when `speechLocale` is unset, and its silence timeout is platform-specific.

## Realtime Talk

A realtime session has separate provider, transport, audio, and agent-routing choices. Begin with a provider supported by the current Talk catalog and use its official setup guide for its provider-owned fields.

```json5
{
  talk: {
    realtime: {
      provider: "openai",
      providers: {
        openai: {
          apiKey: "<secret-ref-or-provider-secret>",
          model: "<current-realtime-model>",
          speakerVoice: "<voice-id>",
        },
      },
      mode: "realtime",
      transport: "webrtc",
      brain: "agent-consult",
      instructions: "Speak warmly and keep answers brief.",
    },
  },
}
```

`webrtc` is client-owned for OpenAI-capable browser and iOS clients. `gateway-relay` keeps provider audio on the Gateway; Android realtime Talk requires that transport. Set `brain: "agent-consult"` when the realtime provider should route tool, memory, and current-information work through OpenClaw policy.

## Verify and recover

1. Inspect the runtime's Talk catalog to confirm the provider, supported session shape, and readiness before changing configuration.
2. Start a device or browser Talk session and verify listening, response, playback, and interruption behavior without placing a carrier call.
3. If the selected provider is unavailable, choose a provider shown as ready in the catalog or resolve its missing credential or plugin prerequisite, then repeat the session check.
4. If speech cuts off too early or lingers too long, adjust `silenceTimeoutMs` gradually and retest on the target device.

## Sources

- OpenClaw Talk mode: https://docs.openclaw.ai/nodes/talk
- ElevenLabs documentation: https://elevenlabs.io/docs
- ElevenLabs Conversational AI overview: https://elevenlabs.io/docs/conversational-ai/overview
