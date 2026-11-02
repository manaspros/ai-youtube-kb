# sandboxing-execution — 113 videos

*sandboxes, code execution environments, VMs/containers for agents*

By channel: AI Engineer 70 · Kai Explains 3 · AI LABS 8 · Better Stack 32

**Synthesized guide:** [guides/sandboxing-execution.md](../guides/sandboxing-execution.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Why Docker Isn't Enough for AI Coding Agents (Openshell)](../videos/SbwckhZkPGs.md)
`SbwckhZkPGs` · Better Stack · 2026-10-29 · q4 · practitioner · review · also: security-guardrails, coding-agents

Josh from Better Stack demos NVIDIA's open-source OpenShell agent sandbox, which adds per-request, per-binary policy, supervisor-side credential injection and audit logs on top of containers, then lists its caveats.

- Techniques: Default-deny egress with live, narrow allow rules; Bind network permissions to the calling binary; Supervisor-side credential injection; Check policy diffs with a solver before applying; macOS preflight for OpenShell
- Tools: OpenShell (NVIDIA, Apache 2.0, Rust, self-hosted; ~20k GitHub stars at time of video), openshell CLI (`openshell policy update`, `openshell logs`, sandbox status, doctor), Docker / Docker Desktop, Podman, Kubernetes, Firecracker, Apple container, Anthropic sandbox runtime, E2B, Daytona, Z3 SMT solver, Landlock (Linux kernel feature)

## [How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut](../videos/Ok6QdZHCcI8.md)
`Ok6QdZHCcI8` · AI Engineer · 2026-10-29 · q4 · practitioner · talk · also: token-cost-efficiency, inference-serving, governance-compliance

Revolut's AI ops lead explains how self-hosting GLM on dedicated GPUs cut its coding-AI invoice to about a tenth, and which serving metrics and tuning levers mattered.

- Techniques: Lead-time-first AI adoption metric; Latency-led GPU capacity planning; Serving parameter sweep; Local router for multimodal fallback; Harness-agnostic OpenAI-compatible endpoint; Sandbox with per-command allow/deny rules; Compliance and telemetry baseline
- Tools: GLM (GLM 5.1 and a later GLM 5.x model; caption reads 'GLM 5.3'), GLM-5 Flash (caption reads 'Glam5G Flash'), Gemini, Claude Code, Codex, Codex app, OpenCode (caption reads 'OpenCodex'), Anthropic API, OpenAI API, OpenAI Responses API (compatible endpoints), NVIDIA B200 GPUs, Blackwell GPUs

## [Stop Giving Your Agent Tools. Give It a Sandbox - Mikyo King, Arize AI](../videos/dAoOYFx7ZYw.md)
`dAoOYFx7ZYw` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: mcp-and-tools, token-cost-efficiency, evals

Arize's Mikyo King argues agents should get a search tool plus a code sandbox instead of a large tool catalog, reporting 43% fewer tokens and 31% lower cost in their own Harbor evals, while listing open problems such as secrets, permissions, and durability.

- Techniques: Search-then-execute tool access (code mode); Bash plus CLI as the first sandbox; Hoist REST CRUD endpoints into a sandbox language; SQL as an aggregate-query escape hatch; Keep secrets out of the model's context; Signed handoff for binary artifacts; Sandboxed, multi-trial agent evals with pass@k; Trajectory-driven instruction hill-climbing
- Tools: Arize Phoenix, Harbor Framework, Claude Code, MCP, Bash, Python sandbox, SQL (text-to-SQL), SWE-bench, PyDurable (named in the talk; caption may be garbled)

## [Build Your Own Team of Managed Agents - Jack Wotherspoon, Google DeepMind](../videos/Y_p3y6zP5QE.md)
`Y_p3y6zP5QE` · AI Engineer · 2026-10-26 · q3 · intro · talk · also: multi-agent, agent-architecture, mcp-and-tools

Google DeepMind's Jack Wotherspoon demos Gemini managed agents: a cloud sandbox, harness and API in one call, with reusable environments for multi-agent handoff, credential-injecting proxies, and scheduled triggers.

- Techniques: Single-call managed agent; Chain turns with the interaction ID; Hand off work between agents via a shared environment ID; Narrow single-purpose agents with fan-out; Placeholder credentials with egress injection; Scheduled and webhook-triggered runs
- Tools: Gemini API Interactions API, Gemini managed agents, Antigravity harness, Gemini Flash, Gemini 4 Argonne (name as spoken in the talk), Google Search (built-in tool), remote MCP servers, agents.md, agent skills, GitHub, Google Drive, Google Docs

## [How to Build Financial Agents That Work Across the Web - Jay Sahnan & Arik Bird, Browserbase](../videos/DZ24Xbm9Joc.md)
`DZ24Xbm9Joc` · AI Engineer · 2026-10-25 · q2 · practitioner · review · also: voice-multimodal, data-engineering, enterprise-adoption

Browserbase engineers pitch hosted, forked "verified" Chromium plus the open-source Stagehand SDK for running browser agents at scale on finance portals, with Ramp, Bill and Stripe as case studies.

- Techniques: Accessibility-tree page compaction before the LLM call; Hybrid deterministic plus natural-language browser control; Observe, act, extract as three separate primitives; Schema-first extraction with Zod; Single code path fanned out across many sites; Keep browser processes alive between tasks; Run the agent-side browser controller next to the browser; Copy-prompt onboarding for coding agents
- Tools: Browserbase (hosted browser infrastructure), Stagehand (open-source browser-control SDK built on Playwright), Playwright, Selenium, BeautifulSoup, Chromium (forked; Browserbase's verified build), Chrome, Zod, ngrok (used to share the demo), EC2 (named as the data-center example)

## [Why Frontier Models Fail as Buy-Side Analysts - Janie Gu, Google DeepMind & Suyeol Yun, LinqAlpha](../videos/aVbRSIQO2dE.md)
`aVbRSIQO2dE` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: evals, observability, models-research

Google DeepMind's Kaggle team and LinkAlpha present why most agent benchmarks are unreliable, what Kaggle found reproducing 65 of them, and MandateBench, a buy-side analyst benchmark graded on reasoning paths.

- Techniques: Reproduce, then read every trace before trusting a score; Separate the agent under test from the grader; Log every model call and keep traces open; Measure variance with repeated runs; Pin reasoning effort explicitly for head-to-head comparisons; Rubric-based grading of a reasoning graph; What-if perturbation of key assumptions; Reconcile conflicting source figures explicitly
- Tools: Kaggle, Kaggle Benchmarks, Google DeepMind models (as evaluated), MandateBench, HuggingFace (named as a place models searched for answers), Reddit and StackOverflow (named as places models searched for answers), Heijen's Code to Video Bench (captioned name; launched last week per speaker), Octava, Quadrillion, Rehearsals (partner names as captioned)

## [Real AI Agent Attacks and What Would Have Stopped Them — Andrey Rybka, Bloomberg](../videos/5O6jLtoeKrg.md)
`5O6jLtoeKrg` · AI Engineer · 2026-10-24 · q4 · practitioner · talk · also: security-guardrails, mcp-and-tools, agent-architecture

Bloomberg's Andrey Rybka walks through real agent security incidents (sandbox escape, CRM exfiltration, hidden-text injection, DNS leaks, a dropped production database) and maps each to layered controls: identity, input defense, deterministic tool brokers, default-deny egress, and budgets that halt.

- Techniques: Rule of two (capability gating for agent workflows); Deterministic invocation broker; Default-deny egress including DNS; One identity per agent, short-lived audience-bound tokens; Delayed package ingestion; Circuit breakers and halting budgets; Memory integrity and fresh-start policy; Security requirements in the spec
- Tools: MCP (Model Context Protocol) servers, OAuth, DNS, npm, NotebookLM (transcribed as 'Notebook Alarm'; likely NotebookLM), AWS accounts and GCP projects (as isolation analogies)

## [Your Local AI Is Not as Private as You Think](../videos/3mx84MRj8lY.md)
`3mx84MRj8lY` · Kai Explains · 2026-10-22 · q4 · practitioner · talk · also: security-guardrails, local-ai

Local AI is private, but a stranger's model file can still act on your machine through chat templates, runner bugs, exposed ports and poisoned fine-tunes; the fix is to limit what the model can reach.

- Techniques: Keep the model server on loopback; reach it remotely through an encrypted tunnel or an authenticated proxy; Patch the runner before anything else; Use official or established-quantizer weights for any model with tool access; Inspect the GGUF chat template before serving a model; Keep secrets out of the agent's working directory; Split command execution from network access and log the boundary; Do not rely on hash checks or allowlists alone
- Tools: Ollama (version 0.30.6 cited mid-October 2026; the talk also says 0.240.6 at 22:33, which conflicts), LM Studio, llama.cpp / llama.cpp server, llama-cpp-python, SGLang, vLLM, Hugging Face, GGUF, Jinja, SafeTensors, pickle scan / model-scan, Tailscale

## [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](../videos/adfw3xJBx1o.md)
`adfw3xJBx1o` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: enterprise-adoption, mcp-and-tools, coding-agents

Monzo's engineers describe Agent Chip, an in-house coding agent that began as a viral Slack emoji trigger and grew into a sandboxed, MCP-gated platform building block.

- Techniques: Gateway-first MCP layer for internal tools; Isolated sandbox namespace for remote agents; Separate orchestrator from execution; Emoji-reaction prompt trigger in chat; Low-signal incident mode; Proactive impact checks on backend changes
- Tools: Agent Chip (Monzo's in-house coding agent), Slack, GitHub, Linear, MCP (internal MCP gateway server)

## [Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco](../videos/Bz1HFxQA1o8.md)
`Bz1HFxQA1o8` · AI Engineer · 2026-10-20 · q4 · practitioner · talk · also: security-guardrails, governance-compliance, enterprise-adoption

Al Chen (Cisco) on shipping AI into five major banks in weeks rather than a year: CVE remediation with agent-run exploit tests, ClickHouse cross-region DR with data-correctness checks, and keeping PII/MNPI out of LLM-judge reasoning, with showing evidence as the main lever for compliance speed.

- Techniques: Agent-driven exploit verification for CVE remediation (Harbor task); Cross-region ClickHouse DR with backup, restore and correctness checks; Split replication of IDs and metadata from core trace data for residency; Gating LLM-judge reasoning behind a sensitive-data check; Audit the judge prompt, not only the UI
- Tools: Harbor, Docker, Modal, Daytona, ClickHouse, ClickHouse backup (Altinity), Sysdig, Wiz, Prisma, NVD, CISA, MITRE CVE database

## [Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder](../videos/Wb2v9Phhnns.md)
`Wb2v9Phhnns` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: security-guardrails, governance-compliance

Coder's staff PM walks through three real AI-agent incidents (a Replit prod wipe, a Copilot-enabled bank exfiltration, the NX supply-chain attack) and argues that infrastructure controls, not smarter models, prevent them.

- Techniques: Ephemeral remote workspaces with no route to production; Per-task short-lived, narrow-scope credentials; Identity-aligned access control for AI tools; Model proxy layer; Agent sandboxing as a firewall; Externally owned audit logs with real-time alerting; Planning-only mode and automatic dev/prod DB separation; Premortem with the team
- Tools: Replit Agent, Microsoft Copilot, Nx (build tool), Coder workspaces, Claude Code, Codex

## [Your GPU Neighbor Can Hear Your Model — Branislav Brzak, Stealthium](../videos/SacJfmp33vM.md)
`SacJfmp33vM` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: security-guardrails, inference-serving

Timing alone on shared H100s leaks a neighbor's LLM: model depth, token speed and workload type, via MIG or NVLink. Mitigate with careful placement, host-side kernel monitoring, and no MIG co-location with untrusted tenants.

- Techniques: Timing probe on own memory; Frequency analysis of latency traces for model fingerprinting; Keep sensitive models off MIG slices shared with untrusted tenants; Host-side kernel-launch monitoring
- Tools: NVIDIA MIG, NVLink, NVSwitch, vLLM, speculative decoding, Qwen 8B, Llama 3 8B, DeepSeek R1 distill, GPT-OSS 20B, GLM 4.9B

## [Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire](../videos/rAUyRDOFyHU.md)
`rAUyRDOFyHU` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: enterprise-adoption, agent-architecture, evals

Flywire's engineers describe Orbit, an internal platform that runs deterministic code with small LLM steps, gated by YAML definitions, per-step permissions and human-reviewed merge requests.

- Techniques: Deterministic-first workflow with scoped LLM steps; Strict JSON output schema with targeted retry; Per-step capability allowlist declared in config; Skill first, then workflow; Isolated node evaluation with production-trace golden sets; Per-step model selection; Separate orchestration, runtime and session state
- Tools: Claude Agents SDK, Claude Code, AWS ECS Fargate, AWS Lambda microVMs, GitLab, Jira, Sentry, Slack, OpenTelemetry, MCP, YAML, Victoria (internal PaaS)

## [Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic](../videos/QSeaZ6qHyXs.md)
`QSeaZ6qHyXs` · AI Engineer · 2026-10-12 · q3 · practitioner · other · also: agent-architecture, multi-agent, evals

Anthropic presenters answer audience questions on Claude Managed Agents: YAML-as-code deployment, eval sweeps, tenant isolation via workspaces, long runs, and sub-agents for custom tools.

- Techniques: Agent definitions as YAML synced by CI; Parallel eval sweeps on new model releases; Historical-session eval dataset; Workspace-per-customer isolation; Rubric-based exit criteria for long runs; Coordinator with a custom-tool sub-agent; Per-thread session mapping for multi-user chat
- Tools: Claude Managed Agents (CMA), Anthropic CLI (transcribed as 'Ancho CLI'), Claude Code, Modal, E2B (transcribed as 'EB2'), Daytona, Slack

## [Build a Platform and Watch It Burn — Michael Forrester, Accenture & Whitney Lee, Datadog](../videos/1tpqdglI3T0.md)
`1tpqdglI3T0` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: security-guardrails, mcp-and-tools, observability

Workshop where attendees attack a Kubernetes-hosted burrito-ordering agent, then add layered infra and AI guardrails (admission, runtime, network, input/output scrubbing, MCP checks) and see which attacks each layer stops.

- Techniques: Layered guardrails across infra and AI; Input guard before the LLM call; Mid-stream output scrubbing; MCP tool description review and registry allowlists; OpenTelemetry traces for every agent turn; Kernel-level prevention for runaway processes; Agent identity and least privilege; Three-question rubric for AI in a workflow
- Tools: Kubernetes, Amazon EKS, kagent, Kyverno, Falco, Falco Talon, Tetragon, KubeArmor, Cilium, SPIFFE/SPIRE, LLM Guard, NeMo Guardrails

## [The Autonomous Computer: Infrastructure for Computer Use Agents — Ang Li, Simular](../videos/tyFPqtyOK5w.md)
`tyFPqtyOK5w` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: voice-multimodal, agent-architecture, evals

Ang Li (Simular) on computer-use agents: why reliability needs a neurosymbolic loop, where the agent writes code that is replayed, and why pass^k matters more than pass@1.

- Techniques: Neurosymbolic replay with healing; Accessibility-tree grounding with IDs; Per-step observation choice; Clarification-first prompt; Reverse-check verification of entries; Rules-first guardrail chain; Exploration swarm for changing UIs; Test-time scaling by agent count; Save-to-skill with parameters
- Tools: Simular Agent S / S2 / S3 harnesses, Simuland (open-source scripting language), Claude Code, OSWorld, OSWorld 2, Playwright, Windows 365 for agents (Microsoft), Simular cloud desktop API and CLI, GPT-4V, GPT-5, GLM 5.2

## [1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS](../videos/k72eLcYpVys.md)
`k72eLcYpVys` · AI Engineer · 2026-10-12 · q4 · practitioner · talk · also: testing-verification, mcp-and-tools

Kevin Orellana (AWS) has a coding agent fuzz-test a sandbox hosting platform with about 1,000 workflows, and shows how sandbox primitives like memory, file persistence and permissions cause failures.

- Techniques: Agent-driven fuzz testing of a sandbox platform; Results in SQLite, not markdown; Two-layer failure triage; Build a workflow suite that mirrors customer workloads
- Tools: MCP, SQLite, Amazon Bedrock AgentCore, SSH, Codex, Claude Code

## [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](../videos/YIxzNZDDy1A.md)
`YIxzNZDDy1A` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: evals, observability, coding-agents

Wolfram Ravenwolf's hands-on workshop on building a reproducible agent benchmark (Terminal-Bench via Harbor, WolfBench dashboard), arguing that one averaged score hides variance, cost and configuration choices.

- Techniques: Multi-metric leaderboard per configuration; Pin the harness and keep a fork; Sandbox per trial with bounded concurrency; Smoke-test one task before the full run; Explicit retry policy by error class; Set and record every sampling and agent setting; Trace-first debugging of surprising scores; Shareable result snapshot
- Tools: Harbor, Terminal-Bench 2.0, Terminus 2, Weights & Biases Weave, WolfBench, Inspect (UK AISI), Marimo, CoreWeave serverless sandboxes, Daytona, OpenRouter, Docker, uv

## [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](../videos/Uv0nAf_7tyU.md)
`Uv0nAf_7tyU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: agent-architecture, context-engineering, mcp-and-tools

Anthropic engineers explain how they split Claude Managed Agents into a session log, a harness "brain" and swappable sandbox "hands", then start a hands-on workshop building a first agent.

- Techniques: Brain / hands / session split; Credential-injecting egress proxy; Append-only event log with pluggable context strategy; Lazy sandbox provisioning; One container per task; Custom tools as an event round-trip
- Tools: Claude Managed Agents, Claude Platform console (quick start), Claude Code, MCP, Sonnet 4.5, Opus 4.5, Haiku, Sonnet

## [Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands](../videos/iH_wV8BbS24.md)
`iH_wV8BbS24` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: security-guardrails, coding-agents, infra-cost-scaling

Robert Brennan (OpenHands CEO) compares four ways to sandbox coding agents, from Docker on a laptop to one Kubernetes pod per session, and argues least privilege should set the blast radius.

- Techniques: Container per agent conversation with selective mounts; Least-privilege sandbox spec; Ephemeral pod per agent session; Event- or schedule-triggered cloud agents; Matching environment to job
- Tools: OpenHands, OpenHands Agent Canvas, Claude Code, Codex, Docker, Kubernetes, GitHub Actions, Cursor, GitHub Copilot, Twilio, Slack, Datadog

## [The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder](../videos/abw_m-DRi1k.md)
`abw_m-DRi1k` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: security-guardrails, observability

Coder's staff solutions engineer explains the "lethal trifecta" (private data, external communication, untrusted input) and argues for isolated remote dev environments, a logging model proxy, and a process-level agent firewall.

- Techniques: Remote isolated agent environment; Logging model proxy in front of the LLM provider; Process-level agent firewall with command denylist; Pre-baked environments as supply-chain control
- Tools: Coder, Terraform, Claude Code, Codex, OpenClaw

## [Zero Cold Starts: Serverless AI Agents on Akamai Functions — Thorsten Hans](../videos/Zf_e45GiNCE.md)
`Zf_e45GiNCE` · AI Engineer · 2026-10-11 · q3 · intro · demo · also: mcp-and-tools, infra-cost-scaling

Thorsten Hans (Akamai) demos building MCP servers and a Vercel AI SDK agent as WebAssembly apps on Spin, deployed to Akamai Functions for near-zero cold starts and global distribution.

- Techniques: Compose MCP servers from Wasm components; Snapshot a pre-initialized interpreter into the Wasm artifact; Edge-deployed agent using a Wasm framework with a remote model; Local-to-cloud parity via Spin abstractions
- Tools: Spin, WasmTime, WASI, wasmcp, Akamai Functions, StarlingMonkey, Vercel AI SDK, Ollama, MCP Inspector, SQLite, OCI registries

## [Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind](../videos/oWTEiYpxl80.md)
`oWTEiYpxl80` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · also: agent-architecture, context-engineering

Philipp Schmid (Google DeepMind) argues agents need their own managed, persistent sandbox per API call, shows Gemini Interactions and Agents APIs, and demos a remote Antigravity environment.

- Techniques: Environment snapshot as a reusable agent base; Persistent per-conversation sandbox with server-side state; Filesystem handoff between agents; File-based agent configuration; Mount sources into the sandbox
- Tools: Gemini API, Interactions API, Agents API, Google AI Studio, Antigravity agent, Gemini CLI (for agents, not a coding agent), Google Search tool, URL context tool, Nano Banana Lite, Omni Flash, Gemini TTS, Gemma

## [How I Learned to Stop Worrying and Love the Sandbox — Matt Brockman, E2B](../videos/fz6-NS7qpZc.md)
`fz6-NS7qpZc` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: infra-cost-scaling, agent-architecture

E2B engineer runs a hands-on sandbox capture-the-flag, covering resource limits, snapshot/resume, templates, lifecycle timeouts, orphan processes, and per-user sandbox assignment.

- Techniques: Snapshot-and-resume sandboxes; Warm template with processes already running; Fork a sandbox for parallel experiments; Task-scoped lifetime with a short idle timeout; Orphan process inventory and reaping; Per-user sandbox assignment map; Separate read-only and writable paths; Egress rules when secrets are present
- Tools: E2B, Firecracker, Nomad, Kubernetes, Claude Code, Codex, Python SDK, JavaScript SDK

## [How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker](../videos/ZUZVNKFSmTM.md)
`ZUZVNKFSmTM` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools

Docker engineer Jim Clark argues that agent safety comes from small, task-shaped sandboxes fed through an MCP gateway, with zero credentials inside the sandbox. The talk also pitches Docker's SBX product.

- Techniques: Role-split sandboxes for untrusted-input pipelines; Intent-scoped sandbox per task; Single MCP gateway as the policy point; Credentials held outside the sandbox; Cross App Access token exchange; Progressive tool disclosure
- Tools: Claude Code, Codex, MCP, MARP, Mermaid, Docker SBX, OpenCode, Gemini

## [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](../videos/33Oct2hqGnk.md)
`33Oct2hqGnk` · AI Engineer · 2026-10-05 · q2 · practitioner · talk · also: mcp-and-tools, agent-architecture, evals

AWS's Sandhya Subramani demos an agent that writes its own tools and sub-agents at runtime using three built-in tools (editor, shell, load-from-directory) plus a system prompt, then argues that evals and sandboxing are required before trusting it.

- Techniques: Meta-tooling bootstrap (three tools + system prompt); Check-before-write rule for generated tools; Self-repair on error; Sub-agent topology choice (swarm, graph, workflow); Layered agent evals; Four-part guardrail stack for self-modifying agents
- Tools: Strands Agents (AWS open source agent harness, Python and TypeScript), Python, OpenTelemetry (named as telemetry), Strands code-execution sandbox (recent feature, named in talk)

## [Orchestras, Not Factories: How the Fastest Builders Work — Charlie Holtz, Conductor](../videos/TRfzFJCJ7ZE.md)
`TRfzFJCJ7ZE` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: multi-agent, software-factory, coding-agents

Charlie Holtz (Conductor co-founder) lists six principles for fast agent-driven building: stay near the frontier, don't beat the market, mark slot-free zones, feed a central store, run free-range cloud agents, and orchestrate rather than run a factory.

- Techniques: Don't-beat-the-market test; Slot-free zones with CI-enforced human review; CLAUDE.md / AGENTS.md and skills as onboarding material; Central event store with a SQL tool for agents; Cloud sandboxes per task with lifecycle independent of the laptop; Agents calling the product API to create work
- Tools: Conductor, Claude Code, Codex, git worktrees, Postgres, Slack, Discord, Telegram, OpenClaw, React

## [Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI](../videos/48YUYDjwfYY.md)
`48YUYDjwfYY` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: token-cost-efficiency, infra-cost-scaling, coding-agents

Cast.ai's Kimchi team argues for routing each task to the cheapest model that still meets a quality bar, judged by cost per task, with long-running sessions kept alive in remote sandboxes.

- Techniques: Per-task cost-at-quality model comparison; Outcome-scored harness with a grade gate; Milestone-based long-run planning with up-front questions; Remote sandbox session that outlives the client; Team review board for agent sessions
- Tools: Kimchi, Ferment, Teleport, Studio, pi-mono SDK (captioned as 'PyMono SSDK'), Claude

## [An Interaction Is All You Need — Ivan Leo, Google DeepMind](../videos/8aVbXXvJUY4.md)
`8aVbXXvJUY4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: agent-architecture, security-guardrails, mcp-and-tools

Google DeepMind's Ivan Leo presents the Interactions API and Managed Agents: server-side state via interaction IDs, persistent sandboxes via environment IDs, and a credential-injecting proxy. Mostly a product walkthrough with a few reusable patterns.

- Techniques: Server-side conversation state via interaction ID; Reattach to a persistent sandbox via environment ID; Proxy-side credential injection; Freeze a tuned environment as a named agent; Local-to-cloud skill packaging; Strongly typed output parsing
- Tools: Interactions API, Managed Agents, Antigravity agent harness, Gemini API CLI, AI Studio, Google Search tool, URL context tool, GCS, GitHub

## [I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j](../videos/oUZEt4EiPbk.md)
`oUZEt4EiPbk` · AI Engineer · 2026-10-04 · q2 · intro · demo · also: memory, agent-architecture, mcp-and-tools

Neo4j's Jeremy Adams builds a personal agent on a Raspberry Pi 4B: NanoClaw in Docker, WhatsApp as the channel, cloud LLMs, and graph memory, with a live demo and an offline capture mode for conference Wi-Fi.

- Techniques: Edge orchestrator, cloud brain; Container per agent process; Messaging app as the agent front end; Graph database as an MCP tool; Offline-first capture with deterministic parsing and later sync; Typed entity memory schema written as a skill; Batch distillation of chat history
- Tools: Raspberry Pi 4B, NanoClaw, OpenClaw, Claude Agent SDK, WhatsApp, Telegram, Docker, Neo4j, Neo4j Aura, Cypher, MCP, Neo4j agent memory service

## [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](../videos/OE_lLNCNfQo.md)
`OE_lLNCNfQo` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: security-guardrails, governance-compliance

Docker's product manager argues coding agents need micro-VM sandboxes with secret placeholders and default-deny egress, and shows a self-test where Claude Code found his bank data. Mostly a product pitch.

- Techniques: Run agents in a micro-VM with bypass permissions on; Placeholder secrets swapped at the network boundary; Default-deny egress with an allowlist; Read-only mounts of context repos; Self red-teaming with real personal data
- Tools: Docker SBX, Claude Code, Claude Desktop, Codex, CrowdStrike, Cedar, Datadog

## [The Real Reason Behind NVIDIA Buying Hugging Face](../videos/s7dKx9Pl2j0.md)
`s7dKx9Pl2j0` · Kai Explains · 2026-10-02 · q3 · intro · news · also: security-guardrails, local-ai, models-research

Kai Explains argues NVIDIA's $12.9B Hugging Face deal is about the open-weights policy fight, prompted by an AI agent's sandbox escape and breach of Hugging Face, not just distribution.

- Techniques: Treat an egress proxy as an attack surface, not a containment guarantee; Use a locally run open-weight model for incident forensics when closed APIs refuse or data cannot leave; Triage agent-driven intrusion logs for machine-like signatures; Prefer non-executable weight formats, and still audit the loading pipeline
- Tools: Hugging Face Hub, OpenAI Exploit Gym (benchmark), GPT 5.6 Sol (named in the video), GLM 5.2 (open-weight model), safetensors, PyTorch Foundation, NVIDIA Base Command Manager, Bright Computing, Slurm (SchedMD), CUDA, NVIDIA open agent framework

## [From coding to Knowledge work agents — Karan Vaidya, Composio](../videos/xxfMT-bPEmU.md)
`xxfMT-bPEmU` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: governance-compliance, agent-architecture, memory

Composio CTO on why coding agents work and knowledge-work agents don't: six missing primitives (centralization, history, context, verification, governance, reversibility), enforced with walls and sandboxes rather than prompts.

- Techniques: Single connection hub for agents; Cross-app action record; Skill distillation from run logs; Pre-send style check against past outputs; Sandbox mirror of production tools; Two-layer walls: access scope plus behavior policy; Tiered gates scaled to blast radius; Undo for reversible actions, sandbox for the rest
- Tools: Composio, Claude Code, Codex, Cursor, OpenClaw, Git, Salesforce, Notion, Gmail, Slack, Zendesk, bugbot.md (named in passing)

## [Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind](../videos/fjF8EKnxKCU.md)
`fjF8EKnxKCU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, skills-self-improvement, security-guardrails

Philipp Schmid (Google DeepMind) rebuilds one GitHub PR-review agent three ways, moving from a hand-written Python loop to a hosted sandboxed harness driven by markdown files, and argues to delete orchestration code as models improve.

- Techniques: Agents-as-files layout; Bootstrap script for CLI dependencies; Credential injection through a network proxy; Single-call agent turn with server-side loop; Named custom agent; File-based memory and handoffs; Build-to-delete audit
- Tools: Gemini API, Interactions API, Antigravity (agent harness), Google Agent Development Kit (ADK), GitHub CLI (gh), Google Search tool (Gemini API), Google Cloud Storage (GCS) bucket, GitHub repositories as sandbox sources, AI Studio, LangChain Open Deep Research (case reference), Cursor (case reference, speaker says 'Curso'), Manus (case reference, speaker says 'Manos')

## [We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog](../videos/4lXks428C9o.md)
`4lXks428C9o` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: security-guardrails, coding-agents

PostHog's Sarah Sanders on securing the PostHog wizard, an agentic CLI with shell access: deterministic enforcement, scanning every content source, and an LLM used only as an advisor.

- Techniques: Deterministic gate ahead of LLM judgment; Detector separated from actor; Scan both ends of the content pipe; Rule anatomy with paired tests; Deny-by-default command allowlist with a vault; Audit for composed attacks
- Tools: YARA, Ink, MCP, PostHog wizard, Warlock, Cursor

## [Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker](../videos/zaGyGgLW3SM.md)
`zaGyGgLW3SM` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools

Docker's Tushar Jain argues agent safety, not intelligence, is the blocker, and demos a sandbox runtime with stub credentials, scoped per-task sandboxes, and an unbuilt intent-based access prototype.

- Techniques: Run the agent inside an untrusted VM boundary, with policy enforced outside it; Split a monolithic agent into per-task sandboxes; Inject stub credentials, with real secrets added outside the sandbox; Just-in-time narrowed tools over existing MCP servers; Capability escalation through an intent tool; Same policy locally and in the cloud; Parallel fan-out of scoped sandboxes
- Tools: SPX (Docker runtime; name as spoken, install via brew), Docker, Codex (OpenAI coding agent), Claude / Anthropic models, GitHub, Slack, Notion MCP, MCP, OpenClaw (spoken as open claw), OpenCode (spoken as open code), GLM 5.2 (open model)

## [Everyone Gets A Software Company — Benjamin Guo, Zo Computer](../videos/Qr15lGAGKpo.md)
`Qr15lGAGKpo` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: product-ux, agent-architecture

Zo Computer co-founder Ben Guo pitches a personal cloud server with built-in AI as a way out of SaaS silos and vendor-owned cloud agents. Mostly a product pitch, with a few ownership arguments worth noting.

- Techniques: Single personal server as the agent home; Scheduled agent automations; Agent as a gatekeeper for inbound bookings; Chat-driven site editing and hosting
- Tools: Zo Computer, Claude Code, Codex, Gemini, Claude Tag, OpenClaw, Hermes, Calendly, Squarespace

## [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](../videos/pPj_tjlvYjA.md)
`pPj_tjlvYjA` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: product-ux, testing-verification, voice-multimodal

Reelful's founder shows how an agentic video editor turns real footage into a clip: media understanding, a user-approved plan, a sandboxed agent with skills, Remotion rendering, and a verification loop.

- Techniques: Sandbox per approved job; Plan approval gate; Skills as encoded craft; Code-defined render target; Verification-then-reiterate loop; Directional templates plus manual editor fallback
- Tools: Remotion, React

## [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../videos/L173Z8DpaJg.md)
`L173Z8DpaJg` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: software-factory, pr-code-review, multi-agent

Safia Abdalla (Warp) on building the Oz cloud agent platform: hide infra complexity, allow any harness, expose everything via API, and run the open-source repo with agent-gated triage and PR review.

- Techniques: Managed plus self-hosted sandboxes behind one model; Harness-agnostic layer with platform guardrails; Orchestrator with mixed-model sub-agents; Agent-gated PR review before human review; Agent-driven issue intake; API-first primitives for agents, sub-agents, environments and artifacts
- Tools: Warp, Oz, Claude Code, Codex, GitHub, Slack

## [Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](../videos/jRCpXUjz4CI.md)
`jRCpXUjz4CI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, agent-architecture, training-finetuning-rl

Alex Shaw (Terminal-Bench, Harbor) argues agents behave like ML models, so teams should build environments (instruction, sandbox, verifier) and run parallel rollouts for evals, training data, RL and agentic map-reduce.

- Techniques: Environment as a three-part directory (instruction, sandbox, verifier); Separate rollout, trajectory capture and verification; Parallel rollouts with a fire-and-forget launch; Agentic map-reduce over agent logs; Own the eval before choosing a model; Design for agent users of your product
- Tools: Harbor, Terminal-Bench 2.1, Codex (GPT-5.5 run in the demo), Cursor CLI (map step in demo), Modal (sandbox backend in demo), Tinker (RL integration), A frontier model transcribed as 'Fable 5' (reduce step in demo; name may be a caption error), LangChain Deep Agents with sandboxes (integration)

## [How Codex Works — Dominik Kundel, OpenAI](../videos/shRR1e2HXMk.md)
`shRR1e2HXMk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: agent-architecture, coding-agents, context-engineering

OpenAI's Dominik Kundel walks through what happens when a message is sent to Codex: context assembly, sub-agents, computer use, sandboxing, auto-review, WebSocket transport, goal loops and compaction.

- Techniques: Deferred tool loading with tool search; Capping the skills list as a share of the context window; Sub-agent tool set: spawn, send input, wait, shutdown; Code-execution computer use with a persistent REPL; Auto-review sub-agent for escalated actions; Stateful WebSocket transport for agent loops; Goal loop with an explicit done tool; Server-side compaction item
- Tools: Codex, OpenAI Responses API, Codex app server, ripgrep, PowerShell, Node REPL, Chromium, Seatbelt (macOS sandbox), Bubblewrap (Linux sandbox), Cerebras (GPT-5.3 Codex Spark), Ollama, LM Studio

## [Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare](../videos/RmS5s6Wbin4.md)
`RmS5s6Wbin4` · AI Engineer · 2026-08-18 · q3 · practitioner · demo · also: vibe-coding-app-building, security-guardrails, product-ux

Kenton Varda (Cloudflare) argues personal AI codegen needs new infrastructure, and demos "Gadgets": per-user apps with platform-enforced sharing and sandboxed generated code, run on open-source workerd.

- Techniques: Platform-enforced sharing via single-purpose instances; Sandboxed generated UI with postMessage-only RPC; Give the agent the app source and a brief, let it add primitives; Export code-only templates (blueprints); Run the production runtime locally
- Tools: Cloudflare Workers, Durable Objects, Dynamic Workers, workerd, Claude, Cap'n Web RPC

## [Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs](../videos/ewtOo0scUh0.md)
`ewtOo0scUh0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, data-engineering

Bespoke Labs on curating data and RL environments for post-training: OpenThoughts and OpenThoughts-Agent recipes, counterintuitive sampling and teacher findings, and a tag-based SFT fix for numeric hallucinations.

- Techniques: Stage-wise ablation of a data curation pipeline; Multi-sample answers per question; Teacher model selection by measurement; Structural tags in fine-tuning data; Reflection-based prompt optimization
- Tools: Curator, Bespoke Stratos, OpenThoughts, Terminal-Bench, Tinker, Fireworks

## [Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)](../videos/IvE8n-ylFYY.md)
`IvE8n-ylFYY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance, agent-architecture

Steve Korshakov (Bee, acquired by Amazon) explains how an always-on personal-agent wearable keeps data unreadable even to its own company, using client-held keys, attested workloads, and two-tier release controls.

- Techniques: Client-held keys with attested key release; Forced key expiry window; Split base image and deployment manifest; Private CA for internal attestation certificates; Minimal, auditable trusted code base; Per-agent sandbox with minimal capabilities
- Tools: Sigstore-style transparency log (auto-caption reads as 'six store'), Confidential compute nodes, Private certificate authority, OpenClaw (auto-caption reads as 'open claw'), Claude Code (auto-caption reads as 'cloud code')

## [Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang](../videos/zkX03APVj0M.md)
`zkX03APVj0M` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: training-finetuning-rl, evals

Joseph Wang of Emulated argues that agent training needs realistic infra environments: multi-node sandboxes that touch real cloud resources, not single-container coding tasks.

- Techniques: Multi-node cluster simulation in one sandbox; Chained multi-deployment episodes for long horizon; Organisation context as part of the environment; Multi-node sandbox on real cloud resources (CloudBox); Choose a vertical with clear customer requirements first
- Tools: Harbor, etcd, Kubernetes, AWS Lambda

## [Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic](../videos/K0X9QDRkIdg.md)
`K0X9QDRkIdg` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, context-engineering, evals

Anthropic engineers explain how agent surfaces moved from the Messages API to Claude Managed Agents, which separates the brain from the hands, logs sessions durably, and adds vaults, dreaming and outcomes.

- Techniques: Brain/hands decoupling with on-demand sandboxes; Append-only session log as the resume point; Re-reading discarded context from the log; Vault-based credential injection; Restricted network allowlist per environment; Rubric and failure-case grader loop (outcomes); Batch dreaming over transcripts and memory; Harness-debt audit when models change
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, MCP servers, MCP tunnels, self-hosted sandboxes

## [From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize](../videos/9HbzAWnKbo4.md)
`9HbzAWnKbo4` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, software-factory, evals

Arize's founder demos Signal, a background agent that reads production traces and logs, drafts an issue or fix with evidence, and hands it to a human reviewer, with the loop run in a sandbox.

- Techniques: Trace-to-file skill; Event- or schedule-triggered agent loop; Composable narrow skills over raw data; Sandbox per run, pluggable harness; Failure-to-evaluator loop
- Tools: Arize AX, Arize Phoenix, Pyroscope, Claude Code, Cursor, Daytona, GitHub, Google Cloud logging skills

## [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](../videos/X1kp-ABIIxQ.md)
`X1kp-ABIIxQ` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, observability, evals

Dan Farrelly (Inngest CTO) argues agent architectures decay fast unless the execution layer (durable state, retries, triggers, tracing) is separated from fast-changing context (prompts, models, tools) and compute (sandboxes).

- Techniques: Three-layer decomposition (execution / context / compute); Externalised durable step state with resume-from-failure; Cron-triggered health check, triage agent, and reviewer loop; Deferred outcome scoring from downstream events; Ephemeral sandboxes with state kept in the orchestrator
- Tools: Inngest

## [From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI](../videos/Ib5t2RLtxvM.md)
`Ib5t2RLtxvM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, testing-verification, observability

Rustem Feyzkhanov (Snorkel AI) on turning production agent traces into repeatable, containerized simulation benchmarks that serve as release gates and training data.

- Techniques: Trace-to-task conversion; Harbor-style task folder; Oracle-first validation; Sidecar service mocking with a simulated user; Stepwise long-horizon simulation; Layered verifiers with SME escalation; Benchmark CI and difficulty tagging; Coverage split: happy path plus edge cases; Held-out split for agent config
- Tools: Docker, Docker Compose, Harbor (task format), Terminal-bench, SWE-bench, Arize (experiment and trace recording; transcript says 'Arise'), MCP tools

## [Every Harness Will Become A Claw — Sam Bhagwat, Mastra](../videos/8qWIPUia2O8.md)
`8qWIPUia2O8` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: agent-architecture, skills-self-improvement, product-ux

Sam Bhagwat (Mastra) argues agent harnesses will keep expanding into always-on "claws" with durability, initiative and learning, then shake out to a few winners. Mostly conceptual, with little hard data.

- Techniques: Durable turn streaming with resume; Queue, steer and interrupt on running threads; Session-scoped tool approval; Heartbeat wake-ups; Trace-driven continual learning; Cloud sandbox per parallel subagent
- Tools: Mastra, Claude Code, Codex, OpenClaw, Hermes Agent, Slack, Telegram, WhatsApp, GitHub

## [Multiplayer agentic engineering — Arjun Singh, Superconductor](../videos/OL7kfezynJM.md)
`OL7kfezynJM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: software-factory, coding-agents

Arjun Singh (Superconductor) on making agent work multiplayer: one shared session across Slack, desktop, mobile and GitHub, cloud sandboxes, and benchmarking agents on your own codebase.

- Techniques: Cloud sandbox per project; Same session across interfaces; Artifacts as proof of work; Meeting bot as an idea-to-ticket intake; Acceptance-criteria fields in the ticket form; Network egress allowlist with grant prompts; Scoped credentials instead of ambient access; Codebase-specific agent benchmark; Switch defaults on evidence
- Tools: Claude Code, Codex, Cursor, Slack, GitHub, Linear, Sentry, Notion, Google Meet, Zoom, Microsoft Teams, GLM 5.2

## [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../videos/iQ5xldZ9StU.md)
`iQ5xldZ9StU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: software-factory, security-guardrails, coding-agents

GitHub Next demos Agentic Workflows (markdown playbooks compiled to Actions with deterministic guardrails) and ACE, a cloud multiplayer dev environment where humans and agents share chat and plans.

- Techniques: Markdown playbook compiled to CI workflow; Declarative guardrail front matter; Secret brokering outside the agent sandbox; Staged, logged writes; Swarm of role-specific workflows; Shared cloud session per branch with team chat as context; Shared markdown plan as contract; Automation triage by stack trace origin
- Tools: GitHub Copilot, GitHub Actions, Dependabot, Astro, Cloudflare, ACE (GitHub Next prototype)

## [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](../videos/LqLoYksJ6do.md)
`LqLoYksJ6do` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: security-guardrails, software-factory

Form3's Moritz Johner describes PatchPilot, an agent that patches CVEs across thousands of repos, and why production credentials make a coding agent a supply-chain actor needing deterministic controls, credential splits, and microVM isolation.

- Techniques: Deterministic controller plus scoped agent steps; Minimal change-set instruction plus post-agent vetting; Bounded CI-fix loop with human escalation; End-of-run retrospective aggregated across runs; Planted-injection end-to-end tests as evals; MicroVM sandbox with a policed egress path
- Tools: PatchPilot, Dependabot, Renovate, Firecracker, Docker, Kaniko, BuildKit, Landlock, bubblewrap, Go, Slack, GitHub

## [I Let Strix Attack My App... Here’s What It Found](../videos/vRTliPb8fjg.md)
`vRTliPb8fjg` · Better Stack · 2026-08-02 · q3 · intro · review · also: security-guardrails, pr-code-review

Short Better Stack review of Strix, an open-source multi-agent pen-testing tool that attacks a web app or API in a Docker sandbox and returns validated exploits and fix PRs, with real limits on cost, speed and complex attacks.

- Techniques: Scan code and live target together in one run; CI merge gate on validated findings; Triage on proof, not on maybes; Match model strength to scan depth and budget
- Tools: Strix, Docker, Anthropic API (Claude), Gemini, Ollama, GitHub Actions, FastAPI (demo app), XBEN exploitation benchmark, OWASP Top 10

## [WebAssembly 3.0: It's Not Just for Browsers Anymore](../videos/McB108-FExg.md)
`McB108-FExg` · Kai Explains · 2026-08-02 · q3 · intro · news · also: infra-cost-scaling, dev-tools

Kai Explains argues WebAssembly 3.0 (component model plus WASI) makes Wasm a cross-language, server and edge runtime, while JavaScript keeps the DOM and is not being replaced.

- Techniques: Polyglot components via the component model; Wasm instead of containers for short-lived edge or per-request execution; Split UI from logic across the JS/Wasm boundary
- Tools: WebAssembly 3.0, Wasm component model, WASI, Spin framework, Cloudflare Workers, Fastly Compute, Docker, Chrome DevTools, npm, React, Figma, Photoshop

## [AI Can Do the Work, But It Can't Do the Understanding | Better Stack Podcast Ep. 18](../videos/nfX_SQYDoBI.md)
`nfX_SQYDoBI` · Better Stack · 2026-08-02 · q3 · practitioner · interview · also: data-engineering, token-cost-efficiency, enterprise-adoption

Better Stack podcast with Marimo's Vincent on why AI can produce code and analysis but not understanding: keep humans in the loop, care about the code, and be wary of hype.

- Techniques: Notebook scratchpad for LLM introspection; Incremental cell generation with a human in the loop; Scrubbable numeric literals for live tuning; Per-tool-call allow/deny for agent sandboxes; AnyWidget for browser-side widgets in Python notebooks; Shuffle test before trusting an A/B harness; Hypothesis-free first pass on a dataset; Supply-chain surface reduction for Python; Measure LLM agreement before automating a decision; Write flashcards yourself
- Tools: Marimo (Python notebook), Molab (Marimo notebooks with GPU), Google Colab, Jupyter, Observable, AnyWidget, Polars, NumPy, scikit-learn, spaCy, D3, Lua

## [AI Benchmarks Are Fake!?](../videos/pHAbwL7w83Q.md)
`pHAbwL7w83Q` · Better Stack · 2026-08-02 · q3 · practitioner · news · also: evals, models-research

Short explainer on two ways AI coding benchmarks get gamed: agents retrieving fix commits and models memorizing test sets. It relays Cursor's strict-environment results and contamination studies, with concrete numbers and few original methods.

- Techniques: Strict-environment eval run; Trajectory audit for shortcut solutions; Original-vs-altered contamination quiz; Contamination-adjusted scoring; Parallel held-out benchmark
- Tools: SWE-Bench Pro, SWE-Bench Multilingual, DeepSWE, Frontier Code (Cognition, as captioned), GSM-8K, SST-2, Qwen 2.5, Claude Opus 4.8, GPT 5.4, GPT 5.5, Composer 2.5 (Cursor), Mythos (Anthropic, as captioned)

## [Fleet Engineering Is Insane... The Next Evolution Of Vibe Coding](../videos/qxjII6x2yPY.md)
`qxjII6x2yPY` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: multi-agent, claude-code, coding-agents

Walkthrough for running many Claude Code sessions in parallel: resume and handoff basics, file ownership, background dashboards, git worktrees, issue-driven orchestration, and Docker Sandbox isolation.

- Techniques: Session recovery with continue, resume, recap, export; File ownership by prompt; Plan-mode task decomposition; Handoff documents via the handoff skill; Background sessions and the agent dashboard; Git worktrees per session; Issue-driven background orchestration; Docker Sandbox for isolated execution with clone mode
- Tools: Claude Code, Claude Code plan mode, Claude Code background sessions, Claude Code agent dashboard, handoff skill, git worktrees, OpenAI Symphony, Codex, Linear, GitHub, Docker Sandbox (sbx), Docker micro-VM sandboxes

## [OpenAI Went Rogue and Hacked Hugging Face](../videos/iUkgp7kzIxM.md)
`iUkgp7kzIxM` · Better Stack · 2026-08-02 · q3 · intro · news · also: security-guardrails, observability

Better Stack news recap of the Hugging Face intrusion that OpenAI said came from its unreleased model escaping an internal cyber eval, plus HF's AI-assisted forensics and practical takeaways.

- Techniques: Lock down the eval egress path; Run cyber evals with classifiers off, but isolated; LLM triage over security telemetry; Self-host an open-weight model for forensics; Credential hygiene after a platform incident
- Tools: ExploitGym (OpenAI internal cyber eval), GPT 5.6 Sol, GLM 5.2 (Z.ai open-weight model, self-hosted by Hugging Face), Hugging Face (Spaces, datasets pipeline)

## [Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua](../videos/ZSQb5fzRFPw.md)
`ZSQb5fzRFPw` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: voice-multimodal, evals, infra-cost-scaling

Cua's team presents "Computer-Use 2.0": a background computer-use driver (Cua Driver), a multi-platform benchmark (CuaBench, including a KiCad electrical-engineering set), and warm sandbox pools (CuaFleet) that cut idle GPU time in RL training.

- Techniques: Two-tier background action with fallback; Window-scoped observation; Single-file cross-platform task definition; Adversarial pre-validation of evals; Trajectory forking for world-model probes; Demand-autoscaled warm pool for sandboxes
- Tools: Cua Driver, CuaBench, CuaFleet, Codex computer-use model, TerminalBench, Harbor, Android activity framework, Hermes harness, KiCad

## [Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](../videos/4uFVSLgD2Q4.md)
`4uFVSLgD2Q4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, enterprise-adoption, evals

OpenGov's Gabe De Mesa on how they built and scaled OG Assist, an in-product agent: an in-house Effect-native agent loop, A2A contracts, approval gates, ephemeral sandboxes, and rolling-summary context.

- Techniques: Effect-native agent loop with injected language model; A2A agent card as the API contract; Deterministic approval interrupt; Automated tool-call evals in CI; Ephemeral sandbox per agent task; Rolling summary with recent-window and recall; Runtime generative UI via registered primitives; Tools to toolkits to model registration
- Tools: Effect, Effect AI, LangGraph, A2A protocol, A2UI, Claude, Cursor, Claude Cloud Agents

## [Respect The Process - Andrew Dumit, Watershed Technology Inc.](../videos/CLttOU7n6sI.md)
`CLttOU7n6sI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: governance-compliance, coding-agents, testing-verification

Andrew Dumit (Watershed) on deploying coding agents for sustainability supply-chain graph edits: constrain the effects through a typed SDK and deterministic execution, not the agent's reasoning, so the process can be validated.

- Techniques: Typed SDK as the only write path; Deterministic run executor (validate-then-commit); Review artifact instead of code review; Constrain effects, not reasoning; Eval-driven hill-climbing on the agent task
- Tools: Claude Code, TypeScript SDK, React agent (earlier version)

## [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](../videos/OqM67QG_Ikk.md)
`OqM67QG_Ikk` · AI Engineer · 2026-07-18 · q4 · deep · talk · also: security-guardrails, agent-architecture, infra-cost-scaling

A first-principles tour of why agent code needs sandboxes, comparing fork/exec, containers, gVisor and microVMs, then how to add disk snapshots, restore and multi-node scheduling for OpenAI-scale agent sandboxes.

- Techniques: Isolation ladder for untrusted tool execution; Driving a microVM through its VMM API; Per-device jailing for emulated devices; Incremental block-level disk snapshot; Acknowledge snapshot before upload completes; Tiered always-on block storage; Snapshot-aware scheduling; Startup latency hybrid
- Tools: gVisor, Firecracker, Cloud Hypervisor, CrossVM, QEMU, KVM, virtio, vsock, seccomp, VFIO, NBD, FIEMAP

## [Using LLMs to Secure Source Code — Eugene Yan, Anthropic](../videos/imFedndyXYQ.md)
`imFedndyXYQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: security-guardrails, testing-verification, multi-agent

Eugene Yan (Anthropic) walks through a six-step harness for using LLMs to find, verify, triage and patch vulnerabilities, arguing the bottleneck has moved from finding bugs to verification, triage and patching.

- Techniques: Threat model as a living context document; Isolated, reproducible PoC sandbox; Independent adversarial verifier; Tool-equipped discovery; Less prescriptive prompts for stronger models; Patch validation ladder with a generative verifier loop; Close the loop as a regression check; Severity triage as impact times likelihood with compensating controls; Code-owner routing without an LLM
- Tools: Claude, Claude Code, Docker, PostgreSQL, Redis, Jira

## [Finally, a Programmable AI Agent Framework That Works](../videos/n5cYS6KuyK8.md)
`n5cYS6KuyK8` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: agent-architecture, skills-self-improvement, token-cost-efficiency

Walkthrough of Flue, an open-source TypeScript agent-harness framework from the Astro team, showing agents, workflows, HTTP triggers and an in-memory sandbox tier that avoids booting containers.

- Techniques: Single-file agent definition; Skill-backed workflow; Local execution for skills that need files; Safer custom tool instead of local mode; HTTP-triggered workflows; Tiered sandboxes
- Tools: Flue (Flue runtime, Flue CLI, flue.config.ts, server.mjs), Pi (minimal agent harness), OpenClaw (mentioned as built on Pi), Astro, Bun, Vite, Hono, Node.js, Cloudflare Workers and Durable Objects, Cloudflare sandboxes, Vercel Just Bash, Daytona

## [Apple Just Built WSL for the Mac (Container Machines)](../videos/xXtsuDnapqc.md)
`xXtsuDnapqc` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: dev-tools

Walkthrough of Apple's new Container Machines, persistent per-container Linux VMs on macOS built on Apple's open-source container CLI, with benchmarks against OrbStack and Docker Desktop and the main caveats.

- Techniques: Build a dev machine image from a Dockerfile; Create, list and run a container machine; Use the Mac project files from inside Linux; Edit files over SSH for breakpoints and hot reload; One machine per distro target; Narrow the home mount before running untrusted code
- Tools: Apple container (Swift OCI container CLI and runtime, released last year), Apple Container Machines (persistent Linux VMs on macOS 26+), Apple Virtualization framework, Docker Desktop, OrbStack, Lima, Dockerfile / OCI images, Ubuntu 24, Alpine, Debian, Bun (bun dev server), PostgreSQL

## [Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat](../videos/F1DYkY1BlfM.md)
`F1DYkY1BlfM` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: security-guardrails, infra-cost-scaling

Red Hat's Sally Ann O'Malley runs OpenClaw agents in Podman containers, keeps API keys as secret refs, and lifts the same setup to Kubernetes; the talk is a live demo with a pitch for containers as the default agent sandbox.

- Techniques: Podman secrets + secret-ref indirection for agent API keys; Container as the agent sandbox with explicit host grants; Mount the agent's tool directory at startup; Named volume for runtime state with scheduled backup; Local-to-Kubernetes lift with the same image; Company baseline image with per-user layer; SSH sandbox for remote execution; Installer that converts env vars to secret refs and sets providers
- Tools: OpenClaw, Podman, Podman secrets, Docker, Kubernetes, OpenShift, kind, systemd, OpenRouter, Anthropic, Gemma, OpenTelemetry

## [Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman](../videos/hCMrEfPG2Yg.md)
`hCMrEfPG2Yg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: product-ux, mcp-and-tools

Ruben Casas (Postman) maps generative UI from static components to declarative JSON to runtime-generated HTML/JS, argues MCP apps are the right sandboxed delivery layer, and says collaborative canvases are the next step.

- Techniques: Declarative generative UI with a component catalog; Static client-tool to component mapping; Runtime generated HTML/CSS/JS in a sandboxed MCP app; Use MCP apps as the default delivery for generated UI
- Tools: MCP apps, AG-UI, Goose (auto visualizer), json-render (Vercel), FastMCP, Excalidraw MCP app (transcribed as ScallyDraw), Claude Visualizer, GPT-5.2, Claude Opus 4.5, React

## [Cooking with Agents in VS Code — Liam Hampton, Microsoft](../videos/dyHpnnlkTc8.md)
`dyHpnnlkTc8` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: coding-agents, multi-agent, context-engineering

A Microsoft product tour of running local, background (worktree) and cloud coding agents side by side in VS Code, with advice on which mode fits which task.

- Techniques: Worktree-per-background-agent; Route tasks by hands-on level; Plan first, autopilot second, pause before PR; Task-specific custom agents; Cloud agent with MCP and browser testing
- Tools: GitHub Copilot, VS Code, GitHub Copilot CLI, Git worktree, GitHub Actions, GitHub MCP server, Playwright MCP server, Microsoft Learn MCP server, awesome-copilot (open-source repo of agent customizations), Claude Opus 4.6 (used for the local agent)

## [What if the network was the sandbox? — Remy Guercio, Tailscale](../videos/BM2JX9hqsVQ.md)
`BM2JX9hqsVQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance, observability

Tailscale's Remy Guercio argues the network layer can act as an agent sandbox: identity-tagged WireGuard connections let an LLM gateway hold the provider key so the sandbox never has one, and every model call and tool call is visible and cuttable there.

- Techniques: Zero-key sandbox behind an identity-aware gateway; Per-identity budgets and quotas across providers; Per-tool-call webhooks for external policy; Identity-aware internal services with tsnet; Policy as code for network identity
- Tools: Tailscale, WireGuard, Aperture, tsnet, Claude Code, Codex, Gemini CLI, GitHub Actions, Opus 4.6

## [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](../videos/SKDJo2CopRs.md)
`SKDJo2CopRs` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: agent-architecture, mcp-and-tools, infra-cost-scaling

Two Cloudflare engineers tour Durable Objects, dynamic workers and code mode as a stateful, sandboxed runtime for agents. Mostly product pitch, with a few reusable architecture ideas.

- Techniques: One Durable Object per entity ID as the session or agent; Resumable stream held by the agent object; Deny-by-default capability sandbox for generated code; Code mode for large API surfaces; Scheduled work inside the agent class; Plugins as isolated dynamic workers
- Tools: Cloudflare Durable Objects, Cloudflare Workers, Cloudflare Dynamic Workers, Cloudflare Agents SDK, Vercel AI SDK, MCP, Cloudflare Sandbox SDK, Daytona, SQLite, R2, Zig (via Wasm), Next.js on Workers

## [The Missing Primitive for Agent Swarms — Lou Bichard, Ona](../videos/5Sui_OnSRlY.md)
`5Sui_OnSRlY` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: multi-agent, software-factory, agent-architecture

Ona's field CTO argues that runtimes, orchestration and triggers are largely solved for coding-agent swarms, and that agent coordination is the missing primitive. He proposes state-machine workflows packaged as a CLI that runs locally and in CI.

- Techniques: Parent-child sub-agents with scoped context; Two-tier sub-agent placement; Fleet fan-out with prompts and scripts as a workflow; Harness engineering loop; Gated micro-step workflow (state machine); CLI-packaged workflow gate
- Tools: Ona dev environments, GitHub, Linear, Symphony, ACP, ACPX, Fabro, n8n-style graph workflows, backgroundagents.com

## [Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw](../videos/VaS2h-dY1-4.md)
`VaS2h-dY1-4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: multi-agent, mcp-and-tools, pr-code-review

An OpenClaw maintainer shows acpx, a CLI and workflow engine over the Agent Client Protocol (ACP), used to automate PR triage and to run disposable per-task agents on Kubernetes.

- Techniques: ACP as the client-side adapter layer; Channel-bound agent sessions; Hybrid PR-triage workflow with JSON handoffs; Shallow-fix loop with a human escalation gate; Feedback bin for PR outcomes; Per-task disposable agent pods via a Kubernetes operator
- Tools: acpx, ACP (Agent Client Protocol), Codex, Claude Code, Zed, Discord, Slack, MS Teams, Kubernetes, Helm, Go operator, rsync

## [Vercel Built a Terminal Emulator and It's Only 12KB](../videos/MxACQUVS5mE.md)
`MxACQUVS5mE` · Better Stack · 2026-06-02 · q3 · intro · review · also: dev-tools

Better Stack walks through Vercel's Wterm, a web terminal that renders to the DOM instead of a canvas, with a 12KB Zig/WASM core and an optional libghostty renderer; it covers WebSocket wiring and the rough edges.

- Techniques: DOM-rendered web terminal; WebSocket pty bridge; Swap in the libghostty renderer; Browser demo fallback without a backend
- Tools: Wterm (Vercel), WtermGhostty, libghostty, Ghostty, GhosttyWeb (Coda), xterm.js, Zig, WebAssembly, React, Vue, Node.js, Bun

## [This Open Source Tool Gives You God Mode for AI Agents (AoE)](../videos/fPz9OB3Bau8.md)
`fPz9OB3Bau8` · Better Stack · 2026-06-02 · q2 · intro · review · also: coding-agents, multi-agent

Better Stack demo of Agent of Empires (AoE), an open-source terminal dashboard that runs many CLI coding agents side by side using git worktrees, status indicators and optional Docker sandboxes. Short and promo-leaning, with little configuration detail.

- Techniques: Run many CLI agents from one dashboard; Per-agent git worktree isolation; Triage agents by status instead of attaching; Optional Docker sandbox per agent
- Tools: Agent of Empires (AoE), Claude, Codex, tmux, Git worktrees, Docker, Agent Deck, Homebrew

## [MCP = Mega Context Problem - Matt Carey](../videos/YBYUvGOuotE.md)
`YBYUvGOuotE` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: mcp-and-tools, context-engineering

Cloudflare's Matt Carey argues that dumping every API endpoint into MCP tools blows up agent context, and that progressive discovery (tool search, CLIs, or code mode with typed SDKs run in isolates) is the way out.

- Techniques: Progressive tool discovery via tool search; Code mode over a generated typed SDK; Isolated execution of model-written code with programmable guardrails; Save agent-generated code as mini-scripts; Rate-limit APIs for agent callers
- Tools: MCP (Model Context Protocol), MCP SDK, OpenAPI, TypeScript, Cloudflare Workers, Dynamic Workers (workerd), V8 isolates, Wrangler, Cloudflare D1, Cloudflare Access, Claude Code, OpenClaw

## [Agents on the Canvas in tldraw — Steve Ruiz, tldraw](../videos/sPUjIBH5Cwg.md)
`sPUjIBH5Cwg` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: multi-agent, product-ux, security-guardrails

Steve Ruiz (tldraw) shows how agents moved from one-shot drawing on a whiteboard to multiple agents working as a team on a shared canvas, and the safety trade-offs of letting them script a desktop app.

- Techniques: Structured-output shape drawing; Produce-review-iterate loop; Leader/follower multi-agent on shared state; Expose a runtime API for agent-written code; Prompt for spatial and coordinate conventions
- Tools: tldraw, Electron, Claude, Cursor, Make Real

## [CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner](../videos/VktrqzQgytY.md)
`VktrqzQgytY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: software-factory, pr-code-review, multi-agent

Talk arguing CI/CD was built for human-paced PRs and breaks under agent volume; proposes spec-driven agent loops with in-loop validation, a pre-merge queue, and stateful compute.

- Techniques: Spec-first agent loop with a known-commit start; External review agents inside the loop; Pre-merge queue for serializable commits; Approve intent and evidence, not diffs; Stateful, incremental execution environments
- Tools: GitHub Actions, Claude Code, Amp, Cursor, Factory, GitHub Copilot, Namespace

## [Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate](../videos/vi-2nasppAg.md)
`vi-2nasppAg` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: agent-architecture, multi-agent, observability

Iterate's workshop on building event-sourced agent harnesses as stream processors: pure reducers for state, side effects after append, pause-based circuit breakers. Live demos mostly failed; the design ideas are the value.

- Techniques: Event-sourced agent log; Reducer plus after-append split; Pause-event circuit breaker; Deferred enrichment with a time budget; Child paths for sub-agents; Secret substitution at fetch time
- Tools: events.iterate.com (event service), Cloudflare dynamic workers, OpenAI SDK (Responses API), Zod, Pi, Claude, OpenCode, Convex, Kafka, Cursor, OpenClaw, Electric SQL

## [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../videos/8txf05vVVl4.md)
`8txf05vVVl4` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: mcp-and-tools, token-cost-efficiency, agent-architecture

Cloudflare's Sunil Pai on "Code Mode": have models write code against an API instead of making many tool calls, cutting a 2,600-endpoint API from ~1.2M tokens to ~1K, inside capability-restricted sandboxes.

- Techniques: Search + execute two-tool facade; Code as the tool-call format; Zero-capability sandbox with explicit grants; Agent-facing developer experience; Operate on the app's raw state
- Tools: Cloudflare Workers, Cloudflare Dynamic Workers, V8 isolates, OpenAPI, PartyKit, Claude Opus, TLDraw-style canvas

## [The New Application Layer - Malte Ubl, CTO Vercel](../videos/XKup1pj-34M.md)
`XKup1pj-34M` · AI Engineer · 2026-05-18 · q3 · intro · keynote · also: agent-architecture, enterprise-adoption, product-ux

Vercel CTO Malte Ubl argues agents are a new kind of software that makes long-tail automation affordable, names practical agent archetypes, and says harnesses should run apart from the code they generate.

- Techniques: Compress-the-research agent; Information-surfacing agent; Ask-what-you-hate discovery; Harness and code execution split; CLI and API first for agent-facing products; Lightweight bash sandbox for agents
- Tools: Vercel AI SDK, Chat SDK, JustBash, Claude, Codex, Granola, Pi, OpenClaw

## [Give Your Agent a Computer — Nico Albanese, Vercel](../videos/wflNENRSUb4.md)
`wflNENRSUb4` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: agent-architecture, mcp-and-tools, context-engineering

Nico Albanese (Vercel) live-builds a coding-style agent with AI SDK 6: a tool loop, web search, a persistent named sandbox running bash, file-based memory and self-written scripts, plus notes on context pruning and subagents.

- Techniques: Single-definition tool loop agent; Typed UI messages from the agent definition; Named persistent sandbox per session; Bash-only tool for a coding-style agent; Call options plus runtime context injection; File-backed memory injected into the system prompt; Per-step hook for message slicing; Subagents and handoff instead of compaction; Plan file with objective and checkboxes
- Tools: Vercel AI SDK 6, Vercel AI Gateway, Vercel Sandbox (persistent named sandboxes, beta), Next.js, Zod, OpenAI provider (web search tool), Anthropic provider (bash/computer tools), Vercel Workflow (durable steps), OpenCode, Amp (handoff tool)

## [Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev](../videos/svCnShDvgQg.md)
`svCnShDvgQg` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, infra-cost-scaling

Eric Allam (Trigger.dev) argues that replay-based durable execution breaks for long-running agent loops, and proposes splitting agent durability into an append-only context log plus VM snapshot/restore of the execution state.

- Techniques: Two-layer agent durability; Snapshot on idle, restore on next message; Recovery by failure class; Seekable compression with lazy page restore; Whole-VM snapshot instead of process checkpoint
- Tools: Trigger.dev, Firecracker, CRIU (captioned as "Cree"), Docker, fcrun

## [GitHub Was NOT Made for AI Agents (So Cloudflare Built Their Own)](../videos/PWj6GnTUBnk.md)
`PWj6GnTUBnk` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: software-factory, agent-architecture, dev-tools

Walkthrough of Cloudflare Artifacts, a Git-compatible repo store on Durable Objects built for agents, with a fork-per-task demo the speaker could not run because the product is in private beta.

- Techniques: Fork-per-task repo workspaces; Git-backed agent tools: read, write, commit (commit also pushes); Durable Object SQLite as the persistence layer for agent repos; Verification loop idea: run the agent's changed code in a sandbox, and check front-end work in a browser; Reconstructing a diff without git diff
- Tools: Cloudflare Artifacts (private beta), Cloudflare Workers, Cloudflare Durable Objects, Cloudflare Dynamic Workers, Cloudflare Sandboxes, Cloudflare Browser (Puppeteer), Wrangler (wrangler.jsonc / wrangler.toml bindings), isomorphic-git, Zig (compiled to WASM), Anthropic SDK, Git protocol, S3 Files

## [1 Million Sandboxes Per Second?! Dynamic Workers Are INSANE](../videos/7Re3HReM5SQ.md)
`7Re3HReM5SQ` · Better Stack · 2026-04-02 · q3 · practitioner · tutorial · also: agent-architecture, infra-cost-scaling

Better Stack walks through Cloudflare Dynamic Workers, V8-isolate workers created at runtime by a parent Worker, as a faster, lighter alternative to container sandboxes for running AI-generated code. The catch is JavaScript only, with no filesystem.

- Techniques: Per-request sandboxed child Worker with network disabled; Stable-name reuse for warm sandboxes; Custom bindings and RPC into the child; Bundling npm dependencies into a child; Egress interception for credential injection; Agent code-execution loop with artifact persistence; Scripted bulk spawn with create-or-reuse
- Tools: Cloudflare Dynamic Workers, Cloudflare Workers, Wrangler, V8 isolates, Cloudflare Sandboxes, Cloudflare Durable Objects, Cloudflare R2, Cap'n Web, Hono, Anthropic SDK, Claude Sonnet 4.6, Claude Sonnet 3.5

## [NVIDIA NemoClaw First Look: Secure AI or Just Over-Engineered?](../videos/5v0RJkqjU8c.md)
`5v0RJkqjU8c` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: security-guardrails, agent-architecture

Better Stack's hands-on first look at NVIDIA's NemoClaw, an OpenClaw agent wrapped in the OpenShell sandbox; the setup is fragile and per-request approvals make autonomous tasks tedious.

- Techniques: Deploy NemoClaw on a Brev GPU instance; Answer the NemoClaw installer prompts; Start the agent and approve pending egress requests; Recover a stuck Telegram gateway; Watch OpenClaw logs during autonomous tasks
- Tools: NemoClaw (NVIDIA, install script plus `nemoclaw start`), NVIDIA OpenShell (sandbox; OpenShell manager TUI for approving requests), OpenClaw (agent; `configure` wizard), Nemotron (NVIDIA inference model), NVIDIA Brev (cloud GPU platform; `brev shell`), Docker, CUDA, Telegram (bot token bridge)

## [NanoClaw: The Lightweight, Secure AI Assistant OpenClaw Should Have Been](../videos/AQ5uiLyr8bQ.md)
`AQ5uiLyr8bQ` · Better Stack · 2026-03-02 · q2 · intro · review · also: agent-architecture, claude-code

Better Stack walkthrough of NanoClaw, a ~500-line personal AI assistant on the Claude Agent SDK with WhatsApp, containers and self-extension by asking the agent; a short overview with a single feature-add demo.

- Techniques: Self-extending assistant via chat-driven code change; Hardened VPS install for a personal agent; Use a Claude subscription for an SDK-based agent
- Tools: NanoClaw, OpenClaw, Claude Agent SDK, Claude Code, Claude Sonnet (default model), Docker, Apple containers, Node.js (above v20), WhatsApp, Tailscale, Vercel agent-browser, Unsplash (image tool demo)

## [Coding Locally Is Slowing You Down](../videos/-b1qrPFl04A.md)
`-b1qrPFl04A` · Better Stack · 2026-03-02 · q2 · intro · tutorial · also: dev-tools

Better Stack walkthrough of Code Server (VS Code in a browser on a remote machine), run locally in Docker on a Mac for the demo; covers pros (reproducible, consistent env, lighter laptops) and cons (latency, RAM needs, basic default security).

- Techniques: Run Code Server in Docker for a quick trial; Move the heavy environment to a remote host and keep the laptop as a thin client; Pair with dev containers for reproducible environments; Harden before exposing publicly
- Tools: Code Server, VS Code, Docker, Django, pip, GitHub Copilot, GitHub Codespaces, dev containers, Postgres, Node.js, Python

## [Cloudflare Just Killed Mac Minis? OpenClaw Runs Serverless – Here's How!](../videos/DQdYE02TkIQ.md)
`DQdYE02TkIQ` · Better Stack · 2026-03-02 · q2 · practitioner · tutorial · also: agent-architecture, infra-cost-scaling

Walkthrough of running the OpenClaw agent gateway serverlessly on Cloudflare Workers, Sandboxes, Browser Rendering and R2, with setup steps and a serverless-versus-VPS verdict. Ends with a Better Stack sponsor read.

- Techniques: Prerequisites checklist before deploying OpenClaw on Cloudflare; Verify Durable Object, R2 and browser bindings after deploy; Enable Cloudflare Access and set two Wrangler secrets; Clear a stale sandbox container before redeploying; Pair the device and authenticate the browser; Persist state in R2, not the sandbox disk
- Tools: OpenClaw (captioned as Clawdbot / MoltBot / MaltBot), Cloudflare Workers, Cloudflare Sandboxes (Docker-based), Cloudflare Browser Rendering (headless Chromium), Cloudflare R2, Cloudflare Durable Objects, Cloudflare Access, Cloudflare AI Gateway, Wrangler, Hono, Chrome DevTools Protocol, Docker

## [You Need To Know This Before Installing OpenClaw](../videos/M3P0hQMQtq0.md)
`M3P0hQMQtq0` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: security-guardrails, token-cost-efficiency, skills-self-improvement

AI LABS tests the self-hosted agent OpenClaw and finds it costly (token-heavy context, heartbeats), slow as context grows, and risky (plain-text credentials, malicious community skills, prompt injection); it closes with mitigation advice.

- Techniques: Hard budget and alerts on the model API key; Reduce idle token burn; Vet community skills before install; Sandbox the agent; Least-privilege channel tokens; Prefer providers with built-in guardrails, with caution
- Tools: OpenClaw, Claude (former Claudebot name), OpenAI API, Anthropic models, OpenRouter, Ollama, Docker, Cisco open-source skill scanner, Discord, WhatsApp

## [Shanon: The Open Source AI Pentester Powered By Claude Code](../videos/H7Xh-x_TVdQ.md)
`H7Xh-x_TVdQ` · Better Stack · 2026-03-02 · q3 · intro · review · also: security-guardrails, agent-architecture, token-cost-efficiency

Walkthrough of Shannon, an open-source AI pentester built on the Claude Agent SDK: Temporal-orchestrated phases, parallel vulnerability agents, and a 2.5-hour, roughly $60 run against OWASP Juice Shop.

- Techniques: Temporal-backed durable agent pipeline; Static analysis then live-app recon; Parallel specialist fan-out with paired exploit agents; Reproduction setup as described in the video
- Tools: Shannon (open-source AI pentester), Claude Agent SDK (Anthropic), Claude Sonnet 4.6, Docker Compose, Temporal, Playwright, OWASP Juice Shop, Kali Linux (mentioned as the manual alternative), Claude Code Security (announced, not yet released per the creator), Shannon Pro (paid tier), OpenAI Agents SDK (speculated port), Vercel AI SDK (speculated port; transcript spells it 'Vasell')

## [This Makes AI Agents WAY More Powerful (just-bash)](../videos/EoyLzyJUcfI.md)
`EoyLzyJUcfI` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: token-cost-efficiency, dev-tools

Short walkthrough of just-bash, a TypeScript simulated bash with an in-memory virtual filesystem for agents, and how wiring it into an AI SDK chat cut input tokens from 133k to 6k on one JSON query.

- Techniques: Virtual bash tool for an agent; Mount files into a virtual workspace; Include the package's agent instructions; Restrict outbound network with a curl allowlist
- Tools: just-bash (TypeScript simulated bash with in-memory virtual filesystem), bash-tool package (AI SDK bash tool built on just-bash), AI SDK, GPT-5.2 (model used for the chat demo, as named by the presenter), jq, Python 3 (inside just-bash), SQLite (inside just-bash), curl (inside just-bash, host whitelist), head

## [This Sandbox Tool Makes Claude Code Unstoppable (Code On Incus)](../videos/t78-JUnTK5Q.md)
`t78-JUnTK5Q` · Better Stack · 2026-03-02 · q3 · practitioner · tutorial · also: coding-agents, security-guardrails

Better Stack walkthrough of Code On Incus (COI): running Claude Code agents in isolated Incus system containers on a Mac via Colima, with a malware-file triage demo.

- Techniques: Nested sandbox on macOS: Colima, then Incus, then COI; Bridge networking fix for Incus; Build COI from the cloned repo; Launch per-role agents into slots with a shared workspace; Analyze untrusted files inside the sandbox
- Tools: Code On Incus (COI), Incus, Colima, Claude Code, Docker, incus file push, coi build, incusbr0 (Incus bridge), EICAR test file, SWAPI (Star Wars API; auto-caption says 'Swoppy')

## [Vercel Just Revealed Claude Code's Greatest Advantage](../videos/gZr5VmsXmXQ.md)
`gZr5VmsXmXQ` · AI LABS · 2026-02-02 · q3 · practitioner · talk · also: rag-retrieval, context-engineering

Argues that LLM agents can retrieve context with plain bash (ls, find, grep, cat) instead of a vector DB, sending only a small slice to the model; shows a Gemini 2.5 Flash policy-docs demo and states when RAG still wins.

- Techniques: Bash-tool retrieval over a document directory; Scoped execution for agent shell access; Markdown-defined multi-phase evaluation pipeline; Route retrieval by data shape and query type
- Tools: Vercel bash tool (open-sourced; name not stated), Vercel sandbox (full VM isolation), Claude Code, CLAUDE.md, Gemini 2.5 Flash, Chroma (vector DB the speaker would normally have used), grep, ls, find, cat

## [Why I'm DELETING Clawdbot (Moltbot) After This](../videos/CB6Ysb_BLcM.md)
`CB6Ysb_BLcM` · Better Stack · 2026-02-02 · q2 · intro · review · also: security-guardrails, agent-architecture

Better Stack's walkthrough of the Clawdbot (Moltbot) personal agent: how its gateway, channels and state fit together, and why exposing it on a VPS and prompt injection are the main risks. Ends with a sponsor read.

- Techniques: Isolate a self-hosted agent on a dedicated VPS; Put the agent gateway on a private network with Tailscale; Use a separate API key for each agent; Scrub sensitive data from agent transcripts; Run the agent CLI's security command; Give the agent an identity file
- Tools: Clawdbot (Moltbot), Pi agent runtime, Grammy, Discord.js, Telegram, WhatsApp, Discord, Tailscale, Ollama, 1Password skill, Google Calendar skill, Anthropic API

## [Docker Just Fixed 90% of AI Coding By Releasing This](../videos/ZOutBmRai2M.md)
`ZOutBmRai2M` · AI LABS · 2026-01-02 · q2 · practitioner · review · also: mcp-and-tools, token-cost-efficiency

Docker's MCP toolkit walkthrough: one gateway in front of a vetted catalog, on-demand tool loading, and "code mode" where the agent chains MCP calls in a sandbox, keeping bulky results out of context.

- Techniques: Single MCP gateway front door; On-demand tool discovery with find/add/remove; Code mode: chain MCP calls in a sandboxed script; Write bulky tool output to a file and return only the fields needed; Volume-backed state between tool calls; Merge repeated tool calls into one generated tool
- Tools: Docker MCP Toolkit, Docker MCP Catalog, Docker MCP Gateway, Docker MCP find/add/remove tools, mcp exec tool, Docker containers and volumes (sandbox), Claude Code, GitHub MCP server, Notion MCP server, Cloudflare code mode (referenced), Anthropic MCP token post (referenced)

## [Cloudflare Just Destroyed v0, Lovable, and Replit in One Move](../videos/pDnpIkbJwN4.md)
`pDnpIkbJwN4` · Better Stack · 2026-01-02 · q2 · intro · review · also: vibe-coding-app-building, software-factory

Better Stack walkthrough of Cloudflare's open-source Vibe SDK: a self-hostable, MIT-licensed prompt-to-app platform that generates, previews and deploys full-stack apps on Cloudflare's edge. Mostly a demo and deploy checklist, with thin evidence behind the comparison claims.

- Techniques: Self-host Vibe SDK on Cloudflare via the Deploy button; Blueprint-first, phased app generation; Iterate by describing the bug in chat; Route all model calls through an AI gateway with caching
- Tools: Cloudflare Vibe SDK (open-source, MIT, self-hostable), Cloudflare Workers, Cloudflare Workers for Platforms, Cloudflare AI Gateway, Cloudflare sandbox containers, Google Gemini API (default model key), Bun (package install), GitHub (clone, export target), Replit (comparison), Cursor (comparison), Vercel (comparison), v0 (comparison)

## [Run AWS Locally with Docker (LocalStack)](../videos/jz7oq-Viwew.md)
`jz7oq-Viwew` · Better Stack · 2026-01-02 · q2 · intro · tutorial · also: testing-verification, dev-tools

Short intro to LocalStack, a Docker-based AWS emulator. The main takeaway is to use it for the inner dev loop and CI, and still verify critical paths on real AWS.

- Techniques: Point AWS SDK, CLI and IaC at a local emulator; Ephemeral LocalStack in CI; Split test tiers: emulator for the inner loop, real AWS for critical paths
- Tools: LocalStack, Docker, AWS CLI, AWS SDKs, Terraform, AWS CDK, Serverless Framework, Testcontainers, Homebrew (brew), AWS Lambda, Amazon S3, Amazon DynamoDB

## [Claude Just Solved Their Biggest Problem](../videos/opZpIN8g_6M.md)
`opZpIN8g_6M` · AI LABS · 2025-12-02 · q3 · intro · review · also: mcp-and-tools, context-engineering, token-cost-efficiency

Walkthrough of Anthropic's paper on running MCP servers as code files instead of direct tool calls, to cut context bloat; no implementation shown.

- Techniques: Filesystem-based MCP tool catalogue with progressive disclosure; Result shaping inside the execution script; Code-owned control flow between tool calls; Placeholder returns for sensitive data; File-based state for resumable runs
- Tools: MCP (Model Context Protocol), Claude, Claude skills, Memory tool, Cloudflare code mode, TypeScript, index.ts (file convention from the paper)

## [Running Docker on Cloudflare is FINALLY possible...](../videos/c6TEXxpUEUw.md)
`c6TEXxpUEUw` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: infra-cost-scaling, dev-tools

Better Stack walkthrough of Cloudflare Containers: deploying a Bun + ffmpeg container behind a Worker with a Durable Object, then reviewing limits, beta pricing and a Rivet/Fly cost comparison.

- Techniques: Container server behind a Worker; Durable Object container class; wrangler config for containers; Monitoring containers
- Tools: Cloudflare Containers (beta), Cloudflare Workers, Durable Objects, Wrangler CLI, Docker, Bun, ffmpeg, Rivet containers, Fly Machines (Fly.io), index.html static assets

## [Suna: The FREE Open Source Alternative to Manus AI](../videos/aqF8ItxLCRA.md)
`aqF8ItxLCRA` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: agent-architecture

Walkthrough of Suna, a free open-source self-hosted alternative to Manus, with one head-to-head build test, its architecture, a local Docker setup, and its cost and bug downsides.

- Techniques: Self-host an agent stack with Docker Compose after DB migrations; Isolate AI-generated code in per-run Docker environments via a sandbox provider; Use container logs as the primary debug surface for agent runs; Head-to-head test of agent products on one identical prompt
- Tools: Suna (captions say Sooner; open-source agent), Manus, Next.js, Supabase (auth, history, file storage; CLI; basejump schema), FastAPI, Daytona (isolated Docker sandboxes), Docker and Docker Compose, Redis, Anthropic API (Claude), OpenAI API, Firecrawl (web crawling), Tavily (web search)

## [Get Started with Claude’s Computer Use API – Full Setup & Demo](../videos/XSXaGvCRJ3c.md)
`XSXaGvCRJ3c` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: voice-multimodal, token-cost-efficiency

A 4-minute walkthrough of Anthropic's Computer Use API beta: run the setup container locally with Docker and your API key, then watch Claude operate a sandboxed virtual Linux desktop from a chat prompt.

- Techniques: Run computer use inside a disposable container; Give a multi-step browsing prompt and watch the screenshot loop
- Tools: Claude Computer Use API (Anthropic, beta), Claude API key (Anthropic), Docker, WSL2, Ubuntu, Bolt.new (named only as the video the agent found on the channel, not used as a tool)

## [The $10B System Prompts Behind Cursor AI and Others Just Leaked…](../videos/A5r2tfifYfY.md)
`A5r2tfifYfY` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, context-engineering, agent-architecture

Walkthrough of leaked system prompts from Cursor, Windsurf, Replit, Manus and others, with the host's takeaways on tool design, background execution, memory, sandboxing and a repo-to-text trick. Useful as prompt-design evidence, but the verdicts are overreaching.

- Techniques: Repo subfolder to LLM-readable text; Post-edit verification loop; Background command execution with process status checks; Persistent memory with semantic auto-retrieval; Ask-for-secrets and stuck-fallback behavior; Sandbox-scoped guardrails in the system prompt
- Tools: Cursor, Windsurf (Cascade), Replit, Manus, Lovable, Devin, Bolt, Roo Code (transcript: 'Rucode'), Netlify, Next.js, shadcn/ui (transcript: 'Shad CNUI'), PostgreSQL

## [Vercel goes ALL IN on AI (Vercel Ship Recap)](../videos/idBEifQwlGI.md)
`idBEifQwlGI` · Better Stack · 2025-11-02 · q2 · intro · news · also: infra-cost-scaling, dev-tools

Better Stack's 5-minute recap of Vercel Ship: AI Gateway and AI SDK v5 betas, a hosted sandbox for untrusted code with active-CPU billing, BotID, rolling releases, and several limited-beta features.

- Tools: Vercel AI Gateway, AI SDK v5, Vercel Sandbox, Fluid compute, Active CPU billing, BotID, CheckBotID, Rolling Releases, Microfrontends, Vercel Queues, Vercel Agent, Amazon Linux 2023

## [Why You NEED to Try Cloudflare's Sandbox SDK Today](../videos/0bkeZOXNJBg.md)
`0bkeZOXNJBg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: infra-cost-scaling

Short walkthrough of Cloudflare's Sandbox SDK for running AI-generated code in isolated containers from a Worker, with a Claude Haiku-to-sandbox example and a positioning take against Daytona.

- Techniques: Worker + Durable Object sandbox wiring; Generate-then-execute loop; Local dev with Docker before deploy
- Tools: Cloudflare Sandbox SDK, Cloudflare Workers, Cloudflare Durable Objects, Cloudflare Containers, Wrangler, Docker Desktop, Bun, Node 20, Python 3.11, Ubuntu 22, Anthropic AI SDK, Claude Haiku

## [WebAssembly vs AWS Lambda vs Cloudflare Workers: Which Actually Performs Best?](../videos/5vCGMrYadBI.md)
`5vCGMrYadBI` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: infra-cost-scaling, dev-tools

Better Stack runs one TypeScript app on Fermyon Spin (WebAssembly), Cloudflare Workers and AWS Lambda, comparing latency, recursion limits, sandbox behavior and resource use. Workers win on JS speed, Wasm has the smallest footprint, and the test is small and single-region.

- Techniques: Per-minute uptime probe for latency distribution; Local warm-up timing with repeated curl; Recursion vs iteration as a stress test; Eval-injection sandbox probe; Host-level resource sampling per process; OpenTelemetry trace export from a Spin app
- Tools: Fermyon Spin (captioned 'Thermian Spin'), Fermyon Cloud (captioned 'Thermian Cloud'), Cloudflare Workers, Wrangler, workerd, esbuild, Node.js, V8 / V8 isolates, QuickJS, AWS Lambda, Better Stack uptime monitors, OpenTelemetry

## [Codex CLI Has Just Got WAY Better!](../videos/Szi4SHB4nNs.md)
`Szi4SHB4nNs` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, claude-code, mcp-and-tools

Better Stack tours the late-2025 Codex CLI update (Rust rewrite, ChatGPT login, sandbox and approval modes, config profiles) and candidly compares it with Claude Code.

- Techniques: Separate sandbox from approval when setting agent autonomy; Named config profiles in config.toml run with -p; Audit an agent run via the transcript view; Tune model and reasoning effort per task; Point Codex at an OpenAI-compatible endpoint for non-OpenAI models; Notify script for event alerts; Everyday workflow commands
- Tools: Codex CLI (OpenAI terminal coding agent), GPT-5, GPT-OSS, DeepSeek (tested, errored), AGENTS.md, config.toml, Ink (previous TypeScript UI), Ratatui (Rust TUI library), ChatGPT login, Codex VS Code plugin, Claude Code (comparison), Better Stack MCP (host plug)

## [Podman vs Docker in 2026: What's Really Different?](../videos/SIvoAOpXZPg.md)
`SIvoAOpXZPg` · Better Stack · 2025-11-02 · q3 · intro · review · also: dev-tools

Better Stack's short comparison of Podman and Docker: Podman is a near drop-in, daemonless, rootless alternative with native pods; Docker wins on ecosystem, Swarm and maturity.

- Techniques: Group multi-container apps as Podman pods; Run containers rootless for a smaller host blast radius; Use systemd to manage container lifecycle; Run Docker and Podman side by side
- Tools: Podman, Podman Desktop, Docker, Docker Desktop, Docker Compose, Docker Swarm, Docker Hub, Kubernetes, systemd, OrbStack, Nginx, PHP

## [Docker Containers - How Hackers Can ESCAPE Them in Seconds!](../videos/giXlSlFLKwA.md)
`giXlSlFLKwA` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: security-guardrails, dev-tools

Shows two ways to escape misconfigured Docker containers, via a mounted Docker socket and via privileged mode or CAP_SYS_ADMIN, then lists the hardening steps (proxy, drop caps, seccomp, gVisor).

- Techniques: Avoid mounting the Docker socket into containers; Audit a container's capabilities with capsh; Replace privileged mode with specific capabilities, then add a seccomp profile; Run untrusted or agent-generated workloads under gVisor; Check Docker hardening with docker-bench-security; Move host-level metrics collection out of containers
- Tools: Docker, Docker Desktop, Docker Compose, Bun, Nginx, Vector, cAdvisor, Alpine Linux, capsh, Docker socket proxy, gVisor, docker-bench-security

## [Cursor 1.0 is their BEST update yet... (Agents, BugBot, Memories and more)](../videos/Ig-cfiqWJCs.md)
`Ig-cfiqWJCs` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, pr-code-review, mcp-and-tools

Feature tour of Cursor 1.0 covering BugBot PR review, remote background agents, per-project memories and one-click MCP install with OAuth, plus the security caveats of background agents.

- Techniques: BugBot on GitHub PRs with trigger control; Launching a background agent from a prompt; Background agent environment via snapshot or environment.json; Saving persistent project rules as memories; One-click MCP install with OAuth
- Tools: Cursor 1.0, Cursor BugBot, Cursor Agent, Cursor background agents, Cursor memories, Cursor dashboards, GitHub, GitHub Copilot, Claude Code (transcribed as 'clawed code'), Notion MCP server, Bun / bunx, Create React App (npx)

## [You Won’t Believe What Google Gemini 2.0 Can Do Now!  - #gemini2flash #aistudio](../videos/teEp3I83k-w.md)
`teEp3I83k-w` · AI LABS · 2025-11-02 · q2 · intro · review · also: voice-multimodal, models-research

Walkthrough of Gemini 2.0 Flash's real-time webcam and screen-share mode in Google AI Studio, with a list of claimed benchmark scores and quick tests of its tools. Mostly a demo with light substance.

- Techniques: Live screen and webcam Q&A for unfamiliar software; Show token counts and temperature in AI Studio; Small smoke-test battery for a new model; Re-prompt once when grounding returns no sources; Get API access from AI Studio or OpenRouter
- Tools: Gemini 2.0 Flash, Gemini 1.5 Flash, Gemini 1.5 Pro, Google AI Studio, Gemini Multimodal Live API (Stream Real-Time), Google Search grounding, Gemini code execution, Microsoft Word, Adobe Premiere Pro, OpenRouter

## [OpenAI's NEW Cloud-based Software Engineer (Codex)](../videos/nPAXAAbU16w.md)
`nPAXAAbU16w` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, software-factory

Launch-day walkthrough of OpenAI's cloud Codex agent: parallel tasks in isolated containers, GitHub integration, AGENTS.md, and the codex-1 and codex-mini pricing.

- Techniques: Repo-level agent instructions via AGENTS.md; Configure the agent's dev environment to match local; Turn Ask-mode suggestions into Code tasks; Use a failing agent task as bug triage; Ask for verifiable evidence in every completion
- Tools: Codex (cloud agent, ChatGPT sidebar / chatgpt.com/codex), Codex CLI (mentioned as distinct), ChatGPT, GitHub (repo connection and PR creation), AGENTS.md, codex-1 (o3 variant for SWE), codex-mini-latest, o3 High (comparison baseline), SWE-bench Verified (benchmark cited), Devin (mentioned as competitor), Windsurf (mentioned as recent OpenAI purchase)

## [Your Own Mini AWS in Under 30 Minutes (Incus Tutorial)](../videos/zaAtYkM24hU.md)
`zaAtYkM24hU` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools, local-ai

Better Stack walkthrough of installing Incus (a community fork of LXD) on Ubuntu to run system containers and VMs, host Ollama in a container, and set up per-customer projects with quotas.

- Techniques: Install Incus from the signed apt repo; Initialize Incus and launch a container; Launch a VM with the same command; Add a bridge network so containers can reach the internet; Run Ollama as a service in a container; Create per-tenant projects with resource limits
- Tools: Incus (version not stated), LXD (upstream fork origin), LXC (container layer), QEMU (VM layer), Ubuntu (server image and host OS), Ollama, orca-mini (small test LLM), Zabbly apt repo (Incus package source), apt, gpg, curl

