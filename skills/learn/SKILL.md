---
name: learn
description: >
  Runs self-directed learning as a system: a curriculum with an exit test,
  deliberate practice, spaced review, and proof it transferred. Use when someone
  is teaching themselves a skill or subject with no course and no exam — a
  language, an instrument, a programming language, a new field at work; when
  they ask how to learn X, what to learn first, or how long it will honestly
  take; when months of tutorials produced nothing they can build; when material
  learned earlier is gone, reviews pile up, or the queue gets skipped for weeks;
  when progress stalls on a plateau, motivation collapses, or a skill goes rusty
  after a lapse; when practice feels productive but nothing transfers to real
  work; when an AI answers so fast that nothing is being learned at all; and when
  a plan, review schedule, error log, or mastery record has to survive across
  sessions. Not for teaching a concept in the moment (`learning`), exam and
  coursework planning (`studying`), or authoring decks (`anki`, `flashcards`).
metadata:
  version: "1.0.5"
  openclaw: '{"emoji":"🎓","requires":{"config":["<state_root>/"]},"os":["linux","darwin","win32"],"displayName":"Learn"}'
  related-skills: '{"anki": "Building and repairing Anki decks when `sr_tool` is Anki.", "flashcards": "Atomic card authoring and export formats without owning the long-horizon learning system.", "learning": "Live teach-me sessions that explain a concept, adapt depth, and check understanding in the moment—not multi-week curriculum ownership.", "memory": "Durable personal facts outside any learning topic.", "spaced-repetition": "Scheduler theory and review economy when the ask is SRS mechanics rather than the full learn loop.", "studying": "Exam or coursework plans with a syllabus and a date rather than open-ended self-directed mastery."}'
---

## State location

Learn state may exist in `<workspace>/learn/`, `<workspace>/memory/learn/`, or `~/learn/`.
Shared boxes used by this skill (projects, contacts, finances, profile) resolve under the same workspace-first convention for their own skill names when those skills are installed; this package still ships write formats in `assets/memory-template.md` so the learner can operate without them.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/learn/`, `<workspace>/memory/learn/`, `~/learn/`.
3. If none exists and state must be created, default to `<workspace>/learn/` after the learner wants durable logs.
4. If more than one candidate exists, use the highest-precedence directory and tell the learner that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/learn/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every learn-owned state operation in this skill. Prefer:

- `<state_root>/config.yaml` — declared preferences (`weekly_hours`, `session_minutes`, …)
- `<state_root>/memory.md` — observed topics, `## Boxes` index, `## Due`, error log
- `<state_root>/profile.yaml` — optional shared locale/timezone fallback when present
- Shared boxes by name only: projects → `<workspace>/projects/` (or that skill's resolved root), contacts → contacts skill root, finances/subscriptions → finances skill root

Write only concrete resolved filesystem paths to disk (expand `<state_root>` before any write). Treat legacy `~/Clawic/data/learn/`, `~/clawic/learn/`, and extra `~/learn/` copies outside the active lookup order as migration sources only—ask before migrating; report any move in one line. Credentials are out of scope: store pointers (`env:…`, `keychain:…`, `1password:…`) and strip values.

## Mode

Mode: **act-as** — operate the learner's system with them (plan, quiz, schedule, verify, record); do not lecture. Teaching a concept in the moment is `learning`.

Learning fails in one of five places: the goal was never testable, the material was never retrieved, the practice was too easy, the feedback arrived too late, or the schedule was fiction. Name which one before proposing a fix. Work from defaults immediately; verify goals and hours later. Precedence for any value: `config.yaml` → `<state_root>/profile.yaml` → Configuration table default.

**Data.** At session start, read `<state_root>/config.yaml` and `<state_root>/memory.md` (including `## Boxes` and `## Due`). Open any file `## Boxes` names when its condition applies. In a shared box, update or remove only rows this skill wrote, matched on that box's identity key; leave other skills' rows unmodified and name every write/deletion in one line. State any overdue row in one line before starting work. If none of the state exists, work from defaults and say nothing about missing files.

**Write before the session ends** whenever something durable was produced: plan changes; topic started/verified/paused/retired; review queue grades; mistakes and misconceptions; practice sessions; resource verdicts; cadences; learner-facing artifacts. `assets/memory-template.md` is the only write-format authority—open it when writing.

## When To Use

- Planning a path from zero to a graded outcome in a self-taught skill or subject (no external course/exam owner)
- Running the loop: practice, retrieval, spaced review, error logging, weekly plan checks
- Diagnosing why learning is not working (tutorials with no capability, abandoned queues, no transfer)
- Proving a skill was acquired — transfer tests, calibration, honest failure
- Keeping an earned skill alive, recovering a rusty one, or retiring a topic on purpose
- Live teaching, exam/coursework calendars, and deck authoring stay with `learning`, `studying`, and `anki` / `flashcards` respectively

## When to load references

| Need | File |
|------|------|
| Exit tests and sequenced curricula | `references/curriculum.md` |
| Choosing primary resources | `references/sources.md` |
| Turning input into testable items | `references/capture.md` |
| Deliberate practice and feedback latency | `references/practice.md` |
| Build-to-learn ladders | `references/projects.md` |
| SM-2-shaped intervals, backlog recovery, leeches | `references/schedule.md` |
| Mastery tests and calibration | `references/verification.md` |
| Plateaus, motivation, relearning | `references/plateaus.md` |
| Domain ratios (language, code, music, …) | `references/domains.md` |
| Fitting work into real weeks | `references/time.md` |
| Maintenance doses after verification | `references/maintenance.md` |
| Learning beside an agent / hint policy | `references/ai-assisted.md` |
| Symptom → cause routing | `references/troubleshooting.md` |
| Verified research URLs (Gate 6) | `references/research-sources.md` |
| Memory / shared-box write formats | `assets/memory-template.md` |

## Quick Reference

| Situation | Play | Depth |
|-----------|------|-------|
| "I want to learn X" with no plan | Write the exit test first, then work backwards (Rule 1) | `references/curriculum.md` |
| "How long will this take?" | Hours ÷ `weekly_hours`, quoted as a range (Rule 8) | `references/curriculum.md` |
| Drowning in bookmarked courses | One primary resource; demote the rest | `references/sources.md` |
| Read it, cannot reproduce it | Convert material into items (Rule 2) | `references/capture.md` |
| Sessions happen, capability does not | Measure success rate; retarget difficulty (Rule 4) | `references/practice.md` |
| Tutorial hell — freezes on blank file | Copy → modify → blank-file ladder | `references/projects.md` |
| Reviews pile up / queue abandoned | Backlog recovery, then cap intake (Rule 3) | `references/schedule.md` |
| Same item failed five times | Leech protocol: reformulate or drop | `references/schedule.md` |
| "I think I know it" | Mastery Ladder + unseen transfer test | `references/verification.md` |
| Confidently wrong | Confidence before check; hunt high-confidence misses | `references/verification.md` |
| Plateau / motivation collapse | Plateau vs wrong practice vs burnout | `references/plateaus.md` |
| Returning after a lapse | Measure what survived before rebuilding | `references/plateaus.md` |
| Domain-specific ratios | Same loop; different drills | `references/domains.md` |
| Five hours/week, twenty-hour plan | Minimum effective dose | `references/time.md` |
| Learned it, gone in six months | Maintenance dose into `## Due` | `references/maintenance.md` |
| AI answers before the learner tries | Raise `hint_policy` | `references/ai-assisted.md` |
| No mentor / slow feedback | Latency-ranked substitutes + self-rubric | `references/practice.md` |
| Anything else | Name the failure place, then route | `references/troubleshooting.md` |

## Core Rules

1. **Write the exit test before choosing a resource.** "Done" is an observable performance with conditions. Goals without a performance ("understand Rust") cannot be sequenced. Cut everything that does not move the exit test (`references/curriculum.md`).
2. **Retrieval before re-exposure, every session.** Open by producing last session's material from memory. On delayed tests, retrieval practice beats rereading; same-day quizzes hide the gap (`references/capture.md`, `references/research-sources.md`).
3. **The schedule is a formula with a workload.** SM-2 shape: `next = last_interval × ease`, ease starts 2.5, −0.20 on failure, floor 1.3; failure resets interval to 1 day but keeps history. At `retention_target` 0.90, budget **8–12 daily reviews per 1 new item/day**. Raising target toward 0.95 multiplies review load roughly 1.5–2× (`references/schedule.md`).
4. **Practice near ~85% success.** Above ~90% teaches little; below ~75% encodes errors. Measure the last 20 attempts; adjust difficulty, not ambition (`references/practice.md`).
5. **Three to four new items, then a retrieval block.** Working memory holds ~4 chunks; a fifth new concept before retrieval evicts one of the first four (`references/capture.md`).
6. **Block until fluent, then interleave.** Massed practice wins in-session and loses on delayed tests (desirable difficulties). Switch near ~80% within-session success (`references/practice.md`).
7. **Feedback latency is a design parameter.** Drills: same minute; exercises: same session; projects: ≤48h to a working signal or review. Slower loops need a proxy chosen before practice (`references/practice.md`).
8. **Quote a range, never a date.** `weeks = total_hours ÷ weekly_hours`, then state `weeks` to `2 × weeks` and what the upper end assumes.
9. **Unscheduled skills decay.** After verification, set the first maintenance touch at the last working interval (often 30–90 days for knowledge) in `## Due` (`references/maintenance.md`).

## Why Nothing Sticks

| Symptom | Most likely cause | First move |
|---|---|---|
| Understands explanation, blanks alone | No retrieval yet | Close notes; reproduce; then check (Rule 2) |
| Perfect today, gone in three weeks | No spacing | Expanding interval (`references/schedule.md`) |
| Passes exercises, fails real task | Pre-decomposed practice | Unprompted method choice (`references/practice.md`) |
| Months of tutorials, blank-file freeze | Scaffolding never removed | Copy → modify → blank (`references/projects.md`) |
| Confident and wrong | Fluency illusion | Confidence before check (`references/verification.md`) |
| Reviews take an hour and get skipped | Intake ratio ignored | Suspend news; drain; recap (Rule 3) |
| One item fails repeatedly | Leech / malformed item | Reformulate or drop |
| Fast then flat | Plateau vs wrong practice vs burnout | Three-question split (`references/plateaus.md`) |
| Can read, cannot speak / produce | Trained recognition only | Production pressure (`references/domains.md`) |
| Knew it, took months off | Normal decay | Test first; rebuild misses |
| Sessions feel productive, capability flat | Difficulty too low or feedback too slow | Rules 4 and 7 |
| Fine with the agent, helpless without | Retrieval offloaded to AI | `hint_policy: after-attempt` or `never` |
| Anything else | Locate the five failure places | `references/troubleshooting.md` |

## The Session Shape

Proportions scale with `session_minutes` (default 45). A session with no production step is a reading session with extra steps.

| Slice | Share | What happens |
|---|---|---|
| Warm retrieval | 10% | Reproduce last session cold |
| Due reviews | 15% | Queue up to `daily_review_limit` |
| Hard block | 50% | New material / target drill at ~85% |
| Production | 20% | Build / write / speak / solve without notes |
| Close | 5% | Grade queue, write errors, name next opener |

At ≤20 minutes, drop the hard block; keep retrieval + production (`references/time.md`).

## Mastery Ladder

| Level | Test | Does not prove |
|---|---|---|
| Recognition | Pick from options | Real use |
| Recall | Blank-prompt production | Knowing when it applies |
| Application | Unseen same-type problem, unprompted | Transfer outside framing |
| Transfer | Different surface / tool / domain | Durability |
| Retention | Transfer again cold after ≥30 days | — |
| Teaching | Novice can act on the explanation | Speed under pressure |

Promote in `## Topics` only on that level's dated test (`references/verification.md`).

## Output Gates

- Observable exit test with conditions you could grade today (Rule 1)?
- Learner produced from memory before seeing answers?
- Estimate is a range from `weekly_hours`, not a date (Rule 8)?
- Intake respects review ratio; queue drainable inside `daily_review_limit` (Rule 3)?
- Success rate near 85%, or difficulty changed (Rule 4)?
- Every practiced item has a correction path with stated latency (Rule 7)?
- Promotions backed by that level's dated test?
- Durable outputs written via `assets/memory-template.md` this turn?

## Configuration

Store declared values in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| weekly_hours | number (0.5–40) | 5 | Curriculum budget; Rule 8 divisor |
| session_minutes | number (10–180) | 45 | Session Shape scale; ≤20 short variant |
| daily_review_limit | number (5–200) | 20 | Cap + sustainable intake (Rule 3) |
| retention_target | number (0.70–0.97) | 0.90 | Interval growth / review load |
| hint_policy | on-request \| after-attempt \| never | after-attempt | When hints/answers are allowed |
| sr_tool | this-skill \| anki \| other \| none | this-skill | Where the queue lives |
| practice_bias | drills \| projects \| balanced | balanced | Hard-block mix |
| plan_review_weeks | number (1–12) | 4 | Plan re-check cadence → `## Due` |

Preference areas (record when stated): tooling, conventions, subject mix, rigor posture, output register, accountability, cadence.

## Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Collecting resources instead of starting | Choosing has no failure state | One primary + dated finish line |
| Highlighting / re-reading | Familiarity ≠ retrieval | Convert to items (Rule 2) |
| Grading with the answer visible | Every answer looks obvious | Confidence before reveal |
| Adding cards on a good day | Rule 3 debt | Cap intake at `daily_review_limit ÷ 10` |
| Restarting beginner course after a lapse | Burns relearning savings | Test first; rebuild misses |
| Practising only what works | Flat ceiling | Hold ~85%; hunt error list |
| Twenty-hour plans on five-hour weeks | Plan dies in month two | Size to `weekly_hours` |
| Course completion as mastery | Attendance ≠ capability | Run the exit test |
| Asking the agent instead of retrieving | No reconstruction | `hint_policy: after-attempt` |
| Studying notation instead of the skill | Theory without production | Production every session |
| Plan outliving evidence | Fiction nobody rereads | `plan_review_weeks` in `## Due` |
| Silent topic drop | Guilt + debt | Retire with date + reason |

## Where Experts Disagree

- **SRS backbone vs garnish** — queue facts that block work when lookup is slow; otherwise practise the workflow (`references/schedule.md`).
- **Projects first vs fundamentals first** — project-first with an explicit gap log (`references/projects.md`).
- **Immersion vs graded input** — immersion after ~90% known; graded below (`references/domains.md`).
- **Deliberate practice as the whole story** — contested as sole expert predictor; keep the operational core: defined sub-skill, above-comfort difficulty, immediate feedback, corrected repetition (`references/research-sources.md`).
- **Streaks** — habit vs fake sessions; track a minimum quality dose (`references/time.md`).
