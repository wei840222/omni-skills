# Traps and Workarounds

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Building JSON with string concatenation or templates | One quote, newline, or backslash in a value produces a document that no longer parses — and an injection point | Build a native structure and serialize it once |
| `try { JSON.parse(x) } catch { return {} }` | Turns a malformed upstream payload into a silent empty result that surfaces three layers away as a missing field | Fail loudly with the byte offset and the first 200 characters |
| `additionalProperties: false` inside an `allOf` branch | A subschema cannot see the sibling's properties, so a valid document fails | `unevaluatedProperties: false` at the composition root, draft 2019-09+ |
| Trusting `format: "date-time"` to reject a bad date | `format` is an annotation by default; most validators only assert it with a plugin enabled | Turn assertion on explicitly, or add a `pattern` |
| Verifying a webhook signature after the JSON middleware | The framework parsed and discarded the raw body; your re-serialization is not what was signed | Capture raw bytes in the body reader, verify, then parse |
| `if (obj.field)` for an optional boolean or number | `false` and `0` are falsy, so a present value reads as absent | `'field' in obj` / `!= null`, and decide the three states first |
| Recursive merge of user-supplied JSON | `__proto__`, `constructor`, `prototype` keys reach the object prototype and poison every object in the process | Null-prototype targets and a key blocklist at the merge, not at the parse |
| Sorting keys to make a diff readable, then hashing it | Sorted output is not the canonical form any spec defines, and the sort is shallow | RFC 8785 for hashing; sort only for human diffs |
| Epoch seconds for a future appointment | An instant is not a wall-clock time; a DST change moves the meeting | RFC 3339 local time plus an IANA zone field, or state that instants are what you mean |
| Storing a whole document in a column "to decide later" | It becomes a schema nobody wrote and everybody depends on; queries end up scanning | Promote queried fields to real columns or generated columns with indexes |
| Streaming an array by splitting on `,` or `}` | Commas and braces appear inside strings; the split corrupts records at random | A real incremental parser, or NDJSON where the delimiter is a newline outside strings |
| Snapshot tests over unsorted, unredacted output | Every unrelated change produces a diff, so the snapshot gets regenerated unread | Canonicalize and redact before writing the golden file |
| A payload decision that lives only in the chat | Re-litigated by the next person who finds the field confusing | `<state_root>/` with the date and what was rejected |
