# Official Sources & Runtime References

This document records the official documentation and technical specifications for the Bun runtime, bundler, and package manager.

## Official Runtime Documentation

- **Bun Documentation Home**: [https://bun.sh/docs](https://bun.sh/docs)
  - Overview of Bun architecture (JavaScriptCore engine, Zig implementation), CLI flags, and native APIs.
- **Bun Bundler**: [https://bun.sh/docs/bundler](https://bun.sh/docs/bundler)
  - Fast native bundler API (`Bun.build`), entry points, code splitting (`--splitting`), asset loaders, and external package configurations.
- **Bun Test Runner**: [https://bun.sh/docs/test](https://bun.sh/docs/test)
  - Native Jest-compatible test runner (`bun test`), lifecycle hooks, mocking API (`mock()`, `spyOn()`), and snapshot testing.
- **Package Manager & Lockfile**: [https://bun.sh/docs/pm/lockfile](https://bun.sh/docs/pm/lockfile)
  - High-speed package installer (`bun install`), workspaces, text-based `bun.lock` format (and legacy binary `bun.lockb`), and yarn/npm compatibility.
