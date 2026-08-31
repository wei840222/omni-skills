# Vite Best Practices

Vite is a frontend build tool and dev server created by Evan You; ongoing stewardship is associated with VoidZero.

## Environment Variables
- Only `VITE_` prefixed vars are exposed to client code — `DB_PASSWORD` stays server-side, `VITE_API_URL` is bundled
- Access via `import.meta.env.VITE_*` not `process.env` — process.env is Node-only and undefined in browser
- `.env.local` overrides `.env` and is gitignored by default — use for local secrets
- `import.meta.env.MODE` is `development` or `production` — use for conditional logic, not `NODE_ENV`

## CommonJS Compatibility
- Pure ESM by default — CommonJS packages need `optimizeDeps.include` for pre-bundling
- Vite uses ESM. For dynamic requires, use `import` or `createRequire` from `module`
- Some packages ship broken ESM — add to `ssr.noExternal` or `optimizeDeps.exclude` and let Vite transform them
- Prefer default-import-then-destructure when CommonJS named exports fail ESM interop: `import pkg from 'pkg'; const { method } = pkg`

## Dependency Pre-bundling
- Vite pre-bundles dependencies on first run — delete `node_modules/.vite` to force rebuild after package changes
- Large dependencies slow down dev server start — add rarely-changing ones to `optimizeDeps.include` for persistent cache
- Linked local packages (`npm link`) aren't pre-bundled — add to `optimizeDeps.include` explicitly
- Reserve `optimizeDeps.force: true` for debugging cache issues; keep it off in normal development to preserve startup speed

## Path Aliases
- Configure in both `vite.config.ts` AND `tsconfig.json` — Vite uses its own, TypeScript uses tsconfig
- Use `path.resolve(__dirname, './src')` not relative paths — relative breaks depending on working directory
- `@/` alias is not built-in — must configure manually unlike some frameworks

```typescript
// vite.config.ts
resolve: {
  alias: { '@': path.resolve(__dirname, './src') }
}
```

## Dev Server Proxy
- Proxy only works in dev — production needs actual CORS config or reverse proxy
- `changeOrigin: true` rewrites Host header — required for most APIs that check origin
- WebSocket proxy needs explicit `ws: true` — HTTP proxy doesn't forward WS by default
- Trailing slashes matter: `/api` proxies `/api/users`, `/api/` only proxies `/api//users`

```typescript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:3000',
      changeOrigin: true,
      ws: true,
      rewrite: path => path.replace(/^\/api/, '')
    }
  }
}
```

## Static Assets
- `public/` files served at root, not processed — use for favicons, robots.txt, files that need exact paths
- `src/assets/` files are processed, hashed, can be imported — use for images, fonts referenced in code
- Import assets to get resolved URL: `import logo from './logo.png'` — hardcoded paths break after build
- `new URL('./img.png', import.meta.url)` for dynamic paths — Use explicit paths with `new URL()` instead of template literals with variables

## Build Optimization
- `build.rollupOptions.output.manualChunks` for code splitting — without it, one giant bundle
- Analyze bundle with `rollup-plugin-visualizer` — find unexpected large dependencies
- `build.target` defaults to modern browsers — set `'es2015'` for legacy support, but increases bundle size
- `build.cssCodeSplit: true` (default) — each async chunk gets its own CSS file

## Library Mode
- `build.lib` for npm packages — different config from app mode
- Set `external` for peer dependencies — Keep React/Vue external from your library bundle
- Generate types separately with `tsc` — Vite doesn't emit `.d.ts` files
- Both ESM and CJS outputs: `formats: ['es', 'cjs']` — some consumers still need require()

## HMR Issues
- Keep module graphs acyclic so HMR can update in place; when a cycle remains, expect a full reload
- State lost on HMR means component isn't accepting updates — check for `import.meta.hot.accept()`
- CSS changes trigger full reload if imported in JS that doesn't accept HMR — import CSS in components that do
- `server.hmr.overlay: false` hides error overlay — useful for custom error handling but hides issues

## SSR Configuration
- `ssr.external` for Node-only packages — prevents bundling node_modules in SSR build
- `ssr.noExternal` forces bundling — needed for packages with browser-specific imports
- CSS imports fail in SSR by default — use `?inline` suffix or configure `css.postcss` for SSR

## Sources

### Official Vite docs
- **Vite Guide — Env Variables and Modes** — client exposure uses `VITE_` prefix and `import.meta.env` via https://vite.dev/guide/env-and-mode.html
- **Vite Config — server.proxy** — dev-only proxy, `changeOrigin`, and WebSocket `ws` via https://vite.dev/config/server-options.html#server-proxy
- **Vite Guide — Building for Production** — `build.target`, CSS code splitting, and Rollup output options via https://vite.dev/guide/build.html
- **Vite Guide — Building for Library Mode** — `build.lib`, `external`, and dual format outputs via https://vite.dev/guide/build.html#library-mode
- **Vite Guide — Server-Side Rendering** — `ssr.external` / `ssr.noExternal` and SSR CSS caveats via https://vite.dev/guide/ssr.html
- **Vite Guide — Features / Dependency Pre-Bundling** — `optimizeDeps` include/exclude/force behavior via https://vite.dev/guide/dep-pre-bundling.html
- **Vite Guide — Backend Integration / Static Asset Handling** — `public/` vs imported assets and `new URL(..., import.meta.url)` via https://vite.dev/guide/assets.html
