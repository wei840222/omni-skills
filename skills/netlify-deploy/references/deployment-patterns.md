# Netlify Deployment Patterns

Load this reference for first deploys, existing-site linking, monorepos, production releases, or recovery from a failed deploy.

## Decision flow

```text
Check authentication with `npx netlify status`.
├─ Not authenticated: run `npx netlify login`, then check status again.
└─ Authenticated: establish the site link.
   ├─ Existing repository: get `origin` and run `npx netlify link --git-remote-url <remote-url>`.
   ├─ No matching site: run `npx netlify init` to create or connect one.
   └─ Linked site: build and verify the publish directory.
      ├─ Preview requested: `npx netlify deploy`
      └─ Production requested and readiness confirmed: `npx netlify deploy --prod`
```

## First-time deploy

1. Run `npx netlify status`; authenticate if required.
2. Discover the project's package manager, build command, publish directory, and monorepo base.
3. Link an existing site when possible; use `npx netlify init` when a new site must be created or connected.
4. Run the declared local build and verify its output directory.
5. Run `npx netlify deploy` and verify the preview URL before a production release.

## Existing repository and site

1. Run `git remote get-url origin`.
2. Run `npx netlify link --git-remote-url <remote-url>`.
3. Build locally, deploy a preview, and inspect its URL before release.

## Monorepo

Deploy from the target package directory or configure `[build].base` in `netlify.toml`. Verify that the build command and publish directory resolve relative to that base before linking or deploying.

## Production promotion

1. Produce a preview deploy.
2. Run the project's smoke checks against the preview URL.
3. Obtain an explicit production request or readiness confirmation.
4. Run `npx netlify deploy --prod`.
5. Report the production URL with the deployed commit context.

## Recovery

| Signal | Recovery |
|---|---|
| Authentication failure | Run `npx netlify login`, then `npx netlify status`. |
| Site is not linked | Re-run the link-first flow; initialize only when no matching site exists. |
| Missing publish directory | Run the declared build, inspect the output, then pass the verified directory to the deploy command or configuration. |
| Build failure | Reproduce with the project's local build command, fix the build error, then redeploy. |
| Wrong app in a monorepo | Correct the working directory or `[build].base`, re-check the site link, then create a new preview. |
