# Event file templates

Use these shapes under the resolved `<state_root>/`. Replace placeholders; omit sections the user did not provide rather than inventing values.

## Single upcoming event

Path examples:

- `<state_root>/upcoming/concerts/radiohead-msg-2026-05-15.md`
- `<state_root>/upcoming/appointments/dentist-2026-03-12.md`
- `<state_root>/upcoming/social/jakes-birthday-2026-03-05.md`
- `<state_root>/upcoming/conferences/sxsw-austin-2026.md` (or a folder for multi-day)

```markdown
# radiohead-msg-2026-05-15

## Event
Radiohead — MSG

## Date & Time
2026-05-15, 20:00 (doors 19:00)

## Venue
Madison Square Garden, NYC

## Tickets
Section 112, Row 8
Confirmation: TM-789456

## People
Going with Jake; meet 18:30 at the main entrance

## Logistics
No large bags; subway preferred; rain plan: indoor meetup still holds

## Deadlines
- Leave home by 17:45
- Exchange/transfer cutoff: (if any)

## Status
upcoming
```

## Hosting folder

```text
<state_root>/hosting/birthday-2026/
├── overview.md
├── guests.md
└── details.md
```

### overview.md

```markdown
# Birthday 2026 — overview

- Date: 2026-04-12, 18:00–22:00
- Venue: home / rented space
- Capacity: 20
- Status checklist:
  - [ ] Venue confirmed
  - [ ] Invitations sent
  - [ ] Food locked
  - [ ] Playlist ready
  - [ ] Day-of run of show
```

### guests.md

```markdown
## Confirmed (12)
- Sarah +1
- Jake

## Pending (5)
- Tom — follow up by 2026-04-01

## Declined (2)
- Amy — out of town
```

### details.md

```markdown
## Food & drinks
...

## Music / setup
...

## Supplies
...
```

## Multi-day event folder

```text
<state_root>/upcoming/conferences/sxsw-2026/
├── overview.md
└── schedule.md
```

### overview.md

```markdown
# SXSW 2026

- Dates: 2026-03-12 → 2026-03-14
- Location: Austin, TX
- Registration ID: ...
- Travel / lodging: ...
- Ticket / badge pickup: ...
```

### schedule.md

```markdown
## 2026-03-12
- 09:00 badge pickup
- 14:00 session …

## 2026-03-13
- …
```

## Annual recurring

Path: `<state_root>/annual/recurring.md`

```markdown
## Birthdays
- Mom: 03-22
- Dad: 07-08

## Annual Events
- Company retreat: September (confirm date yearly)
- Industry conference: March (register early)
```

## Month calendar view

Path: `<state_root>/calendar.md`

Rebuild from `upcoming/` + `annual/recurring.md` when answering "what's next" if stale.

```markdown
## 2026-03
- 05: Jake's birthday party
- 12–14: SXSW Austin
- 22: Mom's birthday
```

## Naming conventions

- Prefer `slug-yyyy-mm-dd.md` for dated singles.
- Use folders when more than one file is required (hosting, multi-day).
- After the event ends, move the file/folder to `<state_root>/past/` keeping the same basename.
