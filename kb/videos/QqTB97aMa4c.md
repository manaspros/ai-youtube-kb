# How to Setup Redis Caching in Node

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `QqTB97aMa4c` · [watch](https://youtu.be/QqTB97aMa4c) · **date:** 2024-11-02 · **length:** 26:20 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** infra-cost-scaling, dev-tools · **tags:** redis, caching, node.js, express, cache-aside, lazy-loading, ttl, load-testing, artillery, write-through, write-behind, refresh-ahead, ubuntu, systemd

> A beginner Node.js tutorial that adds Redis caching to an Express endpoint, load-tests before and after with Artillery, and briefly compares cache-aside, write-through, write-behind and refresh-ahead.

## Summary
The speaker builds a Hacker News clone in Express whose search endpoint calls an external API on every request. He load-tests the baseline with Artillery (600 requests at 10 per second) and sees 91 HTTP 500s and a mean latency of about 1011 ms. He then installs a Redis server on Ubuntu, supervises it with systemd, and connects to it from Node with the redis npm client. The search endpoint is changed to a cache-aside pattern: a lowercased query key, a 300-second expiry, and hit/miss logging. The rerun has no errors and a mean of 43 ms. The video closes with a conceptual comparison of write-through, write-behind and refresh-ahead, with no code for those three. The walkthrough is clear and reproducible, but it is beginner-level and the benchmark is a best-case single-query run.

## Key ideas
- **Caching the result of an expensive, repeated request in Redis removes the duplicate calls to the database or external API.** — A first request fetches from the upstream source and stores the result in memory. Identical follow-up requests are answered from Redis until the entry expires. ([0:00](https://youtu.be/QqTB97aMa4c?t=0))
- **Baseline load test shows the uncached endpoint is slow and error-prone under repeated load.** — Of 600 requests, 91 returned HTTP 500 and the mean was about 1011 ms. The speaker guesses the 500s come from external API rate limiting, which is not verified. ([4:18](https://youtu.be/QqTB97aMa4c?t=258))
- **Cache-aside (lazy loading) is the simplest pattern, and it is the one implemented in the demo.** — Read the cache first. On a miss, fetch from the source, write the result to the cache with an expiry, and return it. The cache only holds data that has actually been requested, and the overhead is only paid on misses. ([20:13](https://youtu.be/QqTB97aMa4c?t=1213))
- **The cache key should be normalized so that trivially different requests share one entry.** — The key is a prefix plus the lowercased search query, so 'Programming' and 'programming' hit the same entry. ([12:42](https://youtu.be/QqTB97aMa4c?t=762))
- **A TTL bounds staleness: entries expire after 5 minutes, so data is refetched even if the same request keeps coming in.** — The speaker says the expiry is a trade-off, and that the right value depends on how fast the upstream data changes. ([15:24](https://youtu.be/QqTB97aMa4c?t=924))
- **Good caching targets have a high hit rate, so data that changes very fast or is rarely requested is a poor fit.** — The speaker describes the goal of caching as a high hit rate and says there is no point caching data that is requested only once a day. ([18:49](https://youtu.be/QqTB97aMa4c?t=1129))
- **Write-through writes to the database and the cache together, which gives consistency at the cost of slower writes.** — It suits data that needs integrity, where the cache and database must match. It is usually paired with lazy loading for reads. ([21:13](https://youtu.be/QqTB97aMa4c?t=1273))
- **Write-behind writes to the cache first and flushes to the database later, which speeds up writes but risks data loss.** — A batch job (the example is every 5 minutes) syncs the cache to the database. Until the job runs the two can disagree, and a crash before the flush loses data. ([23:16](https://youtu.be/QqTB97aMa4c?t=1396))
- **Refresh-ahead predicts which entries will be needed and refreshes them before they expire.** — This gives low latency when access patterns are predictable. Bad predictions add load to the database and waste cache memory. ([24:18](https://youtu.be/QqTB97aMa4c?t=1458))

## Techniques
- **Redis server setup on Ubuntu (systemd-supervised)** — sudo apt-get update; sudo apt-get install redis (as spoken in the video). Edit /etc/redis/redis.conf: comment out the 'supervised auto' line (line 327 in the speaker's file) and set 'supervised systemd'. Then sudo systemctl start redis (the speaker says restart). Verify with redis-cli, then ping, which should return PONG. Other OSes or Docker are covered by the Redis docs. *When:* Running Redis locally or on an Ubuntu server with proper service management.
- **Node client connection with error, ready and connect handling** — npm install redis. In the entry point (server.js): const redis = require('redis'); const redisClient = redis.createClient() (defaults to localhost:6379; pass a port or a URL to change it). Attach redisClient.on('error', ...) and redisClient.on('ready', ...) handlers. At startup, await redisClient.connect() and await redisClient.ping(). *When:* Any Express or Node service that needs a Redis cache, to fail fast on connection problems.
- **Cache-aside (lazy loading) on an HTTP search endpoint** — let results = null; key = 'search:' + query.toLowerCase(); value = await redisClient.get(key). If value is non-null, results = JSON.parse(value) and log 'cache hit'. Otherwise, results = await the upstream fetch (DB or external API), then await redisClient.set(key, JSON.stringify(results), { EX: 300 }) and log 'cache miss'. Return results. *When:* Read-heavy endpoints where identical requests repeat and a few minutes of staleness is acceptable.
- **Normalizing cache keys** — Build the key from a fixed prefix (for example the endpoint name) plus a canonicalized input, such as the lowercased query, so trivially different requests share one entry. *When:* User-typed or case-insensitive inputs where the same data should map to one cache entry.
- **Before and after load test with Artillery** — npm install -g artillery. Create artillery.yml with config.target = the base URL (http://localhost:3000 in the demo), and phases: duration 60, arrivalRate 10 (600 requests total). Add a scenario named 'search Hacker News for programming' that GETs /search with the query programming. Start the app with npm run start, then run artillery run artillery.yml. Read the summary report: HTTP status counts, min/max/mean and p95/p99 latency. Save the report, change the code, and run again to compare. *When:* Proving that a caching or performance change helps before merging it.
- **Write-through** — On a write, update the database and the cache in the same operation, so reads from the cache stay consistent with the database. *When:* When data integrity matters and the cache and database must match at all times. Expect slower writes.
- **Write-behind (write-back)** — On a write, update the cache first and return. A scheduled batch job (the example is every 5 minutes) flushes the cached values to the database. *When:* Write-heavy workloads where write latency matters and some data loss on failure is tolerable. Needs a flush job, and the risk of loss should be accepted.
- **Refresh-ahead** — A background job finds entries that are close to expiry, or that are predicted to be requested, and reloads them before expiry, so requests are cache hits. *When:* Low-latency endpoints with predictable access patterns. Wrong predictions add database load and waste cache space.
- **Deciding what to cache** — Cache only data that is requested often and changes slowly enough that a stale copy is acceptable. Skip data that changes too frequently or is rarely requested. *When:* Before adding any cache layer, to avoid wasting memory and adding complexity.

## Numbers
- Load test volume: 60 s at 10 requests per second, which is 600 requests for one scenario ([2:14](https://youtu.be/QqTB97aMa4c?t=134))
- Baseline (no cache): 509 HTTP 200 responses and 91 HTTP 500 responses ([4:18](https://youtu.be/QqTB97aMa4c?t=258))
- Baseline latency: min 234 ms, max 2456 ms, mean 1011 ms, p95 1790 ms, p99 2104 ms ([4:18](https://youtu.be/QqTB97aMa4c?t=258))
- With cache-aside: 600 HTTP 200 responses, min 11 ms, max 1879 ms, mean 43 ms. p95 and p99 are described as 'massively down' but not quoted. ([18:02](https://youtu.be/QqTB97aMa4c?t=1082))
- Cache entry TTL is 300 seconds (EX 300) ([15:24](https://youtu.be/QqTB97aMa4c?t=924))
- Redis default port is 6379 ([8:04](https://youtu.be/QqTB97aMa4c?t=484))
- Write-behind example batch flush interval is 5 minutes ([23:16](https://youtu.be/QqTB97aMa4c?t=1396))

## Hot takes
- The benchmark is one local run of 600 identical requests, so the 43 ms mean is a near-100% cache-hit best case. It says little about the real hit rate of a mixed workload.
- The disappearance of the 91 HTTP 500s is credited to Redis, and the speaker guesses it was external API rate limiting. That cause is not verified.
- The write-through, write-behind and refresh-ahead sections are conceptual, with no code, and the trade-offs are stated briefly.
- Beginner-level content: the caching guidance is generic, and there is no discussion of invalidation on writes, stampedes, or cache sizing.

## Tools mentioned
Redis (server, default port 6379), redis (npm client for Node.js), Node.js, Express, npm, Artillery (load testing, installed globally), redis-cli, Ubuntu (apt-get, systemd), VS Code, PM2 (npx pm2), Git (used to diff benchmark results), Hacker News API (external upstream in the demo), Docker (mentioned as an alternative)

## Relevance to our work
- **agentos** (1/3): The AgentOS roadmap already uses Redis for budget counters. The cache-aside pattern with TTL and normalized keys is the baseline approach for caching repeated retrieval or tool results, with no new idea beyond it. → *Benchmark a cache-aside layer with a TTL on repeated MemoryMesh retrieval queries, using a fixed-rate before-and-after load test like the Artillery setup shown, and record p95 and error counts.*
