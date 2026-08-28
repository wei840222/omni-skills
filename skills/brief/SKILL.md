---
name: brief
description: "Turns raw material into decision-ready briefs: executive summaries, status updates, meeting pre-reads, and decision documents. Use when asked to brief someone, write a TL;DR or weekly update, prepare a board, investor, or incident update, hand off a project, compare options with a recommendation, or condense a long report, thread, transcript, or doc pile into what the reader needs to act. Also when updates run long, readers skim past the point, or the lede keeps getting buried. Not for plain compression with no decision to serve, or for recurring digests pulled from external sources."
metadata:
  related-skills: '{"summarizer": "compression when there is no decision to serve", "digest": "recurring curated updates pulled from external sources on a schedule", "report": "recurring configured reports with fixed data sources", "meetings": "the full meeting system"}'
  openclaw: '{"requires":{"config":["<state_root>/","<state_root>/profile.yaml"]}}'
---

User configuration and learned preferences live in `<state_root>/` (see `references/setup.md` on first use, `references/preferences-template.md` for the learned-preferences file format). If you have data at an old location (`~/brief/` or `~/clawic/brief/`), move it to `<state_root>/`, and say in one line that you moved it and from where.

## When To Use

- User asks for an executive brief, TL;DR, or bottom-line summary of material they provide
- A recurring status or project update is due and the reader needs the delta, not a restate
- A meeting, board session, or review is coming up and the reader needs decisions-needed plus prep
- An incident is live and stakeholders need impact, status, and a committed next-update time
- A transition, offboarding, or vacation cover needs a handoff with gotchas and open questions
- The reader must choose between options and needs a recommendation with tradeoffs
- A long report, thread, transcript, or doc pile must be condensed to what drives a decision

Not for: compressing content when there is no decision or action to serve — use `summarizer` for shorter-content-only needs.

## Quick Reference

| Reference File | When to load | What it provides |
|----------------|--------------|------------------|
| `references/setup.md` | First use or when troubleshooting config | State location, default values, and setup instructions |
| `references/audiences.md` | When deciding depth or jargon | Audience profiles and how to adapt the brief |
| `references/delivery.md` | When picking a channel or timing | Channel limits, register, and emoji rules |
| `references/dimensions.md` | When interpreting feedback | Feedback-to-preference translation rules |
| `references/preferences-template.md` | First time saving learned preferences | The structure for `<state_root>/preferences.md` |
| `references/recurring.md` | When creating edition 2+ of a brief | Delta rules and baseline handling |
| `references/sources.md` | When analyzing provided raw material | Triage discipline and extraction workflow |
| `references/templates.md` | When structuring the output | Formats for different types of briefs |
| `references/writing.md` | When drafting lines | Bottom-line formulas, bullet rules, hedge blacklist |
| `references/traps.md` | Reviewing a drafted brief | Common failure modes and alternatives |
| `references/expert-disagreement.md` | When dealing with conflicting advice | Industry perspectives on memos vs bullets |
| `references/domain-knowledge.md` | When verifying briefing conventions or Gate 6 sources | Verified URLs for BLUF, executive summaries, memo culture |


| Situation | Play |
|-----------|------|
| Reader must choose between options | Decision brief: recommendation first, 2-3 options including do-nothing (`references/templates.md`) |
| Recurring status update | Project brief: lead with the delta since last brief, never a full restate (`references/recurring.md`) |
| Meeting coming up | Meeting brief: decisions needed + prep checklist; deliver the day before, not the morning of (`references/delivery.md`) |
| Board or investor update due | Board brief: metrics vs plan, lowlights before highlights, explicit asks (`references/templates.md`) |
| Something is on fire right now | Incident brief: impact in user terms, status, committed next-update time (`references/templates.md`) |
| Findings must become a decision | Research brief: answer with confidence level, evidence split from interpretation (`references/templates.md`) |
| Transition, offboarding, vacation cover | Handoff brief: gotchas and open questions outrank achievements (`references/templates.md`) |
| Source is huge or messy | Triage by decision-relevance, never proportionally to source length (`references/sources.md`) |
| Sources disagree or have gaps | Show the conflict and name the gap — never average or silently narrow (`references/sources.md`) |
| Audience unclear or mixed | Name the decider; their action sets depth and jargon (`references/audiences.md`) |
| Formal channel (exec email, external doc) | Same structure, strip emoji markers, plain headers (`references/delivery.md`) |
| Brief keeps coming back "too long" | Cutting passes, hedge blacklist, decision-grade rounding (`references/writing.md`) |
| User reacts to a delivered brief | Record it in `<state_root>/preferences.md`; signal mapping in `references/dimensions.md` |
| Anything else | Executive structure: bottom line, 3 key points, explicit ask |

Depth on demand: `references/templates.md` section-by-section structures per type · `references/sources.md` raw-material triage, conflicts, gaps · `references/audiences.md` reader calibration · `references/delivery.md` channels, register, timing · `references/writing.md` line-level compression · `references/recurring.md` running a brief series · `references/dimensions.md` preference taxonomy · `references/setup.md` first-use loading.

## State Location

The brief skill is stateful and relies on explicit user configurations and learned preferences to operate effectively. All state files reside within the `<state_root>/` directory. The `<state_root>/profile.yaml` file holds cross-skill preferences.

1. `<state_root>/config.yaml`: Contains explicitly stated preferences and configurations.
2. `<state_root>/preferences.md`: Stores inferred, learned preferences based on user feedback.
3. `<state_root>/templates/`: A directory for user-supplied custom brief templates.
4. `<state_root>/profile.yaml`: Cross-skill global preferences (e.g., locale, timezone).

The skill will create `preferences.md` from the `references/preferences-template.md` upon the first explicit feedback signal if the file doesn't exist. Do not interview the user to setup config; rely on defaults and organic updates.

## Core Rules

### 1. User Specifies Sources
When the user requests a brief:
1. User provides the information OR specifies where to get it
2. If a source requires access, the user grants it explicitly
3. Skill structures and formats the output

Example:
```
User: "Brief me on project X status"
Agent: "I'll need access to the project docs. Can you share
        the status doc or grant access to the project folder?"
User: [shares doc or grants access]
→ Brief generated from user-provided source
```

### 2. A Brief Is Not a Summary
A summary compresses content; a brief serves the reader's next action. If you cannot name the decision or action this brief enables, ask "what will you do with this?" before writing. Competent people summarize; briefers select.

### 3. Write in Reverse Reading Order
Compose ask → bottom line → key points → context; the reader consumes the opposite order. Writing front-to-back is how ledes get buried: you discover the point last and leave it there.

### 4. Bottom Line Commits
One sentence, no hedge. If it contains "and", you have two takeaways — keep the one that changes what the reader does, demote the other to key points. "Mostly on track, but..." is not a bottom line; it is a decision you refused to make.

### 5. Three Key Points, Five Hard Max
A point qualifies only if removing it would change the reader's decision. Six "key" points means you haven't decided what matters — cut, or tier the rest under a "more detail" note. This selection rule beats source length: one decision-relevant page outweighs forty pages of background.

### 6. Every Number Carries a Comparator
"$1.2M revenue" is decoration; "$1.2M, 8% under plan" is a brief line. Valid comparators: target, prior period, benchmark. None available → write "no baseline yet" or drop the number.

### 7. Status Words Have Definitions
- **On track** — schedule/scope buffer intact
- **At risk** — buffer being consumed; the first slip counts, no grace period
- **Blocked** — cannot proceed without a named external action

Declaring at-risk early is cheap. A green-to-red flip with no warning destroys trust in every future brief you send. (`status_scheme: rag` in config maps these 1:1 to Green/Amber/Red.)

### 8. Learn Only From Explicit Feedback
"Too detailed" / "missing X" / "perfect" → one line in `<state_root>/preferences.md` with a level (`pattern`/`confirmed`/`locked`, promotion rules in `references/dimensions.md`). Check the file before writing any brief — a well-built brief in the wrong learned format still misses.

## Scope

This skill:
- ✅ Structures information the user provides into briefs (act-as writer: it drafts; the user sends)
- ✅ Learns format preferences from explicit feedback
- ✅ Stores configuration and preferences in `<state_root>/`

**User-driven model:** the user specifies WHAT information to include and grants access to any needed sources; the skill handles STRUCTURE and FORMAT.

**Actionable Boundaries:**
- Only access files, emails, or calendars when the user explicitly requests it.
- Only pull data from sources the user has explicitly specified.
- Only store configuration and format preferences, leaving brief content unstored.

## Output Gates

Run before delivering any brief:
- [ ] Bottom line survives alone — if the reader stops there, they still have the takeaway
- [ ] Every metric has a comparator or an explicit "no baseline yet"
- [ ] The ask names an owner and a date, or states "no action needed" — ensure the ask is explicit rather than implied inside an FYI
- [ ] Bad news sits above the fold, next to its mitigation, not in section four
- [ ] Data that can go stale carries source and as-of date
- [ ] Conflicting sources are shown as a conflict, always retain their individual provenance rather than being averaged into one number
- [ ] Jargon calibrated to the least-technical decider, not the most technical reader
- [ ] Format matches `<state_root>/config.yaml` and `preferences.md` — checked, not remembered

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| default_length | one-screen \| one-page \| two-page | one-page | Sizing target: one-page = 450-500 words (`references/templates.md`); one-screen = fits without scrolling (chat cap, `references/delivery.md`); two-page only when the reader asked for depth |
| status_scheme | words \| rag | words | Status labels everywhere a status renders: On track/At risk/Blocked vs Green/Amber/Red (definitions in Rule 7 apply to both) |
| emoji_markers | bool | true | Section markers (⚡📊🎯) on informal channels; false = plain headers everywhere (formal channels strip them regardless, `references/delivery.md`) |
| default_channel | chat \| email \| doc | chat | Assumed delivery surface; sets register and length caps per `references/delivery.md` |
| locale | text (BCP-47, e.g. en-US) | en-US | Date order (Jul 21 vs 21 Jul), decimal/thousands separators, and currency symbol + placement in every rendered number and date (`references/writing.md`); falls back to `<state_root>/profile.yaml` before the default |

Preference areas — customizable dimensions; a stated preference gets recorded in config.yaml and applied:
- **Audience mix**: who reads most briefs (boss, board, clients, team) — shifts the default template and jargon level (`references/audiences.md`)
- **Conventions**: section names, bullet style, status-word extensions — shifts the structures in `references/templates.md`
- **Timing**: lead times, cadence, delivery day — shifts the scheduling guidance in `references/delivery.md`
- **Exclusions**: topics or metrics never to include (confidential, legal) — screens extraction in `references/sources.md`
- **Voice**: bad-news directness, person (I/we/team), formality floor — shifts the register rules in `references/writing.md`
- **Localization**: beyond the `locale` tag — timezone for timestamps and deadlines, and multi-currency policy (show native vs converted, which symbol) when amounts span currencies — affects number lines in `references/writing.md` and the incident/board timestamps in `references/templates.md`

Config vs learned preferences: `config.yaml` holds what the user declared; `preferences.md` holds what feedback revealed (levels in `references/dimensions.md`). A stated preference that names a config variable goes straight to `config.yaml`. Precedence: config > `confirmed`/`locked` learned preferences > defaults. Universal variables (`locale`, timezone) additionally fall back to `<state_root>/profile.yaml` before their table default: config > `profile.yaml` > default.
