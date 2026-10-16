# Bookings and deadlines

## Shared box

Write flights, stays, cars, trains, and tickets to
`<state_root>/bookings/<year>.md` as one row per locator:

`date | type | provider | locator | travellers | status | free change/cancel until | amount with currency | trip`

- Update the locator row in place; never append a duplicate.
- Leave rows written by other skills untouched.
- If columns differ, match the existing header.

## Due table

Put free-change / free-cancel timestamps into `<state_root>/memory.md` `## Due`
in the property's local time the moment the reservation exists.
