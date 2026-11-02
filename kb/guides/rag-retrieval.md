# Guide: rag-retrieval

*Synthesized by Sonnet from 64 talks since 2026-05-18.*

## State of the art (what practitioners actually do now)

Retrieval is no longer a fixed pipeline. It is a set of tools that an agent calls in a loop. The agent searches, reads, checks if it has enough, and searches again. Recent talks (Jun-Oct 2026) agree on this shape (`UM6sFg_jdlE`, `ksjwtQop4os`, `X4w2Pkz5tDY`, `gonAewBZxfU`).

What a good 2026 stack looks like:

- **Hybrid first.** BM25 plus dense vectors, fused with Reciprocal Rank Fusion (RRF). A reranker is optional and only added when latency allows and precision gain is measured (`ksjwtQop4os`, `gonAewBZxfU`).
- **A small toolbox, not one search call.** Typical tools: wide overview search, deep semantic search, metadata filter, exact keyword or grep, read-with-offset (`1IdzkRVmWAA`, `X4w2Pkz5tDY`, `O84lhGc1OOI`).
- **Bounded loops.** Cap rounds, parallel queries and handoffs. Dedupe chunks across rounds (`1IdzkRVmWAA`, `gonAewBZxfU`).
- **Corpus size picks the method.** Roughly 100 to 1,000 files can use grep and reads. Thousands or more need an index (`X4w2Pkz5tDY`). For code, grep is a strong default, and semantic search adds a smaller gain (`zKk7sDMGDEQ`, `T3SS931wU0I`).
- **Parsing decides the ceiling.** Layout-aware parsing, a fast pass first, and a VLM only for hard pages (`RQi7x-navxU`, `0I07YAuF8xA`, `-x5GEVnkuRw`).
- **Graphs for connected questions only.** Vector search finds the entry node, then graph traversal expands it. Use it for 3+ hop or aggregation questions (`LJ2a9nX3vlo`, `Q0VkgCyNVUg`, `vJukHCIv7Ck`).
- **Tools are retrieved too.** Embed tool descriptions and inject only the top-K schemas (`vh2VGuQ3zhY`, `vJukHCIv7Ck`, `KtBivPzmOM8`).

## Consensus patterns

1. **Hybrid beats vector-only.** BM25 catches exact identifiers that embeddings miss. Fuse by rank (RRF), not by raw score, because the scales differ. `ksjwtQop4os`; `gonAewBZxfU` (hit rate 92% to 97%); `O84lhGc1OOI`; `YXb2Wx1r_Pk`.
2. **Give agents several specialised search tools.** One generic tool leads to keyword-soup queries. `1IdzkRVmWAA`, `X4w2Pkz5tDY`, `UM6sFg_jdlE`, `ynJyIKwjonM`.
3. **Narrow-to-wide tool ladder with guardrails.** Start at chunk search, then fetch a section, then a document. Block oversized dumps, return valid section names on a bad lookup. `gonAewBZxfU`, `1IdzkRVmWAA`.
4. **Tool descriptions are part of retrieval quality.** State when to use the tool, when not to, and ordering. Return query errors to the agent so it can rewrite. `ynJyIKwjonM`, `ORVh4GivEU0`, `spxoDAfh5ig`.
5. **Chunk by structure, not fixed windows.** Use headings, Q&A shape, functions, section paths. Never split a table. `Akm1sqvWG4A`, `dRmWYHuIJxM`, `gonAewBZxfU`, `qflLT3SoVbw`.
6. **Tables need their own handling.** Flatten merged cells into self-contained rows, or store two forms (structured for reasoning, prose for embedding). `gonAewBZxfU`, `0I07YAuF8xA`.
7. **Clean the corpus before indexing.** Dedupe, drop stale files, tag with metadata, apply permissions at ingest. `wzWNYDY7toc`, `X4w2Pkz5tDY`, `5ID22ACI7IM`.
8. **Tune the baseline before comparing methods.** An untuned BM25 made embeddings look better than they were. `fZH97QHHYjY`, `O84lhGc1OOI`.
9. **Judge retrieval by the agent's trajectory and end task, not one-shot rank metrics.** `fZH97QHHYjY`, `T3SS931wU0I`.
10. **Surface source conflicts and provenance.** Do not silently pick one. Carry source and permission tags into answers. `5ID22ACI7IM`, `BiG2ssibKGc`, `tJFjeMBKbIY`.
11. **Structured questions need a query engine, not just RAG.** Discover the schema by sampling, validate generated queries in code, inject tenant filters in code, retry with errors fed back (bounded). `spxoDAfh5ig`, `ORVh4GivEU0`.
12. **Retrieve tools and skills on demand.** Tool schemas cost tokens on every call. `vh2VGuQ3zhY`, `vJukHCIv7Ck`, `KtBivPzmOM8`.
13. **Debug retrieval before touching weights.** Check if the right chunks were retrieved first. `qflLT3SoVbw`.

## Disagreements & open questions

- **Grep vs embeddings.** Braintrust found equal accuracy for coding bug-finding, with vector search costing about 4x more (`T3SS931wU0I`, only ~20 tasks, one trial). Turbopuffer found a file-precision gain from adding semantic search to Claude Code (`zKk7sDMGDEQ`). The likely answer is that it depends on corpus type and scale (`X4w2Pkz5tDY`).
- **Is BM25 enough?** Bergum says BM25 plus grep is strong because agents write long precise queries (`fZH97QHHYjY`). Mixedbread says agents write keyword soup and need training and semantic tools (`1IdzkRVmWAA`). Clavié lands on hybrid (`O84lhGc1OOI`).
- **Does chunking still matter?** AI21 says yes, and index at many sizes (`r9OwPx_HoV0`). Red Hat shows chunkless retrieval over a document outline (`-x5GEVnkuRw`). Storage cost of multiscale indexing is the open price.
- **Graph or not.** Neo4j talks push graphs hard but are vendor talks (`eW_vxrjvERk`, `abvQEhvRI_c`). A practitioner warns graphs are often the wrong tool (`3ySF0I5iE_0`). A file-based wiki skips both (`ZRM_TfEZcIo`).
- **Memory vs context.** Full history beat compaction on one tutor eval (`WP3hjUXd918`). Others want typed, governed memory stores (`BIhiYL4U9_M`, `KtBivPzmOM8`).
- **Cost of agentic search.** It finds the right doc about twice as often but costs 100-1,000x a classic query (`iJVxxxHM_Oc`). Learned sub-agents are a proposed fix, with vendor numbers only.
- **Open:** how many chunk sizes, and is there a better fuser than RRF (`r9OwPx_HoV0`). LLM judges for RAG evals are noisy (`gonAewBZxfU`).

## How thinking changed over time (dated)

- **May 2026.** "Context engineering is mostly search tool choice." Fixed RAG pipelines are replaced by agentic RAG, and zero results can be a failure (`ynJyIKwjonM`). Graph memory is pitched as the fix for vector gaps (`eW_vxrjvERk`).
- **Jun 2026.** "RAG is dead" is reframed as a toolbox plus iterative loops, with embeddings as cached compute (`UM6sFg_jdlE`). Semantic code search measured against grep (`zKk7sDMGDEQ`).
- **Jul 2026.** Focus moves to teaching agents to query well (`1IdzkRVmWAA`), and to tool retrieval (`vh2VGuQ3zhY`). Local, framework-free hybrid RAG becomes a common recipe (`Akm1sqvWG4A`).
- **Aug 2026.** Graphs get more careful: schema-first, deterministic structure, metadata-only layers (`3ySF0I5iE_0`, `kRkcNOsRyYg`).
- **Sep 2026.** Baselines re-examined. BM25 is "back" (`fZH97QHHYjY`), hybrid reaches about 90% on BrowseComp-Plus (`O84lhGc1OOI`), and chunking is revisited (`r9OwPx_HoV0`). Document parsing is treated as the context layer (`RQi7x-navxU`, `0I07YAuF8xA`).
- **Oct 2026.** Practical numbers on regulated RAG (`gonAewBZxfU`), structured query engines (`spxoDAfh5ig`), and a skeptical small eval of vectors for code (`T3SS931wU0I`).

## Numbers worth remembering

- BrowseComp-Plus: bad BM25 about 60%, tuned lexical 70-80%, hybrid harness 90.2% with about 20% fewer tool calls (`O84lhGc1OOI`). Corpus size is stated inconsistently in captions.
- Oracle (gold docs) 93% on BrowseComp-Plus; default Codex tools lose about 9 points; Mixedbread search gets within about 3 (`1IdzkRVmWAA`).
- Multiscale chunking gains about 20-40% recall over the best fixed size (`r9OwPx_HoV0`).
- Hybrid dense+BM25 with RRF: hit rate 92% to 97% on 63 questions (`gonAewBZxfU`). Corpus: about 270 PDFs, 6,000 pages, 3,000 tables.
- Vector search cost about 4x agentic search at equal accuracy, on about 20 tasks (`T3SS931wU0I`).
- Claude Code file precision about 65% baseline to about 87% with semantic search added (`zKk7sDMGDEQ`).
- Tool routing: selection accuracy about 78% at 10 tools, 13.6% at 741 tools. Routed stays above 83%. 741 schemas cost about 127K tokens (`vh2VGuQ3zhY`).
- A local code index cut input tokens about 94% on one small benchmark: about 83K tokens per question down to about 4.9K on a FastAPI repo (53 files, 20 questions) (`dRmWYHuIJxM`).
- Agents spend 30-50% of tokens on search (`iJVxxxHM_Oc`).
- Stale or duplicate files at 30% of a corpus can fill up to 80% of context (`wzWNYDY7toc`, speaker's internal eval).
- Skills of 3-5K tokens each overflow context fast; tools and skills can take over 50% of the window (`KtBivPzmOM8`).
- Context bundle cut one task from up to $2.60 to $1.29 (`ORVh4GivEU0`, single run).
- Local file search fits about 100-1,000 files (`X4w2Pkz5tDY`). Graph RAG matters at 3+ hops (`LJ2a9nX3vlo`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Source: 18 creator videos cited in this section, Nov 2025 to Oct 2026. Mostly tutorials and tool reviews. Most numbers come from one demo, the creator's own benchmark, or a vendor. Treat them as leads to test.

### Practical playbook

1. **Decide per query whether you need retrieval.** Put a thin router in front of a curated Markdown bundle and a vector index. Send exact, high-stakes questions (policy values, prices) to the bundle. Send open-ended questions to RAG. Trust a curated concept over a retrieved chunk. Single creator demo, no measurements (`CnfuoBYmkJE`).
2. **Chunk on the document's own units.** Put section markers first in the splitter's separator list, then blank lines, newlines and spaces. The demo uses scene headings, 2,500-character chunks and 250 characters of overlap. The demo does not test other chunk sizes (`pvCabUerwss`).
3. **Persist the index and rebuild only when it is missing.** Use a local Qdrant path. Open the existing collection first, and build from documents only if it is not found (`pvCabUerwss`).
4. **Start the grounding prompt strict, then loosen it by one line.** A "use only the excerpts" prompt refused an answerable question that was spread across chunks. Add a line that allows the best partial answer. Keep three probes as a regression set: one in-scope, one out-of-scope, one prompt-injection string (`pvCabUerwss`).
5. **Give a coding agent a code index before it greps.** Claude Context indexes code with Tree-sitter chunks and runs vector plus BM25 search. Index once in the background, and do not search while indexing runs. The indexed agent gave richer answers but was not consistently faster or cheaper (`gPeWb4_DMok`).
6. **Benchmark the index on your own repo first.** Run two sessions on the same repo and prompt, one with the index and one with grep and glob only. Compare wall-clock time, tokens per prompt and answer detail. The host's sweet spot is a 20-30k-line repo. Indexing about 1.5M lines took about 50 minutes and about $1.06 in embeddings (`gPeWb4_DMok`).
7. **Use a code graph for call-chain questions.** Build a graph of entities and edges once. Answer "what uses X" and "what breaks if X changes" by walking edges. Re-read only files whose SHA256 changed, and rebuild on each commit with a git hook (`8Kv2tn22QNo`). The impact-walk idea also appears in `cyIWQHYoUg8`.
8. **Label every derived link.** Tag each edge Extracted (parsed), Inferred (model reasoned) or Ambiguous (model flagged). Check Inferred and Ambiguous links before they drive a decision (`8Kv2tn22QNo`).
9. **Limit data egress by source type.** Parse code locally, transcribe audio locally, and send only PDFs and images to a remote model. Offer a code-only mode with no remote pass (`8Kv2tn22QNo`).
10. **Run a lint pass on any wiki the agent maintains.** Check for contradictions, dead pages, stale claims and invented content. Add a rule against adding facts the author did not write. The host says lint is the step most tutorials skip. He says about five minutes a week (`8Kv2tn22QNo`).
11. **Convert to Markdown before indexing.** Use one converter for many file types (`9ZaiZzp4XcY`). Crawl web sources to Markdown with page metadata (`YxC1zEz5TDY`, `BpsRH-1TZk4`). Messy scans and dense tables may need a heavier parser.
12. **Test a vector store on your own data with exact ground truth.** Brute-force the top-K over the vectors you actually loaded. Store the top 1,000 to 10,000 per query so one run serves any smaller k. Sweep each engine's effort setting and compare latency at matched recall (`6Uj6GXIpX9s`).
13. **Route by data shape.** For structured, clearly named data, a bash agent (ls, find, grep, cat) can answer without a vector DB. Use RAG for fuzzy queries or unorganized files. Log every tool call to check the path taken (`gZr5VmsXmXQ`).
14. **Make the agent query the knowledge base on its own.** A rules file can tell the agent to query before it writes PRDs or tasks, and whenever it is unsure. Fall back to code examples when docs are thin. This comes from a video with a sponsor segment (`EgXOaH-ZqfU`).

### Tools creators recommend (tool — what for — video_id)

- Claude Context (MCP) — hybrid code index for any MCP-capable agent; the host calls the video partly a sales pitch for Zilliz — `gPeWb4_DMok`
- Graphify + Obsidian — code graph with provenance labels and a wiki layer; the 70x token figure is self-reported — `8Kv2tn22QNo`
- Graft — code graph that injects matching file:line locations through Claude Code hooks; the benchmark is self-reported — `cyIWQHYoUg8`
- Cloudflare AutoRAG + R2 — managed index over a bucket of Markdown; beta, playground shows per-file scores — `YxC1zEz5TDY`
- Firecrawl — crawl a docs site to Markdown with metadata — `YxC1zEz5TDY`
- Crawl4AI — Python crawler with Markdown output, prefetch, resumable deep crawl and schema extraction — `BpsRH-1TZk4`
- MarkItDown — one converter from Office, PDF, image and audio files to Markdown — `9ZaiZzp4XcY`
- LangExtract — prompt-defined extraction where each field links to its source span — `96P65wL2zmw`
- Google OKF — Markdown concept bundle with index.md per folder and YAML front matter, governed in Git — `CnfuoBYmkJE`, `k4sMSsMzX2g`
- Qdrant FineWeb dataset and toolchain — 10B vectors with exact ground truth for vector store tests — `6Uj6GXIpX9s`
- Archon — self-hosted project docs, backlog and RAG over MCP; needs Supabase and Docker; sponsor segment — `EgXOaH-ZqfU`
- grep.app (MCP) — regex search over public GitHub code for real API usage — `IYyyiA5eWEo`
- AnythingLLM — local RAG app with LanceDB as the default store — `pSYEcJTt4t4`
- Open Notebook — self-hosted NotebookLM alternative with a REST API — `DnMtDdkSIi0`
- NotebookLM CLI — a notebook as the project's source of truth, referenced from CLAUDE.md — `eFCHwtufjJc`
- Postgres-only stack (pgvector, tsvector GIN index, PostGIS) — fewer services for small apps — `MZfhhl6ej-k`

### Where creators agree or clash with the conference talks

- **Agree: structure-aware chunking.** The creator demo splits on scene headings, which matches the conference rule to chunk by structure. The creator default is still a fixed size, while the conference view is that no single size wins (`pvCabUerwss`).
- **Agree: clean ingestion first.** Creators say messy text is the hard part (`96P65wL2zmw`) and convert to Markdown before indexing (`9ZaiZzp4XcY`, `BpsRH-1TZk4`). This matches the "parsing sets the ceiling" point above.
- **Agree: corpus size decides the method.** Grep works for small, clean, structured data (`gZr5VmsXmXQ`). Creator tests on a 1.5M-line repo show mixed speed and cost for an index (`gPeWb4_DMok`). The conference reports a small precision gain from semantic code search. Both fit "it depends on scale."
- **Clash in emphasis: graphs for code.** Two creator videos argue graphs beat chunk RAG for code call relations (`8Kv2tn22QNo`, `cyIWQHYoUg8`). The conference view limits graphs to 3+ hop or aggregation questions. The creator graph numbers (about 70x fewer tokens, 46% fewer tool calls) are self-reported and not reproduced. Read them as support for call-chain queries only.
- **Agree: agent-triggered search.** Creators expose search as MCP tools and let the agent decide when to call them (`EgXOaH-ZqfU`, `gPeWb4_DMok`). Graft's own test found MCP slightly more accurate and CLI injection faster (`cyIWQHYoUg8`). This is a trade-off, not a winner.
- **Clash in evals.** The conference view wants end-task judging and calibrated judges. The creator demo uses three hand-picked probes (`pvCabUerwss`). The Qdrant video is closer to the conference view: exact ground truth on your own slice (`6Uj6GXIpX9s`).
- **Agree: small benchmarks mislead.** The Qdrant video says 1M-vector tests hide memory and tail-latency problems at scale. This matches the conference warning about untuned or narrow baselines.

### Watch first (creator videos)

- `CnfuoBYmkJE` — the curated-versus-RAG routing argument; clearest framing, but one illustrative demo with no numbers.
- `pvCabUerwss` — chunking, persistence and the grounding-probe loop; easy to copy in an afternoon.
- `gPeWb4_DMok` — indexed-versus-grep test on a large repo with cost; partly a vendor pitch.
- `8Kv2tn22QNo` — provenance labels, egress tiers and the lint loop; the graph benchmark is self-reported.
- `6Uj6GXIpX9s` — how to test a vector store on your own slice with brute-force truth.
- `gZr5VmsXmXQ` — bash retrieval versus RAG, and the routing rule for choosing between them.

## Watch first

- `O84lhGc1OOI` — best single source on hybrid search, tuned baselines and manager/searcher subagents, with real BrowseComp-Plus numbers.
- `1IdzkRVmWAA` — why agents write bad queries and a concrete four-tool bounded harness.
- `r9OwPx_HoV0` — chunking as a per-query choice, oracle experiment, multiscale plus RRF.
- `X4w2Pkz5tDY` — corpus-scale rule of thumb and a primitive-tool harness for documents.
- `gonAewBZxfU` — the most complete production RAG case: chunking, tables, hybrid, tool ladder, evals.
- `T3SS931wU0I` — a small honest eval of grep vs vectors and how to build such a dataset from bug-fix PRs.
- `spxoDAfh5ig` — schema discovery, validation and retry loop for structured retrieval.
- `fZH97QHHYjY` — the case for BM25 and a filesystem workspace for results.

## Implications for our projects

**AgentOS MemoryMesh (BM25 + pgvector, GraphRAG, RAGAS).**
- Keep BM25 + pgvector and fuse with RRF. Do not add raw scores (`ksjwtQop4os`, `r9OwPx_HoV0`). Tune BM25 parameters on our own document lengths before judging vector gains (`fZH97QHHYjY`).
- Expose retrieval as a few tools (overview, deep, filter, exact) rather than one endpoint (`1IdzkRVmWAA`, `UM6sFg_jdlE`). Add a cap on rounds and dedupe.
- Try multiscale indexing as a benchmark in the next phase. Extra index storage is the cost (`r9OwPx_HoV0`).
- Use graph retrieval only for multi-hop and aggregation questions, seeded by vector hits (`LJ2a9nX3vlo`, `Q0VkgCyNVUg`). Add an inspect-the-subgraph debug view.
- Score end-task answers, not only retrieval ranks, and calibrate any LLM judge against a hand-labelled set (`fZH97QHHYjY`, `NdrSPm6NCdk`).
- Carry provenance and scope tags on every memory, check scope on write and read, redact before embedding (`BIhiYL4U9_M`, `5ID22ACI7IM`).
- Utility-weighted memory (rank by past usefulness) is a cheap idea for SkillForge, but the numbers are vendor-reported (`Jx4ZFEAq6bY`).

- Per-turn tool swapping cuts tool-schema tokens; the demo gives no accuracy numbers, so treat the benefit as unmeasured (`vJukHCIv7Ck`).

- Pre-computed read copies and insert-time tokens fixed a search scaling wall at Hugging Face (`lyL5QhgIOxc`). Route heavy reports to a separate replica.
- For trace search, let the database do aggregation and return only results (`vJukHCIv7Ck`). Validate generated queries in code, inject tenant scope in code, bounded retries (`spxoDAfh5ig`, `ORVh4GivEU0`).
- Napkin-math the latency and cost before benchmarking (`jQDXzEVHMSE`).

**ProsHarness.**
- Read an index first, then summaries, then raw files. Write answers back to a wiki and keep a log (`ZRM_TfEZcIo`). Fits checkpoint/resume notes.
- Force tool paths with a disallowed-tools flag, not prompt text (`T3SS931wU0I`). Pass parent span IDs to subprocess runs so traces stay linked.
- Rank skills by embedding description and loading top-K (`KtBivPzmOM8`, `vh2VGuQ3zhY`).

**Entity resolution and cheap-model pipelines.**
- Embed-then-threshold matching before creating a new node, fuzzy match first and an LLM only as tiebreaker (`3ySF0I5iE_0`, `ORVh4GivEU0`).
- Staged extraction: cheap NER first, stronger model, LLM last (`B9h9ovW5H9U`). Fits Haiku pipelines.
- Fine-tune only the stable center. Track human override rates until they flatten (`qflLT3SoVbw`).

**Cheap wins to try first.** Add RRF hybrid, an eval on end-task answers, tool-RAG for the registry, and corpus dedupe before indexing (`wzWNYDY7toc`).
