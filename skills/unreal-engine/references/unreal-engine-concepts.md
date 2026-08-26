# Unreal Engine Concepts

Primary sources used for this refactor (Gate 6):

- Unreal Engine Garbage Collection Overview — https://dev.epicgames.com/documentation/unreal-engine/garbage-collection-overview-in-unreal-engine
- Unreal Engine UPROPERTY Specifiers — https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-uproperty-specifiers
- Unreal Engine Actor Lifecycle — https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-actor-lifecycle
- Unreal Engine Networking and Multiplayer — https://dev.epicgames.com/documentation/unreal-engine/networking-and-multiplayer-in-unreal-engine
- Soft Object Pointers — https://dev.epicgames.com/documentation/unreal-engine/soft-object-pointers-in-unreal-engine

## Garbage Collection
- Raw pointers to UObjects get garbage collected — use `UPROPERTY()` to prevent.
- `UPROPERTY()` marks for GC tracking. Ensure `UPROPERTY()` is used to avoid dangling pointers.
- `TWeakObjectPtr` for optional references — doesn't prevent collection, verify with `IsValid()`.
- `NewObject<T>()` for UObjects — GC will not track raw `new` operations.

## UPROPERTY and UFUNCTION
- `UPROPERTY()` required for Blueprint access — and for GC tracking.
- `UFUNCTION()` for Blueprint callable/events — also required for replication.
- `EditAnywhere` vs `VisibleAnywhere` — edit allows changes, visible is read-only.
- `BlueprintReadWrite` vs `BlueprintReadOnly` — controls Blueprint access level.

## Actor Lifecycle
- `BeginPlay` after all components initialized — safe to access components.
- Constructor runs on CDO (Class Default Object) — wait for `BeginPlay` to spawn actors or access the world.
- `PostInitializeComponents` before BeginPlay — for component setup.
- `EndPlay` for cleanup — called on destroy and level transition.

## Tick Performance
- Disable tick when unnecessary — `PrimaryActorTick.bCanEverTick = false`.
- Use timers instead of tick + counter — `GetWorldTimerManager().SetTimer()`.
- Tick groups for ordering — `PrePhysics`, `DuringPhysics`, `PostPhysics`.
- Blueprint tick expensive — move hot logic to C++.

## Replication
- Server is authority — clients request, server validates and replicates.
- `UPROPERTY(Replicated)` for variable sync — implement `GetLifetimeReplicatedProps`.
- `UFUNCTION(Server)` for client-to-server RPC — must be `Reliable` or `Unreliable`.
- `HasAuthority()` to check if server — before executing authoritative logic.
- `Role` and `RemoteRole` for network role checks — `ROLE_Authority` is server.

## Asset References
- Hard references load with parent — bloats memory, use for always-needed.
- Soft references (`TSoftObjectPtr`) load on demand — for optional or large assets.
- `LoadSynchronous()` or `AsyncLoad` for soft refs — ensure loaded before access.
- Blueprint class references: `TSubclassOf<T>` — type-safe class selection.

## Memory and Pointers
- `TSharedPtr` for non-UObjects — reference counted, auto-deletes.
- `TUniquePtr` for exclusive ownership — can't copy, moves only.
- `MakeShared<T>()` for creation — single allocation for object and control block.
- Choose a single memory pattern — stick to either raw `new/delete` or smart pointers, avoid mixing them.

## Common Mistakes
- Accessing null actor in Blueprint — use `IsValid()` node before access.
- PIE (Play In Editor) vs packaged build differ — test shipping build.
- Hot reload corrupts Blueprints — close editor, build, reopen.
- `GetWorld()` null in constructor — world exists later in the lifecycle, use BeginPlay.
- Spawning in constructor crashes — defer to BeginPlay or later.
- `FString` for display, `FName` for identifiers — FName is hashed, faster comparison.
