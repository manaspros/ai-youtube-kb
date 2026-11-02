# software-factory — 95 videos

*autonomous / background coding agents shipping code end-to-end; spec→PR pipelines; agent fleets; "dark factory"*

By channel: AI Engineer 69 · Kai Explains 2 · AI LABS 8 · Better Stack 16

**Synthesized guide:** [guides/software-factory.md](../guides/software-factory.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [I Made a Fruit Fly Review My Code - Nick Nisi, WorkOS](../videos/geMAe-PLJF4.md)
`geMAe-PLJF4` · AI Engineer · 2026-11-01 · q3 · intro · talk · also: pr-code-review, testing-verification

Nick Nisi (WorkOS) demos a fruit-fly connectome trained to approve or reject code diffs, and argues humans should review for intent and proof of work, not bugs.

- Techniques: Team-owned review skill as a gate; Tiered PR escalation pipeline; Agent proof-of-work bundle for review; Measure the reviewer on a labelled diff set; LLM as structured feature extractor before a non-LLM classifier
- Tools: fruitfly.review (speaker's online demo of the fly reviewer; URL as spoken), Greptile (automated AI PR reviewer, named as a comparison), CodeRabbit (automated AI PR reviewer, named as a comparison), Codo (automated reviewer named in the pipeline; name as spoken, may be a caption error), Claude and Codex (named as coding agents that solved the coding problem), Pi (the speaker's coding agent, referenced via 'Pi extensions'; spoken name), GitHub code owners (used to route PRs to the DX team), GEV / JEV / CLEF (LLM and classifier names as spoken; likely auto-caption errors; the LLM is described as a 'System 1 model' that produces the 30 questions), Doom and Beat Saber (prior fruit-fly demos mentioned as context, not tools for the reader)

## [Why Humans Can't Keep Up With AI-Written Code - Tariq Shaukat, Sonar](../videos/LQW_Wvqhp04.md)
`LQW_Wvqhp04` · AI Engineer · 2026-10-30 · q3 · practitioner · talk · also: testing-verification, evals, governance-compliance

Vendor talk arguing AI-generated code makes volume cheap but confidence scarce, so software factories need intent, guide rails, independent verification and evidence, with LLM judges treated as unreliable.

- Techniques: Code confidence formula as a factory checklist; Guide rails over guard rails; Deterministic plus agentic verification mix; Measure judge stability before trusting an LLM judge; Model per-step reliability to pick task length
- Tools: SonarQube, Sonar Vortex, Claude Mythos preview (named as the model in the Meter study, version as stated in talk)

## [Why a One-Line Change Can Break Your Whole Stack - Cole Gannaway, Qodo](../videos/YqxpPI7YUjE.md)
`YqxpPI7YUjE` · AI Engineer · 2026-10-29 · q2 · intro · talk · also: pr-code-review, context-engineering, multi-agent

A Qodo solutions engineer argues PR review is the bottleneck in AI software factories and needs cross-repo blast-radius context, independent reviewers and rules learned from past reviews. Mostly a product demo.

- Techniques: Blast-radius-aware review over a software graph; Rules learned from review comments; Pre-generation context injection; Independent, varied reviewers; Mid-run review checkpoints via skill; Ticket-linked PR review
- Tools: Qodo (spoken as Kodo), Jira, Linear, MCP servers, Claude Code, Anthropic models, OpenAI models, Bitwarden (example repo, open source password manager), CLI

## [How Anthropic Merges 30,000 Code Changes a Day - Manish Kapur, Sonar & Addy Osmani, Anthropic](../videos/AnsXWH2_EBU.md)
`AnsXWH2_EBU` · AI Engineer · 2026-10-29 · q3 · practitioner · panel · also: pr-code-review, testing-verification, governance-compliance

Sonar and Anthropic discuss verification as the bottleneck for agent-written code, covering layered checks, codified taste in CLAUDE.md/AGENTS.md, labeling agent PRs and the lights-on vs dark software factory spectrum.

- Techniques: Verification-first agent loop with a first-pass reviewer; Codify taste in CLAUDE.md or AGENTS.md for review agents; Require verification evidence before human review; Layered verification stack; Label agent-authored PRs and keep a named human owner; Agent guide rails and permission control
- Tools: Claude Code (called 'Cloud Code' in the transcript), Claude (claude.ai web product), Opus 5.5 (Anthropic model, named as a reference point for model quality), Anthropic code review product (named only as a product Anthropic offers), CircleCI (cited statistic), Sonar (verification vendor; survey and product referenced), CLAUDE.md / AGENTS.md (agent instruction files)

## [What Does an AI Engineer Do Now? - Aparna Dhinakaran, Arize AI](../videos/ImnZ7s68jw8.md)
`ImnZ7s68jw8` · AI Engineer · 2026-10-26 · q3 · practitioner · talk · also: observability, evals, agent-architecture

Arize's Aparna Dhinakaran argues the AI engineer's job is now building the build-eval-ship-monitor-improve loop itself, with always-on agents consuming telemetry and evals aligned to human judgment.

- Techniques: Telemetry-triggered always-on agent sweep; Issue memory across agent runs; Sandbox-per-run with single proxy egress; Durable agent resume; Harness and model abstraction with per-run evaluation; Evaluator alignment against golden data; Offline plus online evals on the same definitions; Trace the coding agents too
- Tools: Arize Signal, Arize Evaluator, Claude Code, Cursor, Codex, Anthropic model family (multiple models, unnamed)

## [Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One](../videos/bU5gDVyu_28.md)
`bU5gDVyu_28` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · also: context-engineering, testing-verification

Max Kanat-Alexander (Capital One) argues code quality only matters for durable software: it's worth rigor when consequences, replacement cost, dependencies and maintenance are high, and rigor is cheaper when you standardize and automate it.

- Techniques: Place software on a durable-to-disposable spectrum; Make software more disposable on purpose; Standardize to reduce the cost of rigor; Build in-workflow tooling; Provide in-memory fakes for services; Turn lint rules to maximum from the start
- Tools: Chromium (example codebase), Linux (example Hello World)

## [One Day, $1,000 in Tokens: An AI War Room for Legacy Code — Ford Prior, GEICO](../videos/DouK81O8R3o.md)
`DouK81O8R3o` · AI Engineer · 2026-10-21 · q4 · practitioner · talk · also: multi-agent, context-engineering, enterprise-adoption

GEICO's Ford Pryor describes an AI "war room" for legacy code modernization: a roster of decision makers, a driver, and fleet-managed Claude agents that take a major change from goal to approved design and agent-callable APIs, with human gates along the way.

- Techniques: War room composition for a major change; Three-repo split of enterprise agent context; Goal-to-approval-to-build loop with a queue; Milestone artifacts plus deterministic gate checks; Taxonomy for modernization missions; Local bindings file for agents on a laptop; Cost guardrails for agent-run work
- Tools: Claude Code, Anthropic Code Modernization plugin, Fleet Kit (Anthropic-collaborated fleet manager, markdown rules; not open source yet), beads (per-agent state tracking), Claude artifacts (HTML worksheets), draw.io, Figma, Slack (mission channel), GitHub Issues (example queue), Fable (model, named in the talk), Sonnet 5.5 (model), Opus 4.8 (model, named as too weak for this steering)

## [Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, Sonar](../videos/7b9tov5Uc5s.md)
`7b9tov5Uc5s` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: pr-code-review, governance-compliance, infra-cost-scaling

Gautam Korlam (Sonar/QAR, ex-Uber) on why CI, merge queues and review were built for human speed, and how to keep agent-scale commits green, fast and auditable in regulated teams.

- Techniques: Parallel speculative merge queue; Move checks left and offload expensive checks; Cache, shard and reduce compiler churn; Layered AI review with a fast first pass; Policy-based auto-approval with escalation; Durable decision record on the PR
- Tools: Rust, GitHub, Next.js (captioned 'next text'), Uber SubmitQueue (captioned 'summit cube')

## [Everything is Open Source Now (Reverse Engineer Anything)](../videos/jtfpCGsbSJU.md)
`jtfpCGsbSJU` · Better Stack · 2026-10-12 · q3 · intro · news · also: testing-verification, coding-agents

Better Stack commentary on Artcraft, a viral open-source Adobe clone, and a "reverse engineer anything" MCP; the host tests Opus 5.5 rebuilding a 1990s pinball game in Rust with sub-agents and verification passes.

- Techniques: Reference-driven port with source-address traceability; Fresh-context verification pass after a fan-out; Verifiable-goal loop (test suite as the spec); Clean-room rebuild from public specs and observed behavior
- Tools: Artcraft, Photocraft, Vectorcraft, Filmcraft, Adobe Photoshop, Reverse Engineer Anything (MCP, GitHub), Hopper, Ghidra (transcribed as 'Geirdre'), IDA, Claude Opus 5.5, Rust, Pinball Space Cadet (original EXE from Internet Archive)

## [Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI](../videos/fnuNVFgLjHA.md)
`fnuNVFgLjHA` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: observability, evals, skills-self-improvement

Arize workshop on closing an agent's detect, investigate, fix, verify loop using an always-on trace-analysis agent, coding-agent skills, harness-as-judge scoring and replay experiments; mostly a product walkthrough.

- Techniques: Continuous failure clustering over production traces; Join trace evidence with the code path; Plain-language harness-as-judge rubric with tool access; Failure-dataset replay with agent experiments; Alert-triggered agent investigation; Agent skills for trace analysis from the coding agent
- Tools: Arize Signal, Arize skills, Arize agent experiments, Claude Code, OpenAI Agents SDK, FastAPI, Datadog, GitHub, Cursor, Codex

## [The SDLC You Build Yourself — Andy Wong, Andrei Bocan & Shane Wolf, Atlassian](../videos/ojJXgXLUQFc.md)
`ojJXgXLUQFc` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: pr-code-review, context-engineering, governance-compliance

Atlassian team walks through its AI SDLC stack (Jira Coding Agent, AI Reviewer, AutoDev, AI SRE, AI Planner) built on a shared context engine, with a hands-on workshop that was largely lost to Wi-Fi problems.

- Techniques: Org-wide standards as enforceable PR rules; Trained filter on review comments; Human-set authority flag on context sources; Acceptance-criteria self-check in a sandbox; Progressive migration with per-engineer quotas; Automation-triggered agent session per sub-ticket; Per-skill and per-subagent model selection; Spend caps and WIP limits on autonomous work
- Tools: Jira Coding Agent, AI Reviewer, AI AutoDev, AI SRE, AI Planner, Rovo Dev, Teamwork Graph CLI, Confluence, Bitbucket, Slack, Docker, Claude

## [Parameter Golf with AutoResearch — Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI](../videos/7RFJRDYroic.md)
`7RFJRDYroic` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: evals, agent-architecture, context-engineering

Hands-on workshop on autoresearch loops, where an agent edits code, a fixed eval scores each attempt, and only improvements are kept. Covers eval design, bounded runs, steerability and the Parameter Golf results.

- Techniques: Fixed-budget eval contract; Tree-of-attempts search with per-node diffs; Guidance file as the steering channel; Hidden validation set for contests and benchmarks; Constrained single-metric optimisation; Bridged session for direct steering
- Tools: Weco, Modal, Claude Code, Opus 4.8, OpenAI MLE-bench

## [Software Costs Millions to Make but Claude Cracked It in Seconds. (Pt - 1)](../videos/hl6VOfzky5E.md)
`hl6VOfzky5E` · Kai Explains · 2026-10-12 · q4 · practitioner · news · also: testing-verification, models-research, token-cost-efficiency

Kai Explains on where AI reverse engineering works: it succeeds when an automated answer key (byte-exact compile match, a test or a crash) grades each attempt, and the headline numbers hide that.

- Techniques: Build the oracle before the loop; Compile-and-byte-compare decompilation loop; Reconstruct the toolchain first; Keep the reference when changing the target; Report pass@1 and pass@k with the budget; Track API-equivalent cost next to subscription spend
- Tools: Ghidra, objdiff, Claude Sonnet, Claude Opus, Claude Max plan, GPT-6 Astra, GPT-5.6 Sol, SREBench, FFmpeg, Photocraft

## [From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot](../videos/b9UhZkKjX_A.md)
`b9UhZkKjX_A` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: coding-agents, observability, multi-agent

GitHub's Jose Palafox walks through the Copilot agent surfaces: local agents you steer, reusable shared agents, cross-repo orchestration, and headless agents in CI that get cost and trace visibility through OTel.

- Techniques: Headless one-shot agent in CI; Slash-command phase gates on issues; Scaffold agents from a one-line description; Marketplace or private-repo distribution; Orchestrate: issues as goals, agents per repo; Cross-model plan audit; Small-model codebase explorer; OTel per-agent cost monitoring
- Tools: GitHub Copilot CLI, GitHub Copilot SDK, GitHub Actions, GitHub Agentic Workflows, Awesome Copilot, OpenTelemetry, Slack, Microsoft Teams

## [Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop — Gabriel Martinez, G2i](../videos/6qkzlT962es.md)
`6qkzlT962es` · AI Engineer · 2026-10-10 · q3 · intro · talk · also: pr-code-review, context-engineering, product-ux

Gabo (G2i) argues AI slop comes from generation outrunning judgment. His fixes are conventions, small reviewable chunks, visible accountability, and ORC, an orchestration workflow built around review.

- Techniques: Single canonical pattern per concept; Diagram-first review surface; Small reviewable chunks with explicit ownership; Built-in adversarial and planning gates before merge
- Tools: ORC (G2i's orchestration system, described only at a high level), Ruby on Rails (convention-over-configuration example), SQLite (quoted maintainer comment on PR maintenance cost)

## [AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar](../videos/uuwDWRbxoYo.md)
`uuwDWRbxoYo` · AI Engineer · 2026-10-09 · q2 · intro · talk · also: pr-code-review, observability

Sonar's Ali-Reza Adl-Tabatabai pitches an agentic PR validation system (ex-Guitar) that reviews, fixes, and auto-merges PRs, with a trust ladder for rollout. Mostly product pitch, few numbers.

- Techniques: Trust-gated automation ladder; Autofix loop until green; Flaky-test detection and rule-based retry; Agent plus static-analysis hybrid; Model routing proxy with failover; Aggregate PR and CI analytics
- Tools: Sonar, SonarQube, Guitar (agent platform)

## [Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel](../videos/XqF-IFHBCkM.md)
`XqF-IFHBCkM` · AI Engineer · 2026-10-08 · q3 · intro · panel · also: enterprise-adoption, pr-code-review

Sonar and McKinsey panel on why most companies stall before scaling AI agents in the SDLC, and a staged trust ladder for moving from agent review to fully automated PR merge.

- Techniques: Staged autonomy ladder for agent PR workflows; Derive verification evals from the PRD; Lighthouse teams for best practice; Baseline developer metrics before automation; Write down implicit conventions as explicit specs

## [The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](../videos/exiwa9QbQXI.md)
`exiwa9QbQXI` · AI Engineer · 2026-10-08 · q3 · intro · talk · also: governance-compliance, context-engineering

Factory's Davis Palmie argues engineers should build a "software factory" of agents that turns signals like bug reports into production code, starting narrow, measuring outcomes, and staying model- and surface-agnostic.

- Techniques: Narrow-first, verifiable agent pillar; Close the loop only after tying outputs to input signals; Agent readiness checklist (eight pillars); Per-task model routing for cost versus quality; Single harness and context shared across surfaces; Outcome-based agent metrics
- Tools: Sentry, Slack, AGENTS.md, Factory

## [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](../videos/X6l4lpA0_NY.md)
`X6l4lpA0_NY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · also: agent-architecture, skills-self-improvement

Drew Knox of Tessl on building a "software factory" through harness engineering: three loops (inner, outer, meta), a three-layer setup order, and how Tessl's skills registry and automation support it.

- Techniques: Three-tier loop design for agent quality; Issue-to-PR control plane for agents; Governed skills registry; Mistake-to-skill feedback; Repeated task to scheduled skill; Human-intervention metrics as the factory KPI
- Tools: Tessl, Tessl Agent, tessl launch, Linear, GitHub, GitHub Actions, Codex, Claude Code, Gemini

## [From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI](../videos/F0TNSmbo5hE.md)
`F0TNSmbo5hE` · AI Engineer · 2026-10-06 · q2 · practitioner · workshop · also: observability, evals, claude-code

Arize workshop on closing the agent improvement loop: instrument an OpenAI Agents app with OpenInference, have a coding agent mine traces and patch failures, then automate it with Arize Signal. Vendor-heavy.

- Techniques: Turn on OpenInference tracing for an agent app; Install vendor agent skills into the repo for the coding agent; Trace triage that looks past error status; Single-problem fix loop with re-verification; Triage automated findings into issues, dataset rows, evaluators or PRs; Regression and guardrail evals before merging an automated fix
- Tools: Arize AX, Arize Signal, Alex (Arize in-product assistant), OpenAI Agents SDK, OpenInference, Arize AX CLI, Claude Code (VS Code extension), npx skills (arise-ai skills), npm, GitHub, WonderToys demo app (Arize sample)

## [Cooking with Codex — Charlie Guo & Gabriel Chua, OpenAI](../videos/FwiS44-xyYw.md)
`FwiS44-xyYw` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: coding-agents, multi-agent, context-engineering

OpenAI's hands-on Codex workshop walks through context, computer use, long-running goals, subagents, hooks and automations, then shows the app server for embedding Codex in your own product.

- Techniques: Verifiable goal with milestone files; Milestone-triggered review and goal-audit threads; Side-thread unblock and status query; Subagent vs thread handoff split; Hook-based deterministic guardrails; Heartbeat automation for external waits; Scheduled triage that spawns worktree threads to PRs; Choosing a control surface: computer use vs Chrome extension vs in-app browser; Embedding via the App Server protocol
- Tools: Codex app, Codex CLI, Codex remote (ChatGPT mobile), Codex Chrome extension, Codex computer use, Codex in-app browser, Agents SDK, Sites, Chronicle (research preview, Pro), AppShots (screenshot with embedded text), AGENTS.md, config.toml hooks

## [AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](../videos/Bdrs3uAX0_M.md)
`Bdrs3uAX0_M` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · also: coding-agents, context-engineering, rag-retrieval

Sourcegraph CEO Dan Adler argues that large, decades-old codebases are decaying under the flood of AI-written code, and that agents need code-graph and search infrastructure to see and change them across thousands of repos.

- Techniques: Deterministic scripts for mechanical sweep changes; Hybrid agent and script batch change loop; Code-graph plus search as agent context; Coverage audit for sweeping changes
- Tools: Sourcegraph, agentic batch changes, Claude Code, Codex, Cursor

## [Scale the Judgment, Not the Model — Andrew Orobator, Reddit](../videos/6MudaeKdBSk.md)
`6MudaeKdBSk` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: skills-self-improvement, testing-verification, context-engineering

Reddit's Andrew Orobator on scaling agent judgment rather than model size: encode institutional judgment as skills, work logs, personas and hard gates, verified by recordings, so coding agents can ship with less human review.

- Techniques: Skills as encoded review judgment; Work log plus commit-hook enforcement; Persona prompting for perspective; Recording-based agent QA; Rules-first funnel for LLM cleanup; OS-level gate with operator-only bypass; Three operating modes; Scheduled skill drift audit
- Tools: Codex, git pre-commit and commit hooks, CI, lint, screenshot-based model review

## [Orchestras, Not Factories: How the Fastest Builders Work — Charlie Holtz, Conductor](../videos/TRfzFJCJ7ZE.md)
`TRfzFJCJ7ZE` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: multi-agent, coding-agents, sandboxing-execution

Charlie Holtz (Conductor co-founder) lists six principles for fast agent-driven building: stay near the frontier, don't beat the market, mark slot-free zones, feed a central store, run free-range cloud agents, and orchestrate rather than run a factory.

- Techniques: Don't-beat-the-market test; Slot-free zones with CI-enforced human review; CLAUDE.md / AGENTS.md and skills as onboarding material; Central event store with a SQL tool for agents; Cloud sandboxes per task with lifecycle independent of the laptop; Agents calling the product API to create work
- Tools: Conductor, Claude Code, Codex, git worktrees, Postgres, Slack, Discord, Telegram, OpenClaw, React

## [No, That's Not a Software Factory — Ryan Cooke, WorkOS](../videos/HvboD89DyQ8.md)
`HvboD89DyQ8` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: mcp-and-tools, context-engineering, skills-self-improvement

Ryan Cooke (WorkOS) on why a sandbox plus coding agent is not a software factory. Build around outcome metrics, webhook-driven product workflows, and an internal MCP gateway.

- Techniques: Outcome-based factory metrics; Webhook-driven ticket pipeline; Agent plan refresh after each step; Agent-drafted PRD with human approval gate; Context-rich MCP gateway; Session mining for skill gaps
- Tools: Linear, Slack, GitHub, Notion, Snowflake, Cloudflare sandboxes, Claude Code, Devin, OpenCode, MCP

## [We're the bottleneck, but we don't have to be — Ido Salomon, AgentCraft](../videos/YIVkERhy8xo.md)
`YIVkERhy8xo` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: multi-agent, product-ux, coding-agents

Ido Salomon (AgentCraft) argues that humans are the bottleneck in agent work and demos a game-style orchestrator with attention-jumping, a map view, review kits, shared rooms, and a simpler "loopers" mode for non-engineers.

- Techniques: Attention queue with jump-to-next; Spatial projection of agent activity; Review kit for parallel agent output; Orchestrator with isolated local containers and background loops; Shared room with cross-agent notice board; Progressive disclosure for low-floor use
- Tools: AgentCraft, Claude Code, Codex, OpenCode, OpenClaw, Git, Telegram, MCP Apps (MCPUI)

## [Building Self-Improving Agent Software Factories — Suraj Gupta, Warp](../videos/TN3mj92oZ8I.md)
`TN3mj92oZ8I` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: skills-self-improvement, memory, token-cost-efficiency

Warp's Suraj Gupta on making agent software factories self-improve through outer-loop skill edits gated by PR review, agent-scoped versioned memory, and rule-based model routing for cost.

- Techniques: Outer-loop skill improvement with PR gate; Agent-scoped fact memory with provenance; Rule-based model routing by task class; Best-of-k model sampling to learn routing
- Tools: Warp, Oz (Warp cloud agent platform), Sentry, GitHub, Codex, Claude Code, Opus, Haiku, GLM, Qwen

## [How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner](../videos/I2LL_wd89-A.md)
`I2LL_wd89-A` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: pr-code-review, testing-verification, context-engineering

How the VS Code team moved from monthly to weekly releases by rebuilding its own dev system around agents: code-survival metrics, agent-readable repos, fast CI, UI feedback loops, AI triage, and staged rollouts.

- Techniques: Code survival metric; Agent-readable repo docs; Expert knowledge as a shared skill with an area owner; Screenshot-diff component browser; Self-correcting launch loop; Tiered AI code review; Deterministic filtering before agent action; Staged rollouts with error monitoring; Evals bootstrapped from issues; Prototypes instead of PRs for design talks
- Tools: VS Code, GitHub, GitHub Issues, GitHub Copilot code review, TypeScript Go, Playwright, Electron, Xcode MCP, AGENTS.md, Chrome extension

## [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](../videos/vGCJ7diEtrw.md)
`vGCJ7diEtrw` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: infra-cost-scaling, testing-verification, context-engineering

Factory's engineer defines a "software factory" as a full autonomous lifecycle, not coding agents. Covers model routing for cost, verifiable done-criteria, sequential worker and validator missions, deferred tool loading, and codebase readiness.

- Techniques: Difficulty-classified model routing; Validation contract written before coding; Sequential workers with fresh context per handoff; Two-tier validation; Deferred tool loading; Codebase readiness audit; Codify tacit rules as skills or plugins
- Tools: Factory (software factory platform), Factory missions (orchestrator, worker and validator agents), Automatic model routing, Deferred context engine, Agent readiness framework, Plugins, Auto-wiki, Slack, GitHub, Figma, Notion, Gmail

## [Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp](../videos/tUPPVhBBcoM.md)
`tUPPVhBBcoM` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: skills-self-improvement, pr-code-review, observability

Warp's founder argues software engineering is becoming factory engineering: agent loops run from triage to spec to implementation to monitoring, with humans gating stuck points and observer agents improving the skills.

- Techniques: Software factory loop with human gates; Triage routing by ambiguity; Product spec plus tech spec; Observer agent skill loop; Verification by running the product
- Tools: Warp, Claude Code, CI/CD, GitHub, Computer use

## [Shopify Just Released The Greatest AI Coding Workflow Ever](../videos/bBMp5tLxShQ.md)
`bBMp5tLxShQ` · AI LABS · 2026-10-02 · q2 · practitioner · tutorial · also: multi-agent, testing-verification, claude-code

AI LABS rebuilds Shopify's checkpoint-and-gates agent loop as a Claude Code orchestrator skill; the key idea is enforcing gates with a stop hook, not advisory rules.

- Techniques: Checkpointed build with human plan approval; Stop-hook gate; Test-first behavior gate without a browser; Prototype-driven visual gate; Adversarial critic and fixer loop; Learnings file for cross-task feedback; Single orchestrator entry skill
- Tools: Helix (Shopify internal, not released), Claude Code, Claude sub-agents, Gemini (used by Shopify as UI reviewer), Hedra MCP server (sponsor segment), design.md, Ralph loop (transcribed as RALF), AI LABS orchestrator skill (their own), Checkpoint Planner agent (their own), tdd planner skill (modified, their own), prototype skill (their own), adversarial loop skill (their own)

## [React-Native Is Dead... Thanks to AI.](../videos/r0u83Ss7QRc.md)
`r0u83Ss7QRc` · Better Stack · 2026-10-02 · q3 · intro · news · also: testing-verification, coding-agents, dev-tools

Better Stack commentary on Shopify dropping React Native for native apps, with Shopify's Helix checkpoint-gated agent loop and headless app logic for fast agent testing. Opinion-led, relays Shopify's blog post.

- Techniques: Checkpoint-gated agent migration (Helix pattern); Headless state plus CLI driver for agent testing; Avoid out-of-process UI automation for agent verification
- Tools: React Native, Shopify React Native packages (FlashList, React Native Skia, Restart), Helix (Shopify in-house agent migration system), Swift, Kotlin, SwiftUI, CloudKit, Apple XCUITest

## [Fixing the PR Bottleneck — Matt Pocock, AIHero](../videos/LlgiOCmFG_w.md)
`LlgiOCmFG_w` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: pr-code-review, testing-verification, context-engineering

Matt Pocock on clearing the PR backlog that AI agents create: layer cheap deterministic checks, have an agent review and commit fixes, design deep modules so tests stop being brittle, and run a retro on each session.

- Techniques: Layered brakes for agent PRs; Deep-module design for agent-testable code; Separate implementer and reviewer contexts; Reviewer commits fixes, comments only on open questions; Door-type and blast-radius PR summary; Pseudocode and diagram PR explanations; Retro over sessions and PRs
- Tools: AGENTS.md, coding-standards.md, CodeRabbit, Cursor BugBot, PlanetScale, Opus 5 (model mentioned in the tautological-test example), AIHero skills (version 1.3 announced for the same week)

## [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](../videos/xLUQOqjudtA.md)
`xLUQOqjudtA` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, memory, context-engineering

Tolan's engineers explain how a voice-first AI companion needs sub-two-second turns, stakes-based model routing, retrieval-style memory, and per-turn context rebuilding, plus how they use Claude agent fleets to ship iOS code.

- Techniques: Smart turn-taking from speech patterns; Per-stage latency instrumentation; Stakes-based model tiering with a cheap per-turn router; Retrieval-based memory with nightly consolidation; Stable-versus-volatile memory blocks; Character identity held separately from tone; Multi-judge eval loop for persona changes; Agent fleet with reviewer and PR-shepherd roles
- Tools: Claude, GPT-5.1, OpenAI Responses API, MCP, Linear, Sentry, Datadog, App Store

## [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](../videos/_ehJyfHg1Vk.md)
`_ehJyfHg1Vk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, claude-code, context-engineering

Kieran Klaassen (Every/Cora) on compound engineering: extract your judgment and repeated corrections into repo knowledge so each feature makes the next one easier, with a demo of his open-source plugin's commands.

- Techniques: Compound engineering loop; Ideation against strategy docs; Doc review for sharp questions; Brainstorm with minimal questions; Unattended end-to-end run (/lfg); PR polish with explanation; Extract a design rule from a review fix
- Tools: Claude Code, Codex, Cursor, Claude Cowork, Linear, GitHub, Slack, Intercom, Rails, React, MCP

## [How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face](../videos/FLUoowDJg4I.md)
`FLUoowDJg4I` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, observability, models-research

Hugging Face's Niels Rogge shows how nightly agents open outreach GitHub issues and PRs to move researchers' artifacts onto the Hub, moving from a fixed workflow to an autonomous agent loop.

- Techniques: Deterministic LLM pipeline mirroring the manual process; Cron for overnight background agents; Promote a step to an autonomous loop only where outputs are unpredictable; One container per work item for parallel agents; Skill as a manual trigger that fans out to subagents; Open-model routing through one OpenAI-compatible endpoint; Template completion from source material
- Tools: Claude Agent SDK, Cursor, Modal, GitHub Actions, Langfuse, Hugging Face CLI, Hugging Face inference providers, Slack, Gemini, Claude Code

## [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](../videos/bdHaOXZOhcM.md)
`bdHaOXZOhcM` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, enterprise-adoption, coding-agents

A CTO explains how a manager with a full calendar keeps building by running coding agents overnight (context gathering at 5pm, morning review), using evals and custom-model training as examples.

- Techniques: Overnight agent loop; Context-harvesting prompt; Test-first with end-to-end computer-use verification; Feedback-to-eval hill-climb; Overnight custom-model training with sandboxed cloud access; Prototype branch behind feature flags; Small PRs with an AI reviewer in a clean sub-agent
- Tools: Claude Code, Codex, Cursor, Dia, Wispr Flow, Slack, Jira, Confluence, Notion, SQLite, AWS EC2, ModernBERT

## [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../videos/qqrk7CtkuIw.md)
`qqrk7CtkuIw` · AI Engineer · 2026-09-18 · q3 · practitioner · interview · also: coding-agents, pr-code-review, enterprise-adoption

Anthropic's Mike Krieger on how Labs builds: delegate end states to agents, be less constrained with tools, share intent instead of 2,000-line PRs, and run fast persevere-or-pivot cycles.

- Techniques: Describe the end state, then review the trade-offs; Give agents a full environment instead of a narrow tool set; Port-verify-cross-read loop for large code migrations; Capture production runtime types to guide migrations; Share intent, trade-offs and production measurements in place of raw diffs; Tiered review: deep human review for architecture, fix-forward for cosmetic; Agent as a shared teammate in team channels; Instrument before you need it; use flags and dynamic config; Short bets with two-week persevere-or-pivot reviews; Unship primitives superseded by newer ones
- Tools: Claude Code, Claude Design, Cowork, Claude Code artifacts, Bun, MonkeyType, Slack, Python, TypeScript

## [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../videos/zCJtYuqwm7E.md)
`zCJtYuqwm7E` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, context-engineering

Patrick Debois (Tessl) argues that scaling coding agents is an organizational problem: teams must shift effort from fixing agent output to improving shared context, harnesses, and platform-owned reusable parts.

- Techniques: Convert skeptic critique into context and harness work; System-level retro; Split planning by agent readiness; Platform-owned reusable registry with a named owner; Per-team cost and iteration dashboards; Three-step AI-friendly hiring loop; Risk-tiered autonomy
- Tools: Claude Code

## [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../videos/L173Z8DpaJg.md)
`L173Z8DpaJg` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: pr-code-review, multi-agent, sandboxing-execution

Safia Abdalla (Warp) on building the Oz cloud agent platform: hide infra complexity, allow any harness, expose everything via API, and run the open-source repo with agent-gated triage and PR review.

- Techniques: Managed plus self-hosted sandboxes behind one model; Harness-agnostic layer with platform guardrails; Orchestrator with mixed-model sub-agents; Agent-gated PR review before human review; Agent-driven issue intake; API-first primitives for agents, sub-agents, environments and artifacts
- Tools: Warp, Oz, Claude Code, Codex, GitHub, Slack

## [Building Blocks for Uber’s Software Factory— Uday Kiran Medisetty & Adam Huda, Uber](../videos/17-YSUHo6Lk.md)
`17-YSUHo6Lk` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: mcp-and-tools, pr-code-review, enterprise-adoption

Uber's engineers walk through six building blocks (model gateway, MCP gateway, agent devpods, skills marketplace, context graph, Cortana) behind its managed software factory, then show one feature built end-to-end by an agent.

- Techniques: Single gateway with middleware chain and project attribution; Progressive MCP projection (direct, discovery, CLI, generated code); Pre-warmed agent workspaces; Skill marketplace with lint, review and trace feedback; Shared context graph queried before tool calls; Split review between an inner loop and an outer loop; Managed scheduled maintenance loops with bounded output

## [Every Level Of Claude Code Loop Engineering Explained](../videos/PLyRe6Zk--8.md)
`PLyRe6Zk--8` · AI LABS · 2026-09-02 · q4 · practitioner · tutorial · also: claude-code, agent-architecture, testing-verification

A three-level walkthrough of "loop engineering" in Claude Code: spec-as-/goal for one feature, a queue-driven software factory with a separate adversarial reviewer per branch, then phone control of the loop. Substantive, with the skills and steps shown.

- Techniques: Spec file as a /goal with explicit verification; Queue-file tracker for overnight multi-feature runs; Builder and adversarial verifier split; Clickable HTML mock per feature as planning and verification oracle; PR as the human approval gate; CLI-based platform setup driven by the agent; Minimal CLAUDE.md that points at AGENTS.md; Mobile control of a laptop-resident Claude Code session
- Tools: Claude Code, /goal (Claude Code slash command), /loop (Claude Code slash command), Codex (said to work with the same system), GSAP, Next.js, GitHub (and gh-style CLI), Supabase (and its best-practices skill), Vercel (and deploy-to-Vercel skill), Warp, VS Code, Paseo

## [The Open Model That Popped the AI Bubble](../videos/0y9B_sDLxjQ.md)
`0y9B_sDLxjQ` · Kai Explains · 2026-09-02 · q3 · practitioner · news · also: models-research, local-ai, token-cost-efficiency

News-and-analysis video on Alibaba's open-weight Qwen 3.8 Max: vendor benchmarks, self-run agent demos, weak coding scores, preview pricing, and China-hosted data-handling risk.

- Techniques: Unattended issue-driven build loop; Paper-to-code reproduction with ideation rounds; Base-URL swap to drive existing coding harnesses; Choose a deployment tier by hardware; Checklist before trusting a new open-model claim; Data-sensitivity triage for hosted models
- Tools: Qwen 3.8 Max, Qwen 3.8 27B checkpoint (transcribed as '3.827B'), Qwen 3.7+ and 3.7 Max (comparison models), Claude Opus 4.8, Claude Fable 5, GPT 5.6 Sol, Kimi K3, OhMyCly (repo name as transcribed), Tianchi competition platform, Recreation Bench, Ecommerce Bench, Terminal Bench 2.1

## [fighting slop with slop — Vaibhav Gupta, Boundary](../videos/AMiyLItEtLA.md)
`AMiyLItEtLA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, testing-verification, dev-tools

Vaibhav Gupta of Boundary argues that teams without code review can keep AI-written code stable by building internal tools that enforce invariants, mine agent transcripts, and rethink the language and tooling layers underneath.

- Techniques: Invariant-only architecture file; CLI guard checks for architecture invariants; Required reading as the gate for design docs; Transcript triage loop; A/B test skills or features by agent outcomes; Per-function CLI and describe tool
- Tools: BAML, Claude, Codex, TypeScript, Python, Rust, Go, Ruby, Java, WASM, ripgrep, Notion

## [How Forward Deployed Engineering is done at Cognition — Jia Wu](../videos/RVxym6mmIns.md)
`RVxym6mmIns` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: enterprise-adoption, product-ux

Jia Wu (Cognition) on forward-deployed engineering: embed in enterprise customers, map Devin to real backlog problems, and measure outcomes from agent sessions. Mostly a company pitch, with some case-study numbers.

- Techniques: Session-based value measurement; Event-triggered agent automation; Map backlog to capabilities; Before/after delivery metrics; Autonomous legacy migration
- Tools: Devin, Devin Cloud, Windsurf, Claude Code, Cursor

## [Why Software Factories Fail](../videos/Ib5GBkD555M.md)
`Ib5GBkD555M` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: pr-code-review, evals, context-engineering

Dex (HumanLayer) argues that agent "lights-off" software factories fail because coding models are trained on tests passing, not maintainable code, so teams must restore code review and plan up front.

- Techniques: Staged plan before agent implementation; Review the plan so the PR review is short; Check for test gaming with pre-patch runs and a quality judge; Diagnose RL-style reward gaps
- Tools: Claude Code, Codex, SWE-bench Multilingual, SWE-Marathon, DeepSWE, Frontier Code, Linear, Jira, HumanLayer

## [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](../videos/xIt_mTQp6mY.md)
`xIt_mTQp6mY` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: coding-agents, agent-architecture

Kyle Mistele (HumanLayer) argues agent loops should be built as incremental control loops (sensor, controller, actuator) that keep humans reading the code, not blind "Ralph" loops that dump 40k-line PRs.

- Techniques: Sensor, controller, actuator loop for code migration; Deterministic baseline plus per-PR ratchet; Ast-grep as the sensor; Golden-pattern skill for the actuator; Scheduled CI workflow as the loop runner; Feedback file plus comment-triggered re-steering; Single-open-PR flow control
- Tools: Claude Code, ast-grep, GitHub Actions, Effect (TypeScript), React Doctor, OpenClaw, OpenCode

## [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud](../videos/JJGbw4ggaFs.md)
`JJGbw4ggaFs` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: observability, context-engineering, coding-agents

May Walter (HUD) shows how HUD runs a weekly agentic workflow on GitHub Actions with Claude Code that mines production traces, scores performance fixes by ROI, verifies them at runtime, and sends a human-readable report to Slack.

- Techniques: Scheduled agentic investigation with runtime verification; Function-level production context map; Query language plus task skills; ROI and risk scoring with a human-readable gist; Vendor-neutral workflow layer; Targeted automatic checks for known performance smells
- Tools: Claude Code, GitHub Actions, MCP, ClickHouse, Slack

## [From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize](../videos/9HbzAWnKbo4.md)
`9HbzAWnKbo4` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, evals, sandboxing-execution

Arize's founder demos Signal, a background agent that reads production traces and logs, drafts an issue or fix with evidence, and hands it to a human reviewer, with the loop run in a sandbox.

- Techniques: Trace-to-file skill; Event- or schedule-triggered agent loop; Composable narrow skills over raw data; Sandbox per run, pluggable harness; Failure-to-evaluator loop
- Tools: Arize AX, Arize Phoenix, Pyroscope, Claude Code, Cursor, Daytona, GitHub, Google Cloud logging skills

## [How Forward Deployed Engineering is done at Ramp — Leo Mehr](../videos/ITMXwI6QL6A.md)
`ITMXwI6QL6A` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: enterprise-adoption, evals, context-engineering

Leo Mehr (Ramp) on forward deployed engineering: scope hard before building, then replace each FDE pipeline stage with agents, with evals and good context as the hard parts.

- Techniques: Scoping questionnaire before any build; Clarifying-question intake agent before spec; Stage-by-stage agent factory for the FDE lifecycle; Per-stage quality checks with evals, rubrics and human feedback
- Tools: Notion, Notion Agents, Slack

## [How Forward Deployed Engineering is done at Factory — Eno Reyes](../videos/wpOA-UXynoM.md)
`wpOA-UXynoM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: enterprise-adoption, testing-verification, product-ux

Eno Reyes (Factory CTO) on forward-deployed engineering as the way to build software factories. The bottleneck is agent readiness, meaning deterministic validators in the codebase, not model capability.

- Techniques: Audit validation loops before deploying agents; Bounded long-running harness with an explicit definition of done; Map the signal-to-deploy stages per org; Land-and-expand with a reference implementation; Split automation into one-click fixes and workflow changes; Model-independent harness with owned traces and self-hosted deployment
- Tools: Factory Droid, Missions, LegalDroid, linters, type checkers, security scanners, end-to-end test suites

## [Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](../videos/z0sh8HyTrDo.md)
`z0sh8HyTrDo` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: multi-agent, coding-agents, governance-compliance

Auditoria AI speaker says human attention bottlenecks agent work: use parallel worktree subagents, skills, one-pane UX, goals and loops, and self-improving harnesses, keeping humans at intake and sign-off.

- Techniques: Worktree-per-task parallel subagents; Ticket-to-stage pipeline with two human gates; Encode organizational procedure as skills; Single-pane minimal UX for orchestration; Daily self-retrospective on the agent's own loop; Goals plus loops, monitored from a phone; Background dreaming for pattern compaction
- Tools: Claude Code, git worktrees, Kubernetes, Docker, Jira, GitHub, MCP

## [Multiplayer agentic engineering — Arjun Singh, Superconductor](../videos/OL7kfezynJM.md)
`OL7kfezynJM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: coding-agents, sandboxing-execution

Arjun Singh (Superconductor) on making agent work multiplayer: one shared session across Slack, desktop, mobile and GitHub, cloud sandboxes, and benchmarking agents on your own codebase.

- Techniques: Cloud sandbox per project; Same session across interfaces; Artifacts as proof of work; Meeting bot as an idea-to-ticket intake; Acceptance-criteria fields in the ticket form; Network egress allowlist with grant prompts; Scoped credentials instead of ambient access; Codebase-specific agent benchmark; Switch defaults on evidence
- Tools: Claude Code, Codex, Cursor, Slack, GitHub, Linear, Sentry, Notion, Google Meet, Zoom, Microsoft Teams, GLM 5.2

## [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../videos/iQ5xldZ9StU.md)
`iQ5xldZ9StU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: security-guardrails, coding-agents, sandboxing-execution

GitHub Next demos Agentic Workflows (markdown playbooks compiled to Actions with deterministic guardrails) and ACE, a cloud multiplayer dev environment where humans and agents share chat and plans.

- Techniques: Markdown playbook compiled to CI workflow; Declarative guardrail front matter; Secret brokering outside the agent sandbox; Staged, logged writes; Swarm of role-specific workflows; Shared cloud session per branch with team chat as context; Shared markdown plan as contract; Automation triage by stack trace origin
- Tools: GitHub Copilot, GitHub Actions, Dependabot, Astro, Cloudflare, ACE (GitHub Next prototype)

## [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](../videos/LqLoYksJ6do.md)
`LqLoYksJ6do` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: security-guardrails, sandboxing-execution

Form3's Moritz Johner describes PatchPilot, an agent that patches CVEs across thousands of repos, and why production credentials make a coding agent a supply-chain actor needing deterministic controls, credential splits, and microVM isolation.

- Techniques: Deterministic controller plus scoped agent steps; Minimal change-set instruction plus post-agent vetting; Bounded CI-fix loop with human escalation; End-of-run retrospective aggregated across runs; Planted-injection end-to-end tests as evals; MicroVM sandbox with a policed egress path
- Tools: PatchPilot, Dependabot, Renovate, Firecracker, Docker, Kaniko, BuildKit, Landlock, bubblewrap, Go, Slack, GitHub

## [Bun Moved To Rust... Zig's Creator Fired Back](../videos/0TSxrzBVEwQ.md)
`0TSxrzBVEwQ` · Better Stack · 2026-08-02 · q4 · practitioner · news · also: multi-agent, testing-verification, coding-agents

Bun ported its ~1M-line codebase from Zig to Rust in 11 days using parallel Claude agents with an implementer, two adversarial reviewers and a fixer; the video also covers Zig creator Andrew Kelly's public criticism.

- Techniques: Adversarial review loop per unit of work; Porting spec plus lifetime table before code generation; Faithful port over idiomatic rewrite, all at once; Guardrails for parallel agents on one git repo; Sharding by git worktree; Error-driven crate-by-crate loop; Reviewer rule against justified workarounds; Test-file batch loops as the verification step
- Tools: Bun (1.3.14 final Zig release, 1.4 Rust), Zig, Rust, Claude / Claude Code, Fable 5 (pre-release model, as named in the video), cargo, git (worktrees), Next.js (dev-server hot reload test), JavaScriptCore, TigerBeetle (referenced by Kelly), Hacker News / GitHub (where the porting doc was noticed)

## [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../videos/ZpK5PWX2YRM.md)
`ZpK5PWX2YRM` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: pr-code-review, testing-verification, coding-agents

Alex Volkov on the "Z/L continuum" for how much agent-written code engineers should read in 2026: route review effort by the proof a change needs, not by a blanket rule.

- Techniques: Risk-tiered review routing; Decompose into atomic PRs with agents; Separate writer, inspector and test author; Turn review findings into system rules; Ask the agent where the critical code is; Loops with verification and retry
- Tools: Claude Code, Codex, OpenClaw, Pi, Antigravity, Grok Code

## [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../videos/c35YoMdnI78.md)
`c35YoMdnI78` · AI Engineer · 2026-07-18 · q3 · practitioner · panel · also: testing-verification, context-engineering, agent-architecture

Panel debate on whether agent "loops" (Ralph-style, bash-while-true) are hype or working practice; the consensus is loops work for verifiable tasks, need deterministic feedback and human-owned architecture, and are not yet a full software factory.

- Techniques: Fresh-context loop with file-system state; Back-pressure hooks that talk back; Deterministic controller around the LLM step; Context budget with headroom; Bare-model baseline on each new release; Explicit cost decision for high-value verification; Start small and iterate on real users; Vendor code and minimise open-source dependencies; Prefer statically typed languages for agent-maintained code
- Tools: Claude Code, Ralph loop (bash while-true), pre-commit hooks, PostHog, Notion, Sentry, Git, npm, Rust, Haskell, Python, TypeScript

## [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](../videos/pMggiOb18tc.md)
`pMggiOb18tc` · AI Engineer · 2026-07-18 · q3 · intro · keynote · also: coding-agents, multi-agent, agent-architecture

OpenAI's Codex team argues engineers move from watching agents to running manager-worker loops, with human attention as the scarce resource to spend on the outer loop.

- Techniques: Long-lived manager agent over worker agents; Trigger-driven manager wake-ups; Offload test runs to a separate machine; Server-side compaction for long tasks; Parallel attempts with a fast, strong model; Shared instruction file across agents; Chat-first UI with escalation to direct editing
- Tools: Codex, Codex app, Codex Cloud, Responses API, AGENTS.md, OpenClaw, OpenCode, Cerebras, VS Code extension, Xcode, JetBrains, Slack

## [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](../videos/whue9_YquGA.md)
`whue9_YquGA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: enterprise-adoption, multi-agent, pr-code-review

Angie Jones (Block) describes moving a 3,500-person engineering org to autonomous agent delegation via a maturity model, a power-user champions program, AI-ready repos, and an orchestrator.

- Techniques: Stage-based maturity model for agent use; Champions program of hand-picked power users; Layered repo context files; Delegation from the tools people already use; Review agent plus auto-fix loop; Isolated cloud workspace per agent; Machine-readable system map for orchestration
- Tools: Claude Code, Goose, Codex, BuilderBot, GitHub, Jira, Linear, Slack, MCP, AGENTS.md, CLAUDE.md

## [From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](../videos/GdvKNwMcfd0.md)
`GdvKNwMcfd0` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: coding-agents, context-engineering, multi-agent

Microsoft's Chris Noring on moving from writing code to running agents: start in the CLI, use AGENTS.md, skills and custom agents as guardrails, and delegate background work that comes back as draft PRs for human review.

- Techniques: Layered repo guardrails (AGENTS.md, skills, custom agents); Tools allowlist to constrain an agent; Delegate to a background cloud agent that returns a draft PR; Parallel terminals as a scaling model; Ask the agent to write its own skill or instructions
- Tools: GitHub Copilot CLI, Claude Code, Claude Desktop, VS Code, GitHub Copilot cloud agent, GitHub MCP server, Playwright MCP, AGENTS.md, SKILL.md skills, custom agents (.github/agents)

## [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](../videos/pSto5YaNGUo.md)
`pSto5YaNGUo` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: evals, observability, agent-architecture

Mutagent's CEO and CTO argue agents should be built and improved in an agentic loop: an offline eval-and-optimize loop plus an online trace-diagnose loop, with a demo of their research-preview evaluator and diagnose agents.

- Techniques: Spec-first agent definition; Eval-driven development as TDD for agents; Binary criteria with calibrated LLM judges; Trajectory-level evaluation; Failure-mode library with code-checkable indicators; Tiered trace sampling; Auto-research style optimization gated by evals; Orchestrator dispatching evaluator and diagnose subagents from a coding harness; Diagnostic report with assumptions block and human decisions
- Tools: Claude Code, Codex, Deep Agents (mentioned as a framework), Hermes (mentioned as a framework), Whisper Flow (speech-to-text for feedback), Tracing platform (auto-caption reads 'length use'; name unclear)

## [How Autoresearch is changing ML research — Zhengyao Jiang, Weco](../videos/iCj_ATyThvc.md)
`iCj_ATyThvc` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, models-research

Weco's Zhengyao Jiang on AIDE, an autoresearch agent whose PRs won OpenAI's ParameterGolf and got reused by others; humans design the eval and code abstraction while the agent executes.

- Techniques: Publish-gated agent output; Strict eval API that separates held-out data; Recombine community ideas with the agent's own changes; Constraint-driven follow-up move
- Tools: AIDE (Weco's autoresearch agent), H100 GPU node, Quantization, Qwen gated attention (paper idea)

## ["The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic](../videos/n97BCfyFIvw.md)
`n97BCfyFIvw` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: governance-compliance, pr-code-review, product-ux

Addy Osmani argues engineers are defined by owning the verdict on agent work: choosing what is worth doing, backing it with evidence, and accepting accountability. Keep humans at the highest-leverage checkpoint.

- Techniques: Inner loop / outer loop split; Evidence bundle as the review unit; Explain-it-or-don't-ship gate with named owners; Review as a control system for long runs; Move verification into the harness; Clean code for agents as well as humans
- Tools: Git

## [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](../videos/so9l_MwS2yg.md)
`so9l_MwS2yg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: claude-code, testing-verification, skills-self-improvement

Zack Proser (WorkOS) argues human attention, not agent capacity, is the bottleneck, and shares remote Claude Code from a phone, verification gates, and session-log mining to protect focus.

- Techniques: Three-tier verification ladder for agent output; Closed-loop ticket fixing with explicit done criteria; Remote-controlled session from a phone; Scheduled session-log retrospective; Ticket-tagged overnight agent loop; Parallel large features with worktrees and agent teams; Voice-first brainstorm, then written artifact
- Tools: Claude Code, Claude Opus 4.6, Slack MCP, Linear MCP, GitHub Mobile, Cursor, Codex, Vercel bot, OpenClaw, Twilio, ChatGPT advanced voice mode, git worktrees

## [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../videos/pmoDeA3RBZY.md)
`pmoDeA3RBZY` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: multi-agent, coding-agents, skills-self-improvement

OpenClaw maintainer Vincent Koc on running dozens of parallel coding agents as a "dark factory": swim lanes, opinionated loops, a big plugin refactor, and token efficiency over token maxing.

- Techniques: Swim-lane parallel agents; Big refactor gated by existing tests; Plugin split for blast-radius control; One clone per session instead of worktrees; Explanation quality as a health check; Skill improvement from session logs; Embedding graph for backlog dedupe; Synthetic plus real fake-chat eval harness
- Tools: Codex, Git worktrees, GitHub, Discord, Slack, MS Teams, Docker, GEPA, skills.sh, OpenClaw, NemoClaw, vector embeddings

## [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](../videos/zMiSRliEzv4.md)
`zMiSRliEzv4` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: agent-architecture, evals, observability

PostHog's Joshua Snyder describes a pipeline that turns product signals (errors, replays, Slack, experiments) into grouped reports, runs a Claude Agent SDK research agent in sandboxes, and opens PRs that are iterated until green.

- Techniques: Generate queries from a signal, then embed the queries; Safety classifier at the ingestion edge; Weighted report promotion with a threshold; Three-way actionability gate; Snapshot and rehydrate the sandbox for CI and review loops; Distill repeated agent behavior into a one-shot call; Evaluate on production-representative data
- Tools: Claude Agent SDK, Modal, MCP, Linear, Notion, Sentry, git blame, PostHog, feature flags

## [The Missing Primitive for Agent Swarms — Lou Bichard, Ona](../videos/5Sui_OnSRlY.md)
`5Sui_OnSRlY` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: multi-agent, sandboxing-execution, agent-architecture

Ona's field CTO argues that runtimes, orchestration and triggers are largely solved for coding-agent swarms, and that agent coordination is the missing primitive. He proposes state-machine workflows packaged as a CLI that runs locally and in CI.

- Techniques: Parent-child sub-agents with scoped context; Two-tier sub-agent placement; Fleet fan-out with prompts and scripts as a workflow; Harness engineering loop; Gated micro-step workflow (state machine); CLI-packaged workflow gate
- Tools: Ona dev environments, GitHub, Linear, Symphony, ACP, ACPX, Fabro, n8n-style graph workflows, backgroundagents.com

## [Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline](../videos/yUmS-F9IX90.md)
`yUmS-F9IX90` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: agent-architecture, coding-agents, context-engineering

Ara Khan (Cline) argues for four maturity levels of agent building: framework, hand-built state machine, Kanban as the UX, and cloud execution. Core warnings: keep prompts minimal, keep agents CLI-testable, and keep architecture human-owned.

- Techniques: Agent as explicit state machine; Prune the system prompt on every change; CLI-first agent interface for agent-driven development; Exact reasoning-trace round-tripping; Kanban board as the multi-agent control surface; Per-task cloud agent dispatch; Human-owned architecture before code generation
- Tools: Claude Code, Codex, Cursor, Factory, Cline, LangChain, LangGraph, OpenRouter, Linear, AGENTS.md, VS Code

## [Harness Engineering: The Missing Layer for AI Coding Agents (Archon)](../videos/-1BOhPOcEb8.md)
`-1BOhPOcEb8` · Better Stack · 2026-06-02 · q2 · intro · review · also: agent-architecture, coding-agents

Better Stack demos Archon, an open-source harness that defines coding-agent work as YAML workflows with fixed and AI steps, runs each job in its own git worktree, and auto-loads skills, aiming for repeatable, conflict-free parallel runs.

- Techniques: Process-as-YAML DAG with mixed step types; Per-run git worktree isolation; Skills as on-demand context; Local setup flow shown in the video (no exact commands on screen)
- Tools: Archon, ArchonServe (Archon local UI), Claude Code, Cursor, Codex, LangChain, Agent Skills, git worktree, YAML

## [Why OpenAI Built Symphony and Gave It Away for Free](../videos/n8qDKMPpLXc.md)
`n8qDKMPpLXc` · Better Stack · 2026-06-02 · q3 · intro · review · also: agent-architecture, multi-agent, coding-agents

Better Stack walkthrough of OpenAI's open-source Symphony, which polls Linear for issues and runs a coding agent per issue, with humans involved only at review. Covers setup, workflow file and hooks.

- Techniques: Tracker-driven agent dispatch; Workflow file with YAML front matter plus a per-issue prompt; Clone-and-branch after-create hook, commit-push-PR after-run hook; Spec-driven self-implementation
- Tools: Symphony (OpenAI, open-source orchestrator), Linear (issue tracker), Codex CLI (OpenAI coding agent), GPT-5.5 (model, used at low effort for spec-generated build), Elixir (language for the manual install route), TypeScript and Bun (demo app), Python (spec-generated Symphony version), Go with Charm CLI (community Symphony version), Claude SDK (community Symphony version), uv (Python tool; speaker says OpenAI acquired it, not verified in video), Multica (agent orchestration product, compared), Conductor (agent orchestration product, compared)

## [What Happens When AI Coding Gets a Delivery Pipeline (Routa)](../videos/_16PhraFYjQ.md)
`_16PhraFYjQ` · Better Stack · 2026-06-02 · q3 · intro · review · also: coding-agents, multi-agent, pr-code-review

Walkthrough of Routa, a free, local-first, open-source Kanban desktop app that runs AI coding agents through backlog, dev, and review lanes with evidence and gates instead of one chat thread.

- Techniques: Lane-per-stage agent pipeline; Evidence-backed review gates; Per-task traceability; Self-hosted setup
- Tools: Routa (open-source AI coding delivery tool; spelled Ruta in captions, Routa in the title; desktop app and Docker Compose), OpenCode (agent runtime used for the agents), Anthropic API / Claude (model provider via synced API key), MCP (Model Context Protocol, supported for agent connections), ACP (Agent Client Protocol, supported for agent connections), Docker Compose (self-hosting path), Cursor (chat-first comparison), Claude Code (chat-first comparison), CrewAI (agent framework comparison), LangGraph (agent framework comparison; spelled LaneGraph in captions)

## [Agents Don't Do Standups: Building the Post-Engineer Engineering Org — Mike Spitz, PFF](../videos/VMemhtlsoNk.md)
`VMemhtlsoNk` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: enterprise-adoption, testing-verification, context-engineering

Mike Spitz (PFF) reports a Jan–Mar 2026 case study where agent-driven spec, design doc, ticket and PR flow cut delivery time and dropped Scrum for a 20-engineer team.

- Techniques: Agent-interviewed spec then skill-generated LDD; Auto-generated, non-blocking tickets and PR-driven status; Agent code review limited to opinion-level nits; Post-staging QA agent against acceptance criteria; Composable per-step skills for the delivery lifecycle; Customer survey as the primary retro signal; Phased, non-critical-first rollout
- Tools: Claude Code, Claude Opus, Codex

## [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](../videos/ow1we5PzK-o.md)
`ow1we5PzK-o` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: multi-agent, agent-architecture, testing-verification

Luke Alvoeiro (Factory) on "Missions", a multi-agent system that runs for hours or days by combining delegation, creator/verifier, broadcast and negotiation, with a validation contract written before any code.

- Techniques: Validation contract written at planning time; Fresh-context adversarial validators; Structured worker handoffs; Serial features with read-only parallelism; Per-role model choice; Milestone-based negotiation; Orchestration as prompts and skills
- Tools: Factory Droid (open source Goose lineage mentioned), AGENTS.md, skills, computer use (for user-testing validator), prompt caching

## [Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick](../videos/2TLXsxkz0zI.md)
`2TLXsxkz0zI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: coding-agents, agent-architecture, context-engineering

Chris Parsons runs a live workshop on Ralph loops: re-running Claude Code on fresh context until work ships, fed by ticket files, a sequential queue, and reversibility limits on unattended agents.

- Techniques: Bash while-loop over fresh Claude sessions; Next-most-important-ticket selection over flat markdown tickets; Recovery check for mid-flight work; Reversibility gate with stop-and-report; Fresh-subagent adversarial review; Claude /loop for timed repetition; Resume a project in an interactive session; Simulated audience personas run in parallel subagents; Nightly session digest
- Tools: Claude Code, Codex, Cursor, n8n, Docker Sandbox, Playwright, Obsidian, Lian (embeddings CLI), Beads, Linear, Jira, Telegram

## [CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner](../videos/VktrqzQgytY.md)
`VktrqzQgytY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: pr-code-review, sandboxing-execution, multi-agent

Talk arguing CI/CD was built for human-paced PRs and breaks under agent volume; proposes spec-driven agent loops with in-loop validation, a pre-merge queue, and stateful compute.

- Techniques: Spec-first agent loop with a known-commit start; External review agents inside the loop; Pre-merge queue for serializable commits; Approve intent and evidence, not diffs; Stateful, incremental execution environments
- Tools: GitHub Actions, Claude Code, Amp, Cursor, Factory, GitHub Copilot, Namespace

## [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](../videos/W76woOYHlvY.md)
`W76woOYHlvY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: coding-agents, product-ux, agent-architecture

Louis Knight-Webb (Vibe Kanban) argues engineers will mostly plan and review as agents run longer, then live-demos shutting his company down through the tool.

- Techniques: Task-type mode selection; Clarifying-question planning; Parallel agent workspaces; PR comment shepherding
- Tools: Vibe Kanban, Claude Code, Codex, Cursor, GitHub Copilot, Playwright MCP, GitHub, Cloudflare CDN

## [Full Walkthrough: Workflow for AI Coding — Matt Pocock](../videos/-QFHIoCo-Ko.md)
`-QFHIoCo-Ko` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, testing-verification, multi-agent

Matt Pocock's live workshop on an AI coding workflow: grill-me alignment, PRD, vertical-slice issues with blocking edges, AFK Ralph loops with TDD and feedback loops, and deep-module codebases.

- Techniques: Smart-zone sizing and clear-over-compact; Grill-me alignment skill; Destination doc plus journey issues; Ralph loop (sequential AFK runner); Red-green-refactor TDD for agents; Self-review in a fresh context; Interface-first deep modules with grey-box delegation; Push vs pull for coding standards; Sandcastle-style parallel runs; Delete plans and PRDs after they ship
- Tools: Claude Code, Sandcastle, Docker, TypeScript, GitHub Issues, TLDraw, Slido, Playwright MCP, Sonnet, Opus, Spec Kit, OpenSpec

## [Building your own software factory — Eric Zakariasson, Cursor](../videos/rnDm57Py54A.md)
`rnDm57Py54A` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: context-engineering, testing-verification, coding-agents

Cursor engineer Eric Zakariasson on building a "software factory": how to structure repos, grow rules from observed failures, make agents verify their own work, and automate the human loops. Practical, with a product pitch.

- Techniques: Failure-driven rule growth; Reviewer bot enforces house conventions the model lacks; Self-verification with e2e tests and recorded runs; Scoped, parallel async tasks with front-loaded specs; Per-agent VM with a single dev command; Agentic code owners with risk tiering; Loop and stall detection for background agents; Event-triggered cleanup agents
- Tools: Cursor, Cursor cloud agents, BugBot, Playwright, AGENTS.md, Linear, Slack, GitHub, Datadog, Notion, MCP, Cursor workers

## [GitHub Was NOT Made for AI Agents (So Cloudflare Built Their Own)](../videos/PWj6GnTUBnk.md)
`PWj6GnTUBnk` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: agent-architecture, sandboxing-execution, dev-tools

Walkthrough of Cloudflare Artifacts, a Git-compatible repo store on Durable Objects built for agents, with a fork-per-task demo the speaker could not run because the product is in private beta.

- Techniques: Fork-per-task repo workspaces; Git-backed agent tools: read, write, commit (commit also pushes); Durable Object SQLite as the persistence layer for agent repos; Verification loop idea: run the agent's changed code in a sandbox, and check front-end work in a browser; Reconstructing a diff without git diff
- Tools: Cloudflare Artifacts (private beta), Cloudflare Workers, Cloudflare Durable Objects, Cloudflare Dynamic Workers, Cloudflare Sandboxes, Cloudflare Browser (Puppeteer), Wrangler (wrangler.jsonc / wrangler.toml bindings), isomorphic-git, Zig (compiled to WASM), Anthropic SDK, Git protocol, S3 Files

## [I Let 30 AI Agents Loose in My Repo (Gas Town)](../videos/_mrMidIwCzk.md)
`_mrMidIwCzk` · Better Stack · 2026-03-02 · q2 · intro · review · also: multi-agent, coding-agents

A Better Stack walkthrough of Gastown, an open-source orchestrator that runs many Claude Code agents in parallel on one feature, shown on a Go to-do app with a single prompt and a candid look at the costs.

- Techniques: Mayor-decomposed parallel feature build; Git-backed orchestration state for crash recovery; Verify parallel agent output by diff and running the app
- Tools: Gastown, Claude Code, Go, SQLite, Docker, Homebrew, JWT, GitHub

## [GitHub Actions are DEAD. (Use Agentic Workflows instead)](../videos/-DXkF2Q69Jw.md)
`-DXkF2Q69Jw` · Better Stack · 2026-03-02 · q2 · intro · tutorial · also: pr-code-review, security-guardrails

Walkthrough of GitHub Agentic Workflows: write a natural-language agent.md, compile it to a locked-down Actions workflow, and use it as a PR audit bot. Research prototype, one demo.

- Techniques: Natural-language agent file compiled into an Actions workflow; PR-triggered read-only audit agent with a structured output format; Gated write path for agent actions
- Tools: GitHub Agentic Workflows, ghaw (compile CLI), GitHub Actions, GitHub CLI (gh extension), GitHub Copilot (engine), GitHub Next, Microsoft Research, Better Stack AI SRE (sponsor plug)

## [How AI Will Transform DevOps and SRE Practices | Better Stack Podcast Ep. 12](../videos/K7y8ZAHQYGY.md)
`K7y8ZAHQYGY` · Better Stack · 2026-03-02 · q3 · practitioner · interview · also: observability, dev-tools

Better Stack podcast with SRE consultant Amin Astani on how AI-written code floods CI/CD and on-call, arguing for SLOs, constrained automation and reliability incentives over AI-run production changes.

- Techniques: Error-budget decision test for SLO maturity; Compensatory automation split for production changes; Agentic first-pass alert triage with human escalation; Release-path check before scaling AI code output; Postmortem framing beyond human error; Operational excellence in performance criteria; Self-hosted CI with Concourse
- Tools: Kubernetes, Prometheus, OpenTelemetry, Claude Code (captioned as 'Cloud Code'), incident.io, Honeycomb, Scuba (Meta internal observability tool), Conveyor (Meta internal CD system), Concourse CI, Jenkins, GitHub, Nagios

## [OpenClaw Use Cases That Are Actually Insane](../videos/hp7n45JqvIw.md)
`hp7n45JqvIw` · AI LABS · 2026-03-02 · q2 · practitioner · review · also: agent-architecture, coding-agents

AI LABS walks through weeks of running OpenClaw on a Mac Mini for developer ops: dependency upgrades, cost and uptime monitoring, SEO checks, PRD-to-deploy builds, cold-email drafts and Claude Code delegation.

- Techniques: Guideline-driven dependency upgrade cron; Scheduled research briefing; Cost watchdog skill; Hosted-app heartbeat monitor; SEO heartbeat; PRD-to-deployed-app run; Delegate to Claude Code with subtasks and per-step commits; Draft-only cold outreach via cron; Email triage heartbeat
- Tools: OpenClaw, Claude Code, Codex, Gemini 3, Nano Banana Pro (Google image-generation skill, bundled with OpenClaw), Nano Banana (earlier skill referenced), GOG CLI, Google Workspace CLI, Google Cloud console, AWS CloudWatch, Vercel, GitHub

## [Cloudflare Just Destroyed v0, Lovable, and Replit in One Move](../videos/pDnpIkbJwN4.md)
`pDnpIkbJwN4` · Better Stack · 2026-01-02 · q2 · intro · review · also: vibe-coding-app-building, sandboxing-execution

Better Stack walkthrough of Cloudflare's open-source Vibe SDK: a self-hostable, MIT-licensed prompt-to-app platform that generates, previews and deploys full-stack apps on Cloudflare's edge. Mostly a demo and deploy checklist, with thin evidence behind the comparison claims.

- Techniques: Self-host Vibe SDK on Cloudflare via the Deploy button; Blueprint-first, phased app generation; Iterate by describing the bug in chat; Route all model calls through an AI gateway with caching
- Tools: Cloudflare Vibe SDK (open-source, MIT, self-hostable), Cloudflare Workers, Cloudflare Workers for Platforms, Cloudflare AI Gateway, Cloudflare sandbox containers, Google Gemini API (default model key), Bun (package install), GitHub (clone, export target), Replit (comparison), Cursor (comparison), Vercel (comparison), v0 (comparison)

## [These Factory AI Droids Built My App in 10 Minutes! (Rust + TypeScript!) 👉 Code, Debug & Ship Apps](../videos/4ZYxlTPX-LM.md)
`4ZYxlTPX-LM` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, multi-agent

A hands-on tour of Factory's "droids" (role-specialized coding agents) building a Tauri desktop chat app, covering local bridge setup, command approval, and a model-switch debug. Thin on depth; the title overstates it.

- Techniques: Role-split agent team; Paired local bridge for hosted agents; Pre-approved command checklist with per-command risk prompts; Live file-diff preview during agent edits; Model-swap triage for a model-dependent bug
- Tools: Factory Droids, Factory Bridge (desktop app), Tauri, Rust, TypeScript, OpenAI API, GPT-4, Gemini 2.5 Pro, Notion (integration named), Jira (integration named), Linear (integration named)

## [This $8/hr AI Engineer Could Replace Junior Devs | Devin AI | Agentic Developer.](../videos/rfWx5zB0Cws.md)
`rfWx5zB0Cws` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, security-guardrails

AI LABS walks through Devin's general availability: Slack/GitHub-driven autonomous coding, a self-QA demo, a $500/month plan the narrator converts to about $8/hour, and a live-share security leak. Mostly demo and hype, few hard numbers.

- Techniques: Assign work from Slack, get progress in-thread; Agent-driven E2E QA on every push; Bootstrap an unfamiliar repo by fix-and-run loop; Sign-up sequence to start a Devin account
- Tools: Devin (Cognition), Slack, GitHub, VS Code Live Share, Rust documentation (consulted by the agent), SWE-bench (vendor-reported results), o1-preview (comparison model, named in video), Cursor (mentioned in others' takes)

## [TMUX Coding Is INSANE... Upgrade Your Claude Code Workflow](../videos/UgHbHqg_Wmo.md)
`UgHbHqg_Wmo` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: multi-agent, claude-code

Walkthrough of a tmux-based orchestrator that lets one Claude Code agent spawn and manage several Claude Code teams via scheduled check-ins, spec-driven phases, and a skip-permissions setting. Useful pattern, but the live demo never ran.

- Techniques: tmux-based agent orchestrator setup; Fix hard-coded paths and permission command in the orchestrator; Spec folder as the build blueprint; Team start prompt pattern; Scheduled check-ins with restore-point commits; Summarize an unfamiliar repo with GitIngest
- Tools: tmux, Claude Code, tmuxorchestrator (repo name as spoken), Cursor (used only to show the folder structure on screen), shadcn, shadcn MCP, GitIngest (gitingest.com), ChatGPT (mentioned as a comparison for the summary step), Git (version control and restore-point commits)

## [Is This The Future of Vibe Coding? (Vibe Kanban)](../videos/NKkO8JL6IJg.md)
`NKkO8JL6IJg` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, vibe-coding-app-building

Better Stack walkthrough of Vibe Kanban, a free open-source board that assigns tasks to coding agents, runs them in parallel and sends their diffs to review; the setup is clear, but the depth is thin and the demo shows bugs.

- Techniques: Kanban as a dispatcher for parallel agent tasks; Setup via npx and the in-app flow; Per-task agent and base-branch selection; Human review gate before merge
- Tools: Vibe Kanban (npx vibe-kanban), Claude Code, Amp, Gemini CLI, OpenCode, Codex (transcript shows 'echo', likely Codex), VS Code, GitHub, Nuxt, Tailwind CSS, MCP servers (configurable in the app)

## [Task Master AI Has Changed How I Code FOREVER (w/ Claude Code)](../videos/1I73OFAnvdg.md)
`1I73OFAnvdg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: claude-code, coding-agents, context-engineering

Better Stack walkthrough of Task Master AI with Claude Code: a PRD is parsed into dependency-tracked tasks, scored for complexity, expanded into subtasks, then run one at a time. The demo app built in one pass, but the claims rest on one example.

- Techniques: Pick models per Task Master role; Have the model write the PRD from an example template; Parse the PRD into tasks, then score complexity and expand the hardest tasks; Drive the work loop by task status; Keep project hooks in the loop
- Tools: Task Master AI (taskmaster / task-master-ai), Claude Code, Claude Sonnet, Claude Opus, OpenAI API, Next.js, IndexedDB, MCP (mcp.json), fish shell, Git, bun, npm

## [Amazon's NEW AI IDE is Actually Different (in a good way!) – Kiro](../videos/Z9fUPyowRLI.md)
`Z9fUPyowRLI` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, context-engineering

Walkthrough of Amazon's Kiro, a VS Code fork built around spec-driven development (requirements, design, tasks gated by the human) and event-driven agent hooks saved in the repo.

- Techniques: Staged spec gate before implementation; Spec re-sync after manual edits; Event-driven hook for doc or test upkeep; Steering documents
- Tools: Kiro, VS Code, Claude (Sonnet 3.7 and 4 model options), Cursor (comparison only), React, TypeScript, tRPC, Mermaid, Storybook, MCP servers, GitHub, Google login

## [GitHub Copilot Agent Mode & Project Padawan – A Game Changer?](../videos/y3oo7MGo1DA.md)
`y3oo7MGo1DA` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents

Hands-on walkthrough of GitHub Copilot agent mode and Edits in VS Code, plus a teaser for Project Padawan; the agent runs terminal commands but missed errors and ignored the screenshot, while Claude output matched the target better.

- Techniques: Agent mode for scaffold-and-run tasks; Screenshot as design reference, with a model check; Edits mode with voice input (speaker's caveat); Reviewing edits with diff and undo; Issue-to-PR flow (Padawan, not shown)
- Tools: GitHub Copilot, VS Code, Copilot Agent mode, Copilot Edits, Project Padawan, Cursor, Windsurf, Devin, Claude 3.5 Sonnet, GPT-4o, Gemini 2 Flash, Next.js

## [How To Use Open AI Codex Absolute Beginners](../videos/KpZYZwaHBc0.md)
`KpZYZwaHBc0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering

Beginner walkthrough of OpenAI's Codex CLI and cloud agents: approval modes, AGENTS.md, MCP setup, role-specialized agent files, and running background tasks that end in a GitHub PR.

- Techniques: Full Access approval mode for unattended runs; Model selection by task difficulty; Compact to manage context; Generate AGENTS.md with /init; Role-specialized agent files; Build MCP config from a repo-to-text dump; Cloud task per branch with PR handoff; Plan mode before implementation; BMAD-style planning loop
- Tools: Codex CLI, Codex IDE extension, Codex cloud (ChatGPT app), GPT-5, GPT-5 Codex (Low, High), AGENTS.md, config.toml, Claude Code, Claude Desktop, Cursor, ChatGPT, GitHub

## [You Need Claude Sandboxes... 90% Faster AI Coding](../videos/xckU9n9r8Rs.md)
`xckU9n9r8Rs` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: coding-agents, multi-agent, context-engineering

Walkthrough of running BMAD-planned stories in parallel with git worktrees and one Claude Code instance per subtask, with a QA agent review loop. The 90% title claim is not backed by the numbers shown.

- Techniques: BMAD planning-first pipeline; Prompt the story generator to split stories into non-conflicting parallel subtasks; One git worktree per subtask, managed through Conductor; QA review then fix loop per story; PR per story, merged by Claude Code
- Tools: BMAD method (planning agents, Scrum Manager, dev and QA agents), Claude Code, Claude Desktop, ChatGPT, Cursor, Conductor (multi-workspace UI for parallel Claude Code runs), git worktrees, GitHub, Next.js (initialized in story 1), OutSkill (sponsor segment, not used in the demo)

## [OpenAI's NEW Cloud-based Software Engineer (Codex)](../videos/nPAXAAbU16w.md)
`nPAXAAbU16w` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, sandboxing-execution

Launch-day walkthrough of OpenAI's cloud Codex agent: parallel tasks in isolated containers, GitHub integration, AGENTS.md, and the codex-1 and codex-mini pricing.

- Techniques: Repo-level agent instructions via AGENTS.md; Configure the agent's dev environment to match local; Turn Ask-mode suggestions into Code tasks; Use a failing agent task as bug triage; Ask for verifiable evidence in every completion
- Tools: Codex (cloud agent, ChatGPT sidebar / chatgpt.com/codex), Codex CLI (mentioned as distinct), ChatGPT, GitHub (repo connection and PR creation), AGENTS.md, codex-1 (o3 variant for SWE), codex-mini-latest, o3 High (comparison baseline), SWE-bench Verified (benchmark cited), Devin (mentioned as competitor), Windsurf (mentioned as recent OpenAI purchase)

