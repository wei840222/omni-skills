# Import, Export, and Migration

Undo rarely exists. Every bulk operation starts with a dated export under `<state_root>/crm/exports/<YYYY-MM-DD>/`.

## Import checklist

1. **Export first** — contacts, companies, deals, and activity with ids intact.
2. **Map fields** before the first write; reject columns with no destination.
3. **Identity key** — dedupe on lowercased email (people) / domain (orgs) / deal id.
4. **Dry run** on a 20–50 row sample; inspect collisions and blank-required fields.
5. **Scope** — import only what will be contacted this quarter; archive the rest outside the CRM.
6. **Commit** inside a transaction when the store supports it; otherwise write a rollback copy first.
7. **Log** the import as an artifact: source file, mapping, counts created/updated/skipped.

## Export checklist

- Include people, organizations, deals, and interaction history.
- Preserve stable ids and foreign keys.
- Prefer CSV/JSON the next tool can re-import without paying for an unlock.

## Migration between CRMs

1. Export everything from the old system, including activity history.
2. Map ids object-by-object; do not rely on a contacts-only CSV.
3. Load into the new system, then keep the old system **read-only for one full review cycle**.
4. Compare open-deal counts, next-step coverage, and a sample of interaction timelines before cutting writes over.
5. Only then mark the old system retired in `## System`.
