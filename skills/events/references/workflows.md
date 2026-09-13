# Event workflows

## Intake → file

1. Resolve `<state_root>` (see SKILL.md).
2. Extract: title, date/time, venue, people, tickets/confirmation, logistics, deadlines.
3. Choose category path under `upcoming/` or `hosting/`.
4. Write with `templates.md`; create parent dirs as needed.
5. Patch `calendar.md` month section if the event falls in the current or next two months.
6. Confirm path + one-line summary to the user.

## "What's coming up?"

1. Read `calendar.md` if present.
2. Scan `upcoming/**/*.md` and hosting folders with future dates.
3. Include annual items from `annual/recurring.md` that fall in the requested window (match month-day to the year in question).
4. Sort ascending by start time; lead each line with the critical logistics hook (doors, deadline, RSVP count).
5. Exclude `past/` unless the user asks for history.

## Registration and ticket discipline

- If the user mentions buying or registering, require a confirmation field before calling the record complete.
- Surface registration close dates at least once when the deadline is inside 7 days.
- Never overwrite a confirmation ID with a weaker note; append history if the user rebooks.

## Hosting loop

1. Create hosting folder + three files from templates.
2. Every guest update edits `guests.md` buckets only — do not scatter RSVP state in chat memory.
3. When the user asks for a nudge text, draft one follow-up at a time; send only with explicit approval.
4. Day-of: promote checklist items in `overview.md` rather than inventing a second list.

## Multi-day ops

- Keep travel/lodging/registration in `overview.md`.
- Keep sessions and meetups in `schedule.md` keyed by date.
- If a session conflicts, flag the clash in schedule notes; do not silently drop an item.

## Lifecycle and archive

| Moment | Action |
|---|---|
| Event ended | Move to `past/`; optional one-line outcome (attended / missed / cancelled) |
| Hosting ended | Move whole folder to `past/`; freeze guest list |
| Cancelled before start | Mark status cancelled in-file, then move to `past/` or delete only with user OK |
| User wants memory write-up | Offer `journal` handoff; do not auto-write reflective essays here |

## Bridges to sibling skills

| User intent | Keep in events | Hand off |
|---|---|---|
| "Remind me at 5 to leave" | Event file + leave-by field | `remind` with fire time |
| "Put this on my Mac calendar" | Durable markdown record | `apple-calendar-macos` |
| "Plan the whole trip" | Conference/event folder anchors | `travel-planning` for booking research |
| "I want to write about last night" | Archive in `past/` | `journal` |

## Conflict handling

- Two events same start: present both; ask which logistics constraint wins (travel time, hard doors).
- Annual vs explicit dated entry: dated `upcoming/` wins for that year; keep annual as the recurring template.
- Duplicate files for one show: merge into the richer file, delete duplicate only after user confirms.
