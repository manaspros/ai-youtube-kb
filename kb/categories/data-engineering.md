# data-engineering — 126 videos

*data pipelines, structured extraction, documents, data quality with LLMs*

By channel: AI Engineer 90 · Kai Explains 4 · Better Stack 32

**Synthesized guide:** [guides/data-engineering.md](../guides/data-engineering.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Your AI Agent Wants Your Data. Here's How to Lock It Down - Jeff Smith, Oracle](../videos/LnQce-eHm8k.md)
`LnQce-eHm8k` · AI Engineer · 2026-11-01 · q3 · practitioner · review · also: mcp-and-tools, security-guardrails, context-engineering

Oracle's Jeff Smith on locking down agent access to databases: expose curated reports as MCP tools instead of raw NL-to-SQL, give agents a compact schema tool, and enforce identity-based row and column security inside the database.

- Techniques: Curated report catalogue exposed through two MCP tools; Three server modes: ad hoc SQL, custom tools and reports only, or both; Reveal report SQL to agents under a privileged scope; Action-grouped tools instead of single-purpose tools; Compressed deterministic schema-info tool; Generate schema annotations from enterprise documents; Identity-driven row and column filtering at the database; Diagnose production performance on a read-only standby
- Tools: Oracle AI Database, Oracle MCP server, MCP (Model Context Protocol), MCP apps (spec feature, speaker says added to the spec in July; Oracle plans a GUI for later this year), Claude, Codex, Gemini, LangChain, Azure Entra ID (spoken as 'Azure IntraID'), Oracle Data Guard, AWR (Automatic Workload Repository, Oracle performance report), Confluence

## [Why AI Won't Replace Stock Pickers - Jack Woodruff, Candlestick & Vinoo Ganesh, Kepler](../videos/y2dyD6slKxE.md)
`y2dyD6slKxE` · AI Engineer · 2026-10-30 · q2 · intro · interview · also: governance-compliance, enterprise-adoption

Fireside chat between a hedge fund founder and a Kepler co-founder on how AI changes stock picking: AI raises the baseline, auditability is the trust gate, and edge comes from divergent views and idea velocity.

- Techniques: Audit-first verification of model-produced numbers; AI as attention triage for human research; Automate prep, reinvest time in differentiated work

## [HBO Accidentally Built a Market-Beating Index Fund](../videos/wbRaBUhkVhc.md)
`wbRaBUhkVhc` · Better Stack · 2026-10-26 · q2 · intro · review · also: —

Better Stack backtests seven ways to invest in the company logos from the Silicon Valley title sequence; only a market-cap-weighted, rebalanced "ETF" version beats both the S&P 500 and Nasdaq-100, and the speaker says it is mostly a big-tech fund. No AI content.

- Techniques: Event-driven dataset from frame-by-frame tagging; Compare the same universe under several rule sets
- Tools: Nasdaq-100 (benchmark), S&P 500 (benchmark)

## [How Bridgewater Turned 100 Million Documents Into an Edge - Sam Green & Aaron Linsky, Bridgewater](../videos/CLve4Nx_RwI.md)
`CLve4Nx_RwI` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: rag-retrieval, enterprise-adoption, product-ux

Bridgewater's Applied AI team describes the Vault, a governed corpus of 100M+ unstructured documents, and the lessons from making it useful to both human investors and agents: separate design for each reader, benchmark-driven search, and feeding agent-human synthesis back into the corpus.

- Techniques: Hand-labelled retrieval benchmark before tuning; Cluster-aware native filtering in the vector store; Infer a time window from the question and scope retrieval to it; Separate human and agent retrieval design; Migrate existing user habits into the new tool first; Write synthesis back into the corpus
- Tools: Turbopuffer (vector database, native filtering), Bridgewater Vault (internal unstructured data platform), Aya (internal artificial investment associate), Pocket Analyst (internal AI analyst), Researcher (internal, next-generation analyst), Forecaster (internal, custom model plus foundation models), Slack, IDE integration, CLI for agents, phone app, enterprise chat client (unnamed)

## [How to Build Financial Agents That Work Across the Web - Jay Sahnan & Arik Bird, Browserbase](../videos/DZ24Xbm9Joc.md)
`DZ24Xbm9Joc` · AI Engineer · 2026-10-25 · q2 · practitioner · review · also: voice-multimodal, sandboxing-execution, enterprise-adoption

Browserbase engineers pitch hosted, forked "verified" Chromium plus the open-source Stagehand SDK for running browser agents at scale on finance portals, with Ramp, Bill and Stripe as case studies.

- Techniques: Accessibility-tree page compaction before the LLM call; Hybrid deterministic plus natural-language browser control; Observe, act, extract as three separate primitives; Schema-first extraction with Zod; Single code path fanned out across many sites; Keep browser processes alive between tasks; Run the agent-side browser controller next to the browser; Copy-prompt onboarding for coding agents
- Tools: Browserbase (hosted browser infrastructure), Stagehand (open-source browser-control SDK built on Playwright), Playwright, Selenium, BeautifulSoup, Chromium (forked; Browserbase's verified build), Chrome, Zod, ngrok (used to share the demo), EC2 (named as the data-center example)

## [Do Not Let Models Invent Numbers - Vinoo Ganesh, Kepler](../videos/dZgA6btnb_s.md)
`dZgA6btnb_s` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: rag-retrieval, security-guardrails

Kepler's CEO explains how its finance research platform stops LLMs from inventing numbers: models cite pre-registered SEC facts, deterministic code does the math, and any unverifiable number is stripped.

- Techniques: Cite-don't-write with post-filter; Typed fact registry; Search wide, then re-rank in stages; Per-hit document authorisation; Keep conflicting sources and de-conflict; Measure recall and idempotency as guarantees
- Tools: Kepler (finance research platform), Turbopuffer (vector and BM25 search, namespaces), Zero Entropy embeddings (as stated; 1280 dimensions), Postgres (per-document authorisation), Cross-encoder re-ranker (model not named), XBRL (structured filings data, cited as ~10% incorrect), SEC filings: 10-K, 10-Q, 8-K, S-1, investor presentations, earnings call transcripts, Claude and ChatGPT (used as baseline in evals), Gemini 4 (mentioned, not evaluated)

## [Can AI Understand a Distressed Credit? - Harneet Kaur, Axim Intelligence](../videos/WOszaC1WWbQ.md)
`WOszaC1WWbQ` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · also: evals, models-research

Founder of Axim Intelligence on testing whether LLMs can forecast distressed credit outcomes; models disagreed until a structured, layer-by-layer reasoning process made them converge, though no ground truth was shown.

- Techniques: Layer-by-layer benchmarking of an LLM analysis pipeline; Cross-model disagreement as a diagnostic; Structured reasoning scaffold to force convergence
- Tools: Opus (Opus 5.5, as named in transcript), Astra 6 (named in transcript; the model name may be an auto-caption error)

## [A Bank Trained Its Own Foundation Model to Catch Fraud — Freddy Lecue, Wells Fargo](../videos/UB6hoWyh3B0.md)
`UB6hoWyh3B0` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · also: models-research, enterprise-adoption

Wells Fargo built a ~1B-parameter transformer pre-trained from scratch on customer transaction data as a reusable backbone; it beat its production XGBoost fraud model on detection rate and false positives.

- Techniques: Transaction tokenization for tabular data; Raw-field representation instead of hand-engineered features; Decoder-only pre-training on a transaction sequence, then task fine-tuning; Scaling-law sizing with empirical correction; Standard large-scale training recipe; Benchmark against the production GBDT on business metrics
- Tools: XGBoost (production baseline), Transformer / decoder-only architecture, Chinchilla scaling laws, Flash Attention, RoPE, Mixed precision, Distributed data parallel, Activation checkpointing, Muron (auto-caption; likely AWS Neuron), GPU cluster, Wells Fargo transaction foundation model (internal, ~1B params; 11B in progress)

## [This Looks Like Spy Software... It's Just Public Data](../videos/PQN76wcEt10.md)
`PQN76wcEt10` · Better Stack · 2026-10-23 · q3 · intro · review · also: mcp-and-tools, dev-tools, voice-multimodal

Walkthrough of God's Eye View, an open-source local globe that fuses public live feeds (planes, ships, satellites, cameras, quakes), with its feed-smoothing design and honest data caveats.

- Techniques: Run God's Eye View locally; Render the last update one step behind and interpolate; Dead reckoning for dropped feeds; Ration a free API quota with a budget; Hard spend cap for a realtime voice API; Unlock 3D tiles through an external key
- Tools: God's Eye View (open-source globe project, about 55,000 GitHub stars), Cesium JS, Vite, Node.js (24.14 or newer required; 25 unsupported), npm, SGP4 orbit model, ADS-B, AIS, OpenSky Network, MCP (Model Context Protocol) server, Claude, Codex

## [AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard](../videos/uA4ah-dVHvU.md)
`uA4ah-dVHvU` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: enterprise-adoption, mcp-and-tools, multi-agent

Vanguard's cash-ledger modernization: exposing the legacy codebase over MCP cut a 7-day research loop to 15 minutes, with lessons on migration, idempotent producers and consumer onboarding.

- Techniques: Expose a legacy codebase to agents through an MCP server; Two-stage CDC migration verification; Single write gateway with idempotency for all producers; Consumer access matched to channel; Business-case registration for consumers; Fix forward, do not patch the legacy; Human-readable state values in the new system; Shared team knowledge base
- Tools: MCP server (legacy codebase and migration docs exposed to AI tools), CDC (change data capture, generic), GraphQL (real-time consumer API), Kafka (event topic for inserts and updates), Schema registry (generic, for all consumer channels), Snowflake-style IDs (ID paradigm, not the product), Data warehouse data-share views (batch consumers)

## [The Investor's Edge Lives in Their Head — Anekha Sokhal, Moshi](../videos/UHbODjuviAU.md)
`UHbODjuviAU` · AI Engineer · 2026-10-20 · q2 · intro · talk · also: product-ux, governance-compliance

Vendor talk from Moshi's founder arguing that an investor's edge is human judgment: machines should do the data grind, while every AI claim stays traceable and the human makes the call.

- Techniques: Split grind from judgment; Per-claim traceability and measured hallucination; Deterministic multi-agent decomposition
- Tools: Moshi (the speaker's own product, described as a 24-7 quant analyst for institutional traders)

## [Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa](../videos/L4dUFimVDKU.md)
`L4dUFimVDKU` · AI Engineer · 2026-10-19 · q2 · practitioner · workshop · also: evals, rag-retrieval

Exa's forward-deployed engineer demos ExaSnapshot, point-in-time web search for backtesting agents without future leakage, plus a hands-on acquisition-prediction exercise. Mostly a vendor pitch, but the leakage and holdout-set points hold regardless of vendor.

- Techniques: Point-in-time (as-of date) retrieval for backtests; Content versioning for trusted historical features; Feature-by-feature backtest with a holdout set; Scoring rubric for event prediction; Pin the repo state for coding-model evals
- Tools: Exa, ExaSnapshot, Cursor, Gamma, ChatGPT, Claude

## [Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs](../videos/W4pnzOURwHQ.md)
`W4pnzOURwHQ` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: evals, enterprise-adoption, governance-compliance

Insurance claims data is messy, so AI claims work needs layered extraction, duplicate detection, human verification, and calibrated tiered benchmarks before cross-claim analytics pay off.

- Techniques: Layered extraction with per-level verification; Tiered benchmark with a private held-out tier; Calibrated multi-judge verification; Back-test on historical samples before pilot; Duplicate and co-mingling detection at intake; Human-in-the-loop surfacing with page references
- Tools: Artificial Analysis MLCR benchmark, GPT models, Anthropic models, ChatGPT, Gemini, Claude

## [AI Agents Cut 3-Day Portfolio Builds to Minutes — Jack McDonald, Apollo & Michael Manapat, Rowspace](../videos/BOWYujhIQuo.md)
`BOWYujhIQuo` · AI Engineer · 2026-10-17 · q2 · intro · interview · also: enterprise-adoption, product-ux

Customer case study: Rowspace agents and an embedded team cut Apollo's portfolio builds from days to minutes and weekly trade recaps from hours to a one-minute report, with trust earned through per-field source validation.

- Techniques: Embedded discovery with domain teams; Per-field source precedence; Agent draft then human refinement; Automate recurring reports, keep human QA

## [Stop Chatting With Spreadsheets — Francesco Galletta & Felippe Felisola Caso, Monzo](../videos/e9-br9hveRI.md)
`e9-br9hveRI` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · also: agent-architecture, testing-verification, governance-compliance

Hands-on workshop on building a trustworthy financial-analysis harness around five principles (shared domain, deterministic calculations, evidence, accountability, verification), demoed on a wedding-budget planner.

- Techniques: Interview-style shared-domain planning with a decision tree; Calculation-as-code with tests and golden examples; Fact / assumption / interpretation labelling with provenance; Branching challenge agent with merge or dismiss; Tiered accountability gates
- Tools: Claude Code, Codex, Looker Studio, Google Slides, Google Sheets

## [Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket](../videos/gonAewBZxfU.md)
`gonAewBZxfU` · AI Engineer · 2026-10-15 · q4 · practitioner · talk · also: rag-retrieval, evals, agent-architecture

Two In The Pocket engineers describe a RAG assistant over a Belgian payment scheme's rulebooks: section-aware chunking, table flattening, hybrid retrieval, agentic narrow-to-wide tools, and noisy LLM-judge evals.

- Techniques: Section-path chunking without overlap; Table flattening for merged cells; Hybrid dense plus BM25 with RRF; Narrow-to-wide agent tool ladder; Tool-level recovery guardrails; Stream prose, render structured parts last; Lightweight feedback logging; Promptfoo end-to-end evals plus retrieval-only eval
- Tools: Qdrant, BM25, Reciprocal Rank Fusion, Promptfoo, Pydantic, LLM-as-judge

## [Every Building Is a Balance Sheet: Spatial Memory for Real-World Assets — Jordi Spranger, Spranic](../videos/Fe4aSMXsOZ4.md)
`Fe4aSMXsOZ4` · AI Engineer · 2026-10-14 · q2 · intro · talk · also: voice-multimodal, product-ux

Jordi Spranger (Spranic, with Neo4j) pitches walk-through 3D scans stored as a time-aligned graph, so real buildings become queryable, change-tracked data for insurance and lending.

- Techniques: Repeat-capture alignment and diffing; Graph as the world model; Provenance on every observation; Natural-language query over a graph map
- Tools: Neo4j, off-the-shelf 3D scanning sensor

## [Just-in-Time Ontologies: What Cheap Intelligence Means for Data — Hrishi Olickel, Southbridge AI](../videos/Fa3hQVIKShw.md)
`Fa3hQVIKShw` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: token-cost-efficiency, evals, agent-architecture

Hrishi Olickel (Southbridge AI) argues there is no universal schema, so build just-in-time ontologies per decision, using cheap model tiers, cross-family disagreement, and a failure surface.

- Techniques: Split the job into typed cases before modeling; Fix the question definition, not the threshold; Cross-family disagreement as the audit signal; Cost-tiered checking budget; Bounded pilots, then reusable codons, then production; Pareto surfing with a fixed baseline; Check for prior-driven silent errors
- Tools: Hank Weave (captions: Hank Wave, open-source harness for headless data work), Claude Code (captions: cloud code), Opus, Anthropic Claude models (cheap reasoning tier and frontier tier)

## [Parsing the Epstein Files for JMail — Palak Agarwal & Omar Alhait, Reducto](../videos/HGfsfKaVuGY.md)
`HGfsfKaVuGY` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: evals, product-ux

Reducto staff show how their parse-then-extract pipeline turned 3M+ messy Epstein-file PDFs into the JMail sites, then run a hands-on extraction exercise.

- Techniques: Parse-then-extract pipeline; Agentic OCR with self-correction; Schema review in a playground before deploy; Content-aware schema generation; Separate citation pass; Per-use-case prompts on specialized sub-models; Tiered evaluation with your own benchmark
- Tools: Reducto Studio, Reducto parse, split, extract, edit and classify APIs, Claude Code or Codex (paste-in setup instructions via a QR code, per the speaker)

## [Teaching Agents to Search with NVIDIA Data Designer — Dhruv Nathawani, NVIDIA](../videos/qFaKvbVc5cE.md)
`qFaKvbVc5cE` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: training-finetuning-rl, rag-retrieval, evals

NVIDIA workshop on NVIDIA Data Designer: build column-by-column synthetic data pipelines, seed them with Wikidata random walks and Tavily search traces, and use them to teach a model web search (BrowseComp 0 to about 30%).

- Techniques: Column-by-column DAG for synthetic data; Seeded random walks over a knowledge graph; Teacher trajectories with a tool, then SFT on the trajectories; Overproduce and filter funnel; Layered verification of synthetic labels; Skip the golden answer and use a reward function (RL path); Persona seeds from census marginals
- Tools: NVIDIA Data Designer, Nemo Curator, Nemo Gym, Nemo Anonymizer, Nemo Safe Synthesizer, Tavily, MCP, vLLM, gpt-oss-120b, Wikidata, Hugging Face

## [Building AI Agents with Real-Time Web Data — Yohan Raju, Bright Data](../videos/IK8cC4FScps.md)
`IK8cC4FScps` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: mcp-and-tools, rag-retrieval

Bright Data's Yohan Raju argues that live web data (scrapers, anti-bot handling, and an MCP endpoint with 60+ tools) lets AI agents answer questions that pre-indexed RAG cannot, then demos an Amazon-plus-Reddit buy/no-buy agent.

- Techniques: Live-vs-indexed query routing; Response caching for time-stable answers; One MCP endpoint with many scraping tools; Search-then-scrape chaining; Decision agent over multi-source API data; Record validation and medallion staging
- Tools: Bright Data MCP server, Bright Data Web Unlocker, Bright Data Browser API, Claude Code, Claude, GPT, Gemini API, LangChain, Google Colab-style notebook, Glassdoor, Amazon, Reddit

## [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](../videos/KhRjivBSwiw.md)
`KhRjivBSwiw` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: context-engineering, evals, mcp-and-tools

TypeDef's talk and workshop argue that data and code agents need a computed, traversable context graph; deterministic structure comes first, and agents still default to grep unless tools are shaped and measured.

- Techniques: Deterministic structure first, LLM last; Layered extraction ladder for code; Persistent typed graph with subgraph traversal; Blast-radius tool before edits; Incremental re-indexing keyed to changed files; Isolated data clones for evals, with injected bugs; Tool renaming and shape-matching; Consistency and adoption metrics; Many small focused LLM questions; Eval set pinned to a snapshot, with near-failing tasks
- Tools: Neo4j, Cypher, tree-sitter, rustdoc JSON, Pydantic AI, pydantic evals, Fennec, OpenRouter, Logfire, dbt, Snowflake, Databricks

## [Beyond RAG: A Relational Context Engine That Cuts Token Burn — Unblocked](../videos/ORVh4GivEU0.md)
`ORVh4GivEU0` · AI Engineer · 2026-10-11 · q3 · practitioner · demo · also: rag-retrieval, token-cost-efficiency, context-engineering

Unblocked (Peter) argues RAG misses structured questions, then builds a schema-aware query engine over a document store with validation and self-correction; the talk is a demo-heavy speed run.

- Techniques: Dynamic schema discovery by document sampling; Fuzzy identity resolution with LLM tiebreak; Validate-then-inject for generated queries; Bounded self-correction loop; Per-task context bundle with an A/B harness
- Tools: Claude, MongoDB, GitHub, Slack, Notion

## [Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked](../videos/spxoDAfh5ig.md)
`spxoDAfh5ig` · AI Engineer · 2026-10-11 · q4 · practitioner · workshop · also: rag-retrieval, security-guardrails, context-engineering

Peter Werry (Unblocked) builds a schema-aware natural-language-to-database-query engine from scratch, covering schema sampling, identity mapping, allow-list validation and an error-retry loop, as the structured half of retrieval beyond RAG.

- Techniques: Dynamic schema discovery by document sampling; Deny-by-default query validation; Error-feedback retry loop; Forced tool call for entity extraction, with a fallback; Fuzzy identity mapping; Date-aware prompting for temporal queries; Two-stage schema selection; Hybrid entry point, then structured queries; Webhook-driven ingest and re-embed
- Tools: MongoDB, Postgres (mentioned as a comparison with table definitions), GitHub, Linear, Jira, Slack, MCP, Levenshtein distance

## [RAG Needs a Map: Using GraphRAG to Retrieve Connected Context — Nyah Macklin, Neo4j](../videos/LJ2a9nX3vlo.md)
`LJ2a9nX3vlo` · AI Engineer · 2026-10-11 · q2 · intro · workshop · also: rag-retrieval, context-engineering

Neo4j workshop on GraphRAG: when vector RAG falls short (3+ hops, cross-document aggregation), how an LLM can build a knowledge graph, and how to pair vector search with Cypher in a Neo4j Aura agent.

- Techniques: Hybrid vector-plus-Cypher retrieval tool; Text-to-Cypher tool beside the search tool; Schema-pinned LLM entity extraction; Chunk, embed, extract, load pipeline; Direct Cypher audit after each rebuild; Grounding instruction to restrict the agent to graph content
- Tools: Neo4j, Neo4j Aura (free instance), Aura Agents, GraphAcademy, GraphRAG for Python (neo4j-graphrag), OpenAI (LLM and text-embedding-3-small), Cypher, GitHub Codespaces, VS Code

## [From 15% to 90% GPU Utilization: Fix the Data Pipeline, Not the Model](../videos/tNAV259UhCM.md)
`tNAV259UhCM` · AI Engineer · 2026-10-10 · q4 · practitioner · talk · also: training-finetuning-rl, infra-cost-scaling

Fixing a multimodal SFT data pipeline on Ray (concurrency, prefetch, zero-copy, scheduling) took GPU utilization from 15% to about 90%. The lesson: profile the data path, not the model.

- Techniques: Wait time ratio as the pipeline health metric; Async IO for object-store fetches, process pool for CPU preprocessing; Background prefetch queue; Pass object references instead of data; Spread scheduling and zero-copy retrieval at scale; Scaling-ladder ablation
- Tools: Ray, Ray actors, Ray object store, Megatron, Qwen3-VL (auto-caption reads as "QN3VL"), PIL, NumPy, Hugging Face Transformers tokenizers, pandas, S3, JSONL, asyncio

## [Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI](../videos/TyPpSRXGhbc.md)
`TyPpSRXGhbc` · AI Engineer · 2026-10-10 · q4 · practitioner · talk · also: training-finetuning-rl, evals

Snorkel AI and UC Berkeley Sky lab trained a 4B Qwen3 agent with RL for under $500 that beats its 235B variant on finance QA; simple binary rewards and single-table curricula won.

- Techniques: Multi-stage synthetic eval and training data pipeline; Company-level data split to prevent leakage; Binary reward with reference-based LLM judge; Single-table-first data mixture; Decorator-based RL wrapper for existing agents; Large concurrent rollout generation
- Tools: RLLM, GRPO, Qwen3 4B and 235B, GPT-5 nano (judge), FinQA benchmark, BFCL, EDGAR, H100

## [Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j](../videos/XPj3mIKEtI4.md)
`XPj3mIKEtI4` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · also: memory, skills-self-improvement

Neo4j PM Will Lyon argues agent memory should be a typed, traceable context graph, and shows how to distill that graph into governed, step-by-step agent skills rather than static markdown.

- Techniques: Typed context graph as agent memory; Decision traces as reasoning memory; Scope-first skill distillation; Coverage and coherence checks on generated skills; Staleness-aware skill registry; Typed step schema for skills (APE)
- Tools: Neo4j Agent Memory Service (NAMs), Neo4j graph database, Agent Skills open standard (agentskills.io), APE skill protocol, MCP tools, SkillsBench

## [Grep or Embeddings? Agentic Search Over Company Documents — George He, LlamaIndex](../videos/X4w2Pkz5tDY.md)
`X4w2Pkz5tDY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · also: rag-retrieval, context-engineering

George He (LlamaIndex) argues that agent document search should be a harness of primitives (list, grep, read by offset, semantic search, page screenshots) chosen by corpus scale, not a single RAG pipeline.

- Techniques: Agent retrieval harness with a small primitive set; Hybrid retrieval with weighted fusion and LLM rerank; Parse once, persist, and store page screenshots; Metadata tagging at ingest; Chunked reads with grep then offset and length; Evaluate parsers on table and layout fidelity
- Tools: LlamaIndex, LlamaParse, LightParse, Turbopuffer, Claude Code, grep, BM25, Textract, Tesseract, MCP, Google Drive, SharePoint

## [Why Building an Eval Platform Is Harder Than It Looks — Braintrust](../videos/mUQoVz7THu0.md)
`mUQoVz7THu0` · AI Engineer · 2026-10-07 · q2 · intro · talk · also: evals, observability

Braintrust's solutions lead on why eval platforms are a systems problem: a maturity path from spreadsheets to production-trace flywheels, plus why agent traces are hard to store and query.

- Techniques: Three-part minimal eval harness; Production-failure-to-test-case flywheel; Side-by-side experiment UI for prompt and model changes; Separate hot and cold paths for trace data; Natural-language headless eval runs via coding agents
- Tools: Braintrust, BTQL

## [From Raw Documents to AI-Ready Data — Leo Platzer & Jeff Koss](../videos/wzWNYDY7toc.md)
`wzWNYDY7toc` · AI Engineer · 2026-10-06 · q2 · intro · demo · also: rag-retrieval, governance-compliance

Vendor talk (DZ Labs, now Colibra) on turning millions of messy SharePoint documents into AI-ready data by tagging, deduplicating, freshness-filtering and scoping them before RAG.

- Techniques: Conditional tag tree with AI suggestions and human review; Dedupe and freshness pruning before indexing; Hybrid pattern plus LLM sensitive-data scan; Folder-level context index file; Scheduled data slices
- Tools: SharePoint, DZ Labs (DZ data curation platform, DZ SDK), Colibra, Claude Code, Codex, vector database, knowledge graph

## [Keyword Search Is Dying. Is Your Catalog Ready for AI Agents? — PayPal](../videos/YXb2Wx1r_Pk.md)
`YXb2Wx1r_Pk` · AI Engineer · 2026-10-05 · q2 · intro · talk · also: rag-retrieval, product-ux

PayPal's agentic-commerce director argues merchant catalogs were built for human search, not agents, and shows that enrichment helps semantic recommendations while over-enrichment and boilerplate hurt.

- Techniques: Catalog enrichment for semantic retrieval; Head-to-head baseline test of enriched vs unenriched records; Hybrid keyword plus semantic retrieval; Strip boilerplate from agent-facing text

## [Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI](../videos/FQwTqUmcbRg.md)
`FQwTqUmcbRg` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: training-finetuning-rl, infra-cost-scaling, inference-serving

Datology's CTO on running trillion-token synthetic pretraining data jobs: rephrase seeded documents, batch S3 metadata calls, checkpoint for GPU failures, schedule CPU and GPU pools atomically, and sweep vLLM flags.

- Techniques: Seed-based document rephrasing for synthetic pretraining data; Batched S3 metadata listing at maximum page size; Right-sized partitions with checkpointing and idempotent retries; Atomic CPU and GPU scheduling with dedicated pools; Grid search over vLLM and SGLang serving parameters for batch inference; One workflow for research and product in the same infrastructure
- Tools: Ray, KubeRay, vLLM, SGLang, Apache Spark, Kubernetes, Amazon EKS on HyperPod, Slurm, Amazon S3, Parquet, Beyond Web (DatologyAI synthetic data recipe), Nemotron Synth

## [Columnar Databases Are Incredibly Fast. Here's Why.](../videos/mR06J55fLvo.md)
`mR06J55fLvo` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: infra-cost-scaling, dev-tools

Better Stack compares Postgres, ClickHouse and DuckDB on 100M rows: columnar stores win big on aggregations, but lose on point lookups and single-row updates.

- Techniques: Split workloads by access pattern; Choose the ClickHouse sort key for the dominant filter; Insert in key order to make min/max skipping work; Avoid per-row updates on columnar stores; Benchmark with identical SQL on the same data
- Tools: PostgreSQL, ClickHouse (open-source server, shown as local server), DuckDB (embedded, single-file library)

## [Is it Possible to Run Any LLM in Jev Mode Using llama.cpp?](../videos/Oi4JPj58lUA.md)
`Oi4JPj58lUA` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving, local-ai, evals

Breakdown of "Jeff mode": llama.cpp constrained choice scoring is fast, but its confidence score comes from masking and renormalizing, needs calibration on your own data, and its speed depends on model architecture.

- Techniques: Forced-choice classification via cached-prompt branch scoring; Single-field logprob check on the stock server first; Calibrated confidence gate with escalation; Temperature scaling for post-hoc calibration; Group requests by schema to keep the prompt cache warm; Benchmark hygiene for local inference; Keep dependent fields in plain generation
- Tools: Jeff (TypeSafe structured-classification product, as captioned; the title spells it 'Jev mode'), llama.cpp, llama.cpp fork by Kodakus (parallel constrained decoding, two commits), llama.cpp stock server (n_probs / logprobs parameters), NotJeff (project reproducing the approach with stock llama.cpp, Qwen3-8B reported), Qwen 1.5B (plain attention, 28 layers), Qwen3-8B (captioned 'Quen38b'), Qwen 3.6 35B-A3B (captioned 'Quen 3.635BA3B', MoE), Gemma 4 12B (captioned 'Gemma 412b', sliding-window), Insider LLM 27B model (described as dense; config shows hybrid), Banking77 (public bank-intent dataset), Temperature scaling (calibration method)

## [Polars 2.0 Says 5× Faster... So What's Changed?](../videos/uHELj20WrOc.md)
`uHELj20WrOc` · Better Stack · 2026-10-02 · q3 · practitioner · news · also: dev-tools

Better Stack walks through the Polars 2.0 release candidate: mostly a cleanup release that makes the streaming engine the default, drops row-order guarantees, and removes old APIs with replacement-naming errors. The 5x speedup is unbenchmarked.

- Techniques: Pin row order explicitly; Pre-upgrade audit for unsorted group_bys; Error-driven migration on the RC; Schema check before execution; Hold back RC features that have open bugs
- Tools: Polars 2.0 release candidate (pre-release, installed with the pre flag), Polars Python API (LazyFrame, scan_csv, collect_schema, explain), Pandas, DuckDB, Dask, Spark, uv (uv pip install), Polars Cloud (not open source), polars Rust crate 0.55, Parquet, CSV

## [Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash](../videos/ACPEpji5NV4.md)
`ACPEpji5NV4` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: rag-retrieval, memory, evals

DoorDash's search and personalization lead on using LLMs offline to create graded relevance labels, semantic IDs, and memory, then serving those through small, fast models.

- Techniques: Offline LLM labeling with a distilled labeler; Label-audit by disagreement; Two-stage contrastive retrieval with hard-negative curriculum; Auxiliary ordinal relevance tower with value-function blend; Hierarchical learned semantic IDs as sparse features; Multi-form consumer memory blocks; Batch generation of personalized content with the existing ranking stack
- Tools: GPT-4o mini (named as an example lightweight labeler)

## [Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face](../videos/dKcTBQzR7jI.md)
`dKcTBQzR7jI` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: voice-multimodal, training-finetuning-rl, evals

Merve Noyan (Hugging Face) argues against running VLMs for real-time vision and shows a pipeline where VLMs label and judge data to train small Apache-2.0 detectors such as RF-DETR, plus a toolkit of models exposed as agent tools.

- Techniques: VLM as offline labeler, small detector at runtime; Overlay-and-ask judging; Ensemble of small judges with any-yes merge; License-first model selection; Agent with domain rules and human checkpoints; Models exposed as agent tools
- Tools: RF-DETR, Gemma 4 E4B, LFM2.5-VL, Qwen VLM (auto-caption reads 'Q1 3.5', ~3.5B), Falcon Perception, Moondream 3, MM Grounding DINO, SAM 3.1, Supervision (Roboflow), Hugging Face Jobs, Hugging Face Inference Providers, Hugging Face buckets

## [Robotics Has Been Stuck for 70 Years — Deepak Pathak, Skild AI](../videos/jFHteJjRl8A.md)
`jFHteJjRl8A` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: voice-multimodal, training-finetuning-rl, models-research

Deepak Pathak (Skild AI) argues robotics lacks internet-scale data, so the answer is one omnibodied brain pretrained on diverse data, post-trained on teleop, and improved by a deployment data flywheel.

- Techniques: Pretrain on diverse, scalable data, post-train on small high-quality teleop; Deployment data flywheel; End-to-end camera-to-motor policy with only a low-level PID loop; Learn from human video, then adapt with minimal robot data; Cross-embodiment zero-shot transfer

## [From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam](../videos/T72nqdC92PM.md)
`T72nqdC92PM` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: training-finetuning-rl, models-research, voice-multimodal

Sarvam's Krishna Prasad Srinivasan on training Servam Vision, a 3B state-space document-OCR model built from scratch for English and 22 Indian languages, using block-level OCR, a four-stage curriculum and RL with machine-checkable rewards.

- Techniques: Block-level OCR with layout and reading-order modules; Four-stage training curriculum for a domain VLM; RLVR with unit-test rewards; Real complex documents as RL reward sources, synthetic documents for SFT; Human-in-the-loop workbench with confidence scores and block grounding
- Tools: Servam Vision, Akshar (agentic document workbench), OlmOCR-Bench, OmniDocBench, Qwen, Gemma

## [Physical AI's Next Bottleneck Is Finding the Right Video — Rafael Levi, Bright Data](../videos/I_VEh7XSwyc.md)
`I_VEh7XSwyc` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: voice-multimodal

Rafael Levi (Bright Data) argues physical-AI training is limited by usable action data, not models, and pitches searching indexed public video by action before collecting it.

- Techniques: Action-based clip retrieval before collection; Frame-to-frame motion estimation from plain video; Descriptive queries for retrieval
- Tools: Bright Data video indexing API

## [You’re Not Thinking Big Enough: Rebuilding Food Systems with AI Agents — Cody Menefee, Firecrawl](../videos/ztlXKfPCT3Q.md)
`ztlXKfPCT3Q` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: context-engineering

Firecrawl growth engineer Cody Menefee argues LLM agents could help automate rotational grazing for livestock, with the LLM suggesting moves and a human confirming, plus a recruiting pitch for Firecrawl.

- Techniques: Human-confirmed LLM suggestions over multivariate data; Knowledge base from scattered web sources; Context gathering and packaging for LLM reasoning; Fixed reference object for remote measurement; Model the decision at several levels
- Tools: Firecrawl, OpenPasture, Halter, NoFence, Planet satellite imagery, trail camera

## [Building the Document Context Layer for AI Agents — Jerry Liu, LlamaIndex](../videos/RQi7x-navxU.md)
`RQi7x-navxU` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: rag-retrieval, context-engineering

Jerry Liu (LlamaIndex) argues agents need a document context layer: fast local parsing by default, VLM escalation for hard pages, and cost-aware routing between specialized and frontier models.

- Techniques: Fast-pass then escalate parsing; Hybrid pipeline plus VLM parsing with routing; Regime-based pipeline selection; Structured extraction with provenance and confidence gating; Multi-tool agent retrieval over documents; Accuracy-cost-latency Pareto benchmarking
- Tools: LlamaParse, LightParse, ParseBench, Claude Code, Claude Cowork, Codex, OpenClaw, MCP, BM25, grep, PyPDF, PyMuPDF

## [From Ingestion to Agents: How AI Teams Build on Document Intelligence — Adit Abraham, Reducto](../videos/0I07YAuF8xA.md)
`0I07YAuF8xA` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: rag-retrieval, agent-architecture, evals

Reducto's CEO on why document ingestion decides agent quality: decompose parsing into specialised tools, verify rather than regenerate, store table forms split by job, and eval every pipeline stage.

- Techniques: Decomposed parsing stack; Targeted verification instead of regeneration; Dual table representation; Classify and split before extraction; Agent harness for chart reconstruction; Parent-subagent validation criteria; Per-stage evals
- Tools: Reducto, Gemini, OpenAI models, Anthropic models, Cursor (as analogy for speculative edits), code interpreter

## [GTM Engineering: The Technical Bits — Everett Berry, Clay](../videos/UhCY231d0FQ.md)
`UhCY231d0FQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, multi-agent

Everett Berry (Clay) on the technical hard parts of GTM engineering: data waterfalling, graph-based orchestration, long-running per-account agents, and outbound execution limits.

- Techniques: Waterfall enrichment; Selective field refresh; Typed-node orchestration graph; Persistent per-entity agent with wake-up triggers; Field ownership split; Timed re-engagement cooldown; Multi-domain sending with reply routing; Cross-channel suppression
- Tools: Clay, Salesforce, Outreach, Slack, Smartlead, Forager

## [Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google](../videos/9R--1tg45Jg.md)
`9R--1tg45Jg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: security-guardrails, mcp-and-tools

Google's MCP Toolbox team on separating dev-time from production agent tools. Keep credentials, raw SQL and user identity out of agent control, and use predefined, identity-bound, read-only tools.

- Techniques: Source primitive for connection secrets; Predefined custom SQL tools; Read-only enforcement at the driver level; Blast-radius limits on sources; Bounded and authenticated parameters for identity; Read/write tool split with approval gates; Actionable, retryable tool errors and flat inputs
- Tools: MCP Toolbox for Databases, Google Managed MCP, Model Armor, EvalBench, LangChain, Gemini CLI, Claude Code

## [Your Agreements Are a Database You Can't Query — Hiral Shah, Docusign & Sean Sodha, NVIDIA](../videos/_gvamfT8H-w.md)
`_gvamfT8H-w` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: inference-serving, enterprise-adoption

DocuSign and NVIDIA on turning enterprise agreement PDFs into queryable data, using a small layout-aware table extraction VLM (Nemotron Parse) inside a hybrid OCR pipeline.

- Techniques: Purpose-built small table-extraction VLM; Hybrid two-route document pipeline; Offline-heavy vs online-light compute split; Structured export and API over extracted data; Benchmark on table extraction and track accuracy vs speed
- Tools: Nemotron Parse, Nemotron Retriever, NVIDIA NIM, vLLM, C-RADIO, NVFP4, FP8, Coupa

## [It’s Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners](../videos/xo68uCibfm8.md)
`xo68uCibfm8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: context-engineering, agent-architecture, multi-agent

Kevin Madura (AlixPartners) explains recursive language models (RLMs): the context lives as a variable in a Python REPL, and the model writes code and delegates subcalls to sub-LMs, so only useful results return to the main context.

- Techniques: REPL-held context with sub-LM delegation; Typed I/O shell around an autonomous core; Schema-enforced sub-LM handoff; Bounded self-terminating loop; Dataframes in the REPL instead of JSON tool results; Trace-driven harness optimization (Halo)
- Tools: DSPy, PredictRLM, fastRLM, AXE, Halo, Claude Code, GPT-5, Anthropic Workflows, pandas

## [AI in GTM at Notion — Flora Liu](../videos/L4I7WgiEquo.md)
`L4I7WgiEquo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, multi-agent, agent-architecture

Notion's GTM engineer explains a know/decide/act/learn system that unifies sales and self-serve signals, with humans and agents working in one shared context layer on durable workflows.

- Techniques: Four-layer know/decide/act/learn loop; Denormalized key-addressable profile plus keyed unstructured artifacts; Durable workflow per event with engine-managed retries; Parallel research subagents with score-and-select review loop; Single eligibility and routing classifier; Human approval gate by default, untrusted inbound input; Trace every LLM step and log decisions with outcome links
- Tools: Notion, Snowflake, DynamoDB, Temporal, Clay, Gong, Salesforce, Outreach, Nooks, ZoomInfo, Snowflake (product usage), Notion custom agents

## [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../videos/VjEP0xqTUI0.md)
`VjEP0xqTUI0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, agent-architecture, mcp-and-tools

Arman Vaziri (Ramp) on building go-to-market orchestration: an internal CDP, durable background agents on Temporal, scoped retrieval, and an MCP that turns employee experiments into productized use cases.

- Techniques: Durable thread with checkpointed activities; Account-scoped hybrid retrieval; Per-agent tool scoping with human pause and resume; System skills plus user text instructions; Nightly per-entity fan-out; Persist derived entity matches; Shared tool surface via MCP plus usage mining; Explore vs exploit with guardrails across channels
- Tools: Temporal, Postgres, Kafka, TurboPuffer, dbt, Snowflake, reverse ETL, MCP, GPT-3.5

## [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../videos/-tviRdpmHvs.md)
`-tviRdpmHvs` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: models-research, training-finetuning-rl

Krea's Sangwoo Lee on training the Krea 2 image model: data curation for stylistic diversity, cascaded dedup and classifier filters, and an LLM-style post-training pipeline with RL.

- Techniques: Cascaded dedup; VLM-judge distillation into a small classifier; SAE feature tagging for data hygiene; Two-pass captioning with OCR; Concept coverage via external importance ranking; Progressive resolution pretraining; Prompt expansion model
- Tools: Krea 2, pHash, MD5, SSCD, SigLIP, CLIP, sparse autoencoder, GRPO, OCR, VLM

## [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](../videos/Yphdry8ttAQ.md)
`Yphdry8ttAQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, evals, enterprise-adoption

A seven-step recipe for building vertical AI (finance, pharma) where domain experts in a learning loop, not LLM-as-judge, drive quality and proprietary data is the moat.

- Techniques: Narrow task decomposition; LLM workflow for unstructured-to-structured data curation; Observability traces as the first improvement loop; Domain expert as user in a learning loop; Post-training ladder; AI-in-the-loop reduction of expert time

## [5 Voice Agent Failure Modes You'll Hit in Week One — Venky B, Plivo](../videos/vblnYHzBgS4.md)
`vblnYHzBgS4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, inference-serving, evals

Venky B of Plivo lists five voice-agent failure modes seen in production (latency, transcription, data collection, TTS output, barge-in) and the fixes his team uses. Main takeaway: treat voice as a structured pipeline problem, not a prompt problem.

- Techniques: Per-stage latency budget with time-to-first-audio as the metric; Self-hosted small or MoE open model for the conversational LLM; Dynamic keyword boosting per call phase; LLM post-processing of STT output with domain context; Typed field schema with validation and confirmation for data collection; Field-level unit-test evals for voice agents; Normalization layer between LLM and TTS; Pronunciation smoke tests with known hard names
- Tools: LiveKit, Pipecat, Pydantic, Zod, Qwen 3.5, Gemma 4, Cerebras, Groq

## [Don’t be data poor — Anuj Iravane, Anterior](../videos/XAsb7MIAzm8.md)
`XAsb7MIAzm8` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, skills-self-improvement

Anuj Iravane (Anterior) explains how to generate synthetic medical records when real PHI cannot be kept, by sampling labels and policy reasoning traces first and generating documents backward.

- Techniques: Reverse-generation from sampled labels; Coarse-to-fine layered generation; Round-trip label verification; Cross-document consistency eval in a refinement loop; Skill files as the domain-expert interface
- Tools: internal agent harness (unnamed)

## [This New Postgres Feature Is Crazy Powerful](../videos/_0A2BnRYVCo.md)
`_0A2BnRYVCo` · Better Stack · 2026-09-02 · q3 · practitioner · news · also: dev-tools

Better Stack walks through the headline features of the upcoming Postgres 19 (beta 2): atomic insert-or-select, SQL property graphs over existing tables, REPACK CONCURRENTLY, plan pinning, and smaller changes.

- Techniques: Atomic get-or-create with ON CONFLICT DO SELECT; Declare a property graph over existing tables; Path-style graph query with explicit columns; REPACK CONCURRENTLY to reclaim disk space on large tables; Pin a known-good query plan with pg_plan_advice; Parallel index vacuum (opt-in)
- Tools: PostgreSQL 19 (beta 2), pg_plan_advice (spoken as 'pg plan advice'), PG Repack / pg_repack (extension, referenced as a previous workaround), VACUUM FULL, Neo4j, pg_durable (spoken as 'pg durable', linked for further reading)

## [Why AI Loves Em Dashes](../videos/SIVmsGkLCDU.md)
`SIVmsGkLCDU` · Kai Explains · 2026-09-02 · q3 · intro · other · also: models-research

Debunks the token-efficiency, RLHF-demographics and Medium theories for AI's em-dash habit; argues older print-book pretraining data fits the timeline. Opinion-led, with thin sourcing.

- Techniques: Per-word punctuation rate against a human baseline; Check token cost in context, not in isolation; Do not use one punctuation mark as an AI-text detector
- Tools: ChatGPT, GPT-3.5, GPT-4, GPT-4o, Claude Opus, Gemini, Medium

## [This 600M Model Fixes What Whisper Leaves Behind](../videos/jp0PGmAwK3w.md)
`jp0PGmAwK3w` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: local-ai, coding-agents

Super Whisper's open 600M-parameter S1 Mini cleans raw speech-to-text output (fillers, self-corrections, spoken numbers, emails) locally via GGUF and Ollama. English only, early software.

- Techniques: Post-ASR cleanup layer; Local GGUF serving with Ollama; Keep the cleanup model narrow and use a general LLM for everything else; Fully local dictation pipeline
- Tools: S1 Mini (Super Whisper, open 600M model), S1 Voice (Super Whisper, cloud ASR, not covered), S1 Language (Super Whisper, cloud, not covered), Whisper, Whisper.cpp, Parakeet, MLX Whisper, Ollama, llama.cpp, LM Studio, Hugging Face, GGUF

## [State of Data — Sean Cai, Independent / State of Data](../videos/ZyIoTOAbRfs.md)
`ZyIoTOAbRfs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, evals

Sean Cai argues data markets are the scarce input for turning generalist models into experts, and that single benchmark numbers and contrived expert-made data mislead buyers.

- Techniques: Three-axis verifiability scoring; Multi-harness, multi-infrastructure benchmarking; Per-criterion rubric analysis with deterministic checks plus LLM-as-judge; Long-horizon task checklist; Automatic post-training rerun on base-model swap; Lab spending as a leading indicator

## [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](../videos/Btk8wDUVs74.md)
`Btk8wDUVs74` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: memory, context-engineering, product-ux

monday.com's Omri Bruchim and Tomer Ast argue agents fail because they lack understanding, not data, and describe a two-speed "world model" of the user (slow learned profile plus fast live signals) built ahead of time.

- Techniques: Two-speed user model (slow profile + fast signals); Precompute meaning ahead of time, recompute a thin slice at serve time; Source isolation with fallback to last verified context; Urgency gating for proactive notifications
- Tools: monday.com Sidekick, Monday Vibe, Monday Agent, Monday Workflows, Slack, Claude, Gemini, GPT

## [The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside](../videos/KhYifX22yhE.md)
`KhYifX22yhE` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: training-finetuning-rl, models-research

Poolside's data and training leads on synthetic data at scale, the modular generation pipelines behind Laguna M.1 and XS.2, and the silent-corruption bugs (broken GPU, BF16 accumulation, FP8 kernel race) they found training Laguna S.

- Techniques: Modular six-part synthetic data pipeline; Seed-heavy cheap rephrasing; Staged decomposition of hard generation; Cross-domain porting and judge-evolver loops; Orchestrated agent queue (Hive); Cross-replica weight hash checks; FP32 accumulation for growing activations; Test recipes on a small model before scaling
- Tools: Hugging Face, DeepGEMM (FP8 kernels), Hive (poolside internal generation orchestrator)

## [The Base Model Is Dead — Varun Singh, Arcee AI](../videos/xbPriQWXtWM.md)
`xbPriQWXtWM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: training-finetuning-rl, models-research

Varun Singh (Arcee AI) argues base models have shifted from storing general web knowledge to priming RL for reasoning and agentic behavior, and explains the data-mix changes this requires.

- Techniques: Rephrase-based synthetic upsampling; Early injection of post-training-format data; Mid-training on post-training and long-context traces; Atomic-skill check before RL; Warm-up on test-time compute formats; Monitor MoE expert utilization under data shift
- Tools: Claude Code

## [When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain](../videos/bUJgirn4_yc.md)
`bUJgirn4_yc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, memory

DataChain's Dmitry Petrov argues coding agents need a "data harness" for physical and unstructured data (video, sensors), built on Pydantic schemas, incremental checkpoints and reusable derived datasets.

- Techniques: Pydantic schema as the only data model; Typed mapper and generator functions for parallel processing; Incremental runs with checkpoints; Check for an existing derived dataset before computing; Per-dataset knowledge note with lineage
- Tools: DataChain, Pydantic, Claude Code, YOLO, Ray, Spark, Dask, Git4Data

## [Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley](../videos/Sir59K8ZDPU.md)
`Sir59K8ZDPU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: agent-architecture, security-guardrails

Frank Coyle argues agents need ontologies as a symbolic validator around LLM tool loops, checking outputs against domain constraints before acting.

- Techniques: Validator gate after each tool call; Two-layer boundary checks (Pydantic plus ontology); Side-effect-free planning, then commit; OWL constraints for business rules; Reuse existing vocabularies; Bounding and monitoring agent loops
- Tools: Claude API (Python client, stop_reason tool-use loop), Pydantic, OWL, RDFS, schema.org, DBpedia, Dublin Core, FOAF

## [Ending AI Slop — Thais Castello Branco, Taste Labs](../videos/lCBf9slCanI.md)
`lCBf9slCanI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, training-finetuning-rl

Taste Labs founder argues subjective domains like design and writing can be made verifiable by decomposing quality into checkable parts, routing each part to the right judge, and using quality expert data.

- Techniques: Decompose fuzzy quality into codified components; Per-component routing of grading method; Ground-truth rules instead of similarity to a reference; Diverse expert pool with strict selection to counter mode collapse; Specificity and code-linkage QA on expert labels; Disagreement triage in expert consensus

## [AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j](../videos/kRkcNOsRyYg.md)
`kRkcNOsRyYg` · AI Engineer · 2026-08-18 · q3 · practitioner · workshop · also: rag-retrieval, context-engineering

Neo4j workshop on graph shapes for agents over a lakehouse: a metadata semantic layer over the warehouse, a deterministic document-tree-plus-links graph, and Leiden community "themes" built without LLM labels.

- Techniques: Metadata-only semantic layer graph; Deterministic document-structure graph; Hierarchical URI IDs for scoped search and traversal; Semantic query expansion for full-text search; Structure-only community themes; Spec-driven Cypher generation with a vendor skill; Agent with a database CLI for ad hoc graph reasoning; Partial re-sync of a deterministic graph
- Tools: Neo4j, Neo4j CLI, Cypher, Graph Data Science (GDS), NeoCarta, Neo4j Virtual Graph, Lucene full-text index, Leiden, Louvain (mentioned), Claude Code, Claude Opus 4.8 (model used in demo), BigQuery

## [From Tokens to Cells: Foundation Models for Single-Cell Biology - Akram Baharlouei, Altos Labs](../videos/-561cZmir5Q.md)
`-561cZmir5Q` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: models-research, evals

Altos Labs engineer on why single-cell foundation models (scGPT, Geneformer, PrimeFlow) struggle with noisy data, and why distribution-matching and data quality matter more than scale.

- Techniques: Cell-as-sentence masked modelling; Flow-matching distribution learning; Simple-baseline check before scaling; Distributional scoring with MMD
- Tools: scGPT, Geneformer, PrimeFlow, MMD

## [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face](../videos/lyL5QhgIOxc.md)
`lyL5QhgIOxc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: infra-cost-scaling, rag-retrieval


- Techniques: Insert-time search tokens in a denormalized read collection; Lucene-backed autocomplete instead of regex scans; Read-replica routing by consistency class; Hidden analytics replica; Two-layer autoscaling with event-driven pod scaling
- Tools: MongoDB Atlas, Atlas Search, Apache Lucene, Kubernetes, Horizontal Pod Autoscaler, KEDA, Cast.ai, AWS S3, AWS Redshift

## [Your Moat Is Your Data Model — Mike Phipps, Gates Foundation](../videos/jt1Pbr_n6oU.md)
`jt1Pbr_n6oU` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: mcp-and-tools, enterprise-adoption

Mike Phipps (Gates Foundation) explains why the Strategic Intelligence Platform's defensible asset is a knowledge graph of tacit process knowledge, served to agents through MCP rather than a custom chat UI.

- Techniques: Tacit-knowledge-first data modeling with data owners; Graph with explicit hierarchy types and precomputed roll-ups; Cross-system entity stitching; Document chunks as graph nodes with full-text plus graph retrieval; Curation pipeline before the graph; Expose the graph as an MCP server with state passthrough; Per-question graph-query ground truth plus stability checks
- Tools: Neo4j, MCP, Claude, ChatGPT, Cowork

## [Data Quality Is the Compute Multiplier — Ari Morcos, DatologyAI](../videos/_PdK6x7PQNM.md)
`_PdK6x7PQNM` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: training-finetuning-rl, models-research

Ari Morcos (Datology AI) argues data quality is an under-used compute multiplier, showing curated-data gains in VLMs, multilingual and legal models, and a small-budget frontier-scale run.

- Techniques: Four-C data pipeline (clean, curate, create, compose); Selective synthetic rephrasing into many formats; Domain mid-training with a representative mix; Small-run scaling check under token scarcity; Repeat high-quality data under token limits

## [How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh](../videos/1OMHGsUZiqA.md)
`1OMHGsUZiqA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: enterprise-adoption, product-ux

Vinoo Ganesh on running forward-deployed engineering as a product strategy: go on site, solve small problems fast, define shared terms, and avoid shipping hacks that become permanent.

- Techniques: Three-question discovery before building; Ship-it threshold for small problems; On-site workflow observation; Pain-signal scan; Canonical glossary and ontology; Production-readiness gate for quick fixes
- Tools: Palantir Foundry, Cassandra, Parquet, S3, Groovy, Elasticsearch, Snowflake, Databricks, Tableau, SAP, Slack

## [Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs](../videos/ewtOo0scUh0.md)
`ewtOo0scUh0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, sandboxing-execution

Bespoke Labs on curating data and RL environments for post-training: OpenThoughts and OpenThoughts-Agent recipes, counterintuitive sampling and teacher findings, and a tag-based SFT fix for numeric hallucinations.

- Techniques: Stage-wise ablation of a data curation pipeline; Multi-sample answers per question; Teacher model selection by measurement; Structural tags in fine-tuning data; Reflection-based prompt optimization
- Tools: Curator, Bespoke Stratos, OpenThoughts, Terminal-Bench, Tinker, Fireworks

## [How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh](../videos/Tt2kX2sgQio.md)
`Tt2kX2sgQio` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: governance-compliance, enterprise-adoption, agent-architecture

Kepler's CEO argues finance AI needs a deterministic substrate: the model points to sources and decides what to compute, while code extracts, checks and calculates numbers, with replayable derivation chains.

- Techniques: Atomic provenance ledger; Model decides, code computes; Derivation chains for derived metrics; Deterministic sanity gate on model output
- Tools: Claude, XBRL, ChatGPT, GLM 5.2, Opus 4.8

## [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](../videos/1UmZHb_E_SM.md)
`1UmZHb_E_SM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: infra-cost-scaling, rag-retrieval

Oxylabs' product manager on how public web data infrastructure feeds AI systems: how a video API, a sub-second SERP API and a 60k-rps scraper grew out of repeated client requests, latency cuts and load tests.

- Techniques: Iterate from client requests into an internal library; Narrow the response to what the AI consumer needs; Stage-by-stage latency audit; Realistic load testing with gradual ramp-up; Account for observability as load
- Tools: Oxylabs Fast Search API, headless browsers, proxy network

## [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j](../videos/VGN22pPpb-8.md)
`VGN22pPpb-8` · AI Engineer · 2026-08-18 · q2 · intro · keynote · also: memory, multi-agent

Neo4j keynote arguing that agents should be thin and share an ontology-based semantic layer over enterprise data, with execution traces that teach source selection over time.

- Techniques: Business-to-technical ontology mapping; Process graph for process-guided agents; Trace-derived source scores; Thin agents over a shared substrate
- Tools: Neo4j

## [Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft](../videos/o6U_2vd967Y.md)
`o6U_2vd967Y` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, multi-agent

Divakar Kumar shows how to add an agent tier for gray-zone fraud decisions in an event-sourced system, feeding agents a semantic read layer built from CDC and broker events.

- Techniques: Tier-2 escalation for gray-zone cases; Semantic layer built from CDC and broker events; Fan-out to specialist agents with a verdict agent; Saga-style orchestrator as the sole cross-context router; Hard cap on the agent reasoning loop; In-memory short-term agent memory under an SLA
- Tools: Azure Cosmos DB (event store and change feed), message broker (unnamed), CDC / change feed, rule-based engine, ML risk model (third-party)

## [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](../videos/3ySF0I5iE_0.md)
`3ySF0I5iE_0` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: rag-retrieval, context-engineering

Tim Ainge (Good Collective) on when graphs help AI apps: schema-first graph extraction, entity matching, and graph-native retrieval (personalized PageRank, shortest paths, subgraph pattern matching) for cheaper, more reliable results.

- Techniques: Schema-constrained graph extraction; Ontology normalisation instructions; Embedding-based entity resolution before node creation; Personalized PageRank from a seed node; Subgraph context retrieval via path queries; Subgraph pattern matching on code graphs
- Tools: Cypher (graph query language, ASR-garbled as 'cipher'), SQL (used as the comparison baseline), HippoRAG, Pinterest PixieRank (cited as the PPR reference), Embedding models, Structured outputs from an LLM, eShop (.NET reference codebase)

## [The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller](../videos/GgLQ02aO-hs.md)
`GgLQ02aO-hs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, agent-architecture

DSPy maintainers argue AI programs should be functions with fixed typed contracts, with the model, prompts and harness swappable underneath and optimized against evals.

- Techniques: Typed signature with natural-language instruction; Three-part task spec (instructions, code constraints, examples); Predict-then-reason fallback in code; Optimizer over a fixed metric; Learn a harness per function (DSPy.Flex, announced)
- Tools: DSPy, GEPA (transcript says JEPA; caption error, prompt optimizer from Berkeley), Recursive Language Models (RLM), MultiModule GRPO, BetterTogether, DSPy.Flex (announced for DSPy 4)

## [Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs](../videos/_cVfz88_j7A.md)
`_cVfz88_j7A` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, governance-compliance

Risa Labs (oncology) walks through automating prior-authorization workflows end to end, using confidence-gated multi-agent routing so only some orders skip human review.

- Techniques: Deterministic-first gating before LLM steps; Corroboration across independent sources before automating; Confidence-gated escalation to humans; Evidence-structured questionnaire answering; LLM-generated integration configs from a reusable action library; Self-healing loop for production automations
- Tools: RPA (robotic process automation, unnamed product), SQL database (unnamed), LLM (unnamed model) for extraction and config generation, Patient biomarker graph (internal, unnamed)

## [Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI](../videos/H7puB0RwJMM.md)
`H7puB0RwJMM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, governance-compliance

Daniel Chalef (Zep) on why LLM-built knowledge graphs need provenance modeled as a graph, covering lineage through merges, contradictions, tagging, and deletion.

- Techniques: Provenance as graph edges; Merge-safe lineage; Ingestion-time tagging with inheritance; Lineage-based deletion; Single-shot extraction plus deterministic dedupe
- Tools: Graphiti, Zep, Vector similarity search, Full-text search, BFS graph traversal

## [Build the AI GTM Agent That Knows the Buyer - Dr. Sajjan Kanukolanu, Position2 (Position Squared)](../videos/ltv-L5oMPIs.md)
`ltv-L5oMPIs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: enterprise-adoption, multi-agent

Position Squared's three-layer, multi-agent GTM system (anonymous visitor ID, knowledge-base-gated ICP and CRM matching, rep actions). Lessons: ICP drift, alert fatigue, weak identity accuracy, and approval friction.

- Techniques: Dedupe-then-enrich identification; Knowledge-base-gated ICP filter agent; Per-person context graph with account and deal rollup; Separate fit score from intent score; Personalized returning-visitor chat; Quarterly ICP refresh from closed outcomes; Alert budget tuned to rep capacity; Auditable, adjustable policy engine; One-click draft approval with a 30-second budget
- Tools: HubSpot, Slack, LinkedIn

## [SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)](../videos/KMR_RBoCa4M.md)
`KMR_RBoCa4M` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, enterprise-adoption

Nubank and Snowglobe claim simulated personas with mocked tools produce agent eval data on demand, cutting release cycles from weeks to hours, provided the sim-to-real gap is measured.

- Techniques: Simulated-user eval set generation; Persona-consistent grounding state; Sim pre-screening before A/B tests; Sim-to-real calibration; Same-harness model sweep
- Tools: Snowglobe SDK, LLM-as-judge, Automated prompt optimization (captioned 'JEPA', likely GEPA)

## [Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase](../videos/u1yaOeEX4e8.md)
`u1yaOeEX4e8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, infra-cost-scaling

JPMorgan payments lead on modeling each API request as a short-lived execution DAG, then using per-segment baselines and drift categories to detect anomalies with fewer false alarms.

- Techniques: Request-as-DAG from traces; Tiered detection; Segmented baselines; Drift classification before action; Async telemetry to hot and recon paths; Staged automated remediation; Synthetic training data for detectors
- Tools: OpenTelemetry, Kafka, Neo4j (mentioned as contrast), KL divergence, MMD, EWMA (exponential moving average)

## [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../videos/Ot4OPrPH4xY.md)
`Ot4OPrPH4xY` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: rag-retrieval, infra-cost-scaling

Bright Data's product lead argues that web data is becoming agent context, that repeated queries to paid context services get expensive, and that owning the data can beat renting it past a volume tipping point.

- Techniques: Field-by-field enrichment agent loop; Hybrid search plus direct scrapers; Basic heuristic entity merge; Break-even analysis for build vs rent; Self-healing scrapers
- Tools: Bright Data, Scraper Studio, Exa, Parallel, Tavily, New.com, Amazon AgentCore, Microsoft WebIQ, ZoomInfo / gtm.ai, SERP API, Claude native web search, Opus 4.8

## [Verifiable Environments for AI in Biology — Kenny Workman, LatchBio](../videos/3ZMUiFaQ3qg.md)
`3ZMUiFaQ3qg` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, models-research

LatchBio's CTO on building verifiable benchmarks for biology agents: DAG-decomposed spatial-omics evals, human verification of ambiguous tasks, rubrics for long-horizon work, and refusal testing.

- Techniques: Per-node verifiable eval specs; Human-verification pass over agent trajectories; Rubrics on invariant choke-point nodes; Paired routine and red-team refusal evals
- Tools: Python grader functions, SWE-bench-style task format, Claude models (named by the speaker as the models used for the evals)

## [Microsoft Built a New Charting Language for AI Agents](../videos/xFWhiWe91BE.md)
`xFWhiWe91BE` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: mcp-and-tools, dev-tools

Better Stack walks through Microsoft Research's Flint, a local MCP chart tool where the LLM writes about 10 lines of semantic JSON and a deterministic compiler emits Vega-Lite, ECharts or Chart.js specs; a research preview with no benchmarks yet.

- Techniques: Semantic spec plus deterministic compiler; Change the meaning, not the geometry; Local MCP chart rendering; Validate the IR, not the generated code
- Tools: Flint (Microsoft Research chart language and MCP server, v0.28), Vega-Lite, ECharts, Chart.js, Mermaid, Data Formulator (Microsoft analytics tool that uses Flint), Claude (Claude Code MCP client), Node 18 / TypeScript, npm

## [DuckDB is becoming unstoppable...](../videos/dKbV8MEzVPA.md)
`dKbV8MEzVPA` · Better Stack · 2026-08-02 · q3 · intro · review · also: dev-tools

A six-minute Better Stack walkthrough of DuckDB 1.4 and 1.5, separating their features, showing in-place Parquet queries, and stating where the single-machine analytics engine should not be used.

- Techniques: Query files in place from the DuckDB CLI; Single-statement upserts with MERGE INTO (DuckDB 1.4+); VARIANT column for messy semi-structured data (DuckDB 1.5+); Page-level AES-256 encryption with your own key
- Tools: DuckDB 1.4, DuckDB 1.5, SQLite, Pandas, Snowflake, Google BigQuery, Apache Parquet, Apache Iceberg, Apache Spark, Postgres, CSV, JSON

## [Git Can’t Handle Games… So Epic Built Lore](../videos/i66Bsnv12ZA.md)
`i66Bsnv12ZA` · Better Stack · 2026-08-02 · q3 · intro · review · also: dev-tools

Epic Games' Lore, a Rust, MIT-licensed, centralized-but-local-first version control system for large binary game assets; a walkthrough of its demo plus an honest take that it is pre-1.0 and benchmarks are unverified.

- Techniques: Run a local Lore demo server; Basic Lore workflow
- Tools: Lore (Epic Games, Rust, MIT license, pre-1.0), Git, Git LFS, Perforce, ZStandard, dd, Fortnite (mentioned as Epic's game)

## [AI Can Do the Work, But It Can't Do the Understanding | Better Stack Podcast Ep. 18](../videos/nfX_SQYDoBI.md)
`nfX_SQYDoBI` · Better Stack · 2026-08-02 · q3 · practitioner · interview · also: sandboxing-execution, token-cost-efficiency, enterprise-adoption

Better Stack podcast with Marimo's Vincent on why AI can produce code and analysis but not understanding: keep humans in the loop, care about the code, and be wary of hype.

- Techniques: Notebook scratchpad for LLM introspection; Incremental cell generation with a human in the loop; Scrubbable numeric literals for live tuning; Per-tool-call allow/deny for agent sandboxes; AnyWidget for browser-side widgets in Python notebooks; Shuffle test before trusting an A/B harness; Hypothesis-free first pass on a dataset; Supply-chain surface reduction for Python; Measure LLM agreement before automating a decision; Write flashcards yourself
- Tools: Marimo (Python notebook), Molab (Marimo notebooks with GPU), Google Colab, Jupyter, Observable, AnyWidget, Polars, NumPy, scikit-learn, spaCy, D3, Lua

## [Kimi K3 Fable 5 & GPT 5.6 Sol Killer, Inkling, Xiaomi Robotics U0, MobileWan, Needle & More AI News](../videos/sUamCGBjWkM.md)
`sUamCGBjWkM` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: models-research, local-ai, mcp-and-tools

Weekly AI news roundup (Aug 2026): Kimi K3 and Inkling open-weight releases, ACT2 and Xiaomi robot world models, on-phone 5B video diffusion, a 0.8B end-to-end OCR model, and a 26M function-calling model.

- Techniques: Self-driven fine-tuning loop for a behavioral constraint; Failure-driven single-example post-training loop; Chunk-wise recurrent attention for constant-memory long generation; Attention-only tiny router for tool selection; Long-horizon kernel-optimization evaluation
- Tools: Kimi K3 (Moonshot AI), Kimi Delta Attention, Kimi Code, Kimi Work, Kimi API, Claude Fable 5, GPT 5.6 Sol, Opus 4.8, GPT 5.5, Inkling, InklingSmall, OpenCode

## [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](../videos/Akm1sqvWG4A.md)
`Akm1sqvWG4A` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: rag-retrieval, observability, security-guardrails

Abed Matini (Ogilvy) shows a local, framework-free RAG FAQ bot: Docling to Markdown, structure-aware chunking, hybrid BM25 plus vector search fused with RRF, Python guardrails, and Langfuse telemetry.

- Techniques: Markdown-first ingestion with Docling; Per-document chunking strategy selection in admin; Q&A-shaped chunks for FAQ content; Hybrid retrieval with RRF fusion in Python; Deterministic functions instead of agent loops; Pre-LLM guardrail layer with rigid tests; Per-conversation telemetry with self-hosted Langfuse; Two-model local stack in Docker
- Tools: Docling, Python, FastAPI, React, PostgreSQL, Docker, Ollama, Qwen2.5, BGE-M3, Langfuse, GitHub Codespaces

## [AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent](../videos/Iwe_RY-fYgI.md)
`Iwe_RY-fYgI` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: governance-compliance, enterprise-adoption

Varsha Shah proposes a framework that correlates records across payroll, tax, procurement and finance systems with graph-based entity linking, adaptive risk scoring and jurisdiction normalization to catch compliance fraud that per-document checks miss.

- Techniques: Cross-document entity graph for compliance; Multi-signal risk scoring instead of single rules; Outcome feedback loop; Normalize before scoring across jurisdictions

## [Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon](../videos/LrGCT7G_rU8.md)
`LrGCT7G_rU8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: agent-architecture, security-guardrails, evals

Anna Marie Benzon presents a capstone ETL remediation agent: deterministic rules detect facts, tabular Q-learning picks among six bounded actions, and an external safety layer can force escalation. Results are from synthetic benchmarks.

- Techniques: Event-triggered diagnose-decide-act-verify loop; Rules for facts, learning for choices, guardrails for authority; Tabular Q-learning over a small discrete state; Propose, check, execute, and record separately; Multi-seed evaluation with baselines and confidence intervals
- Tools: AWS Glue, Amazon EventBridge, AWS Lambda, Amazon CloudWatch, AWS Glue Data Catalog, Amazon S3

## [Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra](../videos/EUsPvBeIx70.md)
`EUsPvBeIx70` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: rag-retrieval, agent-architecture, context-engineering

Phaidra engineers explain "semantic blindness": why RAG and LLM-only lookups fail on 400K+ equipment names, and how a hierarchy-based planner plus deterministic set-resolver stays accurate with flat cost at data-center scale.

- Techniques: Hierarchy summary as LLM context; LLM emits a structured search plan; deterministic resolver executes it; Pre-indexed subtrees for set operations; Two- or three-step planner/resolver pipeline in place of an agent loop; Pattern-based search for vague queries; Head-to-head eval against the old system at increasing scale; Move deterministic work out of the prompt

## [Structuring the Unstructured - Cedric Clyburn, Red Hat](../videos/-x5GEVnkuRw.md)
`-x5GEVnkuRw` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: rag-retrieval, mcp-and-tools, context-engineering

Red Hat's Cedric Clyburn demos Docling, an open-source local tool that converts messy PDFs into layout-aware Markdown, JSON, or Pydantic data, plus chunkless RAG over a document outline.

- Techniques: Layout-aware PDF to structured document conversion; Picture enrichment with a local vision-language model; Chunkless agentic RAG over a document outline; Schema-driven extraction from parsed documents; Document conversion as a microservice plus MCP tool; PII removal model before ingestion
- Tools: Docling, docling-serve, Docling MCP server, Pydantic, Ollama, Granite (IBM model), Qwen (via MLX), Jupyter, VS Code, Kubernetes, uvx

## [I Tried the Tool Trying to Kill Apache Airflow (Kestra)](../videos/b8-surdRWKo.md)
`b8-surdRWKo` · Better Stack · 2026-07-02 · q2 · intro · review · also: dev-tools

Quick tour of Kestra, a self-hosted, YAML-first workflow orchestrator pitched against Airflow: pipelines as config and live visual runs, but JVM memory cost, weak dynamic branching, and paywalled SSO.

- Techniques: Declarative flow: list of tasks plus a trigger (YAML); Run a local instance with one Docker command; Debug runs in the visual timeline and per-step logs
- Tools: Kestra, Apache Airflow, n8n, Zapier, Make, cron, Docker, Java / JVM, Python, Node.js, bash, SQL

## [Scrapling: The Web Scraper That Repairs Itself](../videos/q-uj7wk0LRI.md)
`q-uj7wk0LRI` · Better Stack · 2026-07-02 · q3 · intro · review · also: dev-tools, rag-retrieval

Walkthrough of Scrapling, a Python scraping framework whose adaptive parser relocates moved or renamed elements without rewriting selectors, plus its fetcher tiers and spider framework.

- Techniques: Adaptive selector recovery; Tiered fetcher selection; Grow a script into a spider
- Tools: Scrapling (about 53,000+ GitHub stars, per the presenter; no version stated), Python, Requests, Beautiful Soup, Playwright, Selenium, Scrapy

## [Dolt: This Makes SQL Feel Like Git](../videos/SDLfjrUyBw4.md)
`SDLfjrUyBw4` · Better Stack · 2026-07-02 · q3 · intro · tutorial · also: dev-tools

Quick walkthrough of Dolt, a MySQL-compatible SQL database with Git-style branch, diff, commit and merge on tables, plus where it sits relative to Git, DVC and LakeFS.

- Techniques: Clone a DoltHub database and make a versioned change; Branch, change, diff, merge on tables; Serve Dolt over the MySQL protocol for apps and BI tools
- Tools: Dolt (DoltHub getting-started database; CLI commands sql, diff, add, commit, branch, checkout, merge, log, status; SQL server mode), Git, DVC, LakeFS, MySQL-compatible clients, ORMs and BI tools (generic category, not a specific product)

## [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](../videos/iUWwcG-C8OU.md)
`iUWwcG-C8OU` · AI Engineer · 2026-06-18 · q4 · practitioner · demo · also: agent-architecture, context-engineering, enterprise-adoption

WorkOS product lead Garrett Galow demos Studio, an internal agent that answers business questions and turns repeat questions into live widgets. Main lessons: pre-flight checks, runtime tool context, query validation, and keeping the LLM out of widget refresh.

- Techniques: Generated declarative widgets; Pre-flight checks and clarifying questions; Runtime tool-context injection; Layered prompts; Distrust model priors for product facts; Execute-and-validate before deploy; Org-level connectors with role-based defaults
- Tools: Snowflake, Linear, Notion, Convex, LangGraph, Claude Opus, Slack bot, Retool, WorkOS Pipes

## [Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI](../videos/mFLlVpnGpds.md)
`mFLlVpnGpds` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, evals

Pyannote's Hervé Bredin explains why speaker diarization is still unsolved and why merging it with STT word timestamps is hard, with a live DER demo.

- Techniques: DER error breakdown; Benchmark in your own acoustic condition; Exclusive diarization in overlaps; Timestamp-based word-to-speaker alignment; Model-agnostic reconciliation layer
- Tools: pyannote (open-source diarization toolkit), pyannote metrics (DER evaluation), OpenAI Whisper, NVIDIA Parakeet, Hugging Face model hub, pyannoteAI cloud API

## [Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel](../videos/YYH0DMQr30A.md)
`YYH0DMQr30A` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: training-finetuning-rl, evals

Snorkel's Kobe Crawford argues that task quality is data quality for agentic terminal tasks, and shows that RL on verified high-quality tasks gives about 5x the uplift of low-quality ones.

- Techniques: Containerized task environments with a verification test gate; Accepted vs rejected task comparison; Failure taxonomy for benchmark runs; Controlled RL A/B on task quality; Rubric-based human and LLM-judge calibration; Make tasks verifiable on the back end
- Tools: Harbor Framework, Terminal-Bench, Claude Sonnet 4.5, Codex, GPT-5.2, GPT-5.1

## [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](../videos/btxGmN8RvNU.md)
`btxGmN8RvNU` · AI Engineer · 2026-06-18 · q2 · intro · review · also: mcp-and-tools, rag-retrieval

Bright Data pitch: blocked web access makes LLM agents fabricate answers silently. Its MCP (search, markdown scrape, CAPTCHA-solving browser) fixed a 5-site demo, but the evidence is one unreplicated run.

- Techniques: Paired with/without-tools comparison; Load a narrow subset of MCP tools; Scrape to markdown instead of HTML; Batch search across many keywords; LLM writes the parser, script does the extraction; Human-like remote browser instead of detection evasion; Restrict agents to public, non-login data; Pre-collected datasets for non-live needs
- Tools: Bright Data MCP (66 tools per speaker; 69 mentioned later), Bright Data scraping browser (remote, fingerprinted, CAPTCHA solving), Bright Data skills page, Bright Data datasets, GPT-5 (tested without tools as baseline), ChatGPT (cited for broken citations), Google, Bing and DuckDuckGo search (via MCP), Cloudflare bot blocking and AI Labyrinth (cited, not used), VS Code (demo environment)

## [From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](../videos/Bc6Ojl2XS1w.md)
`Bc6Ojl2XS1w` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: voice-multimodal, models-research

Google DeepMind's Thor Schaeff tours Gemini's audio stack: one-call structured audio extraction, director's-note TTS, a native speech-to-speech Live model, and a live tool call to Lyria music generation.

- Techniques: Single-call structured audio extraction; Director's-note TTS prompting; Realtime model with a generation tool; System-instruction persona on a live audio model; Install vendor API skills into coding agents
- Tools: Gemini API, Google AI Studio, Gemini 3 Flash Preview, Gemini 3.1 Flash Live, Gemini Live API (WebSocket), Lyria 3 / Lyria 3 Pro, Gemma 4, Veo 3.1 Lite, Gemini coding-agent skills

## [How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust](../videos/XBaznoTRDFI.md)
`XBaznoTRDFI` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: observability, evals

Braintrust's solutions lead argues agent observability differs from uptime-focused tracing: quality, non-determinism, huge text-heavy traces, and domain experts in the loop.

- Techniques: Split quality metrics from technical metrics; Full-text index on traces with SQL access; Trace to offline dataset to experiment; Human grades with justification to LLM judges; Embed and cluster traces to find unknown unknowns
- Tools: Braintrust, Grafana, Datadog, ClickHouse, Tantivy, Apache Lucene, SQL, CLI

## [Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j](../videos/B9h9ovW5H9U.md)
`B9h9ovW5H9U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: memory, rag-retrieval, context-engineering

Neo4j's Zach Blumenfeld on context graphs: why agents need stored decision traces and precedents, not just documents, plus a one-line scaffold (create-context-graph) and the Neo4j agent memory pipeline.

- Techniques: Hybrid precedent retrieval over decision traces; Scaffold a context-graph app from a domain; Staged entity extraction from text into a graph; Ontology-first graph schema generation; Separate memory stores by kind
- Tools: Neo4j, Neo4j agent memory package, Graph Data Science (GDS), Cypher, uvx create-context-graph, Pydantic AI, Claude, OpenAI embeddings, Next.js, spaCy, GLiNER, MCP

## [From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](../videos/zTZ0qunQXnM.md)
`zTZ0qunQXnM` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: coding-agents, mcp-and-tools, voice-multimodal

A Bright Data vendor demo arguing LLMs should write a reusable scraper once instead of parsing every page, then run and self-repair it on a schedule. Useful pattern, heavy product pitch.

- Techniques: Generate-then-run scraper; Scheduled self-repairing collection loop; Tiered fetch format; Remote browser with human-like input for multi-step flows; Public-data-only policy check
- Tools: Claude Code, Codex, Bright Data MCP, Bright Data scrape-as-markdown, Bright Data Web Unlocker API, Bright Data remote browsers, Bright Data skill docs on GitHub, Haiku

## [Nvidia's Huge releases | Claude Opus 4.8, Liquid AI, Microsoft Lens & More AI News](../videos/_Nh-wDT6Odc.md)
`_Nh-wDT6Odc` · Kai Explains · 2026-06-02 · q3 · intro · news · also: models-research, local-ai, inference-serving

Weekly Kai Explains roundup (June 2026) of open-model and tool releases: NVIDIA Locate Anything 3B and PID decoder, Sapient HRM-Text-1B, Step 3.7 Flash, NuExtract 3, Microsoft Lens, Claude Opus 4.8, and Perplexity's Rust tokenizer.

- Techniques: Parallel box decoding for detection and grounding; Trace inversion for distilling reasoning into a small model; Template-driven document extraction with a reasoning toggle; Dense re-captioning of training data; Tokenizer hot-path optimization; Local runs of open-weight models; Choosing Opus 4.8 effort per task
- Tools: NVIDIA Locate Anything 3B, Qwen2.5-3B, MoonViT, Qwen3-VL, Rex Omni, HRM-Text-1B (Sapient Intelligence), LFM (Liquid AI, transcript reads 'LFM 2.58'), Quopus 3.6, Qwen3.6-27B, NVIDIA PID (Pixel Diffusion Decoder), SeedVR2, Flux.1-Dev

## [The BEST AI Tool for Reliable Deterministic Outputs (Interfaze)](../videos/RQYkKpAFZ4c.md)
`RQYkKpAFZ4c` · Better Stack · 2026-06-02 · q2 · intro · review · also: models-research, evals

Hands-on review of Interfaze, a beta model that claims deterministic structured JSON via task-specific encoders; OCR tests on declassified UFO documents show mixed results, and the main claims are vendor-reported.

- Techniques: Dashboard system-prompt builder to code snippet; Guardrail smoke test before tuning; Shape pinning with a sample output; Confidence-colored bounding-box overlay for OCR
- Tools: Interfaze (beta model and dashboard), SOB (Structured Output Benchmark, vendor-published), Gemini 3 Flash (comparison model, vendor-reported), GPT 5.4 Mini (comparison model, vendor-reported), GPT-4 (mentioned as a generalist example), Gemini (mentioned as a generalist example), Host-built HTML bounding-box viewer (not named)

## [Why building eval platforms is hard — Phil Hetzel, Braintrust](../videos/_fQ7Z_Wfouk.md)
`_fQ7Z_Wfouk` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: evals, observability

Braintrust's Phil Hetzel on why eval platforms are a systems problem: the maturity path from spreadsheets to tracing plus online evals, and why agent traces break ordinary data stacks.

- Techniques: Spreadsheet plus for-loop eval starter; Playground for non-technical experimentation; Failure-mode-driven scoring functions; Online evals on the trace stream; Production-to-offline loop; Topic modeling over traces; Automatic tracing through an AI proxy or gateway
- Tools: Braintrust, Postgres, Neon, DuckDB, Google Sheets

## [Stop Rebuilding Backends… Just Use Directus](../videos/o9-tFFcAhXo.md)
`o9-tFFcAhXo` · Better Stack · 2026-05-02 · q3 · intro · review · also: dev-tools

Better Stack walkthrough of Directus, an open-source data platform that sits on top of an existing SQL database and adds APIs, permissions, an admin UI and flows, built in about 8 minutes from a blank install.

- Techniques: Rapid internal backend on an existing SQL database with Directus; Event-driven email notification with a Directus flow; Local testing of outbound email with Mailpit
- Tools: Directus, PostgreSQL, MySQL, Oracle Database, Docker Compose, Mailpit, Strapi, Payload, Hasura, n8n, Zapier

## [Microsoft Just Solved Document Ingestion for AI Devs (MarkItDown)](../videos/9ZaiZzp4XcY.md)
`9ZaiZzp4XcY` · Better Stack · 2026-05-02 · q2 · intro · tutorial · also: rag-retrieval, mcp-and-tools

Short intro to Microsoft's MarkItDown, an MIT-licensed Python tool and CLI that converts Office files, PDFs, images and audio into LLM-friendly Markdown, with a trade-off note against Pandoc, Unstructured and Docling.

- Techniques: Single-tool ingestion to Markdown (CLI); Python conversion with an LLM for images and charts; Pick the extractor by document difficulty
- Tools: MarkItDown, Pandoc, Unstructured, Docling, OpenAI Python client, Claude Desktop (transcript says 'Claw Desktop', auto-caption error), pip, MCP server (MarkItDown's)

## [The Fastest Python Scraper for RAG? (Crawl4AI)](../videos/BpsRH-1TZk4.md)
`BpsRH-1TZk4` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: rag-retrieval

Better Stack walkthrough of Crawl4AI, a Python crawler that returns clean Markdown/JSON for LLM pipelines, with prefetch mode, resumable deep crawls and schema-based LLM extraction; the "fastest" claim is stated but not measured on screen.

- Techniques: Basic async crawl to Markdown or JSON; Prefetch for link discovery, then selective extraction; Resumable BFS deep crawl; Schema-driven LLM extraction
- Tools: Crawl4AI, Playwright, Pydantic, Ollama, Scrapy, BeautifulSoup, Selenium, pip

## [SQLite is 138x Slower Than This?! (Testing Stoolap)](../videos/t6fbNGC_48c.md)
`t6fbNGC_48c` · Better Stack · 2026-03-02 · q3 · intro · review · also: dev-tools

Tests Stoolap, a Rust embedded analytics DB with a native Node.js binding: 4-6x faster than SQLite on COUNT DISTINCT, well short of the 138x headline, and the npm package was broken at the time.

- Techniques: Head-to-head embedded DB micro-benchmark; Second benchmark for DISTINCT with ORDER BY; Building an unpublished native-binding package from source; Why a native addon beats a socket bridge (napi-rs pattern)
- Tools: Stoolap (embedded Rust OLAP database, Node.js driver), SQLite, Node.js, Rust, napi-rs, Rayon, DuckDB (mentioned as analytics comparison), BigQuery (mentioned as analytics comparison), PostgreSQL (mentioned as OLTP comparison), npm

## [This Google Tool Turns Messy Text Into Clean Data](../videos/96P65wL2zmw.md)
`96P65wL2zmw` · Better Stack · 2026-02-02 · q2 · intro · tutorial · also: rag-retrieval

Short Better Stack overview of LangExtract, Google's free open-source Python library that uses LLMs to pull structured entities and relationships from messy text, with each extraction tied back to its exact source span.

- Techniques: Prompt-defined structured extraction without training data; Setup: clone repo, install requirements, keep the API key in .env; Span-grounded verification loop; Batch mode for large document sets
- Tools: LangExtract (Google open-source Python library, version not stated), Gemini API (Google), GPT (OpenAI models, named as a supported backend), Python, pip, Git, .env file for API keys, JSON output, Auto-generated interactive HTML viewer

## [China's Mind-Control AI Just Dropped on GitHub (100% Free)](../videos/8ear9y9qE7w.md)
`8ear9y9qE7w` · Better Stack · 2026-01-02 · q2 · intro · review · also: multi-agent, security-guardrails

Hype-titled walkthrough of BetterFish, a multi-agent public-opinion pipeline with parallel specialist agents and an LLM-moderated debate. The demo stalls before reports, and the speaker flags legal risks, so treat it as an architecture sketch.

- Techniques: Parallel specialist agents over a precomputed store; LLM-moderated agent debate before synthesis; Per-agent model routing through OpenRouter
- Tools: BetterFish, MindSpider (scraper), Flask, Playwright, MySQL, PostgreSQL, Docker, Hetzner CAX31, OpenRouter, Gemini 3, Kimi, DeepSeek

## [Building a One-Man Empire with AI & the Future of Developer Education | Better Stack Podcast Ep. 9](../videos/XG6ToBSg2HU.md)
`XG6ToBSg2HU` · Better Stack · 2026-01-02 · q3 · practitioner · interview · also: dev-tools, coding-agents, infra-cost-scaling

Better Stack podcast with solo developer David Flanagan (Raw Code Academy) on running a one-person, AI-assisted business: Cloudflare automation, LLM transcript correction, Kubernetes vs serverless cost trade-offs, QEnv and Dagger.

- Techniques: LLM-assisted transcript correction loop; Cron-driven content publishing on Cloudflare Workers; Spec-first delegation to coding agents; Hierarchical env with secret references (QEnv); Per-package CI definitions in a monorepo; Dagger pipelines in TypeScript; Cost-inflection planning for hosting; Reproducible machine via NixOS config
- Tools: Cloudflare Workers, Cloudflare R2, Cloudflare D1, Cloudflare service bindings, Gemini 3, Claude Code, Codex, Droid (multi-model agent CLI), Deepgram Nova 3, Whisper, ElevenLabs, Bluesky

## [SQL Used to Be Mandatory… But Not Anymore (Here’s the Shift)](../videos/nTRzoISgDpo.md)
`nTRzoISgDpo` · Better Stack · 2025-12-02 · q2 · intro · tutorial · also: dev-tools

Beginner tutorial arguing Python developers can skip raw SQL by using SQLModel, an ORM that combines SQLAlchemy and Pydantic, while still learning SQL basics.

- Techniques: Model-as-table with SQLModel; Object-based insert and fetch instead of raw SQL; Drop to raw SQL when needed
- Tools: SQLModel, SQLAlchemy, Pydantic, FastAPI

## [How AWS S3 Hit 1PB/s Using Hard Drives… This Is WILD!](../videos/J1vEUTe4gi0.md)
`J1vEUTe4gi0` · Better Stack · 2025-12-02 · q3 · intro · review · also: infra-cost-scaling

Explains how AWS S3 runs on hard drives at petabyte-per-second scale, using parallel erasure-coded reads, randomized placement, rebalancing and workload decorrelation to avoid hot drives.

- Techniques: Erasure-coded striping for parallel reads; Power of two random choices for placement; Proactive rebalancing by data age and new capacity; Workload aggregation to smooth bursts
- Tools: Amazon S3, Apache Kafka (referenced as an example of log-structured writes)

## [Zod 4 is AMAZING - Here's Everything New (and whats broken!)](../videos/ZBTc0W1lWss.md)
`ZBTc0W1lWss` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: dev-tools

Better Stack's 7-minute walkthrough of Zod 4: Zod Mini for tree-shaking, z.interface, top-level z.email, z.toJSONSchema, a unified error param, and the breaking changes to plan for.

- Techniques: Switch bundle-sensitive code to Zod Mini; Use z.interface for value-optional properties and recursive types; Migrate string formats to top-level functions; Attach metadata with .meta() and export JSON Schema with z.toJSONSchema; Replace old error customization with the unified error parameter; Update error-handling code for the new ZodError; Use z.overwrite for type-preserving transforms
- Tools: Zod 4, Zod Mini, Zod 3, TypeScript, RFC5322 email rule, HTML5 email rule, Gmail email rule

## [I Played DuckDB Doom And It's ACTUALLY Good](../videos/1Q_62NigzN8.md)
`1Q_62NigzN8` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

Better Stack demo of a Doom-like raycasting game whose 3D rendering runs entirely as DuckDB SQL queries in the browser (WASM); a stunt that shows how far an embedded analytical DB can be pushed, not a practical recipe.

- Techniques: Recursive CTE as a ray-march loop; Game state as tables, render as views; Timer-driven full-query refresh; Distance-based glyph shading; Embedded DuckDB WASM from a CDN
- Tools: DuckDB, DuckDB WASM, SQL, Node.js, ClickHouse, BigQuery, Docker Compose, Cursor (editor), CSS

## [Meta Just Changed Data Compression FOREVER (OpenZL Explained)](../videos/_BsjI3IUtlg.md)
`_BsjI3IUtlg` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools, infra-cost-scaling

Better Stack explainer of Meta's open-source OpenZL: format-aware compression with a per-format plan and one universal decoder. The claimed gains are on structured data, from a single Meta test.

- Techniques: Schema-first format description with SDDL; Offline plan training over reversible transforms; Evolve the compression plan without redeploying the decoder
- Tools: OpenZL (Meta, open source, no version stated), SDDL (Simple Data Description Language, OpenZL schema format), ZStandard (ZSTD, used as the fallback backend and as the speed baseline), GZip (named as a general-purpose baseline)

## [Poml: Microsoft's Secret Tool for PERFECT AI Prompts](../videos/tfOwh6YCY8M.md)
`tfOwh6YCY8M` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, coding-agents

Walkthrough of POML, Microsoft's open-source markup language for prompts, showing components, data embedding, templating, and a script that generates an AGENTS.md file.

- Techniques: Compile a POML file to an API-ready message list; Embed a spreadsheet as a prompt data component; Parameterize a prompt with templating and Python context; Generate an AGENTS.md from style documents with a cheap model; Run a compiled prompt through a non-interactive coding agent
- Tools: POML (Microsoft open-source prompt markup language), POML Python SDK, POML TypeScript SDK (said to be unstable at the time), POML VS Code extension, OpenAI Python SDK, GPT-5 mini, GPT-5 nano, Codex CLI (non-interactive), Claude Code, OpenCode, Gemini CLI, LangChain

## [MASTER Apache Kafka in just 8 minutes to Build Real-Time Apps](../videos/feKBnsvO2Pk.md)
`feKBnsvO2Pk` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools, infra-cost-scaling

Beginner Kafka tutorial: topics and pub/sub, disk-backed replayable events, brokers and KRaft, then a two-producer, two-consumer Python log demo run through Docker Compose and uv.

- Techniques: Local single-node Kafka via Docker Compose in KRaft mode; Minimal Python producer writing to a topic; Minimal Python consumer printing a topic; Replay a topic from the beginning; Run Python producers and consumers with uv in separate tabs
- Tools: Apache Kafka, Docker Compose, Python, uv, ZooKeeper (named as the replaced component), KRaft (Kafka Raft, Kafka's built-in metadata management), A Python Kafka client library (not named in the transcript), WebSockets (comparison only), Amazon SQS (comparison only), RabbitMQ (comparison only), Prometheus 3 (plug for another Better Stack video)

## [Why Everyone’s Talking About PostgreSQL 18](../videos/rlyIa7-ow-4.md)
`rlyIa7-ow-4` · Better Stack · 2025-11-02 · q2 · intro · news · also: dev-tools

A 4-minute Better Stack recap of PostgreSQL 18's headline changes: async I/O, skip scans, upgrade-preserved planner stats, virtual generated columns, OAuth 2, and replication and checksum defaults. It is a release-notes summary with no benchmarks or SQL shown.

- Techniques: Single-statement audit of updates via RETURNING old/new; Rely on virtual generated columns for derived fields; Skip-scan-aware index reuse; Major upgrade with preserved planner statistics
- Tools: PostgreSQL 18, pg_upgrade, EXPLAIN, SCRAM, OAuth 2

## [Is Kafka OUTDATED? Could RedPanda Be the Future of Event Streaming?](../videos/tHXWAkJeWmA.md)
`tHXWAkJeWmA` · Better Stack · 2025-11-02 · q2 · intro · review · also: infra-cost-scaling, dev-tools

Better Stack compares Kafka and Redpanda: Redpanda wins architecture and deployment, Kafka wins ecosystem and licensing, and performance depends on the workload, per conflicting benchmarks.

- Techniques: Test Kafka-compatible brokers with existing clients; Minimal Docker Compose deployment for comparison; Benchmark on your own workload with OpenMessaging Benchmark
- Tools: Apache Kafka, Redpanda, Redpanda Console, Redpanda Connect, Kafka Connect, Kafka Streams, MirrorMaker, ZooKeeper, Docker, Docker Compose, Kafka Python client, OpenMessaging Benchmark framework

## [Redis 8 Just Made Every Other Database Obsolete](../videos/b8yANadT0Y4.md)
`b8yANadT0Y4` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

Six-minute Redis 8 walkthrough of time-series downsampling and RedisJSON, using a sensor dashboard and a user-profile app. Command-level detail is useful; the title overclaims and no benchmarks are shown.

- Techniques: One raw time-series key per sensor with a retention window; Automatic downsampled series via a compaction rule; Pick the series and bucket size by requested time window; Store profile and history as JSON with per-field commands; Credentials as hashes and sessions in Redis; Local Redis for the demo
- Tools: Redis 8, RedisTimeSeries (TS.CREATE, TS.ADD, TS.RANGE, time-series rules), RedisJSON (JSON.SET, JSON.GET, array append, numeric increment), Redis hashes (HSET), Docker, Express.js, DuckDB (named as comparison), ClickHouse (named as comparison), MongoDB (named as comparison), Redis 7 (named as baseline)

## [Node.js Job Scheduling with Agenda | JSDOM web-scraping task](../videos/ZE_P7uXZm2c.md)
`ZE_P7uXZm2c` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools, observability

Tutorial on scheduling Node.js jobs with Agenda, MongoDB-backed persistence, priorities, one-off and cron schedules, a JSDOM Hacker News scraper, and Better Stack heartbeat alerts. Not AI-related.

- Techniques: Run MongoDB as the Agenda backing store in Docker; Minimal Agenda setup in an ES module; Graceful shutdown with cancel; Priority via define options; One-off and immediate runs; Dead-man heartbeat for scheduled jobs; Scraping Hacker News with fetch and JSDOM
- Tools: Agenda (npm agenda), MongoDB, mongosh (MongoDB Shell), Docker, Docker Hub (mongo image), Node.js, npm, JSDOM, Better Stack (heartbeats and incidents), VS Code, fetch (Node built-in), fs (Node built-in)

