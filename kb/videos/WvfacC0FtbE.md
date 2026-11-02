# Postgres was rewritten in Rust… and somehow passed every test

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `WvfacC0FtbE` · [watch](https://youtu.be/WvfacC0FtbE) · **date:** 2026-08-02 · **length:** 8:34 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, PostgreSQL, CockroachDB, YugaByte, Hacker News
- **topics:** dev-tools, coding-agents · **tags:** postgres, rust, database-reimplementation, regression-testing, thread-per-connection, psql, docker, ai-assisted-rewrite, compatibility

> Better Stack reviews PG Rust, a from-scratch Rust reimplementation of Postgres that passes the official regression suite but is not production ready, with its headline performance claims unverified.

## Summary
The video walks through PG Rust, a separate Rust reimplementation of Postgres behavior rather than an extension or fork. The host runs the official Docker image and shows that stock psql sees the same SQL, output and query plans as Postgres, including an index scan on a 100,000-row table. The released version reportedly passes about 46,000 official regression queries, speaks the real wire protocol, and can boot from an existing Postgres 18.3 data directory. The main architectural bet is an unreleased thread-per-connection version, which the speaker says reportedly yields about 50% better transactional and roughly 300x analytical performance, but no code or benchmarks are available to check. The host argues that extensions and forks inherit Postgres's architecture, while a separate engine can change it, and that the thread model trades process isolation for lower overhead. Coding agents were used heavily for the rewrite, and the host frames the real question as whether AI makes large architectural experiments affordable. The verdict is clear: passing regression tests is a measurable compatibility target, but not evidence of crash recovery, replication, or extension-ecosystem maturity, so don't use it in production, though it is worth trying.

## Key ideas
- **PG Rust is a separate engine that imitates Postgres behavior, not an extension or feature layered on top of it.** — It keeps Postgres behavior, the client experience and the disk formats, and replaces the engine underneath with Rust. ([0:00](https://youtu.be/WvfacC0FtbE?t=0))
- **Stock psql cannot tell it apart from Postgres in the demo.** — Same client, same SQL, same output, and the planner chose an index scan with real execution stats on a 100k-row table. ([0:48](https://youtu.be/WvfacC0FtbE?t=48))
- **The released version is not the performance story; the unreleased thread-per-connection build is.** — The released build is not heavily optimized and is not expected to be dramatically faster than regular Postgres. The big claims come from the unpublished version. ([2:16](https://youtu.be/WvfacC0FtbE?t=136))
- **Forks and extensions carry Postgres's architecture; a separate engine can change it.** — Extensions sit on the Postgres core, and a fork inherits the same architecture plus the ongoing cost of tracking upstream. Using Postgres behavior as the spec is different from CockroachDB or YugaByte, whose goal is not drop-in compatibility. ([3:25](https://youtu.be/WvfacC0FtbE?t=205))
- **Thread-per-connection removes process walls that currently contain failures.** — Threads lower per-connection overhead and make sharing state easier, but one unsafe extension or memory bug could affect more of the server. ([4:30](https://youtu.be/WvfacC0FtbE?t=270))
- **The real experiment is whether AI makes very large rewrites cheap enough to rethink architecture.** — The rewrite used coding agents heavily. The speaker frames it less as can Rust make Postgres faster and more as can AI make this kind of rewrite affordable. ([4:30](https://youtu.be/WvfacC0FtbE?t=270))
- **Passing the official suite is a measurable bar, but it is not production trust.** — The regression suite is a fixed external judge, unlike vague 'Postgres compatible' claims. It does not cover years of crash recovery and replication testing, or the extension ecosystem, which is still unfinished. ([6:34](https://youtu.be/WvfacC0FtbE?t=394))

## Techniques
- **Use an upstream regression suite as the compatibility oracle** — Run the reimplementation against the official test suite (the default regression and isolation tests) and report pass counts, e.g. 46,000+ queries. Treat the suite as the external spec rather than the project's own tests. *When:* Building a compatible reimplementation of a well-specified system where 'compatible' is otherwise an unmeasurable claim.
- **Smoke-test compatibility with unmodified clients** — Start the official Postgres-compatible Docker image, connect with a stock psql (no custom client), check the reported version, create a table, insert data, and compare EXPLAIN ANALYZE output. The speaker also suggests running your own client library against it. Exact commands are not shown in the video. *When:* Evaluating any wire-compatible database or proxy before trusting it with application code.
- **Check on-disk compatibility by booting an existing data directory** — Point the new server at a data directory created by the target version (here Postgres 18.3) and confirm it starts. *When:* Assessing whether a rewrite can be adopted in place or requires a dump and restore migration.
- **Triage performance claims by asking for the code or benchmark** — Separate claims that have published code and reproducible numbers from those that do not (here, the unreleased thread-per-connection build's 50% and 300x figures). Treat unverified numbers as promising, not settled. *When:* Reading vendor or project benchmark claims for a system you cannot yet run.

## Numbers
- Roughly a million lines of C and nearly four decades of Postgres architecture ([0:00](https://youtu.be/WvfacC0FtbE?t=0))
- Released version passes about 46,000 Postgres regression queries ([0:00](https://youtu.be/WvfacC0FtbE?t=0))
- Demo inserts 100,000 generated rows before running a query plan ([2:16](https://youtu.be/WvfacC0FtbE?t=136))
- Released version targets Postgres 18.3 and boots an existing 18.3 data directory ([3:25](https://youtu.be/WvfacC0FtbE?t=205))
- Unreleased thread-per-connection build claims roughly 50% better transactional performance ([5:34](https://youtu.be/WvfacC0FtbE?t=334))
- Unreleased thread-per-connection build claims roughly 300x Postgres on analytical workloads ([5:34](https://youtu.be/WvfacC0FtbE?t=334))

## Hot takes
- The 50% transactional and 300x analytical claims are unverifiable because the code and benchmarks for the unreleased build are not public; the speaker says to treat them as promising claims, not facts.
- Passing the official regression suite is a serious and measurable achievement, but the speaker says it does not establish production trust.
- Thread-per-connection is not automatically better: it lowers overhead but removes process-level fault containment.
- Verdict: do not replace a production Postgres cluster with PG Rust, but do try it against your own clients.

## Tools mentioned
PG Rust (Postgres 18.3 compatible target), PostgreSQL, Docker, psql, Bun (mentioned as another Rust rewrite), CockroachDB, YugaByte, GitHub, Hacker News

## Relevance to our work
- **agentos** (1/3): AgentOS L3 storage is Postgres/pgvector, and the video's per-connection overhead and pooling tradeoff applies there. The video also offers a compatibility-testing method: an external suite as the measurable target. → *When making compatibility claims for the AgentOS proxy or storage layer, define an external conformance suite and report pass counts instead of saying 'compatible'.*
