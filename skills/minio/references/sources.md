# Official Sources (last-checked 2026-09-18)

Use these primary sources when verifying MinIO behavior, command syntax, or durability features. Prefer the live docs page over memorized flags.

## Core product docs
- MinIO Documentation home — product overview and doc index via https://min.io/docs
- MinIO Server / AIStor docs entry — current server operations guidance via https://docs.min.io/
- MinIO Client (`mc`) overview — CLI workflows for buckets, objects, and admin tasks via https://min.io/docs/minio/linux/reference/minio-mc.html

## Identity, policy, and durability
- MinIO IAM and policy concepts — least-privilege identity design via https://min.io/docs/minio/linux/administration/identity-access-management.html
- Bucket versioning — prerequisite checks before replication and lifecycle changes via https://min.io/docs/minio/linux/administration/object-management/object-versioning.html
- Bucket replication — topology and versioning prerequisites via https://min.io/docs/minio/linux/administration/bucket-replication.html
- Object lock / retention — immutability controls during maintenance via https://min.io/docs/minio/linux/administration/object-management/object-retention.html

## S3 compatibility boundary
- AWS S3 API reference — compare only when diagnosing S3-compatible client expectations via https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html

## Operational note
MinIO command surfaces and package names evolve (including AIStor branding in newer docs). Re-check the linked pages for the installed server/`mc` version before applying destructive or cluster-wide changes.
