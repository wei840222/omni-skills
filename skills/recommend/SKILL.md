---
name: recommend
description: >
  Analyze past choices and stated preferences to produce contextual, ranked
  recommendations with tradeoffs and confidence. Use when the user asks for
  suggestions, choices, comparisons, or what to pick next. Prefer `shopping`
  for buy-vs-wait and purchase timing, `compare` for structured option matrices
  without preference learning, and `decide` for consequential branching choices
  that should be logged as durable decisions.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"👍"}'
  related-skills: '{"compare": "Structured side-by-side option matrices when ranking is secondary to explicit criteria.", "decide": "Log consequential branching decisions and reuse verified outcomes beyond light preference matching.", "shopping": "Purchase timing, deal validation, and return-policy checks after a product recommendation is chosen."}'
---

## State location

Recommend preference state may exist in
`<workspace>/recommend/`, `<workspace>/memory/recommend/`, or `~/recommend/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/recommend/`, `<workspace>/memory/recommend/`, `~/recommend/`.
3. If none exists and durable preference state must be created, default to
   `<workspace>/recommend/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/recommend/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

Host-shared memory such as workspace `MEMORY.md` is outside `<state_root>` and
needs separate consent. Do not store secrets, payment details, or third-party
private data in recommend state.

```text
<state_root>/
├── memory.md          # Durable preference patterns and confirmed defaults
└── <category>.md      # Optional category notes (movies.md, food.md, …)
```

## When to Use

- The user wants suggestions grounded in their history and current context
- Ranking a shortlist with explicit tradeoffs and confidence
- Resolving tension between stated preferences and recent behavior
- Not for checkout execution (`buy`), purchase timing alone (`shopping`), pure
  criteria matrices (`compare`), or durable high-stakes decision logging (`decide`)

## Core Loop

```text
Context → Preferences → Research → Match → Recommend
```

Every recommendation needs both a preference profile and researched options.

1. Resolve `<state_root>` before any state read/write.
2. Load `references/sources.md` to gather preference signals.
3. Load only the relevant section of `references/categories.md`.
4. Open `references/research-sources.md` when preference-science claims need a
   primary citation.
5. Research candidates only after the preference profile exists.

## Step 1: Context Gathering

Load and apply `references/sources.md` before recommending.

**Minimum output:** 3-5 relevant user signals. If fewer than three signals exist,
ask targeted questions before ranking.

## Step 2: Preference Extraction

From gathered context, extract:

| Dimension | Question |
|-----------|----------|
| **Values** | What matters most? (Quality, price, speed, novelty, safety) |
| **Constraints** | Hard limits? (Budget, time, dietary, ethical) |
| **History** | What worked? What disappointed? |
| **Mood** | Adventurous or safe? Exploring or comfort? |

**Output:** 3-5 bullet preference profile for this request.

## Step 3: Research Options

Research candidates only after the preference profile exists:

- Explore multiple distinct options before anchoring on one candidate
- Prefer reviews, ratings, and expert sources over single anecdotal takes
- Check whether information is current and options are actually available

**Output:** Shortlist of 3-7 viable candidates with key attributes.

## Step 4: Match & Rank

Score each candidate against the preference profile:

```text
Candidate → Values alignment + Constraint fit + History match + Mood fit
```

Disqualify anything that violates hard constraints.
Rank by total alignment across dimensions, not a single score.

## Step 5: Recommend

Present 1-3 recommendations:

```text
RECOMMENDATION: [Option]
WHY: Matches [preference], respects [constraint]
TRADEOFF: Less [X] than [Alternative]
CONFIDENCE: [Level] — based on [data quality]
```

Lead with one primary pick. Add a runner-up only when it changes the decision.

## Adaptive Learning

After each recommendation:

- Track whether the user accepted, modified, or rejected the pick
- Reinforce accepted patterns; adjust after rejection
- Note context exceptions: "Normally X, but for Y preferred Z"

Store durable learnings under `<state_root>/` (usually `<state_root>/memory.md`
or a category file) when the user wants preference memory kept.

## Handling Contradictory Preferences

When historical choices diverge from stated preferences (for example, stating
"health-conscious" while frequently choosing fast food):

- Surface the tension explicitly
- Offer options that bridge the gap, or ask whether the current occasion
  overrides the stated preference
- Temporarily weight recent revealed behavior more heavily than older stated
  values when the occasion clearly differs

## Recommendation Quality Checks

Prefer these positive checks over prohibition theater:

- Base ranking on the user profile rather than the agent's personal taste
- Balance historical and recent choices when building the profile
- Validate the occasion (casual lunch vs anniversary) before ranking
- Relax soft constraints when hard limits leave no viable options
- Re-verify preference data when signals look stale or conflicting

---

Recommendations are predictions. More verified context produces better rankings.
