# Prompt iteration workflow

## 1. Define the failure

Record the exact failing input, expected result, observed output, model/version, and whether the failure is reproducible.

## 2. Isolate one variable

Choose one causal change: move a constraint, clarify an output field, add one representative example, or revise a source boundary. This isolates the evidence for the result.

## 3. Re-run the original case

Compare the new result with the original failure against the same success criterion. When it passes, continue to regression testing; when it fails, choose the next branch in `references/failures.md`.

## 4. Run regression tests

Test the original failing case, three to five known-working cases, and two relevant boundaries. Record accuracy, format compliance, latency, and cost when those matter to the task.

## 5. Record the durable result

With user authorization for persistence, write the result to `<state_root>/history.md`:

```markdown
[YYYY-MM-DD] task: [description]
- Baseline: [prompt version or identifier]
- Problem: [observed failure and test input]
- Change: [one changed variable]
- Result: [pass/partial/fail with measured evidence]
```

## 6. Compress the passing prompt

Remove one nonessential line at a time and rerun the relevant case. Retain only wording whose removal changes the measured outcome.

## A/B comparison

For two candidate prompts, use the same test set, evaluate against named criteria, and blind the evaluator when practical. Use at least ten examples when the result will guide a production choice; otherwise label the comparison as directional rather than conclusive.
