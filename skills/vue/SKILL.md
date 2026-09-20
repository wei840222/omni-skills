---
name: vue
description: Build, debug, and optimize Vue 3 applications. Load this skill to resolve
  reactivity loss, component communication issues, SSR hydration mismatches, Pinia
  state warnings, and configuration problems.
metadata:
  openclaw: '{"requires": {"config": ["<state_root>/data/vue/", "<state_root>/vue/",
    "<state_root>/clawic/vue/"]}}'
  related-skills:
    nuxt: Nuxt.js SSR and server logic
    vite: Vite build and configuration
    typescript: Type system design
    javascript: JavaScript semantics
    playwright: End-to-end tests
---
## When to load references
This skill supports deep expertise in Vue 3. When encountering specific issues, load the corresponding reference document:

- **Component communication & structure**: Load `references/components.md` and `references/sfc.md`.
- **Reactivity issues**: Load `references/reactivity.md`.
- **State management**: Load `references/state.md`.
- **Routing & navigation**: Load `references/routing.md`.
- **Composables & lifecycle**: Load `references/composables.md`.
- **Forms & v-model**: Load `references/forms.md`.
- **Performance**: Load `references/performance.md`.
- **Testing**: Load `references/testing.md`.
- **SSR & Hydration**: Load `references/ssr.md`.
- **TypeScript integration**: Load `references/typescript.md`.
- **Security & XSS**: Load `references/security.md`.
- **Migration from Vue 2**: Load `references/migration.md`.
- **Debugging & Error Handling**: Load `references/debug.md` and `references/errors.md`.
- **Setup & Plugins**: Load `references/setup.md` and `references/plugins.md`.
- **Templates & Slots**: Load `references/templates.md`.

## Output Gates

Before emitting a component, composable, or store, verify:

- Every reactive source crossing a function boundary is a ref or a getter, ensuring it is a reactive reference.
- Each `v-for` has a stable identity `:key`, and no `v-if` on the same element.
- Watchers and listeners created outside synchronous setup have a cleanup handle or an `effectScope`.
- Props are treated as read-only; every mutation routed through an emit or a model.
- Any class instance or third-party object is wrapped in `markRaw`/`shallowRef`.
- No user-controlled string reaching `v-html`, `:is`, or `:href` (`security.md`).
- Every async region has a loading, an error, and an empty state, and something above it catches a throw.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/data/vue/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| vue_version | 3.2 \| 3.3 \| 3.4 \| 3.5 \| later | 3.5 | Gates which macros and APIs get recommended. |
| api_style | script-setup \| setup-function \| options | script-setup | Shapes every code sample and the target style. |
| language | ts \| js | ts | Whether examples carry type annotations. |
| state_library | pinia \| vuex \| none | pinia | Selects the store patterns. |
| rendering_mode | spa \| ssr \| ssg | spa | Turns on SSR-safety review. |
| virtualize_threshold | number (rows) | 200 | Row count above which virtual scrolling is recommended. |
| test_runner | vitest \| jest \| none | vitest | Shapes the setup and mocking examples. |
