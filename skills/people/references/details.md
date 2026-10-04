# Details — thirty-second filter

Record a fact only if it would change the first thirty seconds of the next conversation.

## Passes

- Father's surgery next month
- Does not drink
- Worried about the product pivot
- Preferred channel is Signal, not email

## Fails

- "Nice person"
- "We talked about work"
- Generic personality labels
- Transcripts of the whole chat

At `sensitive_details: minimal`, store that a sensitive topic exists ("health topic — do not raise"), not the clinical or financial content. See `privacy.md`.
