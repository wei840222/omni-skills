# Sources - TensorFlow Skill

Last checked: 2026-09-30

Primary references used to verify gotchas in this package. Prefer the live guide over memorized snippets.

## Official TensorFlow guides

- GPU guide — memory growth and device configuration via https://www.tensorflow.org/guide/gpu
- Better performance with tf.function — tracing, retracing, and `input_signature` via https://www.tensorflow.org/guide/function
- Better performance with tf.data — `prefetch`, `cache`, `AUTOTUNE`, and pipeline design via https://www.tensorflow.org/guide/data_performance
- Introduction to gradients and automatic differentiation — `GradientTape`, watching tensors, `persistent` tapes via https://www.tensorflow.org/guide/autodiff
- Using the SavedModel format — export/load and serving-oriented persistence via https://www.tensorflow.org/guide/saved_model

## Verification note

HTTP status for each URL above was checked reachable (200) during this refactor. Re-open the live guide before asserting version-specific API renames or defaults.
