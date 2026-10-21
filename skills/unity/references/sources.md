# Unity Sources

Primary sources re-checked during the 2026-10-21 `unity` handoff (Gate 6). Prefer the project's installed Unity version docs when they differ.

## Lifecycle / player loop

- Event function execution order — https://docs.unity3d.com/Manual/ExecutionOrder.html
- Unity 6.0 execution order mirror — https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html
- `MonoBehaviour.FixedUpdate` — https://docs.unity3d.com/ScriptReference/MonoBehaviour.FixedUpdate.html

## Fake null / Destroy

- `Object.operator ==` (custom null check for native/managed pair) — https://docs.unity3d.com/ScriptReference/Object-operator_eq.html
- `Object.Destroy` — https://docs.unity3d.com/ScriptReference/Object.Destroy.html
- Custom `==` operator background — https://blog.unity.com/engine-platform/custom-operator-should-we-keep-it

## Components / performance / data

- `GameObject.GetComponent` — https://docs.unity3d.com/ScriptReference/GameObject.GetComponent.html
- Reference-type performance notes — https://docs.unity3d.com/Manual/BestPracticeUnderstandingPerformanceInUnity5.html
- Coroutines — https://docs.unity3d.com/Manual/Coroutines.html
- Script serialization — https://docs.unity3d.com/Manual/script-Serialization.html
- ScriptableObject — https://docs.unity3d.com/Manual/class-ScriptableObject.html

## Freshness notes (2026-10-21)

- Execution-order Manual still places `Awake` → `OnEnable` → `Start`, with physics simulation timing dependent on `Physics.simulationMode` (FixedUpdate / Update / Script).
- `Object.operator ==` docs still document overloaded null checks against the native object pointer (fake null), distinct from CLR `ReferenceEquals`.
- Legacy blog URL `.../technology/custom-==-operator-should-we-keep-it` redirects; canonical post path is `.../engine-platform/custom-operator-should-we-keep-it`.
- Older Manual slug `BestPracticeUnderstandingPerformanceInUnity4` is stale for current docs; use the live performance / reference-types Manual pages above.
