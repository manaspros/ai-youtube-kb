# How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `1IdzkRVmWAA` · [watch](https://youtu.be/1IdzkRVmWAA) · **date:** 2026-07-18 · **length:** 14:28 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Hanna Lichtenberg, Amir · **orgs:** Mixedbread, OpenAI, Databricks, Snowflake
- **topics:** rag-retrieval, agent-architecture, training-finetuning-rl, evals · **tags:** agentic-search, knowledge-gap, oracle-gap, query-writing, bm25, tool-design, sft-rl, ndcg, llm-judge, browsecomp-plus, office-qa-pro, medqa

> Mixedbread's team on why agents write keyword-soup queries that hurt retrieval, and how a bounded four-tool search harness, trained with SFT then RL, recovers much of the oracle gap.

## Summary
Hanna Lichtenberg and Amir of Mixedbread argue that LLM reasoning has improved fast while search has barely moved, and that this mismatch, which they call the knowledge gap, is now the bottleneck for agents on document-heavy work. On BrowseComp-Plus and Office QA Pro, the gap between an oracle with the right documents and a default-tools agent (Codex) is about 8-9 points, and swapping in a stronger search tool closes most of it. They find that agents write keyword-stuffed queries, which they trace to coding-agent training (grep), web-tool habits and benchmarks that reward entity-keyword queries. Their answer is a search agent with four tools (wide overview search, full-payload semantic search, metadata-facet filtering, and keyword grep), at most four search rounds with parallel queries per round, and chunk deduplication across rounds. The agent is trained by SFT from a larger teacher model, then on-policy RL with a reward that mixes NDCG and rubric judging of the final ranking with an LLM judge of trajectory quality. Reported results are a jump on the Oblique Congress benchmark and a top leaderboard result on MedQA with Gemini 3.5 Flash using their search tool; the trained agent itself is not released and the results are vendor-reported.

## Key ideas
- **The bottleneck is access to knowledge, not reasoning** — With the right documents supplied (oracle), models score 93% on BrowseComp-Plus and 64% on Office QA Pro. Default agent tools drop about 9 and 8 points, so better retrieval, not a better model, is what is missing. ([2:27](https://youtu.be/1IdzkRVmWAA?t=147))
- **Better search recovers most of the gap** — Plugging in Mixedbread's search (latent-interaction based) with GPT-5 gets within about 3 points of the oracle on BrowseComp-Plus and almost closes it on Office QA Pro. ([2:27](https://youtu.be/1IdzkRVmWAA?t=147))
- **Agents write keyword soup because of their training** — The speaker names three causes: coding-agent training around grep-style regex exploration, web-tool habits that mimic human keyword queries, and benchmarks with entity-style queries that favour BM25. The result is gibberish queries that a semantic engine handles badly. ([3:55](https://youtu.be/1IdzkRVmWAA?t=235))
- **Give the agent several specialised search tools, not one** — Four tools: overview search (up to 50 chunks, summaries only, to see what the corpus contains), main semantic search (full payload for top 10), a metadata-facet filter tool, and a keyword grep tool. The agent picks the tool per sub-question. ([5:20](https://youtu.be/1IdzkRVmWAA?t=320))
- **Keep the loop short and bounded** — The agent gets at most four search rounds, each with up to four parallel queries. It starts with a preview from an initial semantic search plus metadata hints, dedupes chunks across rounds, and submits a ranked list when it has enough evidence. ([6:40](https://youtu.be/1IdzkRVmWAA?t=400))
- **Change the task framing to change the query style** — Asking for one concise sentence describing what to find, instead of asking for a search query, stops the model from falling back to BM25-style keyword strings. Examples of splitting a question into aspects help too. ([8:09](https://youtu.be/1IdzkRVmWAA?t=489))
- **Train a small model with SFT then RL on a combined reward** — Supervised fine-tuning from a larger teacher is followed by on-policy RL. The reward is a retrieval term (NDCG plus rubric-based LLM judging of relevance and ranking plausibility) plus a trajectory term (LLM judging whether queries are natural sentences and whether the amount of exploration is right). ([9:32](https://youtu.be/1IdzkRVmWAA?t=572))

## Techniques
- **Tiered search tool set for agents** — Expose a cheap wide tool that returns only summaries, a deep tool that returns full chunks for a few hits, a metadata-facet filter, and an exact keyword tool. Let the agent choose per sub-question. *When:* When the corpus is large and the agent needs both orientation and precise evidence without filling its context.
- **Bounded parallel search rounds with dedupe** — Cap the loop at a fixed number of rounds (four here), allow a fixed number of parallel queries per round, and deduplicate chunks before they reach the context. *When:* For fast, cheap agents where unbounded exploration would blow up latency and context.
- **Priming with a corpus preview** — Before the agent plans, run one initial semantic search on the user query and include the hits plus available metadata facets in its prompt. *When:* When the agent does not know the corpus vocabulary or structure and would otherwise guess keywords.
- **Describe-the-need query framing** — Ask the model to write one concise natural-language sentence describing the evidence it wants, rather than asking it to write a search query. Add a few examples of splitting a question into aspects. *When:* When the model keeps producing keyword-stuffed queries that suit BM25 but not semantic retrieval.
- **Oracle-gap diagnosis** — Run the task once with gold documents supplied and once with the agent's own retrieval, then compare. The difference shows whether retrieval or reasoning is the bottleneck. *When:* Before investing in a bigger model or more prompt work on a retrieval-heavy agent.
- **SFT then on-policy RL with a mixed reward** — Warm-start a small model on teacher trajectories, then run RL where the reward combines a standard ranking metric and rubric-based LLM judging of the final output, plus an LLM judge of trajectory quality such as query naturalness and exploration amount. *When:* When a narrow agent behaviour (tool choice, query style, search budget) must be taught to a small, fast model.

## Numbers
- Oracle (gold documents supplied) scores: BrowseComp-Plus 93%, Office QA Pro 64% ([2:27](https://youtu.be/1IdzkRVmWAA?t=147))
- Codex with default tools drops about 9 points on BrowseComp-Plus and about 8 points on Office QA Pro versus the oracle ([2:27](https://youtu.be/1IdzkRVmWAA?t=147))
- GPT-5 with Mixedbread search is about 3 points from the oracle on BrowseComp-Plus; Office QA Pro gap almost fully closed ([2:27](https://youtu.be/1IdzkRVmWAA?t=147))
- Overview search returns up to 50 chunks as summaries; semantic search returns full payloads for the top 10 ([5:20](https://youtu.be/1IdzkRVmWAA?t=320))
- Agent loop is capped at 4 search rounds, with up to 4 parallel queries per round ([6:40](https://youtu.be/1IdzkRVmWAA?t=400))
- Oblique Congress benchmark NDCG@10 about 0.4 for their agent, versus 0.18 for the best agent in the benchmark paper (GPT multi-hop agent); speaker says intermediate result ([12:25](https://youtu.be/1IdzkRVmWAA?t=745))
- 93.4% accuracy on Snowflake's MedQA leaderboard (top-1 per speaker) with Gemini 3.5 Flash using their agentic search as the search tool; speaker says it uses less effort than comparable LLMs with other search agents ([13:41](https://youtu.be/1IdzkRVmWAA?t=821))

## Hot takes
- Search has improved very slowly over the last 20 years while LLM reasoning has grown exponentially, so retrieval is now the limiting factor for agents beyond code.
- Models are not bad at reasoning; with the right documents they are very strong, so the gap is in access to knowledge.
- Most current agent benchmarks reward entity-keyword queries and so favour BM25, which pushes agents toward keyword soup.

## Tools mentioned
Mixedbread search, Codex, GPT-5, Gemini 3.5 Flash, grep, BM25

## Relevance to our work
- **agentos** (2/3): MemoryMesh already does hybrid retrieval (BM25 plus pgvector). The talk shows agent-written queries are a weak point and that splitting overview and full-payload search helps. → *Add a cheap overview tool (summaries only, up to about 50 hits) in front of MemoryMesh's full-chunk retrieval, and run an oracle-gap check on a small internal corpus with gold documents supplied.*
- **prosharness** (1/3): Bounded rounds with dedupe is a general harness pattern for keeping a long agent loop cheap and predictable. → *If a ProsHarness search or exploration loop starts to spiral, cap its rounds and dedupe its results, borrowing the four-round, four-parallel-query limits.*
- **general** (1/3): The oracle-gap diagnostic (supply gold inputs, see whether the failure is retrieval or reasoning) also fits entity-resolution candidate generation and any retrieval-heavy pipeline. → *For the entity-resolution work, run the oracle test: give the matcher known-correct candidates and check whether the misses come from candidate retrieval or from the matching step.*
