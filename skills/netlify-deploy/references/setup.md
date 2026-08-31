# Setup — Netlify Deploy

Read this reference when a user first requests a Netlify deployment and the project context is unknown.

## Discover the project

Before proposing deploy commands, establish:

- package manager and declared build command;
- publish directory;
- single-app versus monorepo layout;
- whether the site is already linked;
- whether the user has requested a preview or production release.

## First safe execution

1. Run `npx netlify status`.
2. If authentication is needed, run `npx netlify login` and check status again.
3. If the project has a Git remote, run `git remote get-url origin` and attempt `npx netlify link --git-remote-url <remote>`.
4. Use `npx netlify init` only when a matching site cannot be linked.
5. Run the project's local build and verify the publish directory.
6. Create a preview with `npx netlify deploy`. Run `npx netlify deploy --prod` only after an explicit production request or readiness confirmation.

## Save preferences only when useful

When a user asks to retain deployment defaults, record them in `<state_root>/memory.md`:

- preferred deploy mode;
- frequent project paths and publish directories;
- team constraints such as a required preview review.

The setup is complete once authentication works, linking is reliable, and one preview deploy returns a valid URL.
