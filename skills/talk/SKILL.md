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

1. Identify the target: device Talk mode for continuous voice chat, realtime Talk, or the Voice Call plugin for carrier calls.
2. Load `references/talk-mode.md` for device Talk or realtime sessions; use its provider catalog check before proposing configuration.
3. Load `references/voice-call.md` for carrier calls, then load `references/providers.md` only for the selected carrier or device-TTS provider.
4. Present the smallest viable configuration plus its verification command. Use OpenClaw's credential surface for secrets and placeholders in all examples.

## Verification and boundaries

Before changing a configuration, confirm the selected provider is available and use the matching reference's verification path. Treat provider-account changes, number purchases, public-webhook exposure, and live calls as separate user-authorized actions. Start carrier-call verification with a dry run and enable inbound calling only after defining its caller policy and controls.

This skill does not persist user state; OpenClaw retains configuration through its runtime-managed configuration surface.
