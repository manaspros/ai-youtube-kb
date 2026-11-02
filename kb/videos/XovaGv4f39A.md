# When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XovaGv4f39A` · [watch](https://youtu.be/XovaGv4f39A) · **date:** 2026-07-18 · **length:** 5:52 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Luis Romero-Sevilla · **orgs:** Orbis
- **topics:** rag-retrieval, context-engineering, multi-agent, infra-cost-scaling · **tags:** extended-cache-augmented-generation, ECAG, CAG, KV-cache, GraphRAG, RAG, context-buckets, supervisor-model, long-context, knowledge-representation, document-collections

> Luis Romero-Sevilla (Orbis) on Extended Cache Augmented Generation (ECAG): for large, frequently replaced, densely interrelated document collections, split docs across parallel KV-cached context buckets and let a supervisor model interrogate them, instead of RAG or GraphRAG.

## Summary
The speaker frames a problem where every document in a fast-changing collection is relevant to global questions. Plain vector RAG fails because all documents are needed, and GraphRAG is too expensive to rebuild whenever the data is replaced. Full-context CAG degrades as the window fills. His approach, ECAG, spreads documents across several context buckets with no topical grouping, since a supervisor model ignored domains that looked irrelevant. Each bucket's KV cache is loaded in parallel, and a supervisor model explores buckets and asks targeted follow-ups. He says this builds knowledge faster than GraphRAG and answers more accurately than simple RAG. He concedes KV cache is costly and can be reduced by shortening how long each cache lives. He closes that no single retrieval strategy fits all, and that ECAG is a solution to his specific problem. The talk is short (about 6 minutes) and gives no benchmark numbers.

## Key ideas
- **Plain vector RAG breaks when every document is relevant to a global question.** — Top-k similarity retrieval only returns the closest chunks, so it cannot answer questions that need the whole collection. The speaker's use case also has data that goes obsolete and is replaced often. ([1:40](https://youtu.be/XovaGv4f39A?t=100))
- **GraphRAG is accurate for interconnected documents but costly when data changes.** — An LLM extracts entities and relationships into a knowledge graph, and queries walk the graph. Rebuilding that graph on every data replacement is expensive and slow, so it suits stable collections only. ([1:40](https://youtu.be/XovaGv4f39A?t=100))
- **Full-context caching degrades as the window fills.** — Loading all documents into one long context and caching its KV matrix is simple. The speaker says answer quality drops once the context window is too full. ([3:08](https://youtu.be/XovaGv4f39A?t=188))
- **Distribute documents across parallel context buckets, unordered.** — Each bucket holds a subset of documents with its own cached KV state, and the bucket count is chosen so each holds few documents. Documents are not grouped by domain, because a supervisor model tended to skip domains that looked irrelevant at first glance. ([3:08](https://youtu.be/XovaGv4f39A?t=188))
- **A supervisor model interrogates buckets and builds understanding progressively.** — The supervisor queries each bucket, notices interesting results, and sends follow-up questions to specific buckets before synthesizing one answer. Because the caches load in parallel, ingestion is faster than GraphRAG. ([4:33](https://youtu.be/XovaGv4f39A?t=273))
- **KV cache cost can be reduced by shortening cache lifetime.** — The speaker admits KV cache is expensive. He says the mitigation is to optimize how long each cache is kept alive, and that every retrieval strategy trades compute, cost and speed against each other. ([4:33](https://youtu.be/XovaGv4f39A?t=273))

## Techniques
- **Parallel context buckets with a supervisor (ECAG)** — Split the corpus into N buckets with balanced document counts and no topical grouping. Cache each bucket's KV state, load them in parallel, and let a smarter supervisor model query each bucket, follow up on promising ones, and synthesize the answer. *When:* Collections are small enough to fit in context chunks, every document may matter to global questions, and the data is replaced often so GraphRAG rebuilds are too costly.
- **Dropping topical sharding for bucketing** — Assign documents to buckets in arbitrary order, only balancing counts. Do not pre-categorize by domain. *When:* Documents are densely related across categories, since a domain-based supervisor may ignore buckets that look irrelevant at first glance.
- **Caching KV state per context bucket** — Store the model's KV matrix for each loaded document set so later questions skip re-prefilling the documents. *When:* The same document set answers many questions. Shorten each cache's lifetime to cap the memory cost.

## Numbers
- No benchmark numbers given. Claims are qualitative only: ECAG builds knowledge faster than GraphRAG and gives more accurate answers than simple RAG. ([4:33](https://youtu.be/XovaGv4f39A?t=273))

## Hot takes
- Domain-based partitioning of documents fails for densely interrelated corpora, because the supervisor ignores domains that look irrelevant.

## Tools mentioned
GraphRAG, vector database, KV cache

## Relevance to our work
- **agentos** (2/3): MemoryMesh already does hybrid retrieval plus GraphRAG; ECAG offers a KV-cache-based alternative for small, fast-changing corpora. InferCraft already has pluggable KV-cache strategies, so per-bucket caches fit there. → *Benchmark an ECAG-style bucketed KV-cache path against MemoryMesh's GraphRAG on a small corpus with frequent replacement, measuring ingest time and answer accuracy.*
- **general** (2/3): Relevant to context-engineering choices: when to use RAG, GraphRAG, full-context caching, or bucketed supervisor designs. → *Note the trade-off framing (retrieval strategy versus KV cache cost) when choosing retrieval for a new project.*
- **prosharness** (1/3): Long agent runs need context management, and bucketed context with a supervisor is a possible pattern. The talk is a short sketch with no evidence.
