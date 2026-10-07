# Common Traps - Instacart

- Using Connect when the task only needs a shoppable page → heavier auth and wrong integration surface
- Using MCP for retailer lookup → current Developer Platform MCP create tools do not cover it
- Mixing `product_ids` and `upcs` on the same item → 400 validation error
- Repeating the same UPC or product id across multiple items → duplicate identifier errors
- Stuffing brands into `name` instead of `brand_filters` → weaker fallback matching
- Sending unsupported or vague units → product may match without a useful quantity
- Treating `retailer_key` as a specific store record → bad downstream assumptions
- Recreating identical pages on every run → unnecessary link churn and harder attribution
- Requesting production traffic before approval → key stays pending and does not function
- Publishing UI or marketing copy without guideline review → pause public copy and complete approval plus guideline review first
- Assuming Developer Platform page APIs own checkout or delivery windows → those flows belong to Connect / Marketplace user checkout
