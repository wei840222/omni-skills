# The inventory

A debt register is a living doc, not tickets scattered among features. The #1 maintains one; the #1000 keeps debt "in our heads."

- One row per item: **id, area, type, interest (L/M/H), blast radius (local/structural), payoff cost (S/M/L), trigger, owner.** That is the minimum that prioritizes; less is noise, more rots.
- The **trigger** is the load-bearing field: "pay when we next touch auth," "pay when the dependency goes EOL," "pay when cycle time in this module > X." An item without a trigger is a wish; it will never be prioritized.
- TODOs are not inventory. A TODO is a wish; a register item with a trigger is a commitment. Auditing TODOs produces noise; auditing register items produces decisions.
- Tag debt items in the tracker with a `debt` label AND keep the aggregate register. Tracker-only scatters debt among features and hides it; register-only rots because engineers do not live there. Both: tickets for execution, register for the view.
- A register nobody triages is worse than none: it grows, demoralizes, and is never the source of a real decision. Prune monthly to quarterly: close paid items, re-rate interest, delete items whose code was deleted. An item that survives three prunes unpaid is mis-rated or has no real trigger.
- An empty register means the register is broken, not that there is no debt. Run a "debt wall" session: each engineer adds the items they route around daily. Zero debt = invisible, not absent.
- The register is the week-1 onboarding map: it tells a new hire where the bodies are and which decisions were deliberate. Withholding it makes every new engineer re-learn the traps by stepping in them.
