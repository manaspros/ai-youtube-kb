# AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `uA4ah-dVHvU` · [watch](https://youtu.be/uA4ah-dVHvU) · **date:** 2026-10-21 · **length:** 15:39 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Gareth Yoder · **orgs:** Vanguard
- **topics:** enterprise-adoption, mcp-and-tools, data-engineering, multi-agent · **tags:** legacy-modernization, mainframe, MCP, CDC, idempotency, producer-gateway, consumer-onboarding, business-case-registry, team-brain, fix-forward, observability, migration-docs, Kafka, GraphQL, schema-registry

> Vanguard's cash-ledger modernization: exposing the legacy codebase over MCP cut a 7-day research loop to 15 minutes, with lessons on migration, idempotent producers and consumer onboarding.

## Summary
Gareth Yoder, cash program technical lead at Vanguard, describes modernizing the cash ledger behind the brokerage accounts, which handles money movement (ACH, wires, transfers) across web, mobile and batch channels. The team ran three migration pillars in parallel: data, producers and consumers. The turning point was exposing the legacy mainframe codebase through an MCP server, which turned a 7-day expert research cycle into a 15-minute prompt. For data, they used CDC and daily audits that checked row counts first, then column-level integrity. Producers were funneled through a gateway with idempotency and Snowflake-style IDs, and consumers were served by channel (GraphQL for real-time, per-consumer data-share views for batch, an at-least-once Kafka topic for streaming). The talk closes with a leadership checklist: make legacy AI-queryable, treat migration docs as product, do not lift-and-shift, adopt AI incrementally, and keep observability non-negotiable. The evidence is a single self-reported internal case study with few methodology details.

## Key ideas
- **Making the legacy codebase AI-queryable through an MCP server was the turning point: the 7-day loop for a mainframe engineer to analyze code and answer became a 15-minute prompt for product owners, tech leads and developers.** — Before this, data-schema questions went through mainframe engineers and architects. The MCP exposure made the same answers available to anyone with a prompt. ([1:35](https://youtu.be/uA4ah-dVHvU?t=95))
- **Validate a CDC data migration in two stages: strong consistency first (row-level counts), then integrity (column-level matches on amounts, account data and tax withholdings), run as daily audits.** — A dedicated team ran the audits. Every legacy attribute had to match in the modern store. ([3:01](https://youtu.be/uA4ah-dVHvU?t=181))
- **Do not over-engineer migration glue code, because it is deprecated once the migration finishes.** — The speaker treats the bridging code as temporary by design. ([4:01](https://youtu.be/uA4ah-dVHvU?t=241))
- **Producers used three legacy write paths (direct service request, an API wrapping it, and direct table inserts). All of them were funneled into one gateway that wraps cloud inserts, with idempotency and Snowflake-like IDs for consistency across multiple writers. The team did not lift-and-shift.** — Direct table inserts were the most worrying path because the team could not tell who produced some rows. ([4:01](https://youtu.be/uA4ah-dVHvU?t=241))
- **Migration docs were exposed through the same MCP server, so producer teams could ask questions by prompt instead of chatting with the team. Chat load and producer support dropped sharply. Ledger status codes became human-readable enums.** — 35 producers had to onboard. ([5:01](https://youtu.be/uA4ah-dVHvU?t=301))
- **Consumers were served by access pattern: GraphQL subscriptions for real-time reads (such as the funds-available balance), per-consumer data-share views from the warehouse for batch, and an at-least-once Kafka topic for streaming (fraud teams). Idempotent consumer operations make at-least-once delivery safe.** — A schema registry covered all three channels. Governance pushed for each consumer to see only its needed attributes. ([6:27](https://youtu.be/uA4ah-dVHvU?t=387))
- **Require each consumer to submit a business-case description, not just a three-character application code. AI can then aggregate these into a catalog of modernized use cases, rank the top business functions, and estimate the impact of an SLA breach.** — 50 consumers were onboarded this way. ([8:57](https://youtu.be/uA4ah-dVHvU?t=537))
- **Incident priority should depend on what breaks. A batch app may leave hours to respond, while a real-time API with clients on the other side has minutes to self-heal. The team is exploring linking business-use-case metadata into observability and log traces.** —  ([10:27](https://youtu.be/uA4ah-dVHvU?t=627))
- **Build a team brain: a shared knowledge store so that engineers, including new joiners, get the same context in their prompts. Fix forward in the modernized system instead of patching the legacy one, and let that make producers and consumers move to the cloud.** — Maintaining two codebases was called out as the real cost. Whitelisting is needed in the audit log during the transition. ([11:56](https://youtu.be/uA4ah-dVHvU?t=716))
- **Five leadership takeaways: make legacy AI-queryable; treat migration docs as product; reimagine rather than lift-and-shift (the hardest onboarders were the ones copying old behaviour); adopt AI incrementally; observability is non-negotiable.** — The speaker says observability matters more once the migration moves into business-as-usual operations. ([12:54](https://youtu.be/uA4ah-dVHvU?t=774))

## Techniques
- **Expose a legacy codebase to agents through an MCP server** — Make the mainframe or legacy code and its schema answerable through an MCP tool so that analysis questions become prompts. Publish the migration docs on the same server, so producers can self-serve onboarding questions. *When:* A legacy system is the bottleneck for research, schema discovery or onboarding questions from many teams.
- **Two-stage CDC migration verification** — Run CDC into the new store, then audit daily. Stage 1 checks row-level counts for strong consistency. Stage 2 checks each column for integrity (amounts, account identifiers, federal and state withholdings) against the legacy row. *When:* Migrating a financial or ledger dataset where silent drift is unacceptable.
- **Single write gateway with idempotency for all producers** — Route every legacy write path (service request, wrapper API, direct inserts) through one gateway that performs the cloud inserts. Make writes idempotent, and use Snowflake-style IDs so multiple writers stay consistent. *When:* Many producers write to one store, and some of them bypass the API layer today.
- **Consumer access matched to channel** — Use GraphQL with attribute-level subscriptions for real-time reads, per-consumer data-share views for batch, and an at-least-once event topic for streaming. Put a schema registry over all three. Make consumers idempotent so retries after a partial failure do not duplicate records. *When:* Many downstream consumers have different latency and data-scope needs and must see only their own attributes.
- **Business-case registration for consumers** — At onboarding, collect a use-case description and business justification along with the application code. Have an AI tool aggregate these into a use-case catalog, rank business functions, and attach SLA-breach impact. *When:* You need to know which business functions depend on a platform and how urgently to respond to an outage.
- **Fix forward, do not patch the legacy** — When a bug surfaces in the legacy path, fix it in the modernized system only. Use the same change as the incentive for producers and consumers to migrate. Add audit-log whitelisting for the transition period. *When:* Two codebases must run in parallel for a while.
- **Human-readable state values in the new system** — Replace legacy status codes with readable enums in the new schema, and rely on AI tools to map legacy codes to the new meaning. *When:* Migrating from coded legacy statuses to a modern schema.
- **Shared team knowledge base** — Store knowledge that engineers produce while building features in a common store, so every engineer's prompt (new or long-tenured) draws on the same context. The talk describes this as a team brain. *When:* Teams with high turnover or many engineers working on one domain.

## Numbers
- Mainframe research feedback loop cut from 7 days to about 15 minutes after the legacy codebase was exposed via MCP (self-reported). ([1:35](https://youtu.be/uA4ah-dVHvU?t=95))
- Scale: services receive up to 30 million calls per day, and clients generate about half a million ledgers per day, in an active-active multi-region system. ([1:35](https://youtu.be/uA4ah-dVHvU?t=95))
- 35 producers had to onboard to the modernized ingestion path. ([5:01](https://youtu.be/uA4ah-dVHvU?t=301))
- 50 consumers across the organization were onboarded. ([8:57](https://youtu.be/uA4ah-dVHvU?t=537))
- 90% of engineers in the cash program use the AI tools daily. ([10:27](https://youtu.be/uA4ah-dVHvU?t=627))
- Cash plus offering launched in 2022, and modernization began afterward. ([0:08](https://youtu.be/uA4ah-dVHvU?t=8))

## Hot takes
- Do not over-engineer the migration glue code, because it gets deprecated.
- Migration docs are part of the product, and producers onboard through them.
- The hardest onboarders were the teams that wanted a lift-and-shift instead of a redesign.
- Fix the modernized state, not the legacy, and let that push producers and consumers to migrate.
- The 7-day to 15-minute result is anecdotal and self-reported. The talk gives no methodology, sample size or error rates.

## Tools mentioned
MCP server (legacy codebase and migration docs exposed to AI tools), CDC (change data capture, generic), GraphQL (real-time consumer API), Kafka (event topic for inserts and updates), Schema registry (generic, for all consumer channels), Snowflake-style IDs (ID paradigm, not the product), Data warehouse data-share views (batch consumers)

## Relevance to our work
- **agentos** (1/3): Team-brain / shared knowledge base idea overlaps with MemoryMesh knowledge buckets, but it is an enterprise anecdote, not a technique to build. → *Read the MCP-over-legacy-code pattern as a reference for how to expose an internal codebase to agents in a team setting, if MemoryMesh ever ingests a codebase.*
