# Cloud Agents And Bugbot - Cursor

Use this file when the user is considering remote execution or GitHub-connected review workflows.

Current Cursor docs name the remote execution product **Cloud Agents** (also reachable from desktop, web, mobile, Slack, GitHub/Bitbucket comments, and API). Older "Background Agent" wording may still appear in conversation; treat it as the same remote class unless the user means a different surface.

## Cloud Agents

Treat Cloud Agents as remote execution in isolated cloud VMs, not as "Cursor but later."
Operationally they change several things at once:
- code can be cloned or fetched through connected source-control apps
- commands run outside the local machine in a dedicated environment
- network access, secrets, and remote compute become part of the trust boundary
- handoff is usually a branch / draft PR for human review

Use them only when:
- the task is long-running enough to justify remote execution
- source-control integration is acceptable
- the user agrees to the remote trust and review model

Admin-level source-control connection is required before teammates can start Cloud Agents from a repository. Access follows the triggering user's existing repo reach; starting an agent should not widen permissions.

## Bugbot

Treat Bugbot as a review surface, not as automatic truth.
It is useful when:
- the unit of work is a pull request
- the goal is finding bugs, security issues, or regressions before merge
- the user wants structured review comments instead of another implementation pass

Bugbot can run automatically on PR updates or manually via comments such as `cursor review` or `bugbot run`. Configure repository coverage through Cursor Automations after connecting source control.
Use repo guidance such as `.cursor/BUGBOT.md` only when it exists and is actually maintained.

## Review Discipline

- inspect Cloud Agent output before merging or applying follow-up changes locally
- inspect Bugbot findings before acting on them
- separate "helpful signal" from "approved change"
- if remote work touched the repo, compare the result against local expectations before continuing

## Red Flags

- enabling Cloud Agents just to avoid local setup work
- treating GitHub app access as a harmless toggle
- letting review comments trigger more remote work without clarifying ownership
- assuming privacy-sensitive repos are safe just because the feature is official
