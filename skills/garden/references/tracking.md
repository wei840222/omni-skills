# Plant & Activity Tracking

Copyable plant, zone, harvest, and activity-log templates live in `assets/garden-data-templates.md`.

## Confirmed Tracking Procedure

1. Provide advice first when a user describes an activity or plant problem.
2. When tracking is not already enabled, ask whether the user wants a record at `<state_root>`.
3. After consent, use the relevant asset template and populate it only with user-provided or user-approved details.
4. Report each updated `<state_root>` path.

## Quick Logging

After the user requests or enables activity tracking, log a garden activity:
1. Parse date (default: today)
2. Identify action type
3. Link to affected plant/zone
4. Append to current month's log

"I watered the tomatoes" →
```
- 💧 Watered tomatoes (raised-bed-1)
```

"Harvested 3 zucchinis" →
```
- 🍅 Harvested zucchini x3
```
For a harvest, offer a corresponding `<state_root>/harvests.md` update after confirmation.
