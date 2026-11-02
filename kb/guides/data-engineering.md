# Guide: data-engineering

*Synthesized by Sonnet from 82 talks since 2026-05-18.*

Scope: pipelines, structured extraction, document parsing, data quality with LLMs, synthetic data, and the "context layer" that feeds agents. Many talks are vendor pitches (Reducto, LlamaIndex, Bright Data, Neo4j, TypeDef). Their numbers are self-reported. Treat them as directional.

## State of the art

The newest talks (Sept to Oct 2026) agree on one idea. The model is not the bottleneck. The data and context around it is.

- **Parse documents once, well, and keep the result.** PDFs are built for printing, not reading. Practitioners now run a cheap layout pass on everything. They call a VLM only on hard pages such as tables and charts. They store Markdown plus page screenshots (`X4w2Pkz5tDY`).
- **Do not let the model rewrite what it reads.** Targeted token-level corrections beat a free-form re-transcription, because the model "fixes" values to what it expects (`0I07YAuF8xA`). Sarvam trains OCR with machine-checkable rewards (`T72nqdC92PM`).
- **The LLM plans or labels. Code computes.** Examples: a planner emits a search plan and a resolver runs set operations (`EUsPvBeIx70`). A model writes a pointer to a number and code reads the value (`Tt2kX2sgQio`). Calculations live in tested code (`e9-br9hveRI`). The model chooses the work and code does it.
- **Structure is computed deterministically first.** Parse SQL and code to ASTs. Profile join keys. Use the LLM only for naming and leftover ambiguity (`KhRjivBSwiw`). Load already-structured documents into a graph with regex, no LLM (`kRkcNOsRyYg`).
- **Agentic retrieval over a few primitives.** Give the agent list, grep, read-by-offset, semantic search, and page images. Pick by corpus size. About 100 to 1,000 files can use local search. More needs an index (`X4w2Pkz5tDY`). Hybrid BM25 plus vector with RRF is the default (`Akm1sqvWG4A`, `gonAewBZxfU`).
- **Structured questions need a query engine, not RAG.** Sample documents to infer a schema. Validate generated queries in code. Inject tenant filters in code. Retry with the error fed back, with a cap (`spxoDAfh5ig`, `ORVh4GivEU0`).
- **Cheap models plus disagreement audits.** Run two cheap models from different families. Send only disagreements to a stronger model or a human (`Fa3hQVIKShw`).
- **Synthetic data is a pipeline, not a prompt loop.** Seed it, generate in layers, verify, overproduce, then filter hard (`qFaKvbVc5cE`, `KhYifX22yhE`, `XAsb7MIAzm8`).
- **Corpus hygiene before indexing.** Dedupe, drop stale files, tag, and scan for sensitive data (`wzWNYDY7toc`).

## Consensus patterns

1. **Layout-aware, hybrid parsing beats one-shot VLM parsing.** It is cheaper and hallucinates less on text-only pages. Small CPU layout models find structure. VLMs handle semantics. `RQi7x-navxU`, `0I07YAuF8xA`, `-x5GEVnkuRw`, `_gvamfT8H-w`.
2. **Keep structure in chunks.** Chunk by heading or section path. Never split a table. Flatten merged cells so each row stands alone. `Akm1sqvWG4A`, `gonAewBZxfU`, `0I07YAuF8xA`.
3. **Hybrid retrieval (BM25 plus vectors, fused with RRF) is the baseline.** One team saw hit rate rise from 92% to 97% on 63 questions. `gonAewBZxfU`, `Akm1sqvWG4A`, `X4w2Pkz5tDY`, `YXb2Wx1r_Pk`.
4. **Store a table in two forms.** Markdown or HTML for the reasoning model. A prose description for embedding retrieval. `0I07YAuF8xA`.
5. **Classify and split before extracting.** Route pages of a mixed packet to the right extractor. Do not dump everything into context. `0I07YAuF8xA`, `W4pnzOURwHQ`.
6. **Schema first for extraction and graphs.** Typed Pydantic schemas or pinned ontologies stop the model inventing node or field types. `3ySF0I5iE_0`, `LJ2a9nX3vlo`, `-x5GEVnkuRw`, `bUJgirn4_yc`.
7. **Provenance on every fact.** Return a citation and a confidence score. Hold back low-confidence values. Keep lineage as a graph so merges and deletes stay correct. `RQi7x-navxU`, `H7puB0RwJMM`, `Tt2kX2sgQio`, `BOWYujhIQuo`.
8. **Deterministic validators sit between the model and the world.** Allow-lists, ontology checks, and strip-if-untraceable gates. `Sir59K8ZDPU`, `Tt2kX2sgQio`, `spxoDAfh5ig`, `9R--1tg45Jg`.
9. **LLM as planner, code as executor, for large structured sets.** Do not feed the model huge lists of near-identical names. `EUsPvBeIx70`, `uKUA1a0Kdfc` (agents edit plain-JSON config, humans review).
10. **Verify at each stage of a layered pipeline.** Each layer is checked before the next consumes it. Eval every stage, not just the end. `W4pnzOURwHQ`, `0I07YAuF8xA`, `XAsb7MIAzm8`.
11. **Offline LLM labeling, then distill to a small model.** The LLM labels or judges offline. A small model serves. `ACPEpji5NV4`, `dKcTBQzR7jI`, `hacEQHHhu2Q`.
12. **Overproduce and filter for synthetic data.** Use judges plus cheap heuristics. Use real data for RL rewards and synthetic data for SFT. `qFaKvbVc5cE`, `T72nqdC92PM`, `KhYifX22yhE`. For cascaded dedup at billions of items, see `-tviRdpmHvs`.
13. **Generate code once instead of parsing every page with an LLM.** Run the script in bulk. Call the model only on failure. `zTZ0qunQXnM`.
14. **Precompute meaning offline, serve a thin slice live.** Fall back to the last verified context if a live check fails. `Btk8wDUVs74`.
15. **Fix the data pipeline before the model.** Profile the wait on data. GPU use went from about 15% to 90% on a multimodal SFT job. `tNAV259UhCM`.

## Disagreements & open questions

- **Vector index or no index?** Claude Code dropped its vector index for code. Company documents break that assumption (`X4w2Pkz5tDY`). Another talk uses no chunks and no embeddings, only a section outline the LLM navigates (`-x5GEVnkuRw`). Where the line sits is unsettled.
- **Graphs: essential or often wrong?** Neo4j talks push graphs for estate-level, multi-hop questions (`kRkcNOsRyYg`, `LJ2a9nX3vlo`, `XPj3mIKEtI4`). A practitioner warns graphs are often the wrong tool and projects stall after early letdown (`3ySF0I5iE_0`). Vendor bias is strong here.
- **One universal ontology or just-in-time ones?** The Gates Foundation builds a durable knowledge graph as its moat (`jt1Pbr_n6oU`). Southbridge says there is no universal schema and builds per decision (`Fa3hQVIKShw`). Neo4j wants a shared governed ontology (`VGN22pPpb-8`).
- **How much determinism?** TypeDef found agents still defaulted to grep even with graph tools, and a graph agent was about 2x more consistent over five runs, while pass@5 was close with grep slightly ahead (`KhRjivBSwiw`). Tool shaping and adoption measurement matter as much as the graph.
- **Can LLM judges be trusted?** Calibrate them against expert answers first (`W4pnzOURwHQ`). In domains with no answer key, they fail (`Yphdry8ttAQ`, `lCBf9slCanI`). Kepler rejects voting across LLMs entirely (`Tt2kX2sgQio`).
- **Over-enrichment.** Enriching catalog data helps until it dilutes the signal. Over-enriched catalogs made agents hallucinate more (`YXb2Wx1r_Pk`).
- **Reward design.** A simple binary reward beat an engineered rubric for a finance agent (`TyPpSRXGhbc`). Long-horizon biology tasks need rubrics (`3ZMUiFaQ3qg`).
- **Build vs rent web context.** The break-even depends on query volume (`Ot4OPrPH4xY`). The source is a scraping vendor.
- **Open:** how to measure sim-to-real gaps (`KMR_RBoCa4M`), how to keep graph lineage affordable (`H7puB0RwJMM`), how fast benchmarks go stale (`W4pnzOURwHQ`).

## How thinking changed over time

- **2026-05 to 06:** Focus on observability and eval data shape. Agent traces are huge and text-heavy, with spans of 10 to 20 MB. Ordinary stores struggle (`_fQ7Z_Wfouk`, `XBaznoTRDFI`). Pipelines "that build themselves" appear as scrapers (`zTZ0qunQXnM`). Data quality is framed as task quality for RL (`YYH0DMQr30A`).
- **2026-07:** Hybrid RAG with local parsing becomes the practical default (`Akm1sqvWG4A`, `-x5GEVnkuRw`). Semantic blindness shows that LLMs fail at scale on exact sets, so planner plus resolver appears (`EUsPvBeIx70`). Cross-document fraud graphs are proposed (`Iwe_RY-fYgI`).
- **2026-08-18 (big batch):** Graph, ontology, and "context layer" language dominates (`VGN22pPpb-8`, `kRkcNOsRyYg`, `Btk8wDUVs74`). The deterministic substrate idea matures (`Tt2kX2sgQio`). Synthetic data and data curation for pretraining and post-training get attention (`KhYifX22yhE`, `_PdK6x7PQNM`, `ewtOo0scUh0`, `xbPriQWXtWM`).
- **2026-09:** Documents become "the context layer" for agents. Parsing is decomposed, cost-routed, and benchmarked (`RQi7x-navxU`, `0I07YAuF8xA`, `_gvamfT8H-w`). Reverse generation of synthetic records appears (`XAsb7MIAzm8`).
- **2026-10:** Agentic search harnesses replace fixed RAG pipelines (`X4w2Pkz5tDY`, `gonAewBZxfU`). Structured data gets the same treatment, with schema-aware query engines and retry loops (`spxoDAfh5ig`). Context graphs are computed deterministically (`KhRjivBSwiw`). Cheap-model pipelines with cross-family audits arrive (`Fa3hQVIKShw`). Trust is built per field, with source precedence and human QA (`BOWYujhIQuo`, `e9-br9hveRI`).

## Numbers worth remembering

- Entity resolution: Ohio campaign-finance job went from about $10,000 projected to $795 actual. A cheap reasoning model matched a frontier model at about 2% of the cost. Checking cost about 4x the first pass. `Fa3hQVIKShw`.
- Planner plus resolver: old LLM lookup fell from about 80% (64 GPUs) to about 30% (460,000 GPUs). New approach had 100% on all tests, and about 9,000 tokens per query. `EUsPvBeIx70`.
- Hybrid RRF raised retrieval hit rate from 92% to 97% on 63 questions, about 270 PDFs. `gonAewBZxfU`.
- Local search is fine for about 100 to 1,000 files. `X4w2Pkz5tDY`.
- 30% stale or duplicate files can fill up to 80% of agent context (vendor eval). Pilot on 40 files, production 80,000+. `wzWNYDY7toc`.
- Data-pipeline fix: GPU use about 15% to 90%. Baseline waited about 85% of the time on data. Batch of 256 took over 100 s to fetch against a 15 to 20 s step. `tNAV259UhCM`.
- Context layer on data and code tasks: about 35 points higher task success (vendor benchmark). A grain change inflated a total about 4x. `KhRjivBSwiw`.
- Fine-tuned extraction at 94% was called not good enough for finance. `Tt2kX2sgQio`.
- RL on verified tasks gave about +6% uplift against +1% for low-quality tasks. `YYH0DMQr30A`.
- 4B Qwen3 agent trained for under $500 beat the 235B variant (about 60% vs 51%). `TyPpSRXGhbc`.
- Python UI representation about 70% smaller than JSON when streamed. `Krzs8GeiWTc`.
- Precomputed context bundle: $1.29 vs up to $2.60 on one task (anecdote). `ORVh4GivEU0`.
- Agent traces can reach hundreds of MB per interaction. `mUQoVz7THu0`, `XBaznoTRDFI`.
- Overproduce-and-filter: 50,000 seeds to 7,000 SFT records. `qFaKvbVc5cE`.
- Text-search latency: about 4 s scraper cut to about 650 ms P90 by narrowing the output. `1UmZHb_E_SM`.
- Docling-style CPU extraction claimed about 50x cheaper than VLM or naive OCR. `-x5GEVnkuRw`.
- Rule detector for ETL failures: precision 1.0, recall 0.8, on a synthetic benchmark. `LrGCT7G_rU8`.

## From creator channels (Kai Explains, AI LABS, Better Stack)

Scope: 36 creator notes that touch data work. No AI LABS video is in this set, so this section covers Kai Explains and Better Stack only. Most creator videos are short intros or vendor-led reviews. Their numbers come from one run or from the vendor. Most claims below rest on a single creator video. Those are marked.

### Practical playbook

1. **Pin row order before a Polars 2.0 upgrade.** Pass `maintain_order=True` to joins, group_bys and pivots whose output order matters. Grep for `group_by` calls with no sort after them. Check the plan with `explain()` on the lazy query. (`uHELj20WrOc`, single creator. The 5x speedup is unbenchmarked.)
2. **Migrate by following the errors on the release candidate.** Run existing code on the pre-release. Apply the replacement each error names: `melt` to `unpivot`, `read_csv` to `scan_csv().collect()`, `join nulls` to `nulls_equal`. Call `collect_schema()` to catch type errors before rows are read. Hold `group_by_dynamic` until the open streaming bugs settle. (`uHELj20WrOc`)
3. **Split storage by access pattern.** Keep Postgres for point lookups and frequent small updates. Send wide GROUP BY and COUNT DISTINCT scans to a columnar store. The creator's GROUP BY over 100M rows took 9.7 s on Postgres, 0.28 s on ClickHouse and 0.24 s on DuckDB. That is one dataset, one machine and one run each. (`mR06J55fLvo`)
4. **Put the most common range filter first in a ClickHouse sort key.** The sort key is the only index. Expect block skipping on the leading column and full scans on the rest. The creator's ID lookup took 168 ms on ClickHouse and 2 ms on Postgres. (`mR06J55fLvo`)
5. **Insert in key order, and batch changes on columnar stores.** Min/max skipping only works when rows arrive sorted by the filter key. A single-row update took 5.8 s on ClickHouse and tens of ms on DuckDB. Batch corrections, or append new rows instead. (`mR06J55fLvo`)
6. **Test a forced-choice classifier on the stock server first.** For one yes/no or single-label field, request token probabilities (the `n_probs` or logprobs option). Then renormalize over the allowed labels yourself. Warm up before you time anything. The creator saw cold picks take about 2 s. (`Oi4JPj58lUA`)
7. **Do not gate on raw confidence.** Label a few hundred of your own examples. Bucket predictions by confidence. Choose each cut where the bucket reaches your target accuracy, and track the escalation rate. In the creator's 47-item test, a 0.8 gate sent 62% of items to the bigger model. Fit a temperature on held-out data to fix overconfidence. (`Oi4JPj58lUA`, single creator and a small test. The temperature result is the vendor's own benchmark.)
8. **Read the model config before you trust a speed number.** Check the layer types in config.json. A model labelled dense can be hybrid. In the creator's tests, batched branches lost their speedup on hybrid and MoE models. (`Oi4JPj58lUA`)
9. **Convert every input to Markdown with one tool first.** Install MarkItDown with pip and run its CLI on the file. The caption shows `markitdown doc.pdf -o output.md`, but the `-o` flag is inferred from captions, so check the README. Move to Docling or Unstructured for messy scans and dense tables. (`9ZaiZzp4XcY`, intro-level, no extraction benchmarks.)
10. **Budget one extra LLM call per image.** MarkItDown can describe a chart PNG when you wire in an OpenAI client. Use this only for pages with no usable text layer. (`9ZaiZzp4XcY`)
11. **Make every extracted field point back to its source.** LangExtract ties each field to a source span and writes an HTML view. Click an entity to check its highlight in the text. Keep the API key in `.env`, not in the script. (`96P65wL2zmw`, 4-minute demo with no accuracy or cost numbers.)
12. **Overlay OCR boxes on the page to debug them.** Interfaze returns per-box coordinates and confidence. The host drew the boxes on the page and colored them by threshold (green above 70). Results were mixed on faded pages. (`RQYkKpAFZ4c`, one host's hands-on test, not a benchmark.)
13. **Get or create atomically in Postgres.** Insert with ON CONFLICT on the unique column, then DO SELECT RETURNING the columns you need. Use the FOR UPDATE form if you will modify the row. This is a Postgres 19 beta feature. (`_0A2BnRYVCo`)

### Tools creators recommend (tool — what for — `video_id`)

- DuckDB — embedded analytics, querying Parquet, CSV or JSON in place. MERGE INTO arrives in 1.4 and VARIANT in 1.5. — `dKbV8MEzVPA`. Benchmark in `mR06J55fLvo`.
- ClickHouse — server-side columnar store for wide aggregations. Tune the sort key for your main filter. — `mR06J55fLvo`
- Polars 2.0 RC — streaming engine as the default. Check row order and migrate removed APIs. — `uHELj20WrOc`
- llama.cpp stock server logprobs, then the constrained-choice fork — forced-choice classification with a confidence score. — `Oi4JPj58lUA`
- MarkItDown — one-tool ingestion from Office files and PDFs to Markdown (MIT). — `9ZaiZzp4XcY`
- LangExtract — prompt-defined extraction with span grounding and an HTML review view. — `96P65wL2zmw`
- Crawl4AI — async crawl to Markdown or JSON, with prefetch and resumable deep crawls. — `BpsRH-1TZk4`
- Scrapling — adaptive selectors that survive markup changes, plus tiered fetchers. — `q-uj7wk0LRI`
- Dolt — Git-style branch, diff and merge on tables. — `SDLfjrUyBw4`
- Kestra — YAML-first workflow orchestrator. The creator flags JVM memory (about 4 GB) and a paywalled SSO. — `b8-surdRWKo` (company figures unverified)
- Interfaze — structured-output model with OCR bounding boxes. Beta; its claims are vendor-reported, and the OCR test was one host's hands-on run. — `RQYkKpAFZ4c`

### Where creators agree or clash with the conference talks

- **Agree: fix ingestion first.** The MarkItDown and LangExtract videos make the same case as the guide's "parse once, well" point. Both are intro-level. (`9ZaiZzp4XcY`, `96P65wL2zmw`)
- **Agree: provenance on every field.** LangExtract's span grounding is the same idea as the guide's provenance pattern. This rests on one short demo. (`96P65wL2zmw`)
- **Agree: calibrate before you trust a score.** The guide says to calibrate LLM judges on expert answers. The Kai test shows the same for confidence gates, and puts a number on the cost of a bad gate. (`Oi4JPj58lUA`)
- **Agree on the escalation warning.** The guide's cheap-model numbers show that checking can cost several times the first pass. The Kai gate test shows the same risk from the other side. (`Oi4JPj58lUA`)
- **Clash: where determinism lives.** Interfaze says structured output is built into how the model works. The guide puts deterministic validators outside the model. Interfaze's claims are vendor-reported, and its own OCR test was mixed. (`RQYkKpAFZ4c`)
- **Gap: storage choice.** The guide covers retrieval and extraction. It does not cover OLAP or columnar engines. The creator notes add a view of which store fits which query, from one run on one machine. (`mR06J55fLvo`)
- **Gap: orchestration.** Creator content on schedules and YAML flows (Kestra) has no counterpart in the guide. This rests on one short Better Stack review. (`b8-surdRWKo`)

### Watch first (3-6 `video_id` — why)

1. `mR06J55fLvo` — the clearest picture of why columnar stores are fast and where they fail. One run, but the mechanism is sound.
2. `Oi4JPj58lUA` — the most measured creator test here: speed, calibration and escalation cost, with caveats. Small sample.
3. `uHELj20WrOc` — concrete upgrade hazards for Polars 2.0, including silent row-order changes.
4. `9ZaiZzp4XcY` — a short ingestion baseline with a fair list of limits. Intro-level, no benchmarks.

## Watch first

1. `Fa3hQVIKShw` — Best account of cheap-model entity resolution at scale, with budgets, disagreement audits, and a failure surface.
2. `EUsPvBeIx70` — Clear, measured proof that LLMs should plan and code should resolve on big structured sets.
3. `0I07YAuF8xA` — Most practical document-parsing talk: layered tools, token-level fixes, dual table forms, stage evals.
4. `KhRjivBSwiw` — Deterministic context graph for data and code agents, plus honest eval lessons on tool adoption.
5. `spxoDAfh5ig` — Build a schema-aware query engine with validation and a retry loop, end to end.
6. `Tt2kX2sgQio` — Atomic provenance and derivation chains. A model for trustworthy numbers.
7. `X4w2Pkz5tDY` — Agentic search harness and when each retrieval method fits.
8. `tNAV259UhCM` — Concrete data-path profiling and fixes with real utilization numbers.

## Implications for our projects

**AgentOS MemoryMesh**
- Adopt hybrid BM25 plus pgvector with RRF as the default. It is already your plan, and `gonAewBZxfU` and `Akm1sqvWG4A` show the lift.
- Chunk by section path. Keep tables whole. Store a prose twin of each table for embedding (`0I07YAuF8xA`, `gonAewBZxfU`).
- Treat provenance as a graph. Union source links on merge. Invalidate contradicted facts with a timestamp instead of deleting. Delete a derived fact only when no source remains (`H7puB0RwJMM`). This fits your conflict-resolution and provenance goals.
- Expose a small retrieval primitive set (list, grep, offset read, semantic search) to agents, and benchmark it against pure RAG (`X4w2Pkz5tDY`).
- Build a pre-index dedupe and freshness pass. Run it before embedding (`wzWNYDY7toc`).
- Reverse-generate synthetic eval data for RAGAS: sample the label first, then the document (`XAsb7MIAzm8`, `qFaKvbVc5cE`).

**AgentOS storage and Crucible**
- For the per-tenant DuckDB read tier, copy PlanetScale-style separation: a read copy with pre-computed tokens, plus a hidden analytics replica for heavy queries (`lyL5QhgIOxc`, `uKUA1a0Kdfc`).
- Use deny-by-default validation and code-injected tenant filters for any NL-to-SQL gate (`spxoDAfh5ig`, `9R--1tg45Jg`).
- Use Pydantic plus ontology gates after tool calls in the exec-gate guardrails (`Sir59K8ZDPU`).

- Agent traces are large and text-heavy. Split hot ingest from cold aggregation. Keep big payloads apart from small telemetry rows. Add full-text indexing for word search (`mUQoVz7THu0`, `XBaznoTRDFI`, `_fQ7Z_Wfouk`).
- Apply a stage-by-stage latency audit and a gradual ramp load test (`1UmZHb_E_SM`).

- Use a business-to-technical mapping and trace-derived source scores for catalogue discovery (`VGN22pPpb-8`). Compute structure deterministically first and use the LLM only for naming and summaries (`KhRjivBSwiw`). Precompute roll-ups (`jt1Pbr_n6oU`).

**SkillForge / EvolveCraft**
- Distill skills in scope-first, mostly deterministic stages. Check coverage and coherence of each skill (`XPj3mIKEtI4`). This speaks directly to your skill-worthiness question.
- Record per-step outcomes to score sources and skills (`VGN22pPpb-8`).

**ProsHarness**
- Use a durable workflow with each model and tool call as a checkpointed activity (`VjEP0xqTUI0`, `L4I7WgiEquo`). It matches your checkpoint and resume design.
- Use the propose, check, execute, record split for approvals, and log what was not executed (`LrGCT7G_rU8`).
- Use a task spec of instruction, code constraints, and examples around any cheap-model call (`GgLQ02aO-hs`).

**Entity resolution and Haiku pipelines**
- Run two cheap models of different families. Accept agreements. Escalate disagreements. Sample-check the agreed set. Fix question wording before touching thresholds (`Fa3hQVIKShw`).
- Fuzzy-match first and use the LLM only as tiebreaker. Embed-and-threshold before creating a new entity (`ORVh4GivEU0`, `3ySF0I5iE_0`).
- Set the checking budget before the run. Expect checking to cost several times the first pass (`Fa3hQVIKShw`).
- Calibrate any LLM judge against expert-verified answers (`W4pnzOURwHQ`).
