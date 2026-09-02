# Storybook reference

Use this reference when creating or reviewing Storybook configuration, stories, controls, decorators, documentation, or interaction tests.

## Create a CSF story

Use a default export for component metadata and named exports for states. In TypeScript, use `satisfies Meta<typeof Component>` so the meta and stories remain type-checked.

```ts
import type { Meta, StoryObj } from '@storybook/react-vite';
import { Button } from './Button';

const meta = {
  title: 'Components/Button',
  component: Button,
  args: { label: 'Save' },
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {};
export const Disabled: Story = { args: { disabled: true } };
```

Use object-style named exports for component states. Keep the title aligned with the project's existing sidebar hierarchy.

## Args, argTypes, and decorators

- Use `args` for the props passed to a story; meta-level args are defaults that individual stories may override.
- Use `argTypes` to control the Storybook UI, such as a select control for a bounded set of values or disabling a control for non-serializable content.
- Use decorators for providers, themes, layout wrappers, or other context shared by a component's stories. Render the supplied `Story` component inside the wrapper.

```ts
argTypes: {
  size: { control: 'select', options: ['sm', 'lg'] },
},
decorators: [(Story) => <ThemeProvider><Story /></ThemeProvider>],
```

## Interaction tests

Use a `play` function for behavior that should execute in the rendered canvas. Query within the supplied canvas and use the project's supported Storybook test utilities.

```ts
export const Submits: Story = {
  play: async ({ canvas, userEvent }) => {
    await userEvent.click(await canvas.findByRole('button', { name: 'Save' }));
  },
};
```

When an interaction test fails, first verify the rendered role and accessible name, then confirm the project uses APIs compatible with its installed Storybook version.

## Configuration and review checks

- Keep framework, stories globs, addons, and static assets in `.storybook/main.*`; place global decorators and parameters in `.storybook/preview.*`.
- Add an addon to the project dependency set and to the configured addons list before relying on it in a story.
- Prefer CSF named exports over the legacy `storiesOf` API.
- Give the default meta export a `component` when automatic controls or documentation depend on component inference.
- Model empty, loading, error, disabled, and responsive states as separate stories when they are meaningful user-visible states.
