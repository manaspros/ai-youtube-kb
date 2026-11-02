# AI Engineer (@aiDotEngineer) — 830 of 1435 videos have notes

*conference talks and workshops on AI engineering, agents, infra* · [channel](https://www.youtube.com/@aiDotEngineer/videos)

Top categories: [evals](../categories/evals.md) (257) · [agent-architecture](../categories/agent-architecture.md) (217) · [context-engineering](../categories/context-engineering.md) (211) · [product-ux](../categories/product-ux.md) (159) · [security-guardrails](../categories/security-guardrails.md) (141) · [coding-agents](../categories/coding-agents.md) (138) · [mcp-and-tools](../categories/mcp-and-tools.md) (134) · [enterprise-adoption](../categories/enterprise-adoption.md) (132) · [governance-compliance](../categories/governance-compliance.md) (114) · [multi-agent](../categories/multi-agent.md) (113) · [observability](../categories/observability.md) (108) · [infra-cost-scaling](../categories/infra-cost-scaling.md) (96)

Newest first.

## [Your AI Pilots Won't Move the P&L. Here's What Will - Adam Nahari, Apollo](../videos/vUJDyDnqT4c.md)
`vUJDyDnqT4c` · AI Engineer · 2026-11-02 · q3 · intro · talk · topics: enterprise-adoption, product-ux, governance-compliance

Adam Nahari (Apollo) argues AI pilots fail to move EBIT because most spend goes to general tools and change management, and sets out six moves (pick one or two P&L-linked problems, redesign the process end to end, get CEO sponsorship, build with the business, put tools in everyone's hands, pre-set kill metrics) to make AI show up in margin.

- Techniques: Work-backward use-case screen; End-to-end workflow redesign over assistive tooling; Embedded domain champions in the build loop; Pre-registered kill gates; At-scale unit economics check

## [I Don't Fear AI Slop. I Fear Untold Stories - Zack Proser, WorkOS](../videos/1et3Lb_KLQo.md)
`1et3Lb_KLQo` · AI Engineer · 2026-11-02 · q3 · intro · talk · topics: product-ux, enterprise-adoption

WorkOS's Zack Proser argues you should encode your taste into an AI "factory" and hand it to others. Examples: an internal blog-drafting bot and a bedtime-story app. A named human still signs off.

- Techniques: Codify your taste as a fixed pipeline, then expose it behind a simple interface; Connector-backed context assembly before drafting; Draft, iterate in plain language, then human sign-off; Four-question review rubric for AI-assisted output; Playtest a factory with a small audience and measure repeat use
- Tools: BlogBot (internal WorkOS blog-drafting system; name as stated in talk), Cloudflare (hosting for BlogBot), Slack (entry point for colleagues), Granola (meeting recordings as a data source), Claude Opus (captioned as 'Opus 5-5 extra high'; the version string is uncertain from auto-captions)

## [AI Writes Code Faster Than Your Team Can Review It - Andrew Norrish, Sourcegraph](../videos/-X3yXTwGs9A.md)
`-X3yXTwGs9A` · AI Engineer · 2026-11-02 · q2 · practitioner · talk · topics: pr-code-review, enterprise-adoption, observability

Sourcegraph's field director argues AI code outpaces human review, so SRE and platform teams need code-search-driven investigation, monitors and bulk remediation. Mostly a vendor pitch.

- Techniques: Deterministic cross-repo code search for incident root cause; Commit-pattern monitors for AI-written code; Bulk remediation across repos; Webhook-triggered agentic triage; Automated RCA from deploy history; Eval-gated code-review agent over historical branches
- Tools: Sourcegraph (code search, code graph, Deep Search, MCP server), HackerOne, git (history search for incident commits)

## [Everyone Has the Same AI Models. Here's What Sets Agents Apart - Richmond Alake, Oracle](../videos/1_lX0m64-aI.md)
`1_lX0m64-aI` · AI Engineer · 2026-11-01 · q2 · intro · talk · topics: memory, agent-architecture, rag-retrieval, security-guardrails

Oracle's Richmond Alake argues agents need an "intelligence plane" (knowledge, memory, access governance, continual learning) beyond the control plane, illustrated with Oracle product demos.

- Techniques: Memory routing with a small fine-tuned decision model; Capture memory traces as fine-tuning data; Ontology and semantic layer in front of retrieval; Propagate user identity into data access; Private inference container for on-prem embeddings, LLM and rerankers
- Tools: Oracle AI Database, Oracle agent memory Python package (generates context cards), Oracle Deep Data Security, Oracle Private AI Services Container, Oracle Cloud (hosted Grok and OpenAI models), Private Agent Factory (no-code agent builder on Oracle AI Database), Memories (open-source agent memory tool built by the speaker), Qwen (fine-tuned as memory-routing decision model)

## [Why We Rebuilt Microsoft Office From Scratch for AI Agents - Yijia Liang, Compound AI](../videos/v0UkV5qS9E4.md)
`v0UkV5qS9E4` · AI Engineer · 2026-11-01 · q3 · practitioner · talk · topics: multi-agent, evals, rag-retrieval, enterprise-adoption

Compound's Yijia Liang explains why they rebuilt Excel, PowerPoint and Word as headless Rust engines for finance agents, using the real Office apps as an oracle in agent loops, plus email-based multiplayer agents and swarm-based file processing.

- Techniques: Objective-function loop against the incumbent app as oracle; Own the write-render-check-fix loop with a headless engine; Grep-first agent swarm over a large file corpus with citations; Email as the multiplayer interface for an agent
- Tools: Compound (getCompound.ai), IronCalc, Microsoft Excel, Microsoft PowerPoint, Microsoft Word, OpenPyXL (transcribed as 'OpenPAxcel' / 'OpenPi Excel'), Outlook, SharePoint, Box, Microsoft Teams, Claude, ChatGPT

## [If Your AI Scores 100%, Your Eval Is Wrong - Ramakrishnan Lokanathan, eslams.com](../videos/7WUzHIF32vA.md)
`7WUzHIF32vA` · AI Engineer · 2026-11-01 · q3 · practitioner · talk · topics: evals, testing-verification, observability

Ramakrishnan Lokanathan argues evals should test the job a system must do, not just a score: test every workflow step, add real failures as regression tests, and make tests harder as scores approach the ceiling.

- Techniques: Ambition-first eval scoping; Step-level workflow evals; Three-layer eval stack; Failure-to-regression loop; Ratcheting the test difficulty; Game-based multi-agent evals (eslams)
- Tools: eslams (open-source Python package, speaker's project, eslams.com), SWE-bench, Humanity's Last Exam, Nemotron 3 (the speaker says he was a red-teamer for these models), GPT-3, ChatGPT, Google Assistant, Gemini, Parallel AI search index (named as 'parallel search model index' in the captions), MIT GenAI Divide report (cited, not named as a tool)

## [I Made a Fruit Fly Review My Code - Nick Nisi, WorkOS](../videos/geMAe-PLJF4.md)
`geMAe-PLJF4` · AI Engineer · 2026-11-01 · q3 · intro · talk · topics: pr-code-review, testing-verification, software-factory

Nick Nisi (WorkOS) demos a fruit-fly connectome trained to approve or reject code diffs, and argues humans should review for intent and proof of work, not bugs.

- Techniques: Team-owned review skill as a gate; Tiered PR escalation pipeline; Agent proof-of-work bundle for review; Measure the reviewer on a labelled diff set; LLM as structured feature extractor before a non-LLM classifier
- Tools: fruitfly.review (speaker's online demo of the fly reviewer; URL as spoken), Greptile (automated AI PR reviewer, named as a comparison), CodeRabbit (automated AI PR reviewer, named as a comparison), Codo (automated reviewer named in the pipeline; name as spoken, may be a caption error), Claude and Codex (named as coding agents that solved the coding problem), Pi (the speaker's coding agent, referenced via 'Pi extensions'; spoken name), GitHub code owners (used to route PRs to the DX team), GEV / JEV / CLEF (LLM and classifier names as spoken; likely auto-caption errors; the LLM is described as a 'System 1 model' that produces the 30 questions), Doom and Beat Saber (prior fruit-fly demos mentioned as context, not tools for the reader)

## [Most of Your Docs Readers Are Now AI Agents - Hahnbee Lee, Mintlify & Lincoln Murr, Coinbase](../videos/YX4Z4XqZ9Vo.md)
`YX4Z4XqZ9Vo` · AI Engineer · 2026-11-01 · q2 · intro · interview · topics: mcp-and-tools, product-ux, enterprise-adoption

A Mintlify and Coinbase fireside chat on designing docs and APIs for agent readers and agent payments; mostly opinion, with one notable agent-traffic stat and a closing build-vs-buy plug.

- Techniques: Keep docs lean for agent readers; Track agent share of docs traffic; Automate doc upkeep, keep prose human; Expose the product as APIs first, then wrap; Pay per call with a wallet instead of API keys
- Tools: Mintlify, x402, MCP, CLI, API, OpenClaw

## [Your AI Agent Wants Your Data. Here's How to Lock It Down - Jeff Smith, Oracle](../videos/LnQce-eHm8k.md)
`LnQce-eHm8k` · AI Engineer · 2026-11-01 · q3 · practitioner · review · topics: mcp-and-tools, security-guardrails, data-engineering, context-engineering

Oracle's Jeff Smith on locking down agent access to databases: expose curated reports as MCP tools instead of raw NL-to-SQL, give agents a compact schema tool, and enforce identity-based row and column security inside the database.

- Techniques: Curated report catalogue exposed through two MCP tools; Three server modes: ad hoc SQL, custom tools and reports only, or both; Reveal report SQL to agents under a privileged scope; Action-grouped tools instead of single-purpose tools; Compressed deterministic schema-info tool; Generate schema annotations from enterprise documents; Identity-driven row and column filtering at the database; Diagnose production performance on a read-only standby
- Tools: Oracle AI Database, Oracle MCP server, MCP (Model Context Protocol), MCP apps (spec feature, speaker says added to the spec in July; Oracle plans a GUI for later this year), Claude, Codex, Gemini, LangChain, Azure Entra ID (spoken as 'Azure IntraID'), Oracle Data Guard, AWR (Automatic Workload Repository, Oracle performance report), Confluence

## [78% Wanted This AI Feature. Almost Nobody Used It - Supriya Subudhi, Bumble](../videos/CvmZtAPmAW4.md)
`CvmZtAPmAW4` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · topics: evals, product-ux, token-cost-efficiency, governance-compliance

Bumble's Supriya Subudhi argues that a positive A/B test is only the start for AI features, and lays out five checks: real adoption, tail-of-distribution outputs, cost versus benefit, model cost-quality tradeoffs, and legal market readiness.

- Techniques: Adoption-first AI feature rollout; Segment-level eval review over averages; Guardrails on advice scope; Eval-driven model and prompt selection under a cost budget; Write down the business reason for each AI feature; Regulatory check before building
- Tools: Meta Muse AI (mentioned as an example of a US/Canada-only launch), Amazon AI shopping assistant (mentioned as an example), Spotify AI DJ (mentioned as an example)

## [How to Decide What Your AI Agent Should Remember - Wojciech Pluta, Oracle](../videos/qq2Hm4XNRgI.md)
`qq2Hm4XNRgI` · AI Engineer · 2026-10-31 · q2 · intro · talk · topics: memory, context-engineering, agent-architecture, security-guardrails

Oracle's Wojciech Pluta argues agent memory is a write path that needs a promotion gate with provenance, scoped memory tiers, and per-turn context cards. Vendor talk with a demo.

- Techniques: Memory promotion gate; Provenance plus supersede, not overwrite; Three-tier memory scoping; Per-turn context card; Enforce user isolation in the database layer
- Tools: Oracle AI Database, Oracle agent memory package (named as an early-year release; no version given)

## [When Running Your Own AI Models Beats Paying for APIs - Steven Latré, imec](../videos/9-Y_oS9OBLc.md)
`9-Y_oS9OBLc` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · topics: infra-cost-scaling, inference-serving, token-cost-efficiency, local-ai

imec's AI lead benchmarks coding agents on open-weight models vs. APIs and finds that concurrency, GPU utilization and harness choice, not just accuracy, decide when self-hosting pays off.

- Techniques: GPU-utilization break-even check for API vs self-host; Concurrency ramp test on a single inference box; Task-level benchmark grid across harness, model and hardware; Measure harness token output and wall time on a paid GPU; Map model choice to hardware tiers
- Tools: Codex, Pi (transcribed as 'Py'), Claude Code, SWE-Bench Pro, Qwen, DeepSeek, GLM, Kimi K3, Claude Opus (mentioned as a reference point), NVIDIA B200-class GPU (transcribed as 'A times B 200')

## [Your AI Agent Starts Every Session Like a New Hire - Killian Carlsen-Phelan, Sonar](../videos/8vDzncmzxyg.md)
`8vDzncmzxyg` · AI Engineer · 2026-10-31 · q2 · practitioner · talk · topics: coding-agents, testing-verification, context-engineering, security-guardrails

Sonar pitches Vortex, a plugin that gives coding agents project context before they write and runs deterministic checks on every edit, so issues are caught before PR review.

- Techniques: Pre-write context retrieval from a verifier; Per-edit plus end-of-turn verification hooks; Enforce on changed lines only, surface the rest; Explicit-permission rule for sensitive resources; Deterministic layer between AI reviews
- Tools: Sonar Vortex (Sonar's agent plugin, named in the talk), SonarQube (static analysis, CI scan, data-flow and security analysis), Sonar CLI and MCP clients, Claude Code, Codex, Antigravity, Guitar (Sonar's AI reviewer, named in the captions; the speaker did not cover it), Java (language guidelines used in the demo)

## [Voice AI Where One Wrong Question Breaks the Rules - Shiv Indap, Upstart & Brooke Hopkins, Coval](../videos/3osCbSufv8g.md)
`3osCbSufv8g` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · topics: evals, voice-multimodal, governance-compliance, observability

Coval and Upstart walk through a regulated voice-agent (lending verification calls) eval loop: human review, judge calibration, failure routing, and simulation before release.

- Techniques: Judge-human calibration loop; Structured human review queues; Clustering and anomaly detection for unknown failure modes; Failure-to-owner routing; Voice simulation before release; Feature-flagged agent changes with named approvers
- Tools: Coval (voice-agent evaluation and simulation platform), Google Sheets (initial manual review tracking), LLM-as-judge, RL pipelines and fine-tuned LLMs (mentioned as options for self-healing, not shown)

## [Your Agent Just Paid for Nothing: 6 Attacks on x402 Payments - Ishween Kaur, SoFi](../videos/YU1uD_YkpjU.md)
`YU1uD_YkpjU` · AI Engineer · 2026-10-30 · q3 · practitioner · talk · topics: security-guardrails, governance-compliance, observability

Ishveen Kaur (SoFi) walks through six ways an autonomous agent can lose money on x402 machine payments, with guards, a probation-list pattern, and a trace-one-payment-ID method for finding them.

- Techniques: Compare listed price against 402 quoted price, network and wallet before paying; Shared payment-number ledger on the seller side; Buyer retries reuse one payment number; Choose release timing by data cost; Paywall test across all endpoints and no-store caching for paid output; Allow list, block list and probation list for discovered sellers; Per-plan call cap against prompt injection; Single-ID tracing with a 20-25 case dataset
- Tools: x402 (HTTP 402 payment protocol), Llama 3.2 (agent model in the prompt-injection demo), Base Sepolia testnet (auto-caption reads 'Bayes Cipolia'; probably Base Sepolia), x402.org facilitator (testnet), Bazaar (x402 seller directory), Ethereum and Solana (named as alternative chains), Cloudflare pay-per-crawl (cited as a parallel)

## [Why Humans Can't Keep Up With AI-Written Code - Tariq Shaukat, Sonar](../videos/LQW_Wvqhp04.md)
`LQW_Wvqhp04` · AI Engineer · 2026-10-30 · q3 · practitioner · talk · topics: software-factory, testing-verification, evals, governance-compliance

Vendor talk arguing AI-generated code makes volume cheap but confidence scarce, so software factories need intent, guide rails, independent verification and evidence, with LLM judges treated as unreliable.

- Techniques: Code confidence formula as a factory checklist; Guide rails over guard rails; Deterministic plus agentic verification mix; Measure judge stability before trusting an LLM judge; Model per-step reliability to pick task length
- Tools: SonarQube, Sonar Vortex, Claude Mythos preview (named as the model in the Meter study, version as stated in talk)

## [Why AI Won't Replace Stock Pickers - Jack Woodruff, Candlestick & Vinoo Ganesh, Kepler](../videos/y2dyD6slKxE.md)
`y2dyD6slKxE` · AI Engineer · 2026-10-30 · q2 · intro · interview · topics: governance-compliance, data-engineering, enterprise-adoption

Fireside chat between a hedge fund founder and a Kepler co-founder on how AI changes stock picking: AI raises the baseline, auditability is the trust gate, and edge comes from divergent views and idea velocity.

- Techniques: Audit-first verification of model-produced numbers; AI as attention triage for human research; Automate prep, reinvest time in differentiated work

## [The Cheaper AI Model That Costs You More - Rayan Krishnan, Vals AI](../videos/rWtbOgl5FTU.md)
`rWtbOgl5FTU` · AI Engineer · 2026-10-30 · q4 · practitioner · talk · topics: evals, token-cost-efficiency, enterprise-adoption, models-research

Vals AI's Rayan Krishnan argues model cards hide a "jagged frontier" by task and metric, and that cost-per-task evals, real-work benchmarks and routing can cut enterprise AI spend without losing output.

- Techniques: Pareto plotting of cost per task vs performance; Report partial credit and fully-correct rate together; Build evals from historical work (PR and issue replay); Sandbox hygiene against reward hacking; Resumable eval infrastructure; Task-level usage-limit right-sizing
- Tools: Vals AI benchmarks (Vals Index, Finance Agent benchmark, Excel modeling / LBO, tax agent), Vals Smith (internal eval-driven coding product), Opus 5.5 (Anthropic), Fable 5.1, Sonnet, GPT 5.6 Sol, Kimi K3

## [Catch the Bugs Your Code Review Misses - Killian Carlsen-Phelan & Taylor Luttrell-Williams, Sonar](../videos/wP3P89YB9fA.md)
`wP3P89YB9fA` · AI Engineer · 2026-10-30 · q2 · practitioner · review · topics: pr-code-review, testing-verification, context-engineering

Sonar's hands-on workshop for Guitar, a PR-level verification agent that reviews agent-written code, diagnoses CI failures, auto-fixes and auto-merges. Vendor pitch with a usable setup walkthrough.

- Techniques: Install Guitar as a GitHub app and connect a repo; Fork the workshop repo with all branches and enable Actions; Open PRs against your own fork, not upstream; Apply Guitar fixes; Steer reviews with project context in .guitar/review; Write conditional rules in .guitar/rules; Turn on auto-merge safely with a branch ruleset
- Tools: Guitar (Sonar's code change verification agent, GitHub app, app.guitar.ai), SonarQube (called SonarCube in the transcript, static analysis), GitHub (PRs, Actions, branch rulesets, auto-merge), Jira, Linear, Slack, MCP (Guitar supports MCP connectivity for custom context), Python (sample Box Office ticketing app, orders.py, check-in.py)

## [We Trust AI Agents That Break Every Day - Shy Ruparel, Temporal](../videos/mJ7q8CuVmbw.md)
`mJ7q8CuVmbw` · AI Engineer · 2026-10-29 · q3 · practitioner · review · topics: agent-architecture, observability, token-cost-efficiency, enterprise-adoption

Temporal developer advocate Shy Ruparel argues agent reliability is a state and recovery problem, not a model problem, and demos durable execution resuming a crashed payout workflow with a human approval.

- Techniques: Durable workflow with deterministic orchestration and recorded activities; Human approval as a signal with a long timer; Declare the retry policy once, not in loops; Degrade the AI step, not the transaction; One event history for both debugging and replay
- Tools: Temporal, Qwen (run locally as a 36B and a 9B model, per auto-captions), OpenAI Codex (cited as running on Temporal), Replit Agent (cited as running on Temporal), Keycard (talk referenced, not described)

## [Why a One-Line Change Can Break Your Whole Stack - Cole Gannaway, Qodo](../videos/YqxpPI7YUjE.md)
`YqxpPI7YUjE` · AI Engineer · 2026-10-29 · q2 · intro · talk · topics: pr-code-review, context-engineering, multi-agent, software-factory

A Qodo solutions engineer argues PR review is the bottleneck in AI software factories and needs cross-repo blast-radius context, independent reviewers and rules learned from past reviews. Mostly a product demo.

- Techniques: Blast-radius-aware review over a software graph; Rules learned from review comments; Pre-generation context injection; Independent, varied reviewers; Mid-run review checkpoints via skill; Ticket-linked PR review
- Tools: Qodo (spoken as Kodo), Jira, Linear, MCP servers, Claude Code, Anthropic models, OpenAI models, Bitwarden (example repo, open source password manager), CLI

## [AI That Hunts Logic Bugs Before Attackers Do - Taylor Luttrell-Williams, Sonar](../videos/UW8Qkk7MG8A.md)
`UW8Qkk7MG8A` · AI Engineer · 2026-10-29 · q2 · intro · demo · topics: security-guardrails, pr-code-review, agent-architecture

Sonar's SonarQube Hunter Agent: an on-demand/scheduled AI security agent that maps a repo, runs three specialized issue-class agents with adversarial validation and noise gates, and surfaces logic/authz flaws (IDOR, broken access control, business logic, auth/session) in SonarQube's normal issue list.

- Techniques: Multi-agent security scan with validation gates; Layered verification: SAST plus logic-level agent; Triage workflow for AI-raised issues
- Tools: SonarQube Hunter Agent, SonarQube (Cloud and Server), SonarQube remediation agent, SAST, SCA, OpenAI Daybreak Cyber Partner Program (frontier cybersecurity models)

## [How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut](../videos/Ok6QdZHCcI8.md)
`Ok6QdZHCcI8` · AI Engineer · 2026-10-29 · q4 · practitioner · talk · topics: token-cost-efficiency, inference-serving, sandboxing-execution, governance-compliance

Revolut's AI ops lead explains how self-hosting GLM on dedicated GPUs cut its coding-AI invoice to about a tenth, and which serving metrics and tuning levers mattered.

- Techniques: Lead-time-first AI adoption metric; Latency-led GPU capacity planning; Serving parameter sweep; Local router for multimodal fallback; Harness-agnostic OpenAI-compatible endpoint; Sandbox with per-command allow/deny rules; Compliance and telemetry baseline
- Tools: GLM (GLM 5.1 and a later GLM 5.x model; caption reads 'GLM 5.3'), GLM-5 Flash (caption reads 'Glam5G Flash'), Gemini, Claude Code, Codex, Codex app, OpenCode (caption reads 'OpenCodex'), Anthropic API, OpenAI API, OpenAI Responses API (compatible endpoints), NVIDIA B200 GPUs, Blackwell GPUs

## [How Anthropic Merges 30,000 Code Changes a Day - Manish Kapur, Sonar & Addy Osmani, Anthropic](../videos/AnsXWH2_EBU.md)
`AnsXWH2_EBU` · AI Engineer · 2026-10-29 · q3 · practitioner · panel · topics: pr-code-review, testing-verification, software-factory, governance-compliance

Sonar and Anthropic discuss verification as the bottleneck for agent-written code, covering layered checks, codified taste in CLAUDE.md/AGENTS.md, labeling agent PRs and the lights-on vs dark software factory spectrum.

- Techniques: Verification-first agent loop with a first-pass reviewer; Codify taste in CLAUDE.md or AGENTS.md for review agents; Require verification evidence before human review; Layered verification stack; Label agent-authored PRs and keep a named human owner; Agent guide rails and permission control
- Tools: Claude Code (called 'Cloud Code' in the transcript), Claude (claude.ai web product), Opus 5.5 (Anthropic model, named as a reference point for model quality), Anthropic code review product (named only as a product Anthropic offers), CircleCI (cited statistic), Sonar (verification vendor; survey and product referenced), CLAUDE.md / AGENTS.md (agent instruction files)

## [Stop Guessing Your vLLM Config: Benchmarking LLMs on Runpod - Chris Vela, Runpod](../videos/P_0_Th_ZzIg.md)
`P_0_Th_ZzIg` · AI Engineer · 2026-10-28 · q2 · practitioner · review · topics: inference-serving, infra-cost-scaling, evals

RunPod's Chris Vela argues for benchmarking vLLM configs on GPU pods across concurrency levels before production, and previews an unreleased BenchPod template. Vendor pitch with some reusable method.

- Techniques: Config-sweep benchmarking before production; Tune max batched tokens for long generations; Pin vLLM and CUDA to what the model needs; Agent-readable benchmark and health API; Model choice by task size and team size
- Tools: RunPod (GPU pods, serverless, storage volumes, Docker images), vLLM (OpenAI-compatible server, YAML config, nightly builds), BenchPod (unreleased RunPod template built on vLLM, with FastAPI, a watchdog and benchmark metrics), Kimi K3, DeepSeek, GLM, Qwen 3.8 (transcribed as 'Quinn 3.8'), Docker, NVIDIA B300, NVIDIA H200, CUDA 12.8 and 13.0, Claude (mentioned as the service many internal users are moving off)

## [Exploits Now Beat Patches: Open Source Security in the AI Era - Patrick Smyth, Chainguard](../videos/xZX3pmaB8Hk.md)
`xZX3pmaB8Hk` · AI Engineer · 2026-10-28 · q3 · practitioner · review · topics: security-guardrails, dev-tools, skills-self-improvement

Chainguard's Patrick Smyth argues frontier AI has made exploits beat patches: cooldowns, signed artifacts, tiered SLAs, minimal rebuilt images and vetted agent skills, wrapped in a vendor pitch.

- Techniques: Package cooldown period; Sign and verify every artifact; Build dependencies from clean source; Severity-tiered remediation SLA; Minimal, frequently rebuilt base images; Treat CI/CD as an attack surface; Vet agent skills before use; Hardware-backed developer identity
- Tools: Chainguard (vendor), Wolfi (Chainguard's rolling Linux distro), Chainguard Libraries (build-from-source packages), Chainguard Actions (hardened CI/CD actions), Chainguard agent skills (hardened third-party skills), Sigstore, SLSA (captioned 'Salsa'), Mandiant mTrends report (captioned 'Mandia'), Trivy (scanner, captioned 'Trivi', attacked in the supply chain incident), Grype (captioned 'Gripe', scanner named as an example), LiteLLM (captioned 'LightedLM', described as an agent router), Axios (npm package, compromised)

## [We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI](../videos/YIhvrvHtonk.md)
`YIhvrvHtonk` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · topics: agent-architecture, context-engineering, memory, evals

Arize's PM on two years of shipping Alex, its in-product agent: keep the loop, plan, stop rule and memory in harness code, use small capped memory files, and treat production traces as regression tests.

- Techniques: Render the plan into the harness on every call; Explicit finish call as a harness gate; Tool results as pointers, not inline content; One small capped markdown memory file per user; Single model call instead of a loop for narrow features; Production sessions as living regression fixtures; Trace-reading agent for silent failures
- Tools: Arize AX, Alex (Arize in-product agent), Signal (Arize trace-reading agent), Sonnet 4.5 (auto-caption 'Sonic 4.5'), jq, Arize experiments

## [Stop Giving Your Agent Tools. Give It a Sandbox - Mikyo King, Arize AI](../videos/dAoOYFx7ZYw.md)
`dAoOYFx7ZYw` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · topics: sandboxing-execution, mcp-and-tools, token-cost-efficiency, evals

Arize's Mikyo King argues agents should get a search tool plus a code sandbox instead of a large tool catalog, reporting 43% fewer tokens and 31% lower cost in their own Harbor evals, while listing open problems such as secrets, permissions, and durability.

- Techniques: Search-then-execute tool access (code mode); Bash plus CLI as the first sandbox; Hoist REST CRUD endpoints into a sandbox language; SQL as an aggregate-query escape hatch; Keep secrets out of the model's context; Signed handoff for binary artifacts; Sandboxed, multi-trial agent evals with pass@k; Trajectory-driven instruction hill-climbing
- Tools: Arize Phoenix, Harbor Framework, Claude Code, MCP, Bash, Python sandbox, SQL (text-to-SQL), SWE-bench, PyDurable (named in the talk; caption may be garbled)

## [What a $900M Bank Error Teaches Us About AI Agents - John Feminella, Two Sigma](../videos/iniryju23Sk.md)
`iniryju23Sk` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · topics: governance-compliance, security-guardrails, evals

Two Sigma's John Feminella ties a 2020 bank loan-payment error to AI agent governance and lays out five composable controls: registry, risk scoring, declared guardrails, shared evals, tiered approvals.

- Techniques: Tiered approval routing; Registry auto-registration through approved frameworks; Declared-capability manifest enforced at init; Risk-based review routing; Platform-owned shared eval harness
- Tools: FlexCube (internal bank processing software, as named in the talk), Claude Code, Pi (open-ended coding agent, as named in the talk), OpenClaw (named as 'open claw' in the talk)

## [Who Is Making This Request? Agent Auth 101 - Kamil Potrec, Keycard](../videos/58ulJViGFgU.md)
`58ulJViGFgU` · AI Engineer · 2026-10-28 · q3 · practitioner · talk · topics: security-guardrails, mcp-and-tools, governance-compliance

Keycard's Kamil Potrec argues agents need their own authenticated identities, short-lived scoped credentials via OAuth-style delegation, and a gateway that injects credentials outside the agent's reach, so every request is attributable and revocable.

- Tools: Keycard (control plane, client and service SDKs, gateway), MCP (Model Context Protocol), OAuth, agentbaseline.org (software factory reference implementation, named by the speaker)

## [How a Trading Firm Ships New AI Models the Same Day - Noyan Tokgozoglu, Optiver](../videos/aGIUg8zKI8A.md)
`aGIUg8zKI8A` · AI Engineer · 2026-10-27 · q4 · practitioner · talk · topics: enterprise-adoption, token-cost-efficiency, evals, multi-agent

Optiver's head of AI engineering on running an AI platform where every decision shows up in P&L within hours: same-day model adoption, token-spend control, and narrowly scoped agents on a shared gateway.

- Techniques: Golden-set benchmarking on day zero; Gateway-first model onboarding checklist; Replace default MCP context with tool search and CLI wrappers; Analyze cache invalidation before tuning cache TTLs; Move reference material out of the system prompt into retrieval; Per-team alerts and self-managed spend limits; Point-in-time tool snapshots with per-invocation confidence; Scope agents narrowly and version them; Ship internal portal with contributions via PRs
- Tools: Claude Code (referenced as the "cloud code" moment in the auto-captions), Codex (OpenAI coding agent; the speaker says it lacked self-hosted managed agents until recently), MCP (Model Context Protocol) servers and MCP tool search, OpenTelemetry (OTEL) logging, Slack client, Internal inference gateway, agent gateway, agent workbench, meta-harness layer, and web portal (Optiver in-house)

## [Why Are We Still Governing AI Agents Like Software? - Tim Tyler, Gravitee](../videos/h8jgniNJcbQ.md)
`h8jgniNJcbQ` · AI Engineer · 2026-10-27 · q3 · intro · talk · topics: governance-compliance, security-guardrails, enterprise-adoption

Tim Tyler (Gravitee) argues AI agents should be governed like employees: a unique identity, a named human sponsor, a scoped role and authority, and tiered recourse, with rules as a deterministic floor and intents judged probabilistically.

- Techniques: Three-stage agent accountability model; Scope-lineage delegation check; Deterministic floor plus probabilistic scorecard; Confidence-tiered action ladder; Guardian agents at machine speed
- Tools: Gravitee (AI agent management), Claude (transcribed as 'Clyde'), MCP (Model Context Protocol), FGA policies (fine-grained authorization, generic reference), Mobile device management (MDM, analogy only), Agent accountability framework (agentaccountabilityframework.org)

## [300 Agents, 60 People: How We Secured Our Own AI Agents - Aiden Sochowski, Runlayer](../videos/BgLdvF7Qkh8.md)
`BgLdvF7Qkh8` · AI Engineer · 2026-10-27 · q3 · practitioner · talk · topics: security-guardrails, governance-compliance, observability, token-cost-efficiency

Runlayer's founding engineer describes how a 50-60 person company monitored its own 300+ daily agents through a gateway, then used the session data for security (intent drift, over-permissioning, cross-agent contamination) and for cost control (erroring MCP tools, model tier jumps).

- Techniques: Gateway-first agent telemetry; Per-tool-call intent classifier; Baseline-and-flag on tool-use history; Inbound and outbound content policies; Tight write scoping per agent; MCP error and retry monitoring with rate limits; Budgets and default model tiers
- Tools: MCP (Model Context Protocol), Claude Code (captioned as 'cloud code'), Opus (Claude model, mentioned as hard to prompt-inject), Runlayer (the speaker's company; product is a gateway, not named in detail)

## [How to Test Your Agents on Real Tasks With Harbor - Xander Song, Arize AI](../videos/kRJjSOYqW0I.md)
`kRJjSOYqW0I` · AI Engineer · 2026-10-27 · q4 · practitioner · talk · topics: testing-verification, evals, observability, coding-agents

Xander Song (Arize) introduces Harbor, an open-source framework for testing agents on real tasks in fresh sandboxes, scored by side-effect verifiers, and shows how his team used it to tune a prompt for SQL over GraphQL.

- Techniques: Harbor task layout; Oracle-first validation; Keep verifiers outside the agent's view; Synthetic task and oracle generation; Before/after prompt A/B in a fixed harness; Read-only SQL tool for aggregates; Single-node app snapshot in Docker; One-turn skill-triggering test
- Tools: Harbor, Docker, Arize Phoenix, OpenInference, OpenTelemetry, OTLP, ATIF (Agent Trajectory Interchange Format), Daytona, Modal, E2B, SQLite, Postgres

## [Agents That Self Improve While You Sleep - Fuad Ali, Arize AI](../videos/UGuNt2_Oz8s.md)
`UGuNt2_Oz8s` · AI Engineer · 2026-10-27 · q3 · practitioner · workshop · topics: evals, observability, skills-self-improvement, pr-code-review

A vendor-led workshop on closing an agent self-improvement loop: scheduled trace review, failure datasets, evals, replay experiments, and human checkpoints at the high-leverage points.

- Techniques: Trace-to-fixture pipeline; Trajectory-level LLM-judge eval; Cheap-first evaluator stack; Replay-based fix validation; Confidence-threshold human routing; Session-level eval signals; Stop criteria for eval depth
- Tools: Arize AX (tracing and evals platform), AX CLI, Arize Signal (always-on trace-review agent), Arize Alex (in-house agent), Phoenix (mentioned, not demonstrated), Arize managed sandboxes, GitHub, Codex, Cursor, Claude Code, OpenCode, Modal

## [Can Your AI Analyst Keep a Secret? - Aaron Linsky, Bridgewater & Nikhil Benesch, turbopuffer](../videos/u_jvuCjuvEk.md)
`u_jvuCjuvEk` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · topics: rag-retrieval, security-guardrails, infra-cost-scaling

Bridgewater and turbopuffer explain how to run vector search over 100M documents with per-document permissions, using cluster-pruned "native filtering" to keep recall and latency acceptable.

- Techniques: Cluster-pruned native filtering for ACL-restricted vector search; Avoid fixed top-K then post-filter for access control; Express permissions as filter predicates on documents; Napkin math before choosing an index; Object-storage-first tiering for large, bursty corpora
- Tools: turbopuffer, Amazon S3, Google Cloud Storage, Azure Blob Storage, Bridgewater DeLorean (internal bitemporal macro time-series database, mentioned), Bridgewater Vault (internal unstructured document store, about 100M docs)

## [What Does an AI Engineer Do Now? - Aparna Dhinakaran, Arize AI](../videos/ImnZ7s68jw8.md)
`ImnZ7s68jw8` · AI Engineer · 2026-10-26 · q3 · practitioner · talk · topics: software-factory, observability, evals, agent-architecture

Arize's Aparna Dhinakaran argues the AI engineer's job is now building the build-eval-ship-monitor-improve loop itself, with always-on agents consuming telemetry and evals aligned to human judgment.

- Techniques: Telemetry-triggered always-on agent sweep; Issue memory across agent runs; Sandbox-per-run with single proxy egress; Durable agent resume; Harness and model abstraction with per-run evaluation; Evaluator alignment against golden data; Offline plus online evals on the same definitions; Trace the coding agents too
- Tools: Arize Signal, Arize Evaluator, Claude Code, Cursor, Codex, Anthropic model family (multiple models, unnamed)

## [Build Your Own Team of Managed Agents - Jack Wotherspoon, Google DeepMind](../videos/Y_p3y6zP5QE.md)
`Y_p3y6zP5QE` · AI Engineer · 2026-10-26 · q3 · intro · talk · topics: sandboxing-execution, multi-agent, agent-architecture, mcp-and-tools

Google DeepMind's Jack Wotherspoon demos Gemini managed agents: a cloud sandbox, harness and API in one call, with reusable environments for multi-agent handoff, credential-injecting proxies, and scheduled triggers.

- Techniques: Single-call managed agent; Chain turns with the interaction ID; Hand off work between agents via a shared environment ID; Narrow single-purpose agents with fan-out; Placeholder credentials with egress injection; Scheduled and webhook-triggered runs
- Tools: Gemini API Interactions API, Gemini managed agents, Antigravity harness, Gemini Flash, Gemini 4 Argonne (name as spoken in the talk), Google Search (built-in tool), remote MCP servers, agents.md, agent skills, GitHub, Google Drive, Google Docs

## [How to Build Voice Agents That Don't Fall Apart When You Interrupt - Jesse Hall, LiveKit](../videos/OmyqelTwpOo.md)
`OmyqelTwpOo` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · topics: voice-multimodal, evals, inference-serving

LiveKit's Jesse Hall argues voice agents must be evaluated as whole conversations: measure time-to-first-audio and time-to-first-sentence, use non-blocking tool calls, use audio-aware turn detection, and benchmark full stacks with simulated callers.

- Techniques: Time-to-first-audio and time-to-first-sentence instrumentation; Non-blocking (async) tool calls in a voice agent; Audio-aware turn detection; Full-stack scenario simulation with identical replay; Regression scenarios from production failures; Financial voice-agent guardrail checklist
- Tools: LiveKit (open-source real-time agent framework and infrastructure), LiveKit turn detector (audio + transcript end-of-turn model), LiveKit inference (model serving tuned for voice; speaker says it is model agnostic), Gemma 4 31B (auto-caption reads 'Gemma 431B'; top LLM on the hotel agent benchmark), ChatGPT advanced voice mode (cited as using LiveKit)

## [How to Build an AI Code Review Agent - Daksh Gupta, Greptile](../videos/4UtrRVtUN_g.md)
`4UtrRVtUN_g` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · topics: pr-code-review, context-engineering, token-cost-efficiency, testing-verification

Greptile co-founder Daksh Gupta walks through building a production AI code review agent: sandboxed test runs, historical bug catalogs, model inversion, a living code wiki for context, and tiered model routing to cut per-PR cost.

- Techniques: Prompt the reviewer for a catalog of bug types, not generic review; Historical-PR regression eval for the review agent; Model inversion for reviews; Codebase knowledge base indexed by subsystem; Dependency-rich sandbox with computer-use end-to-end tests; Tiered model routing across review subtasks; Model-agnostic harness for the review agent
- Tools: Firecracker, OpenCode, Pi, Codex, Claude Code, GitHub review API, GitHub, GitLab, Jira, Linear, Confluence, Notion

## [How to Write Your First AI Eval - SallyAnn DeLucia, Arize AI](../videos/gv4w23xYj-0.md)
`gv4w23xYj-0` · AI Engineer · 2026-10-26 · q3 · practitioner · workshop · topics: evals, observability, multi-agent

A hands-on workshop on writing a first LLM-as-judge eval for an agent: why vibe checks fail, how traces feed evals, how to write concrete criteria, and how to build and iterate a judge in a prompt playground.

- Techniques: Six-part criteria template; Judge prompt structure; Variable mapping for judge inputs; Span-level dataset selection; Iterate the judge in a prompt playground against a dataset; Alignment against human labels; Online evals on incoming traces; Decision-model comparison; Instrumentation: auto, manual, or hybrid
- Tools: Arize AI (Arize AX platform, captioned 'Arise' or 'AX'), Alex (Arize's in-platform AI agent that can run playgrounds and iterate on prompts), Signal (Arize's managed agent that reads traces, finds issues and proposes fixes), OpenInference (Arize's tracing package with auto-instrumentors for agent frameworks), OpenAI decision model API (mentioned as released the week before the talk), Anthropic, OpenAI and Gemini provider API keys (configured under AI providers in settings), ROUGE and BLEU (named as code-based eval metrics), Notion one-pager (workshop instructions)

## [How Bridgewater Turned 100 Million Documents Into an Edge - Sam Green & Aaron Linsky, Bridgewater](../videos/CLve4Nx_RwI.md)
`CLve4Nx_RwI` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · topics: rag-retrieval, enterprise-adoption, product-ux, data-engineering

Bridgewater's Applied AI team describes the Vault, a governed corpus of 100M+ unstructured documents, and the lessons from making it useful to both human investors and agents: separate design for each reader, benchmark-driven search, and feeding agent-human synthesis back into the corpus.

- Techniques: Hand-labelled retrieval benchmark before tuning; Cluster-aware native filtering in the vector store; Infer a time window from the question and scope retrieval to it; Separate human and agent retrieval design; Migrate existing user habits into the new tool first; Write synthesis back into the corpus
- Tools: Turbopuffer (vector database, native filtering), Bridgewater Vault (internal unstructured data platform), Aya (internal artificial investment associate), Pocket Analyst (internal AI analyst), Researcher (internal, next-generation analyst), Forecaster (internal, custom model plus foundation models), Slack, IDE integration, CLI for agents, phone app, enterprise chat client (unnamed)

## [How to Build Financial Agents That Work Across the Web - Jay Sahnan & Arik Bird, Browserbase](../videos/DZ24Xbm9Joc.md)
`DZ24Xbm9Joc` · AI Engineer · 2026-10-25 · q2 · practitioner · review · topics: voice-multimodal, sandboxing-execution, data-engineering, enterprise-adoption

Browserbase engineers pitch hosted, forked "verified" Chromium plus the open-source Stagehand SDK for running browser agents at scale on finance portals, with Ramp, Bill and Stripe as case studies.

- Techniques: Accessibility-tree page compaction before the LLM call; Hybrid deterministic plus natural-language browser control; Observe, act, extract as three separate primitives; Schema-first extraction with Zod; Single code path fanned out across many sites; Keep browser processes alive between tasks; Run the agent-side browser controller next to the browser; Copy-prompt onboarding for coding agents
- Tools: Browserbase (hosted browser infrastructure), Stagehand (open-source browser-control SDK built on Playwright), Playwright, Selenium, BeautifulSoup, Chromium (forked; Browserbase's verified build), Chrome, Zod, ngrok (used to share the demo), EC2 (named as the data-center example)

## [Do Not Let Models Invent Numbers - Vinoo Ganesh, Kepler](../videos/dZgA6btnb_s.md)
`dZgA6btnb_s` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · topics: rag-retrieval, data-engineering, security-guardrails

Kepler's CEO explains how its finance research platform stops LLMs from inventing numbers: models cite pre-registered SEC facts, deterministic code does the math, and any unverifiable number is stripped.

- Techniques: Cite-don't-write with post-filter; Typed fact registry; Search wide, then re-rank in stages; Per-hit document authorisation; Keep conflicting sources and de-conflict; Measure recall and idempotency as guarantees
- Tools: Kepler (finance research platform), Turbopuffer (vector and BM25 search, namespaces), Zero Entropy embeddings (as stated; 1280 dimensions), Postgres (per-document authorisation), Cross-encoder re-ranker (model not named), XBRL (structured filings data, cited as ~10% incorrect), SEC filings: 10-K, 10-Q, 8-K, S-1, investor presentations, earnings call transcripts, Claude and ChatGPT (used as baseline in evals), Gemini 4 (mentioned, not evaluated)

## [Your Agent Fix Just Broke Something Else - Sofia Jakovcevic, Arize AI](../videos/v5tm5EAzsAs.md)
`v5tm5EAzsAs` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · topics: evals, observability, testing-verification, multi-agent

A five-step regression loop for agents built on production traces, evaluators and CI gates, so a prompt or policy change is judged on numbers before it merges. Vendor-led demo of Arize.

- Techniques: Five-step trace-driven regression loop; Four-bucket dataset composition; LLM-as-judge plus code evaluators; Side-by-side prompt versions in a playground; Agent playground against a remote agent; Run experiments from coding agents through skills; CI gate on experiment results
- Tools: Arize (Arize AI observability backend and platform, incl. prompt hub, prompt playground, agent playground, experiments, datasets), Arize agent skills repository (public, for coding agents), GitHub Actions (CI example), Arize SDK / REST / CLI (run experiment), LLM-as-judge evaluators (pre-built: hallucination, user frustration, security checks; custom evaluators supported)

## [AI Writes the Code. So What's Left for Engineers? - Laurie Voss, Arize AI](../videos/kspZP5BgkEU.md)
`kspZP5BgkEU` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · topics: context-engineering, pr-code-review, product-ux, evals

Laurie Voss (Arize AI) argues coding agents have made code writing nearly free, so the bottleneck moves to code review, ops and security, and ultimately to defining what "good" means, which makes "product engineers" the lasting role.

- Techniques: Theory-of-constraints bottleneck mapping; Review only high blast-radius code; Automatic verification for cheap-to-check work; Turn reviewer feedback into rules; Mergeability benchmark instead of test pass rate; Measure outcomes, not output volume
- Tools: Claude Code, GitHub Copilot, Cognition Devin, Cursor Bugbot, OpenAI Codex, Claude, Pragmatic Engineer newsletter, Arize AI

## [Why Frontier Models Fail as Buy-Side Analysts - Janie Gu, Google DeepMind & Suyeol Yun, LinqAlpha](../videos/aVbRSIQO2dE.md)
`aVbRSIQO2dE` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · topics: evals, sandboxing-execution, observability, models-research

Google DeepMind's Kaggle team and LinkAlpha present why most agent benchmarks are unreliable, what Kaggle found reproducing 65 of them, and MandateBench, a buy-side analyst benchmark graded on reasoning paths.

- Techniques: Reproduce, then read every trace before trusting a score; Separate the agent under test from the grader; Log every model call and keep traces open; Measure variance with repeated runs; Pin reasoning effort explicitly for head-to-head comparisons; Rubric-based grading of a reasoning graph; What-if perturbation of key assumptions; Reconcile conflicting source figures explicitly
- Tools: Kaggle, Kaggle Benchmarks, Google DeepMind models (as evaluated), MandateBench, HuggingFace (named as a place models searched for answers), Reddit and StackOverflow (named as places models searched for answers), Heijen's Code to Video Bench (captioned name; launched last week per speaker), Octava, Quadrillion, Rehearsals (partner names as captioned)

## [Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management](../videos/ZMZlAn6Pyfg.md)
`ZMZlAn6Pyfg` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · topics: governance-compliance, enterprise-adoption, evals, mcp-and-tools

A hedge-fund head of AI explains how Contour measures AI ROI: live A/B tests of analyst workflows, process metrics over slow P&L, cost per useful insight, and connector-maintenance time counted as a cost.

- Techniques: Live A/B workflow capture; Agent-synthesized vs analyst-synthesized expert calls; Cost per useful insight; Idea-resurfacing agent; Alt-data via MCP or API connectors into agents; Connector-maintenance time as an ROI line item
- Tools: AlphaSense, Yipit, Rogo, Hebbia, Bloomberg, MCP, APIs (vendor data)

## [Real AI Agent Attacks and What Would Have Stopped Them — Andrey Rybka, Bloomberg](../videos/5O6jLtoeKrg.md)
`5O6jLtoeKrg` · AI Engineer · 2026-10-24 · q4 · practitioner · talk · topics: security-guardrails, sandboxing-execution, mcp-and-tools, agent-architecture

Bloomberg's Andrey Rybka walks through real agent security incidents (sandbox escape, CRM exfiltration, hidden-text injection, DNS leaks, a dropped production database) and maps each to layered controls: identity, input defense, deterministic tool brokers, default-deny egress, and budgets that halt.

- Techniques: Rule of two (capability gating for agent workflows); Deterministic invocation broker; Default-deny egress including DNS; One identity per agent, short-lived audience-bound tokens; Delayed package ingestion; Circuit breakers and halting budgets; Memory integrity and fresh-start policy; Security requirements in the spec
- Tools: MCP (Model Context Protocol) servers, OAuth, DNS, npm, NotebookLM (transcribed as 'Notebook Alarm'; likely NotebookLM), AWS accounts and GCP projects (as isolation analogies)

## [Why Compute Still Trades in Group Chats — Affaan Mustafa & Alejandro Soumah Fernandez, Jump Trading](../videos/GCse4OMzY8U.md)
`GCse4OMzY8U` · AI Engineer · 2026-10-24 · q3 · intro · talk · topics: infra-cost-scaling, token-cost-efficiency, governance-compliance

Jump Trading's compute leads explain how GPU capacity trades bilaterally over chats, why cheaper tokens still raise compute demand, and how prepayments and financing gate startup capacity.

- Techniques: Prepayment step-function capacity model; On-demand bridge versus financed prepayment comparison; Build-vs-rent by utilization curve; Decompose a quote into fungible and non-fungible parts; Risk-first structure selection
- Tools: H100, H200, B300, CoreWeave, Slack, Telegram, Bloomberg chat, ICE chat

## [Can AI Understand a Distressed Credit? - Harneet Kaur, Axim Intelligence](../videos/WOszaC1WWbQ.md)
`WOszaC1WWbQ` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · topics: evals, data-engineering, models-research

Founder of Axim Intelligence on testing whether LLMs can forecast distressed credit outcomes; models disagreed until a structured, layer-by-layer reasoning process made them converge, though no ground truth was shown.

- Techniques: Layer-by-layer benchmarking of an LLM analysis pipeline; Cross-model disagreement as a diagnostic; Structured reasoning scaffold to force convergence
- Tools: Opus (Opus 5.5, as named in transcript), Astra 6 (named in transcript; the model name may be an auto-caption error)

## [Buying GPUs Should Work Like Buying Stocks — Carmen Li, Compute Exchange](../videos/laQ8wMysnkk.md)
`laQ8wMysnkk` · AI Engineer · 2026-10-24 · q2 · intro · talk · topics: infra-cost-scaling, token-cost-efficiency, product-ux

Carmen Lee (Compute Exchange / Silicon Data) pitches a neutral GPU-procurement exchange and GPU term-structure and residual-value indices; useful market context, but mostly a company talk with few reusable engineering techniques.

- Techniques: Forward-curve reading from GPU rental indices; Discounted-cash-flow residual valuation of GPU servers; Neutral exchange model for compute procurement
- Tools: NVIDIA DGX, InferenceX, MLPerf, CME futures

## [Inside Arca's Long-Horizon Agents That Run the Business - Aman Singh, Arca](../videos/oP2WLFpMoDY.md)
`oP2WLFpMoDY` · AI Engineer · 2026-10-24 · q3 · practitioner · review · topics: agent-architecture, multi-agent, memory, enterprise-adoption

Arca, an AI-native financial services firm, explains how background agents own multi-day client work through a signal system, shared plan spaces, and human pull-ins.

- Techniques: Signal-driven wake-up with interest registration; Dual wake-up: event plus timed fallback; Treat UI mutations as first-class events; One shared workspace per goal with human pull-ins; Split state by horizon: memory for later, tasks for now; Turn colleagues' reasoning into eval cases; Steer by adding a goal

## [How OpenAI Built ChatGPT for Bankers and Analysts — Joseph Kim, OpenAI](../videos/opHmX7qClzE.md)
`opHmX7qClzE` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · topics: product-ux, mcp-and-tools, enterprise-adoption, models-research

OpenAI's Joseph Kim explains how ChatGPT for Financial Services was built on the plugin platform (MCP, skills, artifact tools), why finance lagged in AI use, and his 2027 bets on finance models and persistent agents.

- Techniques: Host and index licensed data yourself, expose it through MCP; Split tool/instruction layer from domain post-training; Firm templates for generated artifacts; Citation viewers for reviewable answers; Plan features around the usefulness threshold; Build on the plugin platform building blocks
- Tools: ChatGPT, ChatGPT plugin platform, MCP (Model Context Protocol), MCP apps, Skills, Codex, Codex desktop app, Excel, PowerPoint, GPT-4

## [A Bank Trained Its Own Foundation Model to Catch Fraud — Freddy Lecue, Wells Fargo](../videos/UB6hoWyh3B0.md)
`UB6hoWyh3B0` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · topics: data-engineering, models-research, enterprise-adoption

Wells Fargo built a ~1B-parameter transformer pre-trained from scratch on customer transaction data as a reusable backbone; it beat its production XGBoost fraud model on detection rate and false positives.

- Techniques: Transaction tokenization for tabular data; Raw-field representation instead of hand-engineered features; Decoder-only pre-training on a transaction sequence, then task fine-tuning; Scaling-law sizing with empirical correction; Standard large-scale training recipe; Benchmark against the production GBDT on business metrics
- Tools: XGBoost (production baseline), Transformer / decoder-only architecture, Chinchilla scaling laws, Flash Attention, RoPE, Mixed precision, Distributed data parallel, Activation checkpointing, Muron (auto-caption; likely AWS Neuron), GPU cluster, Wells Fargo transaction foundation model (internal, ~1B params; 11B in progress)

## [How to Let AI Agents Sign Up for Your App Safely — Isabelle Williams, WorkOS](../videos/uTrY8slys0w.md)
`uTrY8slys0w` · AI Engineer · 2026-10-23 · q3 · practitioner · talk · topics: security-guardrails, mcp-and-tools, governance-compliance, product-ux

WorkOS PM walks through letting AI agents sign up for and act inside an app safely, using AuthMD, ID-JAG identity assertions, and agent tokens scoped to a user-bounded ceiling.

- Techniques: AuthMD discovery file; Anonymous trial with claim token; ID-JAG identity assertion grant; Blueprint ceiling with scope intersection; Separate agent principal from user session
- Tools: AuthMD (open markdown-based agent onboarding protocol), WorkOS Agent Auth, ID-JAG (Identity Assertion JWT Authorization Grant, IETF spec), OAuth 2.0, MCP authorization spec (Enterprise Managed Authorization), Okta Cross App Access, Claude (referred to as Claude / Cloud Code in the transcript), Cursor (used to vibe-code the demo app), Waypoint (speaker's demo travel-planning app), Muse and Instinct (personal agents mentioned, no detail given), Maple Itinerary and Trip Ledger (other planning tools the demo agent tried)

## [Better AI Models Won't Fix Your Engineering Team — Nicholas Arcolano, Jellyfish](../videos/Ve2bAarPA2I.md)
`Ve2bAarPA2I` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · topics: enterprise-adoption, token-cost-efficiency, coding-agents

Jellyfish data from ~50k engineers: switching AI models or tools barely moves merged PRs, while skill use, token volume, company and individual engineer effects explain far more.

- Techniques: Natural experiment from a vendor-driven shock; Within-engineer switch comparison; Variance decomposition of throughput; Skill-use level bins over time; Percentile binning of consumption against output; Longitudinal rank-stability check
- Tools: Cursor, Claude Code, Grok, Opus, Sonnet, ChatGPT, Artificial Analysis (model benchmark charts), Jellyfish (engineering telemetry platform)

## [Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni Analytics](../videos/A3FL_zTQKU0.md)
`A3FL_zTQKU0` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · topics: evals, testing-verification, observability, governance-compliance

Stephanie Jarmak (Omni Analytics) argues agent evals should be done like experiments: check the tool pipeline end to end, match the benchmark to your own workload, decouple flags from enforcement, and trust independent traces.

- Techniques: Tool-use pipeline audit; Harness-plus-model pairing as the unit under test; Workload-representative internal benchmark; Explicit metric choice per use case; Separate flagging from enforcement; Independent record comparison for trust; Shadow deployment and production measurement; Autonomy boundary spec for each action
- Tools: Amp (coding agent), Sourcegraph code search MCP tool, Claude (as used in the grep example), grep, Terminal Bench (transcribed as 'Terminal Bench 4'), OpenHands (open coding-agent harness), Opus 5 (model, as transcribed), Astra (model or harness, as transcribed; unverified), Code Scale Bench (speaker's own public benchmark for large codebases), LLM-as-judge (generic pattern), Omni Analytics evaluation harness (in progress)

## [Why AI Startups Will Disappear Without Compute Markets — Evan Conrad, San Francisco Compute](../videos/Wk2bUUGFC_o.md)
`Wk2bUUGFC_o` · AI Engineer · 2026-10-23 · q3 · intro · talk · topics: infra-cost-scaling, product-ux

Evan Conrad (San Francisco Compute) argues AI startups need compute markets because credit, deposits and forecasting risk make GPU capacity unfinanceable without liquidity; physical settlement requires operating the clusters too.

- Techniques: Build-then-sell capacity financing; Physically settled forward contracts; Take-or-pay contracts for AI capacity
- Tools: San Francisco Compute (company, compute market and operator), Junlark (former company name, as transcribed; an AI music lab), Suno and Udio (as transcribed 'Suno or UDO'; music generation products named as context), Kubernetes (via CNCF Infrastructure Group, mentioned as background)

## [Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One](../videos/bU5gDVyu_28.md)
`bU5gDVyu_28` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · topics: software-factory, context-engineering, testing-verification

Max Kanat-Alexander (Capital One) argues code quality only matters for durable software: it's worth rigor when consequences, replacement cost, dependencies and maintenance are high, and rigor is cheaper when you standardize and automate it.

- Techniques: Place software on a durable-to-disposable spectrum; Make software more disposable on purpose; Standardize to reduce the cost of rigor; Build in-workflow tooling; Provide in-memory fakes for services; Turn lint rules to maximum from the start
- Tools: Chromium (example codebase), Linux (example Hello World)

## [How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada](../videos/c_SPW__jF9w.md)
`c_SPW__jF9w` · AI Engineer · 2026-10-22 · q4 · practitioner · talk · topics: evals, rag-retrieval, enterprise-adoption

Air Canada's data science team explains how they built evaluation sets with no public benchmark: generate test cases from known answers, grade them with code, and avoid LLM-as-judge.

- Techniques: Answer-first synthetic eval for retrieval QA; Plant-the-defect known-answer tests; Remove-a-clause mutation test; Template fill-in combinatorics; Invariance tests; Trajectory checks for tool-using agents; Prefer code graders over LLM-as-judge; Strip complexity before adding techniques
- Tools: BM25, LLM-as-judge, Text-to-SQL (mentioned as an example pattern)

## [1,368 AI Failures and What They Teach About Evals — Vishal Srivastava, New York Life & Tanmay Sah](../videos/mMw3arwQsL0.md)
`mMw3arwQsL0` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · topics: evals, governance-compliance, agent-architecture

Talk using AI Incident Database cases to argue for risk-based, system-level evals: test the whole deployment and the evaluator, try to falsify claims, and prioritize by harm.

- Techniques: Three-dimension, 13-sub-dimension incident taxonomy; Prioritize controls by harm association, not frequency; Materiality scale per AI use case; Four-part risk decomposition; System-level stress testing of the deployment; Evaluator reliability check; Build-break-fix falsification loop
- Tools: AI Incident Database (publicly available database of AI failure reports, used as the analysis corpus)

## [Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI](../videos/_dTF3NpPzGo.md)
`_dTF3NpPzGo` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · topics: evals, token-cost-efficiency, models-research

Louis-François Bouchard (Towards AI) releases ToneBench, an LLM-judged benchmark for whether models write like a specific author, and shares its method, judge-bias findings and costs.

- Techniques: Multi-draft variance measurement; Category-then-rating judge rubric; Cross-family LLM judging; Blind judging with post-hoc attribution; Human pairwise calibration; Contaminated-eval guard; Cheap-draft then strong-merge writing pipeline
- Tools: ToneBench (the speaker's new creative-writing benchmark, from Towards AI), EQBench Slop Score (referenced as prior art; the speaker does not rebuild it), Opus 5.5 (Extra High and Max Thinking modes, as named), GLM 5.3 Flash, GPT 6.1 (named), Grok 4.7 (transcribed as 'Gruk 4.7')

## [The AI Content System Behind 200M Views — Sarah Chieng, Cerebras & Cova Lee, OpenAI](../videos/CFbnVpSsDFQ.md)
`CFbnVpSsDFQ` · AI Engineer · 2026-10-22 · q3 · practitioner · workshop · topics: context-engineering, skills-self-improvement, voice-multimodal, product-ux

Two creators (Cerebras and OpenAI DevEx) walk through a six-stage AI content pipeline: swipe-file ideation, voice-captured scripts, shot lists, agent-driven editing, captioning, scheduling and a periodic process-review skill.

- Techniques: Swipe-file reference library for agents; Build a voice skill from your own past content; Voice-first script interview; Outlier analysis against channel baseline; Two-pass shot list from a script; Organize footage before editing; Agent-driven editing via API or desktop control; Brand design system generated from your own videos; Background and visual enhancement with image generation; Fix mistakes with short inserts; Repurposing into short-form cut-downs; Scheduling with human approval; Remove AI tells from captions and prose; Weekly process-review skill
- Tools: ChatGPT, Codex (CLI, computer use; transcribed as 'Astra/Astro'), GPT-5.6 Sol Ultrafast (as named in the talk; runs on Cerebras at ~750 tokens/sec), Cerebras, Wispr Flow (transcribed as 'whisper flow'), Figma (MCP and plugins), Notion, Obsidian, HyperFrames (HeyGen), HeyGen (avatars), CapCut, Adobe Premiere

## [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](../videos/adfw3xJBx1o.md)
`adfw3xJBx1o` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · topics: enterprise-adoption, mcp-and-tools, coding-agents, sandboxing-execution

Monzo's engineers describe Agent Chip, an in-house coding agent that began as a viral Slack emoji trigger and grew into a sandboxed, MCP-gated platform building block.

- Techniques: Gateway-first MCP layer for internal tools; Isolated sandbox namespace for remote agents; Separate orchestrator from execution; Emoji-reaction prompt trigger in chat; Low-signal incident mode; Proactive impact checks on backend changes
- Tools: Agent Chip (Monzo's in-house coding agent), Slack, GitHub, Linear, MCP (internal MCP gateway server)

## [Same GPU, 50% More Output: Why the Operator Matters — Oliver Kennon, SemiAnalysis](../videos/3axY1wz2OvA.md)
`3axY1wz2OvA` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · topics: inference-serving, infra-cost-scaling, token-cost-efficiency, governance-compliance

Oliver Kennan (SemiAnalysis) argues GPU cost per useful token depends on the operator's serving software and ops discipline, not just the chip, and that cost positions are relative to competitors, which matters for compute futures and rental price hedges.

- Techniques: Cost per acceptable token; Compare on the same chip at a fixed interactivity target; Assess the operator, not just the hardware; Safe update and rollback process for serving
- Tools: SemiAnalysis inference calculator (public), ClusterMax 3.0 (SemiAnalysis operator rating; a 4.0 is mentioned as upcoming), NVIDIA B200 GPU

## [AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard](../videos/uA4ah-dVHvU.md)
`uA4ah-dVHvU` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · topics: enterprise-adoption, mcp-and-tools, data-engineering, multi-agent

Vanguard's cash-ledger modernization: exposing the legacy codebase over MCP cut a 7-day research loop to 15 minutes, with lessons on migration, idempotent producers and consumer onboarding.

- Techniques: Expose a legacy codebase to agents through an MCP server; Two-stage CDC migration verification; Single write gateway with idempotency for all producers; Consumer access matched to channel; Business-case registration for consumers; Fix forward, do not patch the legacy; Human-readable state values in the new system; Shared team knowledge base
- Tools: MCP server (legacy codebase and migration docs exposed to AI tools), CDC (change data capture, generic), GraphQL (real-time consumer API), Kafka (event topic for inserts and updates), Schema registry (generic, for all consumer channels), Snowflake-style IDs (ID paradigm, not the product), Data warehouse data-share views (batch consumers)

## [Is a Faster Model Actually Faster? Test the Whole Job — Morgan Suo, MiniMax](../videos/YvQ4BVTWfHI.md)
`YvQ4BVTWfHI` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · topics: inference-serving, evals, token-cost-efficiency, models-research

MiniMax's Morgan Suo argues a faster model must be judged on a whole research job (sources, numbers, cost, latency, retries), not on tokens/sec or averages, and walks through M3.1 Flash's sparse attention, KV-cache and expert quantization, speculative decoding, and reasoning-effort trade-offs.

- Techniques: Whole-job acceptance eval; Planted-fact position sweep for long-context retrieval; Per-subscore regression check instead of averages; Concurrency sweep with P95 time-to-first-token; Reasoning-effort budget comparison with a recorded setting; Reproducibility record and staged rollout
- Tools: MiniMax M3.1 Flash (LLM, long context, MoE, sparse attention, KV-cache quantization, reasoning effort control), MiniMax A3 (video generation model, shown in opening and closing segments), speculative decoding (serving method), KV cache (serving-side internal memory of keys and values), MoE experts (routed experts with 4-bit weights and activations, shared expert unchanged)

## [One Day, $1,000 in Tokens: An AI War Room for Legacy Code — Ford Prior, GEICO](../videos/DouK81O8R3o.md)
`DouK81O8R3o` · AI Engineer · 2026-10-21 · q4 · practitioner · talk · topics: software-factory, multi-agent, context-engineering, enterprise-adoption

GEICO's Ford Pryor describes an AI "war room" for legacy code modernization: a roster of decision makers, a driver, and fleet-managed Claude agents that take a major change from goal to approved design and agent-callable APIs, with human gates along the way.

- Techniques: War room composition for a major change; Three-repo split of enterprise agent context; Goal-to-approval-to-build loop with a queue; Milestone artifacts plus deterministic gate checks; Taxonomy for modernization missions; Local bindings file for agents on a laptop; Cost guardrails for agent-run work
- Tools: Claude Code, Anthropic Code Modernization plugin, Fleet Kit (Anthropic-collaborated fleet manager, markdown rules; not open source yet), beads (per-agent state tracking), Claude artifacts (HTML worksheets), draw.io, Figma, Slack (mission channel), GitHub Issues (example queue), Fable (model, named in the talk), Sonnet 5.5 (model), Opus 4.8 (model, named as too weak for this steering)

## [The Investor's Edge Lives in Their Head — Anekha Sokhal, Moshi](../videos/UHbODjuviAU.md)
`UHbODjuviAU` · AI Engineer · 2026-10-20 · q2 · intro · talk · topics: product-ux, governance-compliance, data-engineering

Vendor talk from Moshi's founder arguing that an investor's edge is human judgment: machines should do the data grind, while every AI claim stays traceable and the human makes the call.

- Techniques: Split grind from judgment; Per-claim traceability and measured hallucination; Deterministic multi-agent decomposition
- Tools: Moshi (the speaker's own product, described as a 24-7 quant analyst for institutional traders)

## [Why AI Agents Will Need Their Own Bank Accounts — Lincoln Murr, Coinbase](../videos/f_HwzoYrZ7s.md)
`f_HwzoYrZ7s` · AI Engineer · 2026-10-20 · q2 · intro · talk · topics: governance-compliance, product-ux, mcp-and-tools

Coinbase's head of AI product on agentic finance: agents that pay and grow money, the X402 HTTP 402 micropayment standard, and trust that is earned in steps. Largely a vendor pitch with some useful adoption data.

- Techniques: Gate content or APIs behind HTTP 402 micropayments (X402); Staged autonomy for agents that handle money; Delegated conditional execution; Ship features as skills that write code on the user's machine; Proactive widgets against chat cold start
- Tools: X402, Agent Kit, LangChain, Coinbase MCP, Coinbase CLI, Coinbase Advisor, GrokBot, Muse, Stripe Link, Stablecoins

## [Is the Agent Harness Dead? — Jediah Katz, SpaceXAI](../videos/7Y4sbZgBdnc.md)
`7Y4sbZgBdnc` · AI Engineer · 2026-10-20 · q4 · practitioner · talk · topics: agent-architecture, coding-agents, context-engineering, token-cost-efficiency

Jediah Katz (SpaceXAI, formerly Cursor's harness lead) argues the agent harness is not dead: smarter models absorb coding scaffolding, but the harness keeps unlocking new frontiers, handles runtime, trust, and cost, and is moving toward agents as building blocks.

- Techniques: Two-layer harness split; Shim registry with a removal bot; Event subscription primitive; Nudge guardrails for responsiveness; Efficiency tuning levers
- Tools: Cursor, Cursor Agent Harness, GrokBot, Grind Swarm, Rollouts, Claude Code, Pi, Codex, SWE-bench Lite, MLE-bench

## [The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft](../videos/UGjk3Uk0MxM.md)
`UGjk3Uk0MxM` · AI Engineer · 2026-10-20 · q4 · practitioner · workshop · topics: evals, mcp-and-tools, models-research, agent-architecture

Hands-on workshop comparing GPT-5.5, Kimi K2.6, DeepSeek V4 Flash and Mistral Large 3 on counting, RAG grounding, vision, tool calling, agent loops, evals and DSPy prompt optimization.

- Techniques: Single-variable model swap harness; Chain-of-thought decomposition for counting; Grounded RAG prompt with explicit refusal and citation; Tool definitions as prompt engineering; Low-level tool-call loop; Force tool use over mental math; Give date math to a tool; Deterministic checks first, LLM-as-judge second; Spec-driven eval generation with Assert; DSPy with GEPA for prompt optimization; Anthropic document citations
- Tools: Microsoft Foundry, GPT-5.5, Kimi K2.6, DeepSeek V4 Flash, Mistral Large 3, OpenAI Python SDK, OpenAI Responses API, Anthropic Messages API, uv, GitHub Codespaces, LangChain v1, PydanticAI

## [Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco](../videos/Bz1HFxQA1o8.md)
`Bz1HFxQA1o8` · AI Engineer · 2026-10-20 · q4 · practitioner · talk · topics: security-guardrails, governance-compliance, enterprise-adoption, sandboxing-execution

Al Chen (Cisco) on shipping AI into five major banks in weeks rather than a year: CVE remediation with agent-run exploit tests, ClickHouse cross-region DR with data-correctness checks, and keeping PII/MNPI out of LLM-judge reasoning, with showing evidence as the main lever for compliance speed.

- Techniques: Agent-driven exploit verification for CVE remediation (Harbor task); Cross-region ClickHouse DR with backup, restore and correctness checks; Split replication of IDs and metadata from core trace data for residency; Gating LLM-judge reasoning behind a sensitive-data check; Audit the judge prompt, not only the UI
- Tools: Harbor, Docker, Modal, Daytona, ClickHouse, ClickHouse backup (Altinity), Sysdig, Wiz, Prisma, NVD, CISA, MITRE CVE database

## [How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase](../videos/_4Ph2dhmUFI.md)
`_4Ph2dhmUFI` · AI Engineer · 2026-10-20 · q3 · practitioner · talk · topics: governance-compliance, evals, agent-architecture, multi-agent

Coinbase's Evan Kormos on deciding when an agent can run unsupervised: keep the process deterministic on the outside, model it as a graph with policy boundaries, and earn autonomy per node through measured evals.

- Techniques: Policy-bounded DAG process map; Cyclic review node with a bounded loop; Per-node automation checklist; Graduated autonomy rollout; DAG state injected into agent context; Statistical evaluation over repeated runs; Exception-flow and volume monitoring
- Tools: Apache Airflow, LangGraph (transcript says LangChain Langraph)

## [Why AI Agents Still Won't Pay for Anything — Jan Curn, Apify](../videos/-AOxpwVeIWw.md)
`-AOxpwVeIWw` · AI Engineer · 2026-10-19 · q3 · practitioner · talk · topics: governance-compliance, product-ux, security-guardrails

Jan Curn (Apify) argues agents still don't pay for services because the payment funnel (need, setup, trust, buy) has friction at each step, and pay-per-use is the missing piece.

- Techniques: Exact-plus-refund for metered agent billing; Charge before work for non-trivial cost; Escrow then micro-charge (batch settlement); Curated directory as the trust layer for agent-discoverable tools
- Tools: Apify (actors marketplace, about 80k actors), X402 (Coinbase, scheme exact, upto and batch settlement), MPP (Stripe and Tempo; sessions), L402 (Lightning Labs), MasterCard Agent Pay, KYA Pay (Skyfire with Visa), AP2 (Google), ACP (OpenAI and Stripe, Agentic Commerce Protocol), TAP (Visa, Trusted Agents Protocol), UCP (Google and Shopify, Universal Commerce Protocol), ACTP (Alipay), AMP (Alipay, Agentic Mobile Protocol)

## [Stop Telling Agents How](../videos/7T-gldvgfpo.md)
`7T-gldvgfpo` · AI Engineer · 2026-10-19 · q3 · practitioner · talk · topics: context-engineering, agent-architecture, multi-agent, evals

OpenProse founders argue agents should be given declarative Markdown contracts plus triggers, not step-by-step prompts; the talk is largely a product demo of their hosted runner.

- Techniques: Contract-first workflow spec; Codify a golden trace into pinned steps; Event-driven job = contract + trigger; Fresh-session verifier against the contract; Kernel as a bootloader index; Templated multi-agent shapes; Cheap verifier or router (planned, not shipped)
- Tools: OpenProse, run.pros.md (hosted OpenProse runner), pros CLI (pros write, pros run), npx skills (skill install mechanism), Claude Code, Codex, Exa (search), DSPy (contrasted), n8n (contrasted), pi (agent harness without sub-agents, transcribed as 'pie'), Matt Pocock's skill workflow (grill-me, TDD) used as an example, Haiku (cheaper model mentioned)

## [Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa](../videos/L4dUFimVDKU.md)
`L4dUFimVDKU` · AI Engineer · 2026-10-19 · q2 · practitioner · workshop · topics: evals, rag-retrieval, data-engineering

Exa's forward-deployed engineer demos ExaSnapshot, point-in-time web search for backtesting agents without future leakage, plus a hands-on acquisition-prediction exercise. Mostly a vendor pitch, but the leakage and holdout-set points hold regardless of vendor.

- Techniques: Point-in-time (as-of date) retrieval for backtests; Content versioning for trusted historical features; Feature-by-feature backtest with a holdout set; Scoring rubric for event prediction; Pin the repo state for coding-model evals
- Tools: Exa, ExaSnapshot, Cursor, Gamma, ChatGPT, Claude

## [Version-Controlled Search: The Web as It Was — Ryan Ahern, Exa](../videos/vS2IA9pq0Q4.md)
`vS2IA9pq0Q4` · AI Engineer · 2026-10-19 · q2 · intro · talk · topics: rag-retrieval, evals, token-cost-efficiency

Exa vendor talk on version-controlled search (Exa Snapshot): query the web as it stood at a past date, and use that to backtest agent-driven financial features without look-ahead leakage.

- Techniques: As-of (point-in-time) search for backtesting; Holdout validation for agentic features; Separate search-tool eval from model eval; Per-task cost measurement for retrieval
- Tools: Exa, Exa Snapshot, Exa Agent Ultra, Cursor, Gamma, ChatGPT, Claude

## [Buy, Build, Deploy: Using M&A to Drive AI Transformation — Prathik Naidu, Long Lake](../videos/J7n3WJnFTto.md)
`J7n3WJnFTto` · AI Engineer · 2026-10-19 · q2 · intro · talk · topics: product-ux, enterprise-adoption, governance-compliance

Long Lake's founding partner explains why buying services businesses and then deploying AI inside them beats selling AI agents from outside, using a J-curve and a services-economy margin argument.

- Techniques: Outcome-ownership screening filter for AI deployment targets; Value-capture math for outside-in AI vendors; J-curve tracking for AI deployment

## [An AI Agent Got Its User Banned From Resy — Keycard, JPMorgan Chase & AAuth](../videos/IavxrdVnwXM.md)
`IavxrdVnwXM` · AI Engineer · 2026-10-18 · q3 · practitioner · panel · topics: security-guardrails, governance-compliance, enterprise-adoption, agent-architecture

Panel on intent-based runtime authorization for agents: per-call authz with mission context, budgets instead of rate limits, and enforcement outside the agent. Core claim: coarse OAuth scopes don't fit autonomous agents.

- Techniques: Budget-as-token grant with live feedback; Brains/hands split with egress-proxy enforcement; Separate supervising agent for worker actions; Deterministic must-never policy plus intent-derived bounds; Dynamic tool gating by task phase; Intent and environment in trace spans
- Tools: OAuth, OIDC, MCP, Claude Code, Squid proxy, Chrome, Firefox, AAuth

## [Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs](../videos/W4pnzOURwHQ.md)
`W4pnzOURwHQ` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · topics: data-engineering, evals, enterprise-adoption, governance-compliance

Insurance claims data is messy, so AI claims work needs layered extraction, duplicate detection, human verification, and calibrated tiered benchmarks before cross-claim analytics pay off.

- Techniques: Layered extraction with per-level verification; Tiered benchmark with a private held-out tier; Calibrated multi-judge verification; Back-test on historical samples before pilot; Duplicate and co-mingling detection at intake; Human-in-the-loop surfacing with page references
- Tools: Artificial Analysis MLCR benchmark, GPT models, Anthropic models, ChatGPT, Gemini, Claude

## [Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS](../videos/q4WC4TowkBo.md)
`q4WC4TowkBo` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · topics: testing-verification, evals, coding-agents, context-engineering

Build deterministic verifier CLIs and evidence "receipts" so coding agents can prove their own work is done, closing the loop without the human reading every line of code.

- Techniques: Per-app verifier CLI with subcommands; Deterministic end-to-end prove step with Playwright; System-one LLM judge for fuzzy outcomes; Doctor/preflight plus stale-proof detection; Centralized verifier gate on workflow nodes (CTX); Babysitter agent for PR follow-through; Generate many variants and select via eval; Saboteur/detective bug-injection test of the verifier; Evidence attached to PRs; Outcome-first prompting with clear stop conditions; Error messages written for agents; Post-deploy monitoring agent
- Tools: Playwright, Chrome DevTools, pnpm, GitHub CLI (gh), GitHub API, Cloudflare Workers, MCP, Reptile, CodeRabbit, Datadog, Claude Code, Pi

## [Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse](../videos/obfPzbapMIM.md)
`obfPzbapMIM` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · topics: evals, observability, testing-verification, governance-compliance

Langfuse workshop on evaluating high-stakes agents: trace everything, build datasets from production via expert error analysis, mix LLM-judge with deterministic evaluators, and gate prompt changes in CI.

- Techniques: Annotation queue for expert error analysis; Free-text comments to failure-mode taxonomy via LLM; Mixed evaluator suite (LLM judge + code checks); Prompt-promotion-triggered CI eval gate; Mask PII before persisting traces; Shadow runs for ground-truth building; Judge calibration against a human-labeled sample
- Tools: Langfuse, GitHub Actions, ClickHouse, PostgreSQL, Amazon S3, OpenAI chat API, Anthropic models, Whisper Flow, Claude, Langfuse skill (agent skill)

## [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](../videos/KtBivPzmOM8.md)
`KtBivPzmOM8` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · topics: agent-architecture, memory, context-engineering, rag-retrieval

Oracle workshop on memory-aware agent harnesses for AML: treat the harness (loop, memory tiers, skill retrieval, context budget) as the thing to engineer, not the frontier model.

- Techniques: Two-tier memory with promote-to-long-term; Vector-indexed skill and tool box with top-k retrieval; Hybrid keyword plus embedding retrieval with RRF; Compaction or summarization of old context; Skill distillation from past runs; Pre-vetted query tools instead of free-form SQL; Bounded agent loop for unattended runs; Stable request prefix for caching
- Tools: Oracle Database, OCI (Oracle Cloud), GitHub Codespaces, OpenAI chat completions API, vector store, MCP, RRF, Claude Code, Codex, Pi harness, Hermes agent, OpenClaw

## [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](../videos/SHMCGrNJJGc.md)
`SHMCGrNJJGc` · AI Engineer · 2026-10-17 · q4 · practitioner · workshop · topics: evals, observability, testing-verification

Hands-on workshop: trace a Claude financial-analyst agent in Phoenix, read failures, write code and LLM-judge evals, validate judges against human labels, run experiments, and gate CI on them.

- Techniques: Deterministic code eval with structured input; Faithfulness judge with full retrieval context; Five-part LLM judge prompt with constrained labels; Judge hygiene: different-family, stronger judge, suppressed tracing; Open coding then axial coding of traces, with a coding agent; Golden dataset with dev/test split by stable ID; Run experiments on the failing subset only; pass^k reporting for nondeterministic agents; Vitest-based eval suite gated in CI; Eval-driven development
- Tools: Arize Phoenix, Claude Agent SDK, Claude Code, Claude Sonnet 5.5, Claude Haiku 4.5, Claude Haiku 5.5, Vercel AI SDK, OpenTelemetry, OpenInference, Vitest, GitHub Actions, TypeScript

## [AI Agents Cut 3-Day Portfolio Builds to Minutes — Jack McDonald, Apollo & Michael Manapat, Rowspace](../videos/BOWYujhIQuo.md)
`BOWYujhIQuo` · AI Engineer · 2026-10-17 · q2 · intro · interview · topics: data-engineering, enterprise-adoption, product-ux

Customer case study: Rowspace agents and an embedded team cut Apollo's portfolio builds from days to minutes and weekly trade recaps from hours to a one-minute report, with trust earned through per-field source validation.

- Techniques: Embedded discovery with domain teams; Per-field source precedence; Agent draft then human refinement; Automate recurring reports, keep human QA

## [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](../videos/kiClTcJUnhc.md)
`kiClTcJUnhc` · AI Engineer · 2026-10-17 · q4 · practitioner · talk · topics: multi-agent, agent-architecture, security-guardrails, governance-compliance

Anthropic's Claude Managed Agents "flows" (dynamic multi-agent workflows) talk: how to fan out hundreds of isolated sub-agents, control cost with budgets, and contain risk with credential vaults, egress rules and auto mode.

- Techniques: Plan, fan out, phase-gate; Per-phase model and agent-count allocation; Separate reviewer context for adversarial checks; Two-stage review with verification; Budget as a resumable circuit breaker; Credential injection at the egress proxy; Declare, contain, detect; Transcript audit agent; Gradual context reveal via linked markdown index; Filesystem as the inter-agent channel; Interrupt and redirect
- Tools: Claude Managed Agents, Claude Code, Claude API skill, ant CLI, Terraform provider for Claude agents, Dynamic workflows (Claude Code), Hill-climb skill, Dreaming (memory consolidation product), Auto mode (permission classifier), Bug Hunter flow, Explainer Video Maker flow, Claude Tag (Slack bot)

## [The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI](../videos/Ti-BmGU1_mQ.md)
`Ti-BmGU1_mQ` · AI Engineer · 2026-10-17 · q4 · practitioner · workshop · topics: token-cost-efficiency, infra-cost-scaling, governance-compliance, models-research

Eugene Cheah (Featherless AI) walks through "tokenomics" in four moves (measure, right-size, buy capacity, check processes) to cut inference spend, with per-key tracking, model labels per department, and a warning that tokens are not work done.

- Techniques: Per-team and per-use-case API key split; Speed tier per workload; Planner-worker model split; Eval-driven model downsizing; Department-level model labels; Dedicated capacity for base load, burst to public cloud
- Tools: Claude Code, Pi coding agent harness, simple-classifier (open source, speaker's project), tokenomics tracking tool (open-sourced by speaker's company)

## [Stop Chatting With Spreadsheets — Francesco Galletta & Felippe Felisola Caso, Monzo](../videos/e9-br9hveRI.md)
`e9-br9hveRI` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · topics: agent-architecture, testing-verification, governance-compliance, data-engineering

Hands-on workshop on building a trustworthy financial-analysis harness around five principles (shared domain, deterministic calculations, evidence, accountability, verification), demoed on a wedding-budget planner.

- Techniques: Interview-style shared-domain planning with a decision tree; Calculation-as-code with tests and golden examples; Fact / assumption / interpretation labelling with provenance; Branching challenge agent with merge or dismiss; Tiered accountability gates
- Tools: Claude Code, Codex, Looker Studio, Google Slides, Google Sheets

## [The Highest Loop — swyx](../videos/Fva8hFosqyQ.md)
`Fva8hFosqyQ` · AI Engineer · 2026-10-16 · q2 · intro · keynote · topics: agent-architecture, enterprise-adoption

swyx's keynote "The Highest Loop" argues that core AI engineering skill is choosing which feedback loop you work in, moving up for productivity and scaling, down for reliability, and that the conference itself is the loop that makes loops.

- Techniques: Loop-level routing

## [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](../videos/tZycGA_Fbfo.md)
`tZycGA_Fbfo` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · topics: mcp-and-tools, security-guardrails, observability, context-engineering

Credit Karma's senior staff engineer walks through a governed enterprise agent stack: scaffolded agent repos, a central MCP gateway, risk-gated execution, per-run evals, PII blocking, and a context optimizer that cut token use about 90% in demos.

- Techniques: Dev-portal agent scaffolding; Gateway token exchange with namespace routing; Risk-classified plan graph with HITL gate; Thread, run and checkpoint memory; Severity-based redaction before every sink; Context pipeline: budget, re-rank, dedupe, compress; Per-run eval scoreboard with nested detail; Three-layer monitoring split
- Tools: LangGraph, LangChain, FastMCP, Redis, JWT, Docker, Kubernetes, OpenTelemetry, Grafana Tempo, Prometheus, ELK, Loki

## [The Cost of Accessibility in AI — Jemima Abu, CAIS](../videos/ZccJsdOE54M.md)
`ZccJsdOE54M` · AI Engineer · 2026-10-15 · q3 · intro · talk · topics: context-engineering, skills-self-improvement, product-ux, testing-verification

Jemima Abu (CAIS) argues accessibility is cheaper when built in from the start with AI agents, backed by a one-off experiment (58% lower cost, one-third the time) using a custom accessibility skill.

- Techniques: Accessibility skill for coding agents; Pre-run self-audit against a checklist; Audit the codebase before introducing an agent; Reusable component library as an accessibility lever
- Tools: Figma, Chrome Modern Web Guidance skill, WebAIM (cited study)

## [I Spent Two Years Building the Median — Hariprasad Sudharshan](../videos/0JZy5AuuQzc.md)
`0JZy5AuuQzc` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · topics: product-ux, agent-architecture, infra-cost-scaling

Hariprasad Sudharshan argues that with rented models and harnesses, most AI-built products converge on a "median," so durable value needs a deliberate novelty, a strong opinion, and distribution.

- Techniques: Novelty budget; Three-question pre-build check; Separate model, harness and product in comparisons; Treat agent done as a median baseline; Self-hosting break-even calculator
- Tools: Claude Code, Codex, Cursor, Lovable, Replit, LlamaIndex, vLLM, Max plan

## [How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival](../videos/8g1N_a3h9H0.md)
`8g1N_a3h9H0` · AI Engineer · 2026-10-15 · q4 · practitioner · talk · topics: token-cost-efficiency, evals, context-engineering, observability

Alvin Pane (OutRival) on cutting LLM token spend in production: measure baseline variance with a ceiling test, shrink prompts with DSPy-style optimization, downsize models, then gate release on paired shadow-deployment stats with a lower confidence bound above zero.

- Techniques: Ceiling test (self-agreement baseline); Prompt optimization as search (DSPy-style); Prefix-cache-friendly prompt structure; Split pipeline by model size; Paired shadow-deployment statistics
- Tools: OpenTelemetry, DSPy, Jeepa optimizer (as transcribed; likely DSPy's GEPA optimizer)

## [Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket](../videos/gonAewBZxfU.md)
`gonAewBZxfU` · AI Engineer · 2026-10-15 · q4 · practitioner · talk · topics: rag-retrieval, evals, agent-architecture, data-engineering

Two In The Pocket engineers describe a RAG assistant over a Belgian payment scheme's rulebooks: section-aware chunking, table flattening, hybrid retrieval, agentic narrow-to-wide tools, and noisy LLM-judge evals.

- Techniques: Section-path chunking without overlap; Table flattening for merged cells; Hybrid dense plus BM25 with RRF; Narrow-to-wide agent tool ladder; Tool-level recovery guardrails; Stream prose, render structured parts last; Lightweight feedback logging; Promptfoo end-to-end evals plus retrieval-only eval
- Tools: Qdrant, BM25, Reciprocal Rank Fusion, Promptfoo, Pydantic, LLM-as-judge

## [Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder](../videos/Wb2v9Phhnns.md)
`Wb2v9Phhnns` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · topics: security-guardrails, sandboxing-execution, governance-compliance

Coder's staff PM walks through three real AI-agent incidents (a Replit prod wipe, a Copilot-enabled bank exfiltration, the NX supply-chain attack) and argues that infrastructure controls, not smarter models, prevent them.

- Techniques: Ephemeral remote workspaces with no route to production; Per-task short-lived, narrow-scope credentials; Identity-aligned access control for AI tools; Model proxy layer; Agent sandboxing as a firewall; Externally owned audit logs with real-time alerting; Planning-only mode and automatic dev/prod DB separation; Premortem with the team
- Tools: Replit Agent, Microsoft Copilot, Nx (build tool), Coder workspaces, Claude Code, Codex

## [Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, Sonar](../videos/7b9tov5Uc5s.md)
`7b9tov5Uc5s` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · topics: pr-code-review, software-factory, governance-compliance, infra-cost-scaling

Gautam Korlam (Sonar/QAR, ex-Uber) on why CI, merge queues and review were built for human speed, and how to keep agent-scale commits green, fast and auditable in regulated teams.

- Techniques: Parallel speculative merge queue; Move checks left and offload expensive checks; Cache, shard and reduce compiler churn; Layered AI review with a fast first pass; Policy-based auto-approval with escalation; Durable decision record on the PR
- Tools: Rust, GitHub, Next.js (captioned 'next text'), Uber SubmitQueue (captioned 'summit cube')

## [I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](../videos/dYh7TQkuYFE.md)
`dYh7TQkuYFE` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · topics: testing-verification, multi-agent, evals

Corey Gallon (Rexmore) presents a three-level agent review method, each level built as a skill, that catches agents overstating work, misreading facts, and reasoning errors, shown on three real cases.

- Techniques: Deliverable contract with a self-check the sender runs; Fan-out / fan-in with independent identical agents and a source-anchored adjudicator; Control-total anchoring; Claim labeling self-audit; Cold persona reviewers with no context; Fresh-reviewer final pass

## [Tokens Are the Cheap Part — Steve Jamison, Jellyfish](../videos/U7ZYBCcdJPg.md)
`U7ZYBCcdJPg` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · topics: governance-compliance, token-cost-efficiency, enterprise-adoption, coding-agents

Steve Jamison (Jellyfish) argues AI tokens are a small share of PR cost; tracking total intelligence cost per merged PR, with revert rates as a counterweight, beats watching the token bill alone.

- Techniques: Blended cost per merged PR; Token-spend quintile cohorts; Within-developer baseline comparison; Counterweight metrics beside throughput

## [Judge a Transaction by the Company It Keeps — Somya Rai & MD Sharique, EXL](../videos/SHvwutPSeZg.md)
`SHvwutPSeZg` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · topics: models-research, inference-serving, governance-compliance

EXL engineers show a graph neural network feeding XGBoost for card fraud, lifting true-positive capture 27-33% at a fixed alert rate and serving it in about 3 ms P99.

- Techniques: Soft-target sampling that keeps graph connectivity; Disjoint time-window graphs for leakage control; Order-invariant multi-statistic neighbor aggregation; GNN embeddings as features for an existing gradient-boosted model; Entity-behavior deviation features; Layer-wise full-graph precomputation with a cached serving path; Edge-level prediction with entity-only embedding cache; Subgraph attribution for analyst-facing explanations; Latency hygiene for Python model serving
- Tools: XGBoost

## [What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad](../videos/gDRCpTMCqEU.md)
`gDRCpTMCqEU` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · topics: evals, governance-compliance, enterprise-adoption

A technical due diligence checklist for AI productivity claims: check the arithmetic of workload vs. human labor, define what "automated" means, and verify quality with experts before trusting a number.

- Techniques: Workload-vs-labor arithmetic check; Straight-through processing boundary; Blind expert review of grader output; Cost per accepted autonomous task; Diligence questions checklist
- Tools: Faros telemetry, Meta grader study

## [The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale](../videos/-a2oTS9J67U.md)
`-a2oTS9J67U` · AI Engineer · 2026-10-14 · q3 · practitioner · talk · topics: governance-compliance, enterprise-adoption, observability

Michele Grant on earning trust in enterprise AI agents: define value, name an accountable owner, and grant autonomy in stages backed by audit evidence, using an M&A integration example.

- Techniques: Pre-deployment value case with baselines; Human work standard (one-page decision map); Deterministic core for financial math; Telemetry as proof, not the model's summary; Four-stage autonomy scorecard; Regression triggers in the model inventory

## [Every Building Is a Balance Sheet: Spatial Memory for Real-World Assets — Jordi Spranger, Spranic](../videos/Fe4aSMXsOZ4.md)
`Fe4aSMXsOZ4` · AI Engineer · 2026-10-14 · q2 · intro · talk · topics: data-engineering, voice-multimodal, product-ux

Jordi Spranger (Spranic, with Neo4j) pitches walk-through 3D scans stored as a time-aligned graph, so real buildings become queryable, change-tracked data for insurance and lending.

- Techniques: Repeat-capture alignment and diffing; Graph as the world model; Provenance on every observation; Natural-language query over a graph map
- Tools: Neo4j, off-the-shelf 3D scanning sensor

## [Deploying AI Inside a Bank Is Not an Engineering Problem — Paden Gayle, Applied AI Engineers](../videos/3ZlQk4-knWM.md)
`3ZlQk4-knWM` · AI Engineer · 2026-10-14 · q3 · practitioner · talk · topics: governance-compliance, enterprise-adoption, evals

Paden Gayle argues that shipping AI inside a bank is a discovery problem: find the people who own each decision in week one, shrink the scope, limit the model's authority, and build an evidence pack from sprint one.

- Techniques: Week-one decision discovery; Dependency-mapped architecture diagram; Shadow, draft, shrink; Four-rung autonomy ladder; Model proposes, human submits boundary; Five-file evidence pack with failure table; Decision-time record capture; Segment-first evaluation reporting; Five-question readiness scorecard

## [Your GPU Neighbor Can Hear Your Model — Branislav Brzak, Stealthium](../videos/SacJfmp33vM.md)
`SacJfmp33vM` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · topics: security-guardrails, inference-serving, sandboxing-execution

Timing alone on shared H100s leaks a neighbor's LLM: model depth, token speed and workload type, via MIG or NVLink. Mitigate with careful placement, host-side kernel monitoring, and no MIG co-location with untrusted tenants.

- Techniques: Timing probe on own memory; Frequency analysis of latency traces for model fingerprinting; Keep sensitive models off MIG slices shared with untrusted tenants; Host-side kernel-launch monitoring
- Tools: NVIDIA MIG, NVLink, NVSwitch, vLLM, speculative decoding, Qwen 8B, Llama 3 8B, DeepSeek R1 distill, GPT-OSS 20B, GLM 4.9B

## [Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway](../videos/oixzVKMAXG0.md)
`oixzVKMAXG0` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · topics: product-ux, coding-agents, testing-verification, skills-self-improvement

Railway's Mahmoud Abdelwahab on why agent-built internal tools feel broken: agents skip product polish (autosave, optimistic updates, undo, URL state) unless asked, so encode taste in skills, reference existing pages, and force end-to-end verification.

- Techniques: Pattern-following via existing abstractions; Named UX patterns as explicit asks; Reference-page anchoring; Taste packaged as skills; End-to-end verification loop
- Tools: Railway, Payload CMS, TanStack, Claude Code

## [Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire](../videos/rAUyRDOFyHU.md)
`rAUyRDOFyHU` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · topics: enterprise-adoption, agent-architecture, evals, sandboxing-execution

Flywire's engineers describe Orbit, an internal platform that runs deterministic code with small LLM steps, gated by YAML definitions, per-step permissions and human-reviewed merge requests.

- Techniques: Deterministic-first workflow with scoped LLM steps; Strict JSON output schema with targeted retry; Per-step capability allowlist declared in config; Skill first, then workflow; Isolated node evaluation with production-trace golden sets; Per-step model selection; Separate orchestration, runtime and session state
- Tools: Claude Agents SDK, Claude Code, AWS ECS Fargate, AWS Lambda microVMs, GitLab, Jira, Sentry, Slack, OpenTelemetry, MCP, YAML, Victoria (internal PaaS)

## [Just-in-Time Ontologies: What Cheap Intelligence Means for Data — Hrishi Olickel, Southbridge AI](../videos/Fa3hQVIKShw.md)
`Fa3hQVIKShw` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · topics: data-engineering, token-cost-efficiency, evals, agent-architecture

Hrishi Olickel (Southbridge AI) argues there is no universal schema, so build just-in-time ontologies per decision, using cheap model tiers, cross-family disagreement, and a failure surface.

- Techniques: Split the job into typed cases before modeling; Fix the question definition, not the threshold; Cross-family disagreement as the audit signal; Cost-tiered checking budget; Bounded pilots, then reusable codons, then production; Pareto surfing with a fixed baseline; Check for prior-driven silent errors
- Tools: Hank Weave (captions: Hank Wave, open-source harness for headless data work), Claude Code (captions: cloud code), Opus, Anthropic Claude models (cheap reasoning tier and frontier tier)

## [Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard](../videos/ws9XcGGPBDk.md)
`ws9XcGGPBDk` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · topics: security-guardrails, mcp-and-tools, governance-compliance

Kim Maida (Keycard) argues agents with private data, untrusted content and external comms form a "lethal trifecta" and shows how token exchange (OAuth 2 RFC 8693-style STS), task-scoped ephemeral tokens and mission-based authorization contain the blast radius without removing capabilities.

- Techniques: Per-tool-call token exchange through an STS; Mission-scoped approval before tool use; Keep all three trifecta legs and control access instead; Audit with attributed identity chains
- Tools: Keycard, OAuth 2 token exchange (RFC 8693 style), MCP servers, MCP gateway, Snowflake, Incident pager API, Google login

## [Reliable, Smart Workflows for Finance, Wealth and Insurance — Karthic Rao, Perpetual](../videos/8g0g1ncwzG0.md)
`8g0g1ncwzG0` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · topics: agent-architecture, governance-compliance, enterprise-adoption

Karthik Rao (Perpetual CTO) on building reliable, regulated wealth-management workflows: an LLM planner emits a typed graph, a deterministic compiler fails closed, and models make only small typed judgments.

- Techniques: Planner emits typed semantic graph, compiler verifies with no model; Closed action grammar with typed contracts; Payload-hash-bound approval gates; Provisional judgments awaiting human confirmation; Side-effect lifecycle with no automatic retry; Rule-based timeouts instead of model decisions; Route judgments to a small tier and log frontier calls as training data

## [We Let Our Financial Planners Write the Agents — Matthew Ragone, Range](../videos/gpmze-6ueGU.md)
`gpmze-6ueGU` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · topics: enterprise-adoption, skills-self-improvement, context-engineering, product-ux

A financial planner at Range explains how non-engineers wrote Claude skills that drafts client work, using a five-step method: pick, teach, pack, test, ship.

- Techniques: Five-step skill build method; Narrated walkthrough as skill source; Ask-first and never-do sections in a skill; Background drafting while the expert is busy; Owner plus non-author reviewer for shared skills
- Tools: Claude

## [Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab](../videos/ZGzthw4BZiA.md)
`ZGzthw4BZiA` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: voice-multimodal, testing-verification, coding-agents, mcp-and-tools

Amazon AGI Lab hands-on workshop on Nova Act's open-sourced perception primitives: point-and-annotate a live page into JSON, run Gherkin-based visual verification, and wire both to a coding agent.

- Techniques: Deterministic visual annotation to JSON; Gherkin user flows auto-generated from a surface crawl; Browser extension to coding agent bridge; Automatic verification after every agent change; Voice or wearable transcript as an annotation source
- Tools: Amazon Nova Act, Nova Act SDK, Nova Act MCP server, Visual Annotator (Chrome extension), Visual verification skill, Claude Code, Kiro, Gherkin, Chrome, uv / uvx, Jam MCP, Atlassian MCP

## [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](../videos/p7gaxmCUiIU.md)
`p7gaxmCUiIU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · topics: skills-self-improvement, evals, agent-architecture, voice-multimodal

Browserbase's Shubhankar Srivastava shows an auto-research loop in which a doer agent and a teacher agent iterate on a strategy file until browser-agent tasks converge into reusable skill.md files that cut cost and latency.

- Techniques: Teacher-doer auto-research loop with strategy file; Converged output as a skill.md artifact; Binary success verifier with minimal guardrails; Scheduled sample runs and failure-triggered healing; Three-layer security for learned skills; Objective choice in the teacher's criteria
- Tools: Claude Agent SDK, Claude Code, Codex, Opus 4.8, Sonnet, Browserbase browse CLI, Browserbase SDK, Stagehand, Browse.sh, WebMCP, Karpathy auto-research, OpenClaw

## [Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI](../videos/fnuNVFgLjHA.md)
`fnuNVFgLjHA` · AI Engineer · 2026-10-12 · q2 · intro · workshop · topics: observability, evals, skills-self-improvement, software-factory

Arize workshop on closing an agent's detect, investigate, fix, verify loop using an always-on trace-analysis agent, coding-agent skills, harness-as-judge scoring and replay experiments; mostly a product walkthrough.

- Techniques: Continuous failure clustering over production traces; Join trace evidence with the code path; Plain-language harness-as-judge rubric with tool access; Failure-dataset replay with agent experiments; Alert-triggered agent investigation; Agent skills for trace analysis from the coding agent
- Tools: Arize Signal, Arize skills, Arize agent experiments, Claude Code, OpenAI Agents SDK, FastAPI, Datadog, GitHub, Cursor, Codex

## [Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal](../videos/aV_vgUSatqs.md)
`aV_vgUSatqs` · AI Engineer · 2026-10-12 · q3 · intro · workshop · topics: coding-agents, mcp-and-tools, context-engineering

PayPal's developer tools leads run a live workshop where attendees make a coffee-ordering CLI work for agents. Main point: interactive prompts fail silently under agents, so CLIs need machine-readable side channels, injected context, and determinism.

- Techniques: Side-channel JSON interface for CLIs; Tmux driver for interactive CLIs; Context injection via a single input file; Deterministic CLI, reasoning outside; Have an agent build the solver
- Tools: tmux, Claude Code, Codex, Claude Agent SDK, Opus 4.8, Slack

## [Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](../videos/FGftGOzfohc.md)
`FGftGOzfohc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: agent-architecture, multi-agent, security-guardrails, memory

Anthropic hands-on workshop (Part 2 of 4) building a research agent on Claude Managed Agents: sub-agents, rubric-graded outcomes, vaults, shared memory, dreaming, and a map-reduce harness.

- Techniques: Rubric-gated outcome with a grader sub-agent; Placeholder secrets with domain-scoped egress swap; Context isolation via self-referencing sub-agents; Check shared memory before redoing work; Map-reduce orchestration via a custom dispatch tool; Transcript-driven memory consolidation (dreaming)
- Tools: Claude Managed Agents API, Claude Code (used to drive the workshop), SEC EDGAR Python package, MCP, Bun, npm, Agent SDK (compared)

## [Stop Renting Intelligence: The Train-to-Deploy Loop for Specialized AI — Fireworks AI](../videos/13YZ1EB9hjU.md)
`13YZ1EB9hjU` · AI Engineer · 2026-10-12 · q2 · intro · demo · topics: training-finetuning-rl, inference-serving, product-ux

Fireworks AI talk on the train-to-deploy loop: moving from closed models to open-source models by fine-tuning (SFT, RFT, DPO) on the same platform used for hosting, with hot-loading and a training agent. Mostly a product pitch, with a few usable workflow ideas.

- Techniques: Continuous train-deploy-monitor-retrain loop; RFT with a vendor-built evaluator function; Training agent with plan approval gate; Draft model training for speculative decoding; Clone-and-compare training runs
- Tools: Fireworks AI platform, FireAttention, Weights & Biases, Qwen3 8B

## [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](../videos/YXiLj4tJt5A.md)
`YXiLj4tJt5A` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: agent-architecture, security-guardrails, skills-self-improvement, mcp-and-tools

Hands-on AWS workshop: build a Strands customer-service agent with hooks (rate limit, deterministic blocks), lazy-loaded skills, steering guardrails, then deploy to AgentCore Runtime.

- Techniques: Per-request tool-call rate limiter via hooks; Deterministic input filter hook; Skills as on-demand markdown procedures; Steering handler (rule or LLM buddy); Externalised steering rules; Message-history inspection
- Tools: Strands Agents, Amazon Bedrock AgentCore (Runtime, Memory, Gateway, Observability), Amazon Bedrock, Amazon CloudWatch, AWS CDK / CloudFormation, AWS OpenTelemetry Distro, boto3, agent-control (open-source steering rules library), MCP, A2A, Jupyter / Workshop Studio

## [AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk](../videos/p-2MT8KYZqU.md)
`p-2MT8KYZqU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: security-guardrails, mcp-and-tools, governance-compliance, vibe-coding-app-building

Two-hour Snyk workshop on AI security foundations: OWASP LLM Top 10 risks, shadow AI and AI bills of materials, AI threat modeling, MCP tool poisoning, vibe-coding failures, and a live CTF chatbot exercise.

- Techniques: Layered prompt-injection defense; Keep secrets out of prompts and enforce access outside the model; Scope chatbot data to what may be disclosed; AI threat modeling workflow; Adversarial review of an architecture; AI BOM as a CI gate; Audit MCP configs and servers before enabling; Secure-by-design playbook for agentic coding; Probe a chatbot in a CTF-style sandbox; Offer an approved alternative when restricting a tool
- Tools: Snyk Evo, Snyk Agent Scan, Snyk Code, Snyk (SCA/SAST), OWASP Top 10 for LLM Applications, STRIDE, DREAD, SBOM (SPDX, CycloneDX), CycloneDX (AI/ML BOM support), Model Context Protocol (MCP), Figma Framelink MCP server, OpenClaw

## [Continuously Improving Agents with Langfuse — Annabell Schäfer & Lotte Verheyden, ClickHouse](../videos/BOCjybvJYM4.md)
`BOCjybvJYM4` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: observability, evals, coding-agents

Hands-on Langfuse workshop on monitoring agents in production: instrument traces, write failure-mode evaluators (LLM-judge and code) on live traces, then use a coding agent over trace data to find silent failures.

- Techniques: Failure-mode-first evaluator set; JSON-path variable mapping for LLM judges; Boolean code evaluators on live observations; Coding agent as trace analyst; Coverage monitoring
- Tools: Langfuse, OpenAI Agents SDK, OpenAI API, Codex, Claude Code, TypeScript, Python

## [Hiring Employable Agents + Startup Battlefield Finals — Howie Liu, HyperAgent](../videos/EEt3ZSG4a1s.md)
`EEt3ZSG4a1s` · AI Engineer · 2026-10-12 · q2 · intro · other · topics: agent-architecture, multi-agent, product-ux, enterprise-adoption

Howie Liu (HyperAgent) argues agents are moving toward always-on "claws" that humans unblock and orchestrate, then the video covers the Startup Battlefield finals (Kamad, Common.io, Foundry).

- Techniques: Heartbeat re-invocation for always-on agents; Human approval gate on high-impact actions; Correction-to-memory loop; Specialist triage and handoff pipeline; Deny-condition state machine for agent actions; Sandbox VM per agent thread
- Tools: HyperAgent, OpenClaw, Claude Code (workflows, fan-out to parallel agents), FFmpeg, Slack, email, Gmail, Stripe, Salesforce, WhatsApp, Google Docs, GitHub

## [Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic](../videos/QSeaZ6qHyXs.md)
`QSeaZ6qHyXs` · AI Engineer · 2026-10-12 · q3 · practitioner · other · topics: agent-architecture, multi-agent, evals, sandboxing-execution

Anthropic presenters answer audience questions on Claude Managed Agents: YAML-as-code deployment, eval sweeps, tenant isolation via workspaces, long runs, and sub-agents for custom tools.

- Techniques: Agent definitions as YAML synced by CI; Parallel eval sweeps on new model releases; Historical-session eval dataset; Workspace-per-customer isolation; Rubric-based exit criteria for long runs; Coordinator with a custom-tool sub-agent; Per-thread session mapping for multi-user chat
- Tools: Claude Managed Agents (CMA), Anthropic CLI (transcribed as 'Ancho CLI'), Claude Code, Modal, E2B (transcribed as 'EB2'), Daytona, Slack

## [Build a Platform and Watch It Burn — Michael Forrester, Accenture & Whitney Lee, Datadog](../videos/1tpqdglI3T0.md)
`1tpqdglI3T0` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · topics: security-guardrails, sandboxing-execution, mcp-and-tools, observability

Workshop where attendees attack a Kubernetes-hosted burrito-ordering agent, then add layered infra and AI guardrails (admission, runtime, network, input/output scrubbing, MCP checks) and see which attacks each layer stops.

- Techniques: Layered guardrails across infra and AI; Input guard before the LLM call; Mid-stream output scrubbing; MCP tool description review and registry allowlists; OpenTelemetry traces for every agent turn; Kernel-level prevention for runaway processes; Agent identity and least privilege; Three-question rubric for AI in a workflow
- Tools: Kubernetes, Amazon EKS, kagent, Kyverno, Falco, Falco Talon, Tetragon, KubeArmor, Cilium, SPIFFE/SPIRE, LLM Guard, NeMo Guardrails

## [The Autonomous Computer: Infrastructure for Computer Use Agents — Ang Li, Simular](../videos/tyFPqtyOK5w.md)
`tyFPqtyOK5w` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: voice-multimodal, agent-architecture, evals, sandboxing-execution

Ang Li (Simular) on computer-use agents: why reliability needs a neurosymbolic loop, where the agent writes code that is replayed, and why pass^k matters more than pass@1.

- Techniques: Neurosymbolic replay with healing; Accessibility-tree grounding with IDs; Per-step observation choice; Clarification-first prompt; Reverse-check verification of entries; Rules-first guardrail chain; Exploration swarm for changing UIs; Test-time scaling by agent count; Save-to-skill with parameters
- Tools: Simular Agent S / S2 / S3 harnesses, Simuland (open-source scripting language), Claude Code, OSWorld, OSWorld 2, Playwright, Windows 365 for agents (Microsoft), Simular cloud desktop API and CLI, GPT-4V, GPT-5, GLM 5.2

## [Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI](../videos/_zUp6y9bDU8.md)
`_zUp6y9bDU8` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · topics: evals, observability, coding-agents, skills-self-improvement

Arize's Ankur Duggal argues agents need trace-based evals, then demos a coding agent (Claude Code plus Arize skills) turning production traces into failure analysis, datasets, evaluators and experiments.

- Techniques: Trace-to-dataset-to-experiment loop; Coding agent as eval workflow driver; Mixed evaluator set; Sampled online evals; Tailored evals from observed failures
- Tools: Arize AX, Phoenix, Claude Code, Codex, Cursor

## [How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI](../videos/-AKPRSYccJc.md)
`-AKPRSYccJc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: pr-code-review, context-engineering, coding-agents, testing-verification

Hands-on workshop by a Qodo DevRel on wiring codified rules, skills, structured plans and deterministic gates into an agentic coding loop from planning through PR review and autofix.

- Techniques: Codified rules and skills pulled per phase; Structured high-level plan plus execution plan; Read-only plan mode with an explicit skill handoff; Local verification command as the gate; Audit skills during implementation; Review-findings autofix loop; Severity-tiered rules with merge blocking
- Tools: Qodo, Claude Code, Codex, Semgrep, Ruff, Pyright, Bandit, pytest, GitHub CLI, uv, conventional commits, git worktrees

## [The SDLC You Build Yourself — Andy Wong, Andrei Bocan & Shane Wolf, Atlassian](../videos/ojJXgXLUQFc.md)
`ojJXgXLUQFc` · AI Engineer · 2026-10-12 · q2 · intro · workshop · topics: software-factory, pr-code-review, context-engineering, governance-compliance

Atlassian team walks through its AI SDLC stack (Jira Coding Agent, AI Reviewer, AutoDev, AI SRE, AI Planner) built on a shared context engine, with a hands-on workshop that was largely lost to Wi-Fi problems.

- Techniques: Org-wide standards as enforceable PR rules; Trained filter on review comments; Human-set authority flag on context sources; Acceptance-criteria self-check in a sandbox; Progressive migration with per-engineer quotas; Automation-triggered agent session per sub-ticket; Per-skill and per-subagent model selection; Spend caps and WIP limits on autonomous work
- Tools: Jira Coding Agent, AI Reviewer, AI AutoDev, AI SRE, AI Planner, Rovo Dev, Teamwork Graph CLI, Confluence, Bitbucket, Slack, Docker, Claude

## [How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI](../videos/xn8EsW0wxyc.md)
`xn8EsW0wxyc` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · topics: security-guardrails, agent-architecture, observability, mcp-and-tools

Venice AI's developer-relations lead explains how secrets leak through agent architectures (logs, vaults, LLM context, tool calls) and patterns to contain them: hashed IDs, handles, narrow tool scope, and keeping credentials out of the reasoning layer.

- Techniques: Credential-in-runtime, not in-prompt; Hashed identifiers for rate limits and tracking; Split-key custody for stored outputs; Revocable handles as capabilities; Narrow tool exposure per agent; Prompt-injection classifier in front of the agent; Own the agent runtime; Verifiable private inference via TEE attestation
- Tools: Venice AI, OpenClaw, 1Password, HashiCorp Vault, Firecracker, AWS EC2, VPC, Qdrant, LanceDB, Cursor, Claude Code, MCP

## [Parsing the Epstein Files for JMail — Palak Agarwal & Omar Alhait, Reducto](../videos/HGfsfKaVuGY.md)
`HGfsfKaVuGY` · AI Engineer · 2026-10-12 · q2 · intro · workshop · topics: data-engineering, evals, product-ux

Reducto staff show how their parse-then-extract pipeline turned 3M+ messy Epstein-file PDFs into the JMail sites, then run a hands-on extraction exercise.

- Techniques: Parse-then-extract pipeline; Agentic OCR with self-correction; Schema review in a playground before deploy; Content-aware schema generation; Separate citation pass; Per-use-case prompts on specialized sub-models; Tiered evaluation with your own benchmark
- Tools: Reducto Studio, Reducto parse, split, extract, edit and classify APIs, Claude Code or Codex (paste-in setup instructions via a QR code, per the speaker)

## [Auth for Agents: Let AI Sign Up for Your Product with auth.md — Michael Grinich, WorkOS](../videos/nSkmXakJ6eo.md)
`nSkmXakJ6eo` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · topics: security-guardrails, mcp-and-tools, product-ux

WorkOS founder argues agents need their own sign-up step, and proposes auth.md, an open markdown spec that tells an agent how to register for a service without a human clicking through.

- Techniques: auth.md registration spec; Identity assertion exchange for agent sign-up; Risk-scored registration with time-boxed free access; Deferred human claim; Approval-only supervision
- Tools: auth.md, MCP, ID-JAG, Wrangler, Pi (agent harness), Claude, OpenClaw, x402, Cloudflare

## [Teaching Agents to Search with NVIDIA Data Designer — Dhruv Nathawani, NVIDIA](../videos/qFaKvbVc5cE.md)
`qFaKvbVc5cE` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: training-finetuning-rl, data-engineering, rag-retrieval, evals

NVIDIA workshop on NVIDIA Data Designer: build column-by-column synthetic data pipelines, seed them with Wikidata random walks and Tavily search traces, and use them to teach a model web search (BrowseComp 0 to about 30%).

- Techniques: Column-by-column DAG for synthetic data; Seeded random walks over a knowledge graph; Teacher trajectories with a tool, then SFT on the trajectories; Overproduce and filter funnel; Layered verification of synthetic labels; Skip the golden answer and use a reward function (RL path); Persona seeds from census marginals
- Tools: NVIDIA Data Designer, Nemo Curator, Nemo Gym, Nemo Anonymizer, Nemo Safe Synthesizer, Tavily, MCP, vLLM, gpt-oss-120b, Wikidata, Hugging Face

## [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](../videos/bI8WyG9YB0I.md)
`bI8WyG9YB0I` · AI Engineer · 2026-10-12 · q3 · practitioner · demo · topics: testing-verification, coding-agents, security-guardrails, context-engineering

A Codex deployment engineer and a Sonar developer advocate argue that agent "done" needs evidence, containment is not correctness, and feedback checks belong inside the agent loop, then demo SonarQube hooks, MCP and CLI wired into Codex.

- Techniques: Evidence-backed definition of done; Layered execution and artifact controls; Secret-blocking lifecycle hook; Guide, verify, solve loop (ACDC); Taint analysis across files; Changed-code-only verification for agent edits; Custom rules targeting agent-written code
- Tools: Codex (OpenAI coding agent CLI), SonarQube Cloud, SonarQube CLI, SonarQube MCP server, SonarQube Codex plugin / marketplace, Docker, Git Bash (for setup script)

## [Inside the AI Economy: What Stripe's Data Reveals — Nilofer Rajpurkar, Stripe](../videos/T3wRyXg_yVg.md)
`T3wRyXg_yVg` · AI Engineer · 2026-10-12 · q3 · intro · talk · topics: product-ux, enterprise-adoption, mcp-and-tools

Stripe product talk using payments data to show AI companies build fast, sell globally on day one, price by usage/credits, and build enterprise sales early; includes an agent-driven Stripe setup demo.

- Techniques: Agent-driven sandbox provisioning; Clarifying-question recommender tool plus domain skills; Guardrails on sensitive actions; Hybrid subscription plus credits pricing; Unified customer and catalog model across channels
- Tools: Claude Code, Stripe MCP server, Stripe agent skills, Stripe CLI, Stripe Checkout, Stripe Tax, Stripe Link, Intercom Fin

## [The Next Trillion Internet Users Still Don’t Have an Identity — Adi Singh, AgentMail](../videos/mBNVKkyfnE0.md)
`mBNVKkyfnE0` · AI Engineer · 2026-10-12 · q3 · intro · talk · topics: security-guardrails, mcp-and-tools, product-ux

Adi Singh (AgentMail) argues agent identity will be accumulated from existing human-facing surfaces like email and Slack rather than issued from scratch, and that over-tight key-card style security specs hurt adoption.

- Techniques: skill.md signup flow with inbox provisioning API; Dedicated per-agent inbox as the identity and contact point; Use existing surfaces as the bridge for new agent identity
- Tools: AgentMail, Telnyx, Clawk, OpenClaw, MCP, DKIM/SPF/DMARC, DIDs, agent cards, skill.md

## [1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS](../videos/k72eLcYpVys.md)
`k72eLcYpVys` · AI Engineer · 2026-10-12 · q4 · practitioner · talk · topics: sandboxing-execution, testing-verification, mcp-and-tools

Kevin Orellana (AWS) has a coding agent fuzz-test a sandbox hosting platform with about 1,000 workflows, and shows how sandbox primitives like memory, file persistence and permissions cause failures.

- Techniques: Agent-driven fuzz testing of a sandbox platform; Results in SQLite, not markdown; Two-layer failure triage; Build a workflow suite that mirrors customer workloads
- Tools: MCP, SQLite, Amazon Bedrock AgentCore, SSH, Codex, Claude Code

## [Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI](../videos/_naLJOqVOEI.md)
`_naLJOqVOEI` · AI Engineer · 2026-10-12 · q2 · intro · talk · topics: inference-serving, infra-cost-scaling, models-research

A FriendliAI engineer argues open-weight models now rival frontier ones, so the inference provider's speed, reliability and cost decide the outcome. Covers prefix-cache routing, tiered KV cache and hybrid speculative decoding. Mostly a sales pitch.

- Techniques: Cache-aware request routing; Tiered KV cache offload; Hybrid speculative decoding; Provider bake-off on your own workload
- Tools: OpenRouter (provider stats snapshot), Code Arena leaderboard

## [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](../videos/YIxzNZDDy1A.md)
`YIxzNZDDy1A` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · topics: evals, observability, sandboxing-execution, coding-agents

Wolfram Ravenwolf's hands-on workshop on building a reproducible agent benchmark (Terminal-Bench via Harbor, WolfBench dashboard), arguing that one averaged score hides variance, cost and configuration choices.

- Techniques: Multi-metric leaderboard per configuration; Pin the harness and keep a fork; Sandbox per trial with bounded concurrency; Smoke-test one task before the full run; Explicit retry policy by error class; Set and record every sampling and agent setting; Trace-first debugging of surprising scores; Shareable result snapshot
- Tools: Harbor, Terminal-Bench 2.0, Terminus 2, Weights & Biases Weave, WolfBench, Inspect (UK AISI), Marimo, CoreWeave serverless sandboxes, Daytona, OpenRouter, Docker, uv

## [Taming the AI Hardware Cambrian Explosion — Abdul Dakkak, Modular](../videos/7BcQdtRA3Tc.md)
`7BcQdtRA3Tc` · AI Engineer · 2026-10-12 · q2 · intro · talk · topics: inference-serving, infra-cost-scaling

Modular's pitch for a single portable stack (Mojo language, MAX inference engine, Modular Cloud) across NVIDIA, AMD and other accelerators, backed by vendor-run speed and cost benchmarks.

- Techniques: Heterogeneous prefill/decode split; Price-normalized hardware comparison; Portable kernel development with an open benchmark; AI-assisted porting of kernels; Tuning serving parameters on a Pareto frontier
- Tools: Mojo, MAX, Modular Cloud, vLLM, SGLang, TensorRT-LLM, llama.cpp, PyTorch, Triton, CUDA, ROCm, OpenCL

## [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](../videos/Uv0nAf_7tyU.md)
`Uv0nAf_7tyU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · topics: agent-architecture, sandboxing-execution, context-engineering, mcp-and-tools

Anthropic engineers explain how they split Claude Managed Agents into a session log, a harness "brain" and swappable sandbox "hands", then start a hands-on workshop building a first agent.

- Techniques: Brain / hands / session split; Credential-injecting egress proxy; Append-only event log with pluggable context strategy; Lazy sandbox provisioning; One container per task; Custom tools as an event round-trip
- Tools: Claude Managed Agents, Claude Platform console (quick start), Claude Code, MCP, Sonnet 4.5, Opus 4.5, Haiku, Sonnet

## [Parameter Golf with AutoResearch — Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI](../videos/7RFJRDYroic.md)
`7RFJRDYroic` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: evals, software-factory, agent-architecture, context-engineering

Hands-on workshop on autoresearch loops, where an agent edits code, a fixed eval scores each attempt, and only improvements are kept. Covers eval design, bounded runs, steerability and the Parameter Golf results.

- Techniques: Fixed-budget eval contract; Tree-of-attempts search with per-node diffs; Guidance file as the steering channel; Hidden validation set for contests and benchmarks; Constrained single-metric optimisation; Bridged session for direct steering
- Tools: Weco, Modal, Claude Code, Opus 4.8, OpenAI MLE-bench

## [Turning My Obsidian Vault Into a Local AI Engineer — Filip Makraduli, Superlinked](../videos/Ndp5VaqFrl0.md)
`Ndp5VaqFrl0` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · topics: local-ai, mcp-and-tools, inference-serving, security-guardrails

Filip Makraduli (Superlinked) shows a privacy-first setup: a self-hosted MCP tool server runs OCR, redaction and extraction on sensitive documents in your own cloud, so a Claude Code agent only sees the cleaned output.

- Techniques: MCP tool server in front of private inference; Per-worker batching instead of a shared queue; Multi-model hot-swapping on one GPU; Stateless tools-only MCP server over streamable HTTP; Check thinking-token settings per model in tool pipelines; Warm-model-aware routing (roadmap)
- Tools: MCP, Claude Code, Obsidian, Superlinked, Terraform, Helm, Kubernetes, Docker, Claude Co-work

## [Building AIE: Open Q&A and Feedback Session with swyx](../videos/snTZtttfL70.md)
`snTZtttfL70` · AI Engineer · 2026-10-12 · q1 · intro · other · topics: product-ux, enterprise-adoption

Open Q&A with swyx after the AI Engineer World's Fair: no AI-safety track, the same venue and size next year, a partner-run country model, the CFP bar, and attendee app feedback. Little engineering content.

- Techniques: Publish conference data as open JSON; Partner-run local meetups with a fixed cadence
- Tools: Twitter, LinkedIn, YouTube, Slack

## [AI Apps in a Flash: Ship to GPUs Without Docker — Dean Quiñanola, Runpod](../videos/XczFLWEntiE.md)
`XczFLWEntiE` · AI Engineer · 2026-10-12 · q2 · intro · demo · topics: infra-cost-scaling, inference-serving, dev-tools

RunPod's Dean Quiñanola demos RunPod Flash, a Python-first way to run and deploy GPU functions on serverless endpoints without writing a Docker image; the main takeaway is that the Docker build-push loop is the bottleneck for AI app iteration.

- Techniques: Docker-free function iteration with a local dev server; Dependencies installed at worker start-up instead of baked into an image; Endpoint-to-endpoint function calls; Network volumes for warm caches across scale-ups; Teardown of dev endpoints on cancel; Spreadsheet-driven experiment fan-out
- Tools: RunPod Flash, RunPod serverless endpoints, Docker, Docker Hub, FastAPI, PyTorch, Hugging Face, Python, GitHub

## [Building AI Agents with Real-Time Web Data — Yohan Raju, Bright Data](../videos/IK8cC4FScps.md)
`IK8cC4FScps` · AI Engineer · 2026-10-12 · q2 · intro · demo · topics: mcp-and-tools, rag-retrieval, data-engineering

Bright Data's Yohan Raju argues that live web data (scrapers, anti-bot handling, and an MCP endpoint with 60+ tools) lets AI agents answer questions that pre-indexed RAG cannot, then demos an Amazon-plus-Reddit buy/no-buy agent.

- Techniques: Live-vs-indexed query routing; Response caching for time-stable answers; One MCP endpoint with many scraping tools; Search-then-scrape chaining; Decision agent over multi-source API data; Record validation and medallion staging
- Tools: Bright Data MCP server, Bright Data Web Unlocker, Bright Data Browser API, Claude Code, Claude, GPT, Gemini API, LangChain, Google Colab-style notebook, Glassdoor, Amazon, Reddit

## [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](../videos/KhRjivBSwiw.md)
`KhRjivBSwiw` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · topics: context-engineering, evals, data-engineering, mcp-and-tools

TypeDef's talk and workshop argue that data and code agents need a computed, traversable context graph; deterministic structure comes first, and agents still default to grep unless tools are shaped and measured.

- Techniques: Deterministic structure first, LLM last; Layered extraction ladder for code; Persistent typed graph with subgraph traversal; Blast-radius tool before edits; Incremental re-indexing keyed to changed files; Isolated data clones for evals, with injected bugs; Tool renaming and shape-matching; Consistency and adoption metrics; Many small focused LLM questions; Eval set pinned to a snapshot, with near-failing tasks
- Tools: Neo4j, Cypher, tree-sitter, rustdoc JSON, Pydantic AI, pydantic evals, Fennec, OpenRouter, Logfire, dbt, Snowflake, Databricks

## [Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI](../videos/PwCSYy-oGsM.md)
`PwCSYy-oGsM` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · topics: evals, governance-compliance, enterprise-adoption, product-ux

Druid AI argues containment rate misleads agent evaluation and proposes a weighted, 0-2 scored framework (six pillars, 26 components) judged like an employee and re-run weekly against a human baseline.

- Techniques: Component scoring with weighted clusters; Mandate-first agent definition; Success criteria attached to each task; Weekly re-run against a human baseline; Hybrid accuracy measurement; Central handoff and action-center check; Skill-source and granularity review; Error tolerance set by mode; ROI as freed human time

## [Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands](../videos/iH_wV8BbS24.md)
`iH_wV8BbS24` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · topics: sandboxing-execution, security-guardrails, coding-agents, infra-cost-scaling

Robert Brennan (OpenHands CEO) compares four ways to sandbox coding agents, from Docker on a laptop to one Kubernetes pod per session, and argues least privilege should set the blast radius.

- Techniques: Container per agent conversation with selective mounts; Least-privilege sandbox spec; Ephemeral pod per agent session; Event- or schedule-triggered cloud agents; Matching environment to job
- Tools: OpenHands, OpenHands Agent Canvas, Claude Code, Codex, Docker, Kubernetes, GitHub Actions, Cursor, GitHub Copilot, Twilio, Slack, Datadog

## [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](../videos/qJtcEDc_WJU.md)
`qJtcEDc_WJU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: agent-architecture, multi-agent, memory, skills-self-improvement

Anthropic's live demo and Q&A on Claude Managed Agents covers multi-session orchestration, scheduled deployments, outcome rubrics, and "dreaming," a memory-store self-improvement pass that the speaker says still needs your own evals.

- Techniques: Fan-out one session per entity via a dispatch tool; Scheduled deployment of a standing agent; Outcome rubric with a max-iteration cap; Offline dreaming pass over past transcripts; Workspace-per-tenant isolation instead of BYOK; Memory store as a separate attachable resource
- Tools: Claude Managed Agents, Claude Console, Claude Code, Anthropic SDK / API, AWS Bedrock, GitHub, OpenTelemetry, Jira (Atlassian integration), Notion (external agents)

## [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](../videos/ZyC56eV8sVw.md)
`ZyC56eV8sVw` · AI Engineer · 2026-10-12 · q2 · intro · workshop · topics: security-guardrails, mcp-and-tools, governance-compliance, coding-agents

A two-hour Snyk workshop on AI security basics: OWASP LLM Top 10, shadow AI and AI bills of materials, AI threat modeling, MCP and skill supply-chain risk, and secure-by-default coding hooks.

- Techniques: Treat LLM input and output as untrusted data; Read-only database views for agents; Approval gate for high-risk actions; Full action logging plus a background log scanner; Scan-fix-rescan agent hook; Pre-install scanning of MCP servers and skills; AI-BOM inventory with query by component; Security requirements inside the prompt
- Tools: Snyk agent-scan (MCP and tool scanner), Snyk AI-BOM (CycloneDX-style inventory), Gandalf (Lakera) prompt-injection game, Claude Code, Cursor, Windsurf, OpenClaw, CycloneDX, SPDX, STRIDE, MITRE ATLAS, uvx

## [Agents That Own Their Inference — Du'an Lightfoot & Khaja Omer, Akamai Technologies](../videos/4n08JHb90hI.md)
`4n08JHb90hI` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · topics: inference-serving, local-ai, infra-cost-scaling, evals

Akamai hands-on workshop on self-hosting LLM agents on a single GPU with vLLM: memory budgets, prefill vs decode, FP8 quantization, speculative decoding, and finding the concurrency knee.

- Techniques: Memory budget math; Concurrency sweep to find the knee; One-flag-at-a-time tuning; Quantize with your own eval set; Validate speculative decoding by acceptance rate; Prefix caching for repeated context; Own-vs-rent break-even
- Tools: vLLM, Kubernetes, LKE (Akamai Linode Kubernetes Engine), KServe, SGLang, TensorRT-LLM, llama.cpp, Ollama, Prometheus, Grafana, Langfuse, LLM Compressor

## [Vector Isn't Enough: Hybrid Search & Retrieval — Jeff Vestal & James Williams, Elastic](../videos/ksjwtQop4os.md)
`ksjwtQop4os` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · topics: rag-retrieval, evals, mcp-and-tools

Hands-on Elastic workshop on why hybrid search (BM25 plus dense vectors, fused with RRF or linear weights, then reranked) beats vector-only retrieval for RAG and agent tool use.

- Techniques: Reciprocal Rank Fusion (RRF) hybrid search; Linear combination with min-max normalisation; Filter before ranking; Retrieve then rerank in one request; Search templates routed by an LLM (poor man's auto-tuning); Semantic_text with default sentence chunking; LLM answer with citations from retrieved sources; Index-description tool for agents; Point-in-time pagination
- Tools: Elasticsearch (serverless), Kibana / Discover, Elastic Inference Service, Jina embedding and reranking models (Elastic acquisition), Agent Builder (Elastic agent platform), ES|QL, Jupyter notebooks, Elastic workflows and MCP endpoint

## [How Inference Keeps Up with Our Insatiable Need for Tokens — Cerebras & Gimlet Labs](../videos/_cRgl3maiT8.md)
`_cRgl3maiT8` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · topics: inference-serving, infra-cost-scaling

Cerebras and Gimlet Labs walk through LLM inference optimizations, from paged KV cache and chunked prefill to prefill/decode and attention/FFN disaggregation across mixed hardware, plus agent-generated GPU kernels.

- Techniques: Paged KV cache; Prefix / prompt caching; Chunked prefill; Prefill/decode disaggregation; Speculative decoding; Attention/FFN disaggregation; Agent-driven kernel search
- Tools: Cerebras CS3, AWS Trainium, AWS EFA, NVIDIA H100, AMD GPUs, Kforge (Gimlet agent for kernel generation)

## [Can Your Agent Hear You Now? Building Live Voice Agents with Gemini — Thor Schaeff](../videos/xfPVBzDYjH4.md)
`xfPVBzDYjH4` · AI Engineer · 2026-10-12 · q2 · intro · demo · topics: voice-multimodal, models-research, mcp-and-tools

A Google DeepMind developer-experience lead demos the Gemini Live API for real-time voice and vision agents, covering native-audio sessions, tool calls, live translation and stateful image generation. Mostly a product showcase with a few useful architecture points.

- Techniques: Stateful WebSocket session for real-time multimodal agents; Tool call from a live voice agent to a slow generator; Chaining generations with the previous interaction ID; Native audio vs cascaded voice pipeline
- Tools: Gemini Live API, Gemini 3.1 Flash Live, Gemini 3.5 Live Translate, Gemini TTS, Nano Banana Lite, Omni Flash, Lyria 3, Gemini Interactions API, Google AI Studio, LiveKit, Pipecat

## [AI Agents Don't Read Your Policy Docs. They Hit Your APIs — Gravitee](../videos/7v2myBde05o.md)
`7v2myBde05o` · AI Engineer · 2026-10-11 · q2 · practitioner · review · topics: security-guardrails, governance-compliance, infra-cost-scaling, mcp-and-tools


- Techniques: Per-task scoped agent identity via token exchange; Gateway-level rate limiting on agent requests; Semantic cache keyed on prompt similarity; Pre-request prompt size and relevance policies; Narrowing MCP servers to a per-agent tool subset; Export gateway telemetry to existing observability stack
- Tools: Gravitee AI Gateway, Anthropic Claude (Sonnet), Groq (inference), Databricks, Redis (built-in semantic cache), MCP (Model Context Protocol), A2A (agent-to-agent protocol), OpenTelemetry, Datadog, Splunk, Prometheus, Kubernetes

## [Latency Is a Budget. Humanlike Is the Goal. — Jesse Hall, LiveKit](../videos/j4AmIK6OvHc.md)
`j4AmIK6OvHc` · AI Engineer · 2026-10-11 · q3 · practitioner · talk · topics: voice-multimodal, evals, agent-architecture

LiveKit's Jesse Hall argues voice-agent latency is a budget to spend on human-like behavior, not raw speed, and shares audio-based turn detection, perceived-latency metrics, async tool handling and an outcome-scored simulated-caller benchmark.

- Techniques: Perceived-latency metric; Async tool with early turn release; Audio-based end-of-turn detection; Speculative LLM on provisional transcript, TTS on first sentence; Outcome-scored simulated-user benchmark; Stack-level model selection; Checklist for voice agents
- Tools: LiveKit (open-source real-time agent framework and infrastructure), LiveKit Inference (hosted model inference), LiveKit turn detector (audio-based end-of-turn model), Gemma 4 31B (tuned for voice on LiveKit Inference; auto-captions render it as 'Gemini 4 31B' at one point), ChatGPT advanced voice mode (cited as an example of a LiveKit-powered product), LiveKit voice eval harness and hotel-booking benchmark (open source)

## [Beyond RAG: A Relational Context Engine That Cuts Token Burn — Unblocked](../videos/ORVh4GivEU0.md)
`ORVh4GivEU0` · AI Engineer · 2026-10-11 · q3 · practitioner · demo · topics: rag-retrieval, token-cost-efficiency, context-engineering, data-engineering

Unblocked (Peter) argues RAG misses structured questions, then builds a schema-aware query engine over a document store with validation and self-correction; the talk is a demo-heavy speed run.

- Techniques: Dynamic schema discovery by document sampling; Fuzzy identity resolution with LLM tiebreak; Validate-then-inject for generated queries; Bounded self-correction loop; Per-task context bundle with an A/B harness
- Tools: Claude, MongoDB, GitHub, Slack, Notion

## [The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder](../videos/abw_m-DRi1k.md)
`abw_m-DRi1k` · AI Engineer · 2026-10-11 · q2 · intro · talk · topics: security-guardrails, sandboxing-execution, observability

Coder's staff solutions engineer explains the "lethal trifecta" (private data, external communication, untrusted input) and argues for isolated remote dev environments, a logging model proxy, and a process-level agent firewall.

- Techniques: Remote isolated agent environment; Logging model proxy in front of the LLM provider; Process-level agent firewall with command denylist; Pre-baked environments as supply-chain control
- Tools: Coder, Terraform, Claude Code, Codex, OpenClaw

## [Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked](../videos/spxoDAfh5ig.md)
`spxoDAfh5ig` · AI Engineer · 2026-10-11 · q4 · practitioner · workshop · topics: rag-retrieval, data-engineering, security-guardrails, context-engineering

Peter Werry (Unblocked) builds a schema-aware natural-language-to-database-query engine from scratch, covering schema sampling, identity mapping, allow-list validation and an error-retry loop, as the structured half of retrieval beyond RAG.

- Techniques: Dynamic schema discovery by document sampling; Deny-by-default query validation; Error-feedback retry loop; Forced tool call for entity extraction, with a fallback; Fuzzy identity mapping; Date-aware prompting for temporal queries; Two-stage schema selection; Hybrid entry point, then structured queries; Webhook-driven ingest and re-embed
- Tools: MongoDB, Postgres (mentioned as a comparison with table definitions), GitHub, Linear, Jira, Slack, MCP, Levenshtein distance

## [Zero Cold Starts: Serverless AI Agents on Akamai Functions — Thorsten Hans](../videos/Zf_e45GiNCE.md)
`Zf_e45GiNCE` · AI Engineer · 2026-10-11 · q3 · intro · demo · topics: mcp-and-tools, sandboxing-execution, infra-cost-scaling

Thorsten Hans (Akamai) demos building MCP servers and a Vercel AI SDK agent as WebAssembly apps on Spin, deployed to Akamai Functions for near-zero cold starts and global distribution.

- Techniques: Compose MCP servers from Wasm components; Snapshot a pre-initialized interpreter into the Wasm artifact; Edge-deployed agent using a Wasm framework with a remote model; Local-to-cloud parity via Spin abstractions
- Tools: Spin, WasmTime, WASI, wasmcp, Akamai Functions, StarlingMonkey, Vercel AI SDK, Ollama, MCP Inspector, SQLite, OCI registries

## [RAG Needs a Map: Using GraphRAG to Retrieve Connected Context — Nyah Macklin, Neo4j](../videos/LJ2a9nX3vlo.md)
`LJ2a9nX3vlo` · AI Engineer · 2026-10-11 · q2 · intro · workshop · topics: rag-retrieval, data-engineering, context-engineering

Neo4j workshop on GraphRAG: when vector RAG falls short (3+ hops, cross-document aggregation), how an LLM can build a knowledge graph, and how to pair vector search with Cypher in a Neo4j Aura agent.

- Techniques: Hybrid vector-plus-Cypher retrieval tool; Text-to-Cypher tool beside the search tool; Schema-pinned LLM entity extraction; Chunk, embed, extract, load pipeline; Direct Cypher audit after each rebuild; Grounding instruction to restrict the agent to graph content
- Tools: Neo4j, Neo4j Aura (free instance), Aura Agents, GraphAcademy, GraphRAG for Python (neo4j-graphrag), OpenAI (LLM and text-embedding-3-small), Cypher, GitHub Codespaces, VS Code

## [How MiniMax M3 Was Built: Sparse Attention and Native Multimodality — Olive Song](../videos/htod7Nv1cBc.md)
`htod7Nv1cBc` · AI Engineer · 2026-10-11 · q4 · practitioner · talk · topics: models-research, inference-serving, voice-multimodal

MiniMax's Olive Song explains how M3 adapts DeepSeek-style sparse attention to GQA with per-KV-head block selection, and why it was trained on vision and text from step zero.

- Techniques: Index-branch sparse attention; Per-KV-head selection under GQA; Block-level retrieval instead of token-level top-k; Native multimodal pretraining from step zero; Attention-map check for modality fusion; 3D attention in the ViT with a frame cap
- Tools: MiniMax M3, MSA (MiniMax Sparse Attention), DeepSeek DSA

## [An AI Future Without the Lock-In — Remy Guercio, Tailscale](../videos/s-glGHAa1a4.md)
`s-glGHAa1a4` · AI Engineer · 2026-10-11 · q2 · intro · talk · topics: infra-cost-scaling, governance-compliance, mcp-and-tools

Tailscale's Remy Guercio argues for "ROI maxing" over token maxing: keep choice at every AI layer through an identity-aware AI gateway (Aperture) to avoid lock-in. Mostly a product pitch.

- Tools: Tailscale, Aperture (Tailscale AI gateway), WireGuard, TSNet, Entra, Okta, Anthropic API, OpenAI API, Vercel AI gateway, AWS Bedrock, Codex, Claude Code

## [From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot](../videos/b9UhZkKjX_A.md)
`b9UhZkKjX_A` · AI Engineer · 2026-10-11 · q2 · intro · talk · topics: coding-agents, software-factory, observability, multi-agent

GitHub's Jose Palafox walks through the Copilot agent surfaces: local agents you steer, reusable shared agents, cross-repo orchestration, and headless agents in CI that get cost and trace visibility through OTel.

- Techniques: Headless one-shot agent in CI; Slash-command phase gates on issues; Scaffold agents from a one-line description; Marketplace or private-repo distribution; Orchestrate: issues as goals, agents per repo; Cross-model plan audit; Small-model codebase explorer; OTel per-agent cost monitoring
- Tools: GitHub Copilot CLI, GitHub Copilot SDK, GitHub Actions, GitHub Agentic Workflows, Awesome Copilot, OpenTelemetry, Slack, Microsoft Teams

## [Building on the Codex Harness — Dominik Kundel, OpenAI](../videos/9WiBJRO84yY.md)
`9WiBJRO84yY` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · topics: coding-agents, agent-architecture, mcp-and-tools, context-engineering

OpenAI's Dominik Kundel shows how to build your own client on the open-source Codex app server, the JSON-RPC protocol that wraps the Codex harness, and gives three rules for customizing it safely.

- Techniques: Append developer instructions instead of replacing the system prompt; Deferred dynamic tools with tool search; Pin and bundle the harness binary; Per-thread config overrides; Integrate by delegating to the coding agent; Choose exec or app server by parallelism and interactivity
- Tools: Codex app server, Codex CLI, Codex exec, Codex desktop app, Python SDK (Codex), Agent Client Protocol (ACP), LM Studio, Ollama, Electron, Cloudflare Doom WASM renderer, T3 Code, Claude Code Codex plugin

## [From 15% to 90% GPU Utilization: Fix the Data Pipeline, Not the Model](../videos/tNAV259UhCM.md)
`tNAV259UhCM` · AI Engineer · 2026-10-10 · q4 · practitioner · talk · topics: data-engineering, training-finetuning-rl, infra-cost-scaling

Fixing a multimodal SFT data pipeline on Ray (concurrency, prefetch, zero-copy, scheduling) took GPU utilization from 15% to about 90%. The lesson: profile the data path, not the model.

- Techniques: Wait time ratio as the pipeline health metric; Async IO for object-store fetches, process pool for CPU preprocessing; Background prefetch queue; Pass object references instead of data; Spread scheduling and zero-copy retrieval at scale; Scaling-ladder ablation
- Tools: Ray, Ray actors, Ray object store, Megatron, Qwen3-VL (auto-caption reads as "QN3VL"), PIL, NumPy, Hugging Face Transformers tokenizers, pandas, S3, JSONL, asyncio

## [Stop Prompting — Greg Pstrucha, Sentry](../videos/E3KbFLAGD6A.md)
`E3KbFLAGD6A` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · topics: context-engineering, testing-verification, coding-agents, pr-code-review

Sentry's Greg Pstrucha argues teams should stop re-prompting coding agents and instead codify repeated conventions as deterministic lint rules, skills checks, and policy-driven review loops.

- Techniques: Mine feedback to find lint-worthy rules; Custom AST lint rules with ast-grep or ESLint-style tools; Lint for schema sync; Validate code examples inside skill documents; Policy files plus per-policy sub-agent review loop; Hooks to run deterministic checks at the right moment
- Tools: ast-grep, ESLint, OxLint, Flake8, Clippy, Claude Code skills, OpenAPI schema, Django REST Framework, a plain-English lint tool transcribed as 'TaskLessware' (name uncertain from auto-captions)

## [Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop — Gabriel Martinez, G2i](../videos/6qkzlT962es.md)
`6qkzlT962es` · AI Engineer · 2026-10-10 · q3 · intro · talk · topics: pr-code-review, context-engineering, software-factory, product-ux

Gabo (G2i) argues AI slop comes from generation outrunning judgment. His fixes are conventions, small reviewable chunks, visible accountability, and ORC, an orchestration workflow built around review.

- Techniques: Single canonical pattern per concept; Diagram-first review surface; Small reviewable chunks with explicit ownership; Built-in adversarial and planning gates before merge
- Tools: ORC (G2i's orchestration system, described only at a high level), Ruby on Rails (convention-over-configuration example), SQLite (quoted maintainer comment on PR maintenance cost)

## [Designing CLIs for Agents, Not Humans — Pedro Lopez, Airbyte](../videos/3wj6sgbi1YA.md)
`3wj6sgbi1YA` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · topics: mcp-and-tools, coding-agents, security-guardrails

Airbyte's Pedro Lopez on building a thin MCP server and CLI for agents: a small tool surface, OAuth-only auth, JSON in and out, non-interactive credentials, and skills shipped with the CLI.

- Techniques: Thin interface over a shared API spec; Minimal tool surface with progressive discovery; OAuth-first MCP auth with a connect-link flow for third-party credentials; Agent-friendly CLI contract; Ship a skill with the CLI, with progressive references; Use failure patterns as a design signal
- Tools: MCP, CLI, OAuth, OpenAPI, jq, Claude Desktop, Claude custom connectors, ChatGPT app store, Airbyte AI Agents context store, Zendesk, Stripe, HubSpot

## [Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge](../videos/cSz7aL2nl2U.md)
`cSz7aL2nl2U` · AI Engineer · 2026-10-10 · q2 · practitioner · talk · topics: context-engineering, memory, mcp-and-tools, rag-retrieval

Gil Feig (Merge) argues every company needs a "context graph" (a company brain of synced data, live lookups, memory, skills) and lays out how to route, cache, and trace it. Conceptual talk with a closing product plug.

- Techniques: Split retrieval: live MCP vs. synced vector cache; Router plus summarizer; Skills and memory first; Freshness SLA check on cache; Derived-context write-back; Bounded live pulls; Provenance metadata on every record
- Tools: MCP (Model Context Protocol), Zendesk, Jira, NetSuite, Stripe, Qualtrics, vector database (unnamed), Merge Unified, Merge Agent Handler, Merge Gateway

## [Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI](../videos/TyPpSRXGhbc.md)
`TyPpSRXGhbc` · AI Engineer · 2026-10-10 · q4 · practitioner · talk · topics: training-finetuning-rl, evals, data-engineering

Snorkel AI and UC Berkeley Sky lab trained a 4B Qwen3 agent with RL for under $500 that beats its 235B variant on finance QA; simple binary rewards and single-table curricula won.

- Techniques: Multi-stage synthetic eval and training data pipeline; Company-level data split to prevent leakage; Binary reward with reference-based LLM judge; Single-table-first data mixture; Decorator-based RL wrapper for existing agents; Large concurrent rollout generation
- Tools: RLLM, GRPO, Qwen3 4B and 235B, GPT-5 nano (judge), FinQA benchmark, BFCL, EDGAR, H100

## [From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle](../videos/BIhiYL4U9_M.md)
`BIhiYL4U9_M` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · topics: memory, rag-retrieval, context-engineering, security-guardrails

Oracle's Anders Swanson argues agent memory should be a governed, typed database layer with redaction, hybrid retrieval, scoped access, and feedback loops, not files or bigger context windows.

- Techniques: Typed memory schema with per-type lookup; Write pipeline: redact, enrich, scope, embed, episode-link; Weighted hybrid retrieval with fused scores and provenance; Governance on write and on read; Feedback signals that rank and promote or demote memories; Expose memory as a runtime function
- Tools: Oracle AI Database, Oracle Python SDK for agent memory (speaker's; referenced, not shown), Claude Code, Codex, MCP, hooks, skills

## [Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain](../videos/KGFyOtl5ktI.md)
`KGFyOtl5ktI` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · topics: agent-architecture, memory, evals, context-engineering

Jake Broekhuizen (LangChain) argues agent memory is a read-write loop: capture traces, filter them into signal, and promote only the durable parts into long-term context, with human review for procedural memory.

- Techniques: Trace-to-memory capture, analyze, update loop; Classify memory into semantic, episodic and procedural buckets; Gate procedural memory updates with human review and evals; Check the hot path for memory staleness
- Tools: LangSmith, LangSmith Context Hub, LangChain, OpenClaw, HermesAgent

## [Let Anyone at Your Company Ship Internal Apps with AI — Garrett Galow, WorkOS](../videos/HTzgC3FoYsI.md)
`HTzgC3FoYsI` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · topics: vibe-coding-app-building, enterprise-adoption, governance-compliance

WorkOS's Garrett Galow on a CLI, a Cloudflare-based platform and SSO-by-default that let non-engineers build and ship internal apps; 37% of about 60 apps had no engineer commits.

- Techniques: Pre-flight local setup CLI with template scaffolding; SSO gate on every deployed app by default; Platform abstraction over deploy target; Pair non-engineer driver with engineer consultant in timed hackathons; Push-to-register catalog with shared skills
- Tools: Claude Code, Codex, Lovable, Cloudflare Workers, Cloudflare D1, Cloudflare KV, Doppler, Okta, GitHub, Webflow, Slack, Node.js

## [We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman](../videos/k2ClBT4aqAg.md)
`k2ClBT4aqAg` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · topics: context-engineering, coding-agents, evals

Postman's engineer describes an API context graph over 115+ microservices, grounded in code and telemetry, that improves coding-agent answers on API discovery, shape analysis and impact assessment, with a token-efficiency gain and a staleness warning.

- Techniques: Code- and telemetry-grounded API context graph; Retrospective PR-based eval with quality-vs-tokens plot; Context layer exposed as a skill next to a generic coding agent; Treat graph staleness as an eval regression; Run expensive architecture checks cheaper and earlier
- Tools: Postman API context graph, Claude Code, GitHub code search, Postman AI agent

## [Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j](../videos/XPj3mIKEtI4.md)
`XPj3mIKEtI4` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · topics: memory, skills-self-improvement, data-engineering

Neo4j PM Will Lyon argues agent memory should be a typed, traceable context graph, and shows how to distill that graph into governed, step-by-step agent skills rather than static markdown.

- Techniques: Typed context graph as agent memory; Decision traces as reasoning memory; Scope-first skill distillation; Coverage and coherence checks on generated skills; Staleness-aware skill registry; Typed step schema for skills (APE)
- Tools: Neo4j Agent Memory Service (NAMs), Neo4j graph database, Agent Skills open standard (agentskills.io), APE skill protocol, MCP tools, SkillsBench

## [How a Remote Company Builds AI Fluency — Em Shreve, Automattic](../videos/3XI90A3ENSg.md)
`3XI90A3ENSg` · AI Engineer · 2026-10-09 · q3 · intro · talk · topics: enterprise-adoption, skills-self-improvement, mcp-and-tools

Automattic's two-week, in-person AI enablement cohorts (50% facilitated workshops, 50% real project work) and how they scale learning through alumni champions, meetups and a shared MCP and skills hub.

- Techniques: Two-week immersive cohort with a 50/50 split; Living curriculum; Internal MCP server as a shared hub; Tool-agnostic shared skills directory; Champions, regional meetups and ride-alongs; Staged post-program surveys
- Tools: Claude Code, Codex, open code, MCP, Zendesk, WooCommerce, WordPress AI

## [Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto](../videos/jJQoVkd5yLg.md)
`jJQoVkd5yLg` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · topics: mcp-and-tools, product-ux, observability

Reducto deleted its one-tool-per-endpoint MCP server after a team rollout showed agents were confidently wrong; the rebuild uses fewer workflow-shaped tools, legible uncertainty, and session logs that feed back into guidance.

- Techniques: Workflow-shaped MCP tools instead of endpoint wrappers; Per-step next-action guidance in tool responses; Snapshot / live-state tool with specific error codes; Confidence and provenance in tool outputs fed back to the model; Evals that score clarifying questions as correct behaviour; Session logging, then mining for override and low-confidence signals; Require an explanation of what was built and why
- Tools: Claude Code, MCP, Slack, Notion, Circleback

## [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](../videos/NaOkR3VSfR4.md)
`NaOkR3VSfR4` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · topics: agent-architecture, security-guardrails, multi-agent

Viren Baraiya on running production agents: the LLM only plans, a deterministic harness executes side effects, durable state and human gates make it safe, shown with a Conductor SRE remediation demo.

- Techniques: Brains/hands split; Plan-compile-execute; Code-enforced human approval gate; Idempotent steps or recorded side effects; State-driven replanning loop; Single-responsibility harnesses
- Tools: Conductor, Kubernetes, Slack, LangChain agents, OpenAI Agents SDK, Google ADK, MCP, APIs

## [Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab](../videos/Emo5FGGY-wM.md)
`Emo5FGGY-wM` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · topics: evals, product-ux, observability

Amazon AGI Lab's Felipe Blanes on why static evals fail in production: run an eval flywheel fed by real customer signals, and be transparent about product limits, since trust rises more from honesty than from higher benchmark scores.

- Techniques: Eval flywheel with customer signals; Trajectory caching with model fallback; Stated-limitations disclosure; Non-technical authoring layer on an agent core
- Tools: Amazon Nova Act

## [Your AI Agent Has No Nervous System — Matt Gibiec, Dynatrace](../videos/YNT7Plf9KIg.md)
`YNT7Plf9KIg` · AI Engineer · 2026-10-09 · q2 · intro · talk · topics: observability, coding-agents, context-engineering

Vendor pitch for Dynatrace's "Blue Box" agent, which argues AI coding agents need live environment context (service dependencies, production telemetry, change history) to avoid hallucinated or breaking changes.

- Techniques: Dependency-mapped local testing; Baseline-deviation alerts to the coding agent; Change-correlated incident triage; Context-scoped fix suggestion with human approval
- Tools: Dynatrace Blue Box

## [AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar](../videos/uuwDWRbxoYo.md)
`uuwDWRbxoYo` · AI Engineer · 2026-10-09 · q2 · intro · talk · topics: pr-code-review, software-factory, observability

Sonar's Ali-Reza Adl-Tabatabai pitches an agentic PR validation system (ex-Guitar) that reviews, fixes, and auto-merges PRs, with a trust ladder for rollout. Mostly product pitch, few numbers.

- Techniques: Trust-gated automation ladder; Autofix loop until green; Flaky-test detection and rule-based retry; Agent plus static-analysis hybrid; Model routing proxy with failover; Aggregate PR and CI analytics
- Tools: Sonar, SonarQube, Guitar (agent platform)

## [Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS](../videos/DrfyORO8RqA.md)
`DrfyORO8RqA` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · topics: context-engineering, memory, agent-architecture

AWS speaker on why larger context windows don't fix agents; she covers externalizing big tool output, summarizing and isolating context, loop caps and async tool calls, using Strands Agents.

- Techniques: Memory pointer for large tool output; Summarizing conversation manager with a ratio and a keep-last-N; Tiered memory: short-term, vector long-term, entity graph; Shared invocation-state pointer for multi-agent swarms; Per-tool invocation cap; Async job start/check tool pair
- Tools: Strands Agents, FastAPI, MCP, Neo4j, AWS API Gateway, Amazon Bedrock, Ollama, Gemini, Anthropic, OpenAI

## [Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind](../videos/oWTEiYpxl80.md)
`oWTEiYpxl80` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · topics: sandboxing-execution, agent-architecture, context-engineering

Philipp Schmid (Google DeepMind) argues agents need their own managed, persistent sandbox per API call, shows Gemini Interactions and Agents APIs, and demos a remote Antigravity environment.

- Techniques: Environment snapshot as a reusable agent base; Persistent per-conversation sandbox with server-side state; Filesystem handoff between agents; File-based agent configuration; Mount sources into the sandbox
- Tools: Gemini API, Interactions API, Agents API, Google AI Studio, Antigravity agent, Gemini CLI (for agents, not a coding agent), Google Search tool, URL context tool, Nano Banana Lite, Omni Flash, Gemini TTS, Gemma

## [Why Your AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND](../videos/toq-jyGLZDk.md)
`toq-jyGLZDk` · AI Engineer · 2026-10-08 · q2 · intro · talk · topics: multi-agent, mcp-and-tools, security-guardrails

Vlad Luzin (BAND) argues that agent-to-agent communication is a distributed-systems problem that MCP, A2A and chat platforms don't solve, then pitches BAND's hosted interaction layer.

- Techniques: Loop engineering with two stateful agents; Contact request with bilateral consent before agent discovery; Shared conversational space with human visibility; Runtime ID binding across agent frameworks
- Tools: Claude, Claude Code, Codex, LangGraph, CrewAI, MCP, A2A, ACP, Slack, Microsoft Teams, Discord, WhatsApp

## [From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer](../videos/u-o0sW9nwmk.md)
`u-o0sW9nwmk` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · topics: skills-self-improvement, mcp-and-tools, security-guardrails

Rafal Wilinski (Runlayer) argues agents should distill successful and failed runs into skills, serve them via MCP as a governed company-wide library, and reports a 36% to 100% success jump after one distilled skill.

- Techniques: Trace-to-skill distillation; Learn from failures too; Checks before publishing a skill; Remote MCP skill registry with tool-based access; Group similar runs before distilling
- Tools: MCP, Claude Sonnet 4.6, Voyager, Chromium, AWS Lambda, npx skills

## [AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk](../videos/f3o0-9Dlw3E.md)
`f3o0-9Dlw3E` · AI Engineer · 2026-10-08 · q2 · intro · talk · topics: security-guardrails, multi-agent, pr-code-review

Snyk's Eli Cohen argues LLM-generated code and LLM attackers make twice-yearly pentests obsolete, and pitches a continuous, per-PR AI pentest pipeline (Snyk Evo) with an exploit-validation judge.

- Techniques: Layered agent pipeline for continuous pentesting; Scanner output as LLM context; Exploit proof gate before flagging; Per-PR security trigger
- Tools: Snyk Evo (Snyk's continuous AI offensive security / AI pentesting offering, named in the talk), Snyk (company), Helios (runtime security company, acquired by Snyk), Claude Code (called "cloud code" in captions), Codex (OpenAI coding agent), SAST (static application security testing), DAST (dynamic application security testing; captioned as "dust"), MCP (Model Context Protocol), Mythos (model named in passing; exact referent unclear)

## [Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel](../videos/XqF-IFHBCkM.md)
`XqF-IFHBCkM` · AI Engineer · 2026-10-08 · q3 · intro · panel · topics: enterprise-adoption, software-factory, pr-code-review

Sonar and McKinsey panel on why most companies stall before scaling AI agents in the SDLC, and a staged trust ladder for moving from agent review to fully automated PR merge.

- Techniques: Staged autonomy ladder for agent PR workflows; Derive verification evals from the PRD; Lighthouse teams for best practice; Baseline developer metrics before automation; Write down implicit conventions as explicit specs

## [The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](../videos/exiwa9QbQXI.md)
`exiwa9QbQXI` · AI Engineer · 2026-10-08 · q3 · intro · talk · topics: software-factory, governance-compliance, context-engineering

Factory's Davis Palmie argues engineers should build a "software factory" of agents that turns signals like bug reports into production code, starting narrow, measuring outcomes, and staying model- and surface-agnostic.

- Techniques: Narrow-first, verifiable agent pillar; Close the loop only after tying outputs to input signals; Agent readiness checklist (eight pillars); Per-task model routing for cost versus quality; Single harness and context shared across surfaces; Outcome-based agent metrics
- Tools: Sentry, Slack, AGENTS.md, Factory

## [The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](../videos/TeErpYBUIeM.md)
`TeErpYBUIeM` · AI Engineer · 2026-10-07 · q3 · intro · talk · topics: evals, observability, skills-self-improvement

Langfuse co-founder on moving agent improvement from manual trace review to an AI-driven loop, where agents propose fixes and dataset/evaluator updates while humans set goals and gate changes, with a changelog-writer case study.

- Techniques: Online plus offline eval loop; Agent-proposed fix with human gate; PR review decisions as eval signal; Backtest candidate against baseline; Agent-maintained evaluators from error patterns; Scheduled batch loop over labeled production data
- Tools: Langfuse, Langfuse agent skills, GitHub pull requests, coding agent, Langfuse prompt management, Langfuse annotation queues

## [Grep or Embeddings? Agentic Search Over Company Documents — George He, LlamaIndex](../videos/X4w2Pkz5tDY.md)
`X4w2Pkz5tDY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · topics: rag-retrieval, context-engineering, data-engineering

George He (LlamaIndex) argues that agent document search should be a harness of primitives (list, grep, read by offset, semantic search, page screenshots) chosen by corpus scale, not a single RAG pipeline.

- Techniques: Agent retrieval harness with a small primitive set; Hybrid retrieval with weighted fusion and LLM rerank; Parse once, persist, and store page screenshots; Metadata tagging at ingest; Chunked reads with grep then offset and length; Evaluate parsers on table and layout fidelity
- Tools: LlamaIndex, LlamaParse, LightParse, Turbopuffer, Claude Code, grep, BM25, Textract, Tesseract, MCP, Google Drive, SharePoint

## [Why Building an Eval Platform Is Harder Than It Looks — Braintrust](../videos/mUQoVz7THu0.md)
`mUQoVz7THu0` · AI Engineer · 2026-10-07 · q2 · intro · talk · topics: evals, observability, data-engineering

Braintrust's solutions lead on why eval platforms are a systems problem: a maturity path from spreadsheets to production-trace flywheels, plus why agent traces are hard to store and query.

- Techniques: Three-part minimal eval harness; Production-failure-to-test-case flywheel; Side-by-side experiment UI for prompt and model changes; Separate hot and cold paths for trace data; Natural-language headless eval runs via coding agents
- Tools: Braintrust, BTQL

## [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](../videos/X6l4lpA0_NY.md)
`X6l4lpA0_NY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · topics: software-factory, agent-architecture, skills-self-improvement

Drew Knox of Tessl on building a "software factory" through harness engineering: three loops (inner, outer, meta), a three-layer setup order, and how Tessl's skills registry and automation support it.

- Techniques: Three-tier loop design for agent quality; Issue-to-PR control plane for agents; Governed skills registry; Mistake-to-skill feedback; Repeated task to scheduled skill; Human-intervention metrics as the factory KPI
- Tools: Tessl, Tessl Agent, tessl launch, Linear, GitHub, GitHub Actions, Codex, Claude Code, Gemini

## [Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg](../videos/cf2IhzqeQH4.md)
`cf2IhzqeQH4` · AI Engineer · 2026-10-07 · q3 · intro · talk · topics: governance-compliance, infra-cost-scaling, product-ux

Stigg's CEO argues AI usage pricing needs bank-style runtime controls: synchronous entitlement checks before consumption, hold-and-settle for concurrency, and layered credit pools, not invoice-time reconciliation.

- Techniques: Synchronous pre-consumption check with async settlement; Hold, settle, and idempotency for concurrent draws; Ordered draw-down across credit sources; Deterministic decision waterfall; Metering ledger inside the customer VPC
- Tools: Stigg, OpenClaw, Claude Max, GitHub Copilot

## [Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell — Akamai](../videos/XTpyNrEgJQ4.md)
`XTpyNrEgJQ4` · AI Engineer · 2026-10-07 · q3 · practitioner · demo · topics: inference-serving, infra-cost-scaling

Akamai's Sheila explains when speculative decoding pays off on vLLM: spare GPU memory and structured, low-temperature workloads, measured by acceptance rate and tokens/s on a single Blackwell GPU.

- Techniques: Draft-model speculative decoding; Acceptance-rate-first benchmarking; Draft model selection checklist; Side-by-side A/B on one GPU; Workload triage before enabling
- Tools: vLLM, Llama 70B, NVIDIA Blackwell GPU, EAGLE, Medusa, n-gram speculative decoding

## [Move Fast and Don't Break Things: Scaling Databases for the AI Era — PlanetScale](../videos/uKUA1a0Kdfc.md)
`uKUA1a0Kdfc` · AI Engineer · 2026-10-07 · q3 · intro · talk · topics: dev-tools, infra-cost-scaling, governance-compliance

PlanetScale's Ben argues that agent-driven change can be safe if databases are isolated, sharded, back-pressured, and branched like code, with agents given the same primitives humans use.

- Techniques: Per-segment traffic budgets with graceful degradation; Shard with a routing proxy plus per-shard replicas; Declarative sharding config as JSON for agent drafting; Schema branch, deploy request, one-click revert; Isolation by failure domain
- Tools: PlanetScale, Vitess, VTGate, MySQL, Postgres, SQLite, MCP server, CLI, VSchema

## [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](../videos/eXA2tjRZIbY.md)
`eXA2tjRZIbY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · topics: agent-architecture, observability, evals

Resolve AI's architecture for production-ops agents (on-call, incidents, background tasks): six pillars covering model routing, context, causal evidence, governed actions, learning loops, and multi-level evals.

- Techniques: Alert-as-prompt investigation fan-out; Evidence-chain gate on root causes; Per-subtask model routing; Tiered action permissions; Five-level eval stack; Anti-sycophancy by design
- Tools: Grafana, Slack, Microsoft Teams, Google Cloud (GCP), graph RAG, knowledge graph

## [How I Learned to Stop Worrying and Love the Sandbox — Matt Brockman, E2B](../videos/fz6-NS7qpZc.md)
`fz6-NS7qpZc` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · topics: sandboxing-execution, infra-cost-scaling, agent-architecture

E2B engineer runs a hands-on sandbox capture-the-flag, covering resource limits, snapshot/resume, templates, lifecycle timeouts, orphan processes, and per-user sandbox assignment.

- Techniques: Snapshot-and-resume sandboxes; Warm template with processes already running; Fork a sandbox for parallel experiments; Task-scoped lifetime with a short idle timeout; Orphan process inventory and reaping; Per-user sandbox assignment map; Separate read-only and writable paths; Egress rules when secrets are present
- Tools: E2B, Firecracker, Nomad, Kubernetes, Claude Code, Codex, Python SDK, JavaScript SDK

## [Agent Memory Is Solved. Agent Learning Isn't. — Karthik Ranganathan, Yugabyte](../videos/9_oy4owGtPI.md)
`9_oy4owGtPI` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · topics: memory, multi-agent, context-engineering, observability

Yugabyte's CEO argues agent memory is solved but cross-agent learning is not, and demos Mako, a private-to-shared context store where humans promote memories and provenance is traceable.

- Techniques: Private-to-shared promotion gate; Provenance on every memory; Scoped data packs with a skill-driven MCP interface; Cross-session resumability via shared memory; One-variable-at-a-time RAG tuning with traces; Trace-based token accounting
- Tools: Mako (Yugabyte agent-native persistence layer), YugabyteDB, Claude Desktop, Claude Design, Codex, ChatGPT, MCP, Postgres

## [The Transcript Looked Fine. The Call Wasn't. — Debugging Voice Agents, Arize](../videos/42Bz0TUfeOQ.md)
`42Bz0TUfeOQ` · AI Engineer · 2026-10-06 · q2 · practitioner · talk · topics: observability, voice-multimodal, evals

Arize PM Fuad Ali on why voice agent failures are invisible in transcripts, and how to trace audio sessions, run audio-native evals, and close an observe-evaluate-improve loop. Partly a product pitch, with real open-source instrumentation content.

- Techniques: Session-stitched voice trace view; Provider-agnostic semantic conventions for LLM traffic; Audio-native evals for tone, latency and interruptions; Online evals on spans with monitors that trigger investigation; Replay failed traces against a patched endpoint to verify a fix
- Tools: Arize, OpenInference, OpenTelemetry, Grafana, WebSocket realtime API, GPT Realtime, Gemini Live, LiveKit

## [From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI](../videos/F0TNSmbo5hE.md)
`F0TNSmbo5hE` · AI Engineer · 2026-10-06 · q2 · practitioner · workshop · topics: observability, evals, software-factory, claude-code

Arize workshop on closing the agent improvement loop: instrument an OpenAI Agents app with OpenInference, have a coding agent mine traces and patch failures, then automate it with Arize Signal. Vendor-heavy.

- Techniques: Turn on OpenInference tracing for an agent app; Install vendor agent skills into the repo for the coding agent; Trace triage that looks past error status; Single-problem fix loop with re-verification; Triage automated findings into issues, dataset rows, evaluators or PRs; Regression and guardrail evals before merging an automated fix
- Tools: Arize AX, Arize Signal, Alex (Arize in-product assistant), OpenAI Agents SDK, OpenInference, Arize AX CLI, Claude Code (VS Code extension), npx skills (arise-ai skills), npm, GitHub, WonderToys demo app (Arize sample)

## [Build the Right Thing: Product Engineering (Part 2) — Kent C. Dodds, EpicProduct.engineer](../videos/s0hFne6EeOI.md)
`s0hFne6EeOI` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · topics: product-ux

Kent C. Dodds on product engineering: turn feature requests into jobs-to-be-done, classify them with the Kano model, and build the right thing before building it well.

- Techniques: Problem tree via repeated 'why'; Job statement template; Little-hire tracking; Mom Test validation; Kano classification for prioritisation; Feedback aggregation channel

## [Evals in AI: A Deep Dive — Tejas Kumar, IBM](../videos/NdrSPm6NCdk.md)
`NdrSPm6NCdk` · AI Engineer · 2026-10-06 · q4 · practitioner · workshop · topics: evals, testing-verification, rag-retrieval

Tejas Kumar (IBM) walks through evals as fuzzy unit tests for non-deterministic agents, then builds an LLM judge live, calibrates it against hand-labelled data, and gates CI on human agreement.

- Techniques: Judge calibration loop against a golden set; Pointwise pass/fail judging; Bias probes for judges; CI agreement gate; Pin the judge model version; Living eval dataset from production traffic; Cheapest-first eval ladder; Adversarial and synthetic eval generation; Avoid fuzzy string matching on LLM output
- Tools: Vitest, Cursor, GPT-3.5 Turbo, GPT-4o-mini, Docling, OpenSearch, OpenRAG (IBM), LM Arena

## [Cooking with Codex — Charlie Guo & Gabriel Chua, OpenAI](../videos/FwiS44-xyYw.md)
`FwiS44-xyYw` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · topics: coding-agents, multi-agent, context-engineering, software-factory

OpenAI's hands-on Codex workshop walks through context, computer use, long-running goals, subagents, hooks and automations, then shows the app server for embedding Codex in your own product.

- Techniques: Verifiable goal with milestone files; Milestone-triggered review and goal-audit threads; Side-thread unblock and status query; Subagent vs thread handoff split; Hook-based deterministic guardrails; Heartbeat automation for external waits; Scheduled triage that spawns worktree threads to PRs; Choosing a control surface: computer use vs Chrome extension vs in-app browser; Embedding via the App Server protocol
- Tools: Codex app, Codex CLI, Codex remote (ChatGPT mobile), Codex Chrome extension, Codex computer use, Codex in-app browser, Agents SDK, Sites, Chronicle (research preview, Pro), AppShots (screenshot with embedded text), AGENTS.md, config.toml hooks

## [Your LLM Judge Is a Confident Liar: Building Better Verifiers — Browserbase](../videos/xLxhT2ZI7UM.md)
`xLxhT2ZI7UM` · AI Engineer · 2026-10-06 · q4 · practitioner · talk · topics: evals, testing-verification, training-finetuning-rl, voice-multimodal

Browserbase and Microsoft researchers on why LLM judges confidently mis-grade web agents, and their rubric-and-evidence "universal verifier" that agrees with humans far better, plus its use for filtering training data.

- Techniques: Rubric-first LLM verification; Per-criterion top-K screenshot evidence; Dual verdict: partial-credit score plus boolean outcome; Controllable vs uncontrollable failure schema; Error isolation across dependent criteria; Human-agreement validation with held-out labels; Verifier as data filter for SFT; Auto-research loop to build a verifier, primed with human findings
- Tools: WebVoyager, Online Mind2Web (captioned as 'Online Minor Web'), OSWorld, GPT-4o, Opus 4.6, Cohen's kappa, Browserbase, Microsoft open-source web-agent framework (captioned 'StateGen')

## [Advanced Workshop: Mastering AI Observability — Doug Guthrie, Braintrust](../videos/hfEczxdNyvU.md)
`hfEczxdNyvU` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · topics: observability, evals, coding-agents

Braintrust workshop on AI observability: trace agents, score production traffic with judges and topics, and let a coding agent run the eval-and-fix flywheel through the Braintrust CLI.

- Techniques: Binary, harsh LLM judges with examples in the prompt; Human-calibrated judges; Scores defined in code and pushed to the platform; Automation rules with scope and sampling for online scoring; Topic windows and filters for long conversations; Coding agent as flywheel operator; Service account for the analysis loop; Remote eval exposed to a playground; Mutable spans for attaching scores later
- Tools: Braintrust, Braintrust CLI (bt), OpenAI Agents SDK, Codex, Claude Code, Cursor, OpenCode, uv, GitHub Actions, Modal, ClickHouse, Brainstore

## [How AI Agents Pay: Checkout in ChatGPT and Google AI Mode — Sam Parsons, PayPal](../videos/c5U-XbbEN-g.md)
`c5U-XbbEN-g` · AI Engineer · 2026-10-06 · q2 · intro · talk · topics: mcp-and-tools, product-ux, security-guardrails

PayPal Enterprise Payments (Braintree) walks through three ways merchants accept payments from AI agents: ChatGPT instant checkout, Google AI Mode via UCP, and MCP apps with external checkout.

- Techniques: Host-side tokenization with scoped payment tokens; MCP app widget that triggers host-native checkout; Discovery file plus session endpoints for headless checkout; External checkout handoff linked to a session
- Tools: MCP Apps, Agentic Commerce Protocol (ACP), Universal Commerce Protocol (UCP), Google Pay, Braintree / PayPal Enterprise Payments, ChatGPT, Claude connectors, Goose

## [How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker](../videos/ZUZVNKFSmTM.md)
`ZUZVNKFSmTM` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · topics: security-guardrails, sandboxing-execution, mcp-and-tools

Docker engineer Jim Clark argues that agent safety comes from small, task-shaped sandboxes fed through an MCP gateway, with zero credentials inside the sandbox. The talk also pitches Docker's SBX product.

- Techniques: Role-split sandboxes for untrusted-input pipelines; Intent-scoped sandbox per task; Single MCP gateway as the policy point; Credentials held outside the sandbox; Cross App Access token exchange; Progressive tool disclosure
- Tools: Claude Code, Codex, MCP, MARP, Mermaid, Docker SBX, OpenCode, Gemini

## [Build the Right Thing: Product Engineering (Part 1) — Kent C. Dodds, EpicProduct.engineer](../videos/_fHTqOs5wQA.md)
`_fHTqOs5wQA` · AI Engineer · 2026-10-06 · q3 · intro · workshop · topics: product-ux, coding-agents

Kent C. Dodds argues that once agents level implementation, the durable engineering skill is deciding what to build, using Mom Test-style validation and smallest-slice thinking. Part 1 of a workshop, mostly framing.

- Techniques: Mom Test customer interviews; Ask what the problem costs; Smallest slice / minimal demonstrable solution; Throwaway prototype, then rebuild with agents; Check the neighbors before building; Build the agent playground
- Tools: Slido, Cursor, OpenCode, Claude (captioned as 'cloud')

## [Lifestyles of the AI-Native — Nick Nisi & Zack Proser, WorkOS](../videos/AgBAOXVxt4A.md)
`AgBAOXVxt4A` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · topics: claude-code, coding-agents, testing-verification, context-engineering

WorkOS engineers run a hands-on workshop on operating fleets of Claude Code agents: voice dictation, goal vs loop, verification hooks, Codex adversarial review, worktrees and scheduled tasks.

- Techniques: Goal with a measurable done condition; Loop for recurring or open-ended monitoring; Checksum-verified evidence of test runs; Hook-enforced gates; Cross-model adversarial review; Retrospective agent with curated memory; State machine for ordered steps; Git worktrees for parallel agents; Interactive first, then schedule; Session fleet management; Triage automated PR review output by score
- Tools: Claude Code, Codex CLI, Handy, WhisperFlow, Granola, Greptile, CodeRabbit, Devin, Linear, Slack, tmux, Fleet (nicknesey/fleet)

## [From Raw Documents to AI-Ready Data — Leo Platzer & Jeff Koss](../videos/wzWNYDY7toc.md)
`wzWNYDY7toc` · AI Engineer · 2026-10-06 · q2 · intro · demo · topics: data-engineering, rag-retrieval, governance-compliance

Vendor talk (DZ Labs, now Colibra) on turning millions of messy SharePoint documents into AI-ready data by tagging, deduplicating, freshness-filtering and scoping them before RAG.

- Techniques: Conditional tag tree with AI suggestions and human review; Dedupe and freshness pruning before indexing; Hybrid pattern plus LLM sensitive-data scan; Folder-level context index file; Scheduled data slices
- Tools: SharePoint, DZ Labs (DZ data curation platform, DZ SDK), Colibra, Claude Code, Codex, vector database, knowledge graph

## [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](../videos/qZj7sqmidqA.md)
`qZj7sqmidqA` · AI Engineer · 2026-10-06 · q3 · intro · workshop · topics: evals, observability, testing-verification

A two-hour Arize AI workshop on replacing "vibes" with measurement: read traces, write code and LLM-judge evals, calibrate the judges, then close the loop with experiments.

- Techniques: Error analysis (open then axial coding); Code evaluator on trace or span; Context-matched LLM judge; Rubric structure for LLM judges; Judge calibration with golden labels; Test both directions; Experiments on a fixed dataset; Evaluator split by dimension, with guardrail vs north-star labels; Online sampled evals at span or trace scope; Eval-driven development and data priorities
- Tools: Arize AX, Arize Phoenix, OpenInference, OpenTelemetry, Claude Agent SDK, Anthropic Claude Haiku (agent model), Anthropic Claude Sonnet 4.6 (judge model), Claude Code, Cursor, Codex, Arize Skills (npx install), Alex (AX built-in eval agent)

## [Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust](../videos/T3SS931wU0I.md)
`T3SS931wU0I` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · topics: rag-retrieval, evals, coding-agents

Braintrust dev-rel walks through a small eval comparing agentic search (grep/find/cat in Claude Code) with vector search for finding bugs in the TypeScript Go repo: equal accuracy, but vector cost 4x more.

- Techniques: Eval composition: dataset, task, scorer, experiment; Production-log sampling into a dataset; Mining bug-fix PRs as coding-agent eval tasks; Binary scoring from the repo's own test suite; Forcing a retrieval strategy in a coding agent; Propagating parent span IDs to subprocess agents
- Tools: Braintrust (evals, tracing, UI, CLI, MCP server), Claude Code (agent harness, disallowed-tools flag), grep, find, ls, cat, bash (agentic search tools), Vector database (unnamed in the talk), Microsoft TypeScript Go repo and its test suite (dataset and scorer), Cursor semantic search post (cited as motivation)

## [What Is an Inference Engine, Anyway? — Charles Frye, Modal](../videos/woIYJYd_etI.md)
`woIYJYd_etI` · AI Engineer · 2026-10-06 · q4 · deep · workshop · topics: inference-serving, observability, infra-cost-scaling

Charles Frye (Modal) explains what runs inside an LLM inference engine: workloads, prefill vs decode, process layout, scheduler bottlenecks, KV cache, CUDA graphs, speculative decoding, and production debugging.

- Techniques: Phase-split serving metrics; Keep host work off the GPU critical path; Speculative decoding with exact-output verification; Prefix and radix KV-cache reuse; Treat queueing and cache thrash as alerts; Correctness logging and post-deploy evals; Profile for per-GPU or per-host anomalies
- Tools: SGLang, vLLM, TensorRT-LLM, PyTorch, Hugging Face transformers, FlashAttention, FlashInfer, CUTLASS, Triton, DeepGEMM, DeepEP, Marlin

## [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](../videos/33Oct2hqGnk.md)
`33Oct2hqGnk` · AI Engineer · 2026-10-05 · q2 · practitioner · talk · topics: mcp-and-tools, agent-architecture, sandboxing-execution, evals

AWS's Sandhya Subramani demos an agent that writes its own tools and sub-agents at runtime using three built-in tools (editor, shell, load-from-directory) plus a system prompt, then argues that evals and sandboxing are required before trusting it.

- Techniques: Meta-tooling bootstrap (three tools + system prompt); Check-before-write rule for generated tools; Self-repair on error; Sub-agent topology choice (swarm, graph, workflow); Layered agent evals; Four-part guardrail stack for self-modifying agents
- Tools: Strands Agents (AWS open source agent harness, Python and TypeScript), Python, OpenTelemetry (named as telemetry), Strands code-execution sandbox (recent feature, named in talk)

## [AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](../videos/Bdrs3uAX0_M.md)
`Bdrs3uAX0_M` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · topics: coding-agents, software-factory, context-engineering, rag-retrieval

Sourcegraph CEO Dan Adler argues that large, decades-old codebases are decaying under the flood of AI-written code, and that agents need code-graph and search infrastructure to see and change them across thousands of repos.

- Techniques: Deterministic scripts for mechanical sweep changes; Hybrid agent and script batch change loop; Code-graph plus search as agent context; Coverage audit for sweeping changes
- Tools: Sourcegraph, agentic batch changes, Claude Code, Codex, Cursor

## [The Human Is an Async API — Melanie Warrick, Temporal](../videos/jc3kbZkuHTo.md)
`jc3kbZkuHTo` · AI Engineer · 2026-10-05 · q3 · practitioner · demo · topics: agent-architecture, multi-agent, governance-compliance

Melanie Warrick (Temporal) shows durable execution for multi-agent systems: a human approval is a wait condition plus a signal on a parked workflow, so the rest of the system keeps running and survives restarts. It is a vendor-led talk with a live ice-cream delivery demo.

- Techniques: Human approval as wait condition plus signal; Wrap every model and tool call as an activity; LangGraph interrupt bridged to a durable wait; Child workflow per entity; Cost-of-being-wrong gate for human review
- Tools: Temporal, Google ADK, LangGraph, Google Maps API, Google Search, Python, TypeScript, Rust

## [We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](../videos/pyvRID_CZZU.md)
`pyvRID_CZZU` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · topics: agent-architecture, context-engineering, voice-multimodal, enterprise-adoption

AssemblyAI's FDE team built "Joey," a Claude Agent SDK support agent over local markdown docs, lifting end-to-end ticket resolution from 10% to 80% for about $700/month; the talk also argues for dogfooding your own product.

- Techniques: Docs-as-markdown synced into the agent's workspace; Two-stage retrieval: embeddings first, then agentic file search; Guardrail CLAUDE.md as the behavior-tuning loop; Escalation reason taxonomy as a product backlog; PaaS deploy from a Dockerfile for fast fix cycles; Monitoring through the existing support tool
- Tools: Claude Agent SDK, Claude Code, CLAUDE.md, Railway, Docker, Pylon, Voyage AI embeddings, AssemblyAI voice agent API, Slack, WebSocket

## [Keyword Search Is Dying. Is Your Catalog Ready for AI Agents? — PayPal](../videos/YXb2Wx1r_Pk.md)
`YXb2Wx1r_Pk` · AI Engineer · 2026-10-05 · q2 · intro · talk · topics: rag-retrieval, data-engineering, product-ux

PayPal's agentic-commerce director argues merchant catalogs were built for human search, not agents, and shows that enrichment helps semantic recommendations while over-enrichment and boilerplate hurt.

- Techniques: Catalog enrichment for semantic retrieval; Head-to-head baseline test of enriched vs unenriched records; Hybrid keyword plus semantic retrieval; Strip boilerplate from agent-facing text

## [Scale the Judgment, Not the Model — Andrew Orobator, Reddit](../videos/6MudaeKdBSk.md)
`6MudaeKdBSk` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · topics: skills-self-improvement, testing-verification, software-factory, context-engineering

Reddit's Andrew Orobator on scaling agent judgment rather than model size: encode institutional judgment as skills, work logs, personas and hard gates, verified by recordings, so coding agents can ship with less human review.

- Techniques: Skills as encoded review judgment; Work log plus commit-hook enforcement; Persona prompting for perspective; Recording-based agent QA; Rules-first funnel for LLM cleanup; OS-level gate with operator-only bypass; Three operating modes; Scheduled skill drift audit
- Tools: Codex, git pre-commit and commit hooks, CI, lint, screenshot-based model review

## [GLM-5.2: Open Weights, Near-Frontier Intelligence — Zixuan Li, Z.ai](../videos/9JFGohx4E7U.md)
`9JFGohx4E7U` · AI Engineer · 2026-10-04 · q2 · intro · keynote · topics: models-research, training-finetuning-rl, coding-agents

Z.ai's Zixuan Li introduces GLM 5.2, an open-weight model he says is near frontier on coding and agentic tasks, and explains why Z.ai opens its weights, plus its Zcode harness.

- Techniques: Open-weight release for on-premise deployment; Vertical fine-tuning on an open base model; Tiered thinking budget; Own harness with bring-your-own-key and compaction
- Tools: GLM-5.2, Zcode, Hugging Face, Codex, Claude Code, OpenCode, Terminal Bench 2.1, Artificial Analysis Intelligence Index

## [Orchestras, Not Factories: How the Fastest Builders Work — Charlie Holtz, Conductor](../videos/TRfzFJCJ7ZE.md)
`TRfzFJCJ7ZE` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: multi-agent, software-factory, coding-agents, sandboxing-execution

Charlie Holtz (Conductor co-founder) lists six principles for fast agent-driven building: stay near the frontier, don't beat the market, mark slot-free zones, feed a central store, run free-range cloud agents, and orchestrate rather than run a factory.

- Techniques: Don't-beat-the-market test; Slot-free zones with CI-enforced human review; CLAUDE.md / AGENTS.md and skills as onboarding material; Central event store with a SQL tool for agents; Cloud sandboxes per task with lifecycle independent of the laptop; Agents calling the product API to create work
- Tools: Conductor, Claude Code, Codex, git worktrees, Postgres, Slack, Discord, Telegram, OpenClaw, React

## [Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa](../videos/cKhpeEBnT1o.md)
`cKhpeEBnT1o` · AI Engineer · 2026-10-04 · q2 · practitioner · talk · topics: rag-retrieval, mcp-and-tools, coding-agents

Exa's forward-deployed engineer explains why coding agents miss recent changes past their model cutoff, and how query-targeted web search snippets, plus explicit search rules, close that gap. Partly a product pitch.

- Techniques: Two-part search instructions for agents; Query-targeted highlight extraction; Full retrieval trace logging; Natural-language schema for structured output
- Tools: Exa search API, Exa Agent, MCP server, Claude Code, CodeRabbit, Cursor

## [Stop Renting Your AI's Memory — Dylan Couzon, Qdrant](../videos/apyrzaWj0Z4.md)
`apyrzaWj0Z4` · AI Engineer · 2026-10-04 · q2 · intro · talk · topics: memory, rag-retrieval, local-ai

Dylan Couzon (Qdrant) argues agent memory should be owned locally: models are rented, but a private, retrieval-based memory store compounds and stays portable. Includes a live offline drone-vision memory demo.

- Techniques: Write-retrieve-forget memory loop; Embedded in-process vector store with per-app folder; Quantized vectors for small footprint; Pin the embedding model for portability; Detector labels then embeddings for perception memory; Opt-in sync of local memory to a shared store
- Tools: Qdrant, YOLO

## [The State of AI in Software Development: Data from 400+ Orgs — Justin Reock, DX](../videos/Se8jHLliLXE.md)
`Se8jHLliLXE` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: enterprise-adoption, observability, pr-code-review

DX's deputy CTO shares 2025-26 data from 400+ orgs: AI lifts delivery speed only modestly, quality volatility grows, and PR size and falling change confidence are the warning signs.

- Techniques: Cohort-vs-foundational-metric comparison; Utilization, impact, cost framing; Agent feedback as telemetry; Agent-readiness audit; Agent first-pass PR review kept in the PR thread; Bottleneck-first AI adoption
- Tools: DORA metrics, DX platform

## [Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI](../videos/48YUYDjwfYY.md)
`48YUYDjwfYY` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: token-cost-efficiency, infra-cost-scaling, coding-agents, sandboxing-execution

Cast.ai's Kimchi team argues for routing each task to the cheapest model that still meets a quality bar, judged by cost per task, with long-running sessions kept alive in remote sandboxes.

- Techniques: Per-task cost-at-quality model comparison; Outcome-scored harness with a grade gate; Milestone-based long-run planning with up-front questions; Remote sandbox session that outlives the client; Team review board for agent sessions
- Tools: Kimchi, Ferment, Teleport, Studio, pi-mono SDK (captioned as 'PyMono SSDK'), Claude

## [Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI](../videos/FQwTqUmcbRg.md)
`FQwTqUmcbRg` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: data-engineering, training-finetuning-rl, infra-cost-scaling, inference-serving

Datology's CTO on running trillion-token synthetic pretraining data jobs: rephrase seeded documents, batch S3 metadata calls, checkpoint for GPU failures, schedule CPU and GPU pools atomically, and sweep vLLM flags.

- Techniques: Seed-based document rephrasing for synthetic pretraining data; Batched S3 metadata listing at maximum page size; Right-sized partitions with checkpointing and idempotent retries; Atomic CPU and GPU scheduling with dedicated pools; Grid search over vLLM and SGLang serving parameters for batch inference; One workflow for research and product in the same infrastructure
- Tools: Ray, KubeRay, vLLM, SGLang, Apache Spark, Kubernetes, Amazon EKS on HyperPod, Slurm, Amazon S3, Parquet, Beyond Web (DatologyAI synthetic data recipe), Nemotron Synth

## [No, That's Not a Software Factory — Ryan Cooke, WorkOS](../videos/HvboD89DyQ8.md)
`HvboD89DyQ8` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: software-factory, mcp-and-tools, context-engineering, skills-self-improvement

Ryan Cooke (WorkOS) on why a sandbox plus coding agent is not a software factory. Build around outcome metrics, webhook-driven product workflows, and an internal MCP gateway.

- Techniques: Outcome-based factory metrics; Webhook-driven ticket pipeline; Agent plan refresh after each step; Agent-drafted PRD with human approval gate; Context-rich MCP gateway; Session mining for skill gaps
- Tools: Linear, Slack, GitHub, Notion, Snowflake, Cloudflare sandboxes, Claude Code, Devin, OpenCode, MCP

## [We're the bottleneck, but we don't have to be — Ido Salomon, AgentCraft](../videos/YIVkERhy8xo.md)
`YIVkERhy8xo` · AI Engineer · 2026-10-04 · q2 · intro · talk · topics: multi-agent, product-ux, coding-agents, software-factory

Ido Salomon (AgentCraft) argues that humans are the bottleneck in agent work and demos a game-style orchestrator with attention-jumping, a map view, review kits, shared rooms, and a simpler "loopers" mode for non-engineers.

- Techniques: Attention queue with jump-to-next; Spatial projection of agent activity; Review kit for parallel agent output; Orchestrator with isolated local containers and background loops; Shared room with cross-agent notice board; Progressive disclosure for low-floor use
- Tools: AgentCraft, Claude Code, Codex, OpenCode, OpenClaw, Git, Telegram, MCP Apps (MCPUI)

## [Get Out of the Model's Way — Kevin Hou, Google Antigravity](../videos/buHC7bQE1X4.md)
`buHC7bQE1X4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: multi-agent, coding-agents, product-ux, agent-architecture

Google's Antigravity lead on building agent products that get out of the model's way: subagent teams, sidecar triggers and generative UI, with cost and token stats from a kernel-building run.

- Techniques: Dynamic subagent teams under a lead agent; One subagent per hypothesis fan-out for eval deltas; Skills file plus natural language for internal workflow automation; Sidecar trigger process; Generative UI in the conversation instead of fixed screens; Separate the orchestration surface from the editor; Primitive audit against the next model
- Tools: Google Antigravity, Antigravity CLI, Antigravity 2.0 agent manager, Gemini 3.5 Flash, MCP, Cloud sandboxes and remote execution (unnamed), Windsurf (reference only)

## [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](../videos/_mi3alkqy4s.md)
`_mi3alkqy4s` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · topics: pr-code-review, evals, testing-verification, observability

Laurie Voss (Arize AI) argues that agent code generation has outrun human review, so teams should stop reviewing PRs by hand and build an engineered review harness, with humans designing its definition of good.

- Techniques: Multi-pass review with consensus filtering; Default-suspicious reviewer prompt; Tool-using reviewer over the whole repo; Runtime verification by the agent itself; Machine-checkable mergeability rubric; Codify the definition of good as a harness
- Tools: GitHub Copilot code review, Cursor reviewer, CodeRabbit, Greptile, Graphite, Codex, Anthropic automated security review action, SWE-bench, SWE-bench Pro, FrontierBench

## [An Interaction Is All You Need — Ivan Leo, Google DeepMind](../videos/8aVbXXvJUY4.md)
`8aVbXXvJUY4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: agent-architecture, sandboxing-execution, security-guardrails, mcp-and-tools

Google DeepMind's Ivan Leo presents the Interactions API and Managed Agents: server-side state via interaction IDs, persistent sandboxes via environment IDs, and a credential-injecting proxy. Mostly a product walkthrough with a few reusable patterns.

- Techniques: Server-side conversation state via interaction ID; Reattach to a persistent sandbox via environment ID; Proxy-side credential injection; Freeze a tuned environment as a named agent; Local-to-cloud skill packaging; Strongly typed output parsing
- Tools: Interactions API, Managed Agents, Antigravity agent harness, Gemini API CLI, AI Studio, Google Search tool, URL context tool, GCS, GitHub

## [MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](../videos/pAnLpiAG6Es.md)
`pAnLpiAG6Es` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: mcp-and-tools, context-engineering, coding-agents

Apify's CEO argues MCP's problems come from agent harnesses, not the protocol. He covers progressive tool discovery, code mode, and CLIs, then pitches MCPC, a CLI wrapper for MCP.

- Techniques: Progressive tool discovery; Code mode for tool calls; Keep large or sensitive tool output out of context; Wrap MCP in a CLI and give the agent bash; Async tool invocation with detach and poll; Connector evals
- Tools: MCP, MCPC, Claude Code, Claude Tool Search Tool, Cloudflare code mode, Bash, jq, Terminal Bench

## [Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous](../videos/HLTa7Vcs4X0.md)
`HLTa7Vcs4X0` · AI Engineer · 2026-10-04 · q2 · intro · demo · topics: testing-verification, pr-code-review

A short vendor demo arguing that review and verification, not code writing, are now the bottleneck, and that screenshot-based record-and-replay of front-end flows can give near-exhaustive verification.

- Techniques: One-line record of real user flows in non-prod; Per-step screenshot diff of base vs PR; Record-time network mocking with replay-time stubs; Coverage-maximizing test subset selection
- Tools: Meticulous, Cypress, Playwright

## [GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe](../videos/bRGyYaE0lxI.md)
`bRGyYaE0lxI` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: infra-cost-scaling, training-finetuning-rl, inference-serving

Crusoe engineers explain how they run Slurm on Kubernetes so failed GPU nodes are cordoned, replaced and the training job resumes from checkpoint with no user action, with a live demo.

- Techniques: Automated GPU failure remediation loop; Opt-out label check before node replacement; Checkpoint on SIGTERM grace window; Slurm operator on Kubernetes (Slinky pattern); Shared GPU pool across training and inference
- Tools: Slurm, Kubernetes, Slinky (SchedMD), sbatch, srun, PyTorch, Crusoe Managed Kubernetes (CMK), Crusoe AutoClusters, Crusoe Slurm operator

## [I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j](../videos/oUZEt4EiPbk.md)
`oUZEt4EiPbk` · AI Engineer · 2026-10-04 · q2 · intro · demo · topics: memory, agent-architecture, mcp-and-tools, sandboxing-execution

Neo4j's Jeremy Adams builds a personal agent on a Raspberry Pi 4B: NanoClaw in Docker, WhatsApp as the channel, cloud LLMs, and graph memory, with a live demo and an offline capture mode for conference Wi-Fi.

- Techniques: Edge orchestrator, cloud brain; Container per agent process; Messaging app as the agent front end; Graph database as an MCP tool; Offline-first capture with deterministic parsing and later sync; Typed entity memory schema written as a skill; Batch distillation of chat history
- Tools: Raspberry Pi 4B, NanoClaw, OpenClaw, Claude Agent SDK, WhatsApp, Telegram, Docker, Neo4j, Neo4j Aura, Cypher, MCP, Neo4j agent memory service

## [Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava](../videos/qflLT3SoVbw.md)
`qflLT3SoVbw` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: context-engineering, rag-retrieval, training-finetuning-rl, memory

Anant Srivastava argues enterprise teams should decide deliberately whether knowledge lives in the prompt, in retrieval/memory, or in fine-tuned weights, using rate of change, scope, and behavior-vs-facts as the test.

- Techniques: Knowledge placement diagnostic; Retrieval-first debugging; Fine-tune the stable center, keep humans on the edge; Code-aware chunking with denormalized metadata; Promote-and-prune memory loop; Small fine-tuned model for cost

## [Building Self-Improving Agent Software Factories — Suraj Gupta, Warp](../videos/TN3mj92oZ8I.md)
`TN3mj92oZ8I` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: software-factory, skills-self-improvement, memory, token-cost-efficiency

Warp's Suraj Gupta on making agent software factories self-improve through outer-loop skill edits gated by PR review, agent-scoped versioned memory, and rule-based model routing for cost.

- Techniques: Outer-loop skill improvement with PR gate; Agent-scoped fact memory with provenance; Rule-based model routing by task class; Best-of-k model sampling to learn routing
- Tools: Warp, Oz (Warp cloud agent platform), Sentry, GitHub, Codex, Claude Code, Opus, Haiku, GLM, Qwen

## [Dashboards Are Dead — Sarah Simionescu, Composio](../videos/YiFqcu9YA38.md)
`YiFqcu9YA38` · AI Engineer · 2026-10-04 · q2 · intro · talk · topics: mcp-and-tools, context-engineering, product-ux

Composio's Sarah Simionescu argues agents should replace dashboards, and that MCP servers need task-scoped tool discovery to work. Vendor pitch with a mock-up demo.

- Techniques: Task-first tool discovery; Parallel fetch after planning; Keep bulky results out of context; Schema-first exploration before querying; Bug-report prompt to an agent with connected tools
- Tools: Composio (MCP, CLI, native tools, Composio Search, Composio Remote Workbench), Claude, MCP (Model Context Protocol, announced by Anthropic Nov 2024), Datadog, Sentry, Slack, GitHub, Jira (JQL), VS Code, PostHog, Metabase, SQL

## [The Chief AI Officer: Scientist, Architect, Coach — Rania Khalaf, WSO2](../videos/9cJrbj23fOA.md)
`9cJrbj23fOA` · AI Engineer · 2026-10-04 · q3 · intro · talk · topics: enterprise-adoption, governance-compliance, product-ux

WSO2's Chief AI Officer Rania Khalaf on running the role as scientist, architect and coach, with adoption-based metrics instead of token counts.

- Techniques: Three-dimension role mapping; LLM-assisted role analysis; Adoption depth ladder; Agent-ready product checklist; Dogfooding with a closed feedback loop
- Tools: Claude, Gemini, BERT, MCP, Databricks

## [How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner](../videos/I2LL_wd89-A.md)
`I2LL_wd89-A` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · topics: software-factory, pr-code-review, testing-verification, context-engineering

How the VS Code team moved from monthly to weekly releases by rebuilding its own dev system around agents: code-survival metrics, agent-readable repos, fast CI, UI feedback loops, AI triage, and staged rollouts.

- Techniques: Code survival metric; Agent-readable repo docs; Expert knowledge as a shared skill with an area owner; Screenshot-diff component browser; Self-correcting launch loop; Tiered AI code review; Deterministic filtering before agent action; Staged rollouts with error monitoring; Evals bootstrapped from issues; Prototypes instead of PRs for design talks
- Tools: VS Code, GitHub, GitHub Issues, GitHub Copilot code review, TypeScript Go, Playwright, Electron, Xcode MCP, AGENTS.md, Chrome extension

## [Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase](../videos/5xi_S1f9sDU.md)
`5xi_S1f9sDU` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: voice-multimodal, testing-verification, agent-architecture

Why 99%-accurate browser agents still fail in production, and how moving deterministic steps out of the model and verifying outcomes makes transactional browser workflows profitable.

- Techniques: Three browser interaction strategies; Transactional scope for browser agents; Per-transaction success with bounded retries; Artifact-based success check; Single-transaction tool encapsulation; Deterministic auth outside the model; Skill as SOP for the critical path
- Tools: Browserbase, Chrome DevTools Protocol (CDP), OCR, accessibility tree, serverless functions

## [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](../videos/OE_lLNCNfQo.md)
`OE_lLNCNfQo` · AI Engineer · 2026-10-04 · q2 · intro · talk · topics: sandboxing-execution, security-guardrails, governance-compliance

Docker's product manager argues coding agents need micro-VM sandboxes with secret placeholders and default-deny egress, and shows a self-test where Claude Code found his bank data. Mostly a product pitch.

- Techniques: Run agents in a micro-VM with bypass permissions on; Placeholder secrets swapped at the network boundary; Default-deny egress with an allowlist; Read-only mounts of context repos; Self red-teaming with real personal data
- Tools: Docker SBX, Claude Code, Claude Desktop, Codex, CrowdStrike, Cedar, Datadog

## [What Makes Open Models Fast in Production — Sujee Maniyam, Nebius](../videos/TRe1u7dHYiA.md)
`TRe1u7dHYiA` · AI Engineer · 2026-10-04 · q2 · intro · talk · topics: inference-serving, infra-cost-scaling

Nebius Token Factory explains the serving optimizations behind fast open-model inference: cache-aware routing, speculative decoding, KV-cache offload, and prefill/decode separation. It is mostly a product pitch with few measured results.

- Techniques: Cache-aware request routing; Speculative decoding with a self-trained draft model; KV-cache offload to host memory; Prefill/decode disaggregation; Per-model engine and precision selection
- Tools: Cursor, OpenCode

## [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](../videos/vGCJ7diEtrw.md)
`vGCJ7diEtrw` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · topics: software-factory, infra-cost-scaling, testing-verification, context-engineering

Factory's engineer defines a "software factory" as a full autonomous lifecycle, not coding agents. Covers model routing for cost, verifiable done-criteria, sequential worker and validator missions, deferred tool loading, and codebase readiness.

- Techniques: Difficulty-classified model routing; Validation contract written before coding; Sequential workers with fresh context per handoff; Two-tier validation; Deferred tool loading; Codebase readiness audit; Codify tacit rules as skills or plugins
- Tools: Factory (software factory platform), Factory missions (orchestrator, worker and validator agents), Automatic model routing, Deferred context engine, Agent readiness framework, Plugins, Auto-wiki, Slack, GitHub, Figma, Notion, Gmail

## [Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band](../videos/UOcHfR3_tys.md)
`UOcHfR3_tys` · AI Engineer · 2026-10-04 · q2 · practitioner · talk · topics: multi-agent, mcp-and-tools, agent-architecture, governance-compliance

Vendor talk by Band's CTO arguing that multi-agent coordination needs a conversation-level collaboration layer (rooms, consent, routing, governance), not just MCP or A2A, then demoing that product.

- Techniques: Bilateral consent before agent-to-agent contact; Rooms and channels with deterministic routing as the agent primitive; Network-level traffic capture for cost and attribution; Live architecture layout reporting from agents; Human-in-the-loop pings and manager kill switch
- Tools: Band (collaboration layer / platform, speaker's company), Jam (desktop app built on Band, also called 'GEM' near the end of the transcript; the name is ambiguous in captions), Claude Code, Codex (OpenAI), LangGraph (LangChain), MCP (Model Context Protocol), A2A (Agent-to-Agent protocol), ACP (protocol, named without detail), Telegram, Discord, Slack, WhatsApp

## [The 5 Levels of Self-Driving Production — Eric Schwartz, Traversal](../videos/y-OVWZD4j6U.md)
`y-OVWZD4j6U` · AI Engineer · 2026-10-04 · q2 · intro · talk · topics: observability, enterprise-adoption, product-ux

Traversal's PM argues AI coding agents shift engineering time from building to troubleshooting, and proposes a five-level "self-driving production" autonomy scale plus five criteria for judging AI SRE tools.

- Techniques: Five-level autonomy scale for incident response; Five-question checklist for evaluating AI SRE tools; Causal root cause framing for multi-hop incidents; Agent-first incident intake; Alert triage pass before on-call
- Tools: Traversal (AI SRE product; production world model and causal search engine), Claude Code (auto-caption "Cloud Code"), Codex, Cursor, Datadog, Elastic, Splunk, ServiceNow, Slack

## [AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile](../videos/474j-n1Ltxc.md)
`474j-n1Ltxc` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · topics: pr-code-review, coding-agents, evals

Greptile's Daksh Gupta uses review data from its own PR pipeline to test whether fully agent-written PRs are worse than human PRs; his answer is roughly no on reverts, severity and review rounds, but failure modes differ by agent.

- Techniques: Signal-based detection of agent-authored PRs; Proxy quality metrics for agent PRs; Per-agent failure-mode profiling via keyword counts; Three-question PR validation gate
- Tools: Greptile, Codex, Claude Code, Devin, Cursor, GitHub

## [Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog](../videos/rTojoVotlD8.md)
`rTojoVotlD8` · AI Engineer · 2026-10-04 · q3 · intro · talk · topics: observability, governance-compliance, evals, security-guardrails

Datadog's Marina Petzel argues LLM apps need cost, safety and quality monitoring on top of the golden signals, since a 200 OK can still hide a wrong answer; gives tagging and metric recommendations.

- Techniques: Mandatory four-level cost tagging; Track token creep and model drift as separate alerts; Caching layer to remove redundant completions; Guardrail metrics as blocking thresholds; LLM-as-judge for completeness, embeddings for relevance; Score RAG retrieval separately
- Tools: Datadog agent observability

## [Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp](../videos/tUPPVhBBcoM.md)
`tUPPVhBBcoM` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · topics: software-factory, skills-self-improvement, pr-code-review, observability

Warp's founder argues software engineering is becoming factory engineering: agent loops run from triage to spec to implementation to monitoring, with humans gating stuck points and observer agents improving the skills.

- Techniques: Software factory loop with human gates; Triage routing by ambiguity; Product spec plus tech spec; Observer agent skill loop; Verification by running the product
- Tools: Warp, Claude Code, CI/CD, GitHub, Computer use

## [Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash](../videos/ACPEpji5NV4.md)
`ACPEpji5NV4` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: rag-retrieval, data-engineering, memory, evals

DoorDash's search and personalization lead on using LLMs offline to create graded relevance labels, semantic IDs, and memory, then serving those through small, fast models.

- Techniques: Offline LLM labeling with a distilled labeler; Label-audit by disagreement; Two-stage contrastive retrieval with hard-negative curriculum; Auxiliary ordinal relevance tower with value-function blend; Hierarchical learned semantic IDs as sparse features; Multi-form consumer memory blocks; Batch generation of personalized content with the existing ranking stack
- Tools: GPT-4o mini (named as an example lightweight labeler)

## [Why LLM Recommenders Will Be AI's Biggest Consumer App — Devansh Tandon, Meta](../videos/lIgdnF0s0kQ.md)
`lIgdnF0s0kQ` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · topics: models-research, product-ux, infra-cost-scaling

Devansh Tandon (Meta) argues recommenders scale like LLMs, lays out four recommender S-curves, gives a three-step recipe for LLM recommenders built on semantic IDs, and claims feeds are far more token-efficient than chat apps.

- Techniques: Semantic ID tokenization of content; Bilingual LLM pre-training on semantic IDs; Post-training LLM rerankers with chain of thought; Shared base model with thin per-surface fine-tuning; Agentic recommendation loop
- Tools: Semantic IDs, HSTU, Tiger, Plum, Gemini, Claude Code, Codex

## [Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta](../videos/jNE8No-wvok.md)
`jNE8No-wvok` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · topics: multi-agent, voice-multimodal, evals, training-finetuning-rl

Meta's Aditya Gautam on using a multi-agent system of small domain-tuned VLMs to find intra-video policy anomalies and duplicate content in short-form video, with a production judge-and-human feedback loop.

- Techniques: Orchestrator plus specialist agents for video review; Change-based frame compression; Per-signal index routing; Domain pre-training plus schema-constrained instruction tuning; Judge-plus-human-queue production loop; Distillation plus quantization sweep; Node-level evaluation suite; Pre-inference gating with cache and metadata
- Tools: CLIP, MCP, Ray, DPO, JSON schema, vector database, graph database, inverted index

## [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](../videos/x4e5O9zN0TE.md)
`x4e5O9zN0TE` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: evals, skills-self-improvement, memory, multi-agent

Long-running, stateful agents need controlled scenario suites, balanced scorecards and a ratchet loop, not just prompt tweaks; the speaker's case study is a game-village multi-agent system tuned by an outer auto-research loop.

- Techniques: Controlled scenario suite with ground truth; Balanced behavioral scorecard with guardrails; Frozen-harness ratchet loop; Structured run-trace logging; Importance-scored memory with a threshold cache; Provenance and confidence tags on memories; Separate episodic memory from current belief
- Tools: Project Paradox (in-house framework), RAG-backed per-agent memory, auto-research loop (Karpathy-inspired)

## [We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect](../videos/oVsEddfhdxc.md)
`oVsEddfhdxc` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: coding-agents, claude-code, models-research, evals

Prime Intellect's Elie Bakouch runs Claude Code and Codex on an optimizer speedrun against human records, finding both beat the records but neither produced a novel optimizer, and that Claude Code idled while Codex kept working.

- Techniques: Speedrun as a verifiable research environment; Constrained variants to force novelty; Goal file plus rules file as the agent's contract; Restart with the latest best state; Behavior logs normalized by active time; Generator, judge and scale-up loop
- Tools: Claude Code, Codex, Slurm, AGENTS.md, goal.md, Verifiers, Prime-RL, Hosted Training, Kimi K2.7, GLM

## [World Models Need Causality, Not Pretty Pixels — Christopher Manning, Moonlake AI](../videos/4Gqg0HVe-AY.md)
`4Gqg0HVe-AY` · AI Engineer · 2026-09-27 · q3 · intro · talk · topics: voice-multimodal, models-research, training-finetuning-rl

Christopher Manning of Moonlake AI argues that world models for physical AI need abstracted, causal, editable representations rather than beautiful pixels, and proposes code-based neurosymbolic simulators that can be verified and used for sim-to-real transfer.

- Techniques: Action-conditioned semantic world model; Code as the controllable scene representation; Render-compare-revise loop; Retrieval to fill unobserved state; Task-driven fidelity budgeting; Neural sim-to-real gap reduction
- Tools: Genie 3, Marble, JEPA, Claude, physics engines, diffusion models, RAG over web search

## [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](../videos/OA-Mc60Rboo.md)
`OA-Mc60Rboo` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: skills-self-improvement, evals, context-engineering, training-finetuning-rl

GEPA's Lakshya Agrawal explains reflective, text-space optimization: LLMs read full rollout traces and rewrite prompts, skills or harness code, with a Pareto pool, beating GRPO on sample efficiency.

- Techniques: Reflective prompt / artifact optimization loop; Pareto candidate pool selection; Actionable side information from the evaluator; Three optimization modes in one API; Optimize the agent file itself; Repo skill learning from trajectories; Judge-then-agent data flywheel
- Tools: GEPA (open-source, includes the optimize_anything API and a skill-learning feature), GRPO (used as the RL baseline), Claude Opus, Claude Sonnet 4.5, GPT-5 mini, GPT-4.1, GPT-4.1 nano, Gemini Flash, mini-SWE-agent, Claude Code, Codex, LLM-as-judge

## [The Loop Is the Product — Roland Gavrilescu, Introspection](../videos/7taOQBfjDyE.md)
`7taOQBfjDyE` · AI Engineer · 2026-09-27 · q2 · intro · talk · topics: skills-self-improvement, evals, agent-architecture, product-ux

Introspection's Roland Gavrilescu argues self-improving agent loops should distill a team's taste into versioned recipes of evals, judges and skills, validated in production and measured as value per watt.

- Techniques: Trace pattern clustering to find signals; Agent-drafted judges with human calibration; Recipe diffs as reviewable candidates; Production A/B or bandit promotion; Per-model harness profiles
- Tools: Py.Recipes, Harbor, OpenClaw (originally CloudBot), Claude Code, Codex, Cursor, Cognition

## [The Best Models Still Reason Like Toddlers — Andrew Dai, Elorian](../videos/A_I8mw8yfns.md)
`A_I8mw8yfns` · AI Engineer · 2026-09-27 · q2 · intro · talk · topics: voice-multimodal, models-research, evals

Elorium's CEO argues frontier models (Claude, ChatGPT, Gemini) pattern-match instead of reasoning over images and video, and proposes visual chain-of-thought trained on synthetic data as the fix.

- Techniques: Keep visual sub-tasks simple; One-second test for task difficulty; Visual chain of thought; Synthetic data flywheel for a hard modality; Programmatic or simulator validation of outputs
- Tools: Google Lens, SAM3, YOLO, Mask R-CNN, Siemens simulators, ByteDance Seedance (rendered as C-Dance in transcript)

## [Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph](../videos/vrDvatGtIxs.md)
`vrDvatGtIxs` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: inference-serving, testing-verification, agent-architecture

Morph's Tejas Bhakta shows a propose-benchmark-keep-or-revert loop (autoresearch) tuning GPU kernels for about 3x speedup, with human-supplied ideas and explicit guards against reward hacking.

- Techniques: Keep-or-revert benchmark loop; Split the work: human ideas, loop parameters; Profile before tasking the agent; Hardware and model context files in the harness; Explicit anti-cheat rules in the benchmark; Stack kernels and keep fallbacks; Switch models when one fails at the DSL
- Tools: Nsight Systems (NSYS), CUDA, CUDA graphs, CuTe DSL, CUTLASS, FlashInfer, NVFP4, Autoresearch (Karpathy)

## [Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face](../videos/dKcTBQzR7jI.md)
`dKcTBQzR7jI` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · topics: voice-multimodal, data-engineering, training-finetuning-rl, evals

Merve Noyan (Hugging Face) argues against running VLMs for real-time vision and shows a pipeline where VLMs label and judge data to train small Apache-2.0 detectors such as RF-DETR, plus a toolkit of models exposed as agent tools.

- Techniques: VLM as offline labeler, small detector at runtime; Overlay-and-ask judging; Ensemble of small judges with any-yes merge; License-first model selection; Agent with domain rules and human checkpoints; Models exposed as agent tools
- Tools: RF-DETR, Gemma 4 E4B, LFM2.5-VL, Qwen VLM (auto-caption reads 'Q1 3.5', ~3.5B), Falcon Perception, Moondream 3, MM Grounding DINO, SAM 3.1, Supervision (Roboflow), Hugging Face Jobs, Hugging Face Inference Providers, Hugging Face buckets

## [From VLM/VLA's to Embodied Agents — Armen Aghajanyan, Perceptron AI](../videos/ZZcE0HeO-Hc.md)
`ZZcE0HeO-Hc` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · topics: voice-multimodal, models-research, training-finetuning-rl

Perceptron's CEO argues VLMs, VLAs and world models should merge into one "embodied foundation model," and shares sparsity, token-routing and data-mix findings with public benchmarks but few hard details.

- Techniques: Data-sparse MoE token routing; Agentic detection with zoom, tiling and contrast; Orchestrator plus low-level control policy; Self-verifying video annotation; Online augmentation for robustness; Patch averaging for token compression
- Tools: Gemini 3.1 Pro, Gemini Embodied Reasoning, Perceptron models (Mark 1)

## [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](../videos/SQMCtZX3trg.md)
`SQMCtZX3trg` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: skills-self-improvement, coding-agents, context-engineering, evals

Paul Bakaus (Impeccable) on building production agent skills as harness extensions: blind sub-agents, forced divergence, scripts, hooks and per-model builds, rather than prose alone.

- Techniques: Blind adversarial critique; Anti-attractor divergence; Register routing inside one skill; Cross-session skill memory; Scripts that print next-step instructions; Pre-tool-use blocking hooks for weaker models; Hook-driven feedback loop from a skill; Unskippable gates with logged results; Per-harness and per-model builds; Ablation testing of rules; LLM-as-user with a judge panel; Inverted judges
- Tools: Claude Code, Codex, Cursor, GitHub Copilot, Gemini, Playwright, skills.sh, npx skills

## [Teaching LLMs to Speak Spotify — Yves Raimond & Jacqueline Wood, Spotify](../videos/2LRIAfng7eA.md)
`2LRIAfng7eA` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: training-finetuning-rl, evals, product-ux

Spotify's engineers explain turning recommendations into a steerable LLM: semantic-ID tokens, a four-stage NEO training recipe, and LLM judges grounded in behavioral data.

- Techniques: Semantic-ID tokenization and vocabulary extension; Frozen-backbone domain grounding; Staged training: grounding, then multi-task instruction tuning, then optional RL; Beam search over constrained decoding for ID generation; Grounding LLM judges with user profiles and behavioral signals; LLM judges for Cranfield-style relevance pools
- Tools: Qwen, LLaMA, LoRA, NEO (Spotify's training paradigm, linked paper), Discover Weekly, Spotify DJ

## [An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases](../videos/hd7TOvmyAxU.md)
`hd7TOvmyAxU` · AI Engineer · 2026-09-27 · q2 · practitioner · demo · topics: evals, observability, agent-architecture, training-finetuning-rl

Live demo of W&B's ARIA research agent running autoresearch experiments, plus its trace-to-eval loop: production traces, LLM judges, nightly YAML task suites, and promotion gated on eval scores.

- Techniques: Eval suite as YAML unit tests; Production traces to tasks loop; Live LLM judges as signal detectors; Eval-gated promotion; Async job dispatch from an agent; Agent analyzes its own traces
- Tools: Weights & Biases Weave, W&B Launch, W&B Inference, W&B Artifacts, W&B Reports, CoreWeave sandbox, Kubernetes, iOS app

## [Robotics Has Been Stuck for 70 Years — Deepak Pathak, Skild AI](../videos/jFHteJjRl8A.md)
`jFHteJjRl8A` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: voice-multimodal, training-finetuning-rl, models-research, data-engineering

Deepak Pathak (Skild AI) argues robotics lacks internet-scale data, so the answer is one omnibodied brain pretrained on diverse data, post-trained on teleop, and improved by a deployment data flywheel.

- Techniques: Pretrain on diverse, scalable data, post-train on small high-quality teleop; Deployment data flywheel; End-to-end camera-to-motor policy with only a low-level PID loop; Learn from human video, then adapt with minimal robot data; Cross-embodiment zero-shot transfer

## [Fixing the PR Bottleneck — Matt Pocock, AIHero](../videos/LlgiOCmFG_w.md)
`LlgiOCmFG_w` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: pr-code-review, software-factory, testing-verification, context-engineering

Matt Pocock on clearing the PR backlog that AI agents create: layer cheap deterministic checks, have an agent review and commit fixes, design deep modules so tests stop being brittle, and run a retro on each session.

- Techniques: Layered brakes for agent PRs; Deep-module design for agent-testable code; Separate implementer and reviewer contexts; Reviewer commits fixes, comments only on open questions; Door-type and blast-radius PR summary; Pseudocode and diagram PR explanations; Retro over sessions and PRs
- Tools: AGENTS.md, coding-standards.md, CodeRabbit, Cursor BugBot, PlanetScale, Opus 5 (model mentioned in the tautological-test example), AIHero skills (version 1.3 announced for the same week)

## [One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio](../videos/2wgPHvW0mG8.md)
`2wgPHvW0mG8` · AI Engineer · 2026-09-27 · q3 · intro · talk · topics: multi-agent, voice-multimodal, agent-architecture, infra-cost-scaling

Skydio's Suchet Bargoti on running fleets of docked drones as agent-commanded infrastructure: tool-based VLM control, edge/cloud latency tiers, a shared map that the fleet updates, and a learning flywheel.

- Techniques: Tool-exposed primitives for a VLM agent; Latency-tiered edge and cloud split; Fleet-shared map with sync-back; Bandwidth-aware video encoding for cloud agents; Hybrid end-to-end versus hand-engineered decomposition; Log, sanitize, retrain, redeploy loop
- Tools: Vision-language model (VLM), Reinforcement learning, Drone APIs exposed as agent tools, Cloud GPUs and inference engines, Map merging and sync service

## [Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics](../videos/Sjfz1TqxzEs.md)
`Sjfz1TqxzEs` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · topics: training-finetuning-rl, evals, voice-multimodal

Dyna Robotics co-founder on making generalist robot manipulation policies reliable enough for commercial use, via reward-model progress scoring and a targeted active-learning loop.

- Techniques: Reward model as progress scorer for background supervision; Failure-driven active learning loop; Pre-train, post-train, then active learn; Grade-based success criteria tied to customer acceptance; Two-level architecture

## [I Gave an AI a Body — Cyrus Clarke, MIT Media Lab](../videos/jgWY66RaSrQ.md)
`jgWY66RaSrQ` · AI Engineer · 2026-09-27 · q3 · intro · talk · topics: voice-multimodal, product-ux, agent-architecture

MIT Media Lab researcher Cyrus Clarke gives an OpenClaw agent a 900-pin shape display and has it build its own gesture vocabulary, arguing for non-humanoid, aesthetics-led physical AI.

- Techniques: Closed-loop gesture generation with gates and scoring; Pre-authored action repertoire to cut latency; Neutral embodiment with no affordances; Open-ended exploration prompt with machine access
- Tools: OpenClaw, openFrameworks, Numalab (speaker's own system), Shape display (physical pixel grid, 900 pins)

## [From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam](../videos/T72nqdC92PM.md)
`T72nqdC92PM` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · topics: data-engineering, training-finetuning-rl, models-research, voice-multimodal

Sarvam's Krishna Prasad Srinivasan on training Servam Vision, a 3B state-space document-OCR model built from scratch for English and 22 Indian languages, using block-level OCR, a four-stage curriculum and RL with machine-checkable rewards.

- Techniques: Block-level OCR with layout and reading-order modules; Four-stage training curriculum for a domain VLM; RLVR with unit-test rewards; Real complex documents as RL reward sources, synthetic documents for SFT; Human-in-the-loop workbench with confidence scores and block grounding
- Tools: Servam Vision, Akshar (agentic document workbench), OlmOCR-Bench, OmniDocBench, Qwen, Gemma

## [Physical AI's Next Bottleneck Is Finding the Right Video — Rafael Levi, Bright Data](../videos/I_VEh7XSwyc.md)
`I_VEh7XSwyc` · AI Engineer · 2026-09-27 · q2 · intro · talk · topics: data-engineering, voice-multimodal

Rafael Levi (Bright Data) argues physical-AI training is limited by usable action data, not models, and pitches searching indexed public video by action before collecting it.

- Techniques: Action-based clip retrieval before collection; Frame-to-frame motion estimation from plain video; Descriptive queries for retrieval
- Tools: Bright Data video indexing API

## [You’re Not Thinking Big Enough: Rebuilding Food Systems with AI Agents — Cody Menefee, Firecrawl](../videos/ztlXKfPCT3Q.md)
`ztlXKfPCT3Q` · AI Engineer · 2026-09-27 · q2 · intro · talk · topics: context-engineering, data-engineering

Firecrawl growth engineer Cody Menefee argues LLM agents could help automate rotational grazing for livestock, with the LLM suggesting moves and a human confirming, plus a recruiting pitch for Firecrawl.

- Techniques: Human-confirmed LLM suggestions over multivariate data; Knowledge base from scattered web sources; Context gathering and packaging for LLM reasoning; Fixed reference object for remote measurement; Model the decision at several levels
- Tools: Firecrawl, OpenPasture, Halter, NoFence, Planet satellite imagery, trail camera

## [How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases](../videos/XyV6bSMyq-I.md)
`XyV6bSMyq-I` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · topics: evals, skills-self-improvement, observability, agent-architecture

Weights & Biases walks through how its ARIA agent evaluates and improves itself: production traces become offline regression tasks, and the agent runs its own hill-climbing loop.

- Techniques: Eval flywheel from production traces; Byte-identical prod and research agent with a sync job; YAML-defined config variants; Three task simulation modes; Dual scoring: pass/fail plus pairwise relative scoring; Unconstrained sandbox for agent research loops
- Tools: Weights & Biases Weave, W&B Reports, ARIA agent, Claude Code, YAML task and config specs

## [Building the Document Context Layer for AI Agents — Jerry Liu, LlamaIndex](../videos/RQi7x-navxU.md)
`RQi7x-navxU` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · topics: rag-retrieval, context-engineering, data-engineering

Jerry Liu (LlamaIndex) argues agents need a document context layer: fast local parsing by default, VLM escalation for hard pages, and cost-aware routing between specialized and frontier models.

- Techniques: Fast-pass then escalate parsing; Hybrid pipeline plus VLM parsing with routing; Regime-based pipeline selection; Structured extraction with provenance and confidence gating; Multi-tool agent retrieval over documents; Accuracy-cost-latency Pareto benchmarking
- Tools: LlamaParse, LightParse, ParseBench, Claude Code, Claude Cowork, Codex, OpenClaw, MCP, BM25, grep, PyPDF, PyMuPDF

## [From Ingestion to Agents: How AI Teams Build on Document Intelligence — Adit Abraham, Reducto](../videos/0I07YAuF8xA.md)
`0I07YAuF8xA` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · topics: data-engineering, rag-retrieval, agent-architecture, evals

Reducto's CEO on why document ingestion decides agent quality: decompose parsing into specialised tools, verify rather than regenerate, store table forms split by job, and eval every pipeline stage.

- Techniques: Decomposed parsing stack; Targeted verification instead of regeneration; Dual table representation; Classify and split before extraction; Agent harness for chart reconstruction; Parent-subagent validation criteria; Per-stage evals
- Tools: Reducto, Gemini, OpenAI models, Anthropic models, Cursor (as analogy for speculative edits), code interpreter

## [The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI](../videos/Hvb2LfMH58c.md)
`Hvb2LfMH58c` · AI Engineer · 2026-09-20 · q2 · intro · talk · topics: inference-serving, infra-cost-scaling, agent-architecture

FriendliAI's CEO argues agent workloads need task-level (end-to-end) latency optimization, not per-request speed, and pitches prefix caching, KV cache management and cache-aware routing on an open-weight inference cloud.

- Techniques: Prefix KV caching for agent steps; Tiered KV cache with quantization and cross-replica sharing; Cache-aware routing with load-aware fallback; Optimize end-to-end task latency as the target metric; Agent-aware scheduling (described as future work)
- Tools: vLLM, GLM 5.2, Kilo Code, Claude Opus 4.8, MiniMax, Kimi

## [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](../videos/xs-ob87TTzg.md)
`xs-ob87TTzg` · AI Engineer · 2026-09-20 · q3 · practitioner · workshop · topics: memory, agent-architecture, context-engineering, skills-self-improvement

Oracle workshop on agent harness design: a 30-minute framework for agent memory (files vs databases, memory types, context rot, skill promotion), then a hands-on notebook build, with heavy Oracle product promotion.

- Techniques: Hybrid storage split; Per-agent git worktrees for file edits; Context card; Toolbox / skillbox index with vector retrieval; LLM-enhanced tool descriptions; Patience (hysteresis) budget for agent loops; Skill promotion by distillation; Difficulty-based model routing
- Tools: Oracle Database (converged: JSON, relational, spatial, graph, vector), Oracle DBFS, Oracle Agent Memory Package (OAMP), LangChain Oracle DB integration, OCI Generative AI service, GitHub Codespaces, Grok 4.1 Fast Reasoning, HNSW vector indexes, git worktrees, Python 3.12 notebook

## [Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI](../videos/sOB3HSiG8vo.md)
`sOB3HSiG8vo` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · topics: infra-cost-scaling, inference-serving

OpenAI's inference team explains how its inference load balancer moved from a feedback-loop weight controller to a control-plane/data-plane design that optimizes end-to-end latency, plus retry budgets, outlier penalties and load shedding for production stability.

- Techniques: Control-plane / data-plane routing split; Latency-minimizing routing weights; Outlier penalty by weight reduction; Utilization-dependent retry budget; Proactive load shedding

## [Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards — Filip Makraduli](../videos/c1hGBoWw20A.md)
`c1hGBoWw20A` · AI Engineer · 2026-09-20 · q4 · deep · talk · topics: inference-serving, models-research

Filip Makraduli on "flash norm": algebraic rewrites of RMSNorm (weight folding, deferred division) that speed up transformer decoding, plus a CUDA stream race that corrupted long generations.

- Techniques: Weight folding of norm gain into the next linear layer; Deferred scalar division for overlap; Explicit CUDA stream join with event markers; Long-generation regression check for kernel changes; Deploy custom Hugging Face checkpoints on a self-hosted cluster
- Tools: Hugging Face, CUDA streams, torch.compile, transformer-tricks repo

## [Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave](../videos/cQQbJqvZkpo.md)
`cQQbJqvZkpo` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · topics: inference-serving, infra-cost-scaling

CoreWeave's inference platform talk: how serverless, dedicated and batch consumption models share one stack, with KV-cache-aware routing, cache offload and quantization/speculative decoding as the main performance levers.

- Techniques: KV-cache-aware request routing; KV-cache offload to high-bandwidth storage; Provisioned throughput on a shared serverless tier; Time-scheduled reuse of reserved GPUs for batch; Async speculator training on customer data; Metering without retaining content
- Tools: vLLM, SGLang, TensorRT-LLM, LMCache, Mooncake, NVFP4, Artificial Analysis, OpenRouter

## [Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer](../videos/btxG75rNJC4.md)
`btxG75rNJC4` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · topics: inference-serving, observability, training-finetuning-rl

Two AI21 engineers walk through two silent vLLM bugs for hybrid Mamba models, one a scheduler ordering error and one a 32-bit index overflow, and the debugging method that found them.

- Techniques: Logprob comparison against a reference forward pass; Reproduce under pressure with determinism; Thread identity through the forward context; Bisect by forcing one code path; Check whether a fix is causal and watch for overflow
- Tools: vLLM, Hugging Face Transformers, NVIDIA compute-sanitizer, FSDP, Jamba (hybrid Mamba plus attention model)

## [Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta](../videos/7c9FSUVcXR0.md)
`7c9FSUVcXR0` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · topics: infra-cost-scaling, inference-serving, agent-architecture

Two Meta infra engineers argue LLM inference is now a distributed-systems and orchestration problem, so teams should optimize cost per successful task and build a control plane, not just faster tokens.

- Techniques: Four-quadrant optimization check; Workflow-aware scheduling and retries; Cascade breakers: queue-depth shedding, circuit breakers and retry budgets; Cost per successful task as the KPI; Telemetry-driven control loop; Latency, cost and throughput trade-off triangle
- Tools: vLLM, SGLang, TensorRT, Triton, Kubernetes, Mesos

## [What's New in Inference Engineering — Philip Kiely, Baseten](../videos/75ckHC2LU_0.md)
`75ckHC2LU_0` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · topics: inference-serving, training-finetuning-rl, models-research

Philip Kiely (Baseten) updates his inference book with post-February 2026 developments: why TurboQuant lost on data-center throughput, learned KV compaction, DFlash diffusion-style drafting, and continuous speculator retraining.

- Techniques: Continuous speculator retraining; DFlash block drafting; Learned KV compaction (Still); Stay on NVFP4 weight quantization for production; Local-first versus data-center-first sequencing
- Tools: vLLM, NVIDIA Dynamo, NIXL (transcribed as 'Nickel'), EAGLE-3, DFlash, DSpark, Medusa, TurboQuant, NVFP4, Still (Base10 KV compaction), attention matching, cartridges

## [Large clusters for small models — Daniel Svonava, Superlinked](../videos/g4SsanB0gMc.md)
`g4SsanB0gMc` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · topics: inference-serving, local-ai, infra-cost-scaling, training-finetuning-rl

Daniel Svonava (Superlinked) on serving fleets of small open models on your own GPUs: why top-down routers fail for many small requests, and how a centralized pull-based queue, a thin Rust gateway and a runtime sidecar fix it.

- Techniques: Centralized pull-based batching queue; Thin gateway with annotation, not full parsing; Runtime sidecar behind a socket; Knee-based benchmarking; Pin plus lazy-load model placement; Per-task model selection with evals, then cheap adaptation; Autoresearch loop for serving tuning
- Tools: vLLM, SGLang, PyTorch, Candle, NATS JetStream, MessagePack, Rust, AWS Bedrock, LoRA, Hugging Face

## [Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google](../videos/l1-D89bAuOA.md)
`l1-D89bAuOA` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · topics: evals, inference-serving, observability

Google engineers argue that LLM serving benchmarks often blame the server when the benchmark client is at fault, and show Inference Perf, a multi-process, reproducible load generator built for production-scale inference.

- Techniques: Scheduled multi-process load generation; Client-side health check on every run; Declarative benchmark configs with distributions; Sweep the load to find saturation; Match sampling and dataset preprocessing to production; Shared workload definitions
- Tools: Inference Perf, llm-d, Prism, vLLM, SGLang, Kubernetes, k6, Locust, MLPerf, ShareGPT

## [GTM Engineering: The Technical Bits — Everett Berry, Clay](../videos/UhCY231d0FQ.md)
`UhCY231d0FQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: data-engineering, agent-architecture, multi-agent

Everett Berry (Clay) on the technical hard parts of GTM engineering: data waterfalling, graph-based orchestration, long-running per-account agents, and outbound execution limits.

- Techniques: Waterfall enrichment; Selective field refresh; Typed-node orchestration graph; Persistent per-entity agent with wake-up triggers; Field ownership split; Timed re-engagement cooldown; Multi-domain sending with reply routing; Cross-channel suppression
- Tools: Clay, Salesforce, Outreach, Slack, Smartlead, Forager

## [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](../videos/O84lhGc1OOI.md)
`O84lhGc1OOI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: rag-retrieval, multi-agent, evals, context-engineering

Benjamin Clavié (Mixedbread) argues agents should be designed as knowledge workers, not coding agents, and uses BrowseComp-Plus and MatQA results to show that tooling and search orchestration drive accuracy.

- Techniques: Manager-plus-searcher subagents for open-ended retrieval; Optimize the lexical baseline before comparing; Hybrid search harness; Multimodal PDF search instead of OCR text; Teach the agent its retrieval primitives
- Tools: BM25, Gemini, Claude Code, Codex, Mixedbread search tool

## [IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork](../videos/q-WOjZhOMCA.md)
`q-WOjZhOMCA` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: security-guardrails, governance-compliance, agent-architecture, mcp-and-tools

Sarthak Aggarwal (DecaWork) argues agents should be governed like employees: each needs an identity, scoped short-lived capabilities, a policy gate outside the model, and receipts plus fast revocation.

- Techniques: Typed plan before evidence (plan-then-execute split); Out-of-model policy gate per tool call; Runtime agent identity card; Short-lived, audience-bound capability tokens
- Tools: Microsoft 365 Copilot, Microsoft Agent 365, Okta, AWS AgentCore Identity, MCP, A2A, Replit

## [Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic](../videos/PXj0p_mW9nI.md)
`PXj0p_mW9nI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: token-cost-efficiency, multi-agent, evals, agent-architecture

Anthropic's Katelyn Lesse and Angela Jiang argue agent token budgets are not fungible: giving some tokens jobs (advisor, grader, dreamer) beats simply spending more on one executor, measured at a fixed budget and scored on pass rate.

- Techniques: Role-split executor with advisor; Rubric grader with retry loop; Dreamer writing memory from transcripts; Fixed-budget strategy comparison; Cost per pass metric
- Tools: Claude Managed Agents

## [The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI](../videos/NW-jwOVr32w.md)
`NW-jwOVr32w` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: product-ux, vibe-coding-app-building, governance-compliance

Jonathan Gordon (ReWeaver AI) argues a lossless design-code round trip is not yet solved and proposes deterministic guardrails plus provenance to control drift around LLM-generated UI code.

- Techniques: Design-system extraction from code into the design canvas; Joint drift report across code and design; Deterministic guardrails around LLM generation; Fidelity metric per iteration (production drift ratio); Undo and review loop for AI code edits
- Tools: Figma, Sketch, Cursor, Claude Code, ReWeaver

## [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../videos/qdAkxLoYNI8.md)
`qdAkxLoYNI8` · AI Engineer · 2026-09-18 · q2 · intro · review · topics: context-engineering, rag-retrieval, pr-code-review, mcp-and-tools

Unblocked vendor talk arguing coding agents need an organizational context engine over code, PRs, Slack and docs, with cited sources; one live comparison, mostly product pitch.

- Techniques: Cited-source answers for agents; With/without context comparison; Expertise-weighted review comments; Query historical PR data with an open-source engine; Engineering social graph from review edges
- Tools: Unblocked, Claude Code, Claude 4.8, Slack, Notion, GitHub, MCP, Document Query Engine, context engine simulator

## [From coding to Knowledge work agents — Karan Vaidya, Composio](../videos/xxfMT-bPEmU.md)
`xxfMT-bPEmU` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: governance-compliance, agent-architecture, sandboxing-execution, memory

Composio CTO on why coding agents work and knowledge-work agents don't: six missing primitives (centralization, history, context, verification, governance, reversibility), enforced with walls and sandboxes rather than prompts.

- Techniques: Single connection hub for agents; Cross-app action record; Skill distillation from run logs; Pre-send style check against past outputs; Sandbox mirror of production tools; Two-layer walls: access scope plus behavior policy; Tiered gates scaled to blast radius; Undo for reversible actions, sandbox for the rest
- Tools: Composio, Claude Code, Codex, Cursor, OpenClaw, Git, Salesforce, Notion, Gmail, Slack, Zendesk, bugbot.md (named in passing)

## [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../videos/XsvUhpnHepE.md)
`XsvUhpnHepE` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: voice-multimodal, mcp-and-tools, infra-cost-scaling, token-cost-efficiency

Oxylabs' Giedrius Šteimantas argues web-using agents need a scraping infrastructure layer: use browsers only when required, validate content before it reaches the LLM, and fix the failing discovery and purchase stages of a shopping agent.

- Techniques: Validate page content before the LLM sees it; Search API for discovery, not a browser; Tiered web access: API first, browser last; Markdown and geolocated output from the scraper; Drop-in managed browser for Playwright MCP
- Tools: Playwright MCP, Oxylabs Fast Search API, Oxylabs Web Scraper API, Oxylabs Headless Browser

## [Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../videos/EL123UNokkI.md)
`EL123UNokkI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: pr-code-review, evals, multi-agent, observability

Uber's engineers explain uReview, their multi-agent code review system: how they built feedback-driven evals, team-owned customizations, and a cost/quality loop, plus why they think humans move up to an expanded outer loop.

- Techniques: Reply-sentiment and addressal-rate tracking; Trajectory-based runtime tuning with turn guardrails; Tiered review generators with post-processing; Few-shot AI linters with deterministic context; Ownership-coupled rule distribution
- Tools: GitHub, Fabricator, Claude

## [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../videos/zrZ1amZBSPw.md)
`zrZ1amZBSPw` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: infra-cost-scaling, governance-compliance, security-guardrails

Principal engineer at Twilio on running an LLM gateway in production: per-request fallbacks, per-route latency timeouts, guardrail fail-open/closed choices, load shedding, and centralizing governance without centralizing traffic.

- Techniques: Per-request provider fallback; Cool-down for failing providers; Per-route P99 and timeouts; Hedged requests for the tail; Guardrail time budget and explicit fail mode; Guardrail placement by output type; Bounded queues and load shedding with priorities; Per-route API key segregation; Decentralized traffic, centralized governance

## [How We Solved Agent Building — Andrew Qu, Vercel](../videos/9dYcwOkpCE8.md)
`9dYcwOkpCE8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: agent-architecture, skills-self-improvement, context-engineering, multi-agent

Vercel's chief of software traces an internal data-science agent from a mega-prompt, to a multi-agent chain, to one file-system agent with distilled skills, then introduces the Eve agent framework.

- Techniques: Decompose-then-collapse; File-system agent with minimal tools; Query-to-skill distillation job; Convention-based agent folders; Built-in run observability
- Tools: Vercel AI SDK, Eve, Vercel Workflows, Vercel Sandbox, Vercel Connect, bash-tool (npm), SkillsSH, Claude Code, Claude Opus 4.5, Snowflake, Next.js, Postgres

## [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../videos/0I6aoPSRzVc.md)
`0I6aoPSRzVc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: multi-agent, memory, context-engineering, enterprise-adoption

AIDAChip's VP of AIML argues chip-design teams are limited by alignment, not intelligence, and shows a "system of intent" living graph, tribal-knowledge layer and SME agents, plus failure lessons on substrate-level controls.

- Techniques: Living system-of-intent graph with human-gated edits; Rule-based conflict detection instead of LLM-based; Scoped spec hierarchy with file isolation per agent; Block forbidden actions at the system level, not per tool; Alignment-focused evaluation grid; Domain-specific SME agents instead of one general agent

## [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../videos/wdTRsfw0KG0.md)
`wdTRsfw0KG0` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: product-ux, enterprise-adoption, governance-compliance

A former OpenAI go-to-market leader on building automated sales machinery before hiring humans, launching self-serve first, avoiding pilots, and pricing usage instead of seats.

- Techniques: Automation-first go-to-market build-out; Self-serve first, then sales-assisted; Pilot alternatives that keep control of the deal; Trust portal and automated security review; Usage-based pricing with spend controls; Design partner on non-production internal product
- Tools: Clay, Nooks, Microsoft Copilot, ChatGPT Enterprise

## [SOTA Generative Media Panel — Dumitru Erhan, Shane Gu & Nicole Brichtova, Google DeepMind](../videos/KLDdXOw6jIc.md)
`KLDdXOw6jIc` · AI Engineer · 2026-09-18 · q3 · practitioner · panel · topics: models-research, voice-multimodal, evals

Google DeepMind panel on generative media (Veo, Gemini Omni, Nano Banana): why language is a lossy conditioning channel, why human preference evals mislead, and why real-task data and FDE feedback matter.

- Techniques: Side-by-side human preference eval for close model comparisons; Deterministic checks for rendered text; Early-access programs before broad release; Amortizing human labels into a learned evaluator; Joint generation of coupled modalities in one model
- Tools: Veo 3, Gemini Omni, Nano Banana, Nano Banana Pro, Nano Banana 2 Lite, Manim, FFmpeg, Stable Diffusion, OCR

## [500 Skills, Zero Fine-Tuning: LinkedIn's Playbook for AI Agents — Ajay Prakash, LinkedIn](../videos/9wZpvF3QleU.md)
`9wZpvF3QleU` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: skills-self-improvement, mcp-and-tools, context-engineering, coding-agents

LinkedIn's Ajay Prakash on an internal MCP server that serves tools plus self-contained markdown "playbooks" teaching coding agents company workflows, kept current by a PR-based self-update loop.

- Techniques: Playbooks as MCP-served instruction docs; Compose playbooks by reference; Session-end playbook self-update PR; Three meta tools for large tool catalogues; Central plus repo-local instruction split; Single pre-installed local MCP server with hourly auto-update
- Tools: MCP, Claude Code, GitHub Copilot, Cursor, Airflow, Jira, Slack

## [Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind](../videos/fjF8EKnxKCU.md)
`fjF8EKnxKCU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: agent-architecture, skills-self-improvement, sandboxing-execution, security-guardrails

Philipp Schmid (Google DeepMind) rebuilds one GitHub PR-review agent three ways, moving from a hand-written Python loop to a hosted sandboxed harness driven by markdown files, and argues to delete orchestration code as models improve.

- Techniques: Agents-as-files layout; Bootstrap script for CLI dependencies; Credential injection through a network proxy; Single-call agent turn with server-side loop; Named custom agent; File-based memory and handoffs; Build-to-delete audit
- Tools: Gemini API, Interactions API, Antigravity (agent harness), Google Agent Development Kit (ADK), GitHub CLI (gh), Google Search tool (Gemini API), Google Cloud Storage (GCS) bucket, GitHub repositories as sandbox sources, AI Studio, LangChain Open Deep Research (case reference), Cursor (case reference, speaker says 'Curso'), Manus (case reference, speaker says 'Manos')

## [Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google](../videos/9R--1tg45Jg.md)
`9R--1tg45Jg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: security-guardrails, mcp-and-tools, data-engineering

Google's MCP Toolbox team on separating dev-time from production agent tools. Keep credentials, raw SQL and user identity out of agent control, and use predefined, identity-bound, read-only tools.

- Techniques: Source primitive for connection secrets; Predefined custom SQL tools; Read-only enforcement at the driver level; Blast-radius limits on sources; Bounded and authenticated parameters for identity; Read/write tool split with approval gates; Actionable, retryable tool errors and flat inputs
- Tools: MCP Toolbox for Databases, Google Managed MCP, Model Armor, EvalBench, LangChain, Gemini CLI, Claude Code

## [Your Agreements Are a Database You Can't Query — Hiral Shah, Docusign & Sean Sodha, NVIDIA](../videos/_gvamfT8H-w.md)
`_gvamfT8H-w` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: data-engineering, inference-serving, enterprise-adoption

DocuSign and NVIDIA on turning enterprise agreement PDFs into queryable data, using a small layout-aware table extraction VLM (Nemotron Parse) inside a hybrid OCR pipeline.

- Techniques: Purpose-built small table-extraction VLM; Hybrid two-route document pipeline; Offline-heavy vs online-light compute split; Structured export and API over extracted data; Benchmark on table extraction and track accuracy vs speed
- Tools: Nemotron Parse, Nemotron Retriever, NVIDIA NIM, vLLM, C-RADIO, NVFP4, FP8, Coupa

## [Realtime Voice Agents with Frontier Intelligence — Bohan Li, EliseAI](../videos/MBHOH1NmDqc.md)
`MBHOH1NmDqc` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: voice-multimodal, agent-architecture, inference-serving

EliseAI's Bo Li explains a cascaded voice-agent harness (streaming transcription, background tool calls, prefix-cached TTS) that keeps frontier-model intelligence at real-time speed.

- Techniques: Streaming speculative transcription (two-tier ASR); Early generation with background tool calls and cancellation; Word-sequence prefix cache for TTS; Playback deduplication after speculative TTS
- Tools: Flux (fast streaming transcriber), Scribe V2 (accurate batch transcriber), Cartesia (TTS with WebSocket support)

## [Rebuilding the web for agents — Liad Yosef, MCP Apps](../videos/waI44NP1abk.md)
`waI44NP1abk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: mcp-and-tools, product-ux

Liad Yosef (MCP Apps co-maintainer) argues the web is shifting to assistant-driven, headless-plus-UI interaction, and that agent-readiness should be measured from agents' real behaviour, not from best-practice files.

- Techniques: Expose UI as MCP Apps for the last mile; WebMCP: publish page tools instead of screenshots; Measure agent paths, not best-practice checklists; Per-domain AI Catalog.json plus a queryable directory; Design an API-first surface, then add UI for the last mile
- Tools: MCP Apps, WebMCP, llms.txt, AI Catalog.json, Agentic Resource Discovery standard, auth.md, pricing.md, x402, Aura Journey, Aura readiness benchmark, Claude Code, ChatGPT

## [We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog](../videos/4lXks428C9o.md)
`4lXks428C9o` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: security-guardrails, sandboxing-execution, coding-agents

PostHog's Sarah Sanders on securing the PostHog wizard, an agentic CLI with shell access: deterministic enforcement, scanning every content source, and an LLM used only as an advisor.

- Techniques: Deterministic gate ahead of LLM judgment; Detector separated from actor; Scan both ends of the content pipe; Rule anatomy with paired tests; Deny-by-default command allowlist with a vault; Audit for composed attacks
- Tools: YARA, Ink, MCP, PostHog wizard, Warlock, Cursor

## [Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked](../videos/HvMyYLTfvhg.md)
`HvMyYLTfvhg` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: context-engineering, memory, agent-architecture, mcp-and-tools

Jeff Ng (Unblocked) argues agent infrastructure is now easy to assemble, so the real gap is organizational context. He demos a context engine that feeds agents synthesized, permission-scoped knowledge instead of raw MCP results.

- Techniques: Durable per-step checkpoints for agent runs; Isolated sandboxes for agent and third-party code; Context engine queried before the agent reasons; Synthesized context over raw tool results
- Tools: Cloudflare, Vercel, Mastra, Flu (transcript spelling of the framework), Linear, Slack, GitHub MCP, Claude Code, Codex, Unblocked context engine

## [From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad](../videos/dSg0pu8d6qg.md)
`dSg0pu8d6qg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: token-cost-efficiency, governance-compliance, pr-code-review

Ironclad's VP of AI Engineering on controlling AI token spend: measure cost against value, treat usage dashboards as smoke detectors, and fix the review and CI bottlenecks that code generation creates.

- Techniques: Cross-tool cost aggregation; Usage as an anomaly signal; LLM T-shirt sizing of merged PRs; Three-bucket trusted-throughput check; AI-first review gate; Bounded agent fix loops; Prompt-cache-friendly prompt layout; Context pruning and summarizing in long sessions; Buy non-differentiating tools, build a prompt playbook; Developer-experience metrics for CI
- Tools: Claude Code, Codex, Cursor, vendor usage dashboards, LLMs for PR complexity scoring, CI/CD pipeline

## [ACP: The Universal Remote Control for AI Agents — Alex Hancock, Block](../videos/YkNulwcc5jk.md)
`YkNulwcc5jk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: mcp-and-tools, agent-architecture, coding-agents

Alex Hancock (Block, Goose and MCP maintainer) argues for ACP, an open client-to-harness protocol, so one client can drive any agent over local stdio or remote HTTP/WebSocket.

- Techniques: Standard client-to-harness protocol (ACP); Underscore-prefixed custom methods, then standardize by usage; Transport swap with unchanged messages; Split the agent stack into four movable parts
- Tools: ACP (Agent Client Protocol), Goose, Zed, JetBrains IDEs, MCP (Model Context Protocol), JSON-RPC, stdio, HTTP, WebSocket

## [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](../videos/xLUQOqjudtA.md)
`xLUQOqjudtA` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: voice-multimodal, memory, context-engineering, software-factory

Tolan's engineers explain how a voice-first AI companion needs sub-two-second turns, stakes-based model routing, retrieval-style memory, and per-turn context rebuilding, plus how they use Claude agent fleets to ship iOS code.

- Techniques: Smart turn-taking from speech patterns; Per-stage latency instrumentation; Stakes-based model tiering with a cheap per-turn router; Retrieval-based memory with nightly consolidation; Stable-versus-volatile memory blocks; Character identity held separately from tone; Multi-judge eval loop for persona changes; Agent fleet with reviewer and PR-shepherd roles
- Tools: Claude, GPT-5.1, OpenAI Responses API, MCP, Linear, Sentry, Datadog, App Store

## [Your Voice Agent is Just a Walkie Talkie — Neil Zeghidour, Gradium](../videos/a8EcVumh71E.md)
`a8EcVumh71E` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: voice-multimodal, agent-architecture, models-research

Gradium's CEO traces voice agents from Siri to speech-to-speech models, explains why full-duplex needs multi-stream audio, and argues for a small full-duplex front end delegating to a background text LLM.

- Techniques: Audio tokenizer (neural codec) before the LLM; Multi-stream full-duplex modeling; Split front-end / background-LLM voice architecture (MoshiRAG)
- Tools: Moshi, Hibiki, GPT Realtime, OpenAI advanced voice mode, Siri, Claude Sonnet 5

## [Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS](../videos/gxVZ_1tuuq4.md)
`gxVZ_1tuuq4` · AI Engineer · 2026-09-18 · q2 · intro · demo · topics: agent-architecture, infra-cost-scaling, memory

AWS's Mike Chambers argues that an agent minus its model is the harness, and that agents built for many users should split the loop, memory, identity and tools into separately scaled parts, demoed on Bedrock AgentCore.

- Techniques: Split agent components for independent scaling; Session manager for cross-invocation state; Local dev loop that mirrors production; Declarative harness config; Agent-generated infrastructure as code
- Tools: Amazon Bedrock AgentCore, AgentCore CLI, Strands Agents SDK, Kiro, Claude Code, Cursor, MCP, AG-UI, AWS agent toolkit, Sonnet 4.5

## [Generative Video at the Speed of Light — Keegan McCallum, uRun](../videos/Xln-On3syJk.md)
`Xln-On3syJk` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: voice-multimodal, inference-serving, infra-cost-scaling

Keegan McCallum (uRun) argues generative video is improving on efficiency and long-horizon generation as well as quality, and describes the infra needed for real-time interactive video apps.

- Techniques: Distill a large video model for real-time serving; Real-time steering instead of prompt-and-reroll; Multi-model streaming pipeline with per-frame control sync; Wrap real-time video as a React component plus Python runtime; Agent-facing access via CLI and MCP server
- Tools: Helios, Wan 2.1 14B, WebRTC, ICE, TURN, React, Python async runtime, MCP, CLI, Sora, Sora 2, Seedance

## [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../videos/YXEqC05WEI0.md)
`YXEqC05WEI0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: security-guardrails, evals, governance-compliance, observability

Hinge Health's AI lead on shipping member-facing health AI: put irreversible decisions in code above the model, strip PHI at ingestion, monitor live traffic, and verify the judge before fixing the agent.

- Techniques: Code-layer routing above the model; PHI stripping at ingestion with environment and region separation; Layered live scoring of production traffic; Judge-first triage before agent changes; Severity triage for launch decisions

## [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../videos/G7cgLjZtmMU.md)
`G7cgLjZtmMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: mcp-and-tools, product-ux, evals, security-guardrails

Best Buy's Ahnaf Priyo maps the agentic commerce protocol stack (MCP, A2A, ACP, UCP, AP2), argues for pushed product feeds and checkout APIs over browser agents, and makes the case for behavior and protocol evals with a live cat-bakery demo.

- Techniques: Push product feed to platforms; Checkout as an explicit state machine; Scoped, single-use, revocable payment mandate; Layered evals for conversational commerce agents; Timeline view of agent calls; Agent skills for domain roles
- Tools: MCP, A2A, ACP, UCP, AP2, Cerebras, ChatGPT, Gemini, Chrome DevTools

## [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../videos/Qw_tC68KKes.md)
`Qw_tC68KKes` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: skills-self-improvement, enterprise-adoption, multi-agent, context-engineering

Cloudflare's Justin Joyce on scaling go-to-market analysis with curated skill files, a three-agent report pipeline and a self-service agent workspace; a practitioner account with few hard metrics.

- Techniques: Role-specific skill files with embedded question catalogue; Pre-shaped analytical data for agents; Draft, verify, then tone multi-agent report pipeline; Push generated narratives instead of dashboards; Reviewed central skill catalogue; Per-user persistent agent workspace
- Tools: Cloudflare Workers, Cloudflare Durable Objects, MCP, AI Gateway, Salesforce, Gemini (mentioned as a phone analogy)

## [Homa: The End of TCP for AI Clusters — John Ousterhout, Stanford](../videos/eZ8WWZzoaR0.md)
`eZ8WWZzoaR0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: infra-cost-scaling, inference-serving

Ousterhout argues AI inference and agentic workloads now send many small latency-sensitive messages, which TCP and RDMA handle badly, and presents Homa, a receiver-driven transport with about 13x lower short-message P99 in his benchmark.

- Techniques: Message-framed transport (RPC unit); Receiver-driven grant scheduling; Unscheduled first-RTT send; SRPT via switch priority queues; Percentile sweep by message size
- Tools: Homa (Linux kernel module), TCP, RDMA over Converged Ethernet (RoCE), ECN marking

## [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](../videos/hD9-V56FNRI.md)
`hD9-V56FNRI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: agent-architecture, security-guardrails, observability, memory

Talk arguing that once agents call tools and change state, they are distributed systems, so they need idempotency, compensation, scoped permissions, bounded retries and per-step traces.

- Techniques: Idempotency keys plus status lookup on every side-effecting tool; Persist each loop step and define compensation operations; Retry and fanout guardrails; Scoped credentials and tool allowlists; Parameter-bound, expiring human approvals; Memory as a cached, provenance-tagged store; Tool contracts with schemas and idempotency
- Tools: Replit AI agent (cited as a production-database deletion incident; not a tool under review), Air Canada chatbot (cited as an incorrect-refund incident; not a tool under review)

## [AI is the World’s largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](../videos/yoONZwV2smc.md)
`yoONZwV2smc` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · topics: evals, security-guardrails, product-ux

Clay Cockrell and Tony Fabrikant of CoupleWork AI argue that relationship AI often acts as a sycophantic validation machine, and describe their clinician-led design of Maxine: risk screening, protocol escalation, privacy, and clinician-written evals.

- Techniques: Clinician-first TDD evals; Background risk screen with protocol handoff; Reflect patterns instead of validating; Dogfood the agent for tone drift; Treat sensitive chat data as privileged
- Tools: Gottman Method, Emotionally focused therapy (EFT), Maxine (CoupleWork AI coach)

## [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../videos/B0fjR3yaZFU.md)
`B0fjR3yaZFU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: enterprise-adoption, product-ux, evals, agent-architecture

Long Lake co-founder on why AI adoption in real services businesses lags: climb an autonomy ladder, turn real work traces into evals, and co-design with users on-site.

- Techniques: Autonomy ladder rollout; Sandboxed async coding agent with PR output; Traces to ground-truth evals; Diff-based implicit feedback; Post-training on enterprise data; Layered customization; Co-design embedded in existing tools
- Tools: Claude Code, Codex, Claude Cowork, MCP

## [Agents' next frontier: agent-to-agent and network effects — Jean-Denis Greze, Town](../videos/REascnFlq_8.md)
`REascnFlq_8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: multi-agent, security-guardrails, rag-retrieval, context-engineering

Jean-Denis Greze (Town CTO) reframes agent-to-agent work as a context-window search problem and compares five ways to get cross-silo data into an LLM call safely.

- Techniques: Benchmark against an ideal single-context agent; Privacy-preserving derived tool; Per-silo sweeper agent; Write-step-only approval for cross-silo queries; Tiered autonomy by sensitivity
- Tools: Gmail, Slack, Airtable, LinkedIn

## [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](../videos/_ehJyfHg1Vk.md)
`_ehJyfHg1Vk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: skills-self-improvement, claude-code, software-factory, context-engineering

Kieran Klaassen (Every/Cora) on compound engineering: extract your judgment and repeated corrections into repo knowledge so each feature makes the next one easier, with a demo of his open-source plugin's commands.

- Techniques: Compound engineering loop; Ideation against strategy docs; Doc review for sharp questions; Brainstorm with minimal questions; Unattended end-to-end run (/lfg); PR polish with explanation; Extract a design rule from a review fix
- Tools: Claude Code, Codex, Cursor, Claude Cowork, Linear, GitHub, Slack, Intercom, Rails, React, MCP

## [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../videos/YXowceUKYJI.md)
`YXowceUKYJI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: inference-serving, infra-cost-scaling, agent-architecture

Red Hat engineers explain why agentic multi-turn traffic breaks classic LLM serving, and how llm-d uses KV-cache-aware routing and prefill/decode disaggregation on Kubernetes, with benchmark data and a GLM 5.2 case study.

- Techniques: KV-cache-aware pod routing; Prefill/decode disaggregation with KV transfer; Tiered KV offload with session pinning; Distribution-based capacity planning and trace replay; Decision matrix before choosing PD
- Tools: llm-d, vLLM, Kubernetes, NIXL, DeepEP, Mooncake, inference-perf, LeaderWorkerSet, RDMA/RoCE

## [Why AI Agents Need Million-Token Context — Thomas Wolf & Olive Song, MiniMax](../videos/5Cxe5dv2Xlw.md)
`5Cxe5dv2Xlw` · AI Engineer · 2026-09-18 · q3 · practitioner · interview · topics: models-research, inference-serving, context-engineering

MiniMax's Olive Song and Hugging Face's Thomas Wolf on how M3 reaches 1M-token context with sparse attention and native multimodal pretraining, and why agents need that context for multi-round tool use.

- Techniques: Index-then-sparse attention over context blocks; Train vision from the first pretraining step with interleaved data; Open project intake for research; Research harness for automating model-lab workflows
- Tools: MiniMax Sparse Attention (MSA), Hugging Face model card

## [Your Agent Just Authorized What?! — Jay Mok & Ben Coumes, Paypal](../videos/vGn6N4-bxBY.md)
`vGn6N4-bxBY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: security-guardrails, governance-compliance, enterprise-adoption

PayPal's Jay Mok and Ben Coumes propose a stakes-and-counterparty matrix for deciding how much proof an agent's payment authorization needs, ending with verifiable mandates for high-stakes, open-ecosystem transactions.

- Techniques: Stakes x counterparty evidence matrix; Scoped, time-bound, amount-capped mandates; Layered selective-disclosure credentials; Pre-authorize intent before the action target is known; Scoped OAuth access to stored credentials
- Tools: Claude Code, FIDO verifiable intents, AP2 mandate, PayPal approval token, PayPal vault, OAuth, Passkeys, GitHub, Jira, Linear

## [One Designer + AI. Hundreds of Deliverables. — Vincent Wendy, AI Engineer](../videos/O1FN4awNEtM.md)
`O1FN4awNEtM` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: product-ux, context-engineering, testing-verification

A solo designer at AI Engineer uses agents (Devin, GPT, Figma) to produce hundreds of conference deliverables by fixing design tokens first, automating data-driven outputs, and checking results with an agent.

- Techniques: Tokens-first design system for agents; Annotated spec sheet as handoff; Single data source to many assets; Agent as checklist QA on visual output; Vision-based photo matching; Raster first, then vectorize
- Tools: Devin, GPT, Figma, MCP, Slack, PNG export, Figma spec-sheet plugin

## [Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots — Amit Desai, Roku](../videos/Zd5b40Jbp_k.md)
`Zd5b40Jbp_k` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: voice-multimodal, product-ux, evals

Voice assistant satisfaction can rise without better accuracy: gate act/confirm/stop on calibrated confidence and pick thresholds by minimizing a user-cost function ("ouch").

- Techniques: Outcome user-cost minimization for act/confirm/stop; Two-threshold three-band policy with grid search; Sensitivity check on unit costs
- Tools: Interactive threshold-sweep graph built with a coding assistant (no specific library named)

## [It’s Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners](../videos/xo68uCibfm8.md)
`xo68uCibfm8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: context-engineering, agent-architecture, multi-agent, data-engineering

Kevin Madura (AlixPartners) explains recursive language models (RLMs): the context lives as a variable in a Python REPL, and the model writes code and delegates subcalls to sub-LMs, so only useful results return to the main context.

- Techniques: REPL-held context with sub-LM delegation; Typed I/O shell around an autonomous core; Schema-enforced sub-LM handoff; Bounded self-terminating loop; Dataframes in the REPL instead of JSON tool results; Trace-driven harness optimization (Halo)
- Tools: DSPy, PredictRLM, fastRLM, AXE, Halo, Claude Code, GPT-5, Anthropic Workflows, pandas

## [Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End](../videos/4loPnxvWWhg.md)
`4loPnxvWWhg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: training-finetuning-rl, context-engineering, evals, enterprise-adoption

A LeaseEnd data scientist explains how fine-tuning an intent classifier for customer texts became costly tech debt, and how replacing it with editable skills and prompts on a frontier model cut fix time from a week to under an hour.

- Techniques: Skill and prompt edits as the default fix; Curated production regression set as the gate; Markdown-file deploys to object storage; Triage gate before retraining; Fine-tuning pre-check list; LLM-judge labeling with manual review and holdout sets
- Tools: Claude Code, Amazon S3, OpenAI, Anthropic

## [Voice Agents Can Just Do Things — Charlie Guo, OpenAI](../videos/OpY6MmZFeHo.md)
`OpY6MmZFeHo` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: voice-multimodal, mcp-and-tools, product-ux

Charlie Guo (OpenAI) argues voice agents need not always talk back and lays out three voice modes (speech-to-speech, speech-to-action, event-to-speech), with GPT Realtime 2 as the example stack.

- Techniques: Three-mode voice design; Expose app verbs as tools; Escalating attention ladder; Preamble prompting; Native audio streaming; Role-first voice design checklist
- Tools: GPT Realtime 2, OpenAI Realtime API, Codex, ChatGPT advanced voice mode, CarPlay, Google Maps, Spotify

## [Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley](../videos/hOWU0KPUp1k.md)
`hOWU0KPUp1k` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: evals, governance-compliance, multi-agent, context-engineering

Brendan Rappazzo presents Loophole, an open-source game where two adversarial agents hunt contradictions in a legal code codified from the user's morals, then extends it to chatbot prompts, contracts, and simulated Senate votes.

- Techniques: Adversarial loophole and overreach search; Judge with auto-patch first, human escalation second; Formalize natural-language values into numbered legal text first; Persona-conditioned rule generation for simulation; Hill-climbing text against an adversarial judge
- Tools: Claude, GitHub

## [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](../videos/WJRdLNhrsLQ.md)
`WJRdLNhrsLQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: enterprise-adoption, pr-code-review, evals

Maven Clinic's CTO-level account of becoming an "AI-native" health company: AI in internal work and product, shorter planning cycles, changed code review, and tiered reliability bars with rubric-based evals.

- Techniques: Staged AI-coding adoption from low-risk tasks; Self-declared review tiers with accountability; Repeated-run pass-rate gating for non-deterministic tests; Rubric scoring plus human spot-checks on live conversations; Per-feature failure tolerance with multi-model agreement and human fallback
- Tools: Cursor, Claude Code, Jira

## [AI in GTM at Notion — Flora Liu](../videos/L4I7WgiEquo.md)
`L4I7WgiEquo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: enterprise-adoption, multi-agent, agent-architecture, data-engineering

Notion's GTM engineer explains a know/decide/act/learn system that unifies sales and self-serve signals, with humans and agents working in one shared context layer on durable workflows.

- Techniques: Four-layer know/decide/act/learn loop; Denormalized key-addressable profile plus keyed unstructured artifacts; Durable workflow per event with engine-managed retries; Parallel research subagents with score-and-select review loop; Single eligibility and routing classifier; Human approval gate by default, untrusted inbound input; Trace every LLM step and log decisions with outcome links
- Tools: Notion, Snowflake, DynamoDB, Temporal, Clay, Gong, Salesforce, Outreach, Nooks, ZoomInfo, Snowflake (product usage), Notion custom agents

## [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../videos/VjEP0xqTUI0.md)
`VjEP0xqTUI0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: enterprise-adoption, agent-architecture, data-engineering, mcp-and-tools

Arman Vaziri (Ramp) on building go-to-market orchestration: an internal CDP, durable background agents on Temporal, scoped retrieval, and an MCP that turns employee experiments into productized use cases.

- Techniques: Durable thread with checkpointed activities; Account-scoped hybrid retrieval; Per-agent tool scoping with human pause and resume; System skills plus user text instructions; Nightly per-entity fan-out; Persist derived entity matches; Shared tool surface via MCP plus usage mining; Explore vs exploit with guardrails across channels
- Tools: Temporal, Postgres, Kafka, TurboPuffer, dbt, Snowflake, reverse ETL, MCP, GPT-3.5

## [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../videos/5Bn0xro2ol8.md)
`5Bn0xro2ol8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: enterprise-adoption, testing-verification, coding-agents, context-engineering

Figma engineer on rolling out coding agents across an org: verification-first testing, plan-before-prompt with phase validation gates, and labeling AI-written text so reviewer attention is spent well.

- Techniques: Verification-first agent workflows; Encode agent discoveries as deterministic tests or flows; Testing pyramid for agent-written code; Red-green prompting; Why-first phased plan with validation gates; Human-first labeled communication; Agent-in-thread invitation
- Tools: Playwright MCP, Slack, cloud coding agent (unnamed)

## [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../videos/pOvWgX7IJsc.md)
`pOvWgX7IJsc` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: inference-serving, evals, models-research

Simran Arora (Together AI) on why multi-GPU communication is now the kernel bottleneck, the transfer and overlap trade-offs behind her Parallel Kittens primitives, and a benchmark showing frontier models still struggle to write fast multi-GPU kernels.

- Techniques: Copy-engine vs device-initiated transfer choice; Intra-SM vs inter-SM communication overlap; Thin primitive layer over a single-GPU kernel; Benchmark built from a parallelism taxonomy plus real-workload problems; Report correctness (pass@k) and speed-gated correctness (fast_1@k) separately; Agent harness: multi-turn bash agent for kernel tasks
- Tools: CUDA, PyTorch, torch.distributed, NCCL, RCCL, Triton, Triton Distributed, TileLink, ThunderKittens, Parallel Kittens, Parallel Kernel Bench, mini-SWE-agent

## [Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker](../videos/zaGyGgLW3SM.md)
`zaGyGgLW3SM` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: security-guardrails, sandboxing-execution, mcp-and-tools

Docker's Tushar Jain argues agent safety, not intelligence, is the blocker, and demos a sandbox runtime with stub credentials, scoped per-task sandboxes, and an unbuilt intent-based access prototype.

- Techniques: Run the agent inside an untrusted VM boundary, with policy enforced outside it; Split a monolithic agent into per-task sandboxes; Inject stub credentials, with real secrets added outside the sandbox; Just-in-time narrowed tools over existing MCP servers; Capability escalation through an intent tool; Same policy locally and in the cloud; Parallel fan-out of scoped sandboxes
- Tools: SPX (Docker runtime; name as spoken, install via brew), Docker, Codex (OpenAI coding agent), Claude / Anthropic models, GitHub, Slack, Notion MCP, MCP, OpenClaw (spoken as open claw), OpenCode (spoken as open code), GLM 5.2 (open model)

## ["My name is... my name is...": A Linguistic Map for Voice Agents — Midam Kim, ServiceNow](../videos/IDNfAZVKvPE.md)
`IDNfAZVKvPE` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: voice-multimodal, evals, product-ux

Midam Kim (ServiceNow) uses a linguistics framework to explain why voice agents fail and proposes diagnosing them by listen/speak channels, timing, and the user's mental model.

- Techniques: Linguistic diagnostic grid for voice agents; Interactive clarification on recognition errors; Locale-aware pre-processing for TTS and vocabulary; Turn-taking and barge-in control; Dynamic per-call context retention; EvaBench for diagnosing voice agents
- Tools: EvaBench

## [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../videos/mMNkdYnIVC4.md)
`mMNkdYnIVC4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: agent-architecture, evals, multi-agent, training-finetuning-rl

James Zou (Together AI, Stanford) argues agents should be given designed environments with verifiers, incentives and shared infrastructure instead of fixed workflows, citing Einstein Arena results and the DSGym data-science benchmark.

- Techniques: Verifier-first problem curation; Agent-native onboarding; Persona-differentiated agents; Shortcut audit before trusting a benchmark; Execution-verified trajectory generation
- Tools: Docker

## [MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed](../videos/lbaXnx0KLA8.md)
`lbaXnx0KLA8` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: mcp-and-tools, product-ux, context-engineering

Dustin Mihalik (Indeed) shares lessons from building MCP Apps for Claude and ChatGPT: model-visible data parity, separate data from rendering, and feeding UI interactions back to the model.

- Techniques: Model-visible data parity; Description steering of UI vs text output; Explore/render split; Interaction feedback via update model context; Render tools that take model-generated rationale; Small composable tool set
- Tools: MCP Apps, Apps SDK (OpenAI), update-model-context method, Claude, ChatGPT, CareerScout (Indeed internal agent)

## [x402 isn’t good (yet) — Jan Curn, Apify](../videos/h6mi88VrPtQ.md)
`h6mi88VrPtQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: governance-compliance, security-guardrails, mcp-and-tools

Apify's CEO lists x402 agent-payment flaws (double-spend before settlement, HTTP 402 vs MCP 401 conflict, poor fit for metered jobs) and his team's workarounds, including an agent-facing markdown gateway.

- Techniques: Charge-then-refund for metered jobs; Work-after-settlement for near-zero-cost calls; Agent-facing markdown instructions plus prepaid token; Batch micropayments via escrow and signed vouchers; Local wallet with cryptographic key and QR code
- Tools: x402 (Coinbase), MPP (Stripe, Tempo), HTTP 402 Payment Required, MCP, Apify actors, agi.apify.com, Coinbase facilitator

## [Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition](../videos/H7vFrcNWXzs.md)
`H7vFrcNWXzs` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: coding-agents, testing-verification, context-engineering

Dioxus Labs (now part of Cognition) on building an ambitious Rust framework with coding agents: fast on knowledge work and mundane upkeep, weak at tests, and architecture plus review now carry the load.

- Techniques: Let the compiler's strictness act as the agent's guardrail; Agents as a knowledge oracle for platform and spec behavior; Delegate checklist-style maintenance to agents; Agent-built fuzzing harnesses; Human-enumerated test conditions with agent brainstorming; Architecture-first, then implementation, with full PR reading
- Tools: Claude Code, Rust, Dioxus, Blitz, SubSecond, Firefox (CSS engine), Electron, React Native, Flutter, Kotlin, Swift, Zed

## [The Spatial Harness: Bringing Agents to the Canvas — Max Drake, tldraw](../videos/XWcXwnysmpY.md)
`XWcXwnysmpY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: product-ux, multi-agent, agent-architecture, coding-agents

tldraw's Max Drake on giving LLM agents a spatial canvas: teaching them to read screenshots plus shape data, running multi-agent fairies, and driving live apps and the desktop through code.

- Techniques: Screenshot plus structured data as canvas context; Agentic canvas harness with self-set goals; Visual agent identity and on-canvas task state; Orchestrator agent posting tasks to a shared board; Local editor server for code-mode agents; Dependency graph of agent tasks
- Tools: tldraw SDK, tldraw desktop app, Claude Code, Notion, Gmail, Conductor, OpenAI Symphony

## [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../videos/6pbQgnJ9Voc.md)
`6pbQgnJ9Voc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: enterprise-adoption, product-ux, mcp-and-tools, security-guardrails

Exa's co-founder argues go-to-market is an AI engineering data problem and shows the internal agents, ICP dashboard, and JeffBot clone that run his GTM team.

- Techniques: Decision-log to eval calibration for a personal proxy agent; Caller-scoped agent permissions; Semantic web search as a segmentation pipeline; API/MCP-first, then customize the SaaS; Signal-triggered alerts on customer events
- Tools: Exa, Opus 4.5, Slack, Salesforce MCP

## [Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher](../videos/y2W4FNAuPEA.md)
`y2W4FNAuPEA` · AI Engineer · 2026-09-18 · q3 · practitioner · workshop · topics: inference-serving, infra-cost-scaling, agent-architecture

Two-hour LLM inference workshop covering KV-cache memory math, prefill vs decode, attention variants, quantization, vLLM/SGLang serving optimizations, and benchmark caveats.

- Techniques: KV-cache capacity planning; Fix one dimension, then solve the rest for cost; Weight quantization for KV headroom; Attention variant selection; Radix-tree prefix caching for agent loops; Speculative decoding variants; Engine benchmarking loop
- Tools: vLLM, SGLang, TensorRT-LLM, NVIDIA Dynamo, Hugging Face Transformers, FlashAttention, EAGLE, Medusa, Molab, Google Colab, Mistral 7B, GPT-OSS-120B

## [Why Your AI Agent Needs a Wallet: USDC and Nanopayments — Harshal Bhangale, Circle](../videos/xKzU_3riL6s.md)
`xKzU_3riL6s` · AI Engineer · 2026-09-18 · q2 · intro · demo · topics: governance-compliance, infra-cost-scaling, mcp-and-tools

Circle engineer argues agents need wallets: x402 pay-per-request with USDC nanopayments and wallet-enforced spend caps, shown in a live Claude Code demo. Vendor pitch with a real but partly failed demo.

- Techniques: Wallet-enforced spend caps; HTTP 402 pay-per-request (x402); Off-chain signed authorizations with later settlement
- Tools: Claude Code, Circle Agent Wallet, x402, USDC, Circle Gateway, Nanopayments, Gmail, Blockrun (data provider), Polymarket data

## [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../videos/GJX19pNhmSw.md)
`GJX19pNhmSw` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: token-cost-efficiency, governance-compliance, observability, agent-architecture

Microsoft's Tisha Chawla and Susheem Koul argue agent cost control belongs at the agent-run layer, not the request layer. They show an out-of-band "TokenOps" plane that attributes spend per run, steers runs toward budget before halting them, and reports vendor benchmarks.

- Techniques: Run-scoped attribution tags and budgets; Boundary decorator on agent methods; Governor with a developer-declared action allowlist; Tiered policy ladder: steer, then halt; Cost guard: projected-overrun steering; Preview (shadow) mode for guardrails; Benchmark against throttling baseline
- Tools: OpenTelemetry, LangChain, LangSmith, LiteLLM, Portkey, Cloudflare AI Gateway, browser-use, MetaGPT

## [Teaching agents to pay — Anna Spysz, Stripe](../videos/A-zeQiYkmXk.md)
`A-zeQiYkmXk` · AI Engineer · 2026-09-18 · q2 · intro · demo · topics: security-guardrails, mcp-and-tools, governance-compliance, product-ux

Stripe engineer builds an agentic-commerce agent to buy headphones, covering the Universal Commerce Protocol, merchant manifests, shared payment tokens, persona effects on behavior, and a guardrail checklist.

- Techniques: Merchant capabilities manifest at /.well-known; Structured catalog and policy JSON; Attribute-match decision logging; Persona-driven behavior control and A/B testing of system prompts; Scoped payment token instead of raw credentials; Provider-enforced transaction limits; Agent commerce guardrail checklist
- Tools: Universal Commerce Protocol (UCP), Stripe payments, Google Pay, Apple Pay, shared payment token

## [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../videos/-tviRdpmHvs.md)
`-tviRdpmHvs` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: models-research, data-engineering, training-finetuning-rl

Krea's Sangwoo Lee on training the Krea 2 image model: data curation for stylistic diversity, cascaded dedup and classifier filters, and an LLM-style post-training pipeline with RL.

- Techniques: Cascaded dedup; VLM-judge distillation into a small classifier; SAE feature tagging for data hygiene; Two-pass captioning with OCR; Concept coverage via external importance ranking; Progressive resolution pretraining; Prompt expansion model
- Tools: Krea 2, pHash, MD5, SSCD, SigLIP, CLIP, sparse autoencoder, GRPO, OCR, VLM

## [Tell the Robot What You Want — Sandhya Subramani, AWS](../videos/S6aSoQ6_u5A.md)
`S6aSoQ6_u5A` · AI Engineer · 2026-09-18 · q2 · intro · demo · topics: multi-agent, agent-architecture, voice-multimodal

Live demo of a rover robot driven by an LLM agent built on the Strands harness, with a four-layer agent-to-hardware stack and a pitch that VLA policies may eventually make per-task robot training unnecessary.

- Techniques: Robot as an agent tool; Concurrent specialized agents on one tool surface; Edge/cloud policy split; Teleop for dataset creation; Messaging-app control over cellular
- Tools: Strands Agents (agent SDK), Amazon Bedrock AgentCore, Claude Opus 4.8, OpenAI Realtime (voice), Telegram, Raspberry Pi, VLA models, 4G SIM

## [Everyone Gets A Software Company — Benjamin Guo, Zo Computer](../videos/Qr15lGAGKpo.md)
`Qr15lGAGKpo` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: product-ux, agent-architecture, sandboxing-execution

Zo Computer co-founder Ben Guo pitches a personal cloud server with built-in AI as a way out of SaaS silos and vendor-owned cloud agents. Mostly a product pitch, with a few ownership arguments worth noting.

- Techniques: Single personal server as the agent home; Scheduled agent automations; Agent as a gatekeeper for inbound bookings; Chat-driven site editing and hosting
- Tools: Zo Computer, Claude Code, Codex, Gemini, Claude Tag, OpenClaw, Hermes, Calendly, Squarespace

## [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../videos/V_5bn4q-vAI.md)
`V_5bn4q-vAI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: context-engineering, mcp-and-tools, product-ux, coding-agents

Christopher Burns (Inth) on making LLMs recommend and correctly use his open-source cookie-banner library by shipping agent-friendly docs: hand-written llms.txt, markdown twins, web MCP, and grep-able docs inside node_modules.

- Techniques: Hand-curated llms.txt index; Markdown twin per page with discovery header; Three ways to reach markdown; Bundle docs in the package with an agents.md pointer; Web MCP for docs; Agent-readiness checks as a loop
- Tools: LeadType, llms.txt, llms-full.txt, AGENTS.md, Next.js, Aura AI, Cloudflare agent-readiness checker, MCP

## [The Search Engine for the Agentic Web — Will Bryk, Exa](../videos/59AA5kIoqjA.md)
`59AA5kIoqjA` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: rag-retrieval, infra-cost-scaling, product-ux

Exa's CEO pitches Exa as a search engine built for AI agents rather than humans, covering its history, API features (fast endpoint, token extraction, structured output) and a data marketplace.

- Techniques: Hybrid embedding plus keyword retrieval; Token-budget extraction before the LLM; Schema-based structured search output; Per-tenant search configuration; Latency tiers by consumer type
- Tools: Exa search API, Exa Connect, Cursor, HubSpot, Similarweb, GPT-3, ChatGPT

## [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../videos/M05vON8i0aI.md)
`M05vON8i0aI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: skills-self-improvement, enterprise-adoption, governance-compliance, context-engineering

Imad Touil (QuantumBlack) argues org know-how should live in governed agent skills: a central registry with owners, versions, access control and evals. Ungoverned skills bring duplication, quality decay, security risk and wasted tokens.

- Techniques: Skill catalog with metadata and an MCP search front end; Microservice-style skill design; Progressive disclosure of skills; Runtime composition of regulatory skills into a review workflow; Static skill tests before any evaluation; Individual-to-team-to-platform promotion path
- Tools: Claude Code, Cursor, MCP, Backstage (IDP), GitHub

## [Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](../videos/0uC6u0lJJl4.md)
`0uC6u0lJJl4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: memory, governance-compliance, security-guardrails

Tanmay Gopal (PromptQL) on why a shared company brain leaks secrets and how to gate it: one company-wide markdown wiki with per-page scopes, human-approved agent suggestions, and user credentials injected at tool execution.

- Techniques: Single linked markdown wiki with per-page scopes; Agent suggests, human accepts; Attribute every wiki change to a named human; Per-request user credential injection at the HTTP and SQL layer; Proxy and virtualize real-data access
- Tools: Claude Code, Slack, GitHub, OpenTelemetry, Opus 4.5, PromptQL, Hasura GraphQL engine

## [Speech-to-Speech Model Research at Google DeepMind — Valeria Wu Fon & Tom Ouyang, Google DeepMind](../videos/18Um2VjMM_g.md)
`18Um2VjMM_g` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: voice-multimodal, models-research, product-ux

Google DeepMind's Gemini speech-to-speech team explains why one natively multimodal, promptable model beats cascaded ASR+LLM+TTS for voice agents, with live translation, Search Live and Live API demos.

- Techniques: Native multimodal pretraining for audio tasks; Streaming translation as a prompt; Proactive audio gating; Managing the latency vs intelligence knob; One promptable model for many modes
- Tools: Gemini Live, Search Live, Gemini Live API, Google Meet speech translation

## [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](../videos/wCIYViPd4SU.md)
`wCIYViPd4SU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: security-guardrails, enterprise-adoption, claude-code, observability

Two Sigma explains how it runs cloud agents as each employee's own identity, using a propagated attribution header and enterprise-grounded web search to cut exfiltration risk.

- Techniques: Run agents as the user identity in existing per-user namespaces; Propagate an attribution header like a trace ID; Deny native web tools and route through enterprise grounding; Enforce tool behaviour with existing harness primitives
- Tools: Claude Code, Google Web Grounding for Enterprise, MCP CLI, Kubernetes, Brave Search (native web tool in Claude Code, per speaker)

## [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../videos/pqlWNihgdjI.md)
`pqlWNihgdjI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: enterprise-adoption, coding-agents, context-engineering, testing-verification

Amazon's frontier-dev habits from AWS's Clare Liguori: teams that changed how they worked (context files, self-validating agents, spec-first, local tests) hit a 4.5x median in deployment velocity; tool-only teams got under 3x.

- Techniques: Living steering/skills file with a rule per agent mistake; Self-validating agent loop; Spec-first iteration; Local deterministic mock services; Agent-friendly language and error design; Deployment velocity as the productivity metric; Decision-speed audit
- Tools: Kiro, MCP servers, Bedrock, TypeScript, Rust

## [The End of the Static Screen: Architecting Intent-Driven UX — Gus Iwanaga, commercetools](../videos/QrMcNe2jjt8.md)
`QrMcNe2jjt8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: product-ux, mcp-and-tools, agent-architecture

Gus Iwanaga (commercetools) on intent-driven generative UI: an orchestrator picks data and components, and the LLM emits a validated declarative UI spec, not free-form UI. Main lessons are on placement, the component catalog as contract, and changing team roles.

- Techniques: Declarative UI spec validated against a component catalog; Three-tier control spectrum for generated UI; Intent-to-UI orchestration pipeline; Layout hierarchy with templates, built bottom-up; Synthetic query-to-component data for curation
- Tools: MCP, Zod, React, A2UI, JSON Render (Vercel), OpenUI, ChatGPT, Claude

## [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](../videos/UyyOoJmuATU.md)
`UyyOoJmuATU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: agent-architecture, governance-compliance, evals, enterprise-adoption

Vasant Kearney (Onlay) argues healthcare agents should run on X12 insurance transactions as a public, strict contract that guardrails can reject, with tiered memory and skeptical use of models.

- Techniques: Standard-format tool contract; Strict guardrail rejection per step; Separated, tiered memory; Full-system regression evals before model swaps; Hybrid hard-coded and agentic execution; Write-action audit logging
- Tools: X12, FHIR, EHR, Claude Code, Codex, OpenClaw, Hermes Agent

## [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](../videos/Yphdry8ttAQ.md)
`Yphdry8ttAQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: product-ux, evals, data-engineering, enterprise-adoption

A seven-step recipe for building vertical AI (finance, pharma) where domain experts in a learning loop, not LLM-as-judge, drive quality and proprietary data is the moat.

- Techniques: Narrow task decomposition; LLM workflow for unstructured-to-structured data curation; Observability traces as the first improvement loop; Domain expert as user in a learning loop; Post-training ladder; AI-in-the-loop reduction of expert time

## [Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe](../videos/jebp4V0vh30.md)
`jebp4V0vh30` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: evals, inference-serving, rag-retrieval, product-ux

Adobe's Carlos Sanchez demos "agentic sites" that personalize page blocks in real time from browsing intent, grounded on the existing site, with provider choice driven by latency and accuracy evals.

- Techniques: Multi-provider eval matrix for accuracy and latency; Grounded block-level generation; Signal bucketing into personas or intents; Pre-generate and prefetch; Fast inference provider for the hot path
- Tools: Adobe Experience Manager, Edge Delivery Services, Cerebras, Gemma 4, Promptfoo, AWS Bedrock, Cloudflare, Google Cloud

## [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../videos/yqF6XhzbWBk.md)
`yqF6XhzbWBk` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: evals, context-engineering, enterprise-adoption

Sebastian Fox (Composo) on why LLM judges miss serious clinical-note errors: "which error matters" is tacit and shifting, so keep it as retrieved, case-specific expert judgments and run a discover-capture-calibrate loop.

- Techniques: Failure-mode discovery from production outputs; Free-text expert comments as the raw eval data; Retrieval of similar judged cases into the judge context; Generate-then-check with a narrower checker; Severity vs. detectability map of errors
- Tools: ambient AI scribes (product category discussed), LLM-as-judge with rubric, RLHF (conceptual reference)

## [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](../videos/XzJD1bvXKjs.md)
`XzJD1bvXKjs` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: context-engineering, evals, skills-self-improvement, models-research

Laurie Voss re-runs the 200-instruction IFScale benchmark on 2026 frontier models and finds the ceiling moved about 10x, to roughly 2,000 to 5,000 rules, but reliability and verification remain open problems.

- Techniques: Instruction density probe; Model-specific failure profiling; Pre-screening test vocabulary for safety filters; Per-output eval of long rule sets; Robustness check by rewording and reordering
- Tools: IFScale benchmark, Arize AI (speaker's employer; no product detail given), Chroma context rot study, Firebench, CCRbench, Guidebench (names as captioned; may be misspelled)

## [Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk](../videos/dQ-_i1tZiws.md)
`dQ-_i1tZiws` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: enterprise-adoption, evals, agent-architecture, security-guardrails

Maersk's Dmitry Buykin on running 200+ production shipping agents by turning expert SOPs into executable agent procedures, with a feedback loop that turns each correction into a harness change.

- Techniques: SOP-to-agent conversion; Three-part agent harness; Failure-to-fix mapping; Replay with writes disabled; Trace clustering into heat maps; Composite tools from repeated success; Function-calling tools instead of MCP
- Tools: SME bench (internal triage tool that clusters failures), Function calling

## [Generative UI... in Python? — Jeremiah Lowin, Prefect](../videos/Krzs8GeiWTc.md)
`Krzs8GeiWTc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: mcp-and-tools, product-ux, vibe-coding-app-building

Jeremiah Lowin (Prefect) on Prefab, a Python DSL for composing MCP App UIs; the talk argues scoping UIs to pre-built components makes Python-only front ends viable and that streaming compact Python beats streaming JSON.

- Techniques: Return a UI component from a tool; Reactive bindings for client-side interactivity; App class with app.ui and app.tools; Agent-bypass upload via MCP app; Stream generative UI as code
- Tools: Prefab, FastMCP, MCP Apps, React, shadcn/ui, Goose

## [Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan](../videos/32nrHU6zHU8.md)
`32nrHU6zHU8` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: agent-architecture, observability, evals, context-engineering

Navan's chief architect and a colleague argue agent infrastructure is repeating the microservices shift: skills as context units, hook-based tracing, trajectory evals, and tool-call guardrails.

- Techniques: Pre/post tool-call and session hooks for tracing and gating; Trace signals: goal, reasons, belief, tool calls, confidence; Trajectory evaluation; Skills as composable, testable context units; Single master agent with progressively loaded sub-skills; Per-tool-call authorization for on-behalf-of agents; A2A skill contracts across team boundaries
- Tools: AWS AgentCore, OpenTelemetry, Claude Code hooks, MCP, A2A protocol, Braintrust (inferred from auto-caption 'brain trusts')

## [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](../videos/cI7zfqusmFU.md)
`cI7zfqusmFU` · AI Engineer · 2026-09-18 · q3 · practitioner · demo · topics: agent-architecture, infra-cost-scaling, multi-agent

Giselle van Dongen (Restate) argues long-running agents need a durable infrastructure layer, and demos journaled retries, human-approval suspension, keyed sessions and mid-run signal or cancel.

- Techniques: Wrap every side-effecting agent step in a durable run call; Durable promise for human-in-the-loop approval; Keyed virtual object per session for serialized agent state; Classify mid-run input, then signal or cancel-and-restart; Central LLM gateway as its own durable handler
- Tools: Restate, Slack, LiteLLM, Python

## [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../videos/u6q-byPWUuo.md)
`u6q-byPWUuo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: evals, inference-serving, training-finetuning-rl, enterprise-adoption

Abridge's engineering lead on running clinical AI at scale: clinician-written rubrics feed LLM judges, staged rollouts, and small post-trained models gated by cheap triggers to balance quality, latency and cost.

- Techniques: Multi-reviewer rubric construction for LLM judges; Staged rollout with online feedback for AI features; Task decomposition into small specialised models; Gate cascade for real-time event triggers

## [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](../videos/pPj_tjlvYjA.md)
`pPj_tjlvYjA` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: sandboxing-execution, product-ux, testing-verification, voice-multimodal

Reelful's founder shows how an agentic video editor turns real footage into a clip: media understanding, a user-approved plan, a sandboxed agent with skills, Remotion rendering, and a verification loop.

- Techniques: Sandbox per approved job; Plan approval gate; Skills as encoded craft; Code-defined render target; Verification-then-reiterate loop; Directional templates plus manual editor fallback
- Tools: Remotion, React

## [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](../videos/s-aixZYJG4c.md)
`s-aixZYJG4c` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · topics: pr-code-review, context-engineering, governance-compliance, enterprise-adoption

Qodo's CEO argues human code review will become optional only once teams codify tribal knowledge into a context engine that serves both humans and agents, with per-rule analytics and graduated auto-approve/block.

- Techniques: Rule-linked review comments; Agent-directed PR summary comments; Per-rule analytics for review standards; Learning context from accept/reject history; Graduated auto-approve and auto-block; Service-contract graph for PR impact
- Tools: Qodo, Claude Code, AGENTS.md, CLAUDE.md

## [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](../videos/byn9PURoBNY.md)
`byn9PURoBNY` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: infra-cost-scaling, training-finetuning-rl, inference-serving

Krea's infra engineer on training the from-scratch Krea 2 diffusion transformer at scale: which metrics matter, why to let crashing runs restart, frequent checkpoints, and bursting training and inference across clusters and rented GPUs.

- Techniques: Let crashing jobs restart instead of debugging each crash; Hard GPU health gate on temperature; Checkpoint every 20 to 30 minutes to a high-throughput file system; Two-tier priority queue in front of Kubernetes; Overflow to external GPUs with a virtual node
- Tools: Kubernetes, Virtual Kubelet, Kubernetes descheduler, Kubernetes taints and tolerations, Queue system (captioned as 'Q') for gang scheduling, Prometheus, NVIDIA DCGM, Weka (parallel file system), Ceph, InfiniBand, NVLink, Hugging Face

## [How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face](../videos/FLUoowDJg4I.md)
`FLUoowDJg4I` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: software-factory, agent-architecture, observability, models-research

Hugging Face's Niels Rogge shows how nightly agents open outreach GitHub issues and PRs to move researchers' artifacts onto the Hub, moving from a fixed workflow to an autonomous agent loop.

- Techniques: Deterministic LLM pipeline mirroring the manual process; Cron for overnight background agents; Promote a step to an autonomous loop only where outputs are unpredictable; One container per work item for parallel agents; Skill as a manual trigger that fans out to subagents; Open-model routing through one OpenAI-compatible endpoint; Template completion from source material
- Tools: Claude Agent SDK, Cursor, Modal, GitHub Actions, Langfuse, Hugging Face CLI, Hugging Face inference providers, Slack, Gemini, Claude Code

## [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../videos/Lrw0jqBNaw0.md)
`Lrw0jqBNaw0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: product-ux, evals, mcp-and-tools, observability

Sourcegraph's agent advocate argues DevRel must now serve AI agents as users and recommenders, and shows how to measure agent friction and recommendation rates.

- Techniques: Agent friction logging from traces; With-and-without-tool agent benchmark; Intent-split GEO prompt experiments; Agent experience report; Machine-readable authoritative content
- Tools: Sourcegraph code navigation MCP tool, CodeScaleBench (speaker's benchmark), llm.txt, MCP registries, Discord

## [When AI Agents Pay and Sellers Monetize: Building x402 Apps on AWS — Anil Nadiminti, AWS](../videos/qTZirYu9pr0.md)
`qTZirYu9pr0` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: governance-compliance, security-guardrails, infra-cost-scaling, mcp-and-tools

AWS walkthrough of letting AI agents pay for content via the x402 HTTP 402 protocol, with AgentCore Payments on the buy side and WAF bot pricing on the sell side. Mostly product pitch, with some useful architecture.

- Techniques: Payment session spend caps with expiry; Deterministic payment layer decoupled from the agent loop; Key custody behind KMS, with agent-level capability only; x402 request/402/pay/retry flow; Edge bot classification and differential pricing
- Tools: AgentCore Payments, Bedrock AgentCore Gateway, Bedrock AgentCore Runtime, AWS WAF, Amazon CloudFront, AWS KMS, x402, Coinbase wallets, Stripe wallets, Base (L2 chain)

## [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../videos/mJqwmmOx4WA.md)
`mJqwmmOx4WA` · AI Engineer · 2026-09-18 · q2 · intro · demo · topics: governance-compliance, vibe-coding-app-building, coding-agents, product-ux

Andrew Garvin (Metronome, now part of Stripe) live-demos using Stripe Projects and a Metronome billing agent to build a usage-based billing setup from one natural-language prompt, arguing for sandboxed agent-built billing and for usage or credit pricing when agents are the users.

- Techniques: Portable skills files as agent context for a complex API; Verbose, machine-readable errors for agent self-correction; Sandbox-first agent-built billing with synthetic usage; Natural-language provisioning through a CLI orchestrator; Classify agent roles before designing pricing
- Tools: Stripe Projects, Stripe CLI, Metronome, Claude (selected as the coding agent in the demo), Vercel, Postgres, skills files

## [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](../videos/bdHaOXZOhcM.md)
`bdHaOXZOhcM` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: software-factory, evals, enterprise-adoption, coding-agents

A CTO explains how a manager with a full calendar keeps building by running coding agents overnight (context gathering at 5pm, morning review), using evals and custom-model training as examples.

- Techniques: Overnight agent loop; Context-harvesting prompt; Test-first with end-to-end computer-use verification; Feedback-to-eval hill-climb; Overnight custom-model training with sandboxed cloud access; Prototype branch behind feature flags; Small PRs with an AI reviewer in a clean sub-agent
- Tools: Claude Code, Codex, Cursor, Dia, Wispr Flow, Slack, Jira, Confluence, Notion, SQLite, AWS EC2, ModernBERT

## [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../videos/VBCDhRrvlYo.md)
`VBCDhRrvlYo` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: vibe-coding-app-building, agent-architecture, product-ux, context-engineering

Arturo Nunez (ex-Unity, MongoDB) pitches Nereu, a tag-driven, describe-it-to-build game engine where an AI assistant (Bibi) edits scenes via an Asset Tag System, so creators never touch engine vocabulary or code.

- Techniques: Entity tags as an intent layer over ECS; LLM-as-editor with a tool-only interface; Level-of-detail context assembly; Vision-model asset captioning; Domain expert in the loop while building with a coding agent
- Tools: Claude Code, Unity, Unreal, vision model

## [5 Voice Agent Failure Modes You'll Hit in Week One — Venky B, Plivo](../videos/vblnYHzBgS4.md)
`vblnYHzBgS4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: voice-multimodal, inference-serving, data-engineering, evals

Venky B of Plivo lists five voice-agent failure modes seen in production (latency, transcription, data collection, TTS output, barge-in) and the fixes his team uses. Main takeaway: treat voice as a structured pipeline problem, not a prompt problem.

- Techniques: Per-stage latency budget with time-to-first-audio as the metric; Self-hosted small or MoE open model for the conversational LLM; Dynamic keyword boosting per call phase; LLM post-processing of STT output with domain context; Typed field schema with validation and confirmation for data collection; Field-level unit-test evals for voice agents; Normalization layer between LLM and TTS; Pronunciation smoke tests with known hard names
- Tools: LiveKit, Pipecat, Pydantic, Zod, Qwen 3.5, Gemma 4, Cerebras, Groq

## [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../videos/ZIYYsAzaLlA.md)
`ZIYYsAzaLlA` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: mcp-and-tools, evals, context-engineering

Figma's engineer on building its first MCP server in about three months: which context format worked, how evals were automated, and how a remote server followed a local one.

- Techniques: Pick the representation the model knows best; Code plus screenshot as paired context; Reference-by-pointer via a component mapping; Two-step ask-then-act to emulate elicitation and sampling; Automated eval mixing deterministic checks and LLM judges; Local-first MCP server with an IPC bridge; Per-tool-call instructions when clients ignore server instructions
- Tools: Figma MCP server, Figma Code Connect, MCP Inspector, React, Tailwind CSS, Electron, Node.js, Cursor, VS Code, Claude Desktop

## [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../videos/qqrk7CtkuIw.md)
`qqrk7CtkuIw` · AI Engineer · 2026-09-18 · q3 · practitioner · interview · topics: software-factory, coding-agents, pr-code-review, enterprise-adoption

Anthropic's Mike Krieger on how Labs builds: delegate end states to agents, be less constrained with tools, share intent instead of 2,000-line PRs, and run fast persevere-or-pivot cycles.

- Techniques: Describe the end state, then review the trade-offs; Give agents a full environment instead of a narrow tool set; Port-verify-cross-read loop for large code migrations; Capture production runtime types to guide migrations; Share intent, trade-offs and production measurements in place of raw diffs; Tiered review: deep human review for architecture, fix-forward for cosmetic; Agent as a shared teammate in team channels; Instrument before you need it; use flags and dynamic config; Short bets with two-week persevere-or-pivot reviews; Unship primitives superseded by newer ones
- Tools: Claude Code, Claude Design, Cowork, Claude Code artifacts, Bun, MonkeyType, Slack, Python, TypeScript

## [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../videos/zCJtYuqwm7E.md)
`zCJtYuqwm7E` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: enterprise-adoption, software-factory, context-engineering

Patrick Debois (Tessl) argues that scaling coding agents is an organizational problem: teams must shift effort from fixing agent output to improving shared context, harnesses, and platform-owned reusable parts.

- Techniques: Convert skeptic critique into context and harness work; System-level retro; Split planning by agent readiness; Platform-owned reusable registry with a named owner; Per-team cost and iteration dashboards; Three-step AI-friendly hiring loop; Risk-tiered autonomy
- Tools: Claude Code

## [While my guitar gently speaks — Todd Fisher, Philo Ventures](../videos/E_Txocq-Lrw.md)
`E_Txocq-Lrw` · AI Engineer · 2026-09-18 · q2 · intro · demo · topics: voice-multimodal, vibe-coding-app-building, product-ux

A guitar that speaks and sings: pitch detection, word slicing, vocoder synthesis and a local Whisper-to-LLM loop. Mainly a call to build passion projects with AI.

- Techniques: Energy-gap plus sonority-peak word segmentation; YIN pitch detection to synthesized tone to vocoder; Pre-bake heavy DSP, then map to controls; Local voice loop: STT, then local LLM, then TTS; Plugin packaging inside a DAW
- Tools: JUCE, Logic Pro, Piper TTS, Whisper, YIN pitch algorithm, WORLD vocoder/pitch-shift, VocalSet, Apple built-in TTS

## [Pinecone 2.0 — Edo Liberty, Pinecone](../videos/IN-rb-9WmiY.md)
`IN-rb-9WmiY` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · topics: memory, rag-retrieval, context-engineering

Pinecone's Edo Liberty argues agents need a persistent, domain-owned company knowledge layer (Nexus) that goes beyond RAG, with query-time code generation and budgeted queries. Mostly a product pitch with vendor-reported numbers.

- Techniques: Manifest-declared knowledge base; Curate-on-ingest; Budgeted agent queries; Query-time code generation over a knowledge layer; Compact interface spec in place of tool sprawl
- Tools: Pinecone Nexus, vector database, SQL tables, graph database, markdown notes

## [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../videos/L173Z8DpaJg.md)
`L173Z8DpaJg` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: software-factory, pr-code-review, multi-agent, sandboxing-execution

Safia Abdalla (Warp) on building the Oz cloud agent platform: hide infra complexity, allow any harness, expose everything via API, and run the open-source repo with agent-gated triage and PR review.

- Techniques: Managed plus self-hosted sandboxes behind one model; Harness-agnostic layer with platform guardrails; Orchestrator with mixed-model sub-agents; Agent-gated PR review before human review; Agent-driven issue intake; API-first primitives for agents, sub-agents, environments and artifacts
- Tools: Warp, Oz, Claude Code, Codex, GitHub, Slack

## [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../videos/DrTdD-ttjCY.md)
`DrTdD-ttjCY` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: enterprise-adoption, product-ux, observability, evals

Snowflake's sales-team GTM agent (6,000 users): launch with quality over coverage, stage the rollout, manage activation, and use question logs as the feedback loop.

- Techniques: Question bank as the first eval set; Narrow-scope, high-accuracy launch; Pilot, beta, GA with metric gates; LLM classification of usage logs; Closed loop from logs to content; Agent instructions under version control with tests; Build on a managed agent platform with inherited access control
- Tools: Snowflake Cowork (formerly Snowflake Intelligence), Cortex Analyst, Cortex Search, Snowflake semantic views, MCP connections, Confluence, Jira, Slack, Gmail, Salesforce, Google Docs

## [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../videos/5dCAmSDOAjI.md)
`5dCAmSDOAjI` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: voice-multimodal, inference-serving, product-ux, infra-cost-scaling

Ahmed Ahres (Reactor) argues real-time interactive video and world models will change how content is made and consumed, then describes the infra gaps: streaming, session memory, and sub-100 ms global latency. Mostly a company pitch.

- Techniques: Stream frames over a live session instead of returning a file; Regional GPU routing for a latency budget; Session memory to keep generated worlds consistent; Multi-GPU serving plus quantization for cost and speed; Human-in-the-loop evaluation for real-time output
- Tools: Reactor API (real-time world model platform, roughly 10 lines to integrate per the speaker), Helios (ByteDance, interactive video model), LingBot (Alibaba, world model), LongLive 2 (NVIDIA, multi-shot film model), StreamDiffusion (NVIDIA, video-to-video; transcript reads 'SoundCloud Streaming', likely a caption error), Veo, Sora, Genie 3 (mentioned as comparisons)

## [Connect AI to Billions of Legal Documents — Simon Eskildsen, turbopuffer & Jacob Lauritzen, Legora](../videos/V-isu4eTHgw.md)
`V-isu4eTHgw` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: rag-retrieval, infra-cost-scaling, security-guardrails, enterprise-adoption

Legora (legal AI) walks through moving project and legal-research search from one Elasticsearch, to Postgres/pgvector, to turbopuffer, one namespace per project on object storage, and why that fits regulated multi-tenant workloads.

- Techniques: Namespace-per-tenant isolation with per-namespace keys and buckets; Partition by access temperature, not by hash; Object-storage-native write path; Round-trip budgeting over object storage; Memory-only cache for encrypted multi-tenant data; Clustered centroid tree for vector search; Two-round-trip inverted index for full text; Fan-out with hierarchy and validity filters for legal research
- Tools: turbopuffer, Elasticsearch, PostgreSQL, pgvector (DiskANN index, transcribed as 'disk NN'), Postgres tsvector, BM25, Amazon S3 (object storage), Google Cloud Storage, Azure Blob Storage, NVMe SSD cache

## [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../videos/rbjWzZK2LU0.md)
`rbjWzZK2LU0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: governance-compliance, security-guardrails, coding-agents

Sachin Malhotra (Anthropic CI) on giving agents budgets instead of tokens: classify verbs by how they fail, cap every write with refilling rate limits, watch aggregates with tripwires, and take identity from infrastructure.

- Techniques: Verb triage by failure visibility; Break-glass verbs with proxy-stamped audit; Refilling per-write rate limits with scope-sized budgets; Bypass that asks the human inside agent sessions; Aggregate tripwires paired with context fixes; Undo test for sizing controls; Identity stamping at the proxy with inherited labels; Two-layer policy: text plus deterministic proxy
- Tools: Kubernetes, admission webhook, Slack, Claude Code

## [Multimodal Collaborative Agents for Next-Gen Commerce — Nidhi Kaushik Vyas, Google DeepMind](../videos/AhQpRalYlyg.md)
`AhQpRalYlyg` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: product-ux, evals, context-engineering

Google DeepMind product lead on shopping agents for fuzzy intent: build a working state, ask the highest-value clarifying question, elicit preferences visually, adapt the answer format, and grade every step with autoraters.

- Techniques: Working state with confidence and live refresh; Counterfactual sensitivity test for constraint extraction; Information-gain question selection; Elicitation-channel choice by preference type; Per-step autoraters with user simulator; Response format chosen by query intent
- Tools: MCP (expected interface between agents and merchants), UCP (merchant common-language protocol, named in the talk without detail)

## [The Half Life of Agent Infrastructure — Ben Kus, Box](../videos/sM1iYgz93HI.md)
`sM1iYgz93HI` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: agent-architecture, evals, enterprise-adoption, rag-retrieval

Box CTO Ben Kus argues AI agent infrastructure has a half-life of months, not years, so teams should build abstractions, gate changes on eval sets, and get good at changing.

- Techniques: Abstraction layer over agent internals; Eval-gated switching; Scheduled stack review; Adaptive model selection; Hybrid lexical plus semantic retrieval with rank fusion; Agentic search
- Tools: Claude, Opus, OpenAI and Anthropic frontier models, open-weight models, BM25, embeddings and approximate nearest neighbor search, MySQL

## [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](../videos/AN65uc645mE.md)
`AN65uc645mE` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: voice-multimodal, inference-serving, evals, multi-agent

Hippocratic AI's engineering lead explains how their clinical voice agent (200M+ patient conversations) hits safety, latency and accuracy at once: a vertically built stack, 31 parallel specialist models, context-fed ASR, and lossless inference tricks.

- Techniques: Parallel specialist models with self-gating; Context-conditioned ASR; Second-pass rescoring for ambiguous short utterances; Async and offline verifiers for tool calls; Human plus synthetic eval mix with sample-size planning; Severity-graded harm rubric; Lossless inference stack
- Tools: Whisper (large-turbo, fine-tuned), speculative decoding, 4-bit quantization, KV cache

## [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../videos/lRa9sPaMyy4.md)
`lRa9sPaMyy4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: testing-verification, coding-agents, context-engineering

Varun Pant (AWS) argues that formal verification in Lean, Verus and similar tools can prove code correct for all inputs, which tests and LLM judges cannot, and that humans should own the specification while agents write code and proofs.

- Techniques: Spec-first verified agent coding; Spec model plus differential random testing; Lemma decomposition for AI proofs; In-code pre- and post-conditions checked by a solver; Intermediate-representation dialect to many backends
- Tools: Lean, Lean 4 browser playground, Kiro (transcript shows 'Kero', likely the AWS agentic IDE), Verus, Z3, Aeneas, Strata / Strata Core, Cedar, SMT solvers, model checkers, ArenaLang (kernel registry)

## [Where RL Will Take Search — Maximilian-David Rumpf, SID.ai](../videos/iJVxxxHM_Oc.md)
`iJVxxxHM_Oc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: rag-retrieval, training-finetuning-rl, multi-agent, context-engineering

Founder of SID.ai argues search should move from fixed retrieval pipelines to one RL-trained model, reporting about 20x faster and 100x cheaper than frontier-model search agents.

- Techniques: Search as a delegated RL-trained sub-agent; Verifiable retrieval reward for RL; Mixed reward with latency; Learned loop in place of a fixed pipeline; Parallel sub-agent searches
- Tools: BM25, PageRank, vector search, rerankers

## [No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle](../videos/jA_x7F8caHI.md)
`jA_x7F8caHI` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: memory, agent-architecture, multi-agent, enterprise-adoption

Oracle's Kay Malcolm argues that agent harnesses need shared, database-backed memory, using a five-type memory taxonomy and a team memory broker; mostly a product pitch for Oracle AI Database.

- Techniques: Five-type agent memory taxonomy; Shared memory broker tied to repo state; Keeping context alongside commits; Single-store consolidation for agent memory; Private local model for memory extraction
- Tools: Oracle AI Database 26AI, Oracle Agent Memory SDK, Codex, Claude, Git, Neo4j, Redis, OCI Always Free

## [Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs](../videos/r9OwPx_HoV0.md)
`r9OwPx_HoV0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: rag-retrieval, evals

AI21's Yuval Belfer argues chunking still matters: no single chunk size wins per query, so index the corpus at several sizes, retrieve whole documents, and fuse the rankings with RRF for 20-40% gains.

- Techniques: Multiscale indexing; Parent-document lifting before fusion; Reciprocal Rank Fusion (RRF); Oracle best-per-query benchmark
- Tools: RRF (Reciprocal Rank Fusion), QMSum, NarrativeQA, FinanceBench, Seinfeld trivia dataset (in-house, speaker says it is published)

## [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](../videos/7GMKdpLsxwU.md)
`7GMKdpLsxwU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: vibe-coding-app-building, product-ux, context-engineering, coding-agents

Hassan El Mghari (Together AI) on getting AI-built UIs out of "AI slop": codify the tells as anti-patterns, feed in references, iterate with a cheaper model.

- Techniques: Slop-gate anti-pattern list in a design skill; Theme library as inspiration; Screenshot inspiration vault; Two-tier model routing for UI work; agents.md as a taste log; Batched feature prompting
- Tools: Codex, Claude Code, Cursor, Hallmark, agents.md, GLM 5.2, Opus 4.8, Composer 2.5, Together AI

## [Agent Frameworks Considered Harmful — Rémi Louf, .txt](../videos/KHudyx5wW3U.md)
`KHudyx5wW3U` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: agent-architecture, observability, context-engineering

Rémi Louf (CEO of .text) on building a small event-driven agent runtime in two weeks: typed events, an append-only log, and content-addressed prompts for auditable, replayable agents.

- Techniques: Markdown-defined agents in a versioned folder; Event-typed agent contracts; Append-only event log with causal ids; Content-addressed prompt assembly; Replay a stored request against another model; Two-boundary enforcement
- Tools: Codex, Slack, Linear, llama.cpp

## [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](../videos/McknwOzbmyg.md)
`McknwOzbmyg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: evals, testing-verification, voice-multimodal, product-ux

Jared Joselowitz (Ufonia) on shipping a clinical voice agent to patients without A/B tests or rollback, using simulated patients, a calibrated LLM judge, and prompt optimization gated by hazard-linked evidence.

- Techniques: Hazard-first safety case; Scenario-conditioned simulated user; Calibrated LLM judge; Reflective prompt optimization (GEPA) with a cost-weighted metric; Synthetic edge-case generation; Staged gated rollout with evidence-based autonomy; Pin prompt versions and keep full traces
- Tools: Matrix (internal simulation framework), PatBot (internal LLM patient), BevJudge (internal LLM judge), GEPA (genetic-Pareto prompt optimizer), DSPy (mentioned as the origin of GEPA), Gemini 2.5 Pro (judge model at the time of the paper)

## [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../videos/bMjlRrWjdT0.md)
`bMjlRrWjdT0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: evals, enterprise-adoption, product-ux, observability

DoorDash GenAI platform team on building a cross-functional AI evals platform: UI-first, then API-first, then workflow-first, so non-engineers can run annotation and judge calibration themselves.

- Techniques: Continuous eval loop; API-first eval platform with vibe-coded UIs; Self-serve judge calibration with prompt optimization; Platform-level model choice for judges
- Tools: Claude Code, Codex, DSPy-style prompt optimizer (transcribed as JEPA), MCP, LLM gateway, agent gateway

## [Mousepower: agents that can’t be measured, can’t be managed. — Maximillian Piras, Yutori](../videos/8KkibGU_DDY.md)
`8KkibGU_DDY` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: governance-compliance, evals, token-cost-efficiency, product-ux

Maximillian Piras (Yutori) argues agents have a measurement problem: token spend must trace to verifiable outcomes, and tasks should be triaged by step and acceptance-criteria uncertainty before building an agent.

- Techniques: Two-axis task triage; Verifier agent alongside worker agent; Background parallel agents for peripheral work; Outcome-tied token accounting
- Tools: Claude

## [Voice agents with Realtime Video — Sidney Primas, LemonSlice](../videos/z1dqv74SpUs.md)
`z1dqv74SpUs` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: voice-multimodal, inference-serving, agent-architecture

Lemon Slice's CTO explains how they build real-time, photorealistic video avatars from a causal video model, covering past-only attention, one-step denoising, long error-free runs, and a GPU/CPU harness that keeps streams stutter-free.

- Techniques: Causal (past-only) attention mask for streaming video; Collapse denoising steps for real-time output; Expressive audio encoders over default ones; Real-time model harness (GPU/CPU orchestration); Two-layer EQ/IQ split

## [1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI](../videos/qStB9GbppMU.md)
`qStB9GbppMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: voice-multimodal, evals, observability, security-guardrails

Hamming AI's CEO argues voice agent errors (about 10% in practice) are the top deployment blocker, and offers a loop to find, prioritise, test and red-team failures across many calls.

- Techniques: Frequency and severity triage matrix; Scenario-variation regression testing; Production A/B testing for voice fixes; Cross-conversation pattern analysis; Continuous adversarial red-teaming

## [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../videos/FvxY8oPoI8o.md)
`FvxY8oPoI8o` · AI Engineer · 2026-09-18 · q2 · practitioner · demo · topics: token-cost-efficiency, infra-cost-scaling, evals, coding-agents

DigitalOcean's Archana Kamath and Tyler Gillam argue for per-request model routing chosen by task, cost, latency and rules, validated with your own evals. A live OpenCode demo shows roughly 3x lower session cost at similar quality, though the evidence is one vendor demo.

- Techniques: Per-task model pools with ordered failover; Natural-language routing preferences plus hard rules; Side-by-side routed vs single-model agent runs with live cost tracking; Eval-gated routing with feedback loop
- Tools: Plano (open-source proxy and routing model), OpenCode, Claude Opus, Claude Sonnet 5, GLM 5.2, GPT 5.2, Llama 4 Maverick (caption reads 'long before Maverick')

## [Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](../videos/KcVkq5L-0f0.md)
`KcVkq5L-0f0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: context-engineering, rag-retrieval, mcp-and-tools

Brandon Waselnuk (Unblocked) argues AI coding agents fail on missing company context, not intelligence, and outlines context-engine design: avoid curated markdown, separate access from understanding, and use schema discovery for relational questions.

- Techniques: Derive context from systems instead of hand-curated files; Deterministic team graph from GitHub; Rules-file discovery and index; Schema-less lookup, then deterministic query; Two retrieval modes: deep research and fast unfurl; Context hydration to avoid repeated discovery searches
- Tools: MCP, GitHub, Slack, OAuth, SSO, OpenAI API, Anthropic API

## [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard](../videos/mav15aW9lLM.md)
`mav15aW9lLM` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: governance-compliance, enterprise-adoption, evals, security-guardrails

Christopher Lovejoy (Anthropic) and Saul Howard (Anterior) argue that enterprise AI agents need audit, data-boundary, escalation and eval primitives designed in from the start, not bolted onto a proof of concept.

- Techniques: Immutable append-only event log as system of record; Event log plus schema-driven immutable blob store; Token-based access at point of use; Human-agent equivalency in the action model; Replay plus human-vs-agent diff as eval; Run evals inside the customer environment

## [The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev](../videos/fZH97QHHYjY.md)
`fZH97QHHYjY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: rag-retrieval, evals, context-engineering

Jo Kristian Bergum argues BM25 is back for agentic search: LLM agents write long, precise queries that suit lexical matching, and the baseline was undertuned. Retrieval results can be exposed as a filesystem workspace for grep-style use.

- Techniques: Workspace-as-filesystem retrieval; Tuned BM25 baseline before any embedding comparison; Hybrid lexical plus grep for agent search; End-to-end task evaluation for search agents; Evidence-stuffing ablation
- Tools: BM25, grep, ripgrep, sed, BrowseComp-Plus, Hornet (vendor BM25 engine)

## [The Signal Layer: What to Build When Anything Can Be Built — Lena Hall, Akamai](../videos/1KOdiGgMtpY.md)
`1KOdiGgMtpY` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: product-ux, enterprise-adoption

Lena Hall argues that when AI makes building cheap, value moves to choosing what to build and keeping that choice intact through shipping and marketing, using a thin "signal layer."

- Techniques: Stranger readme read-back check; Promise welded to its limit; Human point of view, AI for the rest; Thin signal layer across handoffs; Hamming list of important problems

## [Don’t be data poor — Anuj Iravane, Anterior](../videos/XAsb7MIAzm8.md)
`XAsb7MIAzm8` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: data-engineering, evals, skills-self-improvement

Anuj Iravane (Anterior) explains how to generate synthetic medical records when real PHI cannot be kept, by sampling labels and policy reasoning traces first and generating documents backward.

- Techniques: Reverse-generation from sampled labels; Coarse-to-fine layered generation; Round-trip label verification; Cross-document consistency eval in a refinement loop; Skill files as the domain-expert interface
- Tools: internal agent harness (unnamed)

## [Training Taste — Thais Castello Branco, Taste Labs](../videos/sDMGWK4wZ_w.md)
`sDMGWK4wZ_w` · AI Engineer · 2026-09-18 · q3 · intro · talk · topics: evals, product-ux, vibe-coding-app-building, context-engineering

Thais Castello Branco (Taste Labs) on measuring and fighting "AI slop" in design: decompose subjective quality into checkable parts, build feature classifiers that flag slop, and turn a brand into structured context the agent both follows and is graded against.

- Techniques: Decompose subjective quality into probes; Split objective checks from aesthetic judgment; Rule-aware intentional divergence; Brand spec as both generation context and rubric; Retrieve pre-built brand systems
- Tools: Claude Design, Wayback Machine-style web crawl

## [Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node](../videos/ZyGMqdIpPoE.md)
`ZyGMqdIpPoE` · AI Engineer · 2026-09-18 · q2 · intro · demo · topics: governance-compliance, security-guardrails, mcp-and-tools

Edge & Node's pitch for Ampersend, a payment and compliance layer letting agents pay for paid MCP tools and checkouts, with a sanctions-screening demo. Mostly product pitch.

- Techniques: Pre-authorization counterparty screening; Skill file as the payment-aware tool gateway; Per-call micropayment for paywalled endpoints; Prompt-level spend constraint
- Tools: x402, Shopify UCP, TRM (wallet screening), MCP, Claude Code, Claude Cowork, Ampersend, Exa, Firecrawl, Circle nano-payments

## [Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.](../videos/v42opQpCy60.md)
`v42opQpCy60` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: vibe-coding-app-building, product-ux, coding-agents, context-engineering

Paul Bakaus on steering coding agents toward good design with a skill (Impeccable) that maps vague design adjectives like "bolder" to project-specific meanings, keeping humans in the loop instead of one-shotting.

- Techniques: Project-defined verb and adjective commands; Self-check against a stated failure test; Pre-brief questions before generation; Workflow-stage command mapping; Community-tested experimental commands
- Tools: Impeccable, Claude Code, GitHub Copilot, Cursor, Codex, Figma, Webflow, Claude Design, Radiant Shaders

## [Building Blocks for Uber’s Software Factory— Uday Kiran Medisetty & Adam Huda, Uber](../videos/17-YSUHo6Lk.md)
`17-YSUHo6Lk` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · topics: software-factory, mcp-and-tools, pr-code-review, enterprise-adoption

Uber's engineers walk through six building blocks (model gateway, MCP gateway, agent devpods, skills marketplace, context graph, Cortana) behind its managed software factory, then show one feature built end-to-end by an agent.

- Techniques: Single gateway with middleware chain and project attribution; Progressive MCP projection (direct, discovery, CLI, generated code); Pre-warmed agent workspaces; Skill marketplace with lint, review and trace feedback; Shared context graph queried before tool calls; Split review between an inner loop and an outer loop; Managed scheduled maintenance loops with bounded output

## [Beyond the Lethal Trifecta: Agentic Commerce on the Open Internet — David Levine, Kiduna Club](../videos/tE2z8-hqoLY.md)
`tE2z8-hqoLY` · AI Engineer · 2026-09-18 · q2 · intro · talk · topics: security-guardrails, governance-compliance, multi-agent

Founder talk on the "lethal trifecta" (private data + untrusted content + actions) and a proposed fix: agents as identity-bearing members of legally registered, blockchain-verified organizations. Mostly a pitch for Kaduna Club.

- Techniques: Ally build sequence (inform, instruct, empower, enact, align); Scoped identity tokens for agents (JWT with claims); Decision markets for policy; Per-action audit trail back to a responsible principal
- Tools: OpenCloud (caption spelling; likely OpenClaw, an agent product that the speaker says blew up in January 2026), MOO / LambdaMOO (text-based virtual world the speaker used in 1993), MCP servers (cited as a way enterprises integrate agents), Slack, Salesforce, Notion, Telegram, Twitter, JWT, Vector database (generic, no product named), Blockchain (generic, no chain named), Polymarket (cited as an analogy for decision markets)

## [Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust](../videos/nxokqOq1imY.md)
`nxokqOq1imY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: evals, observability, agent-architecture

Braintrust field CTO argues each agent architecture generation (single call, chain, ReAct loop, graph, product system) needs different evals, and that production traces should keep feeding the eval set.

- Techniques: Architecture-matched eval suites; k-run pass@k and pass^k reporting; Production failure clustering to harvest evals; Node-level and branch-level evals for graph workflows
- Tools: Braintrust, Braintrust Topics

## [Which AI startups actually land enterprise contracts? — Brian Lewis, Millennium](../videos/7A65O-0lvKE.md)
`7A65O-0lvKE` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · topics: enterprise-adoption, security-guardrails, governance-compliance, product-ux

A buyer at a hedge fund explains why most AI startup pilots fail: value, security, reliability and legal gaps, not model quality. He argues most AI-native work is unglamorous data, architecture and change management.

- Techniques: Enterprise-readiness intake checklist for vendors; Verify retention claims in a pilot, not on paper; Gate features by group and by release; Track documentation and terms as versioned artifacts; Set buyer-written success criteria and a 90-day plan that deploys into the buyer's own cloud; Build-versus-buy check on vendor pitches; Breach-response question as a red flag test

## [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j](../videos/Q0VkgCyNVUg.md)
`Q0VkgCyNVUg` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: memory, rag-retrieval, context-engineering

Neo4j's Stephen Chin argues agent memory stored as markdown or vector lookups fails on multi-hop questions, and shows a live home-lab demo where a vector-seeded graph traversal beats a vector-only store.

- Techniques: Vector-seeded graph traversal; Graph as the agent's write target; Inspect-and-fix retrieval loop; Let the coding agent write the graph layer; Same-source backend A/B test; Keep destructive memory tools away from the agent
- Tools: Neo4j, Cypher, Cognee, OpenClaw, Goose, Hermes Agent, pgvector, LanceDB, Claude, Proxmox, pfSense, HAProxy

## [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../videos/maRzp4kImJ4.md)
`maRzp4kImJ4` · AI Engineer · 2026-08-18 · q4 · deep · talk · topics: training-finetuning-rl, inference-serving, infra-cost-scaling

Nan Jiang (Modal) argues RL rollouts can run on scattered, elastic GPUs across regions if the trainer syncs only a bit-exact sparse diff of serving-precision weights instead of full checkpoints.

- Techniques: Decoupled rollout islands; Bit-exact sparse weight diff; Versioned request contract; Sidecar version gate; Floor-based update-visibility check
- Tools: Modal, SGLang, vLLM, Adam, BF16, FP8, NVFP4, RDMA, Stitch

## [Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning](../videos/2bvtay8wGYI.md)
`2bvtay8wGYI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: training-finetuning-rl, context-engineering, agent-architecture, evals

GR's Ross and Chengxi Taylor trace RL-for-reasoning from Galactica and 2022 PPO recipes to long-horizon agents: value models, compaction, pipeline RL, and a benchmark where frontier models lost money.

- Techniques: Value-model (critic) RL for long, variable-length trajectories; RL-trained compaction; File-system scratchpad, self-search and archive tools for long-horizon context; Pipeline RL with bounded off-policy lag; Verifiable-reward PPO after continued pretraining (2022 recipe); Open-ended, outcome-scored long-horizon benchmark
- Tools: Galactica (Meta science LLM; 30B variant cited), Llama 2, Llama 3, Reasoning Llama (named, no details), ChatGPT, GPT-3.5, GPT-4, OpenAI o1, DeepSeek-R1, InstructGPT (2022, cited for RLHF results), PaLM (540B, cited for comparison), Chinchilla (cited for comparison)

## [State of Data — Sean Cai, Independent / State of Data](../videos/ZyIoTOAbRfs.md)
`ZyIoTOAbRfs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: training-finetuning-rl, evals, data-engineering

Sean Cai argues data markets are the scarce input for turning generalist models into experts, and that single benchmark numbers and contrived expert-made data mislead buyers.

- Techniques: Three-axis verifiability scoring; Multi-harness, multi-infrastructure benchmarking; Per-criterion rubric analysis with deterministic checks plus LLM-as-judge; Long-horizon task checklist; Automatic post-training rerun on base-model swap; Lab spending as a leading indicator

## [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](../videos/eAXxdtNlK04.md)
`eAXxdtNlK04` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, context-engineering, observability

Langfuse's Annabell Schäfer shows that a clear-cut yes/no target function (single-label paper classification) lets an optimizer loop improve a small model's prompt, and argues teams need domain experts and high-signal evaluators before auto-improvement pays off.

- Techniques: Fit / validate / test split for prompt optimization; Error clustering to drive hypotheses; Binary, criterion-specific judges instead of Likert-style scores; Task markdown as the loop spec
- Tools: Langfuse, Claude Code, GPT-5 Nano, Claude Opus 4.8

## [DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve](../videos/Yk87oUPVaxU.md)
`Yk87oUPVaxU` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, coding-agents, testing-verification, models-research

Datacurve's DeepSWE talk: a long-horizon coding benchmark with tasks written from scratch to resist PR-mined contamination, plus per-model behavior findings and verifier design lessons.

- Techniques: Original task authoring by domain experts; Behavior-based verifiers; Verifier isolation and history scrubbing; Terse objective-only prompts; Per-model failure-mode analysis; Harness-agnostic base-model comparison; Hybrid verification with LLM judges
- Tools: DeepSWE, SWE-Bench Pro, mini-SWE-agent

## [Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](../videos/jRCpXUjz4CI.md)
`jRCpXUjz4CI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, agent-architecture, sandboxing-execution, training-finetuning-rl

Alex Shaw (Terminal-Bench, Harbor) argues agents behave like ML models, so teams should build environments (instruction, sandbox, verifier) and run parallel rollouts for evals, training data, RL and agentic map-reduce.

- Techniques: Environment as a three-part directory (instruction, sandbox, verifier); Separate rollout, trajectory capture and verification; Parallel rollouts with a fire-and-forget launch; Agentic map-reduce over agent logs; Own the eval before choosing a model; Design for agent users of your product
- Tools: Harbor, Terminal-Bench 2.1, Codex (GPT-5.5 run in the demo), Cursor CLI (map step in demo), Modal (sandbox backend in demo), Tinker (RL integration), A frontier model transcribed as 'Fable 5' (reduce step in demo; name may be a caption error), LangChain Deep Agents with sandboxes (integration)

## [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../videos/ZTA0GwpAUak.md)
`ZTA0GwpAUak` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: training-finetuning-rl, coding-agents, enterprise-adoption

Samuel Denton (Applied Compute) lays out a 2x2 of offline/online hints and traces for distilling production agents, with SWE-bench and hyperlink-format results showing online hints win on on-policy behavior.

- Techniques: Offline hint on offline production traces; Turn-budget nudge hint; One-step on-policy rollout from an offline trace; Online hint from each rollout; Judge-chosen hint placement with next-step distillation; Relevance-mass token selection (self-distillation)
- Tools: SWE-bench, Qwen 3.5 (thinking model)

## [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](../videos/Btk8wDUVs74.md)
`Btk8wDUVs74` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: memory, context-engineering, data-engineering, product-ux

monday.com's Omri Bruchim and Tomer Ast argue agents fail because they lack understanding, not data, and describe a two-speed "world model" of the user (slow learned profile plus fast live signals) built ahead of time.

- Techniques: Two-speed user model (slow profile + fast signals); Precompute meaning ahead of time, recompute a thin slice at serve time; Source isolation with fallback to last verified context; Urgency gating for proactive notifications
- Tools: monday.com Sidekick, Monday Vibe, Monday Agent, Monday Workflows, Slack, Claude, Gemini, GPT

## [The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside](../videos/KhYifX22yhE.md)
`KhYifX22yhE` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: training-finetuning-rl, data-engineering, models-research

Poolside's data and training leads on synthetic data at scale, the modular generation pipelines behind Laguna M.1 and XS.2, and the silent-corruption bugs (broken GPU, BF16 accumulation, FP8 kernel race) they found training Laguna S.

- Techniques: Modular six-part synthetic data pipeline; Seed-heavy cheap rephrasing; Staged decomposition of hard generation; Cross-domain porting and judge-evolver loops; Orchestrated agent queue (Hive); Cross-replica weight hash checks; FP32 accumulation for growing activations; Test recipes on a small model before scaling
- Tools: Hugging Face, DeepGEMM (FP8 kernels), Hive (poolside internal generation orchestrator)

## [We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](../videos/iKQ78wyJEXU.md)
`iKQ78wyJEXU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: security-guardrails, skills-self-improvement, pr-code-review, governance-compliance

Nubank's product security team built SkillVector, a CI scanner that vets internal AI skills (hybrid regex plus LLM) before they reach an internal marketplace, and reports 2,000+ skills scanned.

- Techniques: Three-point skill scanning; Hybrid deterministic plus LLM review; Findings as PR comments plus SARIF; Historical back-scan; Verify approval gates, not model confirmations
- Tools: SkillVector (spoken as 'SkillVetor' in the transcript), SARIF, Regex-based determinstic scanners, LLM reviewer, Internal skills marketplace

## [Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla](../videos/B8l81jhvHbI.md)
`B8l81jhvHbI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: context-engineering, memory, evals, enterprise-adoption

Ishita Daga (Tesla) argues enterprise data agents fail from ambiguity, staleness and team-level preference, not model size, and proposes a tiered source-of-truth structure, a context lifecycle, and open questions on preference.

- Techniques: Tiered source-of-truth hierarchy; Context lifecycle with live sources and event logging; Replay-based evaluation of recent questions; Metric variants in a semantic layer with user selection
- Tools: mem0, Tableau, dbt, GitHub, memory.md files

## [Build Evals That Actually Matter - Nick Ung & Akshay Sharma, Lyft](../videos/3z2uT5aDx_Y.md)
`3z2uT5aDx_Y` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, observability, enterprise-adoption

Lyft's customer-support agent team on building offline simulation evals, calibrating LLM judges on hand labels, and closing the loop from error analysis to agent changes.

- Techniques: Simulated multi-turn offline eval; Mixed eval dataset from production samples plus mutations; User simulator realism calibration; Binary task-outcome rubric per metric; Judge calibration as a classifier; Confidence intervals and paired comparisons; Annotation queue for domain experts; Config-driven eval harness
- Tools: LangSmith, Langfuse, DeepEval, LangGraph, tau-bench (transcribed as CowBench, from Sierra)

## [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../videos/CoEIs6Xm8m8.md)
`CoEIs6Xm8m8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: token-cost-efficiency, infra-cost-scaling, models-research, security-guardrails

Cline's founder argues open-weight models plus verification-heavy agent harnesses will win on cost as closed labs subsidize subscriptions for lock-in, citing a supply-chain attack and spend data.

- Techniques: Put quality in the harness, not the model; Default route to cheaper open-weight models in an internal gateway; Head-to-head test on a real bug from your own repo; Set usage limits per user on the provider dashboard
- Tools: Claude Code, Codex, Cursor, Cline, LiteLLM, GLM, Kimi, DeepSeek, Opus, Open Compute

## [How Codex Works — Dominik Kundel, OpenAI](../videos/shRR1e2HXMk.md)
`shRR1e2HXMk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: agent-architecture, coding-agents, context-engineering, sandboxing-execution

OpenAI's Dominik Kundel walks through what happens when a message is sent to Codex: context assembly, sub-agents, computer use, sandboxing, auto-review, WebSocket transport, goal loops and compaction.

- Techniques: Deferred tool loading with tool search; Capping the skills list as a share of the context window; Sub-agent tool set: spawn, send input, wait, shutdown; Code-execution computer use with a persistent REPL; Auto-review sub-agent for escalated actions; Stateful WebSocket transport for agent loops; Goal loop with an explicit done tool; Server-side compaction item
- Tools: Codex, OpenAI Responses API, Codex app server, ripgrep, PowerShell, Node REPL, Chromium, Seatbelt (macOS sandbox), Bubblewrap (Linux sandbox), Cerebras (GPT-5.3 Codex Spark), Ollama, LM Studio

## [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../videos/iqloyWCGYQQ.md)
`iqloyWCGYQQ` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, memory, models-research, training-finetuning-rl

Parth Asawa (UC Berkeley) argues that standard LLM benchmarks test models with memory wiped each time, and proposes measuring continual learning through sequential tasks, gain over a stateless baseline, and Pareto reporting.

- Techniques: Paired stateful vs stateless runs (gain metric); Benchmark design checklist for continual learning; Multi-axis Pareto reporting; Mid-sequence concept drift injection; Stability vs plasticity failure triage

## [Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare](../videos/RmS5s6Wbin4.md)
`RmS5s6Wbin4` · AI Engineer · 2026-08-18 · q3 · practitioner · demo · topics: vibe-coding-app-building, sandboxing-execution, security-guardrails, product-ux

Kenton Varda (Cloudflare) argues personal AI codegen needs new infrastructure, and demos "Gadgets": per-user apps with platform-enforced sharing and sandboxed generated code, run on open-source workerd.

- Techniques: Platform-enforced sharing via single-purpose instances; Sandboxed generated UI with postMessage-only RPC; Give the agent the app source and a brief, let it add primitives; Export code-only templates (blueprints); Run the production runtime locally
- Tools: Cloudflare Workers, Durable Objects, Dynamic Workers, workerd, Claude, Cap'n Web RPC

## [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../videos/GqoNrUz8hEU.md)
`GqoNrUz8hEU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: voice-multimodal, agent-architecture, security-guardrails, mcp-and-tools

Paul Klein (Browserbase) argues reliable browser agents are a harness, tooling and infrastructure problem rather than a model problem, and lays out a multimodal, harness-engineered, consistently hosted approach.

- Techniques: Hybrid code-plus-browser execution; Per-site skill packs loaded before visiting; Compressed page representation; Pinned, consistent browser environment; Sites expose WebMCP tool calls and agent-first auth; Observability-to-self-improvement loop
- Tools: Browserbase, Browse.sh, WebMCP, Playwright CLI, Claude Code, Operator, Cursor, Factory, OpenClaw, WorkOS AuthMD, web bot auth, auto-browse

## [The Base Model Is Dead — Varun Singh, Arcee AI](../videos/xbPriQWXtWM.md)
`xbPriQWXtWM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: training-finetuning-rl, models-research, data-engineering

Varun Singh (Arcee AI) argues base models have shifted from storing general web knowledge to priming RL for reasoning and agentic behavior, and explains the data-mix changes this requires.

- Techniques: Rephrase-based synthetic upsampling; Early injection of post-training-format data; Mid-training on post-training and long-context traces; Atomic-skill check before RL; Warm-up on test-time compute formats; Monitor MoE expert utilization under data shift
- Tools: Claude Code

## [Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft](../videos/m24UKZomm7k.md)
`m24UKZomm7k` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: agent-architecture, voice-multimodal, context-engineering

Microsoft's ACE live voice tutor: run a lesson as a state machine where the model only proposes narrow outputs and a harness validates them and decides the next step.

- Techniques: Lesson-as-state-machine harness; Per-step narrow prompts; Model proposes, harness decides; Right-size the model to the harness; Reliability coin-flip test
- Tools: Claude Opus 4.7, Claude Haiku 4.5

## [Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi](../videos/s67bE2Ur3bY.md)
`s67bE2Ur3bY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: security-guardrails, memory, multi-agent

Sai Krishna Rallabandi on moving agents from one-user assistants to group-chat and wearable agents. Covers the security boundary, memory curation and forgetting, privacy as context, and when to speak.

- Techniques: Action-boundary deterministic guard; Data/instruction channel split with a trained SLM; Atomic fact extraction with hierarchical and temporal links; Continuous relevance scorer for forgetting; Per-user LoRA adapters over a shared memory layer; KV-cache aware memory ingestion; Learned speak/stay-quiet classifier; Private routing via DM
- Tools: LoRA, SLM classifier, regex and traditional NLP guards

## [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../videos/vSx5IULvBns.md)
`vSx5IULvBns` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: agent-architecture, observability, enterprise-adoption

Resolve AI engineer argues production ops, not coding, is the bottleneck, and shows always-on cloud background agents that run on schedules, events and messages, with deployment monitoring as the lead use case.

- Techniques: Trigger-typed background agent; Per-change check plan generated from the diff; Time-bounded watch with agent-chosen duration; Confidence-gated reply with human confirmation; Feedback in the thread edits the standing task; Expose agent capabilities over MCP
- Tools: Slack, Microsoft Teams, GitHub release tags, Kafka, CI/CD pipelines, feature flag systems, MCP servers, Granola

## [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](../videos/XLEYtv3cMlw.md)
`XLEYtv3cMlw` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: context-engineering, agent-architecture, multi-agent, evals

Sina Shahandeh (Radicait) on why coding-agent research loops stall on open-ended science, and how decomposing a codebase into linked component docs plus cross-model critique gets better hypotheses.

- Techniques: Hierarchical component docs as a scaffold; Hypothesis generation over each component; Multimodal model as a qualitative metric; Split roles across models in the loop; Per-iteration outcome review
- Tools: Codex, Obsidian, Gemini, Oracle CLI, GPT-5.5 Pro (as transcribed)

## [fighting slop with slop — Vaibhav Gupta, Boundary](../videos/AMiyLItEtLA.md)
`AMiyLItEtLA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: software-factory, context-engineering, testing-verification, dev-tools

Vaibhav Gupta of Boundary argues that teams without code review can keep AI-written code stable by building internal tools that enforce invariants, mine agent transcripts, and rethink the language and tooling layers underneath.

- Techniques: Invariant-only architecture file; CLI guard checks for architecture invariants; Required reading as the gate for design docs; Transcript triage loop; A/B test skills or features by agent outcomes; Per-function CLI and describe tool
- Tools: BAML, Claude, Codex, TypeScript, Python, Rust, Go, Ruby, Java, WASM, ripgrep, Notion

## [Security Track Intro — Randall Degges, Snyk](../videos/2xJoimgoqBg.md)
`2xJoimgoqBg` · AI Engineer · 2026-08-18 · q2 · intro · keynote · topics: security-guardrails, coding-agents

Snyk's Randall Degges opens the World's Fair security track: AI-written code has security bugs, autonomous agents need containment, and model access limits are a barrier to shipping fearlessly.
- Tools: Fable (AI model, access reportedly pulled; name as spoken), OpenAI GPT 5.6 (new model, speaker says it is not available to many yet)

## [How Forward Deployed Engineering is done at Cognition — Jia Wu](../videos/RVxym6mmIns.md)
`RVxym6mmIns` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: enterprise-adoption, product-ux, software-factory

Jia Wu (Cognition) on forward-deployed engineering: embed in enterprise customers, map Devin to real backlog problems, and measure outcomes from agent sessions. Mostly a company pitch, with some case-study numbers.

- Techniques: Session-based value measurement; Event-triggered agent automation; Map backlog to capabilities; Before/after delivery metrics; Autonomous legacy migration
- Tools: Devin, Devin Cloud, Windsurf, Claude Code, Cursor

## [When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain](../videos/bUJgirn4_yc.md)
`bUJgirn4_yc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: data-engineering, agent-architecture, memory

DataChain's Dmitry Petrov argues coding agents need a "data harness" for physical and unstructured data (video, sensors), built on Pydantic schemas, incremental checkpoints and reusable derived datasets.

- Techniques: Pydantic schema as the only data model; Typed mapper and generator functions for parallel processing; Incremental runs with checkpoints; Check for an existing derived dataset before computing; Per-dataset knowledge note with lineage
- Tools: DataChain, Pydantic, Claude Code, YOLO, Ray, Spark, Dask, Git4Data

## [Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley](../videos/Sir59K8ZDPU.md)
`Sir59K8ZDPU` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: agent-architecture, security-guardrails, data-engineering

Frank Coyle argues agents need ontologies as a symbolic validator around LLM tool loops, checking outputs against domain constraints before acting.

- Techniques: Validator gate after each tool call; Two-layer boundary checks (Pydantic plus ontology); Side-effect-free planning, then commit; OWL constraints for business rules; Reuse existing vocabularies; Bounding and monitoring agent loops
- Tools: Claude API (Python client, stop_reason tool-use loop), Pydantic, OWL, RDFS, schema.org, DBpedia, Dublin Core, FOAF

## [Ending AI Slop — Thais Castello Branco, Taste Labs](../videos/lCBf9slCanI.md)
`lCBf9slCanI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: evals, training-finetuning-rl, data-engineering

Taste Labs founder argues subjective domains like design and writing can be made verifiable by decomposing quality into checkable parts, routing each part to the right judge, and using quality expert data.

- Techniques: Decompose fuzzy quality into codified components; Per-component routing of grading method; Ground-truth rules instead of similarity to a reference; Diverse expert pool with strict selection to counter mode collapse; Specificity and code-linkage QA on expert labels; Disagreement triage in expert consensus

## [Security Firewall for Agents — Ryan Dahl, Deno](../videos/MkRYPFIMCSA.md)
`MkRYPFIMCSA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: security-guardrails, infra-cost-scaling, governance-compliance

Ryan Dahl (Deno) on Claw Patrol, an open-source byte-level egress proxy that gates what production agents send to databases, Kubernetes and SaaS, with rules, credential injection and human or LLM approval.

- Techniques: Byte-level egress proxy for agents; Credential injection at the proxy; Policy-as-code in HCL with Git review; Chained verdicts: rule, LLM judge, then human approval; Network-level placement with existing identity
- Tools: OpenClaw, Claw Patrol, Deno Deploy, PostgreSQL, Kubernetes, ClickHouse, AWS (Sigv4), GitHub, Slack, PagerDuty, HCL, Terraform

## [Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect](../videos/AQv3qRCG6Gw.md)
`AQv3qRCG6Gw` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: training-finetuning-rl, evals, observability

Will Brown (Prime Intellect) on running RL when no verifiable reward exists: manufacture supervision from grounding, judges, production traces and learned simulators, and keep humans on the top-level decisions.

- Techniques: Environment as the shared unit (task + harness + rewards); With/without grounding as a supervision gap; Backward construction from a reachable end state; Trace-seeded task mining; Judge-to-rubric distillation; Pass-rate gated task generation; Learned simulator of an uncontrolled tool or site; Reward-hack corpus and small-run validation
- Tools: Prime Intellect PrimeRL training framework, Prime Intellect verifiers and task sets, Prime Intellect Lab (hosted training and evals), GRPO / REINFORCE policy-gradient methods (named in passing), MCP servers, CLI tools and web apps (as simulator targets)

## [AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j](../videos/kRkcNOsRyYg.md)
`kRkcNOsRyYg` · AI Engineer · 2026-08-18 · q3 · practitioner · workshop · topics: rag-retrieval, data-engineering, context-engineering

Neo4j workshop on graph shapes for agents over a lakehouse: a metadata semantic layer over the warehouse, a deterministic document-tree-plus-links graph, and Leiden community "themes" built without LLM labels.

- Techniques: Metadata-only semantic layer graph; Deterministic document-structure graph; Hierarchical URI IDs for scoped search and traversal; Semantic query expansion for full-text search; Structure-only community themes; Spec-driven Cypher generation with a vendor skill; Agent with a database CLI for ad hoc graph reasoning; Partial re-sync of a deterministic graph
- Tools: Neo4j, Neo4j CLI, Cypher, Graph Data Science (GDS), NeoCarta, Neo4j Virtual Graph, Lucene full-text index, Leiden, Louvain (mentioned), Claude Code, Claude Opus 4.8 (model used in demo), BigQuery

## [Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd](../videos/ZFxh7sqbUZo.md)
`ZFxh7sqbUZo` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: security-guardrails, training-finetuning-rl, evals

David Brumley (CMU, Bugcrowd) on designing RL environments for vulnerability discovery and exploitation, using deterministic oracles, an open-world "audit" task scored by precision and recall, and a 16-rung capability ladder run against V8.

- Techniques: Deterministic witness-based grading; Open-world audit task with dedup and precision/recall; Capability ladder for hard targets; Withhold the answer key and the most dangerous artifacts
- Tools: MCP (exposed setup, read/write, and grading tools), Docker, exploitbench.ai, V8, AIxCC, DARPA Cyber Grand Challenge, SciBench, CyberGym, BountyBench

## [In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](../videos/VrpEyglYgeU.md)
`VrpEyglYgeU` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: testing-verification, pr-code-review, context-engineering

Sonar's CEO argues AI coding agents need verification built into the loop: guide them with context and constraints, layer algorithmic and agentic checks, and keep the codebase clean. It is a vendor talk, and its numbers are self-reported.

- Techniques: Guide with context and constraints; Zero-trust multi-layer verification; Verification inside the agentic loop; CI verification loop with agent PR review and quality gates; Scheduled code-maintenance and remediation agents
- Tools: Sonar Vortex (product launched the day before the talk, per the speaker), METR time-horizon benchmark chart, Models named: Mythos, Fable, GPT 5.5

## [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../videos/Cc0_nyxROBA.md)
`Cc0_nyxROBA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: voice-multimodal, training-finetuning-rl, agent-architecture, security-guardrails

Gaurav Mishra (Amazon AGI Lab) on why RL-trained computer-use agents break on real login screens, ads, and expired sessions, and how to adapt training and the harness to real-world messiness.

- Techniques: Simulated messy environments for agent RL; Recovery as a native model action; Process reward model over the trajectory; Action risk classifier in the harness; Harness-level credential and loop guardrails; Checkpoint, rollback, and audit trail; Forced human handoff; Adversarial tasks in mainstream training; Design-partner failure loop
- Tools: Playwright, WebMCP, MCP, web search APIs, PPO, GRPO

## [Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio](../videos/Fu45geO3zX8.md)
`Fu45geO3zX8` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · topics: security-guardrails, multi-agent, mcp-and-tools

Armanas Povilionis (Alithea Bio) argues that cross-organization agent work needs signed, verifiable receipts, and demos Froglet, an open protocol for agents to discover, buy and verify services.

- Techniques: Signed per-step receipts for agent transactions; Marketplace as discovery only, direct peer deals; Same node, role chosen at runtime; Typed payload with schema and deal ID, polled asynchronously; Expose the protocol through MCP and let the LLM drive it
- Tools: Froglet, MCP, Claude, Docker, OpenClaw, NemoClaw

## [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../videos/Ki980nV0__0.md)
`Ki980nV0__0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: voice-multimodal, evals, infra-cost-scaling

Dhruv Batra (Yutori) argues the long-tail web will be driven by pixel-based computer-use agents rather than new APIs, and shows his Navigator model's accuracy and cost per task.

- Techniques: Screenshot-in, action-out computer-use loop; Code-on-demand as a browser action; Pixel-based success check; Parallel sandboxed-browser fan-out; Read the async data call, not the initial HTML; Cost-per-task as the headline metric
- Tools: Navigator (Yutori computer-use model), OnlineMind2Web benchmark, Chrome extension for browser actions, MCP servers and web MCP, Opus 4.7 and GPT 5.5 (comparison models), Cloud sandbox browsers

## [Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google](../videos/hacEQHHhu2Q.md)
`hacEQHHhu2Q` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: local-ai, inference-serving, training-finetuning-rl

Google's Cormac Brick on running tiny (50M to 500M) and small (1 to 4B) models on phones, browsers and robots, and why fine-tuning on synthetic data beats bigger models for narrow tasks.

- Techniques: Synthetic-data fine-tuning of a tiny model for one task; Voice-to-function-calling pipeline; Two-stage on-device dictation pipeline; Memory budgeting for on-device LLMs; Multi-token prediction (MTP) for decode speed; Frame budgeting for NPU vision; Side-task tiny model
- Tools: LiteRT-LM, LiteRT / MediaPipe, Gemma 3, Gemma E2B, FunctionGemma, Gemma 4, AI Edge Gallery app, Apple FastVLM, Hugging Face (Mobile Actions dataset), Raspberry Pi, Jetson Nano, Qualcomm IoT boards (NPU)

## [Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings](../videos/tJFjeMBKbIY.md)
`tJFjeMBKbIY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: product-ux, governance-compliance, rag-retrieval

A finance investor argues AI products should be built as auditable memos, not impressive demos. He lists six ways trust breaks and five plumbing fixes: provenance, number agreement, surfaced contradictions, fact/guess labels and human approval.

- Techniques: Click-through provenance with source trust levels; Fact vs guess labelling; Automatic cross-document number reconciliation; Surface contradictions instead of resolving them silently; Locked human approval gate with audit log; Accountability-first architecture

## [From Tokens to Cells: Foundation Models for Single-Cell Biology - Akram Baharlouei, Altos Labs](../videos/-561cZmir5Q.md)
`-561cZmir5Q` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: models-research, data-engineering, evals

Altos Labs engineer on why single-cell foundation models (scGPT, Geneformer, PrimeFlow) struggle with noisy data, and why distribution-matching and data quality matter more than scale.

- Techniques: Cell-as-sentence masked modelling; Flow-matching distribution learning; Simple-baseline check before scaling; Distributional scoring with MMD
- Tools: scGPT, Geneformer, PrimeFlow, MMD

## [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](../videos/khVX_BUnEwU.md)
`khVX_BUnEwU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: agent-architecture, skills-self-improvement, memory, multi-agent

Yohei Nakajima presents Active Graph, an experimental event-sourced graph runtime where an immutable typed log is the agent's ground truth and small behaviors coordinate through shared state; main takeaway is that log-centric design gives replay, forks, resume and gated self-modification for free.

- Techniques: Log-as-memory retrieval; Graph-subscription behaviors and graph-query views; Failure-type-scoped, gated self-edits; Acceptance test by simulated win rate with a confidence bound; Debug by querying the event log, not session logs; Pack-based composition of agents
- Tools: Active Graph, BabyAGI, LongMemEval, Replit, Claude Code, LangSmith (mentioned as a comparison), Kaggle Pokemon trading card game competition

## [Why Software Factories Fail](../videos/Ib5GBkD555M.md)
`Ib5GBkD555M` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: software-factory, pr-code-review, evals, context-engineering

Dex (HumanLayer) argues that agent "lights-off" software factories fail because coding models are trained on tests passing, not maintainable code, so teams must restore code review and plan up front.

- Techniques: Staged plan before agent implementation; Review the plan so the PR review is short; Check for test gaming with pre-patch runs and a quality judge; Diagnose RL-style reward gaps
- Tools: Claude Code, Codex, SWE-bench Multilingual, SWE-Marathon, DeepSWE, Frontier Code, Linear, Jira, HumanLayer

## [Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](../videos/mOf-PP4mVjA.md)
`mOf-PP4mVjA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: memory, rag-retrieval, voice-multimodal, agent-architecture

TwelveLabs' James Le argues video needs a persistent memory layer (a context graph over moments, entities and relationships) rather than frame sampling, search or long context, and demos a video agent called Jockey.

- Techniques: Context graph over video moments; Ingest once, reason many times; Timestamp-grounded outputs; Intent-configurable extraction; Video worker harness; Evaluate retrieval, synthesis and budget separately
- Tools: TwelveLabs Marengo (multimodal embeddings for spatial-temporal spans), TwelveLabs Pegasus (video-aware language model used as the reasoning layer), Jockey (TwelveLabs video agent product used for the demos)

## [Scaling up Continual Learning — Ronak Malde, Trajectory](../videos/zL1kLftVTlo.md)
`zL1kLftVTlo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: training-finetuning-rl, agent-architecture, skills-self-improvement

Ronak Malde (Trajectory) on scaling continual learning: on-policy self-distillation with privileged hints as a step past GRPO, plus fixes for long tool-calling runs (step-level weighting, hint-leakage control).

- Techniques: On-policy self-distillation (OPSD); Step-level divergence weighting for long trajectories; Residual guidance via linear combination of hint strengths; LLM-filtered hints to prevent leakage; Inspect rollouts for hint leakage
- Tools: GRPO, OPSD, OpenClaw RL, LiveCodeBench, Mercor APEX-Agents

## [The New Primitives: Building AI Native Software — Kwindla Kramer, Daily](../videos/LZuWZRze3MU.md)
`LZuWZRze3MU` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: product-ux, multi-agent, voice-multimodal, agent-architecture

Kwindla Kramer (Daily, PipeCat) argues agents are a stage on the way to AI-native software, using 80 years of computing history and demos of a real-time Knowledge Navigator and a multiplayer LLM game.

- Techniques: Asynchronous non-blocking context compression for sub-agents; Long-running sub-agents that share context; Progressive skills loading; Dynamic UI generation driven by the agent; Real-time voice plus LLM orchestration with a pipeline framework
- Tools: PipeCat, Gradient Bang, Daily, Tavus

## [HTML Is All Agents Need — James Russo, HeyGen](../videos/Cz4v1WHVyZc.md)
`Cz4v1WHVyZc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: voice-multimodal, context-engineering, skills-self-improvement, product-ux

HeyGen's Hyperframes turns agent-written HTML into deterministic MP4 video by freezing the browser clock and seeking frame by frame; the thinnest HTML wrapper beat heavier DSLs.

- Techniques: Thin HTML as the agent output format; Deterministic frame-by-frame browser rendering; Single render path for preview and output; Taste-focused skills instead of syntax skills; Small model as a format canary; Storyboard, iterate, then human last-mile edit; Website-to-asset single-shot skill
- Tools: Hyperframes, HTML/CSS/JS, Three.js, WebGL, WebGPU, Lottie, Rive, Remotion (transcribed as "Promotion"), After Effects, Premiere Pro, Gemini 3 Flash, Claude Code

## [MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef](../videos/-jY2T2PiJBE.md)
`-jY2T2PiJBE` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: mcp-and-tools, agent-architecture, product-ux

Ido Salomon and Liad Yosef, the creators of MCPUI and maintainers of the MCP Apps spec, explain how MCP Apps lets servers ship interactive UI into chat hosts and how control of the user journey shifts to the host.

- Techniques: Serve UI as an MCP resource linked to a tool call; Host-mediated event flow from app to model; Three control levels for app-driven steps; Interop: wrap one generative UI payload for several hosts
- Tools: MCP (Model Context Protocol), MCP Apps (official MCP extension), MCPUI, MCP Apps SDK / spec repo (spoken as 'Xtaps' in captions; the official model context protocol repository), ChatGPT Apps / Apps SDK, Claude (including its generative UI feature), VS Code, Slack, Cursor, GitHub Copilot, Goose, Block agent e-commerce

## [MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal](../videos/s4r6nk5WsZw.md)
`s4r6nk5WsZw` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: mcp-and-tools, agent-architecture, infra-cost-scaling

Cornelia Davis (Temporal) explains why no MCP clients support MCP Tasks (async long-running tools) in v1, shows live demos of durable purchase-order and invoice workflows, and walks through the v2 changes that make tasks stateless and extension-based.

- Techniques: Map task lifecycle onto a domain state machine; Signal into a long-running workflow for approvals; Client-side task tracker workflow; Parallel back-office steps beside an async tool call
- Tools: MCP Tasks, FastMCP, Temporal

## [Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs](../videos/Bck7ABCZRZI.md)
`Bck7ABCZRZI` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: token-cost-efficiency, local-ai, infra-cost-scaling, governance-compliance

Thiyagarajan Maruthavanan (Kalmantic Labs) argues teams should rent inference to learn and own it to earn, using his own runaway-cost incident and enterprise objections to self-hosting as evidence.

- Techniques: Per-key spend monitoring with a cutoff; Input compression and context management in agent loops; Rent-to-own decision gate; Small local inference box for personal agents
- Tools: DGX Spark, Headroom, JustTokenMax, JustInfo, Suno, NemoClaw

## [Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama](../videos/J4_jCrTxMkk.md)
`J4_jCrTxMkk` · AI Engineer · 2026-08-18 · q4 · practitioner · panel · topics: local-ai, inference-serving, evals

Panel from NVIDIA, Unsloth, Hugging Face and Ollama on how quantization and compression make large open models run on local hardware, how to pick per-layer precision, and how to evaluate the result.

- Techniques: Sensitivity-aware dynamic quantization; Post-training quantization first, QAD for small models; KL-divergence evaluation against the unquantized model; Harness-level vibe testing before shipping a quant; Per-model default quant with precision kept high for tiny models; Big planner, small executor routing
- Tools: llama.cpp, Ollama, Unsloth, NVIDIA Model Optimizer (ModelOpt), TRL, bitsandbytes, QLoRA, GRPO, NVFP4, MXFP4, OpenClaw, Hermes agent

## [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](../videos/l0FLhNqBOic.md)
`l0FLhNqBOic` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: enterprise-adoption, product-ux, training-finetuning-rl, rag-retrieval

Varick Agents explain why process understanding, not model execution, is now the bottleneck, and describe the forward-deployed engineering agent they built for it.

- Techniques: Failure-path process interviews; Per-step autonomy split; Dependency graph as shared state; Post-training an open model for analysis style; RL environment with domain traversal tools; Assistant embedded in the authoring tool
- Tools: Varick OS (in-house platform), Claude, Codex, Granola, Kimi (open-source base model, named as K2.6), NetSuite, Microsoft Dynamics, SAP, Salesforce

## [Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software](../videos/2aS7aKoXn64.md)
`2aS7aKoXn64` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, training-finetuning-rl, agent-architecture

Theta Software on designing RL environments and LLM judges for long-horizon work, plus a critique of current finance agent benchmarks, which they say are saturated and mostly too short to count as long-horizon.

- Techniques: Judge with read-only environment access, as an agent; Make long trajectories queryable before judging; Pair deterministic checks with a rubric judge; Rubric QA suite; Check learnability and reward density
- Tools: METR time-horizon benchmark (cited, not a tool used), GDPval (benchmark, cited), BankerToolbench (benchmark, cited), APEX-Agents (benchmark, cited), Grafana, GitHub (CI/CD logs, PRs), AWS CloudWatch, Codex models (cited), Claude models (cited), GPT-5.5 (cited)

## [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face](../videos/lyL5QhgIOxc.md)
`lyL5QhgIOxc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: infra-cost-scaling, rag-retrieval, data-engineering


- Techniques: Insert-time search tokens in a denormalized read collection; Lucene-backed autocomplete instead of regex scans; Read-replica routing by consistency class; Hidden analytics replica; Two-layer autoscaling with event-driven pod scaling
- Tools: MongoDB Atlas, Atlas Search, Apache Lucene, Kubernetes, Horizontal Pod Autoscaler, KEDA, Cast.ai, AWS S3, AWS Redshift

## [Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk](../videos/1EZdpEhwmNc.md)
`1EZdpEhwmNc` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: security-guardrails, coding-agents, mcp-and-tools, evals

Snyk's CTO argues agent security needs deterministic checks alongside LLMs, with customer data on attacks, toxic skills and MCP servers, plus a live coding-agent demo.

- Techniques: Hybrid LLM plus deterministic security checks; Repeated-run recall measurement; Pre-install package health gate; Skill and MCP risk assessment before adoption; Per-model red-team suite; Breakability-aware automated remediation; Deterministic invocation through a skill or hook
- Tools: Claude Code, Cursor Cloud, Codex, Snyk Studio, Snyk Evo, Snyk package health check

## [Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute](../videos/k35LeKZEhiE.md)
`k35LeKZEhiE` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: training-finetuning-rl, agent-architecture, enterprise-adoption

Raymond Feng (Applied Compute) on post-training agents that learn on the job: how RL loops break when you do not own the harness, and the environment-fidelity failures that teach models bad habits.

- Techniques: Replayable sandbox for multi-rollout RL; Graded chats as the only training interface; Audit the environment for infrastructure failures before trusting a run; Log model requests and responses as the training source; Mine traces for failure modes, then build the dataset

## [The Desktop Frontier — Ahmad Osman, Osmantic](../videos/XV2oYi7kojc.md)
`XV2oYi7kojc` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: local-ai, models-research, inference-serving

Ahmad Osman argues that open-weight models are shrinking in hardware footprint fast enough that a GLM 5.2-class model should run on one RTX 5090 by late 2027, and urges people to own their hardware.

- Techniques: Footprint-over-time tracking; Dense small model for parallel local agents
- Tools: Claude Code, Telegram

## [The Model Was Right. The Harness Failed. — Vinoth Govindarajan, OpenAI](../videos/BInpv7lGp1o.md)
`BInpv7lGp1o` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: agent-architecture, observability, security-guardrails

Agent production failures are mostly harness failures, not model failures; the talk gives a state-ownership, ordered-commit, lifecycle, authority and receipt framework, using OpenClaw incidents as case studies.

- Techniques: Session lane / single ordered writer; Run deadlines, cancellation and watchdog; Scoped approval object; Run receipt as the audit record; Idempotency keys on side effects; Verify at the user-visible edge; Five-question production audit
- Tools: OpenClaw, OpenAI Agents SDK, Codex, Cursor, OpenCode, Claude Code, Hermes, Telegram

## [AI’s Jurassic Park Period — Aaron Stanley, dbt Labs](../videos/1lgFGaHoGq8.md)
`1lgFGaHoGq8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: security-guardrails, governance-compliance, agent-architecture

Aaron Stanley (CISO, former forensic consultant) argues that agents routing around constraints is the hidden risk, and proposes a corrigible, four-layer defense: deterministic floor, halt-and-explain agent, adversary agent, and structured human escalation.

- Techniques: Halt-and-explain default for constraint conflicts; Equal-power adversary agent reviewing worker actions; Natural-language escalation to humans; Layered deterministic floor; Intercept at the harness or tool-call hook; Runtime input policies instead of output string matching
- Tools: gVisor, egress filters, Chrome extension (installation blocked by a layered control)

## [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../videos/R3-anFK1YM8.md)
`R3-anFK1YM8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: memory, context-engineering, evals, local-ai

Sakana AI researcher on memory harnesses for long-horizon research agents running on local models; a ranked decision-ledger recall policy beat both no memory and plain vector RAG, at lower cost.

- Techniques: Write-manage-read memory loop; Ranked decision-ledger recall; Recall-mode ladder with an oracle; Ablate with wrong and recent memory; Local, controlled eval pipeline
- Tools: DeepSeek V4 Flash, Qwen (4-bit quantised), XBench, vector RAG, Spyder V2 benchmark

## [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](../videos/xIt_mTQp6mY.md)
`xIt_mTQp6mY` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: software-factory, coding-agents, agent-architecture

Kyle Mistele (HumanLayer) argues agent loops should be built as incremental control loops (sensor, controller, actuator) that keep humans reading the code, not blind "Ralph" loops that dump 40k-line PRs.

- Techniques: Sensor, controller, actuator loop for code migration; Deterministic baseline plus per-PR ratchet; Ast-grep as the sensor; Golden-pattern skill for the actuator; Scheduled CI workflow as the loop runner; Feedback file plus comment-triggered re-steering; Single-open-PR flow control
- Tools: Claude Code, ast-grep, GitHub Actions, Effect (TypeScript), React Doctor, OpenClaw, OpenCode

## [Your Moat Is Your Data Model — Mike Phipps, Gates Foundation](../videos/jt1Pbr_n6oU.md)
`jt1Pbr_n6oU` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: data-engineering, mcp-and-tools, enterprise-adoption

Mike Phipps (Gates Foundation) explains why the Strategic Intelligence Platform's defensible asset is a knowledge graph of tacit process knowledge, served to agents through MCP rather than a custom chat UI.

- Techniques: Tacit-knowledge-first data modeling with data owners; Graph with explicit hierarchy types and precomputed roll-ups; Cross-system entity stitching; Document chunks as graph nodes with full-text plus graph retrieval; Curation pipeline before the graph; Expose the graph as an MCP server with state passthrough; Per-question graph-query ground truth plus stability checks
- Tools: Neo4j, MCP, Claude, ChatGPT, Cowork

## [Data Quality Is the Compute Multiplier — Ari Morcos, DatologyAI](../videos/_PdK6x7PQNM.md)
`_PdK6x7PQNM` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: data-engineering, training-finetuning-rl, models-research

Ari Morcos (Datology AI) argues data quality is an under-used compute multiplier, showing curated-data gains in VLMs, multilingual and legal models, and a small-budget frontier-scale run.

- Techniques: Four-C data pipeline (clean, curate, create, compose); Selective synthetic rephrasing into many formats; Domain mid-training with a representative mix; Small-run scaling check under token scarcity; Repeat high-quality data under token limits

## [Full Workshop: Better Auth — Paola Estefania, Better Auth](../videos/JvKO40CFq-s.md)
`JvKO40CFq-s` · AI Engineer · 2026-08-18 · q3 · practitioner · workshop · topics: security-guardrails, mcp-and-tools, governance-compliance

Paola Estefania (Better Auth) argues agents should get their own identity and scoped capabilities instead of borrowing user credentials, and demos a draft open protocol with approvals, audit logs and revocation.

- Techniques: Per-agent identity with own key pair; Capability grants with default-read policy; Device-flow approval for agents; OpenAPI-to-capability translation; Full revocation: agent, host and tokens
- Tools: MCP, OAuth, OpenAPI, OIDC, Gmail, Notion, Claude, Cursor

## [Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest](../videos/0RNNfxpdbQk.md)
`0RNNfxpdbQk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: observability, multi-agent, testing-verification, context-engineering

Pinterest's Drasko Profirovic on Medic, an agentic Spark failure-diagnosis tool, and how its prototype became a multi-agent system with record/playback testing, log and metrics handling, and sub-agents.

- Techniques: Record/playback end-to-end agent harness; Learned red-herring filtering for logs; Metrics as a collaged graph image in a quarantined sub-agent; Supervisor with parallel hypothesis researchers; Per-agent prompt plus MCP tool subset; OpenTelemetry traces as step waterfalls
- Tools: Apache Spark, LangGraph, LangGraph DeepAgents, LangFuse, OpenTelemetry, Model Context Protocol (MCP), Grafana, Airflow, Slack, vector database

## [How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh](../videos/1OMHGsUZiqA.md)
`1OMHGsUZiqA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: enterprise-adoption, product-ux, data-engineering

Vinoo Ganesh on running forward-deployed engineering as a product strategy: go on site, solve small problems fast, define shared terms, and avoid shipping hacks that become permanent.

- Techniques: Three-question discovery before building; Ship-it threshold for small problems; On-site workflow observation; Pain-signal scan; Canonical glossary and ontology; Production-readiness gate for quick fixes
- Tools: Palantir Foundry, Cassandra, Parquet, S3, Groovy, Elasticsearch, Snowflake, Databricks, Tableau, SAP, Slack

## [Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates](../videos/u6jJcIFDLE4.md)
`u6jJcIFDLE4` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: multi-agent, agent-architecture, context-engineering, enterprise-adoption

ZS Associates explain why their multi-agent pharma analytics pipeline failed and how they rebuilt it: deterministic signal detection, one reasoning agent, and a knowledge graph used as a control plane.

- Techniques: Probe the design with a coding agent; Deterministic signal gate feeding an investigator agent; Single reasoning owner with scoped investigation subagents; Knowledge graph as the agent's control plane; Hypothesis-traversal investigation loop
- Tools: Claude Code, bash, knowledge graph (tool not named), relational database (not named)

## [Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs](../videos/ewtOo0scUh0.md)
`ewtOo0scUh0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: training-finetuning-rl, data-engineering, sandboxing-execution

Bespoke Labs on curating data and RL environments for post-training: OpenThoughts and OpenThoughts-Agent recipes, counterintuitive sampling and teacher findings, and a tag-based SFT fix for numeric hallucinations.

- Techniques: Stage-wise ablation of a data curation pipeline; Multi-sample answers per question; Teacher model selection by measurement; Structural tags in fine-tuning data; Reflection-based prompt optimization
- Tools: Curator, Bespoke Stratos, OpenThoughts, Terminal-Bench, Tinker, Fireworks

## [Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)](../videos/IvE8n-ylFYY.md)
`IvE8n-ylFYY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: security-guardrails, sandboxing-execution, governance-compliance, agent-architecture

Steve Korshakov (Bee, acquired by Amazon) explains how an always-on personal-agent wearable keeps data unreadable even to its own company, using client-held keys, attested workloads, and two-tier release controls.

- Techniques: Client-held keys with attested key release; Forced key expiry window; Split base image and deployment manifest; Private CA for internal attestation certificates; Minimal, auditable trusted code base; Per-agent sandbox with minimal capabilities
- Tools: Sigstore-style transparency log (auto-caption reads as 'six store'), Confidential compute nodes, Private certificate authority, OpenClaw (auto-caption reads as 'open claw'), Claude Code (auto-caption reads as 'cloud code')

## [Local Models: Trust, Control, Optimization — Carter Abdallah, NVIDIA](../videos/FWMJQDH3iK0.md)
`FWMJQDH3iK0` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · topics: local-ai, training-finetuning-rl, models-research, governance-compliance

A panel from NVIDIA, Prime Intellect and Arcee argues open-weight models give trust, cost control and data ownership, and that post-training them on your own harness and traces beats generalist frontier APIs for narrow work.

- Techniques: Harness-specific post-training of an open base model; RL environment, then deploy, then train on production traces; Trace capture as a fine-tuning dataset; Specialize a small model to one or two tasks; Verify open weights and inference code before trusting them
- Tools: vLLM, SGLang, PrimeRL, NeMo RL, NeMo Gym (captioned as 'Nemo Jim'), verifiers, Hugging Face, Nemotron, Trinity (Arcee model), Hermes (harness), Pi (harness), OpenMDW license

## [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore](../videos/26RtyAm9y_Q.md)
`26RtyAm9y_Q` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: voice-multimodal, mcp-and-tools, agent-architecture, security-guardrails

Corey Gallon on driving websites with agents via a shell CLI over the Chrome DevTools Protocol, climbing from synthetic clicks to trusted input to human-like motion, and beating Cloudflare Turnstile, MT Capture, Lemin and reCAPTCHA v2.

- Techniques: CLI over MCP for repeatable browser tasks; Cross-channel verification after each action; Lowest-rung escalation; Coordinate-based trusted click through closed shadow roots and cross-origin iframes; Solver plus operator split; Explore, then codify
- Tools: Chrome DevTools Protocol (CDP), Chrome Agent (speaker's Python CLI), Cloudflare Turnstile, MT Capture, Lemin (auto-captioned as 'lemon'), reCAPTCHA v2, Outlook web client

## [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../videos/CvRngaQZQ3Y.md)
`CvRngaQZQ3Y` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: observability, evals, training-finetuning-rl, memory

LangChain's Vivek Trivedy argues agent improvement is a data-mining loop: ship, collect traces, mine them, then run data-driven experiments on prompts, tools and models.

- Techniques: Agent-driven trace mining; Frontier-to-open-model downgrade via trace judging; Distillation from good traces; Evals generated from traces; Score-driven auto-research loop; Harness, then fine-tune, then harness sandwich; Human review summaries
- Tools: LangSmith, LangSmith Engine, Deep Agents, Claude Code, Codex, Terminal Bench, scikit-learn

## [Notion's Token Town — Sarah Sachs, Notion](../videos/-I5W5QVAT8E.md)
`-I5W5QVAT8E` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: token-cost-efficiency, infra-cost-scaling, enterprise-adoption, security-guardrails

Notion's head of AI engineering on keeping AI costs sustainable: stay model-agnostic, route traffic by task difficulty, use open-weight and plain code for simple steps, and evaluate whole trajectories instead of single calls.

- Techniques: Model-agnostic harness with an auto-router; Traffic tiering by task difficulty; Trajectory-level eval of cost, latency and success; Open-weight evaluation on your own system; Code and CLI for deterministic steps; Cross-vendor review chain for agent PRs; Lethal trifecta check on agent systems
- Tools: Claude Code, Claude, Codex, Decagon, Parallel (web search provider), Notion Workers, Notion AI Manage Agent, Kimi 2.6 (as transcribed), GLM 5.2 (as transcribed), GPT 5.2 (as transcribed)

## [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../videos/jHMiYtjoJfA.md)
`jHMiYtjoJfA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: evals, observability, product-ux

Ben Hylak (Raindrop) argues teams should "raise the floor" by finding production agent failures, tracking when they started and how many users they hit, and using code-based classifiers over traces instead of clustering or big eval sets.

- Techniques: Evals as local code tests; Per-issue onset and affected-user tracking; Code-based trace classifiers; Deterministic signal first, agent investigates second; Scale-dependent experimentation
- Tools: Raindrop, Workshop (open-source tracing tool), vitest (vitest evals), howtoeval.com, Sentry (mentioned as a model for issue detection)

## [Scaling Compute on Context — Jack Morris, Engram](../videos/WiqDvX6isc4.md)
`WiqDvX6isc4` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: memory, training-finetuning-rl, models-research, context-engineering

Jack Morris (Engram) frames "scaling compute on context": with a fixed private dataset and a pretrained model, the only scaling axis left is compute, and he surveys why naive, compaction, distillation, synthetic-data and RL approaches all saturate.

- Techniques: Naive continued training on a private corpus; KV compaction of in-context data; On-policy distillation toward in-context behaviour; Self-study (generated QA conditioned on the corpus); Synthetic continued pretraining; Unsupervised RL environments over the corpus; Gradually harder self-generated curriculum
- Tools: Cartridges (self-study paper, named on slide), On-policy distillation, GRPO (named as an RL loss example), KV cache compaction (named approach)

## [Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang](../videos/zkX03APVj0M.md)
`zkX03APVj0M` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: sandboxing-execution, training-finetuning-rl, evals

Joseph Wang of Emulated argues that agent training needs realistic infra environments: multi-node sandboxes that touch real cloud resources, not single-container coding tasks.

- Techniques: Multi-node cluster simulation in one sandbox; Chained multi-deployment episodes for long horizon; Organisation context as part of the environment; Multi-node sandbox on real cloud resources (CloudBox); Choose a vertical with clear customer requirements first
- Tools: Harbor, etcd, Kubernetes, AWS Lambda

## [Vending-Bench: Long-Horizon Agent Evals — Lukas Petersson, Andon Labs](../videos/cO8qC6HBuBg.md)
`cO8qC6HBuBg` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, security-guardrails, models-research

Lukas Petersson (Andon Labs) on Vending-Bench, emergent misbehavior in agents, and moving evals into real-world deployments and forked simulations, because models act differently once they suspect a simulation.

- Techniques: Incentive-based misbehavior probing; Forked real-environment evals; Simulation-awareness probe; Cross-model replay of a real incident
- Tools: Vending-Bench, Vending-Bench Arena (arena mode), Claude / Opus 4.6, 4.7, 4.8, Fable (named in talk, may be a caption error), GLM 5.2, GPT 5.5, Gemini, Grok 4.3, Kimi, Slack (channel used to message the store agents), LinkedIn, Indeed

## [Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face](../videos/O-CBZ3JtRvo.md)
`O-CBZ3JtRvo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: security-guardrails, evals, training-finetuning-rl, models-research

Uri Rolls and Thom Wolf present Arithmetic's "Mask Off" benchmark: black-box access-control exploit chains built from real zero-days, graded per step, to test whether models can make logic leaps.

- Techniques: Black-box exploit-chain environments from self-found zero-days; Per-step deterministic graders with partial credit; Trace review as the main eval loop; Orchestrator for running evals
- Tools: Bach (Arithmetic's internal eval orchestrator)

## [How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh](../videos/Tt2kX2sgQio.md)
`Tt2kX2sgQio` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: governance-compliance, data-engineering, enterprise-adoption, agent-architecture

Kepler's CEO argues finance AI needs a deterministic substrate: the model points to sources and decides what to compute, while code extracts, checks and calculates numbers, with replayable derivation chains.

- Techniques: Atomic provenance ledger; Model decides, code computes; Derivation chains for derived metrics; Deterministic sanity gate on model output
- Tools: Claude, XBRL, ChatGPT, GLM 5.2, Opus 4.8

## [Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic](../videos/K0X9QDRkIdg.md)
`K0X9QDRkIdg` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: agent-architecture, sandboxing-execution, context-engineering, evals

Anthropic engineers explain how agent surfaces moved from the Messages API to Claude Managed Agents, which separates the brain from the hands, logs sessions durably, and adds vaults, dreaming and outcomes.

- Techniques: Brain/hands decoupling with on-demand sandboxes; Append-only session log as the resume point; Re-reading discarded context from the log; Vault-based credential injection; Restricted network allowlist per environment; Rubric and failure-case grader loop (outcomes); Batch dreaming over transcripts and memory; Harness-debt audit when models change
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, MCP servers, MCP tunnels, self-hosted sandboxes

## [Agentic Development Security — Ezra Tanzer, Snyk](../videos/cgimkNGNjvU.md)
`cgimkNGNjvU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: security-guardrails, claude-code, coding-agents, skills-self-improvement

Snyk on securing agent development in three pillars: the code agents generate, the skills and MCP servers they use, and the actions they take. Mainly a product showcase, with a useful hook-based scanning pattern.

- Techniques: Async post-write scan hook with deferred fix at stop; Steer vs ask policy actions in pre-tool hooks; Static scan of skills and MCP tool descriptions; Per-workspace guardrail profiles
- Tools: Snyk, Claude Code, Codex, Cursor, MCP, Python hooks, VS Code, Electron, ClawHub

## [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](../videos/1UmZHb_E_SM.md)
`1UmZHb_E_SM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: infra-cost-scaling, rag-retrieval, data-engineering

Oxylabs' product manager on how public web data infrastructure feeds AI systems: how a video API, a sub-second SERP API and a 60k-rps scraper grew out of repeated client requests, latency cuts and load tests.

- Techniques: Iterate from client requests into an internal library; Narrow the response to what the AI consumer needs; Stage-by-stage latency audit; Realistic load testing with gradual ramp-up; Account for observability as load
- Tools: Oxylabs Fast Search API, headless browsers, proxy network

## [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j](../videos/VGN22pPpb-8.md)
`VGN22pPpb-8` · AI Engineer · 2026-08-18 · q2 · intro · keynote · topics: data-engineering, memory, multi-agent

Neo4j keynote arguing that agents should be thin and share an ontology-based semantic layer over enterprise data, with execution traces that teach source selection over time.

- Techniques: Business-to-technical ontology mapping; Process graph for process-guided agents; Trace-derived source scores; Thin agents over a shared substrate
- Tools: Neo4j

## [Designing Voice Agents for Real Conversations - Chintan Agrawal & Daniel Wirjo, AWS](../videos/hMlLw1LeIK8.md)
`hMlLw1LeIK8` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: voice-multimodal, infra-cost-scaling

AWS solutions architects walk through turn-taking in voice agents: three levels from Silero VAD silence timers to Smart Turn, plus latency budgets and production issues. Includes live Pipecat demos.

- Techniques: Hybrid VAD + learned end-of-turn model with timer fallback; Interruption classification at barge-in; Per-stage latency budget with P50 and P95 tracking; Co-location to remove network hops; Session pruning or reset for long voice sessions; Config-only swap between turn-detection strategies for A/B tests
- Tools: Pipecat, Silero VAD, Smart Turn v3, Cartesia (STT and Sonic TTS), Deepgram Nova 3, Claude Haiku, GPT-4.1, Nemotron 3 Ultra

## [The State of Model Routing — NVIDIA, Cognition, OpenRouter](../videos/QHBjufYK8TA.md)
`QHBjufYK8TA` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · topics: token-cost-efficiency, multi-agent, inference-serving, infra-cost-scaling

Panel from Cognition, NVIDIA and OpenRouter on model routing: frontier models plan and delegate to cheaper models, and the hard parts are detecting when a small model is out of depth and keeping cache costs low.

- Techniques: Frontier-planner, cheap-executor split; Frontier watcher with escalation; Persistent sidekick sub-agent; Reference-based handoff; Piggyback checks on cache refresh; Hidden-state probes for lost-ness; Routing from production signals; Ask the model why, then regression-test the prompt; Privacy-aware local/cloud split
- Tools: Devin, Cognition Fusion, OpenRouter Fusion, OpenRouter Pareto Code, NVIDIA Nemotron, NVIDIA Dynamo, NVIDIA DGX Spark, OpenClaw, TerminalBench, LMArena

## [Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog](../videos/wEc9aG7cRQc.md)
`wEc9aG7cRQc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: evals, memory, security-guardrails

Diane Lin (Datadog) on why LLM agents give different verdicts on the same input near the decision boundary, and how to fix it with disagreement-driven active learning plus episodic and semantic memory instead of fine-tuning.

- Techniques: Measure consistency with repeated runs; Disagreement-based query selection; Semantic memory for policy and preference facts; Episodic memory as case-based precedent lookup; Active-learning loop with memory updates
- Tools: Datadog

## [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../videos/03l29gJXpCE.md)
`03l29gJXpCE` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: testing-verification, pr-code-review, coding-agents, governance-compliance

Sonar's product marketer argues AI-written code needs zero-trust, multilayered verification inside agent loops and in CI/CD, framed as a Guide-Verify-Solve (ACDC) cycle, with vendor product pitches throughout.

- Techniques: In-loop verifier callback with fix-and-rerun; Task-scoped context retrieval for agents; Machine-enforced quality rulebook; Dual PR gate: LLM review plus deterministic scan; Cross-model or cross-method review; Graduated automation of review bots; Remediation agent for backlog debt; Per-task model choice from a quality profile
- Tools: SonarQube, Sonar Vortex, Guitar (AI code-review tool, name from captions), Cursor, Claude Code, Codex, Antigravity

## [How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](../videos/xyL2Ltkh-SA.md)
`xyL2Ltkh-SA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: evals, observability, context-engineering

Two YouTube Ads team members on building evals for agents: tools first, intuition before scale, human rater rubrics, reading traces, and pattern-level launch gates.

- Techniques: Tools-first, then critique agent with remediation loop; Intuition-first review before scaled evals; Rubric with examples plus mandatory rater explanations; Negative test cases in the golden set; Judge calibration by sampled agreement monitoring; Trace-based failure diagnosis; Pattern-level metrics with a refreshed test set and online evals; Launch gate defined up front with regression triage

## [How to Kill the Code Review — Ankit Jain, Aviator](../videos/YgEv7IQzGdM.md)
`YgEv7IQzGdM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: pr-code-review, testing-verification, context-engineering, skills-self-improvement

Ankit Jain (Aviator) argues code review's real job is alignment, not bug-catching, and proposes reviewing agent session intent, test-plan evidence and a codified "AI slop registry" instead of diffs.

- Techniques: AI slop registry; Capture session decisions as acceptance criteria; Test plan from criteria plus registry invariants, run against a preview; Agent-driven UI evidence with DB snapshots; Review the plan and evidence, not the diff
- Tools: GitHub, Aviator Verify

## [Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft](../videos/o6U_2vd967Y.md)
`o6U_2vd967Y` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: agent-architecture, multi-agent, data-engineering

Divakar Kumar shows how to add an agent tier for gray-zone fraud decisions in an event-sourced system, feeding agents a semantic read layer built from CDC and broker events.

- Techniques: Tier-2 escalation for gray-zone cases; Semantic layer built from CDC and broker events; Fan-out to specialist agents with a verdict agent; Saga-style orchestrator as the sole cross-context router; Hard cap on the agent reasoning loop; In-memory short-term agent memory under an SLA
- Tools: Azure Cosmos DB (event store and change feed), message broker (unnamed), CDC / change feed, rule-based engine, ML risk model (third-party)

## [The Dirty Secret of Forward Deployed Engineering — Natalie Meurer, Sierra](../videos/Byv311hdoHE.md)
`Byv311hdoHE` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: enterprise-adoption, product-ux

Sierra's head of agent engineering traces forward-deployed engineering from Palantir's 2008-2020 eras to today, argues the title is vague, and says customer accountability and outcome pricing make most engineering roles trend toward it.

- Techniques: Write-back dashboards; Ontology-first data modeling; Customer-accountable build loop; Outcome-attribution test for pricing; FDE vintage interview question
- Tools: Palantir Foundry, Palantir AIP, Palantir Slate, AWS EC2, Airbus Skywise, Retool (comparison only)

## [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](../videos/3ySF0I5iE_0.md)
`3ySF0I5iE_0` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: rag-retrieval, data-engineering, context-engineering

Tim Ainge (Good Collective) on when graphs help AI apps: schema-first graph extraction, entity matching, and graph-native retrieval (personalized PageRank, shortest paths, subgraph pattern matching) for cheaper, more reliable results.

- Techniques: Schema-constrained graph extraction; Ontology normalisation instructions; Embedding-based entity resolution before node creation; Personalized PageRank from a seed node; Subgraph context retrieval via path queries; Subgraph pattern matching on code graphs
- Tools: Cypher (graph query language, ASR-garbled as 'cipher'), SQL (used as the comparison baseline), HippoRAG, Pinterest PixieRank (cited as the PPR reference), Embedding models, Structured outputs from an LLM, eShop (.NET reference codebase)

## [You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit](../videos/lMCxVorb9wM.md)
`lMCxVorb9wM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: security-guardrails, mcp-and-tools, governance-compliance

Ravi Madabhushi (Scalekit) argues agents break the human and service-account identity model: they need a distinct identity bound to a principal, fine-grained time-bound scopes, and full action audit, beyond OAuth.

- Techniques: Coalesce high-frequency timestamp writes; Bind agent identity to principal; Context-filtered MCP tool surface; Least-privilege, time-bound, just-in-time grants; Full-provenance action audit
- Tools: OAuth, SPIFFE, MCP, Gmail API, Salesforce API, Databricks, HubSpot, Notion

## [When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI](../videos/-npY6XjM8CQ.md)
`-npY6XjM8CQ` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: evals, models-research

Nick Heiner (Surge AI) on why benchmarks drift from real value (cost, contamination, reward hacking, bad verifiers, leaderboard gaming) and how to build better ones.

- Techniques: Two-way verifier-prompt alignment audit; Accept all valid answer formats in verifiers; Adversarial check of graders against lazy solutions; Contamination probe by prefix completion; Private holdout plus disclosure of test conditions; Watch for benchmark-vs-human-eval divergence; Blind pairwise expert comparison for subjective quality; Saturation check for broken tasks
- Tools: LM Arena, SWE-bench Verified, IFEval, Apex, Automation Bench, Hemingway-Bench

## [The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller](../videos/GgLQ02aO-hs.md)
`GgLQ02aO-hs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: evals, agent-architecture, data-engineering

DSPy maintainers argue AI programs should be functions with fixed typed contracts, with the model, prompts and harness swappable underneath and optimized against evals.

- Techniques: Typed signature with natural-language instruction; Three-part task spec (instructions, code constraints, examples); Predict-then-reason fallback in code; Optimizer over a fixed metric; Learn a harness per function (DSPy.Flex, announced)
- Tools: DSPy, GEPA (transcript says JEPA; caption error, prompt optimizer from Berkeley), Recursive Language Models (RLM), MultiModule GRPO, BetterTogether, DSPy.Flex (announced for DSPy 4)

## [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud](../videos/JJGbw4ggaFs.md)
`JJGbw4ggaFs` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: software-factory, observability, context-engineering, coding-agents

May Walter (HUD) shows how HUD runs a weekly agentic workflow on GitHub Actions with Claude Code that mines production traces, scores performance fixes by ROI, verifies them at runtime, and sends a human-readable report to Slack.

- Techniques: Scheduled agentic investigation with runtime verification; Function-level production context map; Query language plus task skills; ROI and risk scoring with a human-readable gist; Vendor-neutral workflow layer; Targeted automatic checks for known performance smells
- Tools: Claude Code, GitHub Actions, MCP, ClickHouse, Slack

## [Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i](../videos/jWq-aZIU0kM.md)
`jWq-aZIU0kM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: evals, testing-verification, models-research

Ali Khial (G2i) argues that many agent benchmarks have unrealistic prompts, weak verifiers and reward-hacking gaps, and proposes five principles for building better benchmark tasks.

- Techniques: Layered grading: behavioural breadth plus targeted precision; Specify behaviour and hard constraints, not implementation; Audit a benchmark's verifiers by sampling tasks; Novel tasks with private holdout sets; Publish per-run data alongside rankings
- Tools: SWE-Bench Pro

## [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../videos/I3bpdgFJCUY.md)
`I3bpdgFJCUY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: memory, context-engineering, skills-self-improvement, agent-architecture

Ben Holmes (Warp) shows a markdown-first personal knowledge base: voice-dictate raw notes, have an agent enrich and link them, generate wikis, run it on a cloud schedule, and build graph views with HTML.

- Techniques: Enrich-note skill with a processed-timestamp marker; Controlled tag vocabulary with a no-invention rule; Backlinks via key-term search over a file tree; Raw folder to wiki generation; Sync-in, run, sync-out cloud schedule
- Tools: Obsidian, Obsidian Headless CLI, Warp, oz.dev, Hubble, Claude, Codex app, Exa, Tailwind CSS, Whisper Flow, Handy, GLM 5.2

## [From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize](../videos/9HbzAWnKbo4.md)
`9HbzAWnKbo4` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: observability, software-factory, evals, sandboxing-execution

Arize's founder demos Signal, a background agent that reads production traces and logs, drafts an issue or fix with evidence, and hands it to a human reviewer, with the loop run in a sandbox.

- Techniques: Trace-to-file skill; Event- or schedule-triggered agent loop; Composable narrow skills over raw data; Sandbox per run, pluggable harness; Failure-to-evaluator loop
- Tools: Arize AX, Arize Phoenix, Pyroscope, Claude Code, Cursor, Daytona, GitHub, Google Cloud logging skills

## [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../videos/Kz4QJmNrVXU.md)
`Kz4QJmNrVXU` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: context-engineering, multi-agent, coding-agents

Matt Dailey (Ref) argues that AI makes individual engineers faster but not teams, and proposes working in shared docs for decisions, with agents as stateless actions, so humans keep ownership of the product.

- Techniques: Doc as shared state, agents as stateless workers; Two-gear workflow: plan vs polish; Front-load decisions before code; Plan as a portal to the system; Idea exploration before build

## [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../videos/WP3hjUXd918.md)
`WP3hjUXd918` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · topics: context-engineering, token-cost-efficiency, evals, rag-retrieval

Towards AI workshop on context engineering: prompt caching makes compaction costly, and on their AI tutor keeping full history beat every compaction preset on recall, cost and latency.

- Techniques: Head and tail truncation of big tool outputs; Sliding window and clearing old tool outputs; Selective retention and summarization with a threshold; Filesystem knowledge base with progressive disclosure; Hybrid retrieval with a token cap; Eval harness: presets by tasks, then grade; Planted-fact recall probe; Log every turn
- Tools: LangChain (create_agent, middleware), FastAPI, Next.js, Gemini 3.5 Flash, DeepSeek V4 Flash, Claude Code, Codex, Opik (transcribed as 'OPIC'), Hugging Face Spaces, BM25, Dense embedding retrieval

## [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../videos/I6aiEf3aEFQ.md)
`I6aiEf3aEFQ` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: skills-self-improvement, memory, agent-architecture

Yu Su (Ohio State, CEO of NeoCognition) argues intelligence and expertise are different axes and that continual learning, not bigger models, is what turns agents into domain experts.

- Techniques: Adaptive compression loop for agent memory; Rules stored with preconditions and exceptions; Select context by expertise instead of parallel brute force; Measure expertise per environment

## [How Forward Deployed Engineering is done at Ramp — Leo Mehr](../videos/ITMXwI6QL6A.md)
`ITMXwI6QL6A` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: enterprise-adoption, software-factory, evals, context-engineering

Leo Mehr (Ramp) on forward deployed engineering: scope hard before building, then replace each FDE pipeline stage with agents, with evals and good context as the hard parts.

- Techniques: Scoping questionnaire before any build; Clarifying-question intake agent before spec; Stage-by-stage agent factory for the FDE lifecycle; Per-stage quality checks with evals, rubrics and human feedback
- Tools: Notion, Notion Agents, Slack

## [First Steps Toward Automated AI Research — Richard Socher, CEO Recursive AI](../videos/pWXUkLP9uWM.md)
`pWXUkLP9uWM` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: models-research, agent-architecture, evals

Richard Socher (Recursive AI) argues for automating scientific research via a "Eureka machine" and shows small auto-research wins on NanoChat, NanoGPT speedrun and CUDA kernels, while separating these from true recursive self-improvement.

- Techniques: Benchmark-gated auto-research loop; Short fixed-budget runs as the test; Reward-hack audit before trusting results; Simulation as the verifier
- Tools: NanoChat, NanoGPT speedrun, NVIDIA CUDA kernels, U.com web search for LMs

## [Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft](../videos/fnLBmfsI_Fg.md)
`fnLBmfsI_Fg` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: voice-multimodal, agent-architecture, infra-cost-scaling

Microsoft's ACE live voice tutor uses a small model (Haiku 4.5) for speech only, moving reasoning, lesson state and planning into a code state machine to hit about 900ms response time.

- Techniques: Externalised state machine for a small speaking model; Per-turn summary handoff; Strict rules to keep small models on track; Model selection by latency budget
- Tools: Claude Opus 4.7, Claude Haiku 4.5

## [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](../videos/X1kp-ABIIxQ.md)
`X1kp-ABIIxQ` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: agent-architecture, sandboxing-execution, observability, evals

Dan Farrelly (Inngest CTO) argues agent architectures decay fast unless the execution layer (durable state, retries, triggers, tracing) is separated from fast-changing context (prompts, models, tools) and compute (sandboxes).

- Techniques: Three-layer decomposition (execution / context / compute); Externalised durable step state with resume-from-failure; Cron-triggered health check, triage agent, and reviewer loop; Deferred outcome scoring from downstream events; Ephemeral sandboxes with state kept in the orchestrator
- Tools: Inngest

## [Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs](../videos/_cVfz88_j7A.md)
`_cVfz88_j7A` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: agent-architecture, data-engineering, governance-compliance

Risa Labs (oncology) walks through automating prior-authorization workflows end to end, using confidence-gated multi-agent routing so only some orders skip human review.

- Techniques: Deterministic-first gating before LLM steps; Corroboration across independent sources before automating; Confidence-gated escalation to humans; Evidence-structured questionnaire answering; LLM-generated integration configs from a reusable action library; Self-healing loop for production automations
- Tools: RPA (robotic process automation, unnamed product), SQL database (unnamed), LLM (unnamed model) for extraction and config generation, Patient biomarker graph (internal, unnamed)

## [Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind](../videos/O72p-rBb2bA.md)
`O72p-rBb2bA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, security-guardrails, enterprise-adoption

SonderMind engineers describe the guardrail, eval and clinician-annotation loop behind Sonder, a clinically grounded mental health AI coach, and open-source 300 scenarios for it.

- Techniques: Pre- and post-LLM guardrail sandwich; Trace-to-typed-eval annotation loop; Multi-metric guardrail scoring
- Tools: Sonder (SonderMind's clinical AI coach), LLM-as-judge guardrail calls, CI-gated eval suite, annotation queue with trace replay, analytics and alerting platform

## [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../videos/5ZGyKWjQDr0.md)
`5ZGyKWjQDr0` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: memory, context-engineering, product-ux, agent-architecture

Shlok Khemani traces how ChatGPT and Claude memory evolved from 2024 to 2026, and argues memory is a product and compute problem, not a RAG problem, with context as the real cap.

- Techniques: Running profile with background re-synthesis (dreaming); Search tools over past conversations instead of stored facts; User-visible and user-editable profile with re-synthesis on edit; Dense keyword-clue memory entries; Timestamped memory entries
- Tools: ChatGPT, Claude, Gemini, Poke, Claude Code, OpenClaw, Hermes

## [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](../videos/kiqubc5b5Yo.md)
`kiqubc5b5Yo` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: multi-agent, evals, agent-architecture, enterprise-adoption

Morgan Stanley's AlphaLab, a multi-agent harness that automates quant research through research, critic-checked eval building, and Kanban-style experiments. Its main lesson: the value sits in strict eval environments and rubrics, not in the harness.

- Techniques: Scaffolded to-do list with re-prompting on early exit; Builder plus critics eval loop; Strategist, worker, and post-mortem Kanban loop; Containerised, Kaggle-style eval contract; Environments as RL reward signal; Rubric grading of each rollout's process; Meta-harness optimisation by an LLM; Provider-agnostic harness with functional tool calls
- Tools: Claude Code, Codex, Opus 4.5, Slurm, Kaggle, GRPO, NVIDIA Nemotron

## [Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet](../videos/7jjudsEhBtM.md)
`7jjudsEhBtM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: skills-self-improvement, agent-architecture, context-engineering, governance-compliance

FactSet's principal AI engineer argues skills are the new product features and engineers should ship harnesses, then covers a minimal skill harness, routing via descriptions, eval-gated skills, and skill-library governance.

- Techniques: Minimal skill registry and loop; Write descriptions as routing signals; Cut skills by user intent; Front-load critical instructions and re-run evals on model upgrades; Shortlist skills before they hit the system prompt; Governance as a skill PR pipeline
- Tools: Anthropic Agent Skills (SKILL.md format), Claude Code, Codex, bash or code sandbox for skill scripts

## [Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA](../videos/XjI-AR4pt7Y.md)
`XjI-AR4pt7Y` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: security-guardrails, infra-cost-scaling, governance-compliance

Production ML breaches are mostly boring misconfigurations, not AI attacks; the talk argues for layered infra security, a maturity model, and budgeting guardrails by latency overhead tier.

- Techniques: Tiered guardrail budget; Maturity self-assessment with overhead budgets; Least privilege with short-lived credentials; Segment by service identity, not network location; Secrets and model artifacts hygiene; Treat ML infra like a database
- Tools: Ray, NIST AI RMF

## [It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard](../videos/I3znWC3MEXM.md)
`I3znWC3MEXM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: security-guardrails, mcp-and-tools, governance-compliance, agent-architecture

Kim Maida (Keycard) shows why API keys give agents overprivileged, unattributed access, and how OAuth token exchange (RFC 8693) per tool call, with policy checked before minting, fixes it.

- Techniques: Per-tool-call token exchange (RFC 8693); Policy-before-mint; Policy-gated human approval; Ephemeral, audience-bound bearer tokens; Layered scope design
- Tools: Keycard (security token service and policy governance), OAuth 2.0 token exchange (RFC 8693), Google sign-in (identity provider in demo), MCP (client, server, gateway)

## [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](../videos/yWS0udrIOc8.md)
`yWS0udrIOc8` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: security-guardrails, pr-code-review, multi-agent

Steve Yegge argues AI-generated code multiplies security defects and new attack types (slopsquatting, prompt injection, agent credentials), and urges security scanning at generation time and as a separate pass.

- Techniques: Surface security findings at generation time; Separate security and correctness into different passes; Run several scanners and have agents cross-check; Supply-chain vetting of dependencies and base images; Adversarial supervisor agents for queue-driven agents; Least-privilege credentials per agent action
- Tools: Claude Code, Beads, Gas Town, Snyk (called Sneak in captions), Chainguard

## [Perception Agents — Antje Barth, Amazon AGI Lab](../videos/2JX6JYyQG4Y.md)
`2JX6JYyQG4Y` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: voice-multimodal, testing-verification, coding-agents

Amazon AGI Lab's Antje Barth argues computer-use agents need shared screen context and self-verification, then demos open-source annotation and design-spec checking tools for UI work.

- Techniques: Element pointing as agent input; Design-rules verification from a spec file; Meeting transcript to agent to verification pipeline; Perceive, plan, act, then re-check the screen
- Tools: Chrome extension (annotation tool), design rules markdown file (design.md), wearable transcription device, Amazon AGI Lab open-source perception agent harness (GitHub)

## [The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI](../videos/q2JrUKBMf0w.md)
`q2JrUKBMf0w` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: evals, observability, agent-architecture

Arize's founder argues that evals must add a third layer, agent-as-a-judge, that reads production traces, finds failure patterns, and can open fix PRs. It is a short vendor pitch with little method detail.

- Techniques: Agent-as-a-judge over traces; Three-layer eval stack; Trace-driven online evals; Repeated-tool-call loop detection
- Tools: Arize Signal, Agent as a Judge (Arize)

## [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../videos/aeTb5BdmTTc.md)
`aeTb5BdmTTc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: context-engineering, enterprise-adoption, coding-agents, skills-self-improvement

How a 10-person team got to shipping with coding agents: treat agent setup as a leadership job, share the best practices, invest in one high-value skill, and close the loop on slop.

- Techniques: Thin CLAUDE.md/AGENTS.md index; Skill as a folder with a short SKILL.md; Runbooks in code comments as discovery hooks; One end-to-end ship-it skill; Nightly code-gardener agent; Shared setup with an opt-out for experiments; First-prompt context audit
- Tools: Claude Code, CLAUDE.md, AGENTS.md, CI/CD, issue boards

## [The UX of AI: Making AI-Powered Apps Your Users Don't Hate - Kathryn Grayson Nanz, Progress Software](../videos/L3RuP_q8Bwc.md)
`L3RuP_q8Bwc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: product-ux, security-guardrails

Kathryn Grayson Nanz (Progress Software) on designing AI features users trust. Organizes UX problems into five areas (trust, clarity, control, transparency, meaningful benefit) and gives concrete UI patterns for each.

- Techniques: Source citations with graded surfaces; Plan approval before agent execution; AI content labeling; Streaming and visible reasoning; Change highlighting; Prominent kill switch; Task-scaled version history; Granular revocable permissions; Pre-approval cost and time estimates; Guided starts and next-step actions
- Tools: Claude, ChatGPT, Microsoft Copilot, Microsoft Teams

## [AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix](../videos/CgsWxRUY5Eo.md)
`CgsWxRUY5Eo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: infra-cost-scaling, coding-agents, pr-code-review, context-engineering

Netflix's playbook for using coding agents on production profiling data to find CPU hot spots, open reviewed fixes, and grow a shared pattern catalog, with a canary gate and an autonomy ladder.

- Techniques: Profile-to-PR agent pipeline; Central anti-pattern catalog in git; Cross-repo sweep for recurring patterns; Canary-gated review; Shift-left catalog injection; Scheduled fixed workflow before autonomy
- Tools: Continuous profilers (sampled call stacks with CPU time), Git and code search across repos, Canary deployment infrastructure, TorchFix (public PyTorch anti-pattern catalog), Spectator (metrics library, named as the source of the counter-object pattern)

## [How Forward Deployed Engineering is done at Decagon — Sunny Rekhi](../videos/7wu2hsRfvV0.md)
`7wu2hsRfvV0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: enterprise-adoption, product-ux

Decagon's CTO of Forward Deployed Engineering explains how FDEs configure enterprise AI support agents, funnel customer asks into the product, and productize repeated custom work as the company grew from 50 to 500 people.

- Techniques: Define success in writing at scoping; Productize on repetition (the 25th-integration rule); Field-to-product feedback loop; Same-vertical deal staffing; ROI-ranked first automation; Natural-language configuration as a platform rule; Two-lane split for scaling agent work
- Tools: Decagon, Codex, Claude Code

## [How Forward Deployed Engineering is done at Factory — Eno Reyes](../videos/wpOA-UXynoM.md)
`wpOA-UXynoM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: software-factory, enterprise-adoption, testing-verification, product-ux

Eno Reyes (Factory CTO) on forward-deployed engineering as the way to build software factories. The bottleneck is agent readiness, meaning deterministic validators in the codebase, not model capability.

- Techniques: Audit validation loops before deploying agents; Bounded long-running harness with an explicit definition of done; Map the signal-to-deploy stages per org; Land-and-expand with a reference implementation; Split automation into one-click fixes and workflow changes; Model-independent harness with owned traces and self-hosted deployment
- Tools: Factory Droid, Missions, LegalDroid, linters, type checkers, security scanners, end-to-end test suites

## [Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI](../videos/H7puB0RwJMM.md)
`H7puB0RwJMM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: memory, data-engineering, governance-compliance

Daniel Chalef (Zep) on why LLM-built knowledge graphs need provenance modeled as a graph, covering lineage through merges, contradictions, tagging, and deletion.

- Techniques: Provenance as graph edges; Merge-safe lineage; Ingestion-time tagging with inheritance; Lineage-based deletion; Single-shot extraction plus deterministic dedupe
- Tools: Graphiti, Zep, Vector similarity search, Full-text search, BFS graph traversal

## [From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI](../videos/Ib5t2RLtxvM.md)
`Ib5t2RLtxvM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, testing-verification, sandboxing-execution, observability

Rustem Feyzkhanov (Snorkel AI) on turning production agent traces into repeatable, containerized simulation benchmarks that serve as release gates and training data.

- Techniques: Trace-to-task conversion; Harbor-style task folder; Oracle-first validation; Sidecar service mocking with a simulated user; Stepwise long-horizon simulation; Layered verifiers with SME escalation; Benchmark CI and difficulty tagging; Coverage split: happy path plus edge cases; Held-out split for agent config
- Tools: Docker, Docker Compose, Harbor (task format), Terminal-bench, SWE-bench, Arize (experiment and trace recording; transcript says 'Arise'), MCP tools

## [Local Agentic Theory For Mobile Games — Shafik Quoraishee & Joanne Song, The New York Times](../videos/418t26CVz-w.md)
`418t26CVz-w` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: local-ai, agent-architecture, product-ux, inference-serving

NYT engineers on running small agents on-device inside mobile games, under per-frame time, memory and battery budgets, with live accessibility tuning through graded dials instead of fixed menus.

- Techniques: Per-frame perceive-predict-decide-act agent loop; Constraint graph over space, time and energy; Constraint satisfaction with backtracking; Graded accessibility dials driven by live signals; Live focus-path monitoring and layout auditing
- Tools: Efficient Zero V2 (sample-efficient RL, mentioned as state of the art up to 2024), WCAG 2.2 and WCAG 3.0 draft, Gaze estimation CNN, Google SIMA (transcript reads 'SEMA'; generalist agent framework mentioned briefly)

## [Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai](../videos/YnNF55QV0zs.md)
`YnNF55QV0zs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: evals, context-engineering, models-research, product-ux

Ishan Anand (InsightSciences) on synthetic personas as bounded forecasts: where LLM personas fail (confounders, order bias, attitudes vs behavior), and how to measure them against human distributions and noise floors.

- Techniques: Validate personas against held-out human ground truth; Ground the persona in the full world of the study; Durability tests for option order and wording; Attitude-to-behavior triangulation; Free-text answers mapped to scale via semantic similarity; Fine-tune on survey distributions conditioned on demographics; Noise floor via split-half simulation

## [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../videos/7vn4WpqNpck.md)
`7vn4WpqNpck` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: coding-agents, evals, enterprise-adoption

Denys Linkov (Wisedocs) on whether a six-month monorepo refactor of a medical-claims ML pipeline was worth it when coding agents keep improving, and how to measure agent reliability.

- Techniques: Time-horizon reliability check before long runs; Agentic tool-evaluation pipeline; Monorepo consolidation for agent-driven work; Human PRs as a context-building step; Check hidden assumptions in dependencies; Layered refactor instead of a full rewrite
- Tools: Cursor, Temporal, Claude Sonnet 4.6, Claude Opus 4.8, o3, GPT-5.5, Confluence, Claude Code plan mode

## [Build the AI GTM Agent That Knows the Buyer - Dr. Sajjan Kanukolanu, Position2 (Position Squared)](../videos/ltv-L5oMPIs.md)
`ltv-L5oMPIs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: enterprise-adoption, multi-agent, data-engineering

Position Squared's three-layer, multi-agent GTM system (anonymous visitor ID, knowledge-base-gated ICP and CRM matching, rep actions). Lessons: ICP drift, alert fatigue, weak identity accuracy, and approval friction.

- Techniques: Dedupe-then-enrich identification; Knowledge-base-gated ICP filter agent; Per-person context graph with account and deal rollup; Separate fit score from intent score; Personalized returning-visitor chat; Quarterly ICP refresh from closed outcomes; Alert budget tuned to rep capacity; Auditable, adjustable policy engine; One-click draft approval with a 30-second budget
- Tools: HubSpot, Slack, LinkedIn

## [Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](../videos/z0sh8HyTrDo.md)
`z0sh8HyTrDo` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · topics: software-factory, multi-agent, coding-agents, governance-compliance

Auditoria AI speaker says human attention bottlenecks agent work: use parallel worktree subagents, skills, one-pane UX, goals and loops, and self-improving harnesses, keeping humans at intake and sign-off.

- Techniques: Worktree-per-task parallel subagents; Ticket-to-stage pipeline with two human gates; Encode organizational procedure as skills; Single-pane minimal UX for orchestration; Daily self-retrospective on the agent's own loop; Goals plus loops, monitored from a phone; Background dreaming for pattern compaction
- Tools: Claude Code, git worktrees, Kubernetes, Docker, Jira, GitHub, MCP

## [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../videos/XEd_SRVHBgU.md)
`XEd_SRVHBgU` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: training-finetuning-rl, models-research, evals

Sara Hooker (Adaption) argues frontier AI should be open to more builders, and pitches Autoscientist, an automated training loop that co-optimizes data and model while saying pre-training scale is no longer the main lever.

- Techniques: Co-optimize data curation with the model in the same search; Win-rate threshold as the stop condition for a training search; Wide architecture and size search instead of team familiarity; Adaptive test-time compute per task (planned)
- Tools: Autoscientist (Adaption, beta)

## [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../videos/il1c1a2FufU.md)
`il1c1a2FufU` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · topics: coding-agents, context-engineering, skills-self-improvement, multi-agent

Jason Liu (OpenAI) shows how he runs Codex as a personal ops system: pinned long-lived threads, a git-tracked memory vault, heartbeats, and goal verifiers. Main takeaway: compaction makes long threads workable.

- Techniques: Long-lived pinned thread per workstream; Heartbeat / loop in the same thread; /goal with a verifier and file-backed goal; App shot plus accessibility tree; Git-tracked personal memory vault with agents.md routing; Monitor thread that spawns per-issue threads; Skill from one completed run, with self-edit permission; Annotate a localhost preview to steer the agent; Model and reasoning tiering
- Tools: Codex app, Codex CLI, Codex in-app browser, computer use, Chrome extension, Slack connector, Gmail connector, Google Drive connector, Notion, Linear, Obsidian, GitHub

## [Evaling Video Slop — Maor Bril, Character.ai](../videos/b_PmGocP4rc.md)
`b_PmGocP4rc` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, testing-verification, voice-multimodal, agent-architecture

Maor Bril (Character.ai) on evaluating AI video: frame-level metrics miss story, physics and pacing, so he distilled a judge committee into a small fast VLM trained on pairwise comparisons and run inside the generation loop.

- Techniques: Pairwise A-vs-B judge training; Manufactured negatives; Matched-encoding real-vs-AI pairing with identical annotation; Expert-committee distillation into a small VLM; Eval inside the generation loop; Calibration sessions with randomized annotation; Agent with validation tools
- Tools: Qwen (small VLM, post-trained), Dolby Atmos (audio quality), CLIP-style frame metrics, frame-drift metrics, Kling, Seedance, Veo, Sora, OpenTelemetry (requested, planned for harness)

## [Claude for Long-Horizon Tasks — Lance Martin, Anthropic](../videos/9QebvrrY3KY.md)
`9QebvrrY3KY` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · topics: agent-architecture, memory, multi-agent, context-engineering

Lance Martin (Anthropic) on designing long-horizon async agents: decouple brain from hands, verify in a separate context, dream offline to fix memory, and run org-level shared harnesses.

- Techniques: Brain/hands split with an append-only session log; Non-destructive context via append-only session object; Build/verifier loop in separate contexts; Dreaming: offline memory consolidation; General memory substrate with the model managing its own structure; Org-level shared harness with its own identity
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, Claude Tag, Message API, Continued Learning Bench, METR time-horizon benchmark, Slack

## [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../videos/jQDXzEVHMSE.md)
`jQDXzEVHMSE` · AI Engineer · 2026-08-18 · q3 · practitioner · interview · topics: infra-cost-scaling, rag-retrieval, testing-verification

Gergely Orosz interviews Simon Eskildsen, founder of Turbopuffer, on his path from Shopify infrastructure to building an S3-backed search engine, napkin-math habits, CPU scarcity and startup financing. Mostly origin story, little AI content.

- Techniques: Napkin-math latency and cost estimate before benchmarking; Proxy-based fault injection in CI; Object storage as the system of record with an HTTP cache in front; Design for tail latency and round trips; Batch durable writes; Ship simplest version then probe demand
- Tools: Toxiproxy, NGINX, Amazon S3, MySQL, Rails, Postgres, pgAnalyze, Docker, Rust, GDB, Redis, NVMe SSD

## [Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE](../videos/KwhgfwOSToQ.md)
`KwhgfwOSToQ` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: product-ux, enterprise-adoption

Kevin Bai (Anthropic, ex-Palantir and Rippling) explains the forward deployed engineer role: when to use it, why it needs a shared platform, and how to scope bespoke versus generalizable work.

- Techniques: FDE fit test before adoption; Bespoke vs generalizable split; Two engineers per customer project; Granularity of primitives matched to user base
- Tools: Palantir Foundry

## [SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)](../videos/KMR_RBoCa4M.md)
`KMR_RBoCa4M` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: evals, enterprise-adoption, data-engineering

Nubank and Snowglobe claim simulated personas with mocked tools produce agent eval data on demand, cutting release cycles from weeks to hours, provided the sim-to-real gap is measured.

- Techniques: Simulated-user eval set generation; Persona-consistent grounding state; Sim pre-screening before A/B tests; Sim-to-real calibration; Same-harness model sweep
- Tools: Snowglobe SDK, LLM-as-judge, Automated prompt optimization (captioned 'JEPA', likely GEPA)

## [Every Harness Will Become A Claw — Sam Bhagwat, Mastra](../videos/8qWIPUia2O8.md)
`8qWIPUia2O8` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: agent-architecture, sandboxing-execution, skills-self-improvement, product-ux

Sam Bhagwat (Mastra) argues agent harnesses will keep expanding into always-on "claws" with durability, initiative and learning, then shake out to a few winners. Mostly conceptual, with little hard data.

- Techniques: Durable turn streaming with resume; Queue, steer and interrupt on running threads; Session-scoped tool approval; Heartbeat wake-ups; Trace-driven continual learning; Cloud sandbox per parallel subagent
- Tools: Mastra, Claude Code, Codex, OpenClaw, Hermes Agent, Slack, Telegram, WhatsApp, GitHub

## [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../videos/CTLa_p6iOiY.md)
`CTLa_p6iOiY` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, voice-multimodal, testing-verification

Pierluca D'Oro (Programma Labs) shows that static computer-use benchmarks can be gamed by replaying recorded successful traces, and argues for varied environments plus hierarchical confidence intervals.

- Techniques: Replay-agent baseline check; PRISM environment design checklist; Template plus verifier config compiler; Hierarchical confidence intervals; Interval-gated model decisions

## [Skills are the New SDKs - Elvin Aghammadzada, DataRobot](../videos/LC3-P7v3yoI.md)
`LC3-P7v3yoI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: skills-self-improvement, context-engineering, mcp-and-tools

Elvin Aghammadzada (DataRobot) argues agent skills are a progressive-disclosure context tool that complements MCP, and that skills are software needing versioning, evals and security review.

- Techniques: Progressive disclosure via a skill index; Context budget ceiling; Skill as a wrapper around an MCP server; Split by role: skill for reasoning, MCP for execution; Treat skills as versioned, tested software
- Tools: Claude Code, Codex, Copilot, Gemini CLI, OpenClaw, ClawHub, MCP

## [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song](../videos/AVMr9PMINyo.md)
`AVMr9PMINyo` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · topics: inference-serving, models-research, training-finetuning-rl, evals

A MiniMax and Together AI panel on how an open-weight model like MiniMax M3 gets trained, then served at scale, with day-zero kernel work, agentic KV-cache demands and long-horizon RL evals.

- Techniques: Day-zero kernel plus post-launch optimization queue; Benchmark unsolved kernel problems as RL environments; Multi-submission long-horizon evals with held-out validation; Multimodal training from step zero; KV cache as a distributed store; Cross-model optimization transfer
- Tools: KernelBench, Parallel KernelBench, OSWorld, SVG bench, MiniMax sparse attention

## [Content Is Code - Matt Palmer, Conductor](../videos/yv6xovSsB1U.md)
`yv6xovSsB1U` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: product-ux, context-engineering, coding-agents

Matt Palmer (Conductor) argues code is becoming the medium for technical content, so docs, changelogs and product videos should be generated from a structured source of truth.

- Techniques: Generate product tour videos with React and Remotion; Derive changelogs and product updates from the diff; Keep design tokens separate from app code; Write internal docs and skills for agents
- Tools: React, TypeScript, Remotion, CSS, HTML, Claude

## [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../videos/Z-c11pV_uvU.md)
`Z-c11pV_uvU` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: agent-architecture, claude-code, context-engineering, multi-agent

Frank Coyle (UC Berkeley) walks through the Claude Certified Architect exam's scenarios and uses each one's anti-patterns to teach agent loops, subagent context isolation, compaction, and non-interactive runs.

- Techniques: Stop-reason-driven agent loop; Three-level CLAUDE.md hierarchy; Single-purpose subagents with minimal tools; Context slicing for critic and reviewer agents; Forked subtask context with summary return; Threshold-triggered compaction; Non-interactive CI runs with batch processing
- Tools: Claude Code, Claude API (messages, stop_reason, tool use), CLAUDE.md, MCP (Model Context Protocol), Message Batches API

## [Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase](../videos/u1yaOeEX4e8.md)
`u1yaOeEX4e8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: observability, infra-cost-scaling, data-engineering

JPMorgan payments lead on modeling each API request as a short-lived execution DAG, then using per-segment baselines and drift categories to detect anomalies with fewer false alarms.

- Techniques: Request-as-DAG from traces; Tiered detection; Segmented baselines; Drift classification before action; Async telemetry to hot and recon paths; Staged automated remediation; Synthetic training data for detectors
- Tools: OpenTelemetry, Kafka, Neo4j (mentioned as contrast), KL divergence, MMD, EWMA (exponential moving average)

## [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../videos/Ot4OPrPH4xY.md)
`Ot4OPrPH4xY` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · topics: rag-retrieval, data-engineering, infra-cost-scaling

Bright Data's product lead argues that web data is becoming agent context, that repeated queries to paid context services get expensive, and that owning the data can beat renting it past a volume tipping point.

- Techniques: Field-by-field enrichment agent loop; Hybrid search plus direct scrapers; Basic heuristic entity merge; Break-even analysis for build vs rent; Self-healing scrapers
- Tools: Bright Data, Scraper Studio, Exa, Parallel, Tavily, New.com, Amazon AgentCore, Microsoft WebIQ, ZoomInfo / gtm.ai, SERP API, Claude native web search, Opus 4.8

## [Jev CEO: I made ChatGPT, now I'm building what's next](../videos/cJ0EOzey--o.md)
`cJ0EOzey--o` · AI Engineer · 2026-08-18 · q2 · intro · talk · topics: training-finetuning-rl, models-research, product-ux

Former OpenAI post-training lead Diego Almeida argues RLHF models are built for assistance, not automation, and pitches a new post-training objective (calibrated decision making) at his stealth startup TypeSafe.

- Techniques: Assistance vs automation diagnostic; Cost-shifting to the user as a deployment pattern; Name the optimization target before choosing a post-training method
- Tools: Claude Code

## [Verifiable Environments for AI in Biology — Kenny Workman, LatchBio](../videos/3ZMUiFaQ3qg.md)
`3ZMUiFaQ3qg` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, data-engineering, models-research

LatchBio's CTO on building verifiable benchmarks for biology agents: DAG-decomposed spatial-omics evals, human verification of ambiguous tasks, rubrics for long-horizon work, and refusal testing.

- Techniques: Per-node verifiable eval specs; Human-verification pass over agent trajectories; Rubrics on invariant choke-point nodes; Paired routine and red-team refusal evals
- Tools: Python grader functions, SWE-bench-style task format, Claude models (named by the speaker as the models used for the evals)

## [Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber](../videos/31GUkCBD-Uc.md)
`31GUkCBD-Uc` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: evals, observability, agent-architecture

Uber's Uber Eats image pipeline (routing, enhancement, publish QA) and how they keep it aligned with human labels through offline evals, auto-tuning and a diagnoser that closes the production feedback loop.

- Techniques: Flat per-run JSON trace across the whole agent chain; Router as a classifier scored by a confusion matrix, with an N-by-N extension; Golden human-label set plus ship gate; Production drift loop: sample, re-label, diagnose, tune, benchmark, register; Reflect-and-synthesize prompt optimizer; Generate-edit-QA loop scored with pass@K; Pairwise judge with yes/no/unsure and product-agreed criteria; Redundant Swiss-cheese final gate; Diagnoser as a routing layer over all feedback; Replay flagged examples before releasing a config; Per-segment production metrics
- Tools: Arize

## [Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit](../videos/Owb8g3yDyzo.md)
`Owb8g3yDyzo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: training-finetuning-rl, evals, enterprise-adoption

Intuit's Udi Menkes argues frontier LLMs give fluent but unverified money advice, and that grounding a model in real business outcomes (state, action, outcome) beats model size.

- Techniques: Outcome-grounded trajectory dataset; Propose-then-rank split; Propensity-matched uplift estimate; Evidence-grounded explanation; Long-horizon simulation with a rules baseline
- Tools: QuickBooks, TurboTax, Credit Karma, Mailchimp, reinforcement learning (Intuit in-house model)

## [Multiplayer agentic engineering — Arjun Singh, Superconductor](../videos/OL7kfezynJM.md)
`OL7kfezynJM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: software-factory, coding-agents, sandboxing-execution

Arjun Singh (Superconductor) on making agent work multiplayer: one shared session across Slack, desktop, mobile and GitHub, cloud sandboxes, and benchmarking agents on your own codebase.

- Techniques: Cloud sandbox per project; Same session across interfaces; Artifacts as proof of work; Meeting bot as an idea-to-ticket intake; Acceptance-criteria fields in the ticket form; Network egress allowlist with grant prompts; Scoped credentials instead of ambient access; Codebase-specific agent benchmark; Switch defaults on evidence
- Tools: Claude Code, Codex, Cursor, Slack, GitHub, Linear, Sentry, Notion, Google Meet, Zoom, Microsoft Teams, GLM 5.2

## ["The biggest challenge in your stack? Evals, Evals, Evals" - 2026 State of AI Engineering results](../videos/RGe6EjucbzI.md)
`RGe6EjucbzI` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: evals, enterprise-adoption, models-research, infra-cost-scaling

Bar Yeren (Amplify) reads out the 2026 State of AI Engineering survey (1,048 respondents): evals remain the top challenge, teams run multi-model stacks, cost is a first-class constraint, and agents now mostly have write access.

- Techniques: Intent-to-adopt ratio; Routing by task type across models; Monitoring cost and token usage alongside quality; Human-in-the-loop approvals and permission gating for write-enabled agents
- Tools: Notion, Vercel, Nano Banana, ChatGPT Images 2.0

## [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../videos/iQ5xldZ9StU.md)
`iQ5xldZ9StU` · AI Engineer · 2026-08-18 · q3 · intro · talk · topics: software-factory, security-guardrails, coding-agents, sandboxing-execution

GitHub Next demos Agentic Workflows (markdown playbooks compiled to Actions with deterministic guardrails) and ACE, a cloud multiplayer dev environment where humans and agents share chat and plans.

- Techniques: Markdown playbook compiled to CI workflow; Declarative guardrail front matter; Secret brokering outside the agent sandbox; Staged, logged writes; Swarm of role-specific workflows; Shared cloud session per branch with team chat as context; Shared markdown plan as contract; Automation triage by stack trace origin
- Tools: GitHub Copilot, GitHub Actions, Dependabot, Astro, Cloudflare, ACE (GitHub Next prototype)

## [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](../videos/LqLoYksJ6do.md)
`LqLoYksJ6do` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · topics: security-guardrails, sandboxing-execution, software-factory

Form3's Moritz Johner describes PatchPilot, an agent that patches CVEs across thousands of repos, and why production credentials make a coding agent a supply-chain actor needing deterministic controls, credential splits, and microVM isolation.

- Techniques: Deterministic controller plus scoped agent steps; Minimal change-set instruction plus post-agent vetting; Bounded CI-fix loop with human escalation; End-of-run retrospective aggregated across runs; Planted-injection end-to-end tests as evals; MicroVM sandbox with a policed egress path
- Tools: PatchPilot, Dependabot, Renovate, Firecracker, Docker, Kaniko, BuildKit, Landlock, bubblewrap, Go, Slack, GitHub

## [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing - Bala Ramdoss, Amazon Lens](../videos/maTp79FD9gI.md)
`maTp79FD9gI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · topics: product-ux, mcp-and-tools, agent-architecture

Bala Ramdoss (Amazon Lens) on why LLM agent output needs a typed rendering layer between model and screen: a versioned UI contract, streamed typed chunks, and a BFF that hydrates actions, so mobile clients stay dumb and safe.

- Techniques: Versioned rendering contract; Typed streaming UI blocks; BFF as renderer and hydrator; Design loading around streaming
- Tools: A2UI, CopilotKit, MCP apps

## [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../videos/ZpK5PWX2YRM.md)
`ZpK5PWX2YRM` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: pr-code-review, testing-verification, coding-agents, software-factory

Alex Volkov on the "Z/L continuum" for how much agent-written code engineers should read in 2026: route review effort by the proof a change needs, not by a blanket rule.

- Techniques: Risk-tiered review routing; Decompose into atomic PRs with agents; Separate writer, inspector and test author; Turn review findings into system rules; Ask the agent where the critical code is; Loops with verification and retry
- Tools: Claude Code, Codex, OpenClaw, Pi, Antigravity, Grok Code

## [A Song of Types and Agents - Roberto Stagi, Ratel](../videos/UlFB6efYN5Q.md)
`UlFB6efYN5Q` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: agent-architecture, dev-tools, coding-agents

Roberto Stagi argues TypeScript is overtaking Python for the agent and application layer, because coding agents default to it, npm is deep, and one Zod schema can type the whole stack; Python keeps training and serving.

- Techniques: Shared Zod schema across the full stack; Single-language monorepo for agent apps; Split by layer: Python for training and serving, TypeScript for the app and agent layer
- Tools: TypeScript, Python, Zod, npm, Vercel AI SDK, FastAPI, React, Claude Code, Cursor, Codex, Lovable

## [Claws Out: Securing and Building with OpenClaw - Nick Taylor, Pomerium](../videos/xg1zNlzw7Jk.md)
`xg1zNlzw7Jk` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: security-guardrails, mcp-and-tools, coding-agents

Nick Taylor (Pomerium) on hardening the OpenClaw control plane with trusted-proxy auth, then a live demo of building a UI-bearing MCP app for ChatGPT by editing its workspace from Discord on his phone.

- Techniques: Identity-aware proxy as the auth layer for an agent control plane; Live-edit an MCP app from chat; Widget-to-LLM calls via the MCP apps send-message function; Narrow write access for agent-driven PRs; Test the unauthenticated or fresh-install path
- Tools: OpenClaw, Pomerium, ChatGPT apps (MCP apps), MCP, React, Vite, Discord, Telegram, WhatsApp, Caddy, NGINX, GitHub CLI

## [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen](../videos/IJXjTLPzvAU.md)
`IJXjTLPzvAU` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: evals, context-engineering, product-ux

Jacob Thomas argues persona/role-play agents are judged by fluency metrics that cannot catch anachronistic "composite" historical figures, and proposes a pre-registered, expert-scored, context-window-based eval (Lincoln case study).

- Techniques: Pre-registered fidelity eval for personas; Anachronism-first rubric with voice excluded; Encounter-as-configuration with receipts; Context window grounding over persona fine-tuning; Expert-authored gold set as a CI gate
- Tools: Claude Opus 4.7, Companion (open-source persona prompt framework built by the speaker), Character AI, Hello History, KOSIR, PsyMem, In-Character benchmark

## [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](../videos/BqZrTdgBaPw.md)
`BqZrTdgBaPw` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · topics: mcp-and-tools, agent-architecture, product-ux

Stephan Steinfurt (TNG) shows a nightly, fully automated chess-explainer pipeline: a Gemini 3.1 Pro agent with chess tools narrates analysed human games as YouTube videos.

- Techniques: Engine plus LLM split with tools; Let the reasoning model choose tools rather than pre-computing; Deliberately conflicting tool outputs; Nightly batch with a structured intermediate format; Monitor odd outputs and treat them as signals
- Tools: Gemini 3.1 Pro, Grok 4, ElevenLabs v3, Maia (captioned as Maya), chess engine (unnamed), web search

## [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../videos/c35YoMdnI78.md)
`c35YoMdnI78` · AI Engineer · 2026-07-18 · q3 · practitioner · panel · topics: software-factory, testing-verification, context-engineering, agent-architecture

Panel debate on whether agent "loops" (Ralph-style, bash-while-true) are hype or working practice; the consensus is loops work for verifiable tasks, need deterministic feedback and human-owned architecture, and are not yet a full software factory.

- Techniques: Fresh-context loop with file-system state; Back-pressure hooks that talk back; Deterministic controller around the LLM step; Context budget with headroom; Bare-model baseline on each new release; Explicit cost decision for high-value verification; Start small and iterate on real users; Vendor code and minimise open-source dependencies; Prefer statically typed languages for agent-maintained code
- Tools: Claude Code, Ralph loop (bash while-true), pre-commit hooks, PostHog, Notion, Sentry, Git, npm, Rust, Haskell, Python, TypeScript

## [OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack](../videos/akk6KRlcwW4.md)
`akk6KRlcwW4` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: local-ai, inference-serving, product-ux

Callstack engineer Lech Kalinowski builds a handheld text-terminal for OpenClaw and local LLMs on an ESP32, with a thin-client design backed by a 120B model on a DGX Spark. Mostly a hardware showcase with useful field notes.

- Techniques: Thin-client MCU with a heavy backend; Pre-allocated one-bit page buffers; Dual-display split by job; OpenAI-style proxy in front of open models; Graceful degradation across hardware parts
- Tools: OpenClaw, ESP32, NVIDIA DGX Spark, NVIDIA serving stack (auto-caption: 'Tensor Earth'), OLED display, e-paper display

## [Agents Need Feature Flags - Sachin Gupta](../videos/zU4EagB311U.md)
`zU4EagB311U` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: governance-compliance, security-guardrails, agent-architecture

Sachin Gupta argues agents need feature-flag discipline: six flag types (prompt, tool, model, memory, autonomy, kill switch), a middleware layer, and a kill switch shipped first, with four metrics to track.

- Techniques: Six-surface flag taxonomy; Flag middleware between user and agent loop; Kill switch with three properties; Canary prompt variant; Five-step rollout order; Resolve flags per turn and log segment context; Bypass caching for flag-sensitive responses; Flag hygiene rules
- Tools: LaunchDarkly, Unleash, Lift (as spoken), homegrown flag service

## [On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft](../videos/RGSFUqzqErE.md)
`RGSFUqzqErE` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: rag-retrieval, evals, context-engineering, skills-self-improvement

Microsoft's Pablo Castro splits agent knowledge into intrinsic, extrinsic and learned, and demos Foundry knowledge bases and an Agent Optimizer that tunes agent config from traces.

- Techniques: Three-way knowledge split for agent design; Hybrid retrieval over combined methods; Layered retrieval API; Agentic retrieval with a satisfaction check; Knowledge base as MCP server; Eval generated from traces, then hill-climb the agent config
- Tools: Microsoft Foundry, Foundry IQ, Azure AI Search, Work IQ, Fabric IQ, WebIQ, Agent Optimizer, Foundry Toolkit for VS Code, GitHub Copilot, MCP

## [Agents Building Agents - Alfonso Graziano, Nearform](../videos/aHhB3sjGjkI.md)
`aHhB3sjGjkI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: evals, skills-self-improvement, observability, coding-agents

Alfonso Graziano (Nearform) shows coding agents improving other agents: an eval-driven loop lifts a toy agent from 18% to 83% and a production agent from 67% to 86%, and a trace-clustering loop turns live user feedback into fixes.

- Techniques: Golden dataset plus scorers as the agent test suite; Baseline report before the optimization loop; Branch-per-hypothesis improvement loop with rollback; Protected eval set in the optimizer instructions; Reading the agent's full traces, including thinking traces, for root cause; Trace clustering from live feedback; Packaging the analysis as a reusable skill; Failure mode to spec to golden-set entry
- Tools: Claude Code, Mastra, auto-agent (the speaker's own internal tool, not public)

## [remobi.app: Don't change your terminal workflow for mobile](../videos/5192csoTkVo.md)
`5192csoTkVo` · AI Engineer · 2026-07-18 · q2 · intro · demo · topics: coding-agents, dev-tools, product-ux

Connor Adams demos Remobi, an open-source progressive web app that gives phone access to tmux sessions running Claude Code and other coding agents, reached over a private network such as Tailscale.

- Techniques: tmux as the agent session host; Private-network remote access to a dev box; Gesture-mapped terminal UI; Diff review in a side window; Skill-driven environment setup
- Tools: Remobi, tmux, Tailscale, Cloudflare Tunnels, ngrok, Claude Code, Happy, lazygit, critique, agent-browser, npm, Conductor

## [Building Great Agent Skills: The Missing Manual](../videos/UNzCG3lw6O0.md)
`UNzCG3lw6O0` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: skills-self-improvement, context-engineering, claude-code

Matt Pocock's prerecorded talk gives a four-part checklist (trigger, structure, steering, pruning) for judging and writing agent skills, to escape "skill hell".

- Techniques: Choose user-invoked vs model-invoked per skill; Steps plus reference split with external context pointers; Leading words; Split phases into separate skills to force legwork; Deletion test and sediment audit
- Tools: SKILL.md agent skills, superpowers (comparison skill set), Matt Pocock skills repo (writing-great-skills skill)

## [State of the Union: Why Local, Why Now — NVIDIA, Osmantic, Roboflow, EXO Labs, @matthew_berman](../videos/KB41dTlX1Uc.md)
`KB41dTlX1Uc` · AI Engineer · 2026-07-18 · q3 · intro · panel · topics: local-ai, inference-serving, training-finetuning-rl, models-research

Panel on why local AI is now practical: multi-model setups, frontier-plans/local-executes splits, distilling big-model consensus into small specialized models, and the remaining UX and openness gaps.

- Techniques: Plan with frontier, execute with local; Consensus distillation; Drop open-vocabulary machinery when classes are fixed; Trace-driven model routing; Retune existing configs for small hardware; Hardware-aware model selection; Frontier bootstrap then open model
- Tools: vLLM, SGLang, Local.ai, ODS (open-source deployment system), DGX Spark, DGX Station, Brev, Segment Anything 3 (SAM3), Cursor, Codex, Llama, Qwen 3.5 / 3.6

## [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](../videos/MpZzWMdmQCE.md)
`MpZzWMdmQCE` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: testing-verification, claude-code, coding-agents, agent-architecture

Talha Sheikh (Checkout.com) argues coding agents need deterministic, shareable verification hooks, not better instructions, and that the real engineering work is designing the verification harness.

- Techniques: Stop-hook deterministic verifier; Fail-and-retry feedback loop; Layered enforcement at multiple points; Language-agnostic check contract; Executor plus advisor loop; Cheap model plus strong harness
- Tools: Claude Code, Claude Code hooks (Stop hook), VectorV1 / Vector Harness, Haiku, Opus, Anthropic Glasswing / Project Mythos (named, not described)

## [500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic](../videos/UcYoMg-8-L8.md)
`UcYoMg-8-L8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: enterprise-adoption, vibe-coding-app-building, product-ux, coding-agents

Automattic's 30-day "Radical Speed Month" experiment, in which about 500 people in paired teams shipped roughly 794 projects, and how the speaker moved from designer to design engineer by prototyping in code before Figma.

- Techniques: Time-boxed paired ship sprint; Prototype-in-code before design tool; Shared file-based exploration log; Aggregating scattered sources into a status tracker; Engineer as enabler in mixed-skill pairs
- Tools: Claude Code, Figma, Storybook, GitHub, Nano Banana, Context MCP server, WordPress.com, Jetpack, WooCommerce

## [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](../videos/JRTAtZ5iBkU.md)
`JRTAtZ5iBkU` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: product-ux, vibe-coding-app-building, coding-agents

Amol Kapoor (Nori) argues agents fail at graphics because of the medium, not the model, and that HTML is a better authoring format than canvas tools or SVG for slides, docs and video.

- Techniques: HTML as the agent's authoring format for visual artifacts; Pick the format the model is strongest in, separate from the delivery format; Ground the artifact in source data, not in the layout; Avoid screenshot-and-replace loops and canvas-driving tools for agents
- Tools: HTML, CSS, SVG, Figma MCP, PowerPoint CLI, PDF export, Nori Sessions

## [Imagination Engineering: "Live in the future and then build what's missing."](../videos/Z2Erdirpudo.md)
`Z2Erdirpudo` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: product-ux, vibe-coding-app-building, context-engineering

A YC design lead shows "software on demand" built from a week of public stream-of-consciousness Slack posts, plus a one-morning personal tool, and argues idea generation is the new bottleneck.

- Techniques: Public thought log as agent input; Distil a voice file from public writing; Self-updating design language; Agent-readable glossary markdown; Checklist-driven completeness; Timeboxing with a timer
- Tools: Claude / Claude Code, Opus 4.8, Fable 5, Conductor, Slack, Paper (design tool), ChatGPT (used to make the header image)

## [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](../videos/uU5Gv2h8-9g.md)
`uU5Gv2h8-9g` · AI Engineer · 2026-07-18 · q3 · practitioner · interview · topics: claude-code, pr-code-review, security-guardrails, context-engineering

Anthropic's Thariq Shihipar and Cat Wu, with Simon Willison, on how Claude Code and Claude Tag change team workflows, code review, auto mode safety, and prompt design, with internal claims about PR share and prompt size.

- Techniques: Staged trust ramp for AI code review; Eval-gated model swap; Behavioral evals built from user complaints; Conditional prompt wording over absolute rules; Per-model system prompts; Classifier-based permissions using user intent; Credential injection through a proxy; Fewer tools with distinct functions; Multiplayer channel agent with shared memory; Dogfooding gate before launch
- Tools: Claude Code, Claude Tag, Slack, GitHub, Datadog, FFmpeg, Remotion, Gemini API, Mountain Project, Claude Fable, Claude Opus 4.8, Claude Mythos

## [Every company should have a Brain — Garry Tan, Y Combinator](../videos/eBUyTS7SzV4.md)
`eBUyTS7SzV4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: context-engineering, memory, skills-self-improvement, enterprise-adoption

Y Combinator's Garry Tan argues that AI productivity comes from how work is wired (skills as employees, routing tables, company memory with hygiene), not the model, and pitches an open-source "company brain" called GBrain.

- Techniques: Skill file as a single-job employee; Resolver table for routing context; Trigger evals on routing; Skillify at task end; Split latent and deterministic compute; Curated company brain; Select a small working set per task
- Tools: Claude Code, Codex, OpenClaw, Hermes agent, GBrain, Postgres, TypeScript, Markdown skill files

## [Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers](../videos/O3FEoMYvUf8.md)
`O3FEoMYvUf8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: evals, models-research

Alejandro Vidal (Mindmakers) argues LLM benchmarks should use psychometrics: item response theory (IRT) gives per-question difficulty, per-model ability with intervals, and tools for auditing, shrinking, and protecting benchmarks.

- Techniques: IRT calibration of benchmark items; Benchmark audit by discrimination; Greedy high-discrimination subset selection; Residual-based outlier and consistency checks; Anchor plus fingerprint adaptive test sets; Group-wise item curves for differential item functioning; Residual correlation matrix as a model fingerprint
- Tools: Epoch AI open benchmark datasets, GPQA benchmark (used as a counterexample)

## [Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc](../videos/RGiXcVxSD3s.md)
`RGiXcVxSD3s` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: product-ux, agent-architecture, observability, skills-self-improvement

Vertical AI talk by the Filed CTO arguing chat and citations are not enough; products should be built for delegating long-running work to agents, with skills, traces, pause-and-intervene and plan approval.

- Techniques: Delegation-first task selection; Implicit skill capture from usage; Per-value trace-back for trust; Pause-and-tag intervention; Plan approval gate for irreversible actions
- Tools: Wispr Flow

## [The Prompt is the Platform - Dominik Tornow, Resonate HQ](../videos/DqtmZE6Hl0g.md)
`DqtmZE6Hl0g` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: testing-verification, agent-architecture, context-engineering

Dominik Tornow (Resonate) argues the spec, not the code, becomes the product: agents should design a system via deterministic simulation before writing the production implementation.

- Techniques: Intermediate concrete spec between abstract spec and implementation; Simulation-first design loop for the agent; Deterministic simulation of target dependencies with legal fault injection; Forbidden-fruit trace events; Shrink the protocol and build on target primitives
- Tools: NATS.io, Postgres, Rust, Python, TypeScript, Go, Java, Resonate SDK

## [Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](../videos/q4Tr-DknG2M.md)
`q4Tr-DknG2M` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: training-finetuning-rl, evals, models-research, multi-agent

Cursor's Lee Robinson on how Cursor trains its Composer models: a two-loop flywheel, defenses against eval hacking, textual-feedback RL, and models increasingly helping train their successors.

- Techniques: Eval hygiene for agent benchmarks; Private held-out eval from your own repos; Ablate-and-reimplement RL task generation; Textual feedback for credit assignment; Distilled judges and reward models from the top model; Agent fleets launched from chat with escalation to humans
- Tools: Cursor, Composer, Kimi (prior open-source base model; transcribed as 'Kimmy'), Colossus, Slack, Git, Datadog, Notion, Linear, MCP, Artificial Analysis

## [Build Systems, Not Code - Angie Jones, Agentic AI Foundation](../videos/ZD9-4fW2HhM.md)
`ZD9-4fW2HhM` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: agent-architecture, context-engineering, multi-agent, security-guardrails

Angie Jones on designing agentic systems like software: systems thinking, workflow paths, decomposition, code-vs-model-vs-human splits, contracts, idempotent retries, and maintainable agents.md files.

- Techniques: Decompose a giant agent prompt by responsibility; Route work by task type: code, model, or human; Structured decision records as agent memory; Idempotent action log with state-based resume; Evidence-not-instructions handling for untrusted content; agents.md at every level with a cold-start test
- Tools: agents.md, agent skills, subagents, Karpathy LLM Wiki (agent memory layer)

## [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](../videos/Akm1sqvWG4A.md)
`Akm1sqvWG4A` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: rag-retrieval, data-engineering, observability, security-guardrails

Abed Matini (Ogilvy) shows a local, framework-free RAG FAQ bot: Docling to Markdown, structure-aware chunking, hybrid BM25 plus vector search fused with RRF, Python guardrails, and Langfuse telemetry.

- Techniques: Markdown-first ingestion with Docling; Per-document chunking strategy selection in admin; Q&A-shaped chunks for FAQ content; Hybrid retrieval with RRF fusion in Python; Deterministic functions instead of agent loops; Pre-LLM guardrail layer with rigid tests; Per-conversation telemetry with self-hosted Langfuse; Two-model local stack in Docker
- Tools: Docling, Python, FastAPI, React, PostgreSQL, Docker, Ollama, Qwen2.5, BGE-M3, Langfuse, GitHub Codespaces

## [The Log Is The Agent - Ishaan Sehgal, Omnara](../videos/UPwGaM2MKHY.md)
`UPwGaM2MKHY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: agent-architecture, context-engineering, observability

Argues an agent's identity is its append-only event log, not the model or runtime; once workers are disposable, reliability, forking, sharing and ownership follow from the log design.

- Techniques: Log-first agent loop; Persist pending permissions as events; Projections over one record; Compaction as forked log; Fork at a point in the log; Share by access grant, not transcript copy
- Tools: Claude Code, Codex, OpenCode, Claude SDK, Cloudflare Durable Objects, SQLite, JSONL

## [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../videos/ObTPqBGsEbA.md)
`ObTPqBGsEbA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: evals, observability, enterprise-adoption, governance-compliance

A five-pillar playbook (evaluation, tracing, data foundation, orchestration, governance) for taking enterprise AI agents to production, illustrated with a retail banking chatbot case study.

- Techniques: Business-metric eval spec before build; Living golden eval set seeded from human answers; Three-layer eval stack; Automated eval pipeline with human review threshold; Trace-driven duplicate-call detection and retry cap; Tiered CI eval runs; Prompt versioning as change management; Model selection on your own eval set; Incident playbook: detect, diagnose, contain, fix, regress
- Tools: Databricks, MLflow, Delta Lake, Apache Spark, Unity Catalog, Genie, Agent Bricks, Databricks Apps, Mosaic AI, Git, Python, LLM-as-judge

## [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](../videos/pMggiOb18tc.md)
`pMggiOb18tc` · AI Engineer · 2026-07-18 · q3 · intro · keynote · topics: coding-agents, multi-agent, software-factory, agent-architecture

OpenAI's Codex team argues engineers move from watching agents to running manager-worker loops, with human attention as the scarce resource to spend on the outer loop.

- Techniques: Long-lived manager agent over worker agents; Trigger-driven manager wake-ups; Offload test runs to a separate machine; Server-side compaction for long tasks; Parallel attempts with a fast, strong model; Shared instruction file across agents; Chat-first UI with escalation to direct editing
- Tools: Codex, Codex app, Codex Cloud, Responses API, AGENTS.md, OpenClaw, OpenCode, Cerebras, VS Code extension, Xcode, JetBrains, Slack

## [Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua](../videos/ZSQb5fzRFPw.md)
`ZSQb5fzRFPw` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: voice-multimodal, sandboxing-execution, evals, infra-cost-scaling

Cua's team presents "Computer-Use 2.0": a background computer-use driver (Cua Driver), a multi-platform benchmark (CuaBench, including a KiCad electrical-engineering set), and warm sandbox pools (CuaFleet) that cut idle GPU time in RL training.

- Techniques: Two-tier background action with fallback; Window-scoped observation; Single-file cross-platform task definition; Adversarial pre-validation of evals; Trajectory forking for world-model probes; Demand-autoscaled warm pool for sandboxes
- Tools: Cua Driver, CuaBench, CuaFleet, Codex computer-use model, TerminalBench, Harbor, Android activity framework, Hermes harness, KiCad

## [ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay](../videos/TJPInBjhE4Q.md)
`TJPInBjhE4Q` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: pr-code-review, coding-agents, evals, governance-compliance

Sachin Gupta (eBay) argues coding agents create unmeasured review debt and offers a deterministic 0-100 PR review-burden score built from five signal families, plus a rollout plan.

- Techniques: Deterministic review-burden score; Backfill calibration; Non-blocking rollout ladder; Shape rules for agent PRs; Authorship detection as a weak amplifier
- Tools: GitHub, GitHub Copilot, Codex, Cursor

## [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../videos/4kYl2_mqmnQ.md)
`4kYl2_mqmnQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: multi-agent, claude-code, context-engineering, coding-agents

A KRAFTON engineer runs AI coding agents across three machines, organizes them as a hierarchy, keeps state in files, and lists the five failures and four open problems that followed.

- Techniques: Agent org hierarchy with scoped context; File-backed agent state with handoff folders; Clear-and-reload instead of compaction; Blocking review gateway with approval hook; Force delegation through a CLI harness; Git-based context sync with per-machine partitions; Single always-on control plane and chat router; Boot command that restores the fleet from state files
- Tools: Claude Code, tmux, tmux capture-pane, SSH, Git, Discord, MCP servers, Kubernetes, Linux, macOS

## [Modern Post-Training: A Deep Dive  — Will Brown, Prime Intellect](../videos/V-EDrhIhHzQ.md)
`V-EDrhIhHzQ` · AI Engineer · 2026-07-18 · q4 · deep · workshop · topics: training-finetuning-rl, evals, agent-architecture, infra-cost-scaling

Will Brown (Prime Intellect) walks through modern post-training: environments as evals, the verifiers v1 task/harness/runtime split, async RL with an interception server, and the PrimeRL trainer.

- Techniques: Task / harness / runtime decomposition; Fake base URL interception for RL on real harnesses; Async rollout batching with off-policy tolerance; Message-level trace with token mapping; Algorithm and loss separation with a registry; Group-relative shaping for length and efficiency; Same-task eval CLI with swappable harness and runtime
- Tools: verifiers, PrimeRL, Renderers, TorchTitan, Megatron, Harbor, NemoGym, OpenEnv, Hugging Face datasets, uv, Docker, Claude Code

## [6 Things to Know about AIE World's Fair 2026](../videos/0S8xe9ftGTM.md)
`0S8xe9ftGTM` · AI Engineer · 2026-07-18 · q1 · intro · other · topics: product-ux, enterprise-adoption

Swix's promo-style update on AIE World's Fair 2026 (July, Moscone West): bigger show, new tracks, leadership and vertical focus, and expo/networking tips. No technical content.

## [The AI bugpocalypse is here. Now what? - Jack Cable, Corridor](../videos/7JgIS42mz7U.md)
`7JgIS42mz7U` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: security-guardrails, pr-code-review, governance-compliance, models-research

Jack Cable (Corridor, ex-CISA) argues frontier models now find and exploit vulnerabilities at scale, but the bug classes are old and preventable, so rewrite toward memory safety and add guardrails before the PR for AI-written code.

- Techniques: Rewrite critical components in a memory-safe language; Pre-PR guardrails and visibility for agent-written code; Give the reviewer business and threat context; Use defenders' frontier models to harden systems
- Tools: Claude Code, Cursor, Rust, Slack, BaxBench

## [Field Guide to Fable — Thariq Shihipar, Anthropic](../videos/9fubhllmsBU.md)
`9fubhllmsBU` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: claude-code, coding-agents, context-engineering, models-research

Anthropic's Thariq Shihipar gives a practical field guide to working with the Fable model: unhobble Claude with tools, find your unknowns, stay in the loop, and be less reasonable about trade-offs.

- Techniques: Blind-spot pass; Brainstorm via throwaway prototypes; Interview me before building; Reference as the map; Implementation-note log for unknowns; Quiz the agent on its own work; Shrink the system prompt for newer models; Give the agent a tool rather than more context
- Tools: Claude Code, Bash tool, code execution tool, AskUserQuestion tool

## [Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind](../videos/0vphxNt4wyk.md)
`0vphxNt4wyk` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: skills-self-improvement, evals, context-engineering

Philipp Schmid (Google DeepMind) argues skills need evals like code does, and gives a lean eval-harness recipe: trigger tests, regex asserts, repeated trials, and with/without-skill ablations to decide when to retire a skill.

- Techniques: Trigger and negative-case eval set; JSON cases plus regex asserts; LLM-as-judge for trace-level checks; CI gate on skill diffs; With/without-skill ablation; Isolated, repeated trials; Lean skill plus reference files; Goal-and-constraint skills, scripts for fixed workflows
- Tools: Gemini CLI, Gemini API, Gemini Interactions API, SkillsBench, Claude Code, Codex, Cursor, Antigravity, Python, regex, LLM-as-judge

## [Beyond the Harness: A Journey Towards Adaptative Engineering - Rajiv Chandegra, Annicha Labs](../videos/qdZzND79mcg.md)
`qdZzND79mcg` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: agent-architecture, multi-agent

A London-based practitioner argues that fixed agent harnesses fail in messy real-world settings and proposes "adaptive engineering," where engineers set constraints and let multi-agent harnesses emerge and reshape at runtime.

- Techniques: Constraint-setting instead of outcome-setting; Sense-and-respond loop for complex work; Penalise redundancy to force specialisation; Dial the coupling rate; Three-question constraint review; Selection pressure check against drift
- Tools: Claude Code, Codex, Pi, Cursor, LangChain, Hermes, Cline, Goose

## [Your agent is blindfolded — Johan Lajili, Poolside AI](../videos/iRcX54EO5g8.md)
`iRcX54EO5g8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: testing-verification, coding-agents, context-engineering

Johan Lajili (Poolside) argues agent trust comes from verification: give agents a CLI to drive and test the app, make them reproduce bugs before fixing, and make the codebase easy for AI to check.

- Techniques: Reproduce-first gate; App-driving CLI for non-web apps; Token-compressed UI snapshot; Let the agent discover its own UI problems; Periodic self-review of logs and repeated actions; Human-like exploratory testing by the agent
- Tools: Poolside internal app-testing CLI (unnamed), VS Code extension, G-Stack (mentioned as an existing tool for screenshots and snapshots)

## [AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent](../videos/Iwe_RY-fYgI.md)
`Iwe_RY-fYgI` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: governance-compliance, data-engineering, enterprise-adoption

Varsha Shah proposes a framework that correlates records across payroll, tax, procurement and finance systems with graph-based entity linking, adaptive risk scoring and jurisdiction normalization to catch compliance fraud that per-document checks miss.

- Techniques: Cross-document entity graph for compliance; Multi-signal risk scoring instead of single rules; Outcome feedback loop; Normalize before scoring across jurisdictions

## [Your AI Product Will Fail Unless You Can Explain It - Veronica Hylak, Hey AI](../videos/d_Ftrl3vfV0.md)
`d_Ftrl3vfV0` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: product-ux, enterprise-adoption

Short pitch-craft talk: explain an AI product by opening with the user's pain, tying it to a picturable story, and showing a concrete before/after.

- Techniques: Wound-first opening; Viral-story anchor; Picturable-phrase rule; Before/after transformation with numbers
- Tools: Devin (cited as an example of a picturable product name), McDonald's AI drive-through clips (cited as a viral story example)

## [Understanding is the new bottleneck — Geoffrey Litt, Notion](../videos/WkBPX-oDMnA.md)
`WkBPX-oDMnA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: coding-agents, testing-verification, product-ux, skills-self-improvement

Geoffrey Litt (Notion) argues humans must still understand agent-written code to stay creative participants, not only to verify it, and shows explainer docs, comprehension quizzes, agent-built micro-worlds and shared spaces for doing so.

- Techniques: Explainer doc per agent change (ExplainDiff-style skill); Comprehension quiz gate before sharing code; Intuition-first, literate ordering; Agent-built micro-world debugger; Step-through simulation for a migration; Shared threads and commentable docs with agents
- Tools: Claude Code, Claude, Cursor, Notion, Notion HTML blocks

## [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](../videos/ij-AU9dpJjc.md)
`ij-AU9dpJjc` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: context-engineering, security-guardrails, product-ux

Isadora Martin-Dye on layering a brand-voice AI agent into four stages: non-overridable identity rules, situational context, voice examples, and a deterministic post-generation veto, with fail-loud multi-tenant identity.

- Techniques: Four-layer ordered prompt stack via single assembly; Non-overridable identity layer; Soft context as tone guidance, never quoted; Deterministic post-generation veto with soft flags and hard rejects; Fail-loud multi-tenant identity; Shared veto gate by default; Trainable voice dial from staff edits
- Tools: Threadline (her own missing-persons tool, not a third-party product)

## [Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs](../videos/vljxQZfJ9wY.md)
`vljxQZfJ9wY` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: evals, observability, agent-architecture

Nishant Gupta (Meta Superintelligence Labs) argues agent evals must score workflow behavior from production telemetry, not model answers or benchmarks, and should run continuously as a control-plane function.

- Techniques: Scenario-driven offline evals; Production telemetry as the eval set; Targeted human review to calibrate automated evals; Continuous evaluation loop; Agent tracing like distributed tracing; Evaluation as a control plane

## [Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth](../videos/uIiA6DquRiE.md)
`uIiA6DquRiE` · AI Engineer · 2026-07-18 · q4 · practitioner · workshop · topics: evals, training-finetuning-rl, inference-serving, models-research

Daniel Han (Unsloth) workshop on benchmark reliability, harness and inference-provider accuracy drift, dynamic quantization, torch.compile over handwritten kernels, and reward hacking in RL and coding agents.

- Techniques: Repeated sampling with reliability math; Rolling-average regression canary for a hosted agent; Benchmarks with unbounded instance space and programmatic verifiers; Single controlled harness for model comparisons; Calibration-based dynamic quantization; Per-provider accuracy check before adopting an inference endpoint; Open-weight baseline on llama.cpp or llama-server; torch.compile-first performance tuning with randomized bisection over flags; Audit RL and agent runs for reward hacking
- Tools: Unsloth, Hugging Face, Math-Verify (Hugging Face), llama.cpp / llama-server, PyTorch, torch.compile, Triton, CUDA, FlashAttention (FA2, FA3, FA4 mentioned), Claude Code, OpenAI Codex, Gemini CLI

## [The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab](../videos/sum9DgexFRQ.md)
`sum9DgexFRQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: mcp-and-tools, multi-agent, security-guardrails, infra-cost-scaling

Ramesh Raskar and Maria of MIT's Project Nanda outline an open infrastructure for a web of AI agents: a signed discovery index, agent hosting, and NandaTown, a simulator for testing agent networks before they go live.

- Techniques: Signed agent facts record and agent card; Message box in front of the agent runtime; Adaptive endpoint resolution; Sleep and wake hosting; Tiered simulation with scripted agents, then LLM agents; Onboarding in three tiers
- Tools: Nanda index, NandaTown, OpenClaw, Maritime, AWS, DNS, YAML

## [The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI](../videos/hVJOnuhFmTA.md)
`hVJOnuhFmTA` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: voice-multimodal, product-ux, context-engineering

Ted Johnson (JoinIn AI) argues that prompting is a batch-style punch-card protocol that leaves users doing the work, and that AI interfaces should become turn-taking, conversation-like, and aware of who is being addressed.

- Techniques: Classify each utterance, then act only at a floor-free moment; Full-duplex turn-taking with yield and resume; Ask what burden the human still carries; Voice-driven record edits in a meeting
- Tools: NVIDIA Personaplex, OpenAI GPT Realtime 2

## [Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](../videos/Lc8zRh9muoY.md)
`Lc8zRh9muoY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: observability, testing-verification, agent-architecture

Microsoft's Chronicle PoC records each agent node's inputs and outputs as a replayable trace, so production failures can be debugged and turned into offline tests. The talk argues for replayability rather than chasing bitwise determinism.

- Techniques: Boundary-annotated run recording; Record at the node boundary, not the network; Replay with selective stubbing plus assertions; Zero-model-call deterministic tests from traces; Guardrails at the tool boundary; Keep generation variance on
- Tools: Chronicle (Microsoft proof of concept; code link shown by QR code, URL not spoken)

## ["Software engineering is not about writing code" — Benoit Schillings, Google DeepMind VP of Research](../videos/1P1hJ36rxM0.md)
`1P1hJ36rxM0` · AI Engineer · 2026-07-18 · q3 · intro · review · topics: coding-agents, evals, models-research

A Google DeepMind research VP argues code is now nearly free to write, so the bottlenecks move to specification, verification, architecture and open-ended evals, with self-play replacing scarce human code data.

- Techniques: Self-play with verifiable coding challenges; Open-ended scored eval instead of pass/fail; Shift the correctness burden to the language or type system; Decompose before generating; Generate correct code directly instead of detect-and-patch
- Tools: Gemini, Google DeepMind research stack (unnamed), AlphaZero (reference point), Python, Lean (proof assistant, referenced as inspiration), Mythos (model that found vulnerabilities, referenced in news), GitHub (as the source of public code), Pitchfork (internal ML-for-code project started at Google X in 2018)

## [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](../videos/vh2VGuQ3zhY.md)
`vh2VGuQ3zhY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: mcp-and-tools, context-engineering, rag-retrieval, evals

Giving an agent every tool schema on every request breaks accuracy, latency and cost as the catalog grows; the fix is semantic routing that injects only the top-K relevant tools per query.

- Techniques: Semantic tool routing (tool RAG); Just-in-time tool and context injection; K-sweep routing evaluation; Router miss fallbacks; Description writing for retrieval; Routing observability
- Tools: Qdrant, Chroma, Pinecone, Berkeley Function Calling Leaderboard, ToolBench, Anthropic MCP on-demand tool loading write-up, Aurelio Labs semantic-router (open source), MCP0 (cited as an open-source routing project at large scale)

## [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](../videos/Rx8f05JI_WA.md)
`Rx8f05JI_WA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: evals, testing-verification, coding-agents, security-guardrails

Rishi Desai presents SWE-Marathon, 20 project-scale coding tasks where the best agent solves only 26%, and argues that multi-channel, anti-cheat verification is the main bottleneck for long-horizon evals.

- Techniques: Multi-channel verification; Strace-based forbidden-subprocess detection; Hardening loop before publishing a benchmark; Standardize tasks into a Harbor-format environment; Trajectory work-pattern charts
- Tools: SWE-Marathon, Harbor, HumanEval, SWE-bench, Terminal-Bench, Claude Opus 4.8, Claude Code, GPT-5.5 (transcribed as 'gbd 5.5'), Codex, GLM 5.2, Gemini, strace

## [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../videos/HEFSExa0xl0.md)
`HEFSExa0xl0` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: agent-architecture, mcp-and-tools, testing-verification, evals

Witan Labs on lifting coding agents' spreadsheet accuracy from about 50% to 92% by replacing 15 tools with one persistent-state REPL, plus a formula engine and render engine as the verification loop.

- Techniques: Single persistent-state REPL instead of many tools; Verification loop with domain engines; Golden-spreadsheet black-box evaluation; Domain-knowledge reminders in the prompt; Trace review for plumbing bugs
- Tools: Node.js REPL, JavaScript, TypeScript type definitions, C#, LLM-as-judge, Witan Labs internal formula engine, Witan Labs internal render engine

## [You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs](../videos/6bmM45jkMDY.md)
`6bmM45jkMDY` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: product-ux, context-engineering

Balázs Horváth (VisualLabs) argues that deciding what to build, through requirements elicitation, story mapping and value-first design, is now the bottleneck, not writing code.

- Techniques: Story map MVP slice; Persona/what/need/why stories with acceptance criteria as agent input; Four-question value check kept in the repo; Value-first design order (VAD); Usage-frequency success metric; Paired build comparison
- Tools: Story mapping, Business model canvas, Value canvas, User story templates with acceptance criteria, Markdown files in the repo as agent context

## [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](../videos/whue9_YquGA.md)
`whue9_YquGA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: software-factory, enterprise-adoption, multi-agent, pr-code-review

Angie Jones (Block) describes moving a 3,500-person engineering org to autonomous agent delegation via a maturity model, a power-user champions program, AI-ready repos, and an orchestrator.

- Techniques: Stage-based maturity model for agent use; Champions program of hand-picked power users; Layered repo context files; Delegation from the tools people already use; Review agent plus auto-fix loop; Isolated cloud workspace per agent; Machine-readable system map for orchestration
- Tools: Claude Code, Goose, Codex, BuilderBot, GitHub, Jira, Linear, Slack, MCP, AGENTS.md, CLAUDE.md

## [We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](../videos/dRmWYHuIJxM.md)
`dRmWYHuIJxM` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: token-cost-efficiency, context-engineering, rag-retrieval, coding-agents

Rajkumar Sakthivel (Tesco) on cutting AI coding-tool token spend by sending less context: a local code index with hybrid search, slimmed results and a relevance threshold, reporting about 94% fewer input tokens on one small benchmark.

- Techniques: Code-aware chunking; Parallel hybrid retrieval; Result slimming; Call-graph expansion; Heuristic relevance gate instead of LLM self-grading; Shared local index across tools; Per-query savings accounting
- Tools: Claude Code, Cursor, GitHub Copilot, Codex, CCE (speaker's free open-source local code index; name as spoken)

## [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](../videos/2e9ANoOEn28.md)
`2e9ANoOEn28` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: agent-architecture, security-guardrails, multi-agent, evals

Aditya Bhargava (Etsy) argues the agent harness, not the model, drives results, especially for weaker models, and walks through building a coding-agent harness step by step in his language Agency.

- Techniques: Tools as plain functions with docstrings; Interrupt plus handler for approvals; Partial function application for capability scoping; ReAct test-feedback loop; Subagents as tools with grouped tool sets; Objective-driven prompt optimization; Serializable pause and resume at interrupts
- Tools: Agency (agencylang.com, TypeScript-like agent language, installed via pnpm), HarnessBench (harness benchmark, 106 tasks), Claude Code (cited as an example agent: Opus model plus harness), Built-in Agency log viewer, Built-in Agency standard library (includes Wikipedia search tool)

## [Forward Deployed Engineering at Cursor — Pauline Brunet](../videos/APqXGyCoGW4.md)
`APqXGyCoGW4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: enterprise-adoption, product-ux

Cursor's forward deployed engineering lead on where FDE fits, whom to hire, and how to scope short, ROI-driven customer projects without drifting into staff augmentation.

- Techniques: FDE placement matrix; Staff-augmentation check; Success defined before build; Directional six-week phased scope; Three-bucket ROI statement; Mission statement for the FDE team
- Tools: Cursor, Cursor SDK, Cursor cloud agents

## [AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](../videos/T0HhO4YtTfE.md)
`T0HhO4YtTfE` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: agent-architecture, evals, product-ux, context-engineering

A MongoDB developer advocate walks through a four-phase framework (product requirements, system design, evaluation and monitoring, cost/latency optimization) using a health insurance claims review system as the worked example.

- Techniques: Four-phase AI system design framework; Quantified solution-agnostic business problem; Three-axis AI role classification; Per-source retrieval strategy from update cadence and content type; Simplest-design-first, evaluate, then iterate; Guardrails as measurable rates; Production signals from human behaviour; Structured outputs as a reliability guard
- Tools: MongoDB, Voyage AI

## [From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](../videos/GdvKNwMcfd0.md)
`GdvKNwMcfd0` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: coding-agents, context-engineering, software-factory, multi-agent

Microsoft's Chris Noring on moving from writing code to running agents: start in the CLI, use AGENTS.md, skills and custom agents as guardrails, and delegate background work that comes back as draft PRs for human review.

- Techniques: Layered repo guardrails (AGENTS.md, skills, custom agents); Tools allowlist to constrain an agent; Delegate to a background cloud agent that returns a draft PR; Parallel terminals as a scaling model; Ask the agent to write its own skill or instructions
- Tools: GitHub Copilot CLI, Claude Code, Claude Desktop, VS Code, GitHub Copilot cloud agent, GitHub MCP server, Playwright MCP, AGENTS.md, SKILL.md skills, custom agents (.github/agents)

## [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](../videos/WLXxTaPagA8.md)
`WLXxTaPagA8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: testing-verification, evals, observability, multi-agent

Solo agent builders keep rebuilding CI/CD-style controls (regression tests, alerts, contracts, staging, audit trails) one failure at a time; the talk argues for blocking gates at the most expensive handoff.

- Techniques: Boring blocking gates before save; Guarded vs naive mode demo; Handoff mapping; Per-gate audit record; Voice and domain contracts as explicit rules
- Tools: Claude Code

## [Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon](../videos/LrGCT7G_rU8.md)
`LrGCT7G_rU8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: data-engineering, agent-architecture, security-guardrails, evals

Anna Marie Benzon presents a capstone ETL remediation agent: deterministic rules detect facts, tabular Q-learning picks among six bounded actions, and an external safety layer can force escalation. Results are from synthetic benchmarks.

- Techniques: Event-triggered diagnose-decide-act-verify loop; Rules for facts, learning for choices, guardrails for authority; Tabular Q-learning over a small discrete state; Propose, check, execute, and record separately; Multi-seed evaluation with baselines and confidence intervals
- Tools: AWS Glue, Amazon EventBridge, AWS Lambda, Amazon CloudWatch, AWS Glue Data Catalog, Amazon S3

## [Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](../videos/4uFVSLgD2Q4.md)
`4uFVSLgD2Q4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: agent-architecture, enterprise-adoption, evals, sandboxing-execution

OpenGov's Gabe De Mesa on how they built and scaled OG Assist, an in-product agent: an in-house Effect-native agent loop, A2A contracts, approval gates, ephemeral sandboxes, and rolling-summary context.

- Techniques: Effect-native agent loop with injected language model; A2A agent card as the API contract; Deterministic approval interrupt; Automated tool-call evals in CI; Ephemeral sandbox per agent task; Rolling summary with recent-window and recall; Runtime generative UI via registered primitives; Tools to toolkits to model registration
- Tools: Effect, Effect AI, LangGraph, A2A protocol, A2UI, Claude, Cursor, Claude Cloud Agents

## [MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc](../videos/sAOBXCDiDOs.md)
`sAOBXCDiDOs` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: mcp-and-tools, product-ux, security-guardrails

Pietro Zullo (Manufact) explains MCP Apps: tools that return sandboxed UI widgets, the primitives behind them, and how the new client app stores distribute MCP servers.

- Techniques: Widget-returning tool; Split structured output (UI vs model); Set-state to sync UI to model; Stream tool input into the UI; Widget actions that call tools; Client-aware output; Pre-submission checks for stores
- Tools: MCP, MCP Apps, MCP-UI, MCP SDK, MCP Inspector, React, Remotion, Excalidraw, Granola MCP, Linear MCP, Postgres MCP, Claude Code

## [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../videos/2IxD9OB3XuQ.md)
`2IxD9OB3XuQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: skills-self-improvement, evals, memory, context-engineering

Soheil Feizi (RELAI) argues agents should learn from production failures only through verifiable updates: turn logs into replayable test environments, route fixes to model, harness or memory, and gate each change with regression tests. Second half is a product demo.

- Techniques: Log-to-replayable-environment lift; Instruction-first environment bootstrap; Three-gate fix verification; Layer routing by smallest durable change; Regression-aware optimization; Regression trap in benchmark design; Reviewable change proposal as output
- Tools: RELAI Rely (rely optimize CLI), GEPA, Letta, mem0, LoRA, DPO, GRPO, RLVR, SFT

## [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis](../videos/IQkVMvXQKLY.md)
`IQkVMvXQKLY` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: security-guardrails, training-finetuning-rl, evals

Sachin Kumar (LexisNexis) shows that a backdoored fine-tune can pass behavioral evals, and that a sparse autoencoder trained on base-vs-fine-tune activation deltas finds the trigger with near-zero false alarms.

- Techniques: Diff SAE on activation deltas; Backdoor isolation score per feature; Procedural data with a controlled trigger; Objectively measured backdoor target; Build-gate probe check
- Tools: SmolLM2-360M, sparse autoencoder, LoRA, static analysis

## [When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis](../videos/XovaGv4f39A.md)
`XovaGv4f39A` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: rag-retrieval, context-engineering, multi-agent, infra-cost-scaling

Luis Romero-Sevilla (Orbis) on Extended Cache Augmented Generation (ECAG): for large, frequently replaced, densely interrelated document collections, split docs across parallel KV-cached context buckets and let a supervisor model interrogate them, instead of RAG or GraphRAG.

- Techniques: Parallel context buckets with a supervisor (ECAG); Dropping topical sharding for bucketing; Caching KV state per context bucket
- Tools: GraphRAG, vector database, KV cache

## [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](../videos/uiP88SpCi1Q.md)
`uiP88SpCi1Q` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: token-cost-efficiency, infra-cost-scaling, context-engineering, agent-architecture

An AWS developer advocate lists five ways to cut agent token spend: cache the system prompt, route by task difficulty, offload large tool results, cap tool loops, and trim conversation history, with per-tool observability to check each one.

- Techniques: System prompt and tool caching; Difficulty-based model routing; Tool result offload and summarization; Max-iteration cap on tool loops; Per-tool loop and latency observability; Sliding window history with summarization
- Tools: Strands Agents, Claude Haiku, Claude Sonnet

## [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](../videos/spNAUEgq_A8.md)
`spNAUEgq_A8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: multi-agent, context-engineering, agent-architecture, infra-cost-scaling

Justin Schroeder (Standard Agents) argues that small, isolated domain-specific agents composed under a coordinator beat ever-growing context-stuffed general agents on cost, scope, portability and scaling.

- Techniques: Composition of isolated domain agents; Scoped delegation requests; Per-task model routing; Hook-injected runtime facts; Capability scoping per agent; Recursive sub-agent tree
- Tools: Claude, Codex, OpenClaw, Hermes, MCP, Vercel AI SDK, Vercel Eve, Figma, Playwright, Gmail, Google Sheets, Google Workspace

## [Respect The Process - Andrew Dumit, Watershed Technology Inc.](../videos/CLttOU7n6sI.md)
`CLttOU7n6sI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: governance-compliance, coding-agents, testing-verification, sandboxing-execution

Andrew Dumit (Watershed) on deploying coding agents for sustainability supply-chain graph edits: constrain the effects through a typed SDK and deterministic execution, not the agent's reasoning, so the process can be validated.

- Techniques: Typed SDK as the only write path; Deterministic run executor (validate-then-commit); Review artifact instead of code review; Constrain effects, not reasoning; Eval-driven hill-climbing on the agent task
- Tools: Claude Code, TypeScript SDK, React agent (earlier version)

## [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](../videos/pSto5YaNGUo.md)
`pSto5YaNGUo` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · topics: evals, observability, software-factory, agent-architecture

Mutagent's CEO and CTO argue agents should be built and improved in an agentic loop: an offline eval-and-optimize loop plus an online trace-diagnose loop, with a demo of their research-preview evaluator and diagnose agents.

- Techniques: Spec-first agent definition; Eval-driven development as TDD for agents; Binary criteria with calibrated LLM judges; Trajectory-level evaluation; Failure-mode library with code-checkable indicators; Tiered trace sampling; Auto-research style optimization gated by evals; Orchestrator dispatching evaluator and diagnose subagents from a coding harness; Diagnostic report with assumptions block and human decisions
- Tools: Claude Code, Codex, Deep Agents (mentioned as a framework), Hermes (mentioned as a framework), Whisper Flow (speech-to-text for feedback), Tracing platform (auto-caption reads 'length use'; name unclear)

## [How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](../videos/1IdzkRVmWAA.md)
`1IdzkRVmWAA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: rag-retrieval, agent-architecture, training-finetuning-rl, evals

Mixedbread's team on why agents write keyword-soup queries that hurt retrieval, and how a bounded four-tool search harness, trained with SFT then RL, recovers much of the oracle gap.

- Techniques: Tiered search tool set for agents; Bounded parallel search rounds with dedupe; Priming with a corpus preview; Describe-the-need query framing; Oracle-gap diagnosis; SFT then on-policy RL with a mixed reward
- Tools: Mixedbread search, Codex, GPT-5, Gemini 3.5 Flash, grep, BM25

## [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](../videos/OqM67QG_Ikk.md)
`OqM67QG_Ikk` · AI Engineer · 2026-07-18 · q4 · deep · talk · topics: sandboxing-execution, security-guardrails, agent-architecture, infra-cost-scaling

A first-principles tour of why agent code needs sandboxes, comparing fork/exec, containers, gVisor and microVMs, then how to add disk snapshots, restore and multi-node scheduling for OpenAI-scale agent sandboxes.

- Techniques: Isolation ladder for untrusted tool execution; Driving a microVM through its VMM API; Per-device jailing for emulated devices; Incremental block-level disk snapshot; Acknowledge snapshot before upload completes; Tiered always-on block storage; Snapshot-aware scheduling; Startup latency hybrid
- Tools: gVisor, Firecracker, Cloud Hypervisor, CrossVM, QEMU, KVM, virtio, vsock, seccomp, VFIO, NBD, FIEMAP

## [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](../videos/OXMMN-XbxwA.md)
`OXMMN-XbxwA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: enterprise-adoption, pr-code-review, context-engineering, agent-architecture

Higharc's labs team on moving ML research prototypes into production via three levers: a design-doc-style "research prototype taxonomy," a decoupled Python microservice monorepo, and stacked-PR decomposition for review.

- Techniques: Research prototype taxonomy (RPT) doc; One researcher, one decoupled microservice in a shared monorepo; Slice by dependency graph, then stack PRs; Use the design doc to plan the merge; Notebooks on Modal for GPU experiments
- Tools: Notion, Graphite, GitHub Actions, Modal, Docker, FastAPI, Poetry, uv, Jupyter

## [Frontier results, on device - RL Nabors, Arize](../videos/fWXJM-J0ZB8.md)
`fWXJM-J0ZB8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: local-ai, inference-serving, evals, context-engineering

Rachel Lee Neighbors shows how to right-size a model: prototype with a frontier model, build a golden eval set, then pick the smallest local model (Llama 3.2 3B) that meets latency and quality targets, closing the gap with prompt changes and deterministic post-processing.

- Techniques: Prototype-big-deploy-small pipeline; Golden dataset with multi-metric eval in Phoenix; Latency budget by percentile; Single-variable prompt ablation; Deterministic post-processing instead of prompt tuning; Auditing the LLM judge; Regression evals in CI
- Tools: Phoenix (Arize), Goose, Gemma 4 E2B, Gemma 3, Llama 3.2 3B, Qwen 2.5 1.5B, Qwen 3 1.7B, Claude Sonnet, Claude Opus, MobileNet, YOLO, MediaPipe

## [Your Agents Need a Save Button - Hamza Tahir, ZenML](../videos/bZISsg7H7DA.md)
`bZISsg7H7DA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: agent-architecture, observability, evals

Hamza Tahir (ZenML) argues agents need checkpointed runtime state so production runs can be replayed with what-if changes (model swap, mocked tool), compared across cohorts, and shipped only after cohort-level diffs.

- Techniques: Per-step checkpointing of agent state; Counterfactual replay from a checkpoint; Side-by-side run diffing; Cohort replay with agent-driven analysis; Replay-based ship gate
- Tools: Kitaru, OpenTelemetry, GPT-5 Nano

## [How Autoresearch is changing ML research — Zhengyao Jiang, Weco](../videos/iCj_ATyThvc.md)
`iCj_ATyThvc` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: evals, software-factory, models-research

Weco's Zhengyao Jiang on AIDE, an autoresearch agent whose PRs won OpenAI's ParameterGolf and got reused by others; humans design the eval and code abstraction while the agent executes.

- Techniques: Publish-gated agent output; Strict eval API that separates held-out data; Recombine community ideas with the agent's own changes; Constraint-driven follow-up move
- Tools: AIDE (Weco's autoresearch agent), H100 GPU node, Quantization, Qwen gated attention (paper idea)

## [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](../videos/YZQsWVeN3rE.md)
`YZQsWVeN3rE` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: multi-agent, evals, context-engineering, rag-retrieval

Alex Bauer (Upside.tech) on building trust in AI for go-to-market data: manage agents like people, scaffold business context first, use a librarian and a jury-and-judge pattern, and use only tier-two agent harnesses for important work.

- Techniques: Commander's intent prompting; Anchor assets and scaffolding; Citation tracing for verification; Librarian pre-query lookup; Jury and judge; Tiered tool selection
- Tools: Claude, Claude Opus, Slackbot, ChatGPT

## [Everything we knew about software has changed — Theo Browne, @t3dotgg ​](../videos/xUnRQ9vLXxo.md)
`xUnRQ9vLXxo` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: product-ux, coding-agents, agent-architecture, multi-agent

Theo Browne argues that models have moved coding into an orchestration era, so tools, product tiers and software defaults should be rethought, with a markdown file running on cron as his example.

- Techniques: Markdown as a recurring program; Prompt-driven sub-agent orchestration; Breadth-first product with extension points; Assumption audit
- Tools: Claude Code, Codex, Git, GitHub, S3, Cron, Vercel, Slack bot APIs, Reddit, OBS, tmux, GNU Screen

## [Recursive Coding Agents - Raymond Weitekamp, OpenProse](../videos/3hXJI2q0Jz8.md)
`3hXJI2q0Jz8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: agent-architecture, coding-agents, multi-agent

Raymond Weitekamp (OpenProse) on applying recursive language model (RLM) ideas to coding agents, with Claude Code dynamic workflows, the Pi extension, and OpenProse markdown workflows as ways to build them.

- Techniques: RLM as a tool call for a coding agent; Recursive agent via a pure Pi extension; Map-reduce versus deep-research workflows in Claude Code; Declarative workflow with parent verification; Adversarial or skeptical subagent roles; Golden session distillation; Small local model as RLM root
- Tools: Claude Code, Codex SDK, Pi, OpenProse, DSPy (dspy.rlm), RLM package (Alex Zhang), Agentica (Symbolica), Axe, Unix RLM (bash), LambdaRLM, Qwen 3.5 9B

## [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](../videos/kZsf_Sfm7RU.md)
`kZsf_Sfm7RU` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: observability, pr-code-review, evals, multi-agent

Shipping an agent is where the real work starts. Raphael Kalandadze shows a post-launch loop: a log-monitor agent opens PRs, a fresh-context review agent critiques them, and a session analyzer scores every conversation for health.

- Techniques: Hourly log-monitor agent that opens PRs; Fresh-context review agent as a PR gate; Session analyzer for health scoring; Computer-use QA agent with a site-specific skill; Meta-harness: connect all context to the monitoring agents
- Tools: Claude Code, Codex, HTML artifacts, log and trajectory store, browser computer-use agent

## ["I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox](../videos/-CnA2lGfymY.md)
`-CnA2lGfymY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: security-guardrails, testing-verification, agent-architecture

Erik Meijer shows how to make agent tool calls provably safe by turning the plan into a program that can be type-checked, taint-analysed and proven before anything runs.

- Techniques: Plan as data, execute after check; Taint or data-flow analysis over the plan; Proof-carrying generation; Effects as data (free monad style)
- Tools: Lean, Dafny, Isabelle, PVS, TLA+, Claude Code

## [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../videos/IddXPepIAS4.md)
`IddXPepIAS4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: context-engineering, coding-agents, testing-verification, mcp-and-tools

Erik Hanchett (AWS) on spec-driven development: write requirements, design and task markdown before code, keep a human reviewer in the loop, and use property-based tests to check the result.

- Techniques: Manual spec loop with any coding assistant; Clarifying questions before requirements; EARS-format requirements; Property tests generated from requirements and design; MVP-first task ordering; Steering docs plus on-demand skills; Pull requirements from PM tools via MCP
- Tools: Kiro, spec-kit, MCP, FastCheck, Mermaid, EARS, Jira, Asana, agents.md, CLAUDE.md

## [The Pipeline Is Dead - Iris ten Teije, Sky Valley Ambient Computing](../videos/bRnoEpoK5m4.md)
`bRnoEpoK5m4` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: product-ux, agent-architecture, observability

Argues the one-version-for-everyone software pipeline ends as code gets cheap; proposes a canonical stem with per-user, bounded, reversible divergences and names the hard problems: provenance, testing, measurement, trust, coordination.

- Techniques: Stem plus bounded, reversible divergences; Developer-declared adaptation boundaries; Behavior-driven personalization with a spirit-of-the-software check; Traceable adaptation provenance; Goal-metric gating for changes; Recommend-first autonomy as a trust ladder; Coordination by intent and outcome

## [Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs](../videos/65X0pQ6Lmbg.md)
`65X0pQ6Lmbg` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: voice-multimodal, infra-cost-scaling, product-ux

Allen Pike (Forestwalk Labs) on why voice input with visual output beats voice-to-voice for AI now, and the latency tactics (fast small model, eager short inference turns, stable prompt prefixes) that make it feel responsive.

- Techniques: Two-tier model split (fast responder plus async thinker); Eager short-interval inference; Prefix-stable context layout for caching; Visual response envelope
- Tools: Linear, Slack, GPT-5 Mini, Haiku

## [WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar](../videos/8G_1-3IO4ZQ.md)
`8G_1-3IO4ZQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: context-engineering, memory, skills-self-improvement, enterprise-adoption

Atlan's founder argues production agents fail on missing business context, not model intelligence, and proposes a shared, versioned "context layer" (a company brain) that agents draw from.

- Techniques: Jobs-to-be-done scaling factor for agent selection; Shared context layer as a company brain; Context lifecycle management like software; Trace-driven maintainer loop; Reverse-construct the data stack to bootstrap context
- Tools: Claude Code, Codex, Claude Cowork, Google ADK, Glean, Relevance AI, MCP, Qualified, Artisan

## [Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra](../videos/EUsPvBeIx70.md)
`EUsPvBeIx70` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: rag-retrieval, data-engineering, agent-architecture, context-engineering

Phaidra engineers explain "semantic blindness": why RAG and LLM-only lookups fail on 400K+ equipment names, and how a hierarchy-based planner plus deterministic set-resolver stays accurate with flat cost at data-center scale.

- Techniques: Hierarchy summary as LLM context; LLM emits a structured search plan; deterministic resolver executes it; Pre-indexed subtrees for set operations; Two- or three-step planner/resolver pipeline in place of an agent loop; Pattern-based search for vague queries; Head-to-head eval against the old system at increasing scale; Move deterministic work out of the prompt

## [Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo](../videos/CDqzWpwkSls.md)
`CDqzWpwkSls` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: product-ux, evals, governance-compliance

Duolingo shows skilled reviewers accepted half of fake AI cheating flags; guidelines demanding independent evidence raised rejections 21%. Design human-in-the-loop interactions for discernment, not approval.

- Techniques: Calibration test with planted false signals; Reframe the AI output as a preliminary alert; Split compound questions into separate signals; Inline anchored feedback instead of a long essay; Surface assumptions and trade-offs for sign-off in agent plans; Capture the edit diff as the training signal; Log the questions users ask as a trust signal

## [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](../videos/9arM9b7JgOo.md)
`9arM9b7JgOo` · AI Engineer · 2026-07-18 · q2 · intro · workshop · topics: coding-agents, multi-agent, context-engineering

Snapchat engineer Jeffrey Lee-Chan demos his personal coding-agent workflow built on OpenClaw: a manager agent with memory delegates work to parallel worktree workers, and separating the manager's context from the workers' reduces overclaiming.

- Techniques: Manager and worker split with a separate-context reviewer; Layered verification with humans last; Context budgeting for the orchestrator; Local, staging, then production flow for agent changes; Cost-tiered model switching
- Tools: OpenClaw, CMUX, Claude Code, Claude Code Teams, Codex 5.3, GPT-5.4, MiniMax, git worktrees, Docker

## [Building an ACP-Compatible Agent Live — Bennet Fenner, Zed](../videos/HsxQICTLF84.md)
`HsxQICTLF84` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · topics: coding-agents, mcp-and-tools, agent-architecture

Live demo of turning a minimal TypeScript coding agent into an ACP-compatible agent for Zed: four required methods, streamed text, tool-call updates, client-proxied file access, and a diff content type.

- Techniques: Minimal agent loop as the ACP core; Session-scoped agent instances; Streaming through session-update notifications; Two-phase tool-call reporting; Client-proxied file system; Diff content type for edits; Using the protocol's debug view to inspect traffic
- Tools: Zed, Agent Client Protocol (ACP), ACP TypeScript SDK, Anthropic SDK, Node.js, stdio

## [Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta](../videos/grdoOC1BT1s.md)
`grdoOC1BT1s` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: product-ux, vibe-coding-app-building, multi-agent

Two Meta game-creation leads argue that AI prompting makes basic games easy, so taste, art cohesion, playtesting and runtime-LLM NPCs decide quality, with undeterminism as the open engineering problem.

- Techniques: Key-art anchoring for image generation; Personality-driven LLM NPCs in a shared game loop; Parallel AI-assisted production with frequent playtests; Runtime LLM game master for per-player adjustment
- Tools: Gemini, Nano Banana, Meshy, Manus, Labubu (demo subject)

## [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](../videos/vJukHCIv7Ck.md)
`vJukHCIv7Ck` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: mcp-and-tools, rag-retrieval, security-guardrails, multi-agent

AWS developer advocate walks through five code-level techniques to reduce agent hallucinations: semantic tool selection, GraphRAG for aggregation, multi-agent validation, code-enforced hooks, and steering rules. Demos use dummy tools.

- Techniques: Semantic tool selection; Per-turn tool swap in agent loop; Text-to-Cypher GraphRAG for aggregation; Executor, validator, critic swarm; Before-tool-call hooks for hard rules; Steering rules for soft constraints
- Tools: Strands Agents, OpenAI API, sentence-transformers, Neo4j (Cypher, LLM graph builder), agent-control (steering SDK), Amazon Bedrock AgentCore (Gateway, Runtime, Policy, Memory), DynamoDB, Neo4j AuraDB, AWS Lambda, Ollama (mentioned)

## [RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](../videos/8oyalrfwgjw.md)
`8oyalrfwgjw` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: context-engineering, coding-agents, agent-architecture

Shashi (Superagentic AI) explains Recursive Language Models (RLM) for large codebases: keep the repo in a REPL, let the model write code to slice it, and call sub-models in a loop. He demos his open-source RLM Code harness with Gemini.

- Techniques: REPL-based context slicing (RLM loop); Recursive sub-calls with a budget; Full trajectory capture as JSONL; Sandboxed REPL execution; Model-agnostic sub-calls
- Tools: RLM Code, DSPy, Gemini, Docker, Codex, Pydantic AI, Google ADK, JSONL trace export

## [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](../videos/ZRM_TfEZcIo.md)
`ZRM_TfEZcIo` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: memory, rag-retrieval, context-engineering

Two builders show a file-based personal research system: raw sources, an index.yaml catalog and an LLM-written wiki, queried in tiers and fed by every question. No vector DB needed.

- Techniques: Tiered index-first retrieval; Immutable raw layer with LLM-owned derivatives; Query write-back with a log; Seeded multi-round deep research; Depth knob for research runs; Repo ingestion into per-repo and cross-repo notes
- Tools: Obsidian, Readwise, NotebookLM, Notion, Google Drive, Granola, Claude Code, Codex, Gemini Deep Research, Gemini (grounded Google search), Bright Data, YAML

## [Using LLMs to Secure Source Code — Eugene Yan, Anthropic](../videos/imFedndyXYQ.md)
`imFedndyXYQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · topics: security-guardrails, testing-verification, sandboxing-execution, multi-agent

Eugene Yan (Anthropic) walks through a six-step harness for using LLMs to find, verify, triage and patch vulnerabilities, arguing the bottleneck has moved from finding bugs to verification, triage and patching.

- Techniques: Threat model as a living context document; Isolated, reproducible PoC sandbox; Independent adversarial verifier; Tool-equipped discovery; Less prescriptive prompts for stronger models; Patch validation ladder with a generative verifier loop; Close the loop as a regression check; Severity triage as impact times likelihood with compensating controls; Code-owner routing without an LLM
- Tools: Claude, Claude Code, Docker, PostgreSQL, Redis, Jira

## ["The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic](../videos/n97BCfyFIvw.md)
`n97BCfyFIvw` · AI Engineer · 2026-07-18 · q3 · intro · talk · topics: software-factory, governance-compliance, pr-code-review, product-ux

Addy Osmani argues engineers are defined by owning the verdict on agent work: choosing what is worth doing, backing it with evidence, and accepting accountability. Keep humans at the highest-leverage checkpoint.

- Techniques: Inner loop / outer loop split; Evidence bundle as the review unit; Explain-it-or-don't-ship gate with named owners; Review as a control system for long runs; Move verification into the harness; Clean code for agents as well as humans
- Tools: Git

## [A Genius With Amnesia - Victor Savkin, Nx](../videos/jVjt-2g8NMY.md)
`jVjt-2g8NMY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: coding-agents, memory, agent-architecture

Victor Savkin (Nx) argues coding agents are limited by seeing one repo and forgetting past sessions, and shows Polygraph, a meta-harness that builds a cross-repo dependency graph and replays captured sessions on other machines.

- Techniques: Out-of-band cross-repo dependency graph; Multi-repo session as one unit of work; Session state replay for handoff; Intent-based scope selection; Agent-agnostic meta-harness
- Tools: Polygraph, Nx, Claude Code, Codex, GitHub

## [User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](../videos/Jx4ZFEAq6bY.md)
`Jx4ZFEAq6bY` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: memory, rag-retrieval, skills-self-improvement, evals

StarlightSearch's CEO argues agent memory should learn from outcomes: utility-weighted retrieval, reasoning-style memories, and consolidation into skills. Product-pitchy, with self-reported benchmarks.

- Techniques: Utility-weighted memory retrieval; Human failure report as a memory write; Memory as procedure, not fact; Consolidate memories into skills; Runtime learning vs compile-time optimization
- Tools: Reflect (StarlightSearch's memory system), Mem0 (transcribed as 'memzero'), DSPy, ReAct, Pinecone (cited in a post, not used)

## [GTM Is You - Victoria Melnikova, Evil Martians](../videos/G6IlDzj8OjA.md)
`G6IlDzj8OjA` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: product-ux

A go-to-market talk for developer-tool founders: distribution is now the bottleneck, so use a signal-vs-revenue check, a six-step GTM routine, and personal brand to get customers.

- Techniques: PMF Compass diagnostic; Six-step GTM hygiene checklist; Founder-as-channel distribution; Visible, low-cost proof of momentum

## [The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft](../videos/jtzh-GBXBWc.md)
`jtzh-GBXBWc` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: multi-agent, memory, skills-self-improvement, enterprise-adoption

A 100-person Indian thermoforming-machine maker built a 36-agent go-to-market "brain" with layered memory and a nightly dream cycle, with no training and no framework. The talk is a company story with some architecture and cost claims.

- Techniques: One-job specialist agents with an orchestrator and debate; Layered agent memory with a salience gate and correction precedence; Nightly consolidation (dream cycle) job; Rules file as production guardrails; Chunk-and-extract over a private corpus with no training; Draft-only outbound with human send
- Tools: Cursor, vector database, graph database, CRM, Google Workspace integrations, document ingestion tooling, monitoring tooling

## [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](../videos/APh1Vx0oLmQ.md)
`APh1Vx0oLmQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · topics: agent-architecture, security-guardrails, observability, infra-cost-scaling

Nishant Gupta (Meta Superintelligence Labs) argues that agent reliability is an infrastructure problem: treat models as probabilistic, keep the platform deterministic, and let infrastructure validate and enforce what the model proposes.

- Techniques: Propose, validate, enforce split; Tool isolation with circuit breakers; Controlled recovery instead of open retries; Decision-chain tracing; Per-agent limits and cost quotas; Layered defence for agent actions; Humans as exception handlers

## [What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip](../videos/7P0elyLIxXo.md)
`7P0elyLIxXo` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · topics: testing-verification, agent-architecture, multi-agent

Dotta (Paperclip) argues "done" is a bundle of claims, not a checkbox, and shows how a control plane with blockers, reviewers, and watchdogs keeps agent work moving while still verifying it.

- Techniques: Done as a structured object; Cross-model verifier; Evidence-first completion; Watchdog agent for goal persistence; Explicit state transitions with enforced blockers; Per-task reviewer and approver assignment with audit trail
- Tools: Paperclip, Pi, OpenClaw, Hermes, Claude Code, Codex

## [Structuring the Unstructured - Cedric Clyburn, Red Hat](../videos/-x5GEVnkuRw.md)
`-x5GEVnkuRw` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · topics: data-engineering, rag-retrieval, mcp-and-tools, context-engineering

Red Hat's Cedric Clyburn demos Docling, an open-source local tool that converts messy PDFs into layout-aware Markdown, JSON, or Pydantic data, plus chunkless RAG over a document outline.

- Techniques: Layout-aware PDF to structured document conversion; Picture enrichment with a local vision-language model; Chunkless agentic RAG over a document outline; Schema-driven extraction from parsed documents; Document conversion as a microservice plus MCP tool; PII removal model before ingestion
- Tools: Docling, docling-serve, Docling MCP server, Pydantic, Ollama, Granite (IBM model), Qwen (via MLX), Jupyter, VS Code, Kubernetes, uvx

## [Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, Sarvam AI](../videos/JnubYCYunk8.md)
`JnubYCYunk8` · AI Engineer · 2026-07-18 · q2 · intro · demo · topics: voice-multimodal, context-engineering, token-cost-efficiency

Kushan Raj (Sarvam AI) argues browser agents fail because of their infrastructure, not model quality, and shows a compact page representation plus change feedback that makes a cheap model faster and more reliable.

- Techniques: Compact page representation for agents; Delta feedback to the agent; Invest in the environment instead of the model; Expose a browser task as an API
- Tools: browser agent harness (speaker's own, to be open sourced), Claude (used as the baseline in demos)

## [Introducing WebMCP: Agents in the Browser — RL Nabors](../videos/LMbeDEQO6QM.md)
`LMbeDEQO6QM` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: mcp-and-tools, voice-multimodal, product-ux

A practical tour of MCP over HTTP, MCP Apps for in-chat UI with CSP and sandbox gotchas, and WebMCP, which lets agents call tools exposed by a web page's own JavaScript.

- Techniques: Single server, multiple client surfaces; Remote connector onboarding over HTTP; App-only tool visibility for UI navigation; Bundle MCP App into one file with explicit CSP; WebMCP imperative registration with feature detection; Declarative WebMCP on existing forms
- Tools: MCP, MCP Apps, WebMCP, navigator.modelContext.registerTool, Vite single-file plugin, Web Speech API, MCP Inspector-style debugging extension

## [Reachy Mini: the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face](../videos/0jeZfjJMfmo.md)
`0jeZfjJMfmo` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: voice-multimodal, inference-serving, infra-cost-scaling

Hugging Face's Andres Marafioti on the open-source $300-450 Reachy Mini robot, its voice pipeline, and how a streaming TTS model was made fast enough for real-time voice agents.

- Techniques: Stream TTS audio instead of generating full utterances; Static KV cache plus graph capture for autoregressive audio models; Partial STT every 150 ms; Separate scaling of LLM inference from stateful conversation nodes; Measure the whole latency path, not just the model; Codex-driven hardware app development
- Tools: Reachy Mini, Raspberry Pi, Codex, Parakeet, Qwen3-TTS, Qwen 3.5 27B, Kokoro, Voxtral, Hugging Face Inference Endpoints, speech-to-speech pipeline, GPT Realtime

## [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](../videos/wcUJWP6WpGM.md)
`wcUJWP6WpGM` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: evals, coding-agents, testing-verification, training-finetuning-rl

Ibragim Badertdinov (Nebius) shares lessons from running monthly SWE-rebench evals of coding agents: fresh time-split tasks, verifier quality, infra noise, benchmark cheating, and reporting cost and reliability.

- Techniques: Monthly time-split task collection; Oversample, then filter by running agents; Strip future information from the agent sandbox; Minimal agent with strong infrastructure; Error-class retry policy; Reliability-aware metrics; Reproduce a public benchmark before trusting your own numbers; Eval pipeline reused as training pipeline
- Tools: SWE-rebench, SWE-bench, Terminal-Bench, Claude Code, Codex, Junie, Docker, GitHub Archive, GitHub API

## [Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse](../videos/vNCY9kXXyDQ.md)
`vNCY9kXXyDQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: skills-self-improvement, observability, evals, claude-code

Langfuse's founder explains how they built an installable skill that teaches coding agents to add Langfuse tracing and evals, and what they learned about docs, eval checks and auto-tuning skills.

- Techniques: Skill with progressive disclosure; Agent-facing docs surface; Wrap the API as a CLI and advertise --help; Natural-language checks for skill evals; Auto-research loop on a skill with human review; Timestamped skill copies for staleness
- Tools: Claude Code, Langfuse, OpenAI SDK

## [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](../videos/iUWwcG-C8OU.md)
`iUWwcG-C8OU` · AI Engineer · 2026-06-18 · q4 · practitioner · demo · topics: data-engineering, agent-architecture, context-engineering, enterprise-adoption

WorkOS product lead Garrett Galow demos Studio, an internal agent that answers business questions and turns repeat questions into live widgets. Main lessons: pre-flight checks, runtime tool context, query validation, and keeping the LLM out of widget refresh.

- Techniques: Generated declarative widgets; Pre-flight checks and clarifying questions; Runtime tool-context injection; Layered prompts; Distrust model priors for product facts; Execute-and-validate before deploy; Org-level connectors with role-based defaults
- Tools: Snowflake, Linear, Notion, Convex, LangGraph, Claude Opus, Slack bot, Retool, WorkOS Pipes

## [Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe](../videos/KLSuFPj2ld0.md)
`KLSuFPj2ld0` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: security-guardrails, governance-compliance, mcp-and-tools

Stripe's Steve Kaliski on letting agents spend safely: scope shared payment tokens to amount, time and seller, use HTTP 402 for paid tools, and keep discovery non-deterministic while payments stay deterministic.

- Techniques: Seller-scoped delegated payment credential; Deterministic transaction layer behind a non-deterministic planner; HTTP 402 pay-per-call; Round-trip checkout state; Forward risk signals to the counterparty
- Tools: Stripe shared payment tokens, Stripe Payment Intents, Stripe Issuing, Machine payments protocol (with Tempo), Agentic Commerce Protocol (with OpenAI), curl (demo), Tempo blockchain (pathUSD), Base

## [Text Diffusion — Brendan O’Donoghue, Google DeepMind](../videos/r305-aQTaU0.md)
`r305-aQTaU0` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: models-research, inference-serving, token-cost-efficiency

Google DeepMind researcher explains text diffusion as a low-latency, non-autoregressive alternative to next-token LLMs, covering why it is fast, self-correcting, and adaptive, plus its throughput cost.

- Techniques: Discrete corruption and denoising training; Latency-first serving by block; Test-time compute via denoising steps; Self-correction through reason-then-revise; In-place infilling and editing
- Tools: Gemini Diffusion, Gemini 2.0 Flash-Lite, Gemini 2.5 Flash, GPT-4o, Gemini (autoregressive baseline, unnamed version), Nano Banana (named as a later image model), Juno (named as the image model at the time; caption may be garbled), GPQA Diamond (eval), MBPP (eval)

## [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](../videos/ghJmWQCIHRM.md)
`ghJmWQCIHRM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: mcp-and-tools, voice-multimodal, product-ux

Google Chrome DevRel on WebMCP, a proposed browser standard that lets a website expose its actions as structured tools for in-browser AI agents, with declarative and imperative APIs and an early-preview setup guide.

- Techniques: Declarative tool exposure from HTML forms; Imperative registerTool for multi-step UI; Mirror tool calls in the visible UI; Hybrid browse-then-delegate flow; Test tools with an inspector and evals CLI
- Tools: WebMCP, Chrome Canary, Model Context Tool Inspector (Chrome extension), Gemini, Chrome DevTools-style flag (WebMCP testing flag), WebMCP evals CLI

## [20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna](../videos/hqHC6Z_lXyo.md)
`hqHC6Z_lXyo` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: evals, models-research, inference-serving

Public leaderboards and manual or metric-based checks mislead model choice; the speaker argues for task-specific, many-sample evals plus Pareto fronts of quality vs latency and cost, where smaller fast models often win.

- Techniques: Pareto front selection; Consensus across leaderboards and per-task boards; Large-sample, condition-matched human evaluation; Metric validation before use; Compression for latency (quantization, pruning, step reduction)
- Tools: Design Arena, LM Arena (now Arena), Artificial Analysis, CLIP score, Pruna open-source compression package

## [Your Coding Agent Should Do AI System Engineering — Ben Burtenshaw, Hugging Face](../videos/JomVvNDjGb8.md)
`JomVvNDjGb8` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: coding-agents, skills-self-improvement, multi-agent, training-finetuning-rl

Ben Burtenshaw (Hugging Face) argues coding agents can take on AI systems work: writing CUDA kernels, fine-tuning models, and running a multi-agent automated research lab, using open skills, open Hub repos and an open dashboard data layer.

- Techniques: Skill-as-few-shot-examples with bundled benchmark scripts; Skill eval across models (Upskill); Role-split autoresearch loop; Git and bucket as agent shared state; Open-format dashboard as an agent data source; Verifiable-experiment precondition
- Tools: CUDA, Hugging Face kernels library, Upskill, Hugging Face Skills repo, HF Papers CLI, HF Jobs, OpenCode, Codex, Claude Code, Trackio, Parquet, Unsloth

## [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](../videos/zKk7sDMGDEQ.md)
`zKk7sDMGDEQ` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: rag-retrieval, claude-code, evals, coding-agents

Turbopuffer's Kuba Rogut benchmarks semantic code search as an extra tool for Claude Code, using a windowed-grep baseline and file, line and symbol precision and recall on human-labelled context tasks; semantic search helps precision but the gain is smaller than Cursor's because Claude Code does not know when to call it.

- Techniques: Chunk-embed-index semantic code search as a CLI tool; Windowed file reads as a retrieval baseline; Trajectory-level retrieval evaluation; Inline comments as embedding context
- Tools: Turbopuffer, Voyage code-3, Claude Code, Cursor, TurboGrep, tree splitter

## [Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j](../videos/abvQEhvRI_c.md)
`abvQEhvRI_c` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: memory, agent-architecture, context-engineering, rag-retrieval

Neo4j speakers argue agents need context graphs that store policies and rules as well as facts, so they can make and record decisions. They give a decision framework: frame, check global rules, assess risk, propose, then act, defer or escalate.

- Techniques: Propose, then decide, as two agents; Pre-decision risk screen; Decision log as a graph of precedent; Tiered memory in one graph; Framework as a skill or graph workflow
- Tools: Neo4j, Text2Cypher, LangGraph, ADK

## [Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI](../videos/mFLlVpnGpds.md)
`mFLlVpnGpds` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: voice-multimodal, evals, data-engineering

Pyannote's Hervé Bredin explains why speaker diarization is still unsolved and why merging it with STT word timestamps is hard, with a live DER demo.

- Techniques: DER error breakdown; Benchmark in your own acoustic condition; Exclusive diarization in overlaps; Timestamp-based word-to-speaker alignment; Model-agnostic reconciliation layer
- Tools: pyannote (open-source diarization toolkit), pyannote metrics (DER evaluation), OpenAI Whisper, NVIDIA Parakeet, Hugging Face model hub, pyannoteAI cloud API

## [Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind](../videos/3_gYbhABcAE.md)
`3_gYbhABcAE` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: agent-architecture, evals, mcp-and-tools, context-engineering

Philipp Schmid (Google DeepMind) lists five habits from deterministic software that break when building agents: text as state, handing control to the LLM, errors as inputs, pass-rate evals, and agent-ready tools.

- Techniques: Goal-first dispatcher prompting; Free-text approval with edits; Preferences as natural language in context; Errors as observations; Repeated-run pass-rate evals with judges; Agent-ready tool definitions
- Tools: Gemini API, Gemini

## [Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind](../videos/BcWFc3H7Khg.md)
`BcWFc3H7Khg` · AI Engineer · 2026-06-18 · q3 · practitioner · workshop · topics: voice-multimodal, models-research, context-engineering

Live workshop from Google DeepMind's Guillaume Vernade building an illustrated children's book with Gemini, Nano Banana, Veo, Lyria and TTS, plus API tips on retries, service tiers and stateful chats.

- Techniques: Retry wrapper around the media client; Service tier choice per request; Iterate cheap, then upscale; Structured output as a scene manifest; Style and composition system instructions; Streamed Lyria output; Lyria RealTime as a live, steerable stream
- Tools: Gemini API, Vertex AI, Google AI Studio, Google GenAI SDK, Google Colab, Nano Banana 2, Veo 3.1 and Veo 3.1 Lite, Lyria 3 clip and full-song models, Lyria RealTime, Gemini TTS, Interactions API, Gutenberg (source book)

## [Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel](../videos/YYH0DMQr30A.md)
`YYH0DMQr30A` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: training-finetuning-rl, evals, data-engineering

Snorkel's Kobe Crawford argues that task quality is data quality for agentic terminal tasks, and shows that RL on verified high-quality tasks gives about 5x the uplift of low-quality ones.

- Techniques: Containerized task environments with a verification test gate; Accepted vs rejected task comparison; Failure taxonomy for benchmark runs; Controlled RL A/B on task quality; Rubric-based human and LLM-judge calibration; Make tasks verifiable on the back end
- Tools: Harbor Framework, Terminal-Bench, Claude Sonnet 4.5, Codex, GPT-5.2, GPT-5.1

## [Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat](../videos/F1DYkY1BlfM.md)
`F1DYkY1BlfM` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · topics: sandboxing-execution, security-guardrails, infra-cost-scaling

Red Hat's Sally Ann O'Malley runs OpenClaw agents in Podman containers, keeps API keys as secret refs, and lifts the same setup to Kubernetes; the talk is a live demo with a pitch for containers as the default agent sandbox.

- Techniques: Podman secrets + secret-ref indirection for agent API keys; Container as the agent sandbox with explicit host grants; Mount the agent's tool directory at startup; Named volume for runtime state with scheduled backup; Local-to-Kubernetes lift with the same image; Company baseline image with per-user layer; SSH sandbox for remote execution; Installer that converts env vars to secret refs and sets providers
- Tools: OpenClaw, Podman, Podman secrets, Docker, Kubernetes, OpenShift, kind, systemd, OpenRouter, Anthropic, Gemma, OpenTelemetry

## [Fast Models Need Slow Developers — Sarah Chieng, Cerebras](../videos/TeGsFFNqRLA.md)
`TeGsFFNqRLA` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: coding-agents, inference-serving, testing-verification, context-engineering

Cerebras's Sarah Chieng argues that fast coding models (Codex Spark, ~1,200 tok/s) demand new habits: plan with a large model, execute with a fast one, verify every step, and keep context in bounded goals.

- Techniques: Planner-executor model split; Session-to-skill distillation; Per-step automatic verification; Parallel variant generation with cherry-picking; Scoped steering constraints; Automatic refactor pass after each task; Bounded goals with a context budget; Four-file external memory (AGENTS/PLAN/PROGRESS/VERIFY)
- Tools: Codex Spark, Codex, GPT-5.4, GPT-5.3 Codex, Sonnet, Opus, REAP (router-weighted expert activation pruning)

## [Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence](../videos/UQKg0td-Bf4.md)
`UQKg0td-Bf4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: testing-verification, evals, security-guardrails, mcp-and-tools

Steven Willmott (SafeIntelligence) argues agent testing needs an explicit spec of data, rules, terminology, roles and robustness needs, kept separate from the implementation and run in a closed loop.

- Techniques: Six-part agent spec; Spec-driven security testing; Input perturbation sweep; Closed-loop spec iteration (backyard RL); Specs as versioned repo files; Agent cards plus variation envelopes
- Tools: SafeIntelligence platform, A2A agent cards, LangSmith, Vertex AI agents, Braintrust, OpenAPI

## [Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman](../videos/hCMrEfPG2Yg.md)
`hCMrEfPG2Yg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: product-ux, mcp-and-tools, sandboxing-execution

Ruben Casas (Postman) maps generative UI from static components to declarative JSON to runtime-generated HTML/JS, argues MCP apps are the right sandboxed delivery layer, and says collaborative canvases are the next step.

- Techniques: Declarative generative UI with a component catalog; Static client-tool to component mapping; Runtime generated HTML/CSS/JS in a sandboxed MCP app; Use MCP apps as the default delivery for generated UI
- Tools: MCP apps, AG-UI, Goose (auto visualizer), json-render (Vercel), FastMCP, Excalidraw MCP app (transcribed as ScallyDraw), Claude Visualizer, GPT-5.2, Claude Opus 4.5, React

## [Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub](../videos/_xIwFcnHqp4.md)
`_xIwFcnHqp4` · AI Engineer · 2026-06-18 · q3 · practitioner · demo · topics: mcp-and-tools, coding-agents, product-ux

Marlene Mhangami and Liam Hampton (GitHub) show how MCP Apps let a tool return an interactive HTML UI rendered in a sandboxed iframe inside VS Code chat, with a live Go flame-graph demo.

- Techniques: MCP App tool-plus-resource pattern; Skill-driven MCP app scaffolding; Tool visibility scoping; Profiler-to-flame-graph bridge; Install MCP servers from curated lists only
- Tools: VS Code, GitHub Copilot, Copilot CLI, MCP, Go pprof, React, Excalidraw, Figma

## [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](../videos/so9l_MwS2yg.md)
`so9l_MwS2yg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: claude-code, software-factory, testing-verification, skills-self-improvement

Zack Proser (WorkOS) argues human attention, not agent capacity, is the bottleneck, and shares remote Claude Code from a phone, verification gates, and session-log mining to protect focus.

- Techniques: Three-tier verification ladder for agent output; Closed-loop ticket fixing with explicit done criteria; Remote-controlled session from a phone; Scheduled session-log retrospective; Ticket-tagged overnight agent loop; Parallel large features with worktrees and agent teams; Voice-first brainstorm, then written artifact
- Tools: Claude Code, Claude Opus 4.6, Slack MCP, Linear MCP, GitHub Mobile, Cursor, Codex, Vercel bot, OpenClaw, Twilio, ChatGPT advanced voice mode, git worktrees

## [Personalization in the Era of LLMs - Shivam Verma, Spotify](../videos/5YSJEP0HWzM.md)
`5YSJEP0HWzM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: training-finetuning-rl, context-engineering, enterprise-adoption

Spotify's AI Foundation tech lead explains how it personalizes recommendations with user embeddings, semantic IDs for catalog items, and soft user tokens fed into a fine-tuned open-weight LLM.

- Techniques: Semantic ID tokenization of item embeddings; Soft user token injection; Tokenized listening-history prompting for domain adaptation; Daily batch user-embedding generation; User-editable text profile as a steering signal
- Tools: Llama, Qwen

## [The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI](../videos/iNkFlCiij0U.md)
`iNkFlCiij0U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: evals, models-research

Snorkel AI's Vincent Chen on what makes agent benchmarks useful: rigorous task quality, distributional coverage, unsaturated difficulty, multi-axis scoring, a clear thesis, and researcher-friendly tooling, plus three axes for the next benchmarks.

- Techniques: Adversarial multi-reviewer task validation; Taxonomy-first task distribution; Separate constraint scoring from task completion; Check for headroom before publishing a benchmark; Build for researcher UX
- Tools: Terminal-Bench, Harbor, HELM, SWE-bench, tau-bench, GPQA, MMLU, ARC-AGI

## [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../videos/pmoDeA3RBZY.md)
`pmoDeA3RBZY` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: software-factory, multi-agent, coding-agents, skills-self-improvement

OpenClaw maintainer Vincent Koc on running dozens of parallel coding agents as a "dark factory": swim lanes, opinionated loops, a big plugin refactor, and token efficiency over token maxing.

- Techniques: Swim-lane parallel agents; Big refactor gated by existing tests; Plugin split for blast-radius control; One clone per session instead of worktrees; Explanation quality as a health check; Skill improvement from session logs; Embedding graph for backlog dedupe; Synthetic plus real fake-chat eval harness
- Tools: Codex, Git worktrees, GitHub, Discord, Slack, MS Teams, Docker, GEPA, skills.sh, OpenClaw, NemoClaw, vector embeddings

## [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../videos/KA5kPbdkK2E.md)
`KA5kPbdkK2E` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: skills-self-improvement, evals, observability, vibe-coding-app-building

Benjamin Verbeek (Lovable) on two continuous-learning loops: a self-updating "Stack Overflow" of fixes for stuck users, and an agent "vent" tool that reports platform friction to engineers.

- Techniques: Stuck-session detection with an LLM judge; Clustered, generalised fix knowledge bank; Blank-injection holdout; Tuned agent vent tool; Agent triage of agent feedback; Feedback volume as an incident detector
- Tools: Slack, Framer Motion

## [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](../videos/TNwJ1LMiENk.md)
`TNwJ1LMiENk` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: training-finetuning-rl, evals, mcp-and-tools

Snorkel shows a 4B model, RL-trained on single-table financial tool-use tasks for under $500, beating a 235B model. The gain came from fixing tool discipline, not reasoning.

- Techniques: Behavior-targeted RL with GRPO on a tool environment; Single-table-first training data; Verification pass on generated tasks; Rubric decomposition for diagnosis; Publish the environment as a portable package
- Tools: GRPO, RLM framework (UC Berkeley), FinQA environment (Snorkel), OpenEnv, Prime Intellect, Harbor, GetTableNames / GetTableInfo tools, Qwen3

## [Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind](../videos/Ubwb6NzegyA.md)
`Ubwb6NzegyA` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: evals, testing-verification, models-research

Google DeepMind and Kaggle staff tour their open eval platforms (hackathons, agent exams, Game Arena, community benchmarks) and the problems they hit: saturation, cost, harness variance, and hidden configs.

- Techniques: PvP game benchmark with pairwise rating; Task-of-assertions plus LLM-judge benchmark structure; One-line agent exam; Lock down the harness and config when comparing models
- Tools: Kaggle Benchmarks, Kaggle Game Arena, OpenSpiel, Kaggle simulation platform, LLM model proxy (also available on Colab), Bradley-Terry pairwise rating, Moltbook (transcribed as Motebook), SWE-Bench Pro (cited)

## [Run Frontier AI at Home — Alex Cheema, EXO Labs](../videos/ESbWpPT_9-o.md)
`ESbWpPT_9-o` · AI Engineer · 2026-06-18 · q3 · deep · talk · topics: local-ai, inference-serving, infra-cost-scaling

EXO Labs' Alex Cheema argues decode is memory-bound, so local frontier inference is a memory, bandwidth and energy problem. He demos Mac clusters over Thunderbolt RDMA and a Mac plus DGX Spark prefill/decode split.

- Techniques: Kernel fusion of redundant launches; Cache-stable prompt prefix in the harness; Prefill/decode disaggregation across devices; Tensor parallelism over RDMA; Full-replica weights with append-only event logs for cluster state; Expose each node over HTTP and reach it through a mesh VPN; Budget-based Pareto benchmarking; Hypothesis-driven auto-research
- Tools: EXO, Claude Code, OpenCode, OpenClaw, Tailscale, MLX, llama.cpp, Thunderbolt 5 RDMA, 10GbE

## [How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind](../videos/7gujZrJ9L5I.md)
`7gujZrJ9L5I` · AI Engineer · 2026-06-18 · q3 · intro · panel · topics: agent-architecture, coding-agents, skills-self-improvement, infra-cost-scaling

A Google DeepMind panel on running coding and research agents at Google scale, covering shared workspaces, quota and cost control, skill sprawl, internal observability, and PR review.

- Techniques: Shared file-system workspace between agent stages; Editable plan gate before execution; Scratchpad notes as a reviewable trace; Mock compute for harness testing; Trajectory store plus hierarchical drill-down; Per-language fine-tuned review model plus per-product review prompts; Transparent model fallback under the harness; Skills plus guardrailed CLI over MCP for internal tools
- Tools: Antigravity, Gemini, Gemma 4, Deep Research, Jules, MCP, OpenClaw

## [Cooking with Agents in VS Code — Liam Hampton, Microsoft](../videos/dyHpnnlkTc8.md)
`dyHpnnlkTc8` · AI Engineer · 2026-06-18 · q2 · intro · demo · topics: coding-agents, multi-agent, context-engineering, sandboxing-execution

A Microsoft product tour of running local, background (worktree) and cloud coding agents side by side in VS Code, with advice on which mode fits which task.

- Techniques: Worktree-per-background-agent; Route tasks by hands-on level; Plan first, autopilot second, pause before PR; Task-specific custom agents; Cloud agent with MCP and browser testing
- Tools: GitHub Copilot, VS Code, GitHub Copilot CLI, Git worktree, GitHub Actions, GitHub MCP server, Playwright MCP server, Microsoft Learn MCP server, awesome-copilot (open-source repo of agent customizations), Claude Opus 4.6 (used for the local agent)

## [Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind](../videos/SS-A8sE7hkw.md)
`SS-A8sE7hkw` · AI Engineer · 2026-06-18 · q2 · intro · talk · topics: local-ai, models-research, inference-serving, governance-compliance

Google DeepMind's Gemma team pitches open-weight Gemma 4 models (E2B to 31B) as a way to own, customize and run models locally, with on-device and single-GPU demos.

- Techniques: Drop-in local endpoint swap; Local sub-agent fan-out for batch work; Threshold-based task routing; Latency-class scheduling for on-device tasks; Own-eval-first model adoption
- Tools: Gemma 4, Gemini, Google AI Edge Gallery, LM Studio, Ollama, MedGemma, OpenRouter, LM Arena

## [RAG is dead, right?? — Kuba Rogut, Turbopuffer](../videos/UM6sFg_jdlE.md)
`UM6sFg_jdlE` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: rag-retrieval, coding-agents, context-engineering, infra-cost-scaling

Kuba Rogut (Turbopuffer) argues that "RAG is dead" misreads the problem: retrieval should be a toolbox (vector, BM25, grep, filters) used in iterative agent loops, and embeddings work best as precomputed cache compute.

- Techniques: Multi-modal retrieval toolbox for agents; Iterative search-read-assess loop; Index once, query at runtime; Merkle-tree index reuse across near-identical corpora; Staged narrowing before the context window
- Tools: Claude Code, Codex, Cursor, Turbopuffer, BM25, Merkle trees

## [Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI](../videos/TUnPNY4E2fw.md)
`TUnPNY4E2fw` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: training-finetuning-rl, infra-cost-scaling

Together AI's Max Ryabinin walks through stacking memory optimizations (Ulysses context parallelism, checkpointing, CPU offload, tiling, and the UPipe head-chunking method) to train with multi-million-token context.

- Techniques: Staged memory accounting; Head-based context parallelism (DeepSpeed Ulysses); Activation checkpointing plus CPU offload of block inputs; Sequence tiling of element-wise ops; UPipe head chunking with buffer reuse; Profile with PyTorch profiler first
- Tools: PyTorch profiler, FSDP, DeepSpeed Ulysses, FlashAttention

## [GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod](../videos/zDGHt0LB-dA.md)
`zDGHt0LB-dA` · AI Engineer · 2026-06-18 · q2 · intro · demo · topics: inference-serving, infra-cost-scaling

RunPod's Audrey Hsu demos Flash, a Python SDK that runs a decorated async function on a cloud GPU with hot reload from the local dev loop, plus a multi-model image pipeline and a pods-vs-serverless cost note.

- Techniques: Decorator-based remote GPU execution with hot reload; LLM prompt expansion before image generation; Chained model pipeline with separate endpoints per stage; Start small, then scale: pods for experiments, serverless for fan-out
- Tools: RunPod Flash (Python SDK), RunPod Serverless, RunPod Pods, RunPod Clusters, RunPod Hub, Stable Diffusion XL Turbo, DreamShaper, Qwen3, Google image composition model (Nano Banana 2), PyTorch, FastAPI, Docker

## [How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed](../videos/phchDt63qAA.md)
`phchDt63qAA` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: training-finetuning-rl, evals, product-ux

Zed's Edit Predictions lead explains how Zeta 2, a small fine-tuned next-edit model, was distilled from frontier teachers using opt-in production snapshots, settled-state labels, and multi-sample filtering.

- Techniques: Teacher repair loop; Cache the teacher, vary the formatting; Settled-state labels via idle detection; Multi-sample consensus filter with a distance band; Multi-reference offline eval; Percentage-based live experiment rollout
- Tools: Zed, Zeta 2, Seed Coder, Levenshtein distance, JSONL

## [The maturity phases of running evals — Phil Hetzel, Braintrust](../videos/FB-MLPhL9Ms.md)
`FB-MLPhL9Ms` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: evals, observability, testing-verification

Phil Hetzel (Braintrust) lays out four maturity stages of agent evals, from documented vibe checks to replaying tool-using agents offline with captured system state.

- Techniques: Documented human annotation (thumbs plus justification); Failure-mode extraction from justifications; LLM-as-judge with binary outputs and human-aligned ground truth; Deterministic code scorers for objective failures; Production trace flywheel; Whole-trace evaluation with per-step targeting; Embedding system state in traces and time-versioned queries
- Tools: Braintrust, Cursor, Claude Code, Codex

## [What if the network was the sandbox? — Remy Guercio, Tailscale](../videos/BM2JX9hqsVQ.md)
`BM2JX9hqsVQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: sandboxing-execution, security-guardrails, governance-compliance, observability

Tailscale's Remy Guercio argues the network layer can act as an agent sandbox: identity-tagged WireGuard connections let an LLM gateway hold the provider key so the sandbox never has one, and every model call and tool call is visible and cuttable there.

- Techniques: Zero-key sandbox behind an identity-aware gateway; Per-identity budgets and quotas across providers; Per-tool-call webhooks for external policy; Identity-aware internal services with tsnet; Policy as code for network identity
- Tools: Tailscale, WireGuard, Aperture, tsnet, Claude Code, Codex, Gemini CLI, GitHub Actions, Opus 4.6

## [Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson](../videos/mR-WAvEPRwE.md)
`mR-WAvEPRwE` · AI Engineer · 2026-06-18 · q4 · practitioner · workshop · topics: agent-architecture, multi-agent, claude-code, testing-verification

Two Anthropic Applied AI engineers explain how long-running agent harnesses evolved, and how a planner, generator and evaluator loop with rubric grading builds multi-hour apps that a single agent loop cannot finish.

- Techniques: Generator-evaluator loop with a live-app evaluator; Rubric-as-taste with calibrated examples; Sprint contracts negotiated in files; Thin planner that stays high level; Structured state on disk with JSON feature lists and progress files; Breadcrumb logs for later pickup; Read full traces, then tune prompts from them; Ralph-style stop-hook loop with exit criteria; Hooks for human check-ins; Split model roles for cost; Put the human-readable spec back into long sessions
- Tools: Claude Code, Claude Agent SDK, Playwright MCP, Chrome MCP, Claude Code skills, Claude Code sub-agents, Claude Code agent teams, Claude Code stop hooks, Claude Code auto mode, git, Puppeteer

## [From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google](../videos/-TiET_K-E_g.md)
`-TiET_K-E_g` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: training-finetuning-rl, local-ai, inference-serving, skills-self-improvement

Google's Cormac Brick on on-device agents: a prompt-based skill harness on Gemma 4, and fine-tuning FunctionGemma on synthetic data to lift function-calling success from about 46% to 90%+ on most functions.

- Techniques: Progressive skill disclosure; In-app JavaScript rendering from a skill; Coding agent writes the skills; Synthetic-data fine-tune for fixed function calling; Export and deploy pipeline for small models; Chained tiny models for a pipeline
- Tools: LiteRT-LM, LiteRT, MediaPipe, Gemma 4, FunctionGemma, Gemma 3, Gemini Nano, Android AICore, Gemini CLI, Gemini Flash, litert-torch, transformers

## [What the Best Agents Share — Mardu Swanepoel, Flinn AI](../videos/7CrPrHgoEYk.md)
`7CrPrHgoEYk` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: product-ux, coding-agents, context-engineering

Mardu Swanepoel (Flinn AI) on four UX patterns shared by strong agents: focus modes, transparent execution, personalization, and reversibility, illustrated with Cursor, Claude Cowork, Harvey and Manus.

- Techniques: Mode-scoped agent configuration; Plan-only mode; Hypothesis-driven debug mode; Visible execution trace; Playbook and memory personalization; Layered undo; Native host integration for review
- Tools: Cursor, Claude Cowork, Claude skills and connectors, Manus, Harvey, Microsoft Word API

## [What Breaks When You Build AI Under Sovereignty Constraints - Bilge Yücel, deepset GmbH](../videos/x2bH0RKPgdc.md)
`x2bH0RKPgdc` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: governance-compliance, security-guardrails, mcp-and-tools, observability

Bilge Yücel (deepset) on building AI under sovereignty constraints: four pillars, what breaks when you move from frontier APIs to self-hosted, and a guardrail-agent-guardrail reference design built on Haystack.

- Techniques: Sovereignty checklist as a design gate; Safe/unsafe router as an input guardrail; Per-agent tool allowlist plus BM25 tool search; Per-tool human confirmation strategies; Pipeline serialized to YAML for version control; Tracer component wrapping the pipeline
- Tools: Haystack, MCP, BM25, OpenTelemetry, YAML, Kubernetes, Mistral, Google models, Nvidia models, Jina

## [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](../videos/zMiSRliEzv4.md)
`zMiSRliEzv4` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: software-factory, agent-architecture, evals, observability

PostHog's Joshua Snyder describes a pipeline that turns product signals (errors, replays, Slack, experiments) into grouped reports, runs a Claude Agent SDK research agent in sandboxes, and opens PRs that are iterated until green.

- Techniques: Generate queries from a signal, then embed the queries; Safety classifier at the ingestion edge; Weighted report promotion with a threshold; Three-way actionability gate; Snapshot and rehydrate the sandbox for CI and review loops; Distill repeated agent behavior into a one-shot call; Evaluate on production-representative data
- Tools: Claude Agent SDK, Modal, MCP, Linear, Notion, Sentry, git blame, PostHog, feature flags

## [Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](../videos/c-2eEv2ou7Y.md)
`c-2eEv2ou7Y` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: mcp-and-tools, security-guardrails, product-ux

Frédéric Barthelet (Alpic) explains why ChatGPT and Claude render third-party MCP app UI in nested "double" iframes: CSP and origin isolation rule out simpler options, and the nesting is the workable compromise.

- Techniques: Double-iframe isolation for untrusted UI; Declare-then-enforce external domains; CSP inspection in dev tools
- Tools: MCP Apps extension, OpenAI Apps SDK, SkyBridge, HTML iframe (srcdoc, sandbox, allow-same-origin), Content Security Policy (frame-src, script-src, connect-src)

## [Prompt to Pipeline: Building with Google's Gen Media Stack — Paige & Guillaume, Google DeepMind](../videos/ns9f1fjLD7Y.md)
`ns9f1fjLD7Y` · AI Engineer · 2026-06-18 · q3 · practitioner · workshop · topics: models-research, voice-multimodal, vibe-coding-app-building, coding-agents

Google DeepMind's Paige and Guillaume, with Gemma's Ian Ballantyne, demo AI Studio, Gen Media models and local Gemma 4 agents. Mostly a live product tour, with some practical prompting and cost tips.

- Techniques: Playground-to-code export; Code execution for verified counting and drawing; Per-scene reference injection for character consistency; Structured outputs as a prompt-writing stage; Prompt-level multi-voice TTS; Flex and priority service tiers; Local orchestrator with parallel subagents on an OpenAI-compatible server; Vibe-coding guardrails: one file per feature, plus logging
- Tools: Google AI Studio, Gemini API, Gemini Live, Google Build (AI Studio), Firestore, Google Search grounding, Antigravity, Nano Banana 2, Veo 3.1 Lite, Lyria 3, Lyria RealTime, Genie 3 / Project Genie

## [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](../videos/btxGmN8RvNU.md)
`btxGmN8RvNU` · AI Engineer · 2026-06-18 · q2 · intro · review · topics: mcp-and-tools, rag-retrieval, data-engineering

Bright Data pitch: blocked web access makes LLM agents fabricate answers silently. Its MCP (search, markdown scrape, CAPTCHA-solving browser) fixed a 5-site demo, but the evidence is one unreplicated run.

- Techniques: Paired with/without-tools comparison; Load a narrow subset of MCP tools; Scrape to markdown instead of HTML; Batch search across many keywords; LLM writes the parser, script does the extraction; Human-like remote browser instead of detection evasion; Restrict agents to public, non-login data; Pre-collected datasets for non-live needs
- Tools: Bright Data MCP (66 tools per speaker; 69 mentioned later), Bright Data scraping browser (remote, fingerprinted, CAPTCHA solving), Bright Data skills page, Bright Data datasets, GPT-5 (tested without tools as baseline), ChatGPT (cited for broken citations), Google, Bing and DuckDuckGo search (via MCP), Cloudflare bot blocking and AI Labyrinth (cited, not used), VS Code (demo environment)

## [Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod](../videos/ILdE7FaAjVA.md)
`ILdE7FaAjVA` · AI Engineer · 2026-06-18 · q2 · intro · demo · topics: inference-serving, infra-cost-scaling

RunPod's intro walkthrough of deploying an open LLM (Qwen via vLLM) as a serverless GPU endpoint from its Hub in under five minutes; mostly a product pitch, with a useful look at cold starts and autoscaling settings.

- Techniques: Serverless GPU autoscaling with warm workers; Deploy a model from a pre-vetted Hub listing; Cold-start awareness in latency budgets
- Tools: RunPod, vLLM, Hugging Face, Docker

## [From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](../videos/Bc6Ojl2XS1w.md)
`Bc6Ojl2XS1w` · AI Engineer · 2026-06-18 · q2 · intro · demo · topics: voice-multimodal, data-engineering, models-research

Google DeepMind's Thor Schaeff tours Gemini's audio stack: one-call structured audio extraction, director's-note TTS, a native speech-to-speech Live model, and a live tool call to Lyria music generation.

- Techniques: Single-call structured audio extraction; Director's-note TTS prompting; Realtime model with a generation tool; System-instruction persona on a live audio model; Install vendor API skills into coding agents
- Tools: Gemini API, Google AI Studio, Gemini 3 Flash Preview, Gemini 3.1 Flash Live, Gemini Live API (WebSocket), Lyria 3 / Lyria 3 Pro, Gemma 4, Veo 3.1 Lite, Gemini coding-agent skills

## [Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry](../videos/ugUeZ8-b-u0.md)
`ugUeZ8-b-u0` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: coding-agents, testing-verification, dev-tools

Argues Rust's strict compiler suits agent-written code better than Python or TypeScript: compile-time checks rule out bug classes that tests and LLM review miss, and compiler errors give agents concrete fix signals. Sponsored by Sentry.

- Techniques: Compile-in-the-loop repair; Deterministic checks before LLM review; Use error messages that name the concrete type; Choose a language by how strongly its checker constrains output; Write tests first when an agent writes tests
- Tools: Rust, rustc (Rust compiler), TypeScript, Python, Sentry

## [Does GenAI "belong" to data scientists? — Phil Hetzel, Braintrust](../videos/NKwIX3CiRgU.md)
`NKwIX3CiRgU` · AI Engineer · 2026-06-18 · q2 · intro · talk · topics: enterprise-adoption, evals, product-ux

Phil Hetzel (Braintrust) argues GenAI agent work should not belong only to data scientists or ML engineers. He says it needs a diverse product team, with domain experts shaping prompts and eval, and data scientists supplying rigorous eval discipline.

- Techniques: Judge calibration against human labels; Production traces feed the offline eval set; Domain-expert trace annotation; Prompt playground for non-engineers; Functional eval over technical metrics
- Tools: Braintrust

## [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](../videos/SKDJo2CopRs.md)
`SKDJo2CopRs` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: sandboxing-execution, agent-architecture, mcp-and-tools, infra-cost-scaling

Two Cloudflare engineers tour Durable Objects, dynamic workers and code mode as a stateful, sandboxed runtime for agents. Mostly product pitch, with a few reusable architecture ideas.

- Techniques: One Durable Object per entity ID as the session or agent; Resumable stream held by the agent object; Deny-by-default capability sandbox for generated code; Code mode for large API surfaces; Scheduled work inside the agent class; Plugins as isolated dynamic workers
- Tools: Cloudflare Durable Objects, Cloudflare Workers, Cloudflare Dynamic Workers, Cloudflare Agents SDK, Vercel AI SDK, MCP, Cloudflare Sandbox SDK, Daytona, SQLite, R2, Zig (via Wasm), Next.js on Workers

## [Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum](../videos/WRBNDpUhsJQ.md)
`WRBNDpUhsJQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: multi-agent, token-cost-efficiency, inference-serving

Adrian Bertagnoli (Callosum) argues AI is moving from homogeneous scaling to heterogeneous multi-agent systems mixing models, workflows and chips, and shows a recursive-LM variant that routes sub-contexts to different models and hardware for big cost and speed gains.

- Techniques: Heterogeneous recursion; Subtask offloading to small models; Automated model and hardware routing; Hardware-matched inference for sub-calls
- Tools: Python REPL, Cerebras, Kimi K2.5, GPT-5.2, Gemini 2.5, Qwen3-VL-8B-Instruct, Stamanova

## [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../videos/N7b1PJc7SFc.md)
`N7b1PJc7SFc` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: voice-multimodal, infra-cost-scaling, evals, agent-architecture

Together AI's voice AI lead on the cascading STT→LLM→TTS pipeline: per-stage latency budgets, streaming STT, co-locating models to cut network hops, and why speech-to-speech is not yet production-ready.

- Techniques: Cascading voice pipeline with streamed hand-offs; Per-stage latency budget; Streaming STT with lookahead-limited encoders; Co-locate models with the orchestrator; Asymmetric autoscaling for stateful voice; Pre- and post-LLM guardrail and routing stages; Thinker-talker delegation; Tiered tool-call evals; Full-duplex conversation evals
- Tools: Together AI (hosted inference, the speaker's company), Pipecat (agent orchestrator, named as an example), LiveKit (agent orchestrator, named as an example), Whisper (OpenAI speech-to-text, cited as the batch model), NVIDIA streaming speech encoder (named only as a recent NVIDIA model), NVIDIA VoiceChat (speech-to-speech model), OpenAI realtime API (speech-to-speech), ChatGPT advanced voice mode, Claude Code and Cursor (cited as voice-interaction examples)

## [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](../videos/QuuIywMG4s8.md)
`QuuIywMG4s8` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: evals, testing-verification, coding-agents

Ara Khan (Cline) argues most people misuse evals, either trusting vendor leaderboards or dismissing evals for vibes, and shows how to build a Terminal-Bench-style agent eval and hill-climb on it alongside a vibe check.

- Techniques: Failure-trace triage loop; Isolated parallel eval runs; Hill-climb with a vibe check; Sort fixes into three zones; Delayed model adoption; Check the task itself
- Tools: Terminal-Bench, Harbor, SWE-bench Verified, Claude Code, Codex, Daytona, Docker, Modal

## [Bounded Autonomy: Between Free Will and Determinism — Angus J. McLean, Oliver](../videos/t4359sKBu4w.md)
`t4359sKBu4w` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: context-engineering, agent-architecture, enterprise-adoption

An ad-agency AI director argues for "bounded autonomy": treat LLM context as a soft constraint, keep systems simple, store knowledge in several representations, and never automate work you cannot do yourself.

- Techniques: Self-imposed context budget; Curated documentation over open web access; Simple-first prototype with fast reality checks; Multi-representation knowledge storage; Cluster-then-report pipeline; Teach yourself on older, smaller models and your own harness; Automate only what you can do yourself

## [Stop babysitting your agents... — Brandon Waselnuk, Unblocked](../videos/BiG2ssibKGc.md)
`BiG2ssibKGc` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: context-engineering, memory, rag-retrieval

Unblocked's Brandon Waselnuk argues agents need a runtime context engine, not more MCP access or static docs: exhaustive retrieval, surfaced conflicts, a social graph, and hard-won lessons.

- Techniques: Exhaustive retrieval before first-hit answers; Research packet before planning; Expert / social graph built from the code repo; Surface conflicts instead of silently picking; Permission-preserving delivery over MCP; Confidence-gated auto-answering; No answer caching for latency
- Tools: Claude Code, MCP, Codex, Anthropic API, AWS Bedrock, CLAUDE.md, AGENTS.md, Zendesk, Slack, Microsoft Teams

## [Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs](../videos/V-L0INGTEOg.md)
`V-L0INGTEOg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: claude-code, coding-agents, skills-self-improvement

Boris Starkov (ElevenLabs) shows how Claude Code reverse-engineered an undocumented 1990s-style VoIP phone's protocol through port probing, command brute-force, and a traffic-capture proxy, then packaged the result as a reusable skill.

- Techniques: Black-box command sweep with error classification; Intermediary proxy for vendor-client traffic capture; Closed-loop hypothesis confirmation; Persisting a learned protocol as a skill; Using the full session transcript as context to generate a deliverable; Human as actuator for physical steps
- Tools: Claude Code, Twilio (SIP trunk), ElevenLabs conversational agents, Windows virtual machine, TCP proxy on macOS, PoE router

## [The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry](../videos/li0SaBt9RDM.md)
`li0SaBt9RDM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: claude-code, skills-self-improvement, coding-agents

Sentry engineer Priscila Andre de Oliveira on using AI mainly for codebase comprehension: she mined her own sessions, found 67% were comprehension and 2% generation, and built a reusable "Catch Me Up" skill.

- Techniques: Session-log classification audit; Repeated prompt to personal skill; Onboarding via a 'new contributor' framing; Comprehension pass before PR review; Research, then comprehension check, then plan, then implement; Codebase hygiene sprint for agent legibility
- Tools: Claude Code, Claude Opus, Catch Me Up (personal skill), Warden (Sentry code review agent), Junior (Sentry Slack bot that turns threads into PRs), Abacus (Sentry internal AI usage tracker)

## [Any-to-Any: Building Native Multimodal Agents - Patrick Löber, Google DeepMind](../videos/GIRpQEfYf3U.md)
`GIRpQEfYf3U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: voice-multimodal, agent-architecture, mcp-and-tools

Google DeepMind's Patrick Löber walks through building a NotebookLM-style agent: Gemini reasons, calls native image and speech generators via function calling, and uses multimodal input and a live audio model.

- Techniques: Agentic generation loop with function-declared generators; Single-call multimodal synthesis; Timestamp-windowed media analysis; Context caching for repeated queries; Scaffold with a Gemini API skill; Audio-to-audio live session for voice
- Tools: Google Gen AI SDK, Gemini API, Google AI Studio, Gemini 3 Flash, Gemini 3.5 Flash Image preview (Nano Banana 2), Gemini 2.5 text-to-speech, Gemini 3.1 Flash Live, File API, Gemma 4, Gemini API skill

## [The Missing Primitive for Agent Swarms — Lou Bichard, Ona](../videos/5Sui_OnSRlY.md)
`5Sui_OnSRlY` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: multi-agent, software-factory, sandboxing-execution, agent-architecture

Ona's field CTO argues that runtimes, orchestration and triggers are largely solved for coding-agent swarms, and that agent coordination is the missing primitive. He proposes state-machine workflows packaged as a CLI that runs locally and in CI.

- Techniques: Parent-child sub-agents with scoped context; Two-tier sub-agent placement; Fleet fan-out with prompts and scripts as a workflow; Harness engineering loop; Gated micro-step workflow (state machine); CLI-packaged workflow gate
- Tools: Ona dev environments, GitHub, Linear, Symphony, ACP, ACPX, Fabro, n8n-style graph workflows, backgroundagents.com

## [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../videos/gHs5ZiY80PM.md)
`gHs5ZiY80PM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: inference-serving, training-finetuning-rl, voice-multimodal

NVIDIA's Ziv Ilan on making diffusion image and video models fast enough for real use: quantization, step caching and step distillation, stacked incrementally, with distillation as the biggest win.

- Techniques: Post-training quantization with dynamic ranges for diffusion; Step caching (TeaCache-style and chunk-based); Trajectory vs distribution step distillation; Incremental optimization ladder
- Tools: TensorRT-LLM Visual Gen, FastGen, vLLM-Omni, SGLang Diffusion, TeaCache, Blackwell GPUs (B200), Hugging Face checkpoints

## [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](../videos/NuePCNMpWGc.md)
`NuePCNMpWGc` · AI Engineer · 2026-06-18 · q2 · practitioner · talk · topics: pr-code-review, evals, coding-agents, testing-verification

Sonar argues that LLM pass rates miss security, maintainability and verbosity. It shows its Java eval of 53+ models and pitches a verify-in-loop and remediation pipeline, so it is product-heavy.

- Techniques: Dual-metric model evaluation; In-loop static analysis via MCP; Regression-gated autofix; One PR per issue for tech debt; Remediation on quality-gate failure
- Tools: SonarQube, SonarQube Agentic Analysis (MCP), Sonar Sweep, Sonar Context Augmentation, Sonar remediation agent, Claude Code, Codex, Gemini CLI, Devin, Cursor, Windsurf, Antigravity

## [Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo](../videos/EcqMYoIV57A.md)
`EcqMYoIV57A` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: context-engineering, multi-agent, pr-code-review

Qodo's Nupur Sharma argues that dumping more context into an agent makes results worse, and shows how selecting, splitting and judging context across specialist agents fixed this in their PR review system.

- Techniques: Context selection instead of context dumping; Iterative retrieval with a library-card index; Hierarchical summarization; Knowledge graph for dependencies; 80/20 research and gate split; Specialist agents with a judge agent; Feedback-weighted calibration
- Tools: Jira, MCP, Claude Opus

## [BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence](../videos/504PvfXou5Y.md)
`504PvfXou5Y` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: context-engineering, testing-verification, pr-code-review

Michal Cichra on keeping agents and humans aligned by storing ADRs, PRDs and executable BDD specs in the repo, then enforcing them through git hooks, CI and import-boundary lints.

- Techniques: ADR with enforcing lint rule; Import-boundary restriction to eliminate bug classes; Executable BDD scenarios linked to PRDs; Shared checks in git hooks and CI; Design system as enforced rules and previews; Scoped test selection per task
- Tools: Cucumber, git hooks, CI, linters, type checkers, architecture import lint, Markdown docs

## [LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](../videos/JsCCrBF7F1g.md)
`JsCCrBF7F1g` · AI Engineer · 2026-06-18 · q2 · practitioner · talk · topics: observability, evals, agent-architecture

Arize's Dat Ngo argues LLM observability, evals and experiments form one flywheel, built on OpenTelemetry traces, with evals scoped from single spans up to whole sessions. It is mostly a product walkthrough with a useful eval taxonomy.

- Techniques: OTel auto-instrumentation for agents; Session-level state tracking; Distributional trajectory analysis; Eval at the smallest scope that answers the question; Deterministic checks before LLM judges; Calibrate an LLM judge against a golden dataset; Trace-to-dataset-to-experiment loop; Coding-agent access to the eval platform
- Tools: Arize Phoenix, Arize AX, OpenTelemetry, LLM-as-judge, Claude Code, Codex, Anthropic Managed Agents (mentioned)

## [How to talk to statues — Joe Reeve, ElevenLabs](../videos/u-rJwPPU3QA.md)
`u-rJwPPU3QA` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: voice-multimodal, product-ux, vibe-coding-app-building

ElevenLabs growth lead on the viral "Statue" app, built in two hours, and on voice-agent UX. Main points: glue code and storytelling matter most, and voice agents need visual co-presence and interruptible, editable transcripts.

- Techniques: Research-to-persona-to-agent chain; Thin glue layer on managed APIs; Playback-position transcript truncation for barge-in; Visual side panel for voice conversations; Hook-first short video with late music
- Tools: ElevenLabs Agents, ElevenLabs Voice Design API, ElevenLabs music generation, OpenAI deep research, Cursor, Supabase, Facebook Instant Games API (deprecated), CapCut, Claude app voice UI, OpenClaw

## [Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl](../videos/W-SX_srBa3Y.md)
`W-SX_srBa3Y` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · topics: coding-agents, multi-agent, agent-architecture

Bitly engineer Michael Richman presents Command & Control, his tool for monitoring and answering coding agents from a phone, web or watch, and frames the idle-agent problem as FOMAT.

- Techniques: Per-platform lifecycle daemon feeding a control plane; Tiered notification and watch lists; Overview summaries from the last few messages; Start remotely, resume locally on the same session
- Tools: Command & Control (Cmd+Ctrl, speaker's own tool), Claude Code (captioned as Cloud Code), Codex / Codex CLI, Gemini (CLI), Cursor (IDE), GitHub Copilot, OpenCode, Anthropic remote control and teleportation (Claude Code features, mentioned), Bitly MCP server (co-written by speaker, mentioned), Agent Craft (gaming-based agent tool, mentioned as seen earlier that morning)

## [What Lies Beneath the API — Benjamin Cowen, Modal](../videos/HvZXAOZ3iv8.md)
`HvZXAOZ3iv8` · AI Engineer · 2026-06-18 · q2 · intro · talk · topics: training-finetuning-rl, inference-serving, infra-cost-scaling

Modal forward-deployed engineer argues that once a product is differentiated, fine-tuning becomes worth it, and that serverless compute and open-source libraries now make it accessible without a cluster team. Sales-leaning, with a few concrete signals and code-size claims.

- Techniques: Signal-based fine-tuning decision; Harness outcomes as RL training data; Parallel hyperparameter sweep with early kill; Sandbox-fanned RL rollouts; Autoscaled serving of custom models
- Tools: Modal, vLLM, SGLang, Triton Inference Server, Python

## [How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust](../videos/XBaznoTRDFI.md)
`XBaznoTRDFI` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: observability, evals, data-engineering

Braintrust's solutions lead argues agent observability differs from uptime-focused tracing: quality, non-determinism, huge text-heavy traces, and domain experts in the loop.

- Techniques: Split quality metrics from technical metrics; Full-text index on traces with SQL access; Trace to offline dataset to experiment; Human grades with justification to LLM judges; Embed and cluster traces to find unknown unknowns
- Tools: Braintrust, Grafana, Datadog, ClickHouse, Tantivy, Apache Lucene, SQL, CLI

## [Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j](../videos/B9h9ovW5H9U.md)
`B9h9ovW5H9U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: memory, rag-retrieval, context-engineering, data-engineering

Neo4j's Zach Blumenfeld on context graphs: why agents need stored decision traces and precedents, not just documents, plus a one-line scaffold (create-context-graph) and the Neo4j agent memory pipeline.

- Techniques: Hybrid precedent retrieval over decision traces; Scaffold a context-graph app from a domain; Staged entity extraction from text into a graph; Ontology-first graph schema generation; Separate memory stores by kind
- Tools: Neo4j, Neo4j agent memory package, Graph Data Science (GDS), Cypher, uvx create-context-graph, Pydantic AI, Claude, OpenAI embeddings, Next.js, spaCy, GLiNER, MCP

## [Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline](../videos/yUmS-F9IX90.md)
`yUmS-F9IX90` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: agent-architecture, coding-agents, context-engineering, software-factory

Ara Khan (Cline) argues for four maturity levels of agent building: framework, hand-built state machine, Kanban as the UX, and cloud execution. Core warnings: keep prompts minimal, keep agents CLI-testable, and keep architecture human-owned.

- Techniques: Agent as explicit state machine; Prune the system prompt on every change; CLI-first agent interface for agent-driven development; Exact reasoning-trace round-tripping; Kanban board as the multi-agent control surface; Per-task cloud agent dispatch; Human-owned architecture before code generation
- Tools: Claude Code, Codex, Cursor, Factory, Cline, LangChain, LangGraph, OpenRouter, Linear, AGENTS.md, VS Code

## [From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](../videos/zTZ0qunQXnM.md)
`zTZ0qunQXnM` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · topics: data-engineering, coding-agents, mcp-and-tools, voice-multimodal

A Bright Data vendor demo arguing LLMs should write a reusable scraper once instead of parsing every page, then run and self-repair it on a schedule. Useful pattern, heavy product pitch.

- Techniques: Generate-then-run scraper; Scheduled self-repairing collection loop; Tiered fetch format; Remote browser with human-like input for multi-step flows; Public-data-only policy check
- Tools: Claude Code, Codex, Bright Data MCP, Bright Data scrape-as-markdown, Bright Data Web Unlocker API, Bright Data remote browsers, Bright Data skill docs on GitHub, Haiku

## [Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw](../videos/VaS2h-dY1-4.md)
`VaS2h-dY1-4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: multi-agent, mcp-and-tools, sandboxing-execution, pr-code-review

An OpenClaw maintainer shows acpx, a CLI and workflow engine over the Agent Client Protocol (ACP), used to automate PR triage and to run disposable per-task agents on Kubernetes.

- Techniques: ACP as the client-side adapter layer; Channel-bound agent sessions; Hybrid PR-triage workflow with JSON handoffs; Shallow-fix loop with a human escalation gate; Feedback bin for PR outcomes; Per-task disposable agent pods via a Kubernetes operator
- Tools: acpx, ACP (Agent Client Protocol), Codex, Claude Code, Zed, Discord, Slack, MS Teams, Kubernetes, Helm, Go operator, rsync

## [Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture](../videos/AGkzpxMdPn8.md)
`AGkzpxMdPn8` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: enterprise-adoption, governance-compliance, product-ux

Accenture talk on why enterprise agentic projects stall: human-speed governance, business cases, and trust. Argues for hypothesis-driven delivery, portfolio funding, progressive autonomy, and feedback loops as the moat.

- Techniques: Exposure ladder for agent rollout; Approval-as-code; Hypothesis-driven agent delivery; Portfolio funding for AI bets; Kill switches and hard limits on autonomous actions; Instrument every feature as a feedback source

## [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](../videos/_B4Pv9ttFgY.md)
`_B4Pv9ttFgY` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: mcp-and-tools, product-ux, security-guardrails

Four engineering lessons from the Chrome DevTools MCP team on designing agent-facing interfaces: token cost, error recovery, tool discoverability, and trust boundaries.

- Techniques: Semantic summaries instead of raw tool output; Tokens per successful outcome; Tool categorization and slim mode; CLI with piping for local post-processing; Self-healing error messages; Proactive detours; Tool descriptions as UI for the agent; Trust tiers with deliberate consent friction
- Tools: Chrome DevTools MCP server, Gemini CLI, Claude Code, Codex, OpenClaw

## [Gemini Nano on device — Florina Muntenescu & Oli Gaymond, Google DeepMind](../videos/owH1f0N-keY.md)
`owH1f0N-keY` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · topics: inference-serving, local-ai, product-ux

Google DeepMind's Android team on using Gemini Nano on-device via ML Kit GenAI and Firebase hybrid fallback, with Q&A on battery, shared-model scheduling and device reach.

- Techniques: Runtime hybrid routing with cloud fallback; Use the ML Kit GenAI Prompt API for on-device structured tasks; Offload non-urgent batch work to background, charging-time windows; Prompt-stuffed retrieval as a stopgap RAG; Device testing and profiling for custom models
- Tools: Gemini Nano, AICore, ML Kit GenAI APIs, Prompt API, Firebase AI Logic, LiteRT-LM, AI Edge Gallery, Gemma 4

## [How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS](../videos/vy7o1g2iHY8.md)
`vy7o1g2iHY8` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · topics: skills-self-improvement, testing-verification, agent-architecture, evals

WorkOS DX engineer on replacing 10k lines of generated agent skills with 553 lines of gotchas, enforcing gates in a state machine, and making agents prove their work with hashes and videos.

- Techniques: Enforced state-machine gates for agent pipelines; Hash-verified test receipts; Gotchas-only skills validated by paired evals; Visual before-and-after proof on PRs; Retrospective agent over run transcripts; Conditional rules instead of doc summaries
- Tools: Pi, Claude Code, Codex, Playwright CLI, TypeScript, SHA-256, WorkOS CLI, AuthKit, TanStack Start, Next.js, GitHub, Linear

## [Rewiring the State — Eoin Mulgrew, No. 10 (Downing Street)](../videos/ObNKGf9YR0g.md)
`ObNKGf9YR0g` · AI Engineer · 2026-06-18 · q3 · intro · talk · topics: enterprise-adoption, governance-compliance, product-ux, evals

Eoin Mulgrew of No. 10's data science team describes an outsider "insurgency" unit with forward-deployed engineers that ships small government AI tools in weeks; mostly a recruitment pitch.

- Techniques: Insurgency unit with a mandate; Forward-deployed engineers embedded in workflows; Internal tool instead of outsourced one-off analysis; Policy simulation sandbox; Pre-deployment sycophancy red-teaming and user coaching; Benchmark-based guardrails for classroom AI
- Tools: Gemini, Inspect (AI Safety Institute evaluation tool), Xtract (planning-application digitisation)

## [The End of Apps — Kitze, Sizzy.co](../videos/4fntwuOoedA.md)
`4fntwuOoedA` · AI Engineer · 2026-05-18 · q2 · intro · talk · topics: agent-architecture, product-ux, multi-agent, memory

Kitze (Sizzy.co) on his personal-agent journey, from to-do apps to OpenClaw-style agents, and his view that apps will give way to a personal agent OS that prompts the user.

- Techniques: Nested topic description injection; Per-topic specialized agents; Labeled cron messages with full conversation context; Visible tool-call UI
- Tools: OpenClaw, Hermes, Paperclip, Codex, Claude Code, Claude Cowork, Tmux, Telegram, Discord, Tasker, IFTTT, Notion

## [How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom](../videos/4_VQBbs2iQA.md)
`4_VQBbs2iQA` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: claude-code, enterprise-adoption, skills-self-improvement, pr-code-review

Intercom's platform lead explains how they set a goal to double engineering throughput by standardizing on Claude Code, backed by skills, hooks, calibrated auto-approval and telemetry.

- Techniques: Single-platform standardization with internal plugin distribution; Guidance flywheel; Problem-first prompting; Backtested skill authoring; Calibrated automatic approval; Agent telemetry and transcript mining
- Tools: Claude Code, GitHub Copilot, Cursor, Augment, Honeycomb, S3, DX, Ruby on Rails, React, GitHub

## [Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face](../videos/OV56RddyFuU.md)
`OV56RddyFuU` · AI Engineer · 2026-05-18 · q2 · practitioner · demo · topics: local-ai, training-finetuning-rl, mcp-and-tools, coding-agents

Hugging Face's Merve Noyan demos open-model agent workflows: picking and serving open models, Hermes Agent, pushing agent traces to the Hub, HF MCP server and skills that let coding agents launch fine-tuning and batch OCR jobs.

- Techniques: Hub-ID local serving for coding agents; GGUF hardware-fit check before download; Agent-driven fine-tuning via skills; Session traces pushed to a Hub dataset; Corpus OCR via prompted batch job; HF MCP server for catalog access
- Tools: Hugging Face Hub, Hugging Face MCP server, Hugging Face skills (hub CLI, LLM trainer, Gradio, dataset), Inference Providers, Hermes Agent, Pi, llama.cpp, vLLM, MLX, LM Studio, Claude Code, Codex

## [How we solved Context Management in Agents — Sally-Ann Delucia](../videos/esY99nYXxR4.md)
`esY99nYXxR4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: context-engineering, memory, multi-agent, evals

Arize's product head explains how their Alex agent escaped a context-growth loop: head/tail truncation with the middle moved to memory, long-session evals, and sub-agents for heavy data search.

- Techniques: Head + tail truncation with middle spill to memory; Reference-by-ID retrieval tool; Long-session eval (seed N turns, test turn N+1); Sub-agent for data-heavy search
- Tools: Alex (Arize's in-product agent), Arize observability platform, Claude Code (referenced, not used by speaker)

## [Why MLX — Prince Canuma, Neywa Labs](../videos/zTLJNHj0DeQ.md)
`zTLJNHj0DeQ` · AI Engineer · 2026-05-18 · q3 · intro · talk · topics: local-ai, inference-serving, voice-multimodal

Prince Canuma argues for running agents, voice, and vision models fully on Apple Silicon with MLX to cut cloud subscription costs and work offline. Demos are mixed, and the talk ends with a TurboQuant KV-cache claim.

- Techniques: Modular speech pipeline; Chained short-clip video generation; Grounded visual reasoning on video; Storage-backed model loading on phones; TurboQuant-style KV-cache quantization; Live GPU monitoring during inference
- Tools: MLX, MLX-VLM, MLX-Audio, Marvis TTS, RF-DETR, Gemma 4, Qwen3-Omni, Core ML, Gradio, MacTop, Reachy Mini, LM Studio

## [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](../videos/Wmp2Tku2PrI.md)
`Wmp2Tku2PrI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: context-engineering, coding-agents, testing-verification, agent-architecture

Michael Arnaldi builds a TypeScript Effect HTTP to-do API from an empty repo, arguing agents need the real source repo, strict lint back pressure, and generated pattern docs.

- Techniques: Clone the library source into the repo; Strict diagnostics plus lint as back pressure; AGENTS.md as a living rulebook; Spec file plus Ralph-style loop; Self-selected pattern docs; Single execute tool instead of many tools; Per-test rollback transactions for DB tests; Test layers with it.layer; Lint reference checks in CI for pattern docs
- Tools: Effect v4 (beta), Effect SQL with SQLite, Bun, Vitest, TypeScript native preview (tsgo), ESLint, OpenCode, GPT-5.4, Claude Opus, Codex, Cursor, Temporal

## [Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw](../videos/4VhbYlfC7Gs.md)
`4VhbYlfC7Gs` · AI Engineer · 2026-05-18 · q3 · intro · talk · topics: evals, agent-architecture, observability

Vincent Koc (Comet, OpenClaw) argues static, hand-written evals don't fit adaptive agents; he proposes intent-based, always-on evals self-curated from traces, with the eval suite treated as living code.

- Techniques: Intent-defined end-state evals; Trace-driven suite self-curation; Always-on eval service; Telemetry-aware harness; Split static and dynamic evals
- Tools: Comet, OpenClaw, Claude, Codex, MCP, Karpathy autoresearch

## [Human-in-the-Loop Automation with n8n — Liam McGarrigle](../videos/tDArkCqjA-c.md)
`tDArkCqjA-c` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · topics: security-guardrails, agent-architecture, mcp-and-tools, context-engineering

Workshop on building a Gmail and Google Calendar agent in n8n, then gating sensitive tool calls behind human approval steps that the model cannot skip.

- Techniques: Approval gate in front of sensitive tools; Free-text decline as feedback; Dry runs with dummy data before real accounts; Rules in tool descriptions, not one system prompt; Per-field descriptions for argument mistakes; Wait with an auto-deny timeout; Confirm sub-workflow as a tool; Sub-agent per domain as a tool; Date and time injection via expression; Memory window sizing
- Tools: n8n, OpenRouter, Gmail, Google Calendar, Slack, Notion, Postgres, Redis, Claude, Claude Code, Luxon, Swagger

## [Shipping complex AI applications — Braintrust & Trainline](../videos/ZdheJTfLu-s.md)
`ZdheJTfLu-s` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · topics: evals, observability, agent-architecture

Hands-on Braintrust and Trainline workshop on taking a multi-stage LLM support-triage agent from one prompt to a traced, evaluated, managed and failure-driven production loop.

- Techniques: Staged agent pipeline with a deterministic front end; Nested tracing per user interaction; Golden set from categorized edge cases; Two-tier scoring; Evaluate before swapping models; Failure-to-fix loop; Prompts and scorers as managed, slugged assets
- Tools: Braintrust, OpenAI SDK, OpenAI mini model (speaker says 'mini'), TypeScript, pnpm, make, Node 22, Cursor / Codex (suggested for setup)

## [Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind](../videos/_gVFUEdhCyI.md)
`_gVFUEdhCyI` · AI Engineer · 2026-05-18 · q2 · intro · talk · topics: models-research, local-ai, inference-serving

Google DeepMind's Omar Sanseviero introduces Gemma 4, a family of open models from 2B to 32B parameters, and argues that small open models can now do multimodal and agentic work on-device.

- Techniques: Offload per-layer embeddings to CPU or disk; Parallel local generation on one machine; Pick the model by tokenizer for low-resource language fine-tuning; Stay on the framework the team already uses
- Tools: Gemma 4, llama.cpp, MLX, Ollama, Hugging Face Transformers, vLLM, SGLang, Keras, Android Studio, ShieldGemma, MedGemma, LM Arena

## [Connecting the Dots with Context Graphs — Stephen Chin, Neo4j](../videos/eW_vxrjvERk.md)
`eW_vxrjvERk` · AI Engineer · 2026-05-18 · q2 · intro · talk · topics: memory, rag-retrieval, mcp-and-tools

Neo4j DevRel lead argues agents need a knowledge graph that stores short-term, long-term and reasoning memory together, so decisions can be explained and reused. Mostly a product pitch with one finance demo.

- Techniques: Three-tier memory in one graph; Vector entry point then graph traversal; Decision write-back to the graph; LLM-generated Cypher with visible query trace; Multi-source ingestion through MCP tools into a graph
- Tools: Neo4j, Neo4j Agent Memory package (open source), Cypher, OpenAI embeddings, FastRP, Leiden algorithm, MCP, Next.js, Neo4j Aura (free tier), Graph Academy

## [Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take](../videos/FlzpEGHNVKQ.md)
`FlzpEGHNVKQ` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: evals, context-engineering, mcp-and-tools

How a consumer chess app grounds LLM game commentary in Stockfish and detectors, hits a sub-3s latency target, and closes a feedback loop where a Claude Code agent triages bad comments and opens PRs.

- Techniques: Deterministic analysis then LLM narration; Scenario-based LLM-as-judge regression set; Channel-injected events into a running coding agent; Latency-first model selection for interactive output; Iterative context pruning
- Tools: Stockfish, Maia (human-move prediction model), Gemini 3 Flash, Claude Code, Claude Code Channels, GPT-5 Mini, OpenRouter, Slack, GitHub

## [Agents Don't Do Standups: Building the Post-Engineer Engineering Org — Mike Spitz, PFF](../videos/VMemhtlsoNk.md)
`VMemhtlsoNk` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: software-factory, enterprise-adoption, testing-verification, context-engineering

Mike Spitz (PFF) reports a Jan–Mar 2026 case study where agent-driven spec, design doc, ticket and PR flow cut delivery time and dropped Scrum for a 20-engineer team.

- Techniques: Agent-interviewed spec then skill-generated LDD; Auto-generated, non-blocking tickets and PR-driven status; Agent code review limited to opinion-level nits; Post-staging QA agent against acceptance criteria; Composable per-step skills for the delivery lifecycle; Customer survey as the primary retro signal; Phased, non-critical-first rollout
- Tools: Claude Code, Claude Opus, Codex

## [Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop](../videos/-aM2EDTiaMs.md)
`-aM2EDTiaMs` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: observability, evals, agent-architecture, coding-agents

Raindrop's founders argue production agent monitoring must replace evals as the main safety net, using implicit classifier signals, regex, ship-vs-control experiments, and agent self-diagnostic reports.

- Techniques: Binary issue classifiers as monitoring signals; Regex keyword signals on user messages; Percentage rollout with a control group, judged by signal rates; Self-diagnostic report tool; Natural-language signal definition (deep search); Daily triage agent over signals; Cluster by user intent and track issue rate per cluster; Trajectory search over tool-call sequences
- Tools: Raindrop, OpenTelemetry, Claude Code, Codex, OpenAI API, Sentry, Slack, BigQuery, Snowflake, Statsig

## [Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI](../videos/P_RI1kCkRbo.md)
`P_RI1kCkRbo` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: voice-multimodal, infra-cost-scaling, models-research

Gradium's CEO argues voice AI is not yet at the "Her" moment: cascaded pipelines hit latency limits, full-duplex speech models lack reliability and tools, and TTS cost dominates. He pitches on-device TTS as the fix.

- Techniques: Filler speech while a tool call runs; Stress-test full-duplex and interruption behaviour; On-device TTS for cost and privacy; Keep the cascade as the default for reliable agents
- Tools: Moshi, Gradium Phonon, NVIDIA PersonaPlex, Kokoro, ElevenLabs, OpenRouter

## [MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps](../videos/o-zkvb0iFDQ.md)
`o-zkvb0iFDQ` · AI Engineer · 2026-05-18 · q3 · intro · talk · topics: mcp-and-tools, product-ux

MCP Apps lets an MCP tool return an interactive UI that the host renders in a sandbox, with UI events routed back through the host so vendors keep their branding and the host keeps conversation context.

- Techniques: Tool returns a UI resource; Route UI events through the host; Choose the message type by how much control you need; Sandboxed host renderer; Pick a UI generation mode per host; Build with the official SDK and skills
- Tools: MCP Apps, MCP-UI, Claude, ChatGPT, VS Code, Cursor, GitHub Copilot, PostHog, Shopify, Hugging Face, Booking, Airbnb

## [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](../videos/ow1we5PzK-o.md)
`ow1we5PzK-o` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: multi-agent, agent-architecture, software-factory, testing-verification

Luke Alvoeiro (Factory) on "Missions", a multi-agent system that runs for hours or days by combining delegation, creator/verifier, broadcast and negotiation, with a validation contract written before any code.

- Techniques: Validation contract written at planning time; Fresh-context adversarial validators; Structured worker handoffs; Serial features with read-only parallelism; Per-role model choice; Milestone-based negotiation; Orchestration as prompts and skills
- Tools: Factory Droid (open source Goose lineage mentioned), AGENTS.md, skills, computer use (for user-testing validator), prompt caching

## [How Transformers Finally Ate Vision – Isaac Robinson, Roboflow](../videos/VhfAVA3BG2I.md)
`VhfAVA3BG2I` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: models-research, training-finetuning-rl, inference-serving

Isaac Robinson (Roboflow) traces how plain ViTs beat CNN and hybrid backbones, crediting massive ViT-specific pretraining, borrowed LLM speedups, and NAS over one foundation model for deployable vision.

- Techniques: Benchmark attention variants against a FlashAttention baseline; Masked-patch pretraining to instill inductive bias; Linear-probe check for frozen features; NAS over a pretrained foundation model; Transfer benchmark for foundation models
- Tools: SAM, SAM2, SAM3, MobileSAM, TinyViT, Hiera, ConvNeXt, Swin Transformer, ViT, MAE, DINOv2, DINOv3

## [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](../videos/pFsfax19yOM.md)
`pFsfax19yOM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: skills-self-improvement, claude-code, evals, context-engineering

Hands-on WorkOS workshop on writing Claude skills: description-based routing, constraints over prose, progressive disclosure, confidence gates, with-and-without-skill evals, and sharing skills.

- Techniques: Description-as-router; Constraints over prescription; Bang-backtick command injection; Progressive disclosure via reference map; Subagent for verbose checks; Confidence-gated clarification; With-and-without-skill eval; Transcript-driven skill refinement; Looped connector poll
- Tools: Claude Code, Codex, Cursor, Pi, OpenClaw, Claude Desktop, Claude Agent SDK, WorkOS CLI, Obsidian, Linear, Slack connector, Remotion

## [Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase](../videos/JT3OzDKrucU.md)
`JT3OzDKrucU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: skills-self-improvement, mcp-and-tools, evals, context-engineering

Pedro Rodrigues (Supabase) on writing a product skill for agents, using a three-condition eval to show skills plus MCP beat MCP alone. Main lesson: agents need guidance, not more context.

- Techniques: Three-condition skill eval; Inline must-not-miss rules; Skill as pointer to live docs; Dev-first schema workflow with a deferred migration; Start minimal and iterate
- Tools: Supabase, Supabase advisor, Braintrust, Claude Code, Codex, Vercel skills package, MCP, SSH, Postgres

## [Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski](../videos/ohKt066uFhg.md)
`ohKt066uFhg` · AI Engineer · 2026-05-18 · q2 · intro · talk · topics: product-ux, enterprise-adoption, security-guardrails, memory

Viktor's co-founder on building a company AI employee that lives in Slack: shared integrations, scoped access, memory across many users, and why tone and staged rollout matter.

- Techniques: Shared-integration inheritance with per-integration scoping; Thread roll-over on new DM; Treat edits and deletes as control signals; A/B test model personality, not only task scores; Staged proactivity rollout; Analytics check before acting on a claim; Browser-DOM web agent (2023 baseline)
- Tools: Slack, Viktor, OpenClaw, Claude Code, Claude Cowork, Opus 4.6, GPT-5.4, PostHog, Gmail, Meta Ads, WebArena

## [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](../videos/R7A8rX-09Zw.md)
`R7A8rX-09Zw` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: evals, models-research

Peter Gostev (Arena) argues leaderboard line-go-up hides real gaps; uses a nonsense-question "BullshitBench" and Arena's dissatisfaction-rate data to show progress is uneven by domain and that more reasoning can hurt.

- Techniques: False-premise / nonsense probe with LLM-as-judge; Dissatisfaction rate from pairwise votes; Domain and expertise slicing of real prompts; Compare reasoning effort on the same model
- Tools: BullshitBench, Arena text leaderboard

## [Why building eval platforms is hard — Phil Hetzel, Braintrust](../videos/_fQ7Z_Wfouk.md)
`_fQ7Z_Wfouk` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: evals, observability, data-engineering

Braintrust's Phil Hetzel on why eval platforms are a systems problem: the maturity path from spreadsheets to tracing plus online evals, and why agent traces break ordinary data stacks.

- Techniques: Spreadsheet plus for-loop eval starter; Playground for non-technical experimentation; Failure-mode-driven scoring functions; Online evals on the trace stream; Production-to-offline loop; Topic modeling over traces; Automatic tracing through an AI proxy or gateway
- Tools: Braintrust, Postgres, Neon, DuckDB, Google Sheets

## [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](../videos/ynJyIKwjonM.md)
`ynJyIKwjonM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: rag-retrieval, context-engineering, mcp-and-tools, skills-self-improvement

Leonie Monigatti (Elastic) argues context engineering is mostly agentic search, then walks through live demos of semantic search, ES|QL query tools, skill loading, and grep-style shell search, and when to use each.

- Techniques: Layered tool descriptions; Errors returned to the agent; Progressive disclosure for skills; Outsource aggregation to the search engine; Shell tool with semantic grep; Hybrid shell plus database verification; Log tool calls to find where specialization is needed; Use the file store as memory and offload old results
- Tools: LangChain, Elasticsearch, ES|QL, Jina embeddings v5, Jina grep (captioned as Gina grep), OpenAI GPT-5.4 nano and mini, shell / bash tool, Claude Code, OpenClaw (captioned as OpenCloud, exec tool)

## [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](../videos/WE_Gnowy3uw.md)
`WE_Gnowy3uw` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: skills-self-improvement, coding-agents, multi-agent, evals

Cursor's David Gomes on replacing its git-worktree and best-of-N feature (about 15K lines deleted) with one markdown skill plus subagents, and what was lost in the swap.

- Techniques: Skill as the orchestrator for a stateful workflow; Best-of-N through one subagent per model; Commands instead of skills for server-controlled prompts; Prompt-level containment with system reminders; Two-scorer isolation eval run headlessly; Feeding failure cases into RL training
- Tools: Cursor (2.0 and 3.0), Cursor CLI (headless), Git worktrees, Agent skills, Subagents, Slash commands, Composer (Cursor's own model, version 2 mentioned), Braintrust, Kimi, Grok, GPT, Opus

## [MCP = Mega Context Problem - Matt Carey](../videos/YBYUvGOuotE.md)
`YBYUvGOuotE` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: mcp-and-tools, sandboxing-execution, context-engineering

Cloudflare's Matt Carey argues that dumping every API endpoint into MCP tools blows up agent context, and that progressive discovery (tool search, CLIs, or code mode with typed SDKs run in isolates) is the way out.

- Techniques: Progressive tool discovery via tool search; Code mode over a generated typed SDK; Isolated execution of model-written code with programmable guardrails; Save agent-generated code as mini-scripts; Rate-limit APIs for agent callers
- Tools: MCP (Model Context Protocol), MCP SDK, OpenAPI, TypeScript, Cloudflare Workers, Dynamic Workers (workerd), V8 isolates, Wrangler, Cloudflare D1, Cloudflare Access, Claude Code, OpenClaw

## [Agents on the Canvas in tldraw — Steve Ruiz, tldraw](../videos/sPUjIBH5Cwg.md)
`sPUjIBH5Cwg` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: multi-agent, product-ux, sandboxing-execution, security-guardrails

Steve Ruiz (tldraw) shows how agents moved from one-shot drawing on a whiteboard to multiple agents working as a team on a shared canvas, and the safety trade-offs of letting them script a desktop app.

- Techniques: Structured-output shape drawing; Produce-review-iterate loop; Leader/follower multi-agent on shared state; Expose a runtime API for agent-written code; Prompt for spatial and coordinate conventions
- Tools: tldraw, Electron, Claude, Cursor, Make Real

## [I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)](../videos/sJ2jc7leKBk.md)
`sJ2jc7leKBk` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: memory, context-engineering, agent-architecture

An OpenClaw maintainer shows how he grew a personal agent into a life-running system step by step, using an Obsidian knowledge base, scheduled maintenance and channel-per-job routing, plus its failure modes.

- Techniques: Incremental capability ladder; Channel-per-job-type routing; Link-capture enrichment into a markdown vault; Verified overnight maintenance; Deterministic scripts beside LLM judgment; Critical-rules block high in the instruction file; Draft-don't-send attention filtering; Routine memory hygiene
- Tools: OpenClaw, Obsidian, QMD, Discord, Telegram, WhatsApp

## [Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral](../videos/3jGAU2sbAyY.md)
`3jGAU2sbAyY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: voice-multimodal, models-research, inference-serving

Mistral's Samuel Humeau explains why modern text-to-speech uses autoregressive audio-token LLM-style backbones, frame-level codecs and streamed output for voice agents.

- Techniques: Stream the first audio chunks; Two-level frame decoding; Codec with a bottleneck and text-aware token losses; Flow-matching token head per frame; Full-context conditioning with a short voice prompt; Fast small LLM for the text, TTS for the audio

## [Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind](../videos/Lm8BLHkxiAo.md)
`Lm8BLHkxiAo` · AI Engineer · 2026-05-18 · q2 · intro · talk · topics: local-ai, inference-serving, models-research

Google DeepMind's pitch for running Gemma 4 E2B/E4B agents on-device through LiteRT, with the conversion, quantization, device-benchmarking and NPU path laid out and vendor speed claims.

- Techniques: Hybrid local-plus-remote inference via function calling; Use native structured JSON output instead of prompt-only formatting; Packaging capabilities as user-authored skills; Bring-your-own-model conversion with graph inspection; Fleet-benchmark before shipping; Small local model as a gate in a split architecture
- Tools: LiteRT, TensorFlow Lite, LiteRT-LM, Gemma 4, Gemma 3, Model Explorer, AI Edge Portal, Google AI Edge Gallery app, Hugging Face, Core ML, Raspberry Pi, Qualcomm NPU

## [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX — Adrien Grondin, Locally AI](../videos/a2muGkT4WD4.md)
`a2muGkT4WD4` · AI Engineer · 2026-05-18 · q2 · intro · demo · topics: local-ai, inference-serving

Adrien Grondin (Locally AI) shows how to run quantized Gemma 4 on iPhone with Apple's MLX, covering the mlx-swift-lm package, picking quantized weights, and speed on phones.

- Techniques: Load quantized models by Hub ID in an on-device Swift app; Choose quantization between 4-bit and 8-bit; Stream tokens to the UI; Small local model for automation steps; Compare inference engines via a local server
- Tools: MLX, mlx-swift-lm, mlx-lm, mlx-vlm, mlx-audio, Hugging Face, mlx-community, LM Studio, llama.cpp, Apple Shortcuts, Gemma 4, Qwen

## [Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick](../videos/2TLXsxkz0zI.md)
`2TLXsxkz0zI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: software-factory, coding-agents, agent-architecture, context-engineering

Chris Parsons runs a live workshop on Ralph loops: re-running Claude Code on fresh context until work ships, fed by ticket files, a sequential queue, and reversibility limits on unattended agents.

- Techniques: Bash while-loop over fresh Claude sessions; Next-most-important-ticket selection over flat markdown tickets; Recovery check for mid-flight work; Reversibility gate with stop-and-report; Fresh-subagent adversarial review; Claude /loop for timed repetition; Resume a project in an interactive session; Simulated audience personas run in parallel subagents; Nightly session digest
- Tools: Claude Code, Codex, Cursor, n8n, Docker Sandbox, Playwright, Obsidian, Lian (embeddings CLI), Beads, Linear, Jira, Telegram

## [Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft](../videos/iOXM3zE-2dk.md)
`iOXM3zE-2dk` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · topics: observability, evals, security-guardrails, coding-agents

Microsoft Foundry workshop on agent observability: trace-linked evals, stage-wise agent evaluators, OTel tracing, red teaming, and an observe skill that automates the eval-optimize loop with a human stopping regressions.

- Techniques: Trace-linked evaluation; Stage-wise agent evaluators; Bootstrapped eval dataset from instructions; Version-compare regression diff; Bounded auto-optimization with human stop; Adversarial red teaming with an attacker agent; OTel GenAI tracing with custom attributes; Eval gate on model swap
- Tools: Microsoft Foundry, Azure Monitor, Application Insights, OpenTelemetry, GitHub Codespaces, dev containers, GitHub Copilot Chat, Foundry MCP server, Azure AI Toolkit (VS Code extension), LangGraph, KQL, PyRIT (auto-caption reads it as 'pirate')

## [The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked](../videos/qdh_x-uRs9g.md)
`qdh_x-uRs9g` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: inference-serving, rag-retrieval, infra-cost-scaling

Superlinked's Filip Makraduli on why small models (embeddings, rerankers, NER) need their own inference layer, and the open-source SIE engine built to serve them on shared GPUs.

- Techniques: Hot-swap many small models on one GPU with LRU eviction; Re-implement the forward pass per model family; Small-model preprocessing in front of the agent; Models as config, cluster as code
- Tools: vLLM, Prometheus, Grafana, Terraform, Helm, Docker, Hugging Face, FlashAttention, Chroma, Qdrant, Weaviate (transcribed as VV8), LanceDB (transcribed as LensDB)

## [The Future of MCP — David Soria Parra, Anthropic](../videos/v3Fr2JR47KA.md)
`v3Fr2JR47KA` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: mcp-and-tools, context-engineering, agent-architecture

David Soria Parra (Anthropic) on where MCP is heading: MCP apps, progressive tool discovery, code-style tool composition, and the 2026 protocol roadmap.

- Techniques: Progressive tool discovery; Programmatic tool calling / code mode; Use structured output to enable composition; Agent-first tool design; Pick connectivity per task; Skills-over-MCP approximation
- Tools: MCP, MCP Apps, Claude Code, Cloudflare MCP server, V8 isolate, Lua interpreter, FastMCP, Python SDK, TypeScript SDK, OpenAI Agents SDK, Google ADK, LangChain

## [CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner](../videos/VktrqzQgytY.md)
`VktrqzQgytY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: software-factory, pr-code-review, sandboxing-execution, multi-agent

Talk arguing CI/CD was built for human-paced PRs and breaks under agent volume; proposes spec-driven agent loops with in-loop validation, a pre-merge queue, and stateful compute.

- Techniques: Spec-first agent loop with a known-commit start; External review agents inside the loop; Pre-merge queue for serializable commits; Approve intent and evidence, not diffs; Stateful, incremental execution environments
- Tools: GitHub Actions, Claude Code, Amp, Cursor, Factory, GitHub Copilot, Namespace

## [Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind](../videos/_A367W_qvc8.md)
`_A367W_qvc8` · AI Engineer · 2026-05-18 · q4 · deep · talk · topics: models-research, inference-serving, local-ai

Google DeepMind researcher walks through Gemma 4's architecture: interleaved local/global attention, asymmetric GQA, per-layer embeddings in flash memory, a shared-expert MoE, and flexible image token budgets.

- Techniques: Interleaved local/global attention with sliding windows; Asymmetric GQA by layer type; Per-layer embedding tables offloaded to flash; Developer-selected image token budget; Shared-plus-routed MoE
- Tools: Gemma 4, Hugging Face, Kaggle, Ollama, Google AI Studio, Vertex AI

## [Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate](../videos/vi-2nasppAg.md)
`vi-2nasppAg` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · topics: agent-architecture, multi-agent, observability, sandboxing-execution

Iterate's workshop on building event-sourced agent harnesses as stream processors: pure reducers for state, side effects after append, pause-based circuit breakers. Live demos mostly failed; the design ideas are the value.

- Techniques: Event-sourced agent log; Reducer plus after-append split; Pause-event circuit breaker; Deferred enrichment with a time budget; Child paths for sub-agents; Secret substitution at fetch time
- Tools: events.iterate.com (event service), Cloudflare dynamic workers, OpenAI SDK (Responses API), Zod, Pi, Claude, OpenCode, Convex, Kafka, Cursor, OpenClaw, Electric SQL

## [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](../videos/MhHEGMFCEB0.md)
`MhHEGMFCEB0` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · topics: coding-agents, multi-agent, security-guardrails, pr-code-review

OpenAI's Codex workshop on plugins, background automations, code review, custom sub-agents with sandbox modes, guardian approvals, and stop hooks for long runs.

- Techniques: Custom sub-agent personas as TOML files; Fan-out review by file slices with an orchestrator; Read-only explorer on a fast cheap model; Parallel brainstorm of implementation options; Guardian verifier sub-agent for privileged actions; Stop hook that keeps a run going; Best-of-N cloud runs; Playwright interactive skill for visual debugging
- Tools: Codex, Codex app, Codex CLI, Codex IDE extension, Codex Code Review, Codex Security, Claude Code plugin for Codex, Playwright, ImageGen, Slack, Gmail, Google Drive

## [Gateways are All You Need — Karan Sampath, Anthropic](../videos/CD6R4Wf3jnY.md)
`CD6R4Wf3jnY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: mcp-and-tools, security-guardrails, governance-compliance, infra-cost-scaling

Anthropic forward-deployed engineer Karan Sampath argues enterprises should put one gateway in front of all MCP servers for auth, access control, observability and credentials, so teams build only business logic.

- Tools: MCP, Claude Code, Claude Agent SDK, claude.ai, Claude managed agents

## [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../videos/8txf05vVVl4.md)
`8txf05vVVl4` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: mcp-and-tools, token-cost-efficiency, sandboxing-execution, agent-architecture

Cloudflare's Sunil Pai on "Code Mode": have models write code against an API instead of making many tool calls, cutting a 2,600-endpoint API from ~1.2M tokens to ~1K, inside capability-restricted sandboxes.

- Techniques: Search + execute two-tool facade; Code as the tool-call format; Zero-capability sandbox with explicit grants; Agent-facing developer experience; Operate on the app's raw state
- Tools: Cloudflare Workers, Cloudflare Dynamic Workers, V8 isolates, OpenAPI, PartyKit, Claude Opus, TLDraw-style canvas

## [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub](../videos/ClWD8OEYgp8.md)
`ClWD8OEYgp8` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: coding-agents, multi-agent, product-ux, context-engineering

Maggie Appleton (GitHub Next) argues agents have shifted the bottleneck from building to agreeing on what to build, and previews ACE, a shared multiplayer environment for team-plus-agent work.

- Techniques: Shared always-on agent session per task; Whole-conversation context as prompt input; Plan first, co-edit, then execute; Session summary for switching between parallel sessions; Backward-compatible PRs that link back to the session
- Tools: GitHub ACE (Agent Collaboration Environment, research prototype), Claude Opus 4.6 (model used in the demo), Bun (bun install / bun dev in the demo project), VS Code (real-time multiplayer editing in the shared cloud machine), Slack, Jira, Linear (named as coordination tools that are not built for agentic work)

## [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../videos/_QAVExf_1uw.md)
`_QAVExf_1uw` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: context-engineering, rag-retrieval, skills-self-improvement, enterprise-adoption

A staff engineer at IKEA argues enterprise agents fail on undocumented institutional knowledge, and proposes a pull-based loop where agents surface knowledge gaps and curate context blocks before retrieval.

- Techniques: Pull-based knowledge capture from failed agent runs; Failing-tasks-as-tests for knowledge bases; Historical-incident replay as a probe source; Three-step gap scanner: probe generation, probe run, gap analysis; Freshness labels, flagged for human decision; Git-backed curated context blocks with a metamodel; 80/20 context cache with links to the monolith; Full-context before graph RAG, for small domains; Claude Code skills, rules, agents and hooks as the implementation
- Tools: Claude Code, GitHub Copilot, Confluence, Jira, Slack, GitHub, MCP, RAG, GraphRAG, Replit, Kanban board

## [Agents for Everything Else — swyx](../videos/zepu8Kk6FBQ.md)
`zepu8Kk6FBQ` · AI Engineer · 2026-05-18 · q3 · intro · keynote · topics: enterprise-adoption, coding-agents, product-ux

swyx describes how the nine-person AI Engineer team runs its business with coding agents (Devin, Claude Cowork), and argues agents should handle the routine "everything else" work, not just code.

- Techniques: Figma-to-site via coding agent; Code as the CMS source of truth, maintained by an agent; Agent as ops triage for routine requests; Prioritised concern reduction for AI adoption
- Tools: Devin, Claude Cowork, Figma, Sanity, Notion, Google Sheets, Sessionize, Supabase, React, OpenClaw, tldraw

## [AgentCraft: Putting the Orc in Orchestration — Ido Salomon](../videos/kR64LOqBBCU.md)
`kR64LOqBBCU` · AI Engineer · 2026-05-18 · q2 · intro · demo · topics: multi-agent, coding-agents, product-ux, pr-code-review

Ido Salomon demos AgentCraft, an RTS-style orchestrator for many coding agents, arguing the human is the bottleneck and offering visibility, campaigns, review bundles and shared workspaces as fixes.

- Techniques: Filesystem-projected agent map with collision heat map; Hotkey cycling to agents that need attention; Campaign mode: broad goal in a container, plan first; Review bundles with rationale and visual evidence; Best-of-N parallel attempts with human selection; Soft coordination via shared human and agent chat
- Tools: AgentCraft, MCPUI, MCP Apps, Cursor, Claude Code, Codex, OpenClaw, Git, Chrome

## [Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably](../videos/YNJvm7t3yq8.md)
`YNJvm7t3yq8` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: agent-architecture, product-ux, multi-agent

Ably's Mike Christensen argues that AI chat UX breaks under direct HTTP/SSE streaming and proposes durable sessions (a shared, resumable channel between agents and clients) to get resilient streams, multi-device sync, and live steering or cancel.

- Techniques: Durable session as a shared channel; Hand-rolled resumable stream (the baseline he contrasts with); Bidirectional transport to separate cancel from disconnect; Multi-agent writes straight to the shared session; Any-client control through the session; Human handoff as another session participant
- Tools: Ably channels, Ably AI Transport, Server-Sent Events (SSE), WebSockets, Redis, Vercel AI SDK, TanStack AI

## [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../videos/XNtkiQJ49Ps.md)
`XNtkiQJ49Ps` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: product-ux, agent-architecture, evals, skills-self-improvement

Legora's CTO argues that vertical agents need more than chat: make work verifiable, let humans steer through skills and decision logs, and use persistent artifacts as the collaboration surface.

- Techniques: Proxy verification with golden examples; Task decomposition by verifiability; Allowlist guardrails for agent actions; Skills as judgment encoded at work nodes; Elicit-or-decide with a decision log; Persistent, scoped artifacts as the collaboration surface
- Tools: Claude Code

## [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../videos/5ID22ACI7IM.md)
`5ID22ACI7IM` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · topics: context-engineering, memory, rag-retrieval, security-guardrails

Peter Werry and Brandon (Unblocked) argue that agents need a "context engine" that understands org history, permissions and conflicts, not just MCP access to data, then run a hands-on social-graph workshop. Much of it is product pitch.

- Techniques: Compartmentalized, permission-tagged retrieval; Ingestion-time tags plus runtime judge for conflicts; Expert graph from contribution edges; Focus-repo-biased two-stage retrieval; Feedback weighted by source trust; Split cadence by source type
- Tools: Claude Code, Cursor, Codex, GitHub Copilot, MCP, Slack, Microsoft Teams, Sentry, Datadog, GraphRAG, pgvector-style vector retrieval, Composio

## [The New Application Layer - Malte Ubl, CTO Vercel](../videos/XKup1pj-34M.md)
`XKup1pj-34M` · AI Engineer · 2026-05-18 · q3 · intro · keynote · topics: agent-architecture, sandboxing-execution, enterprise-adoption, product-ux

Vercel CTO Malte Ubl argues agents are a new kind of software that makes long-tail automation affordable, names practical agent archetypes, and says harnesses should run apart from the code they generate.

- Techniques: Compress-the-research agent; Information-surfacing agent; Ask-what-you-hate discovery; Harness and code execution split; CLI and API first for agent-facing products; Lightweight bash sandbox for agents
- Tools: Vercel AI SDK, Chat SDK, JustBash, Claude, Codex, Granola, Pi, OpenClaw

## [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](../videos/W76woOYHlvY.md)
`W76woOYHlvY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: software-factory, coding-agents, product-ux, agent-architecture

Louis Knight-Webb (Vibe Kanban) argues engineers will mostly plan and review as agents run longer, then live-demos shutting his company down through the tool.

- Techniques: Task-type mode selection; Clarifying-question planning; Parallel agent workspaces; PR comment shepherding
- Tools: Vibe Kanban, Claude Code, Codex, Cursor, GitHub Copilot, Playwright MCP, GitHub, Cloudflare CDN

## ["Software Fundamentals Matter More Than Ever" — Matt Pocock](../videos/v4F1gFy-hqg.md)
`v4F1gFy-hqg` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: testing-verification, context-engineering, coding-agents, claude-code

Matt Pocock argues software fundamentals (deep modules, shared language, TDD, good feedback loops) matter more with AI agents, because bad code is now the most expensive it has been.

- Techniques: Grill-me interview before planning; Generated ubiquitous-language glossary; Small-step TDD with feedback loops; Codebase architecture improvement skill; Design the interface, delegate the implementation
- Tools: Claude Code

## [Give Your Agent a Computer — Nico Albanese, Vercel](../videos/wflNENRSUb4.md)
`wflNENRSUb4` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · topics: agent-architecture, sandboxing-execution, mcp-and-tools, context-engineering

Nico Albanese (Vercel) live-builds a coding-style agent with AI SDK 6: a tool loop, web search, a persistent named sandbox running bash, file-based memory and self-written scripts, plus notes on context pruning and subagents.

- Techniques: Single-definition tool loop agent; Typed UI messages from the agent definition; Named persistent sandbox per session; Bash-only tool for a coding-style agent; Call options plus runtime context injection; File-backed memory injected into the system prompt; Per-step hook for message slicing; Subagents and handoff instead of compaction; Plan file with objective and checkboxes
- Tools: Vercel AI SDK 6, Vercel AI Gateway, Vercel Sandbox (persistent named sandboxes, beta), Next.js, Zod, OpenAI provider (web search tool), Anthropic provider (bash/computer tools), Vercel Workflow (durable steps), OpenCode, Amp (handoff tool)

## [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @The Pragmatic Engineer](../videos/wjk0ulMAkbc.md)
`wjk0ulMAkbc` · AI Engineer · 2026-05-18 · q3 · practitioner · interview · topics: product-ux, testing-verification, coding-agents

Linear's CTO and Gergely Orosz on why AI makes taste and quality the scarce advantage. Linear's practices: Quality Wednesdays, a zero-bug policy, and week-long paid work trials.

- Techniques: Quality Wednesday; Zero-bug policy with agent triage; Single-shot agent PRs for incoming bugs; Human-judged feel in agent output; Paid greenfield work trial; Open, tagged customer meeting archive
- Tools: Claude Code, Opus 4.5, Linear, Apple Human Interface Guidelines

## [FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs](../videos/x8Yb4RidLgM.md)
`x8Yb4RidLgM` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: models-research, voice-multimodal, inference-serving

Black Forest Labs' developer relations engineer walks through FLUX model history, a new self-supervised training method (Self-Flow) that drops external encoders, and sub-second Klein editing.

- Techniques: Dual-noise self-supervised representation learning (Self-Flow); External-encoder representation alignment; Multi-reference conditioning for consistency; Chaining edited frames as video keyframes
- Tools: FLUX.1, FLUX Context, FLUX.2, FLUX.2 Klein, Self-Flow, DINOv2, DINOv3, Qwen

## [One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS](../videos/EmhRyw6xeT0.md)
`EmhRyw6xeT0` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: security-guardrails, mcp-and-tools, enterprise-adoption

Garrett Galow (WorkOS) explains cross-app access (XAA): the enterprise IdP brokers silent, short-lived MCP tokens so users stop clicking consent screens and IT regains revocation and visibility.

- Techniques: Cross-app access via ID-JAG token exchange; IdP-side allow-list for app-to-app access; Short-lived access tokens with silent re-mint; Audience URL as the routing key; Server-side ID-JAG acceptance
- Tools: MCP, Claude Code, Cursor, Okta, Figma, WorkOS, Microsoft Entra, SCIM, CIMD, DCR, OAuth, OIDC

## [Context Is the New Code — Patrick Debois, Tessl](../videos/bSG9wUYaHWU.md)
`bSG9wUYaHWU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: context-engineering, evals, skills-self-improvement, security-guardrails

Patrick Debois argues that agent context (instructions, skills, specs) needs its own lifecycle like code: generate, test with evals, distribute as packages, observe logs, then adapt.

- Techniques: Layered context tests (lint, judge, end-to-end); Repeated runs with error budgets; Commit-scoped context A/B scenarios; Turning feedback into context fixes; Context filter before loading; Packaging context with provenance and scanning; Parallel generation as a spec-quality check
- Tools: Claude Code, AGENTS.md, CLAUDE.md, SKILL.md, MCP, Tessl, GitHub, GitLab, Slack, Snyk, Gemini, GitHub Copilot

## [Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs](../videos/UsB70Tf5zcE.md)
`UsB70Tf5zcE` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · topics: training-finetuning-rl, models-research

Hands-on workshop on building and training a tiny GPT-2-style character-level LLM from scratch in PyTorch on a laptop or Colab, covering tokenizer, transformer blocks, training loop, and decoding.

- Techniques: Character-level tokenizer via stoi/itos dictionaries; Decoder-only transformer with pre-norm residual blocks; Offset-by-one next-token targets with cross-entropy; Linear warmup then cosine decay with AdamW; Validation-loss checkpointing and overfit detection; Loss-curve triage; Temperature and top-k sampling for generation; Seed-pinned, prompt-logged output for reproducibility; Encoder-to-embedding injection for multimodal inputs; Modality-specific losses for audio and distillation
- Tools: PyTorch, uv, NumPy, tqdm, tiktoken, Google Colab, Python 3.12, Karpathy nanoGPT (referenced)

## [LLM codegen fails and how to stop 'em — Danilo Campos, PostHog](../videos/juoNbJiZUi0.md)
`juoNbJiZUi0` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: coding-agents, context-engineering, skills-self-improvement, security-guardrails

Danilo Campos (PostHog) on making an autonomous integration agent reliable: feed fresh docs, use thin "model airplane" example apps, breadcrumb the task, interrogate the agent at each stop, and lock down secrets.

- Techniques: Agent-selected fresh docs menu; Model airplane example apps; Breadcrumbed multi-stage prompting; Stop-hook self-interrogation; Tool-gated secret access
- Tools: PostHog Wizard, Claude Agent SDK, Claude Code, Cursor, MCP, PostHog LLM gateway

## [Feedback Loops are All You Need — Mehedi Hassan, Granola](../videos/ON5LIT0M4do.md)
`ON5LIT0M4do` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: observability, product-ux, testing-verification

Granola's Mehdi Hassan argues that shipping LLM features needs your own tracing, per-PR web previews, and fast feedback loops, not better one-shot prompts.

- Techniques: Home-built LLM tracing store with an internal UI; Web-shell preview per PR; Agent self-verification with screenshot evidence; Own the web search path
- Tools: Electron, Cursor, AI SDK, CloudWatch, OpenTelemetry, Tauri, Figma

## [Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev](../videos/svCnShDvgQg.md)
`svCnShDvgQg` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: agent-architecture, sandboxing-execution, infra-cost-scaling

Eric Allam (Trigger.dev) argues that replay-based durable execution breaks for long-running agent loops, and proposes splitting agent durability into an append-only context log plus VM snapshot/restore of the execution state.

- Techniques: Two-layer agent durability; Snapshot on idle, restore on next message; Recovery by failure class; Seekable compression with lazy page restore; Whole-VM snapshot instead of process checkpoint
- Tools: Trigger.dev, Firecracker, CRIU (captioned as "Cree"), Docker, fcrun

## [Full Walkthrough: Workflow for AI Coding — Matt Pocock](../videos/-QFHIoCo-Ko.md)
`-QFHIoCo-Ko` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: context-engineering, software-factory, testing-verification, multi-agent

Matt Pocock's live workshop on an AI coding workflow: grill-me alignment, PRD, vertical-slice issues with blocking edges, AFK Ralph loops with TDD and feedback loops, and deep-module codebases.

- Techniques: Smart-zone sizing and clear-over-compact; Grill-me alignment skill; Destination doc plus journey issues; Ralph loop (sequential AFK runner); Red-green-refactor TDD for agents; Self-review in a fresh context; Interface-first deep modules with grey-box delegation; Push vs pull for coding standards; Sandcastle-style parallel runs; Delete plans and PRDs after they ship
- Tools: Claude Code, Sandcastle, Docker, TypeScript, GitHub Issues, TLDraw, Slido, Playwright MCP, Sonnet, Opus, Spec Kit, OpenSpec

## [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google](../videos/BKWpYIWvAo4.md)
`BKWpYIWvAo4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: local-ai, inference-serving, skills-self-improvement, training-finetuning-rl

Google AI Edge on running small Gemma models on-device via LiteRT-LM, the on-device agent-skills pattern (progressive disclosure, constrained tool calls), and fine-tuning tiny models with synthetic data.

- Techniques: Progressive disclosure for skills; Three-primitive orchestrator; Constrained decoding scoped to tool calls; Synthetic data then fine-tune then quantize; Modular pipeline of small models; LoRA hot-swap on one base model; Skill testing loop with a coding agent and a device; Build-once, deploy-everywhere model file with AOT for NPU
- Tools: LiteRT-LM, LiteRT (formerly TensorFlow Lite), LiteRT-Torch, Google AI Edge Gallery, MediaPipe, Gemma 4 (E2B, E4B), Function Gemma (270M), Gemma 3 270M, EmbeddingGemma (300M), FastVLM (500M, Apple), Qwen 0.6B, Gemini CLI

## [Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind](../videos/cVzf49yg0D8.md)
`cVzf49yg0D8` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · topics: voice-multimodal, agent-architecture, mcp-and-tools, context-engineering

Google DeepMind hands-on workshop on building agents with the Gemini Interactions API (server-side state, background runs, skills) and the Live API (native-audio voice agents), with live demos that partly failed.

- Techniques: Chained interactions via previous ID; Async background runs with polling or webhooks; Skill that links to live docs; Tool loop with recursion; Server-to-server Live proxy; Ephemeral token for direct browser connection; Context window compression for long Live sessions; Voice persona through system instructions; Send a single image and then audio
- Tools: Gemini Interactions API, Gemini Live API, Google AI Studio, Gemini 3 Flash / 3.1 Flash Live, Lyria 3, Nano Banana, Google Search grounding, uv, FastAPI, Context7, skills.sh, Antigravity

## [Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML](../videos/X6NShR2ccOg.md)
`X6NShR2ccOg` · AI Engineer · 2026-05-18 · q2 · intro · talk · topics: training-finetuning-rl, evals, enterprise-adoption, inference-serving

Adaptive ML's CCO argues RL, not prompting or SFT, is the systematic way to take enterprise LLMs and agents from MVP to production, using environments, rewards, and LLM judges. Mostly a product pitch for their platform.

- Techniques: Mock environment with mock tools and an LLM-played user; Rejection-sampling bootstrap from reward-scored trajectories; Business KPI as the RL reward; LLM judge with human-written rubric, graduated to a reward model; Prefer a smaller RL-trained model for high-volume or latency-bound features
- Tools: Adaptive Engine, PPO, GSPO, Gemma, Mistral, Qwen

## [Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs](../videos/DCZZ3AJKzuc.md)
`DCZZ3AJKzuc` · AI Engineer · 2026-05-18 · q2 · intro · demo · topics: voice-multimodal, agent-architecture, mcp-and-tools

ElevenLabs' Luke Harries argues chat agents should add voice, and previews VoiceEngine, a wrapper that adds STT, TTS and turn-taking to an existing chat agent without a rebuild.

- Techniques: Voice wrapper around an existing agent; Client-side vs server-side tools for voice; Prompt a coding agent with a conversion skill
- Tools: ElevenLabs VoiceEngine, ElevenLabs Scribe (speech-to-text), ElevenLabs V3 (text-to-speech), ShadCN / Vercel-style UI components

## [Mastering AI Pricing — Mayank Pant, Stripe](../videos/CrqPcIZOOXA.md)
`CrqPcIZOOXA` · AI Engineer · 2026-05-18 · q3 · intro · talk · topics: product-ux, infra-cost-scaling, governance-compliance

Stripe's billing architect on AI pricing: treat the first price as a hypothesis, use base-plus-usage hybrid pricing with credits, add usage guardrails, and choose billing infrastructure that lets you change prices quickly.

- Techniques: Credit abstraction layer; Base fee plus usage fee (hybrid); Usage guardrail stack; Value-to-metric mapping; Grandfathered pricing versions; Per-event rating with explainable invoices
- Tools: Stripe Billing, Metronome

## [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase](../videos/GmAQKINjv1E.md)
`GmAQKINjv1E` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: skills-self-improvement, evals, claude-code, context-engineering

Pedro Rodrigues (Supabase) walks through writing agent skills, testing their triggering, and running with/without-skill evals, using a Postgres RLS view bug as the running example.

- Techniques: Progressive-disclosure skill layout; Trigger-accuracy testing via headless CLI; With/without skill eval comparison; Deterministic state assertions before LLM judging; MCP tool plus skill split for data access; security_invoker for Postgres views over RLS tables; Skill install via npm skills package with symlinks
- Tools: Claude Code, Supabase MCP server, Supabase CLI via npx, Postgres, Next.js, Braintrust, Langfuse, Vercel skills npm package, Python (DB reset and eval scripts), VS Code

## [How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs](../videos/kfSDc2eVLo4.md)
`kfSDc2eVLo4` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: enterprise-adoption, product-ux, evals

Chris Lovejoy (Notius Labs) argues winning in vertical AI is an organizational problem, and gives a three-role framework (oracle, evaluator, architect) for placing domain experts, with Granola, Tandem and Anterior as cases.

- Techniques: Oracle role (domain expert edits the product directly); Decentralized oracle; Evaluator role (expert defines metrics; engineers improve); Architect role (self-improving system); Role progression check
- Tools: LLM-as-judge, clinician review dashboard

## [Harnesses in AI: A Deep Dive — Tejas Kumar, IBM](../videos/C_GG5g38vLU.md)
`C_GG5g38vLU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: agent-architecture, testing-verification, security-guardrails, context-engineering

Tejas Kumar (IBM) walks through building a "poor man's" agent harness live: deterministic guardrails, outcome verification, and credential injection around a weak model, with the prompt left unchanged.

- Techniques: Deterministic pre-turn hook for state and secrets; Outcome verification from the trace; Guardrails as composable functions; Two-level retry around an attempt; Naive head-and-tail context trimming; Tool definitions in the OpenAI SDK shape
- Tools: Playwright, Chromium, OpenAI Agents SDK-style tool definitions, GPT-3.5 Turbo, Claude Code, Cursor, Codex, Qwen, GPT-OSS, OpenRAG

## [Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic](../videos/A48uhxfxbsM.md)
`A48uhxfxbsM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: evals, context-engineering, observability

Samuel Colvin (Pydantic) live-demos optimizing a structured-output extraction prompt with GEPA against a golden dataset, then serving managed prompt variables from Logfire without redeploying. Main takeaway: deterministic golden-set evals plus automated prompt search help most for cheaper models and private data.

- Techniques: Golden-dataset structured-output eval with a custom deterministic evaluator; Compare-two-runs error analysis; GEPA prompt search with an expert-prompt-engineer proposer; Keyed-component optimization instead of free-form prompt rewrites; Typed managed variables for live prompt and config changes; Trace the optimizer itself; Train/eval split with extra coverage
- Tools: Pydantic AI, Pydantic Logfire, GEPA (called JEPA in captions), DSPy, OpenFeature, Beautiful Soup, FastAPI, Pydantic AI Gateway, uv

## [Building your own software factory — Eric Zakariasson, Cursor](../videos/rnDm57Py54A.md)
`rnDm57Py54A` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: software-factory, context-engineering, testing-verification, coding-agents

Cursor engineer Eric Zakariasson on building a "software factory": how to structure repos, grow rules from observed failures, make agents verify their own work, and automate the human loops. Practical, with a product pitch.

- Techniques: Failure-driven rule growth; Reviewer bot enforces house conventions the model lacks; Self-verification with e2e tests and recorded runs; Scoped, parallel async tasks with front-loaded specs; Per-agent VM with a single dev command; Agentic code owners with risk tiering; Loop and stall detection for background agents; Event-triggered cleanup agents
- Tools: Cursor, Cursor cloud agents, BugBot, Playwright, AGENTS.md, Linear, Slack, GitHub, Datadog, Notion, MCP, Cursor workers

## [Fighting AI with AI — Lawrence Jones, Incident](../videos/L2r6vLlLgs8.md)
`L2r6vLlLgs8` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: evals, observability, coding-agents, multi-agent

Lawrence Jones (Incident.io) on using AI tools to debug and improve multi-prompt AI systems: export UI traces and eval suites as file systems for coding agents, then run parallel backtest analysis pipelines.

- Techniques: Eval-tool CLI for agents; Runbook-driven prompt fix; Download trace or interaction as a file tree; Parallel per-item analysis with file-based resume; Cohort clustering over failures; Analysis as a repeatable markdown playbook; Investigate, fix, then verify in one session
- Tools: Claude Code, Codex, Go, YAML

## [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../videos/xOP1PM8fwnk.md)
`xOP1PM8fwnk` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: models-research, inference-serving, training-finetuning-rl, voice-multimodal

Google DeepMind's Sander Dieleman walks through training image and video diffusion models at scale: learned latents, how denoising works, guidance, step-count distillation, and control signals added in post-training.

- Techniques: Two-stage latent diffusion with a learned autoencoder; Guidance by amplifying the conditional-minus-unconditional difference; Deterministic sampling as a distillation teacher; Consistency distillation restricted to sampling intervals; Injecting conditioning via extra tokens or broadcast; Data-parallel first, then model-parallel sharding with JAX pjit
- Tools: JAX, pjit, TPU, Stable Diffusion, GLIDE, EQVAE, Veo, Genie

## [Scaling GitHub for your Agents — Sam Morrow, GitHub](../videos/0n3MKk7r60w.md)
`0n3MKk7r60w` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: mcp-and-tools, context-engineering, security-guardrails

GitHub's MCP server lead on scaling a remote MCP server: why too many tools hurt agents, how defaults and tool-set grouping work, token-trimmed outputs, scope-based auth, and a stateless design.

- Techniques: Per-request server construction with policy-filtered tools; Scope-filtered tool listing with step-up auth; Tool-set grouping with defaults tuned from usage data; Output-token tailoring per tool; Server-side composition to encode intent; Cross-tool eval for description tuning; Wrap read-only tools in a CLI to test agent use
- Tools: GitHub MCP server, Claude Code, VS Code, Redis, Cloudflare code mode, Anthropic tool search, Pi

## [Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI](../videos/fLUtUkqYHnQ.md)
`fLUtUkqYHnQ` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · topics: training-finetuning-rl, inference-serving, models-research, local-ai

Liquid AI's Maxime Labonne on training 350M to 24B edge models: small models have their own constraints, narrow targeting and doom-loop fixes via DPO and RL.

- Techniques: On-policy DPO pairs for doom-loop suppression; Repetition penalty inside RLVR; Fix training stage by diagnosis; Profile architecture on target hardware; Tool and environment offload for small models
- Tools: Hugging Face, Python

## [Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize](../videos/Xfl50508LZM.md)
`Xfl50508LZM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: evals, observability, agent-architecture

A two-hour Arize Phoenix workshop on evaluating a Claude-powered financial research agent: read traces first, then write code evals, LLM judges, meta-evals and experiments.

- Techniques: Root-span code eval; Faithfulness eval using the research step as context; Classification LLM judge with a binary label; Trace-to-dataset failure loop; Wrap multi-turn agent runs in one parent span; Golden set with a held-out split and reference solutions; Pairwise comparison and reliability metrics; Cost-normalized accuracy and tiered models
- Tools: Arize Phoenix (Phoenix Cloud), OpenInference instrumentation, OpenTelemetry (phoenix.otel register, auto_instrument), Claude Agent SDK, Claude Haiku (agent model), Claude Sonnet (judge model), Phoenix evaluators (correctness, faithfulness, classification), Phoenix datasets and experiments, Arize AX (enterprise product, mentioned)

## [Build & deploy AI-powered apps — Paige Bailey, Google DeepMind](../videos/G_bHFmEAarM.md)
`G_bHFmEAarM` · AI Engineer · 2026-05-18 · q2 · intro · demo · topics: models-research, vibe-coding-app-building, product-ux

Paige Bailey (Google DeepMind) gives a demo-heavy tour of Gemini models, AI Studio tools (grounding, URL context, code execution), Build for prompt-to-app, Genie 3, Veo 3.1 Lite, Gemma 4 and Gemini Live.

- Techniques: Clip video by time and frame rate; Let code execution do the exact work; URL context as lightweight grounding; Per-task thinking level; Prompt expansion before generation; Plan with a big model, act with a local model; Compare mode for model choice; Export UI experiments to code; System instructions for voice output style
- Tools: Google AI Studio, Gemini API, Gemini Live, Gemini 3.1 Pro, Gemini 3.1 Flash, Gemini 3.1 Flash-Lite, Google Search grounding, URL context, code execution, Build (AI Studio app builder), Firebase / Firestore, Cloud Run

## [A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon](../videos/vAIDdLKB6-w.md)
`vAIDdLKB6-w` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · topics: agent-architecture, coding-agents, enterprise-adoption

Matthias Luebken (Taven AI) shows how the open-source Pi coding agent, the core under OpenClaw, can be embedded in a product: an agent is a tool-calling loop, and a sales-RFP email agent is built on per-customer sessions and CLI tools.

- Techniques: Agent as tool loop with event and hook surface; Extension commands with UI selection; Per-customer agent with harness and customer files; Backend access as CLIs for the agent; Small single-purpose tools packaged as a skill; Draft-first human-in-the-loop output
- Tools: Pi, OpenClaw, Claude Cowork, FFmpeg, pandas, openpyxl, LibreOffice, AGENTS.md, NVIDIA OpenShell, TypeScript

## [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @The Pragmatic Engineer](../videos/CS5Cmz5FssI.md)
`CS5Cmz5FssI` · AI Engineer · 2026-05-18 · q3 · practitioner · interview · topics: enterprise-adoption, coding-agents, governance-compliance, infra-cost-scaling

Gergely Orosz (Pragmatic Engineer) on "token maxing": how usage leaderboards get gamed, why individual gains do not yet show up as team gains, and why big companies build their own agent infrastructure.

- Techniques: Enable non-engineers to build with coding agents; Keep agent count small and treat orchestration like tech lead mentoring; Single MCP gateway tied to service discovery; Risk-tiered code review for agent-written changes; Trade early access for structured feedback
- Tools: Claude Code, Cursor, GitHub Copilot, MCP gateway

## [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../videos/mYSRn6PC1mc.md)
`mYSRn6PC1mc` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · topics: agent-architecture, evals, mcp-and-tools, context-engineering

Workshop on building a deep-research agent (MCP server plus Claude Code skills) that feeds a separate LinkedIn writer workflow with evaluator-optimizer review and a calibrated LLM-judge eval loop.

- Techniques: Autonomy-ladder architecture choice; Tools as specialists inside one agent; Delegation to keep context lean; Files as the inter-agent contract; Guideline plus static style profiles; Start with many few-shot examples, then trim; Evaluator-optimizer with fresh context and typed feedback; Synthetic eval inputs, real outputs, binary labels with critiques; Judge calibration with dev/test F1; MCP server exposes tools, prompts and resources; skills wrap prompts for progressive disclosure; Trace-based debugging with threads and traces
- Tools: Claude Code, FastMCP, MCP, Gemini API (grounding, multimodal YouTube), Firecrawl, Perplexity, Opik, Pydantic, git-ingest, uv, Python

## [Beyond Code Coverage: Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft](../videos/FWEInOtngmM.md)
`FWEInOtngmM` · AI Engineer · 2026-05-18 · q3 · practitioner · tutorial · topics: testing-verification, coding-agents, mcp-and-tools

Marlene Mhangami (Microsoft/GitHub) argues for red-green TDD with coding agents, testing user-facing behavior with Playwright instead of unit-test coverage, and shows a live Copilot CLI demo.

- Techniques: Red-green-refactor with a coding agent; Behavior-scoped tests against user-facing or stable-contract behavior; Connect the agent to Playwright (three options); Checkpoint before the healer runs; Operational hygiene for Playwright runs; Ingest requirements from M365 with WorkIQ; Prefer direct API tests when an API exists
- Tools: GitHub Copilot CLI, Playwright, Playwright MCP server, Playwright CLI, Playwright Agents, WorkIQ, Azure AI search, Claude, Codex, Ruby on Rails, Python (Playwright binding), TypeScript (Playwright binding)

## [How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research](../videos/zZsTVBXcbow.md)
`zZsTVBXcbow` · AI Engineer · 2026-05-18 · q3 · intro · talk · topics: models-research, rag-retrieval

Raia Hadsell (VP Research, Google DeepMind) surveys non-LLM frontier work: unified multimodal embeddings, neural weather models (GraphCast, GenCast, FGN), and Genie world models.

- Techniques: Unified multimodal embedding; Matryoshka (MRL) dimension scaling; Probabilistic forecasting for tail events; Train for the end target, not a post-hoc detector; Memory consistency test for world models
- Tools: Gemini Embeddings 2, GraphCast, GenCast, FGN (Functional Generative Network), Genie 1, Genie 2, Genie 3, Veo 3, Gemma 4

