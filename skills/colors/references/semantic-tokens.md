# Semantic Color Tokens

Keep three layers. Name each token by role, not by the hue it happens to use today.

```css
/* Layer 1: primitives (raw values) */
--blue-500: #1d4ed8;
--gray-900: #111827;
--red-600: #dc2626;

/* Layer 2: semantic roles */
--color-primary: var(--blue-500);
--color-text: var(--gray-900);
--color-error: var(--red-600);

/* Layer 3: component use */
--btn-primary-bg: var(--color-primary);
--input-border-error: var(--color-error);
```

`text-primary` stays correct if the brand hue changes. `text-blue` does not.

The DTCG format (designtokens.org, 2025.10) is the portable export shape when a token file must leave the stylesheet. Inside CSS, the three custom-property layers above are enough.

## HSL scales

Hold hue and saturation, then step lightness:

```css
--primary-100: hsl(220 90% 95%);
--primary-300: hsl(220 90% 75%);
--primary-500: hsl(220 90% 55%);
--primary-700: hsl(220 90% 35%);
--primary-900: hsl(220 90% 15%);
```

Check the contrast of the pair you will actually ship. A scale step is not a contrast pass.
