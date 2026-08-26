---
name: find
description: Trigger this skill to locate specific information, entities, or sources when the exact location is unknown. It executes a progressive search, validates findings, and iterates until the target is found or all paths are exhausted.
metadata:
  openclaw: '{"emoji":"🔎","displayName":"Find"}'
  related-skills: '{"loop":"For iterating until success criteria are met","cycle":"For multi-phase workflows"}'
---

## Pattern

```
Need → Clarify → Search → Validate → [Found? Deliver : Expand]
```

Keep searching until found or exhausted. Start narrow, expand progressively. Validate before delivering.

## When to Use

- User needs to find something specific
- Location or source is unknown
- "Find me...", "Where can I get...", "I need to find..."

**Alternative:** For things you already know, simple lookups, or casual browsing, use direct search commands instead.

## Setup

Before searching, clarify:

| Element | Why |
|---------|-----|
| What exactly? | Ensure precision of the target |
| Success criteria | How will we know it's right? |
| Constraints | Budget, location, time, format |
| Already tried? | Exclude previously searched paths |

If user is vague → ask ONE clarifying question, then start.

## Search Expansion

> **Loading Instructions:** Before beginning a complex search or if initial obvious sources fail, silently load `references/domain-knowledge.md` to review academic information-seeking models (like Information Foraging and Ellis's activities) to formulate better search strategies.

Start narrow, expand if not found:

```
1. Obvious sources → Direct lookup, known locations
2. Specialized sources → Domain-specific databases, expert communities  
3. Alternative queries → Different words, related concepts
4. Indirect paths → Who would know? What links to this?
5. Ask human → More context, different angle
```

Each expansion: try multiple sources in parallel when possible.

## Validation

Before delivering, verify:
- Is this actually what was asked for?
- Is the source reliable?
- Is it current/valid?
- Any caveats user should know?

If uncertain → say so. "Found X but not 100% sure it's what you need."

## Delivery

```
FOUND: [what]
WHERE: [source]
CONFIDENCE: [high/medium/low]
CAVEATS: [if any]
```

If multiple results: summarize and let user choose.

## Not Found

If exhausted all paths:
1. Report what was tried
2. Closest alternatives found
3. Suggest different approach or more context needed
