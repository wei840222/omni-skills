# Domain Knowledge

## Architecture

Memory lives under the resolved `<state_root>/` tree. If state does not exist
yet, follow `references/setup.md`. Seed file shapes live in
`assets/data-templates.md`.

```text
<state_root>/
├── memory.md       # Durable trigger map, depth preferences, integration status
├── checkpoints.md  # Named breakpoint prompts by workflow phase
├── incidents.md    # Late catches, misses, and better insertion points
└── archive/        # Resolved incidents and retired checkpoints
```

Keep workspace integration small:

- SOUL carries the breakpoint habit so critique fires at the right moment.
- AGENTS carries routing for where to read and write trigger memory.
- HEARTBEAT stays optional; this skill interrupts live work rather than running
  a background review loop.

## Core rules

### 1. Critique at breakpoints
Trigger self-critique when work is about to branch, commit, escalate, or become
expensive to unwind. Focus on major steps so critique stays useful.

### 2. Interrupt before the mistake multiplies
Strong insertion points include framework drafts, decomposition into subtasks,
irreversible edits, external actions, and major recommendations. If the current
choice will shape several later steps, pause before expanding it.

### 3. Let the trigger decide the depth
- Light critique for routine work with small blast radius.
- Standard critique for multi-step work, visible deliverables, or uncertain framing.
- Deep critique only when stakes, novelty, or prior misses justify it.

### 4. Store trigger lessons
Save durable lessons about when critique should fire, how deep it should go, and
what kind of miss it should catch. Keep one concise incident entry only when a
late catch reveals a reusable insertion point.

### 5. Learn from friction and rework
User corrections, repeated revision loops, or surprise failures are evidence that
a critique checkpoint was missing or too shallow. Convert those signals into a
better future trigger.

### 6. Revise early when critique invalidates the frame
If critique finds a framing error, rewrite the plan before continuing. Reset a
weak frame while the work is still cheap to change.

### 7. Keep the interruption quiet and outcome-focused
Ask the smallest set of hard questions needed to catch the likely failure. The
goal is fewer downstream corrections.

## Common traps

| Trap | Why it fails | Better move |
|------|--------------|-------------|
| Critiquing only at the very end | The mistake has already propagated | Insert a breakpoint before decomposition or commitment |
| Running deep critique on every task | Burns time and momentum | Match depth to risk and blast radius |
| Logging every imperfection | Memory becomes noisy and useless | Save only reusable trigger lessons |
| Treating user frustration as only a content fix | Misses the broken process step | Ask where critique should have happened earlier |
| Defending the current plan after critique flags it | Locks in sunk-cost behavior | Reset the frame while change is still cheap |

## Scope

This skill covers:

- breakpoint-based self-critique for live work
- local trigger memory under `<state_root>/`
- optional SOUL/AGENTS integration when the user wants it
- learning which checkpoints deserve more or less scrutiny over time

Leave these to other skills or workflows:

- long reflection rituals on every response (`reflection`)
- default heartbeat / background review loops
- storing sensitive user data unrelated to critique timing
- modifying this package's own `SKILL.md` during normal use

## Security and privacy

Data that stays local:

- trigger preferences and critique depth in `<state_root>/memory.md`
- reusable breakpoints in `<state_root>/checkpoints.md`
- late catches and lessons in `<state_root>/incidents.md`

This skill stays offline for its core loop, does not send critique logs to
external services, and edits files outside `<state_root>/` only when the user
explicitly approves workspace integration in that session.
