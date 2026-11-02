# SQLite is 138x Slower Than This?! (Testing Stoolap)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `t6fbNGC_48c` · [watch](https://youtu.be/t6fbNGC_48c) · **date:** 2026-03-02 · **length:** 7:33 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, Stoolap, SQLite, napi-rs, Rayon
- **topics:** dev-tools, data-engineering · **tags:** embedded-database, olap, sqlite-alternative, rust, nodejs-native-addon, napi-rs, benchmarking, count-distinct, mvcc, parallel-execution, cost-based-optimizer

> Tests Stoolap, a Rust embedded analytics DB with a native Node.js binding: 4-6x faster than SQLite on COUNT DISTINCT, well short of the 138x headline, and the npm package was broken at the time.

## Summary
Better Stack's Andrus introduces Stoolap, a Rust embedded OLAP database that recently shipped a native Node.js driver, and pitches it against SQLite with a headline claim of 138x speed. He explains the design: the Rust engine is compiled through napi-rs into a native addon so queries avoid a serialization bridge, and the engine uses MVCC for concurrent readers and writers, Rayon for parallel query execution, and a cost-based optimizer. The installed npm package failed with a missing native binding, so he built Stoolap from source and linked it locally. He then ran two synthetic benchmarks in in-memory databases: COUNT DISTINCT on 10k and 1M sales rows (about 4x and 6x faster than SQLite), and DISTINCT plus ORDER BY on random log rows (only about 1-1.5x faster). He concludes Stoolap is a strong analytical engine but not a SQLite replacement, since the project itself says SQLite wins on single-row operations.

## Key ideas
- **Stoolap is pitched as an embedded OLAP database: SQLite-style single-file portability with analytics aimed at DuckDB or BigQuery-style workloads, unlike OLTP engines such as SQLite or Postgres.** — Headline claim of 138x faster than SQLite is stated up front and is not reproduced in the tests that follow. ([0:00](https://youtu.be/t6fbNGC_48c?t=0))
- **The Node driver avoids the usual bridge cost. napi-rs compiles the Rust engine into a native binary loaded into the Node process, so there is no JSON conversion or local socket hop, and Node and Rust share memory.** — The presenter calls serialization overhead a major performance killer for Rust or C++ databases reached from Node. ([1:17](https://youtu.be/t6fbNGC_48c?t=77))
- **Three engine features are cited for the speed: MVCC (multiple concurrent readers and writers, unlike SQLite's single writer), parallel query execution across cores via Rayon, and a cost-based optimizer that estimates plan costs.** — These are the author's stated reasons; the video does not verify each one separately. ([2:10](https://youtu.be/t6fbNGC_48c?t=130))
- **The published npm package was broken: it failed with a missing native binding. The workaround was to clone the repo, build from source, and link the local directory as the dependency.** — Presenter hopes the authors will publish binaries or fix linking in the package. ([4:11](https://youtu.be/t6fbNGC_48c?t=251))
- **On 10k rows, COUNT DISTINCT was about 4x faster than SQLite, far short of the headline. At 1M rows the gap was about 6x, so it does not scale to 138x.** — The presenter calls the advertised numbers inflated but says Stoolap is faster on this workload. ([4:11](https://youtu.be/t6fbNGC_48c?t=251))
- **DISTINCT plus ORDER BY on random IP and status-code logs was only about 1-1.5x faster than SQLite.** — Result is much smaller than the COUNT DISTINCT gain, so the advantage depends on the query shape. ([5:13](https://youtu.be/t6fbNGC_48c?t=313))
- **The author concludes Stoolap is not a SQLite killer. Use SQLite for daily transactional work; Stoolap fits analytical and complex queries. The project lists single-row operations as SQLite's strength.** — The verdict is a practitioner judgement from short synthetic tests, not a production evaluation. ([6:13](https://youtu.be/t6fbNGC_48c?t=373))

## Techniques
- **Head-to-head embedded DB micro-benchmark** — In a plain Node.js project, install the candidate DB and SQLite as dependencies. Spin up an in-memory instance of each. Create a sales table, batch-insert 10,000 random rows (user ID 0-1000, one of a few categories), then time a COUNT DISTINCT of one user's sales filtered by category. Repeat at 1M rows to see how the gap scales. *When:* Before switching an embedded database on a benchmark that matches your real query shape, not the vendor's headline.
- **Second benchmark for DISTINCT with ORDER BY** — Ingest random log rows with IP address and status code. Run DISTINCT on the (IP, status) pair ordered by IP ascending and status descending, then compare timings between the two engines. *When:* To check a second query shape, since the speedup from one query type does not carry over to another.
- **Building an unpublished native-binding package from source** — When the npm package fails with a missing native binding, clone the repo, run its build inside the checkout, then point the consumer project's dependency at the local source directory instead of the registry package. *When:* When a native Node addon ships without prebuilt binaries for your platform. Expect to maintain the local link yourself.
- **Why a native addon beats a socket bridge (napi-rs pattern)** — Compile the Rust engine into a native module loaded into the Node process via napi-rs, so queries and results cross an in-process boundary instead of being serialized as JSON over a local socket. *When:* When a Node service calls a Rust or C++ data engine on the hot path and serialization shows up in profiles.

## Numbers
- Headline claim: Stoolap is 138x faster than SQLite (not reproduced in the tests) ([0:00](https://youtu.be/t6fbNGC_48c?t=0))
- COUNT DISTINCT on 10,000 rows: about 4x faster than SQLite ([4:11](https://youtu.be/t6fbNGC_48c?t=251))
- COUNT DISTINCT on 1,000,000 rows: about 6x faster than SQLite ([5:13](https://youtu.be/t6fbNGC_48c?t=313))
- DISTINCT + ORDER BY on random log rows: about 1 to 1.5x faster than SQLite (the 14x figure is cited as the advertised comparison) ([5:13](https://youtu.be/t6fbNGC_48c?t=313))
- Benchmark dataset: 10,000 rows of sales data, user IDs 0 to 1,000, batch inserted into in-memory databases ([3:20](https://youtu.be/t6fbNGC_48c?t=200))

## Hot takes
- The 138x headline is inflated; the presenter measured roughly 4-6x on COUNT DISTINCT and 1-1.5x on DISTINCT + ORDER BY.
- The npm package as shipped was broken (missing native binding), which is a real adoption blocker at the time of the video.
- Stoolap is not a SQLite replacement: SQLite stays the default for transactional and single-row work, and Stoolap suits analytical queries.

## Tools mentioned
Stoolap (embedded Rust OLAP database, Node.js driver), SQLite, Node.js, Rust, napi-rs, Rayon, DuckDB (mentioned as analytics comparison), BigQuery (mentioned as analytics comparison), PostgreSQL (mentioned as OLTP comparison), npm

## Relevance to our work
- **agentos** (1/3): Stoolap is an embedded columnar-style engine that could serve local analytics over agent telemetry, but the tests were small synthetic benchmarks against SQLite, not relevant to the distributed ClickHouse or Postgres stack. → *If the SkillForge telemetry mining needs a local analytics store, benchmark a COUNT DISTINCT and DISTINCT ORDER BY on a real telemetry sample against SQLite or DuckDB before adopting Stoolap.*
