---
name: imap
description: Read, search, and sync IMAP mailboxes with UID-safe fetches, precise filters, and attachment handling. Use when the user asks to inspect an inbox, retrieve messages, triage unread mail, handle attachments, or diagnose IMAP synchronization; route SMTP sending and non-IMAP APIs elsewhere.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📬"}'
  related-skills: '{"api":"API-integration boundary for authenticated mailbox wrappers.","http":"HTTP transport and header debugging outside IMAP.","json":"Structured mailbox-result transformation.","code":"Implementing or verifying a mailbox parser or sync worker.","bash":"Shell-first mailbox automation and repeatable wrappers."}'
---

## When to Use

Use this skill when the user needs to inspect or operate an IMAP mailbox across Gmail, Fastmail, ProtonMail Bridge, Exchange-compatible gateways, or self-hosted mail servers. It does not send mail; route message submission to an SMTP or provider-specific skill.

Activate it for inbox search, unread triage, header and body fetches, attachment handling, folder mapping, or incremental mailbox sync when correctness matters more than quick ad hoc scraping.

## State location

Store non-secret operational state under `<state_root>`. Resolve it in this order before reading or writing:

1. Use a path the user or runtime explicitly configured for this mailbox.
2. Otherwise reuse an existing `./.imap` in the current workspace.
3. Otherwise reuse `~/.config/agent-skills/imap` when it already exists.
4. If durable state is needed and no directory exists, ask before creating `./.imap`; keep one account label per file set.

Use `<state_root>` consistently for `memory.md`, `accounts.md`, `folder-map.md`, `sync-state.md`, and `playbooks.md`. Read `references/setup.md` on first use and `references/memory-template.md` only when creating or revising those files.

## Quick Reference

Load these references explicitly using file-reading tools when the condition is met. Do not guess their contents.

| Topic | File | When to load |
|-------|------|--------------|
| Setup and activation defaults | `references/setup.md` | When setting up a new IMAP connection or reviewing defaults |
| Memory and file templates | `references/memory-template.md` | When creating or modifying IMAP memory state files |
| Session planning and discovery | `references/session-strategy.md` | When starting a new mailbox inspection session |
| Search and fetch patterns | `references/search-and-fetch.md` | When formulating precise IMAP search queries or fetch commands |
| State, flags, and sync rules | `references/state-and-flags.md` | When handling unread state, UIDs, flags, or syncing |
| Attachment and MIME handling | `references/attachments.md` | When reading BODYSTRUCTURE or handling attachments |
| Failure diagnosis and quirks | `references/troubleshooting.md` | When commands fail or parsing provider quirks |
| Core Rules | `references/core-rules.md` | When making decisions about read-safe operations vs mutations |
| IMAP Traps | `references/imap-traps.md` | When troubleshooting strange sequence number or flag behavior |
| Domain knowledge | `references/domain.md` | When needing strict IMAP protocol definitions or RFC details |

## Core rules

1. **Discover capabilities before commands.** Identify namespace, delimiter, special-use folders, and advertised capabilities before selecting extensions or interpreting provider behavior.
2. **Keep inspection read-safe.** Use `EXAMINE`, UID search, and targeted `PEEK` or header fetches for a read request. Before a state change, preview the affected UIDs and obtain explicit approval unless a named standing policy covers that exact action.
3. **Persist UID state defensibly.** Store `UIDVALIDITY`, account, folder, and the checkpoint together. When `UIDVALIDITY` changes, invalidate the old cursor and rescan.
4. **Minimize fetched content.** Start with folders, flags, and headers; inspect MIME metadata before message bodies or attachments.

### 1. Discover mailbox capabilities before making assumptions
- Identify server capabilities, namespace layout, delimiter behavior, and special-use folders before building commands or interpreting results.
- Check whether the server supports features such as `UIDPLUS`, `CONDSTORE`, `QRESYNC`, `MOVE`, or `XLIST` replacements.
- Folder names, archives, and flag behavior vary by provider, so adapt dynamically to the provider semantics for every mailbox.

### 2. Default to read-safe operations unless the user clearly wants mutation
- Start with safe inspection patterns such as capability discovery, folder listing, `EXAMINE`, header fetches, and targeted body retrieval.
- Treat delete, move, copy, expunge, and bulk flag updates as mutating actions that require either explicit user approval or a previously confirmed standing policy.
- If the user only asked to inspect or summarize mail, preserve existing read/unread states and leave mailbox state unaltered.

### 3. Use UIDs and durable sync markers, not volatile sequence numbers
- Sequence numbers shift as mail arrives or is removed, so they are unsafe for persistent tracking.
- For repeatable workflows, store `UIDVALIDITY`, last processed UID, and when available `HIGHESTMODSEQ` or related sync checkpoints in `<state_root>/sync-state.md`.
- If `UIDVALIDITY` changes, treat prior cursors as invalid and rescan instead of trusting stale state.

### 4. Fetch the minimum data that answers the question
- Start with folder listing, counts, flags, and envelope or header data before downloading full bodies or attachments.
- Escalate to body sections, MIME structure, or attachments only when the user actually needs that detail.
- Smaller fetches reduce latency, bandwidth, and the chance of dragging sensitive content into unnecessary downstream processing.

### 5. Search with explicit server-side filters and report what they mean
- Prefer precise IMAP search constraints such as date ranges, sender, subject fragments, flags, size limits, or UID windows over broad mailbox scans.
- Be clear about whether the server search is header-only, text-oriented, charset-sensitive, or provider-specific in its matching behavior.
- When search semantics are ambiguous, explain the limitation and offer a narrower or confirmatory pass.

### 6. Treat MIME and attachments as structured data, not opaque blobs
- Read `BODYSTRUCTURE` or equivalent metadata before assuming where text lives or which parts are attachments.
- Distinguish inline parts from downloadable attachments, decode filenames safely, and preserve charset and transfer-encoding details.
- Fetch metadata and confirm necessity before downloading large attachments, and report part identifiers, sizes, and media types first when triaging.

### 7. Keep credentials out of skill memory and scope network use tightly
- Store only non-secret connection notes, capabilities, and workflow preferences under `<state_root>/`.
- Use existing local auth flows, app passwords, OAuth-backed bridges, or other secure runtime mechanisms the environment already supports.
- Restrict network activity to the user-configured IMAP endpoint needed for the mailbox task at hand.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| User-configured IMAP or IMAPS server | authentication material handled by the runtime, mailbox commands, requested headers, bodies, flags, and attachments | list folders, search messages, fetch content, and update mailbox state when approved |

No other data is sent externally.

## Security & Privacy

Data that stays local:
- Activation defaults, provider quirks, sync checkpoints, and reusable playbooks stored under `<state_root>/`
- Mailbox notes the user explicitly wants remembered for future sessions

Data that leaves your machine:
- Only the IMAP requests needed to talk to the configured mailbox server
- Message metadata, bodies, or attachments fetched from that mailbox when the current task requires them

This skill does NOT:
- store mailbox passwords or OAuth tokens in `<state_root>/`
- assume mutating mailbox access is allowed by default
- send mailbox content to undeclared third parties
- treat sequence numbers as durable sync state

## Trust

By using this skill, data is exchanged with the user-configured mail provider or IMAP bridge.
Only use it with mailbox systems and local credential flows the user already trusts.


## Related skills

Read the `metadata.related-skills` map when the mailbox request crosses into API integration, HTTP transport diagnosis, structured JSON transformation, code implementation, or shell automation.
