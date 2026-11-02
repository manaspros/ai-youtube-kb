# I replaced my entire tech stack with Postgres

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `MZfhhl6ej-k` · [watch](https://youtu.be/MZfhhl6ej-k) · **date:** 2026-09-02 · **length:** 7:02 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools, rag-retrieval, infra-cost-scaling · **tags:** postgresql, pgvector, postgis, pg_cron, jsonb, unlogged-tables, full-text-search, self-hosted, cost-reduction, service-consolidation

> Better Stack walks through replacing separate cache, vector DB, search, geo, cron and document-store services with Postgres features, framed for small apps rather than scale.

## Summary
Better Stack's presenter argues that Postgres and its extensions can replace six separate services: caching, vector search, full-text search, geospatial queries, cron scheduling, and document storage. For each, he shows the basic setup: an UNLOGGED table as a cache, pgvector for embeddings stored beside the source text, a tsvector column with a GIN index for full-text search, a PostGIS geography column with a GiST index for radius and polygon queries, pg_cron for scheduled SQL with a run history, and a JSONB column with a GIN index for document queries. The framing is cost-driven and explicitly aimed at small services; the speaker says the approach is viable when the app does not need to reach hundreds of thousands of users. No benchmarks, latency figures or load tests are shown, and each section is a feature tour with a small example rather than a measured comparison. The useful takeaway is a checklist of Postgres features to evaluate before adding a dependency, not evidence that a single database holds up under production load.

## Key ideas
- **Consolidate onto Postgres to cut the number of paid or hosted services in a small app** — Framed as 'not because we should but because we can'. The pitch is fewer dependencies and lower cost, scoped to apps that do not need large scale. ([0:00](https://youtu.be/MZfhhl6ej-k?t=0))
- **UNLOGGED tables give a cache without Redis or Memcached** — Unlogged tables skip the write-ahead log, so writes are much faster, but the table is emptied on a server crash. The speaker considers that acceptable for cache data. Reads are about the same as normal tables. ([0:00](https://youtu.be/MZfhhl6ej-k?t=0))
- **pgvector stores embeddings next to the source text, so no separate vector database is needed** — He chunks a Wikipedia article, embeds each chunk, inserts both into a table with a vector column, then embeds a question and runs a vector search against it. ([1:28](https://youtu.be/MZfhhl6ej-k?t=88))
- **Built-in full-text search with tsvector and a GIN index replaces Elasticsearch for simple cases** — A generated tsvector column is built from the body text. Stop words are dropped and words are stemmed (jumping to jump), so queries match word variants. A GIN index keeps lookups fast. ([2:38](https://youtu.be/MZfhhl6ej-k?t=158))
- **PostGIS geography type handles real-distance queries in meters** — Locations use the 4326 (GPS latitude/longitude) coordinate system with a GiST index. Radius queries use meters over the earth's surface without manual trigonometry. Longitude goes first in the point constructor, which the speaker says caught him out. Polygons work for zones such as delivery areas or flood boundaries. ([3:57](https://youtu.be/MZfhhl6ej-k?t=237))
- **pg_cron moves scheduled jobs into the database, with a visible job table and run history** — A job has a name, a standard cron expression and a SQL statement. Jobs are listed in a table, every run is recorded, and removing a job calls an unschedule function. The example deletes log rows older than 30 days every night at 3am. ([5:07](https://youtu.be/MZfhhl6ej-k?t=307))
- **JSONB with a GIN index covers schemaless document storage** — The containment operator checks whether one JSON document contains another, and the key-existence operator checks whether a key is present. He also mentions DocumentDB, a MongoDB-compatible layer built on Postgres, and a separate video on durable workflows in Postgres. ([5:56](https://youtu.be/MZfhhl6ej-k?t=356))
- **The closing caveat limits the advice to small services** — The speaker says these extensions can be viable compared with third-party tools when the service does not need to target hundreds of thousands of users. That is the only scale guidance given. ([5:56](https://youtu.be/MZfhhl6ej-k?t=356))

## Techniques
- **Postgres as a cache using UNLOGGED tables** — Create the cache table with the UNLOGGED keyword, wrap reads and writes in a small helper, and accept that contents are lost on a crash. Skipping the write-ahead log is what makes writes faster. *When:* Low-stakes cache data in a small app where losing the cache on a crash is acceptable. Do not use it for data that must survive a crash, such as durable run state.
- **pgvector for embeddings and similarity search** — Install the pgvector extension, create a table with a vector column, chunk the source document, embed each chunk, and insert the text and its embedding together. At query time, embed the question and run a vector similarity search. The embedding model is not named in the video. *When:* Retrieval over a corpus that is small enough that a separate vector database is not justified. Source text and vectors stay in one transactional store.
- **Full-text search with a generated tsvector column and a GIN index** — Add a tsvector column generated from the body text (the video names it tsv), create a GIN index on it, and query it with a web search to tsquery function against that column. Stemming and stop-word removal happen at index time. *When:* Keyword search over a modest text column, where stemmed matching is good enough and the team wants to avoid running Elasticsearch.
- **Geospatial radius and polygon queries with PostGIS** — Enable the PostGIS extension, add a geography column using SRID 4326, and create a GiST index on it. Insert points with longitude first. Query 'within N meters' using the geography type so that N is in real meters. Use the distance operator to order results by proximity. Store polygons for zones and test whether a point falls inside them. *When:* Location lookups such as nearby places, delivery zones or flood areas, inside an app that already runs Postgres.
- **Scheduled SQL with pg_cron** — Schedule a job by giving it a name, a standard cron expression and the SQL to run. Inspect the job table to see what is scheduled, check the run history for failures, and remove a job by calling the unschedule function. Example from the video: delete log rows older than 30 days, daily at 03:00. *When:* Nightly cleanup, report generation or other periodic database work that should stay close to the data, without an external cron service.
- **Document storage with JSONB, a GIN index and containment queries** — Create a table with a JSONB column and add a GIN index. Store arbitrary JSON. Query with the containment operator to match documents that contain a given fragment, or the key-existence operator to test for a key. *When:* Schemaless or varying document shapes in a small service that does not justify a separate document database.

## Numbers
- Scope: suited to services that do not target hundreds of thousands of users; the example app has about five users ([0:00](https://youtu.be/MZfhhl6ej-k?t=0))
- Example cron job: delete log rows older than 30 days, nightly at 3am ([5:07](https://youtu.be/MZfhhl6ej-k?t=307))
- Radius example: rows within 500 meters of a lat/long point, computed in real meters via the geography type ([3:57](https://youtu.be/MZfhhl6ej-k?t=237))
- Speaker lost about 30 minutes to longitude-before-latitude ordering on first use of PostGIS ([3:57](https://youtu.be/MZfhhl6ej-k?t=237))
- Stemming and stop-word example: 'the quick brown foxes were jumping over the lazy dogs' reduces to a handful of stems (brown, dog, fox, jump, lazy, quick) with stop words removed ([2:38](https://youtu.be/MZfhhl6ej-k?t=158))
- No benchmarks, latency or throughput figures are given for any of the six features ([0:00](https://youtu.be/MZfhhl6ej-k?t=0))

## Hot takes
- Framed as a 'poor man's stack' that works 'not because we should but because we can'; the speaker is openly playful about the trade-off.
- The title ('replaced my entire tech stack') overstates the content. The video is a feature tour with small examples and no load or production evidence.
- Unlogged tables trade crash durability for write speed. The speaker treats wipe-on-crash as acceptable only for cache data.
- The only scale guidance is the closing remark that the approach fits services that do not target hundreds of thousands of users.
- No sponsor segment is visible in the transcript.

## Tools mentioned
PostgreSQL, pgvector, PostGIS, pg_cron, JSONB, DocumentDB, Redis, Memcached, Pinecone, Qdrant, Elasticsearch, MongoDB, Wikipedia (sample data source)

## Relevance to our work
- **agentos** (2/3): MemoryMesh already uses pgvector and BM25 hybrid retrieval, and Postgres is the L3 store. The video's tsvector and pgvector sections describe the same building blocks, but it does not compare them with BM25 ranking or cover evals. → *Benchmark MemoryMesh's BM25 plus pgvector hybrid retrieval against a native Postgres tsvector full-text query on the same knowledge bucket, measuring recall and latency, before deciding whether a separate BM25 index is needed.*
- **prosharness** (1/3): Checkpoint and resume of long runs needs durable state. UNLOGGED tables are wiped on crash, so they must not hold checkpoints. pg_cron could drive the loops and schedules if they live in Postgres. → *Keep ProsHarness checkpoint tables as ordinary logged tables, never UNLOGGED. If loops and schedules move into the database, compare pg_cron's job table and run history with the current scheduler's audit trail.*
