# Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `lyL5QhgIOxc` · [watch](https://youtu.be/lyL5QhgIOxc) · **date:** 2026-08-18 · **length:** 21:39 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Arek Borucki · **orgs:** Hugging Face, MongoDB, Cast.ai, AWS, Kubernetes
- **topics:** infra-cost-scaling, rag-retrieval, data-engineering · **tags:** hugging-face, mongodb, atlas-search, lucene, read-replicas, sharding, kubernetes, hpa, keda, cast-ai, autoscaling, p99-latency, denormalization, change-streams

> How Hugging Face scaled its Hub search, MongoDB read path and Kubernetes autoscaling to 3M public models; main lesson is precomputed read copies, read-replica routing, and scaling on workload signals.

## Summary
Arek Borucki, a Hugging Face ML platform and database engineer, describes how the Hub grew from about 20,000 models to 3 million public models and 14 million users. The talk focuses on search latency, since at this size tail (P99) latency hurts many users. Model names are tokenized at insert time into a denormalized read-only MongoDB collection, and search moved from regex scans to Atlas Search, which wraps Apache Lucene. Reads are spread across a 7-node cluster: the primary handles writes and strongly consistent reads, secondaries take the rest, and a hidden replica takes reporting and heavy queries. Sharding is the next planned step, with the shard key left out of scope. On the compute side, the Hub runs an HPA scaling 10 to 500 pods, Cast.ai adds nodes when pods are pending, and a move to KEDA is planned so scaling follows request rate or queue depth rather than CPU alone. The talk is a practitioner account with concrete patterns and few hard benchmark numbers.

## Key ideas
- **Scale is the reason to rethink search: a query that is fast at 20k models breaks at 3M.** — The speaker says that at 20,000 models any query was fast even without an index, and that the same approach fails at 3 million. Slow search costs users, so the team tunes for P99 rather than P50. ([3:40](https://youtu.be/lyL5QhgIOxc?t=220))
- **Keep metadata and binary artifacts apart.** — MongoDB Atlas holds all metadata (users, repos, orgs, billing, access control). Model weights, tokenizer files and configs live in object storage such as S3. This lets metadata, binaries and compute each scale on their own. ([5:54](https://youtu.be/lyL5QhgIOxc?t=354))
- **Use a denormalized read copy with search tokens computed at insert time.** — A separate collection holds only what listing and search need. Model IDs like meta-llama/Llama-3.1-8B are split into tokens at write time and stored in an array, so no tokenization happens at query time. ([8:01](https://youtu.be/lyL5QhgIOxc?t=481))
- **Regex over token arrays stopped scaling, so search moved to a Lucene index.** — The old query was a regex match over the token arrays, sorted by a trending score refreshed every five minutes. It got slower as data grew. Atlas Search (Lucene behind a wrapper process) gives autocomplete over the tokens with the same trending sort, and the speaker reports latency issues gone. ([10:38](https://youtu.be/lyL5QhgIOxc?t=638))
- **Route reads by consistency need and workload type.** — Only queries that need strong consistency run on the primary. Non-urgent reads, heavy aggregations and change-stream consumers go to secondaries. Ad hoc and reporting queries go to a hidden replica that the driver never routes production traffic to. The stated rule is that the primary does only what only the primary can do. ([13:00](https://youtu.be/lyL5QhgIOxc?t=780))
- **Sharding is the next step once one replica set is no longer enough.** — A replica set keeps the full data set on every node. A sharded cluster splits the data across shards, each with its own replicas, and the balancer spreads data as shards are added. The talk says choosing the shard key is hard and does not cover it. ([17:12](https://youtu.be/lyL5QhgIOxc?t=1032))
- **Scale on workload signals, not CPU alone.** — HPA scales on CPU and memory, so a pod with low CPU but a long request queue is not scaled. Moving to KEDA lets scaling use request rate or event-loop utilization. A second layer, Cast.ai, adds nodes when pods are pending. ([18:45](https://youtu.be/lyL5QhgIOxc?t=1125))

## Techniques
- **Insert-time search tokens in a denormalized read collection** — Store a separate read-only document per model with pre-split name tokens in an array. Project only that array for search and listing. The main collection stays the source of truth. *When:* Listing and autocomplete queries are read-heavy and the canonical document shape is too costly to query directly.
- **Lucene-backed autocomplete instead of regex scans** — Create a search index on the token array and query it with the $search aggregation stage, keeping the existing business sort (trending score) after the match. *When:* Regex or prefix scans over a growing collection have rising P99 latency.
- **Read-replica routing by consistency class** — Send strongly consistent reads and all writes to the primary. Send stale-tolerant reads, heavy aggregations and change-stream consumers to secondaries. Send ad hoc and reporting queries to a hidden, non-routable replica member. *When:* One primary is taking reads that do not need it, and analytic queries are affecting production latency.
- **Hidden analytics replica** — Add a replica set member that replicates the primary but is excluded from the driver's read routing. Connect to it directly for reports and expensive queries. *When:* Heavy or exploratory queries must not share capacity with user-facing traffic.
- **Two-layer autoscaling with event-driven pod scaling** — Let the pod autoscaler add pods on load, let a node autoscaler add nodes when pods stay pending, and move the pod signal from CPU/memory to app metrics such as request rate or queue depth via KEDA. *When:* CPU does not track real load, so latency or 503s build up while the autoscaler sees no pressure.

## Numbers
- Hugging Face serves more than 14 million users. ([1:23](https://youtu.be/lyL5QhgIOxc?t=83))
- 3 million public models, 1 million datasets, 50,000 organizations; over 30% of Fortune 500 companies use the Hub. ([1:23](https://youtu.be/lyL5QhgIOxc?t=83))
- Public models grew from about 20,000 to 3 million, roughly a 150x increase in a few years. ([2:32](https://youtu.be/lyL5QhgIOxc?t=152))
- Datasets: about 10K in 2022, 100K in 2024, 500K a year before the talk, 1M at the time of the talk. ([3:40](https://youtu.be/lyL5QhgIOxc?t=220))
- At 14 million users, 1% is about 140,000 people hitting slow search. ([4:44](https://youtu.be/lyL5QhgIOxc?t=284))
- The metadata cluster handles about 1 million queries with a 7-node MongoDB cluster. ([13:00](https://youtu.be/lyL5QhgIOxc?t=780))
- The hub deployment autoscales between 10 and 500 pods. ([18:45](https://youtu.be/lyL5QhgIOxc?t=1125))

## Hot takes
- At 20,000 models any query is fast even without an index; at 3 million the same approach breaks.
- At scale, P99 latency matters more than P50, because even 1% of users is a very large number of people.
- The primary should only do what only the primary can do; everything else should move to other machines.

## Tools mentioned
MongoDB Atlas, Atlas Search, Apache Lucene, Kubernetes, Horizontal Pod Autoscaler, KEDA, Cast.ai, AWS S3, AWS Redshift

## Relevance to our work
- **agentos** (2/3): The L3 roadmap includes a per-tenant DuckDB read tier. The talk's hidden-analytics-replica pattern shows how to keep heavy reads away from the hot path.
