# Core Rules and Scope

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure.

```text
<state_root>/
├── memory.md           # Household summary, activation, red flags, shared rules
├── cats/
│   └── {name}/
│       ├── profile.md
│       ├── timeline.md
│       ├── health.md
│       ├── routines.md
│       ├── behavior.md
│       └── logistics.md
├── shopping.md         # Shared supplies and reorder thresholds
└── sitter-packs/       # Exportable care instructions for trips or absences
```

## Scope

This skill helps with:
- real-world cat care, records, logistics, and behavior tracking
- local files under `<state_root>/` after the user approves memory
- conservative triage and preparation support for veterinary conversations

This skill must:
- state limits when evaluating short descriptions
- send medication dose, human medicine, and toxicology decisions to a veterinarian
- escalate to emergency care immediately when cat-specific red flags appear
- require user approval before writing to memory

## Core Rules

### 1. Start with cat-specific triage

Use `triage.md` before giving advice on symptoms or sudden changes.

Check the smallest set of facts needed to judge risk:
- age and life stage
- sex if urinary risk matters
- indoor or outdoor access
- appetite, water, energy, and hiding
- litter box output and vomiting
- toxins, trauma, and current medication

If breathing trouble, collapse, repeated nonproductive retching, major trauma, toxin exposure, or straining without urine appears, switch to emergency guidance immediately.

### 2. Keep one living record per cat

Use `records.md` and `assets/memory-template.md` to keep each cat's facts stable across sessions.

Store durable facts such as:
- identity, age range, microchip, and household role
- conditions, allergies, meds, and regular vet details
- reliable food, litter, handling, and travel preferences
- ongoing behavior patterns and major milestones

Separate confirmed facts from guesses, and log dates for symptom changes, appointments, and treatments.

### 3. Litter, appetite, and hiding are primary signals

Cats hide decline early. Give extra weight to:
- new litter box avoidance or straining
- reduced appetite or unusual thirst
- hiding, withdrawal, or reduced grooming
- sudden aggression, vocalization, or mobility change

Check health and environment first before labeling the pattern as attitude.

### 4. Solve behavior through environment before force

Use `behavior.md` and `household.md` to fix patterns with setup, routine, and stress reduction.

Prefer:
- litter box changes
- vertical territory and hiding spots
- better scratching options
- shorter, more predictable handling
- introductions done through distance and scent

Use positive reinforcement and gradual exposure rather than punishment or forced exposure.

### 5. Plan around territory and stress

Cats usually care more about safety, predictability, and control than novelty.

When the user mentions:
- visitors
- a new pet or baby
- travel or moving
- carrier fights
- boarding or sitter handoff

load `travel.md` or `household.md` and reduce the plan to the least stressful path.

### 6. Coordinate logistics proactively but safely

Use `records.md` for vet prep, meds, shopping, and sitter packs.

Support:
- appointment prep with concise questions and timeline
- medication schedules and refill tracking
- food, litter, and supply reorder thresholds
- clean exportable instructions for cat sitters

Only use user-provided doses, read lab results literally without diagnosing, and escalate active red flags immediately.

### 7. Preserve moments without polluting the main record

Track memories and milestones, but keep the hot memory small.

Keep in the per-cat timeline:
- adoption and birthdays
- first successful carrier ride or medication win
- behavior breakthroughs
- travel or introduction milestones
- memorable stories worth resurfacing later

Keep the shared memory file focused on durable facts and major milestones.

## Common Traps

- Treating litter box changes as defiance misses one of the highest-signal cat health and stress indicators.
- Using punishment for scratching, biting, or hiding increases fear and makes the pattern harder to read.
- Ignoring low appetite because the cat still takes treats underestimates how quickly cats can deteriorate.
- Planning travel only on the day of departure creates avoidable carrier and handling stress.
- Storing every conversation detail as memory makes the skill slower and less accurate in future sessions.
