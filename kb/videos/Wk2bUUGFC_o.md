# Why AI Startups Will Disappear Without Compute Markets — Evan Conrad, San Francisco Compute

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Wk2bUUGFC_o` · [watch](https://youtu.be/Wk2bUUGFC_o) · **date:** 2026-10-23 · **length:** 17:49 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Evan Conrad · **orgs:** San Francisco Compute, Junlark (former company name, as transcribed), CNCF, Lambda, NVIDIA, TSMC, Stability AI, Character AI
- **topics:** infra-cost-scaling, product-ux · **tags:** compute-markets, gpu-clusters, physical-settlement, capacity-financing, take-or-pay, neolab, ai-startups, consolidation, forecasting-risk

> Evan Conrad (San Francisco Compute) argues AI startups need compute markets because credit, deposits and forecasting risk make GPU capacity unfinanceable without liquidity; physical settlement requires operating the clusters too.

## Summary
Evan Conrad explains why San Francisco Compute runs a physically settled forwards market for GPU capacity, and it operates the hardware itself rather than brokering it. He traces the company's origin to an AI music lab that could not afford its cluster and was forced to sublease it, making it an accidental GPU broker. His core argument is that clusters are financed against the customer's credit, so buyers need long-term take-or-pay contracts, deposits scale with cluster size, and sold-out supply plus poor demand forecasts leave everyone stuck with too much or too little capacity. He frames these as one bundled risk problem and says a compute market has to underwrite the cluster's value rather than the customer's credit. The talk is a company pitch with a strong prediction (consolidation into a few large buyers and labs, with startups gated by credit), and it contains almost no measured data beyond rising deposit sizes.

## Key ideas
- **Compute markets exist to solve financing, not trading: lenders cannot underwrite AI company credit, so GPU clusters are delayed or require large deposits.** — Speaker says the number-one bottleneck in AI is credit, ahead of power, so each new lab or inference company is limited by its cash balance and must put down a deposit before its cluster is deployed. ([8:06](https://youtu.be/Wk2bUUGFC_o?t=486))
- **The riskiest moment is when the customer signs, because the cloud only then orders and deploys the cluster. He argues the cloud should buy and land the cluster first, then sell it.** — Build-then-sell cuts deployment delays. The same passage ties this to failed nodes: without spare capacity to swap in, RMA cycles reset the lead-time problem. ([5:16](https://youtu.be/Wk2bUUGFC_o?t=316))
- **Price sensitivity in AI, unlike SaaS, forces long-term take-or-pay contracts, which lock up capacity and kill liquidity for everyone else.** — SaaS companies survive a doubled cloud bill; AI companies go under, so they chase the cheapest cloud. Lenders therefore want multi-year contracts with investment-grade counterparties, and those contracts block resale. ([6:44](https://youtu.be/Wk2bUUGFC_o?t=404))
- **Physical settlement means the market operator must also operate the hardware, like a hotel that runs its own rooms; brokers cannot fix the operational problems buyers hit.** — Speaker uses a hotel room analogy: a reseller who does not run the building cannot handle room service or cleaning. He says this is why GPU brokering does not work. ([12:11](https://youtu.be/Wk2bUUGFC_o?t=731))
- **Few firms do physical settlement because the operating capacity is so valuable that building it pushes operators to become GPU clouds instead of markets.** — He describes the incentive to become a cloud as the default outcome. San Francisco Compute says it built physical settlement because it needed the market to exist before it could build its own AI lab. ([13:07](https://youtu.be/Wk2bUUGFC_o?t=787))
- **Deposits to enter frontier AI have grown from about $10M to roughly $100M and now about $1B; he does not expect this to continue.** — The speaker reports these figures as a trend. He says no investor will fund a $10B round before a company has revenue or traction. ([13:07](https://youtu.be/Wk2bUUGFC_o?t=787))
- **Without compute markets, startups get gated by credit, so incumbents with credit consolidate the economy; he predicts a future where a new startup needs roughly $100M of tokens to compete.** — Projection, not measured data: credit-gated token access turns into a flywheel for existing firms that build products on their own credit. He predicts a TSMC-like structure with a few clouds and a few labs. ([15:39](https://youtu.be/Wk2bUUGFC_o?t=939))

## Techniques
- **Build-then-sell capacity financing** — Buy and commission the cluster in a data center before a customer signs, so deployment and failure risk are handled before the sale. Keep spare nodes so failed hardware can be replaced without a new lead time. The talk presents this as the fix for the lender-credit problem, not as a proven method. *When:* When you run or resell GPU capacity and deployment lead times or customer credit delay revenue.
- **Physically settled forward contracts** — Sell reserved future capacity that the seller operates end to end, so the buyer gets operational support (fixes, scheduling, node swaps) along with the compute. The talk describes an order book for capacity bought now or later on this basis. *When:* When capacity buyers need guaranteed operations as well as raw GPU hours, and no third party can fix problems at the hardware layer.
- **Take-or-pay contracts for AI capacity** — Sign long-term commitments with investment-grade customers so lenders will finance clusters. The talk notes the tradeoff: the contracts reduce liquidity for other buyers who need capacity immediately. *When:* When financing GPU clusters and the customer's credit alone will not support a loan.

## Numbers
- The company started with a $500K raise and was forced to sublease its cluster, because it was underwater on the cluster every month. ([2:31](https://youtu.be/Wk2bUUGFC_o?t=151))
- The deposit needed to start a frontier AI lab was about $10M when the company began, rising to about $100M, and now about $1B. ([2:31 and 13:07](https://youtu.be/Wk2bUUGFC_o?t=0))
- Speaker projects that within three to five years a new startup might need about $100M of tokens to compete. This is a projection, not measured data. ([15:39](https://youtu.be/Wk2bUUGFC_o?t=939))
- Speaker says credit, not power, is the number-one bottleneck for AI at the moment. ([8:06](https://youtu.be/Wk2bUUGFC_o?t=486))

## Hot takes
- Frames the company's own product (a physically settled compute market) as the solution to the industry's problems. This is a vendor pitch with no benchmarks, customer data or pricing.
- Predicts consolidation into a TSMC-like structure with a few cloud buyers and labs, and a future where new startups must buy about $100M of tokens. These are speculative extrapolations from deposit sizes, not evidence.
- Says lenders cannot underwrite AGI or superintelligence, a rhetorical point that is not supported by any financing data.
- Title says AI startups 'will disappear' without compute markets, which overstates a financing argument. Substance is real but thin on numbers, so quality is capped at 3.

## Tools mentioned
San Francisco Compute (company, compute market and operator), Junlark (former company name, as transcribed; an AI music lab), Suno and Udio (as transcribed 'Suno or UDO'; music generation products named as context), Kubernetes (via CNCF Infrastructure Group, mentioned as background)

## Relevance to our work
- **agentos** (1/3): InferCraft runs on one RTX 5090, so the talk's capacity-planning framing (sold-out supply, over- or under-provisioning, deposits) is only loosely relevant to a single self-hosted GPU. → *When writing the InferCraft capacity assumptions, note the talk's over/under-provisioning risk as a planning caveat. No code change is suggested.*
