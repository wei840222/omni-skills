# Three.js Production Best Practices

## Minimal responsive scene

```js
const clock = new THREE.Clock();
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);

function resize() {
  const { innerWidth: width, innerHeight: height } = window;
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
}
window.addEventListener('resize', resize);

renderer.setAnimationLoop(() => {
  const delta = clock.getDelta();
  controls?.update();
  mixer?.update(delta);
  renderer.render(scene, camera);
});
```

Use `clock.getDelta()` so movement and `AnimationMixer` updates remain frame-rate independent. Use `renderer.setAnimationLoop()` when the renderer owns the loop; it is compatible with WebXR sessions.

## Resource lifecycle

When removing an owned model, dispose each geometry, material, and material texture before removing the object from the scene. Materials can be arrays; textures can appear in multiple material properties. Shared assets need reference ownership so one consumer does not dispose an asset still used by another.

```js
function disposeMaterial(material) {
  for (const value of Object.values(material)) {
    if (value?.isTexture) value.dispose();
  }
  material.dispose();
}

function disposeObject(root) {
  root.traverse((object) => {
    object.geometry?.dispose();
    const materials = Array.isArray(object.material)
      ? object.material
      : object.material ? [object.material] : [];
    materials.forEach(disposeMaterial);
  });
  root.removeFromParent();
}
```

Also dispose render targets, post-processing passes, controls, and the renderer when the whole application lifecycle ends. Verify cleanup with `renderer.info.memory`; a scene transition should not cause resource counts to grow indefinitely.

## Scene setup and assets

- Use `MeshStandardMaterial` or `MeshPhongMaterial` for lit meshes; `MeshBasicMaterial` intentionally ignores lights.
- Begin lit scenes with an ambient baseline plus a directional or environment light. Use `PMREMGenerator` for physically based environment-map reflections.
- Import addons from the path appropriate to the installed Three.js version, for example `three/addons/controls/OrbitControls.js`. With OrbitControls damping enabled, call `controls.update()` inside the loop.
- Load glTF models asynchronously. Show progress through `LoadingManager`, and configure CORS or same-origin hosting before requesting remote textures and models. Use `DRACOLoader` for assets supplied with Draco-compressed geometry.
- Choose camera near and far planes as tightly as the scene permits to limit depth precision issues such as z-fighting. Check loaded-model bounds before positioning the camera.

## Performance tuning

1. Inspect `renderer.info` to establish draw-call, triangle, and texture-memory baselines.
2. Merge genuinely static compatible geometries with `BufferGeometryUtils` when that reduces draw calls without losing needed material or transform boundaries.
3. Use `InstancedMesh` for many copies of the same geometry and material.
4. Keep frustum culling enabled unless a measured bounding-volume issue requires a targeted correction.
5. Cap pixel ratio to the visual requirement; `Math.min(devicePixelRatio, 2)` is a common desktop baseline, not a universal target.

## Recovery paths

| Symptom | Check and recover |
| --- | --- |
| Canvas is stretched after resize | Run the resize sequence above: aspect, projection matrix, then renderer size. |
| Model is black | Confirm it uses a light-responsive material, add lighting, then inspect loaded textures and CORS errors. |
| Controls damping has no effect | Enable damping and call `controls.update()` in each animation tick. |
| Scene transitions leak memory | Traverse and dispose owned resources, then compare `renderer.info.memory` before and after repeated transitions. |
| Large scene flickers or shows z-fighting | Narrow the camera near/far range and recheck model scale and bounds. |
| Frame time is high | Measure with `renderer.info`, then reduce draw calls via instancing or safe static merges before lowering visual quality. |
