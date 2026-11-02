# memory — 88 videos

*long-term / cross-session agent memory, knowledge graphs for agents*

By channel: AI Engineer 63 · Kai Explains 7 · AI LABS 11 · Better Stack 7

**Synthesized guide:** [guides/memory.md](../guides/memory.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Everyone Has the Same AI Models. Here's What Sets Agents Apart - Richmond Alake, Oracle](../videos/1_lX0m64-aI.md)
`1_lX0m64-aI` · AI Engineer · 2026-11-01 · q2 · intro · talk · also: agent-architecture, rag-retrieval, security-guardrails

Oracle's Richmond Alake argues agents need an "intelligence plane" (knowledge, memory, access governance, continual learning) beyond the control plane, illustrated with Oracle product demos.

- Techniques: Memory routing with a small fine-tuned decision model; Capture memory traces as fine-tuning data; Ontology and semantic layer in front of retrieval; Propagate user identity into data access; Private inference container for on-prem embeddings, LLM and rerankers
- Tools: Oracle AI Database, Oracle agent memory Python package (generates context cards), Oracle Deep Data Security, Oracle Private AI Services Container, Oracle Cloud (hosted Grok and OpenAI models), Private Agent Factory (no-code agent builder on Oracle AI Database), Memories (open-source agent memory tool built by the speaker), Qwen (fine-tuned as memory-routing decision model)

## [How to Decide What Your AI Agent Should Remember - Wojciech Pluta, Oracle](../videos/qq2Hm4XNRgI.md)
`qq2Hm4XNRgI` · AI Engineer · 2026-10-31 · q2 · intro · talk · also: context-engineering, agent-architecture, security-guardrails

Oracle's Wojciech Pluta argues agent memory is a write path that needs a promotion gate with provenance, scoped memory tiers, and per-turn context cards. Vendor talk with a demo.

- Techniques: Memory promotion gate; Provenance plus supersede, not overwrite; Three-tier memory scoping; Per-turn context card; Enforce user isolation in the database layer
- Tools: Oracle AI Database, Oracle agent memory package (named as an early-year release; no version given)

## [We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI](../videos/YIhvrvHtonk.md)
`YIhvrvHtonk` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: agent-architecture, context-engineering, evals

Arize's PM on two years of shipping Alex, its in-product agent: keep the loop, plan, stop rule and memory in harness code, use small capped memory files, and treat production traces as regression tests.

- Techniques: Render the plan into the harness on every call; Explicit finish call as a harness gate; Tool results as pointers, not inline content; One small capped markdown memory file per user; Single model call instead of a loop for narrow features; Production sessions as living regression fixtures; Trace-reading agent for silent failures
- Tools: Arize AX, Alex (Arize in-product agent), Signal (Arize trace-reading agent), Sonnet 4.5 (auto-caption 'Sonic 4.5'), jq, Arize experiments

## [Inside Arca's Long-Horizon Agents That Run the Business - Aman Singh, Arca](../videos/oP2WLFpMoDY.md)
`oP2WLFpMoDY` · AI Engineer · 2026-10-24 · q3 · practitioner · review · also: agent-architecture, multi-agent, enterprise-adoption

Arca, an AI-native financial services firm, explains how background agents own multi-day client work through a signal system, shared plan spaces, and human pull-ins.

- Techniques: Signal-driven wake-up with interest registration; Dual wake-up: event plus timed fallback; Treat UI mutations as first-class events; One shared workspace per goal with human pull-ins; Split state by horizon: memory for later, tasks for now; Turn colleagues' reasoning into eval cases; Steer by adding a goal

## [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](../videos/KtBivPzmOM8.md)
`KtBivPzmOM8` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · also: agent-architecture, context-engineering, rag-retrieval

Oracle workshop on memory-aware agent harnesses for AML: treat the harness (loop, memory tiers, skill retrieval, context budget) as the thing to engineer, not the frontier model.

- Techniques: Two-tier memory with promote-to-long-term; Vector-indexed skill and tool box with top-k retrieval; Hybrid keyword plus embedding retrieval with RRF; Compaction or summarization of old context; Skill distillation from past runs; Pre-vetted query tools instead of free-form SQL; Bounded agent loop for unattended runs; Stable request prefix for caching
- Tools: Oracle Database, OCI (Oracle Cloud), GitHub Codespaces, OpenAI chat completions API, vector store, MCP, RRF, Claude Code, Codex, Pi harness, Hermes agent, OpenClaw

## [Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](../videos/FGftGOzfohc.md)
`FGftGOzfohc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, multi-agent, security-guardrails

Anthropic hands-on workshop (Part 2 of 4) building a research agent on Claude Managed Agents: sub-agents, rubric-graded outcomes, vaults, shared memory, dreaming, and a map-reduce harness.

- Techniques: Rubric-gated outcome with a grader sub-agent; Placeholder secrets with domain-scoped egress swap; Context isolation via self-referencing sub-agents; Check shared memory before redoing work; Map-reduce orchestration via a custom dispatch tool; Transcript-driven memory consolidation (dreaming)
- Tools: Claude Managed Agents API, Claude Code (used to drive the workshop), SEC EDGAR Python package, MCP, Bun, npm, Agent SDK (compared)

## [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](../videos/qJtcEDc_WJU.md)
`qJtcEDc_WJU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, multi-agent, skills-self-improvement

Anthropic's live demo and Q&A on Claude Managed Agents covers multi-session orchestration, scheduled deployments, outcome rubrics, and "dreaming," a memory-store self-improvement pass that the speaker says still needs your own evals.

- Techniques: Fan-out one session per entity via a dispatch tool; Scheduled deployment of a standing agent; Outcome rubric with a max-iteration cap; Offline dreaming pass over past transcripts; Workspace-per-tenant isolation instead of BYOK; Memory store as a separate attachable resource
- Tools: Claude Managed Agents, Claude Console, Claude Code, Anthropic SDK / API, AWS Bedrock, GitHub, OpenTelemetry, Jira (Atlassian integration), Notion (external agents)

## [Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge](../videos/cSz7aL2nl2U.md)
`cSz7aL2nl2U` · AI Engineer · 2026-10-10 · q2 · practitioner · talk · also: context-engineering, mcp-and-tools, rag-retrieval

Gil Feig (Merge) argues every company needs a "context graph" (a company brain of synced data, live lookups, memory, skills) and lays out how to route, cache, and trace it. Conceptual talk with a closing product plug.

- Techniques: Split retrieval: live MCP vs. synced vector cache; Router plus summarizer; Skills and memory first; Freshness SLA check on cache; Derived-context write-back; Bounded live pulls; Provenance metadata on every record
- Tools: MCP (Model Context Protocol), Zendesk, Jira, NetSuite, Stripe, Qualtrics, vector database (unnamed), Merge Unified, Merge Agent Handler, Merge Gateway

## [From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle](../videos/BIhiYL4U9_M.md)
`BIhiYL4U9_M` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: rag-retrieval, context-engineering, security-guardrails

Oracle's Anders Swanson argues agent memory should be a governed, typed database layer with redaction, hybrid retrieval, scoped access, and feedback loops, not files or bigger context windows.

- Techniques: Typed memory schema with per-type lookup; Write pipeline: redact, enrich, scope, embed, episode-link; Weighted hybrid retrieval with fused scores and provenance; Governance on write and on read; Feedback signals that rank and promote or demote memories; Expose memory as a runtime function
- Tools: Oracle AI Database, Oracle Python SDK for agent memory (speaker's; referenced, not shown), Claude Code, Codex, MCP, hooks, skills

## [Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain](../videos/KGFyOtl5ktI.md)
`KGFyOtl5ktI` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: agent-architecture, evals, context-engineering

Jake Broekhuizen (LangChain) argues agent memory is a read-write loop: capture traces, filter them into signal, and promote only the durable parts into long-term context, with human review for procedural memory.

- Techniques: Trace-to-memory capture, analyze, update loop; Classify memory into semantic, episodic and procedural buckets; Gate procedural memory updates with human review and evals; Check the hot path for memory staleness
- Tools: LangSmith, LangSmith Context Hub, LangChain, OpenClaw, HermesAgent

## [Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j](../videos/XPj3mIKEtI4.md)
`XPj3mIKEtI4` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · also: skills-self-improvement, data-engineering

Neo4j PM Will Lyon argues agent memory should be a typed, traceable context graph, and shows how to distill that graph into governed, step-by-step agent skills rather than static markdown.

- Techniques: Typed context graph as agent memory; Decision traces as reasoning memory; Scope-first skill distillation; Coverage and coherence checks on generated skills; Staleness-aware skill registry; Typed step schema for skills (APE)
- Tools: Neo4j Agent Memory Service (NAMs), Neo4j graph database, Agent Skills open standard (agentskills.io), APE skill protocol, MCP tools, SkillsBench

## [Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS](../videos/DrfyORO8RqA.md)
`DrfyORO8RqA` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · also: context-engineering, agent-architecture

AWS speaker on why larger context windows don't fix agents; she covers externalizing big tool output, summarizing and isolating context, loop caps and async tool calls, using Strands Agents.

- Techniques: Memory pointer for large tool output; Summarizing conversation manager with a ratio and a keep-last-N; Tiered memory: short-term, vector long-term, entity graph; Shared invocation-state pointer for multi-agent swarms; Per-tool invocation cap; Async job start/check tool pair
- Tools: Strands Agents, FastAPI, MCP, Neo4j, AWS API Gateway, Amazon Bedrock, Ollama, Gemini, Anthropic, OpenAI

## [Agent Memory Is Solved. Agent Learning Isn't. — Karthik Ranganathan, Yugabyte](../videos/9_oy4owGtPI.md)
`9_oy4owGtPI` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: multi-agent, context-engineering, observability

Yugabyte's CEO argues agent memory is solved but cross-agent learning is not, and demos Mako, a private-to-shared context store where humans promote memories and provenance is traceable.

- Techniques: Private-to-shared promotion gate; Provenance on every memory; Scoped data packs with a skill-driven MCP interface; Cross-session resumability via shared memory; One-variable-at-a-time RAG tuning with traces; Trace-based token accounting
- Tools: Mako (Yugabyte agent-native persistence layer), YugabyteDB, Claude Desktop, Claude Design, Codex, ChatGPT, MCP, Postgres

## [Stop Renting Your AI's Memory — Dylan Couzon, Qdrant](../videos/apyrzaWj0Z4.md)
`apyrzaWj0Z4` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: rag-retrieval, local-ai

Dylan Couzon (Qdrant) argues agent memory should be owned locally: models are rented, but a private, retrieval-based memory store compounds and stays portable. Includes a live offline drone-vision memory demo.

- Techniques: Write-retrieve-forget memory loop; Embedded in-process vector store with per-app folder; Quantized vectors for small footprint; Pin the embedding model for portability; Detector labels then embeddings for perception memory; Opt-in sync of local memory to a shared store
- Tools: Qdrant, YOLO

## [I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j](../videos/oUZEt4EiPbk.md)
`oUZEt4EiPbk` · AI Engineer · 2026-10-04 · q2 · intro · demo · also: agent-architecture, mcp-and-tools, sandboxing-execution

Neo4j's Jeremy Adams builds a personal agent on a Raspberry Pi 4B: NanoClaw in Docker, WhatsApp as the channel, cloud LLMs, and graph memory, with a live demo and an offline capture mode for conference Wi-Fi.

- Techniques: Edge orchestrator, cloud brain; Container per agent process; Messaging app as the agent front end; Graph database as an MCP tool; Offline-first capture with deterministic parsing and later sync; Typed entity memory schema written as a skill; Batch distillation of chat history
- Tools: Raspberry Pi 4B, NanoClaw, OpenClaw, Claude Agent SDK, WhatsApp, Telegram, Docker, Neo4j, Neo4j Aura, Cypher, MCP, Neo4j agent memory service

## [Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava](../videos/qflLT3SoVbw.md)
`qflLT3SoVbw` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: context-engineering, rag-retrieval, training-finetuning-rl

Anant Srivastava argues enterprise teams should decide deliberately whether knowledge lives in the prompt, in retrieval/memory, or in fine-tuned weights, using rate of change, scope, and behavior-vs-facts as the test.

- Techniques: Knowledge placement diagnostic; Retrieval-first debugging; Fine-tune the stable center, keep humans on the edge; Code-aware chunking with denormalized metadata; Promote-and-prune memory loop; Small fine-tuned model for cost

## [Building Self-Improving Agent Software Factories — Suraj Gupta, Warp](../videos/TN3mj92oZ8I.md)
`TN3mj92oZ8I` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: software-factory, skills-self-improvement, token-cost-efficiency

Warp's Suraj Gupta on making agent software factories self-improve through outer-loop skill edits gated by PR review, agent-scoped versioned memory, and rule-based model routing for cost.

- Techniques: Outer-loop skill improvement with PR gate; Agent-scoped fact memory with provenance; Rule-based model routing by task class; Best-of-k model sampling to learn routing
- Tools: Warp, Oz (Warp cloud agent platform), Sentry, GitHub, Codex, Claude Code, Opus, Haiku, GLM, Qwen

## [This New Open Source Tool Just Fixed Your Claude Code Workflow](../videos/CHHEjuNBxoQ.md)
`CHHEjuNBxoQ` · AI LABS · 2026-10-02 · q3 · practitioner · review · also: coding-agents, context-engineering, security-guardrails

Walkthrough of Agit, an open-source tool that applies git's model (repos, sessions as branches, turns as commits) to agent conversations, with sharing, revert, cross-agent fork and secret redaction.

- Techniques: Versioned agent sessions via a git-style repo; Reverting a session to an earlier turn; Cherry-picking messages between sessions; Forking a Claude Code session into Codex; Registering known passwords before a session is saved
- Tools: Agit, createagit (installer), npm, GitHub, Claude Code, Codex, AGENTS.md, CLAUDE.md, Runnable (sponsor)

## [Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash](../videos/ACPEpji5NV4.md)
`ACPEpji5NV4` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: rag-retrieval, data-engineering, evals

DoorDash's search and personalization lead on using LLMs offline to create graded relevance labels, semantic IDs, and memory, then serving those through small, fast models.

- Techniques: Offline LLM labeling with a distilled labeler; Label-audit by disagreement; Two-stage contrastive retrieval with hard-negative curriculum; Auxiliary ordinal relevance tower with value-function blend; Hierarchical learned semantic IDs as sparse features; Multi-form consumer memory blocks; Batch generation of personalized content with the existing ranking stack
- Tools: GPT-4o mini (named as an example lightweight labeler)

## [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](../videos/x4e5O9zN0TE.md)
`x4e5O9zN0TE` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: evals, skills-self-improvement, multi-agent

Long-running, stateful agents need controlled scenario suites, balanced scorecards and a ratchet loop, not just prompt tweaks; the speaker's case study is a game-village multi-agent system tuned by an outer auto-research loop.

- Techniques: Controlled scenario suite with ground truth; Balanced behavioral scorecard with guardrails; Frozen-harness ratchet loop; Structured run-trace logging; Importance-scored memory with a threshold cache; Provenance and confidence tags on memories; Separate episodic memory from current belief
- Tools: Project Paradox (in-house framework), RAG-backed per-agent memory, auto-research loop (Karpathy-inspired)

## [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](../videos/xs-ob87TTzg.md)
`xs-ob87TTzg` · AI Engineer · 2026-09-20 · q3 · practitioner · workshop · also: agent-architecture, context-engineering, skills-self-improvement

Oracle workshop on agent harness design: a 30-minute framework for agent memory (files vs databases, memory types, context rot, skill promotion), then a hands-on notebook build, with heavy Oracle product promotion.

- Techniques: Hybrid storage split; Per-agent git worktrees for file edits; Context card; Toolbox / skillbox index with vector retrieval; LLM-enhanced tool descriptions; Patience (hysteresis) budget for agent loops; Skill promotion by distillation; Difficulty-based model routing
- Tools: Oracle Database (converged: JSON, relational, spatial, graph, vector), Oracle DBFS, Oracle Agent Memory Package (OAMP), LangChain Oracle DB integration, OCI Generative AI service, GitHub Codespaces, Grok 4.1 Fast Reasoning, HNSW vector indexes, git worktrees, Python 3.12 notebook

## [From coding to Knowledge work agents — Karan Vaidya, Composio](../videos/xxfMT-bPEmU.md)
`xxfMT-bPEmU` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: governance-compliance, agent-architecture, sandboxing-execution

Composio CTO on why coding agents work and knowledge-work agents don't: six missing primitives (centralization, history, context, verification, governance, reversibility), enforced with walls and sandboxes rather than prompts.

- Techniques: Single connection hub for agents; Cross-app action record; Skill distillation from run logs; Pre-send style check against past outputs; Sandbox mirror of production tools; Two-layer walls: access scope plus behavior policy; Tiered gates scaled to blast radius; Undo for reversible actions, sandbox for the rest
- Tools: Composio, Claude Code, Codex, Cursor, OpenClaw, Git, Salesforce, Notion, Gmail, Slack, Zendesk, bugbot.md (named in passing)

## [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../videos/0I6aoPSRzVc.md)
`0I6aoPSRzVc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: multi-agent, context-engineering, enterprise-adoption

AIDAChip's VP of AIML argues chip-design teams are limited by alignment, not intelligence, and shows a "system of intent" living graph, tribal-knowledge layer and SME agents, plus failure lessons on substrate-level controls.

- Techniques: Living system-of-intent graph with human-gated edits; Rule-based conflict detection instead of LLM-based; Scoped spec hierarchy with file isolation per agent; Block forbidden actions at the system level, not per tool; Alignment-focused evaluation grid; Domain-specific SME agents instead of one general agent

## [Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked](../videos/HvMyYLTfvhg.md)
`HvMyYLTfvhg` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: context-engineering, agent-architecture, mcp-and-tools

Jeff Ng (Unblocked) argues agent infrastructure is now easy to assemble, so the real gap is organizational context. He demos a context engine that feeds agents synthesized, permission-scoped knowledge instead of raw MCP results.

- Techniques: Durable per-step checkpoints for agent runs; Isolated sandboxes for agent and third-party code; Context engine queried before the agent reasons; Synthesized context over raw tool results
- Tools: Cloudflare, Vercel, Mastra, Flu (transcript spelling of the framework), Linear, Slack, GitHub MCP, Claude Code, Codex, Unblocked context engine

## [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](../videos/xLUQOqjudtA.md)
`xLUQOqjudtA` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, context-engineering, software-factory

Tolan's engineers explain how a voice-first AI companion needs sub-two-second turns, stakes-based model routing, retrieval-style memory, and per-turn context rebuilding, plus how they use Claude agent fleets to ship iOS code.

- Techniques: Smart turn-taking from speech patterns; Per-stage latency instrumentation; Stakes-based model tiering with a cheap per-turn router; Retrieval-based memory with nightly consolidation; Stable-versus-volatile memory blocks; Character identity held separately from tone; Multi-judge eval loop for persona changes; Agent fleet with reviewer and PR-shepherd roles
- Tools: Claude, GPT-5.1, OpenAI Responses API, MCP, Linear, Sentry, Datadog, App Store

## [Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS](../videos/gxVZ_1tuuq4.md)
`gxVZ_1tuuq4` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: agent-architecture, infra-cost-scaling

AWS's Mike Chambers argues that an agent minus its model is the harness, and that agents built for many users should split the loop, memory, identity and tools into separately scaled parts, demoed on Bedrock AgentCore.

- Techniques: Split agent components for independent scaling; Session manager for cross-invocation state; Local dev loop that mirrors production; Declarative harness config; Agent-generated infrastructure as code
- Tools: Amazon Bedrock AgentCore, AgentCore CLI, Strands Agents SDK, Kiro, Claude Code, Cursor, MCP, AG-UI, AWS agent toolkit, Sonnet 4.5

## [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](../videos/hD9-V56FNRI.md)
`hD9-V56FNRI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, security-guardrails, observability

Talk arguing that once agents call tools and change state, they are distributed systems, so they need idempotency, compensation, scoped permissions, bounded retries and per-step traces.

- Techniques: Idempotency keys plus status lookup on every side-effecting tool; Persist each loop step and define compensation operations; Retry and fanout guardrails; Scoped credentials and tool allowlists; Parameter-bound, expiring human approvals; Memory as a cached, provenance-tagged store; Tool contracts with schemas and idempotency
- Tools: Replit AI agent (cited as a production-database deletion incident; not a tool under review), Air Canada chatbot (cited as an incorrect-refund incident; not a tool under review)

## [Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](../videos/0uC6u0lJJl4.md)
`0uC6u0lJJl4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: governance-compliance, security-guardrails

Tanmay Gopal (PromptQL) on why a shared company brain leaks secrets and how to gate it: one company-wide markdown wiki with per-page scopes, human-approved agent suggestions, and user credentials injected at tool execution.

- Techniques: Single linked markdown wiki with per-page scopes; Agent suggests, human accepts; Attribute every wiki change to a named human; Per-request user credential injection at the HTTP and SQL layer; Proxy and virtualize real-data access
- Tools: Claude Code, Slack, GitHub, OpenTelemetry, Opus 4.5, PromptQL, Hasura GraphQL engine

## [Pinecone 2.0 — Edo Liberty, Pinecone](../videos/IN-rb-9WmiY.md)
`IN-rb-9WmiY` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: rag-retrieval, context-engineering

Pinecone's Edo Liberty argues agents need a persistent, domain-owned company knowledge layer (Nexus) that goes beyond RAG, with query-time code generation and budgeted queries. Mostly a product pitch with vendor-reported numbers.

- Techniques: Manifest-declared knowledge base; Curate-on-ingest; Budgeted agent queries; Query-time code generation over a knowledge layer; Compact interface spec in place of tool sprawl
- Tools: Pinecone Nexus, vector database, SQL tables, graph database, markdown notes

## [No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle](../videos/jA_x7F8caHI.md)
`jA_x7F8caHI` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: agent-architecture, multi-agent, enterprise-adoption

Oracle's Kay Malcolm argues that agent harnesses need shared, database-backed memory, using a five-type memory taxonomy and a team memory broker; mostly a product pitch for Oracle AI Database.

- Techniques: Five-type agent memory taxonomy; Shared memory broker tied to repo state; Keeping context alongside commits; Single-store consolidation for agent memory; Private local model for memory extraction
- Tools: Oracle AI Database 26AI, Oracle Agent Memory SDK, Codex, Claude, Git, Neo4j, Redis, OCI Always Free

## [PrimeAgent + Opus 5 is INSANE (Why I Dropped Claude Code)](../videos/kg3MmLd0qEM.md)
`kg3MmLd0qEM` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: coding-agents, agent-architecture, skills-self-improvement

A Kai Explains review of Prime Agent, an open-source MIT terminal coding harness with cross-session learning, paired with Claude Opus 5 as a Claude Code replacement; the self-reported benchmarks are flagged as unverified.

- Techniques: Learned-layer self-improvement over an immutable base prompt; Persistent goal with bounded autonomous run; RLM-style context management; Per-task effort dial; Model-agnostic routing with self-hosting; Container isolation for self-modifying agents
- Tools: Prime Agent (Prime Intellect, MIT, open-sourced 2026-08-05), Claude Opus 5 (released 2026-07-24), Claude Code, Cursor, Cline (transcribed as 'Klein'), Claude Fable 5, GPT 5.6 Sol, vLLM, Ollama (transcribed as 'Alama'), LM Studio, FrontierBench v0.1, ARC-AGI-3

## [China Just Open-Sourced Humanlike Memory for AI Agents (Tencent DB)](../videos/W3yHP9_jYNk.md)
`W3yHP9_jYNk` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: context-engineering, token-cost-efficiency, agent-architecture

Teardown of Tencent's open-source agent memory plugin: folding tool output into disk files plus a layered memory store. Claims 33% to 50% pass rate with 61% fewer tokens, which the speaker partly rechecked.

- Techniques: Offload tool output to disk with an ID-indexed map in context; Pressure-scaled folding; Layered consolidation memory; Persona-first recall; Keep the memory prefix cache-stable; Treat shared memory writes as untrusted input; Recompute vendor benchmark tables
- Tools: Tencent Cloud memory plugin (MIT, GitHub, about 10k stars in four months; the repo name is not stated), OpenClaw (install target, one command), SQLite (default local store), Tencent Cloud Vector database backend, Chroma (context-rot study), Mermaid (diagram format for the in-context map), Mem0 (published its own memory benchmark, per the speaker), Zep (published a rebuttal, per the speaker), WideSearch (ByteDance Seed benchmark), WeBench (name as transcribed), SWE-bench (token columns checked by the speaker), PersonaMem (persona benchmark)

## [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j](../videos/Q0VkgCyNVUg.md)
`Q0VkgCyNVUg` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: rag-retrieval, context-engineering

Neo4j's Stephen Chin argues agent memory stored as markdown or vector lookups fails on multi-hop questions, and shows a live home-lab demo where a vector-seeded graph traversal beats a vector-only store.

- Techniques: Vector-seeded graph traversal; Graph as the agent's write target; Inspect-and-fix retrieval loop; Let the coding agent write the graph layer; Same-source backend A/B test; Keep destructive memory tools away from the agent
- Tools: Neo4j, Cypher, Cognee, OpenClaw, Goose, Hermes Agent, pgvector, LanceDB, Claude, Proxmox, pfSense, HAProxy

## [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](../videos/Btk8wDUVs74.md)
`Btk8wDUVs74` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: context-engineering, data-engineering, product-ux

monday.com's Omri Bruchim and Tomer Ast argue agents fail because they lack understanding, not data, and describe a two-speed "world model" of the user (slow learned profile plus fast live signals) built ahead of time.

- Techniques: Two-speed user model (slow profile + fast signals); Precompute meaning ahead of time, recompute a thin slice at serve time; Source isolation with fallback to last verified context; Urgency gating for proactive notifications
- Tools: monday.com Sidekick, Monday Vibe, Monday Agent, Monday Workflows, Slack, Claude, Gemini, GPT

## [Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla](../videos/B8l81jhvHbI.md)
`B8l81jhvHbI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, evals, enterprise-adoption

Ishita Daga (Tesla) argues enterprise data agents fail from ambiguity, staleness and team-level preference, not model size, and proposes a tiered source-of-truth structure, a context lifecycle, and open questions on preference.

- Techniques: Tiered source-of-truth hierarchy; Context lifecycle with live sources and event logging; Replay-based evaluation of recent questions; Metric variants in a semantic layer with user selection
- Tools: mem0, Tableau, dbt, GitHub, memory.md files

## [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../videos/iqloyWCGYQQ.md)
`iqloyWCGYQQ` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, models-research, training-finetuning-rl

Parth Asawa (UC Berkeley) argues that standard LLM benchmarks test models with memory wiped each time, and proposes measuring continual learning through sequential tasks, gain over a stateless baseline, and Pareto reporting.

- Techniques: Paired stateful vs stateless runs (gain metric); Benchmark design checklist for continual learning; Multi-axis Pareto reporting; Mid-sequence concept drift injection; Stability vs plasticity failure triage

## [Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi](../videos/s67bE2Ur3bY.md)
`s67bE2Ur3bY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, multi-agent

Sai Krishna Rallabandi on moving agents from one-user assistants to group-chat and wearable agents. Covers the security boundary, memory curation and forgetting, privacy as context, and when to speak.

- Techniques: Action-boundary deterministic guard; Data/instruction channel split with a trained SLM; Atomic fact extraction with hierarchical and temporal links; Continuous relevance scorer for forgetting; Per-user LoRA adapters over a shared memory layer; KV-cache aware memory ingestion; Learned speak/stay-quiet classifier; Private routing via DM
- Tools: LoRA, SLM classifier, regex and traditional NLP guards

## [When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain](../videos/bUJgirn4_yc.md)
`bUJgirn4_yc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: data-engineering, agent-architecture

DataChain's Dmitry Petrov argues coding agents need a "data harness" for physical and unstructured data (video, sensors), built on Pydantic schemas, incremental checkpoints and reusable derived datasets.

- Techniques: Pydantic schema as the only data model; Typed mapper and generator functions for parallel processing; Incremental runs with checkpoints; Check for an existing derived dataset before computing; Per-dataset knowledge note with lineage
- Tools: DataChain, Pydantic, Claude Code, YOLO, Ray, Spark, Dask, Git4Data

## [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](../videos/khVX_BUnEwU.md)
`khVX_BUnEwU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, skills-self-improvement, multi-agent

Yohei Nakajima presents Active Graph, an experimental event-sourced graph runtime where an immutable typed log is the agent's ground truth and small behaviors coordinate through shared state; main takeaway is that log-centric design gives replay, forks, resume and gated self-modification for free.

- Techniques: Log-as-memory retrieval; Graph-subscription behaviors and graph-query views; Failure-type-scoped, gated self-edits; Acceptance test by simulated win rate with a confidence bound; Debug by querying the event log, not session logs; Pack-based composition of agents
- Tools: Active Graph, BabyAGI, LongMemEval, Replit, Claude Code, LangSmith (mentioned as a comparison), Kaggle Pokemon trading card game competition

## [Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](../videos/mOf-PP4mVjA.md)
`mOf-PP4mVjA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: rag-retrieval, voice-multimodal, agent-architecture

TwelveLabs' James Le argues video needs a persistent memory layer (a context graph over moments, entities and relationships) rather than frame sampling, search or long context, and demos a video agent called Jockey.

- Techniques: Context graph over video moments; Ingest once, reason many times; Timestamp-grounded outputs; Intent-configurable extraction; Video worker harness; Evaluate retrieval, synthesis and budget separately
- Tools: TwelveLabs Marengo (multimodal embeddings for spatial-temporal spans), TwelveLabs Pegasus (video-aware language model used as the reasoning layer), Jockey (TwelveLabs video agent product used for the demos)

## [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../videos/R3-anFK1YM8.md)
`R3-anFK1YM8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, evals, local-ai

Sakana AI researcher on memory harnesses for long-horizon research agents running on local models; a ranked decision-ledger recall policy beat both no memory and plain vector RAG, at lower cost.

- Techniques: Write-manage-read memory loop; Ranked decision-ledger recall; Recall-mode ladder with an oracle; Ablate with wrong and recent memory; Local, controlled eval pipeline
- Tools: DeepSeek V4 Flash, Qwen (4-bit quantised), XBench, vector RAG, Spyder V2 benchmark

## [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../videos/CvRngaQZQ3Y.md)
`CvRngaQZQ3Y` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, evals, training-finetuning-rl

LangChain's Vivek Trivedy argues agent improvement is a data-mining loop: ship, collect traces, mine them, then run data-driven experiments on prompts, tools and models.

- Techniques: Agent-driven trace mining; Frontier-to-open-model downgrade via trace judging; Distillation from good traces; Evals generated from traces; Score-driven auto-research loop; Harness, then fine-tune, then harness sandwich; Human review summaries
- Tools: LangSmith, LangSmith Engine, Deep Agents, Claude Code, Codex, Terminal Bench, scikit-learn

## [Scaling Compute on Context — Jack Morris, Engram](../videos/WiqDvX6isc4.md)
`WiqDvX6isc4` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: training-finetuning-rl, models-research, context-engineering

Jack Morris (Engram) frames "scaling compute on context": with a fixed private dataset and a pretrained model, the only scaling axis left is compute, and he surveys why naive, compaction, distillation, synthetic-data and RL approaches all saturate.

- Techniques: Naive continued training on a private corpus; KV compaction of in-context data; On-policy distillation toward in-context behaviour; Self-study (generated QA conditioned on the corpus); Synthetic continued pretraining; Unsupervised RL environments over the corpus; Gradually harder self-generated curriculum
- Tools: Cartridges (self-study paper, named on slide), On-policy distillation, GRPO (named as an RL loss example), KV cache compaction (named approach)

## [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j](../videos/VGN22pPpb-8.md)
`VGN22pPpb-8` · AI Engineer · 2026-08-18 · q2 · intro · keynote · also: data-engineering, multi-agent

Neo4j keynote arguing that agents should be thin and share an ontology-based semantic layer over enterprise data, with execution traces that teach source selection over time.

- Techniques: Business-to-technical ontology mapping; Process graph for process-guided agents; Trace-derived source scores; Thin agents over a shared substrate
- Tools: Neo4j

## [Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog](../videos/wEc9aG7cRQc.md)
`wEc9aG7cRQc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, security-guardrails

Diane Lin (Datadog) on why LLM agents give different verdicts on the same input near the decision boundary, and how to fix it with disagreement-driven active learning plus episodic and semantic memory instead of fine-tuning.

- Techniques: Measure consistency with repeated runs; Disagreement-based query selection; Semantic memory for policy and preference facts; Episodic memory as case-based precedent lookup; Active-learning loop with memory updates
- Tools: Datadog

## [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../videos/I3bpdgFJCUY.md)
`I3bpdgFJCUY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, skills-self-improvement, agent-architecture

Ben Holmes (Warp) shows a markdown-first personal knowledge base: voice-dictate raw notes, have an agent enrich and link them, generate wikis, run it on a cloud schedule, and build graph views with HTML.

- Techniques: Enrich-note skill with a processed-timestamp marker; Controlled tag vocabulary with a no-invention rule; Backlinks via key-term search over a file tree; Raw folder to wiki generation; Sync-in, run, sync-out cloud schedule
- Tools: Obsidian, Obsidian Headless CLI, Warp, oz.dev, Hubble, Claude, Codex app, Exa, Tailwind CSS, Whisper Flow, Handy, GLM 5.2

## [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../videos/I6aiEf3aEFQ.md)
`I6aiEf3aEFQ` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: skills-self-improvement, agent-architecture

Yu Su (Ohio State, CEO of NeoCognition) argues intelligence and expertise are different axes and that continual learning, not bigger models, is what turns agents into domain experts.

- Techniques: Adaptive compression loop for agent memory; Rules stored with preconditions and exceptions; Select context by expertise instead of parallel brute force; Measure expertise per environment

## [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../videos/5ZGyKWjQDr0.md)
`5ZGyKWjQDr0` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: context-engineering, product-ux, agent-architecture

Shlok Khemani traces how ChatGPT and Claude memory evolved from 2024 to 2026, and argues memory is a product and compute problem, not a RAG problem, with context as the real cap.

- Techniques: Running profile with background re-synthesis (dreaming); Search tools over past conversations instead of stored facts; User-visible and user-editable profile with re-synthesis on edit; Dense keyword-clue memory entries; Timestamped memory entries
- Tools: ChatGPT, Claude, Gemini, Poke, Claude Code, OpenClaw, Hermes

## [Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI](../videos/H7puB0RwJMM.md)
`H7puB0RwJMM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: data-engineering, governance-compliance

Daniel Chalef (Zep) on why LLM-built knowledge graphs need provenance modeled as a graph, covering lineage through merges, contradictions, tagging, and deletion.

- Techniques: Provenance as graph edges; Merge-safe lineage; Ingestion-time tagging with inheritance; Lineage-based deletion; Single-shot extraction plus deterministic dedupe
- Tools: Graphiti, Zep, Vector similarity search, Full-text search, BFS graph traversal

## [Claude for Long-Horizon Tasks — Lance Martin, Anthropic](../videos/9QebvrrY3KY.md)
`9QebvrrY3KY` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: agent-architecture, multi-agent, context-engineering

Lance Martin (Anthropic) on designing long-horizon async agents: decouple brain from hands, verify in a separate context, dream offline to fix memory, and run org-level shared harnesses.

- Techniques: Brain/hands split with an append-only session log; Non-destructive context via append-only session object; Build/verifier loop in separate contexts; Dreaming: offline memory consolidation; General memory substrate with the model managing its own structure; Org-level shared harness with its own identity
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, Claude Tag, Message API, Continued Learning Bench, METR time-horizon benchmark, Slack

## [LLM Wiki + OKF Every Local AI Now Shares ONE Memory](../videos/9ciGYHHOLyU.md)
`9ciGYHHOLyU` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: mcp-and-tools, context-engineering, local-ai

A solo builder turns Karpathy's LLM-wiki idea and Google's OKF spec into a deterministic, local MCP memory layer, then documents the failures that showed up with a local model.

- Techniques: Librarian agent over a deterministic markdown store; Seed memory in MCP instructions and tool descriptions; Enrich-before-create and bidirectional linking rules for memory writes; Deterministic graph lint for orphans and broken links; Contradiction handling by rewrite, not append; Give the memory a model that makes write decisions well
- Tools: Karpathy LLM wiki (concept), Google OKF spec, MCP, llama.cpp server, llamaswap2, Qwen3 30B-A3B, Gemma 12B, Claude Opus (cited as the level of model needed for spec-following), Author's own memory tool, with web UI and graph visualizer (open source, link in description, not named)

## [5 Open Source AI Tools That Feel ILLEGAL To Know About](../videos/-UxcljWN49I.md)
`-UxcljWN49I` · Kai Explains · 2026-08-02 · q2 · intro · review · also: agent-architecture, coding-agents, voice-multimodal

Roundup of five open-source agent building blocks (Browser Use, Firecrawl, Mem0, OpenHands, Dify) mapped to read, act, remember, code and orchestrate roles. Mostly star counts and vendor stats, with no hands-on steps.

- Techniques: Read-decide-act browser agent loop; Scrape-to-markdown before retrieval; Two-phase memory: extract on write, retrieve on read; Sandboxed plan-write-test-iterate coding loop; Per-step tracing and worker queues for visual workflows
- Tools: Firecrawl (transcribed 'fire crawl'), Browser Use, Mem0 (transcribed 'Memzero'), OpenHands (transcribed 'open hands'), Dify (transcribed 'DeFi'), Devin (transcribed 'Devon'; Cognition AI, mentioned as a $500/month closed product), WebVoyager (benchmark, 586 tasks), SWE-bench (benchmark), Langflow (mentioned as Dify's origin comparison), OpenTelemetry (Dify export)

## [LangChain Open Sourced Claude Code (Works With ANY Model)](../videos/jtWjkdBNqlk.md)
`jtWjkdBNqlk` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: agent-architecture, multi-agent, claude-code

Kai Explains reviews LangChain's open-source DeepAgent, a model-agnostic take on Claude Code's harness, arguing it wins for shipping agents to users while Claude Code still wins for personal terminal coding.

- Techniques: Audit your harness against the five-part checklist; Subagents with isolated context returning one summary; Keep agent memory in a store you control; Swap the model behind a fixed harness; Use a lighter agent abstraction for bounded tasks
- Tools: DeepAgent (Deep Agents, LangChain), LangChain 1.0, LangGraph, LangSmith deployment, Claude Code, Claude Opus 4.8 (as stated), Claude Managed Agents, Codex, Cursor agent mode, GPT 5.5 (as stated), PostgreSQL, agents.md

## [Graphify + Obsidian is INSANE: Build an AI Second Brain That Never Forgets](../videos/8Kv2tn22QNo.md)
`8Kv2tn22QNo` · Kai Explains · 2026-08-02 · q3 · intro · review · also: context-engineering, rag-retrieval, token-cost-efficiency

Walkthrough of Graphify, which builds a queryable code and docs graph, paired with Obsidian as a markdown second brain; the useful parts are provenance labels, tiered data egress, and the lint maintenance loop.

- Techniques: Persistent codebase graph, queried by traversal instead of re-reading files; Provenance labels on every derived link (Extracted / Inferred / Ambiguous); Tiered data egress across ingestion sources; Three-layer LLM wiki (Karpathy design); Anti-fabrication rule and weekly lint loop for an AI-maintained notes vault; Staged write access to an Obsidian vault
- Tools: Graphify, Obsidian, Claude Code, Codex, Cursor, TreeSitter, faster-whisper, Neo4j, MCP (Model Context Protocol), Claudian (Obsidian plugin for Claude Code), Smart Connections (Obsidian plugin), Khoj (self-hosted Obsidian plugin)

## [Context Window Lie | Why AI Doesn't Actually Remember (ChatGPT, Claude & Gemini)](../videos/Nf8j9w523pw.md)
`Nf8j9w523pw` · Kai Explains · 2026-08-02 · q3 · intro · talk · also: context-engineering, token-cost-efficiency

Explainer arguing a context window is a finite reading limit, not memory: models re-read the whole transcript each call, attention favors the start and end, so reliable agents budget context deliberately.

- Techniques: Itemized context budget audit; Rolling summarization of old turns; Just-in-time file and tool injection; Position-aware instruction placement; External notes injected at conversation start; Pair large windows with retrieval, summarization and prompt caching
- Tools: ChatGPT, Claude, Gemini

## [Every company should have a Brain — Garry Tan, Y Combinator](../videos/eBUyTS7SzV4.md)
`eBUyTS7SzV4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, skills-self-improvement, enterprise-adoption

Y Combinator's Garry Tan argues that AI productivity comes from how work is wired (skills as employees, routing tables, company memory with hygiene), not the model, and pitches an open-source "company brain" called GBrain.

- Techniques: Skill file as a single-job employee; Resolver table for routing context; Trigger evals on routing; Skillify at task end; Split latent and deterministic compute; Curated company brain; Select a small working set per task
- Tools: Claude Code, Codex, OpenClaw, Hermes agent, GBrain, Postgres, TypeScript, Markdown skill files

## [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../videos/2IxD9OB3XuQ.md)
`2IxD9OB3XuQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: skills-self-improvement, evals, context-engineering

Soheil Feizi (RELAI) argues agents should learn from production failures only through verifiable updates: turn logs into replayable test environments, route fixes to model, harness or memory, and gate each change with regression tests. Second half is a product demo.

- Techniques: Log-to-replayable-environment lift; Instruction-first environment bootstrap; Three-gate fix verification; Layer routing by smallest durable change; Regression-aware optimization; Regression trap in benchmark design; Reviewable change proposal as output
- Tools: RELAI Rely (rely optimize CLI), GEPA, Letta, mem0, LoRA, DPO, GRPO, RLVR, SFT

## [WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar](../videos/8G_1-3IO4ZQ.md)
`8G_1-3IO4ZQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, skills-self-improvement, enterprise-adoption

Atlan's founder argues production agents fail on missing business context, not model intelligence, and proposes a shared, versioned "context layer" (a company brain) that agents draw from.

- Techniques: Jobs-to-be-done scaling factor for agent selection; Shared context layer as a company brain; Context lifecycle management like software; Trace-driven maintainer loop; Reverse-construct the data stack to bootstrap context
- Tools: Claude Code, Codex, Claude Cowork, Google ADK, Glean, Relevance AI, MCP, Qualified, Artisan

## [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](../videos/ZRM_TfEZcIo.md)
`ZRM_TfEZcIo` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: rag-retrieval, context-engineering

Two builders show a file-based personal research system: raw sources, an index.yaml catalog and an LLM-written wiki, queried in tiers and fed by every question. No vector DB needed.

- Techniques: Tiered index-first retrieval; Immutable raw layer with LLM-owned derivatives; Query write-back with a log; Seeded multi-round deep research; Depth knob for research runs; Repo ingestion into per-repo and cross-repo notes
- Tools: Obsidian, Readwise, NotebookLM, Notion, Google Drive, Granola, Claude Code, Codex, Gemini Deep Research, Gemini (grounded Google search), Bright Data, YAML

## [A Genius With Amnesia - Victor Savkin, Nx](../videos/jVjt-2g8NMY.md)
`jVjt-2g8NMY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, agent-architecture

Victor Savkin (Nx) argues coding agents are limited by seeing one repo and forgetting past sessions, and shows Polygraph, a meta-harness that builds a cross-repo dependency graph and replays captured sessions on other machines.

- Techniques: Out-of-band cross-repo dependency graph; Multi-repo session as one unit of work; Session state replay for handoff; Intent-based scope selection; Agent-agnostic meta-harness
- Tools: Polygraph, Nx, Claude Code, Codex, GitHub

## [User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](../videos/Jx4ZFEAq6bY.md)
`Jx4ZFEAq6bY` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: rag-retrieval, skills-self-improvement, evals

StarlightSearch's CEO argues agent memory should learn from outcomes: utility-weighted retrieval, reasoning-style memories, and consolidation into skills. Product-pitchy, with self-reported benchmarks.

- Techniques: Utility-weighted memory retrieval; Human failure report as a memory write; Memory as procedure, not fact; Consolidate memories into skills; Runtime learning vs compile-time optimization
- Tools: Reflect (StarlightSearch's memory system), Mem0 (transcribed as 'memzero'), DSPy, ReAct, Pinecone (cited in a post, not used)

## [The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft](../videos/jtzh-GBXBWc.md)
`jtzh-GBXBWc` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: multi-agent, skills-self-improvement, enterprise-adoption

A 100-person Indian thermoforming-machine maker built a 36-agent go-to-market "brain" with layered memory and a nightly dream cycle, with no training and no framework. The talk is a company story with some architecture and cost claims.

- Techniques: One-job specialist agents with an orchestrator and debate; Layered agent memory with a salience gate and correction precedence; Nightly consolidation (dream cycle) job; Rules file as production guardrails; Chunk-and-extract over a private corpus with no training; Draft-only outbound with human send
- Tools: Cursor, vector database, graph database, CRM, Google Workspace integrations, document ingestion tooling, monitoring tooling

## [PAI: The Life OS for AI-Powered Development](../videos/JukZ7WWtOSg.md)
`JukZ7WWtOSg` · Better Stack · 2026-07-02 · q3 · intro · review · also: claude-code, skills-self-improvement, context-engineering

Better Stack reviews PAI (Personal AI Infrastructure), a memory-and-skills operating layer on Claude Code. Its value is cross-session continuity; it needs terminal comfort and ongoing upkeep.

- Techniques: Persistent project memory loaded every session; Planning prompt that requires risks, assumptions and verification; One custom skill per role or review type; Fixed action order through a multi-step process
- Tools: Claude Code, PAI (Personal AI Infrastructure), Pulse (PAI local dashboard), Telos (PAI goals/ideal-state file, as named in the video), Fabric (named as a prior project of the PAI creator), SecLists (spelled 'SecList' in captions; named as a prior project of the PAI creator), LangChain (compared against), CrewAI (compared against), Next.js (example skill domain)

## [Hermes Agent under Claude Code Is Insane](../videos/Sb96po6S67k.md)
`Sb96po6S67k` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: claude-code, skills-self-improvement, mcp-and-tools

Setup-and-use walkthrough for running the Hermes agent alongside Claude Code: Hermes adds persistent memory and self-evolving skills, and can run as an MCP server, cron-driven monitor, or Claude Code launcher.

- Techniques: Install Hermes and run the manual setup; Onboard Hermes with your context; Expose Hermes to Claude Code as an MCP server; Cron-driven living PRD skill from a Slack channel; Delegate feature work to Claude Code from a Hermes channel; Health-check skill loop for a deployed app
- Tools: Hermes Agent (Nous Research), OpenClaw, Claude Code, Claude Code subscription / non-interactive mode, Anthropic Agent SDK credit (policy claim), hermes setup command, hermes mcp serve command, .mcp.json, user.md and memory.md (Hermes memory files), soul file (Hermes agent personality/instructions), Hermes Skill Hub, Hermes bundled Claude Code skill

## [MemPalace: The Tool That Makes Claude Stop Forgetting](../videos/kRACHOx1p8s.md)
`kRACHOx1p8s` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: claude-code, context-engineering, mcp-and-tools

Better Stack demos MemPalace, a local tool that stores coding-agent conversations verbatim and exposes them to Claude Code over MCP so decisions persist across sessions.

- Techniques: Verbatim store plus compact index; Local project memory setup; Claude Code plugin with a memory protocol; Run alongside context mode; Load pointers instead of project lore; Install hygiene for memory tools
- Tools: MemPalace (mempalace; spoken as Mem Palace; version not stated), uv, pip, ChromaDB, SQLite, MCP (Model Context Protocol), Claude Code (captioned as Cloud Code), Claude Code hooks and plugin, context mode, Memzero, Zapp (transcript spelling; product name unverified)

## [Google Replaced The Karpathy's LLM Wiki](../videos/k4sMSsMzX2g.md)
`k4sMSsMzX2g` · AI LABS · 2026-07-02 · q2 · practitioner · review · also: context-engineering, rag-retrieval, claude-code

AI LABS walks through Google's Open Knowledge Format (OKF), a folder, index.md and YAML-frontmatter convention for markdown knowledge bases, and reports a small team test with lower token use and faster lookups.

- Techniques: Index.md per folder as the agent's entry point; YAML frontmatter with name, description and type on every concept document; Script-first markdown-to-OKF conversion with evals; CLAUDE.md navigation section that documents the bundle; Trial on a Git branch and visualize the bundle
- Tools: Open Knowledge Format (OKF, Google), BigQuery, Claude Code, CLAUDE.md, Obsidian (comparison only), Git / GitHub, Karpathy LLM-wiki pattern (concept, not a product), Google design.md standard (named in passing), Mobbin MCP (sponsor), Cursor, Lovable, v0 (named in sponsor segment), Markdown to OKF skill (the team's own, unnamed script)

## [6 Insane Hermes Agent Use Cases That You Need Right Now](../videos/qMEm1bgxnUM.md)
`qMEm1bgxnUM` · AI LABS · 2026-07-02 · q2 · intro · review · also: token-cost-efficiency, agent-architecture, skills-self-improvement

Walkthrough of six Hermes Agent use cases: cron jobs gated by a wake flag or a no-agent flag, a Slack team second brain, Gmail lead webhooks, PRD-as-skill competitor tracking, and human-reviewed social posting.

- Techniques: Pre-LLM gating with a wake-agent flag; No-agent cron jobs for deterministic checks; Ask the agent to build the automation from a prompt; Draft-then-publish content skill with human review; PRD as a skill plus scheduled research; Gmail lead-triage webhook; Profiles for isolated personas
- Tools: Hermes Agent (desktop app and TUI), OpenClaw, Claude Code (transcribed as "clawed code"), cron, Slack, Stripe, Stripe MCP, AWS, Gemini API, Google Play API, Gmail, Google Cloud

## [Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j](../videos/abvQEhvRI_c.md)
`abvQEhvRI_c` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: agent-architecture, context-engineering, rag-retrieval

Neo4j speakers argue agents need context graphs that store policies and rules as well as facts, so they can make and record decisions. They give a decision framework: frame, check global rules, assess risk, propose, then act, defer or escalate.

- Techniques: Propose, then decide, as two agents; Pre-decision risk screen; Decision log as a graph of precedent; Tiered memory in one graph; Framework as a skill or graph workflow
- Tools: Neo4j, Text2Cypher, LangGraph, ADK

## [Stop babysitting your agents... — Brandon Waselnuk, Unblocked](../videos/BiG2ssibKGc.md)
`BiG2ssibKGc` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: context-engineering, rag-retrieval

Unblocked's Brandon Waselnuk argues agents need a runtime context engine, not more MCP access or static docs: exhaustive retrieval, surfaced conflicts, a social graph, and hard-won lessons.

- Techniques: Exhaustive retrieval before first-hit answers; Research packet before planning; Expert / social graph built from the code repo; Surface conflicts instead of silently picking; Permission-preserving delivery over MCP; Confidence-gated auto-answering; No answer caching for latency
- Tools: Claude Code, MCP, Codex, Anthropic API, AWS Bedrock, CLAUDE.md, AGENTS.md, Zendesk, Slack, Microsoft Teams

## [Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j](../videos/B9h9ovW5H9U.md)
`B9h9ovW5H9U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: rag-retrieval, context-engineering, data-engineering

Neo4j's Zach Blumenfeld on context graphs: why agents need stored decision traces and precedents, not just documents, plus a one-line scaffold (create-context-graph) and the Neo4j agent memory pipeline.

- Techniques: Hybrid precedent retrieval over decision traces; Scaffold a context-graph app from a domain; Staged entity extraction from text into a graph; Ontology-first graph schema generation; Separate memory stores by kind
- Tools: Neo4j, Neo4j agent memory package, Graph Data Science (GDS), Cypher, uvx create-context-graph, Pydantic AI, Claude, OpenAI embeddings, Next.js, spaCy, GLiNER, MCP

## [The End of Apps — Kitze, Sizzy.co](../videos/4fntwuOoedA.md)
`4fntwuOoedA` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: agent-architecture, product-ux, multi-agent

Kitze (Sizzy.co) on his personal-agent journey, from to-do apps to OpenClaw-style agents, and his view that apps will give way to a personal agent OS that prompts the user.

- Techniques: Nested topic description injection; Per-topic specialized agents; Labeled cron messages with full conversation context; Visible tool-call UI
- Tools: OpenClaw, Hermes, Paperclip, Codex, Claude Code, Claude Cowork, Tmux, Telegram, Discord, Tasker, IFTTT, Notion

## [How we solved Context Management in Agents — Sally-Ann Delucia](../videos/esY99nYXxR4.md)
`esY99nYXxR4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: context-engineering, multi-agent, evals

Arize's product head explains how their Alex agent escaped a context-growth loop: head/tail truncation with the middle moved to memory, long-session evals, and sub-agents for heavy data search.

- Techniques: Head + tail truncation with middle spill to memory; Reference-by-ID retrieval tool; Long-session eval (seed N turns, test turn N+1); Sub-agent for data-heavy search
- Tools: Alex (Arize's in-product agent), Arize observability platform, Claude Code (referenced, not used by speaker)

## [Connecting the Dots with Context Graphs — Stephen Chin, Neo4j](../videos/eW_vxrjvERk.md)
`eW_vxrjvERk` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: rag-retrieval, mcp-and-tools

Neo4j DevRel lead argues agents need a knowledge graph that stores short-term, long-term and reasoning memory together, so decisions can be explained and reused. Mostly a product pitch with one finance demo.

- Techniques: Three-tier memory in one graph; Vector entry point then graph traversal; Decision write-back to the graph; LLM-generated Cypher with visible query trace; Multi-source ingestion through MCP tools into a graph
- Tools: Neo4j, Neo4j Agent Memory package (open source), Cypher, OpenAI embeddings, FastRP, Leiden algorithm, MCP, Next.js, Neo4j Aura (free tier), Graph Academy

## [Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski](../videos/ohKt066uFhg.md)
`ohKt066uFhg` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: product-ux, enterprise-adoption, security-guardrails

Viktor's co-founder on building a company AI employee that lives in Slack: shared integrations, scoped access, memory across many users, and why tone and staged rollout matter.

- Techniques: Shared-integration inheritance with per-integration scoping; Thread roll-over on new DM; Treat edits and deletes as control signals; A/B test model personality, not only task scores; Staged proactivity rollout; Analytics check before acting on a claim; Browser-DOM web agent (2023 baseline)
- Tools: Slack, Viktor, OpenClaw, Claude Code, Claude Cowork, Opus 4.6, GPT-5.4, PostHog, Gmail, Meta Ads, WebArena

## [I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)](../videos/sJ2jc7leKBk.md)
`sJ2jc7leKBk` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: context-engineering, agent-architecture

An OpenClaw maintainer shows how he grew a personal agent into a life-running system step by step, using an Obsidian knowledge base, scheduled maintenance and channel-per-job routing, plus its failure modes.

- Techniques: Incremental capability ladder; Channel-per-job-type routing; Link-capture enrichment into a markdown vault; Verified overnight maintenance; Deterministic scripts beside LLM judgment; Critical-rules block high in the instruction file; Draft-don't-send attention filtering; Routine memory hygiene
- Tools: OpenClaw, Obsidian, QMD, Discord, Telegram, WhatsApp

## [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../videos/5ID22ACI7IM.md)
`5ID22ACI7IM` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: context-engineering, rag-retrieval, security-guardrails

Peter Werry and Brandon (Unblocked) argue that agents need a "context engine" that understands org history, permissions and conflicts, not just MCP access to data, then run a hands-on social-graph workshop. Much of it is product pitch.

- Techniques: Compartmentalized, permission-tagged retrieval; Ingestion-time tags plus runtime judge for conflicts; Expert graph from contribution edges; Focus-repo-biased two-stage retrieval; Feedback weighted by source trust; Split cadence by source type
- Tools: Claude Code, Cursor, Codex, GitHub Copilot, MCP, Slack, Microsoft Teams, Sentry, Datadog, GraphRAG, pgvector-style vector retrieval, Composio

## [Hermes: The Self-Improving Agent That Gets Smarter Every Day](../videos/HdxtLpL9CC8.md)
`HdxtLpL9CC8` · Better Stack · 2026-05-02 · q3 · intro · review · also: skills-self-improvement, context-engineering, token-cost-efficiency

Hands-on test of Hermes, an open-source self-improving agent from Nous Research: it stores memory and writes skills from use, and the video shows how it manages context. A single-user demo, so the evidence is anecdotal.

- Techniques: Bounded memory preload plus full-text session archive; Early, selective context compression; Periodic persistence nudge; Style-learning loop that ends in a skill; Mid-session model switch for cost
- Tools: Hermes (open-source self-improving agent, Nous Research), OpenRouter (model provider; Gemma 4 selected), Gemma 4 (default model in the demo), GLM (cheaper model used mid-session; transcribed as 'glm5 turbo'), OpenClaw (compared agent, more channels and sandboxing), NanoClaw (compared agent, built on the Claude Agent SDK), Claude Agent SDK, Claude Code (compaction threshold comparison), SuperMemory (optional external memory processor), Mem0 (optional external memory processor; transcribed as 'Memzero'), OpenViking (optional external memory processor), SQLite with FTS5 (session store and search)

## [This Tool Fixes AI Coding at Scale with 70x Fewer Tokens (Graphify)](../videos/WNru_PFycT8.md)
`WNru_PFycT8` · Better Stack · 2026-05-02 · q3 · intro · review · also: token-cost-efficiency, context-engineering, coding-agents

Better Stack demo of Graphify, a tool that builds a relationship graph of a repo and its docs so Claude Code answers from the map instead of re-reading files. Claims over 70% fewer tokens; the evidence is one small-repo anecdote.

- Techniques: Pre-built repo knowledge graph as the agent's map; Hybrid extraction: parser for structure, LLM for meaning; Label edges with provenance and confidence; Incremental re-indexing with a persisted report
- Tools: Graphify, Claude Code, Cursor, tree-sitter

## [OpenClaw Agents Just Got Better With This](../videos/JC53AcoFh-Q.md)
`JC53AcoFh-Q` · AI LABS · 2026-04-02 · q2 · intro · review · also: security-guardrails, multi-agent, skills-self-improvement

A tool roundup for hardening and extending OpenClaw agents: a security skill suite, a deterministic multi-agent workflow runner, a hybrid memory plugin, a network-API browser skill, Cloudflare hosting, a dashboard, and a curated skill list.

- Techniques: Installing a skill from git when the registry is rate-limited; Self-verifying skills: checksum check with re-download on mismatch; Scheduled security heartbeat over installed skills; Deterministic multi-agent workflow with verifier and fresh contexts; Re-ranked hybrid memory as an agent memory plugin; Replaying site APIs with cookies instead of driving a browser visually; Filtering a large skill registry before installing
- Tools: OpenClaw, ClawSec, Prompt Security, Heartbeat skill, Soul Guardian, OpenClaw Watchdog, Antfarm, Ralph Loop (creator's earlier project, per speaker), AI Dev Task (creator's earlier project, per speaker), ClawHub (skill registry), Awesome OpenClaw Skills (curated list), MemoryLanceDB Pro

## [Give Claude Persistent Memory in 5 Minutes](../videos/ryqpGVWRQxA.md)
`ryqpGVWRQxA` · Better Stack · 2026-03-02 · q2 · intro · review · also: claude-code, context-engineering, token-cost-efficiency

Shows Claude-Mem, an open-source local tool that auto-captures Claude Code session events (bug fixes, decisions, diffs) and recalls compressed context in new sessions.

- Techniques: Automatic session-event capture into a local memory store; Compressed-summary-first recall with expand-on-demand; Tag and keyword search over memories; Reproducing the demo test for a memory tool
- Tools: Claude Code, Claude-Mem (open-source Claude Code memory plugin; version not stated)

## [The Missing Layer in Your AI Stack: Supermemory](../videos/GETMfbGWc0k.md)
`GETMfbGWc0k` · Better Stack · 2025-12-02 · q2 · intro · review · also: rag-retrieval, context-engineering

Walkthrough of Supermemory, a hosted persistent-memory layer with API, SDK, and proxy "memory router" modes, demoed on a Next.js chatbot over imported YouTube stats. Vendor-led; no evaluation of recall quality.

- Techniques: Memory via proxy base URL; Scope memory with a container tag; Force memory lookup with a system instruction; Memory as an agent tool via SDK; Bulk seed from tabular data; Write chat turns back as memories
- Tools: Supermemory (memory API, SDK, memory router proxy, dashboard memory graph), SuperMemoryTools SDK package, Vercel AI SDK, Next.js, OpenAI client, GPT-4 (as the provider in the demo), CSV (ingest format)

## [Mastra: The AI Framework That Changes Everything](../videos/_dG8iZgmicQ.md)
`_dG8iZgmicQ` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: agent-architecture, mcp-and-tools

Beginner walkthrough of Mastra, a TypeScript agent framework: build an agent, add a tool, memory, working memory, an MCP server, and call it via API.

- Techniques: Minimal Mastra agent; Custom tool with zod output schema; Persistent chat memory; Working memory template; Adding MCP server tools to an agent; Calling a Mastra agent from code
- Tools: Mastra (TypeScript agent framework) and Mastra Core, Mastra CLI, Mastra playground and dev script, Mastra memory (Memory class, working memory), Mastra LibSQL storage store, Mastra MCP client, Firecrawl MCP server, zod (output schemas), Mastra Swagger API docs and Mastra client, Mastra 101 course (source of the system prompt, per the presenter), Whisper Flow (dictation, named as Whisperflow in captions), Claude Agent SDK (mentioned as the presenter's earlier video topic)

## [How to Use Cursor AI with Its Own Cursor Memory Bank](../videos/azXNHRtzd5s.md)
`azXNHRtzd5s` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: context-engineering, coding-agents

A short walkthrough of Cline's "Memory Bank" pattern: a set of structured markdown files that keep a coding agent's project context across sessions, set up in Cursor via pasted global rules. Practical but thin, with an admitted rules bug.

- Techniques: Paste a memory-bank rules file into Cursor User Rules; Initialize the memory bank with a single agent-mode prompt; Force plan-then-act with edit blocking; Keep the bank current in act mode
- Tools: Cline (Memory Bank, named 'Klein' in the transcript), Cursor (agent mode, User Rules, Cursor 2), Windsurf, Next.js, React Router, Unsplash API, Mermaid

## [Why Your LLM Answers Are Mediocre (And How to Fix It)](../videos/Ym-iMJ-sds0.md)
`Ym-iMJ-sds0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, product-ux

Beginner tips for getting better LLM answers in ChatGPT (prompting, context windows, memory, Projects, deep research, Canvas), with a brief tour of Codex, Gemini CLI and Claude Code.

- Techniques: Specific, iterated prompting; Fresh chat per idea; Project system prompt with role and sample output; Escalate from web search to deep research; Canvas for partial edits
- Tools: ChatGPT, GPT-5, Claude, Gemini, Gemini CLI, Codex, Claude Code, Nano Banana, ChatGPT Canvas, ChatGPT Deep Research, ChatGPT Projects, ChatGPT Voice Mode

## [All My AI Apps Are Connected to One MIND — With Open Memory](../videos/Y2XI2nk44WE.md)
`Y2XI2nk44WE` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools

Tutorial on Open Memory, a self-hosted shared memory server that several MCP clients (Claude Desktop, Cursor) can read and write, with setup steps and the failure modes the host hit.

- Techniques: Run Open Memory locally; Install the MCP server via generated client commands; Ingest a whole plan as one memory add; End-of-session progress checkpoint; Scope retrieval with specific project wording; Store plain-text memories, not structure
- Tools: Open Memory (Mem0 repo), Mem0, Claude Desktop, Claude, Cursor, Docker, make, OpenAI API, MCP, Next.js, React, TypeScript

## [AI Memory Explained: SuperMemory MCP for Cursor, Claude & Windsurf](../videos/mKXzPVIMFYE.md)
`mKXzPVIMFYE` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, context-engineering

Walkthrough of SuperMemory MCP: one hosted memory store shared across Cursor, Claude Desktop and Windsurf through add and search MCP tools, plus an IDE rule that auto-saves project changes.

- Techniques: Cross-client memory via a hosted MCP server; Milestone summary saved to memory; Auto-sync rule for memory updates; Resume by searching memory first
- Tools: SuperMemory MCP, SuperMemory API, Cursor, Claude Desktop, Windsurf, Next.js, React

## [Claude FINALLY Fixed AI Coding By Releasing This](../videos/oj44Vrh0XyM.md)
`oj44Vrh0XyM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, claude-code, multi-agent

Walks through four Claude Code context-engineering techniques from Anthropic's "Effective Context Engineering for AI Agents" paper: compaction, context editing and memory, structured note-taking, and subagents. Mostly a conceptual intro with small demos; the main takeaway is to pick the technique that fits the task.

- Techniques: Manual compaction with retain instructions; Persistent instruction via the # memory shortcut; CLAUDE.md as the project brief; Structured note files maintained by the agent; Coordinator plus specialist subagents
- Tools: Claude Code, Claude Sonnet 4.5, CLAUDE.md, Claude memory tool, ACI.dev Gate22 (open-source MCP gateway, sponsor), Anthropic paper: Effective Context Engineering for AI Agents

## [Introducing Open-Source PHIDATA: Your first step towards building your own AI Agents](../videos/nkh7q8WU7oU.md)
`nkh7q8WU7oU` · AI LABS · 2024-11-02 · q2 · intro · tutorial · also: agent-architecture

Walkthrough of Phidata's agent playground UI, showing how to serve agents from a local server on port 7777 and chat with them through the hosted app while memory and sessions stay on your machine.

- Techniques: Serve agents from a local server and attach a hosted chat UI; Define an agent with a description, tools and a current date; Keep session history in a local DB file and reset by deleting it; Turn on debug logs with an environment variable
- Tools: Phidata, Phidata agent UI / playground, OpenAI, Exa, DuckDuckGo search, Ollama, Python virtualenv

