# x402 isn’t good (yet) — Jan Curn, Apify

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `h6mi88VrPtQ` · [watch](https://youtu.be/h6mi88VrPtQ) · **date:** 2026-09-18 · **length:** 20:48 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jan Curn · **orgs:** Apify, Coinbase, Stripe, Sentry, Visa, Mastercard, Google, OpenAI, Shopify, Skyfire, Alipay, UnionPay, Tempo
- **topics:** governance-compliance, security-guardrails, mcp-and-tools · **tags:** x402, agentic-payments, micropayments, double-spend, HTTP-402, MCP, Apify, Coinbase, batch-settlement, upto-scheme, agent-marketplace, MPP, agent-identity

> Apify's CEO lists x402 agent-payment flaws (double-spend before settlement, HTTP 402 vs MCP 401 conflict, poor fit for metered jobs) and his team's workarounds, including an agent-facing markdown gateway.

## Summary
Jan Curn, CEO of Apify, gives a sequel to "MCP isn't good yet," arguing that x402 (Coinbase's HTTP-402 agent payment protocol) is promising but has rough edges. He explains why crypto rails suit agent micropayments and walks through the x402 flow: 402 challenge, signed payment, facilitator verification, work, then settlement. The main flaw he shows is a double-spend window, since funds are checked but not reserved until on-chain settlement. He also covers the conflict between the 402 status code and the MCP auth flow's 401, the mismatch between the fixed-fee exact scheme and metered actors, and the upto and batch-settlement schemes. Apify's workarounds were charge-then-refund and an agent-facing markdown site (agi.apify.com) that issues prepaid API tokens. Much of the talk is product promotion for Apify's x402 launch, and the live demo failed.

## Key ideas
- **x402 has a double-spend window** — Payment is verified but not reserved, so the buyer's funds stay usable until on-chain settlement. One wallet can sign many requests. He says this is unsolved in both the exact and upto schemes. ([9:14](https://youtu.be/h6mi88VrPtQ?t=554))
- **402 status code conflicts with MCP auth** — x402 requires HTTP 402 as the first response, while the MCP auth flow expects 401, and a server cannot return both. A common workaround is a separate hostname per payment protocol, which he calls an anti-pattern. He suggests carrying the payment requirement in a header instead of the status code. ([11:36](https://youtu.be/h6mi88VrPtQ?t=696))
- **Fixed-fee scheme does not fit metered tools** — Apify actors run for seconds to hours and bill as they go. The original exact scheme charges a fixed fee per call, so it fits simple APIs poorly. ([11:36](https://youtu.be/h6mi88VrPtQ?t=696))
- **Charge-then-refund workaround** — They charge a fixed amount under the exact scheme, run the job, then refund the unused balance. It works, but it needs two on-chain transactions, adds settlement time and fees, and requires the client to trust the server to refund. ([13:02](https://youtu.be/h6mi88VrPtQ?t=782))
- **Upto scheme still leaves the double-spend problem** — Upto, announced in x402 v2 (Dec 2025) and shipped about two to three months before the talk, lets the client set a maximum and lets the server charge less. He says it does not prevent double-spending, so they went back to the drawing board. ([13:02](https://youtu.be/h6mi88VrPtQ?t=782))
- **Batch settlement as a likely fix** — The client deposits into escrow, receives a signed voucher, signs off-chain micropayments against it, and settles in batches, releasing the remaining escrow at the end. Apify had not implemented it yet when he spoke. ([14:29](https://youtu.be/h6mi88VrPtQ?t=869))
- **Why he thinks crypto fits agent payments** — Card, PayPal and ACH costs are too high for microtransactions. Chargebacks are a problem with agents because there is no agent identity, so the payment must be one-way. He argues a public, decentralized standard avoids a single company taking fees, and says he is not a crypto supporter himself. ([6:23](https://youtu.be/h6mi88VrPtQ?t=383))
- **Agent-facing instructions instead of a new API** — agi.apify.com is one markdown page that tells agents how to buy a prepaid Apify token (a $5 top-up example). That token then works with the normal Apify API or MCP. Agent instructions can change quickly without breaking the API used by tens of thousands of customers. ([15:52](https://youtu.be/h6mi88VrPtQ?t=952))
- **Build vs buy flips when token subsidies end** — He predicts that once agents pay the full cost of tokens, buying external services will beat building them in-house, and agentic payments will grow sharply. He says the current ~$1M per month volume is small. ([19:45](https://youtu.be/h6mi88VrPtQ?t=1185))

## Techniques
- **Charge-then-refund for metered jobs** — Charge a fixed amount up front with the exact scheme, run the job, then refund the unused balance to the client's wallet. *When:* Variable-cost tools on a payment protocol with no safe metered scheme. Accept the extra on-chain transactions and the need for clients to trust the refund.
- **Work-after-settlement for near-zero-cost calls** — Wait for settlement, then do the work and return 200 with a payment response. Double-spend is then harmless for the server, but a failed job leaves the server unpaid. *When:* Calls with near-zero marginal cost, where the risk of a failed job is acceptable.
- **Agent-facing markdown instructions plus prepaid token** — Serve one markdown page that tells agents how to pay. The payment yields a token for the existing API or MCP server, so the payment layer can change without touching the main API. *When:* Several payment protocols are still changing and a large existing API has customers who depend on it.
- **Batch micropayments via escrow and signed vouchers** — Deposit into escrow, receive a signed voucher, sign off-chain micropayments against it, settle in batches on-chain, then release the remaining escrow. *When:* High-frequency small payments where an on-chain write per call is too slow or expensive. Speaker had not yet shipped this.
- **Local wallet with cryptographic key and QR code** — Build a small local wallet tool that holds a key and shows a QR code to fund payments, for testing agent flows. *When:* No ready-made consumer wallet tooling exists for the protocol yet.

## Numbers
- Apify marketplace has about 45,000 tools (actors); community earns over $1M per month in payouts ([1:07](https://youtu.be/h6mi88VrPtQ?t=67))
- Coinbase launch added about 20,000 tools to the x402 agentic market (from about 2,000, roughly 10x); launch drew about 1M views ([2:37](https://youtu.be/h6mi88VrPtQ?t=157))
- x402 has about 20x the transaction count and volume of MPP, per a check the day before the talk ([7:46](https://youtu.be/h6mi88VrPtQ?t=466))
- The 402 status code has sat unused in the HTTP spec for about 30 years ([7:46](https://youtu.be/h6mi88VrPtQ?t=466))
- x402 exact scheme launched May 2025; v2 announced Dec 2025; upto shipped about 2-3 months before the talk ([13:02](https://youtu.be/h6mi88VrPtQ?t=782))
- Batch settlement scheme introduced about two months before the talk ([14:29](https://youtu.be/h6mi88VrPtQ?t=869))
- Demo example: $10 local wallet, $1 allocated for a token, $5 prepaid top-up on the AGI site ([17:16](https://youtu.be/h6mi88VrPtQ?t=1036))
- Setup takes about 10 minutes for a newcomer; x402 transaction volume is about $1M per month (speaker's estimate) ([18:40](https://youtu.be/h6mi88VrPtQ?t=1120))

## Hot takes
- x402's use of HTTP 402 is good for marketing but a design mistake; payment requirements should travel in headers, not the status code.
- A hostname per payment provider (x402.*, mcp.*, mpp.*) is an anti-pattern, like having 20 Amazons for 20 credit cards.
- Crypto is the one payment rail suited to agent micropayments, because card rails are too expensive and chargebacks are unworkable without agent identity.
- For agent-facing services, markdown instructions for agents can replace a stable versioned API because agents can pick up changes.
- Build-vs-buy flips toward buying external services once token subsidies end.

## Tools mentioned
x402 (Coinbase), MPP (Stripe, Tempo), HTTP 402 Payment Required, MCP, Apify actors, agi.apify.com, Coinbase facilitator

## Relevance to our work
- **agentos** (1/3): AgentOS L1 has budgets. The talk shows a double-spend race when a budget or balance is checked but not reserved before work runs. → *When designing budget enforcement in Govrix Scout, reserve budget before work starts, not just check it, and test concurrent requests against one shared budget.*
