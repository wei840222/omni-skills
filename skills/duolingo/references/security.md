# Security and Privacy

## Affirmative posture

- Keep curriculum, attempts, review queues, and streak notes inside the resolved `<state_root>/`.
- Resolve `<state_root>` once per invocation and reuse that concrete path for every read/write.
- When the user asks for an export, share only the named files they approve.
- Treat AGENTS router snippets as user-owned text: show the snippet, wait for the user to paste it.
- Leave `skills/duolingo/` package files unchanged during normal learning sessions.

## Recovery paths

- If a path outside `<state_root>/` is needed, stop and ask which path to open.
- If duplicate candidate state roots exist, use the highest-precedence one, report the others, and leave them untouched.
- If credentials or third-party account tokens appear in chat, refuse to store them under `<state_root>/` and point the user to their secret store.
