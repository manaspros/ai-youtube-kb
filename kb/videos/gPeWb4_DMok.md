# I Stopped Using Grep and My Agent Got 10x Faster

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `gPeWb4_DMok` · [watch](https://youtu.be/gPeWb4_DMok) · **date:** 2026-05-02 · **length:** 8:06 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Zilliz, Milvus, OpenAI, Anthropic
- **topics:** rag-retrieval, mcp-and-tools, coding-agents, token-cost-efficiency · **tags:** claude-context, mcp, codebase-indexing, semantic-search, bm25, hybrid-search, tree-sitter, merkle-dag, zilliz-cloud, milvus, opencode, glm-5-turbo, context-reduction, large-codebases

> Hands-on test of Claude Context, an MCP server that indexes a codebase into Zilliz/Milvus using Tree-sitter chunks, Merkle-based incremental updates and hybrid vector+BM25 search. Faster and richer on mid-size repos, slow to index on huge ones.

## Summary
The host introduces Claude Context, an MCP plugin from Zilliz (the Milvus team) that indexes a codebase for a coding agent instead of letting it grep and glob. It chunks code with Tree-sitter at function and class level across nine languages, tracks file hashes in a Merkle DAG with JSON snapshots so only changed files are re-indexed, and answers queries with a parallel vector search and BM25 keyword search. Setup needs a Zilliz Cloud cluster (free tier timed out, so a serverless one was used) and an OpenAI key for embeddings, and it works with any MCP-capable agent, here OpenCode with GLM5 Turbo. On the VS Code repo (about 1.5M lines) indexing took about 50 minutes and about $1.06 of embeddings. Head-to-head against plain grep/glob, the indexed agent gave richer answers with more code context, but was sometimes slower and used more tokens, and was roughly five times faster on one deep architecture question. The host's verdict is that it suits average-size repos (20-30k lines), and he admits the video is closer to a sales pitch for Zilliz. The "up to 40% context reduction" figure is quoted from the product and not measured in the video.

## Key ideas
- **Indexing the codebase gives the agent code it can find by meaning and keyword, instead of guessing with grep and glob.** — Claude Context exposes index, search, clear-index and index-status MCP tools. The agent queries the index rather than walking files, which is the core claim of the video. ([0:00](https://youtu.be/gPeWb4_DMok?t=0))
- **Retrieval is hybrid: a vector search for semantic meaning and a BM25 keyword search run together.** — Results from the two searches are combined. The host attributes up to 40% context reduction to this design, but it is a product claim, not something his tests measured. ([1:18](https://youtu.be/gPeWb4_DMok?t=78))
- **Chunking is AST-aware and incremental.** — Tree-sitter splits code into function and class chunks for nine languages, including TypeScript, Python, Rust and Go. A Merkle DAG of file hashes, stored as JSON snapshots, means only changed files are re-indexed. ([0:00](https://youtu.be/gPeWb4_DMok?t=0))
- **Indexing a very large repo is slow and costs real money in embeddings.** — On the VS Code repo (about 1.5M lines), indexing took about 50 minutes and added around 223,000 entries. OpenAI embedding spend went from $0.01 (a 23k-line test repo that indexed in under a minute) to $1.06. ([2:36](https://youtu.be/gPeWb4_DMok?t=156))
- **On a large repo, the indexed agent gave richer answers but was not consistently faster or cheaper.** — The indexed agent was slower on the first simple lookup (19s vs 14s). It was slower on one question (40s and 23k tokens vs 12s and 18k tokens), then faster on a code-display request (23s vs 49s). A broad architecture prompt took 49s and 41K tokens, and the plain agent finished faster with fewer tokens. ([3:56](https://youtu.be/gPeWb4_DMok?t=236))
- **On deep follow-up questions the indexed agent came back with more detail, but the plain agent took much longer.** — The Electron main-process follow-up took about 1m47s with the index. The plain agent spawned several sub-agents and took about five minutes, with less detail. The host could not see the sub-agents' token counts. ([5:15](https://youtu.be/gPeWb4_DMok?t=315))
- **The host's rule of thumb: use it for average-size repos, not huge ones.** — For 20-30k-line codebases, indexing is quick and the detail gain is obvious. He says he would rather use it on those than on very large codebases. He plans to keep using it for asking questions about open-source repos. ([6:41](https://youtu.be/gPeWb4_DMok?t=401))
- **Cost and setup friction are real, and the video is partly a vendor plug.** — A Zilliz account, a cluster with a public endpoint and an OpenAI key are all required, even when the agent is Claude Code. The free tier timed out, so a paid serverless cluster was needed. The host says the video is more of a sales win for Zilliz. ([6:41](https://youtu.be/gPeWb4_DMok?t=401))

## Techniques
- **Set up Claude Context as an MCP server** — Use Node >=20 and <24 (the host used 22). Add the server to the agent's MCP config (here an OpenCode JSON file). Provide a Zilliz Cloud API key, the cluster's public endpoint, and an OpenAI key for embeddings. A local Milvus instance is an alternative to Zilliz Cloud. Choose a serverless cluster, since the free tier timed out for him. *When:* When you want a code index available to any MCP-capable agent, not just Claude Code.
- **Index once, then search many times** — Ask the agent to run the index tool on the repo. Indexing runs in the background and can take tens of minutes on a large repo. The host advises against running searches while indexing is still running. Later, use the search tool for queries, the clear-index tool to reset, and the index-status tool to check progress. *When:* For repeated Q&A or exploration on a stable repo where grep and glob keep re-walking files.
- **Compare indexed and plain agents side by side** — Open two sessions on the same repo and the same prompt. One session has the index MCP enabled and the other uses only grep and glob. Compare wall-clock time and token use per prompt, and check the answer's detail. He ran single-prompt tests and then deeper follow-ups. *When:* To decide whether an indexing MCP is worth its setup and embedding cost for a given repo size.
- **Pick the repo size where the trade-off works** — On a 20-30k-line repo, expect a quick index and clearly richer answers. On a ~1.5M-line repo, expect a long index, a noticeable embedding bill, and mixed speed and token results. *When:* Before committing to indexing for a codebase.
- **Test on a cheaper model to save subscription quota** — He ran OpenCode with GLM5 Turbo instead of Claude to avoid using up the Claude Pro weekly limit. He notes that a stronger model such as Opus 4.7 at high effort might get more out of the same index, but he did not test it. *When:* When running many exploratory codebase questions and the primary model's quota is tight.

## Numbers
- Claimed up to 40% context reduction from hybrid search (product claim, not measured by the host) ([0:00](https://youtu.be/gPeWb4_DMok?t=0))
- Test repo VS Code, about 1.5 million lines of code ([1:18](https://youtu.be/gPeWb4_DMok?t=78))
- Full index of VS Code took about 50 minutes and produced over 223,000 entries ([2:36](https://youtu.be/gPeWb4_DMok?t=156))
- OpenAI embedding cost: $0.01 for a 23k-line test repo (under 1 minute to index), $1.06 after VS Code ([2:36](https://youtu.be/gPeWb4_DMok?t=156))
- First lookup (find main entry point): indexed agent 19s, plain agent 14s ([3:56](https://youtu.be/gPeWb4_DMok?t=236))
- Opening a new untitled document: indexed 40s and ~23k tokens; plain 12s and ~18k tokens ([3:56](https://youtu.be/gPeWb4_DMok?t=236))
- Showing the exact code: indexed 23s; plain 49s ([3:56](https://youtu.be/gPeWb4_DMok?t=236))
- Broad architecture prompt: indexed 49s and ~41K tokens; plain agent finished faster with fewer tokens (no figures given) ([3:56](https://youtu.be/gPeWb4_DMok?t=236))
- Electron main-process follow-up: indexed 1m47s with more detail; plain agent about 5 minutes (about 5x longer) ([5:15](https://youtu.be/gPeWb4_DMok?t=315))
- Free Zilliz tier timed out during indexing; a serverless cluster was needed ([1:18](https://youtu.be/gPeWb4_DMok?t=78))

## Hot takes
- The host says the video is more of a sales win for Zilliz, since he had never heard of them before testing the product.
- The 'up to 40% context reduction' figure comes from the product, and the host's own mixed token results do not confirm it.
- Indexing is a poor fit for huge repos. He would only use it on average-size codebases (20-30k lines), not on something like VS Code.
- The free cloud vector tier was not usable in practice (timeouts), so the real setup cost includes a paid cluster and an embeddings bill.

## Tools mentioned
Claude Context (Zilliz MCP plugin for codebase indexing and search), Zilliz Cloud (serverless cluster), Milvus (vector database), OpenAI embeddings API, OpenCode (agent harness), GLM5 Turbo (model), Claude Code (mentioned as a possible agent), Claude Pro (subscription; weekly limit), Opus 4.7 (model, not tested), Tree-sitter (AST chunking, 9 languages), BM25 (keyword index), Merkle DAG with JSON snapshots (change detection), Node.js 20-23 (runtime; 22 used), VS Code (test repo, ~1.5M lines), Electron (app architecture in the test repo)

## Relevance to our work
- **agentos** (2/3): L2A MemoryMesh already does hybrid retrieval (BM25 + pgvector). This video shows a concrete code-retrieval variant with AST chunking, Merkle-hash incremental re-indexing and a parallel vector plus BM25 fusion. It is a directly comparable design for knowledge buckets and code-aware retrieval. → *Benchmark MemoryMesh's hybrid retrieval against this design on a real repo: Tree-sitter chunking, Merkle-based incremental re-index, and BM25 plus vector fusion. Measure latency, tokens per task, and answer quality against a plain grep/glob baseline.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI. A codebase index MCP could cut exploration turns and sub-agent tokens on long runs, but the video's evidence is mixed and anecdotal. → *When ProsHarness runs Claude Code on a large repo, A/B a long task with and without a codebase index MCP, and log tokens per run before deciding whether to add it to the harness defaults.*
