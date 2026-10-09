# Setup — Sentiment Analysis

Read this when `<state_root>/` does not exist or is empty, or on first-run
onboarding after the immediate user question is answered.

## Attitude

Be the user's eyes and ears on public opinion so they can keep building while
someone watches what people say.

## Data storage

All durable tracking data lives under `<state_root>/`. Tell the user their
tracking history stays on their machine unless they explicitly export it.

## Priority order

### 1. First: help with what they asked

If they asked "what are people saying about X?" — finish that analysis and show
value immediately.

### 2. Then: offer ongoing tracking (within the first 2–3 exchanges)

After helping, ask naturally:

- "Want me to keep an eye on this ongoing? I can check daily/weekly and alert on changes."
- "Should I jump in when you mention [topic], or only when you ask?"

Save the answer to host shared memory when the workspace has one, and to
`<state_root>/memory.md` for this skill's tracker.

### 3. Then: understand monitoring needs

Through conversation, learn:

- Entities (brands, products, competitors, crypto, topics)
- Platforms that matter for their domain
- Update cadence
- What counts as alert-worthy for them

### 4. Finally: detail level (only if they want)

Some users want theme breakdowns; others want good/bad/neutral. Adapt.

## What to learn into state

Write to `<state_root>/memory.md` as preferences stabilize:

- **Entities**: name, type, keywords, platforms, schedule
- **Alert thresholds**: default 20% negative above baseline unless overridden
- **Report preferences**: detailed vs summary, frequency, delivery channel
- **Platform priorities**: ordered source list for their domain

## Example first interaction

User: "What are people saying about Notion lately?"

1. Run the multi-source analysis and show the report.
2. Offer monitoring: weekly checks plus complaint-spike alerts.
3. If they accept, create/update `<state_root>/memory.md` and
   `<state_root>/entities/notion.md`. If they decline, stay one-shot.

## Confirmations

When monitoring is enabled, prefer:

- "Got it — Notion sentiment every Monday; I will ping on meaningful shifts."
- "Added to your tracking list — you are monitoring 3 entities."

Prefer outcome language over internal path dumps. If the user asks where data
lives, answer with the resolved `<state_root>` path.
