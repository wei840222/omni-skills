# Setup — University

## First write consent

Before creating `<state_root>/` children:

1. Restate what will be stored (program name, hours/week, deadlines, preference defaults).
2. Ask once for durable-write consent unless the host already granted skill state writes.
3. On yes, create only the files needed for the current mode (usually `config.md` plus one `degrees/[name]/` tree).
4. On no, keep guidance ephemeral for this turn and offer to continue without persistence.

## Bootstrap sequence

1. Resolve `<state_root>` per `SKILL.md`.
2. If `config.md` is missing, create it from the preference schema in `feedback.md` after consent.
3. Ask the minimum diagnostic set:
   - What program, credential, or course set?
   - Current level / prior coursework?
   - Hours available per week and non-study constraints?
   - Hard deadlines (term end, exam date, application date)?
4. Choose mode (`degrees.md`) and generate the first curriculum + calendar draft.
5. Confirm the draft before expanding full module trees.

## Migration from legacy paths

If the user mentions older Clawic university data:

1. Treat `~/Clawic/data/university/` as read-only source.
2. Propose copy → validate → cutover → rollback.
3. Perform migration only after explicit approval.
4. Leave the legacy tree untouched until cutover succeeds.

## Safety

- Do not invent grades, credits, or institutional policies.
- Do not submit coursework, registrations, or payments.
- Academic integrity: practice exams are for preparation; live graded work remains the learner's responsibility.
