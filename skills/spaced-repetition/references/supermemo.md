# SM-2 and FSRS Decision Notes

Load when choosing or explaining a scheduler, diagnosing interval explosion / ease hell, or setting desired retention.

## SM-2 (legacy heuristic)

- Each successful review multiplies the prior interval by an ease factor; "hard"/"easy" drift that factor.
- There is no explicit retention target; the schedule is a heuristic.
- Failure mode: early "easy" grades inflate ease, then intervals explode (multi-month gaps the learner will actually fail).
- Primary write-up: https://www.supermemo.com/en/archives1990-2015/english/ol/sm2

## FSRS (retention-targeted)

- Optimizes toward a desired retention (Anki default commonly 0.90) using parameters fit on the learner's review history.
- Fresh profiles with little history use defaults; fit quality improves as reviews accumulate (order-of-magnitude guidance: ~1k reviews before judging personalization).
- Desired retention is the workload dial: higher targets buy recall with sharply rising review counts (ABC of FSRS).
- Sources: https://github.com/open-spaced-repetition/fsrs4anki and https://github.com/open-spaced-repetition/fsrs4anki/wiki/ABC-of-FSRS
- Product controls live in Anki deck options: https://docs.ankiweb.net/deck-options.html

## Migration note

Moving SM-2 → FSRS re-estimates intervals from history. Expect some cards to shorten (were over-scheduled) and some to lengthen. Wait about a month of honest grading before judging the new schedule.
