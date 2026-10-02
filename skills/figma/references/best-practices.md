# Figma Best Practices

## Output Gates

Before marking frames Ready for dev or publishing a library, verify:

- Every delivered frame survives a full-width drag sweep and the longest realistic string without clipping or overlap?
- Zero layers named `Frame N`, `Group N`, `Rectangle N`, or `Ellipse N` anywhere in the delivered tree?
- Sad paths present: empty, loading, error, disabled, missing image?
- Colors, spacing and radii bound to variables — no raw hex and no typed px inside delivered components?
- Contrast checked on the bound values in every mode that ships, not only in Light?
- A breaking library change versioned rather than edited in place, with a release note naming what moved?


## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Detaching an instance to get a variant that does not exist | The library link is gone for good; the missing variant never returns to the source | Add the variant or a property; detach only for one-off artwork that will never update |
| `Accept all` on a library update | A restructured main rewires overrides across every consuming file at once, silently | Review per component; open one real consuming screen before accepting a structural change |
| Duplicating frames for dark mode | Two trees drift within a sprint and every fix has to land twice | One tree, a second mode on the color collection |
| Fixed height on a text container | Localization and long strings clip with no warning on the canvas | Auto height on the text node, Hug on the parent, tested against the longest realistic string |
| Tuning constraints inside an auto layout frame | Inert except on absolutely-positioned children — the control does nothing | Fix the sizing modes; use absolute position when out-of-flow is genuinely wanted |
| `Lorem ipsum` in a mock | Hides the real length distribution; the layout breaks the day real copy arrives | Real or realistic copy plus the longest string the field permits |
| Pasting codegen output into production | px values, absolute positioning, and class names with no relationship to the codebase | Read the structure (auto layout maps to flex), rewrite against the codebase's own tokens |
| A personal access token inside a plugin bundle or a repo | Plugin bundles are readable by anyone who installs them; repo history keeps the token after deletion | Server-side proxy, scoped tokens, rotate the moment one is exposed |
| One mega-library for the whole org | Every linked file pays its load cost and every edit has org-wide blast radius | Foundations library plus one per product surface |
| Flattening an icon to "clean it up" | Loses the editable path and usually the ability to recolor | Keep the editable copy on a hidden `_source` page; flatten only decorative raster |
| Naming pages and files for the author, not the reader | The cover is the thumbnail in recents; a file nobody can identify is a file that gets duplicated | Cover page first, then `Components`, then `Screens`, `Archive` last |


## Where Experts Disagree

- **Styles vs variables-first.** New files go variables-first; teams mid-migration legitimately run both. The frontier is the coverage gap — where gradients, effects and full text-style binding are not covered by variables, a styles layer still wins. Migrating a large styles-only file is a project, not a refactor.
- **Mega-library vs federated.** Mega wins on consistency below roughly two consuming teams; past that it loses hard on load time and blast radius. The trigger to federate is a second team that needs a different release cadence, not file size.
- **Variants for every state vs separate components.** Variants win when the states share anatomy and the set stays browsable; separate components win when a "state" is really a different object with different content slots. The line is shared anatomy and set size, not taste.
- **Trust codegen vs hand-spec.** Trust generated output for layout structure and token names; never for raw px or absolutely-positioned geometry. Code Connect moves the boundary: mapped components generate real component calls, unmapped ones generate divs.
- **Design in Figma vs design in code.** Figma wins on exploration breadth and stakeholder legibility; the browser wins the moment the artifact must survive real data, real content lengths, and real device behavior. Teams that ship design-system work increasingly validate in code and keep Figma as the shared map — the split is about where the decision is verified, not about tooling loyalty.


## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| figma_plan | starter \| professional \| organization \| enterprise | professional | Resolves every plan-gated recommendation before proposing it: mode count per collection, branching, Dev Mode seats, library analytics, Variables REST API |
| spacing_base | number (px, 2-8) | 8 | The unit every padding, gap and radius number variable snaps to; dense UI uses `spacing_base / 2` as the half-step |
| target_platforms | list (web, ios, android, desktop) | web | Selects export densities, touch-target minimums, safe-area rules and the naming used in platform specs |
| token_pipeline | native \| tokens-studio \| code-connect \| none | native | Chooses the variables-to-code route and what the handoff deliverable has to contain |
| component_naming | slash \| flat | slash | Whether component names build an assets-panel hierarchy (`Button / Primary / Large`) or stay single-segment |
| icon_grid | number (px) | 24 | Frame size for icon sets; the live area is `icon_grid − 4` and stroke weight scales from it |
| library_model | mono \| federated | federated | Whether guidance assumes one library file or a foundations library plus one per product surface |

Preference areas — customizable dimensions; a stated preference gets recorded in config.yaml and applied:

- **Tooling** — desktop app vs browser, plugin appetite (native-only vs plugin-heavy), whether the Dev Mode MCP server or the REST API is reachable from the agent
- **Conventions** — variable naming scheme, page order and cover format, layer-naming style, branch and version-naming — affects every naming recommendation
- **Platform** — density set, locale and RTL coverage, which modes ship (dark, high-contrast, compact), minimum supported viewport
- **Safety posture** — confirm before publishing a library, detaching an instance, flattening, or deleting a page; how loudly to flag a breaking change
- **Output format** — spec verbosity (annotate everything vs annotate deviations only), and whether the deliverable is a file, a written spec, or generated code
- **Work order** — tokens-first vs screens-first, when Ready for dev gets applied, whether accessibility is checked per screen or in one pass
- **Integrations** — Storybook, Jira or Linear, GitHub, Slack, Style Dictionary, Tokens Studio: which the handoff must feed
- **Restrictions** — banned plugins on enterprise files, fonts licensed for the org, compliance regimes that forbid third-party file access
- **Cadence** — library release rhythm, design review schedule, how often the unused-component and detached-instance audit runs
