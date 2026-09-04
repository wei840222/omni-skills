# Configuration

Store a preference in `<state_root>/config.yaml` only after the user has stated it. Defaults apply otherwise.

| Variable | Type | Default | Effect |
|---|---|---|---|
| `max_active_habits` | integer 1–12 | 3 | Limits concurrent habits. |
| `week_start` | `monday` or `sunday` | `monday` | Defines `N×/week` and weekly windows. |
| `day_boundary` | `HH:MM` | `04:00` | Assigns late-night completions to a calendar day. |
| `primary_metric` | `completion-rate` or `streak` | `completion-rate` | Selects the leading status metric; report both. |
| `streak_freeze_budget` | integer 0–4/month | 1 | Plans exclusions from scheduled days. |
| `checkin_style` | `batch`, `per-habit`, or `none` | `batch` | Shapes daily check-ins. |
| `review_day` | weekday | `sunday` | Sets weekly-review timing. |
| `stakes_allowed` | boolean | `false` | Allows stakes only after explicit preference. |
| `external_tracker` | tracker name or `none` | `none` | Makes that tracker the completion source of truth. |

Keep preferences separate from completion records: use `<state_root>/logs/YYYY-MM.md` for completions and misses, and `<state_root>/memory.md` for definitions, review notes, and the durable record.
