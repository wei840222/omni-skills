# Setup — Baidu

Use this reference after the immediate request is answered and the user has approved saving reusable Baidu context.

## Prepare state

1. Resolve `<state_root>` with the resolver in `SKILL.md`; inspect every candidate before creating a default path.
2. Create only the selected `<state_root>` and the files required for the current request.
3. Initialize templates from `references/memory-template.md` when `<state_root>/memory.md` is absent or empty.
4. Apply owner-only permissions appropriate to the host platform without assuming a particular shell, operating system, or filesystem.

## Capture only durable defaults

Capture the smallest stable set of details that changes future advice:

- activation and silence preferences
- Baidu product surfaces in scope
- target region and preferred documentation language
- trusted-source and weak-source patterns
- durable decisions, blockers, and approval boundaries

Confirm before recording account labels, internal team names, or ongoing project notes. Keep inferred context separate from confirmed facts, and retain only safe planning data.
