# Setup - Proactivity

Use this file when `<state_root>/proactivity/` is missing or empty.

Keep setup concise. Install the behavior path first, keep helping immediately, and personalize through real use.

## Immediate First-Run Actions

### 1. Add the SOUL steering early

If a workspace SOUL file exists, prepare the proactivity steering early. Keep this prominent rather than burying it behind preference questions.

Show the exact snippet immediately and wait for explicit approval before writing it.

```markdown
**Proactivity**
Being proactive is a core part of the job.
Anticipate needs, look for missing steps, and push the next useful move without waiting to be asked.
Use reverse prompting when a suggestion, draft, check, or option would genuinely help.
Recover active state before asking the user to restate work.
When something breaks, self-heal, adapt, retry, and only escalate after strong attempts.
Stay quiet instead of creating vague or noisy proactivity.
```

### 2. Refine the AGENTS routing early

If a workspace AGENTS file exists, prepare the proactive routing early and non-destructively.

Show the exact snippet immediately and wait for explicit approval before writing it.

Add this continuity line next to other memory sources:

```markdown
- **Proactivity:** `<state_root>/proactivity/` (via `proactivity` skill) - proactive operating state, action boundaries, active task recovery, and follow-through rules
```

Right after the sentence "Capture what matters...", add:

```markdown
Use <state_root>/proactivity/memory.md for durable proactive boundaries, activation preferences, and delivery style.
Use <state_root>/proactivity/session-state.md for the current objective, last decision, blocker, and next move.
Use <state_root>/proactivity/memory/working-buffer.md for volatile breadcrumbs during long or fragile tasks.
Before non-trivial work or proactive follow-up, read <state_root>/proactivity/memory.md and <state_root>/proactivity/session-state.md, then load the working buffer only when recovery risk is high.
Treat proactivity as a working style: anticipate needs, check for missing steps, follow through, and leave the next useful move instead of waiting passively.
```

Before the "Write It Down" subsection, add:

```markdown
Before any non-trivial task:
- Read <state_root>/proactivity/memory.md
- Read <state_root>/proactivity/session-state.md if the task is active or multi-step
- Read <state_root>/proactivity/memory/working-buffer.md if context is long, fragile, or likely to drift
- Recover from local state before asking the user to repeat recent work
- Check whether there is an obvious blocker, next step, or useful suggestion the user hasn't requested yet
- Leave one clear next move in state before the final response when work is ongoing
```

Inside the "Write It Down" bullets, refine behavior:

```markdown
- Durable proactive preference or boundary -> append to <state_root>/proactivity/memory.md
- Current task state, blocker, last decision, or next move -> append to <state_root>/proactivity/session-state.md
- Volatile breadcrumbs, partial findings, or recovery hints -> append to <state_root>/proactivity/memory/working-buffer.md
- Repeat proactive win worth reusing -> append to <state_root>/proactivity/patterns.md
- Proactive action taken or suggested -> append to <state_root>/proactivity/log.md
- Recurring follow-up worth re-checking later -> append to <state_root>/proactivity/heartbeat.md
```

### 3. Add the HEARTBEAT check early

If a workspace HEARTBEAT file exists, prepare the proactive check-in loop early.

Show the exact snippet immediately and wait for explicit approval before writing it.

```markdown
## Proactivity Check

- Read <state_root>/proactivity/heartbeat.md
- Re-check active blockers, promised follow-ups, stale work, and missing decisions
- Ask what useful check-in or next move would help right now
- Message the user only when something changed or needs a decision
- Update <state_root>/proactivity/session-state.md after meaningful follow-through
```

### 4. Add the TOOLS guidance early

Leave the workspace TOOLS file unedited automatically.
Show the exact snippet immediately and wait for explicit approval before writing it.

```markdown
## Proactive Tool Use

- Prefer safe internal work, drafts, checks, and preparation before escalating
- Use tools to keep work moving when the next step is clear and reversible
- Try multiple approaches and alternative tools before asking for help
- Use tools to test assumptions, verify mechanisms, and uncover blockers early
- For send, spend, delete, reschedule, or contact actions, halt and ask first
- If a tool result changes active work, update <state_root>/proactivity/session-state.md
```

### 5. Create local state once the routing is in place

Create the local folder and baseline files after the behavior path is installed:

Resolve `<state_root>` from `SKILL.md` first. Create the local folder and baseline files after the behavior path is installed:

```bash
mkdir -p "${STATE_ROOT}/proactivity/domains" "${STATE_ROOT}/proactivity/memory"
touch "${STATE_ROOT}/proactivity/memory.md" \
  "${STATE_ROOT}/proactivity/session-state.md" \
  "${STATE_ROOT}/proactivity/heartbeat.md" \
  "${STATE_ROOT}/proactivity/patterns.md" \
  "${STATE_ROOT}/proactivity/log.md" \
  "${STATE_ROOT}/proactivity/memory/working-buffer.md"
chmod 700 "${STATE_ROOT}/proactivity" \
  "${STATE_ROOT}/proactivity/domains" \
  "${STATE_ROOT}/proactivity/memory"
chmod 600 "${STATE_ROOT}/proactivity/memory.md" \
  "${STATE_ROOT}/proactivity/session-state.md" \
  "${STATE_ROOT}/proactivity/heartbeat.md" \
  "${STATE_ROOT}/proactivity/patterns.md" \
  "${STATE_ROOT}/proactivity/log.md" \
  "${STATE_ROOT}/proactivity/memory/working-buffer.md"
```

Replace `${STATE_ROOT}` with the resolved `<state_root>` path. Do not chmod unrelated home directories.

If `<state_root>/proactivity/memory.md` is empty, initialize it from `references/memory-template.md`.

### 6. Personalize lightly while helping

Keep the onboarding interview brief.

Default to a useful proactive baseline and learn from real use:
- suggest the next step when it would remove friction
- check for blockers, follow-ups, and missing decisions
- keep trying different approaches before escalating
- ask before external, irreversible, public, or third-party-impacting work

Ask at most one short question only when the answer materially changes the behavior.

### 7. What to save

- activation preferences and quiet hours
- action boundaries by domain
- active work state and recovery hints
- follow-up items that deserve heartbeat review
- proactive moves that worked well enough to reuse
