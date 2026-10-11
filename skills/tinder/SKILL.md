---
name: tinder
description: Coach Tinder goals with profile reviews, opener feedback, chat triage,
  and local experiments that improve matches and dates over time.
metadata:
  openclaw: '{"requires": {"bins": [], "config": ["<state_root>/"]}, "emoji": "TD",
    "os": ["darwin", "linux", "win32"], "configPaths": ["<state_root>/"], "displayName":
    "Tinder"}'
  related-skills:
  - dates
  - chat
  - network
  - coach
  - empathy
---

## When to Use

User wants ongoing help performing better on Tinder without sounding scripted, wasting good matches, or dragging chats into nowhere.
Use this skill as a local coach: the user can keep sending screenshots, bios, chats, and outcomes, and the agent helps improve profile positioning, opener quality, chat decisions, and date conversion over time.

## Architecture

Memory lives in `<state_root>/`. If `<state_root>/` does not exist, run `references/setup.md`. See `assets/data-templates.md` for structure and starter files.

```text
<state_root>/
|- memory.md         # Activation defaults, tone boundaries, and coaching preferences
|- goals.md          # Current Tinder objective, bottleneck, and weekly targets
|- profile-notes.md  # Photo stack, bio tests, and recurring positioning notes
|- matches.md        # Active matches, stage, and next move
|- experiments.md    # Openers, profile edits, and what changed response quality
`- dates.md          # Proposed plans, logistics preferences, and post-date notes
```

## Quick Reference

Use the smallest relevant guide for the current problem.

| Topic | File |
|-------|------|
| Domain knowledge and core rules | `references/domain.md` |
| Setup and activation behavior | `references/setup.md` |
| Memory templates and local files | `assets/data-templates.md` |
| Goal setting and weekly coaching loop | `references/goal-tracker.md` |
| Photo stack and bio review | `references/profile-audit.md` |
| Match-specific first messages | `references/opener-lab.md` |
| Reading reciprocity and pacing | `references/chat-momentum.md` |
| Moving from chat to plan | `references/date-conversion.md` |
| Weekly experiments and funnel review | `references/pipeline-review.md` |
| Privacy and first-date guardrails | `references/safety-boundaries.md` |

## Requirements

- Profile screenshots, bio text, prompt answers, or pasted chats if the user wants concrete edits
- Explicit user confirmation before any irreversible send, unmatch, report, or block action
- Permission before creating or updating persistent notes in `<state_root>/`

If no screenshots or chat text are available, stay in strategy mode instead of pretending to see the match or thread.

## Data Storage

Local notes stay in `<state_root>/`.
Before creating or changing local files, present the planned write and ask for user confirmation.

## External Endpoints

This skill makes no external requests on its own.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

No data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- None from this skill itself

**Data that stays local:**
- optional funnel notes in `<state_root>/`
- profile observations, active match stages, and date-conversion patterns approved by the user

**Out of Scope actions:**
- auto-send messages
- invent verification, intentions, or compatibility
- scrape Tinder, social media, or private records
- store credentials, payment details, or unnecessary third-party private data
- make undeclared network requests

## Trust

This is an instruction-only Tinder coaching skill.
No credentials are required and no third-party service access is needed.

## Related Skills
More Clawic skills, get them at https://clawic.com/skills/<slug> (install if the user confirms):
- `dates` - shape simple, low-pressure date plans once a match is warm
- `chat` - refine tone, brevity, and communication defaults across conversations
- `network` - build low-pressure outreach and follow-up habits beyond swipe apps
- `coach` - keep weekly accountability on profile tests and conversion goals
- `empathy` - improve reading of tone, reciprocity, and compatibility cues

