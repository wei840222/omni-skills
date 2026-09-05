# Core Rules and Logic

## Core Rules

1. **Day 1 is the first day of full flow, not spotting.** Prediction math anchors on Day 1; counting spotting as Day 1 shifts every downstream date by 1-2 days.
2. **Predict from her median, never a textbook constant.** `next start = last Day 1 + median(last prediction_window cycle lengths)`. Median resists the one outlier cycle a mean would drag. Below 3 cycles there is no baseline: say so.
3. **Attach a range, not a point.** `range = ± (longest − shortest)/2` over the window, rounded up. A woman with cycles 26-34 gets "predicted day X, plus or minus 4 days," always provide a date range.
4. **Ovulation is back-counted, not forward-counted.** `ovulation ≈ next predicted period − 14`. The luteal phase is relatively fixed (~10-16 days); the follicular phase is what varies. This is why long cycles delay ovulation but keep the luteal length.
5. **Classify against FIGO ranges (§Classifying), not against 28.** For adults, 24-38 day cycles are normal frequency; assess regularity against the age-appropriate 7-9 day variation threshold. Irregular is a description, not a defect. PCOS and perimenopause produce genuinely long cycles.
6. **Flag against HER baseline once >=3 cycles set it.** A sustained shift of >9 days in cycle length, or any Red Flag signal, is worth surfacing. A single off cycle is noise, not a flag.
7. **On hormonal contraception, bleeding is not a cycle.** Withdrawal and breakthrough bleeds are method effects, not ovulation — bypass rules 2-4 on them (`references/contraception.md`).


## Prediction Math (worked)

Logged Day 1 dates: Jan 3, Jan 31, Feb 26, Mar 27. Cycle lengths: 28, 26, 29 days.
- Median = 28. Shortest 26, longest 29 → half-spread = (29−26)/2 = 1.5, round to 2.
- Next period = Mar 27 + 28 = **Apr 24, plus or minus 2 days**.
- Ovulation = Apr 24 − 14 = **~Apr 10**. Fertile window = Apr 5 through Apr 10.

If she has only 2 cycles, report "roughly late April, still learning your pattern" and refuse a hard date. Recompute the median every new cycle. The window is the last `prediction_window` cycles (default 6) and exclude cycles older than 12 months — storage keeps everything (her data), but stale drift never re-enters the estimate.


## Classifying A Cycle (FIGO thresholds)

| Axis | Normal | Outside normal |
|------|--------|----------------|
| Frequency (Day 1 to Day 1) | 24-38 days | <24 frequent; >38 infrequent |
| Regularity (spread over 12 cycles) | <=7-9 days, depending on age | > the age-appropriate threshold = irregular |
| Duration (days of bleeding) | 2-8 days | >8 prolonged; <2 very short |
| Flow | soaks a normal pad/tampon in 3-6h | hourly for 2h+, clots >2.5 cm, or >80 mL/cycle = heavy |

These are adult ranges; adolescent and perimenopausal normals differ (`references/irregular.md`). Irregular by these axes is common with PCOS, perimenopause, thyroid issues, or high stress. Report the classification; do not name the cause.


## Fertility Signals (opt-in only)

Enable only when `fertility_tracking` is set or she explicitly asks. Three confirming signals, ranked by predictive value:
- **LH surge (ovulation predictor kit):** positive means ovulation in ~24-36 hours. Best forward predictor.
- **Cervical mucus:** clear, stretchy, egg-white texture marks peak fertility (the 1-2 days before ovulation).
- **Basal body temperature:** a sustained rise of 0.3-0.5 C confirms ovulation already happened — retrospective, so it verifies a cycle but cannot predict the current one.
Cross-check the calendar estimate (rule 4) against these; when they disagree, live signals win. Protocols, conceive/avoid modes, and test timing: `references/fertility.md`.
