# Polars 2.0 Says 5× Faster... So What's Changed?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `uHELj20WrOc` · [watch](https://youtu.be/uHELj20WrOc) · **date:** 2026-10-02 · **length:** 8:33 · **format:** news · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh (Better Stack) · **orgs:** Better Stack, Polars
- **topics:** dev-tools, data-engineering · **tags:** polars, pandas, dataframes, release-candidate, streaming-engine, lazy-evaluation, semver, row-order, python-data

> Better Stack walks through the Polars 2.0 release candidate: mostly a cleanup release that makes the streaming engine the default, drops row-order guarantees, and removes old APIs with replacement-naming errors. The 5x speedup is unbenchmarked.

## Summary
Josh from Better Stack walks through the Polars 2.0 release candidate, installed with the pre-release flag. He explains the two engines: the in-memory engine loads the whole dataset and runs each step across it, while the streaming engine chunks data into cache-sized morsels that flow through the query plan. The headline behavior change is that joins, group_bys and pivots no longer guarantee row order unless maintain_order is set; he demonstrates this with a left join that reorders results until maintain_order=True is passed. The release is otherwise a cleanup: renamed or removed APIs (read_csv, melt, join nulls, int-to-categorical and string-to-date casts) now raise errors that name the replacement, and concat rejects mismatched heights. The "five times faster" claim is the maintainers' own expectation with no benchmark table; he sees smaller gains, and true out-of-core spilling has not landed. He lists RC bugs (group_by_dynamic on streaming, limit not exiting early after a join, string-to-datetime returning null) and advises upgrading for new projects but waiting if code depends on row order or uses group_by_dynamic.

## Key ideas
- **Polars 2.0 changes the default engine: existing queries run on the streaming engine without code edits** — The speaker says every query already written moves to a different engine by default, so the upgrade changes execution without touching the code. ([0:00](https://youtu.be/uHELj20WrOc?t=0))
- **Two Polars engines: in-memory whole-dataset execution versus chunked streaming** — In-memory loads the full dataset and runs each step across it, fast only if it fits in RAM. Streaming splits data into morsels sized for the CPU cache and pipelines them through the plan, so parts of a query keep moving; this is the path toward larger-than-memory work. ([0:53](https://youtu.be/uHELj20WrOc?t=53))
- **Row order is no longer guaranteed for joins, group_bys and pivots unless you ask for it** — Parallel workers finish out of order, so results can come back shuffled. He shows the same left join returning a different order on RC, then getting the original order back with maintain_order=True. explain() on the query shows the behavior if you know to look. ([1:56](https://youtu.be/uHELj20WrOc?t=116))
- **2.0 is a cleanup release with no new features** — Examples: read_csv becomes scan_csv().collect(), LazyFrame profile is removed, melt becomes unpivot, join nulls becomes nulls_equal, direct int-to-categorical and string-to-date casts are removed, and i64 plus u64 now yields Int128 instead of a lossy float. concat now refuses mismatched heights. ([3:05](https://youtu.be/uHELj20WrOc?t=185))
- **Removed APIs raise errors that name their replacement, and collect_schema() catches type errors early** — The suggested workflow is to run the code, fix each error as it names the replacement, and repeat. Calling collect_schema() on a lazy frame surfaces wrong types before any rows are read, which he contrasts with Pandas pushing such problems to runtime. ([4:05](https://youtu.be/uHELj20WrOc?t=245))
- **The 5x speedup is an unbenchmarked expectation; out-of-core execution has not landed** — The post has no benchmark table. He saw real speedups on larger datasets but not 5x, and says streaming means chunked and pipelined, not spill-to-disk beyond RAM. ([5:14](https://youtu.be/uHELj20WrOc?t=314))
- **Main complaints: silent row-order defaults, the word 'streaming', and RC bugs** — Wrong row order causes no crash, only subtly misattached numbers. Open RC issues include a group_by_dynamic DateTime out-of-range error on streaming, limit() not exiting early after a join, and string-to-datetime returning null where it used to raise. The Rust crate is still 0.55. ([6:14](https://youtu.be/uHELj20WrOc?t=374))
- **Upgrade advice: new projects yes; wait if you depend on row order or group_by_dynamic** — Pipelines already using scan Parquet or scan CSV have effectively been streaming. Before upgrading existing code, grep for group_bys without a following sort, and hold off on group_by_dynamic until the bugs settle. ([7:24](https://youtu.be/uHELj20WrOc?t=444))

## Techniques
- **Pin row order explicitly** — Pass maintain_order=True to join, group_by or pivot calls whose output order matters. Use explain() on the lazy query to check the plan. Do not rely on default order after upgrading. *When:* Any pipeline whose downstream logic depends on row position, especially before moving to Polars 2.0.
- **Pre-upgrade audit for unsorted group_bys** — grep the codebase for group_by calls that have no sort after them, and treat each hit as a place where row order was implicitly relied on. *When:* Before upgrading an existing Polars codebase to 2.0.
- **Error-driven migration on the RC** — Run the existing code on the pre-release, then fix each removed-API error by applying the replacement it names: melt to unpivot (with index and on), read_csv to scan_csv().collect(), join nulls to nulls_equal, and cast-based replacements for int-to-categorical and string-to-date. Repeat until clean. *When:* Migrating scripts off deprecated Polars APIs when the release notes are thin.
- **Schema check before execution** — Call collect_schema() on a LazyFrame to inspect column types before collecting, so type mismatches surface before rows are read. *When:* Lazy pipelines where wrong dtypes would otherwise fail deep in execution.
- **Hold back RC features that have open bugs** — Keep group_by_dynamic and limit()-after-join pipelines on the stable release, and do not treat limit() as an early exit after a join. *When:* While the 2.0 release candidate still has the bugs listed in the video.

## Numbers
- Polars' own expectation that the new streaming engine is 'easily five times faster'; no benchmark table in the release post ([5:14](https://youtu.be/uHELj20WrOc?t=314))
- Speaker's own experience: streaming is faster than Pandas and visibly faster on larger datasets, but not five times faster ([7:24](https://youtu.be/uHELj20WrOc?t=444))
- Adding signed and unsigned 64-bit integers now yields Int128 instead of a float that silently loses precision ([3:05](https://youtu.be/uHELj20WrOc?t=185))
- The Rust crate is still at version 0.55, so there is no polars 2.0 crate for Rust yet ([6:14](https://youtu.be/uHELj20WrOc?t=374))

## Hot takes
- Polars 2.0 ships no new features but still changes what existing code does; a semver major bump used as a cleanup of the foundation.
- Silent row-order changes are more dangerous than exceptions, because nothing crashes and the numbers are still correct.
- The word 'streaming' overpromises for an engine that cannot yet spill beyond RAM.
- The 5x speedup is a maintainer expectation without published benchmarks; treat it as unverified.

## Tools mentioned
Polars 2.0 release candidate (pre-release, installed with the pre flag), Polars Python API (LazyFrame, scan_csv, collect_schema, explain), Pandas, DuckDB, Dask, Spark, uv (uv pip install), Polars Cloud (not open source), polars Rust crate 0.55, Parquet, CSV

## Relevance to our work
- **agentos** (1/3):  → *If evaluating Polars for the Parquet archive read tier, benchmark it on real archive data and pin order-sensitive ops with maintain_order=True.*
- **general** (1/3): Data-quality and entity-resolution work depends on deterministic output order, and a silent reorder on library upgrade is a test-coverage gap. → *Add a regression test that fails if a pipeline's output row order changes across a dependency upgrade.*
