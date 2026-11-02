# agent-architecture — 314 videos

*agent loops, harnesses, frameworks, durable execution, long-running agents*

By channel: AI Engineer 217 · Kai Explains 19 · AI LABS 24 · Better Stack 54

**Synthesized guide:** [guides/agent-architecture.md](../guides/agent-architecture.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Everyone Has the Same AI Models. Here's What Sets Agents Apart - Richmond Alake, Oracle](../videos/1_lX0m64-aI.md)
`1_lX0m64-aI` · AI Engineer · 2026-11-01 · q2 · intro · talk · also: memory, rag-retrieval, security-guardrails

Oracle's Richmond Alake argues agents need an "intelligence plane" (knowledge, memory, access governance, continual learning) beyond the control plane, illustrated with Oracle product demos.

- Techniques: Memory routing with a small fine-tuned decision model; Capture memory traces as fine-tuning data; Ontology and semantic layer in front of retrieval; Propagate user identity into data access; Private inference container for on-prem embeddings, LLM and rerankers
- Tools: Oracle AI Database, Oracle agent memory Python package (generates context cards), Oracle Deep Data Security, Oracle Private AI Services Container, Oracle Cloud (hosted Grok and OpenAI models), Private Agent Factory (no-code agent builder on Oracle AI Database), Memories (open-source agent memory tool built by the speaker), Qwen (fine-tuned as memory-routing decision model)

## [How to Decide What Your AI Agent Should Remember - Wojciech Pluta, Oracle](../videos/qq2Hm4XNRgI.md)
`qq2Hm4XNRgI` · AI Engineer · 2026-10-31 · q2 · intro · talk · also: memory, context-engineering, security-guardrails

Oracle's Wojciech Pluta argues agent memory is a write path that needs a promotion gate with provenance, scoped memory tiers, and per-turn context cards. Vendor talk with a demo.

- Techniques: Memory promotion gate; Provenance plus supersede, not overwrite; Three-tier memory scoping; Per-turn context card; Enforce user isolation in the database layer
- Tools: Oracle AI Database, Oracle agent memory package (named as an early-year release; no version given)

## [We Trust AI Agents That Break Every Day - Shy Ruparel, Temporal](../videos/mJ7q8CuVmbw.md)
`mJ7q8CuVmbw` · AI Engineer · 2026-10-29 · q3 · practitioner · review · also: observability, token-cost-efficiency, enterprise-adoption

Temporal developer advocate Shy Ruparel argues agent reliability is a state and recovery problem, not a model problem, and demos durable execution resuming a crashed payout workflow with a human approval.

- Techniques: Durable workflow with deterministic orchestration and recorded activities; Human approval as a signal with a long timer; Declare the retry policy once, not in loops; Degrade the AI step, not the transaction; One event history for both debugging and replay
- Tools: Temporal, Qwen (run locally as a 36B and a 9B model, per auto-captions), OpenAI Codex (cited as running on Temporal), Replit Agent (cited as running on Temporal), Keycard (talk referenced, not described)

## [AI That Hunts Logic Bugs Before Attackers Do - Taylor Luttrell-Williams, Sonar](../videos/UW8Qkk7MG8A.md)
`UW8Qkk7MG8A` · AI Engineer · 2026-10-29 · q2 · intro · demo · also: security-guardrails, pr-code-review

Sonar's SonarQube Hunter Agent: an on-demand/scheduled AI security agent that maps a repo, runs three specialized issue-class agents with adversarial validation and noise gates, and surfaces logic/authz flaws (IDOR, broken access control, business logic, auth/session) in SonarQube's normal issue list.

- Techniques: Multi-agent security scan with validation gates; Layered verification: SAST plus logic-level agent; Triage workflow for AI-raised issues
- Tools: SonarQube Hunter Agent, SonarQube (Cloud and Server), SonarQube remediation agent, SAST, SCA, OpenAI Daybreak Cyber Partner Program (frontier cybersecurity models)

## [We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI](../videos/YIhvrvHtonk.md)
`YIhvrvHtonk` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: context-engineering, memory, evals

Arize's PM on two years of shipping Alex, its in-product agent: keep the loop, plan, stop rule and memory in harness code, use small capped memory files, and treat production traces as regression tests.

- Techniques: Render the plan into the harness on every call; Explicit finish call as a harness gate; Tool results as pointers, not inline content; One small capped markdown memory file per user; Single model call instead of a loop for narrow features; Production sessions as living regression fixtures; Trace-reading agent for silent failures
- Tools: Arize AX, Alex (Arize in-product agent), Signal (Arize trace-reading agent), Sonnet 4.5 (auto-caption 'Sonic 4.5'), jq, Arize experiments

## [What Does an AI Engineer Do Now? - Aparna Dhinakaran, Arize AI](../videos/ImnZ7s68jw8.md)
`ImnZ7s68jw8` · AI Engineer · 2026-10-26 · q3 · practitioner · talk · also: software-factory, observability, evals

Arize's Aparna Dhinakaran argues the AI engineer's job is now building the build-eval-ship-monitor-improve loop itself, with always-on agents consuming telemetry and evals aligned to human judgment.

- Techniques: Telemetry-triggered always-on agent sweep; Issue memory across agent runs; Sandbox-per-run with single proxy egress; Durable agent resume; Harness and model abstraction with per-run evaluation; Evaluator alignment against golden data; Offline plus online evals on the same definitions; Trace the coding agents too
- Tools: Arize Signal, Arize Evaluator, Claude Code, Cursor, Codex, Anthropic model family (multiple models, unnamed)

## [Build Your Own Team of Managed Agents - Jack Wotherspoon, Google DeepMind](../videos/Y_p3y6zP5QE.md)
`Y_p3y6zP5QE` · AI Engineer · 2026-10-26 · q3 · intro · talk · also: sandboxing-execution, multi-agent, mcp-and-tools

Google DeepMind's Jack Wotherspoon demos Gemini managed agents: a cloud sandbox, harness and API in one call, with reusable environments for multi-agent handoff, credential-injecting proxies, and scheduled triggers.

- Techniques: Single-call managed agent; Chain turns with the interaction ID; Hand off work between agents via a shared environment ID; Narrow single-purpose agents with fan-out; Placeholder credentials with egress injection; Scheduled and webhook-triggered runs
- Tools: Gemini API Interactions API, Gemini managed agents, Antigravity harness, Gemini Flash, Gemini 4 Argonne (name as spoken in the talk), Google Search (built-in tool), remote MCP servers, agents.md, agent skills, GitHub, Google Drive, Google Docs

## [Real AI Agent Attacks and What Would Have Stopped Them — Andrey Rybka, Bloomberg](../videos/5O6jLtoeKrg.md)
`5O6jLtoeKrg` · AI Engineer · 2026-10-24 · q4 · practitioner · talk · also: security-guardrails, sandboxing-execution, mcp-and-tools

Bloomberg's Andrey Rybka walks through real agent security incidents (sandbox escape, CRM exfiltration, hidden-text injection, DNS leaks, a dropped production database) and maps each to layered controls: identity, input defense, deterministic tool brokers, default-deny egress, and budgets that halt.

- Techniques: Rule of two (capability gating for agent workflows); Deterministic invocation broker; Default-deny egress including DNS; One identity per agent, short-lived audience-bound tokens; Delayed package ingestion; Circuit breakers and halting budgets; Memory integrity and fresh-start policy; Security requirements in the spec
- Tools: MCP (Model Context Protocol) servers, OAuth, DNS, npm, NotebookLM (transcribed as 'Notebook Alarm'; likely NotebookLM), AWS accounts and GCP projects (as isolation analogies)

## [Inside Arca's Long-Horizon Agents That Run the Business - Aman Singh, Arca](../videos/oP2WLFpMoDY.md)
`oP2WLFpMoDY` · AI Engineer · 2026-10-24 · q3 · practitioner · review · also: multi-agent, memory, enterprise-adoption

Arca, an AI-native financial services firm, explains how background agents own multi-day client work through a signal system, shared plan spaces, and human pull-ins.

- Techniques: Signal-driven wake-up with interest registration; Dual wake-up: event plus timed fallback; Treat UI mutations as first-class events; One shared workspace per goal with human pull-ins; Split state by horizon: memory for later, tasks for now; Turn colleagues' reasoning into eval cases; Steer by adding a goal

## [1,368 AI Failures and What They Teach About Evals — Vishal Srivastava, New York Life & Tanmay Sah](../videos/mMw3arwQsL0.md)
`mMw3arwQsL0` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · also: evals, governance-compliance

Talk using AI Incident Database cases to argue for risk-based, system-level evals: test the whole deployment and the evaluator, try to falsify claims, and prioritize by harm.

- Techniques: Three-dimension, 13-sub-dimension incident taxonomy; Prioritize controls by harm association, not frequency; Materiality scale per AI use case; Four-part risk decomposition; System-level stress testing of the deployment; Evaluator reliability check; Build-break-fix falsification loop
- Tools: AI Incident Database (publicly available database of AI failure reports, used as the analysis corpus)

## [Is the Agent Harness Dead? — Jediah Katz, SpaceXAI](../videos/7Y4sbZgBdnc.md)
`7Y4sbZgBdnc` · AI Engineer · 2026-10-20 · q4 · practitioner · talk · also: coding-agents, context-engineering, token-cost-efficiency

Jediah Katz (SpaceXAI, formerly Cursor's harness lead) argues the agent harness is not dead: smarter models absorb coding scaffolding, but the harness keeps unlocking new frontiers, handles runtime, trust, and cost, and is moving toward agents as building blocks.

- Techniques: Two-layer harness split; Shim registry with a removal bot; Event subscription primitive; Nudge guardrails for responsiveness; Efficiency tuning levers
- Tools: Cursor, Cursor Agent Harness, GrokBot, Grind Swarm, Rollouts, Claude Code, Pi, Codex, SWE-bench Lite, MLE-bench

## [The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft](../videos/UGjk3Uk0MxM.md)
`UGjk3Uk0MxM` · AI Engineer · 2026-10-20 · q4 · practitioner · workshop · also: evals, mcp-and-tools, models-research

Hands-on workshop comparing GPT-5.5, Kimi K2.6, DeepSeek V4 Flash and Mistral Large 3 on counting, RAG grounding, vision, tool calling, agent loops, evals and DSPy prompt optimization.

- Techniques: Single-variable model swap harness; Chain-of-thought decomposition for counting; Grounded RAG prompt with explicit refusal and citation; Tool definitions as prompt engineering; Low-level tool-call loop; Force tool use over mental math; Give date math to a tool; Deterministic checks first, LLM-as-judge second; Spec-driven eval generation with Assert; DSPy with GEPA for prompt optimization; Anthropic document citations
- Tools: Microsoft Foundry, GPT-5.5, Kimi K2.6, DeepSeek V4 Flash, Mistral Large 3, OpenAI Python SDK, OpenAI Responses API, Anthropic Messages API, uv, GitHub Codespaces, LangChain v1, PydanticAI

## [How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase](../videos/_4Ph2dhmUFI.md)
`_4Ph2dhmUFI` · AI Engineer · 2026-10-20 · q3 · practitioner · talk · also: governance-compliance, evals, multi-agent

Coinbase's Evan Kormos on deciding when an agent can run unsupervised: keep the process deterministic on the outside, model it as a graph with policy boundaries, and earn autonomy per node through measured evals.

- Techniques: Policy-bounded DAG process map; Cyclic review node with a bounded loop; Per-node automation checklist; Graduated autonomy rollout; DAG state injected into agent context; Statistical evaluation over repeated runs; Exception-flow and volume monitoring
- Tools: Apache Airflow, LangGraph (transcript says LangChain Langraph)

## [Stop Telling Agents How](../videos/7T-gldvgfpo.md)
`7T-gldvgfpo` · AI Engineer · 2026-10-19 · q3 · practitioner · talk · also: context-engineering, multi-agent, evals

OpenProse founders argue agents should be given declarative Markdown contracts plus triggers, not step-by-step prompts; the talk is largely a product demo of their hosted runner.

- Techniques: Contract-first workflow spec; Codify a golden trace into pinned steps; Event-driven job = contract + trigger; Fresh-session verifier against the contract; Kernel as a bootloader index; Templated multi-agent shapes; Cheap verifier or router (planned, not shipped)
- Tools: OpenProse, run.pros.md (hosted OpenProse runner), pros CLI (pros write, pros run), npx skills (skill install mechanism), Claude Code, Codex, Exa (search), DSPy (contrasted), n8n (contrasted), pi (agent harness without sub-agents, transcribed as 'pie'), Matt Pocock's skill workflow (grill-me, TDD) used as an example, Haiku (cheaper model mentioned)

## [An AI Agent Got Its User Banned From Resy — Keycard, JPMorgan Chase & AAuth](../videos/IavxrdVnwXM.md)
`IavxrdVnwXM` · AI Engineer · 2026-10-18 · q3 · practitioner · panel · also: security-guardrails, governance-compliance, enterprise-adoption

Panel on intent-based runtime authorization for agents: per-call authz with mission context, budgets instead of rate limits, and enforcement outside the agent. Core claim: coarse OAuth scopes don't fit autonomous agents.

- Techniques: Budget-as-token grant with live feedback; Brains/hands split with egress-proxy enforcement; Separate supervising agent for worker actions; Deterministic must-never policy plus intent-derived bounds; Dynamic tool gating by task phase; Intent and environment in trace spans
- Tools: OAuth, OIDC, MCP, Claude Code, Squid proxy, Chrome, Firefox, AAuth

## [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](../videos/KtBivPzmOM8.md)
`KtBivPzmOM8` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · also: memory, context-engineering, rag-retrieval

Oracle workshop on memory-aware agent harnesses for AML: treat the harness (loop, memory tiers, skill retrieval, context budget) as the thing to engineer, not the frontier model.

- Techniques: Two-tier memory with promote-to-long-term; Vector-indexed skill and tool box with top-k retrieval; Hybrid keyword plus embedding retrieval with RRF; Compaction or summarization of old context; Skill distillation from past runs; Pre-vetted query tools instead of free-form SQL; Bounded agent loop for unattended runs; Stable request prefix for caching
- Tools: Oracle Database, OCI (Oracle Cloud), GitHub Codespaces, OpenAI chat completions API, vector store, MCP, RRF, Claude Code, Codex, Pi harness, Hermes agent, OpenClaw

## [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](../videos/kiClTcJUnhc.md)
`kiClTcJUnhc` · AI Engineer · 2026-10-17 · q4 · practitioner · talk · also: multi-agent, security-guardrails, governance-compliance

Anthropic's Claude Managed Agents "flows" (dynamic multi-agent workflows) talk: how to fan out hundreds of isolated sub-agents, control cost with budgets, and contain risk with credential vaults, egress rules and auto mode.

- Techniques: Plan, fan out, phase-gate; Per-phase model and agent-count allocation; Separate reviewer context for adversarial checks; Two-stage review with verification; Budget as a resumable circuit breaker; Credential injection at the egress proxy; Declare, contain, detect; Transcript audit agent; Gradual context reveal via linked markdown index; Filesystem as the inter-agent channel; Interrupt and redirect
- Tools: Claude Managed Agents, Claude Code, Claude API skill, ant CLI, Terraform provider for Claude agents, Dynamic workflows (Claude Code), Hill-climb skill, Dreaming (memory consolidation product), Auto mode (permission classifier), Bug Hunter flow, Explainer Video Maker flow, Claude Tag (Slack bot)

## [Stop Chatting With Spreadsheets — Francesco Galletta & Felippe Felisola Caso, Monzo](../videos/e9-br9hveRI.md)
`e9-br9hveRI` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · also: testing-verification, governance-compliance, data-engineering

Hands-on workshop on building a trustworthy financial-analysis harness around five principles (shared domain, deterministic calculations, evidence, accountability, verification), demoed on a wedding-budget planner.

- Techniques: Interview-style shared-domain planning with a decision tree; Calculation-as-code with tests and golden examples; Fact / assumption / interpretation labelling with provenance; Branching challenge agent with merge or dismiss; Tiered accountability gates
- Tools: Claude Code, Codex, Looker Studio, Google Slides, Google Sheets

## [The Highest Loop — swyx](../videos/Fva8hFosqyQ.md)
`Fva8hFosqyQ` · AI Engineer · 2026-10-16 · q2 · intro · keynote · also: enterprise-adoption

swyx's keynote "The Highest Loop" argues that core AI engineering skill is choosing which feedback loop you work in, moving up for productivity and scaling, down for reliability, and that the conference itself is the loop that makes loops.

- Techniques: Loop-level routing

## [I Spent Two Years Building the Median — Hariprasad Sudharshan](../videos/0JZy5AuuQzc.md)
`0JZy5AuuQzc` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: product-ux, infra-cost-scaling

Hariprasad Sudharshan argues that with rented models and harnesses, most AI-built products converge on a "median," so durable value needs a deliberate novelty, a strong opinion, and distribution.

- Techniques: Novelty budget; Three-question pre-build check; Separate model, harness and product in comparisons; Treat agent done as a median baseline; Self-hosting break-even calculator
- Tools: Claude Code, Codex, Cursor, Lovable, Replit, LlamaIndex, vLLM, Max plan

## [Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket](../videos/gonAewBZxfU.md)
`gonAewBZxfU` · AI Engineer · 2026-10-15 · q4 · practitioner · talk · also: rag-retrieval, evals, data-engineering

Two In The Pocket engineers describe a RAG assistant over a Belgian payment scheme's rulebooks: section-aware chunking, table flattening, hybrid retrieval, agentic narrow-to-wide tools, and noisy LLM-judge evals.

- Techniques: Section-path chunking without overlap; Table flattening for merged cells; Hybrid dense plus BM25 with RRF; Narrow-to-wide agent tool ladder; Tool-level recovery guardrails; Stream prose, render structured parts last; Lightweight feedback logging; Promptfoo end-to-end evals plus retrieval-only eval
- Tools: Qdrant, BM25, Reciprocal Rank Fusion, Promptfoo, Pydantic, LLM-as-judge

## [Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire](../videos/rAUyRDOFyHU.md)
`rAUyRDOFyHU` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: enterprise-adoption, evals, sandboxing-execution

Flywire's engineers describe Orbit, an internal platform that runs deterministic code with small LLM steps, gated by YAML definitions, per-step permissions and human-reviewed merge requests.

- Techniques: Deterministic-first workflow with scoped LLM steps; Strict JSON output schema with targeted retry; Per-step capability allowlist declared in config; Skill first, then workflow; Isolated node evaluation with production-trace golden sets; Per-step model selection; Separate orchestration, runtime and session state
- Tools: Claude Agents SDK, Claude Code, AWS ECS Fargate, AWS Lambda microVMs, GitLab, Jira, Sentry, Slack, OpenTelemetry, MCP, YAML, Victoria (internal PaaS)

## [Just-in-Time Ontologies: What Cheap Intelligence Means for Data — Hrishi Olickel, Southbridge AI](../videos/Fa3hQVIKShw.md)
`Fa3hQVIKShw` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: data-engineering, token-cost-efficiency, evals

Hrishi Olickel (Southbridge AI) argues there is no universal schema, so build just-in-time ontologies per decision, using cheap model tiers, cross-family disagreement, and a failure surface.

- Techniques: Split the job into typed cases before modeling; Fix the question definition, not the threshold; Cross-family disagreement as the audit signal; Cost-tiered checking budget; Bounded pilots, then reusable codons, then production; Pareto surfing with a fixed baseline; Check for prior-driven silent errors
- Tools: Hank Weave (captions: Hank Wave, open-source harness for headless data work), Claude Code (captions: cloud code), Opus, Anthropic Claude models (cheap reasoning tier and frontier tier)

## [Reliable, Smart Workflows for Finance, Wealth and Insurance — Karthic Rao, Perpetual](../videos/8g0g1ncwzG0.md)
`8g0g1ncwzG0` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: governance-compliance, enterprise-adoption

Karthik Rao (Perpetual CTO) on building reliable, regulated wealth-management workflows: an LLM planner emits a typed graph, a deterministic compiler fails closed, and models make only small typed judgments.

- Techniques: Planner emits typed semantic graph, compiler verifies with no model; Closed action grammar with typed contracts; Payload-hash-bound approval gates; Provisional judgments awaiting human confirmation; Side-effect lifecycle with no automatic retry; Rule-based timeouts instead of model decisions; Route judgments to a small tier and log frontier calls as training data

## [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](../videos/p7gaxmCUiIU.md)
`p7gaxmCUiIU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: skills-self-improvement, evals, voice-multimodal

Browserbase's Shubhankar Srivastava shows an auto-research loop in which a doer agent and a teacher agent iterate on a strategy file until browser-agent tasks converge into reusable skill.md files that cut cost and latency.

- Techniques: Teacher-doer auto-research loop with strategy file; Converged output as a skill.md artifact; Binary success verifier with minimal guardrails; Scheduled sample runs and failure-triggered healing; Three-layer security for learned skills; Objective choice in the teacher's criteria
- Tools: Claude Agent SDK, Claude Code, Codex, Opus 4.8, Sonnet, Browserbase browse CLI, Browserbase SDK, Stagehand, Browse.sh, WebMCP, Karpathy auto-research, OpenClaw

## [Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](../videos/FGftGOzfohc.md)
`FGftGOzfohc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: multi-agent, security-guardrails, memory

Anthropic hands-on workshop (Part 2 of 4) building a research agent on Claude Managed Agents: sub-agents, rubric-graded outcomes, vaults, shared memory, dreaming, and a map-reduce harness.

- Techniques: Rubric-gated outcome with a grader sub-agent; Placeholder secrets with domain-scoped egress swap; Context isolation via self-referencing sub-agents; Check shared memory before redoing work; Map-reduce orchestration via a custom dispatch tool; Transcript-driven memory consolidation (dreaming)
- Tools: Claude Managed Agents API, Claude Code (used to drive the workshop), SEC EDGAR Python package, MCP, Bun, npm, Agent SDK (compared)

## [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](../videos/YXiLj4tJt5A.md)
`YXiLj4tJt5A` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: security-guardrails, skills-self-improvement, mcp-and-tools

Hands-on AWS workshop: build a Strands customer-service agent with hooks (rate limit, deterministic blocks), lazy-loaded skills, steering guardrails, then deploy to AgentCore Runtime.

- Techniques: Per-request tool-call rate limiter via hooks; Deterministic input filter hook; Skills as on-demand markdown procedures; Steering handler (rule or LLM buddy); Externalised steering rules; Message-history inspection
- Tools: Strands Agents, Amazon Bedrock AgentCore (Runtime, Memory, Gateway, Observability), Amazon Bedrock, Amazon CloudWatch, AWS CDK / CloudFormation, AWS OpenTelemetry Distro, boto3, agent-control (open-source steering rules library), MCP, A2A, Jupyter / Workshop Studio

## [Hiring Employable Agents + Startup Battlefield Finals — Howie Liu, HyperAgent](../videos/EEt3ZSG4a1s.md)
`EEt3ZSG4a1s` · AI Engineer · 2026-10-12 · q2 · intro · other · also: multi-agent, product-ux, enterprise-adoption

Howie Liu (HyperAgent) argues agents are moving toward always-on "claws" that humans unblock and orchestrate, then the video covers the Startup Battlefield finals (Kamad, Common.io, Foundry).

- Techniques: Heartbeat re-invocation for always-on agents; Human approval gate on high-impact actions; Correction-to-memory loop; Specialist triage and handoff pipeline; Deny-condition state machine for agent actions; Sandbox VM per agent thread
- Tools: HyperAgent, OpenClaw, Claude Code (workflows, fan-out to parallel agents), FFmpeg, Slack, email, Gmail, Stripe, Salesforce, WhatsApp, Google Docs, GitHub

## [Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic](../videos/QSeaZ6qHyXs.md)
`QSeaZ6qHyXs` · AI Engineer · 2026-10-12 · q3 · practitioner · other · also: multi-agent, evals, sandboxing-execution

Anthropic presenters answer audience questions on Claude Managed Agents: YAML-as-code deployment, eval sweeps, tenant isolation via workspaces, long runs, and sub-agents for custom tools.

- Techniques: Agent definitions as YAML synced by CI; Parallel eval sweeps on new model releases; Historical-session eval dataset; Workspace-per-customer isolation; Rubric-based exit criteria for long runs; Coordinator with a custom-tool sub-agent; Per-thread session mapping for multi-user chat
- Tools: Claude Managed Agents (CMA), Anthropic CLI (transcribed as 'Ancho CLI'), Claude Code, Modal, E2B (transcribed as 'EB2'), Daytona, Slack

## [The Autonomous Computer: Infrastructure for Computer Use Agents — Ang Li, Simular](../videos/tyFPqtyOK5w.md)
`tyFPqtyOK5w` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: voice-multimodal, evals, sandboxing-execution

Ang Li (Simular) on computer-use agents: why reliability needs a neurosymbolic loop, where the agent writes code that is replayed, and why pass^k matters more than pass@1.

- Techniques: Neurosymbolic replay with healing; Accessibility-tree grounding with IDs; Per-step observation choice; Clarification-first prompt; Reverse-check verification of entries; Rules-first guardrail chain; Exploration swarm for changing UIs; Test-time scaling by agent count; Save-to-skill with parameters
- Tools: Simular Agent S / S2 / S3 harnesses, Simuland (open-source scripting language), Claude Code, OSWorld, OSWorld 2, Playwright, Windows 365 for agents (Microsoft), Simular cloud desktop API and CLI, GPT-4V, GPT-5, GLM 5.2

## [How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI](../videos/xn8EsW0wxyc.md)
`xn8EsW0wxyc` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: security-guardrails, observability, mcp-and-tools

Venice AI's developer-relations lead explains how secrets leak through agent architectures (logs, vaults, LLM context, tool calls) and patterns to contain them: hashed IDs, handles, narrow tool scope, and keeping credentials out of the reasoning layer.

- Techniques: Credential-in-runtime, not in-prompt; Hashed identifiers for rate limits and tracking; Split-key custody for stored outputs; Revocable handles as capabilities; Narrow tool exposure per agent; Prompt-injection classifier in front of the agent; Own the agent runtime; Verifiable private inference via TEE attestation
- Tools: Venice AI, OpenClaw, 1Password, HashiCorp Vault, Firecracker, AWS EC2, VPC, Qdrant, LanceDB, Cursor, Claude Code, MCP

## [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](../videos/Uv0nAf_7tyU.md)
`Uv0nAf_7tyU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: sandboxing-execution, context-engineering, mcp-and-tools

Anthropic engineers explain how they split Claude Managed Agents into a session log, a harness "brain" and swappable sandbox "hands", then start a hands-on workshop building a first agent.

- Techniques: Brain / hands / session split; Credential-injecting egress proxy; Append-only event log with pluggable context strategy; Lazy sandbox provisioning; One container per task; Custom tools as an event round-trip
- Tools: Claude Managed Agents, Claude Platform console (quick start), Claude Code, MCP, Sonnet 4.5, Opus 4.5, Haiku, Sonnet

## [Parameter Golf with AutoResearch — Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI](../videos/7RFJRDYroic.md)
`7RFJRDYroic` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: evals, software-factory, context-engineering

Hands-on workshop on autoresearch loops, where an agent edits code, a fixed eval scores each attempt, and only improvements are kept. Covers eval design, bounded runs, steerability and the Parameter Golf results.

- Techniques: Fixed-budget eval contract; Tree-of-attempts search with per-node diffs; Guidance file as the steering channel; Hidden validation set for contests and benchmarks; Constrained single-metric optimisation; Bridged session for direct steering
- Tools: Weco, Modal, Claude Code, Opus 4.8, OpenAI MLE-bench

## [Why I’m Switching From Python to Docker Agent for AI Agents](../videos/Mph1H5u3yeA.md)
`Mph1H5u3yeA` · Better Stack · 2026-10-12 · q3 · intro · review · also: multi-agent, mcp-and-tools

Better Stack walks through Docker Agent, an open-source Docker tool that defines agents in YAML, runs them with one command, and serves them over A2A. Demoed with an on-call incident and a Battleship match between two models.

- Techniques: Define an agent as a YAML file; Least-privilege agent split behind A2A; Serve an agent as A2A on a port; Install Docker Agent; Share an agent as an image
- Tools: Docker Agent, Docker Desktop (4.63+), Docker model runner, Docker Hub, Homebrew, A2A protocol, MCP, Claude Haiku 5.5, GPT-6 Luna, Kimi K3, OpenAI, Anthropic

## [The Apollo 11 Code Is Open Source (and it's hilarious)](../videos/ACAd_w3D-io.md)
`ACAd_w3D-io` · Better Stack · 2026-10-12 · q3 · intro · review · also: dev-tools

Walkthrough of the open-sourced Apollo 11 Guidance Computer code: 1960s hardware limits, a priority job scheduler that raised alarm 1202 under overload, restart checkpoints, and how to run it in an emulator.

- Techniques: Fixed-slot priority job scheduler with overflow alarm; Checkpoint-based restart protection; Interpreter VM to trade speed for code size; Verb/noun command language for constrained input; Reproducing Apollo 11 in the Virtual AGC emulator
- Tools: Apollo 11 source code (AGC assembly, GitHub), Virtual AGC (emulator project), DSKY keypad (emulated), VS Code, Raspberry Pi Pico (comparison only)

## [Deno Is Over (Cloudflare Shut It Down)](../videos/W_g7WKMwNeo.md)
`W_g7WKMwNeo` · Better Stack · 2026-10-12 · q3 · intro · news · also: dev-tools, infra-cost-scaling

Deno's team is joining Cloudflare. The Deno runtime gets one more year of monthly fixes, Deno Deploy shuts after six months, and Cloudflare is mainly buying the team and CellD, a self-hostable durable-objects runtime.

- Techniques: Durable objects as per-entity state; Open-source the runtime to remove lock-in fear
- Tools: Deno, Deno Deploy, JSR, Cloudflare Workers, Durable Objects, workerd (WorkerD), CellD, SQLite, RustyV8 (auto-caption 'RustyVA'), Node.js, Supabase Edge Functions, Netlify Edge Functions

## [The End of AI Hallucinations? Meta's New Fix (CLM's)](../videos/9-iiHFQyzuM.md)
`9-iiHFQyzuM` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: context-engineering, token-cost-efficiency, local-ai

Meta/UW's Context Language Model lets the model prune its own context through a bash-edited file instead of harness summaries. Gains are mostly compute; KV-cache costs hurt local use.

- Techniques: Notes-file handoff for long agent runs; Context-as-file self-editing (CLM pattern); Keep edits rare and context small; Suffix Cache Reuse (paper's serving fix)
- Tools: Meta CLM paper (Context Language Model, Meta and University of Washington), Qwen 27B, Qwen 9B, Claude Sonnet, Claude Opus 5.5, GPT, bash, Python, SGLang, vLLM, llama.cpp, Ollama

## [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](../videos/qJtcEDc_WJU.md)
`qJtcEDc_WJU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: multi-agent, memory, skills-self-improvement

Anthropic's live demo and Q&A on Claude Managed Agents covers multi-session orchestration, scheduled deployments, outcome rubrics, and "dreaming," a memory-store self-improvement pass that the speaker says still needs your own evals.

- Techniques: Fan-out one session per entity via a dispatch tool; Scheduled deployment of a standing agent; Outcome rubric with a max-iteration cap; Offline dreaming pass over past transcripts; Workspace-per-tenant isolation instead of BYOK; Memory store as a separate attachable resource
- Tools: Claude Managed Agents, Claude Console, Claude Code, Anthropic SDK / API, AWS Bedrock, GitHub, OpenTelemetry, Jira (Atlassian integration), Notion (external agents)

## [Latency Is a Budget. Humanlike Is the Goal. — Jesse Hall, LiveKit](../videos/j4AmIK6OvHc.md)
`j4AmIK6OvHc` · AI Engineer · 2026-10-11 · q3 · practitioner · talk · also: voice-multimodal, evals

LiveKit's Jesse Hall argues voice-agent latency is a budget to spend on human-like behavior, not raw speed, and shares audio-based turn detection, perceived-latency metrics, async tool handling and an outcome-scored simulated-caller benchmark.

- Techniques: Perceived-latency metric; Async tool with early turn release; Audio-based end-of-turn detection; Speculative LLM on provisional transcript, TTS on first sentence; Outcome-scored simulated-user benchmark; Stack-level model selection; Checklist for voice agents
- Tools: LiveKit (open-source real-time agent framework and infrastructure), LiveKit Inference (hosted model inference), LiveKit turn detector (audio-based end-of-turn model), Gemma 4 31B (tuned for voice on LiveKit Inference; auto-captions render it as 'Gemini 4 31B' at one point), ChatGPT advanced voice mode (cited as an example of a LiveKit-powered product), LiveKit voice eval harness and hotel-booking benchmark (open source)

## [Building on the Codex Harness — Dominik Kundel, OpenAI](../videos/9WiBJRO84yY.md)
`9WiBJRO84yY` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: coding-agents, mcp-and-tools, context-engineering

OpenAI's Dominik Kundel shows how to build your own client on the open-source Codex app server, the JSON-RPC protocol that wraps the Codex harness, and gives three rules for customizing it safely.

- Techniques: Append developer instructions instead of replacing the system prompt; Deferred dynamic tools with tool search; Pin and bundle the harness binary; Per-thread config overrides; Integrate by delegating to the coding agent; Choose exec or app server by parallelism and interactivity
- Tools: Codex app server, Codex CLI, Codex exec, Codex desktop app, Python SDK (Codex), Agent Client Protocol (ACP), LM Studio, Ollama, Electron, Cloudflare Doom WASM renderer, T3 Code, Claude Code Codex plugin

## [Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain](../videos/KGFyOtl5ktI.md)
`KGFyOtl5ktI` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: memory, evals, context-engineering

Jake Broekhuizen (LangChain) argues agent memory is a read-write loop: capture traces, filter them into signal, and promote only the durable parts into long-term context, with human review for procedural memory.

- Techniques: Trace-to-memory capture, analyze, update loop; Classify memory into semantic, episodic and procedural buckets; Gate procedural memory updates with human review and evals; Check the hot path for memory staleness
- Tools: LangSmith, LangSmith Context Hub, LangChain, OpenClaw, HermesAgent

## [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](../videos/NaOkR3VSfR4.md)
`NaOkR3VSfR4` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: security-guardrails, multi-agent

Viren Baraiya on running production agents: the LLM only plans, a deterministic harness executes side effects, durable state and human gates make it safe, shown with a Conductor SRE remediation demo.

- Techniques: Brains/hands split; Plan-compile-execute; Code-enforced human approval gate; Idempotent steps or recorded side effects; State-driven replanning loop; Single-responsibility harnesses
- Tools: Conductor, Kubernetes, Slack, LangChain agents, OpenAI Agents SDK, Google ADK, MCP, APIs

## [Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS](../videos/DrfyORO8RqA.md)
`DrfyORO8RqA` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · also: context-engineering, memory

AWS speaker on why larger context windows don't fix agents; she covers externalizing big tool output, summarizing and isolating context, loop caps and async tool calls, using Strands Agents.

- Techniques: Memory pointer for large tool output; Summarizing conversation manager with a ratio and a keep-last-N; Tiered memory: short-term, vector long-term, entity graph; Shared invocation-state pointer for multi-agent swarms; Per-tool invocation cap; Async job start/check tool pair
- Tools: Strands Agents, FastAPI, MCP, Neo4j, AWS API Gateway, Amazon Bedrock, Ollama, Gemini, Anthropic, OpenAI

## [Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind](../videos/oWTEiYpxl80.md)
`oWTEiYpxl80` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · also: sandboxing-execution, context-engineering

Philipp Schmid (Google DeepMind) argues agents need their own managed, persistent sandbox per API call, shows Gemini Interactions and Agents APIs, and demos a remote Antigravity environment.

- Techniques: Environment snapshot as a reusable agent base; Persistent per-conversation sandbox with server-side state; Filesystem handoff between agents; File-based agent configuration; Mount sources into the sandbox
- Tools: Gemini API, Interactions API, Agents API, Google AI Studio, Antigravity agent, Gemini CLI (for agents, not a coding agent), Google Search tool, URL context tool, Nano Banana Lite, Omni Flash, Gemini TTS, Gemma

## [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](../videos/X6l4lpA0_NY.md)
`X6l4lpA0_NY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · also: software-factory, skills-self-improvement

Drew Knox of Tessl on building a "software factory" through harness engineering: three loops (inner, outer, meta), a three-layer setup order, and how Tessl's skills registry and automation support it.

- Techniques: Three-tier loop design for agent quality; Issue-to-PR control plane for agents; Governed skills registry; Mistake-to-skill feedback; Repeated task to scheduled skill; Human-intervention metrics as the factory KPI
- Tools: Tessl, Tessl Agent, tessl launch, Linear, GitHub, GitHub Actions, Codex, Claude Code, Gemini

## [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](../videos/eXA2tjRZIbY.md)
`eXA2tjRZIbY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · also: observability, evals

Resolve AI's architecture for production-ops agents (on-call, incidents, background tasks): six pillars covering model routing, context, causal evidence, governed actions, learning loops, and multi-level evals.

- Techniques: Alert-as-prompt investigation fan-out; Evidence-chain gate on root causes; Per-subtask model routing; Tiered action permissions; Five-level eval stack; Anti-sycophancy by design
- Tools: Grafana, Slack, Microsoft Teams, Google Cloud (GCP), graph RAG, knowledge graph

## [How I Learned to Stop Worrying and Love the Sandbox — Matt Brockman, E2B](../videos/fz6-NS7qpZc.md)
`fz6-NS7qpZc` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: sandboxing-execution, infra-cost-scaling

E2B engineer runs a hands-on sandbox capture-the-flag, covering resource limits, snapshot/resume, templates, lifecycle timeouts, orphan processes, and per-user sandbox assignment.

- Techniques: Snapshot-and-resume sandboxes; Warm template with processes already running; Fork a sandbox for parallel experiments; Task-scoped lifetime with a short idle timeout; Orphan process inventory and reaping; Per-user sandbox assignment map; Separate read-only and writable paths; Egress rules when secrets are present
- Tools: E2B, Firecracker, Nomad, Kubernetes, Claude Code, Codex, Python SDK, JavaScript SDK

## [Claude Code Mods Can Do Basically Anything...](../videos/EiThSVZ8pME.md)
`EiThSVZ8pME` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: claude-code, dev-tools

Better Stack demos Claude Code "mods," in-process TypeScript plugins that can draw panes, status lines and rewrite events, by building a subscription-usage HUD and a Haiku-powered fake chat.

- Techniques: Build a status-line HUD mod by prompting; Map usage meters to status-bar stats; Read undocumented usage data from the /usage endpoint; Reactive commentary from Haiku; Terminal image fallback; Reopen a closed mod pane with a slash command; Persist a mod across sessions
- Tools: Claude Code, Claude Code mods, Claude Code hooks (comparison), TypeScript, Claude Haiku, Claude desktop app, /usage slash command, /backseat slash command, AGENTS.md support, diff pane

## [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](../videos/33Oct2hqGnk.md)
`33Oct2hqGnk` · AI Engineer · 2026-10-05 · q2 · practitioner · talk · also: mcp-and-tools, sandboxing-execution, evals

AWS's Sandhya Subramani demos an agent that writes its own tools and sub-agents at runtime using three built-in tools (editor, shell, load-from-directory) plus a system prompt, then argues that evals and sandboxing are required before trusting it.

- Techniques: Meta-tooling bootstrap (three tools + system prompt); Check-before-write rule for generated tools; Self-repair on error; Sub-agent topology choice (swarm, graph, workflow); Layered agent evals; Four-part guardrail stack for self-modifying agents
- Tools: Strands Agents (AWS open source agent harness, Python and TypeScript), Python, OpenTelemetry (named as telemetry), Strands code-execution sandbox (recent feature, named in talk)

## [The Human Is an Async API — Melanie Warrick, Temporal](../videos/jc3kbZkuHTo.md)
`jc3kbZkuHTo` · AI Engineer · 2026-10-05 · q3 · practitioner · demo · also: multi-agent, governance-compliance

Melanie Warrick (Temporal) shows durable execution for multi-agent systems: a human approval is a wait condition plus a signal on a parked workflow, so the rest of the system keeps running and survives restarts. It is a vendor-led talk with a live ice-cream delivery demo.

- Techniques: Human approval as wait condition plus signal; Wrap every model and tool call as an activity; LangGraph interrupt bridged to a durable wait; Child workflow per entity; Cost-of-being-wrong gate for human review
- Tools: Temporal, Google ADK, LangGraph, Google Maps API, Google Search, Python, TypeScript, Rust

## [We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](../videos/pyvRID_CZZU.md)
`pyvRID_CZZU` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · also: context-engineering, voice-multimodal, enterprise-adoption

AssemblyAI's FDE team built "Joey," a Claude Agent SDK support agent over local markdown docs, lifting end-to-end ticket resolution from 10% to 80% for about $700/month; the talk also argues for dogfooding your own product.

- Techniques: Docs-as-markdown synced into the agent's workspace; Two-stage retrieval: embeddings first, then agentic file search; Guardrail CLAUDE.md as the behavior-tuning loop; Escalation reason taxonomy as a product backlog; PaaS deploy from a Dockerfile for fast fix cycles; Monitoring through the existing support tool
- Tools: Claude Agent SDK, Claude Code, CLAUDE.md, Railway, Docker, Pylon, Voyage AI embeddings, AssemblyAI voice agent API, Slack, WebSocket

## [Get Out of the Model's Way — Kevin Hou, Google Antigravity](../videos/buHC7bQE1X4.md)
`buHC7bQE1X4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: multi-agent, coding-agents, product-ux

Google's Antigravity lead on building agent products that get out of the model's way: subagent teams, sidecar triggers and generative UI, with cost and token stats from a kernel-building run.

- Techniques: Dynamic subagent teams under a lead agent; One subagent per hypothesis fan-out for eval deltas; Skills file plus natural language for internal workflow automation; Sidecar trigger process; Generative UI in the conversation instead of fixed screens; Separate the orchestration surface from the editor; Primitive audit against the next model
- Tools: Google Antigravity, Antigravity CLI, Antigravity 2.0 agent manager, Gemini 3.5 Flash, MCP, Cloud sandboxes and remote execution (unnamed), Windsurf (reference only)

## [An Interaction Is All You Need — Ivan Leo, Google DeepMind](../videos/8aVbXXvJUY4.md)
`8aVbXXvJUY4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: sandboxing-execution, security-guardrails, mcp-and-tools

Google DeepMind's Ivan Leo presents the Interactions API and Managed Agents: server-side state via interaction IDs, persistent sandboxes via environment IDs, and a credential-injecting proxy. Mostly a product walkthrough with a few reusable patterns.

- Techniques: Server-side conversation state via interaction ID; Reattach to a persistent sandbox via environment ID; Proxy-side credential injection; Freeze a tuned environment as a named agent; Local-to-cloud skill packaging; Strongly typed output parsing
- Tools: Interactions API, Managed Agents, Antigravity agent harness, Gemini API CLI, AI Studio, Google Search tool, URL context tool, GCS, GitHub

## [I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j](../videos/oUZEt4EiPbk.md)
`oUZEt4EiPbk` · AI Engineer · 2026-10-04 · q2 · intro · demo · also: memory, mcp-and-tools, sandboxing-execution

Neo4j's Jeremy Adams builds a personal agent on a Raspberry Pi 4B: NanoClaw in Docker, WhatsApp as the channel, cloud LLMs, and graph memory, with a live demo and an offline capture mode for conference Wi-Fi.

- Techniques: Edge orchestrator, cloud brain; Container per agent process; Messaging app as the agent front end; Graph database as an MCP tool; Offline-first capture with deterministic parsing and later sync; Typed entity memory schema written as a skill; Batch distillation of chat history
- Tools: Raspberry Pi 4B, NanoClaw, OpenClaw, Claude Agent SDK, WhatsApp, Telegram, Docker, Neo4j, Neo4j Aura, Cypher, MCP, Neo4j agent memory service

## [Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase](../videos/5xi_S1f9sDU.md)
`5xi_S1f9sDU` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: voice-multimodal, testing-verification

Why 99%-accurate browser agents still fail in production, and how moving deterministic steps out of the model and verifying outcomes makes transactional browser workflows profitable.

- Techniques: Three browser interaction strategies; Transactional scope for browser agents; Per-transaction success with bounded retries; Artifact-based success check; Single-transaction tool encapsulation; Deterministic auth outside the model; Skill as SOP for the critical path
- Tools: Browserbase, Chrome DevTools Protocol (CDP), OCR, accessibility tree, serverless functions

## [Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band](../videos/UOcHfR3_tys.md)
`UOcHfR3_tys` · AI Engineer · 2026-10-04 · q2 · practitioner · talk · also: multi-agent, mcp-and-tools, governance-compliance

Vendor talk by Band's CTO arguing that multi-agent coordination needs a conversation-level collaboration layer (rooms, consent, routing, governance), not just MCP or A2A, then demoing that product.

- Techniques: Bilateral consent before agent-to-agent contact; Rooms and channels with deterministic routing as the agent primitive; Network-level traffic capture for cost and attribution; Live architecture layout reporting from agents; Human-in-the-loop pings and manager kill switch
- Tools: Band (collaboration layer / platform, speaker's company), Jam (desktop app built on Band, also called 'GEM' near the end of the transcript; the name is ambiguous in captions), Claude Code, Codex (OpenAI), LangGraph (LangChain), MCP (Model Context Protocol), A2A (Agent-to-Agent protocol), ACP (protocol, named without detail), Telegram, Discord, Slack, WhatsApp

## [Agent Harness explained in 8min.. Why its more Important then AI Agent](../videos/qXo1P5H2RXk.md)
`qXo1P5H2RXk` · Kai Explains · 2026-10-02 · q3 · intro · talk · also: context-engineering, claude-code, token-cost-efficiency

Explainer building an agent harness from scratch (agent loop, context management, permission gate, config) and arguing that the harness, not the model, now drives much of a coding agent's score and cost.

- Techniques: Minimal agent loop; Externalize state and use clean-context sub-agents; Harness-owned permission gate; One git work tree per agent; Move repeated instructions into configuration; Audit tool-description overhead; Compare harnesses by trips per task, not only by score
- Tools: Claude Code (Anthropic), Codex (OpenAI), Cursor, Cline (auto-caption reads 'Klein'; the open-source repo is discussed), Anthropic model card (benchmark scaffold footnote), git work trees, NVIDIA H200 (hardware, mentioned as a comparison, not used)

## [LangGraph vs OpenAI Agents SDK vs Claude Agent SDK](../videos/8C3LB6TPxwk.md)
`8C3LB6TPxwk` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: multi-agent, governance-compliance, claude-code

A practitioner comparison of LangGraph, the OpenAI Agents SDK and the Claude Agent SDK: the architectures have converged, but licensing, billing, language support, version stability and data-retention terms are what should drive the choice.

- Techniques: In-distribution test for harness choice; Pick by constraint, not by benchmark; Read the terms section before building; Verify checkpoint and resume claims against release notes; Measure latency on a representative task early; Trace handoffs as tool calls
- Tools: LangGraph, LangChain middleware, OpenAI Agents SDK (0.22; 0.14, 0.20 referenced), Claude Agent SDK (Python and TypeScript; 0.2.x patch 152), Claude Code (transcribed as 'clawed code'), Claude managed agents, OpenAI managed deep agents (public beta, US, CLI first), Microsoft AutoGen, Google ADK, Microsoft's new agent framework (unnamed), Postgres checkpointer (LangGraph), GPT-4o (transcribed as 'GPT-40')

## [This Is What Voice Coding Was Supposed to Be (Qwen Audio Agent)](../videos/blpZ1xgFhCk.md)
`blpZ1xgFhCk` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: voice-multimodal, coding-agents, multi-agent

Hands-on review of Qwen Audio Agent, an open-source voice runtime that keeps a voice conversation alive while Claude Code does slow coding work in the background over ACP. The main lesson is that voice coding is a concurrency problem, not a transcription problem.

- Techniques: Voice front-end + async coding back-end over ACP; Interruption as an explicit state machine; Local fast-path for trivial questions; Setup (as demonstrated)
- Tools: Qwen Audio Agent (open-source voice runtime, Apache 2.0; no model weights shipped), Claude Code (back-end coding agent), Codex, OpenCode, ACP (Agent Client Protocol), Alibaba DashScope (paid cloud voice API), OpenAI Realtime API (mentioned as comparison), PipeCat (mentioned as comparison), LiveKit Agents (mentioned as comparison), Whisper (dictation baseline), Hugging Face speech-to-text pipeline, MLX (Apple Silicon local backend)

## [The Loop Is the Product — Roland Gavrilescu, Introspection](../videos/7taOQBfjDyE.md)
`7taOQBfjDyE` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: skills-self-improvement, evals, product-ux

Introspection's Roland Gavrilescu argues self-improving agent loops should distill a team's taste into versioned recipes of evals, judges and skills, validated in production and measured as value per watt.

- Techniques: Trace pattern clustering to find signals; Agent-drafted judges with human calibration; Recipe diffs as reviewable candidates; Production A/B or bandit promotion; Per-model harness profiles
- Tools: Py.Recipes, Harbor, OpenClaw (originally CloudBot), Claude Code, Codex, Cursor, Cognition

## [Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph](../videos/vrDvatGtIxs.md)
`vrDvatGtIxs` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: inference-serving, testing-verification

Morph's Tejas Bhakta shows a propose-benchmark-keep-or-revert loop (autoresearch) tuning GPU kernels for about 3x speedup, with human-supplied ideas and explicit guards against reward hacking.

- Techniques: Keep-or-revert benchmark loop; Split the work: human ideas, loop parameters; Profile before tasking the agent; Hardware and model context files in the harness; Explicit anti-cheat rules in the benchmark; Stack kernels and keep fallbacks; Switch models when one fails at the DSL
- Tools: Nsight Systems (NSYS), CUDA, CUDA graphs, CuTe DSL, CUTLASS, FlashInfer, NVFP4, Autoresearch (Karpathy)

## [An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases](../videos/hd7TOvmyAxU.md)
`hd7TOvmyAxU` · AI Engineer · 2026-09-27 · q2 · practitioner · demo · also: evals, observability, training-finetuning-rl

Live demo of W&B's ARIA research agent running autoresearch experiments, plus its trace-to-eval loop: production traces, LLM judges, nightly YAML task suites, and promotion gated on eval scores.

- Techniques: Eval suite as YAML unit tests; Production traces to tasks loop; Live LLM judges as signal detectors; Eval-gated promotion; Async job dispatch from an agent; Agent analyzes its own traces
- Tools: Weights & Biases Weave, W&B Launch, W&B Inference, W&B Artifacts, W&B Reports, CoreWeave sandbox, Kubernetes, iOS app

## [One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio](../videos/2wgPHvW0mG8.md)
`2wgPHvW0mG8` · AI Engineer · 2026-09-27 · q3 · intro · talk · also: multi-agent, voice-multimodal, infra-cost-scaling

Skydio's Suchet Bargoti on running fleets of docked drones as agent-commanded infrastructure: tool-based VLM control, edge/cloud latency tiers, a shared map that the fleet updates, and a learning flywheel.

- Techniques: Tool-exposed primitives for a VLM agent; Latency-tiered edge and cloud split; Fleet-shared map with sync-back; Bandwidth-aware video encoding for cloud agents; Hybrid end-to-end versus hand-engineered decomposition; Log, sanitize, retrain, redeploy loop
- Tools: Vision-language model (VLM), Reinforcement learning, Drone APIs exposed as agent tools, Cloud GPUs and inference engines, Map merging and sync service

## [I Gave an AI a Body — Cyrus Clarke, MIT Media Lab](../videos/jgWY66RaSrQ.md)
`jgWY66RaSrQ` · AI Engineer · 2026-09-27 · q3 · intro · talk · also: voice-multimodal, product-ux

MIT Media Lab researcher Cyrus Clarke gives an OpenClaw agent a 900-pin shape display and has it build its own gesture vocabulary, arguing for non-humanoid, aesthetics-led physical AI.

- Techniques: Closed-loop gesture generation with gates and scoring; Pre-authored action repertoire to cut latency; Neutral embodiment with no affordances; Open-ended exploration prompt with machine access
- Tools: OpenClaw, openFrameworks, Numalab (speaker's own system), Shape display (physical pixel grid, 900 pins)

## [How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases](../videos/XyV6bSMyq-I.md)
`XyV6bSMyq-I` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: evals, skills-self-improvement, observability

Weights & Biases walks through how its ARIA agent evaluates and improves itself: production traces become offline regression tasks, and the agent runs its own hill-climbing loop.

- Techniques: Eval flywheel from production traces; Byte-identical prod and research agent with a sync job; YAML-defined config variants; Three task simulation modes; Dual scoring: pass/fail plus pairwise relative scoring; Unconstrained sandbox for agent research loops
- Tools: Weights & Biases Weave, W&B Reports, ARIA agent, Claude Code, YAML task and config specs

## [From Ingestion to Agents: How AI Teams Build on Document Intelligence — Adit Abraham, Reducto](../videos/0I07YAuF8xA.md)
`0I07YAuF8xA` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: data-engineering, rag-retrieval, evals

Reducto's CEO on why document ingestion decides agent quality: decompose parsing into specialised tools, verify rather than regenerate, store table forms split by job, and eval every pipeline stage.

- Techniques: Decomposed parsing stack; Targeted verification instead of regeneration; Dual table representation; Classify and split before extraction; Agent harness for chart reconstruction; Parent-subagent validation criteria; Per-stage evals
- Tools: Reducto, Gemini, OpenAI models, Anthropic models, Cursor (as analogy for speculative edits), code interpreter

## [The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI](../videos/Hvb2LfMH58c.md)
`Hvb2LfMH58c` · AI Engineer · 2026-09-20 · q2 · intro · talk · also: inference-serving, infra-cost-scaling

FriendliAI's CEO argues agent workloads need task-level (end-to-end) latency optimization, not per-request speed, and pitches prefix caching, KV cache management and cache-aware routing on an open-weight inference cloud.

- Techniques: Prefix KV caching for agent steps; Tiered KV cache with quantization and cross-replica sharing; Cache-aware routing with load-aware fallback; Optimize end-to-end task latency as the target metric; Agent-aware scheduling (described as future work)
- Tools: vLLM, GLM 5.2, Kilo Code, Claude Opus 4.8, MiniMax, Kimi

## [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](../videos/xs-ob87TTzg.md)
`xs-ob87TTzg` · AI Engineer · 2026-09-20 · q3 · practitioner · workshop · also: memory, context-engineering, skills-self-improvement

Oracle workshop on agent harness design: a 30-minute framework for agent memory (files vs databases, memory types, context rot, skill promotion), then a hands-on notebook build, with heavy Oracle product promotion.

- Techniques: Hybrid storage split; Per-agent git worktrees for file edits; Context card; Toolbox / skillbox index with vector retrieval; LLM-enhanced tool descriptions; Patience (hysteresis) budget for agent loops; Skill promotion by distillation; Difficulty-based model routing
- Tools: Oracle Database (converged: JSON, relational, spatial, graph, vector), Oracle DBFS, Oracle Agent Memory Package (OAMP), LangChain Oracle DB integration, OCI Generative AI service, GitHub Codespaces, Grok 4.1 Fast Reasoning, HNSW vector indexes, git worktrees, Python 3.12 notebook

## [Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta](../videos/7c9FSUVcXR0.md)
`7c9FSUVcXR0` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · also: infra-cost-scaling, inference-serving

Two Meta infra engineers argue LLM inference is now a distributed-systems and orchestration problem, so teams should optimize cost per successful task and build a control plane, not just faster tokens.

- Techniques: Four-quadrant optimization check; Workflow-aware scheduling and retries; Cascade breakers: queue-depth shedding, circuit breakers and retry budgets; Cost per successful task as the KPI; Telemetry-driven control loop; Latency, cost and throughput trade-off triangle
- Tools: vLLM, SGLang, TensorRT, Triton, Kubernetes, Mesos

## [GTM Engineering: The Technical Bits — Everett Berry, Clay](../videos/UhCY231d0FQ.md)
`UhCY231d0FQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: data-engineering, multi-agent

Everett Berry (Clay) on the technical hard parts of GTM engineering: data waterfalling, graph-based orchestration, long-running per-account agents, and outbound execution limits.

- Techniques: Waterfall enrichment; Selective field refresh; Typed-node orchestration graph; Persistent per-entity agent with wake-up triggers; Field ownership split; Timed re-engagement cooldown; Multi-domain sending with reply routing; Cross-channel suppression
- Tools: Clay, Salesforce, Outreach, Slack, Smartlead, Forager

## [IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork](../videos/q-WOjZhOMCA.md)
`q-WOjZhOMCA` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance, mcp-and-tools

Sarthak Aggarwal (DecaWork) argues agents should be governed like employees: each needs an identity, scoped short-lived capabilities, a policy gate outside the model, and receipts plus fast revocation.

- Techniques: Typed plan before evidence (plan-then-execute split); Out-of-model policy gate per tool call; Runtime agent identity card; Short-lived, audience-bound capability tokens
- Tools: Microsoft 365 Copilot, Microsoft Agent 365, Okta, AWS AgentCore Identity, MCP, A2A, Replit

## [Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic](../videos/PXj0p_mW9nI.md)
`PXj0p_mW9nI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: token-cost-efficiency, multi-agent, evals

Anthropic's Katelyn Lesse and Angela Jiang argue agent token budgets are not fungible: giving some tokens jobs (advisor, grader, dreamer) beats simply spending more on one executor, measured at a fixed budget and scored on pass rate.

- Techniques: Role-split executor with advisor; Rubric grader with retry loop; Dreamer writing memory from transcripts; Fixed-budget strategy comparison; Cost per pass metric
- Tools: Claude Managed Agents

## [From coding to Knowledge work agents — Karan Vaidya, Composio](../videos/xxfMT-bPEmU.md)
`xxfMT-bPEmU` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: governance-compliance, sandboxing-execution, memory

Composio CTO on why coding agents work and knowledge-work agents don't: six missing primitives (centralization, history, context, verification, governance, reversibility), enforced with walls and sandboxes rather than prompts.

- Techniques: Single connection hub for agents; Cross-app action record; Skill distillation from run logs; Pre-send style check against past outputs; Sandbox mirror of production tools; Two-layer walls: access scope plus behavior policy; Tiered gates scaled to blast radius; Undo for reversible actions, sandbox for the rest
- Tools: Composio, Claude Code, Codex, Cursor, OpenClaw, Git, Salesforce, Notion, Gmail, Slack, Zendesk, bugbot.md (named in passing)

## [How We Solved Agent Building — Andrew Qu, Vercel](../videos/9dYcwOkpCE8.md)
`9dYcwOkpCE8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, context-engineering, multi-agent

Vercel's chief of software traces an internal data-science agent from a mega-prompt, to a multi-agent chain, to one file-system agent with distilled skills, then introduces the Eve agent framework.

- Techniques: Decompose-then-collapse; File-system agent with minimal tools; Query-to-skill distillation job; Convention-based agent folders; Built-in run observability
- Tools: Vercel AI SDK, Eve, Vercel Workflows, Vercel Sandbox, Vercel Connect, bash-tool (npm), SkillsSH, Claude Code, Claude Opus 4.5, Snowflake, Next.js, Postgres

## [Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind](../videos/fjF8EKnxKCU.md)
`fjF8EKnxKCU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, sandboxing-execution, security-guardrails

Philipp Schmid (Google DeepMind) rebuilds one GitHub PR-review agent three ways, moving from a hand-written Python loop to a hosted sandboxed harness driven by markdown files, and argues to delete orchestration code as models improve.

- Techniques: Agents-as-files layout; Bootstrap script for CLI dependencies; Credential injection through a network proxy; Single-call agent turn with server-side loop; Named custom agent; File-based memory and handoffs; Build-to-delete audit
- Tools: Gemini API, Interactions API, Antigravity (agent harness), Google Agent Development Kit (ADK), GitHub CLI (gh), Google Search tool (Gemini API), Google Cloud Storage (GCS) bucket, GitHub repositories as sandbox sources, AI Studio, LangChain Open Deep Research (case reference), Cursor (case reference, speaker says 'Curso'), Manus (case reference, speaker says 'Manos')

## [Realtime Voice Agents with Frontier Intelligence — Bohan Li, EliseAI](../videos/MBHOH1NmDqc.md)
`MBHOH1NmDqc` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, inference-serving

EliseAI's Bo Li explains a cascaded voice-agent harness (streaming transcription, background tool calls, prefix-cached TTS) that keeps frontier-model intelligence at real-time speed.

- Techniques: Streaming speculative transcription (two-tier ASR); Early generation with background tool calls and cancellation; Word-sequence prefix cache for TTS; Playback deduplication after speculative TTS
- Tools: Flux (fast streaming transcriber), Scribe V2 (accurate batch transcriber), Cartesia (TTS with WebSocket support)

## [Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked](../videos/HvMyYLTfvhg.md)
`HvMyYLTfvhg` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: context-engineering, memory, mcp-and-tools

Jeff Ng (Unblocked) argues agent infrastructure is now easy to assemble, so the real gap is organizational context. He demos a context engine that feeds agents synthesized, permission-scoped knowledge instead of raw MCP results.

- Techniques: Durable per-step checkpoints for agent runs; Isolated sandboxes for agent and third-party code; Context engine queried before the agent reasons; Synthesized context over raw tool results
- Tools: Cloudflare, Vercel, Mastra, Flu (transcript spelling of the framework), Linear, Slack, GitHub MCP, Claude Code, Codex, Unblocked context engine

## [ACP: The Universal Remote Control for AI Agents — Alex Hancock, Block](../videos/YkNulwcc5jk.md)
`YkNulwcc5jk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, coding-agents

Alex Hancock (Block, Goose and MCP maintainer) argues for ACP, an open client-to-harness protocol, so one client can drive any agent over local stdio or remote HTTP/WebSocket.

- Techniques: Standard client-to-harness protocol (ACP); Underscore-prefixed custom methods, then standardize by usage; Transport swap with unchanged messages; Split the agent stack into four movable parts
- Tools: ACP (Agent Client Protocol), Goose, Zed, JetBrains IDEs, MCP (Model Context Protocol), JSON-RPC, stdio, HTTP, WebSocket

## [Your Voice Agent is Just a Walkie Talkie — Neil Zeghidour, Gradium](../videos/a8EcVumh71E.md)
`a8EcVumh71E` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: voice-multimodal, models-research

Gradium's CEO traces voice agents from Siri to speech-to-speech models, explains why full-duplex needs multi-stream audio, and argues for a small full-duplex front end delegating to a background text LLM.

- Techniques: Audio tokenizer (neural codec) before the LLM; Multi-stream full-duplex modeling; Split front-end / background-LLM voice architecture (MoshiRAG)
- Tools: Moshi, Hibiki, GPT Realtime, OpenAI advanced voice mode, Siri, Claude Sonnet 5

## [Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS](../videos/gxVZ_1tuuq4.md)
`gxVZ_1tuuq4` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: infra-cost-scaling, memory

AWS's Mike Chambers argues that an agent minus its model is the harness, and that agents built for many users should split the loop, memory, identity and tools into separately scaled parts, demoed on Bedrock AgentCore.

- Techniques: Split agent components for independent scaling; Session manager for cross-invocation state; Local dev loop that mirrors production; Declarative harness config; Agent-generated infrastructure as code
- Tools: Amazon Bedrock AgentCore, AgentCore CLI, Strands Agents SDK, Kiro, Claude Code, Cursor, MCP, AG-UI, AWS agent toolkit, Sonnet 4.5

## [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](../videos/hD9-V56FNRI.md)
`hD9-V56FNRI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, observability, memory

Talk arguing that once agents call tools and change state, they are distributed systems, so they need idempotency, compensation, scoped permissions, bounded retries and per-step traces.

- Techniques: Idempotency keys plus status lookup on every side-effecting tool; Persist each loop step and define compensation operations; Retry and fanout guardrails; Scoped credentials and tool allowlists; Parameter-bound, expiring human approvals; Memory as a cached, provenance-tagged store; Tool contracts with schemas and idempotency
- Tools: Replit AI agent (cited as a production-database deletion incident; not a tool under review), Air Canada chatbot (cited as an incorrect-refund incident; not a tool under review)

## [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../videos/B0fjR3yaZFU.md)
`B0fjR3yaZFU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, product-ux, evals

Long Lake co-founder on why AI adoption in real services businesses lags: climb an autonomy ladder, turn real work traces into evals, and co-design with users on-site.

- Techniques: Autonomy ladder rollout; Sandboxed async coding agent with PR output; Traces to ground-truth evals; Diff-based implicit feedback; Post-training on enterprise data; Layered customization; Co-design embedded in existing tools
- Tools: Claude Code, Codex, Claude Cowork, MCP

## [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../videos/YXowceUKYJI.md)
`YXowceUKYJI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: inference-serving, infra-cost-scaling

Red Hat engineers explain why agentic multi-turn traffic breaks classic LLM serving, and how llm-d uses KV-cache-aware routing and prefill/decode disaggregation on Kubernetes, with benchmark data and a GLM 5.2 case study.

- Techniques: KV-cache-aware pod routing; Prefill/decode disaggregation with KV transfer; Tiered KV offload with session pinning; Distribution-based capacity planning and trace replay; Decision matrix before choosing PD
- Tools: llm-d, vLLM, Kubernetes, NIXL, DeepEP, Mooncake, inference-perf, LeaderWorkerSet, RDMA/RoCE

## [It’s Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners](../videos/xo68uCibfm8.md)
`xo68uCibfm8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: context-engineering, multi-agent, data-engineering

Kevin Madura (AlixPartners) explains recursive language models (RLMs): the context lives as a variable in a Python REPL, and the model writes code and delegates subcalls to sub-LMs, so only useful results return to the main context.

- Techniques: REPL-held context with sub-LM delegation; Typed I/O shell around an autonomous core; Schema-enforced sub-LM handoff; Bounded self-terminating loop; Dataframes in the REPL instead of JSON tool results; Trace-driven harness optimization (Halo)
- Tools: DSPy, PredictRLM, fastRLM, AXE, Halo, Claude Code, GPT-5, Anthropic Workflows, pandas

## [AI in GTM at Notion — Flora Liu](../videos/L4I7WgiEquo.md)
`L4I7WgiEquo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, multi-agent, data-engineering

Notion's GTM engineer explains a know/decide/act/learn system that unifies sales and self-serve signals, with humans and agents working in one shared context layer on durable workflows.

- Techniques: Four-layer know/decide/act/learn loop; Denormalized key-addressable profile plus keyed unstructured artifacts; Durable workflow per event with engine-managed retries; Parallel research subagents with score-and-select review loop; Single eligibility and routing classifier; Human approval gate by default, untrusted inbound input; Trace every LLM step and log decisions with outcome links
- Tools: Notion, Snowflake, DynamoDB, Temporal, Clay, Gong, Salesforce, Outreach, Nooks, ZoomInfo, Snowflake (product usage), Notion custom agents

## [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../videos/VjEP0xqTUI0.md)
`VjEP0xqTUI0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, data-engineering, mcp-and-tools

Arman Vaziri (Ramp) on building go-to-market orchestration: an internal CDP, durable background agents on Temporal, scoped retrieval, and an MCP that turns employee experiments into productized use cases.

- Techniques: Durable thread with checkpointed activities; Account-scoped hybrid retrieval; Per-agent tool scoping with human pause and resume; System skills plus user text instructions; Nightly per-entity fan-out; Persist derived entity matches; Shared tool surface via MCP plus usage mining; Explore vs exploit with guardrails across channels
- Tools: Temporal, Postgres, Kafka, TurboPuffer, dbt, Snowflake, reverse ETL, MCP, GPT-3.5

## [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../videos/mMNkdYnIVC4.md)
`mMNkdYnIVC4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, multi-agent, training-finetuning-rl

James Zou (Together AI, Stanford) argues agents should be given designed environments with verifiers, incentives and shared infrastructure instead of fixed workflows, citing Einstein Arena results and the DSGym data-science benchmark.

- Techniques: Verifier-first problem curation; Agent-native onboarding; Persona-differentiated agents; Shortcut audit before trusting a benchmark; Execution-verified trajectory generation
- Tools: Docker

## [The Spatial Harness: Bringing Agents to the Canvas — Max Drake, tldraw](../videos/XWcXwnysmpY.md)
`XWcXwnysmpY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, multi-agent, coding-agents

tldraw's Max Drake on giving LLM agents a spatial canvas: teaching them to read screenshots plus shape data, running multi-agent fairies, and driving live apps and the desktop through code.

- Techniques: Screenshot plus structured data as canvas context; Agentic canvas harness with self-set goals; Visual agent identity and on-canvas task state; Orchestrator agent posting tasks to a shared board; Local editor server for code-mode agents; Dependency graph of agent tasks
- Tools: tldraw SDK, tldraw desktop app, Claude Code, Notion, Gmail, Conductor, OpenAI Symphony

## [Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher](../videos/y2W4FNAuPEA.md)
`y2W4FNAuPEA` · AI Engineer · 2026-09-18 · q3 · practitioner · workshop · also: inference-serving, infra-cost-scaling

Two-hour LLM inference workshop covering KV-cache memory math, prefill vs decode, attention variants, quantization, vLLM/SGLang serving optimizations, and benchmark caveats.

- Techniques: KV-cache capacity planning; Fix one dimension, then solve the rest for cost; Weight quantization for KV headroom; Attention variant selection; Radix-tree prefix caching for agent loops; Speculative decoding variants; Engine benchmarking loop
- Tools: vLLM, SGLang, TensorRT-LLM, NVIDIA Dynamo, Hugging Face Transformers, FlashAttention, EAGLE, Medusa, Molab, Google Colab, Mistral 7B, GPT-OSS-120B

## [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../videos/GJX19pNhmSw.md)
`GJX19pNhmSw` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: token-cost-efficiency, governance-compliance, observability

Microsoft's Tisha Chawla and Susheem Koul argue agent cost control belongs at the agent-run layer, not the request layer. They show an out-of-band "TokenOps" plane that attributes spend per run, steers runs toward budget before halting them, and reports vendor benchmarks.

- Techniques: Run-scoped attribution tags and budgets; Boundary decorator on agent methods; Governor with a developer-declared action allowlist; Tiered policy ladder: steer, then halt; Cost guard: projected-overrun steering; Preview (shadow) mode for guardrails; Benchmark against throttling baseline
- Tools: OpenTelemetry, LangChain, LangSmith, LiteLLM, Portkey, Cloudflare AI Gateway, browser-use, MetaGPT

## [Tell the Robot What You Want — Sandhya Subramani, AWS](../videos/S6aSoQ6_u5A.md)
`S6aSoQ6_u5A` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: multi-agent, voice-multimodal

Live demo of a rover robot driven by an LLM agent built on the Strands harness, with a four-layer agent-to-hardware stack and a pitch that VLA policies may eventually make per-task robot training unnecessary.

- Techniques: Robot as an agent tool; Concurrent specialized agents on one tool surface; Edge/cloud policy split; Teleop for dataset creation; Messaging-app control over cellular
- Tools: Strands Agents (agent SDK), Amazon Bedrock AgentCore, Claude Opus 4.8, OpenAI Realtime (voice), Telegram, Raspberry Pi, VLA models, 4G SIM

## [Everyone Gets A Software Company — Benjamin Guo, Zo Computer](../videos/Qr15lGAGKpo.md)
`Qr15lGAGKpo` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: product-ux, sandboxing-execution

Zo Computer co-founder Ben Guo pitches a personal cloud server with built-in AI as a way out of SaaS silos and vendor-owned cloud agents. Mostly a product pitch, with a few ownership arguments worth noting.

- Techniques: Single personal server as the agent home; Scheduled agent automations; Agent as a gatekeeper for inbound bookings; Chat-driven site editing and hosting
- Tools: Zo Computer, Claude Code, Codex, Gemini, Claude Tag, OpenClaw, Hermes, Calendly, Squarespace

## [The End of the Static Screen: Architecting Intent-Driven UX — Gus Iwanaga, commercetools](../videos/QrMcNe2jjt8.md)
`QrMcNe2jjt8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, mcp-and-tools

Gus Iwanaga (commercetools) on intent-driven generative UI: an orchestrator picks data and components, and the LLM emits a validated declarative UI spec, not free-form UI. Main lessons are on placement, the component catalog as contract, and changing team roles.

- Techniques: Declarative UI spec validated against a component catalog; Three-tier control spectrum for generated UI; Intent-to-UI orchestration pipeline; Layout hierarchy with templates, built bottom-up; Synthetic query-to-component data for curation
- Tools: MCP, Zod, React, A2UI, JSON Render (Vercel), OpenUI, ChatGPT, Claude

## [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](../videos/UyyOoJmuATU.md)
`UyyOoJmuATU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: governance-compliance, evals, enterprise-adoption

Vasant Kearney (Onlay) argues healthcare agents should run on X12 insurance transactions as a public, strict contract that guardrails can reject, with tiered memory and skeptical use of models.

- Techniques: Standard-format tool contract; Strict guardrail rejection per step; Separated, tiered memory; Full-system regression evals before model swaps; Hybrid hard-coded and agentic execution; Write-action audit logging
- Tools: X12, FHIR, EHR, Claude Code, Codex, OpenClaw, Hermes Agent

## [Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk](../videos/dQ-_i1tZiws.md)
`dQ-_i1tZiws` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, evals, security-guardrails

Maersk's Dmitry Buykin on running 200+ production shipping agents by turning expert SOPs into executable agent procedures, with a feedback loop that turns each correction into a harness change.

- Techniques: SOP-to-agent conversion; Three-part agent harness; Failure-to-fix mapping; Replay with writes disabled; Trace clustering into heat maps; Composite tools from repeated success; Function-calling tools instead of MCP
- Tools: SME bench (internal triage tool that clusters failures), Function calling

## [Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan](../videos/32nrHU6zHU8.md)
`32nrHU6zHU8` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: observability, evals, context-engineering

Navan's chief architect and a colleague argue agent infrastructure is repeating the microservices shift: skills as context units, hook-based tracing, trajectory evals, and tool-call guardrails.

- Techniques: Pre/post tool-call and session hooks for tracing and gating; Trace signals: goal, reasons, belief, tool calls, confidence; Trajectory evaluation; Skills as composable, testable context units; Single master agent with progressively loaded sub-skills; Per-tool-call authorization for on-behalf-of agents; A2A skill contracts across team boundaries
- Tools: AWS AgentCore, OpenTelemetry, Claude Code hooks, MCP, A2A protocol, Braintrust (inferred from auto-caption 'brain trusts')

## [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](../videos/cI7zfqusmFU.md)
`cI7zfqusmFU` · AI Engineer · 2026-09-18 · q3 · practitioner · demo · also: infra-cost-scaling, multi-agent

Giselle van Dongen (Restate) argues long-running agents need a durable infrastructure layer, and demos journaled retries, human-approval suspension, keyed sessions and mid-run signal or cancel.

- Techniques: Wrap every side-effecting agent step in a durable run call; Durable promise for human-in-the-loop approval; Keyed virtual object per session for serialized agent state; Classify mid-run input, then signal or cancel-and-restart; Central LLM gateway as its own durable handler
- Tools: Restate, Slack, LiteLLM, Python

## [How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face](../videos/FLUoowDJg4I.md)
`FLUoowDJg4I` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: software-factory, observability, models-research

Hugging Face's Niels Rogge shows how nightly agents open outreach GitHub issues and PRs to move researchers' artifacts onto the Hub, moving from a fixed workflow to an autonomous agent loop.

- Techniques: Deterministic LLM pipeline mirroring the manual process; Cron for overnight background agents; Promote a step to an autonomous loop only where outputs are unpredictable; One container per work item for parallel agents; Skill as a manual trigger that fans out to subagents; Open-model routing through one OpenAI-compatible endpoint; Template completion from source material
- Tools: Claude Agent SDK, Cursor, Modal, GitHub Actions, Langfuse, Hugging Face CLI, Hugging Face inference providers, Slack, Gemini, Claude Code

## [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../videos/VBCDhRrvlYo.md)
`VBCDhRrvlYo` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: vibe-coding-app-building, product-ux, context-engineering

Arturo Nunez (ex-Unity, MongoDB) pitches Nereu, a tag-driven, describe-it-to-build game engine where an AI assistant (Bibi) edits scenes via an Asset Tag System, so creators never touch engine vocabulary or code.

- Techniques: Entity tags as an intent layer over ECS; LLM-as-editor with a tool-only interface; Level-of-detail context assembly; Vision-model asset captioning; Domain expert in the loop while building with a coding agent
- Tools: Claude Code, Unity, Unreal, vision model

## [The Half Life of Agent Infrastructure — Ben Kus, Box](../videos/sM1iYgz93HI.md)
`sM1iYgz93HI` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: evals, enterprise-adoption, rag-retrieval

Box CTO Ben Kus argues AI agent infrastructure has a half-life of months, not years, so teams should build abstractions, gate changes on eval sets, and get good at changing.

- Techniques: Abstraction layer over agent internals; Eval-gated switching; Scheduled stack review; Adaptive model selection; Hybrid lexical plus semantic retrieval with rank fusion; Agentic search
- Tools: Claude, Opus, OpenAI and Anthropic frontier models, open-weight models, BM25, embeddings and approximate nearest neighbor search, MySQL

## [No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle](../videos/jA_x7F8caHI.md)
`jA_x7F8caHI` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: memory, multi-agent, enterprise-adoption

Oracle's Kay Malcolm argues that agent harnesses need shared, database-backed memory, using a five-type memory taxonomy and a team memory broker; mostly a product pitch for Oracle AI Database.

- Techniques: Five-type agent memory taxonomy; Shared memory broker tied to repo state; Keeping context alongside commits; Single-store consolidation for agent memory; Private local model for memory extraction
- Tools: Oracle AI Database 26AI, Oracle Agent Memory SDK, Codex, Claude, Git, Neo4j, Redis, OCI Always Free

## [Agent Frameworks Considered Harmful — Rémi Louf, .txt](../videos/KHudyx5wW3U.md)
`KHudyx5wW3U` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: observability, context-engineering

Rémi Louf (CEO of .text) on building a small event-driven agent runtime in two weeks: typed events, an append-only log, and content-addressed prompts for auditable, replayable agents.

- Techniques: Markdown-defined agents in a versioned folder; Event-typed agent contracts; Append-only event log with causal ids; Content-addressed prompt assembly; Replay a stored request against another model; Two-boundary enforcement
- Tools: Codex, Slack, Linear, llama.cpp

## [Voice agents with Realtime Video — Sidney Primas, LemonSlice](../videos/z1dqv74SpUs.md)
`z1dqv74SpUs` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: voice-multimodal, inference-serving

Lemon Slice's CTO explains how they build real-time, photorealistic video avatars from a causal video model, covering past-only attention, one-step denoising, long error-free runs, and a GPU/CPU harness that keeps streams stutter-free.

- Techniques: Causal (past-only) attention mask for streaming video; Collapse denoising steps for real-time output; Expressive audio encoders over default ones; Real-time model harness (GPU/CPU orchestration); Two-layer EQ/IQ split

## [Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust](../videos/nxokqOq1imY.md)
`nxokqOq1imY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, observability

Braintrust field CTO argues each agent architecture generation (single call, chain, ReAct loop, graph, product system) needs different evals, and that production traces should keep feeding the eval set.

- Techniques: Architecture-matched eval suites; k-run pass@k and pass^k reporting; Production failure clustering to harvest evals; Node-level and branch-level evals for graph workflows
- Tools: Braintrust, Braintrust Topics

## [PrimeAgent + Opus 5 is INSANE (Why I Dropped Claude Code)](../videos/kg3MmLd0qEM.md)
`kg3MmLd0qEM` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: coding-agents, memory, skills-self-improvement

A Kai Explains review of Prime Agent, an open-source MIT terminal coding harness with cross-session learning, paired with Claude Opus 5 as a Claude Code replacement; the self-reported benchmarks are flagged as unverified.

- Techniques: Learned-layer self-improvement over an immutable base prompt; Persistent goal with bounded autonomous run; RLM-style context management; Per-task effort dial; Model-agnostic routing with self-hosting; Container isolation for self-modifying agents
- Tools: Prime Agent (Prime Intellect, MIT, open-sourced 2026-08-05), Claude Opus 5 (released 2026-07-24), Claude Code, Cursor, Cline (transcribed as 'Klein'), Claude Fable 5, GPT 5.6 Sol, vLLM, Ollama (transcribed as 'Alama'), LM Studio, FrontierBench v0.1, ARC-AGI-3

## [Every Level Of Claude Code Loop Engineering Explained](../videos/PLyRe6Zk--8.md)
`PLyRe6Zk--8` · AI LABS · 2026-09-02 · q4 · practitioner · tutorial · also: claude-code, software-factory, testing-verification

A three-level walkthrough of "loop engineering" in Claude Code: spec-as-/goal for one feature, a queue-driven software factory with a separate adversarial reviewer per branch, then phone control of the loop. Substantive, with the skills and steps shown.

- Techniques: Spec file as a /goal with explicit verification; Queue-file tracker for overnight multi-feature runs; Builder and adversarial verifier split; Clickable HTML mock per feature as planning and verification oracle; PR as the human approval gate; CLI-based platform setup driven by the agent; Minimal CLAUDE.md that points at AGENTS.md; Mobile control of a laptop-resident Claude Code session
- Tools: Claude Code, /goal (Claude Code slash command), /loop (Claude Code slash command), Codex (said to work with the same system), GSAP, Next.js, GitHub (and gh-style CLI), Supabase (and its best-practices skill), Vercel (and deploy-to-Vercel skill), Warp, VS Code, Paseo

## [MCP Was Wrong From The Start (They Just Fixed It)](../videos/f4mI3d-nTrI.md)
`f4mI3d-nTrI` · Better Stack · 2026-09-02 · q3 · practitioner · news · also: mcp-and-tools, infra-cost-scaling

Walkthrough of the MCP 2026-07-28 spec, which makes the protocol stateless: no handshake, no session IDs, explicit state handles, input-required round trips, and official tasks for long-running calls.

- Techniques: Stateless MCP tool calls; Explicit state handle; Input-required round trip; Async tasks for slow tools; Gateway routing on MCP headers; Cache hints on list calls; SDK migration
- Tools: MCP (spec version 2026-07-28), MCP TypeScript SDK v2 (separate server and client packages), MCP SDK codemod, Cloudflare Workers, Cloudflare Durable Objects, Google Cloud Run, Redis

## [You Don't Need Frontier Models Anymore (Qwen 3.8 27B + DeepSeek Harness)](../videos/3DVRznjCIS8.md)
`3DVRznjCIS8` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: local-ai, evals, context-engineering

Same local Qwen model, same weights and prompt: the outcome changed with the harness around it (feedback loop, tools, session log, context), so the software matters as much as the model.

- Techniques: Attribute failures to the harness before blaming the model; Close the feedback loop so the agent can verify its own output; Persistent session log as source of truth for long runs; Sweep reasoning effort on a fixed prompt rather than assuming max is best; Size the local model by capacity and bandwidth, then pick quantization; Hybrid local-then-frontier handoff
- Tools: Qwen 3.8 27B (transcript: 'Quen 3.8'), Qwen 3.6, Qwen 3.7 Plus, DeepSeek Harness (transcript: 'DeepSeq Harness'; MIT licensed, plugin components, developer preview), DeepSeek v4 (2-bit quant, transcript: 'DeepSeq v4'), Claude Code (Qwen's benchmark harness for four agentic evals), Opus API (cost comparison), VS Code Copilot (failed reproduction run), Unsloth Q6 build of Qwen 3.8, Simon Willison's test prompt (reasoning-effort test), DeepSWE 1.1 (benchmark), OSWorld (computer-use benchmark)

## [China Just Open-Sourced Humanlike Memory for AI Agents (Tencent DB)](../videos/W3yHP9_jYNk.md)
`W3yHP9_jYNk` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: context-engineering, memory, token-cost-efficiency

Teardown of Tencent's open-source agent memory plugin: folding tool output into disk files plus a layered memory store. Claims 33% to 50% pass rate with 61% fewer tokens, which the speaker partly rechecked.

- Techniques: Offload tool output to disk with an ID-indexed map in context; Pressure-scaled folding; Layered consolidation memory; Persona-first recall; Keep the memory prefix cache-stable; Treat shared memory writes as untrusted input; Recompute vendor benchmark tables
- Tools: Tencent Cloud memory plugin (MIT, GitHub, about 10k stars in four months; the repo name is not stated), OpenClaw (install target, one command), SQLite (default local store), Tencent Cloud Vector database backend, Chroma (context-rot study), Mermaid (diagram format for the in-context map), Mem0 (published its own memory benchmark, per the speaker), Zep (published a rebuttal, per the speaker), WideSearch (ByteDance Seed benchmark), WeBench (name as transcribed), SWE-bench (token columns checked by the speaker), PersonaMem (persona benchmark)

## [Deepseek Harness: Not What You Think](../videos/y0BW4hpMpyM.md)
`y0BW4hpMpyM` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: evals, token-cost-efficiency, security-guardrails

Kai Explains on DeepSeek's open harness: benchmark scores are model-plus-harness pairs, the harness can move scores 5-8 points, and its append-only, cache-stable context design is the most reusable idea, alongside licensing and security concerns.

- Techniques: Report scores as model-plus-harness pairs; Append-only event log with a rebuilt, frozen message history; Cache-stable summarization and compaction; Track cache-hit rate per agent session
- Tools: DeepSeek Harness (DeepSeek's open-source agent harness, version 0.1, MIT license per the host), DeepSeek V4 Pro (pricing mentioned), Terminal Bench (public leaderboard at TBench AI, Terminus 2 research harness), Gemini 3 Pro, Gemini 3.1 Pro, Gemini CLI, Claude Code, Claude Agent SDK (pinned at 0.3 per the host), Claude Code 2.1 (bundled in the sub-agent payload), Opus 5 (as captioned), Fable 5 (as captioned), Codex CLI

## [YC Just Open-Sourced Its Multiplayer Harness](../videos/GrZ-X3-2TVs.md)
`GrZ-X3-2TVs` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: security-guardrails, enterprise-adoption, coding-agents

Better Stack's hands-on tour of YC's open-source "multiplayer" agent harness (QM): a self-hosted, multi-user web app with Slack access, per-workspace containers, a seven-tool surface and org-level approval modes. Promising but two weeks old.

- Techniques: Minimal primitive tool surface plus shell sandbox; Org ceiling with per-team tightening and a posture-independent command deny list; Enable extra harnesses through the admin API; Share context through a team project, keep credentials private by default
- Tools: QM (YC open-source multiplayer agent harness; the caption spelling may be off, and the repo was about two weeks old at the video date), pi (the default agent harness in QM), Claude Code (can be enabled as a harness inside QM), Slack (integration surface), PostgreSQL (session history), GitHub (repo linked in the description)

## [OpenSource AI Tools That Feel ILLEGAL To Get Free](../videos/VghawjhiGkw.md)
`VghawjhiGkw` · Kai Explains · 2026-09-02 · q3 · intro · review · also: coding-agents, local-ai, token-cost-efficiency

Kai Explains reviews five open-source AI tools (Goose, Jan, Money Printer Turbo, a DeepSeek harness) as subscription replacements, stressing that the software is free but inference, API keys and hardware still cost money.

- Techniques: Point an OpenAI-SDK client at a local endpoint; Run the DeepSeek harness as a local web app; Semantic-mismatch test for generated video; Read a README past the marketing lines
- Tools: Goose, Jan, Hugging Face, Llama, Gemma, Qwen (transcribed as 'Quen'), Money Printer Turbo, FFmpeg, Pexels, Pixabay, Coverr (transcribed as 'Caver'), Edge TTS

## [Opus 5 Built An F1 Game... for $1,200](../videos/viHqe5QqTd0.md)
`viHqe5QqTd0` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: multi-agent, testing-verification, token-cost-efficiency

A Better Stack host runs the "Gauntlet Loop" prompt (a goal plus a real-world target, sub-agents, and a screenshot-based critic loop) on Opus 5 to build an F1 racing game, then judges how playable the result is and what it cost.

- Techniques: Gauntlet loop (goal + real-world target + critic loop); Have the agent build its own verification tools; Stop on plateau, not only on a threshold; Meta-prompt to generate the loop prompt
- Tools: Claude Opus 5, Claude (Max plan subscription, used for the run), Claude sub-agents, Gauntlet Loop prompt (Matt Shumer)

## [DeepSeek Harness Just Changed AI Forever](../videos/DTu4yvmc0Fc.md)
`DTu4yvmc0Fc` · Better Stack · 2026-09-02 · q2 · intro · review · also: coding-agents, observability

Short hands-on tour of an open-source, plugin-first coding harness built on the Cordis framework, covering swappable models, an append-only trajectory log, and adding plugins by prompt. Hype title, thin on setup.

- Techniques: Add a plugin by prompting inside the harness; Use an append-only trajectory log to audit a run; Swap the model provider through plugin config
- Tools: DeepSeek harness (open-source agent harness, desktop app and TUI), Cordis (plugin framework; name as auto-captioned), DeepSeek V4 Pro (model; named in the video), GLM 5.2 (model used as a comparison point), Claude Sonnet 4.5 (in sample provider config), OpenClaw (named as "open claw" in the video), OpenCode (compared for in-prompt customization), QM (a harness the channel covered earlier, name as spoken)

## [Anthropic's Biggest Lie! (The Harness War)](../videos/_DZ4kJwQ50s.md)
`_DZ4kJwQ50s` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: context-engineering, claude-code, evals

Compares Claude Code's compaction-based context handling with Prime Intellect's open-source Prime Agent (an RLM-style persistent kernel plus a self-editing "continual harness"). Vendor-reported benchmarks; the context-rot argument is the useful part.

- Techniques: Single persistent kernel as the only tool; Context as a variable (RLM-style chunked processing); Externalized session state instead of compaction; Continual harness: log failures, promote tactics; Guard self-improvement against reward hacking
- Tools: Claude Code, Prime Agent (Prime Intellect, MIT license, installs via a single curl command on Linux or macOS), Claude Opus 5, IPython kernel, Codex (OpenAI coding harness, mentioned by name), GPT-5.4, Gemini, ARC-AGI-3, LongCoT-Mini

## [Anthropic's Model Hardware Standard: Everything You Need To Know](../videos/UEd-I_67qJI.md)
`UEd-I_67qJI` · Kai Explains · 2026-09-02 · q3 · intro · news · also: mcp-and-tools, security-guardrails, models-research

Explainer on Anthropic's Model Hardware Standard (MHS), an MCP-like interface for lab and physical devices, with Carnegie Mellon, Quera and Genentech field results and the main criticisms.

- Techniques: Self-describing device declaration for agent-written drivers; Enforce hard limits in the device or interface layer, not in the prompt; Fault-injection test of the safety layer; Agent-side data-quality check and re-run loop; Report unresolved causes instead of claiming a fix; Three invocation modes for the same device
- Tools: Anthropic Model Hardware Standard (MHS), Model Context Protocol (MCP), Claude Opus 4.8, SiLA (gRPC), OPC UA, Tango, BlueSky, QCoDeS, ROS, PyLabRobot, MATLAB, Python

## [Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning](../videos/2bvtay8wGYI.md)
`2bvtay8wGYI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: training-finetuning-rl, context-engineering, evals

GR's Ross and Chengxi Taylor trace RL-for-reasoning from Galactica and 2022 PPO recipes to long-horizon agents: value models, compaction, pipeline RL, and a benchmark where frontier models lost money.

- Techniques: Value-model (critic) RL for long, variable-length trajectories; RL-trained compaction; File-system scratchpad, self-search and archive tools for long-horizon context; Pipeline RL with bounded off-policy lag; Verifiable-reward PPO after continued pretraining (2022 recipe); Open-ended, outcome-scored long-horizon benchmark
- Tools: Galactica (Meta science LLM; 30B variant cited), Llama 2, Llama 3, Reasoning Llama (named, no details), ChatGPT, GPT-3.5, GPT-4, OpenAI o1, DeepSeek-R1, InstructGPT (2022, cited for RLHF results), PaLM (540B, cited for comparison), Chinchilla (cited for comparison)

## [Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](../videos/jRCpXUjz4CI.md)
`jRCpXUjz4CI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, sandboxing-execution, training-finetuning-rl

Alex Shaw (Terminal-Bench, Harbor) argues agents behave like ML models, so teams should build environments (instruction, sandbox, verifier) and run parallel rollouts for evals, training data, RL and agentic map-reduce.

- Techniques: Environment as a three-part directory (instruction, sandbox, verifier); Separate rollout, trajectory capture and verification; Parallel rollouts with a fire-and-forget launch; Agentic map-reduce over agent logs; Own the eval before choosing a model; Design for agent users of your product
- Tools: Harbor, Terminal-Bench 2.1, Codex (GPT-5.5 run in the demo), Cursor CLI (map step in demo), Modal (sandbox backend in demo), Tinker (RL integration), A frontier model transcribed as 'Fable 5' (reduce step in demo; name may be a caption error), LangChain Deep Agents with sandboxes (integration)

## [How Codex Works — Dominik Kundel, OpenAI](../videos/shRR1e2HXMk.md)
`shRR1e2HXMk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: coding-agents, context-engineering, sandboxing-execution

OpenAI's Dominik Kundel walks through what happens when a message is sent to Codex: context assembly, sub-agents, computer use, sandboxing, auto-review, WebSocket transport, goal loops and compaction.

- Techniques: Deferred tool loading with tool search; Capping the skills list as a share of the context window; Sub-agent tool set: spawn, send input, wait, shutdown; Code-execution computer use with a persistent REPL; Auto-review sub-agent for escalated actions; Stateful WebSocket transport for agent loops; Goal loop with an explicit done tool; Server-side compaction item
- Tools: Codex, OpenAI Responses API, Codex app server, ripgrep, PowerShell, Node REPL, Chromium, Seatbelt (macOS sandbox), Bubblewrap (Linux sandbox), Cerebras (GPT-5.3 Codex Spark), Ollama, LM Studio

## [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../videos/GqoNrUz8hEU.md)
`GqoNrUz8hEU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, security-guardrails, mcp-and-tools

Paul Klein (Browserbase) argues reliable browser agents are a harness, tooling and infrastructure problem rather than a model problem, and lays out a multimodal, harness-engineered, consistently hosted approach.

- Techniques: Hybrid code-plus-browser execution; Per-site skill packs loaded before visiting; Compressed page representation; Pinned, consistent browser environment; Sites expose WebMCP tool calls and agent-first auth; Observability-to-self-improvement loop
- Tools: Browserbase, Browse.sh, WebMCP, Playwright CLI, Claude Code, Operator, Cursor, Factory, OpenClaw, WorkOS AuthMD, web bot auth, auto-browse

## [Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft](../videos/m24UKZomm7k.md)
`m24UKZomm7k` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, context-engineering

Microsoft's ACE live voice tutor: run a lesson as a state machine where the model only proposes narrow outputs and a harness validates them and decides the next step.

- Techniques: Lesson-as-state-machine harness; Per-step narrow prompts; Model proposes, harness decides; Right-size the model to the harness; Reliability coin-flip test
- Tools: Claude Opus 4.7, Claude Haiku 4.5

## [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../videos/vSx5IULvBns.md)
`vSx5IULvBns` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, enterprise-adoption

Resolve AI engineer argues production ops, not coding, is the bottleneck, and shows always-on cloud background agents that run on schedules, events and messages, with deployment monitoring as the lead use case.

- Techniques: Trigger-typed background agent; Per-change check plan generated from the diff; Time-bounded watch with agent-chosen duration; Confidence-gated reply with human confirmation; Feedback in the thread edits the standing task; Expose agent capabilities over MCP
- Tools: Slack, Microsoft Teams, GitHub release tags, Kafka, CI/CD pipelines, feature flag systems, MCP servers, Granola

## [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](../videos/XLEYtv3cMlw.md)
`XLEYtv3cMlw` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, multi-agent, evals

Sina Shahandeh (Radicait) on why coding-agent research loops stall on open-ended science, and how decomposing a codebase into linked component docs plus cross-model critique gets better hypotheses.

- Techniques: Hierarchical component docs as a scaffold; Hypothesis generation over each component; Multimodal model as a qualitative metric; Split roles across models in the loop; Per-iteration outcome review
- Tools: Codex, Obsidian, Gemini, Oracle CLI, GPT-5.5 Pro (as transcribed)

## [When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain](../videos/bUJgirn4_yc.md)
`bUJgirn4_yc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: data-engineering, memory

DataChain's Dmitry Petrov argues coding agents need a "data harness" for physical and unstructured data (video, sensors), built on Pydantic schemas, incremental checkpoints and reusable derived datasets.

- Techniques: Pydantic schema as the only data model; Typed mapper and generator functions for parallel processing; Incremental runs with checkpoints; Check for an existing derived dataset before computing; Per-dataset knowledge note with lineage
- Tools: DataChain, Pydantic, Claude Code, YOLO, Ray, Spark, Dask, Git4Data

## [Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley](../videos/Sir59K8ZDPU.md)
`Sir59K8ZDPU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: security-guardrails, data-engineering

Frank Coyle argues agents need ontologies as a symbolic validator around LLM tool loops, checking outputs against domain constraints before acting.

- Techniques: Validator gate after each tool call; Two-layer boundary checks (Pydantic plus ontology); Side-effect-free planning, then commit; OWL constraints for business rules; Reuse existing vocabularies; Bounding and monitoring agent loops
- Tools: Claude API (Python client, stop_reason tool-use loop), Pydantic, OWL, RDFS, schema.org, DBpedia, Dublin Core, FOAF

## [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../videos/Cc0_nyxROBA.md)
`Cc0_nyxROBA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, training-finetuning-rl, security-guardrails

Gaurav Mishra (Amazon AGI Lab) on why RL-trained computer-use agents break on real login screens, ads, and expired sessions, and how to adapt training and the harness to real-world messiness.

- Techniques: Simulated messy environments for agent RL; Recovery as a native model action; Process reward model over the trajectory; Action risk classifier in the harness; Harness-level credential and loop guardrails; Checkpoint, rollback, and audit trail; Forced human handoff; Adversarial tasks in mainstream training; Design-partner failure loop
- Tools: Playwright, WebMCP, MCP, web search APIs, PPO, GRPO

## [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](../videos/khVX_BUnEwU.md)
`khVX_BUnEwU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: skills-self-improvement, memory, multi-agent

Yohei Nakajima presents Active Graph, an experimental event-sourced graph runtime where an immutable typed log is the agent's ground truth and small behaviors coordinate through shared state; main takeaway is that log-centric design gives replay, forks, resume and gated self-modification for free.

- Techniques: Log-as-memory retrieval; Graph-subscription behaviors and graph-query views; Failure-type-scoped, gated self-edits; Acceptance test by simulated win rate with a confidence bound; Debug by querying the event log, not session logs; Pack-based composition of agents
- Tools: Active Graph, BabyAGI, LongMemEval, Replit, Claude Code, LangSmith (mentioned as a comparison), Kaggle Pokemon trading card game competition

## [Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](../videos/mOf-PP4mVjA.md)
`mOf-PP4mVjA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, rag-retrieval, voice-multimodal

TwelveLabs' James Le argues video needs a persistent memory layer (a context graph over moments, entities and relationships) rather than frame sampling, search or long context, and demos a video agent called Jockey.

- Techniques: Context graph over video moments; Ingest once, reason many times; Timestamp-grounded outputs; Intent-configurable extraction; Video worker harness; Evaluate retrieval, synthesis and budget separately
- Tools: TwelveLabs Marengo (multimodal embeddings for spatial-temporal spans), TwelveLabs Pegasus (video-aware language model used as the reasoning layer), Jockey (TwelveLabs video agent product used for the demos)

## [Scaling up Continual Learning — Ronak Malde, Trajectory](../videos/zL1kLftVTlo.md)
`zL1kLftVTlo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, skills-self-improvement

Ronak Malde (Trajectory) on scaling continual learning: on-policy self-distillation with privileged hints as a step past GRPO, plus fixes for long tool-calling runs (step-level weighting, hint-leakage control).

- Techniques: On-policy self-distillation (OPSD); Step-level divergence weighting for long trajectories; Residual guidance via linear combination of hint strengths; LLM-filtered hints to prevent leakage; Inspect rollouts for hint leakage
- Tools: GRPO, OPSD, OpenClaw RL, LiveCodeBench, Mercor APEX-Agents

## [The New Primitives: Building AI Native Software — Kwindla Kramer, Daily](../videos/LZuWZRze3MU.md)
`LZuWZRze3MU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: product-ux, multi-agent, voice-multimodal

Kwindla Kramer (Daily, PipeCat) argues agents are a stage on the way to AI-native software, using 80 years of computing history and demos of a real-time Knowledge Navigator and a multiplayer LLM game.

- Techniques: Asynchronous non-blocking context compression for sub-agents; Long-running sub-agents that share context; Progressive skills loading; Dynamic UI generation driven by the agent; Real-time voice plus LLM orchestration with a pipeline framework
- Tools: PipeCat, Gradient Bang, Daily, Tavus

## [MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef](../videos/-jY2T2PiJBE.md)
`-jY2T2PiJBE` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: mcp-and-tools, product-ux

Ido Salomon and Liad Yosef, the creators of MCPUI and maintainers of the MCP Apps spec, explain how MCP Apps lets servers ship interactive UI into chat hosts and how control of the user journey shifts to the host.

- Techniques: Serve UI as an MCP resource linked to a tool call; Host-mediated event flow from app to model; Three control levels for app-driven steps; Interop: wrap one generative UI payload for several hosts
- Tools: MCP (Model Context Protocol), MCP Apps (official MCP extension), MCPUI, MCP Apps SDK / spec repo (spoken as 'Xtaps' in captions; the official model context protocol repository), ChatGPT Apps / Apps SDK, Claude (including its generative UI feature), VS Code, Slack, Cursor, GitHub Copilot, Goose, Block agent e-commerce

## [MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal](../videos/s4r6nk5WsZw.md)
`s4r6nk5WsZw` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: mcp-and-tools, infra-cost-scaling

Cornelia Davis (Temporal) explains why no MCP clients support MCP Tasks (async long-running tools) in v1, shows live demos of durable purchase-order and invoice workflows, and walks through the v2 changes that make tasks stateless and extension-based.

- Techniques: Map task lifecycle onto a domain state machine; Signal into a long-running workflow for approvals; Client-side task tracker workflow; Parallel back-office steps beside an async tool call
- Tools: MCP Tasks, FastMCP, Temporal

## [Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software](../videos/2aS7aKoXn64.md)
`2aS7aKoXn64` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, training-finetuning-rl

Theta Software on designing RL environments and LLM judges for long-horizon work, plus a critique of current finance agent benchmarks, which they say are saturated and mostly too short to count as long-horizon.

- Techniques: Judge with read-only environment access, as an agent; Make long trajectories queryable before judging; Pair deterministic checks with a rubric judge; Rubric QA suite; Check learnability and reward density
- Tools: METR time-horizon benchmark (cited, not a tool used), GDPval (benchmark, cited), BankerToolbench (benchmark, cited), APEX-Agents (benchmark, cited), Grafana, GitHub (CI/CD logs, PRs), AWS CloudWatch, Codex models (cited), Claude models (cited), GPT-5.5 (cited)

## [Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute](../videos/k35LeKZEhiE.md)
`k35LeKZEhiE` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, enterprise-adoption

Raymond Feng (Applied Compute) on post-training agents that learn on the job: how RL loops break when you do not own the harness, and the environment-fidelity failures that teach models bad habits.

- Techniques: Replayable sandbox for multi-rollout RL; Graded chats as the only training interface; Audit the environment for infrastructure failures before trusting a run; Log model requests and responses as the training source; Mine traces for failure modes, then build the dataset

## [The Model Was Right. The Harness Failed. — Vinoth Govindarajan, OpenAI](../videos/BInpv7lGp1o.md)
`BInpv7lGp1o` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: observability, security-guardrails

Agent production failures are mostly harness failures, not model failures; the talk gives a state-ownership, ordered-commit, lifecycle, authority and receipt framework, using OpenClaw incidents as case studies.

- Techniques: Session lane / single ordered writer; Run deadlines, cancellation and watchdog; Scoped approval object; Run receipt as the audit record; Idempotency keys on side effects; Verify at the user-visible edge; Five-question production audit
- Tools: OpenClaw, OpenAI Agents SDK, Codex, Cursor, OpenCode, Claude Code, Hermes, Telegram

## [AI’s Jurassic Park Period — Aaron Stanley, dbt Labs](../videos/1lgFGaHoGq8.md)
`1lgFGaHoGq8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance

Aaron Stanley (CISO, former forensic consultant) argues that agents routing around constraints is the hidden risk, and proposes a corrigible, four-layer defense: deterministic floor, halt-and-explain agent, adversary agent, and structured human escalation.

- Techniques: Halt-and-explain default for constraint conflicts; Equal-power adversary agent reviewing worker actions; Natural-language escalation to humans; Layered deterministic floor; Intercept at the harness or tool-call hook; Runtime input policies instead of output string matching
- Tools: gVisor, egress filters, Chrome extension (installation blocked by a layered control)

## [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](../videos/xIt_mTQp6mY.md)
`xIt_mTQp6mY` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, coding-agents

Kyle Mistele (HumanLayer) argues agent loops should be built as incremental control loops (sensor, controller, actuator) that keep humans reading the code, not blind "Ralph" loops that dump 40k-line PRs.

- Techniques: Sensor, controller, actuator loop for code migration; Deterministic baseline plus per-PR ratchet; Ast-grep as the sensor; Golden-pattern skill for the actuator; Scheduled CI workflow as the loop runner; Feedback file plus comment-triggered re-steering; Single-open-PR flow control
- Tools: Claude Code, ast-grep, GitHub Actions, Effect (TypeScript), React Doctor, OpenClaw, OpenCode

## [Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates](../videos/u6jJcIFDLE4.md)
`u6jJcIFDLE4` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: multi-agent, context-engineering, enterprise-adoption

ZS Associates explain why their multi-agent pharma analytics pipeline failed and how they rebuilt it: deterministic signal detection, one reasoning agent, and a knowledge graph used as a control plane.

- Techniques: Probe the design with a coding agent; Deterministic signal gate feeding an investigator agent; Single reasoning owner with scoped investigation subagents; Knowledge graph as the agent's control plane; Hypothesis-traversal investigation loop
- Tools: Claude Code, bash, knowledge graph (tool not named), relational database (not named)

## [Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)](../videos/IvE8n-ylFYY.md)
`IvE8n-ylFYY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, sandboxing-execution, governance-compliance

Steve Korshakov (Bee, acquired by Amazon) explains how an always-on personal-agent wearable keeps data unreadable even to its own company, using client-held keys, attested workloads, and two-tier release controls.

- Techniques: Client-held keys with attested key release; Forced key expiry window; Split base image and deployment manifest; Private CA for internal attestation certificates; Minimal, auditable trusted code base; Per-agent sandbox with minimal capabilities
- Tools: Sigstore-style transparency log (auto-caption reads as 'six store'), Confidential compute nodes, Private certificate authority, OpenClaw (auto-caption reads as 'open claw'), Claude Code (auto-caption reads as 'cloud code')

## [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore](../videos/26RtyAm9y_Q.md)
`26RtyAm9y_Q` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: voice-multimodal, mcp-and-tools, security-guardrails

Corey Gallon on driving websites with agents via a shell CLI over the Chrome DevTools Protocol, climbing from synthetic clicks to trusted input to human-like motion, and beating Cloudflare Turnstile, MT Capture, Lemin and reCAPTCHA v2.

- Techniques: CLI over MCP for repeatable browser tasks; Cross-channel verification after each action; Lowest-rung escalation; Coordinate-based trusted click through closed shadow roots and cross-origin iframes; Solver plus operator split; Explore, then codify
- Tools: Chrome DevTools Protocol (CDP), Chrome Agent (speaker's Python CLI), Cloudflare Turnstile, MT Capture, Lemin (auto-captioned as 'lemon'), reCAPTCHA v2, Outlook web client

## [How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh](../videos/Tt2kX2sgQio.md)
`Tt2kX2sgQio` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: governance-compliance, data-engineering, enterprise-adoption

Kepler's CEO argues finance AI needs a deterministic substrate: the model points to sources and decides what to compute, while code extracts, checks and calculates numbers, with replayable derivation chains.

- Techniques: Atomic provenance ledger; Model decides, code computes; Derivation chains for derived metrics; Deterministic sanity gate on model output
- Tools: Claude, XBRL, ChatGPT, GLM 5.2, Opus 4.8

## [Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic](../videos/K0X9QDRkIdg.md)
`K0X9QDRkIdg` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: sandboxing-execution, context-engineering, evals

Anthropic engineers explain how agent surfaces moved from the Messages API to Claude Managed Agents, which separates the brain from the hands, logs sessions durably, and adds vaults, dreaming and outcomes.

- Techniques: Brain/hands decoupling with on-demand sandboxes; Append-only session log as the resume point; Re-reading discarded context from the log; Vault-based credential injection; Restricted network allowlist per environment; Rubric and failure-case grader loop (outcomes); Batch dreaming over transcripts and memory; Harness-debt audit when models change
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, MCP servers, MCP tunnels, self-hosted sandboxes

## [Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft](../videos/o6U_2vd967Y.md)
`o6U_2vd967Y` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: multi-agent, data-engineering

Divakar Kumar shows how to add an agent tier for gray-zone fraud decisions in an event-sourced system, feeding agents a semantic read layer built from CDC and broker events.

- Techniques: Tier-2 escalation for gray-zone cases; Semantic layer built from CDC and broker events; Fan-out to specialist agents with a verdict agent; Saga-style orchestrator as the sole cross-context router; Hard cap on the agent reasoning loop; In-memory short-term agent memory under an SLA
- Tools: Azure Cosmos DB (event store and change feed), message broker (unnamed), CDC / change feed, rule-based engine, ML risk model (third-party)

## [The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller](../videos/GgLQ02aO-hs.md)
`GgLQ02aO-hs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, data-engineering

DSPy maintainers argue AI programs should be functions with fixed typed contracts, with the model, prompts and harness swappable underneath and optimized against evals.

- Techniques: Typed signature with natural-language instruction; Three-part task spec (instructions, code constraints, examples); Predict-then-reason fallback in code; Optimizer over a fixed metric; Learn a harness per function (DSPy.Flex, announced)
- Tools: DSPy, GEPA (transcript says JEPA; caption error, prompt optimizer from Berkeley), Recursive Language Models (RLM), MultiModule GRPO, BetterTogether, DSPy.Flex (announced for DSPy 4)

## [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../videos/I3bpdgFJCUY.md)
`I3bpdgFJCUY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, context-engineering, skills-self-improvement

Ben Holmes (Warp) shows a markdown-first personal knowledge base: voice-dictate raw notes, have an agent enrich and link them, generate wikis, run it on a cloud schedule, and build graph views with HTML.

- Techniques: Enrich-note skill with a processed-timestamp marker; Controlled tag vocabulary with a no-invention rule; Backlinks via key-term search over a file tree; Raw folder to wiki generation; Sync-in, run, sync-out cloud schedule
- Tools: Obsidian, Obsidian Headless CLI, Warp, oz.dev, Hubble, Claude, Codex app, Exa, Tailwind CSS, Whisper Flow, Handy, GLM 5.2

## [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../videos/I6aiEf3aEFQ.md)
`I6aiEf3aEFQ` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: skills-self-improvement, memory

Yu Su (Ohio State, CEO of NeoCognition) argues intelligence and expertise are different axes and that continual learning, not bigger models, is what turns agents into domain experts.

- Techniques: Adaptive compression loop for agent memory; Rules stored with preconditions and exceptions; Select context by expertise instead of parallel brute force; Measure expertise per environment

## [First Steps Toward Automated AI Research — Richard Socher, CEO Recursive AI](../videos/pWXUkLP9uWM.md)
`pWXUkLP9uWM` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: models-research, evals

Richard Socher (Recursive AI) argues for automating scientific research via a "Eureka machine" and shows small auto-research wins on NanoChat, NanoGPT speedrun and CUDA kernels, while separating these from true recursive self-improvement.

- Techniques: Benchmark-gated auto-research loop; Short fixed-budget runs as the test; Reward-hack audit before trusting results; Simulation as the verifier
- Tools: NanoChat, NanoGPT speedrun, NVIDIA CUDA kernels, U.com web search for LMs

## [Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft](../videos/fnLBmfsI_Fg.md)
`fnLBmfsI_Fg` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: voice-multimodal, infra-cost-scaling

Microsoft's ACE live voice tutor uses a small model (Haiku 4.5) for speech only, moving reasoning, lesson state and planning into a code state machine to hit about 900ms response time.

- Techniques: Externalised state machine for a small speaking model; Per-turn summary handoff; Strict rules to keep small models on track; Model selection by latency budget
- Tools: Claude Opus 4.7, Claude Haiku 4.5

## [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](../videos/X1kp-ABIIxQ.md)
`X1kp-ABIIxQ` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: sandboxing-execution, observability, evals

Dan Farrelly (Inngest CTO) argues agent architectures decay fast unless the execution layer (durable state, retries, triggers, tracing) is separated from fast-changing context (prompts, models, tools) and compute (sandboxes).

- Techniques: Three-layer decomposition (execution / context / compute); Externalised durable step state with resume-from-failure; Cron-triggered health check, triage agent, and reviewer loop; Deferred outcome scoring from downstream events; Ephemeral sandboxes with state kept in the orchestrator
- Tools: Inngest

## [Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs](../videos/_cVfz88_j7A.md)
`_cVfz88_j7A` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: data-engineering, governance-compliance

Risa Labs (oncology) walks through automating prior-authorization workflows end to end, using confidence-gated multi-agent routing so only some orders skip human review.

- Techniques: Deterministic-first gating before LLM steps; Corroboration across independent sources before automating; Confidence-gated escalation to humans; Evidence-structured questionnaire answering; LLM-generated integration configs from a reusable action library; Self-healing loop for production automations
- Tools: RPA (robotic process automation, unnamed product), SQL database (unnamed), LLM (unnamed model) for extraction and config generation, Patient biomarker graph (internal, unnamed)

## [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../videos/5ZGyKWjQDr0.md)
`5ZGyKWjQDr0` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: memory, context-engineering, product-ux

Shlok Khemani traces how ChatGPT and Claude memory evolved from 2024 to 2026, and argues memory is a product and compute problem, not a RAG problem, with context as the real cap.

- Techniques: Running profile with background re-synthesis (dreaming); Search tools over past conversations instead of stored facts; User-visible and user-editable profile with re-synthesis on edit; Dense keyword-clue memory entries; Timestamped memory entries
- Tools: ChatGPT, Claude, Gemini, Poke, Claude Code, OpenClaw, Hermes

## [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](../videos/kiqubc5b5Yo.md)
`kiqubc5b5Yo` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: multi-agent, evals, enterprise-adoption

Morgan Stanley's AlphaLab, a multi-agent harness that automates quant research through research, critic-checked eval building, and Kanban-style experiments. Its main lesson: the value sits in strict eval environments and rubrics, not in the harness.

- Techniques: Scaffolded to-do list with re-prompting on early exit; Builder plus critics eval loop; Strategist, worker, and post-mortem Kanban loop; Containerised, Kaggle-style eval contract; Environments as RL reward signal; Rubric grading of each rollout's process; Meta-harness optimisation by an LLM; Provider-agnostic harness with functional tool calls
- Tools: Claude Code, Codex, Opus 4.5, Slurm, Kaggle, GRPO, NVIDIA Nemotron

## [Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet](../videos/7jjudsEhBtM.md)
`7jjudsEhBtM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: skills-self-improvement, context-engineering, governance-compliance

FactSet's principal AI engineer argues skills are the new product features and engineers should ship harnesses, then covers a minimal skill harness, routing via descriptions, eval-gated skills, and skill-library governance.

- Techniques: Minimal skill registry and loop; Write descriptions as routing signals; Cut skills by user intent; Front-load critical instructions and re-run evals on model upgrades; Shortlist skills before they hit the system prompt; Governance as a skill PR pipeline
- Tools: Anthropic Agent Skills (SKILL.md format), Claude Code, Codex, bash or code sandbox for skill scripts

## [It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard](../videos/I3znWC3MEXM.md)
`I3znWC3MEXM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools, governance-compliance

Kim Maida (Keycard) shows why API keys give agents overprivileged, unattributed access, and how OAuth token exchange (RFC 8693) per tool call, with policy checked before minting, fixes it.

- Techniques: Per-tool-call token exchange (RFC 8693); Policy-before-mint; Policy-gated human approval; Ephemeral, audience-bound bearer tokens; Layered scope design
- Tools: Keycard (security token service and policy governance), OAuth 2.0 token exchange (RFC 8693), Google sign-in (identity provider in demo), MCP (client, server, gateway)

## [The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI](../videos/q2JrUKBMf0w.md)
`q2JrUKBMf0w` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: evals, observability

Arize's founder argues that evals must add a third layer, agent-as-a-judge, that reads production traces, finds failure patterns, and can open fix PRs. It is a short vendor pitch with little method detail.

- Techniques: Agent-as-a-judge over traces; Three-layer eval stack; Trace-driven online evals; Repeated-tool-call loop detection
- Tools: Arize Signal, Agent as a Judge (Arize)

## [Local Agentic Theory For Mobile Games — Shafik Quoraishee & Joanne Song, The New York Times](../videos/418t26CVz-w.md)
`418t26CVz-w` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: local-ai, product-ux, inference-serving

NYT engineers on running small agents on-device inside mobile games, under per-frame time, memory and battery budgets, with live accessibility tuning through graded dials instead of fixed menus.

- Techniques: Per-frame perceive-predict-decide-act agent loop; Constraint graph over space, time and energy; Constraint satisfaction with backtracking; Graded accessibility dials driven by live signals; Live focus-path monitoring and layout auditing
- Tools: Efficient Zero V2 (sample-efficient RL, mentioned as state of the art up to 2024), WCAG 2.2 and WCAG 3.0 draft, Gaze estimation CNN, Google SIMA (transcript reads 'SEMA'; generalist agent framework mentioned briefly)

## [Evaling Video Slop — Maor Bril, Character.ai](../videos/b_PmGocP4rc.md)
`b_PmGocP4rc` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, testing-verification, voice-multimodal

Maor Bril (Character.ai) on evaluating AI video: frame-level metrics miss story, physics and pacing, so he distilled a judge committee into a small fast VLM trained on pairwise comparisons and run inside the generation loop.

- Techniques: Pairwise A-vs-B judge training; Manufactured negatives; Matched-encoding real-vs-AI pairing with identical annotation; Expert-committee distillation into a small VLM; Eval inside the generation loop; Calibration sessions with randomized annotation; Agent with validation tools
- Tools: Qwen (small VLM, post-trained), Dolby Atmos (audio quality), CLIP-style frame metrics, frame-drift metrics, Kling, Seedance, Veo, Sora, OpenTelemetry (requested, planned for harness)

## [Claude for Long-Horizon Tasks — Lance Martin, Anthropic](../videos/9QebvrrY3KY.md)
`9QebvrrY3KY` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: memory, multi-agent, context-engineering

Lance Martin (Anthropic) on designing long-horizon async agents: decouple brain from hands, verify in a separate context, dream offline to fix memory, and run org-level shared harnesses.

- Techniques: Brain/hands split with an append-only session log; Non-destructive context via append-only session object; Build/verifier loop in separate contexts; Dreaming: offline memory consolidation; General memory substrate with the model managing its own structure; Org-level shared harness with its own identity
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, Claude Tag, Message API, Continued Learning Bench, METR time-horizon benchmark, Slack

## [Every Harness Will Become A Claw — Sam Bhagwat, Mastra](../videos/8qWIPUia2O8.md)
`8qWIPUia2O8` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: sandboxing-execution, skills-self-improvement, product-ux

Sam Bhagwat (Mastra) argues agent harnesses will keep expanding into always-on "claws" with durability, initiative and learning, then shake out to a few winners. Mostly conceptual, with little hard data.

- Techniques: Durable turn streaming with resume; Queue, steer and interrupt on running threads; Session-scoped tool approval; Heartbeat wake-ups; Trace-driven continual learning; Cloud sandbox per parallel subagent
- Tools: Mastra, Claude Code, Codex, OpenClaw, Hermes Agent, Slack, Telegram, WhatsApp, GitHub

## [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../videos/Z-c11pV_uvU.md)
`Z-c11pV_uvU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: claude-code, context-engineering, multi-agent

Frank Coyle (UC Berkeley) walks through the Claude Certified Architect exam's scenarios and uses each one's anti-patterns to teach agent loops, subagent context isolation, compaction, and non-interactive runs.

- Techniques: Stop-reason-driven agent loop; Three-level CLAUDE.md hierarchy; Single-purpose subagents with minimal tools; Context slicing for critic and reviewer agents; Forked subtask context with summary return; Threshold-triggered compaction; Non-interactive CI runs with batch processing
- Tools: Claude Code, Claude API (messages, stop_reason, tool use), CLAUDE.md, MCP (Model Context Protocol), Message Batches API

## [Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber](../videos/31GUkCBD-Uc.md)
`31GUkCBD-Uc` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, observability

Uber's Uber Eats image pipeline (routing, enhancement, publish QA) and how they keep it aligned with human labels through offline evals, auto-tuning and a diagnoser that closes the production feedback loop.

- Techniques: Flat per-run JSON trace across the whole agent chain; Router as a classifier scored by a confusion matrix, with an N-by-N extension; Golden human-label set plus ship gate; Production drift loop: sample, re-label, diagnose, tune, benchmark, register; Reflect-and-synthesize prompt optimizer; Generate-edit-QA loop scored with pass@K; Pairwise judge with yes/no/unsure and product-agreed criteria; Redundant Swiss-cheese final gate; Diagnoser as a routing layer over all feedback; Replay flagged examples before releasing a config; Per-segment production metrics
- Tools: Arize

## [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing - Bala Ramdoss, Amazon Lens](../videos/maTp79FD9gI.md)
`maTp79FD9gI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: product-ux, mcp-and-tools

Bala Ramdoss (Amazon Lens) on why LLM agent output needs a typed rendering layer between model and screen: a versioned UI contract, streamed typed chunks, and a BFF that hydrates actions, so mobile clients stay dumb and safe.

- Techniques: Versioned rendering contract; Typed streaming UI blocks; BFF as renderer and hydrator; Design loading around streaming
- Tools: A2UI, CopilotKit, MCP apps

## [Alibaba Just Cut AI Agent Costs by 99% — Here's How](../videos/eCZwexfka6E.md)
`eCZwexfka6E` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: mcp-and-tools, token-cost-efficiency, skills-self-improvement

Alibaba's SkillWeaver paper cuts agent tool-routing tokens from 884k to 1,160 per query by decomposing, retrieving and composing tools, but the benchmark is self-run and execution was mocked.

- Techniques: Decompose-Retrieve-Compose tool routing; Skill-aware decomposition (SAD) feedback loop; Right-size decomposition granularity
- Tools: SkillWeaver (Alibaba research paper, pipeline name), CompSkillBench (Alibaba benchmark: 300 multi-step queries, 2,209 MCP-derived tools, 24 categories), Qwen2.5-7B-Instruct, Qwen Max, MCP (Model Context Protocol) ecosystem, as the tool source, LangChain, LlamaIndex (spelled 'Lama index' in the transcript), GPT 5.5 (mentioned as a model the market is racing to wire in), Opus (mentioned as a model the market is racing to wire in)

## [5 Open Source AI Tools That Feel ILLEGAL To Know About](../videos/-UxcljWN49I.md)
`-UxcljWN49I` · Kai Explains · 2026-08-02 · q2 · intro · review · also: memory, coding-agents, voice-multimodal

Roundup of five open-source agent building blocks (Browser Use, Firecrawl, Mem0, OpenHands, Dify) mapped to read, act, remember, code and orchestrate roles. Mostly star counts and vendor stats, with no hands-on steps.

- Techniques: Read-decide-act browser agent loop; Scrape-to-markdown before retrieval; Two-phase memory: extract on write, retrieve on read; Sandboxed plan-write-test-iterate coding loop; Per-step tracing and worker queues for visual workflows
- Tools: Firecrawl (transcribed 'fire crawl'), Browser Use, Mem0 (transcribed 'Memzero'), OpenHands (transcribed 'open hands'), Dify (transcribed 'DeFi'), Devin (transcribed 'Devon'; Cognition AI, mentioned as a $500/month closed product), WebVoyager (benchmark, 586 tasks), SWE-bench (benchmark), Langflow (mentioned as Dify's origin comparison), OpenTelemetry (Dify export)

## [LangChain Open Sourced Claude Code (Works With ANY Model)](../videos/jtWjkdBNqlk.md)
`jtWjkdBNqlk` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: memory, multi-agent, claude-code

Kai Explains reviews LangChain's open-source DeepAgent, a model-agnostic take on Claude Code's harness, arguing it wins for shipping agents to users while Claude Code still wins for personal terminal coding.

- Techniques: Audit your harness against the five-part checklist; Subagents with isolated context returning one summary; Keep agent memory in a store you control; Swap the model behind a fixed harness; Use a lighter agent abstraction for bounded tasks
- Tools: DeepAgent (Deep Agents, LangChain), LangChain 1.0, LangGraph, LangSmith deployment, Claude Code, Claude Opus 4.8 (as stated), Claude Managed Agents, Codex, Cursor agent mode, GPT 5.5 (as stated), PostgreSQL, agents.md

## [Postgres Just Got It's Biggest Upgrade In Years](../videos/4Lmqvn_yz-c.md)
`4Lmqvn_yz-c` · Better Stack · 2026-08-02 · q3 · intro · tutorial · also: dev-tools

Better Stack walkthrough of PG Durable, a Microsoft open-source Postgres extension for crash-proof durable functions, scheduling, retries and human-in-the-loop approval in plain SQL.

- Techniques: Run a recurring job inside Postgres; Park a workflow until a human approves; Fan out and fan in; Local dev via Docker Compose
- Tools: PG Durable (pgdurable, Postgres extension, Microsoft, open source), PostgreSQL 17, Docker Compose, npm (demo scripts)

## [All The Types Of Claude Loops Explained In 13 Minutes](../videos/8wsM0euQOvc.md)
`8wsM0euQOvc` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: claude-code, multi-agent, testing-verification

AI LABS sorts Claude Code agent loops into five types (stateless, learning, multi-agent review, verification, workflow-improvement) with setup steps; anecdotal, with a sponsor segment.

- Techniques: Goal-command loop with tests as the acceptance criterion; Save-every-working-version rule in CLAUDE.md; Skill-improvement loop (learning loop); Multi-agent review loop with an orchestrator; Implementer vs. scorer verification loop; Workflow-improvement loop with a process optimizer
- Tools: Claude Code, CLAUDE.md, Haiku (completion checker in the goal loop), Ralph loop (named as a stateless loop example), goal command, skill loop command (name as spoken), learning.md, thermonuclear review (review skill, named as spoken), orchestrate command, review loop command, iterate command, JSON files (findings and scores)

## [MCP vs REST vs A2A How AI Agents Actually Talk](../videos/psszX04xeGU.md)
`psszX04xeGU` · Kai Explains · 2026-08-02 · q3 · intro · other · also: mcp-and-tools, multi-agent

Explainer arguing REST, MCP and A2A are stacked layers, not rivals: REST links programs, MCP links an agent to tools, A2A links agents to agents. Advice: learn MCP first and add A2A only for multiple independent agents.

- Techniques: Map each integration to one protocol layer; Expose each tool once as an MCP server; Wrap an existing REST API with a thin MCP server; Publish an agent card for discovery and delegation; Adopt multi-agent protocols only when the pain is specific
- Tools: REST, MCP (Model Context Protocol), A2A (Agent2Agent), JSON-RPC 2.0, HTTP, stdio

## [MCP Is Getting Its Biggest Update Ever (No One's Ready)](../videos/k5f1uID3GcU.md)
`k5f1uID3GcU` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: mcp-and-tools, security-guardrails, infra-cost-scaling

MCP's July 28 rewrite drops the handshake and session ID so any replica can serve any request; state moves into owner-checked handles, and auth fragmentation across clients is the bigger unresolved problem.

- Techniques: Make stateful MCP tools own their handles; Round-trip state through the client as a sealed blob; Split pure tools from stateful tools in deployment; Gateway and proxy checklist for the MCP change; Test each server against every major client; Load tool definitions on demand in the client
- Tools: MCP (Model Context Protocol), July 28 spec revision, OAuth 2.1, Claude Code, Claude.ai, Anthropic API, ChatGPT, Google Cloud, VS Code, Redis, Salesforce, JIRA, Snowflake

## [Build Your Own Fully Private Local AI Stack (Chat, RAG, Coding Agent & Automation)](../videos/np8booSU7Og.md)
`np8booSU7Og` · Kai Explains · 2026-08-02 · q3 · practitioner · tutorial · also: local-ai, rag-retrieval, coding-agents

Kai Explains walkthrough of a fully local AI stack: llama.cpp behind one OpenAI-compatible endpoint, with AnythingLLM for chat and RAG, Pi as a local coding agent, and n8n for email automation.

- Techniques: Single OpenAI-compatible endpoint as the integration bus; llama-server router preset mode, with LlamaSwap as fallback; Headless AnythingLLM in Docker, configured from the UI; Local RAG with AnythingLLM defaults; Pi as a local coding agent; n8n email triage with a local model; Always-on home lab hardening
- Tools: llama.cpp, llama-server, LlamaSwap, AnythingLLM, Open WebUI, LanceDB, Pi (coding agent, npm), OpenCode, n8n, Docker, Docker Compose, Portainer

## [Best Local Agent Harness Right Now (My Top 3)](../videos/YgyyWDGeQWM.md)
`YgyyWDGeQWM` · Kai Explains · 2026-08-02 · q3 · intro · review · also: coding-agents, local-ai, context-engineering

A survey of local/open coding-agent harnesses (OpenCode, Aider, Pi, plus OpenHands, Cline, Goose) arguing the harness now matters more than the model, with local-model pairing advice and a warning that the list goes stale fast.

- Techniques: Git-native atomic AI commits (Aider); Mid-session model downgrade for cost; Lazy-loaded skill blocks to keep the base prompt small (Pi); Custom subagents with per-agent model and permissions (OpenCode); Parallel agents on one GPU via vLLM; Local model sizing by memory footprint; Pre-standardization vetting checklist
- Tools: OpenCode (172k+ GitHub stars per speaker; 1.68M weekly npm installs as of June 2026), Aider, Pi (by Armin Ronacher), OpenClaw, OpenHands (spoken as 'Open hands'), Cline (spoken as 'Klein'), Goose, Roo Code (archived May 2026), Gemini CLI, Claude Code, Claude Opus 4.8, GPT-5.5

## [Claude Code Loop Explained | Loop VS Prompts](../videos/pGS7ku-4Fbs.md)
`pGS7ku-4Fbs` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: claude-code, token-cost-efficiency, testing-verification

Walks through Anthropic's "Getting Started with Loops" post for Claude Code: four loop types (turn, goal, time, proactive) defined by who decides when to stop, plus the skill.md, turn-cap and token-control practices that keep loops safe.

- Techniques: Define the stop condition before starting a loop; Write skill.md as a measured verification protocol; Goal loop with deterministic success criteria and a hard turn cap; Choose local or cloud for time-based polling; Fresh-context adversarial reviewer; Pilot, then scale, and monitor spend mid-run; Route models by task
- Tools: Claude Code, /loop, /schedule, /goal, /usage, /workflows, skill.md, Lighthouse (named as a score example), Opus (named as an example of a capable model)

## [The Guy Who Coined "Event Gateways" Explains Why Webhooks Are Dying | Better Stack Podcast Ep. 17](../videos/ElaEGr2t9XQ.md)
`ElaEGr2t9XQ` · Better Stack · 2026-08-02 · q3 · practitioner · interview · also: infra-cost-scaling, product-ux, dev-tools

Hookdeck's founder explains why he built an event gateway and the open-source Outpost to replace fragile webhook handling with queuing, replay, push-based rate control and per-vendor latency monitoring. Substantive but vendor-led.

- Techniques: Push-based webhook intake in front of your endpoint; Respond fast, queue the work; Per-vendor delivery latency baseline and alerting; Per-tenant queues with a shared push consumer; Event destinations instead of HTTP webhook transport; Open-source-first with a managed twin; Verify agent-written contributions against real APIs
- Tools: Hookdeck (Event Gateway), Outpost (Apache 2.0, open source), Hookdeck Radar, Kafka, RabbitMQ, Amazon SQS, Google Cloud Pub/Sub, AWS EventBridge, Azure Event Grid, Kong event gateway, Cloudflare Queues, BullMQ

## [A Song of Types and Agents - Roberto Stagi, Ratel](../videos/UlFB6efYN5Q.md)
`UlFB6efYN5Q` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: dev-tools, coding-agents

Roberto Stagi argues TypeScript is overtaking Python for the agent and application layer, because coding agents default to it, npm is deep, and one Zod schema can type the whole stack; Python keeps training and serving.

- Techniques: Shared Zod schema across the full stack; Single-language monorepo for agent apps; Split by layer: Python for training and serving, TypeScript for the app and agent layer
- Tools: TypeScript, Python, Zod, npm, Vercel AI SDK, FastAPI, React, Claude Code, Cursor, Codex, Lovable

## [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](../videos/BqZrTdgBaPw.md)
`BqZrTdgBaPw` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: mcp-and-tools, product-ux

Stephan Steinfurt (TNG) shows a nightly, fully automated chess-explainer pipeline: a Gemini 3.1 Pro agent with chess tools narrates analysed human games as YouTube videos.

- Techniques: Engine plus LLM split with tools; Let the reasoning model choose tools rather than pre-computing; Deliberately conflicting tool outputs; Nightly batch with a structured intermediate format; Monitor odd outputs and treat them as signals
- Tools: Gemini 3.1 Pro, Grok 4, ElevenLabs v3, Maia (captioned as Maya), chess engine (unnamed), web search

## [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../videos/c35YoMdnI78.md)
`c35YoMdnI78` · AI Engineer · 2026-07-18 · q3 · practitioner · panel · also: software-factory, testing-verification, context-engineering

Panel debate on whether agent "loops" (Ralph-style, bash-while-true) are hype or working practice; the consensus is loops work for verifiable tasks, need deterministic feedback and human-owned architecture, and are not yet a full software factory.

- Techniques: Fresh-context loop with file-system state; Back-pressure hooks that talk back; Deterministic controller around the LLM step; Context budget with headroom; Bare-model baseline on each new release; Explicit cost decision for high-value verification; Start small and iterate on real users; Vendor code and minimise open-source dependencies; Prefer statically typed languages for agent-maintained code
- Tools: Claude Code, Ralph loop (bash while-true), pre-commit hooks, PostHog, Notion, Sentry, Git, npm, Rust, Haskell, Python, TypeScript

## [Agents Need Feature Flags - Sachin Gupta](../videos/zU4EagB311U.md)
`zU4EagB311U` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: governance-compliance, security-guardrails

Sachin Gupta argues agents need feature-flag discipline: six flag types (prompt, tool, model, memory, autonomy, kill switch), a middleware layer, and a kill switch shipped first, with four metrics to track.

- Techniques: Six-surface flag taxonomy; Flag middleware between user and agent loop; Kill switch with three properties; Canary prompt variant; Five-step rollout order; Resolve flags per turn and log segment context; Bypass caching for flag-sensitive responses; Flag hygiene rules
- Tools: LaunchDarkly, Unleash, Lift (as spoken), homegrown flag service

## [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](../videos/MpZzWMdmQCE.md)
`MpZzWMdmQCE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: testing-verification, claude-code, coding-agents

Talha Sheikh (Checkout.com) argues coding agents need deterministic, shareable verification hooks, not better instructions, and that the real engineering work is designing the verification harness.

- Techniques: Stop-hook deterministic verifier; Fail-and-retry feedback loop; Layered enforcement at multiple points; Language-agnostic check contract; Executor plus advisor loop; Cheap model plus strong harness
- Tools: Claude Code, Claude Code hooks (Stop hook), VectorV1 / Vector Harness, Haiku, Opus, Anthropic Glasswing / Project Mythos (named, not described)

## [Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc](../videos/RGiXcVxSD3s.md)
`RGiXcVxSD3s` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: product-ux, observability, skills-self-improvement

Vertical AI talk by the Filed CTO arguing chat and citations are not enough; products should be built for delegating long-running work to agents, with skills, traces, pause-and-intervene and plan approval.

- Techniques: Delegation-first task selection; Implicit skill capture from usage; Per-value trace-back for trust; Pause-and-tag intervention; Plan approval gate for irreversible actions
- Tools: Wispr Flow

## [The Prompt is the Platform - Dominik Tornow, Resonate HQ](../videos/DqtmZE6Hl0g.md)
`DqtmZE6Hl0g` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: testing-verification, context-engineering

Dominik Tornow (Resonate) argues the spec, not the code, becomes the product: agents should design a system via deterministic simulation before writing the production implementation.

- Techniques: Intermediate concrete spec between abstract spec and implementation; Simulation-first design loop for the agent; Deterministic simulation of target dependencies with legal fault injection; Forbidden-fruit trace events; Shrink the protocol and build on target primitives
- Tools: NATS.io, Postgres, Rust, Python, TypeScript, Go, Java, Resonate SDK

## [Build Systems, Not Code - Angie Jones, Agentic AI Foundation](../videos/ZD9-4fW2HhM.md)
`ZD9-4fW2HhM` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, multi-agent, security-guardrails

Angie Jones on designing agentic systems like software: systems thinking, workflow paths, decomposition, code-vs-model-vs-human splits, contracts, idempotent retries, and maintainable agents.md files.

- Techniques: Decompose a giant agent prompt by responsibility; Route work by task type: code, model, or human; Structured decision records as agent memory; Idempotent action log with state-based resume; Evidence-not-instructions handling for untrusted content; agents.md at every level with a cold-start test
- Tools: agents.md, agent skills, subagents, Karpathy LLM Wiki (agent memory layer)

## [The Log Is The Agent - Ishaan Sehgal, Omnara](../videos/UPwGaM2MKHY.md)
`UPwGaM2MKHY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, observability

Argues an agent's identity is its append-only event log, not the model or runtime; once workers are disposable, reliability, forking, sharing and ownership follow from the log design.

- Techniques: Log-first agent loop; Persist pending permissions as events; Projections over one record; Compaction as forked log; Fork at a point in the log; Share by access grant, not transcript copy
- Tools: Claude Code, Codex, OpenCode, Claude SDK, Cloudflare Durable Objects, SQLite, JSONL

## [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](../videos/pMggiOb18tc.md)
`pMggiOb18tc` · AI Engineer · 2026-07-18 · q3 · intro · keynote · also: coding-agents, multi-agent, software-factory

OpenAI's Codex team argues engineers move from watching agents to running manager-worker loops, with human attention as the scarce resource to spend on the outer loop.

- Techniques: Long-lived manager agent over worker agents; Trigger-driven manager wake-ups; Offload test runs to a separate machine; Server-side compaction for long tasks; Parallel attempts with a fast, strong model; Shared instruction file across agents; Chat-first UI with escalation to direct editing
- Tools: Codex, Codex app, Codex Cloud, Responses API, AGENTS.md, OpenClaw, OpenCode, Cerebras, VS Code extension, Xcode, JetBrains, Slack

## [Modern Post-Training: A Deep Dive  — Will Brown, Prime Intellect](../videos/V-EDrhIhHzQ.md)
`V-EDrhIhHzQ` · AI Engineer · 2026-07-18 · q4 · deep · workshop · also: training-finetuning-rl, evals, infra-cost-scaling

Will Brown (Prime Intellect) walks through modern post-training: environments as evals, the verifiers v1 task/harness/runtime split, async RL with an interception server, and the PrimeRL trainer.

- Techniques: Task / harness / runtime decomposition; Fake base URL interception for RL on real harnesses; Async rollout batching with off-policy tolerance; Message-level trace with token mapping; Algorithm and loss separation with a registry; Group-relative shaping for length and efficiency; Same-task eval CLI with swappable harness and runtime
- Tools: verifiers, PrimeRL, Renderers, TorchTitan, Megatron, Harbor, NemoGym, OpenEnv, Hugging Face datasets, uv, Docker, Claude Code

## [Beyond the Harness: A Journey Towards Adaptative Engineering - Rajiv Chandegra, Annicha Labs](../videos/qdZzND79mcg.md)
`qdZzND79mcg` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: multi-agent

A London-based practitioner argues that fixed agent harnesses fail in messy real-world settings and proposes "adaptive engineering," where engineers set constraints and let multi-agent harnesses emerge and reshape at runtime.

- Techniques: Constraint-setting instead of outcome-setting; Sense-and-respond loop for complex work; Penalise redundancy to force specialisation; Dial the coupling rate; Three-question constraint review; Selection pressure check against drift
- Tools: Claude Code, Codex, Pi, Cursor, LangChain, Hermes, Cline, Goose

## [Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs](../videos/vljxQZfJ9wY.md)
`vljxQZfJ9wY` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: evals, observability

Nishant Gupta (Meta Superintelligence Labs) argues agent evals must score workflow behavior from production telemetry, not model answers or benchmarks, and should run continuously as a control-plane function.

- Techniques: Scenario-driven offline evals; Production telemetry as the eval set; Targeted human review to calibrate automated evals; Continuous evaluation loop; Agent tracing like distributed tracing; Evaluation as a control plane

## [Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](../videos/Lc8zRh9muoY.md)
`Lc8zRh9muoY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: observability, testing-verification

Microsoft's Chronicle PoC records each agent node's inputs and outputs as a replayable trace, so production failures can be debugged and turned into offline tests. The talk argues for replayability rather than chasing bitwise determinism.

- Techniques: Boundary-annotated run recording; Record at the node boundary, not the network; Replay with selective stubbing plus assertions; Zero-model-call deterministic tests from traces; Guardrails at the tool boundary; Keep generation variance on
- Tools: Chronicle (Microsoft proof of concept; code link shown by QR code, URL not spoken)

## [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../videos/HEFSExa0xl0.md)
`HEFSExa0xl0` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: mcp-and-tools, testing-verification, evals

Witan Labs on lifting coding agents' spreadsheet accuracy from about 50% to 92% by replacing 15 tools with one persistent-state REPL, plus a formula engine and render engine as the verification loop.

- Techniques: Single persistent-state REPL instead of many tools; Verification loop with domain engines; Golden-spreadsheet black-box evaluation; Domain-knowledge reminders in the prompt; Trace review for plumbing bugs
- Tools: Node.js REPL, JavaScript, TypeScript type definitions, C#, LLM-as-judge, Witan Labs internal formula engine, Witan Labs internal render engine

## [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](../videos/2e9ANoOEn28.md)
`2e9ANoOEn28` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: security-guardrails, multi-agent, evals

Aditya Bhargava (Etsy) argues the agent harness, not the model, drives results, especially for weaker models, and walks through building a coding-agent harness step by step in his language Agency.

- Techniques: Tools as plain functions with docstrings; Interrupt plus handler for approvals; Partial function application for capability scoping; ReAct test-feedback loop; Subagents as tools with grouped tool sets; Objective-driven prompt optimization; Serializable pause and resume at interrupts
- Tools: Agency (agencylang.com, TypeScript-like agent language, installed via pnpm), HarnessBench (harness benchmark, 106 tasks), Claude Code (cited as an example agent: Opus model plus harness), Built-in Agency log viewer, Built-in Agency standard library (includes Wikipedia search tool)

## [AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](../videos/T0HhO4YtTfE.md)
`T0HhO4YtTfE` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: evals, product-ux, context-engineering

A MongoDB developer advocate walks through a four-phase framework (product requirements, system design, evaluation and monitoring, cost/latency optimization) using a health insurance claims review system as the worked example.

- Techniques: Four-phase AI system design framework; Quantified solution-agnostic business problem; Three-axis AI role classification; Per-source retrieval strategy from update cadence and content type; Simplest-design-first, evaluate, then iterate; Guardrails as measurable rates; Production signals from human behaviour; Structured outputs as a reliability guard
- Tools: MongoDB, Voyage AI

## [Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon](../videos/LrGCT7G_rU8.md)
`LrGCT7G_rU8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: data-engineering, security-guardrails, evals

Anna Marie Benzon presents a capstone ETL remediation agent: deterministic rules detect facts, tabular Q-learning picks among six bounded actions, and an external safety layer can force escalation. Results are from synthetic benchmarks.

- Techniques: Event-triggered diagnose-decide-act-verify loop; Rules for facts, learning for choices, guardrails for authority; Tabular Q-learning over a small discrete state; Propose, check, execute, and record separately; Multi-seed evaluation with baselines and confidence intervals
- Tools: AWS Glue, Amazon EventBridge, AWS Lambda, Amazon CloudWatch, AWS Glue Data Catalog, Amazon S3

## [Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](../videos/4uFVSLgD2Q4.md)
`4uFVSLgD2Q4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: enterprise-adoption, evals, sandboxing-execution

OpenGov's Gabe De Mesa on how they built and scaled OG Assist, an in-product agent: an in-house Effect-native agent loop, A2A contracts, approval gates, ephemeral sandboxes, and rolling-summary context.

- Techniques: Effect-native agent loop with injected language model; A2A agent card as the API contract; Deterministic approval interrupt; Automated tool-call evals in CI; Ephemeral sandbox per agent task; Rolling summary with recent-window and recall; Runtime generative UI via registered primitives; Tools to toolkits to model registration
- Tools: Effect, Effect AI, LangGraph, A2A protocol, A2UI, Claude, Cursor, Claude Cloud Agents

## [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](../videos/uiP88SpCi1Q.md)
`uiP88SpCi1Q` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: token-cost-efficiency, infra-cost-scaling, context-engineering

An AWS developer advocate lists five ways to cut agent token spend: cache the system prompt, route by task difficulty, offload large tool results, cap tool loops, and trim conversation history, with per-tool observability to check each one.

- Techniques: System prompt and tool caching; Difficulty-based model routing; Tool result offload and summarization; Max-iteration cap on tool loops; Per-tool loop and latency observability; Sliding window history with summarization
- Tools: Strands Agents, Claude Haiku, Claude Sonnet

## [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](../videos/spNAUEgq_A8.md)
`spNAUEgq_A8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: multi-agent, context-engineering, infra-cost-scaling

Justin Schroeder (Standard Agents) argues that small, isolated domain-specific agents composed under a coordinator beat ever-growing context-stuffed general agents on cost, scope, portability and scaling.

- Techniques: Composition of isolated domain agents; Scoped delegation requests; Per-task model routing; Hook-injected runtime facts; Capability scoping per agent; Recursive sub-agent tree
- Tools: Claude, Codex, OpenClaw, Hermes, MCP, Vercel AI SDK, Vercel Eve, Figma, Playwright, Gmail, Google Sheets, Google Workspace

## [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](../videos/pSto5YaNGUo.md)
`pSto5YaNGUo` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: evals, observability, software-factory

Mutagent's CEO and CTO argue agents should be built and improved in an agentic loop: an offline eval-and-optimize loop plus an online trace-diagnose loop, with a demo of their research-preview evaluator and diagnose agents.

- Techniques: Spec-first agent definition; Eval-driven development as TDD for agents; Binary criteria with calibrated LLM judges; Trajectory-level evaluation; Failure-mode library with code-checkable indicators; Tiered trace sampling; Auto-research style optimization gated by evals; Orchestrator dispatching evaluator and diagnose subagents from a coding harness; Diagnostic report with assumptions block and human decisions
- Tools: Claude Code, Codex, Deep Agents (mentioned as a framework), Hermes (mentioned as a framework), Whisper Flow (speech-to-text for feedback), Tracing platform (auto-caption reads 'length use'; name unclear)

## [How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](../videos/1IdzkRVmWAA.md)
`1IdzkRVmWAA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: rag-retrieval, training-finetuning-rl, evals

Mixedbread's team on why agents write keyword-soup queries that hurt retrieval, and how a bounded four-tool search harness, trained with SFT then RL, recovers much of the oracle gap.

- Techniques: Tiered search tool set for agents; Bounded parallel search rounds with dedupe; Priming with a corpus preview; Describe-the-need query framing; Oracle-gap diagnosis; SFT then on-policy RL with a mixed reward
- Tools: Mixedbread search, Codex, GPT-5, Gemini 3.5 Flash, grep, BM25

## [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](../videos/OqM67QG_Ikk.md)
`OqM67QG_Ikk` · AI Engineer · 2026-07-18 · q4 · deep · talk · also: sandboxing-execution, security-guardrails, infra-cost-scaling

A first-principles tour of why agent code needs sandboxes, comparing fork/exec, containers, gVisor and microVMs, then how to add disk snapshots, restore and multi-node scheduling for OpenAI-scale agent sandboxes.

- Techniques: Isolation ladder for untrusted tool execution; Driving a microVM through its VMM API; Per-device jailing for emulated devices; Incremental block-level disk snapshot; Acknowledge snapshot before upload completes; Tiered always-on block storage; Snapshot-aware scheduling; Startup latency hybrid
- Tools: gVisor, Firecracker, Cloud Hypervisor, CrossVM, QEMU, KVM, virtio, vsock, seccomp, VFIO, NBD, FIEMAP

## [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](../videos/OXMMN-XbxwA.md)
`OXMMN-XbxwA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: enterprise-adoption, pr-code-review, context-engineering

Higharc's labs team on moving ML research prototypes into production via three levers: a design-doc-style "research prototype taxonomy," a decoupled Python microservice monorepo, and stacked-PR decomposition for review.

- Techniques: Research prototype taxonomy (RPT) doc; One researcher, one decoupled microservice in a shared monorepo; Slice by dependency graph, then stack PRs; Use the design doc to plan the merge; Notebooks on Modal for GPU experiments
- Tools: Notion, Graphite, GitHub Actions, Modal, Docker, FastAPI, Poetry, uv, Jupyter

## [Your Agents Need a Save Button - Hamza Tahir, ZenML](../videos/bZISsg7H7DA.md)
`bZISsg7H7DA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: observability, evals

Hamza Tahir (ZenML) argues agents need checkpointed runtime state so production runs can be replayed with what-if changes (model swap, mocked tool), compared across cohorts, and shipped only after cohort-level diffs.

- Techniques: Per-step checkpointing of agent state; Counterfactual replay from a checkpoint; Side-by-side run diffing; Cohort replay with agent-driven analysis; Replay-based ship gate
- Tools: Kitaru, OpenTelemetry, GPT-5 Nano

## [Everything we knew about software has changed — Theo Browne, @t3dotgg ​](../videos/xUnRQ9vLXxo.md)
`xUnRQ9vLXxo` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: product-ux, coding-agents, multi-agent

Theo Browne argues that models have moved coding into an orchestration era, so tools, product tiers and software defaults should be rethought, with a markdown file running on cron as his example.

- Techniques: Markdown as a recurring program; Prompt-driven sub-agent orchestration; Breadth-first product with extension points; Assumption audit
- Tools: Claude Code, Codex, Git, GitHub, S3, Cron, Vercel, Slack bot APIs, Reddit, OBS, tmux, GNU Screen

## [Recursive Coding Agents - Raymond Weitekamp, OpenProse](../videos/3hXJI2q0Jz8.md)
`3hXJI2q0Jz8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, multi-agent

Raymond Weitekamp (OpenProse) on applying recursive language model (RLM) ideas to coding agents, with Claude Code dynamic workflows, the Pi extension, and OpenProse markdown workflows as ways to build them.

- Techniques: RLM as a tool call for a coding agent; Recursive agent via a pure Pi extension; Map-reduce versus deep-research workflows in Claude Code; Declarative workflow with parent verification; Adversarial or skeptical subagent roles; Golden session distillation; Small local model as RLM root
- Tools: Claude Code, Codex SDK, Pi, OpenProse, DSPy (dspy.rlm), RLM package (Alex Zhang), Agentica (Symbolica), Axe, Unix RLM (bash), LambdaRLM, Qwen 3.5 9B

## ["I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox](../videos/-CnA2lGfymY.md)
`-CnA2lGfymY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: security-guardrails, testing-verification

Erik Meijer shows how to make agent tool calls provably safe by turning the plan into a program that can be type-checked, taint-analysed and proven before anything runs.

- Techniques: Plan as data, execute after check; Taint or data-flow analysis over the plan; Proof-carrying generation; Effects as data (free monad style)
- Tools: Lean, Dafny, Isabelle, PVS, TLA+, Claude Code

## [The Pipeline Is Dead - Iris ten Teije, Sky Valley Ambient Computing](../videos/bRnoEpoK5m4.md)
`bRnoEpoK5m4` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: product-ux, observability

Argues the one-version-for-everyone software pipeline ends as code gets cheap; proposes a canonical stem with per-user, bounded, reversible divergences and names the hard problems: provenance, testing, measurement, trust, coordination.

- Techniques: Stem plus bounded, reversible divergences; Developer-declared adaptation boundaries; Behavior-driven personalization with a spirit-of-the-software check; Traceable adaptation provenance; Goal-metric gating for changes; Recommend-first autonomy as a trust ladder; Coordination by intent and outcome

## [Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra](../videos/EUsPvBeIx70.md)
`EUsPvBeIx70` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: rag-retrieval, data-engineering, context-engineering

Phaidra engineers explain "semantic blindness": why RAG and LLM-only lookups fail on 400K+ equipment names, and how a hierarchy-based planner plus deterministic set-resolver stays accurate with flat cost at data-center scale.

- Techniques: Hierarchy summary as LLM context; LLM emits a structured search plan; deterministic resolver executes it; Pre-indexed subtrees for set operations; Two- or three-step planner/resolver pipeline in place of an agent loop; Pattern-based search for vague queries; Head-to-head eval against the old system at increasing scale; Move deterministic work out of the prompt

## [Building an ACP-Compatible Agent Live — Bennet Fenner, Zed](../videos/HsxQICTLF84.md)
`HsxQICTLF84` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: coding-agents, mcp-and-tools

Live demo of turning a minimal TypeScript coding agent into an ACP-compatible agent for Zed: four required methods, streamed text, tool-call updates, client-proxied file access, and a diff content type.

- Techniques: Minimal agent loop as the ACP core; Session-scoped agent instances; Streaming through session-update notifications; Two-phase tool-call reporting; Client-proxied file system; Diff content type for edits; Using the protocol's debug view to inspect traffic
- Tools: Zed, Agent Client Protocol (ACP), ACP TypeScript SDK, Anthropic SDK, Node.js, stdio

## [RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](../videos/8oyalrfwgjw.md)
`8oyalrfwgjw` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, coding-agents

Shashi (Superagentic AI) explains Recursive Language Models (RLM) for large codebases: keep the repo in a REPL, let the model write code to slice it, and call sub-models in a loop. He demos his open-source RLM Code harness with Gemini.

- Techniques: REPL-based context slicing (RLM loop); Recursive sub-calls with a budget; Full trajectory capture as JSONL; Sandboxed REPL execution; Model-agnostic sub-calls
- Tools: RLM Code, DSPy, Gemini, Docker, Codex, Pydantic AI, Google ADK, JSONL trace export

## [A Genius With Amnesia - Victor Savkin, Nx](../videos/jVjt-2g8NMY.md)
`jVjt-2g8NMY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, memory

Victor Savkin (Nx) argues coding agents are limited by seeing one repo and forgetting past sessions, and shows Polygraph, a meta-harness that builds a cross-repo dependency graph and replays captured sessions on other machines.

- Techniques: Out-of-band cross-repo dependency graph; Multi-repo session as one unit of work; Session state replay for handoff; Intent-based scope selection; Agent-agnostic meta-harness
- Tools: Polygraph, Nx, Claude Code, Codex, GitHub

## [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](../videos/APh1Vx0oLmQ.md)
`APh1Vx0oLmQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: security-guardrails, observability, infra-cost-scaling

Nishant Gupta (Meta Superintelligence Labs) argues that agent reliability is an infrastructure problem: treat models as probabilistic, keep the platform deterministic, and let infrastructure validate and enforce what the model proposes.

- Techniques: Propose, validate, enforce split; Tool isolation with circuit breakers; Controlled recovery instead of open retries; Decision-chain tracing; Per-agent limits and cost quotas; Layered defence for agent actions; Humans as exception handlers

## [What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip](../videos/7P0elyLIxXo.md)
`7P0elyLIxXo` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, multi-agent

Dotta (Paperclip) argues "done" is a bundle of claims, not a checkbox, and shows how a control plane with blockers, reviewers, and watchdogs keeps agent work moving while still verifying it.

- Techniques: Done as a structured object; Cross-model verifier; Evidence-first completion; Watchdog agent for goal persistence; Explicit state transitions with enforced blockers; Per-task reviewer and approver assignment with audit trail
- Tools: Paperclip, Pi, OpenClaw, Hermes, Claude Code, Codex

## [Use This To Make The Hermes Agent Basically Free](../videos/5d02TYoOzfE.md)
`5d02TYoOzfE` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: token-cost-efficiency, context-engineering, coding-agents

Hermes Agent cost-reduction tutorial from AI LABS: where the tokens go, and which model, context, tool, and hard-limit settings cut the bill without hurting output.

- Techniques: Audit token spend before tuning; Route auxiliary and sub-agent work to a cheaper model; Use the OpenRouter Pareto router; Match effort level to task, and turn thinking off for simple work; Compress context early with a lower threshold and target ratio; Cap tool output in context; Use ephemeral system prompts for one-session instructions; Keep knowledge in files the agent loads on demand; Undo the last message and re-prompt with the failure described; Trim tools, skills, and MCP servers to what is used; Set hard limits on output, turns, and loops
- Tools: Hermes Agent, OpenRouter, Pareto router (OpenRouter), OpenAI Codex subscription, OpenAI subscription, Claude Code, Anthropic API, Gemini, MCP servers, Slack, Luma (sponsor), config.yaml

## [Midjourney full body scanner, VibeThinker, Qwen-Robots, Happy Oyster & More | AI News](../videos/aGseXhwqiLg.md)
`aGseXhwqiLg` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, voice-multimodal

Weekly AI news roundup (2026-07-02): a 3B reasoning model with contested benchmarks, Midjourney's ultrasonic full-body scanner, Qwen robot models, world models, TTS, a multi-agent deep research system, and a camera-control model.

- Techniques: Orchestrator, parallel sub-agents, and a global verifier; Progressive training for interactive world models; World memory via retrieval of prior generations; Camera grid as a control signal; Two decoders for trajectory prediction; Unified state-action space for cross-embodiment control; Inline control tokens in TTS input
- Tools: VibeThinker (Weibo AI, 3B reasoning model, MIT license), Midjourney Medical (ultrasonic CT body scanner, unreleased), Qwen Robot Nav, Qwen Robot Manip, Qwen Robot World (Alibaba; Nav built on Qwen3-VL), DreamX World (5B interactive world model), Higgs Audio V3 (Boson AI TTS, research license), Molmo Motion and PointMotionBench (Allen AI), Apodex One (deep research agent, up to 150 sub-agents), Happy Oyster (Alibaba hosted world engine; formerly Happy Horse 1.0), OmniDirector (Kling team camera-control model), Hugging Face (weights), GitHub (code), arXiv (papers)

## [19 Hidden Features To Unlock The True Potential Of Your Hermes Agent Setup](../videos/nN6DZi_fiSo.md)
`nN6DZi_fiSo` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: context-engineering, token-cost-efficiency, multi-agent

AI LABS walks through about 19 Hermes agent config settings (context limits, compression, sub-agents, auxiliary models, quick commands, checkpoints, YOLO, isolation mode) that they changed to fix workflow problems, with defaults and new values.

- Techniques: Per-profile config tuning; Compression threshold and tail tuning; Sub-agent concurrency, depth and permission settings; Cheap auxiliary models and effort control; Exec and alias quick commands; File checkpoints and rollback; Ephemeral system-prompt variable; Isolation mode for config debugging
- Tools: Hermes (agent, config.yaml, Hermes config / auth / personality / rollback commands), Claude Code (compared; dangerously-skip-permissions mode compared to YOLO), Codex (compared; compression threshold comparison), OpenRouter (provider; default auxiliary model fallback), Gemini Flash (auxiliary model used in their setup), Opus (main model example), Gemini (1M-token window model mentioned), Slack (used to coordinate the team via Hermes), Notion, Jira, Airtable (integrations named in the sponsor segment), Helix (sponsor, not evaluated)

## [Finally, a Programmable AI Agent Framework That Works](../videos/n5cYS6KuyK8.md)
`n5cYS6KuyK8` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: sandboxing-execution, skills-self-improvement, token-cost-efficiency

Walkthrough of Flue, an open-source TypeScript agent-harness framework from the Astro team, showing agents, workflows, HTTP triggers and an in-memory sandbox tier that avoids booting containers.

- Techniques: Single-file agent definition; Skill-backed workflow; Local execution for skills that need files; Safer custom tool instead of local mode; HTTP-triggered workflows; Tiered sandboxes
- Tools: Flue (Flue runtime, Flue CLI, flue.config.ts, server.mjs), Pi (minimal agent harness), OpenClaw (mentioned as built on Pi), Astro, Bun, Vite, Hono, Node.js, Cloudflare Workers and Durable Objects, Cloudflare sandboxes, Vercel Just Bash, Daytona

## [TEN Framework: Voice AI That Can Actually Be Interrupted](../videos/ES3HhoYCtIc.md)
`ES3HhoYCtIc` · Better Stack · 2026-07-02 · q3 · intro · review · also: voice-multimodal

Better Stack hands-on test of TEN Framework, an open-source runtime for real-time voice agents built as graphs of extensions, focused on whether interruptions (barge-in) work.

- Techniques: Graph-of-extensions voice agent; Barge-in test for voice agents; Local TEN bring-up with Docker Compose; Graph-based debugging in TEN Manager
- Tools: TEN Framework (open-source real-time voice agent runtime, version not stated), TEN Manager (visual graph designer), Agora (real-time audio / RTC), Deepgram (speech recognition and TTS preset), OpenAI (LLM in the demo), ElevenLabs (TTS), XAI (alternative preset), Docker Compose, LiveKit Agents (alternative, named by presenter), Pipecat (alternative, named by presenter), Python, C++, Go, Rust, TypeScript (extension languages), SIP telephony, ESP32 hardware, speaker diarization (example configs named)

## [Loop Engineering Totally 10x Hermes agents](../videos/AQRDjI5owZI.md)
`AQRDjI5owZI` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: claude-code, multi-agent, skills-self-improvement

Explains "loop engineering": replacing hand-written prompts with self-driving agent loops, split into deterministic loops (tests as the goal) and non-deterministic loops (UI judged by a skill plus a second verifier model), run on the Hermes agent and Claude Code.

- Techniques: Five-step loop; Deterministic loop with tests as the goal; Adversarial builder/verifier loop for judgment tasks; Explicit verification gates and termination; External state files
- Tools: Hermes agent (always-on agent, self-evolving skills), Claude Code (non-interactive and interactive modes), Claude Code hooks, Ralph loop, Claude goal command, Goal Buddy 2, OpenClaw, GitHub CLI (gh), GPT models (named as verifier, no version given), Claude Opus 4.5 (mentioned), Fable 5 (mentioned, no detail)

## [6 Insane Hermes Agent Use Cases That You Need Right Now](../videos/qMEm1bgxnUM.md)
`qMEm1bgxnUM` · AI LABS · 2026-07-02 · q2 · intro · review · also: token-cost-efficiency, skills-self-improvement, memory

Walkthrough of six Hermes Agent use cases: cron jobs gated by a wake flag or a no-agent flag, a Slack team second brain, Gmail lead webhooks, PRD-as-skill competitor tracking, and human-reviewed social posting.

- Techniques: Pre-LLM gating with a wake-agent flag; No-agent cron jobs for deterministic checks; Ask the agent to build the automation from a prompt; Draft-then-publish content skill with human review; PRD as a skill plus scheduled research; Gmail lead-triage webhook; Profiles for isolated personas
- Tools: Hermes Agent (desktop app and TUI), OpenClaw, Claude Code (transcribed as "clawed code"), cron, Slack, Stripe, Stripe MCP, AWS, Gemini API, Google Play API, Gmail, Google Cloud

## [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](../videos/iUWwcG-C8OU.md)
`iUWwcG-C8OU` · AI Engineer · 2026-06-18 · q4 · practitioner · demo · also: data-engineering, context-engineering, enterprise-adoption

WorkOS product lead Garrett Galow demos Studio, an internal agent that answers business questions and turns repeat questions into live widgets. Main lessons: pre-flight checks, runtime tool context, query validation, and keeping the LLM out of widget refresh.

- Techniques: Generated declarative widgets; Pre-flight checks and clarifying questions; Runtime tool-context injection; Layered prompts; Distrust model priors for product facts; Execute-and-validate before deploy; Org-level connectors with role-based defaults
- Tools: Snowflake, Linear, Notion, Convex, LangGraph, Claude Opus, Slack bot, Retool, WorkOS Pipes

## [Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j](../videos/abvQEhvRI_c.md)
`abvQEhvRI_c` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: memory, context-engineering, rag-retrieval

Neo4j speakers argue agents need context graphs that store policies and rules as well as facts, so they can make and record decisions. They give a decision framework: frame, check global rules, assess risk, propose, then act, defer or escalate.

- Techniques: Propose, then decide, as two agents; Pre-decision risk screen; Decision log as a graph of precedent; Tiered memory in one graph; Framework as a skill or graph workflow
- Tools: Neo4j, Text2Cypher, LangGraph, ADK

## [Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind](../videos/3_gYbhABcAE.md)
`3_gYbhABcAE` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: evals, mcp-and-tools, context-engineering

Philipp Schmid (Google DeepMind) lists five habits from deterministic software that break when building agents: text as state, handing control to the LLM, errors as inputs, pass-rate evals, and agent-ready tools.

- Techniques: Goal-first dispatcher prompting; Free-text approval with edits; Preferences as natural language in context; Errors as observations; Repeated-run pass-rate evals with judges; Agent-ready tool definitions
- Tools: Gemini API, Gemini

## [How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind](../videos/7gujZrJ9L5I.md)
`7gujZrJ9L5I` · AI Engineer · 2026-06-18 · q3 · intro · panel · also: coding-agents, skills-self-improvement, infra-cost-scaling

A Google DeepMind panel on running coding and research agents at Google scale, covering shared workspaces, quota and cost control, skill sprawl, internal observability, and PR review.

- Techniques: Shared file-system workspace between agent stages; Editable plan gate before execution; Scratchpad notes as a reviewable trace; Mock compute for harness testing; Trajectory store plus hierarchical drill-down; Per-language fine-tuned review model plus per-product review prompts; Transparent model fallback under the harness; Skills plus guardrailed CLI over MCP for internal tools
- Tools: Antigravity, Gemini, Gemma 4, Deep Research, Jules, MCP, OpenClaw

## [Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson](../videos/mR-WAvEPRwE.md)
`mR-WAvEPRwE` · AI Engineer · 2026-06-18 · q4 · practitioner · workshop · also: multi-agent, claude-code, testing-verification

Two Anthropic Applied AI engineers explain how long-running agent harnesses evolved, and how a planner, generator and evaluator loop with rubric grading builds multi-hour apps that a single agent loop cannot finish.

- Techniques: Generator-evaluator loop with a live-app evaluator; Rubric-as-taste with calibrated examples; Sprint contracts negotiated in files; Thin planner that stays high level; Structured state on disk with JSON feature lists and progress files; Breadcrumb logs for later pickup; Read full traces, then tune prompts from them; Ralph-style stop-hook loop with exit criteria; Hooks for human check-ins; Split model roles for cost; Put the human-readable spec back into long sessions
- Tools: Claude Code, Claude Agent SDK, Playwright MCP, Chrome MCP, Claude Code skills, Claude Code sub-agents, Claude Code agent teams, Claude Code stop hooks, Claude Code auto mode, git, Puppeteer

## [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](../videos/zMiSRliEzv4.md)
`zMiSRliEzv4` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: software-factory, evals, observability

PostHog's Joshua Snyder describes a pipeline that turns product signals (errors, replays, Slack, experiments) into grouped reports, runs a Claude Agent SDK research agent in sandboxes, and opens PRs that are iterated until green.

- Techniques: Generate queries from a signal, then embed the queries; Safety classifier at the ingestion edge; Weighted report promotion with a threshold; Three-way actionability gate; Snapshot and rehydrate the sandbox for CI and review loops; Distill repeated agent behavior into a one-shot call; Evaluate on production-representative data
- Tools: Claude Agent SDK, Modal, MCP, Linear, Notion, Sentry, git blame, PostHog, feature flags

## [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](../videos/SKDJo2CopRs.md)
`SKDJo2CopRs` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: sandboxing-execution, mcp-and-tools, infra-cost-scaling

Two Cloudflare engineers tour Durable Objects, dynamic workers and code mode as a stateful, sandboxed runtime for agents. Mostly product pitch, with a few reusable architecture ideas.

- Techniques: One Durable Object per entity ID as the session or agent; Resumable stream held by the agent object; Deny-by-default capability sandbox for generated code; Code mode for large API surfaces; Scheduled work inside the agent class; Plugins as isolated dynamic workers
- Tools: Cloudflare Durable Objects, Cloudflare Workers, Cloudflare Dynamic Workers, Cloudflare Agents SDK, Vercel AI SDK, MCP, Cloudflare Sandbox SDK, Daytona, SQLite, R2, Zig (via Wasm), Next.js on Workers

## [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../videos/N7b1PJc7SFc.md)
`N7b1PJc7SFc` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, infra-cost-scaling, evals

Together AI's voice AI lead on the cascading STT→LLM→TTS pipeline: per-stage latency budgets, streaming STT, co-locating models to cut network hops, and why speech-to-speech is not yet production-ready.

- Techniques: Cascading voice pipeline with streamed hand-offs; Per-stage latency budget; Streaming STT with lookahead-limited encoders; Co-locate models with the orchestrator; Asymmetric autoscaling for stateful voice; Pre- and post-LLM guardrail and routing stages; Thinker-talker delegation; Tiered tool-call evals; Full-duplex conversation evals
- Tools: Together AI (hosted inference, the speaker's company), Pipecat (agent orchestrator, named as an example), LiveKit (agent orchestrator, named as an example), Whisper (OpenAI speech-to-text, cited as the batch model), NVIDIA streaming speech encoder (named only as a recent NVIDIA model), NVIDIA VoiceChat (speech-to-speech model), OpenAI realtime API (speech-to-speech), ChatGPT advanced voice mode, Claude Code and Cursor (cited as voice-interaction examples)

## [Bounded Autonomy: Between Free Will and Determinism — Angus J. McLean, Oliver](../videos/t4359sKBu4w.md)
`t4359sKBu4w` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: context-engineering, enterprise-adoption

An ad-agency AI director argues for "bounded autonomy": treat LLM context as a soft constraint, keep systems simple, store knowledge in several representations, and never automate work you cannot do yourself.

- Techniques: Self-imposed context budget; Curated documentation over open web access; Simple-first prototype with fast reality checks; Multi-representation knowledge storage; Cluster-then-report pipeline; Teach yourself on older, smaller models and your own harness; Automate only what you can do yourself

## [Any-to-Any: Building Native Multimodal Agents - Patrick Löber, Google DeepMind](../videos/GIRpQEfYf3U.md)
`GIRpQEfYf3U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, mcp-and-tools

Google DeepMind's Patrick Löber walks through building a NotebookLM-style agent: Gemini reasons, calls native image and speech generators via function calling, and uses multimodal input and a live audio model.

- Techniques: Agentic generation loop with function-declared generators; Single-call multimodal synthesis; Timestamp-windowed media analysis; Context caching for repeated queries; Scaffold with a Gemini API skill; Audio-to-audio live session for voice
- Tools: Google Gen AI SDK, Gemini API, Google AI Studio, Gemini 3 Flash, Gemini 3.5 Flash Image preview (Nano Banana 2), Gemini 2.5 text-to-speech, Gemini 3.1 Flash Live, File API, Gemma 4, Gemini API skill

## [The Missing Primitive for Agent Swarms — Lou Bichard, Ona](../videos/5Sui_OnSRlY.md)
`5Sui_OnSRlY` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: multi-agent, software-factory, sandboxing-execution

Ona's field CTO argues that runtimes, orchestration and triggers are largely solved for coding-agent swarms, and that agent coordination is the missing primitive. He proposes state-machine workflows packaged as a CLI that runs locally and in CI.

- Techniques: Parent-child sub-agents with scoped context; Two-tier sub-agent placement; Fleet fan-out with prompts and scripts as a workflow; Harness engineering loop; Gated micro-step workflow (state machine); CLI-packaged workflow gate
- Tools: Ona dev environments, GitHub, Linear, Symphony, ACP, ACPX, Fabro, n8n-style graph workflows, backgroundagents.com

## [LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](../videos/JsCCrBF7F1g.md)
`JsCCrBF7F1g` · AI Engineer · 2026-06-18 · q2 · practitioner · talk · also: observability, evals

Arize's Dat Ngo argues LLM observability, evals and experiments form one flywheel, built on OpenTelemetry traces, with evals scoped from single spans up to whole sessions. It is mostly a product walkthrough with a useful eval taxonomy.

- Techniques: OTel auto-instrumentation for agents; Session-level state tracking; Distributional trajectory analysis; Eval at the smallest scope that answers the question; Deterministic checks before LLM judges; Calibrate an LLM judge against a golden dataset; Trace-to-dataset-to-experiment loop; Coding-agent access to the eval platform
- Tools: Arize Phoenix, Arize AX, OpenTelemetry, LLM-as-judge, Claude Code, Codex, Anthropic Managed Agents (mentioned)

## [Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl](../videos/W-SX_srBa3Y.md)
`W-SX_srBa3Y` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: coding-agents, multi-agent

Bitly engineer Michael Richman presents Command & Control, his tool for monitoring and answering coding agents from a phone, web or watch, and frames the idle-agent problem as FOMAT.

- Techniques: Per-platform lifecycle daemon feeding a control plane; Tiered notification and watch lists; Overview summaries from the last few messages; Start remotely, resume locally on the same session
- Tools: Command & Control (Cmd+Ctrl, speaker's own tool), Claude Code (captioned as Cloud Code), Codex / Codex CLI, Gemini (CLI), Cursor (IDE), GitHub Copilot, OpenCode, Anthropic remote control and teleportation (Claude Code features, mentioned), Bitly MCP server (co-written by speaker, mentioned), Agent Craft (gaming-based agent tool, mentioned as seen earlier that morning)

## [Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline](../videos/yUmS-F9IX90.md)
`yUmS-F9IX90` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: coding-agents, context-engineering, software-factory

Ara Khan (Cline) argues for four maturity levels of agent building: framework, hand-built state machine, Kanban as the UX, and cloud execution. Core warnings: keep prompts minimal, keep agents CLI-testable, and keep architecture human-owned.

- Techniques: Agent as explicit state machine; Prune the system prompt on every change; CLI-first agent interface for agent-driven development; Exact reasoning-trace round-tripping; Kanban board as the multi-agent control surface; Per-task cloud agent dispatch; Human-owned architecture before code generation
- Tools: Claude Code, Codex, Cursor, Factory, Cline, LangChain, LangGraph, OpenRouter, Linear, AGENTS.md, VS Code

## [How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS](../videos/vy7o1g2iHY8.md)
`vy7o1g2iHY8` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: skills-self-improvement, testing-verification, evals

WorkOS DX engineer on replacing 10k lines of generated agent skills with 553 lines of gotchas, enforcing gates in a state machine, and making agents prove their work with hashes and videos.

- Techniques: Enforced state-machine gates for agent pipelines; Hash-verified test receipts; Gotchas-only skills validated by paired evals; Visual before-and-after proof on PRs; Retrospective agent over run transcripts; Conditional rules instead of doc summaries
- Tools: Pi, Claude Code, Codex, Playwright CLI, TypeScript, SHA-256, WorkOS CLI, AuthKit, TanStack Start, Next.js, GitHub, Linear

## [Stop Using Claude Code CLI. Use THIS Instead! (Oh-My-Pi)](../videos/8ukl-0tlVgM.md)
`8ukl-0tlVgM` · Better Stack · 2026-06-02 · q2 · intro · review · also: coding-agents, token-cost-efficiency, dev-tools

A 5-minute Better Stack walkthrough of Oh My Pi, an open-source terminal agent harness built on the Pi framework, covering LSP refactoring, debugger attach, per-task models, hashline edits, and Pi package support.

- Techniques: Hashline edits (anchor-based line editing); LSP-backed workspace refactor; Per-task model routing in a harness; Debugger attach for agent debugging
- Tools: Oh My Pi (open-source terminal agent harness), Pi framework (base for Oh My Pi; source of the Doom package), Claude Code CLI (compared against; plugins and settings are imported on login), Claude Opus (named as the model that reproduces full edit text in Claude Code), Grok 4 Fast (model used for the 61% token-savings claim), DLV (Go debugger), DebugPy (Python debugger), Chrome (launched by the built-in browser tool), Hindsight (agent memory management, mentioned only), Rust (language of the demo app)

## [Harness Engineering: The Missing Layer for AI Coding Agents (Archon)](../videos/-1BOhPOcEb8.md)
`-1BOhPOcEb8` · Better Stack · 2026-06-02 · q2 · intro · review · also: coding-agents, software-factory

Better Stack demos Archon, an open-source harness that defines coding-agent work as YAML workflows with fixed and AI steps, runs each job in its own git worktree, and auto-loads skills, aiming for repeatable, conflict-free parallel runs.

- Techniques: Process-as-YAML DAG with mixed step types; Per-run git worktree isolation; Skills as on-demand context; Local setup flow shown in the video (no exact commands on screen)
- Tools: Archon, ArchonServe (Archon local UI), Claude Code, Cursor, Codex, LangChain, Agent Skills, git worktree, YAML

## [Why OpenAI Built Symphony and Gave It Away for Free](../videos/n8qDKMPpLXc.md)
`n8qDKMPpLXc` · Better Stack · 2026-06-02 · q3 · intro · review · also: multi-agent, coding-agents, software-factory

Better Stack walkthrough of OpenAI's open-source Symphony, which polls Linear for issues and runs a coding agent per issue, with humans involved only at review. Covers setup, workflow file and hooks.

- Techniques: Tracker-driven agent dispatch; Workflow file with YAML front matter plus a per-issue prompt; Clone-and-branch after-create hook, commit-push-PR after-run hook; Spec-driven self-implementation
- Tools: Symphony (OpenAI, open-source orchestrator), Linear (issue tracker), Codex CLI (OpenAI coding agent), GPT-5.5 (model, used at low effort for spec-generated build), Elixir (language for the manual install route), TypeScript and Bun (demo app), Python (spec-generated Symphony version), Go with Charm CLI (community Symphony version), Claude SDK (community Symphony version), uv (Python tool; speaker says OpenAI acquired it, not verified in video), Multica (agent orchestration product, compared), Conductor (agent orchestration product, compared)

## [ADLC: Claude Code's New Lifecycle for AI Coding](../videos/aMBQB_IJ0dQ.md)
`aMBQB_IJ0dQ` · AI LABS · 2026-06-02 · q2 · intro · other · also: evals, claude-code, context-engineering

Conceptual walkthrough of the agentic development lifecycle (ADLC), a phase-by-phase SDLC analogue for non-deterministic agents with a validation gate and staged rollout. Thin on code and data, with a sponsor segment.

- Techniques: Behavior-first planning mode; Human-agent responsibility model; Ground-truth dataset plus baselines as a validation gate; Single orchestration layer for multiple agents; Context hygiene against context rot; Staged rollout with behavioral alerting; Feedback signals and periodic data refresh
- Tools: Claude Code (planning mode, agent view), Cursor, Google Calendar MCP, Gmail MCP, Notion MCP, RAGAS, DeepEval, Gemini (1M-token context, mentioned), Claude Opus (1M-token context, mentioned), ChatGPT (feedback UI example, mentioned), Softr (sponsor, transcribed as 'Softer')

## [I Tried Running a Company Made of AI Agents](../videos/xZ7OmRz2i7o.md)
`xZ7OmRz2i7o` · Better Stack · 2026-06-02 · q3 · intro · review · also: multi-agent, token-cost-efficiency

Walkthrough of Paperclip, a self-hosted control plane that runs several AI agents as a company with an org chart, tickets, heartbeats, budgets and audit logs; useful for multi-agent coordination, overkill for single-agent tasks.

- Techniques: Goal-first company setup; Budget-before-execution guardrail; Heartbeat wake cycles; Ticket ancestry for traceability; Skill files as company rules; Local install and launch
- Tools: Paperclip, npx (Node package runner), Postgres (bundled with Paperclip), CrewAI, AutoGen, LangGraph (rendered as 'Landgraf' in captions), Claude Code, Cursor, GitHub (issues), Jira, Linear

## [The Greatest AI Coding System I've Ever Used, Forget Codex Vs Claude Code](../videos/q7Am0pV6FjQ.md)
`q7Am0pV6FjQ` · AI LABS · 2026-06-02 · q3 · practitioner · review · also: claude-code, multi-agent, context-engineering

Goal Buddy, an open-source plugin for Claude Code and Codex, wraps the native goal command with file-based state, an upfront "oracle" for done, and Scout/Worker/Judge agent roles.

- Techniques: Oracle-first done criteria; Role-separated agents with access limits; File-based run state instead of chat history; Slice contracts; Clarify before looping; Install and start a run
- Tools: Goal Buddy, Claude Code (goal command, resume command), Codex, Ralph Wiggum plugin, Haiku (native goal evaluator)

## [The End of Apps — Kitze, Sizzy.co](../videos/4fntwuOoedA.md)
`4fntwuOoedA` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: product-ux, multi-agent, memory

Kitze (Sizzy.co) on his personal-agent journey, from to-do apps to OpenClaw-style agents, and his view that apps will give way to a personal agent OS that prompts the user.

- Techniques: Nested topic description injection; Per-topic specialized agents; Labeled cron messages with full conversation context; Visible tool-call UI
- Tools: OpenClaw, Hermes, Paperclip, Codex, Claude Code, Claude Cowork, Tmux, Telegram, Discord, Tasker, IFTTT, Notion

## [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](../videos/Wmp2Tku2PrI.md)
`Wmp2Tku2PrI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, coding-agents, testing-verification

Michael Arnaldi builds a TypeScript Effect HTTP to-do API from an empty repo, arguing agents need the real source repo, strict lint back pressure, and generated pattern docs.

- Techniques: Clone the library source into the repo; Strict diagnostics plus lint as back pressure; AGENTS.md as a living rulebook; Spec file plus Ralph-style loop; Self-selected pattern docs; Single execute tool instead of many tools; Per-test rollback transactions for DB tests; Test layers with it.layer; Lint reference checks in CI for pattern docs
- Tools: Effect v4 (beta), Effect SQL with SQLite, Bun, Vitest, TypeScript native preview (tsgo), ESLint, OpenCode, GPT-5.4, Claude Opus, Codex, Cursor, Temporal

## [Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw](../videos/4VhbYlfC7Gs.md)
`4VhbYlfC7Gs` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: evals, observability

Vincent Koc (Comet, OpenClaw) argues static, hand-written evals don't fit adaptive agents; he proposes intent-based, always-on evals self-curated from traces, with the eval suite treated as living code.

- Techniques: Intent-defined end-state evals; Trace-driven suite self-curation; Always-on eval service; Telemetry-aware harness; Split static and dynamic evals
- Tools: Comet, OpenClaw, Claude, Codex, MCP, Karpathy autoresearch

## [Human-in-the-Loop Automation with n8n — Liam McGarrigle](../videos/tDArkCqjA-c.md)
`tDArkCqjA-c` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: security-guardrails, mcp-and-tools, context-engineering

Workshop on building a Gmail and Google Calendar agent in n8n, then gating sensitive tool calls behind human approval steps that the model cannot skip.

- Techniques: Approval gate in front of sensitive tools; Free-text decline as feedback; Dry runs with dummy data before real accounts; Rules in tool descriptions, not one system prompt; Per-field descriptions for argument mistakes; Wait with an auto-deny timeout; Confirm sub-workflow as a tool; Sub-agent per domain as a tool; Date and time injection via expression; Memory window sizing
- Tools: n8n, OpenRouter, Gmail, Google Calendar, Slack, Notion, Postgres, Redis, Claude, Claude Code, Luxon, Swagger

## [Shipping complex AI applications — Braintrust & Trainline](../videos/ZdheJTfLu-s.md)
`ZdheJTfLu-s` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: evals, observability

Hands-on Braintrust and Trainline workshop on taking a multi-stage LLM support-triage agent from one prompt to a traced, evaluated, managed and failure-driven production loop.

- Techniques: Staged agent pipeline with a deterministic front end; Nested tracing per user interaction; Golden set from categorized edge cases; Two-tier scoring; Evaluate before swapping models; Failure-to-fix loop; Prompts and scorers as managed, slugged assets
- Tools: Braintrust, OpenAI SDK, OpenAI mini model (speaker says 'mini'), TypeScript, pnpm, make, Node 22, Cursor / Codex (suggested for setup)

## [Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop](../videos/-aM2EDTiaMs.md)
`-aM2EDTiaMs` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: observability, evals, coding-agents

Raindrop's founders argue production agent monitoring must replace evals as the main safety net, using implicit classifier signals, regex, ship-vs-control experiments, and agent self-diagnostic reports.

- Techniques: Binary issue classifiers as monitoring signals; Regex keyword signals on user messages; Percentage rollout with a control group, judged by signal rates; Self-diagnostic report tool; Natural-language signal definition (deep search); Daily triage agent over signals; Cluster by user intent and track issue rate per cluster; Trajectory search over tool-call sequences
- Tools: Raindrop, OpenTelemetry, Claude Code, Codex, OpenAI API, Sentry, Slack, BigQuery, Snowflake, Statsig

## [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](../videos/ow1we5PzK-o.md)
`ow1we5PzK-o` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: multi-agent, software-factory, testing-verification

Luke Alvoeiro (Factory) on "Missions", a multi-agent system that runs for hours or days by combining delegation, creator/verifier, broadcast and negotiation, with a validation contract written before any code.

- Techniques: Validation contract written at planning time; Fresh-context adversarial validators; Structured worker handoffs; Serial features with read-only parallelism; Per-role model choice; Milestone-based negotiation; Orchestration as prompts and skills
- Tools: Factory Droid (open source Goose lineage mentioned), AGENTS.md, skills, computer use (for user-testing validator), prompt caching

## [I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)](../videos/sJ2jc7leKBk.md)
`sJ2jc7leKBk` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: memory, context-engineering

An OpenClaw maintainer shows how he grew a personal agent into a life-running system step by step, using an Obsidian knowledge base, scheduled maintenance and channel-per-job routing, plus its failure modes.

- Techniques: Incremental capability ladder; Channel-per-job-type routing; Link-capture enrichment into a markdown vault; Verified overnight maintenance; Deterministic scripts beside LLM judgment; Critical-rules block high in the instruction file; Draft-don't-send attention filtering; Routine memory hygiene
- Tools: OpenClaw, Obsidian, QMD, Discord, Telegram, WhatsApp

## [Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick](../videos/2TLXsxkz0zI.md)
`2TLXsxkz0zI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: software-factory, coding-agents, context-engineering

Chris Parsons runs a live workshop on Ralph loops: re-running Claude Code on fresh context until work ships, fed by ticket files, a sequential queue, and reversibility limits on unattended agents.

- Techniques: Bash while-loop over fresh Claude sessions; Next-most-important-ticket selection over flat markdown tickets; Recovery check for mid-flight work; Reversibility gate with stop-and-report; Fresh-subagent adversarial review; Claude /loop for timed repetition; Resume a project in an interactive session; Simulated audience personas run in parallel subagents; Nightly session digest
- Tools: Claude Code, Codex, Cursor, n8n, Docker Sandbox, Playwright, Obsidian, Lian (embeddings CLI), Beads, Linear, Jira, Telegram

## [The Future of MCP — David Soria Parra, Anthropic](../videos/v3Fr2JR47KA.md)
`v3Fr2JR47KA` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: mcp-and-tools, context-engineering

David Soria Parra (Anthropic) on where MCP is heading: MCP apps, progressive tool discovery, code-style tool composition, and the 2026 protocol roadmap.

- Techniques: Progressive tool discovery; Programmatic tool calling / code mode; Use structured output to enable composition; Agent-first tool design; Pick connectivity per task; Skills-over-MCP approximation
- Tools: MCP, MCP Apps, Claude Code, Cloudflare MCP server, V8 isolate, Lua interpreter, FastMCP, Python SDK, TypeScript SDK, OpenAI Agents SDK, Google ADK, LangChain

## [Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate](../videos/vi-2nasppAg.md)
`vi-2nasppAg` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: multi-agent, observability, sandboxing-execution

Iterate's workshop on building event-sourced agent harnesses as stream processors: pure reducers for state, side effects after append, pause-based circuit breakers. Live demos mostly failed; the design ideas are the value.

- Techniques: Event-sourced agent log; Reducer plus after-append split; Pause-event circuit breaker; Deferred enrichment with a time budget; Child paths for sub-agents; Secret substitution at fetch time
- Tools: events.iterate.com (event service), Cloudflare dynamic workers, OpenAI SDK (Responses API), Zod, Pi, Claude, OpenCode, Convex, Kafka, Cursor, OpenClaw, Electric SQL

## [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../videos/8txf05vVVl4.md)
`8txf05vVVl4` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: mcp-and-tools, token-cost-efficiency, sandboxing-execution

Cloudflare's Sunil Pai on "Code Mode": have models write code against an API instead of making many tool calls, cutting a 2,600-endpoint API from ~1.2M tokens to ~1K, inside capability-restricted sandboxes.

- Techniques: Search + execute two-tool facade; Code as the tool-call format; Zero-capability sandbox with explicit grants; Agent-facing developer experience; Operate on the app's raw state
- Tools: Cloudflare Workers, Cloudflare Dynamic Workers, V8 isolates, OpenAPI, PartyKit, Claude Opus, TLDraw-style canvas

## [Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably](../videos/YNJvm7t3yq8.md)
`YNJvm7t3yq8` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: product-ux, multi-agent

Ably's Mike Christensen argues that AI chat UX breaks under direct HTTP/SSE streaming and proposes durable sessions (a shared, resumable channel between agents and clients) to get resilient streams, multi-device sync, and live steering or cancel.

- Techniques: Durable session as a shared channel; Hand-rolled resumable stream (the baseline he contrasts with); Bidirectional transport to separate cancel from disconnect; Multi-agent writes straight to the shared session; Any-client control through the session; Human handoff as another session participant
- Tools: Ably channels, Ably AI Transport, Server-Sent Events (SSE), WebSockets, Redis, Vercel AI SDK, TanStack AI

## [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../videos/XNtkiQJ49Ps.md)
`XNtkiQJ49Ps` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: product-ux, evals, skills-self-improvement

Legora's CTO argues that vertical agents need more than chat: make work verifiable, let humans steer through skills and decision logs, and use persistent artifacts as the collaboration surface.

- Techniques: Proxy verification with golden examples; Task decomposition by verifiability; Allowlist guardrails for agent actions; Skills as judgment encoded at work nodes; Elicit-or-decide with a decision log; Persistent, scoped artifacts as the collaboration surface
- Tools: Claude Code

## [The New Application Layer - Malte Ubl, CTO Vercel](../videos/XKup1pj-34M.md)
`XKup1pj-34M` · AI Engineer · 2026-05-18 · q3 · intro · keynote · also: sandboxing-execution, enterprise-adoption, product-ux

Vercel CTO Malte Ubl argues agents are a new kind of software that makes long-tail automation affordable, names practical agent archetypes, and says harnesses should run apart from the code they generate.

- Techniques: Compress-the-research agent; Information-surfacing agent; Ask-what-you-hate discovery; Harness and code execution split; CLI and API first for agent-facing products; Lightweight bash sandbox for agents
- Tools: Vercel AI SDK, Chat SDK, JustBash, Claude, Codex, Granola, Pi, OpenClaw

## [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](../videos/W76woOYHlvY.md)
`W76woOYHlvY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: software-factory, coding-agents, product-ux

Louis Knight-Webb (Vibe Kanban) argues engineers will mostly plan and review as agents run longer, then live-demos shutting his company down through the tool.

- Techniques: Task-type mode selection; Clarifying-question planning; Parallel agent workspaces; PR comment shepherding
- Tools: Vibe Kanban, Claude Code, Codex, Cursor, GitHub Copilot, Playwright MCP, GitHub, Cloudflare CDN

## [Give Your Agent a Computer — Nico Albanese, Vercel](../videos/wflNENRSUb4.md)
`wflNENRSUb4` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: sandboxing-execution, mcp-and-tools, context-engineering

Nico Albanese (Vercel) live-builds a coding-style agent with AI SDK 6: a tool loop, web search, a persistent named sandbox running bash, file-based memory and self-written scripts, plus notes on context pruning and subagents.

- Techniques: Single-definition tool loop agent; Typed UI messages from the agent definition; Named persistent sandbox per session; Bash-only tool for a coding-style agent; Call options plus runtime context injection; File-backed memory injected into the system prompt; Per-step hook for message slicing; Subagents and handoff instead of compaction; Plan file with objective and checkboxes
- Tools: Vercel AI SDK 6, Vercel AI Gateway, Vercel Sandbox (persistent named sandboxes, beta), Next.js, Zod, OpenAI provider (web search tool), Anthropic provider (bash/computer tools), Vercel Workflow (durable steps), OpenCode, Amp (handoff tool)

## [Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev](../videos/svCnShDvgQg.md)
`svCnShDvgQg` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: sandboxing-execution, infra-cost-scaling

Eric Allam (Trigger.dev) argues that replay-based durable execution breaks for long-running agent loops, and proposes splitting agent durability into an append-only context log plus VM snapshot/restore of the execution state.

- Techniques: Two-layer agent durability; Snapshot on idle, restore on next message; Recovery by failure class; Seekable compression with lazy page restore; Whole-VM snapshot instead of process checkpoint
- Tools: Trigger.dev, Firecracker, CRIU (captioned as "Cree"), Docker, fcrun

## [Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind](../videos/cVzf49yg0D8.md)
`cVzf49yg0D8` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: voice-multimodal, mcp-and-tools, context-engineering

Google DeepMind hands-on workshop on building agents with the Gemini Interactions API (server-side state, background runs, skills) and the Live API (native-audio voice agents), with live demos that partly failed.

- Techniques: Chained interactions via previous ID; Async background runs with polling or webhooks; Skill that links to live docs; Tool loop with recursion; Server-to-server Live proxy; Ephemeral token for direct browser connection; Context window compression for long Live sessions; Voice persona through system instructions; Send a single image and then audio
- Tools: Gemini Interactions API, Gemini Live API, Google AI Studio, Gemini 3 Flash / 3.1 Flash Live, Lyria 3, Nano Banana, Google Search grounding, uv, FastAPI, Context7, skills.sh, Antigravity

## [Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs](../videos/DCZZ3AJKzuc.md)
`DCZZ3AJKzuc` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: voice-multimodal, mcp-and-tools

ElevenLabs' Luke Harries argues chat agents should add voice, and previews VoiceEngine, a wrapper that adds STT, TTS and turn-taking to an existing chat agent without a rebuild.

- Techniques: Voice wrapper around an existing agent; Client-side vs server-side tools for voice; Prompt a coding agent with a conversion skill
- Tools: ElevenLabs VoiceEngine, ElevenLabs Scribe (speech-to-text), ElevenLabs V3 (text-to-speech), ShadCN / Vercel-style UI components

## [Harnesses in AI: A Deep Dive — Tejas Kumar, IBM](../videos/C_GG5g38vLU.md)
`C_GG5g38vLU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: testing-verification, security-guardrails, context-engineering

Tejas Kumar (IBM) walks through building a "poor man's" agent harness live: deterministic guardrails, outcome verification, and credential injection around a weak model, with the prompt left unchanged.

- Techniques: Deterministic pre-turn hook for state and secrets; Outcome verification from the trace; Guardrails as composable functions; Two-level retry around an attempt; Naive head-and-tail context trimming; Tool definitions in the OpenAI SDK shape
- Tools: Playwright, Chromium, OpenAI Agents SDK-style tool definitions, GPT-3.5 Turbo, Claude Code, Cursor, Codex, Qwen, GPT-OSS, OpenRAG

## [Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize](../videos/Xfl50508LZM.md)
`Xfl50508LZM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: evals, observability

A two-hour Arize Phoenix workshop on evaluating a Claude-powered financial research agent: read traces first, then write code evals, LLM judges, meta-evals and experiments.

- Techniques: Root-span code eval; Faithfulness eval using the research step as context; Classification LLM judge with a binary label; Trace-to-dataset failure loop; Wrap multi-turn agent runs in one parent span; Golden set with a held-out split and reference solutions; Pairwise comparison and reliability metrics; Cost-normalized accuracy and tiered models
- Tools: Arize Phoenix (Phoenix Cloud), OpenInference instrumentation, OpenTelemetry (phoenix.otel register, auto_instrument), Claude Agent SDK, Claude Haiku (agent model), Claude Sonnet (judge model), Phoenix evaluators (correctness, faithfulness, classification), Phoenix datasets and experiments, Arize AX (enterprise product, mentioned)

## [A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon](../videos/vAIDdLKB6-w.md)
`vAIDdLKB6-w` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: coding-agents, enterprise-adoption

Matthias Luebken (Taven AI) shows how the open-source Pi coding agent, the core under OpenClaw, can be embedded in a product: an agent is a tool-calling loop, and a sales-RFP email agent is built on per-customer sessions and CLI tools.

- Techniques: Agent as tool loop with event and hook surface; Extension commands with UI selection; Per-customer agent with harness and customer files; Backend access as CLIs for the agent; Small single-purpose tools packaged as a skill; Draft-first human-in-the-loop output
- Tools: Pi, OpenClaw, Claude Cowork, FFmpeg, pandas, openpyxl, LibreOffice, AGENTS.md, NVIDIA OpenShell, TypeScript

## [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../videos/mYSRn6PC1mc.md)
`mYSRn6PC1mc` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: evals, mcp-and-tools, context-engineering

Workshop on building a deep-research agent (MCP server plus Claude Code skills) that feeds a separate LinkedIn writer workflow with evaluator-optimizer review and a calibrated LLM-judge eval loop.

- Techniques: Autonomy-ladder architecture choice; Tools as specialists inside one agent; Delegation to keep context lean; Files as the inter-agent contract; Guideline plus static style profiles; Start with many few-shot examples, then trim; Evaluator-optimizer with fresh context and typed feedback; Synthetic eval inputs, real outputs, binary labels with critiques; Judge calibration with dev/test F1; MCP server exposes tools, prompts and resources; skills wrap prompts for progressive disclosure; Trace-based debugging with threads and traces
- Tools: Claude Code, FastMCP, MCP, Gemini API (grounding, multimodal YouTube), Firecrawl, Perplexity, Opik, Pydantic, git-ingest, uv, Python

## [Claude Routines: The Hidden Costs Nobody Talks About](../videos/yVnsU-xqng4.md)
`yVnsU-xqng4` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: claude-code, token-cost-efficiency

Walkthrough of Claude Routines (cloud-run scheduled, GitHub-event and API-triggered Claude Code tasks), covering setup gotchas, daily run caps and why the presenter finds them too expensive for most automation.

- Techniques: Schedule a remote routine from the CLI; Write prompts for unattended runs; Work around the Bash network block with a custom environment; Ship skills and hooks to the cloud instance through a repo; Trigger PR reviews from GitHub events; Compare routine cost with a self-hosted webhook agent
- Tools: Claude Code, Claude Routines, Claude desktop app, /schedule slash command, Bash, WebFetch, curl, GitHub, GitHub MCP server, Slack, n8n, Hermes Agent

## [This Is The Anthropic Team's Greatest Advice](../videos/O1XLCh-uA_E.md)
`O1XLCh-uA_E` · AI LABS · 2026-05-02 · q2 · practitioner · tutorial · also: claude-code, context-engineering, multi-agent

Practical habits for managing Claude Code's context window (compaction, clear, rewind, sub-agents, recaps) to limit context rot and goal drift in long runs; mostly attributed advice with a sponsored segment.

- Techniques: Manual compaction with an explicit instruction; Clear on task switch; Structured state handoff (save, clear, reload); Periodic recap to reinforce goals; Sub-agent isolation for raw-heavy subtasks; Rewind, then re-prompt
- Tools: Claude Code, Claude (Opus 4.5 and later models, 1M context window), CLAUDE.md, Verdant (sponsor)

## [Multica: The Open Source Tool That Makes Claude Code 10x Better](../videos/WdGSXQPwwmo.md)
`WdGSXQPwwmo` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: coding-agents, multi-agent

Better Stack walks through self-hosting Multica on a VPS to turn Claude Code and OpenCode into assignable, scheduled agents, then judges it technical to set up and less suited to dialogue-style work than managed alternatives.

- Techniques: Self-host Multica with Docker on a VPS; Log in without the emailed code; Connect a machine as an agent runtime; Define an agent; Issue-driven task flow; Scheduled autopilot (recurring agent run)
- Tools: Multica, Claude Code, OpenCode, OpenCode Zen (big pickle model, as named in the video), Codex CLI, Hermes, Claude Routines, Claude Managed Agents, Docker, Go, Next.js, TypeScript

## [GitHub Was NOT Made for AI Agents (So Cloudflare Built Their Own)](../videos/PWj6GnTUBnk.md)
`PWj6GnTUBnk` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: software-factory, sandboxing-execution, dev-tools

Walkthrough of Cloudflare Artifacts, a Git-compatible repo store on Durable Objects built for agents, with a fork-per-task demo the speaker could not run because the product is in private beta.

- Techniques: Fork-per-task repo workspaces; Git-backed agent tools: read, write, commit (commit also pushes); Durable Object SQLite as the persistence layer for agent repos; Verification loop idea: run the agent's changed code in a sandbox, and check front-end work in a browser; Reconstructing a diff without git diff
- Tools: Cloudflare Artifacts (private beta), Cloudflare Workers, Cloudflare Durable Objects, Cloudflare Dynamic Workers, Cloudflare Sandboxes, Cloudflare Browser (Puppeteer), Wrangler (wrangler.jsonc / wrangler.toml bindings), isomorphic-git, Zig (compiled to WASM), Anthropic SDK, Git protocol, S3 Files

## [Anthropic's Managed Agents Are Different (Here's Why)](../videos/uxHolzq1NcA.md)
`uxHolzq1NcA` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: claude-code, security-guardrails, mcp-and-tools

Better Stack walks through Anthropic's Claude Managed Agents: building a Slack-connected agent with no hand-written orchestration code, its per-session-hour pricing, and the session/harness/orchestrator architecture with runtime credential vaulting.

- Techniques: Scaffold a managed agent via the Claude Code skill; Read-only toolset for a retrieval agent; Run setup once, then the runtime; Iterate in the Console and keep version history; Runtime credential injection (vault pattern); Separate durable session log from the executor
- Tools: Claude Managed Agents, Claude Console, Claude Code (managed-agent onboarding skill, `/claude-api managed agents onboarding`), Claude Agent SDK, TypeScript Claude SDK, Claude Opus, Claude Sonnet, Slack (Slack app and bot), Notion (built-in integration), MCP servers, OpenClaw, GitHub (private repo as data source)

## [1 Million Sandboxes Per Second?! Dynamic Workers Are INSANE](../videos/7Re3HReM5SQ.md)
`7Re3HReM5SQ` · Better Stack · 2026-04-02 · q3 · practitioner · tutorial · also: sandboxing-execution, infra-cost-scaling

Better Stack walks through Cloudflare Dynamic Workers, V8-isolate workers created at runtime by a parent Worker, as a faster, lighter alternative to container sandboxes for running AI-generated code. The catch is JavaScript only, with no filesystem.

- Techniques: Per-request sandboxed child Worker with network disabled; Stable-name reuse for warm sandboxes; Custom bindings and RPC into the child; Bundling npm dependencies into a child; Egress interception for credential injection; Agent code-execution loop with artifact persistence; Scripted bulk spawn with create-or-reuse
- Tools: Cloudflare Dynamic Workers, Cloudflare Workers, Wrangler, V8 isolates, Cloudflare Sandboxes, Cloudflare Durable Objects, Cloudflare R2, Cap'n Web, Hono, Anthropic SDK, Claude Sonnet 4.6, Claude Sonnet 3.5

## [Why Every Claude Code User Needs To Try AgentMail (Not Gmail)](../videos/U3TXAdpmvVk.md)
`U3TXAdpmvVk` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: mcp-and-tools, claude-code

Better Stack walkthrough of AgentMail, an email-inbox API for agents, shown through the CLI in Claude Code and a 30-second polling reply agent built on the Claude SDK. Mostly a demo, with no benchmarks.

- Techniques: Give each agent its own inbox via CLI + skill, not an MCP server; Split inboxes by purpose or by agent; Poll for mail with a Claude Code loop for short-lived checks; Custom polling reply agent on the Claude SDK
- Tools: AgentMail (API, dashboard, CLI, skill, MCP server, Python and TypeScript SDKs), Claude Code (loop feature, skills), Claude SDK, Claude Haiku, Google Workspace CLI (mentioned, previous video), Gmail, Codex, Gemini CLI, Electron (transcript says "Electrobon"; desktop app framework, mentioned only)

## [NVIDIA NemoClaw First Look: Secure AI or Just Over-Engineered?](../videos/5v0RJkqjU8c.md)
`5v0RJkqjU8c` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: sandboxing-execution, security-guardrails

Better Stack's hands-on first look at NVIDIA's NemoClaw, an OpenClaw agent wrapped in the OpenShell sandbox; the setup is fragile and per-request approvals make autonomous tasks tedious.

- Techniques: Deploy NemoClaw on a Brev GPU instance; Answer the NemoClaw installer prompts; Start the agent and approve pending egress requests; Recover a stuck Telegram gateway; Watch OpenClaw logs during autonomous tasks
- Tools: NemoClaw (NVIDIA, install script plus `nemoclaw start`), NVIDIA OpenShell (sandbox; OpenShell manager TUI for approving requests), OpenClaw (agent; `configure` wizard), Nemotron (NVIDIA inference model), NVIDIA Brev (cloud GPU platform; `brev shell`), Docker, CUDA, Telegram (bot token bridge)

## [Claude Code Loop: The Feature Everyone Misunderstands](../videos/Xxqu-kz00gw.md)
`Xxqu-kz00gw` · Better Stack · 2026-04-02 · q4 · practitioner · review · also: claude-code

Better Stack walks through Claude Code's new loop skill (repeat a prompt on an interval), argues it is for re-running tasks inside one session rather than a durable assistant, and lists its limits: 3-day auto-expiry and session-only storage.

- Techniques: In-session interval polling with loop; Clock-time daily job; List and delete scheduled jobs; Durable schedules via Claude Desktop or Cowork; Avoid loop for long-lived listeners or Ralph loops
- Tools: Claude Code, loop skill, cron create skill, cron list tool, Claude Desktop, Cowork, Claude Sonnet, Claude Haiku, OpenClaw, Telegram, WhatsApp, Discord

## [Anthropic Just Killed All Your Agent Harnesses](../videos/nBH07G-zayk.md)
`nBH07G-zayk` · AI LABS · 2026-04-02 · q2 · practitioner · review · also: testing-verification, context-engineering, claude-code

Walkthrough of Anthropic's reported harness ablations: with Opus 4.5/4.6, keep a planner, a generator and a separate graded evaluator, and drop micro-level plans, context resets and sprint contracts for strong models.

- Techniques: Product-level planner agent; Separate evaluator with an adversarial stance; Weighted rubric with a score per criterion; Generator and evaluator as agent-team members; Sprint contract for weaker models; Bolt Anthropic's evaluator onto GSD
- Tools: Claude Code, Claude Opus 4.5, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Anthropic agent harness, BMAD, GSD, SpecKit, Superpowers, Ralph Loop, Playwright MCP

## [What REALLY Happened When 16 Claude Agents Tried To Build a C Compiler From Scratch](../videos/SVREdZHPG1I.md)
`SVREdZHPG1I` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: multi-agent, testing-verification, coding-agents

Better Stack breaks down Anthropic's experiment with 16 parallel Claude Opus 4.6 agents building a C compiler: git-based task locks, shared test harnesses, GCC as an oracle, and why the presenter says it was not fully autonomous.

- Techniques: Git-commit task lock for parallel agents; Isolated clones with push-to-upstream; Ralph loop with a fresh session per task; Quiet test harness with a log file; Deterministic sharded test subsets; Reference-compiler oracle for partial builds; README and progress files as cross-session memory; Role-specialized review agents
- Tools: Claude Opus 4.6, Claude (Anthropic agent), Docker, Git, GCC, Ralph loop, Linux kernel, SQLite test suite, LibJPEG test suite, Redis test suite, Rust

## [NanoClaw: The Lightweight, Secure AI Assistant OpenClaw Should Have Been](../videos/AQ5uiLyr8bQ.md)
`AQ5uiLyr8bQ` · Better Stack · 2026-03-02 · q2 · intro · review · also: sandboxing-execution, claude-code

Better Stack walkthrough of NanoClaw, a ~500-line personal AI assistant on the Claude Agent SDK with WhatsApp, containers and self-extension by asking the agent; a short overview with a single feature-add demo.

- Techniques: Self-extending assistant via chat-driven code change; Hardened VPS install for a personal agent; Use a Claude subscription for an SDK-based agent
- Tools: NanoClaw, OpenClaw, Claude Agent SDK, Claude Code, Claude Sonnet (default model), Docker, Apple containers, Node.js (above v20), WhatsApp, Tailscale, Vercel agent-browser, Unsplash (image tool demo)

## [Cloudflare Just Killed Mac Minis? OpenClaw Runs Serverless – Here's How!](../videos/DQdYE02TkIQ.md)
`DQdYE02TkIQ` · Better Stack · 2026-03-02 · q2 · practitioner · tutorial · also: sandboxing-execution, infra-cost-scaling

Walkthrough of running the OpenClaw agent gateway serverlessly on Cloudflare Workers, Sandboxes, Browser Rendering and R2, with setup steps and a serverless-versus-VPS verdict. Ends with a Better Stack sponsor read.

- Techniques: Prerequisites checklist before deploying OpenClaw on Cloudflare; Verify Durable Object, R2 and browser bindings after deploy; Enable Cloudflare Access and set two Wrangler secrets; Clear a stale sandbox container before redeploying; Pair the device and authenticate the browser; Persist state in R2, not the sandbox disk
- Tools: OpenClaw (captioned as Clawdbot / MoltBot / MaltBot), Cloudflare Workers, Cloudflare Sandboxes (Docker-based), Cloudflare Browser Rendering (headless Chromium), Cloudflare R2, Cloudflare Durable Objects, Cloudflare Access, Cloudflare AI Gateway, Wrangler, Hono, Chrome DevTools Protocol, Docker

## [We Tested The Smallest "OpenClaw" AI Agent in the World (zclaw)](../videos/MCTTe8nZEgc.md)
`MCTTe8nZEgc` · Better Stack · 2026-03-02 · q2 · intro · review · also: coding-agents, dev-tools

Better Stack installs zclaw, a tiny ESP-IDF AI assistant for ESP32 boards driven over Telegram, then adds a custom display tool; a hands-on hardware demo with reproducible setup steps and candid limits.

- Techniques: zclaw install and provisioning flow; Wi-Fi bench workaround; Adding a custom tool to zclaw; Natural-language pin aliases stored on-device; Hello-world LED sanity circuit; Telegram allow-list for device control
- Tools: zclaw, ESP32, ESP32-C3, ESP-IDF, Telegram, BotFather (Telegram bot), Telegram user-info bot, OpenRouter, OpenAI, Anthropic, Ollama, Claude Code

## [Shanon: The Open Source AI Pentester Powered By Claude Code](../videos/H7Xh-x_TVdQ.md)
`H7Xh-x_TVdQ` · Better Stack · 2026-03-02 · q3 · intro · review · also: security-guardrails, token-cost-efficiency, sandboxing-execution

Walkthrough of Shannon, an open-source AI pentester built on the Claude Agent SDK: Temporal-orchestrated phases, parallel vulnerability agents, and a 2.5-hour, roughly $60 run against OWASP Juice Shop.

- Techniques: Temporal-backed durable agent pipeline; Static analysis then live-app recon; Parallel specialist fan-out with paired exploit agents; Reproduction setup as described in the video
- Tools: Shannon (open-source AI pentester), Claude Agent SDK (Anthropic), Claude Sonnet 4.6, Docker Compose, Temporal, Playwright, OWASP Juice Shop, Kali Linux (mentioned as the manual alternative), Claude Code Security (announced, not yet released per the creator), Shannon Pro (paid tier), OpenAI Agents SDK (speculated port), Vercel AI SDK (speculated port; transcript spells it 'Vasell')

## [OpenClaw Use Cases That Are Actually Insane](../videos/hp7n45JqvIw.md)
`hp7n45JqvIw` · AI LABS · 2026-03-02 · q2 · practitioner · review · also: coding-agents, software-factory

AI LABS walks through weeks of running OpenClaw on a Mac Mini for developer ops: dependency upgrades, cost and uptime monitoring, SEO checks, PRD-to-deploy builds, cold-email drafts and Claude Code delegation.

- Techniques: Guideline-driven dependency upgrade cron; Scheduled research briefing; Cost watchdog skill; Hosted-app heartbeat monitor; SEO heartbeat; PRD-to-deployed-app run; Delegate to Claude Code with subtasks and per-step commits; Draft-only cold outreach via cron; Email triage heartbeat
- Tools: OpenClaw, Claude Code, Codex, Gemini 3, Nano Banana Pro (Google image-generation skill, bundled with OpenClaw), Nano Banana (earlier skill referenced), GOG CLI, Google Workspace CLI, Google Cloud console, AWS CloudWatch, Vercel, GitHub

## [Claude Code Just Got a Brain Upgrade Inspired By Beads](../videos/-xOAYPjhigY.md)
`-xOAYPjhigY` · Better Stack · 2026-02-02 · q3 · intro · review · also: claude-code, multi-agent, context-engineering

Better Stack walkthrough of Claude Code's new task system (v2.1.6+), which replaces todos with JSON-backed tasks that support dependencies, sub-agents, and shared task lists across sessions; compared against Beads and the Ralph Wiggum loop.

- Techniques: Plan file to tasks, then sub-agent execution; Shared task list across sessions via env var; Version-control task state
- Tools: Claude Code (v2.1.6+), Beads, Ralph Wiggum loop, Opus 4.5, XDL (CLI for downloading videos from X/Twitter, used as the demo project), Better Stack

## [Ship LLM Apps Locally with Dify](../videos/V-YvJdZx6sY.md)
`V-YvJdZx6sY` · Better Stack · 2026-02-02 · q2 · intro · review · also: rag-retrieval, dev-tools

Better Stack's short walkthrough of Dify, a self-hosted visual builder for LLM apps (RAG, chained prompts, agents), with a file-summarization demo and a candid list of drawbacks.

- Techniques: Branch a workflow on input file type; Add a model provider via Settings; Run Dify locally with Docker; Choose between visual builder and code orchestration
- Tools: Dify, LangChain, LlamaIndex, n8n, OpenAI API, Google Gemini, Docker, Vercel, Supabase, ReAct agent pattern

## [I Tried Agentic AI from the Terminal... Here’s What Actually Works](../videos/KRT-7xK97WQ.md)
`KRT-7xK97WQ` · Better Stack · 2026-02-02 · q2 · intro · review · also: dev-tools

Short hands-on look at ASI-1's new Python CLI for its agent API: it works in scripts and keeps session state, but the pip-installed mode drops context, and the API is hard to find.

- Techniques: Script-wrapped agent CLI with a remembered session; Test the agent in the script path before trusting it in automation; Pick the invocation mode by whether state must persist
- Tools: ASI-1 CLI, ASI-1 API, ASI-1 (agentic model platform), Python, pip

## [I Can't Believe Anthropic Messed Up The Ralph Wiggum](../videos/XVAhQ-EcrWA.md)
`XVAhQ-EcrWA` · Better Stack · 2026-02-02 · q3 · practitioner · tutorial · also: context-engineering, coding-agents, claude-code

Better Stack explains the Ralph loop (a bash while-loop that reruns one prompt with a fresh context each time) and why the official Claude Code Ralph plugin, with compaction and iteration caps, drifts from the canonical design.

- Techniques: Fresh-context bash Ralph loop; Plan-file task selection; Keep fixed context small; Human-on-the-loop review; GitHub-issues task queue; Filter error output with an MCP server
- Tools: Ralph loop (bash while-loop pattern), Claude Code, Claude Code Ralph Wiggum plugin (Anthropic, slash command with max iterations and completion promise), agents.md, Raz Mike's Ralphie bash script, agent-browser tool (named Vasell in the captions), GitHub issues, Better Stack MCP server (log and frontend error search), GPT-5 tokenizer (used for a token-count comparison)

## [ShadCN is Way too Powerful Now](../videos/MFJ0mH72_qI.md)
`MFJ0mH72_qI` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · also: claude-code, testing-verification, context-engineering

Ralph stop-hook loop plus TDD and screenshot checks for ShadCN UI work; a separate verification iteration before the completion promise fixed premature "done" claims.

- Techniques: Stop-hook completion-promise loop; Test-first workflow inside the loop; Screenshot verification protocol; Two-phase completion gate
- Tools: ShadCN (UI component library), Claude Code, Ralph plugin (Anthropic, Ralph loop), Claude Code stop hooks, Playwright, Playwright MCP (named only to say it was not used), Notion (reference point for the board view), Automata (sponsor)

## [Moltbook is WILD... (AI Only Reddit)](../videos/EGD1LCuoTuo.md)
`EGD1LCuoTuo` · Better Stack · 2026-02-02 · q2 · intro · review · also: security-guardrails, skills-self-improvement

A walkthrough of Moltbook, a Reddit-style site where only AI agents post, powered by OpenClaw; it mostly shows how steerable and security-risky the setup is.

- Techniques: Human-steered post test for agent autonomy; Markdown skill plus heartbeat as an always-on agent loop
- Tools: Moltbook, OpenClaw (the video says it was formerly called MaltBot/Moltbot and ClaudeBot), Reddit (used as the comparison), Claude Opus 4.5 (shown as the model behind one post)

## [I Couldn't Believe Claude Tasks Could Do This](../videos/li8bIt-mjbA.md)
`li8bIt-mjbA` · AI LABS · 2026-02-02 · q2 · intro · review · also: claude-code, multi-agent, coding-agents

Walkthrough of Claude Code's new built-in task system: a coordinator splits work into a dependency graph, runs independent sub-agents in parallel, and persists tasks outside the context window so they survive /clear and restarts.

- Techniques: Explicit dependency breakdown prompt; Fan out independent sections of a spec; Named long-running sessions; Inspect task state on disk; Batch folder documentation with Cowork; Research-then-implement handoff
- Tools: Claude Code, Cowork, Claude Chat, Opus 4.5, Haiku, Sonnet, CLAUDE.md, Notion, Lovart (sponsor segment, not evaluated)

## [Why I'm DELETING Clawdbot (Moltbot) After This](../videos/CB6Ysb_BLcM.md)
`CB6Ysb_BLcM` · Better Stack · 2026-02-02 · q2 · intro · review · also: security-guardrails, sandboxing-execution

Better Stack's walkthrough of the Clawdbot (Moltbot) personal agent: how its gateway, channels and state fit together, and why exposing it on a VPS and prompt injection are the main risks. Ends with a sponsor read.

- Techniques: Isolate a self-hosted agent on a dedicated VPS; Put the agent gateway on a private network with Tailscale; Use a separate API key for each agent; Scrub sensitive data from agent transcripts; Run the agent CLI's security command; Give the agent an identity file
- Tools: Clawdbot (Moltbot), Pi agent runtime, Grammy, Discord.js, Telegram, WhatsApp, Discord, Tailscale, Ollama, 1Password skill, Google Calendar skill, Anthropic API

## [Anthropic Released A New Way To "Vibe Code"](../videos/XWp4k9K6oK8.md)
`XWp4k9K6oK8` · AI LABS · 2026-01-02 · q3 · practitioner · tutorial · also: coding-agents, context-engineering, testing-verification

Anthropic's long-running-agent harness: an initializer agent sets up a JSON feature list, progress file and git repo, then a coding agent implements one feature per session with browser testing and commits, so work survives compaction.

- Techniques: Initializer + incremental coder harness; Forced browser verification via Puppeteer; Resume from state, not from context
- Tools: Claude Code, Claude.md, Puppeteer, Git, Next.js, BMAD

## [I Let AI Argue About a Stock](../videos/ce3_LzVm2Jg.md)
`ce3_LzVm2Jg` · Better Stack · 2026-01-02 · q2 · intro · tutorial · also: multi-agent, dev-tools

Better Stack demo of Trading Agents, an open-source Python multi-agent project that simulates a trading firm with LLM analyst agents and a bull/bear debate; a quick CLI walkthrough with cost and non-determinism caveats.

- Techniques: Role-specialized analyst agents plus adversarial bull/bear debate; Scripted run instead of CLI; Model-agnostic setup
- Tools: Trading Agents (open source Python project, multi-agent trading simulation), LangGraph, OpenAI API, Alpha Vantage API, Yahoo Finance, Anthropic API, Google models, Conda, Python 3

## [OpenAI Swarm Hype Explodes: AgentKit Drives Multi-Agent AI Revolution](../videos/oV3IjJSXQyM.md)
`oV3IjJSXQyM` · Better Stack · 2026-01-02 · q2 · intro · news · also: multi-agent, mcp-and-tools

Better Stack argues OpenAI's deprecated Swarm is not back and that AgentKit (Oct 2025) is the real multi-agent upgrade, but the video gives few technical details and mostly unsourced claims.

- Techniques: Migrate off Swarm-style stateless handoffs to a framework with state and tracing; Budget multi-agent traces for latency and retries; Built-in trace-and-score evals for agent performance
- Tools: OpenAI Swarm (deprecated March 2025), OpenAI Agents SDK, OpenAI AgentKit (Agent Builder, ChatKit, connector registry), OpenAI Chat Completions API, RFT (reinforcement fine-tuning) beta, o4-mini (transcribed 'O4 Mini'), GPT-5 (multi-model stack, mentioned without detail), MCP (Model Context Protocol; transcribed 'MPC'), DeepSeek (transcribed 'DeepSeq'), Llama (transcribed 'Ulma 3')

## [Claude Ralph - The Bizarre Anthropic Plugin That Every Developer Is Missing](../videos/ny_BAA3eYaI.md)
`ny_BAA3eYaI` · Better Stack · 2026-01-02 · q3 · intro · review · also: claude-code, coding-agents, token-cost-efficiency

Walkthrough of the Ralph Wiggum Claude Code plugin, which re-runs the same prompt through a stop hook until a completion promise appears, with a max-iterations cap as a cost guard.

- Techniques: Ralph-style re-prompt loop (manual); Ralph Claude Code plugin with stop hook; Iteration cap as a spend limit; Tests in the prompt file as the completion gate; Decompose before looping
- Tools: Claude Code, Ralph Wiggum plugin (Anthropic Claude Code plugin, /ralph command), Claude Code stop hook, AMP (agent named as a comparison; no details given), bun test (Bun test runner), beads (suggested pairing, not demonstrated), TypeScript, Python

## [Building AI That Actually Helps You Live Better | Better Stack Podcast Ep. 7](../videos/46EsyQYKMjA.md)
`46EsyQYKMjA` · Better Stack · 2025-12-02 · q3 · intro · interview · also: security-guardrails, context-engineering, mcp-and-tools

Better Stack podcast interview with Ben, founder of Spec, a macOS-native personal-context assistant; main engineering points are local-first data, OS-level access, and side effects gated outside the model.

- Techniques: Permission-scoped local data access for apps with no API; Split draft and send tools, with the send gated by a human click; Write-only agent sandbox; Event listeners and timed services instead of a single chat loop; Living context with distilled per-thread summaries as the trigger input; Route models by task type, separating persona from reasoning
- Tools: Spec (macOS/iOS app, Swift), Swift, Granola, Riverside, Claude Opus 4, Claude Sonnet 4, Claude Sonnet 4.5, Claude Haiku 4.5, GPT-5, GPT-OSS, Gemini 2.5, MCP

## [Before You Pay for Manus AI, See What This Free Tool Can Do](../videos/S3Q7CCV_PzE.md)
`S3Q7CCV_PzE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: local-ai, multi-agent

Walkthrough of installing and running Agentic Seek, an open-source Manus-style multi-agent tool that runs locally or through a cloud API, with the speaker's hardware and cost caveats.

- Techniques: Install from the README; Switch config.ini from local to API mode; Headless browser and voice options; Start order; Planner plus specialized agents
- Tools: Agentic Seek (version not stated), Manus AI, Docker, Python 3.10, Ollama, Qwen, DeepSeek, GPT-4o, GPT-4o mini, Cursor (editor used for config)

## [Suna: The FREE Open Source Alternative to Manus AI](../videos/aqF8ItxLCRA.md)
`aqF8ItxLCRA` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: sandboxing-execution

Walkthrough of Suna, a free open-source self-hosted alternative to Manus, with one head-to-head build test, its architecture, a local Docker setup, and its cost and bug downsides.

- Techniques: Self-host an agent stack with Docker Compose after DB migrations; Isolate AI-generated code in per-run Docker environments via a sandbox provider; Use container logs as the primary debug surface for agent runs; Head-to-head test of agent products on one identical prompt
- Tools: Suna (captions say Sooner; open-source agent), Manus, Next.js, Supabase (auth, history, file storage; CLI; basejump schema), FastAPI, Daytona (isolated Docker sandboxes), Docker and Docker Compose, Redis, Anthropic API (Claude), OpenAI API, Firecrawl (web crawling), Tavily (web search)

## [Agno AI Agent Tutorial: Build & Run AI Agents with Agent UI + MCP + CrewAI (Best Tutorial)](../videos/RWQv6JV7rKw.md)
`RWQv6JV7rKw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: multi-agent, mcp-and-tools

A short tutorial on Agent UI, an open-source Next.js chat front-end for agents. It shows swapping Agno's playground for a FastAPI backend and routing between specialist agents over A2A.

- Techniques: Install Agent UI via the docs' npx template; Swap the Agno Playground for your own backend; Main-agent router over specialist endpoints; Cap reply length with the system prompt
- Tools: Agent UI, Agno, Agno Playground, Next.js, npx, FastAPI, OpenAI SDK, A2A (agent-to-agent protocol), Cursor, LangChain, gpt-4o-mini, Gemini 2.5 Pro (mentioned in the demo answer, not used by the presenter's own setup)

## [The $10B System Prompts Behind Cursor AI and Others Just Leaked…](../videos/A5r2tfifYfY.md)
`A5r2tfifYfY` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, context-engineering, sandboxing-execution

Walkthrough of leaked system prompts from Cursor, Windsurf, Replit, Manus and others, with the host's takeaways on tool design, background execution, memory, sandboxing and a repo-to-text trick. Useful as prompt-design evidence, but the verdicts are overreaching.

- Techniques: Repo subfolder to LLM-readable text; Post-edit verification loop; Background command execution with process status checks; Persistent memory with semantic auto-retrieval; Ask-for-secrets and stuck-fallback behavior; Sandbox-scoped guardrails in the system prompt
- Tools: Cursor, Windsurf (Cascade), Replit, Manus, Lovable, Devin, Bolt, Roo Code (transcript: 'Rucode'), Netlify, Next.js, shadcn/ui (transcript: 'Shad CNUI'), PostgreSQL

## [Mastra: The AI Framework That Changes Everything](../videos/_dG8iZgmicQ.md)
`_dG8iZgmicQ` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, memory

Beginner walkthrough of Mastra, a TypeScript agent framework: build an agent, add a tool, memory, working memory, an MCP server, and call it via API.

- Techniques: Minimal Mastra agent; Custom tool with zod output schema; Persistent chat memory; Working memory template; Adding MCP server tools to an agent; Calling a Mastra agent from code
- Tools: Mastra (TypeScript agent framework) and Mastra Core, Mastra CLI, Mastra playground and dev script, Mastra memory (Memory class, working memory), Mastra LibSQL storage store, Mastra MCP client, Firecrawl MCP server, zod (output schemas), Mastra Swagger API docs and Mastra client, Mastra 101 course (source of the system prompt, per the presenter), Whisper Flow (dictation, named as Whisperflow in captions), Claude Agent SDK (mentioned as the presenter's earlier video topic)

## [Add this Chrome Extension to 10X your productivity](../videos/j8KcvLrZ9uU.md)
`j8KcvLrZ9uU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: product-ux

A walkthrough of MindStudio's Chrome extension for running prebuilt browser agents and building a simple word-lookup agent with its visual block builder. Mostly a product tour with a hype title and thin technical depth.

- Techniques: Install and pin the MindStudio extension; Build a selection-driven lookup agent in the visual builder; Workaround for end-session returning JSON
- Tools: MindStudio (Chrome extension and agent builder), Chrome Web Store, Arc browser, Claude 3.5 Haiku (free model in builder), GPT 4.0 Mini (free model in builder), ChatGPT (mentioned as the manual alternative), Cursor (mentioned), Windsurf (mentioned)

## [OpenAI Agent Builder... n8n Killer?](../videos/RBlHcHUvFKY.md)
`RBlHcHUvFKY` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: mcp-and-tools, pr-code-review

Hands-on walkthrough of OpenAI's new drag-and-drop Agent Builder, used to build a GitHub PR code-review agent; covers guardrails, structured outputs, MCP, widgets and evals, with bugs noted and a verdict that it does not yet replace n8n.

- Techniques: Input guardrail with a fail branch; Structured extraction gate before tool calls; Transform node to flatten nested outputs for a tool; Isolated reviewer context; Natural-language graders over traces; Widget output from a final agent; Adding a custom MCP server
- Tools: OpenAI Agent Builder, ChatKit, Agents SDK, Apps SDK, GitHub MCP server, Context7 MCP server, GPT-5, GPT-4.1, OpenAI vector store (file search), web search tool, code interpreter, n8n

## [This Framework Replaces Your ENTIRE Backend (Motia)](../videos/xvwY4ZKklrc.md)
`xvwY4ZKklrc` · Better Stack · 2025-11-02 · q3 · intro · review · also: observability, dev-tools

Better Stack walks through Motia, a framework that runs APIs, cron jobs, background tasks and AI steps in one runtime built from small "step" files, and demos a four-step tweet pipeline.

- Techniques: One file per step (config + handler); Event chaining between steps; Cron polling of pending work in shared state; Trace-ID-keyed status endpoint; Manual triggering from the dashboard or curl
- Tools: Motia, OpenAI GPT-4, Bluesky, Better Stack, TypeScript, Python, curl

## [Sonnet 4.5 Just Unlocked a New Breed of Agents](../videos/t7VuWwukO3I.md)
`t7VuWwukO3I` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: claude-code, coding-agents, mcp-and-tools

AI LABS walkthrough of running Claude Code as a scheduled GitHub Actions agent (model-news monitor to Slack) and as an issue-triggered background coder, with two rules learned from failed runs: auto-approve tools and test MCP servers first.

- Techniques: Install the Claude Code GitHub app into a repo; Scheduled news monitor on GitHub Actions; Whitelist all tools for headless runs (Rule 1); Verify MCP servers before automation (Rule 2); Post to Slack via incoming webhook with curl; Hand off a background coding task via a GitHub issue; Paste SDK documentation into the task; Verify auth end to end on a branch
- Tools: Claude Code (version 2 announced with Sonnet 4.5), Claude Sonnet 4.5, Claude Code GitHub app, GitHub Actions, GitHub, Slack (incoming webhook via curl), Supabase (auth), Supabase MCP server, Claude Agent SDK (TypeScript and Python docs), BMAD method (referenced), OpenAI Codex (referenced as inspiration for cloud agents), Cursor (referenced for code rewind), GPT-5 (mentioned in the opening)

## [Build Apps with Cursor Like the 1% Using This NEW Method](../videos/OZaxtm3RyCw.md)
`OZaxtm3RyCw` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, context-engineering

Walkthrough of building a wallpaper app in Cursor with Taskmaster AI: the PRD becomes a dependency-ordered task list the agent works through one task at a time, so one chat holds the whole build.

- Techniques: Install and initialize Taskmaster globally, then init per project; Configure keys in .env; Brainstorm with a no-edit instruction; Generate the PRD from an example template; Parse the PRD into tasks, then work them sequentially; Handle implementation drift with an explicit change list; Work in the correct subdirectory
- Tools: Cursor, Taskmaster AI, Claude (Anthropic API), Perplexity API, Unsplash API, Next.js

## [Connect any LLM to any MCP server without any MCP client.](../videos/QZ6AreMxMKA.md)
`QZ6AreMxMKA` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents

A beginner walkthrough of a Python MCP client library that runs an agent over any LLM and any MCP server, so no desktop client is needed. Shows setup, a single-file Airbnb example, multi-server config and Cursor tips.

- Techniques: Provider-agnostic MCP agent from a config file; Cap agent steps and filter results in the prompt; Multi-server config with a service manager; Give a coding assistant the library docs; Flatten a repo for LLM questions (gitingest)
- Tools: MCP (Model Context Protocol), Python, pip3, LangChain, LangChain OpenAI integration, LangChain Anthropic integration, OpenAI, Anthropic, Cursor, Windsurf, Claude Desktop, Airbnb MCP server

## [Figure 03 and the Future of Robotics](../videos/NL2zbYhC5Z4.md)
`NL2zbYhC5Z4` · Better Stack · 2025-11-02 · q2 · intro · news · also: models-research, training-finetuning-rl

Better Stack's overview of Figure 03's claimed actuators, balance control, sensing, cooling and Helix model, plus speculative stack guesses from GitHub repo names; few reproducible details.

- Techniques: Physics-first balance with a learned layer; Layered real-time control stack; Sim-to-real RL with massively parallel environments; Latency budgeting as a first-class metric; Thermal co-design with structure; Fleet-wide offload for centralized training
- Tools: Figure 03, Helix (Figure's large behavior model), NVIDIA Isaac Lab, NVIDIA Isaac Sim, MuJoCo, Brax, nvblox (transcribed as NV Blocks), LightGlue ONNX

## [Cloudflare Just Made AI Agents WAY Easier (Agents SDK)](../videos/l4tHKJFQvRg.md)
`l4tHKJFQvRg` · Better Stack · 2025-11-02 · q3 · intro · review · also: infra-cost-scaling, dev-tools

Better Stack demos Cloudflare's Agents SDK starter: durable-object agents that persist state, sync across browsers, schedule tasks and pause for human approval. Demo-driven, with no benchmarks.

- Techniques: Single shared agent for multi-window sync; Per-user or per-workflow agent routing; Chat agent setup; Persisting UI state; Human-in-the-loop tool approval; Scheduling tasks from chat
- Tools: Cloudflare Agents SDK (starter template), Cloudflare Durable Objects, Cloudflare Workers AI, AI SDK (used for tools and model calls), AIChatAgent (Agents SDK base class for chat), useAgent (React hook from the SDK), React, WebSocket, Hono (official middleware mentioned), OpenAI-compatible API schema (for model choice)

## [NEW OpenAI AI Agents SDK – Multi-Agent AI Made Simple](../videos/ZvvQKie3X70.md)
`ZvvQKie3X70` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: multi-agent, mcp-and-tools, observability

Better Stack walkthrough of OpenAI's new Python Agents SDK: agents, handoffs via a router agent, function and built-in tools, local context, input guardrails, and built-in tracing.

- Techniques: Router/triage agent with handoff descriptions; Function tool from a Python function; Typed local context object; Guardrail as a classifier agent; Inspecting run steps with new_items
- Tools: OpenAI Agents SDK (Python), OpenAI web search tool, Pydantic, OpenAI platform traces

## [Claude code vs Codex vs Cursor: Who gets the cake?](../videos/_Xbe7MQ2NxI.md)
`_Xbe7MQ2NxI` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, coding-agents, mcp-and-tools

Argues Claude Code and other AI CLIs are "portable agent engines": terminal agents can call each other via bash, run headless (-p), deploy to GitHub Actions and act as MCP servers. Opinion-heavy, with a sponsor segment.

- Techniques: Headless single-shot invocation; Cross-agent delegation through bash; Scheduled agent via GitHub Actions; Claude Code GitHub app for PR review; Mixed local and remote MCP servers
- Tools: Claude Code, Claude Code GitHub app, Claude Code for Chrome, Claude for Excel, Agent SDK (formerly Claude Code SDK), Codex CLI, Gemini CLI, Qwen Code (transcript: QuenCode), Cursor CLI, gitingest, GitHub Actions, Slack

## [Codex SDK vs Claude: One is CLEARLY Better](../videos/X1izM-063g0.md)
`X1izM-063g0` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents

Short walkthrough of the TypeScript-only Codex SDK (run, streamed events, sandbox modes, tool calls, a follow-up loop), ending with the host preferring the Claude Agent SDK for its missing features.

- Techniques: Minimal Codex SDK script; Choose a sandbox mode per run; Resume a thread by ID; Structured response via JSON schema or zod; Stream typed events with runStreamed; Interactive loop over one thread
- Tools: Codex SDK (TypeScript), Codex CLI, Codex IDE extension, Codex Web, Claude Agent SDK, OpenAI App SDK, OpenAI Agent Builder, zod

## [LBMs Are About to Change Everything in Robotics](../videos/2Ks449BLuiI.md)
`2Ks449BLuiI` · Better Stack · 2025-11-02 · q2 · intro · news · also: models-research

Explainer on large behavior models (LBMs), robot-control models that map camera, joint and language inputs to actions, using Figure AI's Helix as the example. Thin on substance; mostly hype and analogy.

- Techniques: Two-rate hierarchical control (slow reasoner, fast reflex); One shared policy across several robots; Starting point for hands-on LBM work
- Tools: Helix (Figure AI robot model), OK-Robot (open-source pick-and-place framework), Isaac Gym (simulator), MuJoCo (simulator; auto-caption reads 'Mujocko'), GPT-3 (mentioned as an analogy), GPT-4 (mentioned as an analogy)

## [Sora 2 Cameos & Jailbreaks & Claude Agent SDK | Better Stack Podcast Ep. 5](../videos/YjdMscni2CI.md)
`YjdMscni2CI` · Better Stack · 2025-11-02 · q2 · intro · panel · also: claude-code, voice-multimodal, context-engineering

Better Stack podcast: hosts riff on Sora 2's cameo feature, memorized training data and weak guardrails, then on the Claude Agent SDK for custom agents with their own prompts, tools and hooks. Mostly opinion.

- Techniques: Custom agent on the Claude Agent SDK with an owned system prompt; Local functions as agent tools in place of MCP tools; Hook-based output enforcement with automatic redo; Coaching agent that withholds answers
- Tools: Sora 2, VO3, Claude Agent SDK, Claude Code, Claude Code hooks, MCP, Claude Sonnet 4.5, Claude Opus, GPT-5, GPT-5 Codex, Codex, Grok 4

## [Prisma founder is solving local-first (LiveStore)](../videos/ZW9dVJ_eFIU.md)
`ZW9dVJ_eFIU` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

Prisma founder's LiveStore: a local-first, reactive-SQLite state manager with an immutable event log and git-style push/pull sync, shown via a to-do app on Cloudflare Durable Objects plus D1.

- Techniques: Schema-first LiveStore app structure; Event-sourced state with materialized projections; Reactive queries via queryDb and store.useQuery
- Tools: LiveStore, SQLite, React, Cloudflare Durable Objects, Cloudflare D1, Cloudflare Workers / WebSockets

## [AI Agent Protocols Explained: MCP, A2A, ACP and More](../videos/tb0c70DROYE.md)
`tb0c70DROYE` · Better Stack · 2025-11-02 · q3 · intro · review · also: mcp-and-tools, multi-agent

Better Stack walks through MCP, A2A, ACP and ANP: what each protocol does, where it fits, and short local demos of MCP (Goose), A2A (two agents on Ollama) and ACP (story writer). Practical orientation, no benchmarks.

- Techniques: Add an MCP server to Goose as a command-line extension; Chain MCP servers in one agent task; Build a standalone A2A agent (summarizer / ideator pattern); Serve several ACP agents from one server and call them over HTTP
- Tools: MCP (Model Context Protocol, Anthropic), JSON-RPC 2.0, A2A (Agent2Agent, Google) and its SDK, ACP (Agent Communication Protocol, IBM), ANP (Agent Network Protocol), AITP, ACONP / ACOMP, Coral, Agora, agents.json, WAP push, Goose

## [Building Custom AI Agents Just Got EASIER - Claude Agent SDK](../videos/NsROagHaKxA.md)
`NsROagHaKxA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: claude-code, mcp-and-tools, coding-agents

Better Stack walkthrough of the Claude Code SDK (now also called the Agent SDK): a single-prompt query, a streaming-input REPL, replacing the system prompt, and adding a custom MCP tool, all in one short TypeScript file.

- Techniques: One-shot query; Streaming-input REPL; Full system-prompt replacement; Appending to the system prompt; In-process custom MCP tool; Combined demo structure
- Tools: Claude Code SDK (the video also calls it the Claude Agent SDK in its title), Claude Code CLI, Claude Haiku (model option example), TypeScript, zod, MCP (createSdkMcpServer, tool), Bash tool (built-in), Glob tool (built-in)

## [OpenAI Agent Builder vs Claude: Who Wins Multi-Agent Workflows? (Complete Comparison)](../videos/sLiVXlIlSBQ.md)
`sLiVXlIlSBQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, product-ux, coding-agents

A walkthrough of OpenAI's AgentKit (Agent Builder, ChatKit, widgets), with a Speechmatics sponsor segment up front; practical for seeing the visual workflow and ChatKit setup, thin as a head-to-head comparison.

- Techniques: Classifier-then-route agent workflow; Human approval gate in a workflow; Remote MCP server registration per agent; ChatKit starter quickstart; Theme via Playground, then hand off to a coding agent; Prompt-to-widget, then pin the format in the agent prompt; Custom widgets with Claude Code and agents.md
- Tools: OpenAI Agent Builder, OpenAI AgentKit, OpenAI ChatKit, ChatKit Playground, OpenAI Widget Builder, OpenAI vector store / file search, OpenAI guardrails node, ChatGPT apps, Zapier (MCP servers), Pipedream (MCP servers), n8n (comparison only), Next.js

## [The EASIEST way to build AI apps – AI SDK Overview](../videos/TbjBzopteO4.md)
`TbjBzopteO4` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools, dev-tools

Better Stack's tour of Vercel's AI SDK for TypeScript: it builds a Next.js chat app with streaming, file input, reasoning display, manual, provider and MCP tools, and streamed structured output, all in about 17 minutes.

- Techniques: Streaming chat endpoint; Per-provider options for reasoning; Manual tool with zod schema; External search and page-fetch tools; Provider-defined tools plus source output; MCP server as tools; Agent loop step cap; Smooth streaming; Streamed structured output; Local dev with an AI gateway
- Tools: AI SDK (Vercel), Next.js, React, Svelte, Angular, Zod, Vercel AI Gateway, OpenAI GPT-5, GPT-5 nano, gpt-image-1, Anthropic Claude Sonnet 4, Google Gemini 2.5 Flash

## [Introducing Open-Source PHIDATA: Your first step towards building your own AI Agents](../videos/nkh7q8WU7oU.md)
`nkh7q8WU7oU` · AI LABS · 2024-11-02 · q2 · intro · tutorial · also: memory

Walkthrough of Phidata's agent playground UI, showing how to serve agents from a local server on port 7777 and chat with them through the hosted app while memory and sessions stay on your machine.

- Techniques: Serve agents from a local server and attach a hosted chat UI; Define an agent with a description, tools and a current date; Keep session history in a local DB file and reset by deleting it; Turn on debug logs with an environment variable
- Tools: Phidata, Phidata agent UI / playground, OpenAI, Exa, DuckDuckGo search, Ollama, Python virtualenv

