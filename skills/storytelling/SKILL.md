---
name: storytelling
description: >
  Craft clear, emotionally resonant stories with audience-first framing, causal
  arc control, scene density, evidence placement, and channel-specific rewrites.
  Use when the user needs a product story, founder narrative, case study, pitch,
  speech, long-form narrative, short-form adaptation, or when a draft feels flat,
  disconnected, or emotionally vague. Not for general prose polish without narrative
  intent (writing), conversion sales copy (copywriting), or pure content calendars
  (content-marketing).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📖","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"writing":"Improve sentence-level prose, voice fingerprint, and revision passes when the problem is wording rather than story logic.","content-marketing":"Connect finished stories to funnel stages, distribution plans, and editorial calendars.","storybook":"Create consistent narrative components for UI and product communication flows.","history":"Build chronology-aware historical narratives with source-aware framing.","youtube-video-transcript":"Turn transcript material into tighter narrative scripts and summaries."}'
---

# Storytelling

Turn facts, tension, and proof into a story the audience can follow, feel, and act on. Prefer causal arcs and concrete scenes over topic lists and vague inspiration.

## State location

Storytelling state may exist in `<workspace>/storytelling/`, `<workspace>/memory/storytelling/`, or `~/storytelling/`.
`<workspace>` means the workspace root provided by the host/runtime, not the shell cwd.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/storytelling/`, `<workspace>/memory/storytelling/`, `~/storytelling/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and persistent state must be created, default to `<workspace>/storytelling/` after brief first-write consent.

Use the selected `<state_root>` for every state path in this skill. Resolve `<state_root>` to a real path before filesystem work. Skill package files stay under `references/`; keep learned data in `<state_root>/`, not in `SKILL.md`.

## When to use

- Product stories, founder narratives, case studies, speeches, pitch decks narratives
- Long-form writing that needs a causal arc rather than a topic outline
- Short-form adaptations that must keep conflict, decision, proof, and implication
- Drafts that feel flat, disconnected, chronological-only, or emotionally vague
- Audience-first reframes when the current belief and desired shift are unclear

## Architecture

```text
<state_root>/
|-- memory.md              # Audience profile, goals, constraints, voice notes
|-- story-bank.md          # Reusable stories, scenes, and proof points
|-- messaging-pillars.md   # Core themes, promises, and supporting evidence
`-- edit-log.md            # Draft iterations, decisions, and rejected directions
```

Load `references/memory-template.md` when creating or reshaping state files.

## Progressive disclosure

Keep `SKILL.md` as the routing surface. Load only the smallest reference needed for the current bottleneck.

| Need | Load |
|------|------|
| First-use alignment and activation | `references/setup.md` |
| Memory and status model | `references/memory-template.md` |
| Arc design and sequencing | `references/story-arc-map.md` |
| Scene construction and pacing | `references/scene-design.md` |
| Channel compression and rewrites | `references/rewrite-modes.md` |
| Voice calibration across drafts | `references/voice-consistency.md` |
| Core operating rules | `references/core-rules.md` |
| Common failure modes | `references/storytelling-traps.md` |
| Local state inventory | `references/data-storage.md` |
| Security and privacy boundaries | `references/security-and-privacy.md` |
| Scope boundaries | `references/scope.md` |
| Verified craft sources | `references/sources.md` |

## Operating sequence

1. Resolve `<state_root>` (State location above). On first use or empty state, read `references/setup.md`.
2. Capture one audience outcome, one central tension, and one desired resolution before drafting prose.
3. Build a skeleton arc with `references/story-arc-map.md` (situation → friction → choice → execution → outcome → transfer).
4. Draft scenes only where empathy or credibility must spike; summarize elsewhere (`references/scene-design.md`).
5. Place specific evidence at the point of highest skepticism (`references/core-rules.md`).
6. Run a separate judgment pass: cut, reorder, and sharpen. Keep ideation and critique as two passes.
7. Adapt to channel with `references/rewrite-modes.md` while preserving conflict, decision, proof, and implication.
8. End with one clear action, belief shift, or watchpoint. Persist only consented notes under `<state_root>/`.

## Operating rules

- Anchor every story to one explicit audience outcome before generating language.
- Prefer causal bridges over chronological dumps or topic lists.
- Use concrete moments, constraints, and observed outcomes instead of abstract adjectives.
- Keep drafting and judgment as two passes so the first draft stays generative and the second stays ruthless.
- Compress format without erasing story logic; short form is compression, not sloganization.
- Treat audience profiles, story banks, drafts, and edit logs as local user data. Create or modify `<state_root>/` files only after consent when persistence is needed.
- Remain useful without storage: deliver an in-chat arc and draft when the user declines persistence.

## Scope

This skill handles:

- Narrative strategy for clarity, persuasion, and memorability
- Story logic, evidence placement, pacing, and multi-channel adaptation
- Iterative drafting with explicit quality checks

Route elsewhere or stop when:

- The need is general prose polish without narrative structure (`writing`)
- The need is conversion-first sales copy without story craft (`copywriting`)
- The need is editorial calendars or funnel planning alone (`content-marketing`)
- Facts, legal claims, or testimonials require domain review the user has not provided

## Safety

- Mark unknowns instead of inventing facts or testimonials.
- Claim only outcomes the available evidence can support.
- Prefer placeholders over collecting secrets, passwords, or private credentials.
- Keep network calls explicit and user-requested.
- Treat publish or send actions as separate authorized steps.
