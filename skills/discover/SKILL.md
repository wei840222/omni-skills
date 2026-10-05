---
name: discover
description: >
  Keep discovering new angles, risks, operators, jurisdictions, and practical next
  paths on topics that matter over time. Use when the user asks to keep an eye on a
  topic, track novelty, find non-obvious angles, maintain a discovery watchlist, or
  run quiet heartbeat-backed discovery that returns HEARTBEAT_OK when nothing changed.
  Not for one-shot summaries, generic research dumps without a novelty bar, or pure
  note capture without ongoing discovery intent.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔭","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"heartbeat":"Owns recurring OpenClaw heartbeat playbooks and quiet no-change contracts when discovery is heartbeat-approved.","in-depth-research":"Deep multi-source investigation when a single discovery needs exhaustive methodology rather than ongoing novelty tracking.","market-research":"Market and competitor framing when discovery topics are commercial rather than open-loop life or opportunity tracks.","notes":"Retrieval-oriented capture when the user wants a second brain entry instead of novelty-over-time discovery.","schedule":"Exact-time cron or calendar jobs when discovery work needs precise timing instead of heartbeat."}'
---

# Discover

Turn durable curiosity into a visible watchlist, a high novelty bar, and quiet recurring checks. Prefer findings that change options or next moves over volume.

## State location

Discover state may exist in `<workspace>/discover/`, `<workspace>/memory/discover/`, or `~/discover/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/discover/`, `<workspace>/memory/discover/`, `~/discover/`.
3. If none exists and state must be created, default to `<workspace>/discover/`.

Use the selected `<state_root>` for every state operation in this skill. If multiple candidates exist, use only the highest-precedence one, report the conflict, and leave the others unchanged.

## Shared workspace writes

Workspace `AGENTS.md` and `HEARTBEAT.md` are host-owned paths outside `<state_root>`. Propose the exact blocks from package `AGENTS.md` / `HEARTBEAT.md` and wait for explicit approval before writing them. Keep those edits minimal and discovery-scoped.

## When to use

- Keep discovering opportunities, risks, angles, operators, jurisdictions, sources, or next paths over time
- Maintain a watchlist with an explicit novelty bar
- Run heartbeat-backed discovery that stays quiet when nothing material changed
- Open loops such as relocation, tax residency, market entry, tools to test, or business-model exploration

Hand off when the job is really:

- one-shot research with no ongoing track → `in-depth-research`
- commercial market framing only → `market-research`
- retrieval notes / second brain → `notes`
- exact-time jobs → `schedule`
- generic heartbeat plumbing without discovery state → `heartbeat`

## Detection triggers

Route here when the conversation sounds like any of these:

- "Keep an eye on this"
- "I want to keep discovering things around this"
- "What else should I know here?"
- "Find me angles I have not thought about"
- "Track this over time and tell me only if there is something new"
- "I may move country / change tax residency / enter a market, keep digging"
- "Provide novel insights beyond the obvious stuff"

## Quick reference

Load only the reference that matches the current step. Prefer one-level paths from this skill root.

| Topic | File | Load when |
|-------|------|-----------|
| Architecture | `references/architecture-rules.md` | Resolve state tree roles after `<state_root>` is chosen |
| Core rules | `references/core-rules.md` | Run any discovery pass |
| Security and scope | `references/security-and-scope.md` | Privacy, external lookups, or autonomy boundaries |
| Traps | `references/traps.md` | Review failure modes before expanding scope |
| Setup | `references/setup.md` | First use or empty state |
| Memory schema | `references/memory-template.md` | Create or repair `<state_root>/memory.md` |
| Baseline memory example | `references/memory.md` | Show shape of a live memory file |
| Watchlist schema | `references/watchlist-template.md` | Create or repair `<state_root>/watchlist.md` |
| Baseline watchlist example | `references/watchlist.md` | Show active / parked / retired topics |
| Novelty filter | `references/novelty-test.md` | Decide whether a finding is log-worthy |
| Discovery loop | `references/discovery-loop.md` | Run a full discovery pass with lens rotation |
| Heartbeat rules | `references/heartbeat-rules.md` | Execute an approved recurring check |
| Heartbeat state template | `references/heartbeat-state.md` | Initialize `<state_root>/heartbeat-state.md` |
| Research sources | `references/sources.md` | Verify format, novelty, or heartbeat claims against primary URLs |

## Requirements

- No credentials are required by default.
- Ask before enabling heartbeat or any recurring discovery loop.
- Ask before using paid tools, contacting third parties, or taking action outside research and logging.
- Keep external lookup scope narrow and tied to active watchlist topics.
- Resolve `<state_root>` once per invocation before any state read or write.

## Operating sequence

1. Resolve `<state_root>` (State location above).
2. If state is missing, follow `references/setup.md` and wait for consent on workspace routing / heartbeat blocks.
3. Read `<state_root>/memory.md` and `<state_root>/watchlist.md` when they exist.
4. Lock why the topic matters, then run `references/discovery-loop.md` with one fresh lens.
5. Apply `references/novelty-test.md` before logging.
6. Append only deltas to `<state_root>/findings/{topic}.md`.
7. For heartbeat runs, follow `references/heartbeat-rules.md` and return `HEARTBEAT_OK` when nothing material changed.
