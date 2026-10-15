# Domain Rules and Scope

## Requirements

**Binaries:**

- `himalaya` — cross-platform mail CLI (IMAP/SMTP and other backends). Install via the [official installer](https://github.com/pimalaya/himalaya), `brew install himalaya`, or `cargo install himalaya`.
- `osascript` / `sqlite3` — macOS Apple Mail indexed reads (built-in).

**Credentials (host-owned):**

- Prefer App Passwords or OAuth helpers; never store raw passwords in the skill package.
- himalaya config resolves from `$XDG_CONFIG_HOME/himalaya/config.toml`, `$HOME/.config/himalaya/config.toml`, or `$HOME/.himalayarc` (override with `-c`).
- Documented skill paths use `<state_root>/.config/himalaya/config.toml` only when the host maps config under the resolved state root.

## Platform detection

| Situation | Prefer |
|-----------|--------|
| macOS + Mail.app already syncing + read/search only | Apple Mail SQLite (`references/apple-mail.md`) |
| Need send / IMAP across Linux or macOS | himalaya (`references/himalaya.md`) |
| Provider-native API (Fastmail JMAP, Google Workspace) | Route to `fastmail-api` / `google-workspace-cli` |

Commit to **one** approach per task. Mixing Apple Mail SQLite mutations with himalaya IMAP in the same send/delete flow creates conflicting unread and folder state.

## Core rules

### 1. Read-safe by default

- List and search before fetching full bodies.
- Prefer himalaya `envelope list` / `envelope search` with `--json` for machine parsing.
- On Apple Mail, force a sync before querying the Envelope Index.

### 2. Draft-review-send

1. Compose the full message (headers + body + attachment plan).
2. Show the user the complete content.
3. Wait for an explicit “send” / “OK”.
4. Only then pipe RFC 2822 / composed input into `himalaya message send`.

### 3. Credential hygiene

- Treat keychain / `password.command` / token helpers as read-only unless the user explicitly asks to rotate credentials outside this skill.
- Gmail rejects the normal account password over SASL PLAIN; use an [App Password](https://support.google.com/accounts/answer/185833) (2-Step Verification required) or OAuth via a helper such as ortie.
- Never print secrets into chat logs, `send-log.md`, or PR artifacts.

### 4. Threading

- Include `In-Reply-To` and `References` when replying.
- Do not rely on a `Re:` subject prefix alone.

### 5. Folder and mailbox names

- himalaya accepts mailbox id, name, alias, or role (`inbox`, `sent`, `drafts`, `trash`, …).
- Gmail special folders live under `[Gmail]/…` — quote them or use aliases from config.
- After server-side folder renames, refresh with `himalaya mailbox list`.

### 6. Mutations need confirmation

- Delete, bulk move, expunge, and mass flag updates require an explicit preview of affected ids.
- Record important send/delete outcomes in `<state_root>/send-log.md` when the user wants a trail.

## Scope

This skill:

- ✅ Reads mail via himalaya or Apple Mail SQLite
- ✅ Searches and filters messages
- ✅ Sends via himalaya after draft-review-send
- ✅ Keeps credentials and host config read-only by default
- ❌ Does not rewrite secrets without an explicit out-of-band request
- ❌ Does not auto-send
- ❌ Does not delete without confirmation
- ❌ Does not replace provider-native APIs (`fastmail-api`, `google-workspace-cli`) or protocol-deep `imap` / `smtp` skills

## Common traps

- **Stale Apple Mail index** — SQLite lags until Mail.app syncs.
- **Wrong JSON flag era** — current himalaya documents `--json`; older docs/examples used `--output json` / `-o json`. Prefer `--json` and verify with `himalaya <cmd> --help` on the installed binary.
- **`message list` confusion** — listing goes through `envelope list` / `envelope search`, not a generic `message list`.
- **From / auth mismatch** — some SMTP servers reject when `From` ≠ authenticated identity.
- **Silent-looking success** — verify Sent / save-copy behavior after important sends; use verbose flags when diagnosing rejects.
- **Mixing clients** — do not toggle Apple Mail SQLite and himalaya mid-mutation.
