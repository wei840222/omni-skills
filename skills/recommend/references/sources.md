# Where to Find User Context

Before recommending, search these sources in order:

## 1. Memory Files

Primary preference storage:
- `<state_root>/*.md` — Category-specific files (`movies.md`, `food.md`, etc.)
- `<state_root>/memory.md` — Durable preference patterns
- Decision history from the `decide` skill when installed and authorized

Also consider host-shared `MEMORY.md` only with separate consent; it is outside
`<state_root>`.

**Search for:** Explicit likes/dislikes, past choices, stated values.

## 2. Conversation History

Recent and relevant discussions:
- Direct statements: "I love X", "I hate Y"
- Reactions to suggestions: accepted, modified, rejected
- Complaints and praise about past recommendations
- Context clues: time constraints, mood, occasion

**Search for:** Pattern of choices, implicit preferences, feedback on past recommendations.

## 3. Behavioral Signals

Actions speak louder than words:
- Actual selections compared to stated preferences
- Frequency of certain choices
- Exceptions to stated preferences
- Abandoned or regretted decisions

**Search for:** Gaps between stated and revealed preferences.

## 4. Ask Directly

When data is insufficient:
- Closed questions: "Do you prefer A or B?"
- Constraint discovery: "What's your budget/time/limit?"
- Priority ranking: "Speed, quality, or price—pick two"

**Rule:** Targeted questions beat open-ended prompts. "Sweet or savory?" yields
more signal than "What do you want?"

---

**Output before proceeding:** List 3-5 relevant signals found. If fewer than three,
ask targeted questions.
