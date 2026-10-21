# Unity Runtime Pitfalls

Affirmative patterns for Unity MonoBehaviour / UnityEngine.Object work. Prefer these over negative checklists.

## Lifecycle order

- Use `Awake` for self-init (own fields, `GetComponent` caches). Use `Start` for cross-object references after peer `Awake` calls.
- Expect `OnEnable` after `Awake` and before `Start` when the behaviour becomes active.
- Treat cross-script order as undefined unless Script Execution Order (or explicit init gates) is set.
- Expect `Awake` even when the behaviour starts disabled; `Start` runs only once the behaviour is enabled and active.

## GetComponent performance

- Cache `GetComponent` / `GetComponentInChildren` results in `Awake` or `Start`; avoid per-frame lookups.
- Prefer `TryGetComponent` when absence is normal — it returns a bool and avoids an extra null dance.
- Use `[RequireComponent(typeof(T))]` to document and enforce hard dependencies on the same GameObject.
- Treat deep `GetComponentInChildren` walks as expensive; narrow the search or cache the result.

## Physics timing

- Drive Rigidbody motion in `FixedUpdate` with `Rigidbody.MovePosition` / forces. Direct `transform.position` writes bypass the physics body.
- Expect `FixedUpdate` to run zero or many times relative to a rendered frame; size forces/steps for the physics step, not the frame.
- Use `Time.deltaTime` in `Update` and `Time.fixedDeltaTime` (or `Time.deltaTime`, which matches the active step) inside `FixedUpdate`.
- When `Physics.simulationMode` is not `FixedUpdate`, confirm where the simulation step runs before assuming classic FixedUpdate ordering.

## UnityEngine.Object fake null

- Compare Unity objects with `== null` / `!= null` (or truthiness). Unity overloads `==` so a destroyed / detached object reports as null even when the managed wrapper still exists.
- Prefer overloaded `==` over C# null-conditional `?.` on `UnityEngine.Object` references; `?.` follows CLR reference semantics and can miss the fake-null case.
- After `Object.Destroy`, treat the object as pending destruction until end of frame (or the current update loop completion); avoid relying on immediate native teardown.
- Reserve `DestroyImmediate` for Editor tooling. Player builds should use `Destroy`.

## Coroutines

- Start coroutines only on an active `MonoBehaviour`. Disabling or destroying the host stops its coroutines.
- Use `yield return null` for next frame, `WaitForSeconds` / `WaitForSecondsRealtime` for timed waits, and keep a `Coroutine` handle when you need reliable `StopCoroutine`.
- Prefer callback fields / state machines when a coroutine must publish a result; coroutines themselves are `IEnumerator` and do not return values to the caller.

## Instantiate and pooling

- Pool objects that spawn/despawn frequently. `Instantiate` and `Destroy` are comparatively expensive hot-path calls.
- Prefer `Instantiate(prefab, parent)` when parenting is known up front.
- Return pooled instances with `SetActive(false)` under a pool root; keep inactive clones organized rather than destroying them each cycle.

## Serialization

- Prefer `[SerializeField] private` fields for Inspector wiring. Public fields serialize but widen API surface.
- Use `[HideInInspector]` when a serialized field must stay out of the Inspector, and `[NonSerialized]` / `NonSerializedAttribute` when the field must not serialize at all.
- After first serialization, Inspector values win over code field initializers for serialized fields — change defaults in the asset/prefab when needed.

## ScriptableObjects

- Use ScriptableObjects as shared data assets across scenes/prefabs (`CreateAssetMenu` for authoring).
- Keep runtime mutation of asset instances Editor-only or clone-before-write. Player builds do not persist ScriptableObject asset edits.
- Prefer ScriptableObjects for config tables and item databases to reduce prefab duplication.

## Common mistakes

- Cache `Find*` / tag lookups; avoid scanning every frame.
- Compare tags with `CompareTag("Enemy")` rather than `tag == "Enemy"` (the latter allocates).
- Prefer `NonAlloc` physics queries (`RaycastNonAlloc`, etc.) in hot paths.
- Verify UI anchors across reference resolutions before shipping layout-sensitive HUD work.
- For async gameplay code, use a Unity-aware approach (for example UniTask or explicit main-thread continuations) so exceptions and player-loop timing stay visible.
