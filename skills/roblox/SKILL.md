---
name: roblox
description: Build or review Roblox Luau game logic with secure client/server boundaries, DataStore updates, lifecycle cleanup, replication, and RunService guidance. Use when implementing or auditing Roblox scripts, RemoteEvents, player data, or gameplay systems.
compatibility: "Roblox Studio and Luau"
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎲"}'
  related-skills: '{"review-code":"Review Roblox Luau changes for correctness, security, and maintainability."}'
---

## Scope
Use this skill for Roblox Studio and Luau code. The server is authoritative for game rules and persistent player data.

## Workflow
1. Identify whether each action belongs on the server or in a LocalScript.
2. Validate every client-supplied value, target, and permission on the server before changing game state.
3. Select RemoteEvent for one-way messages; use RemoteFunction only when the client needs a result.
4. For persistent data, wrap service calls in `pcall` and use `UpdateAsync()` for read-modify-write operations.
5. Verify cleanup, replication visibility, and frame-loop cost before shipping.

## State location
This skill does not persist local state. Roblox game state belongs to the experience and its configured DataStores.

## Load detailed guidance
For task-specific implementation details, read `references/roblox-security-and-practices.md` for DataStore handling, RemoteEvent security, lifecycle cleanup, replication, character events, service access, and RunService details.

## Safety boundaries
- Keep authority checks and sensitive game logic on the server.
- Check permissions server-side before handling administrative RemoteEvent actions.
- Use server-side validation even when a client UI already restricts input.
