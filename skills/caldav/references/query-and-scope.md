# Query windows and calendar scope

## Prefer bounded windows

- Use day, 7-day, 14-day, or exact date-range queries instead of open-ended searches.
- Narrow to a specific calendar whenever the user already knows the target.
- Resolve phrases such as "next Friday" or "this evening" into exact dates, times, and timezone assumptions before any write.

## Ambiguity controls

- Titles are not unique identifiers. Duplicate-event risk rises quickly when searching across every calendar at once.
- Prefer title + start + calendar, or UID when available, as the match key.
- If multiple events still match, list the candidates and ask which one to change.

## Read pattern

1. Sync when freshness matters.
2. Query the smallest sufficient window on the intended calendar.
3. Report the returned title, time, calendar, and any UID used for later verification.
