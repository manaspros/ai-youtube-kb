# I Turned Cheap Cloud Storage Into a 1PB Local Drive (With JuiceFS)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ZoBEQWxosGg` · [watch](https://youtu.be/ZoBEQWxosGg) · **date:** 2026-07-02 · **length:** 10:35 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Andres (Better Stack) · **orgs:** Better Stack, JuiceFS, AWS, Google Cloud, Backblaze, ngrok
- **topics:** dev-tools, infra-cost-scaling, observability · **tags:** juicefs, object-storage, s3, distributed-filesystem, redis, local-cache, nas, kubernetes, prometheus, ngrok, dd-benchmark, macfuse

> Walkthrough of JuiceFS, a POSIX file system that stores data in cheap S3-style object storage with metadata in Redis and a local SSD cache, plus wiring its Prometheus metrics into Better Stack.

## Summary
Andres from Better Stack introduces JuiceFS as an open-source distributed file system that keeps file data in object storage (S3, GCS, Backblaze B2) and file metadata in a separate database (Redis, Postgres or TiKV). He sets up a home NAS-style volume with Redis as the metadata engine and an S3 bucket as the data store, running format and then mount. The mounted directory behaves like a local drive, and the first read of a file fetches 4 MB chunks over the network while later reads are served from a local NVMe/SSD cache. A dd benchmark shows the cold read taking a while and the warm read under a second. The video then claims the same setup suits shared Kubernetes volumes and ML training data that streams instead of being downloaded first, without benchmarks. The last section exposes the mount's built-in Prometheus metrics through an ngrok tunnel into Better Stack and generates a dashboard with Better Stack's AI SRE feature. The technical core is accurate but shallow, with one anecdotal benchmark and no cost, latency or throughput numbers.

## Key ideas
- **JuiceFS splits storage: raw file chunks go to the object store, while the file system layout, permissions and metadata live in a fast database such as Redis, Postgres or TiKV.** — This separation is the basis for the rest of the talk and is what lets POSIX semantics sit on top of object storage. ([0:00](https://youtu.be/ZoBEQWxosGg?t=0))
- **Files are broken into small blocks and a local NVMe/SSD partition acts as a hot cache, so the first read goes over the network and repeat reads are served locally.** — The speaker frames this multi-tier caching as the main difference from cloud gateways and plain network shares. ([1:01](https://youtu.be/ZoBEQWxosGg?t=61))
- **The format step only writes the schema into the metadata database and assigns a UUID to the volume. It does not change anything in the bucket yet.** — Data objects are created later, as files are written through the mount. ([1:59](https://youtu.be/ZoBEQWxosGg?t=119))
- **After mounting, the volume looks like a standard POSIX drive, and files written to it appear in the S3 bucket as split data chunks.** — The speaker does not say how chunks are named or laid out in the bucket. ([4:08](https://youtu.be/ZoBEQWxosGg?t=248))
- **A repeated read of the same large file takes under a second, because the first pass warmed the local cache.** — This is a single anecdotal dd run on one video file. No variance, throughput or cache-hit numbers are given. ([5:36](https://youtu.be/ZoBEQWxosGg?t=336))
- **The speaker pitches shared persistent volumes across Kubernetes pods and streaming ML training from S3 without a full local download, but he demonstrates neither.** — These are claims about use cases, not measured results. ([6:50](https://youtu.be/ZoBEQWxosGg?t=410))
- **Each mount exposes a local Prometheus-compatible metrics endpoint with cache hits, read durations and S3 request errors. Better Stack can scrape it through an ngrok tunnel.** — The tunnel needs a custom ngrok-skip-browser-warning header so the scraper gets raw metrics instead of the warning page. ([8:03](https://youtu.be/ZoBEQWxosGg?t=483))
- **Better Stack's AI SRE was prompted to build a cache and throughput dashboard from the scraped JuiceFS metrics.** — This is a vendor feature demo and is the weakest-evidenced part of the talk. ([9:19](https://youtu.be/ZoBEQWxosGg?t=559))

## Techniques
- **JuiceFS volume with Redis metadata and S3 data** — 1) Start Redis in Docker (the exact docker run command is shown on screen and not spoken). 2) Create an S3 bucket plus access key and secret key. 3) Run `juicefs format` with the Redis connection URL, the S3 bucket name and the credentials; this writes the schema to Redis and assigns a UUID. 4) Run `juicefs mount` with the Redis URL and a local directory path, adding the free-space-ratio flag (default 20 percent) so the cache is purged before the disk fills. 5) On macOS, install macFUSE first. Volume name and exact flag names are not spoken in the transcript. *When:* When you want a cheap object store to act as a local NAS or shared POSIX volume for legacy apps that cannot use the S3 API.
- **Cold vs warm read benchmark with dd** — Run `time dd if=<large file on the JuiceFS mount> of=/dev/null bs=4M`, first right after upload (cold), then again (warm). The speaker sets bs=4M to match JuiceFS's chunk size. Compare the two wall-clock times. *When:* To check whether the local cache helps for a given workload before relying on it.
- **Scraping JuiceFS metrics into a hosted dashboard** — The mount serves Prometheus-format plain text on a local port, which the speaker opens in a browser (port not spoken). Expose it with an ngrok tunnel. In the scraper's advanced options add the custom HTTP header `ngrok-skip-browser-warning: true`. Add the tunnel URL as a Prometheus scrape source in Better Stack. *When:* When you need cache hit, latency and S3 error metrics for a JuiceFS mount without running your own Prometheus server.

## Numbers
- Object storage is described as cost-effective, with S3, GCS and Backblaze B2 named. No prices are given. ([0:00](https://youtu.be/ZoBEQWxosGg?t=0))
- Default free-space ratio for the local cache is 20 percent of the drive, which the speaker calls high. The flag is set lower in the demo. ([2:56](https://youtu.be/ZoBEQWxosGg?t=176))
- Block size is 4 MB for both the JuiceFS chunks and the dd benchmark. ([4:08](https://youtu.be/ZoBEQWxosGg?t=248))
- The mounted drive appears to have 1 TB of free space in the demo, while the title says 1 PB. ([4:08](https://youtu.be/ZoBEQWxosGg?t=248))
- The warm second read of the benchmark file finishes in under 1 second. The cold read time is not stated. ([5:36](https://youtu.be/ZoBEQWxosGg?t=336))
- The Better Stack scrape interval is described as every few seconds, with no exact number. ([8:03](https://youtu.be/ZoBEQWxosGg?t=483))

## Hot takes
- Title says 1PB but the demo shows a 1 TB drive, which is a bit misleading; the 1 PB is only the theoretical object-store capacity.
- The Better Stack dashboard section is product promotion for the channel's own platform, and it is the least substantiated part.
- Benchmark evidence is one dd run on one file, with no cold-read number, no variance, and no comparison with other options.
- Storage cost and egress charges, which dominate S3-backed setups, are not mentioned at all despite the cheap-storage pitch.
- Claims about Kubernetes shared volumes and ML training streaming are asserted, not shown.

## Tools mentioned
JuiceFS, Redis, PostgreSQL, TiKV, Amazon S3, Google Cloud Storage, Backblaze B2, Docker, macFUSE, dd, ngrok, Prometheus, Kubernetes, Better Stack, Better Stack AI SRE

## Relevance to our work
- **agentos** (1/3): AgentOS's roadmap has a Parquet + DuckDB archive tier on storage, and this video covers a cache-over-object-store design that could be compared for that. Otherwise it is off-topic for the agent gateway and the model-serving work. → *Benchmark cold vs warm reads of the Parquet archive through a JuiceFS mount against direct S3 reads, with DuckDB queries, before choosing a read tier.*
