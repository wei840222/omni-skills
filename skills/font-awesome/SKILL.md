---
name: font-awesome
description: Add Font Awesome icons to web projects using CDN, npm, React, or SVG methods. Load this skill when the user needs to integrate, style, or search for icons in a web application.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🎨"}'
  related-skills: '{"react": "React development patterns", "html": "HTML best practices", "css": "CSS styling patterns"}'
---

## When to Load

- User needs to add icons to a web project (React, Vue, HTML).
- User wants to search for the correct Font Awesome icon name.
- User needs help with Font Awesome sizing, styling, or accessibility.

Load `references/setup.md` when first discussing icon integration methods with the user.
Load `assets/memory-template.md` only if the user expresses persistent preferences for icon styles or frameworks.

## Architecture

No persistent storage needed. Icon preferences tracked in user's main memory if requested.

## Quick Reference

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` |
| Memory template | `assets/memory-template.md` |

## Core Rules

### 1. Determine Installation Method First
Ask or infer the project setup before suggesting icons:

| Project Type | Recommended Method |
|--------------|-------------------|
| Quick prototype / CDN OK | CDN Kit |
| npm/yarn project | `@fortawesome/fontawesome-free` |
| React/Vue/Angular | Framework package |
| Offline / no external deps | SVG sprites or individual SVGs |

### 2. Use Correct Syntax Per Method

**CDN Kit (easiest):**
```html
<script src="https://kit.fontawesome.com/YOUR_KIT_ID.js" crossorigin="anonymous"></script>
<i class="fa-solid fa-house"></i>
```

**npm (fontawesome-free):**
```bash
npm install @fortawesome/fontawesome-free
```
```javascript
import '@fortawesome/fontawesome-free/css/all.min.css';
```
```html
<i class="fa-solid fa-user"></i>
```

**React:**
```bash
npm install @fortawesome/react-fontawesome @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons
```
```jsx
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHouse } from '@fortawesome/free-solid-svg-icons';

<FontAwesomeIcon icon={faHouse} />
```

### 3. Know the Icon Styles

| Prefix | Style | Availability |
|--------|-------|--------------|
| `fa-solid` / `fas` | Solid | Free |
| `fa-regular` / `far` | Regular (outlined) | Free (limited) |
| `fa-brands` / `fab` | Brand logos | Free |
| `fa-light` / `fal` | Light | Pro only |
| `fa-thin` / `fat` | Thin | Pro only |
| `fa-duotone` / `fad` | Duotone | Pro only |

### 4. Icon Search Strategy

When user asks for an icon:
1. Suggest semantic name first (e.g., `fa-envelope` for email)
2. Provide 2-3 alternatives if ambiguous
3. Specify style availability (free vs pro)

**Common mappings:**
| Concept | Icon | Style |
|---------|------|-------|
| Home | `fa-house` | solid, regular |
| User/Profile | `fa-user` | solid, regular |
| Settings | `fa-gear` | solid |
| Search | `fa-magnifying-glass` | solid |
| Menu | `fa-bars` | solid |
| Close | `fa-xmark` | solid |
| Edit | `fa-pen` | solid |
| Delete | `fa-trash` | solid |
| Save | `fa-floppy-disk` | solid, regular |
| Download | `fa-download` | solid |
| Upload | `fa-upload` | solid |
| Email | `fa-envelope` | solid, regular |
| Phone | `fa-phone` | solid |
| Location | `fa-location-dot` | solid |
| Calendar | `fa-calendar` | solid, regular |
| Clock | `fa-clock` | solid, regular |
| Check | `fa-check` | solid |
| Warning | `fa-triangle-exclamation` | solid |
| Info | `fa-circle-info` | solid |
| Error | `fa-circle-xmark` | solid |
| Success | `fa-circle-check` | solid |
| Arrow right | `fa-arrow-right` | solid |
| Chevron down | `fa-chevron-down` | solid |
| Plus | `fa-plus` | solid |
| Minus | `fa-minus` | solid |
| Star | `fa-star` | solid, regular |
| Heart | `fa-heart` | solid, regular |
| Cart | `fa-cart-shopping` | solid |
| GitHub | `fa-github` | brands |
| Twitter/X | `fa-x-twitter` | brands |
| LinkedIn | `fa-linkedin` | brands |
| Facebook | `fa-facebook` | brands |
| Instagram | `fa-instagram` | brands |
| YouTube | `fa-youtube` | brands |

### 5. Sizing and Styling

**Size classes:**
```html
<i class="fa-solid fa-house fa-xs"></i>   <!-- 0.75em -->
<i class="fa-solid fa-house fa-sm"></i>   <!-- 0.875em -->
<i class="fa-solid fa-house fa-lg"></i>   <!-- 1.25em -->
<i class="fa-solid fa-house fa-xl"></i>   <!-- 1.5em -->
<i class="fa-solid fa-house fa-2xl"></i>  <!-- 2em -->
```

**Fixed width (for alignment in lists):**
```html
<i class="fa-solid fa-house fa-fw"></i>
```

**Animation:**
```html
<i class="fa-solid fa-spinner fa-spin"></i>
<i class="fa-solid fa-heart fa-beat"></i>
<i class="fa-solid fa-bell fa-shake"></i>
```

**Rotation:**
```html
<i class="fa-solid fa-arrow-right fa-rotate-90"></i>
<i class="fa-solid fa-arrow-right fa-rotate-180"></i>
<i class="fa-solid fa-arrow-right fa-flip-horizontal"></i>
```

### 6. Accessibility

Always provide accessible labels:

```html
<!-- Decorative (hidden from screen readers) -->
<i class="fa-solid fa-house" aria-hidden="true"></i>

<!-- Meaningful (needs label) -->
<i class="fa-solid fa-trash" aria-label="Delete item"></i>

<!-- With visible text (icon is decorative) -->
<button>
  <i class="fa-solid fa-save" aria-hidden="true"></i>
  Save
</button>
```

### 7. Version Differences

**v6 (current):**
- Use `fa-solid`, `fa-regular`, `fa-brands`
- Icon names like `fa-house`, `fa-magnifying-glass`

**v5 (legacy):**
- Use `fas`, `far`, `fab`
- Some icon names changed (e.g., `fa-home` → `fa-house`)

If working with existing v5 code, maintain the current version unless the user requests an upgrade.

## Common Traps

- Using Pro icons in free tier → icons fail to render, no error
- Wrong prefix (`fa-solid` vs `fas`) → depends on version, check project
- Missing CSS import with npm → icons show as squares
- Using v5 names in v6 → some work while others fail (e.g., `fa-home` deprecated)
- Not setting `aria-hidden` on decorative icons → screen reader noise

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| kit.fontawesome.com | Kit ID only | Load icons via CDN |
| cdn.fontawesome.net | None | Alternative CDN |

No user data is sent. Icons loaded from public CDN.

## Security & Privacy

**Data that leaves your machine:**
- HTTP request to Font Awesome CDN (if using CDN method)

**Data that stays local:**
- All icon choices and code

**This skill does NOT:**
- Track icon usage
- Send analytics
- Require authentication for free tier
