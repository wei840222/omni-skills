---
name: alexa
description: "Control Alexa smart home devices, automate routines, and guide custom voice skill development. Use when working with device naming, rooms/groups, routines, privacy controls, troubleshooting, and Alexa Skills Kit certification basics."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔊"}'
---

## Device Control

**Naming for reliable control:** Location + device type. "Kitchen light", "Bedroom fan". Use descriptive names instead of model numbers.

**Room-based commands:**
- "Turn off the bedroom" (all devices in room)
- "Turn on downstairs lights" (group)
- "Set living room to 72" (thermostat)

**Protocol hierarchy:** Matter > Zigbee > Wi-Fi. Built-in Zigbee hubs: Echo Plus, Echo 4th gen, Echo Show 10.

**Device not responding?** Check Alexa app → Devices → find device → verify online status. Re-discover if needed.

## Routines

**Create via:** Alexa app → More → Routines

**Triggers:**
- Voice phrase (unique, not similar to built-in commands)
- Schedule (time, sunrise/sunset)
- Device state (door unlocks, motion detected)
- Location (geofence enter/exit)
- Alarm dismissed

**Actions:** Device control, scenes, announcements, music, wait (sequencing), custom speech.

**Routine fails?** Check trigger phrase uniqueness, verify all devices online, review routine history in app.

## Shortcuts Integration

**Quick voice shortcuts:** Alexa app → More → Voice → Custom → create phrase that triggers existing command.

**Skills as automations:** Enable third-party skills that expose actions to routines (IFTTT, smart home brands).

**Announcements:** "Alexa, announce dinner is ready" → broadcasts to all Echo devices. Useful in routines.

## Smart Home Setup

**Adding devices:**
1. Enable brand's skill in Alexa app
2. Link account if required
3. "Alexa, discover devices" or Devices → + → Add Device
4. Assign to room (critical for room-based commands)

**Groups vs Scenes:**
- Groups: multiple devices, same action ("turn off downstairs")
- Scenes: multiple devices, preset states ("movie time" → dim lights, close blinds)

**Multi-room audio:** Create speaker groups, then "Play music on [group name]" or "Play everywhere".

## Skill Development

**When building custom skills:**
- Required intents: AMAZON.HelpIntent, AMAZON.StopIntent, AMAZON.CancelIntent, AMAZON.FallbackIntent
- Test in simulator AND on physical device (simulator misses edge cases)
- 10-20 sample utterances per intent minimum
- Voice-first: design for auditory interactions rather than visual screens

**Certification blockers:** Example phrases that fail to execute exactly as written, generic help intent, missing privacy policy.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| "Device not responding" | Check Wi-Fi, verify in Alexa app, re-discover |
| Routine doesn't trigger | Rename trigger phrase, check routine history |
| Wrong device activates | Rename devices to be more distinct |
| Skill timeout | Check Lambda CloudWatch logs, increase timeout |
| "I don't know that" | Add more sample utterances to intent |

## Privacy Controls

**Voice history:** Alexa app → Privacy → Review Voice History. Enable auto-delete (3 or 18 months).

**Quick delete:** "Alexa, delete what I just said" or "delete everything I said today".

**Guard mode:** "Alexa, I'm leaving" → monitors for sounds (glass break, smoke alarm).

---

## When to Load More

| Situation | When to load | Reference |
|-----------|--------------|-----------|
| Full command list by category | User asks for specific Alexa voice commands | `references/commands.md` |
| Smart home protocols, setup, troubleshooting | User needs help connecting devices or debugging smart home | `references/smart-home.md` |
| Building custom skills, Lambda, certification | User is developing a custom Alexa voice skill | `references/development.md` |
| Official product and developer sources | Need current Alexa Help or ASK certification URLs | `references/sources.md` |
