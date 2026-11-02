# Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Bck7ABCZRZI` · [watch](https://youtu.be/Bck7ABCZRZI) · **date:** 2026-08-18 · **length:** 7:52 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Thiyagarajan Maruthavanan · **orgs:** Kalmantic Labs, Anthropic, OpenAI, Suno, Uber, Netflix
- **topics:** token-cost-efficiency, local-ai, infra-cost-scaling, governance-compliance · **tags:** inference cost, token budget, self-hosting, DGX Spark, API key theft, rent vs own, input compression, enterprise audit, JustTokenMax

> Thiyagarajan Maruthavanan (Kalmantic Labs) argues teams should rent inference to learn and own it to earn, using his own runaway-cost incident and enterprise objections to self-hosting as evidence.

## Summary
The speaker says usage-priced inference is hard to budget: prepaid credits feel like casino chips, and spend passes the limit people set in their heads. He describes building Ultrasono, a reverse Suno app that finds a prompt for a given song, which went viral and ran up hundreds of thousands of dollars in inference. A stolen API key pushed spend from about $7,000 to $10,000 before it was stopped, and he estimates it could have reached $100,000. He blames waste on missing input compression, repeated calls in agent loops, and endpoints that do not know the shape of the workload. He moved the app to a local DGX Spark, found memory to be the bottleneck, and then heard from three enterprises (a fund, a hospital, a tax practice) that had objections to renting or to third-party inference: rate-limit control, audit vendor flags, and reproducing recommendations. His rule is to keep renting before product-market fit and to own infrastructure once a use case is proven or budgeted. He says optimization is possible even while renting, and he promotes his open-source JustTokenMax, which he says beats Headroom, though the talk gives no benchmark numbers. The talk closes with the line "rent to learn, own to earn."

## Key ideas
- **Usage-priced inference is hard to budget** — Prepaid credits encourage overspending, and a large retailer reportedly spent close to $200M with Anthropic. The speaker also cites an Uber budget that ran out by month four. ([0:00](https://youtu.be/Bck7ABCZRZI?t=0))
- **A stolen key can run up costs fast with no cap** — Spend climbed in steps from about $7k to $7.5k to $8k. It was stopped at $10k, and the speaker estimates it could have reached $100k. ([1:13](https://youtu.be/Bck7ABCZRZI?t=73))
- **Waste comes from missing compression and agent loops** — Input tokens are often not compressed, agent loops make many wasteful calls, and the inference endpoint does not know the shape of the workload. ([1:13](https://youtu.be/Bck7ABCZRZI?t=73))
- **Self-hosting on a small box works until memory limits it** — Moving the app from Anthropic to a local DGX Spark worked well, but memory was the bottleneck. The speaker then ran more agents on the same box. ([2:29](https://youtu.be/Bck7ABCZRZI?t=149))
- **Enterprises object to renting for three different reasons** — A fund wanted to control its own rate limits. A hospital failed an audit because a third-party vendor dependency was flagged. A tax practice needed to reproduce recommendations, which requires access to the model internals. ([3:51](https://youtu.be/Bck7ABCZRZI?t=231))
- **Decision rule: rent before product-market fit, own after** — Pre-PMF startups can rent to test demand. Post-PMF companies, and enterprises with a budgeted project, should build their own inference. He compares this to renting in a city before buying a house. ([5:17](https://youtu.be/Bck7ABCZRZI?t=317))
- **Optimization is available even while renting** — Input cost, token management and context management can all be improved before any hardware purchase. The speaker open-sourced JustTokenMax for this and says it beats Headroom, though no numbers are given. ([5:17](https://youtu.be/Bck7ABCZRZI?t=317))
- **Ignore conflicting vendor predictions** — Jensen, Satya Nadella and inference-endpoint providers each predict a different future. The speaker says market rules change every three to six months, so each team has to work out its own answer. ([6:40](https://youtu.be/Bck7ABCZRZI?t=400))

## Techniques
- **Per-key spend monitoring with a cutoff** — Track cumulative inference spend per API key and watch for rising trends. Alert early and revoke or cap the key when spend rises unexpectedly, not only when a total budget is hit. *When:* Any shared or public API key, or any endpoint where a leaked key could run up large costs.
- **Input compression and context management in agent loops** — Compress input tokens and trim context before each model call, especially in agent loops that make many calls. *When:* Agents or loops where the same context is sent repeatedly and inputs are large.
- **Rent-to-own decision gate** — Rent inference while the use case is unproven. Before committing to self-hosting, check audit and vendor-dependency rules, rate-limit control, and whether outputs must be reproducible. *When:* Deciding whether to move from a hosted API to self-hosted inference, especially in regulated or enterprise settings.
- **Small local inference box for personal agents** — Run the model on a single desktop-class box such as a DGX Spark, then host the agents there. Memory is the limit to watch. *When:* Low-volume research or personal agents where cost matters more than throughput.

## Numbers
- A large retailer reportedly spent close to $200M on inference with Anthropic before building its own infrastructure. ([0:00](https://youtu.be/Bck7ABCZRZI?t=0))
- Uber reportedly exhausted a yearly token budget by month four (cited news, not verified in the talk). ([0:00](https://youtu.be/Bck7ABCZRZI?t=0))
- Ultrasono reached hundreds of thousands of users and cost hundreds of thousands of dollars in inference. ([1:13](https://youtu.be/Bck7ABCZRZI?t=73))
- A stolen key moved spend from about $7,000 to $7,500 to $8,000, and it was stopped at $10,000. The speaker estimates it could have reached $100,000. ([1:13](https://youtu.be/Bck7ABCZRZI?t=73))
- The speaker says the key was stolen three weeks before the talk. ([1:13](https://youtu.be/Bck7ABCZRZI?t=73))
- Rules of the AI market change every three to six months. ([6:40](https://youtu.be/Bck7ABCZRZI?t=400))

## Hot takes
- Usage-priced inference works like prepaid casino credits: people overspend without noticing.
- Rent to learn, own to earn.
- Once a use case has product-market fit, building your own inference infrastructure is not optional.
- Enterprises will not accept a third-party inference dependency because of audit and reproducibility needs.

## Tools mentioned
DGX Spark, Headroom, JustTokenMax, JustInfo, Suno, NemoClaw

## Relevance to our work
- **agentos** (2/3): AgentOS already has budgets and a proxy layer (Govrix Scout). The talk's key-theft case shows that a total cap alone may not catch a leaked key draining spend. → *Test Govrix budget enforcement with a stolen-key scenario: spend rising in steps from $7k to $10k should trigger a per-key cutoff, and add a spend-velocity alert alongside the total cap.*
- **prosharness** (1/3): ProsHarness runs long Claude Code agent loops. The talk says repeated calls and uncompressed context waste tokens in loops like these. → *Log tokens per loop iteration to find repeated calls and context growth.*
