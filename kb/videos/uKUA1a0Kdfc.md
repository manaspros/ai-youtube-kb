# Move Fast and Don't Break Things: Scaling Databases for the AI Era — PlanetScale

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `uKUA1a0Kdfc` · [watch](https://youtu.be/uKUA1a0Kdfc) · **date:** 2026-10-07 · **length:** 19:07 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Ben · **orgs:** PlanetScale, Cursor, GitHub, Facebook
- **topics:** dev-tools, infra-cost-scaling, governance-compliance · **tags:** databases, sharding, back-pressure, schema-branching, traffic-control, failure-isolation, vitess, planetscale

> PlanetScale's Ben argues that agent-driven change can be safe if databases are isolated, sharded, back-pressured, and branched like code, with agents given the same primitives humans use.

## Summary
Ben from PlanetScale frames the talk as a way to ship fast without breaking the database layer, pointing out that AI-driven traffic growth is stressing many systems. He lists four reliability and scaling principles: isolation between data plane and other components, redundancy with primary and replica nodes, sharding across many servers, and back pressure so overloaded databases shed load instead of crashing. He argues against combining OLTP, analytics, queues and caching in one database because that couples failures and resource contention. For agents, he describes exposing sharding config as a JSON VSchema that an agent can draft from a schema, traffic tagging with resource budgets that warn and then kill queries, and git-like schema branching with deploy requests and one-click revert. He says humans still review agent changes, and that PlanetScale exposes these primitives through its API, CLI and MCP server. Much of the talk is high-level principle, and the product pitch is present throughout.

## Key ideas
- **Isolate the data plane from everything that ships often** — Control planes, observability, apps and MCP servers change more often and are likelier to fail than a well-run database. Design so a bad control-plane deploy cannot take down data-plane access. ([3:37](https://youtu.be/uKUA1a0Kdfc?t=217))
- **Redundancy is needed at scale because rare failures become frequent** — A single server might fail once every couple of years at small scale. Across thousands of servers the same rate becomes weekly or monthly, so primaries need replicas in other zones ready to take over. ([4:56](https://youtu.be/uKUA1a0Kdfc?t=296))
- **Shard through a proxy, and give each shard its own redundancy** — A proxy (VTGate for MySQL via Vitess) parses queries and routes them to shards. Each shard still needs a primary and replicas so it can self-heal when one node fails. ([6:13](https://youtu.be/uKUA1a0Kdfc?t=373))
- **Back pressure beats crashing under overload** — MySQL, Postgres and SQLite often crash when CPU, connections or cache run out. A system should detect a resource threshold, reject or slow new work, and keep existing users healthy. ([8:40](https://youtu.be/uKUA1a0Kdfc?t=520))
- **Decoupling workloads keeps failures and scaling independent** — Putting OLTP, analytics, queues and caching in one database adds convenience but couples failures and resource contention. Each part should scale on its own. ([9:44](https://youtu.be/uKUA1a0Kdfc?t=584))
- **Agents can edit sharding config because it is plain JSON** — Sharding is set through a VSchema JSON file that names the shard key and table placement. Agents are good at drafting such files from a schema, and a platform can then apply them through its API or CLI. ([13:13](https://youtu.be/uKUA1a0Kdfc?t=793))
- **Tag traffic, set budgets, warn first, then kill** — Traffic is tagged by segment and each segment gets a CPU or backend budget. Over-budget queries get a warning sent to the client and can be killed if the limit is strict. Denying some requests is better than a full outage. ([14:25](https://youtu.be/uKUA1a0Kdfc?t=865))
- **Branch the schema like code and revert without data loss** — Schema changes are made on an isolated branch and merged to production through a deploy request with no downtime. A bad schema change can be reverted in one click without losing data. The same flow is exposed to agents through APIs, CLI and MCP. ([16:39](https://youtu.be/uKUA1a0Kdfc?t=999))

## Techniques
- **Per-segment traffic budgets with graceful degradation** — Tag incoming queries by source or segment. Set a resource budget (CPU, backend processes) per segment. Send a warning to the client when a budget is exceeded, and optionally kill executing queries past a strict limit. *When:* When one noisy caller, such as an agent loop, can overload a shared database and take all users down.
- **Shard with a routing proxy plus per-shard replicas** — Put a query-routing proxy in front of many shards. Give each shard a primary and several replicas so one node failure self-heals within the shard. *When:* When one database node no longer fits the data size or query load (the speaker cites terabytes to petabytes).
- **Declarative sharding config as JSON for agent drafting** — Describe the shard key and table placement in a JSON config file. Ask an agent to propose it from the schema and workload, then review and deploy it through the platform's API or CLI. *When:* When an agent is helping plan or change how data is partitioned across shards.
- **Schema branch, deploy request, one-click revert** — Make schema changes on an isolated branch. Merge to production through a deploy request with no downtime. If a change causes problems, revert to the previous schema state without data loss. *When:* When schema changes ship alongside application code and need a reviewable, reversible path, including when agents open the PRs.
- **Isolation by failure domain** — Keep the data plane separate from control planes, observability, analytics and app deploys so a bad deploy in one domain cannot stop database access. *When:* When fast-changing services share infrastructure with critical data stores.

## Numbers
- Target availability of three to four nines, possibly five nines ([1:12](https://youtu.be/uKUA1a0Kdfc?t=72))
- Customer daily active users rising 2x, 3x, 10x or 100x within months, largely from AI agent demand ([1:12](https://youtu.be/uKUA1a0Kdfc?t=72))
- Speaker's illustration: a failure once every couple of years on one server becomes weekly or monthly across thousands of servers ([4:56](https://youtu.be/uKUA1a0Kdfc?t=296))
- Secondhand claim, from a tweet the speaker cites, that GitHub traffic rose 2-4x on top of an already very high load, mostly attributed to AI agents ([14:25](https://youtu.be/uKUA1a0Kdfc?t=865))

## Hot takes
- Most scaling failures come from coupling and missing isolation, not from raw data volume.
- Agents can take part in database operations safely if the database offers branching, deploy requests and revert, and humans still review the changes.
- Denying some requests under overload is better than a full outage for all users.

## Tools mentioned
PlanetScale, Vitess, VTGate, MySQL, Postgres, SQLite, MCP server, CLI, VSchema

## Relevance to our work
- **agentos** (2/3): Govrix budgets and the priority scheduler could use the tag-budget-warn-kill pattern, and per-tenant isolation maps to the per-segment budget idea. → *Prototype per-caller budgets in the Govrix proxy that send a warning to the client first and only kill requests past a hard limit, then test the degrade path under load in the Locust setup.*
- **general** (1/3): Having an agent draft a declarative JSON config that a human reviews before deploy is a reusable pattern for agent-written infra changes. → *Consider a rule that agent-proposed infra config must be a reviewable declarative file applied through an audited API, not a direct change.*
