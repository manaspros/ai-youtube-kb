# Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zkX03APVj0M` · [watch](https://youtu.be/zkX03APVj0M) · **date:** 2026-08-18 · **length:** 16:33 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Joseph Wang, Sid · **orgs:** Emulated
- **topics:** sandboxing-execution, training-finetuning-rl, evals · **tags:** rl-environments, sandboxes, long-horizon-tasks, infrastructure-engineering, post-training, multi-node-simulation, sim-to-real-gap, data-quality

> Joseph Wang of Emulated argues that agent training needs realistic infra environments: multi-node sandboxes that touch real cloud resources, not single-container coding tasks.

## Summary
Joseph Wang (co-founder of Emulated, with co-founder Sid) presents a data lab that builds environments for training more autonomous agents. The core claim is that model gaps are data gaps, and that current benchmarks only cover code-base tasks, while real engineering also involves tickets, postmortems, deployments, failing nodes, and blast radius on live traffic. He shows that simulating a distributed cluster inside one sandbox gets part of the way but breaks down once you need provisioning, host APIs, auth, deployments, and networking. His proposed next step is a multi-node sandbox wired to real cloud resources, which he calls a "CloudBox", and he says post-training pipelines can run inside it. He is open about the unsolved problems: cost, spin-up time (a full Lambda-like stack can take hours), and keeping a sim-to-real gap that still reflects live traffic. He explains the choice of infrastructure as the first domain: domain expertise improves data quality, and infra customers' requirements are clear. The talk is a recruiting-flavoured company intro, so it offers a clear thesis but few hard numbers.

## Key ideas
- **Model capability gaps are usually data gaps** — The speaker says model capability has not regressed when more high-quality data is added. Current frontier benchmarks (he names SWE-bench Pro and TerminalBench) only test work inside a code base, over 50 to 100 turns, producing a PR of a couple thousand lines. Real engineers also talk to customers, run performance tests, and own infra over years. ([2:28](https://youtu.be/zkX03APVj0M?t=148))
- **Realistic environments need the work around the code** — A realistic environment includes tickets, projects, postmortems, and customer history, which may be out of date. It also includes rolling deployments that can conflict or fail, failing and stale nodes during hardware migration, and live traffic that must not go down. The agent must reason through these problems in real time. ([5:00](https://youtu.be/zkX03APVj0M?t=300))
- **A single-node sandbox can simulate a cluster, but only partly** — The team runs multiple simulated nodes, flapping nodes, and lagging learners in one sandbox, such as an etcd consensus cluster. Chaining several deployments makes the task longer. The speaker says this is still not enough, since standard post-training pipelines use one containerized sandbox each. ([6:24](https://youtu.be/zkX03APVj0M?t=384))
- **Single-node sandboxes break down as services grow** — A service that serves one customer on one machine needs host and resource provisioning (VPCs, subnets, security groups), a customer-facing API with throttling, auth, and audit, software deployment with gradual rollout and rollback, health monitoring that accounts for partitions, DNS and certs, billing, and admin tooling. Past a certain point, one node cannot represent this. ([8:25](https://youtu.be/zkX03APVj0M?t=505))
- **The next environment is a multi-node sandbox with real cloud resources** — The proposal is a sandbox that provisions real infra. The speaker calls it a CloudBox. A post-training pipeline can run inside it, which the speaker links to model training and recursive self-improvement, though he runs short on time to explain this. ([11:05](https://youtu.be/zkX03APVj0M?t=665))
- **Start with infra because domain expertise sets data quality** — Infra is the first domain because the founders know it well, and because infra customers (such as GPU sandbox providers) have clear problem statements. The speaker says lessons from going deep on one vertical should carry over to other domains. He also says infra has become popular again in 2026. ([14:19](https://youtu.be/zkX03APVj0M?t=859))
- **Open problems: cost, spin-up time, and fidelity** — Spinning up a full stack for something like AWS Lambda can take hours, which makes it hard to fit into post-training rollouts. Cost is open. The team still has to show that the sim-to-real gap is closed, and that issues appear only at real scale and with live traffic. ([12:28](https://youtu.be/zkX03APVj0M?t=748))

## Techniques
- **Multi-node cluster simulation in one sandbox** — Run several simulated nodes inside one container, and inject flapping nodes, lagging learners, and deployment steps to create operational failures (for example, an etcd consensus cluster). *When:* Use when you need a cheap, reproducible distributed-systems environment for agent training and cannot yet use real infra.
- **Chained multi-deployment episodes for long horizon** — Lengthen one task by splitting it into several sequential deployments, so the agent has to handle each stage and the effects of the earlier ones. *When:* Use when a single task finishes too quickly and you need the agent to learn over a longer horizon.
- **Organisation context as part of the environment** — Include tickets, project history, postmortems, and simulated customer conversations in the environment, so the agent must read them before making a change. *When:* Use when the agent's work should reflect real engineering context, not just the source code.
- **Multi-node sandbox on real cloud resources (CloudBox)** — Let the sandbox provision real hosts, networks, and APIs, and run the post-training pipeline inside that sandbox. *When:* Use when single-node simulation can no longer capture provisioning, deployment, or blast-radius behaviour and you can afford the cost of real infra.
- **Choose a vertical with clear customer requirements first** — Start with one domain (here infra) where customer requirements are well defined, so the environment and its success criteria are easier to specify, then expand to other domains. *When:* Use when designing RL or eval environments and deciding where to start.

## Numbers
- Current frontier coding benchmarks: about 50 to 100 agent turns to produce a PR of roughly a couple thousand lines, all inside one code base ([2:28](https://youtu.be/zkX03APVj0M?t=148))
- Spinning up the full stack for an AWS Lambda-like serverless service takes hours ([12:28](https://youtu.be/zkX03APVj0M?t=748))
- Speaker's example of a recent DynamoDB outage that took down US-EAST-1 and much of the internet; the talk gives no numbers ([1:13](https://youtu.be/zkX03APVj0M?t=73))

## Hot takes
- Model capability has never regressed when more high-quality data is added, so the gap is a data gap.
- Current post-training pipelines are boring and homogeneous: everything runs in a single containerised sandbox, which does not reflect how real companies run.
- Beyond a certain scale, sandboxing on a single node can only get you so far.
- Software is never finished: investors often forget that deployment, rollback, and ongoing ops are part of the job.

## Tools mentioned
Harbor, etcd, Kubernetes, AWS Lambda

## Relevance to our work
- **agentos** (1/3): Crucible runs sandboxed code on a single celld backend; the talk's case for multi-node, real-infra sandboxes is a design reference for future Crucible scope, not a near-term change. → *Read the talk's multi-node sandbox argument before scoping any multi-node or cloud-backed mode for Crucible.*
- **prosharness** (1/3): Its long-horizon idea (chained deployments with failures and rollback) resembles ProsHarness checkpoint/resume runs, but the talk does not describe any harness. → *Consider adding a multi-step test to ProsHarness checkpoint/resume: deploy, inject a failure, roll back, then resume.*
- **general** (1/3): The talk argues that code-repo benchmarks miss the non-code parts of engineering, which matters for designing agent evals. → *When designing agent evals, include tasks that require reading tickets or postmortems, not just code-repo PRs.*
