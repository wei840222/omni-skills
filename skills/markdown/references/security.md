## Security & Privacy

**Local storage:** preferences, observed targets, doc sets and generated artifacts stay in `<state_root>/` on this machine, plus name-only pointers in the shared `<workspace>/projects/` and `<workspace>/contacts/`. File paths, repo names, slugs and rule ids only — strip all tokens, keys, and passwords before storing, whatever the document the user pasted contained.

**Untrusted input:** Markdown from users, issues, scraped pages, or a model is untrusted HTML in disguise. Rendering it safely is sanitize-after-render, plus a URL-scheme allowlist; MDX from an untrusted source is arbitrary code and is never rendered at all (security rules).

- **MDX and CommonMark updates.** MDX v3 changed default behaviors (requiring ESM), and CommonMark periodically updates its spec. Always verify the current parser version before relying on edge-case syntax (e.g., nesting HTML inside Markdown).
