# DuckDB is becoming unstoppable...

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `dKbV8MEzVPA` · [watch](https://youtu.be/dKbV8MEzVPA) · **date:** 2026-08-02 · **length:** 6:04 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** DuckDB, Snowflake, Google BigQuery, Apache Iceberg project, Apache Spark
- **topics:** data-engineering, dev-tools · **tags:** duckdb, sql, parquet, olap, embedded-database, iceberg, encryption, sqlite, variant-type, merge-into

> A six-minute Better Stack walkthrough of DuckDB 1.4 and 1.5, separating their features, showing in-place Parquet queries, and stating where the single-machine analytics engine should not be used.

## Summary
The speaker presents DuckDB as an embedded, SQLite-like database built for analytics rather than transactions. He demonstrates running SQL directly against a Parquet file on a URL with no import step. He separates two releases that are often conflated: DuckDB 1.4 (September, its first long-term support release) brought AES-256 encryption, MERGE INTO upserts and Iceberg writing, while 1.5 (March) brought a new CLI, a VARIANT type for mixed semi-structured data, and geometry in core. He compares DuckDB with SQLite (row store versus column store), Pandas (SQL optimizer and multi-threaded joins) and cloud warehouses such as Snowflake and BigQuery. The limits he names are memory use at around a billion rows, a single writer with no transactional role, bring-your-own-key encryption with no key management, and a newer Iceberg writing extension. His recommendation is analytics, ELT and notebook work on one machine, and Postgres or SQLite for app backends.

## Key ideas
- **DuckDB is SQLite for analytics: an embedded, single-file, no-server database built to scan and aggregate large row counts quickly** — The speaker frames it as the same embedded model as SQLite but column-oriented and aimed at analysis instead of transactions. ([0:00](https://youtu.be/dKbV8MEzVPA?t=0))
- **No import step: SQL can point straight at Parquet, CSV or JSON files, including files on a URL** — He types duckdb in a terminal to get a SQL prompt, then selects from a remote Parquet file in one line. He says it streamed and queried the file in about five seconds, with no download, schema definition or server. ([1:02](https://youtu.be/dKbV8MEzVPA?t=62))
- **The headline features people mix up belong to 1.4, not 1.5** — Full AES-256 database encryption, MERGE INTO for Git-style upserts and Iceberg table writing all shipped in 1.4 (September), which was also the first long-term support release. 1.5 (March) added a CLI with colors and a pager, a VARIANT type and geometry in core. ([1:02](https://youtu.be/dKbV8MEzVPA?t=62))
- **VARIANT in 1.5 stores mixed types in one column without a schema** — Integers, strings, arrays and objects can share a column with no JSON parsing. The speaker says the data is stored as typed binary, which compresses and queries better than plain JSON text. ([2:07](https://youtu.be/dKbV8MEzVPA?t=127))
- **MERGE INTO removes app-side upsert logic** — He presents a single SQL statement for upserts as a feature that used to need Spark or custom Python. He calls it the feature that changed what you can build on DuckDB. ([2:07](https://youtu.be/dKbV8MEzVPA?t=127))
- **Encryption is page-level AES-256 with bring-your-own-key, and the database does not manage the key** — Without the key, reopening the file in a new session fails. DuckDB does not store, rotate or monitor the key, so losing it means losing the data. ([3:30](https://youtu.be/dKbV8MEzVPA?t=210))
- **Positioning against neighbours: SQLite is row-oriented for transactions, Pandas lacks a real SQL optimizer, and warehouses are multi-user cloud systems** — The speaker says DuckDB gives a real SQL optimizer and multi-threaded joins, which are often a little faster than Pandas on large group-bys. He describes it as one machine in your own process, free, versus cloud warehouses built for teams and petabytes. ([3:30](https://youtu.be/dKbV8MEzVPA?t=210))
- **The stated limits are memory, a single writer and no transactional role, so it is not an app backend** — Billion-row datasets can run out of memory. Only one process writes at a time, so Postgres (or SQLite for small MVPs) stays the backend database. The Iceberg writing extension is new. ([4:32](https://youtu.be/dKbV8MEzVPA?t=272))

## Techniques
- **Query files in place from the DuckDB CLI** — Run `duckdb` in a terminal to open a SQL prompt, then SELECT from a Parquet file given by URL, or from a local CSV or JSON file, with no import or table definition first. Exact SQL is not shown on screen. *When:* Ad hoc exploration of exported or remote data, notebook work, and ELT transforms over Parquet, CSV or JSON on one machine.
- **Single-statement upserts with MERGE INTO (DuckDB 1.4+)** — Use one MERGE INTO SQL statement to insert or update target rows from a source, instead of writing application-side upsert logic. The speaker does not show the syntax. *When:* Incremental loads into an analytics table on a single machine, where Spark or custom Python would otherwise be used.
- **VARIANT column for messy semi-structured data (DuckDB 1.5+)** — Declare or use a VARIANT column and insert mixed values (integers, strings, arrays, objects) into it with no schema and no JSON parsing. Data is stored as typed binary. *When:* Event or log payloads whose shape varies, where a fixed schema is unknown or costly to maintain, and where compressed, typed storage beats plain JSON text.
- **Page-level AES-256 encryption with your own key** — Create or open the database with an encryption key you supply. Queries work with the key. Opening the same file without the key fails. DuckDB does not store, rotate or back up the key, so key management belongs in your own system. *When:* Encrypting a single-machine analytics file at rest. Plan key storage and recovery first, since losing the key loses the data.

## Numbers
- A remote Parquet file was streamed and queried with real SQL in one line, in about five seconds (demo, not a benchmark) ([1:02](https://youtu.be/dKbV8MEzVPA?t=62))
- DuckDB 1.4 shipped in September and was DuckDB's first long-term support release; 1.5 shipped the following March ([1:02](https://youtu.be/dKbV8MEzVPA?t=62))
- Billion-row datasets can run out of memory and crash the process (qualitative threshold, no measurement given) ([4:32](https://youtu.be/dKbV8MEzVPA?t=272))
- Pandas is often a little faster than Pandas on a big group-by is claimed, but no benchmark is shown; the claim is that DuckDB is often a little faster ([3:30](https://youtu.be/dKbV8MEzVPA?t=210))
- DuckDB is MIT-licensed and free with no paywall ([4:32](https://youtu.be/dKbV8MEzVPA?t=272))

## Hot takes
- DuckDB is positioned as a single-machine analytics tool, not an app backend, and the speaker says Postgres or SQLite remain the right choice for transactional work.
- Bring-your-own-key encryption with no key rotation or recovery is a serious operational caveat that many coverage pieces skip.
- The claim that DuckDB often beats Pandas on large group-bys is asserted without a benchmark.
- The speaker warns viewers that the 1.4 and 1.5 features are often confused, which is a fair correction of popular coverage.

## Tools mentioned
DuckDB 1.4, DuckDB 1.5, SQLite, Pandas, Snowflake, Google BigQuery, Apache Parquet, Apache Iceberg, Apache Spark, Postgres, CSV, JSON

## Relevance to our work
- **agentos** (2/3): The roadmap lists a Parquet + DuckDB archive and a per-tenant DuckDB read tier. The video covers in-place Parquet queries and the encryption and single-writer limits that bear on that design. → *Prototype the archive read tier by running DuckDB over exported Parquet files for a few real query shapes, then measure memory use at target row counts before committing to it. Also decide how the encryption key is stored and rotated, since DuckDB will not manage it.*
