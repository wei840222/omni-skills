# Core Rules

## 1. Default to Deep Audit Mode for Broad Workspace Requests

- If the user says "improve my workspace", "analyze my workspace", "why is my agent like this", or anything equally broad, start by proposing a deep audit.
- A deep audit should inspect the current workspace stack, recent memory evidence, active behavior patterns, and the biggest friction points before prescribing changes.
- If the user already names a target such as proactivity, memory, tone, or tools, audit that layer first but still map likely side effects on adjacent layers.
- The default audit order is: bootstrap behavior files first, then memory evidence, then skills, then concrete improvement proposals.
- A good audit ends with three outputs: what is driving the current behavior now, what is misaligned, and the smallest diffs that would materially improve it.

## 2. Diagnose by Layer Instead of Giving Generic Advice

- Provide specific advice by locating which file or mechanism controls that behavior instead of giving generic advice.
- Voice and personality belong in SOUL.md.
- Stable self-presentation and identity markers belong in IDENTITY.md.
- Startup routines, decision defaults, red lines, escalation rules, and proactive behavior belong in AGENTS.md; recurring work belongs in the runtime's current automation mechanism.
- Tool notes belong in TOOLS.md.
- Human-specific context belongs in USER.md.
- Durable recall belongs in MEMORY.md, while recent raw context belongs in memory/ daily files.
- Repeated domain workflows belong in skills, not in bloated root files.

## 3. Use Prior Conversations as Primary Evidence

- Before proposing workspace changes from history, search existing memory first rather than guessing from the current message alone.
- Use memory_search on MEMORY.md plus memory/*.md whenever the question depends on previous preferences, recurring mistakes, deadlines, people, or long-running work.
- If transcript-backed recall is available, use recent session evidence to identify repeated friction, repeated user corrections, and patterns worth turning into workspace rules.
- If transcript recall is not available, say so plainly and propose the smallest safe upgrade path for conversation-based improvement instead of pretending the evidence exists.

## 4. Keep Bootstrap Files High-Leverage and Compact

- AGENTS.md, SOUL.md, and TOOLS.md are bootstrap context, so every line should earn its place.
- Keep identity, startup, boundaries, and execution defaults in root files; move heavy procedures, niche runbooks, and long examples into skills or narrower supporting files.
- If behavior is inconsistent, first check for prompt bloat, duplicate rules, contradictory instructions, and stale sections before adding more text.
- Prefer one sharp rule in the right file over five overlapping paragraphs across the workspace.

## 5. Make the Smallest Change That Fixes the Behavior

- Tune the specific layer that owns the problem instead of rewriting the whole workspace.
- Personality issues should not trigger a memory rewrite.
- Identity presentation issues should not trigger an AGENTS rewrite if IDENTITY.md is the real owner.
- Memory drift should not trigger a SOUL rewrite.
- Missing capability should not be patched into AGENTS.md if it belongs in a skill.
- When proposing improvements, show concrete diffs or exact replacement blocks and explain the expected behavioral change, not just the file destination.

## 6. Tune Proactivity With Boundaries, Not With Vibes

- "Be more proactive" is not enough; define what the agent should notice, when it should act, and when it must ask first.
- Use AGENTS.md for general proactive stance; use the host scheduler or the workspace's current automation mechanism for recurring checks, follow-through, and quiet-time behavior.
- Separate internal initiative from external action: reading, organizing, checking, and drafting can often be proactive; messaging, spending, deleting, scheduling, or publishing usually still need approval.
- If a workspace feels passive, inspect startup rules, the current automation configuration, next-step behavior, and recovery patterns before adding broader instructions.

## 7. Respect Privacy, Session Boundaries, and Real Platform Behavior

- MEMORY.md is high-trust personal context and should be treated more carefully than general workspace notes.
- Only copy private long-term memory into shared-context behavior files if the user explicitly wants that tradeoff.
- TOOLS.md does not grant new tool access; it only improves how the agent uses tools that already exist.
- Conversation-driven upgrades must respect storage, privacy, and operational cost tradeoffs when enabling broader recall.
- Always ensure workspace rewrites are explicit, reviewable, and tied to a concrete reason.
