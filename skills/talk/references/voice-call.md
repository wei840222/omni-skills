# OpenClaw Voice Call plugin

Load this reference when the user wants inbound or outbound carrier calls. It covers OpenClaw's bundled Voice Call plugin, not browser or device Talk mode.

## Prerequisites

- Select a supported carrier provider: Twilio, Telnyx, Plivo, or `mock` for local development.
- Keep provider credentials in the OpenClaw SecretRef credential surface or the provider's supported environment-variable path.
- Prepare a publicly reachable webhook URL for Twilio, Telnyx, or Plivo. Carrier providers cannot deliver webhooks to loopback or private-network addresses.

## Configuration shape

Put Voice Call configuration under `plugins.entries.voice-call.config`. Use only the provider block needed for the selected provider.

```json5
{
  plugins: {
    entries: {
      "voice-call": {
        enabled: true,
        config: {
          provider: "twilio", // "telnyx" | "plivo" | "mock"
          fromNumber: "+15550001234",
          inboundPolicy: "allowlist",
          allowFrom: ["+15550005678"],
          twilio: {
            accountSid: "<twilio-account-sid>",
            authToken: "<secret-ref-or-provider-secret>",
          },
          serve: { port: 3334, path: "/voice/webhook" },
          publicUrl: "https://voice.example.com/voice/webhook",
        },
      },
    },
  },
}
```

For Telnyx, provide its API key, connection ID, and webhook public key. For Plivo, provide its auth ID and auth token. Keep signature verification enabled for carrier traffic. Use `mock` while testing a local integration without network calls.

## Verify safely

1. Run `openclaw voicecall setup --json` to check enablement, provider credentials, public-webhook exposure, and audio-mode compatibility.
2. Run `openclaw voicecall smoke --to "+15555550123"` as a dry run.
3. Place a short test call only after the owner explicitly approves the destination and cost.

Select either `streaming` or `realtime` audio for a call; they cannot be enabled together. For production, use a stable public URL and explicit inbound caller controls.

## Recovery

- If setup reports missing credentials, add only the named provider credential through the configured secret mechanism, then rerun setup.
- If setup rejects webhook exposure, use a public HTTPS endpoint; retain signature verification rather than weakening it.
- If realtime and streaming conflict, select the one required for the call and disable the other before retrying.

## Sources

- OpenClaw Voice Call plugin: https://docs.openclaw.ai/plugins/voice-call
- Twilio Voice API: https://www.twilio.com/docs/voice/api
- Telnyx Voice: https://developers.telnyx.com/docs/voice
