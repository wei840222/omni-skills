# Filing

Archive layout and retention live under `<state_root>`.

## Naming and layout
- Keep original bytes; rename only
- Typical layout: `<state_root>/archive/<YYYY>/<MM>/`
- Ledger index: `<state_root>/ledger/<YYYY>.md`
- Integrity: store hash/size when available; never rewrite the document to "clean" it

## Retention
- Use configured `retention_years`, otherwise follow `tax-rules.md` guidance
- Do not delete within the retention window; mark superseded rows instead of overwriting evidence
