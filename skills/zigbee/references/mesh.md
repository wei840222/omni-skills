# Mesh Design

## Roles

| Role | Power | Routes traffic | Typical devices |
|------|-------|----------------|-----------------|
| Coordinator | Mains / USB host | Yes (root) | USB stick, hub radio |
| Router | Mains | Yes | Smart plugs, in-wall switches, many bulbs |
| End device | Battery or constrained | No | Motion, contact, temperature, buttons |

Battery devices act only as end nodes. Only mains-powered routers extend the mesh.

## Backbone rules

- Build the backbone before sensors: first paired routers become the long-lived mesh fabric.
- Plan roughly one usable router every 10-15m indoors, denser through thick walls, metal, or multi-floor paths.
- One coordinator alone has limited range; do not expect whole-home coverage from the stick by itself.
- After adding routers, some devices need time or a rejoin/reconfigure pass before they learn better routes. Do not assume every leaf auto-optimizes instantly.

## Placement heuristics

1. Put routers in hallways, stair landings, and rooms between the coordinator and far sensors.
2. Prefer always-powered plugs/bulbs over seasonally switched outlets for backbone nodes.
3. Keep critical automation targets within one or two strong hops of a router.
4. If a leaf is at the edge, add a router nearer to it instead of raising TX power as the first move.

## Expansion order

1. Coordinator online and stable
2. 3+ routers forming a continuous path through the home
3. Always-on actuators (locks only with local-safe backup planning, lights, switches)
4. Sleepy sensors and remotes last
