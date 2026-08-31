# `netlify.toml` Quick Reference

Load this reference when configuring build settings, redirects, deploy contexts, or Edge Functions. Netlify uses `netlify.toml` to describe build and deploy configuration; keep sensitive values in Netlify environment-variable settings instead of committing them to this file.

## Minimal build configuration

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

## SPA fallback

```toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## Deploy-context overrides

```toml
[context.production]
  command = "npm run build"

[context.deploy-preview]
  command = "npm run build:preview"
```

## Monorepo base directory

```toml
[build]
  base = "apps/web"
  command = "npm run build"
  publish = "dist"
```

## Edge Functions

```toml
[[edge_functions]]
  path = "/api/*"
  function = "hello"
```

## Validate before release

```bash
npx netlify build --dry
```

Use the project's actual build and publish values; framework defaults are starting points, not proof of the correct output directory.
