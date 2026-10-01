# Configuration rules — Learning

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml` (loading procedure: `references/setup.md`).

| Variable | Type | Default | Effect |
|---|---|---|---|
| entry_format | prose \| example-first \| code-first \| visual | example-first | Starting rung on the format ladder (`references/formats.md`); demonstrated performance still moves it (core Rule 6) |
| depth_default | overview \| standard \| deep | standard | Initial breadth for a new topic before probes adjust; overview compresses to core concepts and deltas |
| pace | relaxed \| standard \| intensive | standard | Where each exchange sits within the 3-5 concept cap and how much consolidation is interleaved; respects the cap |
| check_style | open \| scenario \| mixed | mixed | Surface form of retrieval checks (`references/questions.md`); the generation requirement itself is not configurable |

Preference areas — a stated preference gets recorded in `config.yaml` and applied:

- **Formats** — which ladder rungs work for this learner (diagrams, analogies, code) — sets entry choices in `references/formats.md`
- **Checking** — appetite for being quizzed, tolerated question forms — reshapes check surface in `references/questions.md`, keeps generation
- **Pacing** — session length, review cadence, deadline habits — scales the schedules in `references/retention.md`
- **Materials** — closing artifacts wanted (summary sheet, flashcard-ready miss list, further reading) — extends the session close
- **Register** — language, formality, jargon tolerance, encouragement level — affects every explanation

Universal variables (language, locale): read `<state_root>/profile.yaml` as shared fallback when present. Precedence: `config.yaml` > `profile.yaml` > table defaults.
