# We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `dRmWYHuIJxM` · [watch](https://youtu.be/dRmWYHuIJxM) · **date:** 2026-07-18 · **length:** 10:43 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Rajkumar Sakthivel · **orgs:** Tesco
- **topics:** token-cost-efficiency, context-engineering, rag-retrieval, coding-agents · **tags:** token-cost, local-code-index, hybrid-search, bm25, embeddings, code-search, context-compression, call-graph, claude-code, cursor, copilot, shared-memory, relevance-threshold

> Rajkumar Sakthivel (Tesco) on cutting AI coding-tool token spend by sending less context: a local code index with hybrid search, slimmed results and a relevance threshold, reporting about 94% fewer input tokens on one small benchmark.

## Summary
The speaker and a friend saw their AI coding bill jump without any change in usage. Measurement showed most tokens were irrelevant context that the coding tools sent with every query, while the prompt and output-length tweaks they tried barely moved cost. They built a local layer that splits code into functions and classes, runs semantic and keyword search in parallel, shrinks the hits to names and descriptions, and drops results below a relevance threshold. Their reported benchmark on a FastAPI repo (53 files, 20 questions) went from about 83k to 4.9k tokens per question, and they say the speaker-stated caveats are that real savings are lower and that recall falls on files that do many things. They also added one index and memory shared across Claude Code, Cursor and Copilot. The talk is self-promotional for their free open-source tool, but the method and the honest limits are concrete.

## Key ideas
- **Input context, not model output, drives most of the coding-tool bill** — A typical query sent about 45k tokens of context but only about 5k was relevant. Shortening the prompt does not help because the input is already paid for when the model reads the prompt. Changing max tokens or temperature changes output, not input. ([0:00](https://youtu.be/dRmWYHuIJxM?t=0))
- **Output compression is a small lever** — Asking the model for short answers cut output 75%, but output is about 10% of cost, so the total saving was about 8%. Cutting input 94% saved about 61% of total cost by the speaker's arithmetic. ([2:29](https://youtu.be/dRmWYHuIJxM?t=149))
- **Split code by meaning, not by fixed-size chunks** — The index breaks code into functions, classes and methods so each piece is a complete unit that makes sense on its own. ([3:20](https://youtu.be/dRmWYHuIJxM?t=200))
- **Run semantic and exact-keyword search together** — Meaning search finds related code but misses exact names, and keyword search finds names but misses paraphrases. Each alone misses about 1 in 4 results; combined they miss about 1 in 10. ([4:34](https://youtu.be/dRmWYHuIJxM?t=274))
- **Use a cheap formula to decide what not to send** — The speaker tried asking the model to judge its own search hits, which added 2-3 seconds per query. A weighted score (50% semantic, 30% keyword, 20% recency) with a threshold that adapts to the top result runs in about 0.4 ms with no extra model calls. The speaker's lesson: a simple formula usually beats a complex model. ([5:59](https://youtu.be/dRmWYHuIJxM?t=359))
- **Shrink hits and link them through a call graph** — Each hit is reduced to its name and description, so a 50-line function becomes about 5 lines of context. Calls are tracked so that one hit can pull in its connected functions. ([3:20](https://youtu.be/dRmWYHuIJxM?t=200))
- **Results depend on file structure and the speaker admits the limits** — On a 396-file mixed codebase, recall barely dropped, but the speaker says the approach works best when each file does one thing and struggles when files do many things. The 94% figure is against full-file reading, which real tools already improve on, so real savings are lower. ([7:25](https://youtu.be/dRmWYHuIJxM?t=445))
- **One shared index and memory across all coding tools** — Claude Code, Cursor and Copilot each start fresh and share nothing. A single local index gives all tools the same search results, and a memory layer keeps what one tool learns about the project for the next session. ([8:47](https://youtu.be/dRmWYHuIJxM?t=527))
- **Measure savings by comparing what would have been sent with what was sent** — The tool logs every query, compares the context it would have sent with what it did send, and multiplies the difference by model price. Over 247 queries the speaker reports 12.4M tokens saved, with 84% of the savings from the search layer. ([8:47](https://youtu.be/dRmWYHuIJxM?t=527))

## Techniques
- **Code-aware chunking** — Parse source into functions, classes and methods and index each as one unit instead of fixed-size text windows. *When:* Retrieval over codebases where files have clear structure, so each returned piece is self-contained.
- **Parallel hybrid retrieval** — Run an embedding (meaning) search and an exact-word search on the same query at the same time, then merge the two result sets. *When:* Queries mix exact identifiers (function names) with paraphrased intent (login vs sign in), and either search alone misses results.
- **Result slimming** — Return only the name and description of each hit, not the full body, and fetch full code only when needed. *When:* The context budget is the bottleneck and the model needs to know what exists more than the full text.
- **Call-graph expansion** — Record which functions call which, so one hit can be expanded to its connected functions. *When:* The question needs the surrounding flow, not just the single function that matched.
- **Heuristic relevance gate instead of LLM self-grading** — Score each hit with a weighted sum (semantic 50%, keyword 30%, recency 20%) and drop hits under a threshold that adjusts to the top score, so weak results are not sent. *When:* You need a quality gate on retrieved context that adds almost no latency and no extra model calls.
- **Shared local index across tools** — Run one local index and memory store that every coding tool queries, so project knowledge is explained once and persists across sessions and tools. *When:* A team or person uses several coding agents on the same repository.
- **Per-query savings accounting** — Log every query, compare the context that would have been sent with the context actually sent, and multiply the token difference by model price. *When:* You need to prove or track the cost effect of a context-reduction change on your own project.

## Numbers
- Typical query sent about 45,000 tokens of context; about 5,000 were relevant ([0:00](https://youtu.be/dRmWYHuIJxM?t=0))
- Output compression cut output 75%, but output is about 10% of cost, so about 8% total saving ([2:29](https://youtu.be/dRmWYHuIJxM?t=149))
- About 90% of AI coding cost is input; cutting input 94% saves about 61% of total cost (speaker's arithmetic) ([2:29](https://youtu.be/dRmWYHuIJxM?t=149))
- Semantic search alone misses about 1 in 4 results; keyword search alone about 1 in 4; combined about 1 in 10 ([4:34](https://youtu.be/dRmWYHuIJxM?t=274))
- Asking the model to judge its own results added 2-3 seconds per query ([4:34](https://youtu.be/dRmWYHuIJxM?t=274))
- Relevance scoring formula runs in about 0.4 ms with no extra model calls ([5:59](https://youtu.be/dRmWYHuIJxM?t=359))
- Benchmark on FastAPI (53 files, 20 developer questions): 83k tokens per question without the tool, 4.9k with it (about 94% less) ([5:59](https://youtu.be/dRmWYHuIJxM?t=359))
- With extra compression on top, about 523 tokens per question; recall about 90% of the relevant code (speaker-reported, one public benchmark) ([5:59](https://youtu.be/dRmWYHuIJxM?t=359))
- On a 396-file mixed codebase, recall dropped almost to zero; re-indexing takes under a second ([7:25](https://youtu.be/dRmWYHuIJxM?t=445))
- Real-project report: 247 queries, 12.4 million tokens saved, about 186 saved (currency not stated in the transcript); 84% of savings from the search layer ([8:47](https://youtu.be/dRmWYHuIJxM?t=527))
- Speaker estimates models are about 30% of cost, and the other 70% is what is fed to them as input ([10:05](https://youtu.be/dRmWYHuIJxM?t=605))

## Hot takes
- Fix the input, not the output: shortening answers saves far less than cutting the context you send.
- A simple weighted formula beats asking an LLM to judge its own retrieval results most of the time.
- The model choice matters less than people think; what you feed it drives most of the cost.

## Tools mentioned
Claude Code, Cursor, GitHub Copilot, Codex, CCE (speaker's free open-source local code index; name as spoken)

## Relevance to our work
- **agentos** (2/3): MemoryMesh already plans hybrid retrieval (BM25 + pgvector); the talk gives a measured claim that merging two weak searches cuts misses from about 1 in 4 to about 1 in 10 (code-only, speaker-reported). → *Build a 20-question code-retrieval check and measure miss rate for BM25 alone, pgvector alone, and the merged result, to test whether the 1-in-4 to 1-in-10 pattern holds for MemoryMesh.*
- **prosharness** (2/3): ProsHarness wraps Claude Code runs, and the talk shows that input context drives most spend in Claude Code and that a cheap heuristic gate can cut context without extra model calls. → *Measure input tokens per ProsHarness Claude Code run, then test a slimmed-context mode (names and descriptions for non-target files) and log the token difference.*
- **general** (2/3): Directly relevant to context engineering with coding agents and to the cost of Claude Code use; the speaker's benchmark method and caveats are reusable. → *Try the open-source CCE tool the speaker names on one of our repos and run its benchmark command to get a real token baseline before adopting any approach.*
