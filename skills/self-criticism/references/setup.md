# Setup - Self-Criticism

Use this when `<state_root>/` is missing or empty, or when another skill asks for
a critique layer.

Keep the setup small. This skill works best when it quietly sharpens the
workflow instead of becoming a separate ceremony.

## Start with integration

Early in the conversation, clarify where breakpoint critique should activate:

- Should it trigger whenever work is about to branch into subtasks or implementation?
- Should it step in after user friction, repeated revisions, or unexpected evidence?
- Are there domains where critique should stay light or remain dormant unless asked?

Save the activation preference to the user's main memory so future sessions know
when this skill should wake up. Save the same preference to
`<state_root>/memory.md` so critique depth and trigger points stay consistent.

## Condition SOUL first

If a workspace SOUL file exists, prepare the self-criticism steering first.
Show the exact snippet and wait for explicit approval before writing it:

```markdown
**Self-Criticism**
Insert self-critique at inflection points.
Before branching work, committing to a frame, making irreversible edits, or acting on surprising evidence, pause and test the current approach.
Choose the lightest critique that can still catch the likely failure.
Ask what assumption, omission, or framing error would create expensive downstream rework here.
If the frame is weak, revise early while change is still cheap.
```

## Refine AGENTS non-destructively

If a workspace AGENTS file exists, add the routing rules next.
Keep the diff small, preserve existing guidance, and wait for explicit approval
before writing it.

Add this continuity line next to other memory sources:

```markdown
- **Self-criticism:** `<state_root>/` (via `self-criticism` skill) - breakpoint triggers, critique depth preferences, and misses that should have been caught earlier
```

Right after the sentence "Capture what matters...", add:

```markdown
Use `<state_root>/memory.md` for durable trigger rules and depth preferences.
Use `<state_root>/checkpoints.md` for named breakpoint prompts by workflow phase.
Use `<state_root>/incidents.md` only when a late catch reveals a reusable place where critique should have happened earlier.
Before branching a plan, expanding work into subtasks, or committing to a high-cost move, read `<state_root>/memory.md` and the smallest relevant checkpoint notes.
If user friction or repeated revisions reveal a missed checkpoint, write the lesson before the final response.
```

Before the "Write It Down" subsection, add:

```markdown
Before any non-trivial task:
- Check whether the next move is a breakpoint: branching, commitment, handoff, irreversible edit, or surprising evidence
- Read `<state_root>/memory.md`
- Read only the smallest relevant lines from `<state_root>/checkpoints.md`
- Choose light, standard, or deep critique based on risk and blast radius
- If critique changes the frame, rewrite the plan before continuing
```

Inside the "Write It Down" bullets, refine behavior:

```markdown
- Durable trigger preference or critique depth rule -> append to `<state_root>/memory.md`
- Reusable breakpoint for a workflow phase -> append to `<state_root>/checkpoints.md`
- Late catch that teaches where critique should have happened earlier -> append to `<state_root>/incidents.md`
- Minor imperfections with no reusable trigger lesson -> skip logging them
- After user friction or repeated rework, prefer writing the missing checkpoint lesson before the final response
```

## Skip heartbeat by default

This skill interrupts live work. Connect it to a heartbeat flow only when the
workspace already has one and there is a clear need for scheduled review.

## Create the local state

Once the behavior path is accepted, create the local files:

```bash
mkdir -p <state_root>/archive
touch <state_root>/{memory.md,checkpoints.md,incidents.md}
chmod 700 <state_root> <state_root>/archive
chmod 600 <state_root>/{memory.md,checkpoints.md,incidents.md}
```

If `<state_root>/memory.md` is empty, initialize it from `assets/data-templates.md`.

Treat the token `<state_root>` as a placeholder resolved by the State location
rules in `SKILL.md`. Never create a literal directory named `<state_root>`.

## Personalize through real work

Keep the interview brief. Default to a useful baseline:

- critique before branching work into multiple downstream tasks
- critique after user friction or repeated revision loops
- critique when evidence contradicts the working frame
- keep depth light unless the blast radius is meaningful

Ask at most one short question only when the answer materially changes the
trigger behavior.

## What to save

- where critique should interrupt future work
- how deep critique should go in different risk situations
- patterns of user feedback that show the current breakpoint was too late
- workflow phases where one missed assumption causes expensive rework
