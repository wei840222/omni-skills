# Minecraft Mechanics and Canonical Knowledge

Load this reference when an answer depends on a Java/Bedrock mechanics distinction, a version-sensitive command, redstone behavior, or iron-golem farm conditions. Verify the affected version before presenting a command or a build rate as certain.

## Java Edition and Bedrock Edition

### Redstone

- **Quasi-connectivity** applies to Java Edition: pistons, droppers, and dispensers can be powered by certain redstone components one block diagonally above them. Bedrock Edition needs direct or adjacent power instead.
- Java update behavior and Bedrock update behavior differ. Treat timing-sensitive contraptions as edition-specific and test one isolated module before copying a full design.
- Java sticky pistons can drop a moved block after a one-game-tick pulse; Bedrock sticky pistons do not share that behavior.

### Commands

- Both editions support selectors such as `@p`, `@a`, `@r`, `@e`, and `@s`, but Java's entity-NBT support and command syntax do not transfer directly to Bedrock.
- Bedrock adopted the newer `/execute` form in 1.19.50, but feature parity is incomplete. Check the target version and load the official Bedrock changelog when a subcommand or condition matters.

### Spawning and Iron Golems

- Farm rates depend on edition, simulation distance, loaded chunks, mob caps, player location, and server settings; provide a test checkpoint instead of promising a universal rate.
- For Bedrock iron-golem farms, start by checking village recognition: at least 20 beds, at least 10 villagers, and 75% of villagers having worked during the previous day. Then check the version-specific spawn platform and nearby spawnable space.
- Java iron-golem designs have different village and villager behavior; keep Java and Bedrock troubleshooting separate.

## Primary Sources

- **Minecraft Wiki — Redstone circuits/Quasi-connectivity**: Java-specific quasi-connectivity behavior and affected blocks. <https://minecraft.wiki/w/Redstone_circuits/Quasi-connectivity>
- **Minecraft Wiki — /execute**: command syntax and edition/version notes. <https://minecraft.wiki/w/Commands/execute>
- **Minecraft Wiki — Iron Golem**: edition-specific iron-golem spawning requirements. <https://minecraft.wiki/w/Iron_Golem>
- **Minecraft Feedback — Minecraft 1.19.50 Bedrock**: Bedrock `/execute` syntax update. <https://feedback.minecraft.net/hc/en-us/articles/13321751494029-Minecraft-1-19-50-Bedrock>
