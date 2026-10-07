# Units of Measurement - Instacart

Use documented units when specifying ingredients or line items. Multiple
measurements are allowed via a Measurement array (for example one liter and
32 fluid ounces for broth). Put the preferred measurement first.

## Common measured units

Examples from Instacart Developer Platform docs (non-exhaustive):

| Unit family | Example forms | Typical products |
|-------------|---------------|------------------|
| Volume (US kitchen) | cup, cups, c | cream, oats, walnuts |
| Fluid ounces | fl oz, fl oz can/jar/container/pouch | soups, oils, baby food |
| Mass (avoirdupois) | ounce, oz, pound, lb | milk, produce by weight |
| Larger volume | gallon, gal, milliliter, litre, liter | milk, water, broth |
| Countable | each, bunch, head, loaf, pack, bag | bananas, lettuce, bread |

## Rules

- Prefer `each` for countable products when quantity is a simple count.
- Reject zero or negative quantities before sending traffic.
- Unsupported or vague units often produce a product match without a useful quantity.
- Normalize aliases before caching (`gal` → `gallon`, `lbs` → `lb` when that is the documented form you standardize on).

Authoritative list: Instacart Developer Platform → API reference → Units of measurement.
