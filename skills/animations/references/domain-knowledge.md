# Web Animations Domain Knowledge

## CSS Animations

CSS Animations is a module for Cascading Style Sheets that allows the animation of HTML document elements using CSS. As early as 2007, WebKit had announced its intent to include CSS animation, transitions, and transforms as features of WebKit. It was later adopted across browsers and put forth as a feature of CSS3, managed by the W3C.

Source: https://en.wikipedia.org/wiki/CSS_animations

## Reduced Motion (prefers-reduced-motion)

The `prefers-reduced-motion` CSS media feature is used to detect if the user has requested that the system minimize the amount of non-essential motion it uses. Users with vestibular disorders can experience nausea and dizziness from large movements on screen, so providing an alternative is a critical accessibility best practice.

Source: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion

## GPU Compositing

Modern web browsers use the GPU to accelerate certain CSS operations, which offloads processing from the main thread. Specifically, animating `transform` and `opacity` properties can be handled directly by the compositor thread, leading to 60fps animations without causing layout thrashing or repaints, unlike animating properties like `width`, `top`, or `margin`.

Source: https://developer.mozilla.org/en-US/docs/Learn/Performance/CSS
