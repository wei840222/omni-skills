---
name: tinder
description: >
  Coach Tinder goals with profile reviews, opener feedback, chat triage, and
  local experiments that improve matches and dates over time. Use when the user
  shares Tinder screenshots, bios, chats, match funnel questions, or wants help
  turning warm chats into low-friction public date plans. Prefer `dates` for
  offline date logging, `chat` for general tone preferences, and `coach` for
  non-dating accountability.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"💘"}'
  related-skills: '{"dates":"Offline date logging and person notes once a match leaves the swipe funnel.","chat":"General communication tone and format preferences beyond Tinder threads.","coach":"Non-dating goal coaching and weekly accountability.","empathy":"Reading emotional subtext when a thread feels tense or ambiguous.","couple":"Established relationship milestones after dating becomes a partnership."}'
---

# Tinder

Local **Tinder coaching** for profile positioning, openers, chat momentum, and
date conversion. Keeps optional funnel notes under a portable `<state_root>/`.
Does not send messages, scrape Tinder, or invent verification.

## When to use

- Review photos, bio, and prompts against a concrete dating goal
- Draft match-specific openers from something real in the profile
- Classify a thread as warming / stable-but-stuck / cold and pick the next move
- Convert reciprocal chat into a short public plan with a narrow time window
- Log weekly experiments (opener category, profile edit, stall stage)

Prefer `dates` once the relationship is offline notes. Prefer `chat` for global
tone defaults. Prefer `coach` when the goal is not dating.

## State location

Tinder state may exist in `<workspace>/tinder/`, `<workspace>/memory/tinder/`, or
`~/tinder/`. Before reading or writing state, resolve `<state_root>` once per
invocation:

1. Use an explicitly configured path when the user or host provides one; resolve
   it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/tinder/`, `<workspace>/memory/tinder/`, `~/tinder/`.
3. If multiple candidates exist, keep only the highest-precedence directory,
   report the conflict, and leave siblings unchanged.
4. If none exists and state must be created, default to `<workspace>/tinder/`
   only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/tinder/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this
section, every skill-state path uses `<state_root>/...`. Skill resources stay
under `references/` and `assets/`. Do not treat the literal string
`<state_root>` as a filesystem path. Do not write passwords, payment details,
raw chat archives, or unnecessary third-party private data into tinder files.
Do not write learned preferences into `SKILL.md`.

Default layout (create files on first authorized write from
`assets/data-templates.md`):

```text
<state_root>/
├── memory.md         # activation defaults, tone, coaching preferences
├── goals.md          # active objective, bottleneck, weekly target
├── profile-notes.md  # photo stack, bio tests, positioning
├── matches.md        # active matches, stage, next move
├── experiments.md    # opener/profile tests and outcomes
└── dates.md          # proposed plans and post-date notes
```

If older notes still live under a legacy marketplace path, offer a one-time
migrate into the resolved `<state_root>/` and say in one line what moved; do not
keep marketplace homepage links.

## Core behavior

1. Start from the active goal and bottleneck (`references/goal-tracker.md`)
   before generic dating theory.
2. Fix positioning (`references/profile-audit.md`) before rewriting openers when
   photos or bio are weak or mismatched.
3. Anchor every opener to something real in the match profile
   (`references/opener-lab.md`); give one primary line plus optional backups.
4. Classify momentum (`references/chat-momentum.md`) by reciprocity and logistics
   readiness, not message count.
5. When reciprocity is clear, propose a low-friction public plan with a narrow
   window (`references/date-conversion.md`).
6. Keep the user's real-world voice; do not replace it with generic AI flirt copy.
7. Log only durable experiment signals (`references/pipeline-review.md`).
8. Safety overrides conversion (`references/safety-boundaries.md`).

## Progressive disclosure

| Need | Load |
| --- | --- |
| Core rules and common traps | `references/domain.md` |
| First-run activation and storage consent | `references/setup.md` |
| File templates for `<state_root>/` | `assets/data-templates.md` |
| Goal and weekly loop | `references/goal-tracker.md` |
| Photo/bio audit | `references/profile-audit.md` |
| Opener craft | `references/opener-lab.md` |
| Momentum triage | `references/chat-momentum.md` |
| Date conversion logistics | `references/date-conversion.md` |
| Weekly funnel review | `references/pipeline-review.md` |
| Safety and first-meet defaults | `references/safety-boundaries.md` |
| Verified sources for Gate 6 claims | `references/sources.md` |

## Failure and safety

- No screenshots or chat text: stay in strategy mode; do not pretend to see the
  match or thread.
- Missing `<state_root>/`: coach without persistence until the user consents to
  create files via `references/setup.md`.
- Conflicting multi-root state: use highest-precedence root only; never merge
  silently.
- Irreversible actions (send, unmatch, report, block): require explicit user
  confirmation; never claim a message was sent unless a separate sending tool
  confirms it.
- Money, travel help, sensitive images, or coercive pressure: pull back and load
  `references/safety-boundaries.md`.
- First meetups with thin context: public place, short duration, easy exit, low
  financial pressure.
- Out of scope: auto-send, catfishing, manipulation, scraping Tinder/socials,
  inventing verification or compatibility, storing credentials.

## External endpoints

This skill makes no external network requests on its own.

