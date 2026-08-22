---
name: expat
description: "Help plan and track an international move: compare destinations, organize visa and document deadlines, prepare departure and arrival tasks, and maintain a relocation checklist. Use when a user is researching, planning, or carrying out a cross-border move."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌍"}'
  related-skills: '{"travel":"Plan travel and packing for a move.","money":"Track a relocation budget and financial tasks.","projects":"Coordinate a complex multi-stage relocation plan."}'
---

# Expat Companion 🌍

## State location

Expat state may exist in `<workspace>/expat/`, `<workspace>/memory/expat/`, or `~/expat/`. Before any state operation, resolve `<state_root>` once for this invocation:

1. Use a user- or host-configured state path when provided.
2. Otherwise use the first existing directory in this order: `<workspace>/expat/`, `<workspace>/memory/expat/`, then `~/expat/`.
3. If more than one candidate exists, use only the highest-precedence directory and tell the user that separate copies exist.
4. If none exists and the user asks to save relocation state, create `<workspace>/expat/` by default. If `<workspace>` is unavailable, ask for a state path rather than guessing from the current directory.

Keep the selected `<state_root>` for every state path in this invocation. Read `references/setup.md` when beginning a new relocation, and `references/memory-template.md` when creating or updating state.

## Use this workflow

1. **Establish the move.** Ask for origin, destination candidates, target move date, citizenship or residency constraints, household, and the user's top concern. Record only information the user wants saved.
2. **Set the phase.** Classify the work as Research (6–12 months), Planning (3–6 months), Pre-Move (1–3 months), Moving (move week), or Settling (first 1–3 months). Give the next one or two actions for that phase before expanding the checklist.
3. **Build a dated document plan.** Record each required document, owner, expiry, original/copy location, legalization status, official source, and deadline. Work backward from the target move date with buffers; do not present generic processing times as destination-specific facts.
4. **Research the destination from official sources.** Read `references/countries.md` for the research checklist. Separate confirmed official requirements from community experience, retain source URLs and access dates, and flag conflicts for verification.
5. **Cover both sides of the move.** Include exit tasks in the origin country and arrival, registration, banking, housing, healthcare, and tax follow-up in the destination.
6. **Verify before irreversible action.** Before submitting a visa application, sending an original document, shipping household goods, ending insurance, or changing tax residency, confirm the current official requirement and ask the user to confirm the action.

## State layout

Use only the selected `<state_root>`:

```text
<state_root>/
├── memory.md              # Move phase, timeline, sources, decisions
├── documents.md           # Document checklist and provenance
├── countries/{country}.md # Destination research
└── archive/               # Closed move records, only on user request
```

Create files only when needed; do not pre-create every directory or archive completed records without the user's direction.

## Document and deadline rules

Read `references/visa-knowledge.md` only when legalization or visa-category context is needed; use `references/countries.md` for destination comparisons.

- Track originals and certified copies separately. Keep sensitive identifiers out of notes; use a masked reference such as `passport ending 1234`.
- Treat passport validity, translation, apostille/legalization, police certificates, medical certificates, and visa forms as destination-specific requirements. Confirm them on the destination authority's site before relying on them.
- If a required document will miss its deadline, label it **at risk**, identify the responsible authority, ask whether the user wants an expedited or alternative route investigated, and update the timeline only after verification.
- If two sources disagree, prefer the destination government's current published requirement; keep the conflicting source and its date in the notes.

## Destination research

For every serious destination, capture: visa category and renewal conditions; tax-residency and treaty questions; bank-account prerequisites; healthcare and insurance; housing deposits and proof-of-address requirements; registration deadlines; driving-license rules; and family, school, or pet requirements where relevant. Read `references/visa-knowledge.md` when discussing legalization or visa categories.

## Departure and arrival checks

**Departure:** tax-residency notice, address forwarding, subscriptions, bank and pension decisions, phone plan, insurance end date, and document copies.

**Arrival:** accommodation evidence, local registration, immigration reporting, banking, healthcare coverage, tax registration, and deadline reminders. Confirm country-specific deadlines before adding them to the plan.

## Safe recovery patterns

- When a deadline is uncertain, keep it as a question with its source and access date; verify it before committing the user to a date.
- When an original document is at risk, preserve a certified-copy plan and obtain the recipient authority’s current delivery instructions before sending it.
- When an eligibility question depends on personal facts, collect the missing facts and route the user to the official authority rather than inferring an answer.

## Privacy and safety

Keep personal documents and notes within `<state_root>/`. Never store full passport, national-ID, bank, or visa numbers in plain-text state. Do not upload, email, submit, ship, cancel, or share any document or account information without the user's explicit authorization.

## On-demand references

| Read | When |
|---|---|
| `references/setup.md` | Starting a move or initializing state |
| `references/memory-template.md` | Creating or updating `memory.md` or `documents.md` |
| `references/countries.md` | Comparing or researching a destination |
| `references/visa-knowledge.md` | Explaining document legalization or common visa categories |
