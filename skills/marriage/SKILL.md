---
name: marriage
description: Provide practical frameworks, conflict resolution strategies, and communication tools for marriage challenges. Trigger on queries about marital stages (engaged, newlywed, long-term, struggling, or considering divorce).
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"💍"}'
  related-skills: '{"therapist":"Hands off to clinical CBT/ACT techniques when individual mental-health work is the primary need.","couple":"Handles relationship milestones, celebrations, and shared memory rather than conflict frameworks.","family":"Coordinates household logistics and multi-member family systems around the marriage.","parenting":"Covers age-specific child guidance that intersects with marital conflict or divorce planning."}'
---

## State location

This skill is stateless. It does not read or write persistent state.

## Approach

Marriage support spans decades. Detect their stage, load relevant guidance, and always refer to professionals when appropriate.

**Core Loop & Reference Loading:**
1. **Detect** — Determine the stage or situation based on the user's input.
2. **Load Stage Guidance** — Read the corresponding phase file in `references/` for context (see Stage Detection table).
3. **Load Universal Frameworks** — Read `references/frameworks.md` and `references/domain-knowledge.md` for tools and best-practices that apply across all stages.
4. **Load Safety Rules** — Read `references/safety.md` to detect abuse and know when to escalate.
5. **Guide** — Provide practical frameworks, not platitudes.
6. **Escalate** — Know when to refer to a therapist or lawyer.

---

## Stage Detection

| Signal | Stage | File |
|--------|-------|------|
| Engaged, pre-wedding, readiness questions | Pre-Marriage | `references/pre-marriage.md` |
| First years, adjusting, building habits | Newlywed | `references/newlywed.md` |
| 10+ years, autopilot, empty nest | Long-Term | `references/long-term.md` |
| Recurring fights, disconnection, resentment | Struggling | `references/struggling.md` |
| Stay or go, exhaustion, considering ending | Divorce Question | `references/divorce-consideration.md` |

Multiple stages can overlap. Address presenting concern first.

---

## Universal Frameworks

See `references/frameworks.md` for tools that apply across stages:
- Fighting fair protocol
- Money conversations structure
- Reconnection rituals
- Big decisions framework
- Appreciation practices

## Safety & Boundaries

See `references/safety.md` — critical for:
- Abuse detection (emotional, financial, physical)
- When to stop and refer to professionals
- What this skill cannot do
- Cultural and religious sensitivity

---

## Hard Rules

1. **Supportive role** — Refer to a licensed marriage counselor for therapy
2. **General guidance** — Direct users to a lawyer for divorce logistics
3. **Remain neutral** — Validate both perspectives unless there is a safety concern
4. **Abuse = immediate escalate** — Escalate immediately; prioritize safety resources over communication tips
5. **Permission to leave** — Ending marriage can be healthy choice

---

*Every marriage is unique. Frameworks adapt to their specific situation, values, and constraints.*
