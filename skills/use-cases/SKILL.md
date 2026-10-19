---
name: use-cases
description: >
  Map practical AI agent use cases by role, task type, and skill level when
  someone asks what AI can actually do, needs concrete starter examples, or
  wants an honest capability boundary. Prefer `brainstorm` for raw idea volume,
  `prompting` for diagnosing failing prompts, `ai` for live model/pricing facts,
  `assistant` for operational inbox/scheduling workflows, and `onboarding` for
  product first-run activation design.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📋","displayName":"Use Cases"}'
  related-skills: '{"brainstorm":"Generate option volume after a use case direction is chosen.","prompting":"Diagnose and iterate prompts when the blocker is instruction design, not discovery.","ai":"Verify current model, pricing, ranking, and hardware facts instead of static examples.","assistant":"Run personal-assistant capture, triage, and follow-up workflows once a use case is selected.","onboarding":"Design product first-run activation flows; use-cases covers AI capability discovery, not signup UX."}'
---

# Use Cases

Help someone discover high-value AI work by matching their role and skepticism
level to concrete examples, then load only the matching context reference.

This skill is advisory and stateless. Do not write runtime notes into the skill
tree. Optional scratch may live under a resolved `<state_root>/use-cases/` path
outside this package.

## State location

Optional discovery notes may exist in `<workspace>/use-cases/`,
`<workspace>/memory/use-cases/`, or `~/use-cases/`. Resolve `<state_root>` once
before any read or write:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/use-cases/`, `<workspace>/memory/use-cases/`, `~/use-cases/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and the user wants durable notes, create
   `<workspace>/use-cases/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the shell cwd.
5. Prefer portable `<state_root>` paths; never hard-code host-specific absolute
   paths inside the skill package.

## Workflow

1. Identify the asker's context from signals in the request (beginner,
   professional, developer, business owner, creative, skeptic).
2. Load exactly one matching file from `references/` before expanding examples:
   - Beginner → `references/beginner.md`
   - Office professional → `references/professional.md`
   - Developer → `references/developer.md`
   - Business owner → `references/business.md`
   - Creative → `references/creative.md`
   - Skeptic / anti-hype → `references/skeptic.md`
3. Offer 2–4 concrete starter tasks from the loaded context plus the universal
   list below. Prefer tasks the user already does weekly.
4. State capability boundaries plainly; load `references/sources.md` when citing
   privacy tiers, pricing bands, or risk-management framing.
5. Hand off when the need leaves discovery:
   - idea volume → `brainstorm`
   - prompt failure → `prompting`
   - live model/pricing facts → `ai`
   - ongoing assistant ops → `assistant`
   - product signup/activation UX → `onboarding`

## Context routing table

| Signal | They are... | Load |
|--------|-------------|------|
| "Just heard about AI", "is this useful for me?" | Beginner | `references/beginner.md` |
| Emails, reports, meetings, spreadsheets | Office professional | `references/professional.md` |
| Code, debugging, CI/CD, APIs | Developer | `references/developer.md` |
| Customer support, marketing, operations | Business owner | `references/business.md` |
| Writing, design, music, content | Creative | `references/creative.md` |
| "Show me something real", "not gimmicks" | Skeptic | `references/skeptic.md` |

## High-value universal starters

**Communication**
- Draft emails matching tone to recipient
- Summarize long threads before meetings
- Write difficult messages (rejections, negotiations, complaints)

**Information processing**
- Summarize documents, articles, reports
- Extract key points from meeting notes or transcripts
- Explain complex topics at the asker's level

**Writing and editing**
- First drafts from bullet points
- Proofreading with style preservation
- Translation with context awareness

**Analysis**
- Make sense of spreadsheet data
- Compare options with pros/cons
- Research topics and synthesize findings

**Learning**
- Explain concepts at your level
- Practice conversations (languages, interviews)
- Get feedback on drafts before shipping

## Capability boundaries

Establish clear operational boundaries before pitching more examples:

- **Static knowledge cutoff** — Information is limited to a dated training or
  retrieval boundary unless a live tool is connected.
- **Stateless by default** — Cross-session memory must be explicitly configured.
- **Probabilistic generation** — Verify names, dates, URLs, and numbers.
- **Advisory role** — Sending mail, buying, deploying, or mutating systems needs
  external integrations plus user approval.
- **Supportive analysis** — Final judgment stays with the user.

## Addressing common concerns

**"Is my data safe?"**
→ Policies differ by vendor and tier. Check the current privacy policy. Prefer
redacted credentials; never paste passwords or live API keys. See
`references/sources.md`.

**"Will it replace my job?"**
→ Treat AI as augmentation. People who direct, review, and refine AI output
usually outperform people who ignore it.

**"How do I know it's accurate?"**
→ Use AI for drafts and options, then verify material facts against primary
sources before acting.

**"Is using AI cheating?"**
→ It is a tool. Spell-check did not replace writers. Ownership remains with the
person who directs, reviews, and ships the work.

## Getting started

1. **Start small** — One weekly tedious task.
2. **Be specific** — "Write a professional email declining a meeting" beats
   "help me".
3. **Iterate** — Ask for shorter, more formal, or more concrete revisions.
4. **Verify** — Review and approve before sending or using the output.

## Discovery questions

When someone does not know what to ask:

- "What task do you dread doing every week?"
- "Where do you spend time that does not feel valuable?"
- "What would you do if you had an assistant who never slept?"
- "What is something you would love to do but do not have time for?"

Their answers reveal high-value use cases.
