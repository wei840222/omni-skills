# Common Traps

- Building menus, inventory, and cosmetics before core loop validation → large scope with no fun proof
- Tying physics and gameplay directly to frame rate → inconsistent behavior across devices
- Importing heavy 3D assets too early for browser targets → unusable mobile experience
- Skipping input latency and camera readability checks → players quit despite stable FPS
- Adding multiplayer before single-player loop quality → expensive complexity without retention value
- Ignoring save and state recovery strategy → broken sessions and user frustration
- Leaving GPU resources undisposed across scene changes → mobile tab crashes and rising `renderer.info` memory
- Mixing Browser Instant and Engine Path in one milestone without an explicit migration plan → thrash and half-finished tooling
