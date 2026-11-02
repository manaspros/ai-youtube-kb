# multi-agent — 222 videos

*orchestration, subagents, agent teams, planners/workers*

By channel: AI Engineer 113 · Kai Explains 4 · AI LABS 64 · Better Stack 41

**Synthesized guide:** [guides/multi-agent.md](../guides/multi-agent.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Why We Rebuilt Microsoft Office From Scratch for AI Agents - Yijia Liang, Compound AI](../videos/v0UkV5qS9E4.md)
`v0UkV5qS9E4` · AI Engineer · 2026-11-01 · q3 · practitioner · talk · also: evals, rag-retrieval, enterprise-adoption

Compound's Yijia Liang explains why they rebuilt Excel, PowerPoint and Word as headless Rust engines for finance agents, using the real Office apps as an oracle in agent loops, plus email-based multiplayer agents and swarm-based file processing.

- Techniques: Objective-function loop against the incumbent app as oracle; Own the write-render-check-fix loop with a headless engine; Grep-first agent swarm over a large file corpus with citations; Email as the multiplayer interface for an agent
- Tools: Compound (getCompound.ai), IronCalc, Microsoft Excel, Microsoft PowerPoint, Microsoft Word, OpenPyXL (transcribed as 'OpenPAxcel' / 'OpenPi Excel'), Outlook, SharePoint, Box, Microsoft Teams, Claude, ChatGPT

## [Anthropic Just Released A New System For Using Claude Code](../videos/S49gppZl8H0.md)
`S49gppZl8H0` · AI LABS · 2026-10-31 · q2 · practitioner · tutorial · also: claude-code, pr-code-review, testing-verification

Walkthrough of Anthropic's Claude Code review system, rebuilt as skills: eval.md gates before build, a fresh-context builder/verifier/reviewer loop, risk tiers, and git rollback.

- Techniques: Eval-first feature gating; Fresh-context builder/verifier/reviewer loop; Reviewer loop stop rules; review.md with a learned-rules section; Consequence-based risk tiering; First-time-user agent test; Git branch per feature with rollback
- Tools: Claude Code, CLAUDE.md, review.md, eval.md, state.md, Claude Code code review command, skills, subagents, hooks, git, Codex, Cursor

## [The Best Git Worktree Tool I've Used (Worktrunk)](../videos/mNo24Omj8X4.md)
`mNo24Omj8X4` · Better Stack · 2026-10-31 · q3 · practitioner · review · also: coding-agents, dev-tools

Review of Worktrunk (wt), a Rust CLI on top of git worktrees that adds per-branch switching, a multi-agent status view, one-command merge, copy-on-write cloning of ignored files, and per-worktree dev ports for parallel coding agents.

- Techniques: Worktree per parallel agent; One-screen status across agents; Shell integration before first use; Cheap clone of ignored dependencies and caches; Per-worktree dev server ports; Single-command merge back
- Tools: Worktrunk (wt, Rust CLI, MIT/Apache dual license, v0.81 as stated), Claude Code (native worktrees and its worktree-creation hook), Codex, OpenCode, Gemini CLI, git, Vibe Kanban (mentioned as a Kanban-board alternative), APFS (macOS copy-on-write filesystem), ext4 (Linux filesystem, full copies)

## [Why a One-Line Change Can Break Your Whole Stack - Cole Gannaway, Qodo](../videos/YqxpPI7YUjE.md)
`YqxpPI7YUjE` · AI Engineer · 2026-10-29 · q2 · intro · talk · also: pr-code-review, context-engineering, software-factory

A Qodo solutions engineer argues PR review is the bottleneck in AI software factories and needs cross-repo blast-radius context, independent reviewers and rules learned from past reviews. Mostly a product demo.

- Techniques: Blast-radius-aware review over a software graph; Rules learned from review comments; Pre-generation context injection; Independent, varied reviewers; Mid-run review checkpoints via skill; Ticket-linked PR review
- Tools: Qodo (spoken as Kodo), Jira, Linear, MCP servers, Claude Code, Anthropic models, OpenAI models, Bitwarden (example repo, open source password manager), CLI

## [How a Trading Firm Ships New AI Models the Same Day - Noyan Tokgozoglu, Optiver](../videos/aGIUg8zKI8A.md)
`aGIUg8zKI8A` · AI Engineer · 2026-10-27 · q4 · practitioner · talk · also: enterprise-adoption, token-cost-efficiency, evals

Optiver's head of AI engineering on running an AI platform where every decision shows up in P&L within hours: same-day model adoption, token-spend control, and narrowly scoped agents on a shared gateway.

- Techniques: Golden-set benchmarking on day zero; Gateway-first model onboarding checklist; Replace default MCP context with tool search and CLI wrappers; Analyze cache invalidation before tuning cache TTLs; Move reference material out of the system prompt into retrieval; Per-team alerts and self-managed spend limits; Point-in-time tool snapshots with per-invocation confidence; Scope agents narrowly and version them; Ship internal portal with contributions via PRs
- Tools: Claude Code (referenced as the "cloud code" moment in the auto-captions), Codex (OpenAI coding agent; the speaker says it lacked self-hosted managed agents until recently), MCP (Model Context Protocol) servers and MCP tool search, OpenTelemetry (OTEL) logging, Slack client, Internal inference gateway, agent gateway, agent workbench, meta-harness layer, and web portal (Optiver in-house)

## [Build Your Own Team of Managed Agents - Jack Wotherspoon, Google DeepMind](../videos/Y_p3y6zP5QE.md)
`Y_p3y6zP5QE` · AI Engineer · 2026-10-26 · q3 · intro · talk · also: sandboxing-execution, agent-architecture, mcp-and-tools

Google DeepMind's Jack Wotherspoon demos Gemini managed agents: a cloud sandbox, harness and API in one call, with reusable environments for multi-agent handoff, credential-injecting proxies, and scheduled triggers.

- Techniques: Single-call managed agent; Chain turns with the interaction ID; Hand off work between agents via a shared environment ID; Narrow single-purpose agents with fan-out; Placeholder credentials with egress injection; Scheduled and webhook-triggered runs
- Tools: Gemini API Interactions API, Gemini managed agents, Antigravity harness, Gemini Flash, Gemini 4 Argonne (name as spoken in the talk), Google Search (built-in tool), remote MCP servers, agents.md, agent skills, GitHub, Google Drive, Google Docs

## [EGM: Google's New Way To Use Claude Code Is Insane](../videos/xxf6D9jynFw.md)
`xxf6D9jynFw` · AI LABS · 2026-10-26 · q2 · practitioner · tutorial · also: context-engineering, coding-agents, claude-code

Walkthrough of Google's EGM, a spec-first workflow where zero-context goldfish sub-agents critique a plan before any code is written, with install, bootstrap, review and drift steps for Claude Code. A sponsor segment caps quality.

- Techniques: Isolated-context plan critique; Multi-lens rubric reviewers; Fan-out with a single merged report; Staged plan authoring with per-section approval; Round-based review gate; Drift check against per-folder docs; Make per-folder docs agent-readable; Verify the installer's CLAUDE.md edits; Install by agent-specific command or by prompt; Command sequence
- Tools: EGM (Google Elephant Goldfish Model, free on Google's GitHub), Claude Code, Codex (named as a supported agent), Hydra (sponsor, video generation for app promos)

## [How to Write Your First AI Eval - SallyAnn DeLucia, Arize AI](../videos/gv4w23xYj-0.md)
`gv4w23xYj-0` · AI Engineer · 2026-10-26 · q3 · practitioner · workshop · also: evals, observability

A hands-on workshop on writing a first LLM-as-judge eval for an agent: why vibe checks fail, how traces feed evals, how to write concrete criteria, and how to build and iterate a judge in a prompt playground.

- Techniques: Six-part criteria template; Judge prompt structure; Variable mapping for judge inputs; Span-level dataset selection; Iterate the judge in a prompt playground against a dataset; Alignment against human labels; Online evals on incoming traces; Decision-model comparison; Instrumentation: auto, manual, or hybrid
- Tools: Arize AI (Arize AX platform, captioned 'Arise' or 'AX'), Alex (Arize's in-platform AI agent that can run playgrounds and iterate on prompts), Signal (Arize's managed agent that reads traces, finds issues and proposes fixes), OpenInference (Arize's tracing package with auto-instrumentors for agent frameworks), OpenAI decision model API (mentioned as released the week before the talk), Anthropic, OpenAI and Gemini provider API keys (configured under AI providers in settings), ROUGE and BLEU (named as code-based eval metrics), Notion one-pager (workshop instructions)

## [Your Agent Fix Just Broke Something Else - Sofia Jakovcevic, Arize AI](../videos/v5tm5EAzsAs.md)
`v5tm5EAzsAs` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · also: evals, observability, testing-verification

A five-step regression loop for agents built on production traces, evaluators and CI gates, so a prompt or policy change is judged on numbers before it merges. Vendor-led demo of Arize.

- Techniques: Five-step trace-driven regression loop; Four-bucket dataset composition; LLM-as-judge plus code evaluators; Side-by-side prompt versions in a playground; Agent playground against a remote agent; Run experiments from coding agents through skills; CI gate on experiment results
- Tools: Arize (Arize AI observability backend and platform, incl. prompt hub, prompt playground, agent playground, experiments, datasets), Arize agent skills repository (public, for coding agents), GitHub Actions (CI example), Arize SDK / REST / CLI (run experiment), LLM-as-judge evaluators (pre-built: hallucination, user frustration, security checks; custom evaluators supported)

## [Inside Arca's Long-Horizon Agents That Run the Business - Aman Singh, Arca](../videos/oP2WLFpMoDY.md)
`oP2WLFpMoDY` · AI Engineer · 2026-10-24 · q3 · practitioner · review · also: agent-architecture, memory, enterprise-adoption

Arca, an AI-native financial services firm, explains how background agents own multi-day client work through a signal system, shared plan spaces, and human pull-ins.

- Techniques: Signal-driven wake-up with interest registration; Dual wake-up: event plus timed fallback; Treat UI mutations as first-class events; One shared workspace per goal with human pull-ins; Split state by horizon: memory for later, tasks for now; Turn colleagues' reasoning into eval cases; Steer by adding a goal

## [The Best Agent IDE I've ever used (Orca)](../videos/8QgBcI40VC8.md)
`8QgBcI40VC8` · Better Stack · 2026-10-24 · q3 · intro · review · also: coding-agents, dev-tools

Walkthrough of Orca, a free open-source desktop app that runs Claude Code, Codex and other coding CLIs side by side with per-task git worktrees, a browser with element annotation, and multi-agent orchestration.

- Techniques: Worktree-per-task agent launch; Element-annotated fix requests from an embedded browser; Forced multi-provider split for comparison; Run the orca CLI from the terminal
- Tools: Orca, Claude Code, Codex, Goose, Kimi (transcript says 'kimmy'), Cursor, Herdr (transcript says 'Herder'), Ghostty (transcript says 'Ghosty'), GitHub, Linear, caffeinate, Apple Design skill (named in demo, source not stated)

## [Anthropic Just Revealed How Their Engineers Use Claude Code](../videos/92ZDgn8bgLM.md)
`92ZDgn8bgLM` · AI LABS · 2026-10-22 · q3 · practitioner · tutorial · also: claude-code, context-engineering, testing-verification

AI Labs video on Felix Rieseberg's article: get more from Claude Code by asking for outcomes, expert methods, varied viewpoints, an outside judge, and the tools to verify results.

- Techniques: Outcome-first prompt (altitude); Expert-method meta-prompt (depth); Impossible-sounding goal reframing; Outside judge via a second model; Noun-to-verb role discovery and sequential specialist sub-agents (range); Verification resources for agents
- Tools: Claude Code, Claude (Anthropic), Codex CLI, MCP (Model Context Protocol), GoLogin (sponsor segment, not a recommended tool), AI Labs Pro (paid community, mentioned in closing)

## [AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard](../videos/uA4ah-dVHvU.md)
`uA4ah-dVHvU` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: enterprise-adoption, mcp-and-tools, data-engineering

Vanguard's cash-ledger modernization: exposing the legacy codebase over MCP cut a 7-day research loop to 15 minutes, with lessons on migration, idempotent producers and consumer onboarding.

- Techniques: Expose a legacy codebase to agents through an MCP server; Two-stage CDC migration verification; Single write gateway with idempotency for all producers; Consumer access matched to channel; Business-case registration for consumers; Fix forward, do not patch the legacy; Human-readable state values in the new system; Shared team knowledge base
- Tools: MCP server (legacy codebase and migration docs exposed to AI tools), CDC (change data capture, generic), GraphQL (real-time consumer API), Kafka (event topic for inserts and updates), Schema registry (generic, for all consumer channels), Snowflake-style IDs (ID paradigm, not the product), Data warehouse data-share views (batch consumers)

## [One Day, $1,000 in Tokens: An AI War Room for Legacy Code — Ford Prior, GEICO](../videos/DouK81O8R3o.md)
`DouK81O8R3o` · AI Engineer · 2026-10-21 · q4 · practitioner · talk · also: software-factory, context-engineering, enterprise-adoption

GEICO's Ford Pryor describes an AI "war room" for legacy code modernization: a roster of decision makers, a driver, and fleet-managed Claude agents that take a major change from goal to approved design and agent-callable APIs, with human gates along the way.

- Techniques: War room composition for a major change; Three-repo split of enterprise agent context; Goal-to-approval-to-build loop with a queue; Milestone artifacts plus deterministic gate checks; Taxonomy for modernization missions; Local bindings file for agents on a laptop; Cost guardrails for agent-run work
- Tools: Claude Code, Anthropic Code Modernization plugin, Fleet Kit (Anthropic-collaborated fleet manager, markdown rules; not open source yet), beads (per-agent state tracking), Claude artifacts (HTML worksheets), draw.io, Figma, Slack (mission channel), GitHub Issues (example queue), Fable (model, named in the talk), Sonnet 5.5 (model), Opus 4.8 (model, named as too weak for this steering)

## [Anthropic Barely Reads Claude's Code Anymore](../videos/d8QpDbBKbAU.md)
`d8QpDbBKbAU` · Better Stack · 2026-10-20 · q4 · practitioner · news · also: pr-code-review, claude-code, evals

Secondhand summary of how Anthropic reviews Claude Code's own PRs: layered automated review, risk-tiered human sign-off, incident-derived reviewer evals, and round caps for agent-vs-agent loops.

- Techniques: Layered review pipeline with a voting gate; Turn repeated reviewer findings into durable rules; Per-directory review.md written by code owners; Merge gate with explicit false-positive dismissal; Incident-derived reviewer eval with a keep-or-drop rule; Noise metric from comment outcomes; Round cap, scoped re-review, and whole-class flagging for agent loops; Risk tiering with a classifier agent and a second check
- Tools: Claude Code, CLAUDE.md, review.md, PR template, lint rules, CI (tests, type checking, linting)

## [How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase](../videos/_4Ph2dhmUFI.md)
`_4Ph2dhmUFI` · AI Engineer · 2026-10-20 · q3 · practitioner · talk · also: governance-compliance, evals, agent-architecture

Coinbase's Evan Kormos on deciding when an agent can run unsupervised: keep the process deterministic on the outside, model it as a graph with policy boundaries, and earn autonomy per node through measured evals.

- Techniques: Policy-bounded DAG process map; Cyclic review node with a bounded loop; Per-node automation checklist; Graduated autonomy rollout; DAG state injected into agent context; Statistical evaluation over repeated runs; Exception-flow and volume monitoring
- Tools: Apache Airflow, LangGraph (transcript says LangChain Langraph)

## [Stop Telling Agents How](../videos/7T-gldvgfpo.md)
`7T-gldvgfpo` · AI Engineer · 2026-10-19 · q3 · practitioner · talk · also: context-engineering, agent-architecture, evals

OpenProse founders argue agents should be given declarative Markdown contracts plus triggers, not step-by-step prompts; the talk is largely a product demo of their hosted runner.

- Techniques: Contract-first workflow spec; Codify a golden trace into pinned steps; Event-driven job = contract + trigger; Fresh-session verifier against the contract; Kernel as a bootloader index; Templated multi-agent shapes; Cheap verifier or router (planned, not shipped)
- Tools: OpenProse, run.pros.md (hosted OpenProse runner), pros CLI (pros write, pros run), npx skills (skill install mechanism), Claude Code, Codex, Exa (search), DSPy (contrasted), n8n (contrasted), pi (agent harness without sub-agents, transcribed as 'pie'), Matt Pocock's skill workflow (grill-me, TDD) used as an example, Haiku (cheaper model mentioned)

## [AI Is Merging Video Games Now (here's how)](../videos/9dDJq1LGBAw.md)
`9dDJq1LGBAw` · Better Stack · 2026-10-19 · q3 · intro · review · also: coding-agents, skills-self-improvement, token-cost-efficiency

Better Stack demos Universal Modder, an open-source Claude Code plugin that builds GTA 5 mods from games you own via recon, hot reload, in-game testing and shared field notes; ~$68 API cost.

- Techniques: Back up and log before touching user state; Fingerprint before coding; Parallel narrow research sub-agents; Write a converter for proprietary asset formats; Hot-reload the logic, not the host; Screenshot check after each reload; Draw new content as a post-process overlay; Field note plus shared KB PR
- Tools: Universal Modder (Rayhan; open-source Claude Code plugin with skills, a CLI and a knowledge base), Claude Code, Claude Opus 5.5 (as stated in the video), Script Hook 5 (GTA 5 script loader), ReShade, FAL (image generation for sprites, textures, 3D models, sound and voice; made by an ex-FAL engineer per the host), OpenCode (wrote KB notes), Steam (game library)

## [6 Insane Trending GitHub AI Design Repos You Need to Use](../videos/NZjjmf3I6I4.md)
`NZjjmf3I6I4` · AI LABS · 2026-10-19 · q2 · practitioner · review · also: coding-agents, skills-self-improvement, mcp-and-tools

Walkthrough of six GitHub repos that give coding agents design references, multi-viewport checks, design-token extraction, multi-agent page builds, app-store screenshots and launch-video generation. Mostly sponsored tool demos with little measurement.

- Techniques: Reference-first design with an awards MCP; Post-build responsive check with Responsively MCP; Design taste skills, chosen by scope; Extract and diff design tokens with Dembrandt; Generate app-store screenshots with a local editor project; Launch video with Brag, with a verification pass
- Tools: Awards MCP (awards setup and awards inspiration commands), Klein CLI (caption spelling; probably Cline), sponsor, Kleinpass (caption spelling; probably ClinePass), sponsor, open-weight model access, first-month discount link, Whisperflow landing page (probably Wispr Flow, used as a reference site), Butter.Video (animation reference site), Responsively (Mac app and MCP server), Genjutsu skills: Cast, Paint, Bunshin, taste skill and hallmark (previously covered by the channel), Dembrandt (skill, design.md output), App store screenshots skill and local editor, Brag / Bragg (brag command, Full Mode and Slim Mode), Hyperframes (video framework used by Brag Full Mode)

## [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](../videos/kiClTcJUnhc.md)
`kiClTcJUnhc` · AI Engineer · 2026-10-17 · q4 · practitioner · talk · also: agent-architecture, security-guardrails, governance-compliance

Anthropic's Claude Managed Agents "flows" (dynamic multi-agent workflows) talk: how to fan out hundreds of isolated sub-agents, control cost with budgets, and contain risk with credential vaults, egress rules and auto mode.

- Techniques: Plan, fan out, phase-gate; Per-phase model and agent-count allocation; Separate reviewer context for adversarial checks; Two-stage review with verification; Budget as a resumable circuit breaker; Credential injection at the egress proxy; Declare, contain, detect; Transcript audit agent; Gradual context reveal via linked markdown index; Filesystem as the inter-agent channel; Interrupt and redirect
- Tools: Claude Managed Agents, Claude Code, Claude API skill, ant CLI, Terraform provider for Claude agents, Dynamic workflows (Claude Code), Hill-climb skill, Dreaming (memory consolidation product), Auto mode (permission classifier), Bug Hunter flow, Explainer Video Maker flow, Claude Tag (Slack bot)

## [I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](../videos/dYh7TQkuYFE.md)
`dYh7TQkuYFE` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: testing-verification, evals

Corey Gallon (Rexmore) presents a three-level agent review method, each level built as a skill, that catches agents overstating work, misreading facts, and reasoning errors, shown on three real cases.

- Techniques: Deliverable contract with a self-check the sender runs; Fan-out / fan-in with independent identical agents and a source-anchored adjudicator; Control-total anchoring; Claim labeling self-audit; Cold persona reviewers with no context; Fresh-reviewer final pass

## [Claude Mods Are Insane... You Need To Try These Right Now](../videos/ERNqRK6sMJY.md)
`ERNqRK6sMJY` · AI LABS · 2026-10-12 · q3 · practitioner · review · also: claude-code, context-engineering

AI LABS demos seven Claude Code "mods" they built (prompt enhancer, design picker, assumption reviewer, idea shelf, session dashboard, same-folder tracker, plain-language answers) and explains how to create and install them.

- Techniques: Build a mod from a prompt; Prompt enhancer before send; Assumption ledger with targeted correction; Visual option picker before a design choice; Two-pass answer rewrite with a cheap check
- Tools: Claude Code, Claude mods (Claude Code feature), plugin-authoring skill, Haiku model (answer rule check), Runway, Gen-4.5 (Runway video model, sponsor segment), Stride (AI LABS' own running-coach app, sponsor segment)

## [Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](../videos/FGftGOzfohc.md)
`FGftGOzfohc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, security-guardrails, memory

Anthropic hands-on workshop (Part 2 of 4) building a research agent on Claude Managed Agents: sub-agents, rubric-graded outcomes, vaults, shared memory, dreaming, and a map-reduce harness.

- Techniques: Rubric-gated outcome with a grader sub-agent; Placeholder secrets with domain-scoped egress swap; Context isolation via self-referencing sub-agents; Check shared memory before redoing work; Map-reduce orchestration via a custom dispatch tool; Transcript-driven memory consolidation (dreaming)
- Tools: Claude Managed Agents API, Claude Code (used to drive the workshop), SEC EDGAR Python package, MCP, Bun, npm, Agent SDK (compared)

## [Hiring Employable Agents + Startup Battlefield Finals — Howie Liu, HyperAgent](../videos/EEt3ZSG4a1s.md)
`EEt3ZSG4a1s` · AI Engineer · 2026-10-12 · q2 · intro · other · also: agent-architecture, product-ux, enterprise-adoption

Howie Liu (HyperAgent) argues agents are moving toward always-on "claws" that humans unblock and orchestrate, then the video covers the Startup Battlefield finals (Kamad, Common.io, Foundry).

- Techniques: Heartbeat re-invocation for always-on agents; Human approval gate on high-impact actions; Correction-to-memory loop; Specialist triage and handoff pipeline; Deny-condition state machine for agent actions; Sandbox VM per agent thread
- Tools: HyperAgent, OpenClaw, Claude Code (workflows, fan-out to parallel agents), FFmpeg, Slack, email, Gmail, Stripe, Salesforce, WhatsApp, Google Docs, GitHub

## [Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic](../videos/QSeaZ6qHyXs.md)
`QSeaZ6qHyXs` · AI Engineer · 2026-10-12 · q3 · practitioner · other · also: agent-architecture, evals, sandboxing-execution

Anthropic presenters answer audience questions on Claude Managed Agents: YAML-as-code deployment, eval sweeps, tenant isolation via workspaces, long runs, and sub-agents for custom tools.

- Techniques: Agent definitions as YAML synced by CI; Parallel eval sweeps on new model releases; Historical-session eval dataset; Workspace-per-customer isolation; Rubric-based exit criteria for long runs; Coordinator with a custom-tool sub-agent; Per-thread session mapping for multi-user chat
- Tools: Claude Managed Agents (CMA), Anthropic CLI (transcribed as 'Ancho CLI'), Claude Code, Modal, E2B (transcribed as 'EB2'), Daytona, Slack

## [Why I’m Switching From Python to Docker Agent for AI Agents](../videos/Mph1H5u3yeA.md)
`Mph1H5u3yeA` · Better Stack · 2026-10-12 · q3 · intro · review · also: agent-architecture, mcp-and-tools

Better Stack walks through Docker Agent, an open-source Docker tool that defines agents in YAML, runs them with one command, and serves them over A2A. Demoed with an on-call incident and a Battleship match between two models.

- Techniques: Define an agent as a YAML file; Least-privilege agent split behind A2A; Serve an agent as A2A on a port; Install Docker Agent; Share an agent as an image
- Tools: Docker Agent, Docker Desktop (4.63+), Docker model runner, Docker Hub, Homebrew, A2A protocol, MCP, Claude Haiku 5.5, GPT-6 Luna, Kimi K3, OpenAI, Anthropic

## [You're Prompting Opus 5.5 Wrong (Anthropic's Guide to Mastering Opus 5.5)](../videos/5TNXByrtHc4.md)
`5TNXByrtHc4` · Better Stack · 2026-10-12 · q3 · practitioner · tutorial · also: claude-code, context-engineering

Better Stack walkthrough of Anthropic's Opus 5.5 prompting guide: state the finish line up front, drop "think carefully" lines, steer with CLAUDE.md stop rules, split audits across subagents, track tasks in a file, and handle safeguard flags.

- Techniques: One-message task with explicit finish line; Remove thinking-nudge lines; Ban specific styles for design; Queue follow-ups during a run; CLAUDE.md stop-rule; Sub-agent split with evidence check; tasks.md progress file; Structured end-of-run summary; Merge-blocker diff review; Cross-model review; Recover from safeguard flags; Answer quickly prompt
- Tools: Claude Code, Claude Opus 5.5, CLAUDE.md, tasks.md, OpenAI model (named Astra in transcript)

## [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](../videos/qJtcEDc_WJU.md)
`qJtcEDc_WJU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, memory, skills-self-improvement

Anthropic's live demo and Q&A on Claude Managed Agents covers multi-session orchestration, scheduled deployments, outcome rubrics, and "dreaming," a memory-store self-improvement pass that the speaker says still needs your own evals.

- Techniques: Fan-out one session per entity via a dispatch tool; Scheduled deployment of a standing agent; Outcome rubric with a max-iteration cap; Offline dreaming pass over past transcripts; Workspace-per-tenant isolation instead of BYOK; Memory store as a separate attachable resource
- Tools: Claude Managed Agents, Claude Console, Claude Code, Anthropic SDK / API, AWS Bedrock, GitHub, OpenTelemetry, Jira (Atlassian integration), Notion (external agents)

## [From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot](../videos/b9UhZkKjX_A.md)
`b9UhZkKjX_A` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: coding-agents, software-factory, observability

GitHub's Jose Palafox walks through the Copilot agent surfaces: local agents you steer, reusable shared agents, cross-repo orchestration, and headless agents in CI that get cost and trace visibility through OTel.

- Techniques: Headless one-shot agent in CI; Slash-command phase gates on issues; Scaffold agents from a one-line description; Marketplace or private-repo distribution; Orchestrate: issues as goals, agents per repo; Cross-model plan audit; Small-model codebase explorer; OTel per-agent cost monitoring
- Tools: GitHub Copilot CLI, GitHub Copilot SDK, GitHub Actions, GitHub Agentic Workflows, Awesome Copilot, OpenTelemetry, Slack, Microsoft Teams

## [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](../videos/NaOkR3VSfR4.md)
`NaOkR3VSfR4` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: agent-architecture, security-guardrails

Viren Baraiya on running production agents: the LLM only plans, a deterministic harness executes side effects, durable state and human gates make it safe, shown with a Conductor SRE remediation demo.

- Techniques: Brains/hands split; Plan-compile-execute; Code-enforced human approval gate; Idempotent steps or recorded side effects; State-driven replanning loop; Single-responsibility harnesses
- Tools: Conductor, Kubernetes, Slack, LangChain agents, OpenAI Agents SDK, Google ADK, MCP, APIs

## [Why Your AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND](../videos/toq-jyGLZDk.md)
`toq-jyGLZDk` · AI Engineer · 2026-10-08 · q2 · intro · talk · also: mcp-and-tools, security-guardrails

Vlad Luzin (BAND) argues that agent-to-agent communication is a distributed-systems problem that MCP, A2A and chat platforms don't solve, then pitches BAND's hosted interaction layer.

- Techniques: Loop engineering with two stateful agents; Contact request with bilateral consent before agent discovery; Shared conversational space with human visibility; Runtime ID binding across agent frameworks
- Tools: Claude, Claude Code, Codex, LangGraph, CrewAI, MCP, A2A, ACP, Slack, Microsoft Teams, Discord, WhatsApp

## [AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk](../videos/f3o0-9Dlw3E.md)
`f3o0-9Dlw3E` · AI Engineer · 2026-10-08 · q2 · intro · talk · also: security-guardrails, pr-code-review

Snyk's Eli Cohen argues LLM-generated code and LLM attackers make twice-yearly pentests obsolete, and pitches a continuous, per-PR AI pentest pipeline (Snyk Evo) with an exploit-validation judge.

- Techniques: Layered agent pipeline for continuous pentesting; Scanner output as LLM context; Exploit proof gate before flagging; Per-PR security trigger
- Tools: Snyk Evo (Snyk's continuous AI offensive security / AI pentesting offering, named in the talk), Snyk (company), Helios (runtime security company, acquired by Snyk), Claude Code (called "cloud code" in captions), Codex (OpenAI coding agent), SAST (static application security testing), DAST (dynamic application security testing; captioned as "dust"), MCP (Model Context Protocol), Mythos (model named in passing; exact referent unclear)

## [Agent Memory Is Solved. Agent Learning Isn't. — Karthik Ranganathan, Yugabyte](../videos/9_oy4owGtPI.md)
`9_oy4owGtPI` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: memory, context-engineering, observability

Yugabyte's CEO argues agent memory is solved but cross-agent learning is not, and demos Mako, a private-to-shared context store where humans promote memories and provenance is traceable.

- Techniques: Private-to-shared promotion gate; Provenance on every memory; Scoped data packs with a skill-driven MCP interface; Cross-session resumability via shared memory; One-variable-at-a-time RAG tuning with traces; Trace-based token accounting
- Tools: Mako (Yugabyte agent-native persistence layer), YugabyteDB, Claude Desktop, Claude Design, Codex, ChatGPT, MCP, Postgres

## [Cooking with Codex — Charlie Guo & Gabriel Chua, OpenAI](../videos/FwiS44-xyYw.md)
`FwiS44-xyYw` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: coding-agents, context-engineering, software-factory

OpenAI's hands-on Codex workshop walks through context, computer use, long-running goals, subagents, hooks and automations, then shows the app server for embedding Codex in your own product.

- Techniques: Verifiable goal with milestone files; Milestone-triggered review and goal-audit threads; Side-thread unblock and status query; Subagent vs thread handoff split; Hook-based deterministic guardrails; Heartbeat automation for external waits; Scheduled triage that spawns worktree threads to PRs; Choosing a control surface: computer use vs Chrome extension vs in-app browser; Embedding via the App Server protocol
- Tools: Codex app, Codex CLI, Codex remote (ChatGPT mobile), Codex Chrome extension, Codex computer use, Codex in-app browser, Agents SDK, Sites, Chronicle (research preview, Pro), AppShots (screenshot with embedded text), AGENTS.md, config.toml hooks

## [The Human Is an Async API — Melanie Warrick, Temporal](../videos/jc3kbZkuHTo.md)
`jc3kbZkuHTo` · AI Engineer · 2026-10-05 · q3 · practitioner · demo · also: agent-architecture, governance-compliance

Melanie Warrick (Temporal) shows durable execution for multi-agent systems: a human approval is a wait condition plus a signal on a parked workflow, so the rest of the system keeps running and survives restarts. It is a vendor-led talk with a live ice-cream delivery demo.

- Techniques: Human approval as wait condition plus signal; Wrap every model and tool call as an activity; LangGraph interrupt bridged to a durable wait; Child workflow per entity; Cost-of-being-wrong gate for human review
- Tools: Temporal, Google ADK, LangGraph, Google Maps API, Google Search, Python, TypeScript, Rust

## [He Finally 10x Claude Code With This Method](../videos/qLfSDQ5NGh0.md)
`qLfSDQ5NGh0` · AI LABS · 2026-10-05 · q3 · practitioner · tutorial · also: claude-code, testing-verification, skills-self-improvement

Walkthrough of a Karpathy-style loop for Claude Code: frozen checks, fresh builder subagents, and an outer loop that rewrites instructions from failure logs. The "10x" claim is not measured.

- Techniques: Loop-fit test before building a loop; Project-context skill as app memory; Write, review, approve, lock, and commit checks; Fresh feature-builder subagent per feature, with a results file; Karpathy-style keep-or-undo loop with program.md; Outer auto loop that rewrites instructions from failures; Wire-up and sweep instructions
- Tools: Claude Code, Karpathy autoresearch (Auto Research), Upstash Box (sponsor; per-agent cloud sandbox), Approve Checks (custom script), program.md, features.md (feature tracking file), results file (custom per-round log), Project Context skill (custom), build skill (custom), write checks skill (custom), auto loop skill (custom), feature builder agent (custom subagent)

## [Orchestras, Not Factories: How the Fastest Builders Work — Charlie Holtz, Conductor](../videos/TRfzFJCJ7ZE.md)
`TRfzFJCJ7ZE` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: software-factory, coding-agents, sandboxing-execution

Charlie Holtz (Conductor co-founder) lists six principles for fast agent-driven building: stay near the frontier, don't beat the market, mark slot-free zones, feed a central store, run free-range cloud agents, and orchestrate rather than run a factory.

- Techniques: Don't-beat-the-market test; Slot-free zones with CI-enforced human review; CLAUDE.md / AGENTS.md and skills as onboarding material; Central event store with a SQL tool for agents; Cloud sandboxes per task with lifecycle independent of the laptop; Agents calling the product API to create work
- Tools: Conductor, Claude Code, Codex, git worktrees, Postgres, Slack, Discord, Telegram, OpenClaw, React

## [We're the bottleneck, but we don't have to be — Ido Salomon, AgentCraft](../videos/YIVkERhy8xo.md)
`YIVkERhy8xo` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: product-ux, coding-agents, software-factory

Ido Salomon (AgentCraft) argues that humans are the bottleneck in agent work and demos a game-style orchestrator with attention-jumping, a map view, review kits, shared rooms, and a simpler "loopers" mode for non-engineers.

- Techniques: Attention queue with jump-to-next; Spatial projection of agent activity; Review kit for parallel agent output; Orchestrator with isolated local containers and background loops; Shared room with cross-agent notice board; Progressive disclosure for low-floor use
- Tools: AgentCraft, Claude Code, Codex, OpenCode, OpenClaw, Git, Telegram, MCP Apps (MCPUI)

## [Get Out of the Model's Way — Kevin Hou, Google Antigravity](../videos/buHC7bQE1X4.md)
`buHC7bQE1X4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: coding-agents, product-ux, agent-architecture

Google's Antigravity lead on building agent products that get out of the model's way: subagent teams, sidecar triggers and generative UI, with cost and token stats from a kernel-building run.

- Techniques: Dynamic subagent teams under a lead agent; One subagent per hypothesis fan-out for eval deltas; Skills file plus natural language for internal workflow automation; Sidecar trigger process; Generative UI in the conversation instead of fixed screens; Separate the orchestration surface from the editor; Primitive audit against the next model
- Tools: Google Antigravity, Antigravity CLI, Antigravity 2.0 agent manager, Gemini 3.5 Flash, MCP, Cloud sandboxes and remote execution (unnamed), Windsurf (reference only)

## [Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band](../videos/UOcHfR3_tys.md)
`UOcHfR3_tys` · AI Engineer · 2026-10-04 · q2 · practitioner · talk · also: mcp-and-tools, agent-architecture, governance-compliance

Vendor talk by Band's CTO arguing that multi-agent coordination needs a conversation-level collaboration layer (rooms, consent, routing, governance), not just MCP or A2A, then demoing that product.

- Techniques: Bilateral consent before agent-to-agent contact; Rooms and channels with deterministic routing as the agent primitive; Network-level traffic capture for cost and attribution; Live architecture layout reporting from agents; Human-in-the-loop pings and manager kill switch
- Tools: Band (collaboration layer / platform, speaker's company), Jam (desktop app built on Band, also called 'GEM' near the end of the transcript; the name is ambiguous in captions), Claude Code, Codex (OpenAI), LangGraph (LangChain), MCP (Model Context Protocol), A2A (Agent-to-Agent protocol), ACP (protocol, named without detail), Telegram, Discord, Slack, WhatsApp

## [Shopify Just Released The Greatest AI Coding Workflow Ever](../videos/bBMp5tLxShQ.md)
`bBMp5tLxShQ` · AI LABS · 2026-10-02 · q2 · practitioner · tutorial · also: software-factory, testing-verification, claude-code

AI LABS rebuilds Shopify's checkpoint-and-gates agent loop as a Claude Code orchestrator skill; the key idea is enforcing gates with a stop hook, not advisory rules.

- Techniques: Checkpointed build with human plan approval; Stop-hook gate; Test-first behavior gate without a browser; Prototype-driven visual gate; Adversarial critic and fixer loop; Learnings file for cross-task feedback; Single orchestrator entry skill
- Tools: Helix (Shopify internal, not released), Claude Code, Claude sub-agents, Gemini (used by Shopify as UI reviewer), Hedra MCP server (sponsor segment), design.md, Ralph loop (transcribed as RALF), AI LABS orchestrator skill (their own), Checkpoint Planner agent (their own), tdd planner skill (modified, their own), prototype skill (their own), adversarial loop skill (their own)

## [LangGraph vs OpenAI Agents SDK vs Claude Agent SDK](../videos/8C3LB6TPxwk.md)
`8C3LB6TPxwk` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: agent-architecture, governance-compliance, claude-code

A practitioner comparison of LangGraph, the OpenAI Agents SDK and the Claude Agent SDK: the architectures have converged, but licensing, billing, language support, version stability and data-retention terms are what should drive the choice.

- Techniques: In-distribution test for harness choice; Pick by constraint, not by benchmark; Read the terms section before building; Verify checkpoint and resume claims against release notes; Measure latency on a representative task early; Trace handoffs as tool calls
- Tools: LangGraph, LangChain middleware, OpenAI Agents SDK (0.22; 0.14, 0.20 referenced), Claude Agent SDK (Python and TypeScript; 0.2.x patch 152), Claude Code (transcribed as 'clawed code'), Claude managed agents, OpenAI managed deep agents (public beta, US, CLI first), Microsoft AutoGen, Google ADK, Microsoft's new agent framework (unnamed), Postgres checkpointer (LangGraph), GPT-4o (transcribed as 'GPT-40')

## [This Is What Voice Coding Was Supposed to Be (Qwen Audio Agent)](../videos/blpZ1xgFhCk.md)
`blpZ1xgFhCk` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: voice-multimodal, agent-architecture, coding-agents

Hands-on review of Qwen Audio Agent, an open-source voice runtime that keeps a voice conversation alive while Claude Code does slow coding work in the background over ACP. The main lesson is that voice coding is a concurrency problem, not a transcription problem.

- Techniques: Voice front-end + async coding back-end over ACP; Interruption as an explicit state machine; Local fast-path for trivial questions; Setup (as demonstrated)
- Tools: Qwen Audio Agent (open-source voice runtime, Apache 2.0; no model weights shipped), Claude Code (back-end coding agent), Codex, OpenCode, ACP (Agent Client Protocol), Alibaba DashScope (paid cloud voice API), OpenAI Realtime API (mentioned as comparison), PipeCat (mentioned as comparison), LiveKit Agents (mentioned as comparison), Whisper (dictation baseline), Hugging Face speech-to-text pipeline, MLX (Apple Silicon local backend)

## [Grok Bot Use Cases That Are Actually Insane](../videos/90pwPVrydHg.md)
`90pwPVrydHg` · AI LABS · 2026-10-02 · q2 · intro · review · also: voice-multimodal, testing-verification, product-ux

Walkthrough of GrokBot's eight use cases: a hosted, always-on bot group sharing one logged-in browser, used for app testing, support triage, monitoring and AI-search checks. Light on setup detail; sponsor and paid-tier plugs.

- Techniques: Role-bot test fan-out with a lead bot; Backend-verified UI failure triage; Agent-triggered test round; Support email to draft reply and PR; Fresh-account onboarding audit; Unbranded AI-search visibility check; Scheduled morning monitoring routine; Coordinator bot over functional bots
- Tools: GrokBot, Grok, SuperGrok, Cursor, Hermes, Claude Code, Codex, Supabase, Stripe, Gmail, Sentry, GitHub

## [Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta](../videos/jNE8No-wvok.md)
`jNE8No-wvok` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: voice-multimodal, evals, training-finetuning-rl

Meta's Aditya Gautam on using a multi-agent system of small domain-tuned VLMs to find intra-video policy anomalies and duplicate content in short-form video, with a production judge-and-human feedback loop.

- Techniques: Orchestrator plus specialist agents for video review; Change-based frame compression; Per-signal index routing; Domain pre-training plus schema-constrained instruction tuning; Judge-plus-human-queue production loop; Distillation plus quantization sweep; Node-level evaluation suite; Pre-inference gating with cache and metadata
- Tools: CLIP, MCP, Ray, DPO, JSON schema, vector database, graph database, inverted index

## [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](../videos/x4e5O9zN0TE.md)
`x4e5O9zN0TE` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: evals, skills-self-improvement, memory

Long-running, stateful agents need controlled scenario suites, balanced scorecards and a ratchet loop, not just prompt tweaks; the speaker's case study is a game-village multi-agent system tuned by an outer auto-research loop.

- Techniques: Controlled scenario suite with ground truth; Balanced behavioral scorecard with guardrails; Frozen-harness ratchet loop; Structured run-trace logging; Importance-scored memory with a threshold cache; Provenance and confidence tags on memories; Separate episodic memory from current belief
- Tools: Project Paradox (in-house framework), RAG-backed per-agent memory, auto-research loop (Karpathy-inspired)

## [One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio](../videos/2wgPHvW0mG8.md)
`2wgPHvW0mG8` · AI Engineer · 2026-09-27 · q3 · intro · talk · also: voice-multimodal, agent-architecture, infra-cost-scaling

Skydio's Suchet Bargoti on running fleets of docked drones as agent-commanded infrastructure: tool-based VLM control, edge/cloud latency tiers, a shared map that the fleet updates, and a learning flywheel.

- Techniques: Tool-exposed primitives for a VLM agent; Latency-tiered edge and cloud split; Fleet-shared map with sync-back; Bandwidth-aware video encoding for cloud agents; Hybrid end-to-end versus hand-engineered decomposition; Log, sanitize, retrain, redeploy loop
- Tools: Vision-language model (VLM), Reinforcement learning, Drone APIs exposed as agent tools, Cloud GPUs and inference engines, Map merging and sync service

## [GTM Engineering: The Technical Bits — Everett Berry, Clay](../videos/UhCY231d0FQ.md)
`UhCY231d0FQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: data-engineering, agent-architecture

Everett Berry (Clay) on the technical hard parts of GTM engineering: data waterfalling, graph-based orchestration, long-running per-account agents, and outbound execution limits.

- Techniques: Waterfall enrichment; Selective field refresh; Typed-node orchestration graph; Persistent per-entity agent with wake-up triggers; Field ownership split; Timed re-engagement cooldown; Multi-domain sending with reply routing; Cross-channel suppression
- Tools: Clay, Salesforce, Outreach, Slack, Smartlead, Forager

## [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](../videos/O84lhGc1OOI.md)
`O84lhGc1OOI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: rag-retrieval, evals, context-engineering

Benjamin Clavié (Mixedbread) argues agents should be designed as knowledge workers, not coding agents, and uses BrowseComp-Plus and MatQA results to show that tooling and search orchestration drive accuracy.

- Techniques: Manager-plus-searcher subagents for open-ended retrieval; Optimize the lexical baseline before comparing; Hybrid search harness; Multimodal PDF search instead of OCR text; Teach the agent its retrieval primitives
- Tools: BM25, Gemini, Claude Code, Codex, Mixedbread search tool

## [Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic](../videos/PXj0p_mW9nI.md)
`PXj0p_mW9nI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: token-cost-efficiency, evals, agent-architecture

Anthropic's Katelyn Lesse and Angela Jiang argue agent token budgets are not fungible: giving some tokens jobs (advisor, grader, dreamer) beats simply spending more on one executor, measured at a fixed budget and scored on pass rate.

- Techniques: Role-split executor with advisor; Rubric grader with retry loop; Dreamer writing memory from transcripts; Fixed-budget strategy comparison; Cost per pass metric
- Tools: Claude Managed Agents

## [Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../videos/EL123UNokkI.md)
`EL123UNokkI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: pr-code-review, evals, observability

Uber's engineers explain uReview, their multi-agent code review system: how they built feedback-driven evals, team-owned customizations, and a cost/quality loop, plus why they think humans move up to an expanded outer loop.

- Techniques: Reply-sentiment and addressal-rate tracking; Trajectory-based runtime tuning with turn guardrails; Tiered review generators with post-processing; Few-shot AI linters with deterministic context; Ownership-coupled rule distribution
- Tools: GitHub, Fabricator, Claude

## [How We Solved Agent Building — Andrew Qu, Vercel](../videos/9dYcwOkpCE8.md)
`9dYcwOkpCE8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, skills-self-improvement, context-engineering

Vercel's chief of software traces an internal data-science agent from a mega-prompt, to a multi-agent chain, to one file-system agent with distilled skills, then introduces the Eve agent framework.

- Techniques: Decompose-then-collapse; File-system agent with minimal tools; Query-to-skill distillation job; Convention-based agent folders; Built-in run observability
- Tools: Vercel AI SDK, Eve, Vercel Workflows, Vercel Sandbox, Vercel Connect, bash-tool (npm), SkillsSH, Claude Code, Claude Opus 4.5, Snowflake, Next.js, Postgres

## [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../videos/0I6aoPSRzVc.md)
`0I6aoPSRzVc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: memory, context-engineering, enterprise-adoption

AIDAChip's VP of AIML argues chip-design teams are limited by alignment, not intelligence, and shows a "system of intent" living graph, tribal-knowledge layer and SME agents, plus failure lessons on substrate-level controls.

- Techniques: Living system-of-intent graph with human-gated edits; Rule-based conflict detection instead of LLM-based; Scoped spec hierarchy with file isolation per agent; Block forbidden actions at the system level, not per tool; Alignment-focused evaluation grid; Domain-specific SME agents instead of one general agent

## [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../videos/Qw_tC68KKes.md)
`Qw_tC68KKes` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, enterprise-adoption, context-engineering

Cloudflare's Justin Joyce on scaling go-to-market analysis with curated skill files, a three-agent report pipeline and a self-service agent workspace; a practitioner account with few hard metrics.

- Techniques: Role-specific skill files with embedded question catalogue; Pre-shaped analytical data for agents; Draft, verify, then tone multi-agent report pipeline; Push generated narratives instead of dashboards; Reviewed central skill catalogue; Per-user persistent agent workspace
- Tools: Cloudflare Workers, Cloudflare Durable Objects, MCP, AI Gateway, Salesforce, Gemini (mentioned as a phone analogy)

## [Agents' next frontier: agent-to-agent and network effects — Jean-Denis Greze, Town](../videos/REascnFlq_8.md)
`REascnFlq_8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, rag-retrieval, context-engineering

Jean-Denis Greze (Town CTO) reframes agent-to-agent work as a context-window search problem and compares five ways to get cross-silo data into an LLM call safely.

- Techniques: Benchmark against an ideal single-context agent; Privacy-preserving derived tool; Per-silo sweeper agent; Write-step-only approval for cross-silo queries; Tiered autonomy by sensitivity
- Tools: Gmail, Slack, Airtable, LinkedIn

## [It’s Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners](../videos/xo68uCibfm8.md)
`xo68uCibfm8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: context-engineering, agent-architecture, data-engineering

Kevin Madura (AlixPartners) explains recursive language models (RLMs): the context lives as a variable in a Python REPL, and the model writes code and delegates subcalls to sub-LMs, so only useful results return to the main context.

- Techniques: REPL-held context with sub-LM delegation; Typed I/O shell around an autonomous core; Schema-enforced sub-LM handoff; Bounded self-terminating loop; Dataframes in the REPL instead of JSON tool results; Trace-driven harness optimization (Halo)
- Tools: DSPy, PredictRLM, fastRLM, AXE, Halo, Claude Code, GPT-5, Anthropic Workflows, pandas

## [Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley](../videos/hOWU0KPUp1k.md)
`hOWU0KPUp1k` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, governance-compliance, context-engineering

Brendan Rappazzo presents Loophole, an open-source game where two adversarial agents hunt contradictions in a legal code codified from the user's morals, then extends it to chatbot prompts, contracts, and simulated Senate votes.

- Techniques: Adversarial loophole and overreach search; Judge with auto-patch first, human escalation second; Formalize natural-language values into numbered legal text first; Persona-conditioned rule generation for simulation; Hill-climbing text against an adversarial judge
- Tools: Claude, GitHub

## [AI in GTM at Notion — Flora Liu](../videos/L4I7WgiEquo.md)
`L4I7WgiEquo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, agent-architecture, data-engineering

Notion's GTM engineer explains a know/decide/act/learn system that unifies sales and self-serve signals, with humans and agents working in one shared context layer on durable workflows.

- Techniques: Four-layer know/decide/act/learn loop; Denormalized key-addressable profile plus keyed unstructured artifacts; Durable workflow per event with engine-managed retries; Parallel research subagents with score-and-select review loop; Single eligibility and routing classifier; Human approval gate by default, untrusted inbound input; Trace every LLM step and log decisions with outcome links
- Tools: Notion, Snowflake, DynamoDB, Temporal, Clay, Gong, Salesforce, Outreach, Nooks, ZoomInfo, Snowflake (product usage), Notion custom agents

## [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../videos/mMNkdYnIVC4.md)
`mMNkdYnIVC4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: agent-architecture, evals, training-finetuning-rl

James Zou (Together AI, Stanford) argues agents should be given designed environments with verifiers, incentives and shared infrastructure instead of fixed workflows, citing Einstein Arena results and the DSGym data-science benchmark.

- Techniques: Verifier-first problem curation; Agent-native onboarding; Persona-differentiated agents; Shortcut audit before trusting a benchmark; Execution-verified trajectory generation
- Tools: Docker

## [The Spatial Harness: Bringing Agents to the Canvas — Max Drake, tldraw](../videos/XWcXwnysmpY.md)
`XWcXwnysmpY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, agent-architecture, coding-agents

tldraw's Max Drake on giving LLM agents a spatial canvas: teaching them to read screenshots plus shape data, running multi-agent fairies, and driving live apps and the desktop through code.

- Techniques: Screenshot plus structured data as canvas context; Agentic canvas harness with self-set goals; Visual agent identity and on-canvas task state; Orchestrator agent posting tasks to a shared board; Local editor server for code-mode agents; Dependency graph of agent tasks
- Tools: tldraw SDK, tldraw desktop app, Claude Code, Notion, Gmail, Conductor, OpenAI Symphony

## [Tell the Robot What You Want — Sandhya Subramani, AWS](../videos/S6aSoQ6_u5A.md)
`S6aSoQ6_u5A` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: agent-architecture, voice-multimodal

Live demo of a rover robot driven by an LLM agent built on the Strands harness, with a four-layer agent-to-hardware stack and a pitch that VLA policies may eventually make per-task robot training unnecessary.

- Techniques: Robot as an agent tool; Concurrent specialized agents on one tool surface; Edge/cloud policy split; Teleop for dataset creation; Messaging-app control over cellular
- Tools: Strands Agents (agent SDK), Amazon Bedrock AgentCore, Claude Opus 4.8, OpenAI Realtime (voice), Telegram, Raspberry Pi, VLA models, 4G SIM

## [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](../videos/cI7zfqusmFU.md)
`cI7zfqusmFU` · AI Engineer · 2026-09-18 · q3 · practitioner · demo · also: agent-architecture, infra-cost-scaling

Giselle van Dongen (Restate) argues long-running agents need a durable infrastructure layer, and demos journaled retries, human-approval suspension, keyed sessions and mid-run signal or cancel.

- Techniques: Wrap every side-effecting agent step in a durable run call; Durable promise for human-in-the-loop approval; Keyed virtual object per session for serialized agent state; Classify mid-run input, then signal or cancel-and-restart; Central LLM gateway as its own durable handler
- Tools: Restate, Slack, LiteLLM, Python

## [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../videos/L173Z8DpaJg.md)
`L173Z8DpaJg` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: software-factory, pr-code-review, sandboxing-execution

Safia Abdalla (Warp) on building the Oz cloud agent platform: hide infra complexity, allow any harness, expose everything via API, and run the open-source repo with agent-gated triage and PR review.

- Techniques: Managed plus self-hosted sandboxes behind one model; Harness-agnostic layer with platform guardrails; Orchestrator with mixed-model sub-agents; Agent-gated PR review before human review; Agent-driven issue intake; API-first primitives for agents, sub-agents, environments and artifacts
- Tools: Warp, Oz, Claude Code, Codex, GitHub, Slack

## [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](../videos/AN65uc645mE.md)
`AN65uc645mE` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, inference-serving, evals

Hippocratic AI's engineering lead explains how their clinical voice agent (200M+ patient conversations) hits safety, latency and accuracy at once: a vertically built stack, 31 parallel specialist models, context-fed ASR, and lossless inference tricks.

- Techniques: Parallel specialist models with self-gating; Context-conditioned ASR; Second-pass rescoring for ambiguous short utterances; Async and offline verifiers for tool calls; Human plus synthetic eval mix with sample-size planning; Severity-graded harm rubric; Lossless inference stack
- Tools: Whisper (large-turbo, fine-tuned), speculative decoding, 4-bit quantization, KV cache

## [Where RL Will Take Search — Maximilian-David Rumpf, SID.ai](../videos/iJVxxxHM_Oc.md)
`iJVxxxHM_Oc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: rag-retrieval, training-finetuning-rl, context-engineering

Founder of SID.ai argues search should move from fixed retrieval pipelines to one RL-trained model, reporting about 20x faster and 100x cheaper than frontier-model search agents.

- Techniques: Search as a delegated RL-trained sub-agent; Verifiable retrieval reward for RL; Mixed reward with latency; Learned loop in place of a fixed pipeline; Parallel sub-agent searches
- Tools: BM25, PageRank, vector search, rerankers

## [No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle](../videos/jA_x7F8caHI.md)
`jA_x7F8caHI` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: memory, agent-architecture, enterprise-adoption

Oracle's Kay Malcolm argues that agent harnesses need shared, database-backed memory, using a five-type memory taxonomy and a team memory broker; mostly a product pitch for Oracle AI Database.

- Techniques: Five-type agent memory taxonomy; Shared memory broker tied to repo state; Keeping context alongside commits; Single-store consolidation for agent memory; Private local model for memory extraction
- Tools: Oracle AI Database 26AI, Oracle Agent Memory SDK, Codex, Claude, Git, Neo4j, Redis, OCI Always Free

## [Beyond the Lethal Trifecta: Agentic Commerce on the Open Internet — David Levine, Kiduna Club](../videos/tE2z8-hqoLY.md)
`tE2z8-hqoLY` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: security-guardrails, governance-compliance

Founder talk on the "lethal trifecta" (private data + untrusted content + actions) and a proposed fix: agents as identity-bearing members of legally registered, blockchain-verified organizations. Mostly a pitch for Kaduna Club.

- Techniques: Ally build sequence (inform, instruct, empower, enact, align); Scoped identity tokens for agents (JWT with claims); Decision markets for policy; Per-action audit trail back to a responsible principal
- Tools: OpenCloud (caption spelling; likely OpenClaw, an agent product that the speaker says blew up in January 2026), MOO / LambdaMOO (text-based virtual world the speaker used in 1993), MCP servers (cited as a way enterprises integrate agents), Slack, Salesforce, Notion, Telegram, Twitter, JWT, Vector database (generic, no product named), Blockchain (generic, no chain named), Polymarket (cited as an analogy for decision markets)

## [OpenAI's GPT-6 (Astra) Solves Problems Beyond PhD Level. Is This AGI?](../videos/-aCN5BMq1JI.md)
`-aCN5BMq1JI` · Better Stack · 2026-09-02 · q3 · intro · news · also: models-research, testing-verification

Reports OpenAI's claim that its internal Astra model solved 10 maths and CS problems, checkable via Lean proofs, and argues most of the gain comes from the agent harness, with real sub-agent coordination costs.

- Techniques: Machine-checked verification with a proof assistant; Root agent fans out sub-agents and synthesises; Design long runs against loss of coherence
- Tools: OpenAI Astra (internal, unreleased model), Lean (proof language and compiler), Sol Ultra (OpenAI model with sub-agents, as described in the video), Luna, Terra, Sol (named as OpenAI's existing model family), GPT-5 (OpenAI model, October claim discussed), Claude Code (mentioned only as the host's own point of comparison; not in the transcript)

## [Spotify Made an Agent Harness... I Don't Hate It](../videos/TK1LvtX-Bqs.md)
`TK1LvtX-Bqs` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: coding-agents, dev-tools

Walkthrough of Spotify's closed-source agent session manager "Zerp" (Claude Code, Codex, Gemini in one GUI). Useful session features, but the host finds nothing that justifies the account and closed-source tradeoff.

- Techniques: Dependent worktree chains for agent work; Forking a session to test alternatives; Mid-session agent handoff; Grid monitoring of parallel agents
- Tools: Zerp (Spotify internal agentic development environment; auto-captions transcribe it as Zurb), Claude Code, Codex, Gemini, Portal (Spotify product, related to Zerp), tmux, CMUX, Conductor, T3 Code, Matt Pocock's skills (referenced, not in the video)

## [This Claude Code Skill make Building 10x Faster](../videos/b9k-AE4v5yI.md)
`b9k-AE4v5yI` · AI LABS · 2026-09-02 · q2 · practitioner · review · also: claude-code, skills-self-improvement

AI LABS walks through two Claude Code/Codex skills: one checks existing products and open-source projects before building, and one searches academic papers when nothing is shipped yet. Also covers a publish-once skill distribution setup. Partly a promo.

- Techniques: Clarify-then-search gate with logged assumptions; New-idea vs existing-project branch; Applicability-vs-scale notes for each prior-art project; Three-stage cost check; Install a skill from a GitHub link; Paper-per-sub-agent research fan-out; Publish-once, auto-pull skill distribution; Cheap-first, escalate-on-novelty cascade
- Tools: Claude Code, Codex, GitHub, Advise Project Approach (skill), NeuroArchive (skill), Head Start (skill), skills CLI, Claude Code plugins, Archive (preprint platform), Stream (chat API), Sendbird (chat API), Lovable (sponsor)

## [Buzz Just Fixed AI Agents... But It Has A Serious Flaw](../videos/a8tLTd4q-fU.md)
`a8tLTd4q-fU` · AI LABS · 2026-09-02 · q2 · practitioner · review · also: token-cost-efficiency, coding-agents

AI LABS tests Buzz, an open-source group-chat app where Claude and GPT agents share channels; they find real coordination and token-cost problems but praise its per-agent attribution and cross-vendor adversarial review, and say solo builders should skip it.

- Techniques: Role-explicit prompt for multi-agent planning; Cross-vendor adversarial review of a spec; Per-agent identity and attribution in a shared channel; Agent export with memory; Installing Buzz
- Tools: Buzz (v0.5, open-source group-chat app for agents), Claude Code, Claude Code agent teams, Codex (OpenAI coding agent), GPT (OpenAI model), Goose (coding agent), Slack, Claude Tag (Anthropic Slack agent, team and enterprise plans), OpenAI Codex plugin for Claude Code, EgoLite (sponsored browser-agent skill, Mac only), GitHub, Vercel

## [This Claude Skill Just Fixed Loop Engineering](../videos/D_uojDHkbw4.md)
`D_uojDHkbw4` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: testing-verification, coding-agents

Explains the "gauntlet loop" (agent builds, critic sub-agents judge against a reference) and its two failure modes, then shows a planning-skill fix: a settled spec and pass/fail answer key the critic checks against.

- Techniques: Three-line gauntlet loop prompt; Swap the reference for a planned answer key; Planning fog map; Phased build order inside one loop
- Tools: Claude Code, Wayfinder (Matt Pocock planning skill), Grill Me (Matt Pocock skill), Matt Pocock skill set (installed from GitHub), Claude Max plan, Claude API (cost comparison), SerpAPI (sponsor, not used in the method)

## [Hermes Agent Skills That Make It 10x More Powerful](../videos/WJgxX0Eib6k.md)
`WJgxX0Eib6k` · AI LABS · 2026-09-02 · q2 · intro · review · also: context-engineering, skills-self-improvement, token-cost-efficiency

Walkthrough of third-party skills for the Hermes agent (planning-with-files hook, Delegate Setup, RTK, Mantis security reviews, Agent Reach, Skill Retriever), most of which work with any coding agent; thin on exact commands and partly sponsored.

- Techniques: File-backed plan injected by a hook; Orchestrate several installed coding agents from one agent; Route shell commands through RTK via a skill; Scheduled security review with alerts; Retrieval-filtered skill list
- Tools: Hermes Agent, Claude Code, Codex, Cursor, planning-with-files, Delegate Setup, RTK, Mantis (Google), Agent Reach, Skill Retriever, Plural Workbench, Opus

## [Opus 5 Built An F1 Game... for $1,200](../videos/viHqe5QqTd0.md)
`viHqe5QqTd0` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: agent-architecture, testing-verification, token-cost-efficiency

A Better Stack host runs the "Gauntlet Loop" prompt (a goal plus a real-world target, sub-agents, and a screenshot-based critic loop) on Opus 5 to build an F1 racing game, then judges how playable the result is and what it cost.

- Techniques: Gauntlet loop (goal + real-world target + critic loop); Have the agent build its own verification tools; Stop on plateau, not only on a threshold; Meta-prompt to generate the loop prompt
- Tools: Claude Opus 5, Claude (Max plan subscription, used for the run), Claude sub-agents, Gauntlet Loop prompt (Matt Shumer)

## [GitHub's #1 Trending Author's New Claude Skill Is Insane](../videos/c47uqR7XB_c.md)
`c47uqR7XB_c` · AI LABS · 2026-09-02 · q2 · practitioner · review · also: testing-verification, skills-self-improvement, coding-agents

AI LABS walks through "unlazy," an agent skill that makes coding agents prove each task is done via a gates ledger, tree decomposition and fresh-agent re-checks, plus their fix for its slow sequential runs.

- Techniques: Gates ledger with verifier command; Recursive tree decomposition with depth cap; Orchestrator re-verifies sub-agent claims; Parallel sub-agents with file ownership in plan.md; Explicit give-up instead of silent drop; Installing unlazy into a project
- Tools: unlazy (agent skill; name as spoken in the video), Claude Code, Codex, Ralph loop, Claude goal command, Opus, GPT 5.6, VS Code, Data for SEO (sponsor), model router skill (generic, unnamed)

## [Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi](../videos/s67bE2Ur3bY.md)
`s67bE2Ur3bY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, memory

Sai Krishna Rallabandi on moving agents from one-user assistants to group-chat and wearable agents. Covers the security boundary, memory curation and forgetting, privacy as context, and when to speak.

- Techniques: Action-boundary deterministic guard; Data/instruction channel split with a trained SLM; Atomic fact extraction with hierarchical and temporal links; Continuous relevance scorer for forgetting; Per-user LoRA adapters over a shared memory layer; KV-cache aware memory ingestion; Learned speak/stay-quiet classifier; Private routing via DM
- Tools: LoRA, SLM classifier, regex and traditional NLP guards

## [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](../videos/XLEYtv3cMlw.md)
`XLEYtv3cMlw` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, agent-architecture, evals

Sina Shahandeh (Radicait) on why coding-agent research loops stall on open-ended science, and how decomposing a codebase into linked component docs plus cross-model critique gets better hypotheses.

- Techniques: Hierarchical component docs as a scaffold; Hypothesis generation over each component; Multimodal model as a qualitative metric; Split roles across models in the loop; Per-iteration outcome review
- Tools: Codex, Obsidian, Gemini, Oracle CLI, GPT-5.5 Pro (as transcribed)

## [Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio](../videos/Fu45geO3zX8.md)
`Fu45geO3zX8` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: security-guardrails, mcp-and-tools

Armanas Povilionis (Alithea Bio) argues that cross-organization agent work needs signed, verifiable receipts, and demos Froglet, an open protocol for agents to discover, buy and verify services.

- Techniques: Signed per-step receipts for agent transactions; Marketplace as discovery only, direct peer deals; Same node, role chosen at runtime; Typed payload with schema and deal ID, polled asynchronously; Expose the protocol through MCP and let the LLM drive it
- Tools: Froglet, MCP, Claude, Docker, OpenClaw, NemoClaw

## [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](../videos/khVX_BUnEwU.md)
`khVX_BUnEwU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, skills-self-improvement, memory

Yohei Nakajima presents Active Graph, an experimental event-sourced graph runtime where an immutable typed log is the agent's ground truth and small behaviors coordinate through shared state; main takeaway is that log-centric design gives replay, forks, resume and gated self-modification for free.

- Techniques: Log-as-memory retrieval; Graph-subscription behaviors and graph-query views; Failure-type-scoped, gated self-edits; Acceptance test by simulated win rate with a confidence bound; Debug by querying the event log, not session logs; Pack-based composition of agents
- Tools: Active Graph, BabyAGI, LongMemEval, Replit, Claude Code, LangSmith (mentioned as a comparison), Kaggle Pokemon trading card game competition

## [The New Primitives: Building AI Native Software — Kwindla Kramer, Daily](../videos/LZuWZRze3MU.md)
`LZuWZRze3MU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: product-ux, voice-multimodal, agent-architecture

Kwindla Kramer (Daily, PipeCat) argues agents are a stage on the way to AI-native software, using 80 years of computing history and demos of a real-time Knowledge Navigator and a multiplayer LLM game.

- Techniques: Asynchronous non-blocking context compression for sub-agents; Long-running sub-agents that share context; Progressive skills loading; Dynamic UI generation driven by the agent; Real-time voice plus LLM orchestration with a pipeline framework
- Tools: PipeCat, Gradient Bang, Daily, Tavus

## [Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest](../videos/0RNNfxpdbQk.md)
`0RNNfxpdbQk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: observability, testing-verification, context-engineering

Pinterest's Drasko Profirovic on Medic, an agentic Spark failure-diagnosis tool, and how its prototype became a multi-agent system with record/playback testing, log and metrics handling, and sub-agents.

- Techniques: Record/playback end-to-end agent harness; Learned red-herring filtering for logs; Metrics as a collaged graph image in a quarantined sub-agent; Supervisor with parallel hypothesis researchers; Per-agent prompt plus MCP tool subset; OpenTelemetry traces as step waterfalls
- Tools: Apache Spark, LangGraph, LangGraph DeepAgents, LangFuse, OpenTelemetry, Model Context Protocol (MCP), Grafana, Airflow, Slack, vector database

## [Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates](../videos/u6jJcIFDLE4.md)
`u6jJcIFDLE4` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: agent-architecture, context-engineering, enterprise-adoption

ZS Associates explain why their multi-agent pharma analytics pipeline failed and how they rebuilt it: deterministic signal detection, one reasoning agent, and a knowledge graph used as a control plane.

- Techniques: Probe the design with a coding agent; Deterministic signal gate feeding an investigator agent; Single reasoning owner with scoped investigation subagents; Knowledge graph as the agent's control plane; Hypothesis-traversal investigation loop
- Tools: Claude Code, bash, knowledge graph (tool not named), relational database (not named)

## [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j](../videos/VGN22pPpb-8.md)
`VGN22pPpb-8` · AI Engineer · 2026-08-18 · q2 · intro · keynote · also: data-engineering, memory

Neo4j keynote arguing that agents should be thin and share an ontology-based semantic layer over enterprise data, with execution traces that teach source selection over time.

- Techniques: Business-to-technical ontology mapping; Process graph for process-guided agents; Trace-derived source scores; Thin agents over a shared substrate
- Tools: Neo4j

## [The State of Model Routing — NVIDIA, Cognition, OpenRouter](../videos/QHBjufYK8TA.md)
`QHBjufYK8TA` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · also: token-cost-efficiency, inference-serving, infra-cost-scaling

Panel from Cognition, NVIDIA and OpenRouter on model routing: frontier models plan and delegate to cheaper models, and the hard parts are detecting when a small model is out of depth and keeping cache costs low.

- Techniques: Frontier-planner, cheap-executor split; Frontier watcher with escalation; Persistent sidekick sub-agent; Reference-based handoff; Piggyback checks on cache refresh; Hidden-state probes for lost-ness; Routing from production signals; Ask the model why, then regression-test the prompt; Privacy-aware local/cloud split
- Tools: Devin, Cognition Fusion, OpenRouter Fusion, OpenRouter Pareto Code, NVIDIA Nemotron, NVIDIA Dynamo, NVIDIA DGX Spark, OpenClaw, TerminalBench, LMArena

## [Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft](../videos/o6U_2vd967Y.md)
`o6U_2vd967Y` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, data-engineering

Divakar Kumar shows how to add an agent tier for gray-zone fraud decisions in an event-sourced system, feeding agents a semantic read layer built from CDC and broker events.

- Techniques: Tier-2 escalation for gray-zone cases; Semantic layer built from CDC and broker events; Fan-out to specialist agents with a verdict agent; Saga-style orchestrator as the sole cross-context router; Hard cap on the agent reasoning loop; In-memory short-term agent memory under an SLA
- Tools: Azure Cosmos DB (event store and change feed), message broker (unnamed), CDC / change feed, rule-based engine, ML risk model (third-party)

## [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../videos/Kz4QJmNrVXU.md)
`Kz4QJmNrVXU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: context-engineering, coding-agents

Matt Dailey (Ref) argues that AI makes individual engineers faster but not teams, and proposes working in shared docs for decisions, with agents as stateless actions, so humans keep ownership of the product.

- Techniques: Doc as shared state, agents as stateless workers; Two-gear workflow: plan vs polish; Front-load decisions before code; Plan as a portal to the system; Idea exploration before build

## [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](../videos/kiqubc5b5Yo.md)
`kiqubc5b5Yo` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, agent-architecture, enterprise-adoption

Morgan Stanley's AlphaLab, a multi-agent harness that automates quant research through research, critic-checked eval building, and Kanban-style experiments. Its main lesson: the value sits in strict eval environments and rubrics, not in the harness.

- Techniques: Scaffolded to-do list with re-prompting on early exit; Builder plus critics eval loop; Strategist, worker, and post-mortem Kanban loop; Containerised, Kaggle-style eval contract; Environments as RL reward signal; Rubric grading of each rollout's process; Meta-harness optimisation by an LLM; Provider-agnostic harness with functional tool calls
- Tools: Claude Code, Codex, Opus 4.5, Slurm, Kaggle, GRPO, NVIDIA Nemotron

## [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](../videos/yWS0udrIOc8.md)
`yWS0udrIOc8` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: security-guardrails, pr-code-review

Steve Yegge argues AI-generated code multiplies security defects and new attack types (slopsquatting, prompt injection, agent credentials), and urges security scanning at generation time and as a separate pass.

- Techniques: Surface security findings at generation time; Separate security and correctness into different passes; Run several scanners and have agents cross-check; Supply-chain vetting of dependencies and base images; Adversarial supervisor agents for queue-driven agents; Least-privilege credentials per agent action
- Tools: Claude Code, Beads, Gas Town, Snyk (called Sneak in captions), Chainguard

## [Build the AI GTM Agent That Knows the Buyer - Dr. Sajjan Kanukolanu, Position2 (Position Squared)](../videos/ltv-L5oMPIs.md)
`ltv-L5oMPIs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: enterprise-adoption, data-engineering

Position Squared's three-layer, multi-agent GTM system (anonymous visitor ID, knowledge-base-gated ICP and CRM matching, rep actions). Lessons: ICP drift, alert fatigue, weak identity accuracy, and approval friction.

- Techniques: Dedupe-then-enrich identification; Knowledge-base-gated ICP filter agent; Per-person context graph with account and deal rollup; Separate fit score from intent score; Personalized returning-visitor chat; Quarterly ICP refresh from closed outcomes; Alert budget tuned to rep capacity; Auditable, adjustable policy engine; One-click draft approval with a 30-second budget
- Tools: HubSpot, Slack, LinkedIn

## [Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](../videos/z0sh8HyTrDo.md)
`z0sh8HyTrDo` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: software-factory, coding-agents, governance-compliance

Auditoria AI speaker says human attention bottlenecks agent work: use parallel worktree subagents, skills, one-pane UX, goals and loops, and self-improving harnesses, keeping humans at intake and sign-off.

- Techniques: Worktree-per-task parallel subagents; Ticket-to-stage pipeline with two human gates; Encode organizational procedure as skills; Single-pane minimal UX for orchestration; Daily self-retrospective on the agent's own loop; Goals plus loops, monitored from a phone; Background dreaming for pattern compaction
- Tools: Claude Code, git worktrees, Kubernetes, Docker, Jira, GitHub, MCP

## [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../videos/il1c1a2FufU.md)
`il1c1a2FufU` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: coding-agents, context-engineering, skills-self-improvement

Jason Liu (OpenAI) shows how he runs Codex as a personal ops system: pinned long-lived threads, a git-tracked memory vault, heartbeats, and goal verifiers. Main takeaway: compaction makes long threads workable.

- Techniques: Long-lived pinned thread per workstream; Heartbeat / loop in the same thread; /goal with a verifier and file-backed goal; App shot plus accessibility tree; Git-tracked personal memory vault with agents.md routing; Monitor thread that spawns per-issue threads; Skill from one completed run, with self-edit permission; Annotate a localhost preview to steer the agent; Model and reasoning tiering
- Tools: Codex app, Codex CLI, Codex in-app browser, computer use, Chrome extension, Slack connector, Gmail connector, Google Drive connector, Notion, Linear, Obsidian, GitHub

## [Claude for Long-Horizon Tasks — Lance Martin, Anthropic](../videos/9QebvrrY3KY.md)
`9QebvrrY3KY` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: agent-architecture, memory, context-engineering

Lance Martin (Anthropic) on designing long-horizon async agents: decouple brain from hands, verify in a separate context, dream offline to fix memory, and run org-level shared harnesses.

- Techniques: Brain/hands split with an append-only session log; Non-destructive context via append-only session object; Build/verifier loop in separate contexts; Dreaming: offline memory consolidation; General memory substrate with the model managing its own structure; Org-level shared harness with its own identity
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, Claude Tag, Message API, Continued Learning Bench, METR time-horizon benchmark, Slack

## [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../videos/Z-c11pV_uvU.md)
`Z-c11pV_uvU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: agent-architecture, claude-code, context-engineering

Frank Coyle (UC Berkeley) walks through the Claude Certified Architect exam's scenarios and uses each one's anti-patterns to teach agent loops, subagent context isolation, compaction, and non-interactive runs.

- Techniques: Stop-reason-driven agent loop; Three-level CLAUDE.md hierarchy; Single-purpose subagents with minimal tools; Context slicing for critic and reviewer agents; Forked subtask context with summary return; Threshold-triggered compaction; Non-interactive CI runs with batch processing
- Tools: Claude Code, Claude API (messages, stop_reason, tool use), CLAUDE.md, MCP (Model Context Protocol), Message Batches API

## [This New Skill Finally Solves Thinking For AI Agents](../videos/m6IXL_YGqBQ.md)
`m6IXL_YGqBQ` · AI LABS · 2026-08-02 · q2 · intro · review · also: coding-agents, testing-verification, skills-self-improvement

AI LABS walks through a community "ADHD" skill that makes a coding agent ideate by fanning out isolated sub-agents, each seeded with a different frame, then scoring and merging the results; shown for test planning and pre-ship UX/churn review.

- Techniques: Frame-diversified tree-of-thought fan-out; Three-question gate before auto-invoking an expensive fan-out; Install an agent skill from a repo and fix the config folder for Claude Code; TDD test-strategy planning with PRD and tech spec linked in CLAUDE.md; Pre-launch UX and churn review by fan-out
- Tools: Claude Code, Codex, Cursor, CLAUDE.md, .agents folder (installer target), SKILL.md, Top View (sponsor; AI video skill), Kling, Sea Dance, Nano Banana

## [Jack Dorsey's New App Is Coming for Slack and GitHub (buzz)](../videos/CHEMPZ87FLw.md)
`CHEMPZ87FLw` · Better Stack · 2026-08-02 · q3 · intro · review · also: coding-agents, security-guardrails, token-cost-efficiency

Hands-on walkthrough of Block's open-source Buzz, a Slack-like workspace for humans and AI agents built on Nostr with signed audit trails. Covers agent setup, a two-model coding contest, and a warning about runaway token use.

- Techniques: Bootstrap a Buzz community; Custom agent with persona, harness and model; Head-to-head model contest, then cross-model audit; Stop runaway multi-agent loops
- Tools: Buzz, Nostr protocol (the video says 'Noster'), Nostr relay (Block's hosted relay, in beta), BitChat (Bluetooth mesh app that adopted Nostr 2 as a fallback transport), Agent Client Protocol, Claude Code, OpenAI Codex, Goose (Block's agent framework), OpenRouter, Gemini 3.6 Flash (as named in the video), GLM 5.2 (as named in the video), GPT 5.6 Sol (as named in the video)

## [Anthropic Just Fixed Graph Engineering's Greatest Flaw](../videos/H7t3uUp3HVw.md)
`H7t3uUp3HVw` · AI LABS · 2026-08-02 · q2 · intro · tutorial · also: testing-verification, claude-code, skills-self-improvement

Graph engineering fans agent work across parallel nodes but hides failures; the video's fix is layered verification skills built with Skill Creator, plus a fresh-context Opus second opinion.

- Techniques: Install Skill Creator as a plugin; Standalone deep-review skill; Embedded verification skill that runs after each feature; Embedded rule-gate skill; Second-opinion skill via claude -p; Headless browser for visual verification; One skill per review angle, chained by an orchestrator skill; Write build, test and lint commands into CLAUDE.md; Pin the judging node to a stronger model
- Tools: Claude Code, Claude Opus, Claude Haiku, Codex, Skill Creator plugin, verify skill, code review skill, simplify skill, design skill, design.md, second opinion skill, CLAUDE.md

## [LangChain Open Sourced Claude Code (Works With ANY Model)](../videos/jtWjkdBNqlk.md)
`jtWjkdBNqlk` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: agent-architecture, memory, claude-code

Kai Explains reviews LangChain's open-source DeepAgent, a model-agnostic take on Claude Code's harness, arguing it wins for shipping agents to users while Claude Code still wins for personal terminal coding.

- Techniques: Audit your harness against the five-part checklist; Subagents with isolated context returning one summary; Keep agent memory in a store you control; Swap the model behind a fixed harness; Use a lighter agent abstraction for bounded tasks
- Tools: DeepAgent (Deep Agents, LangChain), LangChain 1.0, LangGraph, LangSmith deployment, Claude Code, Claude Opus 4.8 (as stated), Claude Managed Agents, Codex, Cursor agent mode, GPT 5.5 (as stated), PostgreSQL, agents.md

## [Open Source Is Back. Goodbye Claude.](../videos/wOfm7x0i3sw.md)
`wOfm7x0i3sw` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: coding-agents, token-cost-efficiency, claude-code

Better Stack walkthrough of OpenCode, an open-source terminal coding agent with bring-your-own models and custom subagents, weighed against Claude Code; the cost verdict depends on whether you pay per API token or hold a subscription.

- Techniques: Pin a cheap model to a specialist subagent; Low-temperature review subagent; Same agent definition in one JSON file; Enable LSP for type-aware feedback; Generate AGENTS.md with /init; Plan then build
- Tools: OpenCode, Ghostty, models.dev, big pickle (free default model in OpenCode), GLM 5.2, DeepSeek 4, Claude Sonnet 4, Fable 5 (named as a comparison model), Claude Code, GitHub Copilot (comparison), Design Arena (benchmark), AGENTS.md

## [OpenAI Sol Ultra Just BEAT Claude Fable](../videos/27QLmUQvL2A.md)
`27QLmUQvL2A` · Better Stack · 2026-08-02 · q2 · intro · news · also: models-research, evals, coding-agents

Better Stack on GPT-5.6 Sol and its Ultra sub-agent mode: 91.9% Terminal-Bench 2.1, METR caught heavy test-gaming, Sol costs about half of Claude Fable 5.

- Techniques: Tiered model routing by task weight; Discount benchmark leads when the independent evaluator disputes them; Watch unattended runs for test-gaming
- Tools: OpenAI Codex, GPT-5.6, GPT-5.5, Sol, Terra, Luna, Sol Ultra (Ultra mode), Terminal-Bench 2.1, Claude Mythos 5, Claude Fable 5, METR time-horizon evals, Cerebras chips

## [All The Types Of Claude Loops Explained In 13 Minutes](../videos/8wsM0euQOvc.md)
`8wsM0euQOvc` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: agent-architecture, claude-code, testing-verification

AI LABS sorts Claude Code agent loops into five types (stateless, learning, multi-agent review, verification, workflow-improvement) with setup steps; anecdotal, with a sponsor segment.

- Techniques: Goal-command loop with tests as the acceptance criterion; Save-every-working-version rule in CLAUDE.md; Skill-improvement loop (learning loop); Multi-agent review loop with an orchestrator; Implementer vs. scorer verification loop; Workflow-improvement loop with a process optimizer
- Tools: Claude Code, CLAUDE.md, Haiku (completion checker in the goal loop), Ralph loop (named as a stateless loop example), goal command, skill loop command (name as spoken), learning.md, thermonuclear review (review skill, named as spoken), orchestrate command, review loop command, iterate command, JSON files (findings and scores)

## [Bun Moved To Rust... Zig's Creator Fired Back](../videos/0TSxrzBVEwQ.md)
`0TSxrzBVEwQ` · Better Stack · 2026-08-02 · q4 · practitioner · news · also: software-factory, testing-verification, coding-agents

Bun ported its ~1M-line codebase from Zig to Rust in 11 days using parallel Claude agents with an implementer, two adversarial reviewers and a fixer; the video also covers Zig creator Andrew Kelly's public criticism.

- Techniques: Adversarial review loop per unit of work; Porting spec plus lifetime table before code generation; Faithful port over idiomatic rewrite, all at once; Guardrails for parallel agents on one git repo; Sharding by git worktree; Error-driven crate-by-crate loop; Reviewer rule against justified workarounds; Test-file batch loops as the verification step
- Tools: Bun (1.3.14 final Zig release, 1.4 Rust), Zig, Rust, Claude / Claude Code, Fable 5 (pre-release model, as named in the video), cargo, git (worktrees), Next.js (dev-server hot reload test), JavaScriptCore, TigerBeetle (referenced by Kelly), Hacker News / GitHub (where the porting doc was noticed)

## [MCP vs REST vs A2A How AI Agents Actually Talk](../videos/psszX04xeGU.md)
`psszX04xeGU` · Kai Explains · 2026-08-02 · q3 · intro · other · also: mcp-and-tools, agent-architecture

Explainer arguing REST, MCP and A2A are stacked layers, not rivals: REST links programs, MCP links an agent to tools, A2A links agents to agents. Advice: learn MCP first and add A2A only for multiple independent agents.

- Techniques: Map each integration to one protocol layer; Expose each tool once as an MCP server; Wrap an existing REST API with a thin MCP server; Publish an agent card for discovery and delegation; Adopt multi-agent protocols only when the pain is specific
- Tools: REST, MCP (Model Context Protocol), A2A (Agent2Agent), JSON-RPC 2.0, HTTP, stdio

## [7 Rules To Use GPT 5.6 Sol Better Than 90% Of People](../videos/STczJBYJf7w.md)
`STczJBYJf7w` · AI LABS · 2026-08-02 · q3 · practitioner · review · also: coding-agents, context-engineering, token-cost-efficiency

AI LABS' four-day hands-on comparison of GPT 5.6 Sol and Fable: Sol is better at finishing long autonomous work and screen-based review, Fable at deciding what to build, plus seven usage rules.

- Techniques: Git checkpoint before a long autonomous run; Codex app sandbox and approval configuration; Single-session delegation of multi-session work; Role-by-role journey review after the build; One-instruction-removal test for prompts and skills; Plan with one model, build with another
- Tools: GPT 5.6 Sol, GPT 5.6 Terra, GPT 5.6 Luna, Ultra (Sol multi-agent mode), Codex (app and CLI), ChatGPT app, Fable, Opus 4.8, Opus, Sonnet, Qwen 3.6, Cursor

## [Fleet Engineering Is Insane... The Next Evolution Of Vibe Coding](../videos/qxjII6x2yPY.md)
`qxjII6x2yPY` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: claude-code, sandboxing-execution, coding-agents

Walkthrough for running many Claude Code sessions in parallel: resume and handoff basics, file ownership, background dashboards, git worktrees, issue-driven orchestration, and Docker Sandbox isolation.

- Techniques: Session recovery with continue, resume, recap, export; File ownership by prompt; Plan-mode task decomposition; Handoff documents via the handoff skill; Background sessions and the agent dashboard; Git worktrees per session; Issue-driven background orchestration; Docker Sandbox for isolated execution with clone mode
- Tools: Claude Code, Claude Code plan mode, Claude Code background sessions, Claude Code agent dashboard, handoff skill, git worktrees, OpenAI Symphony, Codex, Linear, GitHub, Docker Sandbox (sbx), Docker micro-VM sandboxes

## [How To Use Claude Fable 5 Better Than 90% Of The People](../videos/GM7-ei-4Xc8.md)
`GM7-ei-4Xc8` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: claude-code, token-cost-efficiency, testing-verification

How a small AI-coding team runs Claude Fable 5 in Claude Code: keep effort at low-high, plan big and implement small, test-first with a separate test author, and layered code and security review subagents.

- Techniques: Keep effort between low and high; PRD-first planner/implementer split; Subagent routing tiers in CLAUDE.md; Ponytail with a test net; Separate test-author subagent (TDD); Parallel scoped security review; Architecture review subagent; HTML mock-up before build; Pre-merge comprehension quiz
- Tools: Claude Code, Claude Fable 5, Claude Sonnet 5, Claude Opus, Claude Mythos, OpenAI Codex CLI, OpenAI Codex plugin for Claude Code, Ponytail, Cursor Thermonuclear Code Quality Review skill, Claude Code security review GitHub Action, CLAUDE.md, Veed (sponsor)

## [Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](../videos/q4Tr-DknG2M.md)
`q4Tr-DknG2M` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: training-finetuning-rl, evals, models-research

Cursor's Lee Robinson on how Cursor trains its Composer models: a two-loop flywheel, defenses against eval hacking, textual-feedback RL, and models increasingly helping train their successors.

- Techniques: Eval hygiene for agent benchmarks; Private held-out eval from your own repos; Ablate-and-reimplement RL task generation; Textual feedback for credit assignment; Distilled judges and reward models from the top model; Agent fleets launched from chat with escalation to humans
- Tools: Cursor, Composer, Kimi (prior open-source base model; transcribed as 'Kimmy'), Colossus, Slack, Git, Datadog, Notion, Linear, MCP, Artificial Analysis

## [Build Systems, Not Code - Angie Jones, Agentic AI Foundation](../videos/ZD9-4fW2HhM.md)
`ZD9-4fW2HhM` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, context-engineering, security-guardrails

Angie Jones on designing agentic systems like software: systems thinking, workflow paths, decomposition, code-vs-model-vs-human splits, contracts, idempotent retries, and maintainable agents.md files.

- Techniques: Decompose a giant agent prompt by responsibility; Route work by task type: code, model, or human; Structured decision records as agent memory; Idempotent action log with state-based resume; Evidence-not-instructions handling for untrusted content; agents.md at every level with a cold-start test
- Tools: agents.md, agent skills, subagents, Karpathy LLM Wiki (agent memory layer)

## [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](../videos/pMggiOb18tc.md)
`pMggiOb18tc` · AI Engineer · 2026-07-18 · q3 · intro · keynote · also: coding-agents, software-factory, agent-architecture

OpenAI's Codex team argues engineers move from watching agents to running manager-worker loops, with human attention as the scarce resource to spend on the outer loop.

- Techniques: Long-lived manager agent over worker agents; Trigger-driven manager wake-ups; Offload test runs to a separate machine; Server-side compaction for long tasks; Parallel attempts with a fast, strong model; Shared instruction file across agents; Chat-first UI with escalation to direct editing
- Tools: Codex, Codex app, Codex Cloud, Responses API, AGENTS.md, OpenClaw, OpenCode, Cerebras, VS Code extension, Xcode, JetBrains, Slack

## [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../videos/4kYl2_mqmnQ.md)
`4kYl2_mqmnQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: claude-code, context-engineering, coding-agents

A KRAFTON engineer runs AI coding agents across three machines, organizes them as a hierarchy, keeps state in files, and lists the five failures and four open problems that followed.

- Techniques: Agent org hierarchy with scoped context; File-backed agent state with handoff folders; Clear-and-reload instead of compaction; Blocking review gateway with approval hook; Force delegation through a CLI harness; Git-based context sync with per-machine partitions; Single always-on control plane and chat router; Boot command that restores the fleet from state files
- Tools: Claude Code, tmux, tmux capture-pane, SSH, Git, Discord, MCP servers, Kubernetes, Linux, macOS

## [Beyond the Harness: A Journey Towards Adaptative Engineering - Rajiv Chandegra, Annicha Labs](../videos/qdZzND79mcg.md)
`qdZzND79mcg` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: agent-architecture

A London-based practitioner argues that fixed agent harnesses fail in messy real-world settings and proposes "adaptive engineering," where engineers set constraints and let multi-agent harnesses emerge and reshape at runtime.

- Techniques: Constraint-setting instead of outcome-setting; Sense-and-respond loop for complex work; Penalise redundancy to force specialisation; Dial the coupling rate; Three-question constraint review; Selection pressure check against drift
- Tools: Claude Code, Codex, Pi, Cursor, LangChain, Hermes, Cline, Goose

## [The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab](../videos/sum9DgexFRQ.md)
`sum9DgexFRQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: mcp-and-tools, security-guardrails, infra-cost-scaling

Ramesh Raskar and Maria of MIT's Project Nanda outline an open infrastructure for a web of AI agents: a signed discovery index, agent hosting, and NandaTown, a simulator for testing agent networks before they go live.

- Techniques: Signed agent facts record and agent card; Message box in front of the agent runtime; Adaptive endpoint resolution; Sleep and wake hosting; Tiered simulation with scripted agents, then LLM agents; Onboarding in three tiers
- Tools: Nanda index, NandaTown, OpenClaw, Maritime, AWS, DNS, YAML

## [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](../videos/whue9_YquGA.md)
`whue9_YquGA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: software-factory, enterprise-adoption, pr-code-review

Angie Jones (Block) describes moving a 3,500-person engineering org to autonomous agent delegation via a maturity model, a power-user champions program, AI-ready repos, and an orchestrator.

- Techniques: Stage-based maturity model for agent use; Champions program of hand-picked power users; Layered repo context files; Delegation from the tools people already use; Review agent plus auto-fix loop; Isolated cloud workspace per agent; Machine-readable system map for orchestration
- Tools: Claude Code, Goose, Codex, BuilderBot, GitHub, Jira, Linear, Slack, MCP, AGENTS.md, CLAUDE.md

## [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](../videos/2e9ANoOEn28.md)
`2e9ANoOEn28` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, security-guardrails, evals

Aditya Bhargava (Etsy) argues the agent harness, not the model, drives results, especially for weaker models, and walks through building a coding-agent harness step by step in his language Agency.

- Techniques: Tools as plain functions with docstrings; Interrupt plus handler for approvals; Partial function application for capability scoping; ReAct test-feedback loop; Subagents as tools with grouped tool sets; Objective-driven prompt optimization; Serializable pause and resume at interrupts
- Tools: Agency (agencylang.com, TypeScript-like agent language, installed via pnpm), HarnessBench (harness benchmark, 106 tasks), Claude Code (cited as an example agent: Opus model plus harness), Built-in Agency log viewer, Built-in Agency standard library (includes Wikipedia search tool)

## [From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](../videos/GdvKNwMcfd0.md)
`GdvKNwMcfd0` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: coding-agents, context-engineering, software-factory

Microsoft's Chris Noring on moving from writing code to running agents: start in the CLI, use AGENTS.md, skills and custom agents as guardrails, and delegate background work that comes back as draft PRs for human review.

- Techniques: Layered repo guardrails (AGENTS.md, skills, custom agents); Tools allowlist to constrain an agent; Delegate to a background cloud agent that returns a draft PR; Parallel terminals as a scaling model; Ask the agent to write its own skill or instructions
- Tools: GitHub Copilot CLI, Claude Code, Claude Desktop, VS Code, GitHub Copilot cloud agent, GitHub MCP server, Playwright MCP, AGENTS.md, SKILL.md skills, custom agents (.github/agents)

## [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](../videos/WLXxTaPagA8.md)
`WLXxTaPagA8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, evals, observability

Solo agent builders keep rebuilding CI/CD-style controls (regression tests, alerts, contracts, staging, audit trails) one failure at a time; the talk argues for blocking gates at the most expensive handoff.

- Techniques: Boring blocking gates before save; Guarded vs naive mode demo; Handoff mapping; Per-gate audit record; Voice and domain contracts as explicit rules
- Tools: Claude Code

## [When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis](../videos/XovaGv4f39A.md)
`XovaGv4f39A` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: rag-retrieval, context-engineering, infra-cost-scaling

Luis Romero-Sevilla (Orbis) on Extended Cache Augmented Generation (ECAG): for large, frequently replaced, densely interrelated document collections, split docs across parallel KV-cached context buckets and let a supervisor model interrogate them, instead of RAG or GraphRAG.

- Techniques: Parallel context buckets with a supervisor (ECAG); Dropping topical sharding for bucketing; Caching KV state per context bucket
- Tools: GraphRAG, vector database, KV cache

## [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](../videos/spNAUEgq_A8.md)
`spNAUEgq_A8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, agent-architecture, infra-cost-scaling

Justin Schroeder (Standard Agents) argues that small, isolated domain-specific agents composed under a coordinator beat ever-growing context-stuffed general agents on cost, scope, portability and scaling.

- Techniques: Composition of isolated domain agents; Scoped delegation requests; Per-task model routing; Hook-injected runtime facts; Capability scoping per agent; Recursive sub-agent tree
- Tools: Claude, Codex, OpenClaw, Hermes, MCP, Vercel AI SDK, Vercel Eve, Figma, Playwright, Gmail, Google Sheets, Google Workspace

## [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](../videos/YZQsWVeN3rE.md)
`YZQsWVeN3rE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: evals, context-engineering, rag-retrieval

Alex Bauer (Upside.tech) on building trust in AI for go-to-market data: manage agents like people, scaffold business context first, use a librarian and a jury-and-judge pattern, and use only tier-two agent harnesses for important work.

- Techniques: Commander's intent prompting; Anchor assets and scaffolding; Citation tracing for verification; Librarian pre-query lookup; Jury and judge; Tiered tool selection
- Tools: Claude, Claude Opus, Slackbot, ChatGPT

## [Everything we knew about software has changed — Theo Browne, @t3dotgg ​](../videos/xUnRQ9vLXxo.md)
`xUnRQ9vLXxo` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: product-ux, coding-agents, agent-architecture

Theo Browne argues that models have moved coding into an orchestration era, so tools, product tiers and software defaults should be rethought, with a markdown file running on cron as his example.

- Techniques: Markdown as a recurring program; Prompt-driven sub-agent orchestration; Breadth-first product with extension points; Assumption audit
- Tools: Claude Code, Codex, Git, GitHub, S3, Cron, Vercel, Slack bot APIs, Reddit, OBS, tmux, GNU Screen

## [Recursive Coding Agents - Raymond Weitekamp, OpenProse](../videos/3hXJI2q0Jz8.md)
`3hXJI2q0Jz8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, coding-agents

Raymond Weitekamp (OpenProse) on applying recursive language model (RLM) ideas to coding agents, with Claude Code dynamic workflows, the Pi extension, and OpenProse markdown workflows as ways to build them.

- Techniques: RLM as a tool call for a coding agent; Recursive agent via a pure Pi extension; Map-reduce versus deep-research workflows in Claude Code; Declarative workflow with parent verification; Adversarial or skeptical subagent roles; Golden session distillation; Small local model as RLM root
- Tools: Claude Code, Codex SDK, Pi, OpenProse, DSPy (dspy.rlm), RLM package (Alex Zhang), Agentica (Symbolica), Axe, Unix RLM (bash), LambdaRLM, Qwen 3.5 9B

## [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](../videos/kZsf_Sfm7RU.md)
`kZsf_Sfm7RU` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: observability, pr-code-review, evals

Shipping an agent is where the real work starts. Raphael Kalandadze shows a post-launch loop: a log-monitor agent opens PRs, a fresh-context review agent critiques them, and a session analyzer scores every conversation for health.

- Techniques: Hourly log-monitor agent that opens PRs; Fresh-context review agent as a PR gate; Session analyzer for health scoring; Computer-use QA agent with a site-specific skill; Meta-harness: connect all context to the monitoring agents
- Tools: Claude Code, Codex, HTML artifacts, log and trajectory store, browser computer-use agent

## [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](../videos/9arM9b7JgOo.md)
`9arM9b7JgOo` · AI Engineer · 2026-07-18 · q2 · intro · workshop · also: coding-agents, context-engineering

Snapchat engineer Jeffrey Lee-Chan demos his personal coding-agent workflow built on OpenClaw: a manager agent with memory delegates work to parallel worktree workers, and separating the manager's context from the workers' reduces overclaiming.

- Techniques: Manager and worker split with a separate-context reviewer; Layered verification with humans last; Context budgeting for the orchestrator; Local, staging, then production flow for agent changes; Cost-tiered model switching
- Tools: OpenClaw, CMUX, Claude Code, Claude Code Teams, Codex 5.3, GPT-5.4, MiniMax, git worktrees, Docker

## [Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta](../videos/grdoOC1BT1s.md)
`grdoOC1BT1s` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: product-ux, vibe-coding-app-building

Two Meta game-creation leads argue that AI prompting makes basic games easy, so taste, art cohesion, playtesting and runtime-LLM NPCs decide quality, with undeterminism as the open engineering problem.

- Techniques: Key-art anchoring for image generation; Personality-driven LLM NPCs in a shared game loop; Parallel AI-assisted production with frequent playtests; Runtime LLM game master for per-player adjustment
- Tools: Gemini, Nano Banana, Meshy, Manus, Labubu (demo subject)

## [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](../videos/vJukHCIv7Ck.md)
`vJukHCIv7Ck` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: mcp-and-tools, rag-retrieval, security-guardrails

AWS developer advocate walks through five code-level techniques to reduce agent hallucinations: semantic tool selection, GraphRAG for aggregation, multi-agent validation, code-enforced hooks, and steering rules. Demos use dummy tools.

- Techniques: Semantic tool selection; Per-turn tool swap in agent loop; Text-to-Cypher GraphRAG for aggregation; Executor, validator, critic swarm; Before-tool-call hooks for hard rules; Steering rules for soft constraints
- Tools: Strands Agents, OpenAI API, sentence-transformers, Neo4j (Cypher, LLM graph builder), agent-control (steering SDK), Amazon Bedrock AgentCore (Gateway, Runtime, Policy, Memory), DynamoDB, Neo4j AuraDB, AWS Lambda, Ollama (mentioned)

## [Using LLMs to Secure Source Code — Eugene Yan, Anthropic](../videos/imFedndyXYQ.md)
`imFedndyXYQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: security-guardrails, testing-verification, sandboxing-execution

Eugene Yan (Anthropic) walks through a six-step harness for using LLMs to find, verify, triage and patch vulnerabilities, arguing the bottleneck has moved from finding bugs to verification, triage and patching.

- Techniques: Threat model as a living context document; Isolated, reproducible PoC sandbox; Independent adversarial verifier; Tool-equipped discovery; Less prescriptive prompts for stronger models; Patch validation ladder with a generative verifier loop; Close the loop as a regression check; Severity triage as impact times likelihood with compensating controls; Code-owner routing without an LLM
- Tools: Claude, Claude Code, Docker, PostgreSQL, Redis, Jira

## [The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft](../videos/jtzh-GBXBWc.md)
`jtzh-GBXBWc` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: memory, skills-self-improvement, enterprise-adoption

A 100-person Indian thermoforming-machine maker built a 36-agent go-to-market "brain" with layered memory and a nightly dream cycle, with no training and no framework. The talk is a company story with some architecture and cost claims.

- Techniques: One-job specialist agents with an orchestrator and debate; Layered agent memory with a salience gate and correction precedence; Nightly consolidation (dream cycle) job; Rules file as production guardrails; Chunk-and-extract over a private corpus with no training; Draft-only outbound with human send
- Tools: Cursor, vector database, graph database, CRM, Google Workspace integrations, document ingestion tooling, monitoring tooling

## [What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip](../videos/7P0elyLIxXo.md)
`7P0elyLIxXo` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, agent-architecture

Dotta (Paperclip) argues "done" is a bundle of claims, not a checkbox, and shows how a control plane with blockers, reviewers, and watchdogs keeps agent work moving while still verifying it.

- Techniques: Done as a structured object; Cross-model verifier; Evidence-first completion; Watchdog agent for goal persistence; Explicit state transitions with enforced blockers; Per-task reviewer and approver assignment with audit trail
- Tools: Paperclip, Pi, OpenClaw, Hermes, Claude Code, Codex

## [19 Hidden Features To Unlock The True Potential Of Your Hermes Agent Setup](../videos/nN6DZi_fiSo.md)
`nN6DZi_fiSo` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: agent-architecture, context-engineering, token-cost-efficiency

AI LABS walks through about 19 Hermes agent config settings (context limits, compression, sub-agents, auxiliary models, quick commands, checkpoints, YOLO, isolation mode) that they changed to fix workflow problems, with defaults and new values.

- Techniques: Per-profile config tuning; Compression threshold and tail tuning; Sub-agent concurrency, depth and permission settings; Cheap auxiliary models and effort control; Exec and alias quick commands; File checkpoints and rollback; Ephemeral system-prompt variable; Isolation mode for config debugging
- Tools: Hermes (agent, config.yaml, Hermes config / auth / personality / rollback commands), Claude Code (compared; dangerously-skip-permissions mode compared to YOLO), Codex (compared; compression threshold comparison), OpenRouter (provider; default auxiliary model fallback), Gemini Flash (auxiliary model used in their setup), Opus (main model example), Gemini (1M-token window model mentioned), Slack (used to coordinate the team via Hermes), Notion, Jira, Airtable (integrations named in the sponsor segment), Helix (sponsor, not evaluated)

## [These Claude Workflows Turn Claude Code Into A Whole OS](../videos/5LnwJyi1il4.md)
`5LnwJyi1il4` · AI LABS · 2026-07-02 · q3 · intro · review · also: coding-agents, claude-code, token-cost-efficiency

Walkthrough of how Claude Code's pieces (CLAUDE.md, MCP, skills, loops/routines, dynamic workflows) form an "OS", with guidance on when a deterministic workflow beats goal or a plain skill; mostly a sponsored-style pitch with thin hands-on steps.

- Techniques: Start a dynamic workflow; Strict output schemas for sub-agents; Choose workflow vs goal vs skill; Convert a skill from a session; Coding-project OS setup; Second-brain audit workflow
- Tools: Claude Code, Claude Opus 4.8, CLAUDE.md, MCP, Google Calendar MCP, Notion MCP, Deep Research workflow, goal command, loops, routines, hooks, skills

## [Krea 2 image model, Sakana Fugu beats Fable 5, Seedance 2.5, Seed 2.1 & More AI News](../videos/q8NQD1IZnFk.md)
`q8NQD1IZnFk` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, skills-self-improvement, voice-multimodal

Weekly AI news roundup (July 2026): Seedance 2.5 preview, Sakana Fugu model routing, Ling/Ring 2.6 open trillion-parameter MoEs, Krea 2 open weights, NVIDIA BioNeMo skills. Nearly all numbers are vendor-reported.

- Techniques: Documented skill specs for domain tools (BioNeMo skills); Single-endpoint learned model assembly (Sakana Fugu); Sparse 3D box blocking for object motion (Loose Control Video); Bidirectional generation for seamless loops (Unitemp); Reasoning effort toggle per task (Ring 2.6); Pick the Krea 2 checkpoint by use (RAW vs Turbo)
- Tools: Seedance 2.5 (transcribed as CDance 2.5), Seedance 2.0, Veo 3.1, Kling 3.0, Sakana Fugu, Trinity (ICLR 2026), Conductor (ICLR 2026), Ling 2.6, Ring 2.6, ICEPOP (async RL method), Gemini 3.1 Pro, Claude Opus 4.7

## [herdr: Is This the Ultimate Agent Multiplexer?](../videos/PlN86TvzGy4.md)
`PlN86TvzGy4` · Better Stack · 2026-07-02 · q3 · intro · review · also: coding-agents, dev-tools

A walkthrough of herdr, a single Rust terminal multiplexer that adds agent awareness (working, blocked, done) to tmux-style panes, lets agents drive it through a CLI or socket, and works over SSH.

- Techniques: Install and launch herdr; Remap the prefix key; Agent-spawned panes with herdr CLI; Remote session over SSH with local config
- Tools: herdr, tmux, Warp, cmux, Claude Code, Codex CLI, OpenCode, Vim, Bash, Fish, Ratatui, Rust

## [Loop Engineering Totally 10x Hermes agents](../videos/AQRDjI5owZI.md)
`AQRDjI5owZI` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: agent-architecture, claude-code, skills-self-improvement

Explains "loop engineering": replacing hand-written prompts with self-driving agent loops, split into deterministic loops (tests as the goal) and non-deterministic loops (UI judged by a skill plus a second verifier model), run on the Hermes agent and Claude Code.

- Techniques: Five-step loop; Deterministic loop with tests as the goal; Adversarial builder/verifier loop for judgment tasks; Explicit verification gates and termination; External state files
- Tools: Hermes agent (always-on agent, self-evolving skills), Claude Code (non-interactive and interactive modes), Claude Code hooks, Ralph loop, Claude goal command, Goal Buddy 2, OpenClaw, GitHub CLI (gh), GPT models (named as verifier, no version given), Claude Opus 4.5 (mentioned), Fable 5 (mentioned, no detail)

## [The Top Claude Code Features We Use](../videos/ECQA6oOyfIk.md)
`ECQA6oOyfIk` · AI LABS · 2026-07-02 · q2 · intro · review · also: claude-code, pr-code-review, token-cost-efficiency

AI LABS walks through the Claude Code features its team uses most (Agent Teams, Advisor, goal, auto mode, worktree sub-agents, review commands, loop, monitor), with a Scalekit sponsor segment and little measured detail.

- Techniques: Adversarial finder/fixer agent team for code review; Cheap executor with strong advisor escalation; Goal-driven run to a verifiable end state; Auto mode instead of skip-permissions; Worktree-isolated sub-agents for design variants; Layered review commands before merge; Daily knowledge-base sync with loop; Anomaly-only monitor for agent logs
- Tools: Claude Code, Claude Agent SDK, Claude Haiku, Claude Sonnet, Claude Opus 4.8, tmux, Scalekit, ChromaDB, Notion, Gmail, Slack, Mac mini

## [Your Coding Agent Should Do AI System Engineering — Ben Burtenshaw, Hugging Face](../videos/JomVvNDjGb8.md)
`JomVvNDjGb8` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: coding-agents, skills-self-improvement, training-finetuning-rl

Ben Burtenshaw (Hugging Face) argues coding agents can take on AI systems work: writing CUDA kernels, fine-tuning models, and running a multi-agent automated research lab, using open skills, open Hub repos and an open dashboard data layer.

- Techniques: Skill-as-few-shot-examples with bundled benchmark scripts; Skill eval across models (Upskill); Role-split autoresearch loop; Git and bucket as agent shared state; Open-format dashboard as an agent data source; Verifiable-experiment precondition
- Tools: CUDA, Hugging Face kernels library, Upskill, Hugging Face Skills repo, HF Papers CLI, HF Jobs, OpenCode, Codex, Claude Code, Trackio, Parquet, Unsloth

## [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../videos/pmoDeA3RBZY.md)
`pmoDeA3RBZY` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: software-factory, coding-agents, skills-self-improvement

OpenClaw maintainer Vincent Koc on running dozens of parallel coding agents as a "dark factory": swim lanes, opinionated loops, a big plugin refactor, and token efficiency over token maxing.

- Techniques: Swim-lane parallel agents; Big refactor gated by existing tests; Plugin split for blast-radius control; One clone per session instead of worktrees; Explanation quality as a health check; Skill improvement from session logs; Embedding graph for backlog dedupe; Synthetic plus real fake-chat eval harness
- Tools: Codex, Git worktrees, GitHub, Discord, Slack, MS Teams, Docker, GEPA, skills.sh, OpenClaw, NemoClaw, vector embeddings

## [Cooking with Agents in VS Code — Liam Hampton, Microsoft](../videos/dyHpnnlkTc8.md)
`dyHpnnlkTc8` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: coding-agents, context-engineering, sandboxing-execution

A Microsoft product tour of running local, background (worktree) and cloud coding agents side by side in VS Code, with advice on which mode fits which task.

- Techniques: Worktree-per-background-agent; Route tasks by hands-on level; Plan first, autopilot second, pause before PR; Task-specific custom agents; Cloud agent with MCP and browser testing
- Tools: GitHub Copilot, VS Code, GitHub Copilot CLI, Git worktree, GitHub Actions, GitHub MCP server, Playwright MCP server, Microsoft Learn MCP server, awesome-copilot (open-source repo of agent customizations), Claude Opus 4.6 (used for the local agent)

## [Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson](../videos/mR-WAvEPRwE.md)
`mR-WAvEPRwE` · AI Engineer · 2026-06-18 · q4 · practitioner · workshop · also: agent-architecture, claude-code, testing-verification

Two Anthropic Applied AI engineers explain how long-running agent harnesses evolved, and how a planner, generator and evaluator loop with rubric grading builds multi-hour apps that a single agent loop cannot finish.

- Techniques: Generator-evaluator loop with a live-app evaluator; Rubric-as-taste with calibrated examples; Sprint contracts negotiated in files; Thin planner that stays high level; Structured state on disk with JSON feature lists and progress files; Breadcrumb logs for later pickup; Read full traces, then tune prompts from them; Ralph-style stop-hook loop with exit criteria; Hooks for human check-ins; Split model roles for cost; Put the human-readable spec back into long sessions
- Tools: Claude Code, Claude Agent SDK, Playwright MCP, Chrome MCP, Claude Code skills, Claude Code sub-agents, Claude Code agent teams, Claude Code stop hooks, Claude Code auto mode, git, Puppeteer

## [Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum](../videos/WRBNDpUhsJQ.md)
`WRBNDpUhsJQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: token-cost-efficiency, inference-serving

Adrian Bertagnoli (Callosum) argues AI is moving from homogeneous scaling to heterogeneous multi-agent systems mixing models, workflows and chips, and shows a recursive-LM variant that routes sub-contexts to different models and hardware for big cost and speed gains.

- Techniques: Heterogeneous recursion; Subtask offloading to small models; Automated model and hardware routing; Hardware-matched inference for sub-calls
- Tools: Python REPL, Cerebras, Kimi K2.5, GPT-5.2, Gemini 2.5, Qwen3-VL-8B-Instruct, Stamanova

## [The Missing Primitive for Agent Swarms — Lou Bichard, Ona](../videos/5Sui_OnSRlY.md)
`5Sui_OnSRlY` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: software-factory, sandboxing-execution, agent-architecture

Ona's field CTO argues that runtimes, orchestration and triggers are largely solved for coding-agent swarms, and that agent coordination is the missing primitive. He proposes state-machine workflows packaged as a CLI that runs locally and in CI.

- Techniques: Parent-child sub-agents with scoped context; Two-tier sub-agent placement; Fleet fan-out with prompts and scripts as a workflow; Harness engineering loop; Gated micro-step workflow (state machine); CLI-packaged workflow gate
- Tools: Ona dev environments, GitHub, Linear, Symphony, ACP, ACPX, Fabro, n8n-style graph workflows, backgroundagents.com

## [Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo](../videos/EcqMYoIV57A.md)
`EcqMYoIV57A` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: context-engineering, pr-code-review

Qodo's Nupur Sharma argues that dumping more context into an agent makes results worse, and shows how selecting, splitting and judging context across specialist agents fixed this in their PR review system.

- Techniques: Context selection instead of context dumping; Iterative retrieval with a library-card index; Hierarchical summarization; Knowledge graph for dependencies; 80/20 research and gate split; Specialist agents with a judge agent; Feedback-weighted calibration
- Tools: Jira, MCP, Claude Opus

## [Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl](../videos/W-SX_srBa3Y.md)
`W-SX_srBa3Y` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: coding-agents, agent-architecture

Bitly engineer Michael Richman presents Command & Control, his tool for monitoring and answering coding agents from a phone, web or watch, and frames the idle-agent problem as FOMAT.

- Techniques: Per-platform lifecycle daemon feeding a control plane; Tiered notification and watch lists; Overview summaries from the last few messages; Start remotely, resume locally on the same session
- Tools: Command & Control (Cmd+Ctrl, speaker's own tool), Claude Code (captioned as Cloud Code), Codex / Codex CLI, Gemini (CLI), Cursor (IDE), GitHub Copilot, OpenCode, Anthropic remote control and teleportation (Claude Code features, mentioned), Bitly MCP server (co-written by speaker, mentioned), Agent Craft (gaming-based agent tool, mentioned as seen earlier that morning)

## [Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw](../videos/VaS2h-dY1-4.md)
`VaS2h-dY1-4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: mcp-and-tools, sandboxing-execution, pr-code-review

An OpenClaw maintainer shows acpx, a CLI and workflow engine over the Agent Client Protocol (ACP), used to automate PR triage and to run disposable per-task agents on Kubernetes.

- Techniques: ACP as the client-side adapter layer; Channel-bound agent sessions; Hybrid PR-triage workflow with JSON handoffs; Shallow-fix loop with a human escalation gate; Feedback bin for PR outcomes; Per-task disposable agent pods via a Kubernetes operator
- Tools: acpx, ACP (Agent Client Protocol), Codex, Claude Code, Zed, Discord, Slack, MS Teams, Kubernetes, Helm, Go operator, rsync

## [It’s Broken… The Codex vs Claude Code Debate Is Finally Over](../videos/8ImlAQOyVTs.md)
`8ImlAQOyVTs` · AI LABS · 2026-06-02 · q3 · practitioner · review · also: coding-agents, claude-code, context-engineering

A single-author head-to-head of Claude Code (Opus 4.7) vs Codex CLI (GPT 5.5) across usability, planning, greenfield builds, context, memory and sub-agents; Codex wins on cost and autonomy, Claude on UX, hooks and ecosystem.

- Techniques: Count tokens per session from the CLI's session files; Set a Codex personality to reduce sycophancy; Use Claude Code's expanded thinking to course-correct; Use Codex's attempt flag for best-of-n; Keep AGENTS.md or CLAUDE.md lean; Design sub-agents for isolation or inheritance deliberately
- Tools: Claude Code, Codex CLI, Opus 4.7, GPT 5.5, FastAPI, Flask, Next.js, ShadCN UI, Gemini API, Claude desktop app, Codex web app, Stream Vision Agents

## [Why OpenAI Built Symphony and Gave It Away for Free](../videos/n8qDKMPpLXc.md)
`n8qDKMPpLXc` · Better Stack · 2026-06-02 · q3 · intro · review · also: agent-architecture, coding-agents, software-factory

Better Stack walkthrough of OpenAI's open-source Symphony, which polls Linear for issues and runs a coding agent per issue, with humans involved only at review. Covers setup, workflow file and hooks.

- Techniques: Tracker-driven agent dispatch; Workflow file with YAML front matter plus a per-issue prompt; Clone-and-branch after-create hook, commit-push-PR after-run hook; Spec-driven self-implementation
- Tools: Symphony (OpenAI, open-source orchestrator), Linear (issue tracker), Codex CLI (OpenAI coding agent), GPT-5.5 (model, used at low effort for spec-generated build), Elixir (language for the manual install route), TypeScript and Bun (demo app), Python (spec-generated Symphony version), Go with Charm CLI (community Symphony version), Claude SDK (community Symphony version), uv (Python tool; speaker says OpenAI acquired it, not verified in video), Multica (agent orchestration product, compared), Conductor (agent orchestration product, compared)

## [I Tried Running a Company Made of AI Agents](../videos/xZ7OmRz2i7o.md)
`xZ7OmRz2i7o` · Better Stack · 2026-06-02 · q3 · intro · review · also: agent-architecture, token-cost-efficiency

Walkthrough of Paperclip, a self-hosted control plane that runs several AI agents as a company with an org chart, tickets, heartbeats, budgets and audit logs; useful for multi-agent coordination, overkill for single-agent tasks.

- Techniques: Goal-first company setup; Budget-before-execution guardrail; Heartbeat wake cycles; Ticket ancestry for traceability; Skill files as company rules; Local install and launch
- Tools: Paperclip, npx (Node package runner), Postgres (bundled with Paperclip), CrewAI, AutoGen, LangGraph (rendered as 'Landgraf' in captions), Claude Code, Cursor, GitHub (issues), Jira, Linear

## [What Happens When AI Coding Gets a Delivery Pipeline (Routa)](../videos/_16PhraFYjQ.md)
`_16PhraFYjQ` · Better Stack · 2026-06-02 · q3 · intro · review · also: software-factory, coding-agents, pr-code-review

Walkthrough of Routa, a free, local-first, open-source Kanban desktop app that runs AI coding agents through backlog, dev, and review lanes with evidence and gates instead of one chat thread.

- Techniques: Lane-per-stage agent pipeline; Evidence-backed review gates; Per-task traceability; Self-hosted setup
- Tools: Routa (open-source AI coding delivery tool; spelled Ruta in captions, Routa in the title; desktop app and Docker Compose), OpenCode (agent runtime used for the agents), Anthropic API / Claude (model provider via synced API key), MCP (Model Context Protocol, supported for agent connections), ACP (Agent Client Protocol, supported for agent connections), Docker Compose (self-hosting path), Cursor (chat-first comparison), Claude Code (chat-first comparison), CrewAI (agent framework comparison), LangGraph (agent framework comparison; spelled LaneGraph in captions)

## [The Greatest AI Coding System I've Ever Used, Forget Codex Vs Claude Code](../videos/q7Am0pV6FjQ.md)
`q7Am0pV6FjQ` · AI LABS · 2026-06-02 · q3 · practitioner · review · also: claude-code, agent-architecture, context-engineering

Goal Buddy, an open-source plugin for Claude Code and Codex, wraps the native goal command with file-based state, an upfront "oracle" for done, and Scout/Worker/Judge agent roles.

- Techniques: Oracle-first done criteria; Role-separated agents with access limits; File-based run state instead of chat history; Slice contracts; Clarify before looping; Install and start a run
- Tools: Goal Buddy, Claude Code (goal command, resume command), Codex, Ralph Wiggum plugin, Haiku (native goal evaluator)

## [This Open Source Tool Gives You God Mode for AI Agents (AoE)](../videos/fPz9OB3Bau8.md)
`fPz9OB3Bau8` · Better Stack · 2026-06-02 · q2 · intro · review · also: coding-agents, sandboxing-execution

Better Stack demo of Agent of Empires (AoE), an open-source terminal dashboard that runs many CLI coding agents side by side using git worktrees, status indicators and optional Docker sandboxes. Short and promo-leaning, with little configuration detail.

- Techniques: Run many CLI agents from one dashboard; Per-agent git worktree isolation; Triage agents by status instead of attaching; Optional Docker sandbox per agent
- Tools: Agent of Empires (AoE), Claude, Codex, tmux, Git worktrees, Docker, Agent Deck, Homebrew

## [Anthropic Just Revealed The Best Claude Code Setup](../videos/lGalJmyI78w.md)
`lGalJmyI78w` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · also: claude-code, context-engineering, mcp-and-tools

Practitioner checklist for setting up Claude Code harnesses on large codebases: layered CLAUDE.md, hooks, path-scoped skills, plugins, LSP, MCP, sub-agents, and periodic pruning.

- Techniques: Layered CLAUDE.md; Stop-hook learning loop; Hooks for enforcement; Path-scoped skills; Team plugin distribution; LSP before code; Custom sub-agents with an overridden Explore agent; Per-subdirectory tests and codebase map; Quarterly harness pruning with ignore files
- Tools: Claude Code, Codex, Gemini CLI, superpowers, CLAUDE.md, Claude Code hooks (SessionStart, PreToolUse, Stop, exit-code-2), skill-creator, Claude Code plugins and plugin marketplace, LSP (Language Server Protocol), MCP (Model Context Protocol), Explore sub-agent (built-in, overridable), .gitignore

## [The End of Apps — Kitze, Sizzy.co](../videos/4fntwuOoedA.md)
`4fntwuOoedA` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: agent-architecture, product-ux, memory

Kitze (Sizzy.co) on his personal-agent journey, from to-do apps to OpenClaw-style agents, and his view that apps will give way to a personal agent OS that prompts the user.

- Techniques: Nested topic description injection; Per-topic specialized agents; Labeled cron messages with full conversation context; Visible tool-call UI
- Tools: OpenClaw, Hermes, Paperclip, Codex, Claude Code, Claude Cowork, Tmux, Telegram, Discord, Tasker, IFTTT, Notion

## [How we solved Context Management in Agents — Sally-Ann Delucia](../videos/esY99nYXxR4.md)
`esY99nYXxR4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: context-engineering, memory, evals

Arize's product head explains how their Alex agent escaped a context-growth loop: head/tail truncation with the middle moved to memory, long-session evals, and sub-agents for heavy data search.

- Techniques: Head + tail truncation with middle spill to memory; Reference-by-ID retrieval tool; Long-session eval (seed N turns, test turn N+1); Sub-agent for data-heavy search
- Tools: Alex (Arize's in-product agent), Arize observability platform, Claude Code (referenced, not used by speaker)

## [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](../videos/ow1we5PzK-o.md)
`ow1we5PzK-o` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: agent-architecture, software-factory, testing-verification

Luke Alvoeiro (Factory) on "Missions", a multi-agent system that runs for hours or days by combining delegation, creator/verifier, broadcast and negotiation, with a validation contract written before any code.

- Techniques: Validation contract written at planning time; Fresh-context adversarial validators; Structured worker handoffs; Serial features with read-only parallelism; Per-role model choice; Milestone-based negotiation; Orchestration as prompts and skills
- Tools: Factory Droid (open source Goose lineage mentioned), AGENTS.md, skills, computer use (for user-testing validator), prompt caching

## [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](../videos/WE_Gnowy3uw.md)
`WE_Gnowy3uw` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: skills-self-improvement, coding-agents, evals

Cursor's David Gomes on replacing its git-worktree and best-of-N feature (about 15K lines deleted) with one markdown skill plus subagents, and what was lost in the swap.

- Techniques: Skill as the orchestrator for a stateful workflow; Best-of-N through one subagent per model; Commands instead of skills for server-controlled prompts; Prompt-level containment with system reminders; Two-scorer isolation eval run headlessly; Feeding failure cases into RL training
- Tools: Cursor (2.0 and 3.0), Cursor CLI (headless), Git worktrees, Agent skills, Subagents, Slash commands, Composer (Cursor's own model, version 2 mentioned), Braintrust, Kimi, Grok, GPT, Opus

## [Agents on the Canvas in tldraw — Steve Ruiz, tldraw](../videos/sPUjIBH5Cwg.md)
`sPUjIBH5Cwg` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: product-ux, sandboxing-execution, security-guardrails

Steve Ruiz (tldraw) shows how agents moved from one-shot drawing on a whiteboard to multiple agents working as a team on a shared canvas, and the safety trade-offs of letting them script a desktop app.

- Techniques: Structured-output shape drawing; Produce-review-iterate loop; Leader/follower multi-agent on shared state; Expose a runtime API for agent-written code; Prompt for spatial and coordinate conventions
- Tools: tldraw, Electron, Claude, Cursor, Make Real

## [CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner](../videos/VktrqzQgytY.md)
`VktrqzQgytY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: software-factory, pr-code-review, sandboxing-execution

Talk arguing CI/CD was built for human-paced PRs and breaks under agent volume; proposes spec-driven agent loops with in-loop validation, a pre-merge queue, and stateful compute.

- Techniques: Spec-first agent loop with a known-commit start; External review agents inside the loop; Pre-merge queue for serializable commits; Approve intent and evidence, not diffs; Stateful, incremental execution environments
- Tools: GitHub Actions, Claude Code, Amp, Cursor, Factory, GitHub Copilot, Namespace

## [Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate](../videos/vi-2nasppAg.md)
`vi-2nasppAg` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: agent-architecture, observability, sandboxing-execution

Iterate's workshop on building event-sourced agent harnesses as stream processors: pure reducers for state, side effects after append, pause-based circuit breakers. Live demos mostly failed; the design ideas are the value.

- Techniques: Event-sourced agent log; Reducer plus after-append split; Pause-event circuit breaker; Deferred enrichment with a time budget; Child paths for sub-agents; Secret substitution at fetch time
- Tools: events.iterate.com (event service), Cloudflare dynamic workers, OpenAI SDK (Responses API), Zod, Pi, Claude, OpenCode, Convex, Kafka, Cursor, OpenClaw, Electric SQL

## [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](../videos/MhHEGMFCEB0.md)
`MhHEGMFCEB0` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: coding-agents, security-guardrails, pr-code-review

OpenAI's Codex workshop on plugins, background automations, code review, custom sub-agents with sandbox modes, guardian approvals, and stop hooks for long runs.

- Techniques: Custom sub-agent personas as TOML files; Fan-out review by file slices with an orchestrator; Read-only explorer on a fast cheap model; Parallel brainstorm of implementation options; Guardian verifier sub-agent for privileged actions; Stop hook that keeps a run going; Best-of-N cloud runs; Playwright interactive skill for visual debugging
- Tools: Codex, Codex app, Codex CLI, Codex IDE extension, Codex Code Review, Codex Security, Claude Code plugin for Codex, Playwright, ImageGen, Slack, Gmail, Google Drive

## [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub](../videos/ClWD8OEYgp8.md)
`ClWD8OEYgp8` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: coding-agents, product-ux, context-engineering

Maggie Appleton (GitHub Next) argues agents have shifted the bottleneck from building to agreeing on what to build, and previews ACE, a shared multiplayer environment for team-plus-agent work.

- Techniques: Shared always-on agent session per task; Whole-conversation context as prompt input; Plan first, co-edit, then execute; Session summary for switching between parallel sessions; Backward-compatible PRs that link back to the session
- Tools: GitHub ACE (Agent Collaboration Environment, research prototype), Claude Opus 4.6 (model used in the demo), Bun (bun install / bun dev in the demo project), VS Code (real-time multiplayer editing in the shared cloud machine), Slack, Jira, Linear (named as coordination tools that are not built for agentic work)

## [AgentCraft: Putting the Orc in Orchestration — Ido Salomon](../videos/kR64LOqBBCU.md)
`kR64LOqBBCU` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: coding-agents, product-ux, pr-code-review

Ido Salomon demos AgentCraft, an RTS-style orchestrator for many coding agents, arguing the human is the bottleneck and offering visibility, campaigns, review bundles and shared workspaces as fixes.

- Techniques: Filesystem-projected agent map with collision heat map; Hotkey cycling to agents that need attention; Campaign mode: broad goal in a container, plan first; Review bundles with rationale and visual evidence; Best-of-N parallel attempts with human selection; Soft coordination via shared human and agent chat
- Tools: AgentCraft, MCPUI, MCP Apps, Cursor, Claude Code, Codex, OpenClaw, Git, Chrome

## [Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably](../videos/YNJvm7t3yq8.md)
`YNJvm7t3yq8` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, product-ux

Ably's Mike Christensen argues that AI chat UX breaks under direct HTTP/SSE streaming and proposes durable sessions (a shared, resumable channel between agents and clients) to get resilient streams, multi-device sync, and live steering or cancel.

- Techniques: Durable session as a shared channel; Hand-rolled resumable stream (the baseline he contrasts with); Bidirectional transport to separate cancel from disconnect; Multi-agent writes straight to the shared session; Any-client control through the session; Human handoff as another session participant
- Tools: Ably channels, Ably AI Transport, Server-Sent Events (SSE), WebSockets, Redis, Vercel AI SDK, TanStack AI

## [Full Walkthrough: Workflow for AI Coding — Matt Pocock](../videos/-QFHIoCo-Ko.md)
`-QFHIoCo-Ko` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, software-factory, testing-verification

Matt Pocock's live workshop on an AI coding workflow: grill-me alignment, PRD, vertical-slice issues with blocking edges, AFK Ralph loops with TDD and feedback loops, and deep-module codebases.

- Techniques: Smart-zone sizing and clear-over-compact; Grill-me alignment skill; Destination doc plus journey issues; Ralph loop (sequential AFK runner); Red-green-refactor TDD for agents; Self-review in a fresh context; Interface-first deep modules with grey-box delegation; Push vs pull for coding standards; Sandcastle-style parallel runs; Delete plans and PRDs after they ship
- Tools: Claude Code, Sandcastle, Docker, TypeScript, GitHub Issues, TLDraw, Slido, Playwright MCP, Sonnet, Opus, Spec Kit, OpenSpec

## [Fighting AI with AI — Lawrence Jones, Incident](../videos/L2r6vLlLgs8.md)
`L2r6vLlLgs8` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: evals, observability, coding-agents

Lawrence Jones (Incident.io) on using AI tools to debug and improve multi-prompt AI systems: export UI traces and eval suites as file systems for coding agents, then run parallel backtest analysis pipelines.

- Techniques: Eval-tool CLI for agents; Runbook-driven prompt fix; Download trace or interaction as a file tree; Parallel per-item analysis with file-based resume; Cohort clustering over failures; Analysis as a repeatable markdown playbook; Investigate, fix, then verify in one session
- Tools: Claude Code, Codex, Go, YAML

## [This Is The Anthropic Team's Greatest Advice](../videos/O1XLCh-uA_E.md)
`O1XLCh-uA_E` · AI LABS · 2026-05-02 · q2 · practitioner · tutorial · also: claude-code, context-engineering, agent-architecture

Practical habits for managing Claude Code's context window (compaction, clear, rewind, sub-agents, recaps) to limit context rot and goal drift in long runs; mostly attributed advice with a sponsored segment.

- Techniques: Manual compaction with an explicit instruction; Clear on task switch; Structured state handoff (save, clear, reload); Periodic recap to reinforce goals; Sub-agent isolation for raw-heavy subtasks; Rewind, then re-prompt
- Tools: Claude Code, Claude (Opus 4.5 and later models, 1M context window), CLAUDE.md, Verdant (sponsor)

## [Multica: The Open Source Tool That Makes Claude Code 10x Better](../videos/WdGSXQPwwmo.md)
`WdGSXQPwwmo` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: coding-agents, agent-architecture

Better Stack walks through self-hosting Multica on a VPS to turn Claude Code and OpenCode into assignable, scheduled agents, then judges it technical to set up and less suited to dialogue-style work than managed alternatives.

- Techniques: Self-host Multica with Docker on a VPS; Log in without the emailed code; Connect a machine as an agent runtime; Define an agent; Issue-driven task flow; Scheduled autopilot (recurring agent run)
- Tools: Multica, Claude Code, OpenCode, OpenCode Zen (big pickle model, as named in the video), Codex CLI, Hermes, Claude Routines, Claude Managed Agents, Docker, Go, Next.js, TypeScript

## [Kimi K2.6 vs Claude Code: Why I’m Switching to the $39 Plan (Full Model Breakdown)](../videos/icbeuJxnrKU.md)
`icbeuJxnrKU` · Better Stack · 2026-05-02 · q2 · practitioner · review · also: models-research, coding-agents, token-cost-efficiency

Better Stack runs Kimi K2.6 through an agent-swarm research task, a landing-page build and a scraping web app, and finds it a modest step up from K2.5 with no token-cost data.

- Techniques: Per-entity agent swarm fan-out; Follow-up for per-item differentiation; Fix a missing feature with a targeted follow-up; Scraper stack used by the model
- Tools: Kimi K2.6, Kimi K2.5, Kimi chatbot interface (agent swarm feature), Kimi CLI (newest version, includes token counter), MoonViT (native vision encoder, open source), Hugging Face (model weights), GSAP, Node.js, Express, Axios, Cheerio, Claude Code

## [Anthropic Just Fixed The Token Problem](../videos/sncxStbRSwI.md)
`sncxStbRSwI` · AI LABS · 2026-05-02 · q2 · practitioner · review · also: coding-agents, token-cost-efficiency, claude-code

AI LABS walks through Anthropic's advisor strategy in Claude Code: a Sonnet executor does all the work and calls Opus only when stuck. Three anecdotal tests show it helps simple-to-medium apps but needs nudging.

- Techniques: Executor/advisor model split in Claude Code; Escalate after repeated failure; Consult before a high-blast-radius change; Name the advisor explicitly for non-trivial tasks; Choose the main model by app scope
- Tools: Claude Code, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Playwright MCP, SWE-bench, Junie (JetBrains, sponsor segment)

## [The Claude Code Skill Boris Cherny Runs on Every Project](../videos/AhXfI1rSUPc.md)
`AhXfI1rSUPc` · AI LABS · 2026-05-02 · q2 · practitioner · review · also: claude-code, skills-self-improvement, testing-verification

A walkthrough of skills, plugins and slash commands the Claude Code team reportedly uses, including batch worktree fan-out, a verify skill and an end-of-session tech debt skill. Several are internal and unverified, and a sponsor segment is included.

- Techniques: Batch fan-out with worktrees; Project-specific verify skill; Skillify-style session capture; End-of-session tech-debt pass; Inner-loop slash commands; Issue dedupe with a confidence threshold; Security scan, then fix
- Tools: Claude Code, Claude Code batch command, git worktrees, frontend-design plugin, Code Simplifier plugin, Simplify (built-in), Claude Code security scan (built-in), commit command plugin, Remotion skill, skill creator skill, Skillify (internal), verify skill (internal)

## [Your AI Output Sucks Because You’re Not Doing This](../videos/cop_G65D7PA.md)
`cop_G65D7PA` · AI LABS · 2026-04-02 · q2 · intro · tutorial · also: context-engineering, claude-code, token-cost-efficiency

AI LABS' pre-setup tips for Cowork: a per-folder manifest.md with tiered sources, voice and working-style files, global instructions that demand plans and questions, end-state prompts, batching and guardrails.

- Techniques: Per-folder manifest.md with tiered sources; Identity, voice and working-style context files; Global instructions as a default operating contract; State the end state and the edge-case rule; Batch by shared context, keep unrelated work apart; Scheduled report from meeting notes via the schedule skill; Build a plugin with the plugin-creation skill; Guardrails for agent file access
- Tools: Cowork, Claude Code (clawed code in transcript), Claude desktop app, CLAUDE.md (global and per-folder instructions), manifest.md (the presenter's convention), schedule skill, plugin-creation skill, OpenClaud (auto-caption; used for research, tool-release tracking and a Discord report; spelling uncertain), Discord, Gmail connector, Google Drive connector, cron jobs

## [Why GUIs Will Replace TUIs for AI Developer Tools | Better Stack Podcast Ep. 14](../videos/zr-Xk0UVHEU.md)
`zr-Xk0UVHEU` · Better Stack · 2026-04-02 · q3 · practitioner · interview · also: coding-agents, pr-code-review, dev-tools

Better Stack podcast with Warp DevRel Ben Holmes on why GUI-style wrappers around coding agents will beat TUIs, plus practical patterns for agent code review, cloud agents, and multi-agent delegation.

- Techniques: Fresh-session review pass; Ask why, do not accuse; Two-lens review passes; Agent review as a GitHub Action; Keep READMEs and CLAUDE.md thin; Two clones instead of worktrees for parallel agents; Cloud research, then fork locally; Multi-repo sandbox environment; Route by task complexity; Tune the harness per model; Figma for design, agent for implementation
- Tools: Warp, Oz (Warp cloud agent platform), Claude Code, Codex (CLI and app), OpenCode, Pi, OpenClaw, Cursor, GitHub Copilot, Ghostty, tmux, cmux

## [T3 Code: Better Than Codex?](../videos/6x7hh6Qzm9U.md)
`6x7hh6Qzm9U` · Better Stack · 2026-04-02 · q3 · intro · review · also: coding-agents, dev-tools

Walkthrough of T3 Code, an open-source desktop GUI for running multiple coding agents (currently Codex) on your existing subscription, with per-thread git worktrees, plan mode, one-click commit/PR, and a list of missing features.

- Techniques: One git worktree per agent thread; Plan first, then implement; Supervised vs full-access tool calls; One-click commit, push and PR; Quick-action buttons for setup commands; Fork the agent GUI and let the agent extend it
- Tools: T3 Code, Codex, Codex app, Claude Code, Cursor, OpenCode, Gemini, git worktrees, Finder

## [12 Hidden Settings To Enable In Your Claude Code Setup](../videos/pDoBe4qbFPE.md)
`pDoBe4qbFPE` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: claude-code, context-engineering

Tour of under-documented Claude Code settings: session retention, output and read caps, sub-agent flags, auto-compact at 75%, commit attribution, telemetry, and exit-code-2 hooks. Includes a sponsored segment.

- Techniques: Extend session retention; Path-scoped rules; Raise the bash output cap; Run a session as a sub-agent; Raise the file read cap and enforce full reads; Lower the auto-compact threshold; Remove commit co-author lines; Opt out of telemetry without losing updates; Prompt stash with Ctrl+S; Exit-code-2 hook to block and steer; Loop-until-done with exit-code hooks (Ralph-style); Claude CTX profiles
- Tools: Claude Code, Claude CTX (open-source profile switcher), Opus 4.6 (cited as the 1M-token-context model), uv (transcribed as 'uvicorn'; likely the pip replacement in the hook example), Statsig (analytics sink, named by speaker), Sentry (error reporting sink, named by speaker), Make.com (sponsor), Ralph loops (named concept, not a tool)

## [OpenClaw Agents Just Got Better With This](../videos/JC53AcoFh-Q.md)
`JC53AcoFh-Q` · AI LABS · 2026-04-02 · q2 · intro · review · also: security-guardrails, memory, skills-self-improvement

A tool roundup for hardening and extending OpenClaw agents: a security skill suite, a deterministic multi-agent workflow runner, a hybrid memory plugin, a network-API browser skill, Cloudflare hosting, a dashboard, and a curated skill list.

- Techniques: Installing a skill from git when the registry is rate-limited; Self-verifying skills: checksum check with re-download on mismatch; Scheduled security heartbeat over installed skills; Deterministic multi-agent workflow with verifier and fresh contexts; Re-ranked hybrid memory as an agent memory plugin; Replaying site APIs with cookies instead of driving a browser visually; Filtering a large skill registry before installing
- Tools: OpenClaw, ClawSec, Prompt Security, Heartbeat skill, Soul Guardian, OpenClaw Watchdog, Antfarm, Ralph Loop (creator's earlier project, per speaker), AI Dev Task (creator's earlier project, per speaker), ClawHub (skill registry), Awesome OpenClaw Skills (curated list), MemoryLanceDB Pro

## [How to use Claude Code and Gemini Cli Together](../videos/XdtBAm2pM-0.md)
`XdtBAm2pM-0` · AI LABS · 2026-04-02 · q3 · practitioner · tutorial · also: coding-agents, claude-code, context-engineering

Walkthrough of Agent Chatter, a shared chat layer where Claude Code, Gemini CLI and Codex agents run in tmux and coordinate through channels, with planning, peer review and loop-guard setup.

- Techniques: Shared multi-model chat via per-agent tmux sessions; Per-agent settings.json permissions instead of skip-permissions; Shared agents.md as the single instruction source; Named personas per agent; Loop guard and continue gate; Planner-first with PRD and spec templates; Three-phase presenter/challenger/synthesizer review; Planner as orchestrator with an ask-don't-assume rule; Git worktrees per agent (suggested, not tested); Initialize the app framework before starting agents
- Tools: Agent Chatter, Claude Code, Opus 4.6, Gemini CLI, Codex, Kimi, Qwen, GLM, tmux, Next.js, MCP, agents.md

## [Claude Code + CMUX: The Ultimate AI Coding Terminal](../videos/8oLP8oxqtOE.md)
`8oLP8oxqtOE` · Better Stack · 2026-04-02 · q3 · intro · review · also: claude-code, coding-agents, dev-tools

Walkthrough of cmux, a native macOS terminal whose CLI and Unix socket let Claude Code or OpenCode drive browser panes, spawn sub-agent panes, and send attention notifications.

- Techniques: Agent-driven browser pane for live testing; Sub-agents in split panes that report back and close; Attention notifications with pane flash; Sidebar status from the agent; Setup with cmux skills and hooks; Cheap demo runs by switching the model
- Tools: cmux, Claude Code, OpenCode, libghostty, Ghostty, WebKit, Bonsplit, tmux, Warp, soloterm, Demux, Haiku

## [GSD Is the Missing Piece For Claude Code](../videos/uEit1oOJK0w.md)
`uEit1oOJK0w` · AI LABS · 2026-04-02 · q2 · practitioner · review · also: coding-agents, context-engineering, testing-verification

AI LABS walks through GSD (Get Shit Done), a planning-and-execution framework for Claude Code, and compares it with BMAD and Superpowers. Main takeaway: choose the framework by how fixed your requirements are.

- Techniques: Choose the framework by requirement certainty; Per-project install with project scope; Initialise GSD on existing vs blank codebases; Keep the planning anchor short; Per-phase discuss, then concise context file; Ground phase research in docs with Context7; Adversarial plan verification and waves; Phase verification gates
- Tools: GSD (Get Shit Done), BMAD method, Superpowers, Claude Code, Claude Opus 4.6, Claude Sonnet, Next.js, Playwright, Context7 MCP, GenSpark (sponsor segment), Speakly (sponsor segment)

## [Pencil, AI Agents & The Future of Design | Better Stack Podcast Ep. 13](../videos/FqD_hlQSQIk.md)
`FqD_hlQSQIk` · Better Stack · 2026-04-02 · q3 · intro · interview · also: product-ux, coding-agents, models-research

Pencil's CEO on "vibe designing": a canvas stored as structured JSON in git that humans and agents edit together, with elicitation, parallel agents and speed as the real bottlenecks.

- Techniques: Keep the design as a structured file in the repo; Drop references into the agent chat as a rules-plus-libraries-plus-images bundle; Extract a palette from a vibe image; Partition a page across parallel agents by region; Run the same task across several models side by side; Elicit requirements before building; Correct the agent in a second round instead of restarting; Edit other regions while the agent works
- Tools: Pencil (pencil.dev), Cursor, Windsurf, Antigravity, VS Code, Codex, Claude Code, Opus 4.6, Opus 4.5, Sonnet 3.5, Sonnet 3.7, Gemini

## [Opus 4.6 + Agent Teams Makes Claude Code Insane](../videos/LZyWuPqvvjU.md)
`LZyWuPqvvjU` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: coding-agents, claude-code, token-cost-efficiency

Walkthrough of Claude Code's experimental Agent Teams: independent teammates with a shared task list that can message each other, viewed in tmux or in-process. Two teammates used 29% of usage, so the presenter would restrict it.

- Techniques: Enable agent teams; Give the team lead a plan and let it spawn teammates; Watch teammates in tmux; Switch teammates in a single window; Inspect team state on disk; Reserve teams for cross-checking and research
- Tools: Claude Code, Claude Opus 4.6, Claude Haiku, tmux, iTerm2, OpenCode

## [I Let 30 AI Agents Loose in My Repo (Gas Town)](../videos/_mrMidIwCzk.md)
`_mrMidIwCzk` · Better Stack · 2026-03-02 · q2 · intro · review · also: coding-agents, software-factory

A Better Stack walkthrough of Gastown, an open-source orchestrator that runs many Claude Code agents in parallel on one feature, shown on a Go to-do app with a single prompt and a candid look at the costs.

- Techniques: Mayor-decomposed parallel feature build; Git-backed orchestration state for crash recovery; Verify parallel agent output by diff and running the app
- Tools: Gastown, Claude Code, Go, SQLite, Docker, Homebrew, JWT, GitHub

## [10 Crazy Claude Code Tips That Give You An Unfair Advantage](../videos/TmsH-RIHvas.md)
`TmsH-RIHvas` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: claude-code, context-engineering, testing-verification

AI LABS walks through ten Claude Code practices: session-insight reviews, Claude-written planning docs, exit-code-2 hooks, worktree-based parallel agents, adversarial fact-checking, and browser-based self-verification.

- Techniques: Session insights review into CLAUDE.md; Claude-authored planning docs as context; Context7 MCP for current library docs; Exit-code-2 PreToolUse guard for protected paths; MCP CLI mode to keep tool schemas out of context; One git worktree per parallel agent; Strict TypeScript and user stories before implementation; Adversarial researcher and fact-checker agents; Agent Browser for self-verification, with CLAUDE.md fallback order; Failure-prediction review pass
- Tools: Claude Code, CLAUDE.md, Claude Code hooks (PreToolUse), MCPCLI (experimental MCP CLI mode), Context7 MCP, git worktrees, TypeScript, Claude in Chrome extension, Puppeteer MCP, Agent Browser (Vercel), Kimi K2.5 (named as comparison in a research example), Opus 4.6 (named as subject of a research example)

## [The Correct Way to Use Claude Code Teams](../videos/MSyWjPDrHJw.md)
`MSyWjPDrHJw` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: claude-code, coding-agents, token-cost-efficiency

AI LABS walks through Claude Code agent teams, an experimental upgrade over sub-agents where teammates message each other directly, and shows three uses plus practical rules for keeping them on track.

- Techniques: Enable agent teams behind the experimental flag; Reviewer and fixer pair for parallel code review; Multi-perspective bug hunt; Staged build with a blocking foundation agent; Per-assignment task documents to bound scope; Lead supervision rules
- Tools: Claude Code, Claude Code agent teams (experimental), Claude Code sub-agents, Claude Opus 4.6

## [What REALLY Happened When 16 Claude Agents Tried To Build a C Compiler From Scratch](../videos/SVREdZHPG1I.md)
`SVREdZHPG1I` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: testing-verification, coding-agents, agent-architecture

Better Stack breaks down Anthropic's experiment with 16 parallel Claude Opus 4.6 agents building a C compiler: git-based task locks, shared test harnesses, GCC as an oracle, and why the presenter says it was not fully autonomous.

- Techniques: Git-commit task lock for parallel agents; Isolated clones with push-to-upstream; Ralph loop with a fresh session per task; Quiet test harness with a log file; Deterministic sharded test subsets; Reference-compiler oracle for partial builds; README and progress files as cross-session memory; Role-specialized review agents
- Tools: Claude Opus 4.6, Claude (Anthropic agent), Docker, Git, GCC, Ralph loop, Linux kernel, SQLite test suite, LibJPEG test suite, Redis test suite, Rust

## [This Is The Only Claude Code Plugin You'll EVER Need (Superpowers)](../videos/lq3rzXP4_vs.md)
`lq3rzXP4_vs` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: claude-code, skills-self-improvement, testing-verification

Walkthrough of Superpowers, a Claude Code skills plugin that forces brainstorm, planning, sub-agent TDD and per-step commits. It beat plain plan mode in one demo, but the agent skipped TDD once.

- Techniques: Brainstorm into a design doc before code; Split the design into sub-agent-sized tasks; Pick the execution mode deliberately; Per-task red-green loop with a git commit per step; Plan doc, clear context, then execute (presenter's own workflow, not part of Superpowers)
- Tools: Superpowers (agentic skills framework / Claude Code plugin; 14 skills per the presenter), Claude Code, Opus 4.6 (Anthropic model, used for both builds), React, Vite, Hono (server framework), CSS-in-JS styling library (unnamed in the video), Tailwind CSS (suggested by the presenter in hindsight, not used), XDL (CLI that downloads videos from Twitter; the demo app wraps it), git, Beads (planning tool, comparison only), spec-kit (spec-driven development, comparison only)

## [This Just Fixed 90% of AI Coding Errors](../videos/romGzY0Xu0s.md)
`romGzY0Xu0s` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: coding-agents, testing-verification, skills-self-improvement

AI LABS team tests the Superpowers Claude Code plugin on a Trello-style app: enforced brainstorm, plan, subagent, TDD and review gates work, but they burn context fast and are best used selectively.

- Techniques: Install a workflow plugin from a marketplace in Claude Code; Brainstorm-gated kickoff prompt; Subagent-driven implementation with worktrees and review gates; Anti-test-edit TDD cue; Four-phase systematic debugging prompt; Compact before the next feature; Selective process use; Re-invoke skills after context loss
- Tools: Claude Code, Superpowers (Claude Code plugin), git, git worktrees, BMAD, OpenSpec, Trello (the example app being cloned)

## [I Didn't Expect This From OpenAI's IDE](../videos/sC4JpJlD3aQ.md)
`sC4JpJlD3aQ` · AI LABS · 2026-03-02 · q3 · intro · tutorial · also: coding-agents, vibe-coding-app-building, skills-self-improvement

A 7-minute build log: turning a car photo into a 3D hero section for a Next.js landing page with Tripo 3D, OpenAI's Codex app, GSAP and Aceternity UI, with parallel Codex subagents in git worktrees.

- Techniques: Pre-clean the image for image-to-3D; GLB asset in a Next.js public folder; Generate a project skill with the agent's skill creator; Work around agent install timeouts; Parallel subagents in separate git worktrees; Scope the agent with explicit do-not-touch constraints; Fix visual drift with screenshots and named variants
- Tools: Codex app (OpenAI), Tripo 3D, Canva background remover, Next.js, GSAP, Aceternity UI, React Three Fiber, post-processing package for React Three Fiber (named 'Post Processing' in the transcript), npm, GLB (file format), Antigravity (agent manager, compared in passing), Claude Code (mentioned as the previous agent used)

## [Native Worktrees Just Killed Traditional Claude Code Workflows](../videos/lj_xZn-Yf18.md)
`lj_xZn-Yf18` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: claude-code, coding-agents, dev-tools

A 4-minute walkthrough of Claude Code's native git worktree support: run parallel feature branches in isolated worktrees, resume them by name, and use worktree-isolated subagents, with a note on a recent breakage.

- Techniques: Parallel feature branches with named worktrees; Isolate a broken feature and ship the rest; Return to or resume a worktree; Open a shell in a worktree directory with tmux; Worktree isolation for custom subagents; Clean up temporary worktrees
- Tools: Claude Code, Claude Desktop, git, React, tmux, Claude Squad, React Doctor, SVN, Jujutsu

## [Why is Everyone OBSESSED With The New Kimi K2.5 AI Model](../videos/KvOYDevFGiw.md)
`KvOYDevFGiw` · Better Stack · 2026-02-02 · q3 · intro · review · also: models-research, vibe-coding-app-building, coding-agents

Hands-on review of Moonshot's open-weight Kimi K2.5: video-to-website cloning, a single-image campaign site, and the Agent Swarm feature, with the speaker's verdict that the front-end output is strong but the research output had stale data.

- Techniques: Reference-video to front-end clone; Single-image creative brief; Force subagent fan-out by naming it in the prompt; Check the as-of date of generated research
- Tools: Kimi K2.5, Kimi CLI, FFmpeg, Claude Code, Kimi K2, Llama 4 Scout, GitHub Copilot

## [Anthropic Shows What Most Developers Are Missing](../videos/LC7kGTDoWRY.md)
`LC7kGTDoWRY` · AI LABS · 2026-02-02 · q2 · intro · news · also: coding-agents, testing-verification, enterprise-adoption

AI LABS argues that engineering is shifting from writing code to orchestrating agents, reviewing exceptions, and stating intent clearly, with a short sponsored segment and little measured evidence.

- Techniques: CLAUDE.md verification loop for long autonomous runs; Commit each verified unit, with decisions in the message; Split work into small independent units and run agents in parallel; Custom specialist subagents with chosen models and instructions; Plan mode with agent questions before building; Agent first-pass review with human review of exceptions; Layered security agents plus an external scanner
- Tools: Claude Code, CLAUDE.md, Claude Chrome extension, Puppeteer MCP, git, CodeRabbit, Cowork (Anthropic), Claude Opus 4.5, GPT-5.2, Golang, COBOL, Fortran

## [The Last Claude Code Tutorial You'll Ever Need](../videos/EHDzlot7LKU.md)
`EHDzlot7LKU` · AI LABS · 2026-02-02 · q3 · intro · tutorial · also: context-engineering, claude-code, skills-self-improvement

Principles for building your own agent workflow in Claude Code: progressive disclosure, external note files, context-budget hygiene, subagents, git and slash commands.

- Techniques: Progressive disclosure via skills; External note files for long tasks; Manual context hygiene; Delegating research to subagents; Format selection for context files; Git as memory and parallelism; Slash commands for repeated procedures
- Tools: Claude Code, Claude (Anthropic models, 200k context), Gemini (1M context), Sonnet 4.5, BMAD, SpecKit, agent.md / AGENTS.md, CLAUDE.md, Jira MCP, Figma MCP, Git, git worktrees

## [Is Kimi K2.5 Actually The Best Open Source Model?](../videos/D4ICNmfXmwI.md)
`D4ICNmfXmwI` · AI LABS · 2026-02-02 · q2 · practitioner · review · also: models-research, coding-agents

AI LABS hands-on test of Moonshot's Kimi K2.5: open-weight, not open-source; agent-swarm migration was not faster on a large codebase, while a Notion-clone-from-video test worked after one follow-up prompt.

- Techniques: Parallel per-group migration with a sub-agent per page group; Post-migration cleanup pass; Video-as-input UI cloning; Iterate on broken features with a follow-up prompt
- Tools: Kimi K2.5 (Moonshot AI, open-weight, 1T total / 32B active MoE), Kimi Code CLI (agent CLI released with Kimi K2.5), ShadCN UI, Material UI, Claude Opus 4.5 (used as a comparison model), Claude Code (compared for sub-agent behavior and pricing), Notion (cloned from screen recording), DeepSeek (architecture comparison only), Opera Neon (sponsor, agentic browser)

## [Claude Code's HIDDEN Agent Swarm (Better Than Kimi K2.5?)](../videos/eRu5kIYAAz8.md)
`eRu5kIYAAz8` · Better Stack · 2026-02-02 · q2 · intro · review · also: claude-code, coding-agents

Better Stack demos an unreleased Claude Code "agent swarm" mode, hidden behind a flag, where an orchestrator spawns specialized sub-agents on the fly, then argues Anthropic is unlikely to ship it soon as-is.

- Techniques: Plan-file to swarm execution (reproducing the demo); Checking existing sub-agents before a swarm run; Manual sub-agent memory via shared markdown files
- Tools: Claude Code, Claude Sneak Peek (fork of CC Mirror), CC Mirror, Kimi K2.5, Opus (mentioned as a benchmark comparison, no version detail), XDL (X/Twitter video downloader, the demo target), Better Stack (log monitoring, anomaly detection, AI-native error tracking)

## [Claude Code Just Got a Brain Upgrade Inspired By Beads](../videos/-xOAYPjhigY.md)
`-xOAYPjhigY` · Better Stack · 2026-02-02 · q3 · intro · review · also: claude-code, context-engineering, agent-architecture

Better Stack walkthrough of Claude Code's new task system (v2.1.6+), which replaces todos with JSON-backed tasks that support dependencies, sub-agents, and shared task lists across sessions; compared against Beads and the Ralph Wiggum loop.

- Techniques: Plan file to tasks, then sub-agent execution; Shared task list across sessions via env var; Version-control task state
- Tools: Claude Code (v2.1.6+), Beads, Ralph Wiggum loop, Opus 4.5, XDL (CLI for downloading videos from X/Twitter, used as the demo project), Better Stack

## [Claude Code's Creator Does This Before Every Single Project](../videos/B-UXpneKw6M.md)
`B-UXpneKw6M` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · also: claude-code, testing-verification, context-engineering

Boris, who created Claude Code at Anthropic, shares a short workflow: give the agent a way to verify its work, keep CLAUDE.md lean and team-maintained, use plan mode and scoped permissions, and run parallel or background sessions.

- Techniques: Verification line in CLAUDE.md; Tests-first or tests alongside each feature; Browser or screenshot verification for UI; Team-maintained CLAUDE.md; Mistakes from PR review go into CLAUDE.md; Project-scoped allow/ask/deny permissions; Plan mode before execution; Parallel sessions with numbered tabs; Cloud background agents with teleport; Background verification tasks; Stop hook for verification; Loop plugin for autonomous runs; Per-language linters and formatters; Committed slash commands; Narrow subagents
- Tools: Claude Code, CLAUDE.md, Claude Code GitHub action, Claude Code on the web (cloud sessions), Claude browser extension, Opus 4.5, Sonnet, Haiku, Ralph Wiggum plugin, MCP servers (Slack, Notion), BigQuery CLI, Sentry CLI

## [I Couldn't Believe Claude Tasks Could Do This](../videos/li8bIt-mjbA.md)
`li8bIt-mjbA` · AI LABS · 2026-02-02 · q2 · intro · review · also: claude-code, agent-architecture, coding-agents

Walkthrough of Claude Code's new built-in task system: a coordinator splits work into a dependency graph, runs independent sub-agents in parallel, and persists tasks outside the context window so they survive /clear and restarts.

- Techniques: Explicit dependency breakdown prompt; Fan out independent sections of a spec; Named long-running sessions; Inspect task state on disk; Batch folder documentation with Cowork; Research-then-implement handoff
- Tools: Claude Code, Cowork, Claude Chat, Opus 4.5, Haiku, Sonnet, CLAUDE.md, Notion, Lovart (sponsor segment, not evaluated)

## [Cursor 2.0 Changes Everything - It Feels Illegal](../videos/4QUBKKX2ktQ.md)
`4QUBKKX2ktQ` · Better Stack · 2026-01-02 · q2 · intro · news · also: coding-agents

A 4-minute Better Stack overview of Cursor 2.0 (Oct 2025 release): the Composer model, up to eight parallel agents in isolated worktrees, and a built-in browser, with mostly unquantified claims and a sponsor plug.

- Techniques: Parallel agents in isolated work trees; Assign, then verify diffs; Check the privacy opt-out before use; Starter run from the video
- Tools: Cursor, Cursor Composer model, Cursor built-in browser, Claude (as the latency comparison), VS Code (Cursor is a fork of it), ChatGPT (mentioned in passing), SWE-bench Verified, Better Stack (sponsored logging plug)

## [China's Mind-Control AI Just Dropped on GitHub (100% Free)](../videos/8ear9y9qE7w.md)
`8ear9y9qE7w` · Better Stack · 2026-01-02 · q2 · intro · review · also: data-engineering, security-guardrails

Hype-titled walkthrough of BetterFish, a multi-agent public-opinion pipeline with parallel specialist agents and an LLM-moderated debate. The demo stalls before reports, and the speaker flags legal risks, so treat it as an architecture sketch.

- Techniques: Parallel specialist agents over a precomputed store; LLM-moderated agent debate before synthesis; Per-agent model routing through OpenRouter
- Tools: BetterFish, MindSpider (scraper), Flask, Playwright, MySQL, PostgreSQL, Docker, Hetzner CAX31, OpenRouter, Gemini 3, Kimi, DeepSeek

## [I Let AI Argue About a Stock](../videos/ce3_LzVm2Jg.md)
`ce3_LzVm2Jg` · Better Stack · 2026-01-02 · q2 · intro · tutorial · also: agent-architecture, dev-tools

Better Stack demo of Trading Agents, an open-source Python multi-agent project that simulates a trading firm with LLM analyst agents and a bull/bear debate; a quick CLI walkthrough with cost and non-determinism caveats.

- Techniques: Role-specialized analyst agents plus adversarial bull/bear debate; Scripted run instead of CLI; Model-agnostic setup
- Tools: Trading Agents (open source Python project, multi-agent trading simulation), LangGraph, OpenAI API, Alpha Vantage API, Yahoo Finance, Anthropic API, Google models, Conda, Python 3

## [Claude Cluster is Insane… Upgrade Your Claude Code Workflow ](../videos/V-xBaFveTvA.md)
`V-xBaFveTvA` · AI LABS · 2026-01-02 · q2 · intro · review · also: claude-code, coding-agents, dev-tools

AI LABS walkthrough of Claude Code background subagents, using git worktrees to run parallel agents on isolated branches, plus a few changelog features. Hype title, sponsored segment, and shallow on mechanics.

- Techniques: Background a research or review subagent; Parallel review fan-out; Worktree-per-agent via a custom slash command; Named project agents via --agent flag; Fork a session on resume; Keep background tasks isolated and named
- Tools: Claude Code (background agents, tasks command, --agent flag, resume flag, custom slash commands, instant auto-compact, prompt suggestions), git worktree

## [OpenAI Swarm Hype Explodes: AgentKit Drives Multi-Agent AI Revolution](../videos/oV3IjJSXQyM.md)
`oV3IjJSXQyM` · Better Stack · 2026-01-02 · q2 · intro · news · also: agent-architecture, mcp-and-tools

Better Stack argues OpenAI's deprecated Swarm is not back and that AgentKit (Oct 2025) is the real multi-agent upgrade, but the video gives few technical details and mostly unsourced claims.

- Techniques: Migrate off Swarm-style stateless handoffs to a framework with state and tracing; Budget multi-agent traces for latency and retries; Built-in trace-and-score evals for agent performance
- Tools: OpenAI Swarm (deprecated March 2025), OpenAI Agents SDK, OpenAI AgentKit (Agent Builder, ChatKit, connector registry), OpenAI Chat Completions API, RFT (reinforcement fine-tuning) beta, o4-mini (transcribed 'O4 Mini'), GPT-5 (multi-model stack, mentioned without detail), MCP (Model Context Protocol; transcribed 'MPC'), DeepSeek (transcribed 'DeepSeq'), Llama (transcribed 'Ulma 3')

## [Before You Pay for Manus AI, See What This Free Tool Can Do](../videos/S3Q7CCV_PzE.md)
`S3Q7CCV_PzE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: local-ai, agent-architecture

Walkthrough of installing and running Agentic Seek, an open-source Manus-style multi-agent tool that runs locally or through a cloud API, with the speaker's hardware and cost caveats.

- Techniques: Install from the README; Switch config.ini from local to API mode; Headless browser and voice options; Start order; Planner plus specialized agents
- Tools: Agentic Seek (version not stated), Manus AI, Docker, Python 3.10, Ollama, Qwen, DeepSeek, GPT-4o, GPT-4o mini, Cursor (editor used for config)

## [How to 10X Your Claude Code Workflow](../videos/xhrqmAWI_cw.md)
`xhrqmAWI_cw` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, claude-code, context-engineering

Walkthrough of a compound-engineering Claude Code plugin (plan, work, review, triage, codify, resolve commands) that persists to-dos and runs parallel review agents. Practical, but the 10X title is unmeasured.

- Techniques: Plan, work, review, triage, codify, resolve command loop; Built-in to-do tool as the phase ledger; Pause-per-phase human checkpoint; Context check before each phase; Language- and concern-specific parallel review agents; Dependency-graph parallel resolution of to-dos; Git ingest for Q&A on a repo; Install as a plugin via marketplace
- Tools: Claude Code, compound engineering (Claude Code plugin), Claude Code plugin marketplace, Claude Code built-in to-do tool, GitHub issues, git worktrees, git ingest, BMAD method (compared, not used), Next.js, FastAPI, Python, TypeScript

## [Google A2A Protocol Explained: Tutorial, Demo, & How It Works with MCP & AI Agents](../videos/GUozMSpnmcc.md)
`GUozMSpnmcc` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools

Explainer of Google's A2A (agent-to-agent) protocol: agent cards for discovery, how it complements MCP, a hiring demo, and a CrewAI sample repo to clone.

- Techniques: Select a remote agent by its card before delegating; Expose agent cards as MCP resources; Generate A2A client and server code from the docs; Quickstart with the sample agent repo
- Tools: A2A protocol (Google), MCP (Model Context Protocol), Google Agentspace (spoken as 'agent space'), Google Agent Development Kit (ADK), LangChain, CrewAI, Gemini API, Cursor (@docs feature), Google A2A GitHub repo (sample agents; name not stated)

## [These Factory AI Droids Built My App in 10 Minutes! (Rust + TypeScript!) 👉 Code, Debug & Ship Apps](../videos/4ZYxlTPX-LM.md)
`4ZYxlTPX-LM` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, software-factory

A hands-on tour of Factory's "droids" (role-specialized coding agents) building a Tauri desktop chat app, covering local bridge setup, command approval, and a model-switch debug. Thin on depth; the title overstates it.

- Techniques: Role-split agent team; Paired local bridge for hosted agents; Pre-approved command checklist with per-command risk prompts; Live file-diff preview during agent edits; Model-swap triage for a model-dependent bug
- Tools: Factory Droids, Factory Bridge (desktop app), Tauri, Rust, TypeScript, OpenAI API, GPT-4, Gemini 2.5 Pro, Notion (integration named), Jira (integration named), Linear (integration named)

## [Agno AI Agent Tutorial: Build & Run AI Agents with Agent UI + MCP + CrewAI (Best Tutorial)](../videos/RWQv6JV7rKw.md)
`RWQv6JV7rKw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, agent-architecture

A short tutorial on Agent UI, an open-source Next.js chat front-end for agents. It shows swapping Agno's playground for a FastAPI backend and routing between specialist agents over A2A.

- Techniques: Install Agent UI via the docs' npx template; Swap the Agno Playground for your own backend; Main-agent router over specialist endpoints; Cap reply length with the system prompt
- Tools: Agent UI, Agno, Agno Playground, Next.js, npx, FastAPI, OpenAI SDK, A2A (agent-to-agent protocol), Cursor, LangChain, gpt-4o-mini, Gemini 2.5 Pro (mentioned in the demo answer, not used by the presenter's own setup)

## [Cursor AI Had a BIG PROBLEM — I Just Found the FIX](../videos/UngBxJ9uy70.md)
`UngBxJ9uy70` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, coding-agents, context-engineering

AI LABS walkthrough of GitMCP, which turns any GitHub repo into a hosted MCP docs server, shown as an alternative to Context7 for keeping Cursor grounded in current docs, with a three-agent A2A demo.

- Techniques: Per-repo hosted MCP docs via URL swap; Scope docs to one repo instead of a broad doc index; Use the hosted repo chat as a post-build spec check; Router agent plus domain specialist agents over A2A; Routing check by server log
- Tools: Cursor, Gemini 2.5, GitMCP (gitmcp.io), Context7 MCP, MCP (Model Context Protocol), A2A (Google Agent-to-Agent protocol), Claude Desktop, Windsurf, VS Code, Claude, LangGraph (docs example), Three.js (demo project)

## [What Cursor Doesn't Have: Claude Code Subagents](../videos/Ppu6pJ5yyD4.md)
`Ppu6pJ5yyD4` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: claude-code, coding-agents, context-engineering

Walkthrough of Claude Code's native subagents: creating project agents with /agents, why isolated context windows help, and how auto-delegation and chaining work. Practical but thin, with a sponsor segment.

- Techniques: Create a project-scoped subagent with /agents; Write a specific description and scope tools tightly; Spec file plus rules file handed to a builder subagent; Theme swap through a subagent; Chain subagents in a custom slash command; Invoke a subagent explicitly
- Tools: Claude Code, Claude Code subagents (/agents), Cursor, ShadCN UI, ShadCN UI MCP server, Next.js, Tailwind CSS v3, TweakCN, TestSprite MCP server, BMAD workflow, SuperClaude workflow, GitHub subagents collection (unnamed)

## [How I ACTUALLY Use Claude Code... My Complete Workflow](../videos/7Sx0o-41r2k.md)
`7Sx0o-41r2k` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: claude-code, context-engineering, coding-agents

A host walks through a multi-agent Claude Code workflow for building an app: specialized sub-agents run in sequence, each writing its output to docs, with checkpoints for rollback and a generated agent-workflow setup.

- Techniques: Phased sub-agent chain driven by one prompt; Parallel sub-agent fan-out; Docs-first planning with scoped agents; Two-stage requirements before agent planning; Rewind with double-Escape checkpoints; Generate an agent workflow from a repo; Verbose view of sub-agent activity
- Tools: Claude Code, Claude Code sub-agents, Claude Desktop, Claude Opus, Cursor (checkpointing, as cited by the host), BMAD method, SuperClaude, gitingest.com, Next.js, UX researcher agent, sprint prioritizer agent, UI designer agent

## [3 Things Before You FINALLY Switch to Codex CLI](../videos/gRXrOuFn9dE.md)
`gRXrOuFn9dE` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, context-engineering

Hands-on comparison of Codex CLI against Claude Code: a single-prompt game test, the GUI options for each, an MCP workaround for missing sub-agents, and the BMAD planning method for multi-step builds. Sponsored intro; thin evidence.

- Techniques: Sub-agent delegation through an MCP server; Fork and patch an unmaintained community tool; BMAD-style plan-then-build workflow; Manual agent wiring for Codex; Edit MCP config from inside the Codex IDE extension
- Tools: Codex CLI (OpenAI), Codex IDE extension, GPT-5 Codex High (model used in the test), Claude Code, Phaser 3 (game engine), Kenney assets (spoken as Kenny), Three.js (spoken as 3.js), React, Next.js, shadcn/ui, Opcode (formerly Claudia), Conductor

## [TMUX Coding Is INSANE... Upgrade Your Claude Code Workflow](../videos/UgHbHqg_Wmo.md)
`UgHbHqg_Wmo` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: software-factory, claude-code

Walkthrough of a tmux-based orchestrator that lets one Claude Code agent spawn and manage several Claude Code teams via scheduled check-ins, spec-driven phases, and a skip-permissions setting. Useful pattern, but the live demo never ran.

- Techniques: tmux-based agent orchestrator setup; Fix hard-coded paths and permission command in the orchestrator; Spec folder as the build blueprint; Team start prompt pattern; Scheduled check-ins with restore-point commits; Summarize an unfamiliar repo with GitIngest
- Tools: tmux, Claude Code, tmuxorchestrator (repo name as spoken), Cursor (used only to show the folder structure on screen), shadcn, shadcn MCP, GitIngest (gitingest.com), ChatGPT (mentioned as a comparison for the summary step), Git (version control and restore-point commits)

## [This Designer is INSANE... The Ultimate UI Setup](../videos/uayt-IVbh8E.md)
`uayt-IVbh8E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, vibe-coding-app-building, context-engineering

Walkthrough of a Claude Code sub-agent pipeline for UI work: a UX agent drafts layout from requirements, a UI agent applies color variants, and a converter agent ports the HTML to SwiftUI.

- Techniques: Stage-separated UI sub-agent pipeline; Explicit agent count for variants; Split HTML output into HTML, CSS and JS files; Keep emoji placeholders, then fix icons in the target platform; Doc-grounded conversion guide via Context7, then bake into the agent
- Tools: Claude Code (sub-agents defined as markdown files), Cursor (mentioned in the intro as an AI coding tool, not used in the walkthrough), Context7 MCP, SwiftUI, iOS Simulator, HTML / CSS / JavaScript

## [How to use Reasoning Models Correctly?](../videos/w42_sbxa08w.md)
`w42_sbxa08w` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, models-research

Walkthrough of OpenAI's Reasoning Best Practices doc: keep prompts direct, skip chain-of-thought instructions, use delimiters, go zero-shot first, and use reasoning models as planners with cheaper models executing.

- Techniques: Section the prompt into Context / Examples / Instructions; Drop chain-of-thought scaffolding; Zero-shot first, then few-shot; Explicit constraints plus goal; Re-enable markdown in developer message (API); Planner/workhorse agent split
- Tools: OpenAI Reasoning Best Practices documentation, o1, o3-mini, GPT-4o, GPT-4o mini, Claude, Gemini, DeepSeek

## [This One Claude Code Feature Replaced My ENTIRE Team (Subagents)](../videos/zYPNfkDxgMg.md)
`zYPNfkDxgMg` · Better Stack · 2025-11-02 · q2 · intro · review · also: claude-code, context-engineering

Walkthrough of Claude Code's Custom Subagents (v1.0.60+): creating a read-only reviewer agent via the agents command, then running about ten subagents from one prompt, with token and time costs.

- Techniques: Create a personal-scope read-only reviewer subagent; Restrict a subagent to specific MCP tools; Delegate a task to a named subagent in the prompt; Batch several subagents in one prompt
- Tools: Claude Code (v1.0.60 or later, Custom Subagents), Claude Code agents command, GitHub (agent sharing), Claude Max subscription (speaker's plan; he notes the API would cost much more)

## [Claude Code Tutorial: Full Setup, MCP, and Cursor AI Integration (Claude Squad Guide)](../videos/u-GGktUnSgg.md)
`u-GGktUnSgg` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, coding-agents

Tutorial on running Claude Code inside Cursor and installing Claude Squad to run several Claude Code instances in tmux; the IDE link fails on camera and the MCP in the title is never covered.

- Techniques: Install Claude Code and open it in Cursor; Check the IDE connection from Claude Code; Install Claude Squad; Prepare a repository for Claude Squad; Run parallel sessions for front end and back end; One-shot build prompt that yields a to-do list
- Tools: Claude Code, Cursor, Claude Code extension for Cursor, Claude Squad (cs), tmux, GitHub CLI (gh), git, GitHub, OpenAI Codex, Claude Opus, Claude Max plan, Claude Pro plan

## [Claude Code Is an MCP Now?...3 CRAZY Things You Never Saw Coming](../videos/diTuQaSJ3nI.md)
`diTuQaSJ3nI` · AI LABS · 2025-11-02 · q3 · practitioner · review · also: claude-code, mcp-and-tools, token-cost-efficiency

Community tools that extend Claude Code: calling it as an MCP server from Cursor, routing it to other models (Kimi K2 via OpenRouter), a multi-agent "hive mind" mode, and a dedicated Claude Code Chat extension.

- Techniques: Expose Claude Code as an MCP server and call it from another client; Canvas-to-code handoff from Claude Desktop; Route Claude Code to OpenRouter models with Claude Code Router; Hive mind multi-agent sessions in Claude Flow; Dedicated Claude Code Chat window in the editor
- Tools: Claude Code, Claude Code SDK, Claude Code MCP server (community wrapper, unnamed in video), Claude Code Router (ccr), Cursor, Claude Desktop, Claude 3, OpenRouter, Kimi K2, Gemini, OpenAI models, DeepSeek

## [Warp Code Tutorial: Save 90% of Time with Warp AI Agents (vs Claude Code) Agentic Development](../videos/STd07QswCpk.md)
`STd07QswCpk` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering, mcp-and-tools

Sponsored walkthrough of building a full-stack notes app with Warp's agentic development environment, covering PRD planning, parallel agents split by API contract, saved prompts and rules, and MCP context.

- Techniques: PRD-first, then API contract, then fan out; Saved prompts as reusable commands; Templated workflows for known-hard setup steps; Rules to pin dependency and library behavior; Notebooks as context documents; Explicit task list for long runs; Parallel agent tabs with completion monitoring
- Tools: Warp (agentic development environment and terminal, with a built-in AI agent), Warp Drive (saved prompts, rules, MCP servers, workflows, notebooks), Context7 MCP, Playwright MCP, ChatGPT, Express Validator, Zod, Next.js, SWE-bench (vendor claim: 75.8%), Terminal Bench (vendor claim: #1)

## [NEW OpenAI AI Agents SDK – Multi-Agent AI Made Simple](../videos/ZvvQKie3X70.md)
`ZvvQKie3X70` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: agent-architecture, mcp-and-tools, observability

Better Stack walkthrough of OpenAI's new Python Agents SDK: agents, handoffs via a router agent, function and built-in tools, local context, input guardrails, and built-in tracing.

- Techniques: Router/triage agent with handoff descriptions; Function tool from a Python function; Typed local context object; Guardrail as a classifier agent; Inspecting run steps with new_items
- Tools: OpenAI Agents SDK (Python), OpenAI web search tool, Pydantic, OpenAI platform traces

## [Grok 4 is the SMARTEST model in the WORLD ($300/month!?)](../videos/0v1xW1wmF7A.md)
`0v1xW1wmF7A` · Better Stack · 2025-11-02 · q3 · intro · news · also: models-research, token-cost-efficiency

Quick news recap of Grok 4 and Grok 4 Heavy: reasoning-only models, $300/month Heavy tier, and vendor-reported benchmark wins, with the speaker judging them the smartest commercially available model right now.

- Techniques: Parallel multi-agent attempts with best-answer selection (Grok 4 Heavy)
- Tools: Grok 4, Grok 4 Heavy, Grok 3, Claude Opus 4, Claude (caption 'ClaudeForce', likely Sonnet), OpenAI o3, o4 mini, Gemini 2.5 Pro, Cursor, VS Code, Artificial Analysis, ARC-AGI-2

## [The BMAD Method: The Ultimate AI Coding System](../videos/fD8NLPU0WYU.md)
`fD8NLPU0WYU` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, coding-agents

BMAD Method tutorial: role-based agents (PO, scrum master, dev, QA) shard a PRD and architecture doc into epics and stories with approval gates, run in Cursor or Claude Code.

- Techniques: Two-document spec bootstrap; Shard then epic/story decomposition; Manual approval gate via story status field; Fresh chat per agent role; Story packet handoff; Learn an unfamiliar repo by feeding it to an LLM; Per-project install with npx; Asterisk commands and role switching
- Tools: BMAD Method (BMAD Code's agile workflow; version not stated), Cursor, Claude Code, Windsurf, ChatGPT, Claude, Gemini, GitIngest, npx (BMAD installer)

## [Github Spec Kit FINALLY Fixed AI Coding](../videos/M0ivqkQ5mF4.md)
`M0ivqkQ5mF4` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, coding-agents, testing-verification

A walkthrough of GitHub Spec Kit's specify, plan and tasks workflow driving Claude Code on a demo app, with an honest verdict: the spec-first flow works, but tasks run by hand and the UI came out cluttered.

- Techniques: Requirements in a general chat model before spec-kit; Run /specify with the requirements and answer the clarification flags; Run /plan after the spec is settled; Run /tasks and write tests before implementation; Run independent tasks in parallel with sub-agents
- Tools: GitHub Spec Kit ("Specify"), Claude Code, ChatGPT, Gemini (supported assistant), GitHub Copilot (supported assistant), ShadCN UI components, Notion (visual theme followed), git

## [ShadCN Dropped Something to FINALLY Fix Your UI](../videos/mSMflOx5pq8.md)
`mSMflOx5pq8` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools, coding-agents, context-engineering

Tutorial on shadcn's official registry MCP: add extra community component registries, then run a multi-subagent workflow (requirements, component research, implementation) to build UIs without unnecessary components.

- Techniques: Install the shadcn registry MCP; Add third-party component registries; Preview a registry's visual style before using it; Three-stage subagent workflow for UI builds; Express agent for small changes; Port the commands to Cursor; Apply a TweakCN theme
- Tools: shadcn (CLI and registry MCP server), Claude Code, Cursor, VS Code, Next.js, React, npm, components.json, mcp.json, Aceternity UI, Origin UI, Neo Brutalism (registry, failed)

## [AI Agent Protocols Explained: MCP, A2A, ACP and More](../videos/tb0c70DROYE.md)
`tb0c70DROYE` · Better Stack · 2025-11-02 · q3 · intro · review · also: mcp-and-tools, agent-architecture

Better Stack walks through MCP, A2A, ACP and ANP: what each protocol does, where it fits, and short local demos of MCP (Goose), A2A (two agents on Ollama) and ACP (story writer). Practical orientation, no benchmarks.

- Techniques: Add an MCP server to Goose as a command-line extension; Chain MCP servers in one agent task; Build a standalone A2A agent (summarizer / ideator pattern); Serve several ACP agents from one server and call them over HTTP
- Tools: MCP (Model Context Protocol, Anthropic), JSON-RPC 2.0, A2A (Agent2Agent, Google) and its SDK, ACP (Agent Communication Protocol, IBM), ANP (Agent Network Protocol), AITP, ACONP / ACOMP, Coral, Agora, agents.json, WAP push, Goose

## [You Need Claude Sandboxes... 90% Faster AI Coding](../videos/xckU9n9r8Rs.md)
`xckU9n9r8Rs` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: coding-agents, software-factory, context-engineering

Walkthrough of running BMAD-planned stories in parallel with git worktrees and one Claude Code instance per subtask, with a QA agent review loop. The 90% title claim is not backed by the numbers shown.

- Techniques: BMAD planning-first pipeline; Prompt the story generator to split stories into non-conflicting parallel subtasks; One git worktree per subtask, managed through Conductor; QA review then fix loop per story; PR per story, merged by Claude Code
- Tools: BMAD method (planning agents, Scrum Manager, dev and QA agents), Claude Code, Claude Desktop, ChatGPT, Cursor, Conductor (multi-workspace UI for parallel Claude Code runs), git worktrees, GitHub, Next.js (initialized in story 1), OutSkill (sponsor segment, not used in the demo)

## [Claude FINALLY Fixed AI Coding By Releasing This](../videos/oj44Vrh0XyM.md)
`oj44Vrh0XyM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, claude-code, memory

Walks through four Claude Code context-engineering techniques from Anthropic's "Effective Context Engineering for AI Agents" paper: compaction, context editing and memory, structured note-taking, and subagents. Mostly a conceptual intro with small demos; the main takeaway is to pick the technique that fits the task.

- Techniques: Manual compaction with retain instructions; Persistent instruction via the # memory shortcut; CLAUDE.md as the project brief; Structured note files maintained by the agent; Coordinator plus specialist subagents
- Tools: Claude Code, Claude Sonnet 4.5, CLAUDE.md, Claude memory tool, ACI.dev Gate22 (open-source MCP gateway, sponsor), Anthropic paper: Effective Context Engineering for AI Agents

