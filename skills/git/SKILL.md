---
name: git
description: >
  Commits, branches, merges, and rebases Git repositories, resolves conflicts,
  and recovers lost history. Use when the work touches a repo, commit, branch, merge,
  rebase, stash, tag, or submodule; when Git refuses a command — index.lock exists,
  push rejected as non-fast-forward, detached HEAD, dubious ownership, unrelated histories,
  conflict markers left behind; when something looks lost after a hard reset, a bad
  rebase, a deleted branch, or a dropped stash; when splitting a mixed change, wording
  commit messages, cleaning history before review, or force-pushing without wrecking
  a teammate's work; when a credential or a huge file got committed; when setting
  up worktrees, hooks, LFS, sparse checkout, signing, or separate work and personal
  identities. Not for CI pipeline YAML (github-actions, gitlab) or for composing the
  pull request description itself (pull-request).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📚","requires":{"bins":["git"]}}'
  related-skills: '{"pull-request":"when the branch is ready and the PR itself has to be written and validated","review-code":"when the job is judging another contributors diff, not producing it","github-actions":"when the failure is in workflow YAML rather than in the repository","gitlab":"GitLab CI/CD pipelines and merge-request settings","code":"planning, implementing, and verifying the change the commits will carry"}'
---

# Git

Operate on repositories with blast-radius discipline: rewrite only unpublished history, force-push with lease on own branches, and recover with `reflog` before panic.

## State location

Git preferences and memory may exist in `<workspace>/git/`, `<workspace>/memory/git/`, or `~/git/`.
`<workspace>` is the host/runtime workspace root (from host config), not the shell cwd alone.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/git/`, `<workspace>/memory/git/`, `~/git/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and durable notes must be saved, propose `<workspace>/git/` (or an explicit path if no workspace is available) and obtain named consent before creating it.
5. Legacy paths `~/Clawic/data/git/`, `~/clawic/git/`, and bare copies outside the selected root are migration sources only. Copy into the selected layout only after the user names the destination; leave legacy trees untouched unless the user asks to remove them.

Use the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Skill package files stay under `references/` and `assets/`; never write learned data into `SKILL.md`.

### State tree (after resolution)

```text
<state_root>/
├── config.yaml   # declared preferences (optional until first save)
└── memory.md     # observed conventions, boundaries, corrections
```

On first use, read `references/setup.md`. Create files from `assets/memory-template.md` only after consent.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml` after State location is resolved.

| Variable | Type | Default | Effect |
|---|---|---|---|
| integration_style | rebase \| merge \| squash \| repo-default | repo-default | How branches get combined and what `pull` does; `repo-default` reads the last 20 merges (`git log --merges --oneline -20`) and follows what the repo already does |
| commit_style | conventional \| plain \| repo-default | repo-default | Shape of every generated commit subject (Commit Discipline); `repo-default` copies the style found in `git log --oneline -20` |
| branch_naming | text (pattern) | type/topic | Template used when creating branches, lowercase and hierarchical by default |
| protected_branches | list | main, master | Branches strictly restricted from being committed to, rewritten, or force-pushed (Core Rule 2, Push gate); a request that targets one becomes "branch first, then propose the merge" |
| force_push_policy | never \| own-branches \| any | own-branches | Governs the Push gate: `never` turns every rewrite into a `git revert`; `any` still requires `--force-with-lease` |
| subject_max | number (chars, 50-100) | 72 | Hard stop for every generated commit subject (Core Rule 6) and the length any `commit-msg` gate enforces |
| message_language | text (language) \| repo-default | repo-default | Language of generated commit subjects, bodies, and tag messages; `repo-default` copies the language already in `git log --oneline -20` |
| remote_host | github \| gitlab \| bitbucket \| gitea \| other | github | Selects PR-vs-MR wording, blob size limits, and squash-merge semantics quoted in review and release guidance |
| signing | off \| ssh \| gpg | off | Adds signing flags and `commit.gpgsign` setup to commit and tag flows |

Preference areas to record as the user reveals them:

- **tooling** — CLI vs GUI vs IDE Git, hosting CLI in use, pre-commit framework, mergetool of choice
- **conventions** — subject format, ticket-ID placement, tag scheme, trailers such as `Co-authored-by`, monorepo tag prefixes
- **thresholds** — body-length and file-count limits a commit may reach, the large-file guard's size (`--above=`), reflog retention (`gc.reflogExpireUnreachable`), clone depth and filter in CI
- **restrictions** — repos, paths, or file types the agent must leave alone; operations banned outright (no rebase, no `filter-repo`); compliance regimes demanding signed or reviewed commits
- **platform** — hosting provider, SSH vs HTTPS, monorepo vs polyrepo, Windows/macOS line-ending and case sensitivity constraints
- **safety posture** — whether the agent may commit or push unprompted, confirmation before `--hard`/`clean -f`/history rewrites
- **work order** — commit granularity, whether to sync before starting, review gates expected before a push
- **cadence** — how often to fetch/prune, when to run maintenance on large clones

## When To Use

- Any task touching a Git repository: staging, commits, branches, merges, rebases, tags, stashes, submodules.
- Something looks lost — deleted branch, bad rebase, hard reset, vanished stash: recovery is a first-class use (→ Recovery Playbook, `references/recovery.md`).
- Git refuses to run and the message is opaque (`index.lock`, non-fast-forward, dubious ownership, detached HEAD) → `references/errors.md`.
- Before any history rewrite or force push: run the Output Gates below first.
- Investigating when a behavior broke, who changed a line, or where code came from → `references/forensics.md`.
- Not for CI pipeline configuration — GitHub workflows are `github-actions`, GitLab pipelines are `gitlab`; writing the PR description itself is `pull-request`.

## Quick Reference

| Situation | File |
|-----------|------|
| Staging surgery, splitting a mixed change, wording a message, stashing | `references/commits.md` |
| Creating or switching branches, merge vs rebase, stacked branches | `references/branching.md` |
| A merge or rebase stopped on conflicts | `references/conflicts.md` |
| Undoing: reset, revert, amend, rewriting a branch before review | `references/history.md` |
| Work looks lost: bad reset, dropped stash, deleted branch, detached commits | `references/recovery.md` |
| Git printed an error and refuses to proceed | `references/errors.md` |
| "When did this break", "who wrote this line", "where did this code go" | `references/forensics.md` |
| Push/pull friction, review flow, force-pushing on a shared branch | `references/collaboration.md` |
| Forks, upstreams, mirrors, moving or splitting a repository | `references/remotes.md` |
| Two checkouts at once: hotfix mid-refactor, parallel agent tasks | `references/worktrees.md` |
| Nested repositories: submodules, subtrees, vendored code | `references/submodules.md` |
| Slow clone or status, monorepo scale, huge files, LFS | `references/large-repos.md` |
| Pre-commit/pre-push automation, lint gates, a hook that never runs | `references/hooks.md` |
| A credential or a giant blob reached the history | `references/secrets.md` |
| Wrong author identity, auth failures, ignore rules, CRLF churn | `references/config.md` |
| Tags, version bumps, backports, release branches, changelogs | `references/releases.md` |
| A flag or one-time config that removes a whole trap class | `references/commands.md` |
| Git driven from a script, a CI job, or a non-interactive agent | `references/scripting.md` |
| User states a workflow preference | `references/setup.md` + `assets/memory-template.md` |
| Anything else | Stay here — Core Rules, Revision Syntax, and the Recovery Playbook cover the default path |

## Core Rules

1. **Rewrite only unpushed history.** Check: `git log @{u}..` lists exactly the commits safe to amend/rebase/squash. A commit missing from that output is published — fix forward with `git revert` instead.
2. **Force push = `--force-with-lease`, own branch only, never a branch in `protected_branches`.** The lease is void if anything fetched after the remote moved — IDE auto-fetch does this without warning — so add `--force-if-includes` (git >=2.30) to close that hole.
3. **Destructive command → name the casualties first.** `git status` before `reset --hard`, `git clean -n` before `git clean -f`, `git diff @{u}` before force push. If you cannot list what dies, you are not ready to run it. Cheap insurance when you are unsure: `git branch backup/$(date +%F-%H%M)` costs one ref and zero bytes.
4. **`git reflog` before panic.** Committed work survives 90 days (reachable) / 30 days (unreachable) — those are reflog-entry lifetimes, and a commit some reflog entry still names does not count as unreachable, so `gc`'s shorter two-week prune window never applies to it (→ `references/recovery.md`). The only truly unrecoverable losses: unstaged edits killed by `reset --hard`/`restore`, and untracked files killed by `clean -f`.
5. **Conflicts repeat per commit in rebase, once in merge.** Same region conflicting across 3+ replayed commits → abort and merge instead (one resolution), or enable `rerere` so each resolution is recorded once.
6. **Commit = one reviewable change.** Mixed changes → `git add -p` to split. Subject: aim ≤50 chars (convention), strict limit `subject_max`, default 72 because `git log` indents bodies by four spaces inside an 80-column terminal — hosts truncate around the same width in list views. Body explains why, not what; subject and body both follow `message_language`.
7. **A pushed secret is a leaked secret.** Rotate the credential first; history rewrite (filter-repo) is cleanup, not containment — forks, clones, and CI caches keep the old objects.
8. **Escalate undo by blast radius; stop at the first tool that reaches the goal.** `git restore` (one file, nothing else moves) → `git revert` (one commit, safe on shared branches) → `git reset` (moves your branch pointer only) → `git rebase` (new SHAs, everyone tracking the branch pays) → `git filter-repo` (every clone in existence is now wrong). Reaching for the right-hand tools when a left-hand one suffices is the single most common self-inflicted Git incident.

## Revision Syntax

See `references/revision-syntax.md`.

## Recovery Playbook

See `references/recovery-playbook.md`.

## Commit Discipline

See `references/commit-discipline.md`.

## Conflict Basics

See `references/conflict-basics.md`.

## Output Gates

Before declaring Git work done:

- [ ] Rewrite gate: every amended/rebased commit appeared in `git log @{u}..` before I touched it
- [ ] Deletion gate: I listed the casualties (`git status`, `git clean -n`) before any `--hard` / `-f`
- [ ] Push gate: target is not in `protected_branches` and not a shared branch; if forcing at all, `--force-with-lease` minimum, and within `force_push_policy`
- [ ] Conflict gate: marker grep is clean AND the project builds after resolution
- [ ] Identity gate: `git config user.email` is the right identity for this repo (work vs personal)
- [ ] Content gate: `git diff --cached --stat` reviewed — no credential, no build artifact, no blob the host will reject

## Traps

See `references/traps.md`.

## Where Experts Disagree

See `references/experts-disagree.md`.
