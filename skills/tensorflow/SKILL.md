---
name: tensorflow
description: Resolve TensorFlow execution, memory, shape, and training gotchas. Use when debugging tf.function retracing, GPU OOM, tf.data bottlenecks, GradientTape issues, or SavedModel export; skip pure PyTorch or generic Python numerical work.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧠","requires":{"bins":["python3"]}}'
  related-skills: '{"pytorch":"Use when the stack is PyTorch rather than TensorFlow/Keras.","keras":"High-level Keras model-building patterns that often sit on top of TensorFlow.","numpy":"Array and broadcasting fundamentals that TensorFlow interops with outside the graph."}'
---

## When to load

Load this skill when writing or debugging TensorFlow / `tf.keras` code and the failure mode is execution graph, device memory, input pipeline, shapes, gradients, training-mode mismatch, or model export.

Do not load as the primary skill for pure PyTorch work, generic NumPy-only numerical code, or non-ML Python tasks.

## Critical rules

- Enable GPU memory growth before the first GPU op when sharing a device or debugging OOM: `tf.config.experimental.set_memory_growth(gpu, True)`.
- Stabilize `tf.function` tracing with `input_signature` / `TensorSpec` when shapes should be fixed; treat plain Python values as trace-time constants.
- Build `tf.data` pipelines with `cache` → map/augment → `batch` → `prefetch(tf.data.AUTOTUNE)` so host prep overlaps device work.
- Set `model.trainable` / BatchNorm `training=` **before** compile or the step that must observe the mode; post-compile toggles are a common silent miss.
- Prefer SavedModel for serving and custom objects; treat H5 as weights-oriented and limited for full object graphs.

## State location

This skill is stateless guidance. It does not own a mutable `<state_root>` package path. Project artifacts (checkpoints, SavedModel directories, logs) stay in the user workspace or an explicitly configured training output path.

## Progressive disclosure

For implementation detail, load the matching file under `references/`:

- Read `references/gotchas.md` for `tf.function` retracing, GPU memory growth, `tf.data` performance, shapes, GradientTape, training-mode traps, export formats, and common graph/eager mistakes.
- Read `references/sources.md` for the official TensorFlow guides used to verify those heuristics.
