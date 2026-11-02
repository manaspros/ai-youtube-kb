# Leaving AWS to Build a Better Redis w/ Roman Gershman (Dragonfly Co-Founder)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `tXdDddCgGnE` · [watch](https://youtu.be/tXdDddCgGnE) · **date:** 2025-11-02 · **length:** 16:50 · **format:** interview · **quality:** 3/5 · **depth:** intro
- **speakers:** Roman Gershman · **orgs:** DragonflyDB, AWS, Google
- **topics:** infra-cost-scaling, dev-tools · **tags:** redis, dragonfly, in-memory-datastore, rewrite-vs-fork, source-available-license, bsl, ssd-tiering, founder-interview

> Founder interview with Dragonfly's co-founder and CTO Roman Gershman on why he left AWS ElastiCache to rewrite Redis from scratch, plus the license and language choices behind it.

## Summary
Better Stack interviews Roman Gershman, co-founder and CTO of DragonflyDB, a Redis-compatible in-memory store. He describes his path from Google Suggest to AWS ElastiCache, and the year-plus internal debate that led him to leave AWS and start Dragonfly. The core technical argument is that incremental multi-threading of Redis (the KeyDB approach, per the captions) still suffers contention on multi-key transactions and Lua scripting, so he chose a full rewrite instead of a fork. He explains keeping the Redis API for ecosystem compatibility, and a source-available license that converts to Apache after four years, reset with each significant release. He also covers choosing C++ over Rust, a lean core team with a hands-on founder, and a roadmap item to use local SSDs as a transparent extension of memory. The host closes by announcing Dragonfly Swarm, which he says combines vertical and horizontal scaling. The content is mostly company history and opinion, with few benchmarks.

## Key ideas
- **Left AWS ElastiCache after more than a year of internal debate, concluding that incremental Redis improvements could not disrupt the market and that real change requires working outside the system.** — The argument was that Redis is good software that sometimes fails, and that the proposed improvements were not enough to justify a rewrite. He chose to start his own company. ([4:05](https://youtu.be/tXdDddCgGnE?t=245))
- **Rewrote from scratch rather than forking, because incremental multi-threading (KeyDB, per the captions) still ran into lock contention on multi-key transactions and Lua scripting.** — He says a full architectural redesign was the only way to cover all use cases with multi-threading, and that the incremental approach led to high contention. ([6:48](https://youtu.be/tXdDddCgGnE?t=408))
- **Kept the Redis API on purpose so the client libraries, frameworks and tooling around Redis keep working, and LLMs trained on Redis code also transfer.** — Users generally change nothing in their application; some tuning may be needed on the Dragonfly side. The host adds that LLMs' familiarity with the Redis API makes switching easier. ([6:48](https://youtu.be/tXdDddCgGnE?t=408))
- **Chose a source-available license with a time-delayed Apache conversion (four years, renewed with each significant release) over plain Apache or AGPL.** — The aim is to prevent cloud providers from capitalizing on the code right away while keeping it open for community use. He describes the arrangement as giving the company a four-year development head start on any managed service. ([8:05](https://youtu.be/tXdDddCgGnE?t=485))
- **Chose C++ over Rust: he would pick Rust at 20, but at this point learning a new language would cost about two years of building.** — He says he has since learned some Rust for another project and liked its package system, but still would not rewrite Dragonfly in it. ([9:26](https://youtu.be/tXdDddCgGnE?t=566))
- **Stays deliberately lean and hands-on: the C++ core team is under 10 people within an engineering team of about 20, and the founder answers users directly in GitHub issues and Discord.** — He says he wants no middlemen between the company and its users, and credits Redis's Salvatore Sanfilippo for the same approach. ([10:51](https://youtu.be/tXdDddCgGnE?t=651))
- **Roadmap focus is making memory cheaper by using local SSDs transparently, so the database uses memory and disk without users managing the split.** — He claims local SSDs now respond in tens of microseconds, which is fast enough for users not to notice. No benchmark is given. ([14:59](https://youtu.be/tXdDddCgGnE?t=899))
- **Host announces Dragonfly Swarm at the end, which combines vertical and horizontal scaling for terabyte-scale in-memory deployments.** — Stated by the host as a recent announcement, not discussed in depth by the founder; no benchmark or architecture details are given. ([16:09](https://youtu.be/tXdDddCgGnE?t=969))

## Techniques
- **Rewrite the core instead of forking when the bottleneck is architectural** — Founder's reasoning: if a fork adds multi-threading to a single-threaded design, multi-key transactions and Lua scripting still contend on shared state. Redesign the core around the requirements (multi-key transactions, scripting, multi-threading) and keep the external protocol. *When:* A widely used system has an interface your users depend on, but its internals cannot support the concurrency or transaction semantics you need.
- **Keep the wire API for ecosystem compatibility** — Implement the existing protocol and API faithfully and test against the surrounding client libraries and frameworks. Accept some per-deployment tuning on the new backend. *When:* Switching to a new backend for an existing stack, where client libraries, frameworks and LLM-generated code already target the old API.
- **Time-delayed source-available license** — Publish the source under a restrictive license with a fixed date (four years here) after which it converts to Apache. Push the date forward with each significant release. *When:* You want public source access and community use but want to limit managed-cloud competitors during the early years. Note the trade-off: the license is not OSI open source in the interim.
- **Stay hands-on with the community** — The founder answers issues and questions personally on GitHub and Discord instead of routing them through support. *When:* Early-stage open source where direct user feedback drives the roadmap.

## Numbers
- Google Suggest, a real-time, high-scale in-memory service the founder co-designed at Google, around 2007-2008. ([1:24](https://youtu.be/tXdDddCgGnE?t=84))
- Left Google in 2014, and left AWS around 2021 during COVID. ([2:48](https://youtu.be/tXdDddCgGnE?t=168))
- He worked nights without pay for many months while starting Dragonfly. ([5:20](https://youtu.be/tXdDddCgGnE?t=320))
- Dragonfly's source license converts to Apache after four years, renewed with each significant release. ([8:05](https://youtu.be/tXdDddCgGnE?t=485))
- C++ core team under 10 people; overall engineering team about 20. ([10:51](https://youtu.be/tXdDddCgGnE?t=651))
- Local SSDs can return data in dozens of microseconds (founder's claim, no benchmark given). ([14:59](https://youtu.be/tXdDddCgGnE?t=899))
- Learning a new language like Rust would have cost about two years of development time. ([9:26](https://youtu.be/tXdDddCgGnE?t=566))

## Hot takes
- Plain Apache or AGPL are both wrong for a database company: Apache leaves it open to cloud competitors, AGPL is too restrictive, so a time-delayed source-available license is the middle ground.
- Rewriting the core is better than forking a single-threaded database and adding threads, because the contention problems are architectural.
- Choosing a language you already know beats chasing a trendy one like Rust when the goal is to ship a product.

## Tools mentioned
DragonflyDB, Dragonfly Cloud, Dragonfly Swarm (announced by host, not detailed), Redis, Redis API, AWS ElastiCache, KeyDB (captions read it as KDB; the reference is inferred, not stated), Lua scripting, C++, Rust, Visual Studio Code, GitHub Copilot, Google Bigtable and Spanner (mentioned as Google's persistent stores), Discord, GitHub

## Relevance to our work
- **agentos** (1/3): AgentOS uses Redis in its storage layer, and the roadmap includes Redis multi-instance budget counters. Dragonfly is a Redis-compatible alternative, but this interview gives no benchmarks or workload details to justify a switch. → *If the Redis budget-counter work goes ahead, benchmark Dragonfly as a drop-in on the actual counter workload, and read its license terms before adopting it.*
