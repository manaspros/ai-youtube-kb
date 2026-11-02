# How AWS S3 Hit 1PB/s Using Hard Drives… This Is WILD!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `J1vEUTe4gi0` · [watch](https://youtu.be/J1vEUTe4gi0) · **date:** 2025-12-02 · **length:** 8:54 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus (Better Stack host) · **orgs:** AWS, Better Stack
- **topics:** infra-cost-scaling, data-engineering · **tags:** s3, hard-drives, erasure-coding, load-balancing, hot-partitions, storage, distributed-systems, log-structured-writes, tiering

> Explains how AWS S3 runs on hard drives at petabyte-per-second scale, using parallel erasure-coded reads, randomized placement, rebalancing and workload decorrelation to avoid hot drives.

## Summary
The video is a short explainer, based on a write-up by Stanislav Kozlovsky, of why S3 still stores data on hard disk drives. The host argues cost is the main reason: HDDs are roughly half the price of SSDs per the video, and at AWS's purchase volume that matters. HDD performance is limited by mechanical seek and rotation, so random reads are slow (about 32 MB/s per drive on his math), while sequential writes are cheap, which he likens to a log. S3's answer is to spread each object across many drives with erasure coding (described as 5 data shards plus 4 parity shards) so reads run in parallel. To avoid hot drives, S3 places new shards with the "power of two random choices" heuristic, proactively rebalances older data and new racks, and relies on the smoothing effect of many independent workloads. The host closes by saying this only works at a very large scale. The content is a secondary summary with no code, configs or measurements of its own, and some of its arithmetic does not fully reconcile.

## Key ideas
- **Cost drives the choice of HDDs over SSDs at S3 scale** — The host says HDDs stay about twice as cheap as SSDs, and at tens of millions of drives every dollar counts. He also notes HDD IOPS have stayed around 120 for 30 years. ([1:13](https://youtu.be/J1vEUTe4gi0?t=73))
- **HDD reads are bottlenecked by mechanical seek and rotation, so one drive is slow** — Access involves actuator seek (up to about 25 ms), spindle rotation (up to about 8.3 ms) and transfer. Averaged for a 0.5 MB read this gives roughly 16 ms, or about 32 MB/s per drive, a figure he says has not changed in 30 years. ([2:28](https://youtu.be/J1vEUTe4gi0?t=148))
- **Sequential, log-style writes suit HDDs, which is why S3 writes sequentially** — Consecutive on-disk layout lets the actuator stay still. The host ties this to the log structure Apache Kafka uses. Random reads are the hard case because the address location is unknown. ([2:28](https://youtu.be/J1vEUTe4gi0?t=148))
- **Erasure coding turns one object into parallel reads across many drives** — The object is split into K data shards plus M parity shards and can be rebuilt from any K. He says S3 uses 5 data plus 4 parity. Reading in parallel sums the throughput of all the drives involved, which is how aggregate speed reaches about 1 PB/s. ([3:29](https://youtu.be/J1vEUTe4gi0?t=209))
- **Power of two random choices places new data without a global view of load** — Finding the least-loaded drive across millions is impractical, so S3 picks two random disks and writes to the one with more free space. The host calls this a well-studied load-balancing result. ([5:57](https://youtu.be/J1vEUTe4gi0?t=357))
- **Rebalancing targets the hotness of new data and new hardware** — Newer data is usually hotter, so S3 proactively rebalances older data. New racks start empty and are rebalanced too, which spreads load and avoids cascading hot disks. ([6:54](https://youtu.be/J1vEUTe4gi0?t=414))
- **Workload decorrelation makes large systems more predictable** — Single tenants burst unpredictably, but independent workloads rarely peak together. Adding workloads fills idle capacity and smooths aggregate load. The host concludes this only works at very large scale. ([7:48](https://youtu.be/J1vEUTe4gi0?t=468))

## Techniques
- **Erasure-coded striping for parallel reads** — Split each object into K data shards and M parity shards, spread them across many independent drives, and rebuild from any K shards. The video's example is 5+4 for S3, and reads fan out across the shards to sum their throughput. *When:* When single-device throughput or latency is the bottleneck and you need durability without full replication.
- **Power of two random choices for placement** — For each new shard, sample two candidate devices at random and place it on the one with more free space or lower load. No global load map is needed. *When:* When finding the globally least-loaded node is too expensive across a large fleet and you want cheap, near-balanced placement.
- **Proactive rebalancing by data age and new capacity** — Treat newer data as hotter and migrate older data in the background as routine. Immediately rebalance newly added empty racks so they are not idle or overloaded. *When:* When access frequency correlates with age, or when capacity is added in large batches.
- **Workload aggregation to smooth bursts** — Co-locate many independent tenants on shared infrastructure so their peaks do not coincide, and the aggregate load becomes predictable enough to plan capacity against. *When:* When you run a shared multi-tenant service and individual workloads are bursty.

## Numbers
- S3 stores more than 400 trillion objects ([0:00](https://youtu.be/J1vEUTe4gi0?t=0))
- S3 handles about 150 million requests per second ([0:00](https://youtu.be/J1vEUTe4gi0?t=0))
- S3 reaches more than 1 PB/s aggregate throughput, using tens of millions of hard drives ([0:00](https://youtu.be/J1vEUTe4gi0?t=0))
- HDDs are about twice as cheap as SSDs per the video ([1:13](https://youtu.be/J1vEUTe4gi0?t=73))
- HDD IOPS stuck around 120 for the past 30 years ([1:13](https://youtu.be/J1vEUTe4gi0?t=73))
- Seek up to 25 ms, rotation up to 8.3 ms, transfer about 2.5 ms for 0.5 MB ([2:28](https://youtu.be/J1vEUTe4gi0?t=148))
- Average read latency about 16 ms for 0.5 MB, roughly 32 MB/s per drive ([3:29](https://youtu.be/J1vEUTe4gi0?t=209))
- Example: a 1 TB file spread across 20,000 drives ([3:29](https://youtu.be/J1vEUTe4gi0?t=209))
- S3 erasure coding uses 5 data shards and 4 parity shards ([4:50](https://youtu.be/J1vEUTe4gi0?t=290))

## Hot takes
- The headline 1 PB/s is aggregate across the whole fleet, not what one object or client sees. The title's framing can make it sound like a single-stream speed.
- The arithmetic does not fully reconcile. Worst-case seek, rotation and transfer add to about 36 ms, while the stated average is about 16 ms, and the video does not show how the average was derived.
- The 'SSDs move electricity at about 50% of light speed' framing is a loose analogy. The concrete numbers in the video are about mechanical limits, not signal speed.
- The 5+4 erasure-coding parameters and the cost ratio are taken from a secondary article and are not checked in the video.
- 'It only works if you're a billion-dollar company' is editorial, not a measured claim.
- Format is a secondary explainer with no code, config or first-hand measurement. Quality is capped around 3 because it adds little beyond the original article, though the mechanisms are well explained.

## Tools mentioned
Amazon S3, Apache Kafka (referenced as an example of log-structured writes)

## Relevance to our work
- **agentos** (1/3): Tiered storage in the L3 roadmap (Parquet/DuckDB archive) needs a hot-versus-cold placement rule, and the video gives age-based hotness and proactive migration as the frame. → *When designing the Parquet/DuckDB archive tier, use data age as the hotness signal and plan a background migration of cold partitions, then read Kozlovsky's S3 article for the original numbers.*
