# Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ZyGMqdIpPoE` · [watch](https://youtu.be/ZyGMqdIpPoE) · **date:** 2026-09-18 · **length:** 20:48 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Rodrigo Coelho, Pranav Maheshwari · **orgs:** Edge & Node, Coinbase, Google, Circle, Shopify, Cloudflare, TRM, MasterCard, Stripe, Amazon, Exa, Firecrawl
- **topics:** governance-compliance, security-guardrails, mcp-and-tools · **tags:** agentic-commerce, x402, micropayments, paid-mcp, sanctions-screening, wallet, compliance, ampersend, shopify-ucp, agent-payments

> Edge & Node's pitch for Ampersend, a payment and compliance layer letting agents pay for paid MCP tools and checkouts, with a sanctions-screening demo. Mostly product pitch.

## Summary
Rodrigo Coelho (CEO of Edge & Node, creators of The Graph) and Pranav Maheshwari present Ampersend, an agentic-commerce layer. They argue traditional payment rails assume a human approves each payment, which fails for machine-speed agents, and that enterprises need compliance controls (sanctions, counterparty identity, policy limits) before adopting agent payments. Pranav runs three demos: an agent with a paid-MCP aggregator skill file finds information that a no-skill agent cannot, an agent buys a sub-$10 Father's Day gift through a Shopify UCP checkout from a wallet, and a sanctioned-wallet agent is blocked once TRM wallet screening is enabled. The core claim is that most MCP tools will become paid, so agent capability will track access to paid tools and wallets. The talk gives little technical detail on how the controls work and is largely a product pitch, though the compliance framing is a useful statement of the problem. One numeric claim is internally inconsistent (total stated as $9, charge stated as $11).

## Key ideas
- **Traditional payment rails assume a human in the loop approving each payment, which does not fit agents that transact at machine speed around the clock.** — The speaker says existing controls and policies were built for humans and cannot keep up with machine-speed transactions, so a new method is needed. ([4:02](https://youtu.be/ZyGMqdIpPoE?t=242))
- **Compliance is the gate for enterprise adoption of agent payments.** — Counterparty checks (sanctions, terrorism links, identity behind a wallet) are needed because an agent presents only a wallet address. The speaker says a chief legal or policy officer must be confident agents cannot hallucinate, overspend or break policy, and that fines can reach tens to billions of dollars. ([5:27](https://youtu.be/ZyGMqdIpPoE?t=327))
- **Most MCP tools are free today, but the speaker expects many to become paid, and agent capability will follow access to paid tools.** — Rather than giving a card to each provider, the agent uses an aggregator marketplace. The user installs one skill file, and payments happen in the background from a wallet. The speaker says an agent is only as powerful as the paid tools and payment trail it has. ([8:20](https://youtu.be/ZyGMqdIpPoE?t=500))
- **Demo: a paid-tool call is visible as a small recorded transaction, and an agent without the skill file cannot complete the same task.** — Both agents got the same prompt to find a MasterCard crypto executive's email. The agent with the skill file returned the contact details and showed a small settled transaction for the paid endpoint. The agent without it could only give a guessed email format. ([9:44](https://youtu.be/ZyGMqdIpPoE?t=584))
- **Agentic checkout via a standard commerce protocol, with a spend limit given in the prompt.** — The agent used Shopify's UCP to find and buy a gift under $10 from a wallet, with no user name, address or phone number given. The speaker credits the agent's stored memory of preferences. The budget was stated in the prompt, and no enforcement mechanism is described. ([12:06](https://youtu.be/ZyGMqdIpPoE?t=726))
- **Compliance must apply to both buyer and seller, and the sanctioned-wallet demo shows blocking at the screening step.** — With screening off, a good agent and a flagged agent both transact. With TRM wallet screening on, the flagged wallet's transactions are rejected as blocklisted while the good agent still transacts. ([15:56](https://youtu.be/ZyGMqdIpPoE?t=956))
- **Agents will not go through card checkout flows like Stripe; they will use their own wallets or cards.** — The speaker says agents will have their own payment forms rather than human-oriented checkout guardrails, and that this only succeeds if wallet infrastructure and paid MCPs are both in place. ([18:28](https://youtu.be/ZyGMqdIpPoE?t=1108))

## Techniques
- **Pre-authorization counterparty screening** — Before a payment settles, check the counterparty wallet against a sanctions/risk screening service (TRM in the demo). Block the transaction if the wallet is flagged, and check both buyer and seller sides. *When:* Machine-to-machine payments where the agent sees only a wallet address and no human reviews each transaction.
- **Skill file as the payment-aware tool gateway** — Install one skill file in the agent. It routes tool calls to an aggregator marketplace of paid MCP tools, and the aggregator pays per call from the agent's wallet, so the user never enters a card per provider. *When:* Useful tools are paywalled and you want one integration point instead of separate accounts and cards for each vendor.
- **Per-call micropayment for paywalled endpoints** — Charge sub-cent amounts per request, such as 0.1 cent per scrape. The speaker says batching reduces gas costs for nano-payments and draws on an earlier micropayment and batching system their team built, and cites the x402 HTTP 402 approach. *When:* Per-request pricing for data or tool endpoints where card fees would exceed the price of each call.
- **Prompt-level spend constraint** — State the budget in natural language in the task prompt (for example, keep the gift under $10). *When:* Only as a demo example in this talk. The speaker does not describe any enforcement, so treat it as a prompt instruction, not a control.

## Numbers
- The Graph has served 1.8 trillion queries of on-chain data since it launched in 2018. ([0:08](https://youtu.be/ZyGMqdIpPoE?t=8))
- The first electronic transaction is dated to 1981. ([1:09](https://youtu.be/ZyGMqdIpPoE?t=69))
- The team built a micropayment system for queries in 2021. ([1:09](https://youtu.be/ZyGMqdIpPoE?t=69))
- The traditional financial industry is described as almost a quadrillion dollar industry (speaker's figure, not sourced). ([4:02](https://youtu.be/ZyGMqdIpPoE?t=242))
- Enforcement fines for compliance failures are described as reaching tens, hundreds or billions of dollars. ([5:27](https://youtu.be/ZyGMqdIpPoE?t=327))
- A scraping service charges 0.1 cent per request, paid by the buying agent. ([16:56](https://youtu.be/ZyGMqdIpPoE?t=1016))
- In the gift demo, the speaker says the total was $9 and then that $11 was charged. The two figures are not reconciled. ([13:20](https://youtu.be/ZyGMqdIpPoE?t=800))

## Hot takes
- Most MCP tools are free today, but they will become paid, and an agent's power will equal the paid tools and wallet access it has.
- Agents will not pay through Stripe-style checkout flows with human guardrails. They will use their own wallets or cards.
- Agent payments will only scale to enterprises once sanctions and counterparty screening apply on both buyer and seller sides.

## Tools mentioned
x402, Shopify UCP, TRM (wallet screening), MCP, Claude Code, Claude Cowork, Ampersend, Exa, Firecrawl, Circle nano-payments

## Relevance to our work
- **agentos** (1/3): AgentOS L1 (Govrix Scout) already plans budgets and an audit log. The talk's point is a per-transaction policy check before a paid call settles, plus counterparty screening, which AgentOS does not have. → *Compare Govrix budget enforcement with a pre-authorization hook on paid tool calls that checks a spend cap and a blocklist before the call goes through.*
- **prosharness** (1/3): ProsHarness already has phone-driven approvals. The talk's main argument is a human-free spend gate that stops a run before money moves. → *Consider using the existing phone-approval flow as a spend gate for any paid tool call above a threshold.*
- **general** (1/3): This is a useful statement of the agent-payments and compliance gap for enterprise buyers, though the talk is a product pitch with little technical depth. → *Read the x402 spec (the talk says Coinbase and Google co-developed it and that Edge & Node contributed batching) before designing any paid-endpoint support.*
