# Email Send Protocol

## Draft-review-send workflow

Require explicit review before sending. Always follow this flow:

1. **Compose** — generate full email content (To, Cc/Bcc, Subject, Body, attachment plan).
2. **Review** — show the user the complete message.
3. **Confirm** — wait for an explicit `send` / `OK` (or an equivalent clear approval).
4. **Send** — execute `himalaya message send` (or a reviewed `message compose …` pipeline).
5. **Verify** — check Sent / save-copy behavior for important mail.

Never auto-send from a draft the user has not approved.

## Reply threading

Include these headers or the thread breaks across clients:

```text
In-Reply-To: <original-message-id@domain.com>
References: <original-message-id@domain.com>
```

**Trap:** a `Re:` subject prefix is unreliable. Some clients add it; others omit it.

## RFC 2822 / stdin shape

When piping a raw message into `himalaya message send`, use a complete header block and blank line before the body:

```text
From: sender@example.com
To: recipient@example.com
Subject: Your Subject
In-Reply-To: <message-id>
Content-Type: text/plain; charset=utf-8

Email body here.
```

For richer MIME, signing, or editor-driven flows, chain a composer such as [mml](https://github.com/pimalaya/mml) into `himalaya message send` rather than hand-building multipart by hand in chat.

Simple flag-based compose (still requires review before `--send`):

```bash
himalaya message compose --to you@example.org --subject Hello --body Hi
# only after explicit OK:
himalaya message compose --to you@example.org --subject Hello --body Hi --send
```

## SMTP / provider rejection cases

- **From mismatch** — some servers reject when `From` ≠ authenticated user.
- **Missing headers** — include Date / Message-ID when constructing raw messages; composers usually add them.
- **Gmail auth** — App Password or OAuth; normal account password fails SASL PLAIN.
- **Rate / policy limits** — treat provider daily caps as mutable; verify against current Google Workspace / consumer docs before stating numbers.
- **Save-copy** — himalaya v2.2.1 supports `message.send.save-copy` and `--no-save`; Gmail/Graph often file Sent themselves.

## Attachments

Prefer composer / MIME tooling over ad-hoc multipart in the agent transcript. If attaching files, show the attachment list during review and confirm paths before send.

## Trap: looking successful while delivery failed

- Confirm exit status **and** provider response / Sent folder presence for critical mail.
- Diagnose with verbose flags (`himalaya -v …` when available on the installed build).
- Log the decision and message id in `<state_root>/send-log.md` when the user wants a durable trail — never log secrets.
