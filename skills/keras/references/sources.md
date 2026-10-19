# Sources — Keras

Live-checked on 2026-10-19. Prefer these URLs over memorized API facts. Re-check
before quoting backend selection rules, deprecated preprocessing APIs, or
optimizer/callback field names.

## Agent Skills / packaging

| Claim topic | Source | Checked |
|-------------|--------|---------|
| Agent Skills specification | https://agentskills.io/specification | HTTP 200 |
| Agent Skills llms.txt | https://agentskills.io/llms.txt | HTTP 200 |

## Keras 3 core

| Claim topic | Source | Checked |
|-------------|--------|---------|
| Keras 3 overview / multi-backend | https://keras.io/keras_3/ | HTTP 200 |
| Migrating to Keras 3 | https://keras.io/guides/migrating_to_keras_3/ | HTTP 200 |
| Getting started | https://keras.io/getting_started/ | HTTP 200 |
| Intro for engineers | https://keras.io/getting_started/intro_to_keras_for_engineers/ | HTTP 200 |
| Functional API | https://keras.io/guides/functional_api/ | HTTP 200 |
| New layers / models via subclassing | https://keras.io/guides/making_new_layers_and_models_via_subclassing/ | HTTP 200 |
| Model training APIs | https://keras.io/api/models/model_training_apis/ | HTTP 200 |
| `keras.ops` API | https://keras.io/api/ops/ | HTTP 200 |

## Data loading and preprocessing

| Claim topic | Source | Checked |
|-------------|--------|---------|
| Keras data loading (`image_dataset_from_directory`, etc.) | https://keras.io/api/data_loading/ | HTTP 200 |
| Preprocessing layers | https://keras.io/api/layers/preprocessing_layers/ | HTTP 200 |
| Legacy `ImageDataGenerator` (TensorFlow docs; marked deprecated) | https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator | HTTP 200 |
| Image classification from scratch example | https://keras.io/examples/vision/image_classification_from_scratch/ | HTTP 200 |

## Layers, optimizers, callbacks

| Claim topic | Source | Checked |
|-------------|--------|---------|
| Dense layer | https://keras.io/api/layers/core_layers/dense/ | HTTP 200 |
| Conv2D | https://keras.io/api/layers/convolution_layers/convolution2d/ | HTTP 200 |
| Optimizers overview | https://keras.io/api/optimizers/ | HTTP 200 |
| Adam (`learning_rate`) | https://keras.io/api/optimizers/adam/ | HTTP 200 |
| EarlyStopping | https://keras.io/api/callbacks/early_stopping/ | HTTP 200 |
| ModelCheckpoint | https://keras.io/api/callbacks/model_checkpoint/ | HTTP 200 |
| ReduceLROnPlateau | https://keras.io/api/callbacks/reduce_lr_on_plateau/ | HTTP 200 |
| Writing your own callbacks | https://keras.io/guides/writing_your_own_callbacks/ | HTTP 200 |
| Custom train step (TensorFlow) | https://keras.io/guides/custom_train_step_in_tensorflow/ | HTTP 200 |

## Domain packages

| Claim topic | Source | Checked |
|-------------|--------|---------|
| KerasCV | https://keras.io/keras_cv/ | HTTP 200 |
| KerasNLP | https://keras.io/keras_nlp/ | HTTP 200 |

## Unreachable / moved from this runner

| Attempted source | Result | Handling |
|------------------|--------|----------|
| https://keras.io/guides/writing_a_training_loop_from_scratch/ | HTTP 404 | Do not cite; use Model training APIs + custom train-step guides instead. |
| https://keras.io/guides/customizing_what_happens_in_fit/ | HTTP 404 | Do not cite; use `custom_train_step_in_tensorflow` when a custom step is required. |

## Claim checklist

Before stating a Keras API fact in answers or PRs:

1. Open the matching URL above (or a newer official replacement).
2. Quote only what the live page supports (backend env var, API names, deprecation).
3. If the page is unreachable, say so and keep guidance at the portable `keras.*` layer.
