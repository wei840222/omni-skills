# Memory and configuration guide

## Resolve state first

Follow `SKILL.md` **State location** before any read/write. Never persist the literal `<state_root>` string.

## Default config (`config.yaml`)

| Variable | Type | Default | Effect |
|----------|------|---------|--------|
| mode | act-as \| advise | act-as | Coach the user vs support the user-as-coach |
| session_model | grow \| oskar \| clear \| none | grow | Session arc |
| session_length_min | number (15–90) | 45 | Scales phase shares |
| checkin_cadence | daily \| weekly \| biweekly \| monthly \| none | weekly | Post-30-day repeating-behavior check-ins; `## Due` rows |
| commitment_cap | number (1–5) | 3 | Hard ceiling per session |
| challenge_level | supportive \| balanced \| direct | balanced | How bluntly patterns are named |
| advice_mode | pure \| hybrid | hybrid | Whether expertise may be offered with a named switch |
| horizon_days | number (30–365) | 90 | Goal planning chunk + review date |
| notes_detail | none \| brief \| full | brief | Session note depth; `none` still records commitments/misses |
| niche | text | none | Default niche slice and progress metrics |

Preference areas (store when stated): tooling for commitments, goal phrasing conventions, timezone/locale/currency, safety posture, output register, cadence, ethics extras, practice model.

## `memory.md` shape

```text
# Coach memory

## Boxes
- clients/ → when advise mode names a client file
- commitments → open board if used
- sessions/2026.md → when notes_detail != none

## Due
| When | What | Source |
|------|------|--------|

## Patterns
- (observables across sessions; mark coach theories as yours)

## Boundaries
- referral fact + date only
```

## Write destinations

| Durable event | Destination |
|---------------|-------------|
| Commitment made/kept/missed | `commitments.md` and/or session note; update `## Due` |
| Goal change | `memory.md` + client file if advise |
| Session held | `sessions/<year>.md` per notes_detail |
| New client / contract / rate | `clients/<name>.md` |
| Referral | client file or `## Boundaries` — fact+date only |
| Pattern named | `## Patterns` |
| User artifact (plan, values, agreement) | path under `<state_root>/` agreed with user |

## Shared contacts

- One person one row; identity `Key` = lowercased email → handle → `<kebab-name>` + disambiguator.
- Read before add; update in place on key match.
- Coaching-specific material stays in `clients/<name>.md` and references the person by name only.
- In shared boxes, update/delete **only rows this skill wrote**, matched on identity key. Other skills' rows are read-only.
- Announce each write/deletion in one line as it happens.

## Credentials

Never write secrets under `<state_root>/`. Store pointers only:

- `env:CALENDLY_TOKEN`
- `keychain:coaching-portal`
- `1password:Work/Practice/stripe`
- `file:~/.config/invoicing/creds`

Strip values from anything the user pastes to save.
