# Guide: memory

*Synthesized by Sonnet from 54 talks since 2026-05-18.*

Scope: long-term and cross-session agent memory, knowledge graphs for agents, and the "context layer" ideas around them. Many talks are vendor pitches (Neo4j, Oracle, Qdrant, Pinecone, Unblocked). Treat their numbers as claims.

## State of the art

What practitioners do now, newest talks first.

- **Memory is a loop, not a store.** Write, manage, read, evaluate, govern. The storage backend matters less than the policy for what gets written and recalled (`R3-anFK1YM8`, `BIhiYL4U9_M`, `apyrzaWj0Z4`).
- **Memory is typed.** The common split is short-term (the context window), then long-term as episodic, semantic and procedural. Each type gets a store and lookup that fits it (`BIhiYL4U9_M`, `jA_x7F8caHI`, `xs-ob87TTzg`, `KtBivPzmOM8`).
- **Consumer products moved from RAG to a running profile.** A background job re-writes one compact profile every day or few days. The profile goes into every chat. Search tools over past chats cover the rest (`5ZGyKWjQDr0`).
- **"Dreaming" is the default offline step.** A nightly or scheduled pass replays traces, merges, flags contradictions, prunes stale items and distils skills. Anthropic ships it in Managed Agents. Its own speaker says you still need your own evals to gate the result (`qJtcEDc_WJU`, `9QebvrrY3KY`, `jtzh-GBXBWc`, `xLUQOqjudtA`).
- **Memory shifts from facts to procedures and outcomes.** Store "when X, check Y" rules. Re-rank by past usefulness. Fold clusters of memories into skills (`Jx4ZFEAq6bY`, `XPj3mIKEtI4`, `xxfMT-bPEmU`, `2IxD9OB3XuQ`).
- **Shared memory is the new hard part.** Per-agent memory is called solved. Learning across agents, teams and users needs scopes, provenance and a human gate for promotion (`9_oy4owGtPI`, `0uC6u0lJJl4`, `BIhiYL4U9_M`, `5ID22ACI7IM`).
- **Graph memory is pitched hard by Neo4j.** The claim: vector search finds seeds, graph traversal adds multi-hop context, and you can inspect what entered the context (`Q0VkgCyNVUg`, `XPj3mIKEtI4`, `B9h9ovW5H9U`). Counter-examples use plain files or a log (below).
- **Files-only still works for personal use.** An immutable raw folder, an index file and an LLM-written wiki, with no vector DB (`ZRM_TfEZcIo`, `I3bpdgFJCUY`).

## Consensus patterns

1. **Keep a short context and externalize the rest.** Big tool output goes to storage. The agent holds only a pointer. Old turns are summarized or moved out and fetched by ID (`DrfyORO8RqA`, `esY99nYXxR4`, `KtBivPzmOM8`, `9QebvrrY3KY`).
2. **Bigger windows do not fix degradation.** More tokens means less attention per item, even under the advertised limit (`DrfyORO8RqA`, `KtBivPzmOM8`, `xs-ob87TTzg`, `9_oy4owGtPI`).
3. **Retrieve tools and skills on demand.** Embed their descriptions. Load only the top few per loop step (`xs-ob87TTzg`, `KtBivPzmOM8`).
4. **Hybrid retrieval beats vectors alone.** Fuse keyword and embedding results, often with RRF. Add entity, graph and recency branches. Return the matched branches as provenance (`BIhiYL4U9_M`, `KtBivPzmOM8`, `Q0VkgCyNVUg`).
5. **Provenance on every memory.** Link each fact to its source episode. Merges union the sources. A contradicted fact gets an invalid-at time instead of being deleted. Delete a derived fact only when no source remains (`H7puB0RwJMM`, `9_oy4owGtPI`, `BIhiYL4U9_M`, `Q0VkgCyNVUg`).
6. **Scope on write and on read.** Tag facts with the groups of their sources. Return them only to people who hold all those groups (`5ID22ACI7IM`, `BIhiYL4U9_M`, `0uC6u0lJJl4`, `ohKt066uFhg`).
7. **The agent suggests, a human promotes.** Do not auto-write shared memory. Attribute each change to a named human (`0uC6u0lJJl4`, `9_oy4owGtPI`).
8. **Corrections outrank everything.** A human fix is stored permanently and overrides other facts (`jtzh-GBXBWc`, `Jx4ZFEAq6bY`, `wEc9aG7cRQc`).
9. **Consolidate offline.** Dedupe, resolve conflicts, prune, promote to skills, then report to a human (`jtzh-GBXBWc`, `xLUQOqjudtA`, `9QebvrrY3KY`, `qJtcEDc_WJU`).
10. **Decision traces are memory.** Store the plan, evidence, rule applied and result. Later runs use them as precedent (`eW_vxrjvERk`, `abvQEhvRI_c`, `B9h9ovW5H9U`, `XPj3mIKEtI4`).
11. **Check memory before redoing work.** Query the store for the same entity first. Write notes back at the end (`FGftGOzfohc`, `TN3mj92oZ8I`).
12. **Context needs a lifecycle.** Versions, owners, dependents, and event logs of corrections fed back on a schedule (`8G_1-3IO4ZQ`, `B8l81jhvHbI`).
13. **Put knowledge in the right place.** Prompt for small, stable behavior. Memory for large, fast-changing, citable facts. Weights only for what stopped changing. Debug retrieval before touching weights (`qflLT3SoVbw`).
14. **Treat memory as an untrusted write path.** Redact before embedding. Watch for durable prompt injection. Let admins suppress poisoned records (`BIhiYL4U9_M`, `s67bE2Ur3bY`, `0uC6u0lJJl4`).

## Disagreements & open questions

- **Graph vs files vs log.** Neo4j says markdown and vector lookups fail on multi-hop (`Q0VkgCyNVUg`). The personal-wiki talks say skip graphs and vector DBs (`ZRM_TfEZcIo`). Active Graph uses a plain embedded event log with no fact extraction (`khVX_BUnEwU`). No talk compares them head to head at scale.
- **Files vs database.** Oracle talks say use both. Files for scratch, a DB for what must persist and be shared (`xs-ob87TTzg`, `jA_x7F8caHI`). Both are vendor-led.
- **Does memory help at all?** One benchmark found vanilla in-context learning beat costlier context-management systems (`iqloyWCGYQQ`). Another found memory helps only when the answer falls outside the window (`R3-anFK1YM8`).
- **Write policy.** Auto-write with gates (`jtzh-GBXBWc`) versus human-approved only (`0uC6u0lJJl4`, `9_oy4owGtPI`).
- **Do not feed past answers back.** One talk warns against caching answers (`5ID22ACI7IM`). Others write every answer into the wiki or graph (`ZRM_TfEZcIo`, `eW_vxrjvERk`).
- **Where continual learning lives.** In a profile outside the weights today (`5ZGyKWjQDr0`), or compressed into weights and KV (`WiqDvX6isc4`, `I6aiEf3aEFQ`). Naive training on a private corpus memorizes but does not generalize (`WiqDvX6isc4`).
- **Conflict resolution.** Recency alone fails. Proposals: ingestion tags plus a judge, then show both to a human (`5ID22ACI7IM`, `BiG2ssibKGc`).
- **Open:** a success signal for skill-worthiness, how to measure forgetting under drift, and a cost model for lineage and graph builds (`iqloyWCGYQQ`, `H7puB0RwJMM`).

## How thinking changed over time

- **2026-05-18.** Memory is framed as a graph with three stores (short-term, long-term, reasoning) (`eW_vxrjvERk`). Context engineering is truncation plus spill to memory, with long-session evals (`esY99nYXxR4`). Enterprise talks say access is not understanding (`5ID22ACI7IM`).
- **2026-06-18.** The emphasis moves to decision traces and precedent (`abvQEhvRI_c`, `B9h9ovW5H9U`). Unblocked adds exhaustive retrieval and surfaced conflicts (`BiG2ssibKGc`).
- **2026-07-18.** Memory becomes learning. Fixes are routed to model, harness or memory behind a regression gate (`2IxD9OB3XuQ`). Utility-weighted retrieval and skills from memory appear (`Jx4ZFEAq6bY`). The company brain and the nightly dream cycle arrive (`eBUyTS7SzV4`, `jtzh-GBXBWc`). Cross-session session replay appears (`jVjt-2g8NMY`).
- **2026-08-18.** Peak memory month. The consumer history is told as profile plus dreaming (`5ZGyKWjQDr0`). Memory is a write-manage-read loop (`R3-anFK1YM8`). Provenance and lineage get a full talk (`H7puB0RwJMM`). A benchmark for continual learning, Continual Learning Bench 1.0 (`iqloyWCGYQQ`). The brain/hands split and dreaming come from Anthropic (`9QebvrrY3KY`).
- **2026-09-18 to 09-20.** Governance and team memory. Per-user credentials, scopes and a leak-proof brain (`0uC6u0lJJl4`). Five-type taxonomy and a shared broker tied to repo state (`jA_x7F8caHI`, `xs-ob87TTzg`). Vendors pitch managed knowledge layers (`IN-rb-9WmiY`).
- **2026-10.** Typed, governed memory with hybrid fusion (`BIhiYL4U9_M`). The claim "per-agent memory is solved, shared learning is not" (`9_oy4owGtPI`). Skills distilled from graph memory with coverage checks (`XPj3mIKEtI4`). Knowledge placement as a deliberate choice (`qflLT3SoVbw`). Local-first and owned memory (`apyrzaWj0Z4`). Anthropic Managed Agents ships dreaming and scheduled deployments (`qJtcEDc_WJU`, `FGftGOzfohc`).

## Numbers worth remembering

- Ranked decision-ledger recall beat no memory and vector RAG on 68 long-horizon questions, and cost less (`R3-anFK1YM8`).
- Vanilla in-context learning topped the reward leaderboard and Pareto frontiers against costlier memory systems. The metric is gain, which is stateful minus stateless reward (`iqloyWCGYQQ`).
- ChatGPT memory V1 was a fact list in Feb 2024. V2 was a running profile in Apr 2025, almost 4,000 tokens. Claude's first memory in Aug 2025 had search tools and no profile (`5ZGyKWjQDr0`).
- 93 real security alerts run 3 times each. About 25% flip-flopped. Episodic memory made about 15% consistent (the wording is ambiguous) (`wEc9aG7cRQc`).
- RAG faithfulness started at 14% (MD) and 20% (PDF). One-variable tuning raised scores to the 80s. Context chunks fell from over 7,000 to about 1,000 (`9_oy4owGtPI`).
- Policy benchmark: 66% baseline, 76% with memory, 80% with skills. Vendor-reported (`Jx4ZFEAq6bY`).
- Skill definitions cost 3,000-5,000 tokens each. Tools and skills can take over 50% of the window (`KtBivPzmOM8`).
- Summarizing manager example: ratio 50%, keep last 4 messages, cap 3 calls per tool (`DrfyORO8RqA`).
- A context engine cut a task from about 2.5 hours and 21M tokens to 25 minutes and 10M. The speaker says the figures may be inaccurate (`5ID22ACI7IM`).
- The speaker says a memory system that works at about 1,000 records can degrade silently by 50,000 to a million. This is qualitative, with no measurement (`BIhiYL4U9_M`).
- A company brain of about 5,000 wiki pages, with daily update counts that keep rising, is read as healthy. The speaker admits this is early data (`0uC6u0lJJl4`). An Obsidian vault of about 3,000 notes (`sJ2jc7leKBk`).
- Smart turn-taking halved early aborts for about 60 ms extra latency. Voice target is under 2 s (`xLUQOqjudtA`).
- Self-edit loop: 8 to 13 loops, 4 to 5 patches kept, on LongMemEval (about 500 questions) (`khVX_BUnEwU`).
- Semantic layer plus canonical queries solve about 80% of data-agent problems. This is the speaker's estimate (`B8l81jhvHbI`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Scope: 23 creator videos, from 2024-11 to 2026-10. Most are single-builder demos or tool reviews. None runs an independent controlled test against a baseline; the Tencent video's baseline comparisons are vendor-run. Vendor-run numbers and sponsored segments are flagged below.

### Practical playbook

1. **Keep a project brief that loads every session.** Put the overview, build and run commands, constraints and "must remember" items in the project-root CLAUDE.md. The speaker frames it as the place for persistent project instructions (`oj44Vrh0XyM`, single demo).
2. **Write a persistent rule with the `#` shortcut.** In Claude Code, type `#` plus the instruction, then pick the project scope so it lands in CLAUDE.md (`oj44Vrh0XyM`).
3. **Compact by hand before auto-compact.** Check usage first, then run compact with retain instructions that name project state, decisions and open tasks. One session dropped from 92% to 36% context (`oj44Vrh0XyM`, one session).
4. **Budget the window per turn, not by the advertised size.** Count the system prompt, tool definitions, kept turns, file reads and room for output. The speaker's example reaches 54k tokens before the model writes anything (`Nf8j9w523pw`, illustrative, not measured).
5. **Put critical rules at the top, and repeat them near the end.** Middle-of-context instructions get less attention. No effect size is given (`Nf8j9w523pw`).
6. **Write big tool output to files, not to the prompt.** Keep a short step map with one ID per node. Fetch raw text by ID when an error needs detail. Cap the map at about 20% of the token budget. Fold mildly at about 50% of the window and hard at about 85% (`W3yHP9_jYNk`, vendor-run benchmark, single video).
7. **Give each folder an index.** Add an `index.md` per folder, one concept per file, and YAML frontmatter with name, description and type. Document the layout in CLAUDE.md, because the speaker says Claude ignored the structure until it was written there (`k4sMSsMzX2g`, team test, no numbers).
8. **Seed the client with what the memory holds.** Put a short live summary in the MCP server instructions and in the query tool description. The speaker says clients do not call a memory they cannot see (`9ciGYHHOLyU`, one build).
9. **Write rules for the memory store.** Search for an existing concept before creating a file. Rewrite a stale fact everywhere it appears instead of appending the new value. Run a non-LLM lint for orphans and broken links, and exclude auto-generated index files as link sources (`9ciGYHHOLyU`).
10. **Split memory into a small preload and a searchable archive.** Keep a memory file of about 3,500 characters, loaded each session. Save each full session to SQLite with an FTS5 index and search it on recall (`HdxtLpL9CC8`, single-user test).
11. **Checkpoint at session end, and search first in a new one.** Ask the agent to save progress to memory when a session ends. In the next chat, ask it to search memory for the project before doing anything else (`Y2XI2nk44WE`, `mKXzPVIMFYE`). The Open Memory test lost structured content, so the speaker recommends plain text.
12. **Test recall before you trust it.** Plant a known bug fix in session one. Open a new session and ask for the fix without re-explaining. Then check that keyword search returns the compressed entry (`ryqpGVWRQxA`, a one-bug demo).
13. **Label every derived link.** Tag graph edges as Extracted, Inferred or Ambiguous, and treat the last two as unverified before they drive a decision. Re-index only files whose SHA256 changed, and rebuild on each commit with a git hook (`8Kv2tn22QNo`, `WNru_PFycT8`).
14. **Gate model calls behind a cheap check.** In a cron job, run a plain script first and call the LLM only when it fires. The video does not show the flag syntax (`qMEm1bgxnUM`, one video).

### Tools creators recommend

- Claude-Mem: automatic capture of Claude Code session events, with compressed recall. Local store. `ryqpGVWRQxA`
- Open Memory (Mem0 repo): self-hosted shared memory for MCP clients, run with Docker, UI on localhost:3000. `Y2XI2nk44WE`
- SuperMemory: hosted memory through MCP or a memory-router base URL. Vendor-led. `mKXzPVIMFYE`, `GETMfbGWc0k`
- Cline Memory Bank pattern: a fixed set of markdown files for project context, pasted into Cursor rules. `azXNHRtzd5s`
- Mastra: TypeScript agent with chat memory and a working-memory template. `_dG8iZgmicQ`
- Phidata: local agent server with a session database file. `nkh7q8WU7oU`
- Hermes: bounded memory file, session archive, skills, and `hermes mcp serve` so other agents can use it. `HdxtLpL9CC8`, `Sb96po6S67k`
- Graphify: repo graph with provenance labels and hash-based incremental rebuilds. `WNru_PFycT8`, `8Kv2tn22QNo`
- MemPalace: verbatim local store with a compact index, MCP server and Claude Code plugin. `kRACHOx1p8s`
- PAI: persistent memory and per-role skills on top of Claude Code. `JukZ7WWtOSg`
- Google OKF: folder bundles with index.md files and frontmatter. `k4sMSsMzX2g`
- Librarian MCP over a markdown wiki: deterministic store, model used only for write decisions. `9ciGYHHOLyU`
- Tencent memory plugin (MIT): offloads tool output to disk and runs a four-layer memory. Vendor-run numbers. `W3yHP9_jYNk`
- Mem0 (in a roundup): extract facts on write, retrieve relevant ones on read. `-UxcljWN49I`
- LangChain DeepAgent: memory in your own Postgres, or a plain agents.md file. `jtWjkdBNqlk`
- Prime Agent: a refine command turns session observations into reviewable updates. `kg3MmLd0qEM`
- Agit: git-style versioning of agent sessions, with revert and fork. The segment on Runnable is sponsored. `CHHEjuNBxoQ`

### Where creators agree or clash with the conference talks

- **Agree: keep the window short and externalize the rest.** Creators make the same point with concrete steps: file-backed tool output, a step map, and budgets (`W3yHP9_jYNk`, `Nf8j9w523pw`).
- **Agree: a bigger window does not fix degradation.** Both the context-budget video and the Tencent video cite attention falling off with length. The first cites lost-in-the-middle without naming the paper (`Nf8j9w523pw`, `W3yHP9_jYNk`).
- **Agree: files can be enough.** The LLM-wiki build calls RAG the wrong default for personal memory and relies on linked files (`9ciGYHHOLyU`). That matches the conference view that files-only still works.
- **Clash: graphs.** Graphify's own benchmark claims about 70x fewer tokens per query on a mixed codebase, self-reported and not reproduced outside (`8Kv2tn22QNo`). The demo's figure, about 14k tokens down to a couple hundred on one small repo, is a single anecdote (`WNru_PFycT8`). No video compares it with RAG on the same questions. The graph-versus-files question stays open.
- **Clash: write policy.** Conference talks favour human-gated shared memory. Creators auto-capture by default, with no governance story (`ryqpGVWRQxA`, `HdxtLpL9CC8`). Only the Tencent video names the poisoning risk, and it does not describe a fix (`W3yHP9_jYNk`).
- **Clash: when to consolidate.** Conference talks run consolidation offline. The Tencent design folds facts online every five turns and rebuilds the persona every 50 memories (`W3yHP9_jYNk`). That is one vendor's design.
- **Clash: benchmark gains.** The Tencent video reports 33% to 50% on WideSearch and 61% fewer tokens. The speaker found one row that does not reconcile, and the gains shrink on harder tasks. A conference talk found in-context learning beat costlier memory systems. Treat both as unverified (`W3yHP9_jYNk`).
- **Caution: prompt caching.** The Tencent video says per-turn memory injection at the front of the prompt breaks prefix caching. The speaker calls this an open issue (`W3yHP9_jYNk`). Check cache hits before you inject memory into every call.

### Watch first

- `W3yHP9_jYNk` — layered memory and offload-to-disk, plus a worked check of vendor arithmetic. One vendor-run benchmark.
- `Nf8j9w523pw` — the context-budget audit. Mostly conceptual, with no measurements.
- `9ciGYHHOLyU` — the most concrete write rules: enrich before create, link both ways, orphan lint. One builder, no benchmarks.
- `8Kv2tn22QNo` — provenance labels and tiered data egress for ingestion. The title oversells the tool, but the lint and label ideas transfer.
- `kRACHOx1p8s` — verbatim storage versus summaries, and the costs of local memory, and a supply-chain caution about lookalike sites.

## Watch first

- `5ZGyKWjQDr0` — the clearest history of consumer memory. Profile vs search, dreaming, and the compute trade-off.
- `BIhiYL4U9_M` — the best design checklist. Typed schema, write pipeline, weighted hybrid retrieval, governance on write and read.
- `R3-anFK1YM8` — one of the few real experiments. A fixed model with recall modes and an oracle.
- `iqloyWCGYQQ` — how to measure memory. Paired stateful and stateless runs, drift, Pareto reporting.
- `H7puB0RwJMM` — provenance, merge-safe lineage and deletion. Directly useful for conflict handling.
- `9_oy4owGtPI` — private-to-shared promotion and why handing off only output loses reasoning.
- `9QebvrrY3KY` — brain/hands split, append-only context, separate-context verifier, dreaming.
- `0uC6u0lJJl4` — leak control for a shared brain. Scopes, human gate, per-user credentials at the proxy.

## Implications for our projects

**AgentOS MemoryMesh**
- Adopt the typed schema: episodic, semantic, procedural, working. Add valid-to, last-used, scope and audit fields. Store a linked episode, not the whole transcript (`BIhiYL4U9_M`).
- Hybrid BM25 plus pgvector already matches the consensus. Add weighted branches (entity, recency, feedback) with RRF fusion. Return the matched branches with each hit (`BIhiYL4U9_M`, `KtBivPzmOM8`).
- Make provenance a graph walk: facts link to every source episode. Merges union sources. Contradictions set invalid-at. Delete only unsupported facts (`H7puB0RwJMM`). This fits the conflict-resolution and provenance pillar.
- Build RAGAS-style evals around the recall policy: no memory, vector, ranked, oracle, with seeds and a wrong-memory ablation (`R3-anFK1YM8`). Add paired stateful vs stateless gain and a mid-run schema drift case (`iqloyWCGYQQ`).
- Add a nightly consolidation worker with a human-readable report. Gate its rewrites with evals (`jtzh-GBXBWc`, `qJtcEDc_WJU`).
- Add utility-weighted re-ranking from run outcomes. Store memories as conditional procedures (`Jx4ZFEAq6bY`).
- Keep Neo4j for GraphRAG behind a vector-seeded traversal. Log the subgraph that entered context for debugging (`Q0VkgCyNVUg`). Treat the claim that graphs beat vectors as unproven.
- Add a private-to-shared promotion gate and per-memory scopes. Put the scope check at the Govrix proxy so credentials never enter the sandbox (`9_oy4owGtPI`, `0uC6u0lJJl4`, `5ID22ACI7IM`).

**AgentOS SkillForge / EvolveCraft**
- Distill skills from memory clusters, with coverage and coherence checks, and keep the LLM to wording only (`XPj3mIKEtI4`, `Jx4ZFEAq6bY`, `xxfMT-bPEmU`).
- Use the three-gate rule for any self-edit: executable test, measured delta, regression suite (`2IxD9OB3XuQ`, `khVX_BUnEwU`). Keep rejected patches with their verdicts.
- Route each fix to the cheapest layer first: memory fact, prompt, tool, then weights (`2IxD9OB3XuQ`).

- The registry is a context layer: versioned skills with owner, approver and dependents, flagging downstream skills on change (`8G_1-3IO4ZQ`).
- Trace-derived source scores can drive source choice and trust (`VGN22pPpb-8`).
- Mining traces needs an agent, not a person. Cost is dominated by input tokens (`CvRngaQZQ3Y`).

**ProsHarness**
- Use an append-only event log and re-fetch instead of destructive compaction. This pairs with checkpoint/resume (`9QebvrrY3KY`, `khVX_BUnEwU`).
- Replay a session on another machine from intent, SHAs, PRs and trace (`jVjt-2g8NMY`).
- Run the builder and verifier in separate contexts with an iteration cap, matching the plan-critique loop (`9QebvrrY3KY`, `FGftGOzfohc`).
- A resolver table plus trigger evals gives skill routing a test (`eBUyTS7SzV4`).

**Entity resolution and cheap-model pipelines**
- Measure flip rate over repeated runs. Pick review cases by disagreement, not confidence. Back them with episodic precedent and semantic rules (`wEc9aG7cRQc`).
- Use a staged extractor where cheap steps handle most text before a stronger model (`B9h9ovW5H9U`).
- Reconcile human labels against behavior to find bad labels (`ACPEpji5NV4`).
- A small router model can pick the model per turn (`xLUQOqjudtA`).

**Storage roadmap**
- An embedded vector store with one isolated folder per app fits local-first, portable memory. Keep the same embedding model so the folder stays usable (`apyrzaWj0Z4`).
