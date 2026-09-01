---
compatibility: "OpenClaw Gateway with an available Talk provider or the voice-call plugin"
name: talk
description: Configure OpenClaw Talk mode or Voice Call telephony. Use when a user wants continuous voice chat, TTS playback, inbound or outbound phone calls, a voice provider, or voice-call setup and diagnostics.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📞"}'
  related-skills: '{"api":"Covers provider API integration and webhook diagnostics beyond the OpenClaw voice configuration.","setup":"Covers general OpenClaw installation and configuration outside voice-specific workflows."}'
---

## Use this skill

1. Identify the target: device Talk mode for continuous voice chat, or the Voice Call plugin for carrier calls.
2. For device Talk mode, load `references/talk-mode.md` before proposing provider configuration.
3. For carrier calls, load `references/voice-call.md` and then `references/providers.md` for the selected provider.
4. Present the smallest viable configuration and verification command. Keep secrets in OpenClaw's credential surface rather than examples or source-controlled files.

## Operating boundaries

Treat a configuration edit, provider-account change, number purchase, public-webhook exposure, and placement of a real call as separate user-authorized actions. Use a dry-run verification before an actual outbound call. Configure inbound calls with an explicit policy and caller controls before enabling them.

This skill is stateless and does not store local configuration or persistent user state.
