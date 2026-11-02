# Dolt: This Makes SQL Feel Like Git

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `SDLfjrUyBw4` · [watch](https://youtu.be/SDLfjrUyBw4) · **date:** 2026-07-02 · **length:** 6:59 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, DoltHub
- **topics:** dev-tools, data-engineering · **tags:** dolt, version-control, git-for-data, sql, branching, diff-merge, mysql-compatible, prolly-tree, dvc, lakefs

> Quick walkthrough of Dolt, a MySQL-compatible SQL database with Git-style branch, diff, commit and merge on tables, plus where it sits relative to Git, DVC and LakeFS.

## Summary
The host argues that structured data lacks a Git-like review workflow: databases have no clean branch or diff, and CSV/JSON in Git loses SQL, schema enforcement and joins. Dolt is presented as a SQL database with Git's command shape (status, diff, add, commit, branch, checkout, merge, log) applied to tables. In the demo, a public DoltHub getting-started database is opened with the SQL shell, a small edit is shown as a row- and column-level diff, then committed on a branch, edited again, and merged back to main. The host says Dolt can also run as a server that MySQL-compatible clients, ORMs and BI tools connect to. Storage is described as a tree structure that shares unchanged parts between commits rather than copying the whole database. The video places Dolt against Git-tracked files, DVC (ML artifacts), LakeFS (object-storage lakes) and traditional database history features, and closes by saying it should not be dropped into every production system, only tried where structured data changes can break things. No benchmarks or adoption numbers are given.

## Key ideas
- **Structured data has no good review workflow: databases lack branch and diff, while CSV/JSON in Git loses SQL, schema enforcement and joins.** — The host frames the problem as choosing between a real database with weak change review and Git-tracked flat files with weak database features. Dolt is pitched as having both. ([0:00](https://youtu.be/SDLfjrUyBw4?t=0))
- **Dolt reuses Git's command vocabulary but operates on table rows.** — Commands named in the video: branch, diff, commit, merge, status, add, checkout, log. The host's point is that the workflow is familiar; the object being versioned is the table. ([1:16](https://youtu.be/SDLfjrUyBw4?t=76))
- **dolt diff shows the actual table change, not a changed file.** — After an edit in the SQL shell, the diff reports which row and column changed, with old and new values. ([2:40](https://youtu.be/SDLfjrUyBw4?t=160))
- **Branch, change, diff, commit, merge is the full loop, and the same loop supports rollback.** — The demo makes a change, commits, branches with checkout, makes a second change, commits, switches to main and merges. Rollback is mentioned but not shown. ([2:40](https://youtu.be/SDLfjrUyBw4?t=160))
- **Running Dolt as a server makes it usable from normal SQL clients and application code.** — The host says apps can treat Dolt like an ordinary MySQL-compatible database while keeping version control. This is the main argument for production use over a CLI-only tool. ([3:58](https://youtu.be/SDLfjrUyBw4?t=238))
- **Storage uses a prolly tree (auto-captions say 'Crawley tree'), which shares unchanged parts across commits.** — Per the host, commits do not copy the whole database. Reads can ask what a row looked like before a change. Only a verbal description is given; no internals or benchmarks. ([3:58](https://youtu.be/SDLfjrUyBw4?t=238))
- **Dolt is positioned against Git, DVC, LakeFS and traditional DB history features, not as a replacement for all of them.** — Git lacks schema awareness and constraints. DVC targets ML data and artifacts. LakeFS is Git-like for object storage. Temporal tables, audit logs and CDC exist but lack the branch-diff-merge workflow. ([4:52](https://youtu.be/SDLfjrUyBw4?t=292))
- **The host explicitly advises against adopting Dolt in every production system.** — Suggested fit: structured data that changes over time where a single bad change can break things. Caveats such as performance and operational maturity are not discussed. ([5:47](https://youtu.be/SDLfjrUyBw4?t=347))

## Techniques
- **Clone a DoltHub database and make a versioned change** — Clone the DoltHub getting-started repository from GitHub (exact URL not shown), cd into it, then run `dolt sql` to open the SQL shell. Make a small UPDATE-style change (the statement is not shown), exit, and run `dolt diff` to see the row and column change. Then `dolt add` and `dolt commit -m "<message>"` (the -m flag is inferred from captions; the video shows only 'M'). *When:* Trying Dolt for the first time, or checking that a data change is reviewable before adopting the workflow.
- **Branch, change, diff, merge on tables** — Create a branch with `dolt checkout -b <name>` (the -b flag is inferred from captions, shown as 'B'). Make another row change, run `dolt diff`, then `dolt add` and `dolt commit`. Switch back with `dolt checkout main` and run `dolt merge <name>`. Inspect history with `dolt log`. *When:* Making a bulk or risky data edit (config rows, imported CSVs, manual corrections) that should be reviewed before it reaches main.
- **Serve Dolt over the MySQL protocol for apps and BI tools** — Start Dolt's SQL server mode (the video says 'DOLT SQL Server'; the CLI subcommand is `dolt sql-server`, which is not typed on screen). Connect MySQL-compatible clients, ORMs, BI tools or application code to it as to any MySQL-style database. *When:* An application needs ordinary SQL access but also wants commit history and diffs over its data, without changing its data-access layer.

## Numbers
- No benchmarks, latencies, storage sizes or adoption figures are given. ([0:00](https://youtu.be/SDLfjrUyBw4?t=0))
- Host says setup can be done 'in the next couple of minutes'; video length is 6:59. ([0:00](https://youtu.be/SDLfjrUyBw4?t=0))

## Hot takes
- Git-for-data is a useful framing, but the host says outright not to put Dolt in every production system.
- Dismisses Git-tracked CSV/JSON as adequate only for tiny, simple data, and calls DVC and LakeFS different layers. This is a reasonable scope claim with no comparison data.
- Speaker claims Dolt has versions for SQLite and Postgres ('you name it') without showing either.
- Quality is capped by thin substance: a feature walkthrough with no benchmarks, no failure modes, no rollback demo and no discussion of performance or scale. Several subscribe calls, but no sponsorship is shown.

## Tools mentioned
Dolt (DoltHub getting-started database; CLI commands sql, diff, add, commit, branch, checkout, merge, log, status; SQL server mode), Git, DVC, LakeFS, MySQL-compatible clients, ORMs and BI tools (generic category, not a specific product)

## Relevance to our work
- **agentos** (1/3): AgentOS's MemoryMesh knowledge buckets and RAGAS eval datasets are structured data that changes; branch and diff over tables could make corpus or label edits reviewable. Low priority, since the video shows no evidence on scale or on the Postgres/pgvector stack already used. → *Spike the DoltHub getting-started database, then make a small eval-dataset table change on a branch and diff it, to decide whether branch-and-diff is worth it for AgentOS eval data.*
