# Feelings tracking system

Load this file when logging check-ins, expanding emotion vocabulary, or maintaining triggers / helps / patterns files under `<state_root>/`.

## Core behavior

- User shares how they feel → log with context under `<state_root>/log/`
- User asks about patterns → surface insights from their own files
- Proactively check in only during windows the user already marked difficult
- Create `<state_root>/` via the SKILL.md State location resolver before the first write

## File structure

```text
<state_root>/
├── log/
│   └── YYYY/
│       └── MM/
│           └── DD.md
├── patterns.md
├── triggers.md
├── helps.md
└── insights.md
```

All runtime paths use `<state_root>/...`. Do not hard-code `~/feelings/` outside the resolver section in `SKILL.md`.

## Feeling entry format

```markdown
# log/YYYY/MM/DD.md
## Morning — 8:00 AM
Feeling: Anxious, 6/10
Context: Big presentation today
Body: Tight chest, restless
Thought: "What if I mess up"

## Afternoon — 2:00 PM
Feeling: Relieved, calm, 8/10
Context: Presentation went well
Note: Was overthinking this morning

## Evening — 9:00 PM
Feeling: Content, tired
Context: Good day overall
Grateful: Positive feedback from team
```

Minimum fields when logging: **Feeling**, **Intensity (1–10)**, **Context**. Capture **Body** whenever offered or when intensity ≥ 7.

## Quick check-in

Prompt shape: "How are you feeling?"

Capture:

1. emotion name(s)
2. intensity 1–10
3. brief context / trigger
4. time of day
5. body sensation when available

Then append to today's `<state_root>/log/YYYY/MM/DD.md`.

## Emotion vocabulary

Help expand beyond good/bad when the user is stuck on labels:

- Anxious, worried, nervous, overwhelmed
- Sad, lonely, disappointed, grief
- Angry, frustrated, irritated, resentful
- Happy, joyful, excited, peaceful
- Tired, drained, exhausted, burned out
- Hopeful, motivated, inspired, curious

Offer two or three options; let the user pick or correct.

## Triggers tracking

```markdown
# triggers.md
## Negative
- Work deadlines → anxiety
- Poor sleep → irritability
- Social media → comparison / low mood
- Skipping exercise → low energy

## Positive
- Morning walk → calm
- Time with friends → joy
- Completing tasks → satisfaction
- Creative work → flow state
```

Write only patterns the user confirmed. Mark hypotheses as provisional until seen ≥ 3 times.

## What helps

```markdown
# helps.md
## When Anxious
- Deep breathing (works fast)
- Walk outside
- Talk to a trusted person
- Write it out

## When Sad
- Stay connected (avoid isolation)
- Music
- Gentle movement even when motivation is low

## When Overwhelmed
- Make a short list
- Do one small next action
- Ask for help

## General
- Protect sleep
- Move the body
- Talk rather than bottle
```

Prefer the user's verified helps over this starter list. After a hard episode, ask once: "Did anything help enough to save?"

## Patterns

```markdown
# patterns.md
## Time-Based
- Sundays: often anxious (week ahead)
- Mornings: better after exercise
- Late nights: tendency to spiral

## Seasonal
- Winter: lower baseline mood
- Need more social effort Dec–Feb

## Correlations
- Sleep < 6h → next day irritable
- No exercise 3+ days → low mood
- Alcohol → next day anxiety
```

Pattern bar: call something a pattern only after repeated evidence in the user's logs (default ≥ 3 occurrences or user confirmation).

## What to surface

- "You've logged anxious 4 times this week"
- "Last time you felt this way, walking helped (helps.md)"
- "Sleep notes under 6h may be linked to today's irritability"
- "Sundays show up as harder in your patterns — want a lighter plan?"

Always tie claims to the user's files. If logs are thin, say so and offer a fresh check-in.

## Proactive check-ins

Use only when tracking is already active and a known difficult window appears:

- Morning opener the user requested
- After a noted difficult event
- When patterns.md flags a recurring hard slot
- Celebrate good streaks the user cares about

## Insights over time

```markdown
# insights.md
## Learned about myself
- Anxiety is often louder than the outcome
- Alone time recharges me
- Exercise is non-negotiable for mood
- Sleep debt compounds

## Growth
- Noticing feelings earlier
- Asking for help more often
- Less reactive when tired
```

Update insights sparingly after reviews, not after every check-in.

## What to track

- Emotion name(s)
- Intensity (1–10)
- Context / trigger
- Physical sensations
- What helped (after)

## Progressive enhancement

1. Daily or on-demand check-ins
2. Notice triggers and what helps
3. Weekly pattern review
4. Personal toolkit in helps.md / triggers.md

## Mandatory practices

- Accept emotions neutrally without judgment
- Acknowledge current feelings; keep the stated emotion in frame and skip forced positive reframes
- Address and log physical sensations alongside emotions when present
- Prioritize tracking especially during difficult or negative states
- Keep secrets and credentials out of logs; store pointers only if the user pastes sensitive material by mistake
