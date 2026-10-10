# Feedback system — Meditate

## Interpreting user responses

### Explicit positive

Phrases indicating value:

- “That’s useful” / “Good observation”
- “I hadn’t thought of that”
- “Yes, let me look into that”
- Taking follow-up thought based on the insight (user-initiated)

**Action:** Prioritize topic; continue similar meditations.

### Explicit negative

Phrases indicating no value:

- “Not relevant” / “Don’t care about that”
- “Exclude topic X” / “Don’t think about X”
- “That’s not helpful”
- Dismissive response

**Action:** Demote or exclude topic; note in `<state_root>/feedback.md`.

### Neutral

- “OK” / “Noted”
- Brief acknowledgment
- No follow-up

**Action:** Keep topic at current priority.

### Silence

No response to an insight within about 24 hours (host-time estimate).

**Action:**

- After 1 silence: no change
- After 2 consecutive: reduce frequency
- After 3 consecutive: pause meditations and ask if they are still useful

## Rhythm adjustment

```text
current_frequency = base_frequency × engagement_factor

engagement_factor:
  80%+ positive → 1.2 (more frequent)
  50–80% positive → 1.0 (maintain)
  20–50% positive → 0.7 (less frequent)
  <20% positive → 0.3 (rare; ask about continuing)
```

Apply factors as soft guidance when deciding whether to generate a new insight.

## Confirmation prompts

When direction is unclear after several mixed signals, ask:

```text
🧘 Quick check-in

My recent meditations focused on [topics].
Have these been useful? Should I:
A) Continue this direction
B) Focus more on [alternative]
C) Reduce meditation frequency
D) Exclude [topic] from meditation
```

Ask only after **5+** meditations with mixed or unclear feedback.

## Recovery from a bad state

If the user seems annoyed or says meditations are not useful:

1. Immediately reduce to minimum frequency (or pause).
2. Ask for explicit guidance on topics.
3. Reset profile confidence toward `unknown`.
4. Restart with 1–2 minimal observations.
5. Expand again only after a clear positive signal.
