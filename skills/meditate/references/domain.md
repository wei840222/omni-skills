# Domain rules — Meditate

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for setup.

```text
<state_root>/
├── profile.md         # User type, focus areas, rhythm preferences
├── topics.md          # Active meditation topics with priority
├── insights.md        # Pending insights to present (queue)
├── feedback.md        # User reactions to past insights
└── archive/           # Delivered insights with outcomes
```

## Scope

This skill only:

- Reads conversation history the user already shared in-session
- Reads and writes memory files under `<state_root>/`
- Generates text reflections and questions
- Stores insights in the local queue and archive

This skill stays inside reflection:

- Prefer observations and questions over commands or scripts
- Keep file writes inside `<state_root>/`
- Keep outbound messages, notifications, and external service calls out of meditation output
- Keep executable code and on-behalf-of user actions out of meditation output

## Package integrity

Leave `SKILL.md` unchanged at runtime. Persist only under `<state_root>/`.

## Core rules

### 1. Sandbox is absolute

- Generate text observations and questions only.
- Prefer “What if we considered X?” over “I’ll do X”.
- Keep output as pure reflection rather than a staged action plan.
- Run `references/sandbox.md` before every present.

### 2. Adaptive rhythm

| User activity | Meditation frequency |
|---------------|----------------------|
| Very active (daily chats) | 1–2× per night, brief |
| Moderate (weekly) | 2–3× per week, medium |
| Low (monthly) | 1× per week, comprehensive |
| No feedback on insights | Reduce frequency |
| Positive feedback | Maintain or slightly increase |

Cadence is guidance, not a hard scheduler. If the host already ran a recent meditation and the queue is full, skip generation.

### 3. Start small, expand with permission

- First meditations: 1–2 short observations
- After positive feedback: expand breadth
- After the user asks to exclude topic X: remove X from topics
- After “this is useful”: prioritize similar topics
- Confirm preferences through feedback instead of assuming them

### 4. Detect user profile

Observe conversation patterns to identify a working profile:

| Profile | Focus areas |
|---------|-------------|
| Entrepreneur | Projects, priorities, strategy gaps |
| Developer | Architecture, code quality, tech debt |
| Creative | Prompt patterns, style evolution, tools |
| Personal | Calendar, habits, goals mentioned |
| System | Configurations, workflows, automations |

Store the detected profile in `<state_root>/profile.md`. Raise confidence only after confirmatory feedback. Multiple profiles may coexist.

### 5. Meditation output format

Present insights as questions or observations:

```text
🧘 Meditation Insights

**Observation:** [what you noticed]
**Question:** [something to consider]
**Context:** [brief why this might matter]

---
Feedback: Was this useful? (helps me adjust)
```

### 6. Feedback integration

| User response | Action |
|---------------|--------|
| “Useful” / positive | Log topic as high-value, continue |
| “Not relevant” | Demote topic priority |
| “Exclude topic X” / “don’t think about X” | Remove X from topics entirely |
| “Think more about Y” | Prioritize Y |
| Silence | Reduce frequency slightly after repeated misses |

Detailed interpretation lives in `references/feedback.md`.

### 7. Insight queue management

- Maximum **3** pending insights at any time
- Present oldest first
- Archive after presenting (with user reaction when available)
- Keep each generated insight distinct from recent archive entries

### 8. Privacy boundaries

- Meditate only on data the user shared directly in reachable context
- Analyze external sources only with explicit permission for that turn
- Prefer non-personal summaries in the insight queue
- Clear archive entries older than **30 days** when the archive is touched

## Common traps → recovery

| Trap | Recovery |
|------|----------|
| Action items instead of reflections | Reframe as observation + question; drop imperative plans |
| Too frequent when user disengages | Apply silence rules; pause after 3 consecutive silences |
| Assumed topic interest | Demote until positive feedback |
| Executable content creep | Re-run sandbox checklist; omit if still doubtful |
