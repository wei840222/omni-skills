---
name: mail
description: >
  Read, search, draft, and send email with himalaya or Apple Mail SQLite using
  draft-review-send safety. Use when the user asks to inspect an inbox, triage
  recent mail, compose a reply, or send after explicit review on macOS or Linux.
  Prefer `imap` for protocol-level UID sync, `smtp` for submission/debug only,
  `apple-mail-macos` for Mail.app automation without himalaya, `fastmail-api` /
  `google-workspace-cli` for provider-native APIs, and `email-management` for
  inbox triage strategy rather than transport mechanics.
metadata:
  version: "1.2.0"
  openclaw: '{"emoji":"📧","requires":{"bins":["himalaya"],"anyBins":["osascript","sqlite3"]},"os":["darwin","linux"],"displayName":"Mail","configPaths":["<state_root>/"]}'
  related-skills: '{"imap":"Protocol-level IMAP UID search/sync when himalaya wrappers are not enough.","smtp":"Outbound SMTP dry-run and deliverability debugging without inbox triage.","apple-mail-macos":"Mail.app / osascript / Shortcuts automation when himalaya is unavailable.","email-management":"Inbox triage, reply drafting, and follow-up tracking strategy.","fastmail-api":"Fastmail JMAP native API instead of generic IMAP/SMTP.","google-workspace-cli":"Gmail via Google Workspace CLI / APIs instead of himalaya."}'
---

# Mail

Operate email with **himalaya** (cross-platform IMAP/SMTP and related backends)
or **Apple Mail SQLite** (macOS indexed reads). Keep credentials read-only, and
require explicit confirmation before send, delete, or bulk mutation.

## State location

Operational notes may live under `<workspace>/mail/`,
`<workspace>/memory/mail/`, or `~/mail/`. Before reading or writing state,
resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/mail/`, `<workspace>/memory/mail/`, `~/mail/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to
   `<workspace>/mail/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill.
himalaya's own config still resolves through XDG /
`<state_root>/.config/himalaya/config.toml` when documented below; never write
secrets into the skill package.

## When to use

Load this skill when the user needs practical inbox operations:

- list / search / read recent messages
- draft a reply and wait for review before send
- choose between Apple Mail SQLite (macOS, read-heavy) and himalaya (send + IMAP)

Prefer adjacent skills when the ask is narrower:

- `imap` — raw IMAP UID correctness and sync semantics
- `smtp` — submission/auth/deliverability debugging
- `apple-mail-macos` — Mail.app automation without himalaya
- `fastmail-api` / `google-workspace-cli` — provider-native APIs
- `email-management` — triage policy and follow-up tracking

## Architecture

```text
<state_root>/
├── memory.md           # accounts in scope, preferred client path, safety defaults
├── accounts.md         # non-secret account labels and mailbox aliases
├── send-log.md         # reviewed drafts, send decisions, message ids
└── incidents.md        # auth failures, stale-index misses, SMTP rejects
```

himalaya config (host-owned, not skill package content):

- `$XDG_CONFIG_HOME/himalaya/config.toml`
- `$HOME/.config/himalaya/config.toml`
- `$HOME/.himalayarc`

Apple Mail indexed reads (macOS only, read-only):

- `<state_root>/Library/Mail/V*/MailData/Envelope Index` when the host maps home under `<state_root>`
- otherwise the live host path `$HOME/Library/Mail/V*/MailData/Envelope Index`

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Core rules, scope, traps | `references/domain.md` | Every non-trivial mail task |
| himalaya CLI patterns | `references/himalaya.md` | Cross-platform list/read/send |
| Apple Mail SQLite | `references/apple-mail.md` | macOS indexed read/search |
| Send / reply protocol | `references/sending.md` | Before compose or send |
| Official sources | `references/sources.md` | Version, auth, or flag claims |

## Operating path

1. Detect platform and commit to **one** client for the task (Apple Mail SQLite **or** himalaya). Do not mix in the same mutation.
2. Resolve `<state_root>` before writing notes; ask before creating new durable files.
3. For reads: prefer JSON/`--json` machine output from himalaya, or force Apple Mail sync before SQLite queries.
4. For sends: follow draft → show full content → wait for explicit OK → `himalaya message send`.
5. Record send/delete decisions in `<state_root>/send-log.md` when the user wants a durable trail.

## Core rules (summary)

1. **Credentials stay read-only.** Never rewrite keychain entries or config passwords unless the user explicitly asks to rotate them outside this skill.
2. **Draft-review-send.** Show To/Subject/Body (and attachments) and wait for an explicit send confirmation.
3. **Confirm deletes and bulk moves.** Preview affected ids/folders first.
4. **Thread by headers.** Prefer `In-Reply-To` / `References`; do not trust `Re:` alone.
5. **Refresh caches.** Force Apple Mail sync before SQLite; run `himalaya mailbox list` after server-side folder changes.

Read `references/domain.md` for the full rule set and traps.
