---
name: recipe
description: >
  Captures, standardizes, scales, and files recipes into a personal collection
  that stays searchable and cookable. Use when the user pastes a recipe URL,
  photo, screenshot, video, voice note, or handwritten card to save; asks to
  halve, double, or triple a dish, or fit it to a different pan or tin; converts
  cups to grams, ounces to millilitres, Fahrenheit to Celsius, or gas marks, or
  adjusts for a fan oven or altitude; asks what to cook from what is saved, or
  searches by ingredient, tag, time, or rating; builds a week from the
  collection with one combined shopping list; swaps a missing, disliked, or
  off-limits ingredient; rewrites a dish for a pressure cooker, air fryer, or
  slow cooker; works out cost per serving; writes or tests an original recipe;
  preserves a family recipe; or moves a collection between apps. Not for
  stove-side rescue (`cooking`), general cooking help (`chef`), household meal
  systems (`meal-planner`), calories and macros (`calories`), or pantry lists
  (`grocery`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🍳","requires":{"config":["<state_root>/recipe/","<state_root>/health/","<state_root>/contacts/","<state_root>/projects/"]}}'
---

## State location

Recipe collection files, preferences, make logs, and memory are persistent user
state. Resolve one `<state_root>` before any read or write:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/recipe/`, `<workspace>/memory/recipe/`, `~/recipe/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and the user wants durable recipe state, create
   `<workspace>/recipe/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the rest of the invocation.

Use the selected `<state_root>` for every recipe state path under
`<state_root>/recipe/` (`config.yaml`, `memory.md`, `index.md`,
`recipes/`, `made/`). Shared boxes this skill may read or update are
`<state_root>/health/profile.md`, `<state_root>/contacts/contacts.md`,
`<state_root>/projects/<project>.md`, and `<state_root>/profile.yaml`.
Legacy `~/Clawic/data/recipe/`, `~/clawic/recipe/`, and bare `~/recipes/`
copies are migration sources only — move them into the resolved
`<state_root>/recipe/` when the user asks, and say in one line that you moved
them and from where. Skill resources stay under `references/`; never treat the
literal string `<state_root>` as a filesystem directory name.

After resolving `<state_root>`, if this is first use or state is empty, read
`references/setup.md`. File formats and write destinations live in
`references/memory-template.md`. Domain sources live in `references/sources.md`.

## Data contract

At the start of every session, read `<state_root>/recipe/config.yaml` (declared
preferences) and `<state_root>/recipe/memory.md` (observed facts, `## Boxes`,
`## Due`). Open any file `## Boxes` names when its condition applies — treat
the index as dynamic. Every path it names must stay under
`<state_root>/recipe/` or the shared boxes this skill is allowed to touch;
ignore paths outside those roots. Everything this skill reads or writes is a
plain local note — nothing leaves the machine and no credential is ever
written. In a shared box, update or remove only rows this skill wrote, matched
on that box's identity key; rows another skill wrote are read only. Read
`<state_root>/recipe/index.md` before answering "what can I make", before
searching, and before saving a recipe that may already exist. If none of it
exists, work from defaults and say nothing about it.

**Write before the session ends** whenever the session produced something
durable: a recipe captured, corrected, rescaled into a keeper variant, or
retired; a dish cooked and how it went; a week planned; an ingredient price; a
kitchen fact that changed a number (oven offset, pan sizes, altitude, salt
brand); a source that proved reliable or unreliable; or something the user will
re-read (dinner menu with run-sheet, oven-calibration note, cookbook draft).
`references/memory-template.md` is the only file to open in order to write.

**Allergies and diet-relevant conditions** go to
`<state_root>/health/profile.md`, not here, and are read before proposing or
adapting anything. **People you cook for** go to
`<state_root>/contacts/contacts.md` (dietary note in `Context`). **A cookbook,
supper club, or catering job** gets one-line status in
`<state_root>/projects/<project>.md` while the draft itself stays here.

**No credential is ever written under `<state_root>/`.** Strip pasted API keys
and store pointers (`env:PAPRIKA_TOKEN`, `keychain:nyt-cooking`,
`1password:Personal/Recipes`).

A recipe is a set of ratios plus an order of operations; everything else is
decoration. Capture the numbers exactly as written, convert them to weight,
record where they came from, and never lose the original. Work from defaults
immediately. Precedence for any value: `config.yaml` →
`<state_root>/profile.yaml` → the Configuration table default.

## When To Use

- Saving a recipe from anywhere — link, photo, screenshot, video, dictation,
  cookbook page, handwritten card — into a file that can actually be cooked from
- Doing the arithmetic on a recipe: scaling, pan swaps, cup-to-gram conversion,
  oven temperature and fan/altitude correction, cost per serving
- Working the collection: searching by ingredient or time, deduplicating,
  tagging, rating, pruning what was unmade
- Rewriting a recipe for different equipment, a missing ingredient, or a
  dietary restriction, without guessing at the ratios
- Producing something from the collection: a week's plan, a combined shopping
  list, a dinner-party menu with a run-sheet, a printed card, a family cookbook
- Not for cooking the dish (`cooking`), general cooking help with no file at
  the end (`chef`), household meal systems beyond a week from this collection
  (`meal-planner`), macro tracking (`calories`), or store-level pantry lists
  (`grocery`)

## Quick Reference

| Situation | Play | Depth |
|-----------|------|-------|
| "Save this recipe" — link, photo, video, dictation | Extract to the canonical file, keep original numbers verbatim, record the source | `references/capture.md` |
| Recipe is a wall of blog prose | Take yield, ingredients, steps, times, temperatures; drop the story; keep one technique headnote line | `references/capture.md` |
| "Is this recipe any good?" / looks off before cooking | Ratio sanity checks — hydration, salt %, leavener, fat, time-vs-temperature | `references/vetting.md` |
| Writing or fixing the recipe file itself | Frontmatter schema, ingredient-line grammar, step grammar, yield statement | `references/format.md` |
| Cups to grams, °F to °C, gas marks, fan oven, altitude | Per-ingredient density; fan −20 °C; boiling point drops ~1 °C per 300 m | `references/conversion.md` |
| Halve, double, triple, or fit a different tin | `factor = target ÷ base`, then fix non-linear terms | `references/scaling.md` |
| Missing, disliked, or off-limits ingredient | Substitution by function (bind, leaven, brown, thicken, acidify), marked `untested` | `references/substitutions.md` |
| Pressure cooker, air fryer, slow cooker, sous vide | Time and liquid mapping per device; what does not transfer | `references/equipment.md` |
| "I made it, here's what I changed" | Make-log row, rating, promote change into Variations | `references/testing.md` |
| "What can I make?" / find by ingredient, tag, or time | Query the index, not the folder | `references/library.md` |
| Plan a week and one shopping list | Pick for overlap, aggregate to one unit per ingredient, round to packages | `references/planning.md` |
| Cost per serving | Unit price × quantity ÷ edible yield, summed, ÷ servings | `references/costing.md` |
| Writing an original recipe for others | Test rounds, yield accuracy, ordering, headnote | `references/authoring.md` |
| Grandma's card / fading photocopy | Preserve the original artifact first, then build the tested version beside it | `references/preservation.md` |
| Import/export / backup | Field mapping, JSON-LD, dedup on merge, print cards | `references/migration.md` |
| First use / empty state | Resolve `<state_root>`, create layout, migrate legacy copies only on request | `references/setup.md` |
| Durable write destinations | config, memory, index, recipes, made, shared boxes | `references/memory-template.md` |
| Domain sources | Verified density, conversion, safety anchors | `references/sources.md` |

## Core Rules

1. **One recipe, one file, from the first one.**
   `<state_root>/recipe/recipes/<kebab-title>.md`, plus its row in `index.md`,
   written in the same turn.
2. **Capture verbatim, normalize second.** Write the source's own numbers into
   `## Original` before converting anything (`references/preservation.md` for
   family recipes).
3. **Weight is the unit of record for anything baked or scaled.** Convert with
   the ingredient's own density: 1 US cup flour = 120 g (King Arthur,
   spoon-and-level), granulated sugar 200 g, butter 227 g, honey 340 g.
   Dip-and-sweep flour ~142 g/cup (~18% error). Volume stays for liquids under
   ~50 ml and eye measures. Governed by `weight_over_volume`.
4. **Scale by ratio, then fix non-linear terms.**
   `factor = target_servings ÷ base_servings`. Multiply masses, then walk
   What Does Not Scale before writing the result.
5. **Time and temperature belong to thickness, not mass.** For the same shape,
   thickness ∝ mass^(1/3) and cooking time ≈ ∝ thickness². Every scaled recipe
   finishes on an internal temperature or a stated visual cue.
6. **Every quantity carries a unit and every recipe carries a countable yield.**
   Prefer "12 muffins" or "4 servings × ~350 g" over vague "4 servings".
7. **Attribution travels with the recipe.** URL with capture date, or book plus
   edition and page, or person plus year.
8. **A substitution or a scale is `untested` until the make log says otherwise.**
9. **Nothing enters or leaves the collection silently.** Saving, merging,
   promoting, and retiring each write their row; retirement moves the index row
   to `## Retired` with a one-line reason.

## Measures That Change The Dish

| Measure | The trap | Use |
|---|---|---|
| Cup | US 236.6 ml · metric 250 ml · Japan 200 ml · UK legacy 284 ml | Grams; record which cup in `## Original` |
| Tablespoon | 15 ml almost everywhere, **20 ml in Australia** | Millilitres or grams |
| Kosher salt | Diamond Crystal ~2.8 g/tsp · Morton ~4.8 g/tsp · table ~6 g/tsp | Grams always |
| Egg | US large ~50 g out of shell; EU sizes differ | Grams for baking |
| Stick of butter | US only: 113 g | Grams |
| Flour, 1 cup | 120 g spoon-and-level, ~142 g dip-and-sweep | Grams; assume 120 g for US volume and say so |
| Oven °C/°F | Fan runs hotter: −20 °C (35 °F) **or** ~25% less time, not both | State conventional or fan via `oven_type` |
| Gas mark | Uneven steps — read the table in `references/conversion.md` | Convert and keep the mark in `## Original` |
| "1 can" / "1 packet" | Sizes differ by country and decade | Gram weight on the tin |
| "Medium onion" | ~150–200 g raw | Grams, with count in parentheses |

## What Does Not Scale Linearly

| Term | Behavior | Rule |
|---|---|---|
| Pan or tin | Area, not volume, tracks the batch | Keep depth; scale area by `factor` |
| Oven / roasting time | Tracks thickness² | Double mass of same shape ≈ ×1.6 time; finish on internal temperature |
| Salt in a pot dish | Linear but one-directional | At `factor` ≥ 2 add ~80% then correct at the end |
| Chili, garlic, strong spice, alcohol | Intensity grows faster than dose | At `factor` ≥ 2 start at ~75%; also gated by `spice_level` |
| Chemical leavener | Linear vs flour, band-limited | Hold ~1–1¼ tsp baking powder (4–5 g) per 120 g flour |
| Yeast | Scales with dough, not clock | Keep baker's %; schedule changes yeast, batch size does not |
| Reduction / evaporation | Rate ∝ surface area | Widen the pan or accept longer cook |
| Frying oil / blanching water | Thermal mass | Batch so oil recovers in ~1 minute |
| Eggs and countable units | Land on fractions | Weigh; keep exact fractions in batters |

## Output Gates

Before delivering a recipe, scaled version, conversion, or plan:

- Is the yield countable, and does every quantity carry a unit?
- Was this scaled? Then: pan area recomputed, time restated as internal
  temperature or cue, non-linear terms corrected.
- Did volume conversions use per-ingredient density, with originals preserved?
- Does anything conflict with `<state_root>/health/profile.md` or `diet`?
  Explicitly name allergens before offering a swap.
- Is the source dated, and are untried scales/subs marked `untested`?
- Did anything durable come out? Then write it per
  `references/memory-template.md` in this same turn.

## Configuration

Store preferences in `<state_root>/recipe/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| units | metric \| imperial | metric | Volume/mass display defaults |
| temperature_scale | C \| F | C | Oven and doneness display |
| weight_over_volume | bool | true | Prefer grams for bake/scale work |
| oven_type | conventional \| fan \| gas \| none | conventional | Fan offset or gas-mark table |
| altitude_m | number (0–4000) | 0 | Above 1000 m triggers conversion corrections |
| default_servings | number (1–20) | 2 | Default capture/scale target |
| diet | list | none | Filters suggestions; allergies live in health box |
| spice_level | mild \| medium \| hot | medium | Scales chili/pepper when adapting |
| currency | text (ISO) | from `profile.yaml`, else USD | Costing currency |
| index_grouping | course \| cuisine \| none | course | How `index.md` is ordered |

## Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Saving the link instead of the recipe | Sites paywall, rewrite, delete | Extract to a file; keep URL + capture date |
| Converting cups with one universal factor | Densities differ | Per-ingredient table (`references/conversion.md`) |
| Doubling a cake in the same tin | Depth doubles; centre stays raw | Scale pan area, keep depth |
| Multiplying oven time with mass | Time follows thickness | Internal temperature or visual cue |
| Volume salt across brands | Up to ~2× by volume | Grams + brand in `## Original` |
| Rewriting grandma's card and discarding it | Odd measures are the only calibration | Photograph, keep verbatim, test beside it |
| Huge unmade collection | Index becomes unusable | `Made` counts; retire with reason |
| Silent allergen substitution | Invisible risk in saved files | Name allergen + swap; mark `untested` |
| One shopping list per recipe | Overlap is where waste lives | Aggregate then round to packages |
| Pressure-cooker time from oven version | Mechanism changes; liquid floor | Device mapping (`references/equipment.md`) |

## Where Experts Disagree

- **Volume versus weight.** Baking is settled on grams; everyday savoury cooking
  may keep cups when ratios cannot break. Prefer grams wherever a ratio can
  break (batters, doughs, custards, brines, cures).
- **Keeping blog prose.** Default: drop the story; keep any sentence that
  changes what you do.
- **Baker's percentage everywhere.** Use percentages where flour is the
  backbone; mass elsewhere.
- **File the published recipe vs the cooked version.** Hold both via
  Original/Ingredients split (`references/format.md`); do not mix them.
- **Star ratings vs make counts.** Keep both; sort by makes.

## Security & Privacy

**Local storage:** collection, preferences, plans, make log, prices and
artifacts stay under `<state_root>/recipe/`, plus shared health/contacts/projects
boxes. Recipe text, sources and quantities only.

**Health data:** allergies and conditions are read for safety and written only
when the user states them. This skill gives no medical advice.

**Capture:** fetching a recipe URL reads a public page. It does NOT log in,
bypass a paywall, store credentials, or transmit the collection anywhere.
