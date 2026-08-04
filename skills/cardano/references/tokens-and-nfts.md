# Native Tokens and NFTs

## Native Token Basics

Cardano tokens are first-class protocol citizens — not smart contracts:
- No separate token contract needed
- Minting/burning controlled by policy scripts
- Tokens can be transferred alongside ADA in same transaction
- Policy ID uniquely identifies the token family

## Token Standards

| Standard | Purpose | Notes |
|----------|---------|-------|
| CIP-20 | Transaction metadata | Message attachment |
| CIP-25 | NFT metadata | JSON metadata with media links |
| CIP-26 | Token registry | Off-chain metadata registration |
| CIP-27 | Royalties | CNFT royalty standard |
| CIP-67 | Fungible token metadata | Asset name label scheme |
| CIP-68 | Token metadata | Reference NFT pattern |

## Minting Workflow

### Step 1: Create policy script

```bash
# Time-locked policy (expires after deadline)
cat << EOF > policy.script
{
  "type": "all",
  "scripts": [
    {
      "type": "before",
      "slot": EXPIRY_SLOT
    },
    {
      "type": "sig",
      "keyHash": "YOUR_KEY_HASH"
    }
  ]
}
EOF

# Calculate policy ID
cardano-cli transaction policyid --script-file policy.script > policy.id
```

### Step 2: Create metadata (CIP-25 for NFTs)

```bash
cat << EOF > metadata.json
{
  "721": {
    "POLICY_ID": {
      "ASSET_NAME": {
        "name": "Token Name",
        "image": "ipfs://IPFS_HASH",
        "description": "Description",
        "files": [{"src": "ipfs://MEDIA_HASH", "name": "filename", "mediaType": "image/png"}]
      }
    }
  }
}
EOF
```

### Step 3: Build minting transaction

```bash
cardano-cli transaction build \
  --mint "1 POLICY_ID.ASSET_NAME" \
  --minting-script-file policy.script \
  --metadata-json-file metadata.json \
  --tx-in YOUR_UTXO \
  --tx-out "RECIPIENT_ADDRESS+2000000+1 POLICY_ID.ASSET_NAME" \
  --change-address YOUR_ADDRESS \
  --invalid-hereafter EXPIRY_SLOT \
  --out-file mint.tx
```

### Verification checkpoints before minting

- [ ] Policy script matches intended constraints (time-lock, signatures)
- [ ] Metadata follows correct CIP standard structure
- [ ] Asset name is properly hex-encoded
- [ ] Minimum UTxO value calculated for output with tokens
- [ ] `--invalid-hereafter` matches policy time-lock slot

## Burning Tokens

Burning requires the same policy script that was used for minting:

```bash
cardano-cli transaction build \
  --mint "-1 POLICY_ID.ASSET_NAME" \
  --minting-script-file policy.script \
  --tx-in YOUR_UTXO_WITH_TOKEN \
  --tx-out "YOUR_ADDRESS+ADA_AMOUNT" \
  --change-address YOUR_ADDRESS \
  --invalid-hereafter EXPIRY_SLOT \
  --out-file burn.tx
```

**Time-locked policies:** If the policy has expired (current slot > `before` slot), tokens cannot be minted OR burned. This is irreversible — verify time-locks carefully.

## Token Safety

### Verifying token authenticity

Scam tokens can copy names and metadata. Always verify by policy ID:

```bash
# Check policy ID against known legitimate projects
# Official project channels publish their policy ID
cardano-cli transaction txid --tx-file tx.body
```

### Common token anti-patterns

- **Trusting token name alone** — anyone can mint a token named "ADA" or "SUNDAE"
- **Ignoring policy ID** — policy ID is the true identifier, not the name
- **Not checking IPFS pinning** — unpinned IPFS content disappears
- **Minting without time-lock** — unlimited supply possible forever
- **Using `any` instead of `all` in policy scripts** — weakens minting constraints

## NFT Marketplaces

- jpg.store — largest Cardano NFT marketplace
- cnft.io — marketplace and analytics
- Verify NFT policies before buying — check policy ID, metadata, and IPFS links

## References

- [CIP-25: Transaction metadata](https://github.com/cardano-foundation/CIPs/tree/master/CIP-0025)
- [CIP-68: Token metadata standard](https://github.com/cardano-foundation/CIPs/tree/master/CIP-0068)
- [Cardano native tokens documentation](https://docs.cardano.org/native-tokens/learn/)
- [Token metadata registry](https://developers.cardano.org/docs/developers/curriculum/native-tokens/metadata-registry/)
