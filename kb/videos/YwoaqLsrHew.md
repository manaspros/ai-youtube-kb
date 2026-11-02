# Redis 8 Makes AI Search Blazingly FAST

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `YwoaqLsrHew` · [watch](https://youtu.be/YwoaqLsrHew) · **date:** 2025-11-02 · **length:** 5:26 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Redis, Better Stack, OpenAI
- **topics:** rag-retrieval, dev-tools · **tags:** redis, vector-sets, vector-search, embeddings, similarity-search, recommendations, in-memory-db, express, docker, redisearch

> Short Better Stack tutorial showing Redis 8 vector sets for product similarity search in a small Express app, plus a clarification of how they differ from the Redis vector database.

## Summary
The speaker builds a demo clothing store where each product page shows similar items, computed entirely by Redis rather than hard-coded rules. Product text (name, description, category, price) is embedded with the OpenAI embeddings API, converted to a Float32 buffer, and written to a Redis vector set with VADD using the product's numeric ID. Recommendations come from VSIM queried by the current product's ID, requesting four results with scores, dropping the item itself, and returning the other three. The app is Express with EJS templates and Redis runs in Docker. The speaker notes a cosine-similarity JavaScript function as a fallback that the demo did not use. He points out that user signals like purchases or preferences could be added to the embedded text. Caveats are that Redis is in-memory, so very large live datasets (he suggests over 100 GB) are a poor fit, and that persistence mode can write data to disk as a backup. He then separates two products that share the Redis name: vector sets (beta, sorted-set inspired, fast similarity only) and the more mature Redis vector database (hash or JSON storage, flat and other index types, via RediSearch and the Redis vector library, open source). He closes by arguing the license is unlikely to flip back to closed, citing the original creator's return in 2024. No benchmarks or latency numbers are measured; speed is shown only by eye in the browser.

## Key ideas
- **Redis can serve as a fast similarity-search store for product recommendations without custom ranking code** — The demo's 'similar products' feature is produced by Redis vector queries; the speaker stresses nothing is hard-coded or run through a server-side algorithm he wrote. ([0:00](https://youtu.be/YwoaqLsrHew?t=0))
- **Embed a plain-text product description, then store the vector keyed by the item's ID** — Embedding input is the product name, description, category and price concatenated; the embedding is saved on the product object and later written to Redis under the product's numeric ID. ([1:26](https://youtu.be/YwoaqLsrHew?t=86))
- **Redis expects a Float32 buffer for vectors, so convert the array before writing** — The JS float array is converted to a Float32Array and then to a buffer, which is the format Redis accepts for vector writes via VADD. ([1:26](https://youtu.be/YwoaqLsrHew?t=86))
- **Similarity lookup is a query by an existing element's ID rather than by a new query vector** — VSIM is called with the current product's ID; the app requests four results with scores, removes the current product and returns three. ([2:52](https://youtu.be/YwoaqLsrHew?t=172))
- **The app ships with a JS cosine-similarity fallback that the demo never exercised** — The speaker mentions it as a safety net if the Redis path fails, but notes it was not used in the demo, so it is unverified in this setup. ([1:26](https://youtu.be/YwoaqLsrHew?t=86))
- **Redis is in-memory, so size limits and persistence are the main operational constraints** — He advises against very large live datasets (he says over 100 GB) and points to Redis persistence mode as a disk backup. ([2:52](https://youtu.be/YwoaqLsrHew?t=172))
- **Redis 'vector' has two different products with different maturity** — Vector sets (beta) are a sorted-set-inspired structure for fast similarity; the Redis vector database (stable) stores data in hashes or JSON and supports more index types such as flat, and works with the Redis vector library and RediSearch. ([4:08](https://youtu.be/YwoaqLsrHew?t=248))
- **The licence concern is discussed but the speaker judges reversal unlikely** — He cites the original Redis creator, who stepped down in 2020 and rejoined in 2024 and helped push the project back to open source and implement vector sets. This is his opinion, not a stated company commitment. ([4:08](https://youtu.be/YwoaqLsrHew?t=248))

## Techniques
- **Embed product text for similarity, then store vectors in a Redis vector set** — Concatenate name, description, category and price into one string; call the OpenAI embeddings API; convert the float array to a Float32 buffer; write each product with VADD using its numeric ID as the element name. The speaker says user-specific data such as past purchases or preferences could be added to the embedded text. *When:* Product, blog-post or FAQ recommendations in an app where the catalogue is small enough to live in memory.
- **Query neighbours by element ID with VSIM** — Read the current item's ID from the URL, call VSIM against the vector set for that element, request four results with scores, filter out the current element and return the other three to the page. *When:* A 'related items' panel where the seed is an item already in the index, so no query embedding is needed.
- **Keep a plain cosine-similarity function as a fallback** — The speaker keeps a JavaScript cosine-similarity implementation in the codebase for use if the Redis similarity call fails; he says it was not exercised in the demo. *When:* When a similarity feature must degrade gracefully; it should be tested separately since it was not run here.
- **Turn on persistence for an in-memory vector store** — Enable Redis persistence mode so data is also written to disk as a backup. The speaker only mentions this; no config keys are shown. *When:* When the vector data should survive a restart and would be costly to rebuild from embeddings.
- **Choose between vector sets and the Redis vector database** — Use vector sets (beta) for simple, fast element-to-element similarity. Use the Redis vector database (hash or JSON storage, RediSearch-backed, flat and other index types, Redis vector library) when you need more algorithms or richer records. *When:* Deciding which Redis vector feature fits a project, given the beta status of vector sets.

## Numbers
- Demo catalogue of 8 hard-coded test products ([0:00](https://youtu.be/YwoaqLsrHew?t=0))
- VSIM requests 4 results including the current product; 3 similar products are returned after removing it ([2:52](https://youtu.be/YwoaqLsrHew?t=172))
- Speaker's rough upper bound for live data in memory: about 100 GB, with persistence as a disk backup option ([2:52](https://youtu.be/YwoaqLsrHew?t=172))
- Original Redis creator stepped down in 2020 and rejoined in 2024; speaker credits him with helping add vector sets and the return to open source ([4:08](https://youtu.be/YwoaqLsrHew?t=248))

## Hot takes
- The 'Blazingly FAST' title is supported only by a visual check in the browser; no latency, throughput or recall numbers are measured.
- The speaker treats a return to a closed-source Redis licence as very unlikely, based on his own reading of the creator's involvement rather than a stated commitment.
- Vector sets are described as beta, yet the video presents them as a simple production-ready way to add recommendations.

## Tools mentioned
Redis 8, Redis vector sets (beta, VADD / VSIM), Redis vector database (hash or JSON storage; RediSearch / Redis Query Engine, referred to as 'ready search'), Redis vector library, Express, EJS, Docker, OpenAI embeddings API

## Relevance to our work
- **agentos** (1/3): MemoryMesh already uses BM25 + pgvector hybrid retrieval; Redis vector sets are a possible small, in-memory similarity tier, but the video shows only an 8-item demo and the feature is beta. → *If MemoryMesh needs a hot-set similarity tier, prototype VADD/VSIM on the same embeddings beside pgvector and compare p95 latency and results before adopting; check the vector sets beta status first.*
