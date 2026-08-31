# Netlify CLI Commands

Load this reference when exact Netlify CLI syntax is needed. Confirm current flags with `npx netlify <command> --help` before executing an unfamiliar or version-sensitive operation.

## Authentication and project status

```bash
npx netlify login
npx netlify status
npx netlify logout
```

## Site linking

```bash
npx netlify link
npx netlify link --git-remote-url <url>
npx netlify init
npx netlify unlink
```

For a repository already associated with a Netlify project, prefer `netlify link` over `netlify init`.

## Deployments

```bash
npx netlify deploy
npx netlify deploy --prod
npx netlify deploy --dir=dist
npx netlify deploy --message="release note"
npx netlify deploy:list
```

## Environment variables

```bash
npx netlify env:list
npx netlify env:set KEY value
npx netlify env:get KEY
npx netlify env:import .env
```

Treat environment variables as sensitive. Prefer Netlify's managed environment-variable settings and avoid committing secret values to `netlify.toml`.

## Build and diagnostics

```bash
npx netlify build
npx netlify build --dry
npx netlify --version
npx netlify status --verbose
npx netlify help deploy
```

## Dashboard shortcuts

```bash
npx netlify open
npx netlify open:admin
npx netlify open:site
```
