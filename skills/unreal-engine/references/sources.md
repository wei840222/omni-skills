# Official Sources & Engine Architecture References

This document records the official Epic Games documentation and architectural specifications for Unreal Engine C++ development.

## Official Engine Documentation

- **Unreal Engine C++ Programming**: [https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-cpp-in-unreal-engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-cpp-in-unreal-engine)
  - Engine architectural patterns, UCLASS/UFUNCTION reflection macros, and engine delegate binding.
- **Unreal Object Handling & Memory Management**: [https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-object-handling-in-unreal-engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-object-handling-in-unreal-engine)
  - UObject garbage collection, root sets, `UPROPERTY()` referencing constraints to prevent dangling pointers, and weak pointers (`TWeakObjectPtr`).
- **Actor Lifecycle & Ticking**:
  - AActor spawning (`SpawnActor`), component attachment, `BeginPlay`, and frame ticking hierarchies.
