# Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zKk7sDMGDEQ` · [watch](https://youtu.be/zKk7sDMGDEQ) · **date:** 2026-06-18 · **length:** 16:08 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kuba Rogut · **orgs:** Turbopuffer, Anthropic, Cursor, Voyage AI
- **topics:** rag-retrieval, claude-code, evals, coding-agents · **tags:** semantic code search, claude code, agentic search, grep, turbopuffer, embeddings, context retrieval, precision recall, contextbench, tool design

> Turbopuffer's Kuba Rogut benchmarks semantic code search as an extra tool for Claude Code, using a windowed-grep baseline and file, line and symbol precision and recall on human-labelled context tasks; semantic search helps precision but the gain is smaller than Cursor's because Claude Code does not know when to call it.

## Summary
The speaker from Turbopuffer, a serverless vector and full-text search database, argues that agentic grep is the default for Claude Code but that embedding-based semantic code search is a cache of computed meaning that pays off across sessions and agents. He built TurboGrep, a CLI that splits code with a tree splitter, embeds chunks with Voyage's code model and stores them in Turbopuffer. He evaluated three conditions (raw Claude Code, Claude Code with 50-line read windows, and windowed reads plus semantic search) on 50 tasks using a human-labelled dataset of golden files, lines and symbols. Semantic search raised file precision (about 65% baseline to 87% with both tools) and reduced wasted file reads, but recall did not improve overall. It helped on tasks needing behaviour-adjacent files with different keywords, while grep helped on import tracing. He says Cursor's gains are larger because Cursor trains its Composer model to know when to use the search tool, while Claude Code treats it as an extra tool. The Q&A notes that good inline comments help embeddings and that vector search suits multimodal and knowledge-base data that grep cannot handle.

## Key ideas
- **Claude Code uses agentic grep by default, and Boris said early versions used a local vector DB but grep worked better.** — Semantic code search is not built in. Cursor does index codebases into a vector store and reports real gains, so the speaker treats the question as open. ([0:00](https://youtu.be/zKk7sDMGDEQ?t=0))
- **Embeddings can be thought of as cached compute.** — Grep-based search repeats the same file reads for every session and agent on the same repo. An index pays a one-off chunk-and-embed cost, then later queries get the needed chunks faster and with fewer tokens. The saving is small per run but adds up when several agents run at once. ([2:26](https://youtu.be/zKk7sDMGDEQ?t=146))
- **Judge retrieval by the process, not only by the final answer.** — He used a human-labelled dataset (ContextBench-style) that lists the golden files, lines and symbols an agent should read. It scores whether the agent found them along the way, which the end-to-end pass rate does not show. ([4:54](https://youtu.be/zKk7sDMGDEQ?t=294))
- **Unbounded file reads make the comparison noisy, so the baseline caps reads at 50 lines.** — Reading whole files of about 1,000 lines swamped the signal. He tested raw Claude Code, Claude Code with 50-line windowed reads, and windowed reads plus semantic search. ([4:54](https://youtu.be/zKk7sDMGDEQ?t=294))
- **Semantic search raises file precision but not overall recall.** — Baseline Claude Code had about 65% file precision. Adding windowed grep and then semantic search brought it to about 87%, meaning roughly one wasted file in eight versus one in three. Recall stayed about the same and line recall dropped in some runs. ([6:21](https://youtu.be/zKk7sDMGDEQ?t=381))
- **The two search methods win on different kinds of task.** — Semantic search found behaviour-adjacent files, such as ORM handling spread across libraries, where keywords missed them. Grep won on tracing imports, where a keyword from the first or second call finds the chain. Routing between them per task is the open problem. ([8:49](https://youtu.be/zKk7sDMGDEQ?t=529))
- **The gap with Cursor comes from tool-use training, not from the search tool.** — Claude Code is built around grep, so semantic search feels like an extra tool that the model rarely knows when to call. Cursor's Composer model is trained to use its search tool, which the speaker links to its larger gain. He predicts that lightweight tools for different retrieval modes will win long term. ([10:06](https://youtu.be/zKk7sDMGDEQ?t=606))

## Techniques
- **Chunk-embed-index semantic code search as a CLI tool** — Walk the file tree, split code with a tree-based splitter, embed chunks with a code embedding model (Voyage code-3 in the talk) and upsert them into a vector DB (Turbopuffer). The agent calls a search command that embeds the query and returns the nearest chunks. *When:* When the same repo is searched across many sessions or agents, and queries need behaviour-adjacent files that do not share keywords.
- **Windowed file reads as a retrieval baseline** — Cap each read tool call at about 50 lines so the agent cannot pull whole files. This keeps the measure of which lines were read clean. *When:* When benchmarking agent context retrieval, to stop long files from drowning out the precision and recall signal.
- **Trajectory-level retrieval evaluation** — Score an agent on which golden files, lines and symbols it reads along the way (file, line and symbol precision and recall), using a human-labelled dataset, not only whether the task passed. *When:* When you want to know whether a coding agent is looking in the right places, or to compare retrieval tools fairly.
- **Inline comments as embedding context** — Keep docstrings and comments above functions in the indexed chunks, since they add natural-language meaning that the code embedding can match. *When:* When semantic code search is weak on code with little natural-language description.

## Numbers
- Cursor reports about a 24% relative improvement in answer accuracy with its Composer model when semantic code search is enabled, and about 12 to 13% across all models. ([1:04](https://youtu.be/zKk7sDMGDEQ?t=64))
- Cursor's online A/B test: +2.6% code retention in large codebases and -2.2% dissatisfied user requests with semantic search enabled. ([1:04](https://youtu.be/zKk7sDMGDEQ?t=64))
- Baseline Claude Code file precision about 65%, rising to about 87% with windowed grep plus semantic search. Roughly one wasted file in three reads falls to one in eight. ([6:21](https://youtu.be/zKk7sDMGDEQ?t=381))
- Line precision about 33% and symbol precision about 43% at baseline. ([6:21](https://youtu.be/zKk7sDMGDEQ?t=381))
- Benchmark covers 50 tasks; the speaker cites a 23.5% performance gain for Cursor's Composer model with semantic search. ([8:49](https://youtu.be/zKk7sDMGDEQ?t=529))
- A 6,000-token grep trace is cited as the cost of one agentic search pass; the cost compounds across sessions and parallel agents. ([2:26](https://youtu.be/zKk7sDMGDEQ?t=146))

## Hot takes
- Grep-only agentic search is not enough long term, and lightweight semantic tools will win.
- Claude Code is built for grep, so a bolted-on semantic tool underperforms because the model does not know when to use it.

## Tools mentioned
Turbopuffer, Voyage code-3, Claude Code, Cursor, TurboGrep, tree splitter

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code, so the finding that Claude Code under-uses an extra search tool bears directly on how the harness exposes tools and skills. → *When adding a tool to the ProsHarness Claude Code setup, test whether the model actually calls it using a trajectory-level check, not only a pass/fail check.*
- **general** (2/3): Concrete evidence that tool choice and tool-use training matter as much as the tool, plus a trajectory-level eval method for coding agents. → *Read the ContextBench paper and add file, line and symbol precision and recall to any coding-agent eval harness.*
- **agentos** (1/3): Relevant to the RAG and retrieval layer (L2A MemoryMesh) and the cheap-indexing idea. The talk is about coding-agent retrieval, not AgentOS's own agent traffic. → *Read the ContextBench paper and reuse its file, line and symbol precision and recall as a retrieval metric when evaluating MemoryMesh hybrid retrieval.*
