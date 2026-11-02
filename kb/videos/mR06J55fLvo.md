# Columnar Databases Are Incredibly Fast. Here's Why.

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `mR06J55fLvo` · [watch](https://youtu.be/mR06J55fLvo) · **date:** 2026-10-02 · **length:** 6:39 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** ClickHouse, DuckDB
- **topics:** data-engineering, infra-cost-scaling, dev-tools · **tags:** columnar-database, clickhouse, duckdb, postgres, analytics, sort-key, benchmark, olap-vs-oltp

> Better Stack compares Postgres, ClickHouse and DuckDB on 100M rows: columnar stores win big on aggregations, but lose on point lookups and single-row updates.

## Summary
The video explains why columnar databases run aggregation queries far faster than Postgres, using the same SQL over 100 million rows. It attributes the speedup to reading fewer blocks and only the columns a query needs. ClickHouse uses a sort key with a sparse index of block marks, and DuckDB keeps min/max statistics per chunk. The same benchmarks show the trade-off: a row lookup by ID is slow on ClickHouse (168 ms vs 2 ms on Postgres) because its only index is the sort key, and single-row updates are very slow because stored column files are immutable. The speaker frames ClickHouse as a client-server database and DuckDB as an embedded, file-based library with limited concurrency. The video is short and uses one dataset on one machine, with no hardware, version or methodology details.

## Key ideas
- **Same SQL, 100M rows, GROUP BY revenue: Postgres about 9.7 s, ClickHouse 0.28 s, DuckDB 0.24 s, roughly 40x faster.** — The speedup comes from doing far less work: only the needed columns are opened and most data is skipped, not from a different query language. ([0:00](https://youtu.be/mR06J55fLvo?t=0))
- **ClickHouse sorts the table by a sort key, splits it into blocks of about 8192 rows (granules), and keeps only the first key value of each block in memory.** — A time-range count for March read 1,633 of 12,208 blocks and skipped the rest. The video says about 12,000 index marks fit in memory for 100M rows. ([2:25](https://youtu.be/mR06J55fLvo?t=145))
- **DuckDB keeps a min and max for every chunk of a column, so it can skip whole chunks whose range does not match the filter.** — This gave the same time-range count in 0.03 s. The video also says DuckDB only opens the columns the query names. ([2:25](https://youtu.be/mR06J55fLvo?t=145))
- **Point lookup by ID is the columnar weak spot: Postgres 2 ms (B-tree), ClickHouse 168 ms, DuckDB 2 ms.** — ClickHouse's only index is the sort key (timestamp, then ID), so a lookup by ID checks all 12,208 blocks and then opens all eight column files to rebuild the row. ([2:25](https://youtu.be/mR06J55fLvo?t=145))
- **DuckDB's ID lookup is fast only because the IDs were inserted in order, so the chunk min/max ranges line up with the ID. Shuffled IDs would force a full column scan.** — The speaker presents this as luck with the data, not a general property of the engine. ([3:42](https://youtu.be/mR06J55fLvo?t=222))
- **Single-row updates are expensive in ClickHouse because data files are immutable: changing one value rewrites the whole column file for that chunk.** — Timings: Postgres 5 ms, ClickHouse 5.8 s, DuckDB tens of ms. The video says ClickHouse has a lightweight update in beta, meant for at most about 10% of the table. ([3:42](https://youtu.be/mR06J55fLvo?t=222))
- **Architecture differs: ClickHouse is an open-source server you run, while DuckDB is an in-process library that stores one database in a single file, and that file can be locked while an update runs.** — The speaker says this limits DuckDB's concurrency. He adds that the real choice depends on scalability, redundancy and extensibility, not only query speed. ([5:49](https://youtu.be/mR06J55fLvo?t=349))

## Techniques
- **Split workloads by access pattern** — Use a row store (Postgres) for point lookups and frequent small updates, and a columnar store (ClickHouse or DuckDB) for wide aggregations such as GROUP BY and COUNT DISTINCT over many rows. The video runs both on the same dataset. *When:* When one system has to serve both transactional lookups and analytics scans over the same large table.
- **Choose the ClickHouse sort key for the dominant filter** — The table's ORDER BY sort key is its only index. Put the most common range filter first (the video uses timestamp, then ID). Expect block skipping on that column and full scans on everything else. *When:* When designing a ClickHouse table, or when a query on a non-leading column is slow.
- **Insert in key order to make min/max skipping work** — Write rows in increasing order of the key you filter on, so each chunk's min/max covers a narrow range. The video shows DuckDB finding one ID quickly only because the IDs were inserted in order. *When:* When using DuckDB or any min/max-per-chunk engine for lookups on a monotonic key such as an ID or timestamp.
- **Avoid per-row updates on columnar stores** — Batch changes or append new rows instead of updating single rows. The video measures one-row updates at 5.8 s in ClickHouse, which rewrites the column chunk, versus tens of ms in DuckDB. *When:* When a columnar table receives frequent single-row corrections or status changes.
- **Benchmark with identical SQL on the same data** — Load the same 100M-row table into each engine and run the same query, with minimal syntax changes, timing each one. The video reports one run per query with no warm-up or hardware details. *When:* Before choosing a database for an analytics path. Repeat runs and record hardware and versions before drawing firm conclusions.

## Numbers
- GROUP BY revenue over 100M rows: Postgres 9.7 s, ClickHouse 0.28 s, DuckDB 0.24 s (over 40x faster) ([0:00](https://youtu.be/mR06J55fLvo?t=0))
- ClickHouse sparse index holds about 12,000 block marks for 100M rows, with 8192 rows per block ([2:25](https://youtu.be/mR06J55fLvo?t=145))
- Time-range count for March (about 13% of events): Postgres 5.9 s, ClickHouse 0.06 s, DuckDB 0.03 s; ClickHouse read 1,633 of 12,208 blocks ([1:14](https://youtu.be/mR06J55fLvo?t=74))
- Single-row ID lookup: Postgres 2 ms, ClickHouse 168 ms, DuckDB 2 ms ([2:25](https://youtu.be/mR06J55fLvo?t=145))
- Single-row update: Postgres 5 ms, ClickHouse 5.8 s, DuckDB tens of ms ([3:42](https://youtu.be/mR06J55fLvo?t=222))
- COUNT DISTINCT users over the full table: Postgres 38.4 s, ClickHouse 0.78 s, DuckDB under 1 s ([4:43](https://youtu.be/mR06J55fLvo?t=283))

## Hot takes
- The 40x headline holds only for scan-heavy aggregations. The same video shows ClickHouse losing badly to Postgres on ID lookups (168 ms vs 2 ms) and updates (5.8 s vs 5 ms).
- No methodology is given: one dataset, one run per query, no hardware, no versions, no cache state. The numbers are illustrative, not a benchmark to copy.
- The claim that an aggressive Postgres index would not get close to ClickHouse and DuckDB on the March query is asserted, not measured.
- No sponsored segment. The only promotion is a subscribe call-out, so quality is not capped on that basis.

## Tools mentioned
PostgreSQL, ClickHouse (open-source server, shown as local server), DuckDB (embedded, single-file library)

## Relevance to our work
- **agentos** (2/3): The L3 storage roadmap includes ClickHouse analytics and a Parquet + DuckDB archive tier. The video gives concrete evidence that DuckDB handles lookups and updates better than ClickHouse, which matters for choosing the archive read tier. → *Before building the ClickHouse analytics path or the DuckDB archive tier, run the same 100M-row set through Postgres, ClickHouse and DuckDB for three query types: aggregation, ID lookup and single-row update. Record hardware and versions.*
