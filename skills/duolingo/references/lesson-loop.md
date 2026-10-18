# Lesson Runtime Loop

Every session runs one topic at a time with quick iterations.

## Standard loop (60–90 seconds)

1. Present one micro-challenge.
2. Collect attempt (retrieval before reveal).
3. Grade and explain one correction.
4. Run one reinforcement prompt.
5. Update queue and session log.

## Placement loop (new topic)

- Run 2–5 questions from easy to hard.
- Conclude after a clear level signal.
- Set the initial lane in `curriculum.md`.
- Add first lessons to `queue.md`.

## Session writeback

After each loop, update:

- `topics/<slug>/sessions.md` with outcome
- `topics/<slug>/queue.md` with next item
- `memory.md` with streak and rotation notes

## Difficulty adjustments

- 2 misses in a row → drop one difficulty step.
- 3 clean wins in a row → raise one step.
- Repeated misses on the same node → inject guided review before new content.

## Exit rule

Session ends only after a clear next action is queued:

- next lesson id
- next review due window
- checkpoint trigger if threshold met
