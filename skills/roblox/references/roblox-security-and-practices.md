# Roblox security and implementation guidance

## RemoteEvents and server authority
- Put authoritative game logic in `ServerScriptService`; use LocalScripts only for client behavior.
- Treat RemoteEvent and RemoteFunction arguments as untrusted. On the server, validate types, bounds, ownership, target state, rate, and permissions before applying an action.
- `FilteringEnabled` does not replace RemoteEvent validation.
- Use `RemoteEvent` for fire-and-forget communication. Use `RemoteFunction` only where a request must return a value; keep handlers bounded so clients are not stalled.

## DataStores
- Wrap `GetAsync()`, `SetAsync()`, and `UpdateAsync()` in `pcall`; handle failures with bounded retries and a clear recovery path.
- Use `UpdateAsync()` for read-modify-write updates so the transformation runs against the current stored value.
- Avoid concurrent save paths for the same player. Define a session-locking strategy before enabling cross-server rejoin behavior.
- Batch and queue saves to stay within platform limits. Test Studio API access only in a safe test environment.

## Lifecycle and memory
- Store each event connection you create and call `:Disconnect()` when its owner is no longer needed.
- Call `:Destroy()` for Instances that are permanently removed.
- Clean up player-owned data in `Players.PlayerRemoving` and reset character-specific connections in `CharacterAdded`.
- Release table references that retain no-longer-needed Instances or players.

## Replication and services
- `ServerStorage` is server-only; `ReplicatedStorage` is shared; `ReplicatedFirst` is for early client loading; Workspace replicates to clients, while the server remains authoritative.
- Retrieve services through `game:GetService("ServiceName")`, then cache frequently used references.
- Wait for `player.CharacterAdded` when character-dependent code may run before a character exists.

## RunService and timing
- Use `Heartbeat` for post-physics gameplay work, `RenderStepped` only for client visual work such as camera updates, and `Stepped` for pre-physics coordination.
- Keep per-frame work small; distribute expensive operations across frames.
- Prefer `task.wait()`, `task.spawn()`, and `task.defer()` to deprecated `wait()` and `spawn()`.
