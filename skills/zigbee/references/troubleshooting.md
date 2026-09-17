# Troubleshooting

Work the mesh bottom-up: coordinator health → channel/interference → router density → leaf device.

## Symptom ladder

### Device shows online but remains unresponsive
1. Power-cycle the leaf.
2. Send a command while watching live logs/route tables.
3. Check whether the path still has a living router hop.
4. Re-interview or rejoin the leaf only after the backbone looks healthy.

### Intermittent responses
- Mesh is often too sparse. Add mains-powered routers on the weak path.
- Recheck 2.4GHz overlap with loud Wi-Fi APs.
- Move the coordinator off noisy USB ports.

### Delayed commands
- Too many hops or a congested path. Add a closer router.
- Confirm the target is not a sleepy end device waiting for its next wake.

### New device fails to pair
- Network not actually in join mode, or join window already closed
- Device not factory-reset
- Coordinator too far during first join
- Model unsupported / needs quirks
- Conflicting second coordinator still powered

### Whole rooms drop after hub reboot
- Groups that depended on the coordinator may not restore local switch behavior
- Rebuild critical wall-switch control with binding where supported
- Confirm coordinator backup/restore actually reloaded the network key and device table

## Recovery order

1. Stabilize coordinator host and stick placement
2. Fix channel conflict if evidence is strong
3. Add or relocate routers
4. Re-pair the failing leaf
5. Full mesh rebuild only as last resort after backup
