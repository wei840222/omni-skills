# Verification reference

Consult when verifying implementations visually or with tests.

## Screenshots

- Wait for full page load (no spinners)
- Review yourself before sending
- Split long pages into 3–5 sections (~800px each)
- Caption each: "Hero", "Features", "Footer"

## Before sending

```
[ ] Content loaded
[ ] Shows the specific change
[ ] No visual bugs
[ ] Caption explains what the user sees
```

## Fix-before-send

If a screenshot shows a problem:

1. Fix the code
2. Re-deploy or re-run locally
3. Capture a new screenshot
4. Still broken? → back to 1
5. Fixed? → send

Resolve issues locally before sending reports.

## No UI? Show output

When verifying API endpoints, show the actual output:

```
GET /api/users -> {"id": 1, "name": "test"}
```

Include the actual response payload, not only "it works".

## Flows

Number sequential states: "1/4: Form", "2/4: Loading", "3/4: Error", "4/4: Success".

## Test pyramid orientation

Prefer many narrow unit checks, fewer integration checks, and sparse end-to-end
journeys (see `references/sources.md`). Ask for the failing log before guessing
a build fix.
