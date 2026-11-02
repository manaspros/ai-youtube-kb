# Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `cf2IhzqeQH4` · [watch](https://youtu.be/cf2IhzqeQH4) · **date:** 2026-10-07 · **length:** 20:08 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Dor Sasson · **orgs:** Stigg, Anthropic, OpenAI, GitHub, Uber, Replit
- **topics:** governance-compliance, infra-cost-scaling, product-ux · **tags:** usage-based-pricing, budgets, entitlements, double-spend, hold-and-settle, credit-pools, metering, agent-cost-control, ledger, idempotency

> Stigg's CEO argues AI usage pricing needs bank-style runtime controls: synchronous entitlement checks before consumption, hold-and-settle for concurrency, and layered credit pools, not invoice-time reconciliation.

## Summary
The speaker, co-founder and CEO of Stigg (a pricing and entitlements vendor), argues that AI companies are rebuilding banking infrastructure without realising it. He cites a run of pricing emergencies in April: Anthropic cutting third-party agents off from subscription plans, OpenAI's Pro price change, GitHub Copilot free-tier removal, and cost blowouts at Uber and Replit. His diagnosis is that entitlement checks happen after the invoice, when they should happen before the token is spent. He proposes a synchronous decision at request time, with reconciliation done asynchronously afterwards, using the ATM as the analogy. He covers concurrency (the double-spend problem, which needs hold, settle, idempotency and auditability), non-fungible credit pools that need draw-down ordering rules, and four recurring patterns: reserve before inference and settle after, keeping the metering ledger inside the VPC, checks for agents whose cost is unknown in advance, and per-team/user/model visibility for finance buyers. The talk is opinionated and partly a product pitch, but the architectural points are concrete.

## Key ideas
- **AI pricing emergencies are infrastructure problems, not just finance problems** — The speaker ties the April pricing shocks to systems that cannot tell subscription users from API users, so the cost side got subsidised until access was cut. ([1:39](https://youtu.be/cf2IhzqeQH4?t=99))
- **Entitlement checks run after the invoice when they should run before consumption** — Spend is reconciled only after the usage is logged and billed, which leads to overspend and sticker shock. He wants a synchronous check before the draw-down, similar to an ATM checking the balance before paying out cash. ([4:21](https://youtu.be/cf2IhzqeQH4?t=261))
- **Decide synchronously at request time, reconcile asynchronously afterwards** — The hot path is a single deterministic decision (access, rate limits, plan, trial or promo) made at request time. Settlement and billing happen later. He says this is a financial decision system, not just billing. ([7:10](https://youtu.be/cf2IhzqeQH4?t=430))
- **Concurrent draws against one pool create a double-spend problem** — Thousands of agents hitting the same balance at once will all look valid. Banks handle this with hold and settle, and AI systems need idempotency and an audit trail too. ([9:49](https://youtu.be/cf2IhzqeQH4?t=589))
- **Credit pools are not fungible** — A 1,700-credit balance may come from several sources (earlier grants, promotions) with different rules. Draw-down order matters, so a single integer balance will not hold up as the business scales. ([12:35](https://youtu.be/cf2IhzqeQH4?t=755))
- **Enterprise buyers want attribution by team, user, agent and model** — The buyer who signs a large annual commit expects to see who used the credits and how, with fine-grained spend caps. Budgets are set at the top, and the hierarchy below them is no longer flat. ([13:51](https://youtu.be/cf2IhzqeQH4?t=831))
- **Four recurring patterns for usage-based AI** — (1) Reserve before inference and settle actuals after. (2) Keep the metering ledger inside your VPC for latency, cost and sovereignty reasons. (3) Check balances as agents spawn when the final cost is unknown. (4) Give CFO and CIO visibility across models, features and products. ([15:16](https://youtu.be/cf2IhzqeQH4?t=916))
- **A pricing change can be an infrastructure change** — OpenAI's April change kept per-token price the same but changed how fast tokens burn. The speaker argues this is a rate change in how the software is consumed, and it needs the underlying system to support it. ([18:02](https://youtu.be/cf2IhzqeQH4?t=1082))

## Techniques
- **Synchronous pre-consumption check with async settlement** — Evaluate entitlement, rate limit and balance in the request path before the model call. Place a hold for the expected cost, then settle the actual usage asynchronously and release any unused amount. *When:* Usage-based AI products where the cost is only known after inference, or where a subscription and API tier share the same backend.
- **Hold, settle, and idempotency for concurrent draws** — Treat credit draw-down like double-entry bookkeeping. Create a hold on request, settle it when the work completes, use idempotency keys so retries do not double-charge, and keep an auditable event log. *When:* Many agents or users drawing from one shared pool, such as an org-level credit balance.
- **Ordered draw-down across credit sources** — Keep each credit grant as its own record with a source and rules, such as granted date or promotional status. Define the order in which grants are consumed instead of storing one total. *When:* Mixed credit types: pre-commit contracts, promotions, trials, and per-team allocations.
- **Deterministic decision waterfall** — Run a fixed ordered list of checks (feature access, plan limits, trial or promo status, rate limits, balance) at request time. The same inputs always give the same result. *When:* Gating access to features or models per user, plan or agent, where the result must be explainable.
- **Metering ledger inside the customer VPC** — Record usage events and balances in the customer's own network and only send aggregates outward. *When:* Latency, cost or data-sovereignty requirements rule out sending every usage event to a third-party cloud.

## Numbers
- Pro tier price rose about 5x overnight in April (speaker's words: 'bumping the price overnight, 5x') ([1:39](https://youtu.be/cf2IhzqeQH4?t=99))
- Anthropic's subscription cost for OpenClaw-style use was roughly '150 to even 750' against much smaller per-user daily revenue; the units are not stated in the transcript ([2:56](https://youtu.be/cf2IhzqeQH4?t=176))
- A single org was reported to burn through about half a billion of AI cloud credits in a short period (undisclosed company, as stated) ([2:56](https://youtu.be/cf2IhzqeQH4?t=176))
- Uber reportedly used up its whole annual AI usage budget within a few weeks of the year ([4:21](https://youtu.be/cf2IhzqeQH4?t=261))
- Example pool of 1,700 credits drawn from several differently sourced grants ([12:35](https://youtu.be/cf2IhzqeQH4?t=755))
- Buyer example: a seven-digit pre-commit annual AI contract ([13:51](https://youtu.be/cf2IhzqeQH4?t=831))

## Hot takes
- Every AI company is accidentally building a bank, and the industry is missing its 'Stripe moment' for usage-based entitlements.
- Usage-based AI billing should not be a post-hoc invoicing problem. The access and spend decision belongs in the synchronous request path.
- Changing the token burn rate while keeping per-token price the same is a pricing change, and it has to be treated as an infrastructure change.

## Tools mentioned
Stigg, OpenClaw, Claude Max, GitHub Copilot

## Relevance to our work
- **agentos** (2/3): L1 budgets and PII/strategy checks in the Rust proxy sit in the request path; the talk's hold-and-settle and concurrent-draw points apply directly to shared agent budgets. → *Check whether Govrix budget enforcement runs before the upstream call. Add a reserve/settle step with idempotency keys so concurrent agents sharing one budget cannot overspend.*
- **prosharness** (1/3): Long agent runs spend tokens over many loop steps, and a per-run spend cap works like the reserve-before-inference pattern. The talk does not cover loops directly. → *Consider a per-run spend hold that is checked before each loop step and settled after, for the checkpoint/resume flow.*
- **general** (1/3): Useful framing for any team pricing or metering agent usage, and the four patterns list is a quick reference for the design. → *Read the talk's four-pattern list (reserve before, ledger in VPC, unknown-cost agent checks, finance visibility) as a design checklist before building any usage metering.*
