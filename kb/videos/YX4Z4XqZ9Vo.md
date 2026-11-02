# Most of Your Docs Readers Are Now AI Agents - Hahnbee Lee, Mintlify & Lincoln Murr, Coinbase

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YX4Z4XqZ9Vo` · [watch](https://youtu.be/YX4Z4XqZ9Vo) · **date:** 2026-11-01 · **length:** 18:52 · **format:** interview · **quality:** 2/5 · **depth:** intro
- **speakers:** Hahnbee Lee, Lincoln Murr · **orgs:** Mintlify, Coinbase, Cloudflare, Stripe, American Express, Mastercard, Visa
- **topics:** mcp-and-tools, product-ux, enterprise-adoption · **tags:** agent-readable-docs, docs-for-agents, agentic-payments, x402, api-first, mcp-vs-cli, build-vs-buy, context-window-budget

> A Mintlify and Coinbase fireside chat on designing docs and APIs for agent readers and agent payments; mostly opinion, with one notable agent-traffic stat and a closing build-vs-buy plug.

## Summary
Hanbi Lee (co-founder and CTO of Mintlify, a developer docs platform) and Lincoln Murr (head of AI product at Coinbase) discuss how agents are becoming the main readers of documentation and the main users of web services. Lee says agents ignore visual design and care about page size, context-window cost and accuracy, and that an agent hitting friction either brute-forces or switches to another product. He reports that agent share of traffic across Mintlify sites went from about 10% at the start of the year to about 80% now, a figure from the company's own internal tracker. Murr describes Coinbase's strategy of exposing its whole business through APIs, with x402 as an internet-native payment standard and about 100 million on-chain agent transactions in the past year, mostly paying for API access per call. Both say APIs are the base layer, with MCP adding natural-language context and CLI adding terminal access. On the docs side they agree that automation should gather technical context from PRs and Slack for writers, while narrative prose stays human-written. The chat ends with a plug for buying rather than building documentation tooling. There are few technical details and no demo, so the practical value is limited to the framing and the traffic number.

## Key ideas
- **For agent readers, docs quality is measured by page size, how much of the context window a page consumes, and accuracy. Visual design and branding no longer matter to agents.** — Agents do not see the site design. If an agent hits friction while setting something up, it either brute-forces the problem or moves to a competing product, so friction in the docs costs the vendor the customer. ([1:13](https://youtu.be/YX4Z4XqZ9Vo?t=73))
- **Docs need automation to avoid going stale, even though docs quality is still subjective.** — The speaker says keeping docs current through automation is very important. They are still working out how to judge whether AI-written docs are good. ([2:21](https://youtu.be/YX4Z4XqZ9Vo?t=141))
- **Coinbase's agent strategy has two parts: build products for agents, and make the whole core business reachable through APIs so agents can use it without browser automation.** — Browser use is possible but a poor fit for finance because of authentication and security risk. The stated goal is guardrails and limits on what an agent can do with an account. ([3:22](https://youtu.be/YX4Z4XqZ9Vo?t=202))
- **x402 is Coinbase's internet-native payment standard. It has been moved into a separate foundation co-governed by Cloudflare, Stripe, American Express, Mastercard and Visa.** — The speaker's argument for crypto is cheap, fast, permissionless digital dollars. The main use case is microtransactions, where an agent pays a fraction of a cent for one API call or paywalled page. ([5:38](https://youtu.be/YX4Z4XqZ9Vo?t=338))
- **Agents with wallets already pay per API call instead of needing a pre-funded account and API key per service. The speaker reports about 100 million agent transactions on-chain in the past year.** — The old flow was: find the website, fund an account, get an API key, then hand the key to the agent. The new flow is: give the agent a wallet and it pays for each call. The speaker frames money access as the lever for agent autonomy. ([6:40](https://youtu.be/YX4Z4XqZ9Vo?t=400))
- **Mintlify reports that agents went from about 10% of site viewership at the start of the year to about 80% now, and the company tracks this internally.** — This is an internal, unaudited figure from a vendor. It is useful as a signal of direction, not as a benchmark. ([12:22](https://youtu.be/YX4Z4XqZ9Vo?t=742))
- **Both speakers agree the API is the base layer. MCP adds context for natural-language use, and the CLI does the same with a terminal requirement.** — The speaker expects all three to coexist for some time and treats the ideal end state as unsettled. ([9:02](https://youtu.be/YX4Z4XqZ9Vo?t=542))
- **Technical writing is split into two steps. Gathering context (related PRs, Slack threads, decisions) can be automated. Narrative and creative prose should stay human.** — The speaker says it is tedious to find PRs and Slack decisions and then place them into the right docs. Agents also hallucinate when asked for product insights, which can make teams prioritize the wrong things. ([16:04](https://youtu.be/YX4Z4XqZ9Vo?t=964))
- **The build-vs-buy question depends on who maintains the tool over time. Hackathon projects are often built and then nobody maintains them.** — The speaker argues AI makes building faster but not maintenance cheaper, and that companies should keep effort on their core value and buy the rest from specialists who track the state of the art. ([17:10](https://youtu.be/YX4Z4XqZ9Vo?t=1030))

## Techniques
- **Keep docs lean for agent readers** — Cut page length and remove low-value content so a page fits in an agent's context window. Keep the content accurate, because an agent that reads wrong content will not notice and will fail later. *When:* When your docs or setup guides are read by coding agents and agents fail partway through setup or give wrong answers.
- **Track agent share of docs traffic** — Classify requests to docs sites as agent or human traffic and track the agent percentage over time. Mintlify does this in an internal tracker and runs internal bets on the trend. *When:* When deciding where to invest in docs, APIs or agent-facing surfaces. The speaker's numbers suggest the share is rising quickly.
- **Automate doc upkeep, keep prose human** — Use automation to gather context from PRs, Slack threads and decision records, and inject it into the docs corpus. Leave narrative and creative writing to humans. *When:* When engineering ships faster than docs can be updated and technical reference pages go stale.
- **Expose the product as APIs first, then wrap** — Build the core API as the foundation. Add an MCP server for natural-language context and nuance, and a CLI for terminal use. Do not treat any one wrapper as the whole interface. *When:* When making a product usable by agents and developers without a browser and without per-user manual setup.
- **Pay per call with a wallet instead of API keys** — Give the agent a funded wallet or financial account and let it pay for each request under the provider's payment standard (x402 in the talk). Enforce spending limits and guardrails on the agent's account. *When:* For pay-per-use APIs or paywalled content where pre-funded accounts and per-service API keys are a barrier to agent use.

## Numbers
- Agent share of viewership across Mintlify sites: about 10% at the start of the year, about 80% at recording (company's internal tracker, unaudited). ([12:22](https://youtu.be/YX4Z4XqZ9Vo?t=742))
- About 100 million agent transactions on-chain in the past year, mostly for paying for API access. ([6:40](https://youtu.be/YX4Z4XqZ9Vo?t=400))
- Microtransactions of one thousandth of a cent, or even one millionth of a cent, cited as the target for per-call agent payments (an aspirational example, not a measured figure). ([5:38](https://youtu.be/YX4Z4XqZ9Vo?t=338))

## Hot takes
- Agents do not see your website design, so front-end polish matters less than API quality and docs that stay accurate.
- Agents are already the main consumers of documentation, and developer-centric software companies should invest in APIs first.
- Buying documentation and developer tooling beats building it in-house, because the maintenance cost is usually underestimated.
- Vendor-led fireside chat: the closing build-vs-buy point is a product pitch, and the traffic figure comes from the speaker's own company.
- The DAO idea (automation at the core, humans at the edges) may finally be realized through agents with access to money. The speaker says this openly with uncertainty.

## Tools mentioned
Mintlify, x402, MCP, CLI, API, OpenClaw

## Relevance to our work
- **agentos** (1/3): Per-call wallet payments (x402) are a possible billing model for the proxy's budget pillar. This is an outside idea, not a current requirement. → *Read the x402 spec and compare it with the budget counters in the L1 proxy, to see whether pay-per-call fits the budget model as a later option.*
- **prosharness** (1/3): Harness docs and context files are read by agents, so the same context-budget and accuracy point applies. The rest of the talk is not about harness design. → *Measure how many tokens CLAUDE.md and the skill files take at session start. Keep them small enough that they do not crowd out the working context.*
