# Examples — Frontend

## Landing Page

**Prompt:**
```
Build a SaaS landing page for an AI writing tool.
Dark theme, editorial typography. Sections: hero
with animated demo, features grid, pricing table,
FAQ accordion, footer with newsletter signup.
```

**Design choices:**
- Tone: Editorial/Magazine
- Font: Cabinet Grotesk (display) + Plus Jakarta Sans (body)
- Color: Near-black bg (#0c0c0c), warm white text, accent copper
- Memorable: Full-bleed hero with scroll-reveal text

## Dashboard

**Prompt:**
```
Create an analytics dashboard. Sidebar navigation,
header with search and user menu. Main area: stats
cards row, line chart, data table with pagination.
Light theme, clean and professional.
```

**Design choices:**
- Tone: Utilitarian/Clean
- Layout: 240px fixed sidebar, fluid main
- Components: shadcn/ui cards, Recharts for graphs
- Data table: TanStack Table with sorting/filtering

For dashboard IA beyond generic layout, also load `dashboard`.

## Checkout Form

**Prompt:**
```
Build a multi-step checkout form. Steps: cart review,
shipping address, payment method, confirmation.
Progress indicator, back/next navigation, form
validation with inline errors.
```

**Design choices:**
- Stepped progress bar at top
- React Hook Form + Zod for validation
- Preserve all input on navigation and failed submits
- Optimistic feedback only when rollback is defined

For specialized field UX and recovery paths, also load `forms`.

## Pre-Implementation Checklist

- [ ] Typography distinctive (not Inter/Roboto as hero)
- [ ] Color follows 70-20-10
- [ ] Background has depth
- [ ] One memorable element
- [ ] Mobile-first responsive
- [ ] Focus states visible
- [ ] Loading states for async work
- [ ] Error recovery preserves input
- [ ] LCP/CLS targets considered (https://web.dev/articles/vitals)
