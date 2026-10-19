---
name: keras
description: >
  Build, train, and debug deep learning models with Keras patterns, layer
  recipes, callbacks, and training diagnostics. Use when designing Sequential /
  Functional / subclassed models, fixing NaN loss or overfitting, choosing
  Keras 3 backends, or adapting architectures to JAX / TensorFlow / PyTorch
  constraints. Prefer `tensorflow` for tf.function, GPU OOM, tf.data, and
  SavedModel execution issues; prefer `pytorch` for pure torch training loops;
  prefer `models` / `ai` for LLM portfolio or live AI-product facts rather than
  neural-net training craft.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧠","requires":{"bins":["python3"]}}'
  related-skills: '{"tensorflow":"tf.function retracing, GPU memory growth, tf.data bottlenecks, GradientTape, and SavedModel export beyond high-level Keras APIs.","pytorch":"Pure PyTorch train/eval loops, device matching, and state_dict persistence when the stack is not Keras.","ai":"Live AI product, pricing, ranking, and outage facts instead of stale catalog memory.","models":"Task-to-model and cost-tier portfolio choices for LLMs rather than Keras neural-net training."}'
---

# Keras

High-level neural-network craft for Keras 3 (and `tf.keras` workflows that still
share the same APIs). This skill advises architecture, callbacks, and training
diagnostics; it does not upload models or call remote hubs without an explicit
user request.

Optional persistent notes live under a resolved `<state_root>/` tree outside
this package. Never write runtime state into the skill tree.

## State location

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/keras/`, `<workspace>/memory/keras/`, `~/keras/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and the user wants durable notes, create
   `<workspace>/keras/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the shell cwd.
5. Prefer portable `<state_root>` paths; never hard-code host-specific absolute
   roots. Skill resources stay under `references/` and `assets/`; never treat
   the literal string `<state_root>` as a filesystem path.

Persistent state is enabled only when the user explicitly requests retention or
approves a named persistent write.

```text
<state_root>/
|-- memory.md   # Preferred architectures, hyperparams, hardware notes
`-- models/     # Optional saved model config sketches (not training data)
```

## Setup

On first use, read `references/setup.md` for activation questions, consent
before storing preferences, and what belongs in `<state_root>/memory.md`.

## When to Use

Use this skill when the user is designing, training, or debugging deep learning
models with Keras: layer stacks, Functional graphs, residual blocks, callbacks,
loss/metric pairing, Keras 3 multi-backend constraints, or NaN/overfit/underfit
diagnostics.

Hand off when the work becomes stack-specific:

- `tf.function` retracing, GPU OOM, `tf.data` pipelines, SavedModel → `tensorflow`
- Pure PyTorch train/eval / `state_dict` loops → `pytorch`
- LLM portfolio / cost-tier routing → `models`
- Live AI prices, rankings, outages → `ai`

## When to load what

| Need | Load |
|------|------|
| First-run activation + consent | `references/setup.md` |
| Memory / status template shapes | `assets/data-templates.md` |
| Dense / Conv / RNN / attention recipes | `references/layers.md` |
| Loss plateau, overfit, NaN, LR finder | `references/training.md` |
| CNN / transfer / text CNN / residual sketches | `references/architectures.md` |
| Verified primary URLs (Gate 6) | `references/sources.md` |

Load `references/sources.md` before restating Keras 3 backend rules, deprecated
preprocessing APIs, or callback/optimizer field names as current facts.

## Core Rules

### 1. Sequential vs Functional vs Subclassing

- Sequential: simple stacks, no branching.
- Functional: multi-input/output, skip connections, shared layers.
- Subclassing: custom forward pass or dynamic architectures.

```python
# Sequential - simple stack
model = keras.Sequential([
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax"),
])

# Functional - flexible graphs
inputs = keras.Input(shape=(784,))
x = layers.Dense(64, activation="relu")(inputs)
outputs = layers.Dense(10, activation="softmax")(x)
model = keras.Model(inputs, outputs)
```

### 2. Input Shape Patterns

- First layer needs `input_shape` / `Input(...)` excluding the batch dimension.
- Images (`channels_last`): `(height, width, channels)`
- Sequences: `(timesteps, features)`
- Tabular: `(features,)`

```python
layers.Conv2D(32, 3, input_shape=(224, 224, 3))
layers.LSTM(64, input_shape=(100, 50))
layers.Dense(64, input_shape=(20,))
```

### 3. Activation / Loss Pairing

| Task | Output Activation | Loss |
|------|-------------------|------|
| Binary classification | `sigmoid` | `binary_crossentropy` |
| Multi-class | `softmax` | `categorical_crossentropy` (or `sparse_...`) |
| Multi-label | `sigmoid` | `binary_crossentropy` |
| Regression | `linear` (none) | `mse` or `mae` |

### 4. Regularization Stack

Apply in this order for overfitting:

1. Dropout after dense/conv blocks (0.2–0.5)
2. BatchNormalization (before or after activation; keep one convention)
3. L2 regularization on kernels (0.01–0.001)
4. EarlyStopping with `restore_best_weights=True`

```python
layers.Dense(64, activation="relu", kernel_regularizer=keras.regularizers.l2(0.01))
layers.Dropout(0.3)
layers.BatchNormalization()
```

### 5. Callbacks Essentials

```python
callbacks = [
    keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=5, restore_best_weights=True
    ),
    keras.callbacks.ModelCheckpoint(
        "best_model.keras", save_best_only=True
    ),
    keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss", factor=0.5, patience=3
    ),
    keras.callbacks.TensorBoard(log_dir="./logs"),
]
```

### 6. Data Pipeline

Prefer Keras 3 data loaders / `tf.data` over legacy generators:

```python
# Preferred: directory → batched dataset
train_ds = keras.utils.image_dataset_from_directory(
    "data/train",
    image_size=(224, 224),
    batch_size=32,
)
train_ds = train_ds.prefetch(tf.data.AUTOTUNE)

# Or build tf.data explicitly
dataset = tf.data.Dataset.from_tensor_slices((x, y))
dataset = dataset.shuffle(10_000).batch(32).prefetch(tf.data.AUTOTUNE)
```

Treat `ImageDataGenerator` as legacy TensorFlow Keras preprocessing. Prefer
`image_dataset_from_directory` plus Keras preprocessing layers for new work.

### 7. Compile Checklist

```python
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)
```

- Learning rate: start near `1e-3`, reduce on plateau.
- Batch size: 32–128 typical; larger batches smooth gradients but need LR retune.
- Always set `learning_rate=` (not the legacy `lr=` alias) in new code.

### 8. Keras 3 Multi-Backend

Keras 3 can run on JAX, TensorFlow, or PyTorch:

- Select backend with `KERAS_BACKEND` or `os.environ["KERAS_BACKEND"] = "jax"`
  **before** importing Keras.
- Prefer `keras.ops` over backend-specific math (`tf.math`, raw torch ops) in
  custom layers that must stay portable.
- For vision / NLP building blocks, prefer maintained `keras_cv` / `keras_nlp`
  components when they match the task.

## Common Traps

- `Input shape mismatch` → align data shape to `input_shape`, exclude batch dim,
  then re-run a one-batch `model.summary()` / dry forward.
- `Loss is NaN` → check inputs for NaN/Inf, lower LR, add `clipnorm` /
  `clipvalue`, and only then reconsider mixed precision.
- `Validation loss diverges` → add regularization, reduce capacity, or gather
  more data before changing the optimizer brand.
- `Model not learning` → verify label encoding matches the loss, confirm the
  metric/task pairing, and inspect a single-batch overfit test.
- `GPU OOM` → cut batch size, enable mixed precision carefully, or reduce
  resolution / sequence length before chasing exotic checkpointing.
- `Slow training` → ensure prefetch/AUTOTUNE, avoid Python loops in the step,
  and profile before enabling XLA as a first move.
- `Backend surprise` → confirm `KERAS_BACKEND` was set before import; do not
  assume TensorFlow ops work under JAX/PyTorch backends.
- `Legacy ImageDataGenerator` → migrate new pipelines to
  `image_dataset_from_directory` / preprocessing layers; keep generators only
  when maintaining an old stack.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| Keras / TensorFlow application weights (e.g. ImageNet) | None (download only) | Pretrained weights when `weights="imagenet"` |

Transfer-learning helpers download weights on first use. Pass `weights=None`
for fully offline construction.

## Security & Privacy

**Data that stays local:**

- Model architectures and preference notes under `<state_root>/`
- Hardware constraints and hyperparameters the user shared

**Boundaries:**

- Keep training runs and file access inside `<state_root>/` and the current
  working project unless the user names another path.
- Do not persist raw training corpora into skill state; keep those in the
  project's data directories.
- Do not upload models, datasets, or credentials without explicit approval.
