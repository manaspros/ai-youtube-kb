# Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `r9OwPx_HoV0` · [watch](https://youtu.be/r9OwPx_HoV0) · **date:** 2026-09-18 · **length:** 18:01 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Yuval Belfer · **orgs:** AI21 Labs, Anthropic, LlamaIndex
- **topics:** rag-retrieval, evals · **tags:** chunking, multiscale-indexing, reciprocal-rank-fusion, oracle-experiment, retrieval-tuning, agentic-search, index-cost

> AI21's Yuval Belfer argues chunking still matters: no single chunk size wins per query, so index the corpus at several sizes, retrieve whole documents, and fuse the rankings with RRF for 20-40% gains.

## Summary
The speaker says agentic search (grep, ls, find) does not replace retrieval infrastructure, because it gets slow and expensive at large data scale and does not handle ordering across many folders well. Chunk size is a lossy compression choice: small chunks miss broad context, large chunks dilute embeddings, and the best size depends on the query. An oracle experiment across QMSum, NarrativeQA, a Seinfeld trivia set and FinanceBench showed that picking the best fixed size per query leaves a 20-40% recall gap. The proposed method, multiscale indexing, builds one copy of the index per chunk size, queries all copies in parallel, maps hits to parent documents so the rankings are comparable, and merges them with Reciprocal Rank Fusion (RRF). Reported results match or beat the best fixed size on the four datasets, with the cost being extra index storage that grows with the number of copies. Open questions the speaker names are how many chunk sizes to use and whether something better than RRF exists.

## Key ideas
- **Agentic search does not remove the need for retrieval infrastructure** — grep, ls and find work on small data, but they become costly and inefficient at scale, and aggregating answers across many folders is slow. ([2:48](https://youtu.be/r9OwPx_HoV0?t=168))
- **Chunk size is lossy compression with no universal right answer** — Small chunks lose broad context and large chunks dilute embeddings and nuance. The speaker claims the best size depends on the query, not only on the dataset. ([4:11](https://youtu.be/r9OwPx_HoV0?t=251))
- **Oracle experiment shows a large per-query headroom** — Choosing the best chunk size per query, with hindsight, beats every fixed size by roughly 20-40% recall. The blue fixed-size curves intersect, so no single size dominates. ([8:09](https://youtu.be/r9OwPx_HoV0?t=489))
- **The gap exists because the information is missing at each stage** — At indexing time the queries are unknown, and at query time the chunk size is already fixed. Neither stage can adapt the chunking to the query. ([9:33](https://youtu.be/r9OwPx_HoV0?t=573))
- **Multiscale indexing: index at several sizes and query all of them** — Duplicate the corpus once per window size, query every copy for each request, and combine the results. The speaker says this beats prior work such as contextual retrieval, which keeps one fixed chunk size. ([10:32](https://youtu.be/r9OwPx_HoV0?t=632))
- **Retrieve whole documents so rankings from different chunk sizes can be compared** — Chunks of different sizes cannot be ranked against each other, but documents can. Each copy's hits are mapped to parent documents, which gives N rankings of the same items. ([12:02](https://youtu.be/r9OwPx_HoV0?t=722))
- **Simple RRF fusion works best among methods tried** — The speaker treats fusion as voting. The script is short and needs no trained model. He says RRF won over the alternatives tested but that better methods may exist. ([13:11](https://youtu.be/r9OwPx_HoV0?t=791))
- **Cost is extra storage, not latency** — The approach needs a copy of the index per chunk size, which adds memory. Retrieval runs in parallel and RRF is cheap, so latency is roughly unchanged. ([15:55](https://youtu.be/r9OwPx_HoV0?t=955))

## Techniques
- **Multiscale indexing** — Chunk the same corpus at several window sizes (the talk uses values such as 50, 100, 200, up to 2000 tokens), store one index per size, fan each query out to all indexes in parallel, and merge the results. *When:* Use when one corpus serves mixed query types, such as narrow fact lookups and broad questions, and a fixed chunk size loses recall on one of them.
- **Parent-document lifting before fusion** — Map every chunk hit to its parent document before ranking. Fusion then combines comparable document-level ranks instead of chunk ranks from different window sizes. *When:* Use whenever you merge result lists built from chunks of different sizes.
- **Reciprocal Rank Fusion (RRF)** — Combine the N ranked lists with the RRF score, which sums 1/(k + rank) across lists. It is parameter-light and needs no training. *When:* Use as a default merge step when you have several retrievers or indexes and no labelled data to tune weights.
- **Oracle best-per-query benchmark** — Build one index per candidate setting and, for each query, take the best setting's recall as an upper bound. Compare that bound with each fixed setting. *When:* Use before building a complex retrieval scheme, to check whether the gap is worth the cost.

## Numbers
- Oracle best-chunk-size-per-query beats fixed chunk sizes by roughly 20-40% (recall) ([9:33](https://youtu.be/r9OwPx_HoV0?t=573))
- Multiscale indexing improves over the best fixed size by about 20-40% on QMSum, NarrativeQA, Seinfeld and FinanceBench (recall at 1 to 10) ([14:33](https://youtu.be/r9OwPx_HoV0?t=873))
- Reported gains of about 10-40% on MTab, per the speaker's blog post (not shown in the talk) ([14:33](https://youtu.be/r9OwPx_HoV0?t=873))
- Experiment used six chunk-size copies of each database, from 2000 tokens down to 50-100 ([5:32](https://youtu.be/r9OwPx_HoV0?t=332))
- Extra memory cost is a constant multiple of the index size, one copy per chunk size. The figure is garbled in the captions and may be 2-5x, so treat it as unverified ([15:55](https://youtu.be/r9OwPx_HoV0?t=955))

## Hot takes
- Retrieval did not die. It turned into infrastructure, and that infrastructure is still stuck in 2022.
- There is no right chunk size, and chunking is query-dependent, not dataset-dependent.
- Agentic search does not kill retrieval tuning; at scale it is expensive and inefficient.
- Overfitting to a benchmark is less of a risk for RAG chunking than for models, because the chunk size cannot be tuned per dataset.

## Tools mentioned
RRF (Reciprocal Rank Fusion), QMSum, NarrativeQA, FinanceBench, Seinfeld trivia dataset (in-house, speaker says it is published)

## Relevance to our work
- **agentos** (2/3): MemoryMesh already does hybrid retrieval (BM25 + pgvector) over knowledge buckets with RAGAS evals. A multi-granularity index with RRF fusion is a direct, testable change to that layer. → *Prototype a multiscale index for one MemoryMesh bucket (e.g. 3 window sizes plus parent-document lifting and RRF) and compare recall@k against the current fixed-chunk index on the RAGAS eval set.*
- **general** (1/3): The oracle experiment is a reusable way to measure how much a retrieval design choice is worth before building it. → *Read the AI21 blog post and the published Seinfeld dataset, then reuse the oracle best-per-query check as a retrieval eval for any RAG system before choosing a chunk size.*
