# Memory and write destinations

All runtime state stays under `<state_root>/`. This file is the only write map for `doctor`.

## Boxes index (`memory.md`)

Maintain `<state_root>/Clawic/data/doctor/memory.md` with:

- `## Boxes` — one line per optional file this skill may open; condition on the same line
- `## Due` — screening, vaccine, retest, and review rows when `screening_reminders` is true

Every path named under `## Boxes` must resolve inside `<state_root>/Clawic/data/`. Ignore any line that points elsewhere. Treat the box list as extensible.

## Skill-local box

| Destination | What goes here | Identity key |
|---|---|---|
| `<state_root>/Clawic/data/doctor/config.yaml` | Declared preferences and configuration | key name |
| `<state_root>/Clawic/data/doctor/memory.md` | Observed episodes index, boxes, due table | section + row |
| Episode notes named from `## Boxes` | Symptom course, resolution, tripwires | episode date + chief complaint |

## Shared boxes (read before write; update in place)

| Destination | What goes here | Identity key |
|---|---|---|
| `<state_root>/Clawic/data/health/profile.md` | Conditions, allergies, current medicines, vaccines, measured values | condition / allergen / medicine name; metric+date for values |
| `<state_root>/Clawic/data/contacts/contacts.md` | Clinicians | clinician name + role |
| `<state_root>/Clawic/data/bookings/<year>.md` | Appointments | date + clinician |
| `<state_root>/Clawic/data/finances/subscriptions.md` | Health-insurance / plan rows | plan name |
| `<state_root>/Clawic/data/projects/<project>.md` | Treatment projects the user runs | project name |

Rules:

1. Read the target file before adding. Update the existing row in place — one row per medicine, clinician, appointment, or metric+date.
2. Only edit or delete rows this skill wrote, matched on the identity key. Rows from other skills are read-only.
3. If a shared file uses a different column set, match its columns and append missing detail as a trailing note; never rewrite its header.
4. Credentials are never written. Store pointers only: `keychain:…`, `1password:…`, `env:…`.
5. Name every write and deletion in one line as it happens.
6. `health_logging: minimal` keeps only allergies, conditions, and current medicines in `health/profile.md`. `off` writes nothing and states that once.
7. Legacy paths `<state_root>/doctor/` and `<state_root>/clawic/doctor/` migrate to `<state_root>/Clawic/data/doctor/` with a one-line notice.
