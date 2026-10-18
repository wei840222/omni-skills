# Core Rules

## 1. Bootstrap the Learning OS before the first lesson

If `<state_root>/` is missing or empty, create the full scaffold from `blueprint.md`.
Start teaching only when all of the following are present:

- global memory file
- router files
- at least one topic namespace

## 2. Offer optional AGENTS router integration

If the user wants automatic routing, provide the AGENTS router snippet from `activation-routing.md`.
Generate snippet text only; the user applies it.
If the user skips router integration, keep the skill fully manual and user-invocable.

## 3. Keep each topic isolated, then coordinate globally

Every topic gets its own namespace under `<state_root>/topics/<topic-slug>/`.
Keep files segregated by topic.
Global planning may schedule multiple topics in one day, but lesson state stays per-topic.

## 4. Run lessons as tight interactive loops

Use `lesson-loop.md` for every session:

1. micro-challenge
2. learner attempt
3. immediate correction
4. reinforcement challenge
5. queue update

One loop should finish in about 60–90 seconds.

## 5. Support concurrent tracks without context loss

The user can learn multiple topics at once (for example English and cooking).
For each session, select one active topic, load only that namespace, then update the global planner with:

- completion result
- next due lesson
- next review date

## 6. Use a transparent progression economy

Apply XP, hearts, streaks, and mastery rules from `progression.md`.
Rewards reflect demonstrated learning instead of random activity.
When motivation drops, adjust pacing before adding gamification complexity.

## 7. Prioritize retention and review over new content volume

Follow `retention-ops.md` and `launch-scorecard.md` weekly.
A healthy system always knows:

- what to review now
- what to practice next
- why the learner returned or stayed away
