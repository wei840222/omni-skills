# Schedule — Intervals, Load, Leeches

Load for review math, abandoned queues, and repeated failures.

## SM-2 shape (when `sr_tool` is this-skill)

- `next = last_interval × ease`
- ease starts at 2.5; −0.20 on failure; floor 1.3
- failure resets interval to 1 day; keep item history

This is an operational default aligned with classic SM-2 notes, not a claim that SM-2 beats FSRS for every deck. If `sr_tool` is Anki/other, own cadence/leeches/workload here and leave algorithm knobs to that tool (`spaced-repetition`, `anki`).

## Intake ratio

At `retention_target` ≈ 0.90, budget **8–12 daily reviews per 1 new item/day** in mature queues. Raising target toward 0.95 multiplies reviews roughly 1.5–2× for small recall gains—treat retention as a workload dial.

## Backlog recovery

1. Suspend new items
2. Drain due/overdue inside `daily_review_limit`
3. Resume intake at `daily_review_limit ÷ 10` until stable for a month

Never silently skip overflow—reschedule by the formula.

## Leeches

After ~5 failures on the same wording: reformulate, split, add mnemonic/image, or drop. Re-drilling the identical broken item encodes frustration, not memory.
