# himalaya CLI Patterns

Verified against Himalaya **v2.2.1** docs and README (2026-10-02 release). Re-check `himalaya --help` on the installed binary before asserting flags.

## Installation

```bash
# Official installer (see README)
curl -sSL https://raw.githubusercontent.com/pimalaya/himalaya/master/install.sh | PREFIX=~/.local sh

# Or
brew install himalaya
cargo install himalaya
```

## Configuration paths

Loaded from the first valid path among:

1. `$XDG_CONFIG_HOME/himalaya/config.toml`
2. `$HOME/.config/himalaya/config.toml`
3. `$HOME/.himalayarc`

Override with `-c <PATH>` (multiple paths may be `:`-merged). Documented skill examples may show `<state_root>/.config/himalaya/config.toml` when the host maps config under the resolved state root.

Bare `himalaya` launches the wizard (discover account → write TOML). Inspect with `himalaya account list` / `himalaya account check`.

## Gmail example (App Password)

Gmail rejects the normal account password over SASL PLAIN. Use an App Password or OAuth.

```toml
[accounts.gmail]

imap.server = "imaps://imap.gmail.com:993"
imap.sasl.plain.username = "user@gmail.com"
imap.sasl.plain.password.command = "security find-internet-password -s imap.gmail.com -a user@gmail.com -w"

smtp.server = "smtps://smtp.gmail.com:465"
smtp.sasl.plain.username = "user@gmail.com"
smtp.sasl.plain.password.command = "security find-internet-password -s smtp.gmail.com -a user@gmail.com -w"

mailbox.alias.inbox = "INBOX"
mailbox.alias.sent = "[Gmail]/Sent Mail"
mailbox.alias.drafts = "[Gmail]/Drafts"
mailbox.alias.trash = "[Gmail]/Trash"
mailbox.alias.archive = "[Gmail]/All Mail"
```

Linux hosts typically use `pass show …` or another `password.command` helper instead of macOS `security`.

## Essential commands

| Command | Purpose |
|---------|---------|
| `himalaya mailbox list` | List mailboxes / folders |
| `himalaya envelope list --json` | List envelopes (machine-readable) |
| `himalaya envelope list --page 2` | Paginate listing |
| `himalaya envelope search from alice and after 2026-01-01 order by date desc` | Cross-backend search DSL |
| `himalaya message read <id>` | Read message body / structured view |
| `himalaya message send` | Send from stdin / composer pipeline |
| `himalaya message compose --to … --subject … --body …` | Simple compose (add `--send` only after review) |
| `himalaya attachment download <id>` | Download attachments |
| `himalaya flag add --flag seen <ids…>` | Mutate flags (confirm first) |

`-m/--mailbox` accepts id, name, alias, or role (`inbox`, `sent`, `drafts`, `trash`, …) and defaults to inbox.

## JSON output

Prefer **`--json`** for programmatic parsing on current himalaya builds. Older tutorials used `--output json` / `-o json`; treat those as legacy and confirm with local `--help`.

## Traps

- Listing is `envelope list` / `envelope search`, not `message list`.
- Quote Gmail `[Gmail]/…` mailboxes or use aliases.
- After server-side folder changes, refresh with `himalaya mailbox list`.
- `message send` reads composed content from stdin / composer pipeline — do not stuff the whole RFC 2822 body into an argv string.
- OAuth / XOAUTH2 flows use external token helpers (for example ortie); keep tokens out of chat and skill state files.
- Important sends: verify Sent / `message.send.save-copy` behavior afterward.
