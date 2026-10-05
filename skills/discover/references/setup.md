# Setup - Discover

Use this file when `<state_root>/` is missing or empty.

Answer the immediate question first, then install the future discovery behavior early so the skill knows what to keep exploring and how proactive it may be.

## Immediate first-run actions

### 1. Lock integration behavior early

Within the first exchanges, clarify:
- should this activate when the user asks for new angles, opportunities, or things they may not know yet
- should it also activate when the user hints at an open loop like moving country, changing tax setup, or exploring a new market
- are there topics where discovery should stay quiet unless explicitly asked

Keep this short. One tight integration question is enough.

### 2. Lock the novelty bar

Clarify what counts as worth logging:
- new fact or source
- changed rule, constraint, or market condition
- new operator or practical path
- contrarian risk or hidden downside
- better comparison across options, geographies, or stakeholders

Default to a high novelty bar:
- no generic summaries
- no repeated explanations
- no "interesting but irrelevant" findings

### 3. Lock autonomy and heartbeat boundaries

Before any recurring loop exists, clarify:
- should discovery be on-request only, suggestive, or heartbeat-backed
- which topics may be revisited automatically
- what should happen when nothing new appears
- active hours and timezone if heartbeat is approved

Default to conservative behavior:
- propose heartbeat tracks first
- log without comment when nothing changed
- ask before any new recurring topic, schedule, or tool with cost

### 4. Prepare the AGENTS routing early

If a workspace `AGENTS.md` exists, show the exact block from package `AGENTS.md` and wait for explicit approval before writing it.

Keep the change small.
The goal is only to make discovery activate when the user wants new things, not to rewrite the workspace personality.

### 5. Prepare the HEARTBEAT contract early

If a workspace `HEARTBEAT.md` exists, show the exact block from package `HEARTBEAT.md` and wait for explicit approval before writing it.

Heartbeat should stay quiet by default.
No novelty means `HEARTBEAT_OK`.

### 6. Create local state after the behavior path is accepted

```bash
# After resolving the real directory for <state_root> (never mkdir the literal placeholder):
mkdir -p "$STATE_ROOT"/{findings,archive}
touch "$STATE_ROOT"/{memory.md,watchlist.md,heartbeat-state.md}
chmod 700 "$STATE_ROOT" "$STATE_ROOT"/findings "$STATE_ROOT"/archive
chmod 600 "$STATE_ROOT"/{memory.md,watchlist.md,heartbeat-state.md}
```

If the files are empty:
- initialize `<state_root>/memory.md` from `references/memory-template.md`
- initialize `<state_root>/watchlist.md` from `references/watchlist-template.md`
- initialize `<state_root>/heartbeat-state.md` from `references/heartbeat-state.md`

### 7. What to save

Save only what improves future discovery:
- activation and suppression preferences
- recurring discovery interests
- novelty bar and source preferences
- heartbeat approvals, pauses, and active hours
- findings that were actually new enough to matter

Keep secrets, credentials, and one-off curiosities out of durable tracking.
