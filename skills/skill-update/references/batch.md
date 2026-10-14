# Batch Updates — Many Skills at Once

"Update everything" is one sentence of consent covering many behavior changes.
Keep the batch honest: cheap updates flow, risky ones get singled out.

## Triage first

```bash
npx clawic list    # installed + versions; compare against published
```

Split every pending update into three buckets before touching anything:

| Bucket | Contents | Handling |
|---|---|---|
| Flow | Patches and minors, clean diffs, no local edits | Batch together: one combined preview, one approval |
| Single out | Majors, breaking signals, migrations, local edits | Each gets its own preview and its own yes |
| Skip | `pinned_skills`, skills mid-use in active work | Named in the report as skipped, with the reason |

`update --all` is only safe when the "single out" bucket is empty. Otherwise
handle risky ones first (or exclude them), then flow the rest.

## The combined preview

One message, three parts, in this order:

1. **Singled out** (needs individual decisions): slug, delta, one line on why.
2. **Flowing** (one yes covers these): slug + delta + one-line summary each. A
   skill whose summary cannot honestly say "no behavior change that touches you"
   belongs in the singled-out list.
3. **Skipped**: slug + reason (pinned, in use).

Backups still happen per skill — one timestamped folder each under
`<state_root>/backups/`, one update-log line each. Batch consent never batches
the backups away.

## Order within the batch

- Related sets move together: skills that reference each other or share data
  conventions update in the same batch or not at all.
- A skill whose update changes its data format goes **last** in its set: migrate
  once, after everything reading that data is current.
- Otherwise order does not matter; do not invent ceremony.

## Mid-batch failure

One skill fails at position k of n:

1. Stop the batch — do not finish the rest and come back.
2. Report the split: 1..k-1 applied, k failed (with the error), k+1..n untouched.
3. Offer rollback for the failed skill only; already-applied ones stay unless
   the user says otherwise.
4. Resume the remainder only on a fresh go-ahead.

## Verify after a batch

One real task per singled-out skill; for the flow bucket, one task on the skill
the user uses most is the honest floor — say which skills were verified and
which were not.

## Batch report

Close with a table the update log mirrors: slug · old→new ·
applied/failed/skipped · backup path. The user should reconstruct the whole
batch from this one table a week later.
