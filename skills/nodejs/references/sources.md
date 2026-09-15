# Research Sources — nodejs

Gate 6 anchors for Node.js runtime behavior, HTTP timeouts, modules, packaging, security, and operations. Prefer primary Node.js docs, MDN, and NIST/OWASP baselines over secondary blog posts when rules conflict.

## Runtime, releases, and ABI

- **Node.js — Previous Releases** — live Current / Active LTS / Maintenance majors and EOL dates via https://nodejs.org/en/about/previous-releases
- **Node.js — API documentation (latest LTS)** — core modules, process, timers, diagnostics via https://nodejs.org/docs/latest/api/
- **Node.js — Release schedule** — major cadence and LTS phases via https://github.com/nodejs/release#release-schedule
- **Node.js — N-API / ABI stability** — native module compatibility expectations via https://nodejs.org/api/n-api.html

## Event loop, async, streams, diagnostics

- **Node.js — Event loop best practices** — blocking, timers, and I/O scheduling via https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick
- **Node.js — stream.pipeline** — error propagation and cleanup for piped streams via https://nodejs.org/api/stream.html#streampipelinesource-transforms-destination-callback
- **Node.js — Diagnostics / `--cpu-prof`** — CPU profiling entry points via https://nodejs.org/en/learn/diagnostics/poor-performance/using-cpu-profile
- **Joyent — Error handling patterns in Node.js** — operational vs programmer errors framing via https://www.joyent.com/node-js/production/design/errors

## HTTP servers, clients, and proxies

- **Node.js — http.Server timeout knobs** — `keepAliveTimeout`, `headersTimeout`, `requestTimeout` via https://nodejs.org/api/http.html#serverkeepalivetimeout
- **AWS ELB — idle timeout** — ALB/NLB idle timeout defaults that interact with Node keep-alive via https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#connection-idle-timeout
- **MDN — AbortSignal.timeout()** — outbound request deadlines via https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/timeout_static
- **Node.js — Undici / fetch** — built-in fetch dispatcher behavior via https://nodejs.org/api/globals.html#fetch

## Modules, packages, and lockfiles

- **Node.js — ECMAScript modules** — ESM resolution, extensions, `__dirname` replacements via https://nodejs.org/api/esm.html
- **Node.js — Packages / exports** — `exports` map and dual-package caveats via https://nodejs.org/api/packages.html
- **npm — `npm ci`** — clean CI installs from a committed lockfile via https://docs.npmjs.com/cli/v10/commands/npm-ci
- **npm — package-lock.json** — lockfile role and reproducibility via https://docs.npmjs.com/cli/v10/configuring-npm/package-lock-json

## Security and hardening

- **Node.js — Security best practices** — threat model for the runtime and dependencies via https://nodejs.org/en/learn/getting-started/security-best-practices
- **OWASP — Node.js Security Cheat Sheet** — injection, path traversal, ReDoS, secrets handling via https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html
- **Node.js — `vm` module warning** — not a security sandbox via https://nodejs.org/api/vm.html#vm-executing-javascript
- **CWE-400 / CWE-1333** — uncontrolled resource consumption and ReDoS classes via https://cwe.mitre.org/data/definitions/400.html

## Containers, signals, and production ops

- **Kubernetes — Pod lifecycle / termination** — `terminationGracePeriodSeconds` and SIGTERM drain windows via https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination
- **Docker — PID 1 signal handling** — why bare `node` as PID 1 drops signals without an init via https://docs.docker.com/engine/reference/run/#foreground-and-background
- **Node.js — Process / signal events** — SIGTERM/SIGINT handlers and exit codes via https://nodejs.org/api/process.html#signal-events

## Notes for agents

- Keep **Node runtime operations** (this skill) separate from language-only JS (`javascript`), type-system design (`typescript`), container packaging (`docker`), and HTTP API contracts (`api`).
- Re-check `nodejs.org/en/about/previous-releases` before quoting LTS/EOL dates; cadence is stable, the live majors are not.
- Prefer primary Node/npm/MDN/OWASP docs when diagnosing hangs, OOM, module format mismatches, or proxy 502 patterns.
- Local state stays under portable `<state_root>/nodejs/`; store credential **pointers** only.

## Obsolete / removed coupling

- Removed clawic.com homepage/promotional Related Skills blurb and deleted `_meta.json` (Gate 5).
- Replaced hardcoded `~/Clawic/data/nodejs/` and related configPaths with portable `<state_root>/...` (Gate 3).
- Moved flat topic files into `references/` and rewrote progressive-disclosure routing in `SKILL.md` (Gate 2 / Gate 7).
