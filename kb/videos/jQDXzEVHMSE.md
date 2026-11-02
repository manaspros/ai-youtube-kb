# Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jQDXzEVHMSE` · [watch](https://youtu.be/jQDXzEVHMSE) · **date:** 2026-08-18 · **length:** 56:30 · **format:** interview · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Gergely Orosz, Simon Eskildsen · **orgs:** Turbopuffer, Shopify, Cursor, Readwise, NVIDIA, Reflection, Google Cloud
- **topics:** infra-cost-scaling, rag-retrieval, testing-verification · **tags:** turbopuffer, vector-search, s3, object-storage, napkin-math, toxiproxy, fault-injection, group-commit, cpu-scarcity, fundraising, remote-culture, founder-story

> Gergely Orosz interviews Simon Eskildsen, founder of Turbopuffer, on his path from Shopify infrastructure to building an S3-backed search engine, napkin-math habits, CPU scarcity and startup financing. Mostly origin story, little AI content.

## Summary
Gergely Orosz interviews Simon Eskildsen, founder and CEO of Turbopuffer. Eskildsen describes his self-taught path into infrastructure, eight years at Shopify, and the Toxiproxy fault-injection tool he built there. He explains the "napkin math" habit of estimating hardware limits before trusting benchmarks, which led him to batching and to a search engine built on object storage. The first version was deliberately simple: clustered vector files on S3, a centroid file, and an NGINX cache in front. Cursor became the first major customer after a cost-driven migration, and the talk covers CPU scarcity as RL and agent workloads grow. It closes with his views on early fundraising, the six reasons to raise capital, and running a fully remote company with "campfire" meetups. Very little of the talk is about AI engineering directly.

## Key ideas
- **Napkin math as a sanity check on benchmarks** — Eskildsen keeps a table of hardware costs and latencies (DRAM, S3, NVMe, EBS, round trips) and flashcards for it. If a benchmark disagrees with the back-of-envelope estimate, the benchmark or its query plan is probably wrong. He says he distrusts benchmarks as a basis for infra decisions. ([15:06](https://youtu.be/jQDXzEVHMSE?t=906))
- **Fault injection at the network layer, run in CI** — Toxiproxy sits between the app and the database, and an API can take the database down or slow it. Testing through a real proxy exercises the actual drivers' failure handling, which mocks skip. It surfaced many bugs in the MySQL driver and Rails at Shopify. ([11:01](https://youtu.be/jQDXzEVHMSE?t=661))
- **Group commit explains write throughput** — A fsync takes about 1 ms, which would cap writes near 1,000 per second. MySQL did about 10,000 writes per second on a small box because each fsync persisted a batch of writes. Mental models that skip batching give wrong capacity estimates. ([19:24](https://youtu.be/jQDXzEVHMSE?t=1164))
- **Design object storage around P99 round trips** — An S3 GET of a 256–512 KB object has roughly 200 ms P99 latency. A tree-shaped read path multiplies that per level, so the design should minimise round trips and be judged on P99 and P999, not P50. ([23:57](https://youtu.be/jQDXzEVHMSE?t=1437))
- **Ship the dumbest correct version first** — The first version clustered vectors into S3 files with a centroid file: fetch centroids, then the nearest clusters. Caching was just an NGINX reverse proxy in front of S3, with no separate cache layer. It ran on one VM in tmux and was launched publicly to see if anyone cared. ([26:06](https://youtu.be/jQDXzEVHMSE?t=1566))
- **Hot-cold split for large vector indexes** — Eskildsen's account of the Cursor idea: keep only actively used namespaces in RAM or cache and let the rest sit in object storage, loaded on demand. This was the pattern that fit the unit economics of Cursor's DRAM-heavy setup. ([29:11](https://youtu.be/jQDXzEVHMSE?t=1751))
- **Price from napkin math, then optimise to the margin** — The launch price was set from a rough estimate of what a better implementation should cost. He then optimised until the vendor's cost sat below the price, which he describes as basic business sense. He also says he chose not to raise early because the company was profitable. ([43:22](https://youtu.be/jQDXzEVHMSE?t=2602))
- **CPU demand is rising from RL and agents** — RL training runs and agents running code need lots of general-purpose CPU and NVMe, and hyperscalers are allocating these scarcely. He says even large customers are maxed out on long contracts. Turbopuffer copes by running across many machine SKUs. ([38:54](https://youtu.be/jQDXzEVHMSE?t=2334))

## Techniques
- **Napkin-math latency and cost estimate before benchmarking** — List the hardware primitives (DRAM bandwidth, SSD and S3 round-trip, fsync cost, $/GB) and compute the expected time or cost for a query or design. Treat a large gap from measured results as a bug in either the benchmark or your understanding. *When:* Choosing a database or storage design, or reviewing a vendor benchmark that does not match intuition.
- **Proxy-based fault injection in CI** — Put a thin layer-4/7 proxy between the service and its database or dependency. Expose an API to take it down, slow it, or corrupt data, then run each failure case inside the test suite against the real drivers. *When:* Verifying that services degrade correctly when a stateful dependency fails, and catching driver-level bugs that mocks miss.
- **Object storage as the system of record with an HTTP cache in front** — Store index clusters and a centroid file as objects on S3. At query time, read the centroids, then fetch only the nearest clusters. Place an NGINX reverse proxy cache in front of S3 for hot objects and invalidate it by path. *When:* Building a cheap, durable vector or search store where per-query latency can tolerate a few object reads.
- **Design for tail latency and round trips** — Count the sequential object reads a query needs. Use P99 or P999 for each round trip as the budget, and restructure the tree or layout to cut levels. *When:* Any design built on high-latency remote storage where one request fans out into several dependent reads.
- **Batch durable writes** — Accept writes into a batch and persist them with one fsync or one object write, rather than one per write. This is why a database can exceed the fsync-rate cap on writes. *When:* Reasoning about write throughput on a single disk or when designing a write-ahead path.
- **Ship simplest version then probe demand** — Build the smallest reliable version on a single node, launch it publicly, and only harden for scale once real users appear. Keep the durability invariants even though the code is simple. *When:* Early-stage infrastructure projects where you do not yet know whether anyone needs them.

## Numbers
- S3 P99 latency for a 256 or 512 KB object is around 200 ms ([23:57](https://youtu.be/jQDXzEVHMSE?t=1437))
- Estimated cost of running Readwise-style vector recommendations on the original stack was about $30K per month, against roughly $5K per month for all of its other infrastructure ([23:57](https://youtu.be/jQDXzEVHMSE?t=1437))
- Cost reference points used: about $2 per GB of memory, about $0.02 per GB of S3, about $0.10 per GB of disk ([16:31](https://youtu.be/jQDXzEVHMSE?t=991))
- fsync takes about 1 ms, which would cap writes near 1,000 per second, yet MySQL on a small box did about 10,000 writes per second through batching ([19:24](https://youtu.be/jQDXzEVHMSE?t=1164))
- Early pitch: one million vectors for about $1, where the previous cheapest working option was about $100 per million ([29:11](https://youtu.be/jQDXzEVHMSE?t=1751))
- Cursor's bill dropped about 95% after migrating to Turbopuffer ([32:59](https://youtu.be/jQDXzEVHMSE?t=1979))
- Initial guarantee to Cursor was a bill of about $4K per month ([43:22](https://youtu.be/jQDXzEVHMSE?t=2602))
- First outside raise targeted about $700K to fund two engineers for the rest of the year ([46:53](https://youtu.be/jQDXzEVHMSE?t=2813))
- Eskildsen cites 2013 Shopify growth of 120–140% year over year ([12:26](https://youtu.be/jQDXzEVHMSE?t=746))
- Turbopuffer holds in-person offsites twice a year ([47:00](https://youtu.be/jQDXzEVHMSE?t=2820))

## Hot takes
- Benchmarks are a poor basis for infrastructure decisions. Napkin math based on hardware primitives is a better check.
- Raising venture capital for founder ego is a very dangerous reason. It dilutes employees and sets a price for future hires.
- CPU scarcity will get worse before it gets better, because RL training and agents running code consume CPUs.
- Startups can take irrational risks when they have conviction. Showing up in person and helping a customer's database problem built the trust that led to the Cursor deal.
- Software that ages well is simple. Simplicity beats cleverness in long-lived systems.

## Tools mentioned
Toxiproxy, NGINX, Amazon S3, MySQL, Rails, Postgres, pgAnalyze, Docker, Rust, GDB, Redis, NVMe SSD, GCP C4 / Z4D / C4A machine types

## Relevance to our work
- **agentos** (2/3): AgentOS thesis is proving the stack as a distributed system. Toxiproxy-style dependency fault injection and object-storage tiering are directly relevant to the L3 storage and archive roadmap. → *Put a Toxiproxy-style proxy in front of Postgres, Redis and Neo4j in the test suite and write CI cases for down, slow and corrupt modes, starting with the MemoryMesh retrieval path.*
