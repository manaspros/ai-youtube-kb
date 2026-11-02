# The Search Engine for the Agentic Web — Will Bryk, Exa

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `59AA5kIoqjA` · [watch](https://youtu.be/59AA5kIoqjA) · **date:** 2026-09-18 · **length:** 17:49 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Will Bryk · **orgs:** Exa, Metaphor, Cursor, HubSpot, Y Combinator, Similarweb, OpenAI
- **topics:** rag-retrieval, infra-cost-scaling, product-ux · **tags:** search-api, agentic-web, embeddings, hybrid-search, token-extraction, structured-output, voice-agents, data-marketplace, company-pitch

> Exa's CEO pitches Exa as a search engine built for AI agents rather than humans, covering its history, API features (fast endpoint, token extraction, structured output) and a data marketplace.

## Summary
Will Bryk, co-founder of Exa (formerly Metaphor), argues that AI agents will soon make more web searches than humans and that they need a different kind of search than Google, which was built for humans. He tells the company story: started in 2021 betting that transformer embeddings could make semantic search work, launched a search product in 2022, and found that developers wanted an API for LLMs. He describes current product features: a roughly 200 ms search endpoint for voice agents, token extraction that returns only the most relevant tokens from search results to cut LLM cost, structured-output search for list-building, and per-customer configuration of domains, time windows and speed versus quality. He also presents Exa Connect, a marketplace where data providers license private data to agent developers. The talk is mostly vision and company promotion, with few technical details or evidence for its headline numbers.

## Key ideas
- **AI systems will soon issue more searches than humans, and the gap is expected to grow to about 1000x.** — The speaker's framing: AI searches overtake human searches in 2026, then grow far faster. This is a forecast with no source shown in the talk. ([0:08](https://youtu.be/59AA5kIoqjA?t=8))
- **Google-style search is built for humans and behaves like a recommender, so it fails on set-complete queries.** — Examples: 'shirts without stripes' returns striped shirts, and 'everyone in Singapore who works on AI search' returns documents, not a full list of matches. Agents need database-like completeness. ([2:20](https://youtu.be/59AA5kIoqjA?t=140))
- **Running an LLM over every document for every query is too expensive, so the work is to pre-index documents with embeddings.** — The thought experiment: an LLM judging a trillion documents per search would cost about $10M per query. Embeddings let you precompute document representations and then query them cheaply, usually combined with keyword matching. ([6:12](https://youtu.be/59AA5kIoqjA?t=372))
- **The business model came from LLM developers asking for a search API, because models cannot hold the whole web and must retrieve.** — Speaker's claim: even very large models are tiny relative to the web, so they always need a retrieval layer. AI systems want near-database access, not SEO or ads. ([8:30](https://youtu.be/59AA5kIoqjA?t=510))
- **Agent-facing search needs tunable latency: a very fast endpoint for voice, and slower, deeper queries that can run for minutes.** — The speaker says a voice agent can't afford search latency, so Exa offers an endpoint around 200 ms. Other customers accept minutes of search time in exchange for higher quality. ([11:21](https://youtu.be/59AA5kIoqjA?t=681))
- **Token extraction returns the most relevant passages from search results, not full snippets, to reduce downstream LLM spend.** — Example: from 10 documents, return about 100 of the most important tokens. The speaker frames this as a way to address the compute and token-cost problem. ([11:21](https://youtu.be/59AA5kIoqjA?t=681))
- **Structured output lets the search return typed fields extracted from pages, such as a paper's citation count or a person's education.** — Example: a recruiting agent asks for engineers who recently left a big lab, with their most-cited paper, college and graduation year, returned as structured data. ([12:22](https://youtu.be/59AA5kIoqjA?t=742))
- **There is no single perfect search. Each customer effectively gets its own configured search, with knobs for domain allow and deny lists, time windows, product-page exclusion and speed versus quality.** — The speaker says Exa runs roughly one search configuration per customer, with the customer choosing the tradeoffs. ([12:22](https://youtu.be/59AA5kIoqjA?t=742))
- **Exa Connect adds licensed private or paid data providers to search results, creating a market where data owners set prices and developers pick sources.** — Example shown: combining public web results with Similarweb traffic data that is not publicly available. The speaker describes this as a free market for agent-accessible data. ([13:23](https://youtu.be/59AA5kIoqjA?t=803))

## Techniques
- **Hybrid embedding plus keyword retrieval** — Precompute embeddings for each document so a query can be matched semantically without running a model per document, and combine with keyword matching where embeddings alone fall short. *When:* Retrieval over a large corpus where queries are complex or semantic and per-document model calls are too costly.
- **Token-budget extraction before the LLM** — Take the top-k retrieved documents and return only the top N tokens (e.g. about 100 from 10 docs) instead of full pages or long snippets. *When:* An agent needs grounding but the LLM context and cost must stay small.
- **Schema-based structured search output** — Ask the search to return named fields (e.g. paper citations, education, graduation year) for each matching entity, not free-text passages. *When:* Agents that build lists or databases of people, companies or papers.
- **Per-tenant search configuration** — Expose knobs per customer: include or exclude domains, date windows, product-page filtering, and a speed versus quality setting. *When:* A multi-tenant search service where each customer's agent has different accuracy, latency and source needs.
- **Latency tiers by consumer type** — Offer a very fast search path for real-time voice agents and a slow, high-quality path for background research that may take minutes. *When:* One retrieval service serving both interactive and batch agent workloads.

## Numbers
- Web searches by AI systems expected to exceed human searches in 2026, then grow about 1000x over the next few years (speaker forecast, no source given). ([0:08](https://youtu.be/59AA5kIoqjA?t=8))
- Over 5,000 companies and over 400,000 developers use Exa. ([1:10](https://youtu.be/59AA5kIoqjA?t=70))
- The web is on the order of a trillion pages. ([2:20](https://youtu.be/59AA5kIoqjA?t=140))
- Running a neural model over a trillion documents per query would cost about $10M per search (speaker's estimate). ([6:12](https://youtu.be/59AA5kIoqjA?t=372))
- Company raised a couple million dollars and spent about half on a GPU cluster early on. ([7:28](https://youtu.be/59AA5kIoqjA?t=448))
- Search endpoint latency of about 200 ms. ([11:21](https://youtu.be/59AA5kIoqjA?t=681))
- Token extraction example: from 10 retrieved documents, return about 100 tokens. ([11:21](https://youtu.be/59AA5kIoqjA?t=681))
- Progress in a quarter or two now equals the previous five years of progress (speaker's claim). ([15:31](https://youtu.be/59AA5kIoqjA?t=931))

## Hot takes
- AI systems will soon search far more than humans, roughly 1000x, and search should be built for them rather than for people.
- Search for AI should not be ad-driven or SEO-driven; AI systems want an almost database-like view of the world's information.
- Keyword search and recommendation-style ranking can't answer complete, set-based queries, so embedding-based search is needed.
- Information access is the key unsolved problem, and better search is needed to prevent manipulation and poor collective decisions.

## Tools mentioned
Exa search API, Exa Connect, Cursor, HubSpot, Similarweb, GPT-3, ChatGPT

## Relevance to our work
- **agentos** (1/3): MemoryMesh (L2A) does hybrid BM25 plus pgvector retrieval. The talk's token-budget extraction is one retrieval-side pattern to compare against it, but the talk gives no measurements. → *In the MemoryMesh retrieval path, add an optional top-N token trim on retrieved chunks, then compare LLM token cost and answer quality with and without it on the existing RAGAS eval set.*
