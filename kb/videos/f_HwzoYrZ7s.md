# Why AI Agents Will Need Their Own Bank Accounts — Lincoln Murr, Coinbase

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `f_HwzoYrZ7s` · [watch](https://youtu.be/f_HwzoYrZ7s) · **date:** 2026-10-20 · **length:** 16:58 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Lincoln Murr · **orgs:** Coinbase, Stripe, Cloudflare, AWS, Visa, Mastercard, PayPal, American Express, LangChain
- **topics:** governance-compliance, product-ux, mcp-and-tools · **tags:** agentic-payments, x402, http-402, stablecoins, micropayments, agentic-finance, coinbase, paper-trading, trust-autonomy, ai-advisor, micro-vm, skills, mcp, cli, widgets, cold-start

> Coinbase's head of AI product on agentic finance: agents that pay and grow money, the X402 HTTP 402 micropayment standard, and trust that is earned in steps. Largely a vendor pitch with some useful adoption data.

## Summary
Lincoln Murr (head of AI product, Coinbase) defines agentic finance as agents that either pay with money or grow money. He describes Coinbase's first attempt, Agent Kit (LangChain plus a crypto wallet, about two years ago), which gave agents money but nothing to buy. The fix was X402, an open standard built on the HTTP 402 "Payment Required" status code, using stablecoins as the payment rail. He reports adoption well ahead of an internal goal and argues that publishers will gate content behind tiny per-request agent payments. For growing money he lists three use cases: a delegated allocation account, autonomous trades triggered by conditions, and turning a natural-language idea into a strategy. His lessons are that trust and autonomy are earned gradually, that AI is the enabler rather than the product (Coinbase Advisor), that widgets solve the blank-canvas problem in chat, and that per-agent micro-VMs plus skills let the team ship features like paper trading quickly. The talk closes with speculative ideas about self-sustaining AI and DAO-like organizations. Much of it promotes Coinbase products, and the protocol mechanics are not explained.

## Key ideas
- **Agentic finance covers any agent that moves money or has a financial account, split into agents that pay and agents that grow money (growing is the less mature category).** — The speaker frames the whole talk around these two use cases. ([0:08](https://youtu.be/f_HwzoYrZ7s?t=8))
- **Giving an agent a wallet without anything to pay for was the core early mistake. Agent Kit (LangChain plus a wallet) let agents send money but had no commerce layer.** — About two years ago, before MCP or standard tool protocols, the team used LangChain with a wallet. Developers quickly showed the gap. ([1:10](https://youtu.be/f_HwzoYrZ7s?t=70))
- **X402 revives HTTP 402 Payment Required as a machine-to-machine payment standard, using stablecoins as a cheap, fast rail.** — The speaker notes 402 has been reserved for future use in the HTTP spec for decades. X402 is described as an open standard, launched around May of the previous year. ([2:22](https://youtu.be/f_HwzoYrZ7s?t=142))
- **Agent adoption of X402 grew well past the internal goal. The team targeted 25,000 agent transactions by year end and was seeing one about every 17 seconds by then.** — The speaker reports tens of millions in volume and hundreds of millions of transactions per 30 days now. Named adopters include payments and card companies. These are the speaker's own numbers, not independently verified. ([3:27](https://youtu.be/f_HwzoYrZ7s?t=207))
- **The motivating problem is publisher revenue: bot traffic has passed human traffic, and AI chat and overviews bypass ad-supported sites. The proposed fix is to charge agents a tiny fee per read.** — The example is a Substack charging agents a fraction of a cent per article. The speaker expects a shift from attention-based ads to micro-transactions. He says AWS and Cloudflare, which he says carry about 40% of internet traffic, have enabled X402 gating, but adoption is still early. ([4:25](https://youtu.be/f_HwzoYrZ7s?t=265))
- **Growing money with agents means delegating a bounded task while the human keeps directing it. Three use cases are delegated allocation, autonomous execution on conditions, and natural-language strategy.** — Examples: a set-and-forget 80/15/5 style allocation, a trade triggered by a scenario the user defines, and turning a phrase like 'invest in space' into a portfolio. ([6:48](https://youtu.be/f_HwzoYrZ7s?t=408))
- **Trust and autonomy are earned one step at a time. The expected path runs from hesitation, to small amounts, to an isolated portfolio with guardrails.** — The speaker compares this to self-driving cars. He says in his team's experience no model has blown up a user's account irrecoverably, though this is anecdotal. Guardrails and policies come before isolated portfolios. ([10:11](https://youtu.be/f_HwzoYrZ7s?t=611))
- **In financial services AI is the enabler, not the product. Coinbase Advisor is an SEC-registered AI advisor whose value is scaling advice to many users for free.** — The speaker says users mostly do not care about AI behind the scenes. Expect generative UI with agents hidden behind conventional interfaces. ([11:21](https://youtu.be/f_HwzoYrZ7s?t=681))
- **Proactive widgets solve the blank-canvas cold start in chat, and the team reports strong conversion from them.** — Users do not know what agents can do, so the product shows proactive insights and opportunities as widgets instead of waiting for a prompt. ([12:12](https://youtu.be/f_HwzoYrZ7s?t=732))
- **Per-agent micro-VMs with storage and a filesystem, plus skills that write code onto the user's machine, let the team ship features like paper trading without the usual internal release cycle.** — The speaker admits this is probably not the most efficient approach but says it speeds iteration. Access to accounts is through CLIs and MCP servers. ([13:14](https://youtu.be/f_HwzoYrZ7s?t=794))

## Techniques
- **Gate content or APIs behind HTTP 402 micropayments (X402)** — Respond with 402 Payment Required, let the calling agent pay in stablecoins, then serve the resource. The talk names the standard and rail but gives no protocol details, so consult the X402 spec before building. *When:* Publishers or APIs that want per-request monetization from agents rather than ads or subscriptions. Could inform pay-per-call routes in the gateway.
- **Staged autonomy for agents that handle money** — Start with a small amount, give the agent an isolated portfolio or sub-account, layer guardrails and policies, then widen scope as trust builds. The speaker calls this a progression rather than a single switch. *When:* Any agent action with real cost or irreversible effects, such as approvals, spend limits or trading.
- **Delegated conditional execution** — The user writes conditions in natural language (for example, if this scenario happens, make that trade). The agent monitors news or markets over time and acts when the condition fires. *When:* Tasks where a human would otherwise need to watch markets or news continuously, such as weekend monitoring.
- **Ship features as skills that write code on the user's machine** — Give each agent a micro-VM with a filesystem and storage, then have a skill generate the feature code (the speaker's example is paper trading) instead of routing the change through internal repos and releases. *When:* Fast iteration on user-facing capabilities where the speed of delivery matters more than efficiency.
- **Proactive widgets against chat cold start** — Show users concrete opportunities and insights in widgets alongside a chat interface so they learn what the agent can do. *When:* Products where users do not know the agent's capabilities and conversion from chat is low.

## Numbers
- Internal goal of 25,000 agent transactions by end of the first year after X402 launched in around May ([3:27](https://youtu.be/f_HwzoYrZ7s?t=207))
- Actual rate reached by year end was about one agent transaction every 17 seconds ([3:27](https://youtu.be/f_HwzoYrZ7s?t=207))
- Current scale claimed: tens of millions in volume and hundreds of millions of transactions per 30 days ([3:27](https://youtu.be/f_HwzoYrZ7s?t=207))
- Bot traffic has passed human traffic on the internet, per the speaker ([4:25](https://youtu.be/f_HwzoYrZ7s?t=265))
- AWS and Cloudflare together reportedly control about 40% of internet traffic, and both have enabled X402 gating ([5:30](https://youtu.be/f_HwzoYrZ7s?t=330))
- Example micropayment price: one ten-thousandth of a cent per read ([5:30](https://youtu.be/f_HwzoYrZ7s?t=330))
- Coinbase Advisor is described as an SEC-registered AI financial advisor, offered free ([11:21](https://youtu.be/f_HwzoYrZ7s?t=681))

## Hot takes
- Agents will become self-sustaining, paying for their own inference, compute and upkeep, and may run DAO-like organizations with AI at the core and humans at the edges (speculative, the speaker calls it a long way off).
- Per-request micropayments will replace attention-based ads as the main monetization model online.
- Trust in agents with money is earned by a gradual progression, and the team has seen no model blow up an account in an unrecoverable way (anecdotal, not evidence).
- Much of the talk is a product pitch for Coinbase products (X402, Coinbase MCP, Coinbase Advisor), and adoption numbers come from the speaker, not an independent source.

## Tools mentioned
X402, Agent Kit, LangChain, Coinbase MCP, Coinbase CLI, Coinbase Advisor, GrokBot, Muse, Stripe Link, Stablecoins

## Relevance to our work
- **agentos** (1/3):  → *Read the X402 spec and check whether a 402-style payment-required response fits as a budget or metering pattern for paid routes.*
- **prosharness** (1/3): The talk's staged-autonomy ladder (small amounts, isolated sub-accounts, guardrails first) maps loosely to ProsHarness approvals and zero-token credential handling. → *Consider whether ProsHarness approval gates should widen permissions step by step, starting from small or isolated scopes.*
