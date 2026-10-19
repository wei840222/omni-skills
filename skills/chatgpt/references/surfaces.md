# ChatGPT Surface Routing

Pick the lightest surface that fits the job. Most ChatGPT problems are routing
problems before they are prompting problems.

Load `references/sources.md` before claiming plan-specific availability.

## Decision table

| Surface | Best for | Out of scope | Strong signal |
|---------|----------|--------------|---------------|
| Standard chat | Fast one-off asks, short iterations, casual drafting | Long projects with many files or decisions | User needs speed more than memory |
| Temporary Chat | Sensitive work, one-off experiments, contamination recovery | Ongoing work that should persist | User wants clean history / controlled personalization |
| Projects | Multi-turn work with shared files, repeated revisions, durable context | Tiny tasks that end in one or two turns | There is a file set, a brief, and a decision trail |
| Custom instructions | Stable preferences that should affect many future chats | Temporary goals, single projects, volatile requirements | Same preference keeps being repeated across sessions |
| GPTs / plugins | Narrow recurring jobs with a fixed role and reusable instructions | Broad general-purpose help or rapidly changing needs | The workflow is stable enough to package; plan/workspace allows it |

## Routing heuristics

- Start with standard chat unless memory or files clearly matter.
- Move to Temporary Chat when stale context, privacy, or experimentation make
  persistence a liability.
- Before the first Temporary Chat message, choose Personalized or
  Unpersonalized when the product offers that control.
- Move to Projects when the user says "keep these files together," "continue
  this later," or "preserve decisions."
- Use custom instructions only for defaults that should survive unrelated tasks.
- Recommend a GPT or plugin only after the workflow is stable and after checking
  current creation / migration policy for the user's plan or workspace.

## Search and freshness

- If the task needs current facts, tell the user to use ChatGPT Search / deep
  research or to verify externally.
- Do not treat remembered Project context as proof of freshness.
- Separate "current facts" from "stable internal brief" in the prompt packet.

## Fast recovery rule

When a chat feels contaminated:

1. Start a new thread instead of continuing the same one.
2. Rebuild the source of truth in a fresh surface.
3. Paste only the active brief, needed files, and output contract.

Switching surfaces is often faster than over-correcting a broken conversation.
