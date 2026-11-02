# Why AI Agents Still Won't Pay for Anything — Jan Curn, Apify

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-AOxpwVeIWw` · [watch](https://youtu.be/-AOxpwVeIWw) · **date:** 2026-10-19 · **length:** 20:37 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jan Curn · **orgs:** Apify, Gartner, Coinbase, Stripe, Tempo, Google, Shopify, OpenAI, Anthropic, Visa, Mastercard, Alipay, UnionPay, OKX, Lightning Labs, Skyfire, Exa, Perplexity
- **topics:** governance-compliance, product-ux, security-guardrails · **tags:** agentic-payments, x402, mpp, pay-per-use, batch-settlement, agent-marketplace, trust-directory, api-keys, crypto-payments, stablecoin, x402-scan

> Jan Curn (Apify) argues agents still don't pay for services because the payment funnel (need, setup, trust, buy) has friction at each step, and pay-per-use is the missing piece.

## Summary
Jan Curn, CEO of Apify, explains why agentic payment protocols exist but see almost no real volume. He lists more than a dozen competing standards (X402, MPP, AP2, ACP, UCP, TAP and others) and cites on-chain data showing roughly $1M in 30-day X402 volume and about $1,500 for MPP. He argues agents buy mostly through API keys and fixed accounts, not autonomous payment, so payments compete with API keys rather than cards. He frames adoption as a funnel: need, setup, trust/discovery, and buy. Trust is expected to come from curated directories and marketplaces, as with Claude connectors and ChatGPT apps. The buy step is blocked by fixed-price-per-call schemes, so he walks through X402's 402-challenge flow and the failure modes of its "upto" and "exact plus refund" workarounds, which led to batch settlement (escrow on-chain, then microtransaction charges later). He closes by saying the market will start moving soon and that vendors should prepare now.

## Key ideas
- **Agent payment protocols are proliferating, but agents are not using them** — The speaker names more than a dozen standards from fintech, crypto and big tech (L402, AP2, ACP, UCP, TAP, MPP, AMP and others) and says the space has become a battleground for network control. He asks why agents still do not pay. ([0:08](https://youtu.be/-AOxpwVeIWw?t=8))
- **Real agent revenue flows through API keys, not autonomous payment** — He says Apify, Exa, Perplexity and another provider together earn more than $1M per month from agent traffic, but through API keys and fixed accounts. So the real competitor for agent payments is API keys, not card networks. ([7:35](https://youtu.be/-AOxpwVeIWw?t=455))
- **The payment funnel has four steps: need, setup, discover and trust, buy** — Friction exists at each step. Agents first need a reason to pay, then a wallet or payment setup, then a way to discover and trust sellers, then a payment scheme that handles real usage. ([9:01](https://youtu.be/-AOxpwVeIWw?t=541))
- **Trust is the hard part, and marketplaces act as trusted middlemen** — Human commerce relies on networks, reviews and consumer protection. Agents lack those signals, so he expects curated directories (Claude connectors, ChatGPT apps, Apify's store) to become the trust layer. ([14:38](https://youtu.be/-AOxpwVeIWw?t=878))
- **Fixed price per call is not enough, and pay-per-use is the real requirement** — Real jobs (compute, LLM-driven tasks) need variable pricing. He says X402 added batch settlement and MPP added sessions for this, which is what enables metered billing. ([16:02](https://youtu.be/-AOxpwVeIWw?t=962))
- **X402 settles after the work, so the seller carries risk** — The flow is: API request, 402 response with a payment-required header, signed payment retry, facilitator verification, work, on-chain settlement, settled response. Sellers doing non-trivial compute may need to charge before doing the work. ([17:27](https://youtu.be/-AOxpwVeIWw?t=1047))
- **The upto scheme allowed double-spending, so Apify worked around it with exact plus refund** — Because settlement happens on-chain later, an agent could spend the same budget twice under upto. Apify charged a fixed amount upfront, then refunded the unused part, which requires trusting the seller and means two transactions. Batch settlement, which escrows funds on-chain and charges microtransactions later, was added to fix this. ([18:25](https://youtu.be/-AOxpwVeIWw?t=1105))

## Techniques
- **Exact-plus-refund for metered agent billing** — Charge a fixed upfront amount (his example: $10), perform the metered work (consumed $2), then refund the unused remainder once the job finishes. This works with schemes that only support exact payment, but it needs seller trust and costs two on-chain transactions. *When:* When the payment scheme cannot safely meter variable cost (for example X402 upto, where settlement is delayed and funds can be double-spent) and the buyer can trust the seller to refund.
- **Charge before work for non-trivial cost** — Require payment settled and verified before running expensive compute. Verifying the facilitator response before starting the job avoids the case where the work is done and the payment never arrives. *When:* When a request has a real compute or LLM cost and the seller cannot absorb a failed payment.
- **Escrow then micro-charge (batch settlement)** — Lock funds in an on-chain escrow up front, then charge small amounts against the escrow as work completes. The speaker says this removes the double-spend problem and the two-transaction overhead, but he does not explain the mechanics. *When:* For pay-per-use agent workloads on X402 or similar schemes where per-call on-chain settlement is too expensive or slow.
- **Curated directory as the trust layer for agent-discoverable tools** — Publish services through a verified marketplace or connector directory that the agent provider reviews, so agents can discover and buy from listed sellers instead of arbitrary URLs. *When:* When agents will find and purchase tools on their own, and sellers need to be trusted by default.

## Numbers
- Apify runs a marketplace of about 80,000 tools (actors) built by a global creator community ([0:08](https://youtu.be/-AOxpwVeIWw?t=8))
- Apify paid creators almost $2M in the last month (two-sided marketplace) ([1:06](https://youtu.be/-AOxpwVeIWw?t=66))
- Gartner (as cited, speaker hedges) predicts a $15T agent economy by 2028, with 80% of B2B activity done autonomously ([2:34](https://youtu.be/-AOxpwVeIWw?t=154))
- X402 on-chain payment volume was about $1M over the last 30 days; MPP about $1,500 ([7:35](https://youtu.be/-AOxpwVeIWw?t=455))
- Apify, Exa, Perplexity and another provider together make more than $1M per month from agents, but through API keys ([7:35](https://youtu.be/-AOxpwVeIWw?t=455))
- A $100/month Claude subscription can buy about $14,000 of tokens if fully used (speaker's claim, used to argue for the end of token subsidies) ([11:47](https://youtu.be/-AOxpwVeIWw?t=707))
- Refund example: $10 charged upfront, $2 consumed, remainder refunded ([18:25](https://youtu.be/-AOxpwVeIWw?t=1105))

## Hot takes
- Vendor talk: the speaker runs Apify, a marketplace that benefits from agent payments, and most of his adoption argument rests on Apify's own numbers.
- Adoption figures come from on-chain volume only, so they miss API-key and card traffic. His point that agents do not pay is partly a measurement choice.
- He says crypto is 'very well positioned to win' agent payments and calls it a bright future. He admits he is not a crypto person, and this is an opinion, not evidence.
- Expecting Claude, ChatGPT or other agent platforms to add crypto payments as a built-in feature is speculation presented as an imminent unlock.
- The end of token subsidies (OpenAI and Anthropic IPOs) is presented as a driver of buying over building, with no data behind it.
- Some provider and protocol names are garbled in the captions (for example 'Farcruel', 'Temple', 'Explorer II', 'OKEx'); the notes use the most likely names.

## Tools mentioned
Apify (actors marketplace, about 80k actors), X402 (Coinbase, scheme exact, upto and batch settlement), MPP (Stripe and Tempo; sessions), L402 (Lightning Labs), MasterCard Agent Pay, KYA Pay (Skyfire with Visa), AP2 (Google), ACP (OpenAI and Stripe, Agentic Commerce Protocol), TAP (Visa, Trusted Agents Protocol), UCP (Google and Shopify, Universal Commerce Protocol), ACTP (Alipay), AMP (Alipay, Agentic Mobile Protocol), APOP (UnionPay), OKX agent payment protocol, Agent Pay for machines (MasterCard), X402 scan and MPP scan (on-chain transaction monitors), Claude connectors directory, ChatGPT apps

## Relevance to our work
- **agentos** (2/3): AgentOS L1 (Govrix Scout proxy) already has budgets and exec gates. Pay-per-use metering, the upto double-spend problem and the exact-plus-refund workaround are directly relevant to budget enforcement and to any future paid-tool routing. → *Model per-agent budget caps as a pre-authorize, meter, refund flow in the L1 proxy. Read the X402 batch-settlement and MPP session specs before designing paid tool calls.*
- **prosharness** (1/3): ProsHarness has phone-driven approvals and budget-aware runs. The funnel's trust and budget steps map to approval gates before an agent spends money. → *Add a spend-approval gate to ProsHarness runs that caps upfront spend and requires an explicit approval before any paid tool call.*
