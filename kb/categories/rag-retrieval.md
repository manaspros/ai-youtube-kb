# rag-retrieval — 111 videos

*retrieval, search, embeddings, chunking, GraphRAG, agentic search*

By channel: AI Engineer 77 · Kai Explains 5 · AI LABS 8 · Better Stack 21

**Synthesized guide:** [guides/rag-retrieval.md](../guides/rag-retrieval.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Everyone Has the Same AI Models. Here's What Sets Agents Apart - Richmond Alake, Oracle](../videos/1_lX0m64-aI.md)
`1_lX0m64-aI` · AI Engineer · 2026-11-01 · q2 · intro · talk · also: memory, agent-architecture, security-guardrails

Oracle's Richmond Alake argues agents need an "intelligence plane" (knowledge, memory, access governance, continual learning) beyond the control plane, illustrated with Oracle product demos.

- Techniques: Memory routing with a small fine-tuned decision model; Capture memory traces as fine-tuning data; Ontology and semantic layer in front of retrieval; Propagate user identity into data access; Private inference container for on-prem embeddings, LLM and rerankers
- Tools: Oracle AI Database, Oracle agent memory Python package (generates context cards), Oracle Deep Data Security, Oracle Private AI Services Container, Oracle Cloud (hosted Grok and OpenAI models), Private Agent Factory (no-code agent builder on Oracle AI Database), Memories (open-source agent memory tool built by the speaker), Qwen (fine-tuned as memory-routing decision model)

## [Why We Rebuilt Microsoft Office From Scratch for AI Agents - Yijia Liang, Compound AI](../videos/v0UkV5qS9E4.md)
`v0UkV5qS9E4` · AI Engineer · 2026-11-01 · q3 · practitioner · talk · also: multi-agent, evals, enterprise-adoption

Compound's Yijia Liang explains why they rebuilt Excel, PowerPoint and Word as headless Rust engines for finance agents, using the real Office apps as an oracle in agent loops, plus email-based multiplayer agents and swarm-based file processing.

- Techniques: Objective-function loop against the incumbent app as oracle; Own the write-render-check-fix loop with a headless engine; Grep-first agent swarm over a large file corpus with citations; Email as the multiplayer interface for an agent
- Tools: Compound (getCompound.ai), IronCalc, Microsoft Excel, Microsoft PowerPoint, Microsoft Word, OpenPyXL (transcribed as 'OpenPAxcel' / 'OpenPi Excel'), Outlook, SharePoint, Box, Microsoft Teams, Claude, ChatGPT

## [Can Your AI Analyst Keep a Secret? - Aaron Linsky, Bridgewater & Nikhil Benesch, turbopuffer](../videos/u_jvuCjuvEk.md)
`u_jvuCjuvEk` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · also: security-guardrails, infra-cost-scaling

Bridgewater and turbopuffer explain how to run vector search over 100M documents with per-document permissions, using cluster-pruned "native filtering" to keep recall and latency acceptable.

- Techniques: Cluster-pruned native filtering for ACL-restricted vector search; Avoid fixed top-K then post-filter for access control; Express permissions as filter predicates on documents; Napkin math before choosing an index; Object-storage-first tiering for large, bursty corpora
- Tools: turbopuffer, Amazon S3, Google Cloud Storage, Azure Blob Storage, Bridgewater DeLorean (internal bitemporal macro time-series database, mentioned), Bridgewater Vault (internal unstructured document store, about 100M docs)

## [How Bridgewater Turned 100 Million Documents Into an Edge - Sam Green & Aaron Linsky, Bridgewater](../videos/CLve4Nx_RwI.md)
`CLve4Nx_RwI` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: enterprise-adoption, product-ux, data-engineering

Bridgewater's Applied AI team describes the Vault, a governed corpus of 100M+ unstructured documents, and the lessons from making it useful to both human investors and agents: separate design for each reader, benchmark-driven search, and feeding agent-human synthesis back into the corpus.

- Techniques: Hand-labelled retrieval benchmark before tuning; Cluster-aware native filtering in the vector store; Infer a time window from the question and scope retrieval to it; Separate human and agent retrieval design; Migrate existing user habits into the new tool first; Write synthesis back into the corpus
- Tools: Turbopuffer (vector database, native filtering), Bridgewater Vault (internal unstructured data platform), Aya (internal artificial investment associate), Pocket Analyst (internal AI analyst), Researcher (internal, next-generation analyst), Forecaster (internal, custom model plus foundation models), Slack, IDE integration, CLI for agents, phone app, enterprise chat client (unnamed)

## [Do Not Let Models Invent Numbers - Vinoo Ganesh, Kepler](../videos/dZgA6btnb_s.md)
`dZgA6btnb_s` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: data-engineering, security-guardrails

Kepler's CEO explains how its finance research platform stops LLMs from inventing numbers: models cite pre-registered SEC facts, deterministic code does the math, and any unverifiable number is stripped.

- Techniques: Cite-don't-write with post-filter; Typed fact registry; Search wide, then re-rank in stages; Per-hit document authorisation; Keep conflicting sources and de-conflict; Measure recall and idempotency as guarantees
- Tools: Kepler (finance research platform), Turbopuffer (vector and BM25 search, namespaces), Zero Entropy embeddings (as stated; 1280 dimensions), Postgres (per-document authorisation), Cross-encoder re-ranker (model not named), XBRL (structured filings data, cited as ~10% incorrect), SEC filings: 10-K, 10-Q, 8-K, S-1, investor presentations, earnings call transcripts, Claude and ChatGPT (used as baseline in evals), Gemini 4 (mentioned, not evaluated)

## [How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada](../videos/c_SPW__jF9w.md)
`c_SPW__jF9w` · AI Engineer · 2026-10-22 · q4 · practitioner · talk · also: evals, enterprise-adoption

Air Canada's data science team explains how they built evaluation sets with no public benchmark: generate test cases from known answers, grade them with code, and avoid LLM-as-judge.

- Techniques: Answer-first synthetic eval for retrieval QA; Plant-the-defect known-answer tests; Remove-a-clause mutation test; Template fill-in combinatorics; Invariance tests; Trajectory checks for tool-using agents; Prefer code graders over LLM-as-judge; Strip complexity before adding techniques
- Tools: BM25, LLM-as-judge, Text-to-SQL (mentioned as an example pattern)

## [Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa](../videos/L4dUFimVDKU.md)
`L4dUFimVDKU` · AI Engineer · 2026-10-19 · q2 · practitioner · workshop · also: evals, data-engineering

Exa's forward-deployed engineer demos ExaSnapshot, point-in-time web search for backtesting agents without future leakage, plus a hands-on acquisition-prediction exercise. Mostly a vendor pitch, but the leakage and holdout-set points hold regardless of vendor.

- Techniques: Point-in-time (as-of date) retrieval for backtests; Content versioning for trusted historical features; Feature-by-feature backtest with a holdout set; Scoring rubric for event prediction; Pin the repo state for coding-model evals
- Tools: Exa, ExaSnapshot, Cursor, Gamma, ChatGPT, Claude

## [Version-Controlled Search: The Web as It Was — Ryan Ahern, Exa](../videos/vS2IA9pq0Q4.md)
`vS2IA9pq0Q4` · AI Engineer · 2026-10-19 · q2 · intro · talk · also: evals, token-cost-efficiency

Exa vendor talk on version-controlled search (Exa Snapshot): query the web as it stood at a past date, and use that to backtest agent-driven financial features without look-ahead leakage.

- Techniques: As-of (point-in-time) search for backtesting; Holdout validation for agentic features; Separate search-tool eval from model eval; Per-task cost measurement for retrieval
- Tools: Exa, Exa Snapshot, Exa Agent Ultra, Cursor, Gamma, ChatGPT, Claude

## [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](../videos/KtBivPzmOM8.md)
`KtBivPzmOM8` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · also: agent-architecture, memory, context-engineering

Oracle workshop on memory-aware agent harnesses for AML: treat the harness (loop, memory tiers, skill retrieval, context budget) as the thing to engineer, not the frontier model.

- Techniques: Two-tier memory with promote-to-long-term; Vector-indexed skill and tool box with top-k retrieval; Hybrid keyword plus embedding retrieval with RRF; Compaction or summarization of old context; Skill distillation from past runs; Pre-vetted query tools instead of free-form SQL; Bounded agent loop for unattended runs; Stable request prefix for caching
- Tools: Oracle Database, OCI (Oracle Cloud), GitHub Codespaces, OpenAI chat completions API, vector store, MCP, RRF, Claude Code, Codex, Pi harness, Hermes agent, OpenClaw

## [Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket](../videos/gonAewBZxfU.md)
`gonAewBZxfU` · AI Engineer · 2026-10-15 · q4 · practitioner · talk · also: evals, agent-architecture, data-engineering

Two In The Pocket engineers describe a RAG assistant over a Belgian payment scheme's rulebooks: section-aware chunking, table flattening, hybrid retrieval, agentic narrow-to-wide tools, and noisy LLM-judge evals.

- Techniques: Section-path chunking without overlap; Table flattening for merged cells; Hybrid dense plus BM25 with RRF; Narrow-to-wide agent tool ladder; Tool-level recovery guardrails; Stream prose, render structured parts last; Lightweight feedback logging; Promptfoo end-to-end evals plus retrieval-only eval
- Tools: Qdrant, BM25, Reciprocal Rank Fusion, Promptfoo, Pydantic, LLM-as-judge

## [What Really Happens Inside ChatGPT (AI Explained)](../videos/ZTmZOdB5o0U.md)
`ZTmZOdB5o0U` · Better Stack · 2026-10-12 · q3 · intro · other · also: models-research, mcp-and-tools, training-finetuning-rl

An eight-minute beginner tour of LLM internals (tokens, weights, transformers, training, LoRA, quantization, RAG, tool calling, MCP, agent loops) with no product pitch, pitched at newcomers rather than builders.

- Techniques: Stateless chat memory via replay; Tool-calling loop; Agent loop with task handoff; Retrieval-augmented generation (RAG); LoRA fine-tuning; Weight quantization for local models; Reinforcement learning with a programmatic checker
- Tools: ChatGPT, GitHub, Slack, Better Stack, Model Context Protocol (MCP)

## [Teaching Agents to Search with NVIDIA Data Designer — Dhruv Nathawani, NVIDIA](../videos/qFaKvbVc5cE.md)
`qFaKvbVc5cE` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: training-finetuning-rl, data-engineering, evals

NVIDIA workshop on NVIDIA Data Designer: build column-by-column synthetic data pipelines, seed them with Wikidata random walks and Tavily search traces, and use them to teach a model web search (BrowseComp 0 to about 30%).

- Techniques: Column-by-column DAG for synthetic data; Seeded random walks over a knowledge graph; Teacher trajectories with a tool, then SFT on the trajectories; Overproduce and filter funnel; Layered verification of synthetic labels; Skip the golden answer and use a reward function (RL path); Persona seeds from census marginals
- Tools: NVIDIA Data Designer, Nemo Curator, Nemo Gym, Nemo Anonymizer, Nemo Safe Synthesizer, Tavily, MCP, vLLM, gpt-oss-120b, Wikidata, Hugging Face

## [Building AI Agents with Real-Time Web Data — Yohan Raju, Bright Data](../videos/IK8cC4FScps.md)
`IK8cC4FScps` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: mcp-and-tools, data-engineering

Bright Data's Yohan Raju argues that live web data (scrapers, anti-bot handling, and an MCP endpoint with 60+ tools) lets AI agents answer questions that pre-indexed RAG cannot, then demos an Amazon-plus-Reddit buy/no-buy agent.

- Techniques: Live-vs-indexed query routing; Response caching for time-stable answers; One MCP endpoint with many scraping tools; Search-then-scrape chaining; Decision agent over multi-source API data; Record validation and medallion staging
- Tools: Bright Data MCP server, Bright Data Web Unlocker, Bright Data Browser API, Claude Code, Claude, GPT, Gemini API, LangChain, Google Colab-style notebook, Glassdoor, Amazon, Reddit

## [Vector Isn't Enough: Hybrid Search & Retrieval — Jeff Vestal & James Williams, Elastic](../videos/ksjwtQop4os.md)
`ksjwtQop4os` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: evals, mcp-and-tools

Hands-on Elastic workshop on why hybrid search (BM25 plus dense vectors, fused with RRF or linear weights, then reranked) beats vector-only retrieval for RAG and agent tool use.

- Techniques: Reciprocal Rank Fusion (RRF) hybrid search; Linear combination with min-max normalisation; Filter before ranking; Retrieve then rerank in one request; Search templates routed by an LLM (poor man's auto-tuning); Semantic_text with default sentence chunking; LLM answer with citations from retrieved sources; Index-description tool for agents; Point-in-time pagination
- Tools: Elasticsearch (serverless), Kibana / Discover, Elastic Inference Service, Jina embedding and reranking models (Elastic acquisition), Agent Builder (Elastic agent platform), ES|QL, Jupyter notebooks, Elastic workflows and MCP endpoint

## [Beyond RAG: A Relational Context Engine That Cuts Token Burn — Unblocked](../videos/ORVh4GivEU0.md)
`ORVh4GivEU0` · AI Engineer · 2026-10-11 · q3 · practitioner · demo · also: token-cost-efficiency, context-engineering, data-engineering

Unblocked (Peter) argues RAG misses structured questions, then builds a schema-aware query engine over a document store with validation and self-correction; the talk is a demo-heavy speed run.

- Techniques: Dynamic schema discovery by document sampling; Fuzzy identity resolution with LLM tiebreak; Validate-then-inject for generated queries; Bounded self-correction loop; Per-task context bundle with an A/B harness
- Tools: Claude, MongoDB, GitHub, Slack, Notion

## [Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked](../videos/spxoDAfh5ig.md)
`spxoDAfh5ig` · AI Engineer · 2026-10-11 · q4 · practitioner · workshop · also: data-engineering, security-guardrails, context-engineering

Peter Werry (Unblocked) builds a schema-aware natural-language-to-database-query engine from scratch, covering schema sampling, identity mapping, allow-list validation and an error-retry loop, as the structured half of retrieval beyond RAG.

- Techniques: Dynamic schema discovery by document sampling; Deny-by-default query validation; Error-feedback retry loop; Forced tool call for entity extraction, with a fallback; Fuzzy identity mapping; Date-aware prompting for temporal queries; Two-stage schema selection; Hybrid entry point, then structured queries; Webhook-driven ingest and re-embed
- Tools: MongoDB, Postgres (mentioned as a comparison with table definitions), GitHub, Linear, Jira, Slack, MCP, Levenshtein distance

## [RAG Needs a Map: Using GraphRAG to Retrieve Connected Context — Nyah Macklin, Neo4j](../videos/LJ2a9nX3vlo.md)
`LJ2a9nX3vlo` · AI Engineer · 2026-10-11 · q2 · intro · workshop · also: data-engineering, context-engineering

Neo4j workshop on GraphRAG: when vector RAG falls short (3+ hops, cross-document aggregation), how an LLM can build a knowledge graph, and how to pair vector search with Cypher in a Neo4j Aura agent.

- Techniques: Hybrid vector-plus-Cypher retrieval tool; Text-to-Cypher tool beside the search tool; Schema-pinned LLM entity extraction; Chunk, embed, extract, load pipeline; Direct Cypher audit after each rebuild; Grounding instruction to restrict the agent to graph content
- Tools: Neo4j, Neo4j Aura (free instance), Aura Agents, GraphAcademy, GraphRAG for Python (neo4j-graphrag), OpenAI (LLM and text-embedding-3-small), Cypher, GitHub Codespaces, VS Code

## [Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge](../videos/cSz7aL2nl2U.md)
`cSz7aL2nl2U` · AI Engineer · 2026-10-10 · q2 · practitioner · talk · also: context-engineering, memory, mcp-and-tools

Gil Feig (Merge) argues every company needs a "context graph" (a company brain of synced data, live lookups, memory, skills) and lays out how to route, cache, and trace it. Conceptual talk with a closing product plug.

- Techniques: Split retrieval: live MCP vs. synced vector cache; Router plus summarizer; Skills and memory first; Freshness SLA check on cache; Derived-context write-back; Bounded live pulls; Provenance metadata on every record
- Tools: MCP (Model Context Protocol), Zendesk, Jira, NetSuite, Stripe, Qualtrics, vector database (unnamed), Merge Unified, Merge Agent Handler, Merge Gateway

## [From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle](../videos/BIhiYL4U9_M.md)
`BIhiYL4U9_M` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: memory, context-engineering, security-guardrails

Oracle's Anders Swanson argues agent memory should be a governed, typed database layer with redaction, hybrid retrieval, scoped access, and feedback loops, not files or bigger context windows.

- Techniques: Typed memory schema with per-type lookup; Write pipeline: redact, enrich, scope, embed, episode-link; Weighted hybrid retrieval with fused scores and provenance; Governance on write and on read; Feedback signals that rank and promote or demote memories; Expose memory as a runtime function
- Tools: Oracle AI Database, Oracle Python SDK for agent memory (speaker's; referenced, not shown), Claude Code, Codex, MCP, hooks, skills

## [Grep or Embeddings? Agentic Search Over Company Documents — George He, LlamaIndex](../videos/X4w2Pkz5tDY.md)
`X4w2Pkz5tDY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · also: context-engineering, data-engineering

George He (LlamaIndex) argues that agent document search should be a harness of primitives (list, grep, read by offset, semantic search, page screenshots) chosen by corpus scale, not a single RAG pipeline.

- Techniques: Agent retrieval harness with a small primitive set; Hybrid retrieval with weighted fusion and LLM rerank; Parse once, persist, and store page screenshots; Metadata tagging at ingest; Chunked reads with grep then offset and length; Evaluate parsers on table and layout fidelity
- Tools: LlamaIndex, LlamaParse, LightParse, Turbopuffer, Claude Code, grep, BM25, Textract, Tesseract, MCP, Google Drive, SharePoint

## [Evals in AI: A Deep Dive — Tejas Kumar, IBM](../videos/NdrSPm6NCdk.md)
`NdrSPm6NCdk` · AI Engineer · 2026-10-06 · q4 · practitioner · workshop · also: evals, testing-verification

Tejas Kumar (IBM) walks through evals as fuzzy unit tests for non-deterministic agents, then builds an LLM judge live, calibrates it against hand-labelled data, and gates CI on human agreement.

- Techniques: Judge calibration loop against a golden set; Pointwise pass/fail judging; Bias probes for judges; CI agreement gate; Pin the judge model version; Living eval dataset from production traffic; Cheapest-first eval ladder; Adversarial and synthetic eval generation; Avoid fuzzy string matching on LLM output
- Tools: Vitest, Cursor, GPT-3.5 Turbo, GPT-4o-mini, Docling, OpenSearch, OpenRAG (IBM), LM Arena

## [From Raw Documents to AI-Ready Data — Leo Platzer & Jeff Koss](../videos/wzWNYDY7toc.md)
`wzWNYDY7toc` · AI Engineer · 2026-10-06 · q2 · intro · demo · also: data-engineering, governance-compliance

Vendor talk (DZ Labs, now Colibra) on turning millions of messy SharePoint documents into AI-ready data by tagging, deduplicating, freshness-filtering and scoping them before RAG.

- Techniques: Conditional tag tree with AI suggestions and human review; Dedupe and freshness pruning before indexing; Hybrid pattern plus LLM sensitive-data scan; Folder-level context index file; Scheduled data slices
- Tools: SharePoint, DZ Labs (DZ data curation platform, DZ SDK), Colibra, Claude Code, Codex, vector database, knowledge graph

## [Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust](../videos/T3SS931wU0I.md)
`T3SS931wU0I` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: evals, coding-agents

Braintrust dev-rel walks through a small eval comparing agentic search (grep/find/cat in Claude Code) with vector search for finding bugs in the TypeScript Go repo: equal accuracy, but vector cost 4x more.

- Techniques: Eval composition: dataset, task, scorer, experiment; Production-log sampling into a dataset; Mining bug-fix PRs as coding-agent eval tasks; Binary scoring from the repo's own test suite; Forcing a retrieval strategy in a coding agent; Propagating parent span IDs to subprocess agents
- Tools: Braintrust (evals, tracing, UI, CLI, MCP server), Claude Code (agent harness, disallowed-tools flag), grep, find, ls, cat, bash (agentic search tools), Vector database (unnamed in the talk), Microsoft TypeScript Go repo and its test suite (dataset and scorer), Cursor semantic search post (cited as motivation)

## [AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](../videos/Bdrs3uAX0_M.md)
`Bdrs3uAX0_M` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · also: coding-agents, software-factory, context-engineering

Sourcegraph CEO Dan Adler argues that large, decades-old codebases are decaying under the flood of AI-written code, and that agents need code-graph and search infrastructure to see and change them across thousands of repos.

- Techniques: Deterministic scripts for mechanical sweep changes; Hybrid agent and script batch change loop; Code-graph plus search as agent context; Coverage audit for sweeping changes
- Tools: Sourcegraph, agentic batch changes, Claude Code, Codex, Cursor

## [Keyword Search Is Dying. Is Your Catalog Ready for AI Agents? — PayPal](../videos/YXb2Wx1r_Pk.md)
`YXb2Wx1r_Pk` · AI Engineer · 2026-10-05 · q2 · intro · talk · also: data-engineering, product-ux

PayPal's agentic-commerce director argues merchant catalogs were built for human search, not agents, and shows that enrichment helps semantic recommendations while over-enrichment and boilerplate hurt.

- Techniques: Catalog enrichment for semantic retrieval; Head-to-head baseline test of enriched vs unenriched records; Hybrid keyword plus semantic retrieval; Strip boilerplate from agent-facing text

## [Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa](../videos/cKhpeEBnT1o.md)
`cKhpeEBnT1o` · AI Engineer · 2026-10-04 · q2 · practitioner · talk · also: mcp-and-tools, coding-agents

Exa's forward-deployed engineer explains why coding agents miss recent changes past their model cutoff, and how query-targeted web search snippets, plus explicit search rules, close that gap. Partly a product pitch.

- Techniques: Two-part search instructions for agents; Query-targeted highlight extraction; Full retrieval trace logging; Natural-language schema for structured output
- Tools: Exa search API, Exa Agent, MCP server, Claude Code, CodeRabbit, Cursor

## [Stop Renting Your AI's Memory — Dylan Couzon, Qdrant](../videos/apyrzaWj0Z4.md)
`apyrzaWj0Z4` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: memory, local-ai

Dylan Couzon (Qdrant) argues agent memory should be owned locally: models are rented, but a private, retrieval-based memory store compounds and stays portable. Includes a live offline drone-vision memory demo.

- Techniques: Write-retrieve-forget memory loop; Embedded in-process vector store with per-app folder; Quantized vectors for small footprint; Pin the embedding model for portability; Detector labels then embeddings for perception memory; Opt-in sync of local memory to a shared store
- Tools: Qdrant, YOLO

## [Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava](../videos/qflLT3SoVbw.md)
`qflLT3SoVbw` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: context-engineering, training-finetuning-rl, memory

Anant Srivastava argues enterprise teams should decide deliberately whether knowledge lives in the prompt, in retrieval/memory, or in fine-tuned weights, using rate of change, scope, and behavior-vs-facts as the test.

- Techniques: Knowledge placement diagnostic; Retrieval-first debugging; Fine-tune the stable center, keep humans on the edge; Code-aware chunking with denormalized metadata; Promote-and-prune memory loop; Small fine-tuned model for cost

## [Github Top Trending Tool Just Fixed The AI Agent’s Biggest Problem](../videos/cyIWQHYoUg8.md)
`cyIWQHYoUg8` · AI LABS · 2026-10-02 · q3 · practitioner · review · also: token-cost-efficiency, context-engineering, coding-agents

Walkthrough of Graft, a free open-source CLI that builds a code knowledge graph and hooks into Claude Code to cut search turns, tokens and cost; the benchmark is self-reported by its makers.

- Techniques: Code knowledge graph for impact-aware retrieval; Pre-prompt context injection via a UserPromptSubmit hook; Hook trio for a Claude Code workflow; Pick CLI injection or MCP on-demand lookup; Long autonomous run setup for a token-hungry model; Install and initialize Graft in a Claude Code project
- Tools: Graft, Claude Code, Codex, MCP, Opus, GPT 5.6, GPT Astra (as transcribed, unverified), Fable 5.1 (as transcribed), Hydra (sponsor; API for AI generation)

## [Most Vector DB Benchmarks Are Wrong. Here's The Fix. (Qdrant FineWeb 10b)](../videos/6Uj6GXIpX9s.md)
`6Uj6GXIpX9s` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: evals

Better Stack walks through Qdrant's open 10B-vector FineWeb benchmark dataset, which ships exact nearest-neighbor ground truth, and reruns a 1M slice against four vector engines. Lesson: test on your own data with brute-force truth.

- Techniques: Exact brute-force ground truth on your own slice; Store deep ground truth and truncate for smaller k; Recall-vs-latency sweep per engine; Sequential, isolated engine runs over the same loaded data; Benchmark filtered and sparse/hybrid queries separately
- Tools: Qdrant, Milvus, Elasticsearch, PGVector (pgvector), FineWeb (Hugging Face dataset), GTE Multilingual Base (embedding model), MS MARCO (query set), Docker, Qdrant open-source benchmark toolchain (Apache 2.0; named 'Supernova' in the captions, name unverified)

## [Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash](../videos/ACPEpji5NV4.md)
`ACPEpji5NV4` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: data-engineering, memory, evals

DoorDash's search and personalization lead on using LLMs offline to create graded relevance labels, semantic IDs, and memory, then serving those through small, fast models.

- Techniques: Offline LLM labeling with a distilled labeler; Label-audit by disagreement; Two-stage contrastive retrieval with hard-negative curriculum; Auxiliary ordinal relevance tower with value-function blend; Hierarchical learned semantic IDs as sparse features; Multi-form consumer memory blocks; Batch generation of personalized content with the existing ranking stack
- Tools: GPT-4o mini (named as an example lightweight labeler)

## [Building the Document Context Layer for AI Agents — Jerry Liu, LlamaIndex](../videos/RQi7x-navxU.md)
`RQi7x-navxU` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: context-engineering, data-engineering

Jerry Liu (LlamaIndex) argues agents need a document context layer: fast local parsing by default, VLM escalation for hard pages, and cost-aware routing between specialized and frontier models.

- Techniques: Fast-pass then escalate parsing; Hybrid pipeline plus VLM parsing with routing; Regime-based pipeline selection; Structured extraction with provenance and confidence gating; Multi-tool agent retrieval over documents; Accuracy-cost-latency Pareto benchmarking
- Tools: LlamaParse, LightParse, ParseBench, Claude Code, Claude Cowork, Codex, OpenClaw, MCP, BM25, grep, PyPDF, PyMuPDF

## [From Ingestion to Agents: How AI Teams Build on Document Intelligence — Adit Abraham, Reducto](../videos/0I07YAuF8xA.md)
`0I07YAuF8xA` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: data-engineering, agent-architecture, evals

Reducto's CEO on why document ingestion decides agent quality: decompose parsing into specialised tools, verify rather than regenerate, store table forms split by job, and eval every pipeline stage.

- Techniques: Decomposed parsing stack; Targeted verification instead of regeneration; Dual table representation; Classify and split before extraction; Agent harness for chart reconstruction; Parent-subagent validation criteria; Per-stage evals
- Tools: Reducto, Gemini, OpenAI models, Anthropic models, Cursor (as analogy for speculative edits), code interpreter

## [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](../videos/O84lhGc1OOI.md)
`O84lhGc1OOI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: multi-agent, evals, context-engineering

Benjamin Clavié (Mixedbread) argues agents should be designed as knowledge workers, not coding agents, and uses BrowseComp-Plus and MatQA results to show that tooling and search orchestration drive accuracy.

- Techniques: Manager-plus-searcher subagents for open-ended retrieval; Optimize the lexical baseline before comparing; Hybrid search harness; Multimodal PDF search instead of OCR text; Teach the agent its retrieval primitives
- Tools: BM25, Gemini, Claude Code, Codex, Mixedbread search tool

## [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../videos/qdAkxLoYNI8.md)
`qdAkxLoYNI8` · AI Engineer · 2026-09-18 · q2 · intro · review · also: context-engineering, pr-code-review, mcp-and-tools

Unblocked vendor talk arguing coding agents need an organizational context engine over code, PRs, Slack and docs, with cited sources; one live comparison, mostly product pitch.

- Techniques: Cited-source answers for agents; With/without context comparison; Expertise-weighted review comments; Query historical PR data with an open-source engine; Engineering social graph from review edges
- Tools: Unblocked, Claude Code, Claude 4.8, Slack, Notion, GitHub, MCP, Document Query Engine, context engine simulator

## [Agents' next frontier: agent-to-agent and network effects — Jean-Denis Greze, Town](../videos/REascnFlq_8.md)
`REascnFlq_8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: multi-agent, security-guardrails, context-engineering

Jean-Denis Greze (Town CTO) reframes agent-to-agent work as a context-window search problem and compares five ways to get cross-silo data into an LLM call safely.

- Techniques: Benchmark against an ideal single-context agent; Privacy-preserving derived tool; Per-silo sweeper agent; Write-step-only approval for cross-silo queries; Tiered autonomy by sensitivity
- Tools: Gmail, Slack, Airtable, LinkedIn

## [The Search Engine for the Agentic Web — Will Bryk, Exa](../videos/59AA5kIoqjA.md)
`59AA5kIoqjA` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: infra-cost-scaling, product-ux

Exa's CEO pitches Exa as a search engine built for AI agents rather than humans, covering its history, API features (fast endpoint, token extraction, structured output) and a data marketplace.

- Techniques: Hybrid embedding plus keyword retrieval; Token-budget extraction before the LLM; Schema-based structured search output; Per-tenant search configuration; Latency tiers by consumer type
- Tools: Exa search API, Exa Connect, Cursor, HubSpot, Similarweb, GPT-3, ChatGPT

## [Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe](../videos/jebp4V0vh30.md)
`jebp4V0vh30` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, inference-serving, product-ux

Adobe's Carlos Sanchez demos "agentic sites" that personalize page blocks in real time from browsing intent, grounded on the existing site, with provider choice driven by latency and accuracy evals.

- Techniques: Multi-provider eval matrix for accuracy and latency; Grounded block-level generation; Signal bucketing into personas or intents; Pre-generate and prefetch; Fast inference provider for the hot path
- Tools: Adobe Experience Manager, Edge Delivery Services, Cerebras, Gemma 4, Promptfoo, AWS Bedrock, Cloudflare, Google Cloud

## [Pinecone 2.0 — Edo Liberty, Pinecone](../videos/IN-rb-9WmiY.md)
`IN-rb-9WmiY` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: memory, context-engineering

Pinecone's Edo Liberty argues agents need a persistent, domain-owned company knowledge layer (Nexus) that goes beyond RAG, with query-time code generation and budgeted queries. Mostly a product pitch with vendor-reported numbers.

- Techniques: Manifest-declared knowledge base; Curate-on-ingest; Budgeted agent queries; Query-time code generation over a knowledge layer; Compact interface spec in place of tool sprawl
- Tools: Pinecone Nexus, vector database, SQL tables, graph database, markdown notes

## [Connect AI to Billions of Legal Documents — Simon Eskildsen, turbopuffer & Jacob Lauritzen, Legora](../videos/V-isu4eTHgw.md)
`V-isu4eTHgw` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: infra-cost-scaling, security-guardrails, enterprise-adoption

Legora (legal AI) walks through moving project and legal-research search from one Elasticsearch, to Postgres/pgvector, to turbopuffer, one namespace per project on object storage, and why that fits regulated multi-tenant workloads.

- Techniques: Namespace-per-tenant isolation with per-namespace keys and buckets; Partition by access temperature, not by hash; Object-storage-native write path; Round-trip budgeting over object storage; Memory-only cache for encrypted multi-tenant data; Clustered centroid tree for vector search; Two-round-trip inverted index for full text; Fan-out with hierarchy and validity filters for legal research
- Tools: turbopuffer, Elasticsearch, PostgreSQL, pgvector (DiskANN index, transcribed as 'disk NN'), Postgres tsvector, BM25, Amazon S3 (object storage), Google Cloud Storage, Azure Blob Storage, NVMe SSD cache

## [The Half Life of Agent Infrastructure — Ben Kus, Box](../videos/sM1iYgz93HI.md)
`sM1iYgz93HI` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: agent-architecture, evals, enterprise-adoption

Box CTO Ben Kus argues AI agent infrastructure has a half-life of months, not years, so teams should build abstractions, gate changes on eval sets, and get good at changing.

- Techniques: Abstraction layer over agent internals; Eval-gated switching; Scheduled stack review; Adaptive model selection; Hybrid lexical plus semantic retrieval with rank fusion; Agentic search
- Tools: Claude, Opus, OpenAI and Anthropic frontier models, open-weight models, BM25, embeddings and approximate nearest neighbor search, MySQL

## [Where RL Will Take Search — Maximilian-David Rumpf, SID.ai](../videos/iJVxxxHM_Oc.md)
`iJVxxxHM_Oc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: training-finetuning-rl, multi-agent, context-engineering

Founder of SID.ai argues search should move from fixed retrieval pipelines to one RL-trained model, reporting about 20x faster and 100x cheaper than frontier-model search agents.

- Techniques: Search as a delegated RL-trained sub-agent; Verifiable retrieval reward for RL; Mixed reward with latency; Learned loop in place of a fixed pipeline; Parallel sub-agent searches
- Tools: BM25, PageRank, vector search, rerankers

## [Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs](../videos/r9OwPx_HoV0.md)
`r9OwPx_HoV0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals

AI21's Yuval Belfer argues chunking still matters: no single chunk size wins per query, so index the corpus at several sizes, retrieve whole documents, and fuse the rankings with RRF for 20-40% gains.

- Techniques: Multiscale indexing; Parent-document lifting before fusion; Reciprocal Rank Fusion (RRF); Oracle best-per-query benchmark
- Tools: RRF (Reciprocal Rank Fusion), QMSum, NarrativeQA, FinanceBench, Seinfeld trivia dataset (in-house, speaker says it is published)

## [Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](../videos/KcVkq5L-0f0.md)
`KcVkq5L-0f0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: context-engineering, mcp-and-tools

Brandon Waselnuk (Unblocked) argues AI coding agents fail on missing company context, not intelligence, and outlines context-engine design: avoid curated markdown, separate access from understanding, and use schema discovery for relational questions.

- Techniques: Derive context from systems instead of hand-curated files; Deterministic team graph from GitHub; Rules-file discovery and index; Schema-less lookup, then deterministic query; Two retrieval modes: deep research and fast unfurl; Context hydration to avoid repeated discovery searches
- Tools: MCP, GitHub, Slack, OAuth, SSO, OpenAI API, Anthropic API

## [The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev](../videos/fZH97QHHYjY.md)
`fZH97QHHYjY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, context-engineering

Jo Kristian Bergum argues BM25 is back for agentic search: LLM agents write long, precise queries that suit lexical matching, and the baseline was undertuned. Retrieval results can be exposed as a filesystem workspace for grep-style use.

- Techniques: Workspace-as-filesystem retrieval; Tuned BM25 baseline before any embedding comparison; Hybrid lexical plus grep for agent search; End-to-end task evaluation for search agents; Evidence-stuffing ablation
- Tools: BM25, grep, ripgrep, sed, BrowseComp-Plus, Hornet (vendor BM25 engine)

## [This Open-Source Tool Fixes Browser History (Hister)](../videos/NMk9XVNTygA.md)
`NMk9XVNTygA` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: dev-tools, security-guardrails

Hister is a self-hosted tool that indexes the full rendered text of every page you read in Chrome or Firefox, so you can search your browsing by content; useful, but pre-1.0 with real security gaps.

- Techniques: Local recall index for your own reading; Scoped full-text queries; Backfilling from existing browser history; Hardening before exposure; Agent access to a personal reading index
- Tools: Hister, Chrome extension for Hister, Firefox extension for Hister, Docker (multi-arch image), Nix flake (Darwin module), MCP, Karakeep (transcribed as 'Para Keep', 28k stars), ArchiveBox, Wallabag, Readwise Reader, Gatekeeper (macOS)

## [I replaced my entire tech stack with Postgres](../videos/MZfhhl6ej-k.md)
`MZfhhl6ej-k` · Better Stack · 2026-09-02 · q3 · intro · tutorial · also: dev-tools, infra-cost-scaling

Better Stack walks through replacing separate cache, vector DB, search, geo, cron and document-store services with Postgres features, framed for small apps rather than scale.

- Techniques: Postgres as a cache using UNLOGGED tables; pgvector for embeddings and similarity search; Full-text search with a generated tsvector column and a GIN index; Geospatial radius and polygon queries with PostGIS; Scheduled SQL with pg_cron; Document storage with JSONB, a GIN index and containment queries
- Tools: PostgreSQL, pgvector, PostGIS, pg_cron, JSONB, DocumentDB, Redis, Memcached, Pinecone, Qdrant, Elasticsearch, MongoDB

## [If You Understand These 5 AI Terms, You’re Ahead of 90% of People](../videos/04rRN1oqO2A.md)
`04rRN1oqO2A` · Kai Explains · 2026-09-02 · q2 · intro · review · also: context-engineering, local-ai

Kai Explains walks through five foundational AI terms (tokens, context window, temperature, hallucination, RAG) for non-engineers, using plain analogies and personal anecdotes.

- Techniques: Verify-before-trust workflow for AI output; Restate critical context in long sessions; Adjust temperature for the task; Mental model of RAG for debugging products
- Tools: Claude, ChatGPT, Gemini

## [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j](../videos/Q0VkgCyNVUg.md)
`Q0VkgCyNVUg` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, context-engineering

Neo4j's Stephen Chin argues agent memory stored as markdown or vector lookups fails on multi-hop questions, and shows a live home-lab demo where a vector-seeded graph traversal beats a vector-only store.

- Techniques: Vector-seeded graph traversal; Graph as the agent's write target; Inspect-and-fix retrieval loop; Let the coding agent write the graph layer; Same-source backend A/B test; Keep destructive memory tools away from the agent
- Tools: Neo4j, Cypher, Cognee, OpenClaw, Goose, Hermes Agent, pgvector, LanceDB, Claude, Proxmox, pfSense, HAProxy

## [AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j](../videos/kRkcNOsRyYg.md)
`kRkcNOsRyYg` · AI Engineer · 2026-08-18 · q3 · practitioner · workshop · also: data-engineering, context-engineering

Neo4j workshop on graph shapes for agents over a lakehouse: a metadata semantic layer over the warehouse, a deterministic document-tree-plus-links graph, and Leiden community "themes" built without LLM labels.

- Techniques: Metadata-only semantic layer graph; Deterministic document-structure graph; Hierarchical URI IDs for scoped search and traversal; Semantic query expansion for full-text search; Structure-only community themes; Spec-driven Cypher generation with a vendor skill; Agent with a database CLI for ad hoc graph reasoning; Partial re-sync of a deterministic graph
- Tools: Neo4j, Neo4j CLI, Cypher, Graph Data Science (GDS), NeoCarta, Neo4j Virtual Graph, Lucene full-text index, Leiden, Louvain (mentioned), Claude Code, Claude Opus 4.8 (model used in demo), BigQuery

## [Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings](../videos/tJFjeMBKbIY.md)
`tJFjeMBKbIY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: product-ux, governance-compliance

A finance investor argues AI products should be built as auditable memos, not impressive demos. He lists six ways trust breaks and five plumbing fixes: provenance, number agreement, surfaced contradictions, fact/guess labels and human approval.

- Techniques: Click-through provenance with source trust levels; Fact vs guess labelling; Automatic cross-document number reconciliation; Surface contradictions instead of resolving them silently; Locked human approval gate with audit log; Accountability-first architecture

## [Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](../videos/mOf-PP4mVjA.md)
`mOf-PP4mVjA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, voice-multimodal, agent-architecture

TwelveLabs' James Le argues video needs a persistent memory layer (a context graph over moments, entities and relationships) rather than frame sampling, search or long context, and demos a video agent called Jockey.

- Techniques: Context graph over video moments; Ingest once, reason many times; Timestamp-grounded outputs; Intent-configurable extraction; Video worker harness; Evaluate retrieval, synthesis and budget separately
- Tools: TwelveLabs Marengo (multimodal embeddings for spatial-temporal spans), TwelveLabs Pegasus (video-aware language model used as the reasoning layer), Jockey (TwelveLabs video agent product used for the demos)

## [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](../videos/l0FLhNqBOic.md)
`l0FLhNqBOic` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: enterprise-adoption, product-ux, training-finetuning-rl

Varick Agents explain why process understanding, not model execution, is now the bottleneck, and describe the forward-deployed engineering agent they built for it.

- Techniques: Failure-path process interviews; Per-step autonomy split; Dependency graph as shared state; Post-training an open model for analysis style; RL environment with domain traversal tools; Assistant embedded in the authoring tool
- Tools: Varick OS (in-house platform), Claude, Codex, Granola, Kimi (open-source base model, named as K2.6), NetSuite, Microsoft Dynamics, SAP, Salesforce

## [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face](../videos/lyL5QhgIOxc.md)
`lyL5QhgIOxc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: infra-cost-scaling, data-engineering


- Techniques: Insert-time search tokens in a denormalized read collection; Lucene-backed autocomplete instead of regex scans; Read-replica routing by consistency class; Hidden analytics replica; Two-layer autoscaling with event-driven pod scaling
- Tools: MongoDB Atlas, Atlas Search, Apache Lucene, Kubernetes, Horizontal Pod Autoscaler, KEDA, Cast.ai, AWS S3, AWS Redshift

## [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](../videos/1UmZHb_E_SM.md)
`1UmZHb_E_SM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: infra-cost-scaling, data-engineering

Oxylabs' product manager on how public web data infrastructure feeds AI systems: how a video API, a sub-second SERP API and a 60k-rps scraper grew out of repeated client requests, latency cuts and load tests.

- Techniques: Iterate from client requests into an internal library; Narrow the response to what the AI consumer needs; Stage-by-stage latency audit; Realistic load testing with gradual ramp-up; Account for observability as load
- Tools: Oxylabs Fast Search API, headless browsers, proxy network

## [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](../videos/3ySF0I5iE_0.md)
`3ySF0I5iE_0` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: data-engineering, context-engineering

Tim Ainge (Good Collective) on when graphs help AI apps: schema-first graph extraction, entity matching, and graph-native retrieval (personalized PageRank, shortest paths, subgraph pattern matching) for cheaper, more reliable results.

- Techniques: Schema-constrained graph extraction; Ontology normalisation instructions; Embedding-based entity resolution before node creation; Personalized PageRank from a seed node; Subgraph context retrieval via path queries; Subgraph pattern matching on code graphs
- Tools: Cypher (graph query language, ASR-garbled as 'cipher'), SQL (used as the comparison baseline), HippoRAG, Pinterest PixieRank (cited as the PPR reference), Embedding models, Structured outputs from an LLM, eShop (.NET reference codebase)

## [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../videos/WP3hjUXd918.md)
`WP3hjUXd918` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: context-engineering, token-cost-efficiency, evals

Towards AI workshop on context engineering: prompt caching makes compaction costly, and on their AI tutor keeping full history beat every compaction preset on recall, cost and latency.

- Techniques: Head and tail truncation of big tool outputs; Sliding window and clearing old tool outputs; Selective retention and summarization with a threshold; Filesystem knowledge base with progressive disclosure; Hybrid retrieval with a token cap; Eval harness: presets by tasks, then grade; Planted-fact recall probe; Log every turn
- Tools: LangChain (create_agent, middleware), FastAPI, Next.js, Gemini 3.5 Flash, DeepSeek V4 Flash, Claude Code, Codex, Opik (transcribed as 'OPIC'), Hugging Face Spaces, BM25, Dense embedding retrieval

## [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../videos/jQDXzEVHMSE.md)
`jQDXzEVHMSE` · AI Engineer · 2026-08-18 · q3 · practitioner · interview · also: infra-cost-scaling, testing-verification

Gergely Orosz interviews Simon Eskildsen, founder of Turbopuffer, on his path from Shopify infrastructure to building an S3-backed search engine, napkin-math habits, CPU scarcity and startup financing. Mostly origin story, little AI content.

- Techniques: Napkin-math latency and cost estimate before benchmarking; Proxy-based fault injection in CI; Object storage as the system of record with an HTTP cache in front; Design for tail latency and round trips; Batch durable writes; Ship simplest version then probe demand
- Tools: Toxiproxy, NGINX, Amazon S3, MySQL, Rails, Postgres, pgAnalyze, Docker, Rust, GDB, Redis, NVMe SSD

## [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../videos/Ot4OPrPH4xY.md)
`Ot4OPrPH4xY` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: data-engineering, infra-cost-scaling

Bright Data's product lead argues that web data is becoming agent context, that repeated queries to paid context services get expensive, and that owning the data can beat renting it past a volume tipping point.

- Techniques: Field-by-field enrichment agent loop; Hybrid search plus direct scrapers; Basic heuristic entity merge; Break-even analysis for build vs rent; Self-healing scrapers
- Tools: Bright Data, Scraper Studio, Exa, Parallel, Tavily, New.com, Amazon AgentCore, Microsoft WebIQ, ZoomInfo / gtm.ai, SERP API, Claude native web search, Opus 4.8

## [Google Shrunk 31GB of AI Memory Down to 4GB (TurboQuant)](../videos/dfMeOTLSar8.md)
`dfMeOTLSar8` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: inference-serving, token-cost-efficiency, local-ai

Explains TurboQuant, Google's training-free vector compression (31GB to about 4GB for 10M vectors), the independent TurboVec build, and KV-cache gains. Google published math only, not a supported product.

- Techniques: Data-oblivious rotate-and-round quantization; 1-bit residual sign correction (QJL); Filtered search inside the distance kernel; Same rotation applied to the KV cache; Adoption rule of thumb
- Tools: TurboQuant (Google research, published as a paper; no official product), TurboVec (Rust library with Python bindings, by Ryan Kodry; version not stated), FAISS FastScan (Meta; named in the transcript as 'face fast scan'), Qdrant (vector database; now ships the rotation trick, per the speaker), LangChain, LlamaIndex, Lloyd-Max quantizer, QJL (1-bit residual method), Product quantization (background concept, not used)

## [Graphify + Obsidian is INSANE: Build an AI Second Brain That Never Forgets](../videos/8Kv2tn22QNo.md)
`8Kv2tn22QNo` · Kai Explains · 2026-08-02 · q3 · intro · review · also: memory, context-engineering, token-cost-efficiency

Walkthrough of Graphify, which builds a queryable code and docs graph, paired with Obsidian as a markdown second brain; the useful parts are provenance labels, tiered data egress, and the lint maintenance loop.

- Techniques: Persistent codebase graph, queried by traversal instead of re-reading files; Provenance labels on every derived link (Extracted / Inferred / Ambiguous); Tiered data egress across ingestion sources; Three-layer LLM wiki (Karpathy design); Anti-fabrication rule and weekly lint loop for an AI-maintained notes vault; Staged write access to an Obsidian vault
- Tools: Graphify, Obsidian, Claude Code, Codex, Cursor, TreeSitter, faster-whisper, Neo4j, MCP (Model Context Protocol), Claudian (Obsidian plugin for Claude Code), Smart Connections (Obsidian plugin), Khoj (self-hosted Obsidian plugin)

## [Build Your Own Fully Private Local AI Stack (Chat, RAG, Coding Agent & Automation)](../videos/np8booSU7Og.md)
`np8booSU7Og` · Kai Explains · 2026-08-02 · q3 · practitioner · tutorial · also: local-ai, coding-agents, agent-architecture

Kai Explains walkthrough of a fully local AI stack: llama.cpp behind one OpenAI-compatible endpoint, with AnythingLLM for chat and RAG, Pi as a local coding agent, and n8n for email automation.

- Techniques: Single OpenAI-compatible endpoint as the integration bus; llama-server router preset mode, with LlamaSwap as fallback; Headless AnythingLLM in Docker, configured from the UI; Local RAG with AnythingLLM defaults; Pi as a local coding agent; n8n email triage with a local model; Always-on home lab hardening
- Tools: llama.cpp, llama-server, LlamaSwap, AnythingLLM, Open WebUI, LanceDB, Pi (coding agent, npm), OpenCode, n8n, Docker, Docker Compose, Portainer

## [Google OKF + RAG: The Ultimate AI Agent Architecture](../videos/CnfuoBYmkJE.md)
`CnfuoBYmkJE` · Kai Explains · 2026-08-02 · q2 · intro · review · also: context-engineering, mcp-and-tools

Explainer arguing agents should route high-stakes facts to a curated, Git-versioned markdown knowledge bundle (Google's OKF) and open-ended queries to RAG; a thin router decides per query.

- Techniques: Curated-first hybrid routing; OKF-style concept files; Governing knowledge in Git; Single retrieval facade; Baseline RAG ingestion
- Tools: Google Cloud OKF (Open Knowledge Format, June 2026 per speaker), RAG (retrieval-augmented generation), Pinecone, Weaviate, Qdrant, Milvus, Chroma, PostgreSQL with pgvector, LangChain, LlamaIndex, MCP (Model Context Protocol), Claude

## [On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft](../videos/RGSFUqzqErE.md)
`RGSFUqzqErE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: evals, context-engineering, skills-self-improvement

Microsoft's Pablo Castro splits agent knowledge into intrinsic, extrinsic and learned, and demos Foundry knowledge bases and an Agent Optimizer that tunes agent config from traces.

- Techniques: Three-way knowledge split for agent design; Hybrid retrieval over combined methods; Layered retrieval API; Agentic retrieval with a satisfaction check; Knowledge base as MCP server; Eval generated from traces, then hill-climb the agent config
- Tools: Microsoft Foundry, Foundry IQ, Azure AI Search, Work IQ, Fabric IQ, WebIQ, Agent Optimizer, Foundry Toolkit for VS Code, GitHub Copilot, MCP

## [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](../videos/Akm1sqvWG4A.md)
`Akm1sqvWG4A` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: data-engineering, observability, security-guardrails

Abed Matini (Ogilvy) shows a local, framework-free RAG FAQ bot: Docling to Markdown, structure-aware chunking, hybrid BM25 plus vector search fused with RRF, Python guardrails, and Langfuse telemetry.

- Techniques: Markdown-first ingestion with Docling; Per-document chunking strategy selection in admin; Q&A-shaped chunks for FAQ content; Hybrid retrieval with RRF fusion in Python; Deterministic functions instead of agent loops; Pre-LLM guardrail layer with rigid tests; Per-conversation telemetry with self-hosted Langfuse; Two-model local stack in Docker
- Tools: Docling, Python, FastAPI, React, PostgreSQL, Docker, Ollama, Qwen2.5, BGE-M3, Langfuse, GitHub Codespaces

## [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](../videos/vh2VGuQ3zhY.md)
`vh2VGuQ3zhY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: mcp-and-tools, context-engineering, evals

Giving an agent every tool schema on every request breaks accuracy, latency and cost as the catalog grows; the fix is semantic routing that injects only the top-K relevant tools per query.

- Techniques: Semantic tool routing (tool RAG); Just-in-time tool and context injection; K-sweep routing evaluation; Router miss fallbacks; Description writing for retrieval; Routing observability
- Tools: Qdrant, Chroma, Pinecone, Berkeley Function Calling Leaderboard, ToolBench, Anthropic MCP on-demand tool loading write-up, Aurelio Labs semantic-router (open source), MCP0 (cited as an open-source routing project at large scale)

## [We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](../videos/dRmWYHuIJxM.md)
`dRmWYHuIJxM` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: token-cost-efficiency, context-engineering, coding-agents

Rajkumar Sakthivel (Tesco) on cutting AI coding-tool token spend by sending less context: a local code index with hybrid search, slimmed results and a relevance threshold, reporting about 94% fewer input tokens on one small benchmark.

- Techniques: Code-aware chunking; Parallel hybrid retrieval; Result slimming; Call-graph expansion; Heuristic relevance gate instead of LLM self-grading; Shared local index across tools; Per-query savings accounting
- Tools: Claude Code, Cursor, GitHub Copilot, Codex, CCE (speaker's free open-source local code index; name as spoken)

## [When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis](../videos/XovaGv4f39A.md)
`XovaGv4f39A` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: context-engineering, multi-agent, infra-cost-scaling

Luis Romero-Sevilla (Orbis) on Extended Cache Augmented Generation (ECAG): for large, frequently replaced, densely interrelated document collections, split docs across parallel KV-cached context buckets and let a supervisor model interrogate them, instead of RAG or GraphRAG.

- Techniques: Parallel context buckets with a supervisor (ECAG); Dropping topical sharding for bucketing; Caching KV state per context bucket
- Tools: GraphRAG, vector database, KV cache

## [How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](../videos/1IdzkRVmWAA.md)
`1IdzkRVmWAA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, training-finetuning-rl, evals

Mixedbread's team on why agents write keyword-soup queries that hurt retrieval, and how a bounded four-tool search harness, trained with SFT then RL, recovers much of the oracle gap.

- Techniques: Tiered search tool set for agents; Bounded parallel search rounds with dedupe; Priming with a corpus preview; Describe-the-need query framing; Oracle-gap diagnosis; SFT then on-policy RL with a mixed reward
- Tools: Mixedbread search, Codex, GPT-5, Gemini 3.5 Flash, grep, BM25

## [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](../videos/YZQsWVeN3rE.md)
`YZQsWVeN3rE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: multi-agent, evals, context-engineering

Alex Bauer (Upside.tech) on building trust in AI for go-to-market data: manage agents like people, scaffold business context first, use a librarian and a jury-and-judge pattern, and use only tier-two agent harnesses for important work.

- Techniques: Commander's intent prompting; Anchor assets and scaffolding; Citation tracing for verification; Librarian pre-query lookup; Jury and judge; Tiered tool selection
- Tools: Claude, Claude Opus, Slackbot, ChatGPT

## [Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra](../videos/EUsPvBeIx70.md)
`EUsPvBeIx70` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: data-engineering, agent-architecture, context-engineering

Phaidra engineers explain "semantic blindness": why RAG and LLM-only lookups fail on 400K+ equipment names, and how a hierarchy-based planner plus deterministic set-resolver stays accurate with flat cost at data-center scale.

- Techniques: Hierarchy summary as LLM context; LLM emits a structured search plan; deterministic resolver executes it; Pre-indexed subtrees for set operations; Two- or three-step planner/resolver pipeline in place of an agent loop; Pattern-based search for vague queries; Head-to-head eval against the old system at increasing scale; Move deterministic work out of the prompt

## [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](../videos/vJukHCIv7Ck.md)
`vJukHCIv7Ck` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: mcp-and-tools, security-guardrails, multi-agent

AWS developer advocate walks through five code-level techniques to reduce agent hallucinations: semantic tool selection, GraphRAG for aggregation, multi-agent validation, code-enforced hooks, and steering rules. Demos use dummy tools.

- Techniques: Semantic tool selection; Per-turn tool swap in agent loop; Text-to-Cypher GraphRAG for aggregation; Executor, validator, critic swarm; Before-tool-call hooks for hard rules; Steering rules for soft constraints
- Tools: Strands Agents, OpenAI API, sentence-transformers, Neo4j (Cypher, LLM graph builder), agent-control (steering SDK), Amazon Bedrock AgentCore (Gateway, Runtime, Policy, Memory), DynamoDB, Neo4j AuraDB, AWS Lambda, Ollama (mentioned)

## [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](../videos/ZRM_TfEZcIo.md)
`ZRM_TfEZcIo` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: memory, context-engineering

Two builders show a file-based personal research system: raw sources, an index.yaml catalog and an LLM-written wiki, queried in tiers and fed by every question. No vector DB needed.

- Techniques: Tiered index-first retrieval; Immutable raw layer with LLM-owned derivatives; Query write-back with a log; Seeded multi-round deep research; Depth knob for research runs; Repo ingestion into per-repo and cross-repo notes
- Tools: Obsidian, Readwise, NotebookLM, Notion, Google Drive, Granola, Claude Code, Codex, Gemini Deep Research, Gemini (grounded Google search), Bright Data, YAML

## [User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](../videos/Jx4ZFEAq6bY.md)
`Jx4ZFEAq6bY` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: memory, skills-self-improvement, evals

StarlightSearch's CEO argues agent memory should learn from outcomes: utility-weighted retrieval, reasoning-style memories, and consolidation into skills. Product-pitchy, with self-reported benchmarks.

- Techniques: Utility-weighted memory retrieval; Human failure report as a memory write; Memory as procedure, not fact; Consolidate memories into skills; Runtime learning vs compile-time optimization
- Tools: Reflect (StarlightSearch's memory system), Mem0 (transcribed as 'memzero'), DSPy, ReAct, Pinecone (cited in a post, not used)

## [Structuring the Unstructured - Cedric Clyburn, Red Hat](../videos/-x5GEVnkuRw.md)
`-x5GEVnkuRw` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: data-engineering, mcp-and-tools, context-engineering

Red Hat's Cedric Clyburn demos Docling, an open-source local tool that converts messy PDFs into layout-aware Markdown, JSON, or Pydantic data, plus chunkless RAG over a document outline.

- Techniques: Layout-aware PDF to structured document conversion; Picture enrichment with a local vision-language model; Chunkless agentic RAG over a document outline; Schema-driven extraction from parsed documents; Document conversion as a microservice plus MCP tool; PII removal model before ingestion
- Tools: Docling, docling-serve, Docling MCP server, Pydantic, Ollama, Granite (IBM model), Qwen (via MLX), Jupyter, VS Code, Kubernetes, uvx

## [Google Replaced The Karpathy's LLM Wiki](../videos/k4sMSsMzX2g.md)
`k4sMSsMzX2g` · AI LABS · 2026-07-02 · q2 · practitioner · review · also: context-engineering, memory, claude-code

AI LABS walks through Google's Open Knowledge Format (OKF), a folder, index.md and YAML-frontmatter convention for markdown knowledge bases, and reports a small team test with lower token use and faster lookups.

- Techniques: Index.md per folder as the agent's entry point; YAML frontmatter with name, description and type on every concept document; Script-first markdown-to-OKF conversion with evals; CLAUDE.md navigation section that documents the bundle; Trial on a Git branch and visualize the bundle
- Tools: Open Knowledge Format (OKF, Google), BigQuery, Claude Code, CLAUDE.md, Obsidian (comparison only), Git / GitHub, Karpathy LLM-wiki pattern (concept, not a product), Google design.md standard (named in passing), Mobbin MCP (sponsor), Cursor, Lovable, v0 (named in sponsor segment), Markdown to OKF skill (the team's own, unnamed script)

## [Finally… A NotebookLM Alternative With an API](../videos/DnMtDdkSIi0.md)
`DnMtDdkSIi0` · Better Stack · 2026-07-02 · q2 · intro · review · also: local-ai, dev-tools

Walkthrough of Open Notebook, a self-hosted NotebookLM alternative with a REST API, swappable model providers including local Ollama, and podcast generation. Privacy and API access are the main draw; the Docker-first setup is a barrier.

- Techniques: Self-host via Docker Compose, then open the web UI; One notebook per project as a scoped research workspace; Structural codebase questions over an ingested repo; Custom podcast from dense documents; Pick the model provider per notebook based on sensitivity and cost
- Tools: Open Notebook, NotebookLM, AnythingLLM, Ollama, Docker / Docker Compose, SurrealDB, Gemini (named as the default-style provider the tool is not locked to)

## [Your AI Agent Is Missing Half the Internet… Until Now (Agent-Reach)](../videos/aanqEqQwjNU.md)
`aanqEqQwjNU` · Better Stack · 2026-07-02 · q3 · intro · review · also: mcp-and-tools, coding-agents

A 6-minute Better Stack review of Agent Reach, an MIT-licensed Python CLI that gives coding agents multi-platform web access (social, code, video, Chinese platforms) with health checks and fallback backends.

- Techniques: Per-platform channel adapters with primary and fallback backends; One-sentence agent-driven install plus a doctor health check; Shell permission as a prerequisite for self-install
- Tools: Agent Reach (Python CLI and library, MIT licensed, over 28,000 GitHub stars), Claude (used inside VS Code), Cursor 2, Playwright (suggested for interactive browser actions), Firecrawl (suggested for plain web pages; transcript says 'fire crawl'), YouTube, GitHub, Twitter/X, Reddit, Bilibili, Xiaohongshu (platform channels)

## [Scrapling: The Web Scraper That Repairs Itself](../videos/q-uj7wk0LRI.md)
`q-uj7wk0LRI` · Better Stack · 2026-07-02 · q3 · intro · review · also: data-engineering, dev-tools

Walkthrough of Scrapling, a Python scraping framework whose adaptive parser relocates moved or renamed elements without rewriting selectors, plus its fetcher tiers and spider framework.

- Techniques: Adaptive selector recovery; Tiered fetcher selection; Grow a script into a spider
- Tools: Scrapling (about 53,000+ GitHub stars, per the presenter; no version stated), Python, Requests, Beautiful Soup, Playwright, Selenium, Scrapy

## [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](../videos/zKk7sDMGDEQ.md)
`zKk7sDMGDEQ` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: claude-code, evals, coding-agents

Turbopuffer's Kuba Rogut benchmarks semantic code search as an extra tool for Claude Code, using a windowed-grep baseline and file, line and symbol precision and recall on human-labelled context tasks; semantic search helps precision but the gain is smaller than Cursor's because Claude Code does not know when to call it.

- Techniques: Chunk-embed-index semantic code search as a CLI tool; Windowed file reads as a retrieval baseline; Trajectory-level retrieval evaluation; Inline comments as embedding context
- Tools: Turbopuffer, Voyage code-3, Claude Code, Cursor, TurboGrep, tree splitter

## [Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j](../videos/abvQEhvRI_c.md)
`abvQEhvRI_c` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: memory, agent-architecture, context-engineering

Neo4j speakers argue agents need context graphs that store policies and rules as well as facts, so they can make and record decisions. They give a decision framework: frame, check global rules, assess risk, propose, then act, defer or escalate.

- Techniques: Propose, then decide, as two agents; Pre-decision risk screen; Decision log as a graph of precedent; Tiered memory in one graph; Framework as a skill or graph workflow
- Tools: Neo4j, Text2Cypher, LangGraph, ADK

## [RAG is dead, right?? — Kuba Rogut, Turbopuffer](../videos/UM6sFg_jdlE.md)
`UM6sFg_jdlE` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: coding-agents, context-engineering, infra-cost-scaling

Kuba Rogut (Turbopuffer) argues that "RAG is dead" misreads the problem: retrieval should be a toolbox (vector, BM25, grep, filters) used in iterative agent loops, and embeddings work best as precomputed cache compute.

- Techniques: Multi-modal retrieval toolbox for agents; Iterative search-read-assess loop; Index once, query at runtime; Merkle-tree index reuse across near-identical corpora; Staged narrowing before the context window
- Tools: Claude Code, Codex, Cursor, Turbopuffer, BM25, Merkle trees

## [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](../videos/btxGmN8RvNU.md)
`btxGmN8RvNU` · AI Engineer · 2026-06-18 · q2 · intro · review · also: mcp-and-tools, data-engineering

Bright Data pitch: blocked web access makes LLM agents fabricate answers silently. Its MCP (search, markdown scrape, CAPTCHA-solving browser) fixed a 5-site demo, but the evidence is one unreplicated run.

- Techniques: Paired with/without-tools comparison; Load a narrow subset of MCP tools; Scrape to markdown instead of HTML; Batch search across many keywords; LLM writes the parser, script does the extraction; Human-like remote browser instead of detection evasion; Restrict agents to public, non-login data; Pre-collected datasets for non-live needs
- Tools: Bright Data MCP (66 tools per speaker; 69 mentioned later), Bright Data scraping browser (remote, fingerprinted, CAPTCHA solving), Bright Data skills page, Bright Data datasets, GPT-5 (tested without tools as baseline), ChatGPT (cited for broken citations), Google, Bing and DuckDuckGo search (via MCP), Cloudflare bot blocking and AI Labyrinth (cited, not used), VS Code (demo environment)

## [Stop babysitting your agents... — Brandon Waselnuk, Unblocked](../videos/BiG2ssibKGc.md)
`BiG2ssibKGc` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: context-engineering, memory

Unblocked's Brandon Waselnuk argues agents need a runtime context engine, not more MCP access or static docs: exhaustive retrieval, surfaced conflicts, a social graph, and hard-won lessons.

- Techniques: Exhaustive retrieval before first-hit answers; Research packet before planning; Expert / social graph built from the code repo; Surface conflicts instead of silently picking; Permission-preserving delivery over MCP; Confidence-gated auto-answering; No answer caching for latency
- Tools: Claude Code, MCP, Codex, Anthropic API, AWS Bedrock, CLAUDE.md, AGENTS.md, Zendesk, Slack, Microsoft Teams

## [Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j](../videos/B9h9ovW5H9U.md)
`B9h9ovW5H9U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: memory, context-engineering, data-engineering

Neo4j's Zach Blumenfeld on context graphs: why agents need stored decision traces and precedents, not just documents, plus a one-line scaffold (create-context-graph) and the Neo4j agent memory pipeline.

- Techniques: Hybrid precedent retrieval over decision traces; Scaffold a context-graph app from a domain; Staged entity extraction from text into a graph; Ontology-first graph schema generation; Separate memory stores by kind
- Tools: Neo4j, Neo4j agent memory package, Graph Data Science (GDS), Cypher, uvx create-context-graph, Pydantic AI, Claude, OpenAI embeddings, Next.js, spaCy, GLiNER, MCP

## [Why I’m Switching To Powabase for My AI Apps](../videos/wC2QpP_A9-Y.md)
`wC2QpP_A9-Y` · Better Stack · 2026-06-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents

Better Stack tests PowerBase, a hosted backend bundling Postgres, pgvector RAG and an agent workflow builder, by having Claude Code build a RAG chatbot over an 80s hardware catalog. One demo, no measurements.

- Techniques: Agent-driven backend setup from docs and credentials; Single-Postgres RAG with pgvector; Ingest an existing OCR text export for RAG; Corpus-bounded answers with a missing-item probe; Node-based guardrails around LLM tool use; Review the session run log
- Tools: PowerBase (powerbase.ai), Supabase, PostgreSQL, pgvector, Claude Code

## [Connecting the Dots with Context Graphs — Stephen Chin, Neo4j](../videos/eW_vxrjvERk.md)
`eW_vxrjvERk` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: memory, mcp-and-tools

Neo4j DevRel lead argues agents need a knowledge graph that stores short-term, long-term and reasoning memory together, so decisions can be explained and reused. Mostly a product pitch with one finance demo.

- Techniques: Three-tier memory in one graph; Vector entry point then graph traversal; Decision write-back to the graph; LLM-generated Cypher with visible query trace; Multi-source ingestion through MCP tools into a graph
- Tools: Neo4j, Neo4j Agent Memory package (open source), Cypher, OpenAI embeddings, FastRP, Leiden algorithm, MCP, Next.js, Neo4j Aura (free tier), Graph Academy

## [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](../videos/ynJyIKwjonM.md)
`ynJyIKwjonM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, mcp-and-tools, skills-self-improvement

Leonie Monigatti (Elastic) argues context engineering is mostly agentic search, then walks through live demos of semantic search, ES|QL query tools, skill loading, and grep-style shell search, and when to use each.

- Techniques: Layered tool descriptions; Errors returned to the agent; Progressive disclosure for skills; Outsource aggregation to the search engine; Shell tool with semantic grep; Hybrid shell plus database verification; Log tool calls to find where specialization is needed; Use the file store as memory and offload old results
- Tools: LangChain, Elasticsearch, ES|QL, Jina embeddings v5, Jina grep (captioned as Gina grep), OpenAI GPT-5.4 nano and mini, shell / bash tool, Claude Code, OpenClaw (captioned as OpenCloud, exec tool)

## [The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked](../videos/qdh_x-uRs9g.md)
`qdh_x-uRs9g` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: inference-serving, infra-cost-scaling

Superlinked's Filip Makraduli on why small models (embeddings, rerankers, NER) need their own inference layer, and the open-source SIE engine built to serve them on shared GPUs.

- Techniques: Hot-swap many small models on one GPU with LRU eviction; Re-implement the forward pass per model family; Small-model preprocessing in front of the agent; Models as config, cluster as code
- Tools: vLLM, Prometheus, Grafana, Terraform, Helm, Docker, Hugging Face, FlashAttention, Chroma, Qdrant, Weaviate (transcribed as VV8), LanceDB (transcribed as LensDB)

## [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../videos/_QAVExf_1uw.md)
`_QAVExf_1uw` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, skills-self-improvement, enterprise-adoption

A staff engineer at IKEA argues enterprise agents fail on undocumented institutional knowledge, and proposes a pull-based loop where agents surface knowledge gaps and curate context blocks before retrieval.

- Techniques: Pull-based knowledge capture from failed agent runs; Failing-tasks-as-tests for knowledge bases; Historical-incident replay as a probe source; Three-step gap scanner: probe generation, probe run, gap analysis; Freshness labels, flagged for human decision; Git-backed curated context blocks with a metamodel; 80/20 context cache with links to the monolith; Full-context before graph RAG, for small domains; Claude Code skills, rules, agents and hooks as the implementation
- Tools: Claude Code, GitHub Copilot, Confluence, Jira, Slack, GitHub, MCP, RAG, GraphRAG, Replit, Kanban board

## [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../videos/5ID22ACI7IM.md)
`5ID22ACI7IM` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: context-engineering, memory, security-guardrails

Peter Werry and Brandon (Unblocked) argue that agents need a "context engine" that understands org history, permissions and conflicts, not just MCP access to data, then run a hands-on social-graph workshop. Much of it is product pitch.

- Techniques: Compartmentalized, permission-tagged retrieval; Ingestion-time tags plus runtime judge for conflicts; Expert graph from contribution edges; Focus-repo-biased two-stage retrieval; Feedback weighted by source trust; Split cadence by source type
- Tools: Claude Code, Cursor, Codex, GitHub Copilot, MCP, Slack, Microsoft Teams, Sentry, Datadog, GraphRAG, pgvector-style vector retrieval, Composio

## [How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research](../videos/zZsTVBXcbow.md)
`zZsTVBXcbow` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: models-research

Raia Hadsell (VP Research, Google DeepMind) surveys non-LLM frontier work: unified multimodal embeddings, neural weather models (GraphCast, GenCast, FGN), and Genie world models.

- Techniques: Unified multimodal embedding; Matryoshka (MRL) dimension scaling; Probabilistic forecasting for tail events; Train for the end target, not a post-hoc detector; Memory consistency test for world models
- Tools: Gemini Embeddings 2, GraphCast, GenCast, FGN (Functional Generative Network), Genie 1, Genie 2, Genie 3, Veo 3, Gemma 4

## [I Stopped Using Grep and My Agent Got 10x Faster](../videos/gPeWb4_DMok.md)
`gPeWb4_DMok` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: mcp-and-tools, coding-agents, token-cost-efficiency

Hands-on test of Claude Context, an MCP server that indexes a codebase into Zilliz/Milvus using Tree-sitter chunks, Merkle-based incremental updates and hybrid vector+BM25 search. Faster and richer on mid-size repos, slow to index on huge ones.

- Techniques: Set up Claude Context as an MCP server; Index once, then search many times; Compare indexed and plain agents side by side; Pick the repo size where the trade-off works; Test on a cheaper model to save subscription quota
- Tools: Claude Context (Zilliz MCP plugin for codebase indexing and search), Zilliz Cloud (serverless cluster), Milvus (vector database), OpenAI embeddings API, OpenCode (agent harness), GLM5 Turbo (model), Claude Code (mentioned as a possible agent), Claude Pro (subscription; weekly limit), Opus 4.7 (model, not tested), Tree-sitter (AST chunking, 9 languages), BM25 (keyword index), Merkle DAG with JSON snapshots (change detection)

## [Microsoft Just Solved Document Ingestion for AI Devs (MarkItDown)](../videos/9ZaiZzp4XcY.md)
`9ZaiZzp4XcY` · Better Stack · 2026-05-02 · q2 · intro · tutorial · also: data-engineering, mcp-and-tools

Short intro to Microsoft's MarkItDown, an MIT-licensed Python tool and CLI that converts Office files, PDFs, images and audio into LLM-friendly Markdown, with a trade-off note against Pandoc, Unstructured and Docling.

- Techniques: Single-tool ingestion to Markdown (CLI); Python conversion with an LLM for images and charts; Pick the extractor by document difficulty
- Tools: MarkItDown, Pandoc, Unstructured, Docling, OpenAI Python client, Claude Desktop (transcript says 'Claw Desktop', auto-caption error), pip, MCP server (MarkItDown's)

## [This Open-Source Tool Replaces Ollama + LangChain + Your UI](../videos/pSYEcJTt4t4.md)
`pSYEcJTt4t4` · Better Stack · 2026-04-02 · q3 · intro · review · also: local-ai, dev-tools

Better Stack walkthrough of AnythingLLM, a self-hosted open-source AI workspace that bundles local LLM chat, drag-and-drop RAG, no-code agents and a REST API into one desktop app, with an honest pros/cons take.

- Techniques: Single-app local RAG setup; Citation-grounded codebase Q&A; Visual agent with tool embedding; Swap providers mid-chat; Embed private RAG in other products
- Tools: AnythingLLM, Ollama, LanceDB, pgvector, Qdrant, LangChain, Open WebUI, PrivateGPT, Flowise, Langflow, SERP API, MCP servers

## [The Fastest Python Scraper for RAG? (Crawl4AI)](../videos/BpsRH-1TZk4.md)
`BpsRH-1TZk4` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: data-engineering

Better Stack walkthrough of Crawl4AI, a Python crawler that returns clean Markdown/JSON for LLM pipelines, with prefetch mode, resumable deep crawls and schema-based LLM extraction; the "fastest" claim is stated but not measured on screen.

- Techniques: Basic async crawl to Markdown or JSON; Prefetch for link discovery, then selective extraction; Resumable BFS deep crawl; Schema-driven LLM extraction
- Tools: Crawl4AI, Playwright, Pydantic, Ollama, Scrapy, BeautifulSoup, Selenium, pip

## [How To Use NotebookLM - 7 Crazy Ways](../videos/eFCHwtufjJc.md)
`eFCHwtufjJc` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: context-engineering, claude-code, coding-agents

AI LABS shows seven ways to wire Google's NotebookLM CLI into Claude Code as a grounded knowledge base: a second brain, research store, codebase onboarding, debugging KB, agent-readable visualizations, and a security handbook.

- Techniques: Install and verify the NotebookLM CLI; Notebook as project second brain via CLAUDE.md; Research offload to a notebook; Codebase onboarding via Repomix; Debugging knowledge base in place of web search; Export mind maps and tables as agent-readable artifacts; Security handbook notebook for grounded reviews; Shared notebook as knowledge base for people and other agents
- Tools: NotebookLM (Google), NotebookLM CLI (version not stated), Claude Code, CLAUDE.md, Repomix (CLI, installed via npm), GitHub CLI (gh), Gemini (answers NotebookLM queries, per the speaker), Cursor, Gemini CLI, OWASP cheat sheets, Make (sponsor, pre-built market research agent)

## [How to Build a RAG System That Actually Works](../videos/pvCabUerwss.md)
`pvCabUerwss` · Better Stack · 2026-02-02 · q3 · intro · tutorial · also: context-engineering

Better Stack walkthrough of building a RAG system over Star Wars scripts with LangChain, OpenAI embeddings and local Qdrant, focused on scene-aware chunking and prompt grounding.

- Techniques: Scene-aware recursive chunking; Persist-or-build vector store; Fixed-k retrieval with a deterministic chat model; Prompt grounding tuned with a scope test set
- Tools: LangChain, langchain-openai, langchain-qdrant, qdrant-client, langchain-text-splitters, BeautifulSoup4, requests, uv, Qdrant (local vector database, written in Rust), OpenAI text-embedding-3-small, GPT-4o

## [Stack Overflow is Dead (Here's Why)](../videos/dsfqyVYkrbM.md)
`dsfqyVYkrbM` · Better Stack · 2026-02-02 · q2 · intro · other · also: dev-tools, product-ux

Opinion essay (Better Stack) arguing Stack Overflow's question volume collapsed after 2014 moderation changes, was accelerated by ChatGPT, and that AI is gatekeeping public developer knowledge.
- Tools: Stack Overflow, ChatGPT, Answer Overflow, Discord, Slack, Reddit, Apollo (third-party Reddit app, mentioned as shut down)

## [Ship LLM Apps Locally with Dify](../videos/V-YvJdZx6sY.md)
`V-YvJdZx6sY` · Better Stack · 2026-02-02 · q2 · intro · review · also: agent-architecture, dev-tools

Better Stack's short walkthrough of Dify, a self-hosted visual builder for LLM apps (RAG, chained prompts, agents), with a file-summarization demo and a candid list of drawbacks.

- Techniques: Branch a workflow on input file type; Add a model provider via Settings; Run Dify locally with Docker; Choose between visual builder and code orchestration
- Tools: Dify, LangChain, LlamaIndex, n8n, OpenAI API, Google Gemini, Docker, Vercel, Supabase, ReAct agent pattern

## [This Google Tool Turns Messy Text Into Clean Data](../videos/96P65wL2zmw.md)
`96P65wL2zmw` · Better Stack · 2026-02-02 · q2 · intro · tutorial · also: data-engineering

Short Better Stack overview of LangExtract, Google's free open-source Python library that uses LLMs to pull structured entities and relationships from messy text, with each extraction tied back to its exact source span.

- Techniques: Prompt-defined structured extraction without training data; Setup: clone repo, install requirements, keep the API key in .env; Span-grounded verification loop; Batch mode for large document sets
- Tools: LangExtract (Google open-source Python library, version not stated), Gemini API (Google), GPT (OpenAI models, named as a supported backend), Python, pip, Git, .env file for API keys, JSON output, Auto-generated interactive HTML viewer

## [Vercel Just Revealed Claude Code's Greatest Advantage](../videos/gZr5VmsXmXQ.md)
`gZr5VmsXmXQ` · AI LABS · 2026-02-02 · q3 · practitioner · talk · also: context-engineering, sandboxing-execution

Argues that LLM agents can retrieve context with plain bash (ls, find, grep, cat) instead of a vector DB, sending only a small slice to the model; shows a Gemini 2.5 Flash policy-docs demo and states when RAG still wins.

- Techniques: Bash-tool retrieval over a document directory; Scoped execution for agent shell access; Markdown-defined multi-phase evaluation pipeline; Route retrieval by data shape and query type
- Tools: Vercel bash tool (open-sourced; name not stated), Vercel sandbox (full VM isolation), Claude Code, CLAUDE.md, Gemini 2.5 Flash, Chroma (vector DB the speaker would normally have used), grep, ls, find, cat

## [The Missing Layer in Your AI Stack: Supermemory](../videos/GETMfbGWc0k.md)
`GETMfbGWc0k` · Better Stack · 2025-12-02 · q2 · intro · review · also: memory, context-engineering

Walkthrough of Supermemory, a hosted persistent-memory layer with API, SDK, and proxy "memory router" modes, demoed on a Next.js chatbot over imported YouTube stats. Vendor-led; no evaluation of recall quality.

- Techniques: Memory via proxy base URL; Scope memory with a container tag; Force memory lookup with a system instruction; Memory as an agent tool via SDK; Bulk seed from tabular data; Write chat turns back as memories
- Tools: Supermemory (memory API, SDK, memory router proxy, dashboard memory graph), SuperMemoryTools SDK package, Vercel AI SDK, Next.js, OpenAI client, GPT-4 (as the provider in the demo), CSV (ingest format)

## [Redis 8 Makes AI Search Blazingly FAST](../videos/YwoaqLsrHew.md)
`YwoaqLsrHew` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

Short Better Stack tutorial showing Redis 8 vector sets for product similarity search in a small Express app, plus a clarification of how they differ from the Redis vector database.

- Techniques: Embed product text for similarity, then store vectors in a Redis vector set; Query neighbours by element ID with VSIM; Keep a plain cosine-similarity function as a fallback; Turn on persistence for an in-memory vector store; Choose between vector sets and the Redis vector database
- Tools: Redis 8, Redis vector sets (beta, VADD / VSIM), Redis vector database (hash or JSON storage; RediSearch / Redis Query Engine, referred to as 'ready search'), Redis vector library, Express, EJS, Docker, OpenAI embeddings API

## [Build A RAG AI System in 5 Minutes with Cloudflare + Firecrawl!](../videos/YxC1zEz5TDY.md)
`YxC1zEz5TDY` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools

Four-minute tutorial wiring Firecrawl-scraped docs into R2, indexing them with Cloudflare AutoRAG, and exposing the index to Cursor through Cloudflare's MCP server.

- Techniques: Crawl a docs site to Markdown with page metadata; Use R2 as the S3-compatible document store for RAG; Index an R2 bucket with AutoRAG using the auto models; Expose an AutoRAG index to Cursor as a global MCP server
- Tools: Firecrawl (Node package, crawl-URL method, Markdown export), Cloudflare R2 (S3-compatible object storage), Bun S3 client, Cloudflare AutoRAG (beta), Cloudflare vector database (used by AutoRAG; not named in the video), Cloudflare Workers, Cloudflare MCP servers (AutoRAG server, one of about 30 released recently), Cursor, Claude (comparison point only), Tailwind CSS (only referenced as an example doc set and a separate video)

## [Using this will make your AI AGENTS EVEN SMARTER!](../videos/2G-xavWw1bY.md)
`2G-xavWw1bY` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, token-cost-efficiency

A 5-minute tip for loading a whole GitHub repo into an LLM, either through a chat tool or a repo-to-text converter (gitingest), to answer questions and find install steps.

- Techniques: Repo URL swap into a chat-with-repo tool; gitingest repo-to-text conversion; Pick the model by token count; Explicit completeness prompting; Iterative setup questions on an ingested repo
- Tools: gitingest (named 'git ingest' in the transcript), DeepSeek (model, transcribed as 'DeepSeq'), Gemini (model), Cursor IDE, Claude (install instructions in the repo), GitHub, MCP server (example repo, unnamed)

## [Time to UPGRADE… Unified AI Agents Are Finally Here](../videos/VDql5GzoSoc.md)
`VDql5GzoSoc` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, coding-agents

Walkthrough of ACI.dev, a hosted platform that connects apps to agents via an app store, an agent playground and a unified MCP server with search and execute tools; the hype title outruns the unbenchmarked speed claims.

- Techniques: Attach apps to an agent in ACI's playground; Unified MCP server in Cursor; Separate agents with separate tool sets
- Tools: ACI.dev, ACI unified MCP server, ACI app MCP server, Agent Playground (ACI), Google Calendar, YouTube, Google Maps, Gmail, Brave Search, Archive (app named in video), Cursor, Claude Desktop

## [ChatGPT Search Just Launched! Say Goodbye to Google?](../videos/f57EGI35bwI.md)
`f57EGI35bwI` · AI LABS · 2025-11-02 · q2 · intro · review · also: product-ux

Short AI LABS walkthrough of ChatGPT's web search for Plus users, with cited sources, live stock and flight queries, and a Chrome extension that routes browser searches to ChatGPT.

- Techniques: Run a cited web search in ChatGPT; Make ChatGPT the browser's default search
- Tools: ChatGPT, ChatGPT web search, Google Search, Perplexity, Google Chrome, Chrome Web Store

## [Stack Overflow for your LLMs (and you!)](../videos/IYyyiA5eWEo.md)
`IYyyiA5eWEo` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, mcp-and-tools

A short Better Stack tool walkthrough of grep.app, a fast regex code search over GitHub, and its MCP server, which lets Claude Code or Cursor pull real library usage into context instead of hallucinating APIs.

- Techniques: Add grep.app as an MCP server in Cursor or Claude Code; Literal and regex code search with filters; Version-specific search for new packages; Regex to detect committed secrets (defensive use)
- Tools: grep.app, GitHub, Claude Code, Cursor, MCP, Lexical, Next.js, React Router, Payload CMS

## [RAG Just Got Updated…](../videos/EgXOaH-ZqfU.md)
`EgXOaH-ZqfU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, mcp-and-tools, coding-agents

Setup and demo of Archon, a beta self-hosted tool that gives Claude Code or Cursor project docs, a task backlog, and on-demand RAG over crawled docs via MCP. Includes a sponsor segment and an oversold title.

- Techniques: Local Archon stack setup; Project docs and backlog from a feature description; Rules-file-driven on-demand RAG; Crawl vendor docs into a knowledge base
- Tools: Archon, Claude Code, Cursor, Supabase, Docker, Docker Compose, MCP (Model Context Protocol), OpenAI API (embeddings), Google Gemini API (embeddings, free tier), SwiftUI, Xcode, Liquid Glass (Apple UI design)

## [Hao Sheng on Building Human-Business Interfaces with AI | Better Stack Podcast Ep 3](../videos/IFSK3_M6Fuk.md)
`IFSK3_M6Fuk` · Better Stack · 2025-11-02 · q2 · intro · interview · also: product-ux, enterprise-adoption

Hao Sheng (Expertise AI) on a human-to-business interface that generates per-visitor pages, with founder lessons from Dialogflow, Cresta and bootstrapping; mostly narrative, thin technical detail.

- Techniques: Start-from-problem validation before building; Query rewriting before retrieval; Multimodal retrieval with cross-modal consistency checks; Human-in-the-loop labeling for intent classifiers; Per-visitor generated page from conversation
- Tools: Dialogflow (Google), Expertise AI (formerly Chat Simple), Cresta, HubSpot, AlexNet, ImageNet

