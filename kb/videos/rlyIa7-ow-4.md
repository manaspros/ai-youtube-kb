# Why Everyone’s Talking About PostgreSQL 18

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `rlyIa7-ow-4` · [watch](https://youtu.be/rlyIa7-ow-4) · **date:** 2025-11-02 · **length:** 4:43 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, PostgreSQL
- **topics:** dev-tools, data-engineering · **tags:** postgresql, postgresql-18, async-io, skip-scan, pg_upgrade, generated-columns, returning-old-new, explain, oauth, scram, logical-replication, replication-slots, page-checksums, vacuum, wal

> A 4-minute Better Stack recap of PostgreSQL 18's headline changes: async I/O, skip scans, upgrade-preserved planner stats, virtual generated columns, OAuth 2, and replication and checksum defaults. It is a release-notes summary with no benchmarks or SQL shown.

## Summary
The speaker (Andrus, Better Stack) walks through PostgreSQL 18 as a set of release highlights rather than a hands-on tutorial. Performance items are a new asynchronous I/O subsystem that issues parallel reads (up to 3x faster reads in some workloads on supported systems) and skip scans for multi-column indexes. Upgrade items are planner statistics that carry across major upgrades and a faster pg_upgrade with parallel checks and a swap flag. Developer items are virtual-by-default generated columns, old and new values in RETURNING, and buffer usage shown by default in EXPLAIN. Security items are OAuth 2 support and deprecation of the MD5 password method. Operations items are automatic cleanup of idle replication slots, conflict reporting and parallel table streaming for logical replication, and page checksums enabled by default on new clusters, plus more aggressive vacuum freezing. The video gives no benchmarks, no SQL examples and no upgrade walkthrough, so each claim is a pointer to the release notes rather than evidence.

## Key ideas
- **New asynchronous I/O subsystem: Postgres can issue multiple disk read requests in parallel instead of one at a time.** — Speaker says up to 3x faster reads in certain workloads on supported systems. No workload or hardware detail is given. ([0:00](https://youtu.be/rlyIa7-ow-4?t=0))
- **Skip scans for multi-column indexes let a query use an index even when it does not filter on the first column.** — Pitched as reducing full table scans and making index use more flexible for query writing. ([0:00](https://youtu.be/rlyIa7-ow-4?t=0))
- **Planner statistics now survive major version upgrades, so queries do not slow down until ANALYZE is re-run.** — pg_upgrade is described as faster, with better parallel checks and a new swap flag aimed at reducing downtime. The flag is not named in the video. ([1:01](https://youtu.be/rlyIa7-ow-4?t=61))
- **Generated columns default to virtual, computed on read rather than stored on disk.** — Framed as saving storage and keeping schemas cleaner. The video does not discuss the read-cost trade-off. ([1:01](https://youtu.be/rlyIa7-ow-4?t=61))
- **RETURNING can reference both old and new row values, which helps auditing and logging of updates.** — EXPLAIN now shows buffer usage by default along with richer stats for debugging performance. ([1:49](https://youtu.be/rlyIa7-ow-4?t=109))
- **OAuth 2 authentication is added, and the MD5 password method is deprecated in favor of SCRAM or external auth.** — Positioned as easier integration with modern identity providers and a stronger default security posture. ([1:49](https://youtu.be/rlyIa7-ow-4?t=109))
- **Unused replication slots are dropped automatically, which prevents idle slots from causing WAL growth that fills disks.** — The speaker describes idle slots piling up in older versions and filling disks without warning. ([2:54](https://youtu.be/rlyIa7-ow-4?t=174))
- **Logical replication reports apply conflicts on the subscriber and streams tables in parallel by default.** — Presented as making large-scale replication faster and more transparent. ([2:54](https://youtu.be/rlyIa7-ow-4?t=174))
- **New clusters enable page checksums by default, and vacuum freezes old tuples more aggressively to reduce transaction ID wraparound risk.** — Checksums are presented as detecting silent corruption with no extra setup. Only new clusters get the default, so existing clusters are not covered. ([2:54](https://youtu.be/rlyIa7-ow-4?t=174))

## Techniques
- **Single-statement audit of updates via RETURNING old/new** — Use the old and new row references in an UPDATE's RETURNING clause to get the previous and new values in one result set, then write them to an audit or log table. The speaker does not show the SQL. *When:* Auditing or logging row changes without a separate read before the write.
- **Rely on virtual generated columns for derived fields** — Define generated columns with the 18 default, which computes values on read and stores nothing on disk. *When:* Derived columns where storage matters more than read cost. The speaker names no read-cost trade-off, so benchmark before relying on it for hot queries.
- **Skip-scan-aware index reuse** — Keep an existing multi-column index and write queries that filter only on a later column, without adding a second index. The speaker shows no query plans. *When:* When an index exists for a column combination but a query does not filter on its leading column.
- **Major upgrade with preserved planner statistics** — Run pg_upgrade on 17 to 18 and rely on carried-over planner statistics instead of an immediate ANALYZE. The speaker mentions a new swap flag for reduced downtime but does not name it, so check the release docs for the exact option. *When:* Planning a major version upgrade where post-upgrade slowdowns or long downtime are the concern.

## Numbers
- Async I/O gives up to 3x faster reads in certain workloads on supported systems. No benchmark, workload or hardware is named. ([0:00](https://youtu.be/rlyIa7-ow-4?t=0))
- Video length is 4:43. No other figures are given. ([0:00](https://youtu.be/rlyIa7-ow-4?t=0))

## Hot takes
- This is a release-notes recap, not hands-on content. There are no benchmarks, SQL examples or upgrade steps, and the 3x read claim has no workload attached.
- The title says 'Everyone's Talking About', but the substance is a list of changes, with no judgment on which ones matter for production.

## Tools mentioned
PostgreSQL 18, pg_upgrade, EXPLAIN, SCRAM, OAuth 2

## Relevance to our work
- **agentos** (2/3): AgentOS L3 storage is Postgres/pgvector and MemoryMesh uses pgvector hybrid retrieval, so the 18 upgrade path (stats preservation, skip scans, default page checksums on new clusters) touches the core store, though the video is shallow. → *Test a pg_upgrade from 17 to 18 on a copy of the AgentOS Postgres/pgvector instance, confirming planner stats and the pgvector extension survive, and check the release notes for the exact swap flag and checksum behavior.*
