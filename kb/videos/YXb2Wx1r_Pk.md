# Keyword Search Is Dying. Is Your Catalog Ready for AI Agents? — PayPal

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YXb2Wx1r_Pk` · [watch](https://youtu.be/YXb2Wx1r_Pk) · **date:** 2026-10-05 · **length:** 16:05 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Nixon Dinh · **orgs:** PayPal
- **topics:** rag-retrieval, data-engineering, product-ux · **tags:** catalog-enrichment, semantic-search, hybrid-search, agentic-commerce, product-data, hallucination, structured-data, trust-signals

> PayPal's agentic-commerce director argues merchant catalogs were built for human search, not agents, and shows that enrichment helps semantic recommendations while over-enrichment and boilerplate hurt.

## Summary
PayPal's director of product for agentic commerce, Nixon Dinh, frames commerce as moving from a search era to an intent era and then a delegation era, where shoppers hand tasks to agents. He argues that merchant catalogs and feed specs were built for human search and ad syndication, not for agents to read and rank. He contrasts keyword search (precise, literal) with semantic search (meaning-based, fuzzy) and says the practical answer is a hybrid of both. PayPal enriched merchant product data with attributes, description depth, buyer context and review-based trust signals, and the enriched records beat an unenriched baseline head-to-head. Gains were largest for the thinnest catalogs, while piling on unstructured or boilerplate text diluted the signal, and over-enrichment made the agent hallucinate more. The closing advice is to assess your catalog first, since more text is not better. Much of the talk is market positioning, and its market figures are not sourced or detailed.

## Key ideas
- **Commerce is moving from a search era to an intent era, then a delegation era where shoppers trust agents to act for them.** — Shoppers state needs in plain language, so brands must be discoverable where agents represent them. The speaker expects trust to build before delegation grows. ([1:44](https://youtu.be/YXb2Wx1r_Pk?t=104))
- **Merchant catalogs and feed specs were built for human search and ad syndication, not for agents to read and rank.** — Agents may use different models with different ranking logic, and vector retrieval is not always deterministic, so the optimization target is unclear. The speaker's answer is to run experiments. ([7:02](https://youtu.be/YXb2Wx1r_Pk?t=422))
- **Keyword search is precise but misses intent; semantic search is meaning-based but fuzzy; the speaker's answer is a hybrid of both.** — Example: a query for jogging footwear misses shoes labelled only as running shoes. Semantic search can find marathon-training shoes with no shared words, but injecting too much meaning loses focus and can hallucinate. ([9:11](https://youtu.be/YXb2Wx1r_Pk?t=551))
- **Enrichment works, but the right enrichment depends on how thin or spec-heavy the catalog already is.** — Enrichment patterns included attribute filling, description depth, buyer context and trust signals. Thin catalogs gain the most, and weak product data has the most room to improve. ([11:40](https://youtu.be/YXb2Wx1r_Pk?t=700))
- **Content quality drives retrieval results more than schema does, and unstructured piling-on dilutes the signal.** — Enriched records beat the unenriched baseline in head-to-head tests. Review data helped the search match terms like training and mesh. ([12:41](https://youtu.be/YXb2Wx1r_Pk?t=761))
- **Boilerplate brand copy is irrelevant to agents and can hurt; over-enriched catalogs made the agent hallucinate more and underperform.** — Examples of boilerplate include welcome-to-our-store messages and family-owned-business claims. The speaker admits this is one set of experiments with no universal recommendation. ([14:11](https://youtu.be/YXb2Wx1r_Pk?t=851))
- **Practical takeaway: assess your catalog structure first, and remember that more text is not better.** — Structured, quality content wins. The speaker says AI will reward content quality and not brands, while still rewarding some trust signals. ([15:10](https://youtu.be/YXb2Wx1r_Pk?t=910))

## Techniques
- **Catalog enrichment for semantic retrieval** — Fill missing attributes, add description depth, add buyer context (use cases) and trust signals such as review data, and keep the content structured. Avoid generic marketing copy. *When:* Use for thin or spec-light product catalogs, where enrichment gave the largest gains.
- **Head-to-head baseline test of enriched vs unenriched records** — Run the same agent recommendation task over enriched and unenriched product data, then compare which records get recommended. *When:* Use when you are unsure whether a data change helps agents; the speaker used it to validate enrichment.
- **Hybrid keyword plus semantic retrieval** — Combine literal keyword matching with embedding-based meaning matching, instead of choosing one. *When:* Use when precise literal matches and intent-level matches both matter for the same query.
- **Strip boilerplate from agent-facing text** — Remove welcome messages, brand stories and other text that does not help the agent decide. *When:* Use when indexing or feeding text that an agent will read and rank on.

## Numbers
- Bain projects 15 to 25% of all commerce will be executed by an agent by 2030; agents are predicted to outnumber humans online within a decade. ([4:45](https://youtu.be/YXb2Wx1r_Pk?t=285))
- PayPal expects about $1 trillion of US retail commerce to be agentic, and $3 to $5 trillion globally. ([4:45](https://youtu.be/YXb2Wx1r_Pk?t=285))
- Over 2 billion users are projected to use AI to start their shopping journey over the next few years. ([4:45](https://youtu.be/YXb2Wx1r_Pk?t=285))
- Partners reported referral traffic from AI engines up by a figure the auto-captions render as '693%' (text is garbled, so the exact value is unverified). ([5:50](https://youtu.be/YXb2Wx1r_Pk?t=350))
- 39% of US shoppers already use AI for shopping, per PayPal's consumer study. ([5:50](https://youtu.be/YXb2Wx1r_Pk?t=350))
- When shoppers start with an agent, order completion conversion can be up to 4x higher, according to the speaker, because the agent surfaces richer product data. ([5:50](https://youtu.be/YXb2Wx1r_Pk?t=350))

## Hot takes
- Catalogs were not built for agents, and most merchants are not ready for agent discovery.
- AI will reward content quality, not brands.
- More text is not better; over-enrichment and boilerplate hurt agent recommendations.
- Keyword search alone is not enough, and neither is semantic search alone; hybrid is the answer.

## Relevance to our work
- **agentos** (1/3): MemoryMesh uses hybrid retrieval (BM25 plus pgvector). The talk's keyword-versus-semantic tradeoff and its over-enrichment hallucination finding apply to how that hybrid index is fed, but the talk offers no retrieval method or benchmark for it. → *When tuning MemoryMesh hybrid retrieval, A/B an enriched versus raw document set on a fixed query set, and track hallucination or wrong-recall cases when enrichment text grows.*
- **general** (1/3): Context-engineering takeaway: extra boilerplate in agent-facing context can dilute signal and raise hallucination risk, which matters for CLAUDE.md and skill files. → *Review CLAUDE.md and skill descriptions for boilerplate; keep only what changes the agent's decisions.*
