# Introduction to Node Clustering

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Nz0OfV2L5m0` · [watch](https://youtu.be/Nz0OfV2L5m0) · **date:** 2024-11-02 · **length:** 15:23 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, PM2
- **topics:** dev-tools, infra-cost-scaling · **tags:** nodejs, cluster-module, horizontal-scaling, pm2, autocannon, express, load-testing, multi-process, logging

> Better Stack tutorial on Node.js's cluster module: fork one worker per CPU core to get past single-threaded Node, benchmark the gain with autocannon (22k to 61k requests in 10s), then do the same with PM2 and note the state and logging caveats.

## Summary
The video explains that Node runs on a single thread by default, so a plain Express app uses one CPU core. It shows the cluster module: a primary process forks one worker per core, and the primary distributes incoming connections across workers, all listening on the same port. The speaker benchmarks a simple file-read endpoint with autocannon for 10 seconds, getting about 22,000 requests, then adds a cluster.js with a respawn-on-exit handler and gets about 61,000. He then installs PM2 globally, runs it with instances set to 0 (one per core), and reports roughly the same throughput. The closing section covers the main caveats: workers do not share memory or session state, so state belongs in Redis or a database; Node does not auto-detect usable cores; the primary also needs CPU; and multi-process logs should carry process identifiers, for example via Pino or Winston. The content is a basic, practical tutorial with a light plug for a newsletter and Better Stack logging, not a sponsored segment.

## Key ideas
- **Node is single-threaded by default, so a plain Node process uses one CPU core even on a multi-core machine.** — The speaker frames clustering as the fix for this: multiple instances of the same app, one per core, instead of one process handling everything. ([0:00](https://youtu.be/Nz0OfV2L5m0?t=0))
- **In cluster mode, a primary process accepts all incoming requests and distributes them across workers, with round-robin as the example strategy.** — The primary acts as a load balancer, and every worker listens on the same port (3000 in the demo), not one port per worker. ([0:48](https://youtu.be/Nz0OfV2L5m0?t=48))
- **Get a baseline before clustering, using a fixed-duration load test with a request count to beat.** — Baseline on the single-process Express app was about 22,000 requests in 10 seconds. The speaker warns that a CPU-heavy workload would show a bigger gain. ([3:04](https://youtu.be/Nz0OfV2L5m0?t=184))
- **Use os.availableParallelism() rather than the raw CPU count to size the worker pool.** — The speaker says available parallelism accounts for cores that other applications already occupy, so it is the better number for worker count. ([4:06](https://youtu.be/Nz0OfV2L5m0?t=246))
- **Add a respawn handler so a crashed worker is replaced.** — cluster.on('exit') logs the worker's pid, code and signal, then calls cluster.fork() to start a replacement on the freed core, so the remaining workers keep serving while it restarts. ([7:37](https://youtu.be/Nz0OfV2L5m0?t=457))
- **Clustering roughly tripled throughput on the demo app, from about 22k to about 61k requests in 10 seconds.** — The speaker says the same benchmark command was rerun unchanged against the clustered build. The speedup is for an I/O-light endpoint on an unstated machine. ([9:57](https://youtu.be/Nz0OfV2L5m0?t=597))
- **PM2 wraps the cluster module, so you can skip writing cluster code; instances 0 means one per core.** — pm2 start index.js with instances set to 0 gave about the same throughput (61k) as the hand-written cluster.js. The speaker recommends PM2 for its edge-case handling. ([11:03](https://youtu.be/Nz0OfV2L5m0?t=663))
- **Workers do not share memory, so session and login state must live outside the process.** — Each worker is a separate instance. The speaker advises a database or Redis for state and says cross-worker messaging is possible but he does not show it. ([13:17](https://youtu.be/Nz0OfV2L5m0?t=797))
- **Leave a core free for the primary process, and log with process identifiers in multi-process setups.** — The speaker notes that the primary also needs CPU. For debugging he suggests Pino or Winston, which add process details, and forwarding logs to a central store such as Better Stack. ([14:34](https://youtu.be/Nz0OfV2L5m0?t=874))

## Techniques
- **Hand-rolled cluster primary with respawn** — Create cluster.js. Import cluster from 'node:cluster' and os from 'node:os'. Build __dirname with fileURLToPath(import.meta.url) and dirname (the speaker reports a missing path import, which he fixes). Call cluster.setupPrimary({ exec: <path to index.js> }). Loop i from 0 to os.availableParallelism() and call cluster.fork(). Register cluster.on('exit', (worker, code, signal) => { log worker.process.pid, code and signal; cluster.fork(); }). Start it with `node cluster.js`, not `npm run start`. *When:* You want clustering with no dependencies and full control over worker lifecycle. Use it for stateless HTTP servers that are CPU-bound enough to benefit from using all cores.
- **Benchmark before and after with autocannon** — Run `npx autocannon -d 10 --renderStatusCodes http://localhost:3000/read-content` (the flags are as spoken in the video; check autocannon's help if they differ). Record the total request count and latency, make the change, and run the same command again. *When:* Before and after any scaling change, to get a comparable throughput number. Use the same machine and the same endpoint each time.
- **PM2 cluster mode** — Install globally with `npm install -g pm2`. Start the app with `pm2 start index.js -i 0`, where 0 means one instance per available core. Stop everything with `pm2 delete all`. The app code does not change. *When:* You want clustering plus restarts, process supervision and other operational features without writing cluster code. Use it when you deploy on the same machine as the app.
- **Move shared state out of workers** — Do not keep sessions, login data or counters in process memory. Store them in Redis, a database, or another shared store that all workers can reach. Cross-worker messaging exists via process.send, but the speaker only links to an article for it. *When:* Any clustered service that holds per-user or cross-request state. Apply it before scaling out, because the bugs it causes appear only under multiple workers.

## Numbers
- Single-process Express baseline: about 22,000 requests in 10 seconds with autocannon. ([3:04](https://youtu.be/Nz0OfV2L5m0?t=184))
- Clustered (cluster.js, one worker per core): about 61,000 requests in 10 seconds, roughly 2.8x the baseline. Core count and hardware are not stated. ([9:57](https://youtu.be/Nz0OfV2L5m0?t=597))
- PM2 with instances set to 0: about 61,000 requests in 10 seconds, the same as the hand-written cluster.js in this single run. ([12:16](https://youtu.be/Nz0OfV2L5m0?t=736))
- Benchmark duration used in the video: 10 seconds, one run each; no variance or repeat runs are shown. ([1:52](https://youtu.be/Nz0OfV2L5m0?t=112))

## Hot takes
- Node's cluster module plus a small respawn loop gives close to the same throughput as PM2 on this demo, so PM2 is mainly operational convenience (supervision, restarts, edge cases), not raw speed.
- The 22k-to-61k result is one unrepeated run on an unstated core count and an I/O-light endpoint. Treat the ~2.8x as illustrative, not as a general expectation.
- Shared state is the real cost of clustering: workers cannot see each other's memory, so any in-process session or counter must move to Redis or a database first.
- The speaker says to reserve a core for the primary process. The primary is light for a simple proxy, so this advice is about heavier primary workloads he did not measure.

## Tools mentioned
Node.js, cluster module (node:cluster), os.availableParallelism, Express, autocannon, PM2, Pino, Winston, Better Stack

## Relevance to our work
- **agentos** (1/3): AgentOS's Govrix proxy and budget counters are the same kind of per-process state that clustering splits across workers. The roadmap already names Redis multi-instance budget counters, and this video is a reminder why that is needed. → *Check whether per-process state in the proxy (budgets, rate counters, session routing) breaks once it runs as several workers or instances, and confirm that counters move to Redis before scaling out.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI around long runs with checkpoint and resume. A respawned worker has no in-memory state, so checkpoint state must be stored outside the process. → *Confirm that ProsHarness checkpoints live on disk or in a store, so a worker that is restarted or replaced can resume the run without in-process state.*
