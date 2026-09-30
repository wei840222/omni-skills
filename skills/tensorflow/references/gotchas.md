# TensorFlow Gotchas and Common Mistakes

## tf.function Retracing

- New input **shape** or **dtype** forces a retrace — expensive and often prints a retracing warning.
- Lock expected inputs with `input_signature`, for example `@tf.function(input_signature=[tf.TensorSpec(shape=(None, 224, 224, 3), dtype=tf.float32)])`.
- Plain Python `int`/`float`/`bool` values become trace-time constants; pass tensors when the value should vary without retracing.
- Python side effects inside `tf.function` run at trace time. Keep them for tracing control only; use TensorFlow ops for per-call behavior.

## GPU Memory

- By default TensorFlow can reserve nearly all visible GPU memory up front.
- Before any GPU init, enable growth per device:

```python
gpus = tf.config.list_physical_devices("GPU")
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
```

- Still OOM with large models: lower batch size, enable gradient checkpointing, or shard work.
- Force CPU for isolation tests with `CUDA_VISIBLE_DEVICES=""`.

## Data Pipeline

- Missing `.prefetch()` leaves the accelerator idle between batches.
- `.cache()` after expensive deterministic maps, and usually **before** random augmentation.
- Prefer `.batch()` before vectorizable `.map()` work when the map can run on batches.
- Use `num_parallel_calls=tf.data.AUTOTUNE` and `prefetch(tf.data.AUTOTUNE)` so the runtime can tune parallelism.
- Pure-Python eager iteration over `tf.data` is slow; consume datasets inside `tf.function` or `model.fit`.

## Shape Issues

- Keras `Input` first dimension is batch — use `None` for variable batch size.
- Without an `Input` layer, call `model.build(input_shape)` (or run one forward) before weight-dependent ops.
- Unclear reshape failures: add `tf.debugging.assert_shapes` near the suspect site.
- Silent broadcasting can hide rank bugs; assert ranks when contracts matter.

## Gradient Tape

- Variables are watched by default; intermediate **tensors** need `tape.watch(tensor)`.
- Use `persistent=True` only when multiple `tape.gradient` calls are required on the same tape; delete the tape when finished.
- `tape.gradient(...) is None` usually means a disconnected graph path (wrong tensor, stopped gradient, or non-differentiable op).
- `@tf.custom_gradient` defines a custom backward when stock ops are insufficient.

## Training Gotchas

- `model.trainable = False` after `compile` does not retroactively rebuild the optimized step the way callers often expect — set freeze flags before compile when that graph must observe them.
- BatchNorm and Dropout differ in train vs inference; pass `training=True/False` through custom trains.
- `model.fit` shuffles training data by default — set `shuffle=False` for strict sequence order.
- `validation_split` takes a tail slice — shuffle first when order encodes bias.

## Saving Models

- Full `model.save` / SavedModel path keeps architecture, variables, and often optimizer state for resume/serve flows.
- `save_weights` stores weights only; restore needs matching model code.
- Prefer SavedModel for serving and custom objects.
- H5 is limited for custom object graphs; use SavedModel when those objects must round-trip.

## Common Mistakes

- Mixing raw TF ops into `Sequential` without `layers.Lambda` (or a custom layer) breaks the Keras graph contract.
- `print` inside `tf.function` runs at trace time; use `tf.print` for per-call values.
- NumPy ops inside a graph context execute only in eager paths — prefer TF ops in compiled functions.
- Custom training loops that forget `tf.reduce_mean` on per-example losses diverge from Keras' default averaging behavior.
