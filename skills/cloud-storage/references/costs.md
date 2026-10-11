# Cost Calculation

Numbers below are **orientation baselines** captured during refactor research.
Before any customer-facing quote, open the live vendor pages listed in
`references/sources.md` for the exact region, class, and SKU.

## The three cost categories

| Category | What it includes | Often overlooked |
|----------|------------------|------------------|
| Storage | GB-month stored | Minimum duration on cold classes |
| Operations | PUT/POST/LIST/GET-class requests | LIST/inventory at millions of keys |
| Transfer | Egress / inter-region / retrieval | Usually the largest surprise on migrations |

---

## Orientation comparison (verify live)

| Provider / class | Storage / GB-mo (orient.) | Egress notes (orient.) | Request notes (orient.) |
|------------------|--------------------------|------------------------|-------------------------|
| S3 Standard (common commercial tiers) | ~$0.023 class of rates still widely cited; confirm region table | Internet egress commonly ~$0.09/GB early tiers in many public examples | PUT/LIST-class and GET-class priced per 1,000; confirm current request table |
| S3 Glacier / Deep Archive family | Much lower storage; retrieval extra | Egress still applies after restore | Minimum storage durations commonly **90 days** (Flexible/Instant family variants) and **180 days** (Deep Archive)—confirm class docs |
| GCS Standard | Region-specific; often low-cent GB-mo | Inter-continent and internet egress can dominate | Class A/B operation prices differ by storage class |
| Azure Blob Hot | Region-specific hot tier rates | Internet egress separate from storage | Tier changes and archive rehydrate add cost/time |
| Backblaze B2 | Marketing/list pages have used ~$0.006/GB-mo class rates; calculator math in public page used ~$6.95/TB-mo style inputs | Public materials emphasize low egress and allowances (for example 3× stored data free egress patterns)—confirm current offer | API transaction packaging differs from AWS 10k blocks |
| Cloudflare R2 Standard | Docs list **$0.015 / GB-month** | Docs list **egress to Internet free** (with stated caveats) | Class A and Class B per million; free tier for Standard only |

**Working insight:** R2-style free egress helps public/hot read traffic; B2-style low storage + egress allowances helps backup/archive economics; classic hyperscaler object stores often lose large migrations on egress unless free tiers, private interconnect, or transfer programs apply.

---

## Hidden costs

### Minimum storage duration

- **S3 Glacier family** — early delete can still bill minimum duration (commonly 90 days on several Glacier classes; Deep Archive commonly 180 days). Confirm [storage class docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).
- **GCS Archive / cold classes** — longer minimums than Standard; confirm class table.
- **R2 Infrequent Access** — docs describe minimum duration and retrieval fees separate from Standard free tier.

### Small objects and chatty APIs

- Minimum object billable size on some providers (B2 historically called out small-file floors).
- Millions of LIST/HEAD calls can rival storage cost; prefer inventory reports and caching.

### Cross-region and cross-cloud

- Replication and migration bill egress on the source and write ops on the destination.
- Same-region copies avoid internet egress but still incur requests and capacity.

---

## Before large operations

### Migration sketch (orientation math)

```text
Files: 100,000
Size: 500 GB
Source: S3 us-east-1 → Destination: GCS europe-west1

Orientation egress: 500 GB × ~$0.09 ≈ $45
Destination writes: still usually small vs egress at this scale
Monthly keep-in-place storage: 500 × ~$0.023 ≈ $11.50

Always replace ~$0.09 / ~$0.023 with the live regional SKU before presenting a quote.
```

### Serving sketch

```text
10 TB / month egress
Hyperscaler internet egress at ~$0.09/GB → on the order of $900
R2 documented free internet egress → $0 egress line-item (still pay storage + ops)
```

---

## Cost optimization checklist

- [ ] Cold data on an appropriate cold class with known minimum duration
- [ ] Lifecycle rules for transition and multipart abort cleanup
- [ ] Egress path reviewed (CDN, R2, private link, same-region processing)
- [ ] Inventories instead of repeated full-bucket LIST
- [ ] Abandoned multipart uploads cleaned
- [ ] Live pricing pages opened for the exact regions involved
