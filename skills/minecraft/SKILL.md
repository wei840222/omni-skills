---
name: minecraft
description: Plan and troubleshoot Minecraft worlds, builds, redstone, commands, farms, mods, and servers without mixing Java and Bedrock rules. Use when a request needs edition-aware gameplay, build, automation, command, or server guidance.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧱"}'
  related-skills: '{"gaming":"Provides broader game strategy outside Minecraft-specific mechanics.","home-server":"Covers private self-hosted infrastructure for a Minecraft server.","java":"Covers Java runtime and tooling issues behind Java Edition launchers, mods, or dedicated servers.","linux":"Covers Linux host administration for Minecraft servers or containers.","server":"Covers general dedicated-server deployment and troubleshooting patterns."}'
---

## State location

Minecraft state may exist in `<workspace>/minecraft/`, `<workspace>/memory/minecraft/`, or `~/minecraft/`. Before any state operation, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured state path when one is supplied.
2. Otherwise, use the first existing directory in this order: `<workspace>/minecraft/`, `<workspace>/memory/minecraft/`, then `~/minecraft/`.
3. When multiple candidates exist, use only the highest-precedence location and report that separate copies exist.
4. When none exists and the user requests persistent Minecraft preferences or notes, create `<workspace>/minecraft/`.
5. When the host does not provide `<workspace>`, use an existing `~/minecraft/`; otherwise request a state path before creating data.

Keep the selected `<state_root>` for all state operations. Create `archive/` and optional note files only when the corresponding task needs them.

# Minecraft

Minecraft workflow for real play decisions. Use this when the agent must help with world planning, survival progression, builds, commands, redstone, modded setups, or server issues without blending edition-specific rules.

## When to Use

Use this skill when the task is actually about Minecraft execution, not generic gaming chat.

Typical activation moments:
- when the user needs a build plan, farm layout, or resource estimate
- when a command, datapack, redstone machine, or automation chain is failing
- when Java vs Bedrock differences change the answer
- when a world upgrade, modpack change, or server setup needs a safer path
- when the user wants a survival route, boss prep checklist, or progression shortcut
- when coordinates, dimensions, spawn logic, chunk behavior, or mob rules matter

## Architecture

Persistence is optional: if the user wants one-off help only, keep the work session-only and do not create or update local files.

```text
<state_root>/
├── memory.md        # edition, version, style, and activation defaults
├── worlds.md        # optional world seeds, key locations, and constraints
├── builds.md        # optional build briefs and recurring dimensions
├── servers.md       # optional server stack, mod loaders, and admin notes
└── archive/         # retired saves, old versions, and deprecated setups
```

## Reference routing

Load only the file that matches the current lane so the answer stays practical instead of turning into a giant wiki dump.

| Topic | File | When to load |
|-------|------|--------------|
| Setup and activation behavior | `references/setup.md` | When initializing the skill or workspace for the first time. |
| Optional local memory schema | `references/memory-template.md` | When creating or reading from `<state_root>/` files. |
| Java vs Bedrock gating | `references/edition-gate.md` | When user request edition or platform is unclear. |
| Build planning template | `references/build-brief.md` | When asked to plan a structure, building, or layout. |
| Redstone and farm debugging | `references/redstone-debug.md` | When troubleshooting or designing redstone or farms. |
| Commands and datapack patterns | `references/command-patterns.md` | When generating commands, datapacks, or command blocks. |
| Survival progression routes | `references/survival-routes.md` | When user asks for survival mode goals or progression checklists. |
| Server, Realm, and modpack lanes | `references/server-lanes.md` | When handling server setup, modpacks, or administration. |

## Requirements

- No credentials or external binaries are required for planning and troubleshooting.
- Runtime tools depend on the player's actual setup: vanilla world, Realm, dedicated server, mod loader, or admin console.
- Verify operator rights, creative access, or command privileges before proceeding with commands.
- Require explicit confirmation before advising destructive world edits, rollback-hostile commands, or risky modpack changes.

## Core Rules

### 1. Gate on Edition, Version, and Authority First
- Confirm Java or Bedrock, approximate version, single-player or multiplayer, and whether the user has cheats, operator rights, or admin access.
- Minecraft advice breaks fast when edition, version, or permissions are wrong.
- If that surface is unclear, ask the smallest question that changes the answer before giving steps.

### 2. Work in Lanes, Not Mixed Advice
- Separate the task into one main lane: build planning, survival progression, commands/datapacks, redstone/farms, or server/modpack operations.
- Keep advice strictly within the requested edition (Java or Bedrock) and game mode (survival or creative), unless the user explicitly requests a mix.
- If a task crosses lanes, solve the blocker first and keep the dependencies visible.

### 3. Translate Goals into Coordinates, Counts, and Checkpoints
- Good Minecraft help uses dimensions, block counts, spawn spaces, fuel/time estimates, and test checkpoints.
- Prefer "build a 17x17 interior with two-block walkways and mark chunk borders first" over vague aesthetic advice.
- Every plan should tell the user what to verify before they scale it.

### 4. Preserve World Safety Before Speed
- Recommend backups, test copies, or small-area rehearsals before destructive commands, version jumps, chunk loaders, or modpack updates.
- For command blocks and datapacks, start in a disposable test world if the blast radius is unclear.
- Never suggest `/kill`, `/fill`, `/clone`, `/tp`, or world-edit style operations against a live area without naming the risk.

### 5. Debug the Smallest Reproducible Slice
- For redstone and farms: isolate one module, one clock, one spawn rule, or one villager pathing segment at a time.
- For commands: reduce to the smallest selector, target, and output before adding conditions or scoreboards.
- For servers/modpacks: confirm version, loader, logs, and one failing mod or plugin before proposing broad rewrites.

### 6. Keep Mechanics Canonical and Version-Aware
- Distinguish between hard mechanics, community conventions, and aesthetic preferences.
- If a mechanic changed between versions, say so directly instead of acting certain.
- When exact rates depend on simulation distance, tick settings, or gamerules, call that out.

### 7. Optimize for the Player's Constraint, Not Your Favorite Meta
- Some users want fastest progression, some want low-risk survival, some want pretty builds, and some want minimal admin burden.
- Match the answer to their actual constraint: time, materials, skill level, server lag, platform, or co-op play.
- If the constraint is not stated, infer cautiously and make the assumption explicit.

## Operating Lanes

Start by naming the main lane before recommending blocks, commands, or hosting changes. That keeps the answer grounded in the actual job instead of mixing unrelated systems.

| Lane | First questions | Best file |
|------|-----------------|-----------|
| Build planning | edition, biome/style, scale, material budget, survival or creative | `references/build-brief.md` |
| Redstone or farm issue | edition, version, single-player/server, exact failure symptom | `references/redstone-debug.md` |
| Commands or datapacks | edition, version, command access, target behavior | `references/command-patterns.md` |
| Survival route | world stage, current gear, objective, risk tolerance | `references/survival-routes.md` |
| Server or modpack | hosting type, loader, version, player count, logs | `references/server-lanes.md` |

## Default Output Pack

When the task is substantial, prefer this shape:
- edition, version, and authority assumptions
- recommended lane and why
- step-by-step plan with dimensions, counts, or commands
- risk checks before irreversible actions
- what to test next if the first fix fails

If the user wants a fast answer, compress the same logic into a short plan plus one critical warning.

## Common Traps

Most bad Minecraft advice fails because it skips the gating step, not because the mechanic is complicated. Use these traps as a quick filter before giving a confident answer.

| Trap | Why It Fails | Better Move |
|------|--------------|-------------|
| Mixing Java and Bedrock syntax | Commands, redstone, and farm rules diverge fast | Gate on edition before giving steps |
| Designing with unlimited blocks in a survival task | The plan becomes unusable in practice | Start from material budget and progression stage |
| Rebuilding the whole contraption at once | Debug signal is lost | Isolate one module and verify it works alone |
| Upgrading world, loader, and mods together | Root cause becomes unreadable | Change one layer at a time with backup first |
| Giving exact mob rates without server settings | Tick and simulation differences change results | State assumptions and give tuning checkpoints |
| Using destructive commands as "quick fixes" | Live areas get damaged fast | Use test copies, boundaries, and explicit confirmation |
| Treating every build as aesthetic only | Function often matters first | Ask whether the priority is beauty, throughput, safety, or lag |

## Security & Privacy

**Data that leaves your machine:**
- None by default. This is an instruction-only Minecraft execution skill.

**Data stored locally:**
- Optional notes in `<state_root>/` about edition, preferred play style, build constraints, and server context only if the user wants persistence.

## Trust

This skill provides structured Minecraft guidance and optional local note patterns.
No credentials are required and no third-party services are contacted by default.
