# Revision Syntax

Most "Git did something I did not ask for" reports are a misread revision expression. Decoder:

| Expression | Means | Trap |
|---|---|---|
| `HEAD~2` | Two commits back along first parents | Follows the mainline through merges, skipping the merged branch |
| `HEAD^2` | The SECOND PARENT of a merge commit | Not "two back": `^` selects a parent, `~` walks generations |
| `HEAD@{2}` | Where HEAD pointed two reflog moves ago | Time, not ancestry — and local to this clone only |
| `@{u}` / `@{push}` | The tracked upstream / where a push would land | They differ in triangular setups (fork: pull from upstream, push to origin) |
| `A..B` | Commits reachable from B but not A | In `git diff`, the same expression means the plain A-to-B diff |
| `A...B` | `log`: commits on either side but not both. `diff`: B against the MERGE-BASE | The one expression whose meaning changes between `log` and `diff` — the source of "my diff shows unrelated files" |
| `:/fix login` | Most recent commit whose message contains that text | Searches all reachable history, not just this branch |
| `:1:file` `:2:file` `:3:file` | During a conflict: base, ours, theirs | Numbering is fixed; "ours/theirs" inverts under rebase (→ Conflict Basics) |
| `main@{yesterday}` | Branch tip as of yesterday | Reflog-based: empty in a fresh clone, and gone after reflog expiry |
| `v1.2^{}` | The commit an annotated tag points at | Without peeling, a tag is its own object — `git diff v1.2` compares against the tag object's target, scripts that assume a commit break |

Ambiguity between a branch and a path is resolved with `--`: `git checkout -- config` is always the file.
