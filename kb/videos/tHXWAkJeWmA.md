# Is Kafka OUTDATED? Could RedPanda Be the Future of Event Streaming?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `tHXWAkJeWmA` · [watch](https://youtu.be/tHXWAkJeWmA) · **date:** 2025-11-02 · **length:** 7:29 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Redpanda, Confluent, LinkedIn, Netflix, Uber, AWS, GCP
- **topics:** infra-cost-scaling, data-engineering, dev-tools · **tags:** kafka, redpanda, event-streaming, benchmarking, jvm, zookeeper, kafka-compatibility, licensing, self-hosting

> Better Stack compares Kafka and Redpanda: Redpanda wins architecture and deployment, Kafka wins ecosystem and licensing, and performance depends on the workload, per conflicting benchmarks.

## Summary
The video compares Apache Kafka (LinkedIn, 2011, Apache 2.0) with Redpanda (2021, C++, Business Source License) across architecture, deployment, performance, ecosystem and licensing. The host scores architecture and deployment for Redpanda: a single dependency-free binary with a thread-per-core model, and a Docker Compose setup that bundles a schema registry, HTTP proxy, automatic partitioning and an admin REST API. Both speak the Kafka protocol, so an existing Kafka Python client works unchanged against Redpanda. Performance is left unresolved: the host did not run benchmarks himself, and cites a Redpanda blog claim of 20x faster against a Confluent principal's tests that show Redpanda falling behind at 50 producers and Kafka scaling better with more partitions. Kafka wins ecosystem (Kafka Connect, Streams, MirrorMaker, cloud support, learning material) and licensing (true open source, forkable, though the host is not a Java developer). The host's final pick is Redpanda because he wants to avoid anything JVM-based. A short sponsored segment on Better Stack monitoring sits in the middle.

## Key ideas
- **Architecture favors Redpanda: a single C++ binary with no external dependencies, versus Kafka's JVM stack and, until recently, a ZooKeeper dependency for broker metadata.** — Redpanda uses a thread-per-core model that pins each application to a CPU core to reduce context switching and blocking. Newer Kafka releases no longer need ZooKeeper but still depend on the JVM. ([1:18](https://youtu.be/tHXWAkJeWmA?t=78))
- **Deployment favors Redpanda because more is bundled: schema registry, HTTP proxy, automatic partitioning, an admin REST API and a web console (Redpanda Console).** — The host stripped both Docker Compose files to a minimum and found the Kafka one more complex. Redpanda's Kafka compatibility means existing clients such as the Kafka Python library work without code changes. ([1:18](https://youtu.be/tHXWAkJeWmA?t=78))
- **Performance results depend on the workload and hardware, and the host does not settle it.** — He could not get the OpenMessaging Benchmark setup for Kafka working or access the large EC2 instances it needs, so he relied on published articles. Results conflict, so he gives performance to both. ([2:40](https://youtu.be/tHXWAkJeWmA?t=160))
- **A vendor blog claim of Redpanda being 20x faster is contested by a Confluent principal's tests.** — The Redpanda post claims 3 Redpanda nodes beat 4 Kafka nodes at 1 GB/s throughput on three EC2 instance types. Jack Van Lightly's tests show Redpanda slightly ahead at 4 producers, behind Kafka at 50 producers, and Kafka ahead with higher partition counts. ([2:40](https://youtu.be/tHXWAkJeWmA?t=160))
- **Ecosystem and licensing both go to Kafka.** — Kafka's ecosystem is about 10 years older. Redpanda Connect claims more connectors, but Kafka has more third-party integrations, tutorials and books. Kafka is Apache 2.0. Redpanda uses the Business Source License, which the host does not count as open source. He still sees value in Redpanda's vendor support and steady release cadence. ([5:03](https://youtu.be/tHXWAkJeWmA?t=303))
- **The final recommendation depends on the team's stack and needs; the host's own pick is Redpanda to avoid JVM-based systems.** — The host frames this as a personal preference, not a benchmark result. ([6:24](https://youtu.be/tHXWAkJeWmA?t=384))

## Techniques
- **Test Kafka-compatible brokers with existing clients** — Point an existing Kafka client library (the host uses the Kafka Python library) at the Redpanda broker with no code changes, to check protocol compatibility before committing to a migration. *When:* Evaluating a drop-in Kafka replacement for an existing producer/consumer codebase.
- **Minimal Docker Compose deployment for comparison** — Write a Docker Compose file for each broker with only the essential configuration, then compare the number of settings and dependencies needed for each (the host compares JVM and ZooKeeper requirements against a single Redpanda container). *When:* Judging operational complexity of a streaming platform for local dev or small self-hosted deployments.
- **Benchmark on your own workload with OpenMessaging Benchmark** — Run the Open Messaging benchmark framework against both brokers on your own hardware, varying producer counts and partition counts, rather than relying on vendor blog posts. The host recommends reading the Hacker News discussion and the Confluent article for methodology. *When:* Before choosing a broker for a throughput-sensitive workload, since the results shown here flip with producer count, partitions and hardware.

## Numbers
- Kafka was built by LinkedIn in 2011, about 15 years before the video. ([0:00](https://youtu.be/tHXWAkJeWmA?t=0))
- Redpanda was released in 2021. ([0:00](https://youtu.be/tHXWAkJeWmA?t=0))
- Redpanda blog claim: 20x faster, 3 Redpanda nodes vs 4 Kafka nodes, 1 GB/s throughput, three EC2 instance types (vendor claim, not verified by the host). ([2:40](https://youtu.be/tHXWAkJeWmA?t=160))
- Confluent principal's tests: Redpanda performs well at 4 producers but worse than Kafka at 50 producers; Kafka performs better with more partitions. ([3:37](https://youtu.be/tHXWAkJeWmA?t=217))
- Kafka has about 10 years of head start over Redpanda, so a wider ecosystem and adoption. ([5:03](https://youtu.be/tHXWAkJeWmA?t=303))

## Hot takes
- Sponsored segment: a Better Stack monitoring plug (Prometheus dashboards, status pages, free tier) sits in the middle of the performance section (about 3:37 to 5:03). Quality is capped at 2 under the sponsored-segment rule.
- The host did not run any benchmarks; the performance verdict is a split taken from a vendor blog post and a rebuttal, so it is not an independent measurement.
- The title asks whether Kafka is outdated, but the video concludes it depends on the team; Kafka wins two of five categories and Redpanda two, with performance split.
- The Redpanda 20x claim is a vendor claim according to the host, and the host also describes the Confluent rebuttal as coming from a Confluent employee, so both sides have a stake.
- The 'Redpanda for me' conclusion rests on the host's dislike of the JVM, not on measured results.

## Tools mentioned
Apache Kafka, Redpanda, Redpanda Console, Redpanda Connect, Kafka Connect, Kafka Streams, MirrorMaker, ZooKeeper, Docker, Docker Compose, Kafka Python client, OpenMessaging Benchmark framework, Prometheus, Better Stack

## Relevance to our work
- **agentos** (1/3): AgentOS has an audit log and a ClickHouse analytics roadmap. A durable event bus could sit between them, but no streaming layer is in the profile today. → *If AgentOS audit or telemetry ever needs a durable event bus, benchmark Kafka vs Redpanda on your own producer and partition counts, and check that your Kafka clients connect unchanged, before choosing.*
