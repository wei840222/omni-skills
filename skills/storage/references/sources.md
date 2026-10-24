# Official Sources & Storage System Specifications

This document records the official documentation and technical specifications for modern storage architectures, filesystems, and in-memory caches.

## Storage Specifications & Standards

- **NVM Express (NVMe & NVMe-oF) Specifications**: [https://nvmexpress.org/specifications/](https://nvmexpress.org/specifications/)
  - Direct attached and networked NVMe storage protocols over RDMA and TCP/IP fabrics.
- **Linux Kernel Filesystem Documentation**: [https://www.kernel.org/doc/html/latest/filesystems/index.html](https://www.kernel.org/doc/html/latest/filesystems/index.html)
  - VFS interface, block device drivers, ext4, XFS, Btrfs, and page cache writeback behavior.

## In-Memory Caching & Distributed Storage

- **Valkey Open Source In-Memory Datastore**: [https://valkey.io/](https://valkey.io/) and [https://github.com/valkey-io/valkey](https://github.com/valkey-io/valkey)
  - High-performance key-value caching, Redis-compatible commands under open-source governance (Linux Foundation), persistence options (RDB/AOF), and cluster sharding.
