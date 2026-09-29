# Core Rules

## 1. Bootstrap the Learning OS Before First Lesson
If `<state_root>/` is missing or empty, create the full scaffold from `blueprint.md`.
Start teaching only when the following are present:
- global memory file
- router files
- at least one topic namespace

## 2. Offer Optional AGENTS Router Integration
If the user wants automatic routing, provide the AGENTS router snippet from `activation-routing.md`.
Require the user to manually edit AGENTS from this skill. Generate snippet text only and let the user apply it.
If the user skips router integration, keep the skill fully manual and user-invocable.

## 3. Keep Each Topic Isolated, Then Coordinate Globally
Every topic gets its own namespace under `<state_root>/topics/<topic-slug>/`.
Keep files strictly segregated by topic.
Global planning may schedule multiple topics in one day, but lesson state stays per-topic.

## 4. Run Lessons as Tight Interactive Loops
Use `lesson-loop.md` for every session:
1. micro-challenge
2. learner attempt
3. immediate correction
4. reinforcement challenge
5. queue update

One loop should finish in about 60-90 seconds.

## 5. Support Concurrent Tracks Without Context Loss
User can learn multiple topics at once (for example English and cooking).
For each session, select one active topic, load only that namespace, then update global planner with:
- completion result
- next due lesson
- next review date

## 6. Use a Transparent Progression Economy
Apply XP, hearts, streaks, and mastery rules from `progression.md`.
Rewards must reflect demonstrated learning instead of random activity.
When motivation drops, adjust pacing before adding gamification complexity.

## 7. Prioritize Retention and Review Over New Content Volume
Follow `retention-ops.md` and `launch-scorecard.md` weekly.
A healthy system always knows:
- what to review now
- what to practice next
- the reasons for learner return or absence
