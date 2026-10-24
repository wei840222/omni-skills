---
name: work
description: >
  Navigate day-to-day office work: clarifying vague assignments, drafting
  professional status updates and emails, preparing for meetings, handling
  credit-taking or political friction, building visibility, and pacing the
  first 90 days. Use when the user asks how to talk to a manager, write a
  status update, respond after someone takes credit, get recognized without
  bragging, or onboard into a new role. Prefer `career` for offer, promotion,
  and stay/leave strategy; prefer `productivity` for personal planning systems;
  prefer `meetings` when the artifact is an agenda, facilitation plan, or
  meeting record.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"💼"}'
  related-skills: '{"career": "Offer evaluation, negotiation, promotions, pivots, and layoff response beyond day-to-day office tactics.", "management": "People-management craft for leading a team rather than navigating as an IC.", "meetings": "Agendas, facilitation, minutes, and follow-ups when the meeting itself is the deliverable.", "productivity": "Personal planning, overwhelm triage, and habit repair rather than workplace communication."}'
---

# Work

Advise on day-to-day effectiveness inside a corporate or office environment.
Stay in **advise** mode: draft language the human can send, but do not send
messages, escalate, or store private workplace facts without explicit consent.

## State location

Work-profile notes may exist in `<workspace>/work/`, `<workspace>/memory/work/`,
or `~/work/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/work/`, `<workspace>/memory/work/`, `~/work/`.
3. If none exists and durable notes must be created, ask once and default to
   `<workspace>/work/`.
4. If more than one candidate exists, use only the highest-precedence directory,
   report the conflict, and leave other copies unchanged.
5. If `<workspace>` cannot be resolved, read an existing `~/work/` only.
   Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill.
Preferred files:

- `<state_root>/profile.md` — environment, key relationships, culture signals,
  recurring challenges
- `<state_root>/brag.md` — wins, impact, recognition, learning for reviews

Never write secrets, passwords, private HR case details, or verbatim gossip.
Confirm before creating or updating either file. Treat legacy `~/Clawic/data/work/`
as a migration source only—ask before migrating.

## When to use

| Signal | Context | Load |
|--------|---------|------|
| First 90 days, onboarding, new hire | New role adaptation | `references/new-hire.md` |
| Credit-taking, undermining, politics | Workplace dynamics | `references/politics.md` and `references/scripts.md` |
| Email drafts, meeting prep, status updates | Communication tasks | `references/comms.md` |
| Visibility, recognition, being overlooked | Perception management | `references/visibility.md` |
| Vague assignments, unclear priorities | Task clarity | `references/clarity.md` |
| Domain evidence / source URLs | Research refresh | `references/sources.md` |

Hand off when the ask is career strategy (`career`), personal productivity systems
(`productivity`), or owning the meeting artifact itself (`meetings`).

## Core workflow

1. Identify the situation from the table above and load only the needed reference.
2. Ask for the missing decision inputs: audience, deadline, desired outcome, and
   constraints. Prefer one clarifying question over a questionnaire.
3. Draft the smallest useful next move: a clarifying ask, status note, private
   follow-up, or 90-day action.
4. Offer exact wording the user can send. Keep tone calibrated to audience.
5. If the user wants continuity, propose a concise update to
   `<state_root>/profile.md` or `<state_root>/brag.md` and wait for consent.

## Professional communication quick path

**Email drafts:** Put the ask or outcome first; details below. Match tone to
recipient and urgency.

**Meeting prep:**
1. Review prior threads and decisions.
2. Define your contribution: questions, updates, blockers.
3. Prepare a one-liner if asked for updates.

**Status formula:**
```text
DONE: [completed items with impact]
IN PROGRESS: [current focus + ETA]
BLOCKED: [what needs input/decision]
```

Load `references/comms.md` for templates. Load `references/scripts.md` for
difficult-conversation wording.

## Workplace dynamics quick path

- Before credit issues: keep a written trail and present your own work when possible.
- When credit is taken: reclaim gently in the room if safe; otherwise follow up
  privately with a specific ask.
- When undermined publicly: pause, then address privately once with facts.
- Building alliances: be useful to influential stakeholders and stay visible on
  shared outcomes.

Load `references/politics.md` for patterns and `references/scripts.md` for scripts.

## First 90 days quick path

- Weeks 1–4: absorb norms, map influence, clarify what “good” looks like.
- Weeks 5–8: deliver small visible wins and ask for feedback.
- Weeks 9–12: own one bounded end-to-end outcome and run a how-am-I-doing check-in.

Load `references/new-hire.md` for the full week-by-week plan.

## Failure modes

- Do not invent org politics, HR policy, or legal advice. Stay on communication tactics.
- Do not escalate, confront, or send messages on the user's behalf.
- Do not store sensitive workplace allegations without explicit consent and need.
- If the request is really career strategy or personal productivity, route instead
  of stretching this skill.

## Sources

Load `references/sources.md` when refreshing domain evidence. Prefer the live
URLs there over remembered benchmarks or viral workplace advice.
