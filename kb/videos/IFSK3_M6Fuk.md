# Hao Sheng on Building Human-Business Interfaces with AI | Better Stack Podcast Ep 3

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `IFSK3_M6Fuk` · [watch](https://youtu.be/IFSK3_M6Fuk) · **date:** 2025-11-02 · **length:** 47:45 · **format:** interview · **quality:** 2/5 · **depth:** intro
- **speakers:** Hao Sheng (founder, Expertise AI), Better Stack podcast host · **orgs:** Expertise AI, Chat Simple, Google, Cresta, Lysena, 500 Global, Better Stack, Verizon, AT&T
- **topics:** product-ux, rag-retrieval, enterprise-adoption · **tags:** founder-story, human-to-business-interface, dynamic-generated-ui, rag, query-rewriting, reranking, multimodal-retrieval, product-market-fit, bootstrapping, dialogflow, intent-classification, b2b-sales-agent, website-chatbot

> Hao Sheng (Expertise AI) on a human-to-business interface that generates per-visitor pages, with founder lessons from Dialogflow, Cresta and bootstrapping; mostly narrative, thin technical detail.

## Summary
Better Stack podcast interview with Hao Sheng, founder of Expertise AI (formerly Chat Simple). He tells his path from a failed license-plate-recognition startup in university, through Google Dialogflow (pre-LLM intent classification) and Cresta (real-time agent assist), to bootstrapping a website AI sales agent for B2B SMBs. The core pitch is a two-way "human-to-business interface" where the site answers visitors and generates rich, per-visitor page content from the conversation. He gives a short RAG outline (vector retrieval, reranking, LLM query rewriting, image-text consistency), says the hardest problem has been product-market fit rather than code, and reports about a million message exchanges per month. Most of the episode is founder story and opinion; the engineering detail is brief and no benchmarks or architecture specifics are given.

## Key ideas
- **Start from a validated problem, not a technology.** — The founder's first startup (Lysena) found a robust license-plate recognition model first and then looked for a market. Parking lot owners had no incentive to adopt it, and the lesson he draws is to find the problem before the solution. ([5:07](https://youtu.be/IFSK3_M6Fuk?t=307))
- **Pre-LLM conversational AI was classification plus human labeling.** — At Google's Dialogflow team the product sorted user utterances into hundreds of intent subcategories with ML, and used human-in-the-loop labeling to build training phrases for each intent. He calls it a forced decision tree that the LLM era later replaced. ([7:52](https://youtu.be/IFSK3_M6Fuk?t=472))
- **Google withheld an LLM demo over hallucination and credibility concerns.** — He says Google showed a conversational object-persona demo around 2021 but did not launch it publicly because of hallucinations. His view is that this caution, not a lack of capability, let OpenAI reach the market first. ([11:55](https://youtu.be/IFSK3_M6Fuk?t=715))
- **Early traction came from SMB websites and cheap prosumer pricing.** — Chat Simple started as a website AI that captured business emails for small and medium businesses. It was priced close to prosumer tiers, had a couple dozen paying customers at an accelerator stage, and the goal was the first 100 customers before pitching investors. ([19:50](https://youtu.be/IFSK3_M6Fuk?t=1190))
- **The product's core bet is that a website should generate content per visitor.** — Instead of a static page served to everyone, the AI builds a dynamic microsite from the conversation, using public site content as the knowledge base and pulling in text, images, videos and links that fit what the visitor asked. ([26:09](https://youtu.be/IFSK3_M6Fuk?t=1569))
- **Rich-answer RAG needs more than basic vector search.** — Baseline is embedding into a vector store and reranking, then he adds LLM query rewriting to infer intent and expand the query. He also flags two hard problems: indexing video and image assets, and making sure a retrieved image is consistent with the retrieved text. ([30:24](https://youtu.be/IFSK3_M6Fuk?t=1824))
- **Product-market fit and marketing were the hardest problems, not engineering.** — He says coding accuracy was the easy part for an engineer. Finding ideal customers, B2B marketing and SEO were the real challenges, and he treats podcasts and public sharing as brand and ecosystem building. ([31:47](https://youtu.be/IFSK3_M6Fuk?t=1907))
- **Rename once the product outgrows its name, before brand equity locks it in.** — Chat Simple became Expertise AI because the vision moved past language chat to generated GUI and modular agent expertise (sales, personality). He renamed early because the brand gets harder to migrate the longer you wait. ([35:28](https://youtu.be/IFSK3_M6Fuk?t=2128))

## Techniques
- **Start-from-problem validation before building** — Pick a concrete customer segment first (for example SMB websites), build a small product, and aim for about 100 paying customers before raising. The founder says pitching investors without traction did not work in his experience. *When:* Early-stage products where the technology is ready but the market is unclear.
- **Query rewriting before retrieval** — Run the user's query through an LLM to infer what they actually want and expand it with related intents, then retrieve with the rewritten query. Combine with embedding search and reranking. Specific prompts and models were not given. *When:* Retrieval over site or knowledge-base content where raw user phrasing is vague or short.
- **Multimodal retrieval with cross-modal consistency checks** — Index images and videos alongside text, retrieve candidates from each, and check that the image and the generated text fit together before showing them. He presents this as an open engineering problem and gives no implementation detail. *When:* Assembling rich responses that mix text, images and video.
- **Human-in-the-loop labeling for intent classifiers** — Train ML classifiers over hundreds of intent subcategories, then have human labelers annotate conversations to build and extend training phrases per intent. Described as the Dialogflow-era workflow, pre-LLM. *When:* Intent systems that have no LLM and need labeled training data for each category.
- **Per-visitor generated page from conversation** — Keep the conversation as the state. From it, select content (articles, videos, links) that matches the visitor's stated interests and lay it out as a page, rather than serving one static page to every visitor. Next-step prompts such as a recommended article or a HubSpot integration video follow from the discussion. *When:* Sales or support funnels on websites where the visitor's intent is known only through the conversation.

## Numbers
- License-plate recognition reached about 99.7-99.9% accuracy on the tech side, but parking adoption stayed low; the company had been operating about nine years at that point. ([3:53](https://youtu.be/IFSK3_M6Fuk?t=233))
- Dialogflow classified utterances into hundreds of intent subcategories. ([7:52](https://youtu.be/IFSK3_M6Fuk?t=472))
- Company had a couple dozen paying customers at the accelerator stage, priced close to prosumer rates. ([19:50](https://youtu.be/IFSK3_M6Fuk?t=1190))
- Goal of about 100 customers before raising. ([18:30](https://youtu.be/IFSK3_M6Fuk?t=1110))
- About 1 million message exchanges per month, reported as growing exponentially over the last two years. ([35:28](https://youtu.be/IFSK3_M6Fuk?t=2128))
- Hundreds of B2B customers after roughly two years of niching. ([23:57](https://youtu.be/IFSK3_M6Fuk?t=1437))
- Funding raised of about 2.5 million CAD so far. ([45:23](https://youtu.be/IFSK3_M6Fuk?t=2723))

## Hot takes
- Businesses will become living, consistent-personality entities that talk back and eventually make decisions and allocate budget on their own.
- Within five years, agents will follow instructions very precisely while still being creative and improvising outside the box; he calls self-improving frontier AI very hard to predict.
- Google had more advanced LLM tech than OpenAI around 2021 and held it back out of credibility concerns.
- Intro says the company raised $1.8M in venture funding; the founder says about 2.5M CAD at 45:23. These may be the same raise in different currencies, but this is unverified.
- Quality is capped at 2 because the episode is mostly founder narrative and product pitch with only brief engineering detail, and no sponsor segment was seen.

## Tools mentioned
Dialogflow (Google), Expertise AI (formerly Chat Simple), Cresta, HubSpot, AlexNet, ImageNet

## Relevance to our work
- **agentos** (1/3): The RAG section (query rewriting before retrieval, reranking, and checking that text and image retrieval results agree) is a brief, high-level overlap with MemoryMesh's hybrid BM25 + pgvector retrieval. It gives no measurements. → *Try an LLM query-rewrite step ahead of MemoryMesh hybrid retrieval, and measure recall and RAGAS scores with and without it.*
