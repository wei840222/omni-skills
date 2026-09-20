# Notifications — Proactive Speech

Spoken notifications interrupt whatever the user is doing; each one is a claim that this exact moment mattered. Default: most notifications belong in text, silently.

## Gate Before Speaking

Speak only when both hold:

1. **Time-sensitive** — acting later loses value (a meeting in 5 minutes, a timer, a failing deploy).
2. **Actionable or subscribed** — the user can do something now, or explicitly asked to be told aloud.

Everything else goes to text without comment. Quiet hours (stored under the `contexts` preference area) suppress all but critical; critical = safety, security, or the user's own standing "always tell me about X".

## Utterance Shape

- Source first, payload second: "Calendar: standup in five minutes." The source primes the listener before the fact lands — audio has no sender icon.
- Two sentences max: about 25 words / 10 seconds at the 2.5 words-per-second base (SKILL.md rule 1).
- End with the action when one exists: "...I can snooze it."
- Start directly with the core message — the audio starting already took their attention; spend the words on content.

## Batching and Repeats

- Multiple pending → one summary utterance ("Three updates: two builds passed, one meeting moved."), details on request — consolidate into a single summary utterance.
- Repeat policy: once. A critical unacknowledged alert repeats once more after a gap, then escalates channel (text, push) — escalate to text after one repetition.
- Timers and alarms: name the timer, not just the event ("Pasta timer done") — timers outlive the context that set them.
- Recurring notifications the user talks over or dismisses twice: that is a two-signal mute for that source (SKILL.md rule 7); confirm and store it.

## Privacy Aloud

Shared-space rules live in `audiences.md`; the notification-specific rule:

- Speak secrets only when explicitly requested aloud: "You have a verification code" without the digits — the code itself goes to text unless the user asked for it aloud.
- Financial amounts, medical content, and third-party message bodies: headline without payload ("New message from Sam") unless the `contexts` config says this space is private.
