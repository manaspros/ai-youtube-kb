# Neon: The FUTURE of Postgres? Branching, HTTP Queries, and More!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `7KglfRnIlfc` · [watch](https://youtu.be/7KglfRnIlfc) · **date:** 2025-11-02 · **length:** 4:22 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Neon, Cloudflare, GitHub
- **topics:** dev-tools, infra-cost-scaling · **tags:** serverless-postgres, scale-to-zero, cold-start, copy-on-write-branching, time-travel, serverless-driver, http-sql, edge-functions, cloudflare-workers, hono

> Short Better Stack review of Neon serverless Postgres, covering scale-to-zero compute, copy-on-write branches, time travel, and an HTTP driver for edge runtimes; mostly feature claims with one Cloudflare Worker demo.

## Summary
The host presents Neon, a serverless Postgres platform, as a strong option for new projects, based on three features. First, compute scales to zero when idle, so the user pays only for storage; the host measured about 3 s to suspend and about 967 ms to resume, though most of the resume latency came from a UK-to-Ohio network path. Second, branches are created instantly by pointing a new compute at the same storage, so only changed chunks are stored; this supports per-environment and per-PR isolation with a GitHub integration. Third, Neon's architecture (object storage, safekeepers writing WAL, a page server) lets the user restore or time-travel to a past point. The host also explains that TCP is hard on edge runtimes, so Neon's serverless driver speaks HTTP or WebSockets to a proxy that talks TCP to the database. A short Cloudflare Worker built with Hono runs a query with no extra TCP code. The video contains no pricing, no benchmarks beyond one latency measurement, and no setup commands; the "most cost-effective" claim is asserted, not shown.

## Key ideas
- **Storage and compute are decoupled, and Neon compute scales to zero, so an idle database costs only storage.** — Many providers either couple storage and compute (you pay for both while idle) or decouple them but still bill some idle compute for instant availability. Neon suspends compute completely. ([0:00](https://youtu.be/7KglfRnIlfc?t=0))
- **Cold start has a measurable cost: suspend and resume timings from an idle database.** — The host saw about 3 s to suspend compute, then about an hour idle, then resume in roughly 967 ms (auto-caption reads 'nine six seven milliseconds'). Most of the resume latency was network distance, since the app is in the UK and the database is in Ohio. ([1:30](https://youtu.be/7KglfRnIlfc?t=90))
- **Branches are instant because they are copy-on-write pointers to shared storage, similar to Git.** — A new branch creates a new compute layer that points at the main branch's storage. Only data changed on the branch is written as new chunks. The host suggests using this for isolating dev environments or PRs, especially with the GitHub integration. ([1:30](https://youtu.be/7KglfRnIlfc?t=90))
- **Time travel and restore come from the storage design, not from extra snapshots.** — Neon writes changes through safekeepers using the write-ahead log, stores data in object storage (S3-like), and a page server reconstructs data at any requested point. The host says this also avoids duplicating storage, which reduces cost. ([2:53](https://youtu.be/7KglfRnIlfc?t=173))
- **Serverless edge runtimes can't use plain TCP, so Neon's serverless driver tunnels queries over HTTP or WebSockets through a proxy.** — The proxy holds the TCP connection to Postgres. The host argues TCP is reliable and persistent, but edge platforms such as Cloudflare Workers may not support it or make it hard to configure. ([2:53](https://youtu.be/7KglfRnIlfc?t=173))
- **Demo: a deployed Cloudflare Worker (Hono) queries Neon and returns JSON with no TCP-specific code.** — The host opened the deployed worker's dashboard to show the query result. The video does not show the connection code or the driver setup, so a reader must check the Neon docs for the driver package and connection string format. ([2:53](https://youtu.be/7KglfRnIlfc?t=173))

## Techniques
- **Per-PR or per-environment database branches** — Create a Neon branch in the UI or with the Neon CLI (the video does not show commands). Each branch is a new compute on shared storage, so writes stay isolated and the branch is created without copying data. With the GitHub integration, a branch can be tied to a PR. *When:* When each PR, test run, or dev environment needs its own database state without a full copy.
- **Scale-to-zero for idle databases** — Let compute suspend when idle so only storage is billed. Budget for a cold start on the first request after idle; the video measured roughly 1 s to resume, plus network latency to the database region. *When:* For low-traffic or dev/staging databases where idle cost matters more than first-request latency, and where the app is in the same region as the database.
- **Query Postgres from edge runtimes over HTTP/WebSocket** — Use Neon's serverless driver inside the edge function (the video demo used a Cloudflare Worker with Hono). The driver sends queries over HTTP or WebSockets to Neon's proxy, which speaks TCP to Postgres. No custom TCP code is needed. *When:* When the runtime (Cloudflare Workers, edge functions) cannot open or reliably keep raw TCP connections to Postgres.
- **Point-in-time restore and time travel** — Use Neon's restore or time-travel feature to return the database to an earlier state or read it at a past point. The video describes the mechanism (WAL, safekeepers, page server) but gives no command or UI steps. *When:* For recovering from bad writes or migrations, or for inspecting past data, without taking manual snapshots.

## Numbers
- Compute suspend took about 3 seconds after idle. ([1:30](https://youtu.be/7KglfRnIlfc?t=90))
- The host went about an hour without activity before resume; resume took about 967 ms (auto-caption reads 'nine six seven milliseconds'). Latency includes the UK-to-Ohio network path. ([1:30](https://youtu.be/7KglfRnIlfc?t=90))
- Idle cost is storage only, because compute scales to zero. No pricing or free-tier limits are given. ([0:00](https://youtu.be/7KglfRnIlfc?t=0))

## Hot takes
- The host calls Neon 'the most cost-effective and performance solution out there' with no pricing or benchmark data in the video.
- The 'FUTURE of Postgres?' title is hype; the content is a four-minute feature tour of one vendor with no comparison to other providers.
- The one latency figure is confounded by the UK-to-Ohio network path, so it does not isolate Neon's resume time.
- The host says Neon is now his 'go-to' for all future projects, a personal opinion with no stated sponsorship or evaluation method.
- Quality is capped at 2 under the hype-title rule: thin substance, no steps, and a vendor-favorable framing.

## Tools mentioned
Neon (serverless Postgres), Neon CLI, Neon serverless driver (HTTP/WebSocket to TCP proxy), Cloudflare Workers, Hono, GitHub integration, Vercel edge functions (caption reads 'cell edge functions'; the host does not name a provider)

## Relevance to our work
- **agentos** (1/3): AgentOS's L3 storage roadmap uses Postgres/pgvector. Copy-on-write branches could isolate per-run eval or benchmark databases, but the video says nothing about pgvector or self-hosting. Neon is hosted, while AgentOS is self-hosted. → *Check whether Neon's copy-on-write branching would give each MemoryMesh eval or benchmark run an isolated Postgres, and confirm pgvector support in the Neon docs (the video does not cover it).*
