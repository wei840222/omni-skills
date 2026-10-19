# CISO setup

Use this file on first activation or when the user asks to persist CISO context.

1. Confirm whether durable notes are wanted under `<state_root>/ciso/`.
2. If yes, resolve `<state_root>` using the State location rules in `SKILL.md`.
3. Create only the files the user approves (`memory.md`, `risk-register.md`,
   `vendor-reviews.md`, `incidents.md`).
4. Never store passwords, API keys, session cookies, or raw PHI/PII dumps in
   those files — store vault references and ticket IDs instead.
5. Re-read `references/sources.md` before quoting statutory notification clocks.

For code-level remediations, load `security-best-practices` instead of expanding
this program-level skill.
