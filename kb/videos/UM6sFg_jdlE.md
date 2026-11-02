# RAG is dead, right?? — Kuba Rogut, Turbopuffer

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `UM6sFg_jdlE` · [watch](https://youtu.be/UM6sFg_jdlE) · **date:** 2026-06-18 · **length:** 11:13 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kuba Rogut · **orgs:** Turbopuffer, Cursor, Anthropic, Google
- **topics:** rag-retrieval, coding-agents, context-engineering, infra-cost-scaling · **tags:** rag, agentic-search, vector-search, bm25, full-text-search, merkle-tree, codebase-indexing, context-window, cache-compute, turbopuffer

> Kuba Rogut (Turbopuffer) argues that "RAG is dead" misreads the problem: retrieval should be a toolbox (vector, BM25, grep, filters) used in iterative agent loops, and embeddings work best as precomputed cache compute.

## Summary
The speaker, a deployed engineer at Turbopuffer (a vector and full-text search database on object storage), argues that the "RAG is dead" posts conflate RAG with naive one-shot vector search. He says retrieval covers vector search, BM25 full-text, grep, glob, regex and metadata filters, and that "agentic search" is commonly equated with file-system grep. He defines agentic search as giving agents tools to search, read and reason over context progressively. He cites Cursor as a strong example: it indexes codebases with Merkle-tree hashing so teammates' near-identical repos reuse embeddings, and it reports measurable answer-accuracy gains from semantic search. He notes that per-query benefit is diluted because semantic search is not used on every query, which is why online A/B deltas look small. He says Claude Code reportedly dropped an early local vector-RAG design, and he frames embeddings as cache compute: pay indexing once rather than repeating grep-read loops in every session. He closes with a Jeff Dean quote, "you don't need a trillion at once, you need the right million", arguing that staged retrieval stays necessary even with huge context windows. The data comes from a vendor employee and relies on secondhand claims about Cursor and Claude Code, so treat the figures as indicative rather than verified.

## Key ideas
- **Retrieval is not just vector search** — The speaker splits RAG into retrieval plus augmented generation and says retrieval includes vector search, BM25 full-text, grep, glob, regex and basic filters. Naive RAG (embed, search once, stuff the context) is the narrow version people are calling dead. ([1:06](https://youtu.be/UM6sFg_jdlE?t=66))
- **Agentic search means giving agents progressive retrieval tools** — People often equate agentic search with grepping a file system (as in Claude Code or Codex). The speaker's definition is broader: agents get tools to search, read, judge whether they have enough, and repeat until the task state is satisfied. ([2:06](https://youtu.be/UM6sFg_jdlE?t=126))
- **Cursor shares codebase indexes across teammates with Merkle trees** — Most engineers on a team open near-identical repos. Cursor hashes files into Merkle trees to find similar codebases, copies existing embeddings, and re-chunks and re-embeds only changed files. The speaker says Turbopuffer stores the index and that this is done securely. ([3:04](https://youtu.be/UM6sFg_jdlE?t=184))
- **Semantic search gives measurable accuracy gains inside an agent** — On Cursor's internal context benchmark (not public), semantic search raised answer accuracy by roughly 12.5 to 13.5 percent on average across models, and about 24 percent for the Composer model before Composer 2. Online A/B results were smaller (about 2.6 percent code retention and 2.2 percent fewer dissatisfied requests) because the tool is not used on every query. ([4:27](https://youtu.be/UM6sFg_jdlE?t=267))
- **Embeddings act as cache compute for agents** — Per-session discovery makes an agent repeat grep, read and assess steps every time a question is asked, across many developers and days. A one-time index plus a lightweight runtime query saves tokens, time and money. The speaker notes Claude Code reportedly moved away from an early local vector-RAG design. ([7:08](https://youtu.be/UM6sFg_jdlE?t=428))
- **Retrieval has become an iterative multi-call loop** — Sophisticated customers run many searches (semantic or full-text), reason between steps, and fetch only what the specific use case needs. Retrieval is no longer one call to a vector DB. ([8:30](https://youtu.be/UM6sFg_jdlE?t=510))
- **Large context windows do not remove the need for staged retrieval** — Quoting Jeff Dean, the speaker argues that even trillion-token windows need a lightweight mechanism to narrow a corpus to the right million, or the right 100k or 10k, before it enters the context. ([9:55](https://youtu.be/UM6sFg_jdlE?t=595))

## Techniques
- **Multi-modal retrieval toolbox for agents** — Expose vector search, BM25 full-text, regex/grep, glob and metadata filters to the agent as separate tools, and let it choose and combine them per step. *When:* Agent tasks over code or documents where exact-match and semantic lookups both matter, and one retrieval method alone misses things.
- **Iterative search-read-assess loop** — Let the agent search, read the hits, decide whether the information is sufficient, and search again with refined queries, stopping when the task state is met. *When:* Multi-step questions where the first retrieval is rarely enough and the agent can judge what it is still missing.
- **Index once, query at runtime** — Parse, chunk and embed a corpus ahead of time into a shared store, then expose a cheap semantic-query tool so agents skip repeated grep-and-read discovery in each session. *When:* Many users or sessions repeatedly ask about the same corpus, such as a team codebase or internal docs.
- **Merkle-tree index reuse across near-identical corpora** — Hash files into a Merkle tree, find existing indexes with similar hashes, copy their embeddings, and re-chunk and re-embed only the changed files. *When:* A team or organisation opens many near-identical repos or branches, so full re-indexing on each open is expensive.
- **Staged narrowing before the context window** — Use a cheap retrieval layer to reduce a huge corpus to the relevant subset before the LLM sees it, instead of relying on a bigger context window. *When:* The corpus is far larger than any usable context, such as trillions of tokens across customer data.

## Numbers
- Average answer-accuracy increase from semantic search across models on Cursor's internal context benchmark (internal, not public) ([4:27](https://youtu.be/UM6sFg_jdlE?t=267))
- Answer-accuracy increase for the Composer model before Composer 2 with semantic search ([4:27](https://youtu.be/UM6sFg_jdlE?t=267))
- Online A/B: about 2.6 percent code retention increase in large codebases (as stated) ([4:27](https://youtu.be/UM6sFg_jdlE?t=267))
- Online A/B: about 2.2 percent decrease in dissatisfied user requests (small because semantic search is not used on every query) ([5:38](https://youtu.be/UM6sFg_jdlE?t=338))
- Illustrative cost of one per-session grep-read sub-step in an agent trace is about 6,000 tokens (repeated per developer per day) ([7:08](https://youtu.be/UM6sFg_jdlE?t=428))
- Turbopuffer customers store trillions of tokens; the goal is narrowing to roughly 100k to 1M tokens for context ([9:55](https://youtu.be/UM6sFg_jdlE?t=595))

## Hot takes
- RAG is not dead; the narrow one-shot vector-search version is what is dying, and agentic search is retrieval with iterative tool calls.
- Embeddings are better treated as precomputed cache compute for agents than as a per-session discovery step.
- Claude Code reportedly abandoned an early local vector-RAG design, and per-query benefit from semantic search is small, so aggregate A/B numbers understate it.
- Bigger context windows do not replace retrieval: you still need the right million tokens, not the whole trillion.

## Tools mentioned
Claude Code, Codex, Cursor, Turbopuffer, BM25, Merkle trees

## Relevance to our work
- **agentos** (2/3): MemoryMesh already does hybrid BM25 plus pgvector retrieval and RAGAS evals. The talk's case for giving agents multiple retrieval tools and iterative search bears directly on how MemoryMesh is exposed to agents. → *Add an eval arm in MemoryMesh comparing one-shot hybrid retrieval against an agent loop that can issue BM25, regex and vector queries iteratively, scored on RAGAS plus token cost per answer.*
- **prosharness** (1/3): ProsHarness resumes long Claude Code runs, so repeated repo discovery per session may waste tokens. The talk's point that cached indexes cut per-session discovery applies in principle. → *Measure how many tokens a resumed run spends rediscovering repo structure, and test whether a cached index or search tool reduces that cost.*
- **general** (1/3): The talk gives a concrete, customer-linked view of how coding agents retrieve context, which fits the recurring interests in context engineering and Claude Code workflows. → *Read Cursor's codebase-indexing blog post (Merkle-tree reuse) and the semantic-search blog post the speaker cites, and compare the reported numbers against the speaker's secondhand summary.*
