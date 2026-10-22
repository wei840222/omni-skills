# Progress Tracking System

All paths below are under the resolved `<state_root>/` from `SKILL.md`.

## Score Tracking

Maintain in `<state_root>/profile.md`:

```text
## Score History
| Date | RW | Math | Total | Form | Notes |
|------|----|------|-------|------|-------|
| 2026-01-15 | 650 | 700 | 1350 | Bluebook PT1 | Diagnostic |
| 2026-02-01 | 680 | 720 | 1400 | Bluebook PT2 | Timed, quiet room |
```

Update after every full practice test. Note whether conditions matched test day (device, timing, breaks).

## Section-Level Tracking

For each section, track in `<state_root>/sections/`:

**Reading and Writing (`rw.md`):**

```text
## Domain Accuracy
- Craft and Structure: 78% (last test)
- Information and Ideas: 85%
- Standard English Conventions: 65% ← PRIORITY
- Expression of Ideas: 70%

## Weak Topics
- Comma usage in complex sentences
- Transition word selection
- Vocabulary in context (advanced)
```

**Math (`math.md`):**

```text
## Domain Accuracy
- Algebra: 88%
- Advanced Math: 72% ← PRIORITY
- Problem-Solving and Data Analysis: 80%
- Geometry and Trigonometry: 67% ← PRIORITY

## Weak Topics
- Quadratic word problems
- Circle equations
- Systems with no/infinite solutions
```

## Mistake Log

Track every wrong answer in `<state_root>/mistakes/`:

```text
## 2026-02-01 Practice Test
| Q# | Section | Topic | Error Type | Review Date |
|----|---------|-------|------------|-------------|
| 17 | RW | Transitions | Misread context | 2026-02-08 |
| 32 | Math | Quadratics | Calculation | 2026-02-05 |
| 41 | Math | Geometry | Concept gap | 2026-02-08 |
```

Error types:

- **Concept gap** — Did not know how to solve
- **Calculation** — Knew method, arithmetic/algebra slip
- **Misread** — Misread the question or stimulus
- **Time pressure** — Rushed due to clock
- **Careless** — Knew it, silly miss

## Time Analysis

Track time per question / module to find slow areas:

```text
## Timing Patterns
- RW average: 1.1 min/question (budget ≈ 1.2)
- Math average: 1.8 min/question (budget ≈ 1.6) ← TOO SLOW

Slowest topics:
- Geometry word problems: 2.5 min avg
- Reading inference: 1.8 min avg
```

## Score Prediction Model

Based on practice data, predict test-day score only from **timed Bluebook-like** forms:

```text
Diagnostic: 1350
Practice avg (last 3 timed): 1420
Improvement rate: +23 pts/week
Days until test: 21

Predicted score: 1450-1490
Confidence: Medium (need more official practice tests)
```

Factors that affect prediction:

- Practice test conditions (timed? distraction-free? Bluebook?)
- Number of official tests taken
- Score variance across tests
- Recency of practice
- Whether Module 1 accuracy is stable enough to reach harder Module 2 paths
