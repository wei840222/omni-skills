---
name: siri
description: >
  Troubleshoot Siri activation and transcription failures, configure Siri-friendly
  HomeKit and Shortcuts names, implement App Intents / SiriKit, and diagnose
  unresponsiveness across iPhone, HomePod, Watch, and CarPlay. Use when Hey Siri
  stops listening, a HomeKit device name fails by voice, a Shortcut will not run
  by Siri, or an iOS app needs parameterized voice commands. Prefer `homepod`
  for HomePod-specific audio and hub recovery, `smart-home` for cross-vendor
  Home architecture, and `ios` for broader app lifecycle or entitlement work.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🗣️","displayName":"Siri"}'
  related-skills: '{"homepod":"HomePod-specific Siri, audio, hub, and automation recovery.","smart-home":"Cross-vendor smart-home architecture beyond Apple Home voice control.","ios":"Broader iOS app lifecycle, entitlements, and platform debugging.","apple-health":"Health data workflows when App Intents log health metrics.","voice-notes":"Structured note capture when voice transcripts need knowledge organization."}'
---

# Siri

Voice-first guidance for activation, HomeKit naming, Shortcuts, and App Intents.
This skill teaches configuration and diagnosis; it does not mutate the user's
Apple devices or accounts.

Optional persistent notes live under a resolved `<state_root>/siri/` tree outside
this package. Never write runtime state into the skill tree.

## State location

Siri preferences, device-naming inventories, Shortcut test logs, and App Intent
notes are persistent user state. Resolve one `<state_root>` before any read or
write:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/siri/`, `<workspace>/memory/siri/`, `~/siri/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and the user wants durable Siri notes, create
   `<workspace>/siri/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the shell cwd.
5. Prefer portable `<state_root>` paths; never hard-code host-specific absolute
   roots. Skill resources stay under `references/`; never treat them as writable
   state.

Optional files under the selected root: `<state_root>/memory.md`,
`<state_root>/device-names.md`, `<state_root>/shortcut-tests.md`,
`<state_root>/intent-notes.md`. Ask before creating or modifying persistent
notes.

## Main workflow

1. Classify the ask: activation / transcription, HomeKit naming or scenes,
   Shortcuts voice trigger, or App Intents / SiriKit development.
2. Capture device model, OS version, language, and one failing phrase.
3. Apply the narrowest reversible check from the matching reference, then
   retest the same phrase before escalating.

## Quick start

1. Confirm the failing phrase, device, and OS version.
2. If activation fails, use Activation & Setup + Troubleshooting below.
3. If a HomeKit name fails by voice, load `references/homekit.md`.
4. If a Shortcut will not trigger, load `references/shortcuts.md`.
5. If the ask is app development, load `references/development.md` and
   `references/sources.md`.

Prefer `homepod` when the symptom is HomePod audio/hub only; prefer
`smart-home` for non-Apple hubs or VLAN design; prefer `ios` for
entitlements and App Store lifecycle.

## Activation & Setup

**Trigger methods:**

- Hold Side / Home button
- "Hey Siri" (always-listening when enabled)
- "Siri" alone (iOS 17+ Listen for "Siri" or "Hey Siri")

**Hey Siri not working?** Check Settings → Siri & Search → Listen for, retrain
the voice model, test the mic with Voice Memos, and disable Low Power Mode.
Confirm language matches the spoken phrase.

## Command Patterns

**Structure:** Action + Target + Details

- "Call Mom on speaker"
- "Set a timer for 12 minutes"
- "Remind me to buy milk when I get home"

**Discovery:** "What can I say?" or "What can you do with [App]?"

**Corrections:** Say "Change that to..." after Siri transcribes wrong.

## Smart Home (HomeKit)

**Device naming:** Short, distinct, no special characters. Prefer
"Kitchen light" over "Philips Hue A19 Kitchen #2".

**Room-aware commands:**

- "Turn off the lights" (current room on HomePod)
- "Turn off the bedroom lights" (specific room)
- "Turn off downstairs" (zone)

**Scenes:** Name for voice: "Good morning", "Movie time", "I'm leaving".
Trigger with "Hey Siri, [scene name]".

**Schedules:** "Turn on porch light at sunset", "Lock doors at 10 PM".

**Security accessories** (locks, garage): May require device unlock or HomePod
voice recognition before completing.

For HomePod-only hub / multiroom recovery, prefer `homepod`. For cross-vendor
hub and VLAN design, prefer `smart-home`.

## Shortcuts Integration

**Naming for voice:**

- Short (2–3 words)
- Unique (avoid similar sounds)
- No punctuation
- Test pronunciation aloud before relying on it

**Triggering:** Say the shortcut name. Works on iPhone, HomePod, Apple Watch,
and CarPlay when the shortcut is Siri-enabled.

**User input:** Use "Ask for Input"—Siri speaks the prompt and waits.

**Parameterized commands (iOS 16+):** App Intents allow phrases like
"Log 8 glasses of water" where the number is parsed. Requires developer
implementation in the app.

**Feedback:** End shortcuts with "Show Result" for spoken response or
"Show Notification" for silent confirmation.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Siri doesn't hear me | Check mic, remove case, disable Bluetooth audio |
| Wrong transcription | Speak slower, reduce noise, verify language setting |
| "I can't do that" | Feature unsupported or app not Siri-enabled |
| HomeKit device not responding | Check Home app, device online, restart Home hub |
| Shortcut won't run by voice | Rename shorter; confirm Siri toggle in shortcut settings |

## Power Tips

- **CarPlay:** Hands-free after the beep
- **AirPods:** Squeeze stem or say "Siri" when enabled
- **Type to Siri:** Settings → Accessibility → Siri → Type to Siri
- **Announce notifications:** HomePod / AirPods can read incoming messages
- **Intercom:** "Hey Siri, intercom I'm home" broadcasts to HomePods in the home

## When to Load More

| Situation | Reference |
|-----------|-----------|
| Full command list by category | `references/commands.md` |
| HomeKit setup, scenes, zones, troubleshooting | `references/homekit.md` |
| Building Shortcuts, triggers, automation | `references/shortcuts.md` |
| SiriKit, App Intents, developer integration | `references/development.md` |
| Verified official sources for Gate 6 claims | `references/sources.md` |

## Safety

- Do not claim account changes, factory resets, or remote HomeKit mutations
  without explicit user confirmation.
- Treat spoken phrases and device names as personal context; keep them in
  `<state_root>` only when the user opts in.
- Prefer reversible checks before reset or re-pairing.
