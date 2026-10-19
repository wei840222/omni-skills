---
name: chatgpt
description: >
  Improve ChatGPT product workflows with surface routing, prompt packets,
  Projects hygiene, memory boundaries, GPTs/plugins guidance, and output QA.
  Use when the user wants better results from ChatGPT itself for research,
  writing, analysis, planning, or recurring assistant workflows. Prefer
  `prompting` for provider-agnostic prompt iteration and failure diagnosis,
  `memory` for durable host-side memory design beyond ChatGPT settings, and
  API/SDK skills when the ask is OpenAI platform integration rather than
  ChatGPT UI.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💬"}'
  related-skills: '{"assistant":"Build clearer working agreements and recurring collaboration patterns with an AI assistant.","brainstorm":"Expand idea generation before converging into a final prompt packet.","chat":"Improve conversational structure and turn-taking in multi-turn interactions.","documentation":"Turn ChatGPT outputs into tighter docs, guides, and reusable written artifacts.","memory":"Design durable host-side memory patterns beyond ChatGPT product memory settings.","prompting":"Iterate and diagnose provider-agnostic prompts when the ask is not ChatGPT UI routing."}'
---

# ChatGPT

Advise-and-operate mode for work done inside the ChatGPT product. This skill
helps route surfaces, build prompt packets, keep project context clean, manage
memory boundaries, and QA outputs before reuse.

It does not call the OpenAI API, automate browser uploads, publish content, or
overwrite active ChatGPT / local workflow state without explicit user consent.

Optional durable local notes live under a resolved `<state_root>/` tree outside
this package. Never write runtime state into the skill tree.

Load `references/sources.md` before restating product availability, Memory
controls, Temporary Chat personalization, Projects limits, or GPT creation /
retirement claims.

## State location

ChatGPT workflow notes may exist in `<workspace>/chatgpt/`,
`<workspace>/memory/chatgpt/`, or `~/chatgpt/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Prefer an explicit host- or user-configured state root when present.
2. Else use the first existing candidate among:
   - `<workspace>/chatgpt/`
   - `<workspace>/memory/chatgpt/`
   - `~/chatgpt/`
3. If none exist, create `<workspace>/chatgpt/` when the host provides a
   workspace; otherwise create `~/chatgpt/`.
4. Keep the selected `<state_root>` fixed for the rest of the invocation.

Use the selected `<state_root>` for every state operation in this skill.
Legacy `~/Clawic/data/chatgpt/` is not in the active lookup order; migrate only
with explicit user consent, copy/validate/cutover/rollback steps, and never by
silent move or delete.

## When to use

Use this skill when the user wants:

- better ChatGPT prompts, packets, or multi-pass workflows
- help choosing standard chat, Temporary Chat, Projects, custom instructions,
  GPTs, or plugins
- project charter / file hygiene / decision-log patterns inside ChatGPT
- memory and privacy boundary guidance for ChatGPT product features
- output QA before shipping ChatGPT drafts

Route away when the ask is mainly:

- provider-agnostic prompt iteration or failure diagnosis → `prompting`
- host-side durable memory architecture beyond ChatGPT settings → `memory`
- OpenAI API / SDK / platform coding → API or coding skills
- general multi-agent collaboration contracts → `assistant` / `chat`

## Architecture

```text
<state_root>/
|- memory.md      # Activation preference, constraints, default workflow
|- workflows.md    # Reusable prompt packet patterns that worked well
|- projects.md     # Active ChatGPT projects, files, and decision logs
|- gpts.md         # Custom GPT / plugin roles, guardrails, limitations
`- qa.md           # Output failures, hallucination catches, and fixes
```

Create child files only when the matching workflow needs persistence.

## Quick reference

| Topic | File |
|-------|------|
| Setup and activation | `references/setup.md` |
| Memory / status templates | `assets/data-templates.md` |
| Surface routing | `references/surfaces.md` |
| Prompt packets | `references/prompt-packets.md` |
| Projects playbook | `references/project-playbook.md` |
| Output QA | `references/output-qa.md` |
| Drift recovery | `references/troubleshooting.md` |
| Verified sources | `references/sources.md` |

## Operating sequence

1. Confirm the job is ChatGPT-product help, not API integration.
2. Route the lightest surface first (`references/surfaces.md`).
3. Build a prompt packet with goal, context, source of truth, deliverable,
   constraints, and review standard.
4. For factual or consequential work, require confirmed / inferred / unknown
   labels before treating the draft as reliable.
5. For multi-turn work, keep a visible decision log and name the authoritative
   file when drafts compete.
6. QA before shipping (`references/output-qa.md`).
7. Persist only reusable defaults under `<state_root>/` after consent.

## Core rules

1. **Route before rewriting.** Wrong surface creates false prompt problems.
2. **Packets beat adjectives.** Specify output shape and constraints before style.
3. **Separate durable prefs from task context.** Custom instructions and Memory
   are for stable preferences; project briefs stay in Projects or the current chat.
4. **Temporary Chat is not one mode.** Choose Personalized vs Unpersonalized
   before the first message when the product offers that control.
5. **Evidence over confidence.** Unsupported claims stay drafts.
6. **One improvement target per pass** for multi-pass work.
7. **Recover by restarting the source of truth**, not by stacking style nags.

## Common traps

- stuffing temporary requirements into custom instructions
- using one long chat for unrelated jobs
- asking for a final answer before audience, format, and success criteria
- trusting confident claims without an evidence trail
- uploading files without naming the authoritative source
- letting Projects keep stale drafts as silent anchors
- treating GPT creation as universally available when plan/workspace policy differs

## Security and privacy

**Data that leaves the machine:** anything the user types, pastes, or uploads
into ChatGPT, plus instructions or files deliberately used in that workflow.

**Data that stays local:** activation preferences, reusable workflows, project
notes, GPT/plugin notes, and QA learnings under `<state_root>/`.

**This skill does not:**

- automate browser sessions or uploads
- store secrets unless the user explicitly asks for a safe local boundary note
- treat remembered preferences as facts when the current prompt overrides them
- modify its own skill package

## Trust

This skill improves work done inside ChatGPT. Prompts and uploads used in those
workflows may be sent to OpenAI through ChatGPT. Use it only when that data flow
is acceptable for the task.
