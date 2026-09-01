---
name: openclaw-workspace
description: Audit and improve an OpenClaw workspace's agent behavior, bootstrap files, memory, tools, skills, and automation boundaries. Use when a user asks why an OpenClaw agent behaves a certain way or requests a workspace audit, redesign, or targeted improvement.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧩"}'
  related-skills: '{"analysis":"Structures evidence-backed workspace and system audits.","memory":"Designs memory architecture when recall requirements exceed this workspace audit.","proactivity":"Tunes initiative, follow-through, and automation boundaries.","self-improving":"Turns recurring corrections into durable operating improvements."}'
---


## When to Use

Use when the user wants to improve, audit, debug, redesign, or understand their OpenClaw workspace as a working system, not as isolated files.

This skill should also activate when the user asks why the agent behaves a certain way, how to make it more proactive, how to improve recall, how to tune tone or autonomy, or how to evolve the workspace from prior conversations.

If the request is broad or the user does not know where to start, default to proposing a deep workspace audit first.

## Improvement Surface

| Layer | Improve Here When | What Good Looks Like |
|------|-------------------|----------------------|
| SOUL.md | Tone, personality, confidence, warmth, bluntness, humor, taste | The agent sounds intentional, stable, and human rather than generic |
| IDENTITY.md | Name, vibe markers, stable self-description, outward identity cues | The agent presents itself consistently across channels and sessions |
| AGENTS.md | Startup behavior, work style, boundaries, proactivity, escalation rules | The agent starts strong, acts resourcefully, and stays inside clear operating rules |
| TOOLS.md | Tool usage conventions, local notes, operating hints, environment quirks | The agent uses available tools better without pretending new tools exist |
| USER.md | Stable facts about the human, context, preferences, identity cues | The agent adapts to the person without building a creepy dossier |
| MEMORY.md | Durable lessons, recurring priorities, long-term preferences, important facts | Main-session recall is sharp without becoming bloated or stale |
| memory/ daily notes | Recent context, fresh changes, current projects, recent mistakes or wins | The agent can reason from recency instead of relying only on old summaries |
| Automations / scheduled jobs | Recurring checks, proactive follow-through, idle-time maintenance | Proactivity has explicit timing and delivery behavior instead of surprise messages |
| skills/ | Capability gaps, reusable playbooks, domain-specific operating rules | Repeated problems move out of ad hoc prompting and into reusable skill behavior |

## Default Audit Output

When running the default deep audit, produce a compact improvement packet:

1. Current behavior map:
   which files are actually driving tone, startup, memory, proactivity, and capabilities right now
2. Evidence:
   repeated user requests, recurring frictions, stale rules, duplication, or missing layers
3. Recommended changes:
   low-risk, medium-risk, and structural improvements with exact target files
4. Suggested next move:
   review diffs, apply one layer only, or run a full workspace cleanup

Ensure the user leaves with a real plan tied to specific workspace files.


## References

| File | When to load |
|---|---|
| `references/core-rules.md` | When executing a deep workspace audit or fixing broad behavior issues. |
| `references/common-traps.md` | When reviewing workspace changes to avoid anti-patterns. |
| `references/best-practices.md` | When designing structural changes like boundaries, tools, or memory layers. |
