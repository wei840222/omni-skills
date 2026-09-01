# Voice provider setup

Load this reference after the user selects a provider. Use provider consoles only after the user authorizes the associated account change, purchase, or credential creation.

## Twilio

1. Create or select a Voice-capable Twilio number.
2. Obtain the Account SID and Auth Token from the Twilio Console.
3. Configure a public webhook endpoint in OpenClaw, then point the number's Voice URL at it.
4. Run the OpenClaw Voice Call setup and dry-run smoke checks before placing a live call.

Official documentation: https://www.twilio.com/docs/voice

## Telnyx

1. Create a Call Control application and attach a voice-capable number.
2. Obtain the API key, connection ID, and Mission Control Portal webhook public key.
3. Configure the public webhook and preserve signature verification.
4. Run OpenClaw setup and its dry-run smoke check.

Official documentation: https://developers.telnyx.com/docs/voice

## Plivo

1. Create or select a Voice-capable number and application.
2. Obtain the auth ID and auth token through the provider's credential workflow.
3. Set a public webhook URL and validate the OpenClaw configuration before live calls.

Official documentation: https://www.plivo.com/docs/voice/

## ElevenLabs for device Talk TTS

For device Talk mode, configure ElevenLabs in `talk.providers.elevenlabs`; use `references/talk-mode.md` for the OpenClaw configuration shape. Confirm the available voice and model in the ElevenLabs account before setting them.

Official documentation: https://elevenlabs.io/docs
