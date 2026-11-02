# enterprise-adoption — 143 videos

*adoption stories at companies, org change, AI-native teams, case studies*

By channel: AI Engineer 132 · Kai Explains 3 · AI LABS 2 · Better Stack 6

**Synthesized guide:** [guides/enterprise-adoption.md](../guides/enterprise-adoption.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Your AI Pilots Won't Move the P&L. Here's What Will - Adam Nahari, Apollo](../videos/vUJDyDnqT4c.md)
`vUJDyDnqT4c` · AI Engineer · 2026-11-02 · q3 · intro · talk · also: product-ux, governance-compliance

Adam Nahari (Apollo) argues AI pilots fail to move EBIT because most spend goes to general tools and change management, and sets out six moves (pick one or two P&L-linked problems, redesign the process end to end, get CEO sponsorship, build with the business, put tools in everyone's hands, pre-set kill metrics) to make AI show up in margin.

- Techniques: Work-backward use-case screen; End-to-end workflow redesign over assistive tooling; Embedded domain champions in the build loop; Pre-registered kill gates; At-scale unit economics check

## [I Don't Fear AI Slop. I Fear Untold Stories - Zack Proser, WorkOS](../videos/1et3Lb_KLQo.md)
`1et3Lb_KLQo` · AI Engineer · 2026-11-02 · q3 · intro · talk · also: product-ux

WorkOS's Zack Proser argues you should encode your taste into an AI "factory" and hand it to others. Examples: an internal blog-drafting bot and a bedtime-story app. A named human still signs off.

- Techniques: Codify your taste as a fixed pipeline, then expose it behind a simple interface; Connector-backed context assembly before drafting; Draft, iterate in plain language, then human sign-off; Four-question review rubric for AI-assisted output; Playtest a factory with a small audience and measure repeat use
- Tools: BlogBot (internal WorkOS blog-drafting system; name as stated in talk), Cloudflare (hosting for BlogBot), Slack (entry point for colleagues), Granola (meeting recordings as a data source), Claude Opus (captioned as 'Opus 5-5 extra high'; the version string is uncertain from auto-captions)

## [AI Writes Code Faster Than Your Team Can Review It - Andrew Norrish, Sourcegraph](../videos/-X3yXTwGs9A.md)
`-X3yXTwGs9A` · AI Engineer · 2026-11-02 · q2 · practitioner · talk · also: pr-code-review, observability

Sourcegraph's field director argues AI code outpaces human review, so SRE and platform teams need code-search-driven investigation, monitors and bulk remediation. Mostly a vendor pitch.

- Techniques: Deterministic cross-repo code search for incident root cause; Commit-pattern monitors for AI-written code; Bulk remediation across repos; Webhook-triggered agentic triage; Automated RCA from deploy history; Eval-gated code-review agent over historical branches
- Tools: Sourcegraph (code search, code graph, Deep Search, MCP server), HackerOne, git (history search for incident commits)

## [Why We Rebuilt Microsoft Office From Scratch for AI Agents - Yijia Liang, Compound AI](../videos/v0UkV5qS9E4.md)
`v0UkV5qS9E4` · AI Engineer · 2026-11-01 · q3 · practitioner · talk · also: multi-agent, evals, rag-retrieval

Compound's Yijia Liang explains why they rebuilt Excel, PowerPoint and Word as headless Rust engines for finance agents, using the real Office apps as an oracle in agent loops, plus email-based multiplayer agents and swarm-based file processing.

- Techniques: Objective-function loop against the incumbent app as oracle; Own the write-render-check-fix loop with a headless engine; Grep-first agent swarm over a large file corpus with citations; Email as the multiplayer interface for an agent
- Tools: Compound (getCompound.ai), IronCalc, Microsoft Excel, Microsoft PowerPoint, Microsoft Word, OpenPyXL (transcribed as 'OpenPAxcel' / 'OpenPi Excel'), Outlook, SharePoint, Box, Microsoft Teams, Claude, ChatGPT

## [Most of Your Docs Readers Are Now AI Agents - Hahnbee Lee, Mintlify & Lincoln Murr, Coinbase](../videos/YX4Z4XqZ9Vo.md)
`YX4Z4XqZ9Vo` · AI Engineer · 2026-11-01 · q2 · intro · interview · also: mcp-and-tools, product-ux

A Mintlify and Coinbase fireside chat on designing docs and APIs for agent readers and agent payments; mostly opinion, with one notable agent-traffic stat and a closing build-vs-buy plug.

- Techniques: Keep docs lean for agent readers; Track agent share of docs traffic; Automate doc upkeep, keep prose human; Expose the product as APIs first, then wrap; Pay per call with a wallet instead of API keys
- Tools: Mintlify, x402, MCP, CLI, API, OpenClaw

## [Why AI Won't Replace Stock Pickers - Jack Woodruff, Candlestick & Vinoo Ganesh, Kepler](../videos/y2dyD6slKxE.md)
`y2dyD6slKxE` · AI Engineer · 2026-10-30 · q2 · intro · interview · also: governance-compliance, data-engineering

Fireside chat between a hedge fund founder and a Kepler co-founder on how AI changes stock picking: AI raises the baseline, auditability is the trust gate, and edge comes from divergent views and idea velocity.

- Techniques: Audit-first verification of model-produced numbers; AI as attention triage for human research; Automate prep, reinvest time in differentiated work

## [The Cheaper AI Model That Costs You More - Rayan Krishnan, Vals AI](../videos/rWtbOgl5FTU.md)
`rWtbOgl5FTU` · AI Engineer · 2026-10-30 · q4 · practitioner · talk · also: evals, token-cost-efficiency, models-research

Vals AI's Rayan Krishnan argues model cards hide a "jagged frontier" by task and metric, and that cost-per-task evals, real-work benchmarks and routing can cut enterprise AI spend without losing output.

- Techniques: Pareto plotting of cost per task vs performance; Report partial credit and fully-correct rate together; Build evals from historical work (PR and issue replay); Sandbox hygiene against reward hacking; Resumable eval infrastructure; Task-level usage-limit right-sizing
- Tools: Vals AI benchmarks (Vals Index, Finance Agent benchmark, Excel modeling / LBO, tax agent), Vals Smith (internal eval-driven coding product), Opus 5.5 (Anthropic), Fable 5.1, Sonnet, GPT 5.6 Sol, Kimi K3

## [We Trust AI Agents That Break Every Day - Shy Ruparel, Temporal](../videos/mJ7q8CuVmbw.md)
`mJ7q8CuVmbw` · AI Engineer · 2026-10-29 · q3 · practitioner · review · also: agent-architecture, observability, token-cost-efficiency

Temporal developer advocate Shy Ruparel argues agent reliability is a state and recovery problem, not a model problem, and demos durable execution resuming a crashed payout workflow with a human approval.

- Techniques: Durable workflow with deterministic orchestration and recorded activities; Human approval as a signal with a long timer; Declare the retry policy once, not in loops; Degrade the AI step, not the transaction; One event history for both debugging and replay
- Tools: Temporal, Qwen (run locally as a 36B and a 9B model, per auto-captions), OpenAI Codex (cited as running on Temporal), Replit Agent (cited as running on Temporal), Keycard (talk referenced, not described)

## [How a Trading Firm Ships New AI Models the Same Day - Noyan Tokgozoglu, Optiver](../videos/aGIUg8zKI8A.md)
`aGIUg8zKI8A` · AI Engineer · 2026-10-27 · q4 · practitioner · talk · also: token-cost-efficiency, evals, multi-agent

Optiver's head of AI engineering on running an AI platform where every decision shows up in P&L within hours: same-day model adoption, token-spend control, and narrowly scoped agents on a shared gateway.

- Techniques: Golden-set benchmarking on day zero; Gateway-first model onboarding checklist; Replace default MCP context with tool search and CLI wrappers; Analyze cache invalidation before tuning cache TTLs; Move reference material out of the system prompt into retrieval; Per-team alerts and self-managed spend limits; Point-in-time tool snapshots with per-invocation confidence; Scope agents narrowly and version them; Ship internal portal with contributions via PRs
- Tools: Claude Code (referenced as the "cloud code" moment in the auto-captions), Codex (OpenAI coding agent; the speaker says it lacked self-hosted managed agents until recently), MCP (Model Context Protocol) servers and MCP tool search, OpenTelemetry (OTEL) logging, Slack client, Internal inference gateway, agent gateway, agent workbench, meta-harness layer, and web portal (Optiver in-house)

## [Why Are We Still Governing AI Agents Like Software? - Tim Tyler, Gravitee](../videos/h8jgniNJcbQ.md)
`h8jgniNJcbQ` · AI Engineer · 2026-10-27 · q3 · intro · talk · also: governance-compliance, security-guardrails

Tim Tyler (Gravitee) argues AI agents should be governed like employees: a unique identity, a named human sponsor, a scoped role and authority, and tiered recourse, with rules as a deterministic floor and intents judged probabilistically.

- Techniques: Three-stage agent accountability model; Scope-lineage delegation check; Deterministic floor plus probabilistic scorecard; Confidence-tiered action ladder; Guardian agents at machine speed
- Tools: Gravitee (AI agent management), Claude (transcribed as 'Clyde'), MCP (Model Context Protocol), FGA policies (fine-grained authorization, generic reference), Mobile device management (MDM, analogy only), Agent accountability framework (agentaccountabilityframework.org)

## [How Bridgewater Turned 100 Million Documents Into an Edge - Sam Green & Aaron Linsky, Bridgewater](../videos/CLve4Nx_RwI.md)
`CLve4Nx_RwI` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: rag-retrieval, product-ux, data-engineering

Bridgewater's Applied AI team describes the Vault, a governed corpus of 100M+ unstructured documents, and the lessons from making it useful to both human investors and agents: separate design for each reader, benchmark-driven search, and feeding agent-human synthesis back into the corpus.

- Techniques: Hand-labelled retrieval benchmark before tuning; Cluster-aware native filtering in the vector store; Infer a time window from the question and scope retrieval to it; Separate human and agent retrieval design; Migrate existing user habits into the new tool first; Write synthesis back into the corpus
- Tools: Turbopuffer (vector database, native filtering), Bridgewater Vault (internal unstructured data platform), Aya (internal artificial investment associate), Pocket Analyst (internal AI analyst), Researcher (internal, next-generation analyst), Forecaster (internal, custom model plus foundation models), Slack, IDE integration, CLI for agents, phone app, enterprise chat client (unnamed)

## [How to Build Financial Agents That Work Across the Web - Jay Sahnan & Arik Bird, Browserbase](../videos/DZ24Xbm9Joc.md)
`DZ24Xbm9Joc` · AI Engineer · 2026-10-25 · q2 · practitioner · review · also: voice-multimodal, sandboxing-execution, data-engineering

Browserbase engineers pitch hosted, forked "verified" Chromium plus the open-source Stagehand SDK for running browser agents at scale on finance portals, with Ramp, Bill and Stripe as case studies.

- Techniques: Accessibility-tree page compaction before the LLM call; Hybrid deterministic plus natural-language browser control; Observe, act, extract as three separate primitives; Schema-first extraction with Zod; Single code path fanned out across many sites; Keep browser processes alive between tasks; Run the agent-side browser controller next to the browser; Copy-prompt onboarding for coding agents
- Tools: Browserbase (hosted browser infrastructure), Stagehand (open-source browser-control SDK built on Playwright), Playwright, Selenium, BeautifulSoup, Chromium (forked; Browserbase's verified build), Chrome, Zod, ngrok (used to share the demo), EC2 (named as the data-center example)

## [Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management](../videos/ZMZlAn6Pyfg.md)
`ZMZlAn6Pyfg` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · also: governance-compliance, evals, mcp-and-tools

A hedge-fund head of AI explains how Contour measures AI ROI: live A/B tests of analyst workflows, process metrics over slow P&L, cost per useful insight, and connector-maintenance time counted as a cost.

- Techniques: Live A/B workflow capture; Agent-synthesized vs analyst-synthesized expert calls; Cost per useful insight; Idea-resurfacing agent; Alt-data via MCP or API connectors into agents; Connector-maintenance time as an ROI line item
- Tools: AlphaSense, Yipit, Rogo, Hebbia, Bloomberg, MCP, APIs (vendor data)

## [Inside Arca's Long-Horizon Agents That Run the Business - Aman Singh, Arca](../videos/oP2WLFpMoDY.md)
`oP2WLFpMoDY` · AI Engineer · 2026-10-24 · q3 · practitioner · review · also: agent-architecture, multi-agent, memory

Arca, an AI-native financial services firm, explains how background agents own multi-day client work through a signal system, shared plan spaces, and human pull-ins.

- Techniques: Signal-driven wake-up with interest registration; Dual wake-up: event plus timed fallback; Treat UI mutations as first-class events; One shared workspace per goal with human pull-ins; Split state by horizon: memory for later, tasks for now; Turn colleagues' reasoning into eval cases; Steer by adding a goal

## [How OpenAI Built ChatGPT for Bankers and Analysts — Joseph Kim, OpenAI](../videos/opHmX7qClzE.md)
`opHmX7qClzE` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · also: product-ux, mcp-and-tools, models-research

OpenAI's Joseph Kim explains how ChatGPT for Financial Services was built on the plugin platform (MCP, skills, artifact tools), why finance lagged in AI use, and his 2027 bets on finance models and persistent agents.

- Techniques: Host and index licensed data yourself, expose it through MCP; Split tool/instruction layer from domain post-training; Firm templates for generated artifacts; Citation viewers for reviewable answers; Plan features around the usefulness threshold; Build on the plugin platform building blocks
- Tools: ChatGPT, ChatGPT plugin platform, MCP (Model Context Protocol), MCP apps, Skills, Codex, Codex desktop app, Excel, PowerPoint, GPT-4

## [A Bank Trained Its Own Foundation Model to Catch Fraud — Freddy Lecue, Wells Fargo](../videos/UB6hoWyh3B0.md)
`UB6hoWyh3B0` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · also: data-engineering, models-research

Wells Fargo built a ~1B-parameter transformer pre-trained from scratch on customer transaction data as a reusable backbone; it beat its production XGBoost fraud model on detection rate and false positives.

- Techniques: Transaction tokenization for tabular data; Raw-field representation instead of hand-engineered features; Decoder-only pre-training on a transaction sequence, then task fine-tuning; Scaling-law sizing with empirical correction; Standard large-scale training recipe; Benchmark against the production GBDT on business metrics
- Tools: XGBoost (production baseline), Transformer / decoder-only architecture, Chinchilla scaling laws, Flash Attention, RoPE, Mixed precision, Distributed data parallel, Activation checkpointing, Muron (auto-caption; likely AWS Neuron), GPU cluster, Wells Fargo transaction foundation model (internal, ~1B params; 11B in progress)

## [Better AI Models Won't Fix Your Engineering Team — Nicholas Arcolano, Jellyfish](../videos/Ve2bAarPA2I.md)
`Ve2bAarPA2I` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · also: token-cost-efficiency, coding-agents

Jellyfish data from ~50k engineers: switching AI models or tools barely moves merged PRs, while skill use, token volume, company and individual engineer effects explain far more.

- Techniques: Natural experiment from a vendor-driven shock; Within-engineer switch comparison; Variance decomposition of throughput; Skill-use level bins over time; Percentile binning of consumption against output; Longitudinal rank-stability check
- Tools: Cursor, Claude Code, Grok, Opus, Sonnet, ChatGPT, Artificial Analysis (model benchmark charts), Jellyfish (engineering telemetry platform)

## [How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada](../videos/c_SPW__jF9w.md)
`c_SPW__jF9w` · AI Engineer · 2026-10-22 · q4 · practitioner · talk · also: evals, rag-retrieval

Air Canada's data science team explains how they built evaluation sets with no public benchmark: generate test cases from known answers, grade them with code, and avoid LLM-as-judge.

- Techniques: Answer-first synthetic eval for retrieval QA; Plant-the-defect known-answer tests; Remove-a-clause mutation test; Template fill-in combinatorics; Invariance tests; Trajectory checks for tool-using agents; Prefer code graders over LLM-as-judge; Strip complexity before adding techniques
- Tools: BM25, LLM-as-judge, Text-to-SQL (mentioned as an example pattern)

## [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](../videos/adfw3xJBx1o.md)
`adfw3xJBx1o` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: mcp-and-tools, coding-agents, sandboxing-execution

Monzo's engineers describe Agent Chip, an in-house coding agent that began as a viral Slack emoji trigger and grew into a sandboxed, MCP-gated platform building block.

- Techniques: Gateway-first MCP layer for internal tools; Isolated sandbox namespace for remote agents; Separate orchestrator from execution; Emoji-reaction prompt trigger in chat; Low-signal incident mode; Proactive impact checks on backend changes
- Tools: Agent Chip (Monzo's in-house coding agent), Slack, GitHub, Linear, MCP (internal MCP gateway server)

## [AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard](../videos/uA4ah-dVHvU.md)
`uA4ah-dVHvU` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: mcp-and-tools, data-engineering, multi-agent

Vanguard's cash-ledger modernization: exposing the legacy codebase over MCP cut a 7-day research loop to 15 minutes, with lessons on migration, idempotent producers and consumer onboarding.

- Techniques: Expose a legacy codebase to agents through an MCP server; Two-stage CDC migration verification; Single write gateway with idempotency for all producers; Consumer access matched to channel; Business-case registration for consumers; Fix forward, do not patch the legacy; Human-readable state values in the new system; Shared team knowledge base
- Tools: MCP server (legacy codebase and migration docs exposed to AI tools), CDC (change data capture, generic), GraphQL (real-time consumer API), Kafka (event topic for inserts and updates), Schema registry (generic, for all consumer channels), Snowflake-style IDs (ID paradigm, not the product), Data warehouse data-share views (batch consumers)

## [One Day, $1,000 in Tokens: An AI War Room for Legacy Code — Ford Prior, GEICO](../videos/DouK81O8R3o.md)
`DouK81O8R3o` · AI Engineer · 2026-10-21 · q4 · practitioner · talk · also: software-factory, multi-agent, context-engineering

GEICO's Ford Pryor describes an AI "war room" for legacy code modernization: a roster of decision makers, a driver, and fleet-managed Claude agents that take a major change from goal to approved design and agent-callable APIs, with human gates along the way.

- Techniques: War room composition for a major change; Three-repo split of enterprise agent context; Goal-to-approval-to-build loop with a queue; Milestone artifacts plus deterministic gate checks; Taxonomy for modernization missions; Local bindings file for agents on a laptop; Cost guardrails for agent-run work
- Tools: Claude Code, Anthropic Code Modernization plugin, Fleet Kit (Anthropic-collaborated fleet manager, markdown rules; not open source yet), beads (per-agent state tracking), Claude artifacts (HTML worksheets), draw.io, Figma, Slack (mission channel), GitHub Issues (example queue), Fable (model, named in the talk), Sonnet 5.5 (model), Opus 4.8 (model, named as too weak for this steering)

## [Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco](../videos/Bz1HFxQA1o8.md)
`Bz1HFxQA1o8` · AI Engineer · 2026-10-20 · q4 · practitioner · talk · also: security-guardrails, governance-compliance, sandboxing-execution

Al Chen (Cisco) on shipping AI into five major banks in weeks rather than a year: CVE remediation with agent-run exploit tests, ClickHouse cross-region DR with data-correctness checks, and keeping PII/MNPI out of LLM-judge reasoning, with showing evidence as the main lever for compliance speed.

- Techniques: Agent-driven exploit verification for CVE remediation (Harbor task); Cross-region ClickHouse DR with backup, restore and correctness checks; Split replication of IDs and metadata from core trace data for residency; Gating LLM-judge reasoning behind a sensitive-data check; Audit the judge prompt, not only the UI
- Tools: Harbor, Docker, Modal, Daytona, ClickHouse, ClickHouse backup (Altinity), Sysdig, Wiz, Prisma, NVD, CISA, MITRE CVE database

## [Buy, Build, Deploy: Using M&A to Drive AI Transformation — Prathik Naidu, Long Lake](../videos/J7n3WJnFTto.md)
`J7n3WJnFTto` · AI Engineer · 2026-10-19 · q2 · intro · talk · also: product-ux, governance-compliance

Long Lake's founding partner explains why buying services businesses and then deploying AI inside them beats selling AI agents from outside, using a J-curve and a services-economy margin argument.

- Techniques: Outcome-ownership screening filter for AI deployment targets; Value-capture math for outside-in AI vendors; J-curve tracking for AI deployment

## [An AI Agent Got Its User Banned From Resy — Keycard, JPMorgan Chase & AAuth](../videos/IavxrdVnwXM.md)
`IavxrdVnwXM` · AI Engineer · 2026-10-18 · q3 · practitioner · panel · also: security-guardrails, governance-compliance, agent-architecture

Panel on intent-based runtime authorization for agents: per-call authz with mission context, budgets instead of rate limits, and enforcement outside the agent. Core claim: coarse OAuth scopes don't fit autonomous agents.

- Techniques: Budget-as-token grant with live feedback; Brains/hands split with egress-proxy enforcement; Separate supervising agent for worker actions; Deterministic must-never policy plus intent-derived bounds; Dynamic tool gating by task phase; Intent and environment in trace spans
- Tools: OAuth, OIDC, MCP, Claude Code, Squid proxy, Chrome, Firefox, AAuth

## [Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs](../videos/W4pnzOURwHQ.md)
`W4pnzOURwHQ` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: data-engineering, evals, governance-compliance

Insurance claims data is messy, so AI claims work needs layered extraction, duplicate detection, human verification, and calibrated tiered benchmarks before cross-claim analytics pay off.

- Techniques: Layered extraction with per-level verification; Tiered benchmark with a private held-out tier; Calibrated multi-judge verification; Back-test on historical samples before pilot; Duplicate and co-mingling detection at intake; Human-in-the-loop surfacing with page references
- Tools: Artificial Analysis MLCR benchmark, GPT models, Anthropic models, ChatGPT, Gemini, Claude

## [AI Agents Cut 3-Day Portfolio Builds to Minutes — Jack McDonald, Apollo & Michael Manapat, Rowspace](../videos/BOWYujhIQuo.md)
`BOWYujhIQuo` · AI Engineer · 2026-10-17 · q2 · intro · interview · also: data-engineering, product-ux

Customer case study: Rowspace agents and an embedded team cut Apollo's portfolio builds from days to minutes and weekly trade recaps from hours to a one-minute report, with trust earned through per-field source validation.

- Techniques: Embedded discovery with domain teams; Per-field source precedence; Agent draft then human refinement; Automate recurring reports, keep human QA

## [The Highest Loop — swyx](../videos/Fva8hFosqyQ.md)
`Fva8hFosqyQ` · AI Engineer · 2026-10-16 · q2 · intro · keynote · also: agent-architecture

swyx's keynote "The Highest Loop" argues that core AI engineering skill is choosing which feedback loop you work in, moving up for productivity and scaling, down for reliability, and that the conference itself is the loop that makes loops.

- Techniques: Loop-level routing

## [Tokens Are the Cheap Part — Steve Jamison, Jellyfish](../videos/U7ZYBCcdJPg.md)
`U7ZYBCcdJPg` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: governance-compliance, token-cost-efficiency, coding-agents

Steve Jamison (Jellyfish) argues AI tokens are a small share of PR cost; tracking total intelligence cost per merged PR, with revert rates as a counterweight, beats watching the token bill alone.

- Techniques: Blended cost per merged PR; Token-spend quintile cohorts; Within-developer baseline comparison; Counterweight metrics beside throughput

## [What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad](../videos/gDRCpTMCqEU.md)
`gDRCpTMCqEU` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: evals, governance-compliance

A technical due diligence checklist for AI productivity claims: check the arithmetic of workload vs. human labor, define what "automated" means, and verify quality with experts before trusting a number.

- Techniques: Workload-vs-labor arithmetic check; Straight-through processing boundary; Blind expert review of grader output; Cost per accepted autonomous task; Diligence questions checklist
- Tools: Faros telemetry, Meta grader study

## [The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale](../videos/-a2oTS9J67U.md)
`-a2oTS9J67U` · AI Engineer · 2026-10-14 · q3 · practitioner · talk · also: governance-compliance, observability

Michele Grant on earning trust in enterprise AI agents: define value, name an accountable owner, and grant autonomy in stages backed by audit evidence, using an M&A integration example.

- Techniques: Pre-deployment value case with baselines; Human work standard (one-page decision map); Deterministic core for financial math; Telemetry as proof, not the model's summary; Four-stage autonomy scorecard; Regression triggers in the model inventory

## [Deploying AI Inside a Bank Is Not an Engineering Problem — Paden Gayle, Applied AI Engineers](../videos/3ZlQk4-knWM.md)
`3ZlQk4-knWM` · AI Engineer · 2026-10-14 · q3 · practitioner · talk · also: governance-compliance, evals

Paden Gayle argues that shipping AI inside a bank is a discovery problem: find the people who own each decision in week one, shrink the scope, limit the model's authority, and build an evidence pack from sprint one.

- Techniques: Week-one decision discovery; Dependency-mapped architecture diagram; Shadow, draft, shrink; Four-rung autonomy ladder; Model proposes, human submits boundary; Five-file evidence pack with failure table; Decision-time record capture; Segment-first evaluation reporting; Five-question readiness scorecard

## [Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire](../videos/rAUyRDOFyHU.md)
`rAUyRDOFyHU` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: agent-architecture, evals, sandboxing-execution

Flywire's engineers describe Orbit, an internal platform that runs deterministic code with small LLM steps, gated by YAML definitions, per-step permissions and human-reviewed merge requests.

- Techniques: Deterministic-first workflow with scoped LLM steps; Strict JSON output schema with targeted retry; Per-step capability allowlist declared in config; Skill first, then workflow; Isolated node evaluation with production-trace golden sets; Per-step model selection; Separate orchestration, runtime and session state
- Tools: Claude Agents SDK, Claude Code, AWS ECS Fargate, AWS Lambda microVMs, GitLab, Jira, Sentry, Slack, OpenTelemetry, MCP, YAML, Victoria (internal PaaS)

## [Reliable, Smart Workflows for Finance, Wealth and Insurance — Karthic Rao, Perpetual](../videos/8g0g1ncwzG0.md)
`8g0g1ncwzG0` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: agent-architecture, governance-compliance

Karthik Rao (Perpetual CTO) on building reliable, regulated wealth-management workflows: an LLM planner emits a typed graph, a deterministic compiler fails closed, and models make only small typed judgments.

- Techniques: Planner emits typed semantic graph, compiler verifies with no model; Closed action grammar with typed contracts; Payload-hash-bound approval gates; Provisional judgments awaiting human confirmation; Side-effect lifecycle with no automatic retry; Rule-based timeouts instead of model decisions; Route judgments to a small tier and log frontier calls as training data

## [We Let Our Financial Planners Write the Agents — Matthew Ragone, Range](../videos/gpmze-6ueGU.md)
`gpmze-6ueGU` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · also: skills-self-improvement, context-engineering, product-ux

A financial planner at Range explains how non-engineers wrote Claude skills that drafts client work, using a five-step method: pick, teach, pack, test, ship.

- Techniques: Five-step skill build method; Narrated walkthrough as skill source; Ask-first and never-do sections in a skill; Background drafting while the expert is busy; Owner plus non-author reviewer for shared skills
- Tools: Claude

## [Hiring Employable Agents + Startup Battlefield Finals — Howie Liu, HyperAgent](../videos/EEt3ZSG4a1s.md)
`EEt3ZSG4a1s` · AI Engineer · 2026-10-12 · q2 · intro · other · also: agent-architecture, multi-agent, product-ux

Howie Liu (HyperAgent) argues agents are moving toward always-on "claws" that humans unblock and orchestrate, then the video covers the Startup Battlefield finals (Kamad, Common.io, Foundry).

- Techniques: Heartbeat re-invocation for always-on agents; Human approval gate on high-impact actions; Correction-to-memory loop; Specialist triage and handoff pipeline; Deny-condition state machine for agent actions; Sandbox VM per agent thread
- Tools: HyperAgent, OpenClaw, Claude Code (workflows, fan-out to parallel agents), FFmpeg, Slack, email, Gmail, Stripe, Salesforce, WhatsApp, Google Docs, GitHub

## [Inside the AI Economy: What Stripe's Data Reveals — Nilofer Rajpurkar, Stripe](../videos/T3wRyXg_yVg.md)
`T3wRyXg_yVg` · AI Engineer · 2026-10-12 · q3 · intro · talk · also: product-ux, mcp-and-tools

Stripe product talk using payments data to show AI companies build fast, sell globally on day one, price by usage/credits, and build enterprise sales early; includes an agent-driven Stripe setup demo.

- Techniques: Agent-driven sandbox provisioning; Clarifying-question recommender tool plus domain skills; Guardrails on sensitive actions; Hybrid subscription plus credits pricing; Unified customer and catalog model across channels
- Tools: Claude Code, Stripe MCP server, Stripe agent skills, Stripe CLI, Stripe Checkout, Stripe Tax, Stripe Link, Intercom Fin

## [Building AIE: Open Q&A and Feedback Session with swyx](../videos/snTZtttfL70.md)
`snTZtttfL70` · AI Engineer · 2026-10-12 · q1 · intro · other · also: product-ux

Open Q&A with swyx after the AI Engineer World's Fair: no AI-safety track, the same venue and size next year, a partner-run country model, the CFP bar, and attendee app feedback. Little engineering content.

- Techniques: Publish conference data as open JSON; Partner-run local meetups with a fixed cadence
- Tools: Twitter, LinkedIn, YouTube, Slack

## [Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI](../videos/PwCSYy-oGsM.md)
`PwCSYy-oGsM` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: evals, governance-compliance, product-ux

Druid AI argues containment rate misleads agent evaluation and proposes a weighted, 0-2 scored framework (six pillars, 26 components) judged like an employee and re-run weekly against a human baseline.

- Techniques: Component scoring with weighted clusters; Mandate-first agent definition; Success criteria attached to each task; Weekly re-run against a human baseline; Hybrid accuracy measurement; Central handoff and action-center check; Skill-source and granularity review; Error tolerance set by mode; ROI as freed human time

## [Let Anyone at Your Company Ship Internal Apps with AI — Garrett Galow, WorkOS](../videos/HTzgC3FoYsI.md)
`HTzgC3FoYsI` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · also: vibe-coding-app-building, governance-compliance

WorkOS's Garrett Galow on a CLI, a Cloudflare-based platform and SSO-by-default that let non-engineers build and ship internal apps; 37% of about 60 apps had no engineer commits.

- Techniques: Pre-flight local setup CLI with template scaffolding; SSO gate on every deployed app by default; Platform abstraction over deploy target; Pair non-engineer driver with engineer consultant in timed hackathons; Push-to-register catalog with shared skills
- Tools: Claude Code, Codex, Lovable, Cloudflare Workers, Cloudflare D1, Cloudflare KV, Doppler, Okta, GitHub, Webflow, Slack, Node.js

## [How a Remote Company Builds AI Fluency — Em Shreve, Automattic](../videos/3XI90A3ENSg.md)
`3XI90A3ENSg` · AI Engineer · 2026-10-09 · q3 · intro · talk · also: skills-self-improvement, mcp-and-tools

Automattic's two-week, in-person AI enablement cohorts (50% facilitated workshops, 50% real project work) and how they scale learning through alumni champions, meetups and a shared MCP and skills hub.

- Techniques: Two-week immersive cohort with a 50/50 split; Living curriculum; Internal MCP server as a shared hub; Tool-agnostic shared skills directory; Champions, regional meetups and ride-alongs; Staged post-program surveys
- Tools: Claude Code, Codex, open code, MCP, Zendesk, WooCommerce, WordPress AI

## [Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel](../videos/XqF-IFHBCkM.md)
`XqF-IFHBCkM` · AI Engineer · 2026-10-08 · q3 · intro · panel · also: software-factory, pr-code-review

Sonar and McKinsey panel on why most companies stall before scaling AI agents in the SDLC, and a staged trust ladder for moving from agent review to fully automated PR merge.

- Techniques: Staged autonomy ladder for agent PR workflows; Derive verification evals from the PRD; Lighthouse teams for best practice; Baseline developer metrics before automation; Write down implicit conventions as explicit specs

## [We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](../videos/pyvRID_CZZU.md)
`pyvRID_CZZU` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · also: agent-architecture, context-engineering, voice-multimodal

AssemblyAI's FDE team built "Joey," a Claude Agent SDK support agent over local markdown docs, lifting end-to-end ticket resolution from 10% to 80% for about $700/month; the talk also argues for dogfooding your own product.

- Techniques: Docs-as-markdown synced into the agent's workspace; Two-stage retrieval: embeddings first, then agentic file search; Guardrail CLAUDE.md as the behavior-tuning loop; Escalation reason taxonomy as a product backlog; PaaS deploy from a Dockerfile for fast fix cycles; Monitoring through the existing support tool
- Tools: Claude Agent SDK, Claude Code, CLAUDE.md, Railway, Docker, Pylon, Voyage AI embeddings, AssemblyAI voice agent API, Slack, WebSocket

## [The State of AI in Software Development: Data from 400+ Orgs — Justin Reock, DX](../videos/Se8jHLliLXE.md)
`Se8jHLliLXE` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: observability, pr-code-review

DX's deputy CTO shares 2025-26 data from 400+ orgs: AI lifts delivery speed only modestly, quality volatility grows, and PR size and falling change confidence are the warning signs.

- Techniques: Cohort-vs-foundational-metric comparison; Utilization, impact, cost framing; Agent feedback as telemetry; Agent-readiness audit; Agent first-pass PR review kept in the PR thread; Bottleneck-first AI adoption
- Tools: DORA metrics, DX platform

## [The Chief AI Officer: Scientist, Architect, Coach — Rania Khalaf, WSO2](../videos/9cJrbj23fOA.md)
`9cJrbj23fOA` · AI Engineer · 2026-10-04 · q3 · intro · talk · also: governance-compliance, product-ux

WSO2's Chief AI Officer Rania Khalaf on running the role as scientist, architect and coach, with adoption-based metrics instead of token counts.

- Techniques: Three-dimension role mapping; LLM-assisted role analysis; Adoption depth ladder; Agent-ready product checklist; Dogfooding with a closed feedback loop
- Tools: Claude, Gemini, BERT, MCP, Databricks

## [The 5 Levels of Self-Driving Production — Eric Schwartz, Traversal](../videos/y-OVWZD4j6U.md)
`y-OVWZD4j6U` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: observability, product-ux

Traversal's PM argues AI coding agents shift engineering time from building to troubleshooting, and proposes a five-level "self-driving production" autonomy scale plus five criteria for judging AI SRE tools.

- Techniques: Five-level autonomy scale for incident response; Five-question checklist for evaluating AI SRE tools; Causal root cause framing for multi-hop incidents; Agent-first incident intake; Alert triage pass before on-call
- Tools: Traversal (AI SRE product; production world model and causal search engine), Claude Code (auto-caption "Cloud Code"), Codex, Cursor, Datadog, Elastic, Splunk, ServiceNow, Slack

## [We're Headed For Superintelligence By 2030](../videos/k-qAht4w9Rg.md)
`k-qAht4w9Rg` · Better Stack · 2026-10-02 · q2 · intro · news · also: models-research, security-guardrails

Better Stack scores the 2025 "AI 2027" forecast against 2026 events: alignment incidents and the junior-engineer squeeze match, while China consolidation and the protests do not, and the authors now push superintelligence to 2029-2033.

- Techniques: Dated prediction scorecard; Use open-weight models as the verifiable size bound
- Tools: AI 2027 (paper), Epoch AI (compute estimates), Indeed (job postings data), GPT-5.3 Codex, Grok 4, Kimi 3, DeepSeek V4 Pro, Claude Haiku, Sonnet and Opus (as named in an Anthropic report), Mythos Preview (Anthropic model, named in a survey), Fable (captioned; model name unclear)

## [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../videos/0I6aoPSRzVc.md)
`0I6aoPSRzVc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: multi-agent, memory, context-engineering

AIDAChip's VP of AIML argues chip-design teams are limited by alignment, not intelligence, and shows a "system of intent" living graph, tribal-knowledge layer and SME agents, plus failure lessons on substrate-level controls.

- Techniques: Living system-of-intent graph with human-gated edits; Rule-based conflict detection instead of LLM-based; Scoped spec hierarchy with file isolation per agent; Block forbidden actions at the system level, not per tool; Alignment-focused evaluation grid; Domain-specific SME agents instead of one general agent

## [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../videos/wdTRsfw0KG0.md)
`wdTRsfw0KG0` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: product-ux, governance-compliance

A former OpenAI go-to-market leader on building automated sales machinery before hiring humans, launching self-serve first, avoiding pilots, and pricing usage instead of seats.

- Techniques: Automation-first go-to-market build-out; Self-serve first, then sales-assisted; Pilot alternatives that keep control of the deal; Trust portal and automated security review; Usage-based pricing with spend controls; Design partner on non-production internal product
- Tools: Clay, Nooks, Microsoft Copilot, ChatGPT Enterprise

## [Your Agreements Are a Database You Can't Query — Hiral Shah, Docusign & Sean Sodha, NVIDIA](../videos/_gvamfT8H-w.md)
`_gvamfT8H-w` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: data-engineering, inference-serving

DocuSign and NVIDIA on turning enterprise agreement PDFs into queryable data, using a small layout-aware table extraction VLM (Nemotron Parse) inside a hybrid OCR pipeline.

- Techniques: Purpose-built small table-extraction VLM; Hybrid two-route document pipeline; Offline-heavy vs online-light compute split; Structured export and API over extracted data; Benchmark on table extraction and track accuracy vs speed
- Tools: Nemotron Parse, Nemotron Retriever, NVIDIA NIM, vLLM, C-RADIO, NVFP4, FP8, Coupa

## [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../videos/Qw_tC68KKes.md)
`Qw_tC68KKes` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, multi-agent, context-engineering

Cloudflare's Justin Joyce on scaling go-to-market analysis with curated skill files, a three-agent report pipeline and a self-service agent workspace; a practitioner account with few hard metrics.

- Techniques: Role-specific skill files with embedded question catalogue; Pre-shaped analytical data for agents; Draft, verify, then tone multi-agent report pipeline; Push generated narratives instead of dashboards; Reviewed central skill catalogue; Per-user persistent agent workspace
- Tools: Cloudflare Workers, Cloudflare Durable Objects, MCP, AI Gateway, Salesforce, Gemini (mentioned as a phone analogy)

## [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../videos/B0fjR3yaZFU.md)
`B0fjR3yaZFU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, evals, agent-architecture

Long Lake co-founder on why AI adoption in real services businesses lags: climb an autonomy ladder, turn real work traces into evals, and co-design with users on-site.

- Techniques: Autonomy ladder rollout; Sandboxed async coding agent with PR output; Traces to ground-truth evals; Diff-based implicit feedback; Post-training on enterprise data; Layered customization; Co-design embedded in existing tools
- Tools: Claude Code, Codex, Claude Cowork, MCP

## [Your Agent Just Authorized What?! — Jay Mok & Ben Coumes, Paypal](../videos/vGn6N4-bxBY.md)
`vGn6N4-bxBY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance

PayPal's Jay Mok and Ben Coumes propose a stakes-and-counterparty matrix for deciding how much proof an agent's payment authorization needs, ending with verifiable mandates for high-stakes, open-ecosystem transactions.

- Techniques: Stakes x counterparty evidence matrix; Scoped, time-bound, amount-capped mandates; Layered selective-disclosure credentials; Pre-authorize intent before the action target is known; Scoped OAuth access to stored credentials
- Tools: Claude Code, FIDO verifiable intents, AP2 mandate, PayPal approval token, PayPal vault, OAuth, Passkeys, GitHub, Jira, Linear

## [Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End](../videos/4loPnxvWWhg.md)
`4loPnxvWWhg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: training-finetuning-rl, context-engineering, evals

A LeaseEnd data scientist explains how fine-tuning an intent classifier for customer texts became costly tech debt, and how replacing it with editable skills and prompts on a frontier model cut fix time from a week to under an hour.

- Techniques: Skill and prompt edits as the default fix; Curated production regression set as the gate; Markdown-file deploys to object storage; Triage gate before retraining; Fine-tuning pre-check list; LLM-judge labeling with manual review and holdout sets
- Tools: Claude Code, Amazon S3, OpenAI, Anthropic

## [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](../videos/WJRdLNhrsLQ.md)
`WJRdLNhrsLQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: pr-code-review, evals

Maven Clinic's CTO-level account of becoming an "AI-native" health company: AI in internal work and product, shorter planning cycles, changed code review, and tiered reliability bars with rubric-based evals.

- Techniques: Staged AI-coding adoption from low-risk tasks; Self-declared review tiers with accountability; Repeated-run pass-rate gating for non-deterministic tests; Rubric scoring plus human spot-checks on live conversations; Per-feature failure tolerance with multi-model agreement and human fallback
- Tools: Cursor, Claude Code, Jira

## [AI in GTM at Notion — Flora Liu](../videos/L4I7WgiEquo.md)
`L4I7WgiEquo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: multi-agent, agent-architecture, data-engineering

Notion's GTM engineer explains a know/decide/act/learn system that unifies sales and self-serve signals, with humans and agents working in one shared context layer on durable workflows.

- Techniques: Four-layer know/decide/act/learn loop; Denormalized key-addressable profile plus keyed unstructured artifacts; Durable workflow per event with engine-managed retries; Parallel research subagents with score-and-select review loop; Single eligibility and routing classifier; Human approval gate by default, untrusted inbound input; Trace every LLM step and log decisions with outcome links
- Tools: Notion, Snowflake, DynamoDB, Temporal, Clay, Gong, Salesforce, Outreach, Nooks, ZoomInfo, Snowflake (product usage), Notion custom agents

## [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../videos/VjEP0xqTUI0.md)
`VjEP0xqTUI0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, data-engineering, mcp-and-tools

Arman Vaziri (Ramp) on building go-to-market orchestration: an internal CDP, durable background agents on Temporal, scoped retrieval, and an MCP that turns employee experiments into productized use cases.

- Techniques: Durable thread with checkpointed activities; Account-scoped hybrid retrieval; Per-agent tool scoping with human pause and resume; System skills plus user text instructions; Nightly per-entity fan-out; Persist derived entity matches; Shared tool surface via MCP plus usage mining; Explore vs exploit with guardrails across channels
- Tools: Temporal, Postgres, Kafka, TurboPuffer, dbt, Snowflake, reverse ETL, MCP, GPT-3.5

## [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../videos/5Bn0xro2ol8.md)
`5Bn0xro2ol8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: testing-verification, coding-agents, context-engineering

Figma engineer on rolling out coding agents across an org: verification-first testing, plan-before-prompt with phase validation gates, and labeling AI-written text so reviewer attention is spent well.

- Techniques: Verification-first agent workflows; Encode agent discoveries as deterministic tests or flows; Testing pyramid for agent-written code; Red-green prompting; Why-first phased plan with validation gates; Human-first labeled communication; Agent-in-thread invitation
- Tools: Playwright MCP, Slack, cloud coding agent (unnamed)

## [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../videos/6pbQgnJ9Voc.md)
`6pbQgnJ9Voc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, mcp-and-tools, security-guardrails

Exa's co-founder argues go-to-market is an AI engineering data problem and shows the internal agents, ICP dashboard, and JeffBot clone that run his GTM team.

- Techniques: Decision-log to eval calibration for a personal proxy agent; Caller-scoped agent permissions; Semantic web search as a segmentation pipeline; API/MCP-first, then customize the SaaS; Signal-triggered alerts on customer events
- Tools: Exa, Opus 4.5, Slack, Salesforce MCP

## [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../videos/M05vON8i0aI.md)
`M05vON8i0aI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, governance-compliance, context-engineering

Imad Touil (QuantumBlack) argues org know-how should live in governed agent skills: a central registry with owners, versions, access control and evals. Ungoverned skills bring duplication, quality decay, security risk and wasted tokens.

- Techniques: Skill catalog with metadata and an MCP search front end; Microservice-style skill design; Progressive disclosure of skills; Runtime composition of regulatory skills into a review workflow; Static skill tests before any evaluation; Individual-to-team-to-platform promotion path
- Tools: Claude Code, Cursor, MCP, Backstage (IDP), GitHub

## [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](../videos/wCIYViPd4SU.md)
`wCIYViPd4SU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, claude-code, observability

Two Sigma explains how it runs cloud agents as each employee's own identity, using a propagated attribution header and enterprise-grounded web search to cut exfiltration risk.

- Techniques: Run agents as the user identity in existing per-user namespaces; Propagate an attribution header like a trace ID; Deny native web tools and route through enterprise grounding; Enforce tool behaviour with existing harness primitives
- Tools: Claude Code, Google Web Grounding for Enterprise, MCP CLI, Kubernetes, Brave Search (native web tool in Claude Code, per speaker)

## [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../videos/pqlWNihgdjI.md)
`pqlWNihgdjI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: coding-agents, context-engineering, testing-verification

Amazon's frontier-dev habits from AWS's Clare Liguori: teams that changed how they worked (context files, self-validating agents, spec-first, local tests) hit a 4.5x median in deployment velocity; tool-only teams got under 3x.

- Techniques: Living steering/skills file with a rule per agent mistake; Self-validating agent loop; Spec-first iteration; Local deterministic mock services; Agent-friendly language and error design; Deployment velocity as the productivity metric; Decision-speed audit
- Tools: Kiro, MCP servers, Bedrock, TypeScript, Rust

## [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](../videos/UyyOoJmuATU.md)
`UyyOoJmuATU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, governance-compliance, evals

Vasant Kearney (Onlay) argues healthcare agents should run on X12 insurance transactions as a public, strict contract that guardrails can reject, with tiered memory and skeptical use of models.

- Techniques: Standard-format tool contract; Strict guardrail rejection per step; Separated, tiered memory; Full-system regression evals before model swaps; Hybrid hard-coded and agentic execution; Write-action audit logging
- Tools: X12, FHIR, EHR, Claude Code, Codex, OpenClaw, Hermes Agent

## [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](../videos/Yphdry8ttAQ.md)
`Yphdry8ttAQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, evals, data-engineering

A seven-step recipe for building vertical AI (finance, pharma) where domain experts in a learning loop, not LLM-as-judge, drive quality and proprietary data is the moat.

- Techniques: Narrow task decomposition; LLM workflow for unstructured-to-structured data curation; Observability traces as the first improvement loop; Domain expert as user in a learning loop; Post-training ladder; AI-in-the-loop reduction of expert time

## [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../videos/yqF6XhzbWBk.md)
`yqF6XhzbWBk` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, context-engineering

Sebastian Fox (Composo) on why LLM judges miss serious clinical-note errors: "which error matters" is tacit and shifting, so keep it as retrieved, case-specific expert judgments and run a discover-capture-calibrate loop.

- Techniques: Failure-mode discovery from production outputs; Free-text expert comments as the raw eval data; Retrieval of similar judged cases into the judge context; Generate-then-check with a narrower checker; Severity vs. detectability map of errors
- Tools: ambient AI scribes (product category discussed), LLM-as-judge with rubric, RLHF (conceptual reference)

## [Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk](../videos/dQ-_i1tZiws.md)
`dQ-_i1tZiws` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, agent-architecture, security-guardrails

Maersk's Dmitry Buykin on running 200+ production shipping agents by turning expert SOPs into executable agent procedures, with a feedback loop that turns each correction into a harness change.

- Techniques: SOP-to-agent conversion; Three-part agent harness; Failure-to-fix mapping; Replay with writes disabled; Trace clustering into heat maps; Composite tools from repeated success; Function-calling tools instead of MCP
- Tools: SME bench (internal triage tool that clusters failures), Function calling

## [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../videos/u6q-byPWUuo.md)
`u6q-byPWUuo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, inference-serving, training-finetuning-rl

Abridge's engineering lead on running clinical AI at scale: clinician-written rubrics feed LLM judges, staged rollouts, and small post-trained models gated by cheap triggers to balance quality, latency and cost.

- Techniques: Multi-reviewer rubric construction for LLM judges; Staged rollout with online feedback for AI features; Task decomposition into small specialised models; Gate cascade for real-time event triggers

## [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](../videos/s-aixZYJG4c.md)
`s-aixZYJG4c` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: pr-code-review, context-engineering, governance-compliance

Qodo's CEO argues human code review will become optional only once teams codify tribal knowledge into a context engine that serves both humans and agents, with per-rule analytics and graduated auto-approve/block.

- Techniques: Rule-linked review comments; Agent-directed PR summary comments; Per-rule analytics for review standards; Learning context from accept/reject history; Graduated auto-approve and auto-block; Service-contract graph for PR impact
- Tools: Qodo, Claude Code, AGENTS.md, CLAUDE.md

## [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](../videos/bdHaOXZOhcM.md)
`bdHaOXZOhcM` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: software-factory, evals, coding-agents

A CTO explains how a manager with a full calendar keeps building by running coding agents overnight (context gathering at 5pm, morning review), using evals and custom-model training as examples.

- Techniques: Overnight agent loop; Context-harvesting prompt; Test-first with end-to-end computer-use verification; Feedback-to-eval hill-climb; Overnight custom-model training with sandboxed cloud access; Prototype branch behind feature flags; Small PRs with an AI reviewer in a clean sub-agent
- Tools: Claude Code, Codex, Cursor, Dia, Wispr Flow, Slack, Jira, Confluence, Notion, SQLite, AWS EC2, ModernBERT

## [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../videos/qqrk7CtkuIw.md)
`qqrk7CtkuIw` · AI Engineer · 2026-09-18 · q3 · practitioner · interview · also: software-factory, coding-agents, pr-code-review

Anthropic's Mike Krieger on how Labs builds: delegate end states to agents, be less constrained with tools, share intent instead of 2,000-line PRs, and run fast persevere-or-pivot cycles.

- Techniques: Describe the end state, then review the trade-offs; Give agents a full environment instead of a narrow tool set; Port-verify-cross-read loop for large code migrations; Capture production runtime types to guide migrations; Share intent, trade-offs and production measurements in place of raw diffs; Tiered review: deep human review for architecture, fix-forward for cosmetic; Agent as a shared teammate in team channels; Instrument before you need it; use flags and dynamic config; Short bets with two-week persevere-or-pivot reviews; Unship primitives superseded by newer ones
- Tools: Claude Code, Claude Design, Cowork, Claude Code artifacts, Bun, MonkeyType, Slack, Python, TypeScript

## [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../videos/zCJtYuqwm7E.md)
`zCJtYuqwm7E` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: software-factory, context-engineering

Patrick Debois (Tessl) argues that scaling coding agents is an organizational problem: teams must shift effort from fixing agent output to improving shared context, harnesses, and platform-owned reusable parts.

- Techniques: Convert skeptic critique into context and harness work; System-level retro; Split planning by agent readiness; Platform-owned reusable registry with a named owner; Per-team cost and iteration dashboards; Three-step AI-friendly hiring loop; Risk-tiered autonomy
- Tools: Claude Code

## [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../videos/DrTdD-ttjCY.md)
`DrTdD-ttjCY` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: product-ux, observability, evals

Snowflake's sales-team GTM agent (6,000 users): launch with quality over coverage, stage the rollout, manage activation, and use question logs as the feedback loop.

- Techniques: Question bank as the first eval set; Narrow-scope, high-accuracy launch; Pilot, beta, GA with metric gates; LLM classification of usage logs; Closed loop from logs to content; Agent instructions under version control with tests; Build on a managed agent platform with inherited access control
- Tools: Snowflake Cowork (formerly Snowflake Intelligence), Cortex Analyst, Cortex Search, Snowflake semantic views, MCP connections, Confluence, Jira, Slack, Gmail, Salesforce, Google Docs

## [Connect AI to Billions of Legal Documents — Simon Eskildsen, turbopuffer & Jacob Lauritzen, Legora](../videos/V-isu4eTHgw.md)
`V-isu4eTHgw` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: rag-retrieval, infra-cost-scaling, security-guardrails

Legora (legal AI) walks through moving project and legal-research search from one Elasticsearch, to Postgres/pgvector, to turbopuffer, one namespace per project on object storage, and why that fits regulated multi-tenant workloads.

- Techniques: Namespace-per-tenant isolation with per-namespace keys and buckets; Partition by access temperature, not by hash; Object-storage-native write path; Round-trip budgeting over object storage; Memory-only cache for encrypted multi-tenant data; Clustered centroid tree for vector search; Two-round-trip inverted index for full text; Fan-out with hierarchy and validity filters for legal research
- Tools: turbopuffer, Elasticsearch, PostgreSQL, pgvector (DiskANN index, transcribed as 'disk NN'), Postgres tsvector, BM25, Amazon S3 (object storage), Google Cloud Storage, Azure Blob Storage, NVMe SSD cache

## [The Half Life of Agent Infrastructure — Ben Kus, Box](../videos/sM1iYgz93HI.md)
`sM1iYgz93HI` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: agent-architecture, evals, rag-retrieval

Box CTO Ben Kus argues AI agent infrastructure has a half-life of months, not years, so teams should build abstractions, gate changes on eval sets, and get good at changing.

- Techniques: Abstraction layer over agent internals; Eval-gated switching; Scheduled stack review; Adaptive model selection; Hybrid lexical plus semantic retrieval with rank fusion; Agentic search
- Tools: Claude, Opus, OpenAI and Anthropic frontier models, open-weight models, BM25, embeddings and approximate nearest neighbor search, MySQL

## [No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle](../videos/jA_x7F8caHI.md)
`jA_x7F8caHI` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: memory, agent-architecture, multi-agent

Oracle's Kay Malcolm argues that agent harnesses need shared, database-backed memory, using a five-type memory taxonomy and a team memory broker; mostly a product pitch for Oracle AI Database.

- Techniques: Five-type agent memory taxonomy; Shared memory broker tied to repo state; Keeping context alongside commits; Single-store consolidation for agent memory; Private local model for memory extraction
- Tools: Oracle AI Database 26AI, Oracle Agent Memory SDK, Codex, Claude, Git, Neo4j, Redis, OCI Always Free

## [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../videos/bMjlRrWjdT0.md)
`bMjlRrWjdT0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, product-ux, observability

DoorDash GenAI platform team on building a cross-functional AI evals platform: UI-first, then API-first, then workflow-first, so non-engineers can run annotation and judge calibration themselves.

- Techniques: Continuous eval loop; API-first eval platform with vibe-coded UIs; Self-serve judge calibration with prompt optimization; Platform-level model choice for judges
- Tools: Claude Code, Codex, DSPy-style prompt optimizer (transcribed as JEPA), MCP, LLM gateway, agent gateway

## [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard](../videos/mav15aW9lLM.md)
`mav15aW9lLM` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: governance-compliance, evals, security-guardrails

Christopher Lovejoy (Anthropic) and Saul Howard (Anterior) argue that enterprise AI agents need audit, data-boundary, escalation and eval primitives designed in from the start, not bolted onto a proof of concept.

- Techniques: Immutable append-only event log as system of record; Event log plus schema-driven immutable blob store; Token-based access at point of use; Human-agent equivalency in the action model; Replay plus human-vs-agent diff as eval; Run evals inside the customer environment

## [The Signal Layer: What to Build When Anything Can Be Built — Lena Hall, Akamai](../videos/1KOdiGgMtpY.md)
`1KOdiGgMtpY` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: product-ux

Lena Hall argues that when AI makes building cheap, value moves to choosing what to build and keeping that choice intact through shipping and marketing, using a thin "signal layer."

- Techniques: Stranger readme read-back check; Promise welded to its limit; Human point of view, AI for the rest; Thin signal layer across handoffs; Hamming list of important problems

## [Building Blocks for Uber’s Software Factory— Uday Kiran Medisetty & Adam Huda, Uber](../videos/17-YSUHo6Lk.md)
`17-YSUHo6Lk` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: software-factory, mcp-and-tools, pr-code-review

Uber's engineers walk through six building blocks (model gateway, MCP gateway, agent devpods, skills marketplace, context graph, Cortana) behind its managed software factory, then show one feature built end-to-end by an agent.

- Techniques: Single gateway with middleware chain and project attribution; Progressive MCP projection (direct, discovery, CLI, generated code); Pre-warmed agent workspaces; Skill marketplace with lint, review and trace feedback; Shared context graph queried before tool calls; Split review between an inner loop and an outer loop; Managed scheduled maintenance loops with bounded output

## [Which AI startups actually land enterprise contracts? — Brian Lewis, Millennium](../videos/7A65O-0lvKE.md)
`7A65O-0lvKE` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance, product-ux

A buyer at a hedge fund explains why most AI startup pilots fail: value, security, reliability and legal gaps, not model quality. He argues most AI-native work is unglamorous data, architecture and change management.

- Techniques: Enterprise-readiness intake checklist for vendors; Verify retention claims in a pilot, not on paper; Gate features by group and by release; Track documentation and terms as versioned artifacts; Set buyer-written success criteria and a 90-day plan that deploys into the buyer's own cloud; Build-versus-buy check on vendor pitches; Breach-response question as a red flag test

## [ChatGPT is in big Trouble (AI Bubble)!](../videos/EK8y8O5st_M.md)
`EK8y8O5st_M` · Kai Explains · 2026-09-02 · q3 · intro · news · also: models-research, infra-cost-scaling

Kai Explains argues that leaked 2025 OpenAI financials, huge compute commitments, and lost enterprise and coding share make ChatGPT's position structurally weak. The figures are reported second-hand, not audited.

- Techniques: Route each job to the cheapest model that meets its quality bar; Judge AI vendor health by unit economics, not user count
- Tools: ChatGPT, GPT-5, GPT-5.4, Gemini, Gemini 3, Claude, DeepSeek, Kimi, AWS Bedrock, Azure AI Foundry, Google Vertex, Sora

## [YC Just Open-Sourced Its Multiplayer Harness](../videos/GrZ-X3-2TVs.md)
`GrZ-X3-2TVs` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: agent-architecture, security-guardrails, coding-agents

Better Stack's hands-on tour of YC's open-source "multiplayer" agent harness (QM): a self-hosted, multi-user web app with Slack access, per-workspace containers, a seven-tool surface and org-level approval modes. Promising but two weeks old.

- Techniques: Minimal primitive tool surface plus shell sandbox; Org ceiling with per-team tightening and a posture-independent command deny list; Enable extra harnesses through the admin API; Share context through a team project, keep credentials private by default
- Tools: QM (YC open-source multiplayer agent harness; the caption spelling may be off, and the repo was about two weeks old at the video date), pi (the default agent harness in QM), Claude Code (can be enabled as a harness inside QM), Slack (integration surface), PostgreSQL (session history), GitHub (repo linked in the description)

## [This Is How Forward Deployed Engineering Is Actually Done](../videos/AD-EmZ3v6-g.md)
`AD-EmZ3v6-g` · AI LABS · 2026-09-02 · q2 · intro · tutorial · also: product-ux, evals, mcp-and-tools

How to do forward deployed engineering: audit a business process before building, sort each step into software, model or human, then eval against real cases. Useful method, but includes a sponsored segment and unsourced stats.

- Techniques: Shadow-and-document the process; Three-filter triage per step; Connect to existing systems instead of migrating; Keep process steps visible with checkpoints; Labelled-case eval loop; Value-and-error-cost accounting; Process audit as the first deliverable
- Tools: Claude Code (used for the internal chatbot case study), MCP (Model Context Protocol), Notion (named as the example system for MCP connection), Slack, Cursor (as a company example), OpenAI (as a company example), Anthropic (as a company example), Dex (job-matching sponsor; named in a sponsored segment)

## [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../videos/ZTA0GwpAUak.md)
`ZTA0GwpAUak` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: training-finetuning-rl, coding-agents

Samuel Denton (Applied Compute) lays out a 2x2 of offline/online hints and traces for distilling production agents, with SWE-bench and hyperlink-format results showing online hints win on on-policy behavior.

- Techniques: Offline hint on offline production traces; Turn-budget nudge hint; One-step on-policy rollout from an offline trace; Online hint from each rollout; Judge-chosen hint placement with next-step distillation; Relevance-mass token selection (self-distillation)
- Tools: SWE-bench, Qwen 3.5 (thinking model)

## [Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla](../videos/B8l81jhvHbI.md)
`B8l81jhvHbI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, memory, evals

Ishita Daga (Tesla) argues enterprise data agents fail from ambiguity, staleness and team-level preference, not model size, and proposes a tiered source-of-truth structure, a context lifecycle, and open questions on preference.

- Techniques: Tiered source-of-truth hierarchy; Context lifecycle with live sources and event logging; Replay-based evaluation of recent questions; Metric variants in a semantic layer with user selection
- Tools: mem0, Tableau, dbt, GitHub, memory.md files

## [Build Evals That Actually Matter - Nick Ung & Akshay Sharma, Lyft](../videos/3z2uT5aDx_Y.md)
`3z2uT5aDx_Y` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, observability

Lyft's customer-support agent team on building offline simulation evals, calibrating LLM judges on hand labels, and closing the loop from error analysis to agent changes.

- Techniques: Simulated multi-turn offline eval; Mixed eval dataset from production samples plus mutations; User simulator realism calibration; Binary task-outcome rubric per metric; Judge calibration as a classifier; Confidence intervals and paired comparisons; Annotation queue for domain experts; Config-driven eval harness
- Tools: LangSmith, Langfuse, DeepEval, LangGraph, tau-bench (transcribed as CowBench, from Sierra)

## [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../videos/vSx5IULvBns.md)
`vSx5IULvBns` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, observability

Resolve AI engineer argues production ops, not coding, is the bottleneck, and shows always-on cloud background agents that run on schedules, events and messages, with deployment monitoring as the lead use case.

- Techniques: Trigger-typed background agent; Per-change check plan generated from the diff; Time-bounded watch with agent-chosen duration; Confidence-gated reply with human confirmation; Feedback in the thread edits the standing task; Expose agent capabilities over MCP
- Tools: Slack, Microsoft Teams, GitHub release tags, Kafka, CI/CD pipelines, feature flag systems, MCP servers, Granola

## [How Forward Deployed Engineering is done at Cognition — Jia Wu](../videos/RVxym6mmIns.md)
`RVxym6mmIns` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: product-ux, software-factory

Jia Wu (Cognition) on forward-deployed engineering: embed in enterprise customers, map Devin to real backlog problems, and measure outcomes from agent sessions. Mostly a company pitch, with some case-study numbers.

- Techniques: Session-based value measurement; Event-triggered agent automation; Map backlog to capabilities; Before/after delivery metrics; Autonomous legacy migration
- Tools: Devin, Devin Cloud, Windsurf, Claude Code, Cursor

## [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](../videos/l0FLhNqBOic.md)
`l0FLhNqBOic` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: product-ux, training-finetuning-rl, rag-retrieval

Varick Agents explain why process understanding, not model execution, is now the bottleneck, and describe the forward-deployed engineering agent they built for it.

- Techniques: Failure-path process interviews; Per-step autonomy split; Dependency graph as shared state; Post-training an open model for analysis style; RL environment with domain traversal tools; Assistant embedded in the authoring tool
- Tools: Varick OS (in-house platform), Claude, Codex, Granola, Kimi (open-source base model, named as K2.6), NetSuite, Microsoft Dynamics, SAP, Salesforce

## [Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute](../videos/k35LeKZEhiE.md)
`k35LeKZEhiE` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, agent-architecture

Raymond Feng (Applied Compute) on post-training agents that learn on the job: how RL loops break when you do not own the harness, and the environment-fidelity failures that teach models bad habits.

- Techniques: Replayable sandbox for multi-rollout RL; Graded chats as the only training interface; Audit the environment for infrastructure failures before trusting a run; Log model requests and responses as the training source; Mine traces for failure modes, then build the dataset

## [Your Moat Is Your Data Model — Mike Phipps, Gates Foundation](../videos/jt1Pbr_n6oU.md)
`jt1Pbr_n6oU` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: data-engineering, mcp-and-tools

Mike Phipps (Gates Foundation) explains why the Strategic Intelligence Platform's defensible asset is a knowledge graph of tacit process knowledge, served to agents through MCP rather than a custom chat UI.

- Techniques: Tacit-knowledge-first data modeling with data owners; Graph with explicit hierarchy types and precomputed roll-ups; Cross-system entity stitching; Document chunks as graph nodes with full-text plus graph retrieval; Curation pipeline before the graph; Expose the graph as an MCP server with state passthrough; Per-question graph-query ground truth plus stability checks
- Tools: Neo4j, MCP, Claude, ChatGPT, Cowork

## [How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh](../videos/1OMHGsUZiqA.md)
`1OMHGsUZiqA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: product-ux, data-engineering

Vinoo Ganesh on running forward-deployed engineering as a product strategy: go on site, solve small problems fast, define shared terms, and avoid shipping hacks that become permanent.

- Techniques: Three-question discovery before building; Ship-it threshold for small problems; On-site workflow observation; Pain-signal scan; Canonical glossary and ontology; Production-readiness gate for quick fixes
- Tools: Palantir Foundry, Cassandra, Parquet, S3, Groovy, Elasticsearch, Snowflake, Databricks, Tableau, SAP, Slack

## [Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates](../videos/u6jJcIFDLE4.md)
`u6jJcIFDLE4` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: multi-agent, agent-architecture, context-engineering

ZS Associates explain why their multi-agent pharma analytics pipeline failed and how they rebuilt it: deterministic signal detection, one reasoning agent, and a knowledge graph used as a control plane.

- Techniques: Probe the design with a coding agent; Deterministic signal gate feeding an investigator agent; Single reasoning owner with scoped investigation subagents; Knowledge graph as the agent's control plane; Hypothesis-traversal investigation loop
- Tools: Claude Code, bash, knowledge graph (tool not named), relational database (not named)

## [Notion's Token Town — Sarah Sachs, Notion](../videos/-I5W5QVAT8E.md)
`-I5W5QVAT8E` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: token-cost-efficiency, infra-cost-scaling, security-guardrails

Notion's head of AI engineering on keeping AI costs sustainable: stay model-agnostic, route traffic by task difficulty, use open-weight and plain code for simple steps, and evaluate whole trajectories instead of single calls.

- Techniques: Model-agnostic harness with an auto-router; Traffic tiering by task difficulty; Trajectory-level eval of cost, latency and success; Open-weight evaluation on your own system; Code and CLI for deterministic steps; Cross-vendor review chain for agent PRs; Lethal trifecta check on agent systems
- Tools: Claude Code, Claude, Codex, Decagon, Parallel (web search provider), Notion Workers, Notion AI Manage Agent, Kimi 2.6 (as transcribed), GLM 5.2 (as transcribed), GPT 5.2 (as transcribed)

## [How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh](../videos/Tt2kX2sgQio.md)
`Tt2kX2sgQio` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: governance-compliance, data-engineering, agent-architecture

Kepler's CEO argues finance AI needs a deterministic substrate: the model points to sources and decides what to compute, while code extracts, checks and calculates numbers, with replayable derivation chains.

- Techniques: Atomic provenance ledger; Model decides, code computes; Derivation chains for derived metrics; Deterministic sanity gate on model output
- Tools: Claude, XBRL, ChatGPT, GLM 5.2, Opus 4.8

## [The Dirty Secret of Forward Deployed Engineering — Natalie Meurer, Sierra](../videos/Byv311hdoHE.md)
`Byv311hdoHE` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: product-ux

Sierra's head of agent engineering traces forward-deployed engineering from Palantir's 2008-2020 eras to today, argues the title is vague, and says customer accountability and outcome pricing make most engineering roles trend toward it.

- Techniques: Write-back dashboards; Ontology-first data modeling; Customer-accountable build loop; Outcome-attribution test for pricing; FDE vintage interview question
- Tools: Palantir Foundry, Palantir AIP, Palantir Slate, AWS EC2, Airbus Skywise, Retool (comparison only)

## [How Forward Deployed Engineering is done at Ramp — Leo Mehr](../videos/ITMXwI6QL6A.md)
`ITMXwI6QL6A` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: software-factory, evals, context-engineering

Leo Mehr (Ramp) on forward deployed engineering: scope hard before building, then replace each FDE pipeline stage with agents, with evals and good context as the hard parts.

- Techniques: Scoping questionnaire before any build; Clarifying-question intake agent before spec; Stage-by-stage agent factory for the FDE lifecycle; Per-stage quality checks with evals, rubrics and human feedback
- Tools: Notion, Notion Agents, Slack

## [Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind](../videos/O72p-rBb2bA.md)
`O72p-rBb2bA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, security-guardrails

SonderMind engineers describe the guardrail, eval and clinician-annotation loop behind Sonder, a clinically grounded mental health AI coach, and open-source 300 scenarios for it.

- Techniques: Pre- and post-LLM guardrail sandwich; Trace-to-typed-eval annotation loop; Multi-metric guardrail scoring
- Tools: Sonder (SonderMind's clinical AI coach), LLM-as-judge guardrail calls, CI-gated eval suite, annotation queue with trace replay, analytics and alerting platform

## [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](../videos/kiqubc5b5Yo.md)
`kiqubc5b5Yo` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: multi-agent, evals, agent-architecture

Morgan Stanley's AlphaLab, a multi-agent harness that automates quant research through research, critic-checked eval building, and Kanban-style experiments. Its main lesson: the value sits in strict eval environments and rubrics, not in the harness.

- Techniques: Scaffolded to-do list with re-prompting on early exit; Builder plus critics eval loop; Strategist, worker, and post-mortem Kanban loop; Containerised, Kaggle-style eval contract; Environments as RL reward signal; Rubric grading of each rollout's process; Meta-harness optimisation by an LLM; Provider-agnostic harness with functional tool calls
- Tools: Claude Code, Codex, Opus 4.5, Slurm, Kaggle, GRPO, NVIDIA Nemotron

## [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../videos/aeTb5BdmTTc.md)
`aeTb5BdmTTc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, coding-agents, skills-self-improvement

How a 10-person team got to shipping with coding agents: treat agent setup as a leadership job, share the best practices, invest in one high-value skill, and close the loop on slop.

- Techniques: Thin CLAUDE.md/AGENTS.md index; Skill as a folder with a short SKILL.md; Runbooks in code comments as discovery hooks; One end-to-end ship-it skill; Nightly code-gardener agent; Shared setup with an opt-out for experiments; First-prompt context audit
- Tools: Claude Code, CLAUDE.md, AGENTS.md, CI/CD, issue boards

## [How Forward Deployed Engineering is done at Decagon — Sunny Rekhi](../videos/7wu2hsRfvV0.md)
`7wu2hsRfvV0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: product-ux

Decagon's CTO of Forward Deployed Engineering explains how FDEs configure enterprise AI support agents, funnel customer asks into the product, and productize repeated custom work as the company grew from 50 to 500 people.

- Techniques: Define success in writing at scoping; Productize on repetition (the 25th-integration rule); Field-to-product feedback loop; Same-vertical deal staffing; ROI-ranked first automation; Natural-language configuration as a platform rule; Two-lane split for scaling agent work
- Tools: Decagon, Codex, Claude Code

## [How Forward Deployed Engineering is done at Factory — Eno Reyes](../videos/wpOA-UXynoM.md)
`wpOA-UXynoM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, testing-verification, product-ux

Eno Reyes (Factory CTO) on forward-deployed engineering as the way to build software factories. The bottleneck is agent readiness, meaning deterministic validators in the codebase, not model capability.

- Techniques: Audit validation loops before deploying agents; Bounded long-running harness with an explicit definition of done; Map the signal-to-deploy stages per org; Land-and-expand with a reference implementation; Split automation into one-click fixes and workflow changes; Model-independent harness with owned traces and self-hosted deployment
- Tools: Factory Droid, Missions, LegalDroid, linters, type checkers, security scanners, end-to-end test suites

## [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../videos/7vn4WpqNpck.md)
`7vn4WpqNpck` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: coding-agents, evals

Denys Linkov (Wisedocs) on whether a six-month monorepo refactor of a medical-claims ML pipeline was worth it when coding agents keep improving, and how to measure agent reliability.

- Techniques: Time-horizon reliability check before long runs; Agentic tool-evaluation pipeline; Monorepo consolidation for agent-driven work; Human PRs as a context-building step; Check hidden assumptions in dependencies; Layered refactor instead of a full rewrite
- Tools: Cursor, Temporal, Claude Sonnet 4.6, Claude Opus 4.8, o3, GPT-5.5, Confluence, Claude Code plan mode

## [Build the AI GTM Agent That Knows the Buyer - Dr. Sajjan Kanukolanu, Position2 (Position Squared)](../videos/ltv-L5oMPIs.md)
`ltv-L5oMPIs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: multi-agent, data-engineering

Position Squared's three-layer, multi-agent GTM system (anonymous visitor ID, knowledge-base-gated ICP and CRM matching, rep actions). Lessons: ICP drift, alert fatigue, weak identity accuracy, and approval friction.

- Techniques: Dedupe-then-enrich identification; Knowledge-base-gated ICP filter agent; Per-person context graph with account and deal rollup; Separate fit score from intent score; Personalized returning-visitor chat; Quarterly ICP refresh from closed outcomes; Alert budget tuned to rep capacity; Auditable, adjustable policy engine; One-click draft approval with a 30-second budget
- Tools: HubSpot, Slack, LinkedIn

## [Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE](../videos/KwhgfwOSToQ.md)
`KwhgfwOSToQ` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: product-ux

Kevin Bai (Anthropic, ex-Palantir and Rippling) explains the forward deployed engineer role: when to use it, why it needs a shared platform, and how to scope bespoke versus generalizable work.

- Techniques: FDE fit test before adoption; Bespoke vs generalizable split; Two engineers per customer project; Granularity of primitives matched to user base
- Tools: Palantir Foundry

## [SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)](../videos/KMR_RBoCa4M.md)
`KMR_RBoCa4M` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, data-engineering

Nubank and Snowglobe claim simulated personas with mocked tools produce agent eval data on demand, cutting release cycles from weeks to hours, provided the sim-to-real gap is measured.

- Techniques: Simulated-user eval set generation; Persona-consistent grounding state; Sim pre-screening before A/B tests; Sim-to-real calibration; Same-harness model sweep
- Tools: Snowglobe SDK, LLM-as-judge, Automated prompt optimization (captioned 'JEPA', likely GEPA)

## [Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit](../videos/Owb8g3yDyzo.md)
`Owb8g3yDyzo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, evals

Intuit's Udi Menkes argues frontier LLMs give fluent but unverified money advice, and that grounding a model in real business outcomes (state, action, outcome) beats model size.

- Techniques: Outcome-grounded trajectory dataset; Propose-then-rank split; Propensity-matched uplift estimate; Evidence-grounded explanation; Long-horizon simulation with a rules baseline
- Tools: QuickBooks, TurboTax, Credit Karma, Mailchimp, reinforcement learning (Intuit in-house model)

## ["The biggest challenge in your stack? Evals, Evals, Evals" - 2026 State of AI Engineering results](../videos/RGe6EjucbzI.md)
`RGe6EjucbzI` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: evals, models-research, infra-cost-scaling

Bar Yeren (Amplify) reads out the 2026 State of AI Engineering survey (1,048 respondents): evals remain the top challenge, teams run multi-model stacks, cost is a first-class constraint, and agents now mostly have write access.

- Techniques: Intent-to-adopt ratio; Routing by task type across models; Monitoring cost and token usage alongside quality; Human-in-the-loop approvals and permission gating for write-enabled agents
- Tools: Notion, Vercel, Nano Banana, ChatGPT Images 2.0

## [AI Can Do the Work, But It Can't Do the Understanding | Better Stack Podcast Ep. 18](../videos/nfX_SQYDoBI.md)
`nfX_SQYDoBI` · Better Stack · 2026-08-02 · q3 · practitioner · interview · also: data-engineering, sandboxing-execution, token-cost-efficiency

Better Stack podcast with Marimo's Vincent on why AI can produce code and analysis but not understanding: keep humans in the loop, care about the code, and be wary of hype.

- Techniques: Notebook scratchpad for LLM introspection; Incremental cell generation with a human in the loop; Scrubbable numeric literals for live tuning; Per-tool-call allow/deny for agent sandboxes; AnyWidget for browser-side widgets in Python notebooks; Shuffle test before trusting an A/B harness; Hypothesis-free first pass on a dataset; Supply-chain surface reduction for Python; Measure LLM agreement before automating a decision; Write flashcards yourself
- Tools: Marimo (Python notebook), Molab (Marimo notebooks with GPU), Google Colab, Jupyter, Observable, AnyWidget, Polars, NumPy, scikit-learn, spaCy, D3, Lua

## [500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic](../videos/UcYoMg-8-L8.md)
`UcYoMg-8-L8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: vibe-coding-app-building, product-ux, coding-agents

Automattic's 30-day "Radical Speed Month" experiment, in which about 500 people in paired teams shipped roughly 794 projects, and how the speaker moved from designer to design engineer by prototyping in code before Figma.

- Techniques: Time-boxed paired ship sprint; Prototype-in-code before design tool; Shared file-based exploration log; Aggregating scattered sources into a status tracker; Engineer as enabler in mixed-skill pairs
- Tools: Claude Code, Figma, Storybook, GitHub, Nano Banana, Context MCP server, WordPress.com, Jetpack, WooCommerce

## [Every company should have a Brain — Garry Tan, Y Combinator](../videos/eBUyTS7SzV4.md)
`eBUyTS7SzV4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, memory, skills-self-improvement

Y Combinator's Garry Tan argues that AI productivity comes from how work is wired (skills as employees, routing tables, company memory with hygiene), not the model, and pitches an open-source "company brain" called GBrain.

- Techniques: Skill file as a single-job employee; Resolver table for routing context; Trigger evals on routing; Skillify at task end; Split latent and deterministic compute; Curated company brain; Select a small working set per task
- Tools: Claude Code, Codex, OpenClaw, Hermes agent, GBrain, Postgres, TypeScript, Markdown skill files

## [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../videos/ObTPqBGsEbA.md)
`ObTPqBGsEbA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: evals, observability, governance-compliance

A five-pillar playbook (evaluation, tracing, data foundation, orchestration, governance) for taking enterprise AI agents to production, illustrated with a retail banking chatbot case study.

- Techniques: Business-metric eval spec before build; Living golden eval set seeded from human answers; Three-layer eval stack; Automated eval pipeline with human review threshold; Trace-driven duplicate-call detection and retry cap; Tiered CI eval runs; Prompt versioning as change management; Model selection on your own eval set; Incident playbook: detect, diagnose, contain, fix, regress
- Tools: Databricks, MLflow, Delta Lake, Apache Spark, Unity Catalog, Genie, Agent Bricks, Databricks Apps, Mosaic AI, Git, Python, LLM-as-judge

## [6 Things to Know about AIE World's Fair 2026](../videos/0S8xe9ftGTM.md)
`0S8xe9ftGTM` · AI Engineer · 2026-07-18 · q1 · intro · other · also: product-ux

Swix's promo-style update on AIE World's Fair 2026 (July, Moscone West): bigger show, new tracks, leadership and vertical focus, and expo/networking tips. No technical content.

## [AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent](../videos/Iwe_RY-fYgI.md)
`Iwe_RY-fYgI` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: governance-compliance, data-engineering

Varsha Shah proposes a framework that correlates records across payroll, tax, procurement and finance systems with graph-based entity linking, adaptive risk scoring and jurisdiction normalization to catch compliance fraud that per-document checks miss.

- Techniques: Cross-document entity graph for compliance; Multi-signal risk scoring instead of single rules; Outcome feedback loop; Normalize before scoring across jurisdictions

## [Your AI Product Will Fail Unless You Can Explain It - Veronica Hylak, Hey AI](../videos/d_Ftrl3vfV0.md)
`d_Ftrl3vfV0` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: product-ux

Short pitch-craft talk: explain an AI product by opening with the user's pain, tying it to a picturable story, and showing a concrete before/after.

- Techniques: Wound-first opening; Viral-story anchor; Picturable-phrase rule; Before/after transformation with numbers
- Tools: Devin (cited as an example of a picturable product name), McDonald's AI drive-through clips (cited as a viral story example)

## [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](../videos/whue9_YquGA.md)
`whue9_YquGA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: software-factory, multi-agent, pr-code-review

Angie Jones (Block) describes moving a 3,500-person engineering org to autonomous agent delegation via a maturity model, a power-user champions program, AI-ready repos, and an orchestrator.

- Techniques: Stage-based maturity model for agent use; Champions program of hand-picked power users; Layered repo context files; Delegation from the tools people already use; Review agent plus auto-fix loop; Isolated cloud workspace per agent; Machine-readable system map for orchestration
- Tools: Claude Code, Goose, Codex, BuilderBot, GitHub, Jira, Linear, Slack, MCP, AGENTS.md, CLAUDE.md

## [Forward Deployed Engineering at Cursor — Pauline Brunet](../videos/APqXGyCoGW4.md)
`APqXGyCoGW4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: product-ux

Cursor's forward deployed engineering lead on where FDE fits, whom to hire, and how to scope short, ROI-driven customer projects without drifting into staff augmentation.

- Techniques: FDE placement matrix; Staff-augmentation check; Success defined before build; Directional six-week phased scope; Three-bucket ROI statement; Mission statement for the FDE team
- Tools: Cursor, Cursor SDK, Cursor cloud agents

## [Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](../videos/4uFVSLgD2Q4.md)
`4uFVSLgD2Q4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, evals, sandboxing-execution

OpenGov's Gabe De Mesa on how they built and scaled OG Assist, an in-product agent: an in-house Effect-native agent loop, A2A contracts, approval gates, ephemeral sandboxes, and rolling-summary context.

- Techniques: Effect-native agent loop with injected language model; A2A agent card as the API contract; Deterministic approval interrupt; Automated tool-call evals in CI; Ephemeral sandbox per agent task; Rolling summary with recent-window and recall; Runtime generative UI via registered primitives; Tools to toolkits to model registration
- Tools: Effect, Effect AI, LangGraph, A2A protocol, A2UI, Claude, Cursor, Claude Cloud Agents

## [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](../videos/OXMMN-XbxwA.md)
`OXMMN-XbxwA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: pr-code-review, context-engineering, agent-architecture

Higharc's labs team on moving ML research prototypes into production via three levers: a design-doc-style "research prototype taxonomy," a decoupled Python microservice monorepo, and stacked-PR decomposition for review.

- Techniques: Research prototype taxonomy (RPT) doc; One researcher, one decoupled microservice in a shared monorepo; Slice by dependency graph, then stack PRs; Use the design doc to plan the merge; Notebooks on Modal for GPU experiments
- Tools: Notion, Graphite, GitHub Actions, Modal, Docker, FastAPI, Poetry, uv, Jupyter

## [WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar](../videos/8G_1-3IO4ZQ.md)
`8G_1-3IO4ZQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, memory, skills-self-improvement

Atlan's founder argues production agents fail on missing business context, not model intelligence, and proposes a shared, versioned "context layer" (a company brain) that agents draw from.

- Techniques: Jobs-to-be-done scaling factor for agent selection; Shared context layer as a company brain; Context lifecycle management like software; Trace-driven maintainer loop; Reverse-construct the data stack to bootstrap context
- Tools: Claude Code, Codex, Claude Cowork, Google ADK, Glean, Relevance AI, MCP, Qualified, Artisan

## [The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft](../videos/jtzh-GBXBWc.md)
`jtzh-GBXBWc` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: multi-agent, memory, skills-self-improvement

A 100-person Indian thermoforming-machine maker built a 36-agent go-to-market "brain" with layered memory and a nightly dream cycle, with no training and no framework. The talk is a company story with some architecture and cost claims.

- Techniques: One-job specialist agents with an orchestrator and debate; Layered agent memory with a salience gate and correction precedence; Nightly consolidation (dream cycle) job; Rules file as production guardrails; Chunk-and-extract over a private corpus with no training; Draft-only outbound with human send
- Tools: Cursor, vector database, graph database, CRM, Google Workspace integrations, document ingestion tooling, monitoring tooling

## [AI passed every benchmark… then failed at real work](../videos/7s2IIIP47GM.md)
`7s2IIIP47GM` · Kai Explains · 2026-07-02 · q2 · intro · other · also: evals, coding-agents

Opinion piece arguing AI coding tools look strong on benchmarks but fail on open-ended, underspecified real work, and that failures are quiet. Recommends measuring shipped outcomes and keeping humans on costly decisions.

- Techniques: Outcome-based tool evaluation; Human gating by cost of error; Evaluate on your own codebase and problems
- Tools: Claude Code (transcript says "Clawed code"), GitHub Copilot, Gemini CLI, Cursor

## [Genesis Eno, Unitree H2 Plus, Atlas In Factory, Figure AI 1 Robot/Hour, Humanoid-GPT & More AI News](../videos/laFa8sZ5CFU.md)
`laFa8sZ5CFU` · Kai Explains · 2026-07-02 · q2 · intro · news · also: models-research, voice-multimodal

Weekly robotics news roundup from Kai Explains: Genesis AI's Eno robot, Unitree H2 Plus, XPeng, Figure's production scale-up, Boston Dynamics Atlas at Hyundai, and HumanoidGPT and Deep Robotics DR02 demos.

- Techniques: Multi-expert RL distillation into one motion-tracking policy (HumanoidGPT); Lightweight fine-tuning for out-of-distribution motions; VR teleoperation demonstrations as training data (Atlas); Fleet telemetry feeding model training (Figure Helix); End-of-line functional test gating with burn-in (Figure BotQ); Visible intent display for robots working near people (Eno cognitive interface)
- Tools: Genesis AI Eno, Gene (Genesis AI model), Unitree H2 Plus, NVIDIA Jetson Thor, NVIDIA Blackwell GPU, Sharpa Wave tactile hands, NVIDIA Isaac GR00T (transcribed 'Isaac Groot'), NVIDIA Isaac Sim, NVIDIA Isaac Lab, NVIDIA Isaac ROS (transcribed 'Isaac Ross'), XPeng iron humanoid, Figure 03

## [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](../videos/iUWwcG-C8OU.md)
`iUWwcG-C8OU` · AI Engineer · 2026-06-18 · q4 · practitioner · demo · also: data-engineering, agent-architecture, context-engineering

WorkOS product lead Garrett Galow demos Studio, an internal agent that answers business questions and turns repeat questions into live widgets. Main lessons: pre-flight checks, runtime tool context, query validation, and keeping the LLM out of widget refresh.

- Techniques: Generated declarative widgets; Pre-flight checks and clarifying questions; Runtime tool-context injection; Layered prompts; Distrust model priors for product facts; Execute-and-validate before deploy; Org-level connectors with role-based defaults
- Tools: Snowflake, Linear, Notion, Convex, LangGraph, Claude Opus, Slack bot, Retool, WorkOS Pipes

## [Personalization in the Era of LLMs - Shivam Verma, Spotify](../videos/5YSJEP0HWzM.md)
`5YSJEP0HWzM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: training-finetuning-rl, context-engineering

Spotify's AI Foundation tech lead explains how it personalizes recommendations with user embeddings, semantic IDs for catalog items, and soft user tokens fed into a fine-tuned open-weight LLM.

- Techniques: Semantic ID tokenization of item embeddings; Soft user token injection; Tokenized listening-history prompting for domain adaptation; Daily batch user-embedding generation; User-editable text profile as a steering signal
- Tools: Llama, Qwen

## [Does GenAI "belong" to data scientists? — Phil Hetzel, Braintrust](../videos/NKwIX3CiRgU.md)
`NKwIX3CiRgU` · AI Engineer · 2026-06-18 · q2 · intro · talk · also: evals, product-ux

Phil Hetzel (Braintrust) argues GenAI agent work should not belong only to data scientists or ML engineers. He says it needs a diverse product team, with domain experts shaping prompts and eval, and data scientists supplying rigorous eval discipline.

- Techniques: Judge calibration against human labels; Production traces feed the offline eval set; Domain-expert trace annotation; Prompt playground for non-engineers; Functional eval over technical metrics
- Tools: Braintrust

## [Bounded Autonomy: Between Free Will and Determinism — Angus J. McLean, Oliver](../videos/t4359sKBu4w.md)
`t4359sKBu4w` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: context-engineering, agent-architecture

An ad-agency AI director argues for "bounded autonomy": treat LLM context as a soft constraint, keep systems simple, store knowledge in several representations, and never automate work you cannot do yourself.

- Techniques: Self-imposed context budget; Curated documentation over open web access; Simple-first prototype with fast reality checks; Multi-representation knowledge storage; Cluster-then-report pipeline; Teach yourself on older, smaller models and your own harness; Automate only what you can do yourself

## [Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture](../videos/AGkzpxMdPn8.md)
`AGkzpxMdPn8` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: governance-compliance, product-ux

Accenture talk on why enterprise agentic projects stall: human-speed governance, business cases, and trust. Argues for hypothesis-driven delivery, portfolio funding, progressive autonomy, and feedback loops as the moat.

- Techniques: Exposure ladder for agent rollout; Approval-as-code; Hypothesis-driven agent delivery; Portfolio funding for AI bets; Kill switches and hard limits on autonomous actions; Instrument every feature as a feedback source

## [Rewiring the State — Eoin Mulgrew, No. 10 (Downing Street)](../videos/ObNKGf9YR0g.md)
`ObNKGf9YR0g` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: governance-compliance, product-ux, evals

Eoin Mulgrew of No. 10's data science team describes an outsider "insurgency" unit with forward-deployed engineers that ships small government AI tools in weeks; mostly a recruitment pitch.

- Techniques: Insurgency unit with a mandate; Forward-deployed engineers embedded in workflows; Internal tool instead of outsourced one-off analysis; Policy simulation sandbox; Pre-deployment sycophancy red-teaming and user coaching; Benchmark-based guardrails for classroom AI
- Tools: Gemini, Inspect (AI Safety Institute evaluation tool), Xtract (planning-application digitisation)

## [How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom](../videos/4_VQBbs2iQA.md)
`4_VQBbs2iQA` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: claude-code, skills-self-improvement, pr-code-review

Intercom's platform lead explains how they set a goal to double engineering throughput by standardizing on Claude Code, backed by skills, hooks, calibrated auto-approval and telemetry.

- Techniques: Single-platform standardization with internal plugin distribution; Guidance flywheel; Problem-first prompting; Backtested skill authoring; Calibrated automatic approval; Agent telemetry and transcript mining
- Tools: Claude Code, GitHub Copilot, Cursor, Augment, Honeycomb, S3, DX, Ruby on Rails, React, GitHub

## [Agents Don't Do Standups: Building the Post-Engineer Engineering Org — Mike Spitz, PFF](../videos/VMemhtlsoNk.md)
`VMemhtlsoNk` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: software-factory, testing-verification, context-engineering

Mike Spitz (PFF) reports a Jan–Mar 2026 case study where agent-driven spec, design doc, ticket and PR flow cut delivery time and dropped Scrum for a 20-engineer team.

- Techniques: Agent-interviewed spec then skill-generated LDD; Auto-generated, non-blocking tickets and PR-driven status; Agent code review limited to opinion-level nits; Post-staging QA agent against acceptance criteria; Composable per-step skills for the delivery lifecycle; Customer survey as the primary retro signal; Phased, non-critical-first rollout
- Tools: Claude Code, Claude Opus, Codex

## [Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski](../videos/ohKt066uFhg.md)
`ohKt066uFhg` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: product-ux, security-guardrails, memory

Viktor's co-founder on building a company AI employee that lives in Slack: shared integrations, scoped access, memory across many users, and why tone and staged rollout matter.

- Techniques: Shared-integration inheritance with per-integration scoping; Thread roll-over on new DM; Treat edits and deletes as control signals; A/B test model personality, not only task scores; Staged proactivity rollout; Analytics check before acting on a claim; Browser-DOM web agent (2023 baseline)
- Tools: Slack, Viktor, OpenClaw, Claude Code, Claude Cowork, Opus 4.6, GPT-5.4, PostHog, Gmail, Meta Ads, WebArena

## [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../videos/_QAVExf_1uw.md)
`_QAVExf_1uw` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, rag-retrieval, skills-self-improvement

A staff engineer at IKEA argues enterprise agents fail on undocumented institutional knowledge, and proposes a pull-based loop where agents surface knowledge gaps and curate context blocks before retrieval.

- Techniques: Pull-based knowledge capture from failed agent runs; Failing-tasks-as-tests for knowledge bases; Historical-incident replay as a probe source; Three-step gap scanner: probe generation, probe run, gap analysis; Freshness labels, flagged for human decision; Git-backed curated context blocks with a metamodel; 80/20 context cache with links to the monolith; Full-context before graph RAG, for small domains; Claude Code skills, rules, agents and hooks as the implementation
- Tools: Claude Code, GitHub Copilot, Confluence, Jira, Slack, GitHub, MCP, RAG, GraphRAG, Replit, Kanban board

## [Agents for Everything Else — swyx](../videos/zepu8Kk6FBQ.md)
`zepu8Kk6FBQ` · AI Engineer · 2026-05-18 · q3 · intro · keynote · also: coding-agents, product-ux

swyx describes how the nine-person AI Engineer team runs its business with coding agents (Devin, Claude Cowork), and argues agents should handle the routine "everything else" work, not just code.

- Techniques: Figma-to-site via coding agent; Code as the CMS source of truth, maintained by an agent; Agent as ops triage for routine requests; Prioritised concern reduction for AI adoption
- Tools: Devin, Claude Cowork, Figma, Sanity, Notion, Google Sheets, Sessionize, Supabase, React, OpenClaw, tldraw

## [The New Application Layer - Malte Ubl, CTO Vercel](../videos/XKup1pj-34M.md)
`XKup1pj-34M` · AI Engineer · 2026-05-18 · q3 · intro · keynote · also: agent-architecture, sandboxing-execution, product-ux

Vercel CTO Malte Ubl argues agents are a new kind of software that makes long-tail automation affordable, names practical agent archetypes, and says harnesses should run apart from the code they generate.

- Techniques: Compress-the-research agent; Information-surfacing agent; Ask-what-you-hate discovery; Harness and code execution split; CLI and API first for agent-facing products; Lightweight bash sandbox for agents
- Tools: Vercel AI SDK, Chat SDK, JustBash, Claude, Codex, Granola, Pi, OpenClaw

## [One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS](../videos/EmhRyw6xeT0.md)
`EmhRyw6xeT0` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools

Garrett Galow (WorkOS) explains cross-app access (XAA): the enterprise IdP brokers silent, short-lived MCP tokens so users stop clicking consent screens and IT regains revocation and visibility.

- Techniques: Cross-app access via ID-JAG token exchange; IdP-side allow-list for app-to-app access; Short-lived access tokens with silent re-mint; Audience URL as the routing key; Server-side ID-JAG acceptance
- Tools: MCP, Claude Code, Cursor, Okta, Figma, WorkOS, Microsoft Entra, SCIM, CIMD, DCR, OAuth, OIDC

## [Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML](../videos/X6NShR2ccOg.md)
`X6NShR2ccOg` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: training-finetuning-rl, evals, inference-serving

Adaptive ML's CCO argues RL, not prompting or SFT, is the systematic way to take enterprise LLMs and agents from MVP to production, using environments, rewards, and LLM judges. Mostly a product pitch for their platform.

- Techniques: Mock environment with mock tools and an LLM-played user; Rejection-sampling bootstrap from reward-scored trajectories; Business KPI as the RL reward; LLM judge with human-written rubric, graduated to a reward model; Prefer a smaller RL-trained model for high-volume or latency-bound features
- Tools: Adaptive Engine, PPO, GSPO, Gemma, Mistral, Qwen

## [How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs](../videos/kfSDc2eVLo4.md)
`kfSDc2eVLo4` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: product-ux, evals

Chris Lovejoy (Notius Labs) argues winning in vertical AI is an organizational problem, and gives a three-role framework (oracle, evaluator, architect) for placing domain experts, with Granola, Tandem and Anterior as cases.

- Techniques: Oracle role (domain expert edits the product directly); Decentralized oracle; Evaluator role (expert defines metrics; engineers improve); Architect role (self-improving system); Role progression check
- Tools: LLM-as-judge, clinician review dashboard

## [A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon](../videos/vAIDdLKB6-w.md)
`vAIDdLKB6-w` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, coding-agents

Matthias Luebken (Taven AI) shows how the open-source Pi coding agent, the core under OpenClaw, can be embedded in a product: an agent is a tool-calling loop, and a sales-RFP email agent is built on per-customer sessions and CLI tools.

- Techniques: Agent as tool loop with event and hook surface; Extension commands with UI selection; Per-customer agent with harness and customer files; Backend access as CLIs for the agent; Small single-purpose tools packaged as a skill; Draft-first human-in-the-loop output
- Tools: Pi, OpenClaw, Claude Cowork, FFmpeg, pandas, openpyxl, LibreOffice, AGENTS.md, NVIDIA OpenShell, TypeScript

## [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @The Pragmatic Engineer](../videos/CS5Cmz5FssI.md)
`CS5Cmz5FssI` · AI Engineer · 2026-05-18 · q3 · practitioner · interview · also: coding-agents, governance-compliance, infra-cost-scaling

Gergely Orosz (Pragmatic Engineer) on "token maxing": how usage leaderboards get gamed, why individual gains do not yet show up as team gains, and why big companies build their own agent infrastructure.

- Techniques: Enable non-engineers to build with coding agents; Keep agent count small and treat orchestration like tech lead mentoring; Single MCP gateway tied to service discovery; Risk-tiered code review for agent-written changes; Trade early access for structured feedback
- Tools: Claude Code, Cursor, GitHub Copilot, MCP gateway

## [Anthropic Shows What Most Developers Are Missing](../videos/LC7kGTDoWRY.md)
`LC7kGTDoWRY` · AI LABS · 2026-02-02 · q2 · intro · news · also: coding-agents, multi-agent, testing-verification

AI LABS argues that engineering is shifting from writing code to orchestrating agents, reviewing exceptions, and stating intent clearly, with a short sponsored segment and little measured evidence.

- Techniques: CLAUDE.md verification loop for long autonomous runs; Commit each verified unit, with decisions in the message; Split work into small independent units and run agents in parallel; Custom specialist subagents with chosen models and instructions; Plan mode with agent questions before building; Agent first-pass review with human review of exceptions; Layered security agents plus an external scanner
- Tools: Claude Code, CLAUDE.md, Claude Chrome extension, Puppeteer MCP, git, CodeRabbit, Cowork (Anthropic), Claude Opus 4.5, GPT-5.2, Golang, COBOL, Fortran

## [How Crypto Is Secretly Taking Over Banking with @SarahBensonCodes  | Better Stack Podcast Ep. 8](../videos/taTXejPts4E.md)
`taTXejPts4E` · Better Stack · 2026-01-02 · q2 · intro · interview · also: dev-tools, mcp-and-tools

Better Stack podcast with Sarah Benson (Amber Data) on crypto vs Web3, tokenized real-world assets and smart-contract basics. Mostly opinion, with a short note on exposing data to LLMs via MCP.

- Techniques: Start a smart contract from an audited template; Expose analytics data to agent LLMs via MCP plus semantic tags; Private permissioned chain for institutional settlement; Vet a Web3 project before trusting it; Full-build tutorial structure
- Tools: Solidity, Rust, Forge (Foundry), Hardhat, React, TypeScript, web3.js, ethers.js, Thirdweb, Polymarket, pump.fun, Canton Network

## [Hao Sheng on Building Human-Business Interfaces with AI | Better Stack Podcast Ep 3](../videos/IFSK3_M6Fuk.md)
`IFSK3_M6Fuk` · Better Stack · 2025-11-02 · q2 · intro · interview · also: product-ux, rag-retrieval

Hao Sheng (Expertise AI) on a human-to-business interface that generates per-visitor pages, with founder lessons from Dialogflow, Cresta and bootstrapping; mostly narrative, thin technical detail.

- Techniques: Start-from-problem validation before building; Query rewriting before retrieval; Multimodal retrieval with cross-modal consistency checks; Human-in-the-loop labeling for intent classifiers; Per-visitor generated page from conversation
- Tools: Dialogflow (Google), Expertise AI (formerly Chat Simple), Cresta, HubSpot, AlexNet, ImageNet

## [How to hire, motivate and retain 10x engineers with David Pavlik](../videos/yr_8HIZNQOw.md)
`yr_8HIZNQOw` · Better Stack · 2024-11-02 · q3 · intro · talk · also: product-ux

Engineering leader David Pavlik on hiring, motivating and retaining top engineers, drawing on Netflix, SpaceX, Microsoft and Amazon: mission and people beat perks, and hiring is the manager's job.

- Techniques: Paid collaborative trial instead of a coding interview; Outside bar raiser in the hiring loop; Ask what motivates the candidate, then align the pitch; Recruit with an extra-mile experience; Engagement check via a best-friend-at-work question; Re-validate team alignment after a mission pivot; Life-event review and environment adjustment; Dual-track promotion with a step-back path; Stock refresher grants instead of four-year cliffs

