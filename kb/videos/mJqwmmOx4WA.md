# How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `mJqwmmOx4WA` · [watch](https://youtu.be/mJqwmmOx4WA) · **date:** 2026-09-18 · **length:** 17:49 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrew Garvin · **orgs:** Stripe, Metronome, Lovable, HubSpot, OpenAI, Anthropic, Vercel, Hugging Face, Salesforce, Andreessen (demo day), Cognition, Cursor
- **topics:** governance-compliance, vibe-coding-app-building, coding-agents, product-ux · **tags:** billing, usage-based-pricing, credits, metering, stripe-projects, skills-files, sandbox-testing, agent-as-buyer, agent-as-user, vibe-coding, live-demo

> Andrew Garvin (Metronome, now part of Stripe) live-demos using Stripe Projects and a Metronome billing agent to build a usage-based billing setup from one natural-language prompt, arguing for sandboxed agent-built billing and for usage or credit pricing when agents are the users.

## Summary
The speaker co-founded Metronome, a usage-billing platform that he says was acquired by Stripe. He presents Stripe Projects, a CLI orchestrator that provisions a Stripe account plus back-end services such as Postgres, Vercel, and a Metronome billing agent. In a live demo he prompts the agent to replicate Lovable's credits-plus-auto-recharge pricing as a sandbox billing engine, then shows the resulting customer, credit, and draft invoice in the Metronome UI. His main advice is to use coding agents to accelerate work in test environments rather than operate billing in production unsupervised, and to make the test meaningful by flowing synthetic usage through it. He frames three agent roles (agent as product, agent as buyer, agent as user) and argues that these push vendors toward usage and credit pricing, plus commit and offer structures. Most of the talk is product positioning, so the technical content is thin, but the framing and the demo flow are useful.

## Key ideas
- **Agents can run up spend fast, so spend controls need to exist at the agent level.** — The speaker says the impact of failures is growing because agents can run away with spend. He suggests giving each agent a wallet it alone can draw from, with controls set at that level, and passing similar controls down to customers. ([2:23](https://youtu.be/mJqwmmOx4WA?t=143))
- **Ship skills files and verbose errors so the agent can self-correct.** — Metronome is complex and easy to misuse. The team built an extensible, portable set of skills files that give the implementing agent context on the API. It also wants much more verbose, clearer error messages so agents can recover without a human. ([6:01](https://youtu.be/mJqwmmOx4WA?t=361))
- **Use coding agents to speed up work in a test environment, not to run billing in production unsupervised.** — The speaker says the goal is not to let a customer run the whole system without a human. Billing is business critical and full of business logic. Their setup is a sandbox, and the agent is directed to flow usage into it so the test looks like a live customer. ([7:25](https://youtu.be/mJqwmmOx4WA?t=445))
- **A useful test of a billing setup must include usage, not just provisioned objects.** — Seeing a contract or a provisioned customer is not enough. The speaker says the test has to show usage drawing down balances and generating invoices, so the agent's skills files direct it to send usage into the platform. ([7:25](https://youtu.be/mJqwmmOx4WA?t=445))
- **Agents play three different roles that change how you price.** — Agent as product: the agent is what you sell, so its token use must be metered. Agent as buyer: an agent procures services itself, as Stripe Projects does through the CLI. Agent as user: an agent operates the platform, so seat pricing matters less and value may accrue to one agent user. ([9:53](https://youtu.be/mJqwmmOx4WA?t=593))
- **Headless agent use is pushing vendors from seats to credits, and enterprises toward commit structures.** — The speaker cites HubSpot moving from seats to credits, starting in EMEA, and says agent-run sales-led products make usage pricing necessary. He describes prepaid and postpaid commitments and offers per customer type as the direction, copying cloud-provider commit models. ([10:59](https://youtu.be/mJqwmmOx4WA?t=659))
- **Credits should be a first-class billing object.** — In the demo, a credit is created for the test period, usage draws down the balance, and overage becomes an invoice at period end. Lovable's model combines a credits-only plan with monthly auto-recharge and several credit types scoped to different usage. Metronome models these directly rather than as ad hoc counters. ([14:07](https://youtu.be/mJqwmmOx4WA?t=847))

## Techniques
- **Portable skills files as agent context for a complex API** — Ship a set of skill files that tell the coding agent how to use your API correctly and avoid known pitfalls. Make them installable outside your org so customers can reuse them. *When:* Your product has many footguns and an agent will be the main integrator, so you want first-time setup to succeed without a human.
- **Verbose, machine-readable errors for agent self-correction** — Return error messages that name the cause and the fix clearly enough for an agent to repair its own call. Find more failure cases through the developer experience team and expand the messages. *When:* Agents are doing setup and initialization and you want them to recover without a support loop.
- **Sandbox-first agent-built billing with synthetic usage** — Have the agent provision a test account and billing configuration, then feed simulated usage through the real metering path so balances, drawdowns and invoices can be inspected before anything goes live. *When:* You are validating a new pricing model and want to check the full billing path, not just the configuration.
- **Natural-language provisioning through a CLI orchestrator** — Give the CLI one prompt describing a business model, such as replicating a competitor's pricing. The orchestrator provisions accounts and back-end services, and the billing agent creates the matching plan, credits and customer objects. *When:* You want to try a known pricing model quickly, without setting up a billing product by hand.
- **Classify agent roles before designing pricing** — Separate agent as product (meter its token usage), agent as buyer (procure services programmatically), and agent as user (operate your platform headlessly), then price each one differently. *When:* You are deciding whether seats, usage or credits fit a product whose main user may be an agent.

## Numbers
- Stripe CLI usage has grown exponentially over the past five to six months (no figure given). ([1:06](https://youtu.be/mJqwmmOx4WA?t=66))
- Metronome meters all API calls to OpenAI and Anthropic for its customers, including before they had revenue (speaker's claim). ([2:23](https://youtu.be/mJqwmmOx4WA?t=143))
- Lovable's pricing as replicated in the demo: credits-only, auto-recharged monthly, with several credit types scoped to usage (Build, plan mode, cloud, AI gateway credits) and overage invoiced at period end. ([15:14](https://youtu.be/mJqwmmOx4WA?t=914))
- HubSpot is moving from seat-based to credits-based pricing, starting in EMEA, with a dramatically lower seat price plus credits (speaker's claim). ([9:53](https://youtu.be/mJqwmmOx4WA?t=593))

## Hot takes
- Seat-based pricing matters less once an agent can operate the whole system (headlessness).
- Agents should not run a billing system in production without a human in the loop, even though they can build the setup.
- Agent-as-buyer procurement through a CLI is an important direction for making services discoverable to agents.

## Tools mentioned
Stripe Projects, Stripe CLI, Metronome, Claude (selected as the coding agent in the demo), Vercel, Postgres, skills files

## Relevance to our work
- **agentos** (2/3): Govrix Scout (L1) already does budgets. The talk's idea of an agent-scoped wallet with a first-class credit balance, draw-down and overage rules could change how budgets are modelled. → *Prototype per-agent budgets in Govrix Scout as a credit balance with draw-down and overage events, and compare it with the current flat counter. Time estimate: about one day.*
- **prosharness** (1/3): Long Claude Code runs can overspend in a loop. The wallet idea and the sandbox-first testing of billing both apply to ProsHarness's loops and schedules. → *Add a per-run spend cap to ProsHarness loops, enforced by the harness, and test it in a sandbox run before live use.*
