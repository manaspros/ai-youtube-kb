# mcp-and-tools — 286 videos

*MCP, tool calling, tool design, APIs for agents, agent interoperability (A2A)*

By channel: AI Engineer 134 · Kai Explains 9 · AI LABS 78 · Better Stack 65

**Synthesized guide:** [guides/mcp-and-tools.md](../guides/mcp-and-tools.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Most of Your Docs Readers Are Now AI Agents - Hahnbee Lee, Mintlify & Lincoln Murr, Coinbase](../videos/YX4Z4XqZ9Vo.md)
`YX4Z4XqZ9Vo` · AI Engineer · 2026-11-01 · q2 · intro · interview · also: product-ux, enterprise-adoption

A Mintlify and Coinbase fireside chat on designing docs and APIs for agent readers and agent payments; mostly opinion, with one notable agent-traffic stat and a closing build-vs-buy plug.

- Techniques: Keep docs lean for agent readers; Track agent share of docs traffic; Automate doc upkeep, keep prose human; Expose the product as APIs first, then wrap; Pay per call with a wallet instead of API keys
- Tools: Mintlify, x402, MCP, CLI, API, OpenClaw

## [Your AI Agent Wants Your Data. Here's How to Lock It Down - Jeff Smith, Oracle](../videos/LnQce-eHm8k.md)
`LnQce-eHm8k` · AI Engineer · 2026-11-01 · q3 · practitioner · review · also: security-guardrails, data-engineering, context-engineering

Oracle's Jeff Smith on locking down agent access to databases: expose curated reports as MCP tools instead of raw NL-to-SQL, give agents a compact schema tool, and enforce identity-based row and column security inside the database.

- Techniques: Curated report catalogue exposed through two MCP tools; Three server modes: ad hoc SQL, custom tools and reports only, or both; Reveal report SQL to agents under a privileged scope; Action-grouped tools instead of single-purpose tools; Compressed deterministic schema-info tool; Generate schema annotations from enterprise documents; Identity-driven row and column filtering at the database; Diagnose production performance on a read-only standby
- Tools: Oracle AI Database, Oracle MCP server, MCP (Model Context Protocol), MCP apps (spec feature, speaker says added to the spec in July; Oracle plans a GUI for later this year), Claude, Codex, Gemini, LangChain, Azure Entra ID (spoken as 'Azure IntraID'), Oracle Data Guard, AWR (Automatic Workload Repository, Oracle performance report), Confluence

## [Stop Giving Your Agent Tools. Give It a Sandbox - Mikyo King, Arize AI](../videos/dAoOYFx7ZYw.md)
`dAoOYFx7ZYw` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: sandboxing-execution, token-cost-efficiency, evals

Arize's Mikyo King argues agents should get a search tool plus a code sandbox instead of a large tool catalog, reporting 43% fewer tokens and 31% lower cost in their own Harbor evals, while listing open problems such as secrets, permissions, and durability.

- Techniques: Search-then-execute tool access (code mode); Bash plus CLI as the first sandbox; Hoist REST CRUD endpoints into a sandbox language; SQL as an aggregate-query escape hatch; Keep secrets out of the model's context; Signed handoff for binary artifacts; Sandboxed, multi-trial agent evals with pass@k; Trajectory-driven instruction hill-climbing
- Tools: Arize Phoenix, Harbor Framework, Claude Code, MCP, Bash, Python sandbox, SQL (text-to-SQL), SWE-bench, PyDurable (named in the talk; caption may be garbled)

## [Who Is Making This Request? Agent Auth 101 - Kamil Potrec, Keycard](../videos/58ulJViGFgU.md)
`58ulJViGFgU` · AI Engineer · 2026-10-28 · q3 · practitioner · talk · also: security-guardrails, governance-compliance

Keycard's Kamil Potrec argues agents need their own authenticated identities, short-lived scoped credentials via OAuth-style delegation, and a gateway that injects credentials outside the agent's reach, so every request is attributable and revocable.

- Tools: Keycard (control plane, client and service SDKs, gateway), MCP (Model Context Protocol), OAuth, agentbaseline.org (software factory reference implementation, named by the speaker)

## [Build Your Own Team of Managed Agents - Jack Wotherspoon, Google DeepMind](../videos/Y_p3y6zP5QE.md)
`Y_p3y6zP5QE` · AI Engineer · 2026-10-26 · q3 · intro · talk · also: sandboxing-execution, multi-agent, agent-architecture

Google DeepMind's Jack Wotherspoon demos Gemini managed agents: a cloud sandbox, harness and API in one call, with reusable environments for multi-agent handoff, credential-injecting proxies, and scheduled triggers.

- Techniques: Single-call managed agent; Chain turns with the interaction ID; Hand off work between agents via a shared environment ID; Narrow single-purpose agents with fan-out; Placeholder credentials with egress injection; Scheduled and webhook-triggered runs
- Tools: Gemini API Interactions API, Gemini managed agents, Antigravity harness, Gemini Flash, Gemini 4 Argonne (name as spoken in the talk), Google Search (built-in tool), remote MCP servers, agents.md, agent skills, GitHub, Google Drive, Google Docs

## [Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management](../videos/ZMZlAn6Pyfg.md)
`ZMZlAn6Pyfg` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · also: governance-compliance, enterprise-adoption, evals

A hedge-fund head of AI explains how Contour measures AI ROI: live A/B tests of analyst workflows, process metrics over slow P&L, cost per useful insight, and connector-maintenance time counted as a cost.

- Techniques: Live A/B workflow capture; Agent-synthesized vs analyst-synthesized expert calls; Cost per useful insight; Idea-resurfacing agent; Alt-data via MCP or API connectors into agents; Connector-maintenance time as an ROI line item
- Tools: AlphaSense, Yipit, Rogo, Hebbia, Bloomberg, MCP, APIs (vendor data)

## [Real AI Agent Attacks and What Would Have Stopped Them — Andrey Rybka, Bloomberg](../videos/5O6jLtoeKrg.md)
`5O6jLtoeKrg` · AI Engineer · 2026-10-24 · q4 · practitioner · talk · also: security-guardrails, sandboxing-execution, agent-architecture

Bloomberg's Andrey Rybka walks through real agent security incidents (sandbox escape, CRM exfiltration, hidden-text injection, DNS leaks, a dropped production database) and maps each to layered controls: identity, input defense, deterministic tool brokers, default-deny egress, and budgets that halt.

- Techniques: Rule of two (capability gating for agent workflows); Deterministic invocation broker; Default-deny egress including DNS; One identity per agent, short-lived audience-bound tokens; Delayed package ingestion; Circuit breakers and halting budgets; Memory integrity and fresh-start policy; Security requirements in the spec
- Tools: MCP (Model Context Protocol) servers, OAuth, DNS, npm, NotebookLM (transcribed as 'Notebook Alarm'; likely NotebookLM), AWS accounts and GCP projects (as isolation analogies)

## [This Tiny Qwen 27B Model Runs on a 12GB GPU](../videos/XKejQWnispc.md)
`XKejQWnispc` · Better Stack · 2026-10-24 · q3 · practitioner · review · also: local-ai, inference-serving, evals

Better Stack reviews Saluki 27B, a ~7.9GB quantization of a 27B Qwen-family model tuned to keep tool calling intact at the cost of math, and tests it on local llama.cpp and a DGX Spark.

- Techniques: Serve a GGUF quant locally with llama.cpp; Two-part tool-calling smoke test; Tool-call reliability count; Recommended settings for tool calls; Report strict and lenient parser scores separately; Measure agent throughput, not just file size; Pick by workload
- Tools: Saluki 27B (model name as captioned; the transcript attributes it to Underdog), Qwen 27B base model (captioned as 'QEN 3.827B'), Qwen 3.8 Flash (captioned as 'Quen 3.8 Flash next'; used as a comparison model at 4-bit), llama.cpp (llama-server, stock build), Ollama, Unsloth quants (4-bit, IQ2_XXS, IQ2_S), ISTA-DAS Lab 2-bit quant (RCO quantization search), Ternary Bonsai 2 (PrismML custom llama.cpp fork), MLX (an unfinished port was mentioned), BFCL (Berkeley function-calling benchmark, single-turn), AIME 2025, SWE-bench Verified (50-task subset)

## [How OpenAI Built ChatGPT for Bankers and Analysts — Joseph Kim, OpenAI](../videos/opHmX7qClzE.md)
`opHmX7qClzE` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · also: product-ux, enterprise-adoption, models-research

OpenAI's Joseph Kim explains how ChatGPT for Financial Services was built on the plugin platform (MCP, skills, artifact tools), why finance lagged in AI use, and his 2027 bets on finance models and persistent agents.

- Techniques: Host and index licensed data yourself, expose it through MCP; Split tool/instruction layer from domain post-training; Firm templates for generated artifacts; Citation viewers for reviewable answers; Plan features around the usefulness threshold; Build on the plugin platform building blocks
- Tools: ChatGPT, ChatGPT plugin platform, MCP (Model Context Protocol), MCP apps, Skills, Codex, Codex desktop app, Excel, PowerPoint, GPT-4

## [How to Let AI Agents Sign Up for Your App Safely — Isabelle Williams, WorkOS](../videos/uTrY8slys0w.md)
`uTrY8slys0w` · AI Engineer · 2026-10-23 · q3 · practitioner · talk · also: security-guardrails, governance-compliance, product-ux

WorkOS PM walks through letting AI agents sign up for and act inside an app safely, using AuthMD, ID-JAG identity assertions, and agent tokens scoped to a user-bounded ceiling.

- Techniques: AuthMD discovery file; Anonymous trial with claim token; ID-JAG identity assertion grant; Blueprint ceiling with scope intersection; Separate agent principal from user session
- Tools: AuthMD (open markdown-based agent onboarding protocol), WorkOS Agent Auth, ID-JAG (Identity Assertion JWT Authorization Grant, IETF spec), OAuth 2.0, MCP authorization spec (Enterprise Managed Authorization), Okta Cross App Access, Claude (referred to as Claude / Cloud Code in the transcript), Cursor (used to vibe-code the demo app), Waypoint (speaker's demo travel-planning app), Muse and Instinct (personal agents mentioned, no detail given), Maple Itinerary and Trip Ledger (other planning tools the demo agent tried)

## [This Looks Like Spy Software... It's Just Public Data](../videos/PQN76wcEt10.md)
`PQN76wcEt10` · Better Stack · 2026-10-23 · q3 · intro · review · also: dev-tools, voice-multimodal, data-engineering

Walkthrough of God's Eye View, an open-source local globe that fuses public live feeds (planes, ships, satellites, cameras, quakes), with its feed-smoothing design and honest data caveats.

- Techniques: Run God's Eye View locally; Render the last update one step behind and interpolate; Dead reckoning for dropped feeds; Ration a free API quota with a budget; Hard spend cap for a realtime voice API; Unlock 3D tiles through an external key
- Tools: God's Eye View (open-source globe project, about 55,000 GitHub stars), Cesium JS, Vite, Node.js (24.14 or newer required; 25 unsupported), npm, SGP4 orbit model, ADS-B, AIS, OpenSky Network, MCP (Model Context Protocol) server, Claude, Codex

## [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](../videos/adfw3xJBx1o.md)
`adfw3xJBx1o` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: enterprise-adoption, coding-agents, sandboxing-execution

Monzo's engineers describe Agent Chip, an in-house coding agent that began as a viral Slack emoji trigger and grew into a sandboxed, MCP-gated platform building block.

- Techniques: Gateway-first MCP layer for internal tools; Isolated sandbox namespace for remote agents; Separate orchestrator from execution; Emoji-reaction prompt trigger in chat; Low-signal incident mode; Proactive impact checks on backend changes
- Tools: Agent Chip (Monzo's in-house coding agent), Slack, GitHub, Linear, MCP (internal MCP gateway server)

## [AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard](../videos/uA4ah-dVHvU.md)
`uA4ah-dVHvU` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: enterprise-adoption, data-engineering, multi-agent

Vanguard's cash-ledger modernization: exposing the legacy codebase over MCP cut a 7-day research loop to 15 minutes, with lessons on migration, idempotent producers and consumer onboarding.

- Techniques: Expose a legacy codebase to agents through an MCP server; Two-stage CDC migration verification; Single write gateway with idempotency for all producers; Consumer access matched to channel; Business-case registration for consumers; Fix forward, do not patch the legacy; Human-readable state values in the new system; Shared team knowledge base
- Tools: MCP server (legacy codebase and migration docs exposed to AI tools), CDC (change data capture, generic), GraphQL (real-time consumer API), Kafka (event topic for inserts and updates), Schema registry (generic, for all consumer channels), Snowflake-style IDs (ID paradigm, not the product), Data warehouse data-share views (batch consumers)

## [Why AI Agents Will Need Their Own Bank Accounts — Lincoln Murr, Coinbase](../videos/f_HwzoYrZ7s.md)
`f_HwzoYrZ7s` · AI Engineer · 2026-10-20 · q2 · intro · talk · also: governance-compliance, product-ux

Coinbase's head of AI product on agentic finance: agents that pay and grow money, the X402 HTTP 402 micropayment standard, and trust that is earned in steps. Largely a vendor pitch with some useful adoption data.

- Techniques: Gate content or APIs behind HTTP 402 micropayments (X402); Staged autonomy for agents that handle money; Delegated conditional execution; Ship features as skills that write code on the user's machine; Proactive widgets against chat cold start
- Tools: X402, Agent Kit, LangChain, Coinbase MCP, Coinbase CLI, Coinbase Advisor, GrokBot, Muse, Stripe Link, Stablecoins

## [The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft](../videos/UGjk3Uk0MxM.md)
`UGjk3Uk0MxM` · AI Engineer · 2026-10-20 · q4 · practitioner · workshop · also: evals, models-research, agent-architecture

Hands-on workshop comparing GPT-5.5, Kimi K2.6, DeepSeek V4 Flash and Mistral Large 3 on counting, RAG grounding, vision, tool calling, agent loops, evals and DSPy prompt optimization.

- Techniques: Single-variable model swap harness; Chain-of-thought decomposition for counting; Grounded RAG prompt with explicit refusal and citation; Tool definitions as prompt engineering; Low-level tool-call loop; Force tool use over mental math; Give date math to a tool; Deterministic checks first, LLM-as-judge second; Spec-driven eval generation with Assert; DSPy with GEPA for prompt optimization; Anthropic document citations
- Tools: Microsoft Foundry, GPT-5.5, Kimi K2.6, DeepSeek V4 Flash, Mistral Large 3, OpenAI Python SDK, OpenAI Responses API, Anthropic Messages API, uv, GitHub Codespaces, LangChain v1, PydanticAI

## [6 Insane Trending GitHub AI Design Repos You Need to Use](../videos/NZjjmf3I6I4.md)
`NZjjmf3I6I4` · AI LABS · 2026-10-19 · q2 · practitioner · review · also: coding-agents, skills-self-improvement, multi-agent

Walkthrough of six GitHub repos that give coding agents design references, multi-viewport checks, design-token extraction, multi-agent page builds, app-store screenshots and launch-video generation. Mostly sponsored tool demos with little measurement.

- Techniques: Reference-first design with an awards MCP; Post-build responsive check with Responsively MCP; Design taste skills, chosen by scope; Extract and diff design tokens with Dembrandt; Generate app-store screenshots with a local editor project; Launch video with Brag, with a verification pass
- Tools: Awards MCP (awards setup and awards inspiration commands), Klein CLI (caption spelling; probably Cline), sponsor, Kleinpass (caption spelling; probably ClinePass), sponsor, open-weight model access, first-month discount link, Whisperflow landing page (probably Wispr Flow, used as a reference site), Butter.Video (animation reference site), Responsively (Mac app and MCP server), Genjutsu skills: Cast, Paint, Bunshin, taste skill and hallmark (previously covered by the channel), Dembrandt (skill, design.md output), App store screenshots skill and local editor, Brag / Bragg (brag command, Full Mode and Slim Mode), Hyperframes (video framework used by Brag Full Mode)

## [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](../videos/tZycGA_Fbfo.md)
`tZycGA_Fbfo` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: security-guardrails, observability, context-engineering

Credit Karma's senior staff engineer walks through a governed enterprise agent stack: scaffolded agent repos, a central MCP gateway, risk-gated execution, per-run evals, PII blocking, and a context optimizer that cut token use about 90% in demos.

- Techniques: Dev-portal agent scaffolding; Gateway token exchange with namespace routing; Risk-classified plan graph with HITL gate; Thread, run and checkpoint memory; Severity-based redaction before every sink; Context pipeline: budget, re-rank, dedupe, compress; Per-run eval scoreboard with nested detail; Three-layer monitoring split
- Tools: LangGraph, LangChain, FastMCP, Redis, JWT, Docker, Kubernetes, OpenTelemetry, Grafana Tempo, Prometheus, ELK, Loki

## [Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard](../videos/ws9XcGGPBDk.md)
`ws9XcGGPBDk` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: security-guardrails, governance-compliance

Kim Maida (Keycard) argues agents with private data, untrusted content and external comms form a "lethal trifecta" and shows how token exchange (OAuth 2 RFC 8693-style STS), task-scoped ephemeral tokens and mission-based authorization contain the blast radius without removing capabilities.

- Techniques: Per-tool-call token exchange through an STS; Mission-scoped approval before tool use; Keep all three trifecta legs and control access instead; Audit with attributed identity chains
- Tools: Keycard, OAuth 2 token exchange (RFC 8693 style), MCP servers, MCP gateway, Snowflake, Incident pager API, Google login

## [What Really Happens Inside ChatGPT (AI Explained)](../videos/ZTmZOdB5o0U.md)
`ZTmZOdB5o0U` · Better Stack · 2026-10-12 · q3 · intro · other · also: models-research, rag-retrieval, training-finetuning-rl

An eight-minute beginner tour of LLM internals (tokens, weights, transformers, training, LoRA, quantization, RAG, tool calling, MCP, agent loops) with no product pitch, pitched at newcomers rather than builders.

- Techniques: Stateless chat memory via replay; Tool-calling loop; Agent loop with task handoff; Retrieval-augmented generation (RAG); LoRA fine-tuning; Weight quantization for local models; Reinforcement learning with a programmatic checker
- Tools: ChatGPT, GitHub, Slack, Better Stack, Model Context Protocol (MCP)

## [Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab](../videos/ZGzthw4BZiA.md)
`ZGzthw4BZiA` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: voice-multimodal, testing-verification, coding-agents

Amazon AGI Lab hands-on workshop on Nova Act's open-sourced perception primitives: point-and-annotate a live page into JSON, run Gherkin-based visual verification, and wire both to a coding agent.

- Techniques: Deterministic visual annotation to JSON; Gherkin user flows auto-generated from a surface crawl; Browser extension to coding agent bridge; Automatic verification after every agent change; Voice or wearable transcript as an annotation source
- Tools: Amazon Nova Act, Nova Act SDK, Nova Act MCP server, Visual Annotator (Chrome extension), Visual verification skill, Claude Code, Kiro, Gherkin, Chrome, uv / uvx, Jam MCP, Atlassian MCP

## [Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal](../videos/aV_vgUSatqs.md)
`aV_vgUSatqs` · AI Engineer · 2026-10-12 · q3 · intro · workshop · also: coding-agents, context-engineering

PayPal's developer tools leads run a live workshop where attendees make a coffee-ordering CLI work for agents. Main point: interactive prompts fail silently under agents, so CLIs need machine-readable side channels, injected context, and determinism.

- Techniques: Side-channel JSON interface for CLIs; Tmux driver for interactive CLIs; Context injection via a single input file; Deterministic CLI, reasoning outside; Have an agent build the solver
- Tools: tmux, Claude Code, Codex, Claude Agent SDK, Opus 4.8, Slack

## [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](../videos/YXiLj4tJt5A.md)
`YXiLj4tJt5A` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, security-guardrails, skills-self-improvement

Hands-on AWS workshop: build a Strands customer-service agent with hooks (rate limit, deterministic blocks), lazy-loaded skills, steering guardrails, then deploy to AgentCore Runtime.

- Techniques: Per-request tool-call rate limiter via hooks; Deterministic input filter hook; Skills as on-demand markdown procedures; Steering handler (rule or LLM buddy); Externalised steering rules; Message-history inspection
- Tools: Strands Agents, Amazon Bedrock AgentCore (Runtime, Memory, Gateway, Observability), Amazon Bedrock, Amazon CloudWatch, AWS CDK / CloudFormation, AWS OpenTelemetry Distro, boto3, agent-control (open-source steering rules library), MCP, A2A, Jupyter / Workshop Studio

## [AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk](../videos/p-2MT8KYZqU.md)
`p-2MT8KYZqU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: security-guardrails, governance-compliance, vibe-coding-app-building

Two-hour Snyk workshop on AI security foundations: OWASP LLM Top 10 risks, shadow AI and AI bills of materials, AI threat modeling, MCP tool poisoning, vibe-coding failures, and a live CTF chatbot exercise.

- Techniques: Layered prompt-injection defense; Keep secrets out of prompts and enforce access outside the model; Scope chatbot data to what may be disclosed; AI threat modeling workflow; Adversarial review of an architecture; AI BOM as a CI gate; Audit MCP configs and servers before enabling; Secure-by-design playbook for agentic coding; Probe a chatbot in a CTF-style sandbox; Offer an approved alternative when restricting a tool
- Tools: Snyk Evo, Snyk Agent Scan, Snyk Code, Snyk (SCA/SAST), OWASP Top 10 for LLM Applications, STRIDE, DREAD, SBOM (SPDX, CycloneDX), CycloneDX (AI/ML BOM support), Model Context Protocol (MCP), Figma Framelink MCP server, OpenClaw

## [Build a Platform and Watch It Burn — Michael Forrester, Accenture & Whitney Lee, Datadog](../videos/1tpqdglI3T0.md)
`1tpqdglI3T0` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: security-guardrails, sandboxing-execution, observability

Workshop where attendees attack a Kubernetes-hosted burrito-ordering agent, then add layered infra and AI guardrails (admission, runtime, network, input/output scrubbing, MCP checks) and see which attacks each layer stops.

- Techniques: Layered guardrails across infra and AI; Input guard before the LLM call; Mid-stream output scrubbing; MCP tool description review and registry allowlists; OpenTelemetry traces for every agent turn; Kernel-level prevention for runaway processes; Agent identity and least privilege; Three-question rubric for AI in a workflow
- Tools: Kubernetes, Amazon EKS, kagent, Kyverno, Falco, Falco Talon, Tetragon, KubeArmor, Cilium, SPIFFE/SPIRE, LLM Guard, NeMo Guardrails

## [How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI](../videos/xn8EsW0wxyc.md)
`xn8EsW0wxyc` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: security-guardrails, agent-architecture, observability

Venice AI's developer-relations lead explains how secrets leak through agent architectures (logs, vaults, LLM context, tool calls) and patterns to contain them: hashed IDs, handles, narrow tool scope, and keeping credentials out of the reasoning layer.

- Techniques: Credential-in-runtime, not in-prompt; Hashed identifiers for rate limits and tracking; Split-key custody for stored outputs; Revocable handles as capabilities; Narrow tool exposure per agent; Prompt-injection classifier in front of the agent; Own the agent runtime; Verifiable private inference via TEE attestation
- Tools: Venice AI, OpenClaw, 1Password, HashiCorp Vault, Firecracker, AWS EC2, VPC, Qdrant, LanceDB, Cursor, Claude Code, MCP

## [Auth for Agents: Let AI Sign Up for Your Product with auth.md — Michael Grinich, WorkOS](../videos/nSkmXakJ6eo.md)
`nSkmXakJ6eo` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: security-guardrails, product-ux

WorkOS founder argues agents need their own sign-up step, and proposes auth.md, an open markdown spec that tells an agent how to register for a service without a human clicking through.

- Techniques: auth.md registration spec; Identity assertion exchange for agent sign-up; Risk-scored registration with time-boxed free access; Deferred human claim; Approval-only supervision
- Tools: auth.md, MCP, ID-JAG, Wrangler, Pi (agent harness), Claude, OpenClaw, x402, Cloudflare

## [Inside the AI Economy: What Stripe's Data Reveals — Nilofer Rajpurkar, Stripe](../videos/T3wRyXg_yVg.md)
`T3wRyXg_yVg` · AI Engineer · 2026-10-12 · q3 · intro · talk · also: product-ux, enterprise-adoption

Stripe product talk using payments data to show AI companies build fast, sell globally on day one, price by usage/credits, and build enterprise sales early; includes an agent-driven Stripe setup demo.

- Techniques: Agent-driven sandbox provisioning; Clarifying-question recommender tool plus domain skills; Guardrails on sensitive actions; Hybrid subscription plus credits pricing; Unified customer and catalog model across channels
- Tools: Claude Code, Stripe MCP server, Stripe agent skills, Stripe CLI, Stripe Checkout, Stripe Tax, Stripe Link, Intercom Fin

## [The Next Trillion Internet Users Still Don’t Have an Identity — Adi Singh, AgentMail](../videos/mBNVKkyfnE0.md)
`mBNVKkyfnE0` · AI Engineer · 2026-10-12 · q3 · intro · talk · also: security-guardrails, product-ux

Adi Singh (AgentMail) argues agent identity will be accumulated from existing human-facing surfaces like email and Slack rather than issued from scratch, and that over-tight key-card style security specs hurt adoption.

- Techniques: skill.md signup flow with inbox provisioning API; Dedicated per-agent inbox as the identity and contact point; Use existing surfaces as the bridge for new agent identity
- Tools: AgentMail, Telnyx, Clawk, OpenClaw, MCP, DKIM/SPF/DMARC, DIDs, agent cards, skill.md

## [1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS](../videos/k72eLcYpVys.md)
`k72eLcYpVys` · AI Engineer · 2026-10-12 · q4 · practitioner · talk · also: sandboxing-execution, testing-verification

Kevin Orellana (AWS) has a coding agent fuzz-test a sandbox hosting platform with about 1,000 workflows, and shows how sandbox primitives like memory, file persistence and permissions cause failures.

- Techniques: Agent-driven fuzz testing of a sandbox platform; Results in SQLite, not markdown; Two-layer failure triage; Build a workflow suite that mirrors customer workloads
- Tools: MCP, SQLite, Amazon Bedrock AgentCore, SSH, Codex, Claude Code

## [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](../videos/Uv0nAf_7tyU.md)
`Uv0nAf_7tyU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: agent-architecture, sandboxing-execution, context-engineering

Anthropic engineers explain how they split Claude Managed Agents into a session log, a harness "brain" and swappable sandbox "hands", then start a hands-on workshop building a first agent.

- Techniques: Brain / hands / session split; Credential-injecting egress proxy; Append-only event log with pluggable context strategy; Lazy sandbox provisioning; One container per task; Custom tools as an event round-trip
- Tools: Claude Managed Agents, Claude Platform console (quick start), Claude Code, MCP, Sonnet 4.5, Opus 4.5, Haiku, Sonnet

## [Turning My Obsidian Vault Into a Local AI Engineer — Filip Makraduli, Superlinked](../videos/Ndp5VaqFrl0.md)
`Ndp5VaqFrl0` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: local-ai, inference-serving, security-guardrails

Filip Makraduli (Superlinked) shows a privacy-first setup: a self-hosted MCP tool server runs OCR, redaction and extraction on sensitive documents in your own cloud, so a Claude Code agent only sees the cleaned output.

- Techniques: MCP tool server in front of private inference; Per-worker batching instead of a shared queue; Multi-model hot-swapping on one GPU; Stateless tools-only MCP server over streamable HTTP; Check thinking-token settings per model in tool pipelines; Warm-model-aware routing (roadmap)
- Tools: MCP, Claude Code, Obsidian, Superlinked, Terraform, Helm, Kubernetes, Docker, Claude Co-work

## [Why I’m Switching From Python to Docker Agent for AI Agents](../videos/Mph1H5u3yeA.md)
`Mph1H5u3yeA` · Better Stack · 2026-10-12 · q3 · intro · review · also: multi-agent, agent-architecture

Better Stack walks through Docker Agent, an open-source Docker tool that defines agents in YAML, runs them with one command, and serves them over A2A. Demoed with an on-call incident and a Battleship match between two models.

- Techniques: Define an agent as a YAML file; Least-privilege agent split behind A2A; Serve an agent as A2A on a port; Install Docker Agent; Share an agent as an image
- Tools: Docker Agent, Docker Desktop (4.63+), Docker model runner, Docker Hub, Homebrew, A2A protocol, MCP, Claude Haiku 5.5, GPT-6 Luna, Kimi K3, OpenAI, Anthropic

## [Building AI Agents with Real-Time Web Data — Yohan Raju, Bright Data](../videos/IK8cC4FScps.md)
`IK8cC4FScps` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: rag-retrieval, data-engineering

Bright Data's Yohan Raju argues that live web data (scrapers, anti-bot handling, and an MCP endpoint with 60+ tools) lets AI agents answer questions that pre-indexed RAG cannot, then demos an Amazon-plus-Reddit buy/no-buy agent.

- Techniques: Live-vs-indexed query routing; Response caching for time-stable answers; One MCP endpoint with many scraping tools; Search-then-scrape chaining; Decision agent over multi-source API data; Record validation and medallion staging
- Tools: Bright Data MCP server, Bright Data Web Unlocker, Bright Data Browser API, Claude Code, Claude, GPT, Gemini API, LangChain, Google Colab-style notebook, Glassdoor, Amazon, Reddit

## [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](../videos/KhRjivBSwiw.md)
`KhRjivBSwiw` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: context-engineering, evals, data-engineering

TypeDef's talk and workshop argue that data and code agents need a computed, traversable context graph; deterministic structure comes first, and agents still default to grep unless tools are shaped and measured.

- Techniques: Deterministic structure first, LLM last; Layered extraction ladder for code; Persistent typed graph with subgraph traversal; Blast-radius tool before edits; Incremental re-indexing keyed to changed files; Isolated data clones for evals, with injected bugs; Tool renaming and shape-matching; Consistency and adoption metrics; Many small focused LLM questions; Eval set pinned to a snapshot, with near-failing tasks
- Tools: Neo4j, Cypher, tree-sitter, rustdoc JSON, Pydantic AI, pydantic evals, Fennec, OpenRouter, Logfire, dbt, Snowflake, Databricks

## [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](../videos/ZyC56eV8sVw.md)
`ZyC56eV8sVw` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: security-guardrails, governance-compliance, coding-agents

A two-hour Snyk workshop on AI security basics: OWASP LLM Top 10, shadow AI and AI bills of materials, AI threat modeling, MCP and skill supply-chain risk, and secure-by-default coding hooks.

- Techniques: Treat LLM input and output as untrusted data; Read-only database views for agents; Approval gate for high-risk actions; Full action logging plus a background log scanner; Scan-fix-rescan agent hook; Pre-install scanning of MCP servers and skills; AI-BOM inventory with query by component; Security requirements inside the prompt
- Tools: Snyk agent-scan (MCP and tool scanner), Snyk AI-BOM (CycloneDX-style inventory), Gandalf (Lakera) prompt-injection game, Claude Code, Cursor, Windsurf, OpenClaw, CycloneDX, SPDX, STRIDE, MITRE ATLAS, uvx

## [Vector Isn't Enough: Hybrid Search & Retrieval — Jeff Vestal & James Williams, Elastic](../videos/ksjwtQop4os.md)
`ksjwtQop4os` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: rag-retrieval, evals

Hands-on Elastic workshop on why hybrid search (BM25 plus dense vectors, fused with RRF or linear weights, then reranked) beats vector-only retrieval for RAG and agent tool use.

- Techniques: Reciprocal Rank Fusion (RRF) hybrid search; Linear combination with min-max normalisation; Filter before ranking; Retrieve then rerank in one request; Search templates routed by an LLM (poor man's auto-tuning); Semantic_text with default sentence chunking; LLM answer with citations from retrieved sources; Index-description tool for agents; Point-in-time pagination
- Tools: Elasticsearch (serverless), Kibana / Discover, Elastic Inference Service, Jina embedding and reranking models (Elastic acquisition), Agent Builder (Elastic agent platform), ES|QL, Jupyter notebooks, Elastic workflows and MCP endpoint

## [Can Your Agent Hear You Now? Building Live Voice Agents with Gemini — Thor Schaeff](../videos/xfPVBzDYjH4.md)
`xfPVBzDYjH4` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: voice-multimodal, models-research

A Google DeepMind developer-experience lead demos the Gemini Live API for real-time voice and vision agents, covering native-audio sessions, tool calls, live translation and stateful image generation. Mostly a product showcase with a few useful architecture points.

- Techniques: Stateful WebSocket session for real-time multimodal agents; Tool call from a live voice agent to a slow generator; Chaining generations with the previous interaction ID; Native audio vs cascaded voice pipeline
- Tools: Gemini Live API, Gemini 3.1 Flash Live, Gemini 3.5 Live Translate, Gemini TTS, Nano Banana Lite, Omni Flash, Lyria 3, Gemini Interactions API, Google AI Studio, LiveKit, Pipecat

## [AI Agents Don't Read Your Policy Docs. They Hit Your APIs — Gravitee](../videos/7v2myBde05o.md)
`7v2myBde05o` · AI Engineer · 2026-10-11 · q2 · practitioner · review · also: security-guardrails, governance-compliance, infra-cost-scaling


- Techniques: Per-task scoped agent identity via token exchange; Gateway-level rate limiting on agent requests; Semantic cache keyed on prompt similarity; Pre-request prompt size and relevance policies; Narrowing MCP servers to a per-agent tool subset; Export gateway telemetry to existing observability stack
- Tools: Gravitee AI Gateway, Anthropic Claude (Sonnet), Groq (inference), Databricks, Redis (built-in semantic cache), MCP (Model Context Protocol), A2A (agent-to-agent protocol), OpenTelemetry, Datadog, Splunk, Prometheus, Kubernetes

## [Zero Cold Starts: Serverless AI Agents on Akamai Functions — Thorsten Hans](../videos/Zf_e45GiNCE.md)
`Zf_e45GiNCE` · AI Engineer · 2026-10-11 · q3 · intro · demo · also: sandboxing-execution, infra-cost-scaling

Thorsten Hans (Akamai) demos building MCP servers and a Vercel AI SDK agent as WebAssembly apps on Spin, deployed to Akamai Functions for near-zero cold starts and global distribution.

- Techniques: Compose MCP servers from Wasm components; Snapshot a pre-initialized interpreter into the Wasm artifact; Edge-deployed agent using a Wasm framework with a remote model; Local-to-cloud parity via Spin abstractions
- Tools: Spin, WasmTime, WASI, wasmcp, Akamai Functions, StarlingMonkey, Vercel AI SDK, Ollama, MCP Inspector, SQLite, OCI registries

## [An AI Future Without the Lock-In — Remy Guercio, Tailscale](../videos/s-glGHAa1a4.md)
`s-glGHAa1a4` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: infra-cost-scaling, governance-compliance

Tailscale's Remy Guercio argues for "ROI maxing" over token maxing: keep choice at every AI layer through an identity-aware AI gateway (Aperture) to avoid lock-in. Mostly a product pitch.

- Tools: Tailscale, Aperture (Tailscale AI gateway), WireGuard, TSNet, Entra, Okta, Anthropic API, OpenAI API, Vercel AI gateway, AWS Bedrock, Codex, Claude Code

## [Building on the Codex Harness — Dominik Kundel, OpenAI](../videos/9WiBJRO84yY.md)
`9WiBJRO84yY` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: coding-agents, agent-architecture, context-engineering

OpenAI's Dominik Kundel shows how to build your own client on the open-source Codex app server, the JSON-RPC protocol that wraps the Codex harness, and gives three rules for customizing it safely.

- Techniques: Append developer instructions instead of replacing the system prompt; Deferred dynamic tools with tool search; Pin and bundle the harness binary; Per-thread config overrides; Integrate by delegating to the coding agent; Choose exec or app server by parallelism and interactivity
- Tools: Codex app server, Codex CLI, Codex exec, Codex desktop app, Python SDK (Codex), Agent Client Protocol (ACP), LM Studio, Ollama, Electron, Cloudflare Doom WASM renderer, T3 Code, Claude Code Codex plugin

## [Designing CLIs for Agents, Not Humans — Pedro Lopez, Airbyte](../videos/3wj6sgbi1YA.md)
`3wj6sgbi1YA` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: coding-agents, security-guardrails

Airbyte's Pedro Lopez on building a thin MCP server and CLI for agents: a small tool surface, OAuth-only auth, JSON in and out, non-interactive credentials, and skills shipped with the CLI.

- Techniques: Thin interface over a shared API spec; Minimal tool surface with progressive discovery; OAuth-first MCP auth with a connect-link flow for third-party credentials; Agent-friendly CLI contract; Ship a skill with the CLI, with progressive references; Use failure patterns as a design signal
- Tools: MCP, CLI, OAuth, OpenAPI, jq, Claude Desktop, Claude custom connectors, ChatGPT app store, Airbyte AI Agents context store, Zendesk, Stripe, HubSpot

## [Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge](../videos/cSz7aL2nl2U.md)
`cSz7aL2nl2U` · AI Engineer · 2026-10-10 · q2 · practitioner · talk · also: context-engineering, memory, rag-retrieval

Gil Feig (Merge) argues every company needs a "context graph" (a company brain of synced data, live lookups, memory, skills) and lays out how to route, cache, and trace it. Conceptual talk with a closing product plug.

- Techniques: Split retrieval: live MCP vs. synced vector cache; Router plus summarizer; Skills and memory first; Freshness SLA check on cache; Derived-context write-back; Bounded live pulls; Provenance metadata on every record
- Tools: MCP (Model Context Protocol), Zendesk, Jira, NetSuite, Stripe, Qualtrics, vector database (unnamed), Merge Unified, Merge Agent Handler, Merge Gateway

## [How a Remote Company Builds AI Fluency — Em Shreve, Automattic](../videos/3XI90A3ENSg.md)
`3XI90A3ENSg` · AI Engineer · 2026-10-09 · q3 · intro · talk · also: enterprise-adoption, skills-self-improvement

Automattic's two-week, in-person AI enablement cohorts (50% facilitated workshops, 50% real project work) and how they scale learning through alumni champions, meetups and a shared MCP and skills hub.

- Techniques: Two-week immersive cohort with a 50/50 split; Living curriculum; Internal MCP server as a shared hub; Tool-agnostic shared skills directory; Champions, regional meetups and ride-alongs; Staged post-program surveys
- Tools: Claude Code, Codex, open code, MCP, Zendesk, WooCommerce, WordPress AI

## [Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto](../videos/jJQoVkd5yLg.md)
`jJQoVkd5yLg` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: product-ux, observability

Reducto deleted its one-tool-per-endpoint MCP server after a team rollout showed agents were confidently wrong; the rebuild uses fewer workflow-shaped tools, legible uncertainty, and session logs that feed back into guidance.

- Techniques: Workflow-shaped MCP tools instead of endpoint wrappers; Per-step next-action guidance in tool responses; Snapshot / live-state tool with specific error codes; Confidence and provenance in tool outputs fed back to the model; Evals that score clarifying questions as correct behaviour; Session logging, then mining for override and low-confidence signals; Require an explanation of what was built and why
- Tools: Claude Code, MCP, Slack, Notion, Circleback

## [Why Your AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND](../videos/toq-jyGLZDk.md)
`toq-jyGLZDk` · AI Engineer · 2026-10-08 · q2 · intro · talk · also: multi-agent, security-guardrails

Vlad Luzin (BAND) argues that agent-to-agent communication is a distributed-systems problem that MCP, A2A and chat platforms don't solve, then pitches BAND's hosted interaction layer.

- Techniques: Loop engineering with two stateful agents; Contact request with bilateral consent before agent discovery; Shared conversational space with human visibility; Runtime ID binding across agent frameworks
- Tools: Claude, Claude Code, Codex, LangGraph, CrewAI, MCP, A2A, ACP, Slack, Microsoft Teams, Discord, WhatsApp

## [From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer](../videos/u-o0sW9nwmk.md)
`u-o0sW9nwmk` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · also: skills-self-improvement, security-guardrails

Rafal Wilinski (Runlayer) argues agents should distill successful and failed runs into skills, serve them via MCP as a governed company-wide library, and reports a 36% to 100% success jump after one distilled skill.

- Techniques: Trace-to-skill distillation; Learn from failures too; Checks before publishing a skill; Remote MCP skill registry with tool-based access; Group similar runs before distilling
- Tools: MCP, Claude Sonnet 4.6, Voyager, Chromium, AWS Lambda, npx skills

## [How AI Agents Pay: Checkout in ChatGPT and Google AI Mode — Sam Parsons, PayPal](../videos/c5U-XbbEN-g.md)
`c5U-XbbEN-g` · AI Engineer · 2026-10-06 · q2 · intro · talk · also: product-ux, security-guardrails

PayPal Enterprise Payments (Braintree) walks through three ways merchants accept payments from AI agents: ChatGPT instant checkout, Google AI Mode via UCP, and MCP apps with external checkout.

- Techniques: Host-side tokenization with scoped payment tokens; MCP app widget that triggers host-native checkout; Discovery file plus session endpoints for headless checkout; External checkout handoff linked to a session
- Tools: MCP Apps, Agentic Commerce Protocol (ACP), Universal Commerce Protocol (UCP), Google Pay, Braintree / PayPal Enterprise Payments, ChatGPT, Claude connectors, Goose

## [How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker](../videos/ZUZVNKFSmTM.md)
`ZUZVNKFSmTM` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: security-guardrails, sandboxing-execution

Docker engineer Jim Clark argues that agent safety comes from small, task-shaped sandboxes fed through an MCP gateway, with zero credentials inside the sandbox. The talk also pitches Docker's SBX product.

- Techniques: Role-split sandboxes for untrusted-input pipelines; Intent-scoped sandbox per task; Single MCP gateway as the policy point; Credentials held outside the sandbox; Cross App Access token exchange; Progressive tool disclosure
- Tools: Claude Code, Codex, MCP, MARP, Mermaid, Docker SBX, OpenCode, Gemini

## [I Gave a Robot Duck a 15MB AI Brain (Needle 3)](../videos/KQcQ7P78eTI.md)
`KQcQ7P78eTI` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: training-finetuning-rl, local-ai, evals

Walkthrough of Cactus Compute's Needle 3 on-device tool-calling model: a size-adjustable layer ladder, local fine-tuning on a robot-duck task, and a 49-prompt held-out eval (27% base, 84% fine-tuned 20-layer).

- Techniques: Closed-set tool dispatcher; Layer-truncatable model (intelligence ladder); Rule-categorised synthetic training data; Hand-written held-out scoreboard; Split controller from the LLM decision layer; Local fine-tune over LAN to a GPU box
- Tools: Needle 3, Needle 2, Cactus Compute fine-tuning platform, OpenDuck Mini, MuJoCo, DeepSeek V4 Flash, NVIDIA RTX 5090, ESP32, Pebble Index Ring, BDX droids (Disney)

## [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](../videos/33Oct2hqGnk.md)
`33Oct2hqGnk` · AI Engineer · 2026-10-05 · q2 · practitioner · talk · also: agent-architecture, sandboxing-execution, evals

AWS's Sandhya Subramani demos an agent that writes its own tools and sub-agents at runtime using three built-in tools (editor, shell, load-from-directory) plus a system prompt, then argues that evals and sandboxing are required before trusting it.

- Techniques: Meta-tooling bootstrap (three tools + system prompt); Check-before-write rule for generated tools; Self-repair on error; Sub-agent topology choice (swarm, graph, workflow); Layered agent evals; Four-part guardrail stack for self-modifying agents
- Tools: Strands Agents (AWS open source agent harness, Python and TypeScript), Python, OpenTelemetry (named as telemetry), Strands code-execution sandbox (recent feature, named in talk)

## [Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa](../videos/cKhpeEBnT1o.md)
`cKhpeEBnT1o` · AI Engineer · 2026-10-04 · q2 · practitioner · talk · also: rag-retrieval, coding-agents

Exa's forward-deployed engineer explains why coding agents miss recent changes past their model cutoff, and how query-targeted web search snippets, plus explicit search rules, close that gap. Partly a product pitch.

- Techniques: Two-part search instructions for agents; Query-targeted highlight extraction; Full retrieval trace logging; Natural-language schema for structured output
- Tools: Exa search API, Exa Agent, MCP server, Claude Code, CodeRabbit, Cursor

## [No, That's Not a Software Factory — Ryan Cooke, WorkOS](../videos/HvboD89DyQ8.md)
`HvboD89DyQ8` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: software-factory, context-engineering, skills-self-improvement

Ryan Cooke (WorkOS) on why a sandbox plus coding agent is not a software factory. Build around outcome metrics, webhook-driven product workflows, and an internal MCP gateway.

- Techniques: Outcome-based factory metrics; Webhook-driven ticket pipeline; Agent plan refresh after each step; Agent-drafted PRD with human approval gate; Context-rich MCP gateway; Session mining for skill gaps
- Tools: Linear, Slack, GitHub, Notion, Snowflake, Cloudflare sandboxes, Claude Code, Devin, OpenCode, MCP

## [An Interaction Is All You Need — Ivan Leo, Google DeepMind](../videos/8aVbXXvJUY4.md)
`8aVbXXvJUY4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: agent-architecture, sandboxing-execution, security-guardrails

Google DeepMind's Ivan Leo presents the Interactions API and Managed Agents: server-side state via interaction IDs, persistent sandboxes via environment IDs, and a credential-injecting proxy. Mostly a product walkthrough with a few reusable patterns.

- Techniques: Server-side conversation state via interaction ID; Reattach to a persistent sandbox via environment ID; Proxy-side credential injection; Freeze a tuned environment as a named agent; Local-to-cloud skill packaging; Strongly typed output parsing
- Tools: Interactions API, Managed Agents, Antigravity agent harness, Gemini API CLI, AI Studio, Google Search tool, URL context tool, GCS, GitHub

## [MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](../videos/pAnLpiAG6Es.md)
`pAnLpiAG6Es` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: context-engineering, coding-agents

Apify's CEO argues MCP's problems come from agent harnesses, not the protocol. He covers progressive tool discovery, code mode, and CLIs, then pitches MCPC, a CLI wrapper for MCP.

- Techniques: Progressive tool discovery; Code mode for tool calls; Keep large or sensitive tool output out of context; Wrap MCP in a CLI and give the agent bash; Async tool invocation with detach and poll; Connector evals
- Tools: MCP, MCPC, Claude Code, Claude Tool Search Tool, Cloudflare code mode, Bash, jq, Terminal Bench

## [I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j](../videos/oUZEt4EiPbk.md)
`oUZEt4EiPbk` · AI Engineer · 2026-10-04 · q2 · intro · demo · also: memory, agent-architecture, sandboxing-execution

Neo4j's Jeremy Adams builds a personal agent on a Raspberry Pi 4B: NanoClaw in Docker, WhatsApp as the channel, cloud LLMs, and graph memory, with a live demo and an offline capture mode for conference Wi-Fi.

- Techniques: Edge orchestrator, cloud brain; Container per agent process; Messaging app as the agent front end; Graph database as an MCP tool; Offline-first capture with deterministic parsing and later sync; Typed entity memory schema written as a skill; Batch distillation of chat history
- Tools: Raspberry Pi 4B, NanoClaw, OpenClaw, Claude Agent SDK, WhatsApp, Telegram, Docker, Neo4j, Neo4j Aura, Cypher, MCP, Neo4j agent memory service

## [Dashboards Are Dead — Sarah Simionescu, Composio](../videos/YiFqcu9YA38.md)
`YiFqcu9YA38` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: context-engineering, product-ux

Composio's Sarah Simionescu argues agents should replace dashboards, and that MCP servers need task-scoped tool discovery to work. Vendor pitch with a mock-up demo.

- Techniques: Task-first tool discovery; Parallel fetch after planning; Keep bulky results out of context; Schema-first exploration before querying; Bug-report prompt to an agent with connected tools
- Tools: Composio (MCP, CLI, native tools, Composio Search, Composio Remote Workbench), Claude, MCP (Model Context Protocol, announced by Anthropic Nov 2024), Datadog, Sentry, Slack, GitHub, Jira (JQL), VS Code, PostHog, Metabase, SQL

## [Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band](../videos/UOcHfR3_tys.md)
`UOcHfR3_tys` · AI Engineer · 2026-10-04 · q2 · practitioner · talk · also: multi-agent, agent-architecture, governance-compliance

Vendor talk by Band's CTO arguing that multi-agent coordination needs a conversation-level collaboration layer (rooms, consent, routing, governance), not just MCP or A2A, then demoing that product.

- Techniques: Bilateral consent before agent-to-agent contact; Rooms and channels with deterministic routing as the agent primitive; Network-level traffic capture for cost and attribution; Live architecture layout reporting from agents; Human-in-the-loop pings and manager kill switch
- Tools: Band (collaboration layer / platform, speaker's company), Jam (desktop app built on Band, also called 'GEM' near the end of the transcript; the name is ambiguous in captions), Claude Code, Codex (OpenAI), LangGraph (LangChain), MCP (Model Context Protocol), A2A (Agent-to-Agent protocol), ACP (protocol, named without detail), Telegram, Discord, Slack, WhatsApp

## [DBX Is Almost the Perfect Free Database Client](../videos/b6rVCrBPbe8.md)
`b6rVCrBPbe8` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: dev-tools, security-guardrails

Hands-on review of DBX, a free desktop database client with an optional MCP server that lets coding agents query saved connections; the reviewer praises the workflow but flags plaintext passwords in its local SQLite file as a blocker for production credentials.

- Techniques: Stand up a multi-engine local test rig; Add a connection with a test-before-save step; Register the DBX MCP server with Claude Code and check it appears; Agent prompts used for smoke testing; Audit a local client's credential store before storing production secrets
- Tools: DBX (free desktop database client, version not stated), DBX MCP server (separate binary), Claude Code (used to register and call the MCP tools), Docker Compose, MySQL, Redis, MongoDB, Postgres, SQLite (dbxdb file), DuckDB, Navicat, DataGrip

## [Github #1 Trending Skill's Author Just Fixed Claude's Design Problem](../videos/Ow_z94c3wKk.md)
`Ow_z94c3wKk` · AI LABS · 2026-10-02 · q2 · practitioner · review · also: coding-agents, vibe-coding-app-building

Walkthrough of Inspo, a free MCP server of 832 captured sites with per-site design.md files that lets coding agents pull real references before designing. Sponsored segment; tested on one demo page.

- Techniques: Pre-build style menu; Reference provenance check; Filter-scoped reference search; Cap reference study depth; Install Inspo in user scope; Split design and animation into separate MCP lookups
- Tools: Inspo (MCP server, free, no account or API key), UI Skills MCP server, Emil Kowalski animation skill, Mengto scroll animation skill (name as transcribed), Hallmark design skill (name as transcribed), AI Labs Pro design system (community resource), Claude Code, Manid (sponsor, agent tools API gateway)

## [IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork](../videos/q-WOjZhOMCA.md)
`q-WOjZhOMCA` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance, agent-architecture

Sarthak Aggarwal (DecaWork) argues agents should be governed like employees: each needs an identity, scoped short-lived capabilities, a policy gate outside the model, and receipts plus fast revocation.

- Techniques: Typed plan before evidence (plan-then-execute split); Out-of-model policy gate per tool call; Runtime agent identity card; Short-lived, audience-bound capability tokens
- Tools: Microsoft 365 Copilot, Microsoft Agent 365, Okta, AWS AgentCore Identity, MCP, A2A, Replit

## [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../videos/qdAkxLoYNI8.md)
`qdAkxLoYNI8` · AI Engineer · 2026-09-18 · q2 · intro · review · also: context-engineering, rag-retrieval, pr-code-review

Unblocked vendor talk arguing coding agents need an organizational context engine over code, PRs, Slack and docs, with cited sources; one live comparison, mostly product pitch.

- Techniques: Cited-source answers for agents; With/without context comparison; Expertise-weighted review comments; Query historical PR data with an open-source engine; Engineering social graph from review edges
- Tools: Unblocked, Claude Code, Claude 4.8, Slack, Notion, GitHub, MCP, Document Query Engine, context engine simulator

## [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../videos/XsvUhpnHepE.md)
`XsvUhpnHepE` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: voice-multimodal, infra-cost-scaling, token-cost-efficiency

Oxylabs' Giedrius Šteimantas argues web-using agents need a scraping infrastructure layer: use browsers only when required, validate content before it reaches the LLM, and fix the failing discovery and purchase stages of a shopping agent.

- Techniques: Validate page content before the LLM sees it; Search API for discovery, not a browser; Tiered web access: API first, browser last; Markdown and geolocated output from the scraper; Drop-in managed browser for Playwright MCP
- Tools: Playwright MCP, Oxylabs Fast Search API, Oxylabs Web Scraper API, Oxylabs Headless Browser

## [500 Skills, Zero Fine-Tuning: LinkedIn's Playbook for AI Agents — Ajay Prakash, LinkedIn](../videos/9wZpvF3QleU.md)
`9wZpvF3QleU` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: skills-self-improvement, context-engineering, coding-agents

LinkedIn's Ajay Prakash on an internal MCP server that serves tools plus self-contained markdown "playbooks" teaching coding agents company workflows, kept current by a PR-based self-update loop.

- Techniques: Playbooks as MCP-served instruction docs; Compose playbooks by reference; Session-end playbook self-update PR; Three meta tools for large tool catalogues; Central plus repo-local instruction split; Single pre-installed local MCP server with hourly auto-update
- Tools: MCP, Claude Code, GitHub Copilot, Cursor, Airflow, Jira, Slack

## [Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google](../videos/9R--1tg45Jg.md)
`9R--1tg45Jg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: security-guardrails, data-engineering

Google's MCP Toolbox team on separating dev-time from production agent tools. Keep credentials, raw SQL and user identity out of agent control, and use predefined, identity-bound, read-only tools.

- Techniques: Source primitive for connection secrets; Predefined custom SQL tools; Read-only enforcement at the driver level; Blast-radius limits on sources; Bounded and authenticated parameters for identity; Read/write tool split with approval gates; Actionable, retryable tool errors and flat inputs
- Tools: MCP Toolbox for Databases, Google Managed MCP, Model Armor, EvalBench, LangChain, Gemini CLI, Claude Code

## [Rebuilding the web for agents — Liad Yosef, MCP Apps](../videos/waI44NP1abk.md)
`waI44NP1abk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux

Liad Yosef (MCP Apps co-maintainer) argues the web is shifting to assistant-driven, headless-plus-UI interaction, and that agent-readiness should be measured from agents' real behaviour, not from best-practice files.

- Techniques: Expose UI as MCP Apps for the last mile; WebMCP: publish page tools instead of screenshots; Measure agent paths, not best-practice checklists; Per-domain AI Catalog.json plus a queryable directory; Design an API-first surface, then add UI for the last mile
- Tools: MCP Apps, WebMCP, llms.txt, AI Catalog.json, Agentic Resource Discovery standard, auth.md, pricing.md, x402, Aura Journey, Aura readiness benchmark, Claude Code, ChatGPT

## [Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked](../videos/HvMyYLTfvhg.md)
`HvMyYLTfvhg` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: context-engineering, memory, agent-architecture

Jeff Ng (Unblocked) argues agent infrastructure is now easy to assemble, so the real gap is organizational context. He demos a context engine that feeds agents synthesized, permission-scoped knowledge instead of raw MCP results.

- Techniques: Durable per-step checkpoints for agent runs; Isolated sandboxes for agent and third-party code; Context engine queried before the agent reasons; Synthesized context over raw tool results
- Tools: Cloudflare, Vercel, Mastra, Flu (transcript spelling of the framework), Linear, Slack, GitHub MCP, Claude Code, Codex, Unblocked context engine

## [ACP: The Universal Remote Control for AI Agents — Alex Hancock, Block](../videos/YkNulwcc5jk.md)
`YkNulwcc5jk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, coding-agents

Alex Hancock (Block, Goose and MCP maintainer) argues for ACP, an open client-to-harness protocol, so one client can drive any agent over local stdio or remote HTTP/WebSocket.

- Techniques: Standard client-to-harness protocol (ACP); Underscore-prefixed custom methods, then standardize by usage; Transport swap with unchanged messages; Split the agent stack into four movable parts
- Tools: ACP (Agent Client Protocol), Goose, Zed, JetBrains IDEs, MCP (Model Context Protocol), JSON-RPC, stdio, HTTP, WebSocket

## [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../videos/G7cgLjZtmMU.md)
`G7cgLjZtmMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, evals, security-guardrails

Best Buy's Ahnaf Priyo maps the agentic commerce protocol stack (MCP, A2A, ACP, UCP, AP2), argues for pushed product feeds and checkout APIs over browser agents, and makes the case for behavior and protocol evals with a live cat-bakery demo.

- Techniques: Push product feed to platforms; Checkout as an explicit state machine; Scoped, single-use, revocable payment mandate; Layered evals for conversational commerce agents; Timeline view of agent calls; Agent skills for domain roles
- Tools: MCP, A2A, ACP, UCP, AP2, Cerebras, ChatGPT, Gemini, Chrome DevTools

## [Voice Agents Can Just Do Things — Charlie Guo, OpenAI](../videos/OpY6MmZFeHo.md)
`OpY6MmZFeHo` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: voice-multimodal, product-ux

Charlie Guo (OpenAI) argues voice agents need not always talk back and lays out three voice modes (speech-to-speech, speech-to-action, event-to-speech), with GPT Realtime 2 as the example stack.

- Techniques: Three-mode voice design; Expose app verbs as tools; Escalating attention ladder; Preamble prompting; Native audio streaming; Role-first voice design checklist
- Tools: GPT Realtime 2, OpenAI Realtime API, Codex, ChatGPT advanced voice mode, CarPlay, Google Maps, Spotify

## [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../videos/VjEP0xqTUI0.md)
`VjEP0xqTUI0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, agent-architecture, data-engineering

Arman Vaziri (Ramp) on building go-to-market orchestration: an internal CDP, durable background agents on Temporal, scoped retrieval, and an MCP that turns employee experiments into productized use cases.

- Techniques: Durable thread with checkpointed activities; Account-scoped hybrid retrieval; Per-agent tool scoping with human pause and resume; System skills plus user text instructions; Nightly per-entity fan-out; Persist derived entity matches; Shared tool surface via MCP plus usage mining; Explore vs exploit with guardrails across channels
- Tools: Temporal, Postgres, Kafka, TurboPuffer, dbt, Snowflake, reverse ETL, MCP, GPT-3.5

## [Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker](../videos/zaGyGgLW3SM.md)
`zaGyGgLW3SM` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, sandboxing-execution

Docker's Tushar Jain argues agent safety, not intelligence, is the blocker, and demos a sandbox runtime with stub credentials, scoped per-task sandboxes, and an unbuilt intent-based access prototype.

- Techniques: Run the agent inside an untrusted VM boundary, with policy enforced outside it; Split a monolithic agent into per-task sandboxes; Inject stub credentials, with real secrets added outside the sandbox; Just-in-time narrowed tools over existing MCP servers; Capability escalation through an intent tool; Same policy locally and in the cloud; Parallel fan-out of scoped sandboxes
- Tools: SPX (Docker runtime; name as spoken, install via brew), Docker, Codex (OpenAI coding agent), Claude / Anthropic models, GitHub, Slack, Notion MCP, MCP, OpenClaw (spoken as open claw), OpenCode (spoken as open code), GLM 5.2 (open model)

## [MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed](../videos/lbaXnx0KLA8.md)
`lbaXnx0KLA8` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: product-ux, context-engineering

Dustin Mihalik (Indeed) shares lessons from building MCP Apps for Claude and ChatGPT: model-visible data parity, separate data from rendering, and feeding UI interactions back to the model.

- Techniques: Model-visible data parity; Description steering of UI vs text output; Explore/render split; Interaction feedback via update model context; Render tools that take model-generated rationale; Small composable tool set
- Tools: MCP Apps, Apps SDK (OpenAI), update-model-context method, Claude, ChatGPT, CareerScout (Indeed internal agent)

## [x402 isn’t good (yet) — Jan Curn, Apify](../videos/h6mi88VrPtQ.md)
`h6mi88VrPtQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: governance-compliance, security-guardrails

Apify's CEO lists x402 agent-payment flaws (double-spend before settlement, HTTP 402 vs MCP 401 conflict, poor fit for metered jobs) and his team's workarounds, including an agent-facing markdown gateway.

- Techniques: Charge-then-refund for metered jobs; Work-after-settlement for near-zero-cost calls; Agent-facing markdown instructions plus prepaid token; Batch micropayments via escrow and signed vouchers; Local wallet with cryptographic key and QR code
- Tools: x402 (Coinbase), MPP (Stripe, Tempo), HTTP 402 Payment Required, MCP, Apify actors, agi.apify.com, Coinbase facilitator

## [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../videos/6pbQgnJ9Voc.md)
`6pbQgnJ9Voc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, product-ux, security-guardrails

Exa's co-founder argues go-to-market is an AI engineering data problem and shows the internal agents, ICP dashboard, and JeffBot clone that run his GTM team.

- Techniques: Decision-log to eval calibration for a personal proxy agent; Caller-scoped agent permissions; Semantic web search as a segmentation pipeline; API/MCP-first, then customize the SaaS; Signal-triggered alerts on customer events
- Tools: Exa, Opus 4.5, Slack, Salesforce MCP

## [Why Your AI Agent Needs a Wallet: USDC and Nanopayments — Harshal Bhangale, Circle](../videos/xKzU_3riL6s.md)
`xKzU_3riL6s` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: governance-compliance, infra-cost-scaling

Circle engineer argues agents need wallets: x402 pay-per-request with USDC nanopayments and wallet-enforced spend caps, shown in a live Claude Code demo. Vendor pitch with a real but partly failed demo.

- Techniques: Wallet-enforced spend caps; HTTP 402 pay-per-request (x402); Off-chain signed authorizations with later settlement
- Tools: Claude Code, Circle Agent Wallet, x402, USDC, Circle Gateway, Nanopayments, Gmail, Blockrun (data provider), Polymarket data

## [Teaching agents to pay — Anna Spysz, Stripe](../videos/A-zeQiYkmXk.md)
`A-zeQiYkmXk` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: security-guardrails, governance-compliance, product-ux

Stripe engineer builds an agentic-commerce agent to buy headphones, covering the Universal Commerce Protocol, merchant manifests, shared payment tokens, persona effects on behavior, and a guardrail checklist.

- Techniques: Merchant capabilities manifest at /.well-known; Structured catalog and policy JSON; Attribute-match decision logging; Persona-driven behavior control and A/B testing of system prompts; Scoped payment token instead of raw credentials; Provider-enforced transaction limits; Agent commerce guardrail checklist
- Tools: Universal Commerce Protocol (UCP), Stripe payments, Google Pay, Apple Pay, shared payment token

## [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../videos/V_5bn4q-vAI.md)
`V_5bn4q-vAI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: context-engineering, product-ux, coding-agents

Christopher Burns (Inth) on making LLMs recommend and correctly use his open-source cookie-banner library by shipping agent-friendly docs: hand-written llms.txt, markdown twins, web MCP, and grep-able docs inside node_modules.

- Techniques: Hand-curated llms.txt index; Markdown twin per page with discovery header; Three ways to reach markdown; Bundle docs in the package with an agents.md pointer; Web MCP for docs; Agent-readiness checks as a loop
- Tools: LeadType, llms.txt, llms-full.txt, AGENTS.md, Next.js, Aura AI, Cloudflare agent-readiness checker, MCP

## [The End of the Static Screen: Architecting Intent-Driven UX — Gus Iwanaga, commercetools](../videos/QrMcNe2jjt8.md)
`QrMcNe2jjt8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, agent-architecture

Gus Iwanaga (commercetools) on intent-driven generative UI: an orchestrator picks data and components, and the LLM emits a validated declarative UI spec, not free-form UI. Main lessons are on placement, the component catalog as contract, and changing team roles.

- Techniques: Declarative UI spec validated against a component catalog; Three-tier control spectrum for generated UI; Intent-to-UI orchestration pipeline; Layout hierarchy with templates, built bottom-up; Synthetic query-to-component data for curation
- Tools: MCP, Zod, React, A2UI, JSON Render (Vercel), OpenUI, ChatGPT, Claude

## [Generative UI... in Python? — Jeremiah Lowin, Prefect](../videos/Krzs8GeiWTc.md)
`Krzs8GeiWTc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, vibe-coding-app-building

Jeremiah Lowin (Prefect) on Prefab, a Python DSL for composing MCP App UIs; the talk argues scoping UIs to pre-built components makes Python-only front ends viable and that streaming compact Python beats streaming JSON.

- Techniques: Return a UI component from a tool; Reactive bindings for client-side interactivity; App class with app.ui and app.tools; Agent-bypass upload via MCP app; Stream generative UI as code
- Tools: Prefab, FastMCP, MCP Apps, React, shadcn/ui, Goose

## [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../videos/Lrw0jqBNaw0.md)
`Lrw0jqBNaw0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, evals, observability

Sourcegraph's agent advocate argues DevRel must now serve AI agents as users and recommenders, and shows how to measure agent friction and recommendation rates.

- Techniques: Agent friction logging from traces; With-and-without-tool agent benchmark; Intent-split GEO prompt experiments; Agent experience report; Machine-readable authoritative content
- Tools: Sourcegraph code navigation MCP tool, CodeScaleBench (speaker's benchmark), llm.txt, MCP registries, Discord

## [When AI Agents Pay and Sellers Monetize: Building x402 Apps on AWS — Anil Nadiminti, AWS](../videos/qTZirYu9pr0.md)
`qTZirYu9pr0` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: governance-compliance, security-guardrails, infra-cost-scaling

AWS walkthrough of letting AI agents pay for content via the x402 HTTP 402 protocol, with AgentCore Payments on the buy side and WAF bot pricing on the sell side. Mostly product pitch, with some useful architecture.

- Techniques: Payment session spend caps with expiry; Deterministic payment layer decoupled from the agent loop; Key custody behind KMS, with agent-level capability only; x402 request/402/pay/retry flow; Edge bot classification and differential pricing
- Tools: AgentCore Payments, Bedrock AgentCore Gateway, Bedrock AgentCore Runtime, AWS WAF, Amazon CloudFront, AWS KMS, x402, Coinbase wallets, Stripe wallets, Base (L2 chain)

## [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../videos/ZIYYsAzaLlA.md)
`ZIYYsAzaLlA` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, context-engineering

Figma's engineer on building its first MCP server in about three months: which context format worked, how evals were automated, and how a remote server followed a local one.

- Techniques: Pick the representation the model knows best; Code plus screenshot as paired context; Reference-by-pointer via a component mapping; Two-step ask-then-act to emulate elicitation and sampling; Automated eval mixing deterministic checks and LLM judges; Local-first MCP server with an IPC bridge; Per-tool-call instructions when clients ignore server instructions
- Tools: Figma MCP server, Figma Code Connect, MCP Inspector, React, Tailwind CSS, Electron, Node.js, Cursor, VS Code, Claude Desktop

## [Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](../videos/KcVkq5L-0f0.md)
`KcVkq5L-0f0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: context-engineering, rag-retrieval

Brandon Waselnuk (Unblocked) argues AI coding agents fail on missing company context, not intelligence, and outlines context-engine design: avoid curated markdown, separate access from understanding, and use schema discovery for relational questions.

- Techniques: Derive context from systems instead of hand-curated files; Deterministic team graph from GitHub; Rules-file discovery and index; Schema-less lookup, then deterministic query; Two retrieval modes: deep research and fast unfurl; Context hydration to avoid repeated discovery searches
- Tools: MCP, GitHub, Slack, OAuth, SSO, OpenAI API, Anthropic API

## [Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node](../videos/ZyGMqdIpPoE.md)
`ZyGMqdIpPoE` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: governance-compliance, security-guardrails

Edge & Node's pitch for Ampersend, a payment and compliance layer letting agents pay for paid MCP tools and checkouts, with a sanctions-screening demo. Mostly product pitch.

- Techniques: Pre-authorization counterparty screening; Skill file as the payment-aware tool gateway; Per-call micropayment for paywalled endpoints; Prompt-level spend constraint
- Tools: x402, Shopify UCP, TRM (wallet screening), MCP, Claude Code, Claude Cowork, Ampersend, Exa, Firecrawl, Circle nano-payments

## [Building Blocks for Uber’s Software Factory— Uday Kiran Medisetty & Adam Huda, Uber](../videos/17-YSUHo6Lk.md)
`17-YSUHo6Lk` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: software-factory, pr-code-review, enterprise-adoption

Uber's engineers walk through six building blocks (model gateway, MCP gateway, agent devpods, skills marketplace, context graph, Cortana) behind its managed software factory, then show one feature built end-to-end by an agent.

- Techniques: Single gateway with middleware chain and project attribution; Progressive MCP projection (direct, discovery, CLI, generated code); Pre-warmed agent workspaces; Skill marketplace with lint, review and trace feedback; Shared context graph queried before tool calls; Split review between an inner loop and an outer loop; Managed scheduled maintenance loops with bounded output

## [TanStack Did It Again... They Fixed Charts](../videos/odbQhwcIo4Q.md)
`odbQhwcIo4Q` · Better Stack · 2026-09-02 · q3 · intro · review · also: dev-tools

Better Stack walks through TanStack Charts, a week-old framework-agnostic charting library built on a grammar-of-graphics model, and claims a much smaller bundle than Recharts and Chart.js.

- Techniques: Declare a chart as marks plus scales; Add reference lines and overlays as marks; Data-driven mark styling; Three-level theming
- Tools: TanStack Charts, React, ggplot2 (referenced as the inspiration for the grammar of graphics), Recharts (comparison), Chart.js (comparison), TanStack (library family)

## [MCP Was Wrong From The Start (They Just Fixed It)](../videos/f4mI3d-nTrI.md)
`f4mI3d-nTrI` · Better Stack · 2026-09-02 · q3 · practitioner · news · also: agent-architecture, infra-cost-scaling

Walkthrough of the MCP 2026-07-28 spec, which makes the protocol stateless: no handshake, no session IDs, explicit state handles, input-required round trips, and official tasks for long-running calls.

- Techniques: Stateless MCP tool calls; Explicit state handle; Input-required round trip; Async tasks for slow tools; Gateway routing on MCP headers; Cache hints on list calls; SDK migration
- Tools: MCP (spec version 2026-07-28), MCP TypeScript SDK v2 (separate server and client packages), MCP SDK codemod, Cloudflare Workers, Cloudflare Durable Objects, Google Cloud Run, Redis

## [I Tried Both New 30B Models... One Of Them Is a DISASTER! (Muse Glimmer & Lightning 3.5)](../videos/mzQC9UK9n84.md)
`mzQC9UK9n84` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: local-ai, evals, models-research

Hands-on test of Meta's Muse Glimmer and NVIDIA's Nemotron Lightning 3.5 (both ~30B, local via Ollama) on three agentic tasks; Glimmer passes two of three, Lightning fails all three.

- Techniques: Same-prompt, multi-round correction test; Serve two local models and drive them from an agent CLI; Expose a desktop editor to models through a custom UXP plugin; Check numbers against the source document; Treat tool-error fallback as a test case
- Tools: Muse Glimmer (Meta), Muse Spark (Meta), Nemotron Lightning 3.5 (NVIDIA), NeMo Switchyard (NVIDIA routing), D-Flash speculative decoding, Ollama, OpenCode, Opus 5 (reference model), Adobe Premiere Pro, Adobe Bridge, UXP plugin (custom), Epidemic Sound MCP server

## [This Is How Forward Deployed Engineering Is Actually Done](../videos/AD-EmZ3v6-g.md)
`AD-EmZ3v6-g` · AI LABS · 2026-09-02 · q2 · intro · tutorial · also: enterprise-adoption, product-ux, evals

How to do forward deployed engineering: audit a business process before building, sort each step into software, model or human, then eval against real cases. Useful method, but includes a sponsored segment and unsourced stats.

- Techniques: Shadow-and-document the process; Three-filter triage per step; Connect to existing systems instead of migrating; Keep process steps visible with checkpoints; Labelled-case eval loop; Value-and-error-cost accounting; Process audit as the first deliverable
- Tools: Claude Code (used for the internal chatbot case study), MCP (Model Context Protocol), Notion (named as the example system for MCP connection), Slack, Cursor (as a company example), OpenAI (as a company example), Anthropic (as a company example), Dex (job-matching sponsor; named in a sponsored segment)

## [MCP is Dead...](../videos/Rrju5Y0iiBM.md)
`Rrju5Y0iiBM` · Kai Explains · 2026-09-02 · q3 · practitioner · news · also: context-engineering, security-guardrails

Kai Explains argues "MCP is dead" misreads the moment: the protocol's own pain points (tool-definition context bloat, session state) were real, and a July 2026 spec rewrite addresses them, while adoption kept growing.

- Techniques: Cap the number of MCP servers attached to an agent; Diagnose tool-definition bloat before blaming the protocol; Design remote MCP servers to be stateless for load balancing; Vet community MCP servers before installing
- Tools: Model Context Protocol (MCP) with July 28 2026 spec, MCP SDKs (Anthropic-maintained; one other SDK referenced), GitHub MCP server, Filesystem MCP server, Notion (database connector), Hyperframes (video framework), Google Cloud managed remote MCP servers, JetBrains, Cursor, Windsurf, Replit

## [Anthropic's Model Hardware Standard: Everything You Need To Know](../videos/UEd-I_67qJI.md)
`UEd-I_67qJI` · Kai Explains · 2026-09-02 · q3 · intro · news · also: security-guardrails, agent-architecture, models-research

Explainer on Anthropic's Model Hardware Standard (MHS), an MCP-like interface for lab and physical devices, with Carnegie Mellon, Quera and Genentech field results and the main criticisms.

- Techniques: Self-describing device declaration for agent-written drivers; Enforce hard limits in the device or interface layer, not in the prompt; Fault-injection test of the safety layer; Agent-side data-quality check and re-run loop; Report unresolved causes instead of claiming a fix; Three invocation modes for the same device
- Tools: Anthropic Model Hardware Standard (MHS), Model Context Protocol (MCP), Claude Opus 4.8, SiLA (gRPC), OPC UA, Tango, BlueSky, QCoDeS, ROS, PyLabRobot, MATLAB, Python

## [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../videos/GqoNrUz8hEU.md)
`GqoNrUz8hEU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, agent-architecture, security-guardrails

Paul Klein (Browserbase) argues reliable browser agents are a harness, tooling and infrastructure problem rather than a model problem, and lays out a multimodal, harness-engineered, consistently hosted approach.

- Techniques: Hybrid code-plus-browser execution; Per-site skill packs loaded before visiting; Compressed page representation; Pinned, consistent browser environment; Sites expose WebMCP tool calls and agent-first auth; Observability-to-self-improvement loop
- Tools: Browserbase, Browse.sh, WebMCP, Playwright CLI, Claude Code, Operator, Cursor, Factory, OpenClaw, WorkOS AuthMD, web bot auth, auto-browse

## [Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio](../videos/Fu45geO3zX8.md)
`Fu45geO3zX8` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: security-guardrails, multi-agent

Armanas Povilionis (Alithea Bio) argues that cross-organization agent work needs signed, verifiable receipts, and demos Froglet, an open protocol for agents to discover, buy and verify services.

- Techniques: Signed per-step receipts for agent transactions; Marketplace as discovery only, direct peer deals; Same node, role chosen at runtime; Typed payload with schema and deal ID, polled asynchronously; Expose the protocol through MCP and let the LLM drive it
- Tools: Froglet, MCP, Claude, Docker, OpenClaw, NemoClaw

## [MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef](../videos/-jY2T2PiJBE.md)
`-jY2T2PiJBE` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: agent-architecture, product-ux

Ido Salomon and Liad Yosef, the creators of MCPUI and maintainers of the MCP Apps spec, explain how MCP Apps lets servers ship interactive UI into chat hosts and how control of the user journey shifts to the host.

- Techniques: Serve UI as an MCP resource linked to a tool call; Host-mediated event flow from app to model; Three control levels for app-driven steps; Interop: wrap one generative UI payload for several hosts
- Tools: MCP (Model Context Protocol), MCP Apps (official MCP extension), MCPUI, MCP Apps SDK / spec repo (spoken as 'Xtaps' in captions; the official model context protocol repository), ChatGPT Apps / Apps SDK, Claude (including its generative UI feature), VS Code, Slack, Cursor, GitHub Copilot, Goose, Block agent e-commerce

## [MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal](../videos/s4r6nk5WsZw.md)
`s4r6nk5WsZw` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: agent-architecture, infra-cost-scaling

Cornelia Davis (Temporal) explains why no MCP clients support MCP Tasks (async long-running tools) in v1, shows live demos of durable purchase-order and invoice workflows, and walks through the v2 changes that make tasks stateless and extension-based.

- Techniques: Map task lifecycle onto a domain state machine; Signal into a long-running workflow for approvals; Client-side task tracker workflow; Parallel back-office steps beside an async tool call
- Tools: MCP Tasks, FastMCP, Temporal

## [Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk](../videos/1EZdpEhwmNc.md)
`1EZdpEhwmNc` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: security-guardrails, coding-agents, evals

Snyk's CTO argues agent security needs deterministic checks alongside LLMs, with customer data on attacks, toxic skills and MCP servers, plus a live coding-agent demo.

- Techniques: Hybrid LLM plus deterministic security checks; Repeated-run recall measurement; Pre-install package health gate; Skill and MCP risk assessment before adoption; Per-model red-team suite; Breakability-aware automated remediation; Deterministic invocation through a skill or hook
- Tools: Claude Code, Cursor Cloud, Codex, Snyk Studio, Snyk Evo, Snyk package health check

## [Your Moat Is Your Data Model — Mike Phipps, Gates Foundation](../videos/jt1Pbr_n6oU.md)
`jt1Pbr_n6oU` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: data-engineering, enterprise-adoption

Mike Phipps (Gates Foundation) explains why the Strategic Intelligence Platform's defensible asset is a knowledge graph of tacit process knowledge, served to agents through MCP rather than a custom chat UI.

- Techniques: Tacit-knowledge-first data modeling with data owners; Graph with explicit hierarchy types and precomputed roll-ups; Cross-system entity stitching; Document chunks as graph nodes with full-text plus graph retrieval; Curation pipeline before the graph; Expose the graph as an MCP server with state passthrough; Per-question graph-query ground truth plus stability checks
- Tools: Neo4j, MCP, Claude, ChatGPT, Cowork

## [Full Workshop: Better Auth — Paola Estefania, Better Auth](../videos/JvKO40CFq-s.md)
`JvKO40CFq-s` · AI Engineer · 2026-08-18 · q3 · practitioner · workshop · also: security-guardrails, governance-compliance

Paola Estefania (Better Auth) argues agents should get their own identity and scoped capabilities instead of borrowing user credentials, and demos a draft open protocol with approvals, audit logs and revocation.

- Techniques: Per-agent identity with own key pair; Capability grants with default-read policy; Device-flow approval for agents; OpenAPI-to-capability translation; Full revocation: agent, host and tokens
- Tools: MCP, OAuth, OpenAPI, OIDC, Gmail, Notion, Claude, Cursor

## [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore](../videos/26RtyAm9y_Q.md)
`26RtyAm9y_Q` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: voice-multimodal, agent-architecture, security-guardrails

Corey Gallon on driving websites with agents via a shell CLI over the Chrome DevTools Protocol, climbing from synthetic clicks to trusted input to human-like motion, and beating Cloudflare Turnstile, MT Capture, Lemin and reCAPTCHA v2.

- Techniques: CLI over MCP for repeatable browser tasks; Cross-channel verification after each action; Lowest-rung escalation; Coordinate-based trusted click through closed shadow roots and cross-origin iframes; Solver plus operator split; Explore, then codify
- Tools: Chrome DevTools Protocol (CDP), Chrome Agent (speaker's Python CLI), Cloudflare Turnstile, MT Capture, Lemin (auto-captioned as 'lemon'), reCAPTCHA v2, Outlook web client

## [You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit](../videos/lMCxVorb9wM.md)
`lMCxVorb9wM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance

Ravi Madabhushi (Scalekit) argues agents break the human and service-account identity model: they need a distinct identity bound to a principal, fine-grained time-bound scopes, and full action audit, beyond OAuth.

- Techniques: Coalesce high-frequency timestamp writes; Bind agent identity to principal; Context-filtered MCP tool surface; Least-privilege, time-bound, just-in-time grants; Full-provenance action audit
- Tools: OAuth, SPIFFE, MCP, Gmail API, Salesforce API, Databricks, HubSpot, Notion

## [It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard](../videos/I3znWC3MEXM.md)
`I3znWC3MEXM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance, agent-architecture

Kim Maida (Keycard) shows why API keys give agents overprivileged, unattributed access, and how OAuth token exchange (RFC 8693) per tool call, with policy checked before minting, fixes it.

- Techniques: Per-tool-call token exchange (RFC 8693); Policy-before-mint; Policy-gated human approval; Ephemeral, audience-bound bearer tokens; Layered scope design
- Tools: Keycard (security token service and policy governance), OAuth 2.0 token exchange (RFC 8693), Google sign-in (identity provider in demo), MCP (client, server, gateway)

## [Skills are the New SDKs - Elvin Aghammadzada, DataRobot](../videos/LC3-P7v3yoI.md)
`LC3-P7v3yoI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: skills-self-improvement, context-engineering

Elvin Aghammadzada (DataRobot) argues agent skills are a progressive-disclosure context tool that complements MCP, and that skills are software needing versioning, evals and security review.

- Techniques: Progressive disclosure via a skill index; Context budget ceiling; Skill as a wrapper around an MCP server; Split by role: skill for reasoning, MCP for execution; Treat skills as versioned, tested software
- Tools: Claude Code, Codex, Copilot, Gemini CLI, OpenClaw, ClawHub, MCP

## [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing - Bala Ramdoss, Amazon Lens](../videos/maTp79FD9gI.md)
`maTp79FD9gI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: product-ux, agent-architecture

Bala Ramdoss (Amazon Lens) on why LLM agent output needs a typed rendering layer between model and screen: a versioned UI contract, streamed typed chunks, and a BFF that hydrates actions, so mobile clients stay dumb and safe.

- Techniques: Versioned rendering contract; Typed streaming UI blocks; BFF as renderer and hydrator; Design loading around streaming
- Tools: A2UI, CopilotKit, MCP apps

## [Microsoft Built a New Charting Language for AI Agents](../videos/xFWhiWe91BE.md)
`xFWhiWe91BE` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: data-engineering, dev-tools

Better Stack walks through Microsoft Research's Flint, a local MCP chart tool where the LLM writes about 10 lines of semantic JSON and a deterministic compiler emits Vega-Lite, ECharts or Chart.js specs; a research preview with no benchmarks yet.

- Techniques: Semantic spec plus deterministic compiler; Change the meaning, not the geometry; Local MCP chart rendering; Validate the IR, not the generated code
- Tools: Flint (Microsoft Research chart language and MCP server, v0.28), Vega-Lite, ECharts, Chart.js, Mermaid, Data Formulator (Microsoft analytics tool that uses Flint), Claude (Claude Code MCP client), Node 18 / TypeScript, npm

## [LLM Wiki + OKF Every Local AI Now Shares ONE Memory](../videos/9ciGYHHOLyU.md)
`9ciGYHHOLyU` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: memory, context-engineering, local-ai

A solo builder turns Karpathy's LLM-wiki idea and Google's OKF spec into a deterministic, local MCP memory layer, then documents the failures that showed up with a local model.

- Techniques: Librarian agent over a deterministic markdown store; Seed memory in MCP instructions and tool descriptions; Enrich-before-create and bidirectional linking rules for memory writes; Deterministic graph lint for orphans and broken links; Contradiction handling by rewrite, not append; Give the memory a model that makes write decisions well
- Tools: Karpathy LLM wiki (concept), Google OKF spec, MCP, llama.cpp server, llamaswap2, Qwen3 30B-A3B, Gemma 12B, Claude Opus (cited as the level of model needed for spec-following), Author's own memory tool, with web UI and graph visualizer (open source, link in description, not named)

## [Alibaba Just Cut AI Agent Costs by 99% — Here's How](../videos/eCZwexfka6E.md)
`eCZwexfka6E` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: token-cost-efficiency, skills-self-improvement, agent-architecture

Alibaba's SkillWeaver paper cuts agent tool-routing tokens from 884k to 1,160 per query by decomposing, retrieving and composing tools, but the benchmark is self-run and execution was mocked.

- Techniques: Decompose-Retrieve-Compose tool routing; Skill-aware decomposition (SAD) feedback loop; Right-size decomposition granularity
- Tools: SkillWeaver (Alibaba research paper, pipeline name), CompSkillBench (Alibaba benchmark: 300 multi-step queries, 2,209 MCP-derived tools, 24 categories), Qwen2.5-7B-Instruct, Qwen Max, MCP (Model Context Protocol) ecosystem, as the tool source, LangChain, LlamaIndex (spelled 'Lama index' in the transcript), GPT 5.5 (mentioned as a model the market is racing to wire in), Opus (mentioned as a model the market is racing to wire in)

## [MCP vs REST vs A2A How AI Agents Actually Talk](../videos/psszX04xeGU.md)
`psszX04xeGU` · Kai Explains · 2026-08-02 · q3 · intro · other · also: agent-architecture, multi-agent

Explainer arguing REST, MCP and A2A are stacked layers, not rivals: REST links programs, MCP links an agent to tools, A2A links agents to agents. Advice: learn MCP first and add A2A only for multiple independent agents.

- Techniques: Map each integration to one protocol layer; Expose each tool once as an MCP server; Wrap an existing REST API with a thin MCP server; Publish an agent card for discovery and delegation; Adopt multi-agent protocols only when the pain is specific
- Tools: REST, MCP (Model Context Protocol), A2A (Agent2Agent), JSON-RPC 2.0, HTTP, stdio

## [MCP Is Getting Its Biggest Update Ever (No One's Ready)](../videos/k5f1uID3GcU.md)
`k5f1uID3GcU` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: agent-architecture, security-guardrails, infra-cost-scaling

MCP's July 28 rewrite drops the handshake and session ID so any replica can serve any request; state moves into owner-checked handles, and auth fragmentation across clients is the bigger unresolved problem.

- Techniques: Make stateful MCP tools own their handles; Round-trip state through the client as a sealed blob; Split pure tools from stateful tools in deployment; Gateway and proxy checklist for the MCP change; Test each server against every major client; Load tool definitions on demand in the client
- Tools: MCP (Model Context Protocol), July 28 spec revision, OAuth 2.1, Claude Code, Claude.ai, Anthropic API, ChatGPT, Google Cloud, VS Code, Redis, Salesforce, JIRA, Snowflake

## [China Drops LongCat, Anthropic Fires Sonnet 5, Google Omni Flash & Robots Learn to Vibe Code AI News](../videos/RgREa6QEsgA.md)
`RgREa6QEsgA` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, inference-serving, token-cost-efficiency

Weekly AI news roundup (Aug 2026): Meituan's LongCat 2.0, Claude Sonnet 5, Google's Nano Banana 2 Lite and Gemini Omni Flash, Booster Studio for robots, Claude Science, and ComfyUI's Claude MCP.

- Techniques: Comfy Cloud MCP setup for Claude Code and Claude Desktop; Two-stage cheap-then-expensive media pipeline; Dedicated reviewer agent for research outputs; Use anonymous or stealth router listings as an adoption signal
- Tools: LongCat 2.0 (Meituan, 1.6T MoE, MIT license), GPT 5.5 (comparison baseline), Claude Sonnet 5 (model string as spoken: Claude-Sonnet-5), Claude Opus 4.8 (comparison baseline), Claude Sonnet 4.6 (comparison baseline), Claude Code, Claude Desktop, ComfyUI / Comfy Cloud MCP, ComfySkills Marketplace, ComfyCloud plugin, Nano Banana 2 Lite, Nano Banana (original)

## [Google OKF + RAG: The Ultimate AI Agent Architecture](../videos/CnfuoBYmkJE.md)
`CnfuoBYmkJE` · Kai Explains · 2026-08-02 · q2 · intro · review · also: rag-retrieval, context-engineering

Explainer arguing agents should route high-stakes facts to a curated, Git-versioned markdown knowledge bundle (Google's OKF) and open-ended queries to RAG; a thin router decides per query.

- Techniques: Curated-first hybrid routing; OKF-style concept files; Governing knowledge in Git; Single retrieval facade; Baseline RAG ingestion
- Tools: Google Cloud OKF (Open Knowledge Format, June 2026 per speaker), RAG (retrieval-augmented generation), Pinecone, Weaviate, Qdrant, Milvus, Chroma, PostgreSQL with pgvector, LangChain, LlamaIndex, MCP (Model Context Protocol), Claude

## [Kimi K3 Fable 5 & GPT 5.6 Sol Killer, Inkling, Xiaomi Robotics U0, MobileWan, Needle & More AI News](../videos/sUamCGBjWkM.md)
`sUamCGBjWkM` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: models-research, local-ai, data-engineering

Weekly AI news roundup (Aug 2026): Kimi K3 and Inkling open-weight releases, ACT2 and Xiaomi robot world models, on-phone 5B video diffusion, a 0.8B end-to-end OCR model, and a 26M function-calling model.

- Techniques: Self-driven fine-tuning loop for a behavioral constraint; Failure-driven single-example post-training loop; Chunk-wise recurrent attention for constant-memory long generation; Attention-only tiny router for tool selection; Long-horizon kernel-optimization evaluation
- Tools: Kimi K3 (Moonshot AI), Kimi Delta Attention, Kimi Code, Kimi Work, Kimi API, Claude Fable 5, GPT 5.6 Sol, Opus 4.8, GPT 5.5, Inkling, InklingSmall, OpenCode

## [Claws Out: Securing and Building with OpenClaw - Nick Taylor, Pomerium](../videos/xg1zNlzw7Jk.md)
`xg1zNlzw7Jk` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: security-guardrails, coding-agents

Nick Taylor (Pomerium) on hardening the OpenClaw control plane with trusted-proxy auth, then a live demo of building a UI-bearing MCP app for ChatGPT by editing its workspace from Discord on his phone.

- Techniques: Identity-aware proxy as the auth layer for an agent control plane; Live-edit an MCP app from chat; Widget-to-LLM calls via the MCP apps send-message function; Narrow write access for agent-driven PRs; Test the unauthenticated or fresh-install path
- Tools: OpenClaw, Pomerium, ChatGPT apps (MCP apps), MCP, React, Vite, Discord, Telegram, WhatsApp, Caddy, NGINX, GitHub CLI

## [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](../videos/BqZrTdgBaPw.md)
`BqZrTdgBaPw` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: agent-architecture, product-ux

Stephan Steinfurt (TNG) shows a nightly, fully automated chess-explainer pipeline: a Gemini 3.1 Pro agent with chess tools narrates analysed human games as YouTube videos.

- Techniques: Engine plus LLM split with tools; Let the reasoning model choose tools rather than pre-computing; Deliberately conflicting tool outputs; Nightly batch with a structured intermediate format; Monitor odd outputs and treat them as signals
- Tools: Gemini 3.1 Pro, Grok 4, ElevenLabs v3, Maia (captioned as Maya), chess engine (unnamed), web search

## [The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab](../videos/sum9DgexFRQ.md)
`sum9DgexFRQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: multi-agent, security-guardrails, infra-cost-scaling

Ramesh Raskar and Maria of MIT's Project Nanda outline an open infrastructure for a web of AI agents: a signed discovery index, agent hosting, and NandaTown, a simulator for testing agent networks before they go live.

- Techniques: Signed agent facts record and agent card; Message box in front of the agent runtime; Adaptive endpoint resolution; Sleep and wake hosting; Tiered simulation with scripted agents, then LLM agents; Onboarding in three tiers
- Tools: Nanda index, NandaTown, OpenClaw, Maritime, AWS, DNS, YAML

## [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](../videos/vh2VGuQ3zhY.md)
`vh2VGuQ3zhY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, rag-retrieval, evals

Giving an agent every tool schema on every request breaks accuracy, latency and cost as the catalog grows; the fix is semantic routing that injects only the top-K relevant tools per query.

- Techniques: Semantic tool routing (tool RAG); Just-in-time tool and context injection; K-sweep routing evaluation; Router miss fallbacks; Description writing for retrieval; Routing observability
- Tools: Qdrant, Chroma, Pinecone, Berkeley Function Calling Leaderboard, ToolBench, Anthropic MCP on-demand tool loading write-up, Aurelio Labs semantic-router (open source), MCP0 (cited as an open-source routing project at large scale)

## [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../videos/HEFSExa0xl0.md)
`HEFSExa0xl0` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: agent-architecture, testing-verification, evals

Witan Labs on lifting coding agents' spreadsheet accuracy from about 50% to 92% by replacing 15 tools with one persistent-state REPL, plus a formula engine and render engine as the verification loop.

- Techniques: Single persistent-state REPL instead of many tools; Verification loop with domain engines; Golden-spreadsheet black-box evaluation; Domain-knowledge reminders in the prompt; Trace review for plumbing bugs
- Tools: Node.js REPL, JavaScript, TypeScript type definitions, C#, LLM-as-judge, Witan Labs internal formula engine, Witan Labs internal render engine

## [MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc](../videos/sAOBXCDiDOs.md)
`sAOBXCDiDOs` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: product-ux, security-guardrails

Pietro Zullo (Manufact) explains MCP Apps: tools that return sandboxed UI widgets, the primitives behind them, and how the new client app stores distribute MCP servers.

- Techniques: Widget-returning tool; Split structured output (UI vs model); Set-state to sync UI to model; Stream tool input into the UI; Widget actions that call tools; Client-aware output; Pre-submission checks for stores
- Tools: MCP, MCP Apps, MCP-UI, MCP SDK, MCP Inspector, React, Remotion, Excalidraw, Granola MCP, Linear MCP, Postgres MCP, Claude Code

## [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../videos/IddXPepIAS4.md)
`IddXPepIAS4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, coding-agents, testing-verification

Erik Hanchett (AWS) on spec-driven development: write requirements, design and task markdown before code, keep a human reviewer in the loop, and use property-based tests to check the result.

- Techniques: Manual spec loop with any coding assistant; Clarifying questions before requirements; EARS-format requirements; Property tests generated from requirements and design; MVP-first task ordering; Steering docs plus on-demand skills; Pull requirements from PM tools via MCP
- Tools: Kiro, spec-kit, MCP, FastCheck, Mermaid, EARS, Jira, Asana, agents.md, CLAUDE.md

## [Building an ACP-Compatible Agent Live — Bennet Fenner, Zed](../videos/HsxQICTLF84.md)
`HsxQICTLF84` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: coding-agents, agent-architecture

Live demo of turning a minimal TypeScript coding agent into an ACP-compatible agent for Zed: four required methods, streamed text, tool-call updates, client-proxied file access, and a diff content type.

- Techniques: Minimal agent loop as the ACP core; Session-scoped agent instances; Streaming through session-update notifications; Two-phase tool-call reporting; Client-proxied file system; Diff content type for edits; Using the protocol's debug view to inspect traffic
- Tools: Zed, Agent Client Protocol (ACP), ACP TypeScript SDK, Anthropic SDK, Node.js, stdio

## [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](../videos/vJukHCIv7Ck.md)
`vJukHCIv7Ck` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: rag-retrieval, security-guardrails, multi-agent

AWS developer advocate walks through five code-level techniques to reduce agent hallucinations: semantic tool selection, GraphRAG for aggregation, multi-agent validation, code-enforced hooks, and steering rules. Demos use dummy tools.

- Techniques: Semantic tool selection; Per-turn tool swap in agent loop; Text-to-Cypher GraphRAG for aggregation; Executor, validator, critic swarm; Before-tool-call hooks for hard rules; Steering rules for soft constraints
- Tools: Strands Agents, OpenAI API, sentence-transformers, Neo4j (Cypher, LLM graph builder), agent-control (steering SDK), Amazon Bedrock AgentCore (Gateway, Runtime, Policy, Memory), DynamoDB, Neo4j AuraDB, AWS Lambda, Ollama (mentioned)

## [Structuring the Unstructured - Cedric Clyburn, Red Hat](../videos/-x5GEVnkuRw.md)
`-x5GEVnkuRw` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: data-engineering, rag-retrieval, context-engineering

Red Hat's Cedric Clyburn demos Docling, an open-source local tool that converts messy PDFs into layout-aware Markdown, JSON, or Pydantic data, plus chunkless RAG over a document outline.

- Techniques: Layout-aware PDF to structured document conversion; Picture enrichment with a local vision-language model; Chunkless agentic RAG over a document outline; Schema-driven extraction from parsed documents; Document conversion as a microservice plus MCP tool; PII removal model before ingestion
- Tools: Docling, docling-serve, Docling MCP server, Pydantic, Ollama, Granite (IBM model), Qwen (via MLX), Jupyter, VS Code, Kubernetes, uvx

## [The Rise of Generative UI for Developers (CopilotKit)](../videos/kVL_7csy_ZM.md)
`kVL_7csy_ZM` · Better Stack · 2026-07-02 · q3 · intro · review · also: product-ux

Better Stack walkthrough of CopilotKit as a front-end stack for agent UIs: AG-UI event protocol, generative UI, shared state, and approval gates, with a candid trade-off section versus Vercel AI SDK and building in-house.

- Techniques: Generative UI: agent triggers real components; Bidirectional shared state between UI and agent (co-agents); Approval gate before state-changing tool calls; Scaffold the stack from the project's install command
- Tools: CopilotKit, AG-UI, Vercel AI SDK, LangGraph, CrewAI, Mastra, React, Next.js

## [Hermes Agent under Claude Code Is Insane](../videos/Sb96po6S67k.md)
`Sb96po6S67k` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: claude-code, skills-self-improvement, memory

Setup-and-use walkthrough for running the Hermes agent alongside Claude Code: Hermes adds persistent memory and self-evolving skills, and can run as an MCP server, cron-driven monitor, or Claude Code launcher.

- Techniques: Install Hermes and run the manual setup; Onboard Hermes with your context; Expose Hermes to Claude Code as an MCP server; Cron-driven living PRD skill from a Slack channel; Delegate feature work to Claude Code from a Hermes channel; Health-check skill loop for a deployed app
- Tools: Hermes Agent (Nous Research), OpenClaw, Claude Code, Claude Code subscription / non-interactive mode, Anthropic Agent SDK credit (policy claim), hermes setup command, hermes mcp serve command, .mcp.json, user.md and memory.md (Hermes memory files), soul file (Hermes agent personality/instructions), Hermes Skill Hub, Hermes bundled Claude Code skill

## [MemPalace: The Tool That Makes Claude Stop Forgetting](../videos/kRACHOx1p8s.md)
`kRACHOx1p8s` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: memory, claude-code, context-engineering

Better Stack demos MemPalace, a local tool that stores coding-agent conversations verbatim and exposes them to Claude Code over MCP so decisions persist across sessions.

- Techniques: Verbatim store plus compact index; Local project memory setup; Claude Code plugin with a memory protocol; Run alongside context mode; Load pointers instead of project lore; Install hygiene for memory tools
- Tools: MemPalace (mempalace; spoken as Mem Palace; version not stated), uv, pip, ChromaDB, SQLite, MCP (Model Context Protocol), Claude Code (captioned as Cloud Code), Claude Code hooks and plugin, context mode, Memzero, Zapp (transcript spelling; product name unverified)

## [Your AI Agent Is Missing Half the Internet… Until Now (Agent-Reach)](../videos/aanqEqQwjNU.md)
`aanqEqQwjNU` · Better Stack · 2026-07-02 · q3 · intro · review · also: coding-agents, rag-retrieval

A 6-minute Better Stack review of Agent Reach, an MIT-licensed Python CLI that gives coding agents multi-platform web access (social, code, video, Chinese platforms) with health checks and fallback backends.

- Techniques: Per-platform channel adapters with primary and fallback backends; One-sentence agent-driven install plus a doctor health check; Shell permission as a prerequisite for self-install
- Tools: Agent Reach (Python CLI and library, MIT licensed, over 28,000 GitHub stars), Claude (used inside VS Code), Cursor 2, Playwright (suggested for interactive browser actions), Firecrawl (suggested for plain web pages; transcript says 'fire crawl'), YouTube, GitHub, Twitter/X, Reddit, Bilibili, Xiaohongshu (platform channels)

## [Insane Claude Design Skills You Need To Build Beautiful Websites](../videos/Ot582-E61ac.md)
`Ot582-E61ac` · AI LABS · 2026-07-02 · q3 · intro · review · also: skills-self-improvement, product-ux, coding-agents

A walkthrough of Claude design skills (Anthropic frontend-design, ShadCN, UI UX Pro Max, GSAP, Material 3, SwiftUI, Expo) for building less generic websites and mobile apps, with a sponsor segment.

- Techniques: Commit to a design direction before generating; Separate functional and marketing design skills; Pair a rules skill with a component-registry MCP; Separate layout reasoning from component work for dashboards; Use a taste preset instead of a full design system; Prefer compositor-friendly animation properties
- Tools: Claude, Anthropic frontend-design skill, Opus 4.8, Fable 5, ShadCN, ShadCN MCP, UI UX Pro Max, GSAP, Higgsfield, C-Dance (as captioned; video model), Material 3, SwiftUI

## [I Tried the Open Source ElevenLabs Alternative (Voicebox)](../videos/RL_PDX_BVxw.md)
`RL_PDX_BVxw` · Better Stack · 2026-07-02 · q3 · intro · review · also: voice-multimodal, local-ai

Better Stack walkthrough of Voicebox, a free open-source local voice studio for cloning, TTS, system-wide dictation and agent speech. Works well on Apple Silicon, but the tool is early and the agent integration was not tested.

- Techniques: Desktop install instead of Docker; Clone a voice from a short sample; System-wide dictation via global hotkey; Restart to clear app-level glitches; Pick the model for emotion control
- Tools: Voicebox, ElevenLabs, Ollama, Docker, Piper, Whisper, Claude Code, Cursor, Chatterbox TTS Turbo, MCP

## [Introducing WebMCP: Agents in the Browser — RL Nabors](../videos/LMbeDEQO6QM.md)
`LMbeDEQO6QM` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: voice-multimodal, product-ux

A practical tour of MCP over HTTP, MCP Apps for in-chat UI with CSP and sandbox gotchas, and WebMCP, which lets agents call tools exposed by a web page's own JavaScript.

- Techniques: Single server, multiple client surfaces; Remote connector onboarding over HTTP; App-only tool visibility for UI navigation; Bundle MCP App into one file with explicit CSP; WebMCP imperative registration with feature detection; Declarative WebMCP on existing forms
- Tools: MCP, MCP Apps, WebMCP, navigator.modelContext.registerTool, Vite single-file plugin, Web Speech API, MCP Inspector-style debugging extension

## [Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe](../videos/KLSuFPj2ld0.md)
`KLSuFPj2ld0` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance

Stripe's Steve Kaliski on letting agents spend safely: scope shared payment tokens to amount, time and seller, use HTTP 402 for paid tools, and keep discovery non-deterministic while payments stay deterministic.

- Techniques: Seller-scoped delegated payment credential; Deterministic transaction layer behind a non-deterministic planner; HTTP 402 pay-per-call; Round-trip checkout state; Forward risk signals to the counterparty
- Tools: Stripe shared payment tokens, Stripe Payment Intents, Stripe Issuing, Machine payments protocol (with Tempo), Agentic Commerce Protocol (with OpenAI), curl (demo), Tempo blockchain (pathUSD), Base

## [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](../videos/ghJmWQCIHRM.md)
`ghJmWQCIHRM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, product-ux

Google Chrome DevRel on WebMCP, a proposed browser standard that lets a website expose its actions as structured tools for in-browser AI agents, with declarative and imperative APIs and an early-preview setup guide.

- Techniques: Declarative tool exposure from HTML forms; Imperative registerTool for multi-step UI; Mirror tool calls in the visible UI; Hybrid browse-then-delegate flow; Test tools with an inspector and evals CLI
- Tools: WebMCP, Chrome Canary, Model Context Tool Inspector (Chrome extension), Gemini, Chrome DevTools-style flag (WebMCP testing flag), WebMCP evals CLI

## [Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind](../videos/3_gYbhABcAE.md)
`3_gYbhABcAE` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: agent-architecture, evals, context-engineering

Philipp Schmid (Google DeepMind) lists five habits from deterministic software that break when building agents: text as state, handing control to the LLM, errors as inputs, pass-rate evals, and agent-ready tools.

- Techniques: Goal-first dispatcher prompting; Free-text approval with edits; Preferences as natural language in context; Errors as observations; Repeated-run pass-rate evals with judges; Agent-ready tool definitions
- Tools: Gemini API, Gemini

## [Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence](../videos/UQKg0td-Bf4.md)
`UQKg0td-Bf4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: testing-verification, evals, security-guardrails

Steven Willmott (SafeIntelligence) argues agent testing needs an explicit spec of data, rules, terminology, roles and robustness needs, kept separate from the implementation and run in a closed loop.

- Techniques: Six-part agent spec; Spec-driven security testing; Input perturbation sweep; Closed-loop spec iteration (backyard RL); Specs as versioned repo files; Agent cards plus variation envelopes
- Tools: SafeIntelligence platform, A2A agent cards, LangSmith, Vertex AI agents, Braintrust, OpenAPI

## [Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman](../videos/hCMrEfPG2Yg.md)
`hCMrEfPG2Yg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: product-ux, sandboxing-execution

Ruben Casas (Postman) maps generative UI from static components to declarative JSON to runtime-generated HTML/JS, argues MCP apps are the right sandboxed delivery layer, and says collaborative canvases are the next step.

- Techniques: Declarative generative UI with a component catalog; Static client-tool to component mapping; Runtime generated HTML/CSS/JS in a sandboxed MCP app; Use MCP apps as the default delivery for generated UI
- Tools: MCP apps, AG-UI, Goose (auto visualizer), json-render (Vercel), FastMCP, Excalidraw MCP app (transcribed as ScallyDraw), Claude Visualizer, GPT-5.2, Claude Opus 4.5, React

## [Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub](../videos/_xIwFcnHqp4.md)
`_xIwFcnHqp4` · AI Engineer · 2026-06-18 · q3 · practitioner · demo · also: coding-agents, product-ux

Marlene Mhangami and Liam Hampton (GitHub) show how MCP Apps let a tool return an interactive HTML UI rendered in a sandboxed iframe inside VS Code chat, with a live Go flame-graph demo.

- Techniques: MCP App tool-plus-resource pattern; Skill-driven MCP app scaffolding; Tool visibility scoping; Profiler-to-flame-graph bridge; Install MCP servers from curated lists only
- Tools: VS Code, GitHub Copilot, Copilot CLI, MCP, Go pprof, React, Excalidraw, Figma

## [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](../videos/TNwJ1LMiENk.md)
`TNwJ1LMiENk` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: training-finetuning-rl, evals

Snorkel shows a 4B model, RL-trained on single-table financial tool-use tasks for under $500, beating a 235B model. The gain came from fixing tool discipline, not reasoning.

- Techniques: Behavior-targeted RL with GRPO on a tool environment; Single-table-first training data; Verification pass on generated tasks; Rubric decomposition for diagnosis; Publish the environment as a portable package
- Tools: GRPO, RLM framework (UC Berkeley), FinQA environment (Snorkel), OpenEnv, Prime Intellect, Harbor, GetTableNames / GetTableInfo tools, Qwen3

## [What Breaks When You Build AI Under Sovereignty Constraints - Bilge Yücel, deepset GmbH](../videos/x2bH0RKPgdc.md)
`x2bH0RKPgdc` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: governance-compliance, security-guardrails, observability

Bilge Yücel (deepset) on building AI under sovereignty constraints: four pillars, what breaks when you move from frontier APIs to self-hosted, and a guardrail-agent-guardrail reference design built on Haystack.

- Techniques: Sovereignty checklist as a design gate; Safe/unsafe router as an input guardrail; Per-agent tool allowlist plus BM25 tool search; Per-tool human confirmation strategies; Pipeline serialized to YAML for version control; Tracer component wrapping the pipeline
- Tools: Haystack, MCP, BM25, OpenTelemetry, YAML, Kubernetes, Mistral, Google models, Nvidia models, Jina

## [Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](../videos/c-2eEv2ou7Y.md)
`c-2eEv2ou7Y` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: security-guardrails, product-ux

Frédéric Barthelet (Alpic) explains why ChatGPT and Claude render third-party MCP app UI in nested "double" iframes: CSP and origin isolation rule out simpler options, and the nesting is the workable compromise.

- Techniques: Double-iframe isolation for untrusted UI; Declare-then-enforce external domains; CSP inspection in dev tools
- Tools: MCP Apps extension, OpenAI Apps SDK, SkyBridge, HTML iframe (srcdoc, sandbox, allow-same-origin), Content Security Policy (frame-src, script-src, connect-src)

## [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](../videos/btxGmN8RvNU.md)
`btxGmN8RvNU` · AI Engineer · 2026-06-18 · q2 · intro · review · also: rag-retrieval, data-engineering

Bright Data pitch: blocked web access makes LLM agents fabricate answers silently. Its MCP (search, markdown scrape, CAPTCHA-solving browser) fixed a 5-site demo, but the evidence is one unreplicated run.

- Techniques: Paired with/without-tools comparison; Load a narrow subset of MCP tools; Scrape to markdown instead of HTML; Batch search across many keywords; LLM writes the parser, script does the extraction; Human-like remote browser instead of detection evasion; Restrict agents to public, non-login data; Pre-collected datasets for non-live needs
- Tools: Bright Data MCP (66 tools per speaker; 69 mentioned later), Bright Data scraping browser (remote, fingerprinted, CAPTCHA solving), Bright Data skills page, Bright Data datasets, GPT-5 (tested without tools as baseline), ChatGPT (cited for broken citations), Google, Bing and DuckDuckGo search (via MCP), Cloudflare bot blocking and AI Labyrinth (cited, not used), VS Code (demo environment)

## [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](../videos/SKDJo2CopRs.md)
`SKDJo2CopRs` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: sandboxing-execution, agent-architecture, infra-cost-scaling

Two Cloudflare engineers tour Durable Objects, dynamic workers and code mode as a stateful, sandboxed runtime for agents. Mostly product pitch, with a few reusable architecture ideas.

- Techniques: One Durable Object per entity ID as the session or agent; Resumable stream held by the agent object; Deny-by-default capability sandbox for generated code; Code mode for large API surfaces; Scheduled work inside the agent class; Plugins as isolated dynamic workers
- Tools: Cloudflare Durable Objects, Cloudflare Workers, Cloudflare Dynamic Workers, Cloudflare Agents SDK, Vercel AI SDK, MCP, Cloudflare Sandbox SDK, Daytona, SQLite, R2, Zig (via Wasm), Next.js on Workers

## [Any-to-Any: Building Native Multimodal Agents - Patrick Löber, Google DeepMind](../videos/GIRpQEfYf3U.md)
`GIRpQEfYf3U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, agent-architecture

Google DeepMind's Patrick Löber walks through building a NotebookLM-style agent: Gemini reasons, calls native image and speech generators via function calling, and uses multimodal input and a live audio model.

- Techniques: Agentic generation loop with function-declared generators; Single-call multimodal synthesis; Timestamp-windowed media analysis; Context caching for repeated queries; Scaffold with a Gemini API skill; Audio-to-audio live session for voice
- Tools: Google Gen AI SDK, Gemini API, Google AI Studio, Gemini 3 Flash, Gemini 3.5 Flash Image preview (Nano Banana 2), Gemini 2.5 text-to-speech, Gemini 3.1 Flash Live, File API, Gemma 4, Gemini API skill

## [From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](../videos/zTZ0qunQXnM.md)
`zTZ0qunQXnM` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: data-engineering, coding-agents, voice-multimodal

A Bright Data vendor demo arguing LLMs should write a reusable scraper once instead of parsing every page, then run and self-repair it on a schedule. Useful pattern, heavy product pitch.

- Techniques: Generate-then-run scraper; Scheduled self-repairing collection loop; Tiered fetch format; Remote browser with human-like input for multi-step flows; Public-data-only policy check
- Tools: Claude Code, Codex, Bright Data MCP, Bright Data scrape-as-markdown, Bright Data Web Unlocker API, Bright Data remote browsers, Bright Data skill docs on GitHub, Haiku

## [Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw](../videos/VaS2h-dY1-4.md)
`VaS2h-dY1-4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: multi-agent, sandboxing-execution, pr-code-review

An OpenClaw maintainer shows acpx, a CLI and workflow engine over the Agent Client Protocol (ACP), used to automate PR triage and to run disposable per-task agents on Kubernetes.

- Techniques: ACP as the client-side adapter layer; Channel-bound agent sessions; Hybrid PR-triage workflow with JSON handoffs; Shallow-fix loop with a human escalation gate; Feedback bin for PR outcomes; Per-task disposable agent pods via a Kubernetes operator
- Tools: acpx, ACP (Agent Client Protocol), Codex, Claude Code, Zed, Discord, Slack, MS Teams, Kubernetes, Helm, Go operator, rsync

## [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](../videos/_B4Pv9ttFgY.md)
`_B4Pv9ttFgY` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: product-ux, security-guardrails

Four engineering lessons from the Chrome DevTools MCP team on designing agent-facing interfaces: token cost, error recovery, tool discoverability, and trust boundaries.

- Techniques: Semantic summaries instead of raw tool output; Tokens per successful outcome; Tool categorization and slim mode; CLI with piping for local post-processing; Self-healing error messages; Proactive detours; Tool descriptions as UI for the agent; Trust tiers with deliberate consent friction
- Tools: Chrome DevTools MCP server, Gemini CLI, Claude Code, Codex, OpenClaw

## [This Is The Greatest Shift In Codex CLI And Claude Code](../videos/B44bXmzU60s.md)
`B44bXmzU60s` · AI LABS · 2026-06-02 · q2 · practitioner · review · also: context-engineering, claude-code

Walkthrough of Mirage, a virtual file system that mounts Gmail, Drive, Slack and similar services as folders so Claude Code can read them with bash instead of MCP tool calls. Partly sponsored, with a hype title.

- Techniques: Mount a SaaS service as a folder; Run the mount as a long-lived process; Start the agent inside the mounted workspace; Chain bash commands across services instead of MCP calls; Read attachments as files; Preserve a session across restarts; Wrap any API as a file system; macOS FUSE prerequisite
- Tools: Mirage (virtual file system for agents, cloned from source), Claude Code, MCP (Model Context Protocol), Gmail MCP, Google Drive MCP, Google Chat, Slack, Notion, Telegram, Figma (mentioned as a possible target), Claude Design (mentioned in passing, unverified), Google Cloud Console

## [MCP Apps Are Changing the Internet. Here’s How to Build One! (Skybridge)](../videos/9X8GRGcl5oA.md)
`9X8GRGcl5oA` · Better Stack · 2026-06-02 · q3 · intro · tutorial · also: coding-agents, vibe-coding-app-building

Better Stack walkthrough of Alpic's SkyBridge 1.0, a TypeScript/React framework for building MCP apps (interactive widgets inside chatbots), shown by building and testing a camera-lens store app with its local dev dashboard, tunnel and Beacon Audit.

- Techniques: Install the SkyBridge skill into the repo, then prompt the agent to build the app; Test tools and widget state in the SkyBridge dashboard before involving a chatbot; Expose a local MCP server with the dashboard tunnel and attach it as a Claude custom connector; Run Beacon Audit before submitting to an app store
- Tools: SkyBridge 1.0 (Alpic, open-source TypeScript framework for MCP apps), Alpic Playground (sandbox inside the SkyBridge dashboard), Beacon Audit (SkyBridge app audit tool), React, TypeScript, Claude (builds the app and hosts the custom connector; the transcript does not name the surface used for generation), ChatGPT (developer settings used for testing the tunnel URL), Skybridge agent skill (installed into the repo's .agents directory)

## [Perplexity Open-Sourced a Scanner Every Dev Should Know (Bumblebee)](../videos/L6iAw5yitfc.md)
`L6iAw5yitfc` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: security-guardrails, dev-tools

Better Stack demos Perplexity's open-source Bumblebee, a read-only Go binary that inventories a dev machine's packages, editor and browser extensions, and MCP configs from local metadata, for supply-chain incident response.

- Techniques: Weekly baseline inventory dumped centrally; Escalate scan depth by incident state; Query NDJSON with jq or a SIEM; Treat MCP configs as part of the secret and dependency surface
- Tools: Bumblebee (Perplexity open-source scanner), Go (go install, single binary), npm, pnpm, yarn, bun, Go modules, VS Code, Cursor, Claude, jq, MDM

## [Stop Overpaying for LLMs... This Router Cut My Costs 70% (Manifest)](../videos/BXme4u4uoyA.md)
`BXme4u4uoyA` · Better Stack · 2026-06-02 · q3 · intro · review · also: token-cost-efficiency, infra-cost-scaling

Better Stack walkthrough of Manifest, a self-hostable LLM router that scores each request across 23 dimensions and sends it to the cheapest capable model; the speaker claims up to 70% cost cuts with no agent code changes.

- Techniques: Drop-in LLM router in front of agents; Deterministic request scoring for model routing; Route to subscriptions and local models before paid API tokens; Failover on provider errors; Per-agent cost tracking and budgets
- Tools: Manifest, Docker, Docker Compose, OpenAI API (base_url change), Anthropic API, Ollama, OpenRouter, LiteLLM, llama.cpp, Python (demo agent script)

## [Anthropic Just Revealed The Best Claude Code Setup](../videos/lGalJmyI78w.md)
`lGalJmyI78w` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · also: claude-code, context-engineering, multi-agent

Practitioner checklist for setting up Claude Code harnesses on large codebases: layered CLAUDE.md, hooks, path-scoped skills, plugins, LSP, MCP, sub-agents, and periodic pruning.

- Techniques: Layered CLAUDE.md; Stop-hook learning loop; Hooks for enforcement; Path-scoped skills; Team plugin distribution; LSP before code; Custom sub-agents with an overridden Explore agent; Per-subdirectory tests and codebase map; Quarterly harness pruning with ignore files
- Tools: Claude Code, Codex, Gemini CLI, superpowers, CLAUDE.md, Claude Code hooks (SessionStart, PreToolUse, Stop, exit-code-2), skill-creator, Claude Code plugins and plugin marketplace, LSP (Language Server Protocol), MCP (Model Context Protocol), Explore sub-agent (built-in, overridable), .gitignore

## [This Is Insane... This Just Ended The Google Stitch VS Claude Design Debate](../videos/PJ9CmTODmVo.md)
`PJ9CmTODmVo` · AI LABS · 2026-06-02 · q2 · intro · review · also: product-ux, coding-agents, context-engineering

Hands-on head-to-head of Claude Design and Google Stitch across features, limits, design quality, animation, iteration and handoff; each tool wins different categories.

- Techniques: Batch design comments before sending; Import a design system from a URL; Portable design.md design system; Coding agent drives the design tool through MCP; Generate the design system before the screens
- Tools: Claude Design, Claude Opus 4.7, Google Stitch, Gemini 3, Nano Banana, Claude Code, Figma, Google AI Studio, Firebase, GitHub, design.md

## [Claude Code + Better Stack: The Only Error Debugging Setup You Need](../videos/u2tqAXKkb4c.md)
`u2tqAXKkb4c` · Better Stack · 2026-06-02 · q2 · intro · tutorial · also: observability, claude-code

Better Stack demo of triaging a live React frontend error from the terminal: Claude Code pulls error data through the Better Stack MCP server, opens a fix PR, then resolves the issue. Short, vendor-led.

- Techniques: MCP-backed error triage loop; Deferred tool loading for MCP servers; Frontend error capture with a vendor DSN and an agent setup prompt; Scheduled error-triage routine
- Tools: Claude Code, Better Stack (error tracking, session replay, MCP server), Sentry React SDK, Telegram, WhatsApp, email

## [Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face](../videos/OV56RddyFuU.md)
`OV56RddyFuU` · AI Engineer · 2026-05-18 · q2 · practitioner · demo · also: local-ai, training-finetuning-rl, coding-agents

Hugging Face's Merve Noyan demos open-model agent workflows: picking and serving open models, Hermes Agent, pushing agent traces to the Hub, HF MCP server and skills that let coding agents launch fine-tuning and batch OCR jobs.

- Techniques: Hub-ID local serving for coding agents; GGUF hardware-fit check before download; Agent-driven fine-tuning via skills; Session traces pushed to a Hub dataset; Corpus OCR via prompted batch job; HF MCP server for catalog access
- Tools: Hugging Face Hub, Hugging Face MCP server, Hugging Face skills (hub CLI, LLM trainer, Gradio, dataset), Inference Providers, Hermes Agent, Pi, llama.cpp, vLLM, MLX, LM Studio, Claude Code, Codex

## [Human-in-the-Loop Automation with n8n — Liam McGarrigle](../videos/tDArkCqjA-c.md)
`tDArkCqjA-c` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: security-guardrails, agent-architecture, context-engineering

Workshop on building a Gmail and Google Calendar agent in n8n, then gating sensitive tool calls behind human approval steps that the model cannot skip.

- Techniques: Approval gate in front of sensitive tools; Free-text decline as feedback; Dry runs with dummy data before real accounts; Rules in tool descriptions, not one system prompt; Per-field descriptions for argument mistakes; Wait with an auto-deny timeout; Confirm sub-workflow as a tool; Sub-agent per domain as a tool; Date and time injection via expression; Memory window sizing
- Tools: n8n, OpenRouter, Gmail, Google Calendar, Slack, Notion, Postgres, Redis, Claude, Claude Code, Luxon, Swagger

## [Connecting the Dots with Context Graphs — Stephen Chin, Neo4j](../videos/eW_vxrjvERk.md)
`eW_vxrjvERk` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: memory, rag-retrieval

Neo4j DevRel lead argues agents need a knowledge graph that stores short-term, long-term and reasoning memory together, so decisions can be explained and reused. Mostly a product pitch with one finance demo.

- Techniques: Three-tier memory in one graph; Vector entry point then graph traversal; Decision write-back to the graph; LLM-generated Cypher with visible query trace; Multi-source ingestion through MCP tools into a graph
- Tools: Neo4j, Neo4j Agent Memory package (open source), Cypher, OpenAI embeddings, FastRP, Leiden algorithm, MCP, Next.js, Neo4j Aura (free tier), Graph Academy

## [Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take](../videos/FlzpEGHNVKQ.md)
`FlzpEGHNVKQ` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: evals, context-engineering

How a consumer chess app grounds LLM game commentary in Stockfish and detectors, hits a sub-3s latency target, and closes a feedback loop where a Claude Code agent triages bad comments and opens PRs.

- Techniques: Deterministic analysis then LLM narration; Scenario-based LLM-as-judge regression set; Channel-injected events into a running coding agent; Latency-first model selection for interactive output; Iterative context pruning
- Tools: Stockfish, Maia (human-move prediction model), Gemini 3 Flash, Claude Code, Claude Code Channels, GPT-5 Mini, OpenRouter, Slack, GitHub

## [MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps](../videos/o-zkvb0iFDQ.md)
`o-zkvb0iFDQ` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: product-ux

MCP Apps lets an MCP tool return an interactive UI that the host renders in a sandbox, with UI events routed back through the host so vendors keep their branding and the host keeps conversation context.

- Techniques: Tool returns a UI resource; Route UI events through the host; Choose the message type by how much control you need; Sandboxed host renderer; Pick a UI generation mode per host; Build with the official SDK and skills
- Tools: MCP Apps, MCP-UI, Claude, ChatGPT, VS Code, Cursor, GitHub Copilot, PostHog, Shopify, Hugging Face, Booking, Airbnb

## [Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase](../videos/JT3OzDKrucU.md)
`JT3OzDKrucU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: skills-self-improvement, evals, context-engineering

Pedro Rodrigues (Supabase) on writing a product skill for agents, using a three-condition eval to show skills plus MCP beat MCP alone. Main lesson: agents need guidance, not more context.

- Techniques: Three-condition skill eval; Inline must-not-miss rules; Skill as pointer to live docs; Dev-first schema workflow with a deferred migration; Start minimal and iterate
- Tools: Supabase, Supabase advisor, Braintrust, Claude Code, Codex, Vercel skills package, MCP, SSH, Postgres

## [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](../videos/ynJyIKwjonM.md)
`ynJyIKwjonM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: rag-retrieval, context-engineering, skills-self-improvement

Leonie Monigatti (Elastic) argues context engineering is mostly agentic search, then walks through live demos of semantic search, ES|QL query tools, skill loading, and grep-style shell search, and when to use each.

- Techniques: Layered tool descriptions; Errors returned to the agent; Progressive disclosure for skills; Outsource aggregation to the search engine; Shell tool with semantic grep; Hybrid shell plus database verification; Log tool calls to find where specialization is needed; Use the file store as memory and offload old results
- Tools: LangChain, Elasticsearch, ES|QL, Jina embeddings v5, Jina grep (captioned as Gina grep), OpenAI GPT-5.4 nano and mini, shell / bash tool, Claude Code, OpenClaw (captioned as OpenCloud, exec tool)

## [MCP = Mega Context Problem - Matt Carey](../videos/YBYUvGOuotE.md)
`YBYUvGOuotE` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: sandboxing-execution, context-engineering

Cloudflare's Matt Carey argues that dumping every API endpoint into MCP tools blows up agent context, and that progressive discovery (tool search, CLIs, or code mode with typed SDKs run in isolates) is the way out.

- Techniques: Progressive tool discovery via tool search; Code mode over a generated typed SDK; Isolated execution of model-written code with programmable guardrails; Save agent-generated code as mini-scripts; Rate-limit APIs for agent callers
- Tools: MCP (Model Context Protocol), MCP SDK, OpenAPI, TypeScript, Cloudflare Workers, Dynamic Workers (workerd), V8 isolates, Wrangler, Cloudflare D1, Cloudflare Access, Claude Code, OpenClaw

## [The Future of MCP — David Soria Parra, Anthropic](../videos/v3Fr2JR47KA.md)
`v3Fr2JR47KA` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: context-engineering, agent-architecture

David Soria Parra (Anthropic) on where MCP is heading: MCP apps, progressive tool discovery, code-style tool composition, and the 2026 protocol roadmap.

- Techniques: Progressive tool discovery; Programmatic tool calling / code mode; Use structured output to enable composition; Agent-first tool design; Pick connectivity per task; Skills-over-MCP approximation
- Tools: MCP, MCP Apps, Claude Code, Cloudflare MCP server, V8 isolate, Lua interpreter, FastMCP, Python SDK, TypeScript SDK, OpenAI Agents SDK, Google ADK, LangChain

## [Gateways are All You Need — Karan Sampath, Anthropic](../videos/CD6R4Wf3jnY.md)
`CD6R4Wf3jnY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: security-guardrails, governance-compliance, infra-cost-scaling

Anthropic forward-deployed engineer Karan Sampath argues enterprises should put one gateway in front of all MCP servers for auth, access control, observability and credentials, so teams build only business logic.

- Tools: MCP, Claude Code, Claude Agent SDK, claude.ai, Claude managed agents

## [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../videos/8txf05vVVl4.md)
`8txf05vVVl4` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: token-cost-efficiency, sandboxing-execution, agent-architecture

Cloudflare's Sunil Pai on "Code Mode": have models write code against an API instead of making many tool calls, cutting a 2,600-endpoint API from ~1.2M tokens to ~1K, inside capability-restricted sandboxes.

- Techniques: Search + execute two-tool facade; Code as the tool-call format; Zero-capability sandbox with explicit grants; Agent-facing developer experience; Operate on the app's raw state
- Tools: Cloudflare Workers, Cloudflare Dynamic Workers, V8 isolates, OpenAPI, PartyKit, Claude Opus, TLDraw-style canvas

## [Give Your Agent a Computer — Nico Albanese, Vercel](../videos/wflNENRSUb4.md)
`wflNENRSUb4` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: agent-architecture, sandboxing-execution, context-engineering

Nico Albanese (Vercel) live-builds a coding-style agent with AI SDK 6: a tool loop, web search, a persistent named sandbox running bash, file-based memory and self-written scripts, plus notes on context pruning and subagents.

- Techniques: Single-definition tool loop agent; Typed UI messages from the agent definition; Named persistent sandbox per session; Bash-only tool for a coding-style agent; Call options plus runtime context injection; File-backed memory injected into the system prompt; Per-step hook for message slicing; Subagents and handoff instead of compaction; Plan file with objective and checkboxes
- Tools: Vercel AI SDK 6, Vercel AI Gateway, Vercel Sandbox (persistent named sandboxes, beta), Next.js, Zod, OpenAI provider (web search tool), Anthropic provider (bash/computer tools), Vercel Workflow (durable steps), OpenCode, Amp (handoff tool)

## [One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS](../videos/EmhRyw6xeT0.md)
`EmhRyw6xeT0` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: security-guardrails, enterprise-adoption

Garrett Galow (WorkOS) explains cross-app access (XAA): the enterprise IdP brokers silent, short-lived MCP tokens so users stop clicking consent screens and IT regains revocation and visibility.

- Techniques: Cross-app access via ID-JAG token exchange; IdP-side allow-list for app-to-app access; Short-lived access tokens with silent re-mint; Audience URL as the routing key; Server-side ID-JAG acceptance
- Tools: MCP, Claude Code, Cursor, Okta, Figma, WorkOS, Microsoft Entra, SCIM, CIMD, DCR, OAuth, OIDC

## [Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind](../videos/cVzf49yg0D8.md)
`cVzf49yg0D8` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: voice-multimodal, agent-architecture, context-engineering

Google DeepMind hands-on workshop on building agents with the Gemini Interactions API (server-side state, background runs, skills) and the Live API (native-audio voice agents), with live demos that partly failed.

- Techniques: Chained interactions via previous ID; Async background runs with polling or webhooks; Skill that links to live docs; Tool loop with recursion; Server-to-server Live proxy; Ephemeral token for direct browser connection; Context window compression for long Live sessions; Voice persona through system instructions; Send a single image and then audio
- Tools: Gemini Interactions API, Gemini Live API, Google AI Studio, Gemini 3 Flash / 3.1 Flash Live, Lyria 3, Nano Banana, Google Search grounding, uv, FastAPI, Context7, skills.sh, Antigravity

## [Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs](../videos/DCZZ3AJKzuc.md)
`DCZZ3AJKzuc` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: voice-multimodal, agent-architecture

ElevenLabs' Luke Harries argues chat agents should add voice, and previews VoiceEngine, a wrapper that adds STT, TTS and turn-taking to an existing chat agent without a rebuild.

- Techniques: Voice wrapper around an existing agent; Client-side vs server-side tools for voice; Prompt a coding agent with a conversion skill
- Tools: ElevenLabs VoiceEngine, ElevenLabs Scribe (speech-to-text), ElevenLabs V3 (text-to-speech), ShadCN / Vercel-style UI components

## [Scaling GitHub for your Agents — Sam Morrow, GitHub](../videos/0n3MKk7r60w.md)
`0n3MKk7r60w` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: context-engineering, security-guardrails

GitHub's MCP server lead on scaling a remote MCP server: why too many tools hurt agents, how defaults and tool-set grouping work, token-trimmed outputs, scope-based auth, and a stateless design.

- Techniques: Per-request server construction with policy-filtered tools; Scope-filtered tool listing with step-up auth; Tool-set grouping with defaults tuned from usage data; Output-token tailoring per tool; Server-side composition to encode intent; Cross-tool eval for description tuning; Wrap read-only tools in a CLI to test agent use
- Tools: GitHub MCP server, Claude Code, VS Code, Redis, Cloudflare code mode, Anthropic tool search, Pi

## [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../videos/mYSRn6PC1mc.md)
`mYSRn6PC1mc` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: agent-architecture, evals, context-engineering

Workshop on building a deep-research agent (MCP server plus Claude Code skills) that feeds a separate LinkedIn writer workflow with evaluator-optimizer review and a calibrated LLM-judge eval loop.

- Techniques: Autonomy-ladder architecture choice; Tools as specialists inside one agent; Delegation to keep context lean; Files as the inter-agent contract; Guideline plus static style profiles; Start with many few-shot examples, then trim; Evaluator-optimizer with fresh context and typed feedback; Synthetic eval inputs, real outputs, binary labels with critiques; Judge calibration with dev/test F1; MCP server exposes tools, prompts and resources; skills wrap prompts for progressive disclosure; Trace-based debugging with threads and traces
- Tools: Claude Code, FastMCP, MCP, Gemini API (grounding, multimodal YouTube), Firecrawl, Perplexity, Opik, Pydantic, git-ingest, uv, Python

## [Beyond Code Coverage: Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft](../videos/FWEInOtngmM.md)
`FWEInOtngmM` · AI Engineer · 2026-05-18 · q3 · practitioner · tutorial · also: testing-verification, coding-agents

Marlene Mhangami (Microsoft/GitHub) argues for red-green TDD with coding agents, testing user-facing behavior with Playwright instead of unit-test coverage, and shows a live Copilot CLI demo.

- Techniques: Red-green-refactor with a coding agent; Behavior-scoped tests against user-facing or stable-contract behavior; Connect the agent to Playwright (three options); Checkpoint before the healer runs; Operational hygiene for Playwright runs; Ingest requirements from M365 with WorkIQ; Prefer direct API tests when an API exists
- Tools: GitHub Copilot CLI, Playwright, Playwright MCP server, Playwright CLI, Playwright Agents, WorkIQ, Azure AI search, Claude, Codex, Ruby on Rails, Python (Playwright binding), TypeScript (Playwright binding)

## [I Stopped Using Grep and My Agent Got 10x Faster](../videos/gPeWb4_DMok.md)
`gPeWb4_DMok` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: rag-retrieval, coding-agents, token-cost-efficiency

Hands-on test of Claude Context, an MCP server that indexes a codebase into Zilliz/Milvus using Tree-sitter chunks, Merkle-based incremental updates and hybrid vector+BM25 search. Faster and richer on mid-size repos, slow to index on huge ones.

- Techniques: Set up Claude Context as an MCP server; Index once, then search many times; Compare indexed and plain agents side by side; Pick the repo size where the trade-off works; Test on a cheaper model to save subscription quota
- Tools: Claude Context (Zilliz MCP plugin for codebase indexing and search), Zilliz Cloud (serverless cluster), Milvus (vector database), OpenAI embeddings API, OpenCode (agent harness), GLM5 Turbo (model), Claude Code (mentioned as a possible agent), Claude Pro (subscription; weekly limit), Opus 4.7 (model, not tested), Tree-sitter (AST chunking, 9 languages), BM25 (keyword index), Merkle DAG with JSON snapshots (change detection)

## [Microsoft Just Solved Document Ingestion for AI Devs (MarkItDown)](../videos/9ZaiZzp4XcY.md)
`9ZaiZzp4XcY` · Better Stack · 2026-05-02 · q2 · intro · tutorial · also: rag-retrieval, data-engineering

Short intro to Microsoft's MarkItDown, an MIT-licensed Python tool and CLI that converts Office files, PDFs, images and audio into LLM-friendly Markdown, with a trade-off note against Pandoc, Unstructured and Docling.

- Techniques: Single-tool ingestion to Markdown (CLI); Python conversion with an LLM for images and charts; Pick the extractor by document difficulty
- Tools: MarkItDown, Pandoc, Unstructured, Docling, OpenAI Python client, Claude Desktop (transcript says 'Claw Desktop', auto-caption error), pip, MCP server (MarkItDown's)

## [Lightpanda: The 64MB Browser That is 60x FASTER than Chrome](../videos/yFWYK3wN88w.md)
`yFWYK3wN88w` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: voice-multimodal

Better Stack tests Lightpanda, a Zig-built headless browser that speaks CDP, against headless Chrome in a Claude SDK web-fetch agent: far less memory and faster at scale, but it fails on the Airbnb single-page app.

- Techniques: Lightpanda as a CDP fetch backend; Custom WebFetch tool in a Claude SDK agent loop; Fair headless-browser benchmark; Route by page type (implied by the verdict)
- Tools: Lightpanda, Chrome (headless), Puppeteer, Playwright, Claude SDK, Chrome DevTools Protocol, OpenClaw, Vercel agent browser, Chrome MCP server (referenced as a related video)

## [Anthropic's Managed Agents Are Different (Here's Why)](../videos/uxHolzq1NcA.md)
`uxHolzq1NcA` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: agent-architecture, claude-code, security-guardrails

Better Stack walks through Anthropic's Claude Managed Agents: building a Slack-connected agent with no hand-written orchestration code, its per-session-hour pricing, and the session/harness/orchestrator architecture with runtime credential vaulting.

- Techniques: Scaffold a managed agent via the Claude Code skill; Read-only toolset for a retrieval agent; Run setup once, then the runtime; Iterate in the Console and keep version history; Runtime credential injection (vault pattern); Separate durable session log from the executor
- Tools: Claude Managed Agents, Claude Console, Claude Code (managed-agent onboarding skill, `/claude-api managed agents onboarding`), Claude Agent SDK, TypeScript Claude SDK, Claude Opus, Claude Sonnet, Slack (Slack app and bot), Notion (built-in integration), MCP servers, OpenClaw, GitHub (private repo as data source)

## [Google's New CLI Is The Missing Piece for Claude Code](../videos/EKG9kX86u0s.md)
`EKG9kX86u0s` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: token-cost-efficiency, claude-code, coding-agents

Walkthrough of Google's new Rust Workspace CLI for agents: OAuth setup pain, CLI vs MCP token trade-offs, and design choices (nested JSON, runtime schema lookup, field masks) that keep context use low.

- Techniques: Agent-discoverable CLI with runtime help and schema; Nested JSON params flag for complex calls; Field selection to trim API responses; Layer skills on top of the CLI for guidance; Google Workspace OAuth setup for a CLI; Choose CLI vs MCP by token and portability trade-offs
- Tools: Google Workspace CLI (GWS CLI, Rust, written by a developer named Justin; no version stated), Claude / Claude Code, gcloud CLI (Google Cloud CLI, installed with Homebrew), Google Cloud Console (OAuth client, consent screen, Audience), Gmail, Google Drive, Google Slides, Google Sheets, Google Calendar (Workspace APIs used in the demos), SkillsSH (skills registry; over 100 Workspace skills), MCP (Model Context Protocol; compared, not reviewed in depth), Playwright CLI (mentioned as a prior example of an MCP server turned into a CLI; covered in an earlier video), Electrobun (Electron alternative powered by Bun; promoted at the end, not covered)

## [Chrome Just Became the Ultimate Agent Browser (Finally!)](../videos/51m_GGbXAng.md)
`51m_GGbXAng` · Better Stack · 2026-04-02 · q3 · practitioner · tutorial · also: coding-agents, dev-tools

Chrome 144+ lets the Chrome DevTools MCP server auto-attach to your running browser for login-state debugging, element selection and network inspection, plus an experimental CLI alternative that avoids MCP context cost.

- Techniques: Attach the Chrome DevTools MCP server to your running Chrome (auto-connect); Select an element in DevTools to hand it to the agent; Isolated profile for security-sensitive use; Sandboxed MCP server with an HTTP remote debugging port; Chrome DevTools CLI instead of the MCP server; Persist the debugging profile across sessions
- Tools: Chrome DevTools MCP server (auto-connect option), Chrome DevTools CLI (experimental, in the MCP skills directory), Google Chrome 144+, OpenCode, Claude Code (terminal), Lighthouse (audit tool used by the agent), Playwright (mentioned as a comparison), Agent Browser (mentioned as the presenter's preferred tool), Comet (mentioned as an AI browser), Claude Chrome extension (mentioned), React Grab (mentioned), Arc (mentioned; the presenter wishes the feature came to it)

## [Why Every Claude Code User Needs To Try AgentMail (Not Gmail)](../videos/U3TXAdpmvVk.md)
`U3TXAdpmvVk` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: claude-code, agent-architecture

Better Stack walkthrough of AgentMail, an email-inbox API for agents, shown through the CLI in Claude Code and a 30-second polling reply agent built on the Claude SDK. Mostly a demo, with no benchmarks.

- Techniques: Give each agent its own inbox via CLI + skill, not an MCP server; Split inboxes by purpose or by agent; Poll for mail with a Claude Code loop for short-lived checks; Custom polling reply agent on the Claude SDK
- Tools: AgentMail (API, dashboard, CLI, skill, MCP server, Python and TypeScript SDKs), Claude Code (loop feature, skills), Claude SDK, Claude Haiku, Google Workspace CLI (mentioned, previous video), Gmail, Codex, Gemini CLI, Electron (transcript says "Electrobon"; desktop app framework, mentioned only)

## [GPT-5.4: The Pros & Cons](../videos/c8b-tyFWlg8.md)
`c8b-tyFWlg8` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: models-research, coding-agents, token-cost-efficiency

Better Stack's 5-minute review of OpenAI's GPT-5.4: native computer use, tool search and a fast mode on the upside; slower output, a long-context price cliff and a generic UI style on the downside.

- Techniques: Tool search (deferred tool definitions); Playwright self-verification loop for front-end work; Compact context before the long-context price cliff; Fast mode as a priority tier
- Tools: GPT-5.4, Codex (5.3 referenced as the prior default), GPT-5.2 (referenced), Playwright (experimental skill), image generation skill (unnamed), Opus 4.6, Gemini, Artificial Analysis (benchmarks), Design Arena (design ranking)

## [I Didn't Know This Was Possible Until Now](../videos/LqN_ItMqovA.md)
`LqN_ItMqovA` · AI LABS · 2026-04-02 · q3 · practitioner · review · also: token-cost-efficiency, claude-code, context-engineering

A team's walkthrough of MCP context bloat and a runtime MCP-to-CLI converter (MCP2CLI), plus CLAUDE.md and skills rules that keep large tool outputs out of the context window.

- Techniques: Run MCP2CLI without installing it; Give the agent the MCP access tokens through environment or file references; Verify MCP connections by asking the agent to count the tools; CLAUDE.md rule to consult docs before coding; Move per-MCP guidance from CLAUDE.md into one skill per MCP; Ask for TOON output for verbose documentation MCPs; Redirect large MCP output to a file and grep it; Use Claude's browser extension for stateful browser testing

## [Claude Code is Expensive. This MCP Server Fixes It (Context Mode)](../videos/QUHrntlfPo4.md)
`QUHrntlfPo4` · Better Stack · 2026-04-02 · q3 · intro · review · also: token-cost-efficiency, context-engineering

Better Stack demo of Context Mode, a Claude Code MCP plugin that indexes large tool outputs in local SQLite FTS5 and keeps a small snapshot across compaction. Practical, with one small measured example.

- Techniques: Index large tool output into a local FTS5 store; Priority-tiered snapshot injected on compaction; Remember failed attempts across resets; Install Context Mode in Claude Code; Install Context Mode in Gemini CLI or VS Code Copilot; Measure the savings with the stats command; Demo prompt for indexed log analysis
- Tools: Claude Code, Context Mode, SQLite, FTS5, Playwright, GitHub, Gemini CLI, VS Code Copilot, npm, Python

## [Google Just Solved The Greatest Limitation of AI Agents](../videos/uprZUcv0FSc.md)
`uprZUcv0FSc` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: voice-multimodal, coding-agents

Walkthrough of WebMCP, a proposed browser standard where websites register callable tools for agents instead of agents guessing from screenshots or DOM. Covers declarative and imperative APIs, per-page tool loading, and current limits.

- Techniques: Declarative WebMCP tool on an HTML form; Imperative WebMCP tool registration per route; Scope tool lists to the page (contextual loading); Write tool descriptions for a cold reader; Inspect tool schemas with the Model Context Tool Inspector extension; Test with the Gemini-backed demo paths
- Tools: WebMCP, Chrome Canary, Chrome 146, Chrome Labs WebMCP repo, Model Context Tool Inspector extension, Claude Code, Gemini (built into Chrome; Gemini API key option in the demo), Next.js, React, Zen browser, Community WebMCP bridge (unnamed, not identified), Brilliant (sponsor)

## [NEW Browser API That Makes AI Agents Actually Work (WebMCP)](../videos/jI2mYU8-PqU.md)
`jI2mYU8-PqU` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: security-guardrails

WebMCP is a proposed browser API, backed by Google and Microsoft, that lets a site's front-end expose its own features as tools for AI agents. The speaker demos it in Chrome Canary and argues it beats agents scraping pages.

- Techniques: Imperative WebMCP tool registration; Read-only state tool for on-page data; Declarative WebMCP via HTML form attributes; Design principle: expose explicit tools, not the whole UI
- Tools: WebMCP (browser API proposal), window.navigator.modelContext (proposed browser API), Chrome Canary, MCP (Model Context Protocol), React, Playwright, ChatGPT Atlas, Gemini, Arc, a browser extension used to drive the demo (unnamed)

## [How I Turned Claude Into a Design Tool with Pencil.dev](../videos/DFcvz2kcR74.md)
`DFcvz2kcR74` · Better Stack · 2026-03-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents

Walkthrough of Pencil, a free agent-driven design tool that Claude Code can drive over MCP to build dashboards and a bakery website, then code them. Shows a workable loop, with no benchmarks.

- Techniques: Drive a design tool from Claude Code via its MCP server; Build a UI from a UI kit; Blank-canvas site generation with a style guide; Fix AI design output by direct manipulation; Hand designs to the agent for implementation; Import existing Figma designs
- Tools: Pencil (pencil.dev), Pencil MCP server, Pencil batch design tool, Claude Code, Figma, Figma MCP tool, Sketch, Sketch MCP tool, Lunaris UI kit, Halo UI kit, Nitro UI kit, Unsplash

## [Playwright CLI vs MCP Server: Which is Actually BETTER for Claude Code?](../videos/V2qjnBDZZ7A.md)
`V2qjnBDZZ7A` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: token-cost-efficiency, coding-agents, testing-verification

Better Stack runs the same Twitter-video download task through the Playwright CLI and the Playwright MCP server in Claude Code, and finds the CLI cheaper in context, with MCP better for portable agent loops.

- Techniques: Drive the browser through a CLI skill instead of an MCP server (in Claude Code); Turn a repeated browser check into a bash script for humans and agents; Keep MCP for portable agent loops and trim its tool list
- Tools: Playwright CLI, Playwright MCP server, Claude Code, agent-browser (a Rust CLI that runs Playwright under the hood; spelled 'Vasell' in the auto-captions)

## [Anthropic Have FINALLY Solved the MCP Context Nightmare](../videos/1RpGVqgqLaE.md)
`1RpGVqgqLaE` · Better Stack · 2026-02-02 · q2 · intro · news · also: token-cost-efficiency, context-engineering, claude-code

Claude Code's MCP tool search loads only the 3-5 most relevant tools on demand instead of preloading every schema, cutting context use. A short explainer that compares it with Cloudflare's code-orchestration approach.

- Techniques: Threshold-gated tool search; Programmatic tool orchestration; Wrap MCP servers as CLI commands
- Tools: Claude Code, Claude Opus, MCP (Model Context Protocol), Cloudflare Workers, Cloudflare (programmatic tool calling), Cursor, Agent Skills, mcporter, Python, TypeScript, Better Stack MCP server, Gemini (1M-token window, mentioned only)

## [This Exceeded Every Expectation I Had](../videos/iC9loBJjduM.md)
`iC9loBJjduM` · AI LABS · 2026-02-02 · q3 · practitioner · tutorial · also: context-engineering, claude-code, token-cost-efficiency

Applies Cursor's dynamic context discovery ideas to Claude Code via CLAUDE.md: offload big tool output and chat history to files, lazy-load MCP tools, and grep logs instead of re-running them.

- Techniques: Offload large MCP responses to files; Per-session history file as compaction insurance; Timestamped terminal logs with grep-and-tail retrieval; Progressive-disclosure skills; Lazy MCP tool loading with the experimental MCP CLI flag
- Tools: Claude Code, Cursor, Antigravity, Codex, Gemini CLI, Claude Chrome extension, CLAUDE.md, MCP (Model Context Protocol), MCP CLI (experimental Claude Code flag), Claude advanced tool search (developer platform), Cursor semantic search, grep

## [This is How I Design With Stitch Now](../videos/VNx9Gy5pHZI.md)
`VNx9Gy5pHZI` · AI LABS · 2026-02-02 · q3 · practitioner · tutorial · also: coding-agents, testing-verification, vibe-coding-app-building

A Stitch-as-MCP design workflow in Claude Code: plan first, generate one long landing page, pull its HTML, then test with Vercel's snapshot-based Agent Browser. The Stitch MCP wrapper is unofficial.

- Techniques: Stitch MCP for agent-driven design generation; Plan-mode UI guide before design; One long page prompt instead of per-section prompts; Pulling Stitch screen code into a project; Follow-up refactor after code dump; CLAUDE.md rules that mandate a test tool; Snapshot-driven UI testing with Vercel Agent Browser
- Tools: Google Stitch, Stitch MCP (community, unofficial), Google Cloud SDK / gcloud CLI, Homebrew (brew), Claude Code (plan mode, CLAUDE.md), Gemini 3 Flash, Next.js, curl, Vercel Agent Browser, Claude's Chrome extension (compared), Playwright (compared), Puppeteer (compared)

## [Claude Now Builds Custom Interfaces to Plan Your Life](../videos/jRBiWoSKpIo.md)
`jRBiWoSKpIo` · Better Stack · 2026-02-02 · q2 · intro · review · also: claude-code, coding-agents

A 4-minute demo of Claude Canvas, an open-source Claude Code plugin that opens tmux split panes rendered with Ink to preview emails, flights and calendar items, with the pane sending user choices back to Claude. The data shown is invented, and the "future of terminal assistants" claim is opinion.

- Techniques: Skill-routed CLI that spawns a split pane; Preview a draft in a pane before sending; Bidirectional pane-to-agent IPC for user selections
- Tools: Claude Code, Claude Canvas (Claude Code plugin), tmux, bun, Ink, Ghostty, iTerm, Apple Terminal, Gmail MCP server (mentioned as a possible source of From/To fields, not demoed), Astro (creator mentioned as suggesting generated UI)

## [Claude Code Can Now Control Your Browser (Thanks to Vercel)](../videos/P7JrP57AxR0.md)
`P7JrP57AxR0` · Better Stack · 2026-02-02 · q3 · practitioner · review · also: testing-verification, coding-agents, voice-multimodal

Walkthrough of Vercel's open-source Agent Browser, a headless-Chromium CLI that lets a coding agent snapshot, click and test web pages, with a comparison to Browser Use and the Playwright MCP server.

- Techniques: Agent-driven UI verification loop; Install the CLI globally and let the agent discover it; Generate a bash regression test from the browser session; Prefer snapshot references, fall back to semantic locators
- Tools: Agent Browser (Vercel, open source), Rust, Node.js, Playwright, Chromium, OpenCode, GLM 4.7, npm, shadcn/ui (transcribed as 'Shadxian'), React (transcribed as 'Riat'), Vite, Browser Use

## [How Crypto Is Secretly Taking Over Banking with @SarahBensonCodes  | Better Stack Podcast Ep. 8](../videos/taTXejPts4E.md)
`taTXejPts4E` · Better Stack · 2026-01-02 · q2 · intro · interview · also: dev-tools, enterprise-adoption

Better Stack podcast with Sarah Benson (Amber Data) on crypto vs Web3, tokenized real-world assets and smart-contract basics. Mostly opinion, with a short note on exposing data to LLMs via MCP.

- Techniques: Start a smart contract from an audited template; Expose analytics data to agent LLMs via MCP plus semantic tags; Private permissioned chain for institutional settlement; Vet a Web3 project before trusting it; Full-build tutorial structure
- Tools: Solidity, Rust, Forge (Foundry), Hardhat, React, TypeScript, web3.js, ethers.js, Thirdweb, Polymarket, pump.fun, Canton Network

## [Docker Just Fixed 90% of AI Coding By Releasing This](../videos/ZOutBmRai2M.md)
`ZOutBmRai2M` · AI LABS · 2026-01-02 · q2 · practitioner · review · also: token-cost-efficiency, sandboxing-execution

Docker's MCP toolkit walkthrough: one gateway in front of a vetted catalog, on-demand tool loading, and "code mode" where the agent chains MCP calls in a sandbox, keeping bulky results out of context.

- Techniques: Single MCP gateway front door; On-demand tool discovery with find/add/remove; Code mode: chain MCP calls in a sandboxed script; Write bulky tool output to a file and return only the fields needed; Volume-backed state between tool calls; Merge repeated tool calls into one generated tool
- Tools: Docker MCP Toolkit, Docker MCP Catalog, Docker MCP Gateway, Docker MCP find/add/remove tools, mcp exec tool, Docker containers and volumes (sandbox), Claude Code, GitHub MCP server, Notion MCP server, Cloudflare code mode (referenced), Anthropic MCP token post (referenced)

## [This Tool Turns Claude Into an Automation Engine (ActivePieces)](../videos/K_6IYK2cIqs.md)
`K_6IYK2cIqs` · Better Stack · 2026-01-02 · q2 · intro · review · also: dev-tools, infra-cost-scaling

Quick review of ActivePieces, a self-hostable, MIT-licensed Zapier/Make alternative whose integrations are also exposed as MCP servers; shallow demo, with the Claude angle mostly asserted rather than shown.

- Techniques: Self-host ActivePieces with Docker; Start from a template in New flow; Build a flow from scratch: trigger, AI step, sink; Expose automation pieces to Claude Desktop through their MCP URL
- Tools: ActivePieces, Docker, Claude Desktop, Claude, Cursor, MCP, Zapier, Make.com, Gmail, OpenAI, Notion, VPS

## [The Best MCP Servers of 2025](../videos/kRxdsv1ZY1E.md)
`kRxdsv1ZY1E` · AI LABS · 2026-01-02 · q2 · intro · review · also: context-engineering, coding-agents

AI LABS roundup of six MCP servers for AI coding agents: Context7, Docker MCP, ShadCN, Google's managed servers, Notion and Supabase. Anecdotal, partly sponsored, and thin on measurements.

- Tools: Model Context Protocol (MCP), Context7, Ref, Docker MCP (MCP Find, MCP Add), Cloudflare code mode (concept), ShadCN registry MCP, shadcn components.json, Aceternity UI, Magic UI, Gemini 3, Google Maps MCP, BigQuery MCP

## [Inngest's New Tool Is Insane For AI Coding](../videos/8vvTHnta59A.md)
`8vvTHnta59A` · AI LABS · 2026-01-02 · q2 · intro · review · also: coding-agents, testing-verification

Short demo of Inngest's MCP server for its local dev server, showing a coding agent sending test events, polling run status and checking its own workflow runs in Claude Code.

- Techniques: Wire an event-driven dev server into Claude Code via MCP; Agent-driven verify loop: send event, poll run, check result; Switch model provider through a gateway in one prompt
- Tools: Inngest, Inngest dev server, Inngest MCP server, Claude Code, Cursor, Next.js, OpenAI API, Vercel AI Gateway (auto-captioned as 'Versal'), Puppeteer MCP, CLAUDE.md, .mcp.json

## [I Tried TanStack AI... (it's good)](../videos/sdL6bF74t68.md)
`sdL6bF74t68` · Better Stack · 2026-01-02 · q3 · intro · review · also: dev-tools

Hands-on flyby of TanStack AI (alpha): server-side streaming chat, a typed useChat client hook, and isomorphic tool definitions wired to web search. The speaker finds little that differs from Vercel's AI SDK.

- Techniques: Typed server chat route with stream response; Client useChat hook with server-sent events; Shared tool definition for server execution and client typing
- Tools: TanStack AI (alpha), Vercel AI SDK, OpenAI adapter, Anthropic adapter, Gemini adapter, Ollama (captioned as 'Alarma'), OpenRouter (no adapter yet), React, Solid, Vanilla JS client, Svelte (planned), GPT-5

## [The Greatest Design System I've Ever Used](../videos/61Z2jLH4yGU.md)
`61Z2jLH4yGU` · AI LABS · 2026-01-02 · q2 · intro · review · also: vibe-coding-app-building, product-ux

A short AI-design tool roundup: Design OS for guided planning, image generators, competitor-screenshot style extraction, Figma-to-Lottie animation and an HTML-to-Figma MCP, with a sponsored agency pitch at the end.

- Techniques: Design OS planning loop before building; Competitor style extraction into Claude Code; Figma animation to Lottie to Claude Code; HTML to Figma via MCP
- Tools: Design OS (Builder Methods), Claude Code, Claude, Cursor, GitHub Copilot, Viscom, Google Mixboard, Nano Banana, Go Full Page (browser extension), Figma, Magic Animator (Figma plugin), Lottie (Figma plugin)

## [OpenAI Swarm Hype Explodes: AgentKit Drives Multi-Agent AI Revolution](../videos/oV3IjJSXQyM.md)
`oV3IjJSXQyM` · Better Stack · 2026-01-02 · q2 · intro · news · also: multi-agent, agent-architecture

Better Stack argues OpenAI's deprecated Swarm is not back and that AgentKit (Oct 2025) is the real multi-agent upgrade, but the video gives few technical details and mostly unsourced claims.

- Techniques: Migrate off Swarm-style stateless handoffs to a framework with state and tracing; Budget multi-agent traces for latency and retries; Built-in trace-and-score evals for agent performance
- Tools: OpenAI Swarm (deprecated March 2025), OpenAI Agents SDK, OpenAI AgentKit (Agent Builder, ChatKit, connector registry), OpenAI Chat Completions API, RFT (reinforcement fine-tuning) beta, o4-mini (transcribed 'O4 Mini'), GPT-5 (multi-model stack, mentioned without detail), MCP (Model Context Protocol; transcribed 'MPC'), DeepSeek (transcribed 'DeepSeq'), Llama (transcribed 'Ulma 3')

## [I Gave Claude Code Permanent Memory - The Results Are Shocking](../videos/EsFa7W-FYdM.md)
`EsFa7W-FYdM` · Better Stack · 2026-01-02 · q2 · intro · review · also: context-engineering, coding-agents

Beads gives coding agents a git-synced issue tracker (SQLite locally, JSON Lines in git) so task state survives context resets. A 4-minute overview with claimed context savings and no measured results.

- Techniques: Repo-local issue tracker as agent working memory; Dependency-graph querying instead of loading planning docs; Compaction of closed issues; Spec first, then issues
- Tools: Beads, Beads MCP server, SQLite, JSON Lines, Git, Jira, SpecKit, Kiro, Claude Code, Sourcegraph, AMP

## [xAI Dropped Grok-4.1… and It’s Actually SCARY Good](../videos/kRQgww49C90.md)
`kRQgww49C90` · Better Stack · 2026-01-02 · q2 · intro · news · also: models-research, observability

Better Stack recap of xAI's Grok 4.1 beta and Grok 4.1 Fast API (Nov 2025): emotional intelligence, lower hallucinations, a 2M-context tool-calling model, and a dummy-log SRE demo. Mostly restates vendor claims.

- Techniques: Agent-side log triage prompt on a fast tool-calling model; Server-side tools inside one model call (Agent Tools API)
- Tools: Grok 4.1 (beta), Grok 4.1 Fast, Grok 4.1 Thinking / non-thinking, Grok 4, Grok 5 (expected Q1 2026, not released), Agent Tools API, xAI X search (xSearch), Grok.com, Gemini 3.0, LM Arena leaderboard, EQBench, Creative Writing v3 benchmark

## [Building AI That Actually Helps You Live Better | Better Stack Podcast Ep. 7](../videos/46EsyQYKMjA.md)
`46EsyQYKMjA` · Better Stack · 2025-12-02 · q3 · intro · interview · also: security-guardrails, context-engineering, agent-architecture

Better Stack podcast interview with Ben, founder of Spec, a macOS-native personal-context assistant; main engineering points are local-first data, OS-level access, and side effects gated outside the model.

- Techniques: Permission-scoped local data access for apps with no API; Split draft and send tools, with the send gated by a human click; Write-only agent sandbox; Event listeners and timed services instead of a single chat loop; Living context with distilled per-thread summaries as the trigger input; Route models by task type, separating persona from reasoning
- Tools: Spec (macOS/iOS app, Swift), Swift, Granola, Riverside, Claude Opus 4, Claude Sonnet 4, Claude Sonnet 4.5, Claude Haiku 4.5, GPT-5, GPT-OSS, Gemini 2.5, MCP

## [Claude Just Solved Their Biggest Problem](../videos/opZpIN8g_6M.md)
`opZpIN8g_6M` · AI LABS · 2025-12-02 · q3 · intro · review · also: context-engineering, token-cost-efficiency, sandboxing-execution

Walkthrough of Anthropic's paper on running MCP servers as code files instead of direct tool calls, to cut context bloat; no implementation shown.

- Techniques: Filesystem-based MCP tool catalogue with progressive disclosure; Result shaping inside the execution script; Code-owned control flow between tool calls; Placeholder returns for sensitive data; File-based state for resumable runs
- Tools: MCP (Model Context Protocol), Claude, Claude skills, Memory tool, Cloudflare code mode, TypeScript, index.ts (file convention from the paper)

## [You can literally win 50K... Just By Prompting](../videos/yq3EN46qw_U.md)
`yq3EN46qw_U` · AI LABS · 2025-12-02 · q2 · intro · tutorial · also: coding-agents

Sponsored walkthrough of Apify's $1M actor-building challenge (Nov 2025 to Jan 31 2026), showing how Claude Code plus Apify's agent prompt and CLI can produce a publishable actor quickly.

- Techniques: Template to agent prompt to CLI deploy; Actor publish checklist; Idea sourcing from published wish lists
- Tools: Apify (actor platform, Apify Store, Apify console), Apify CLI, Claude Code, Google Maps (scraper input requires a Google API key), Gemini MCP (actor built by the host), MCP server template (Apify), Discord

## [A Problem You Never Knew About](../videos/w3pmfaczpLc.md)
`w3pmfaczpLc` · AI LABS · 2025-12-02 · q2 · intro · review · also: product-ux

Sponsored demo of Thesis's C1, a generative UI API that turns LLM output into interactive components (forms, tables, dashboards) via a React SDK. Pitch-level; no evaluation data.

- Techniques: Generative UI middleware in front of the LLM; Two-step retrofit of an existing AI app; Form submission as the next prompt; Documentation skill for coding agents
- Tools: Thesis C1 (generative UI API), C1 React SDK, Vercel AI SDK (transcribed as 'Versal AI SDK'), GPT-5, Claude, Claude skill (custom, for C1)

## [Claude 4 is HERE and is taking on Cursor... (Claude Code)](../videos/-Qdlg-dkrX8.md)
`-Qdlg-dkrX8` · Better Stack · 2025-11-02 · q3 · intro · news · also: coding-agents, claude-code, models-research

Better Stack's launch-day recap of Claude 4 (Sonnet 4, Opus 4) with a short Claude Code VS Code demo. It mostly relays Anthropic's benchmark and behavior claims, with light skepticism.

- Techniques: Claude Code inside VS Code or JetBrains via the CLI; Paste-the-error bug fix; Agent-maintained memory file; Remote MCP servers through the Claude API; One-hour prompt cache TTL; Tagging Claude Code in GitHub PRs
- Tools: Claude Opus 4, Claude Sonnet 4, Claude 3.7 Sonnet, Claude Code, Claude Code SDK, Claude API (remote MCP connector), VS Code, JetBrains IDEs, Next.js, Excalidraw, GitHub Copilot agent, Codex 1

## [The PERFECT Design Workflow with Claude Code](../videos/9uFVCxfkLCo.md)
`9uFVCxfkLCo` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents, context-engineering

Walkthrough of capturing a website component with the Web2 MCP Chrome extension, cloning it one-to-one with a Claude Code/Cursor agent using a modified CLAUDE.md, and generating variants with SuperDesign. Mixed results, with a Rocket.new sponsor segment.

- Techniques: Capture an element with Web2 MCP and reference it by ID; Initialize SuperDesign rule files and edit CLAUDE.md for one-to-one cloning; Two-session workflow: clone first, then generate variants; Use SuperDesign's canvas view to inspect how a design was produced
- Tools: Web2 MCP (paid Chrome extension and MCP server; $2.50/month Pro tier as stated), MCP Pointer (open-source alternative, judged weaker), SuperDesign (superdesign.dev; editor extension with rule files for Cursor, Windsurf and CLAUDE.md), Claude Code, Cursor, Windsurf, Stagewise (mentioned as a prior featured tool), Arc browser, shadcn/ui (described as the common component library), Rocket.new (sponsor; no version), Netlify (mentioned in the Rocket.new segment)

## [3 Ways to Clone Any Site Using Cursor AI](../videos/zmP8Pl-MJXw.md)
`zmP8Pl-MJXw` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, coding-agents

Three practical ways to clone a website's design into a Next.js or HTML project using Cursor plus Gemini, the Figma MCP, or the Firecrawl MCP, with the presenter noting where each one falls short.

- Techniques: Full-page screenshot capture for layout cloning; Marker-based splitting of generated code into a Next.js app; Figma selection link to Cursor via the Figma MCP; Turning a GitHub repo into indexable docs for Cursor; Scraping a live site with Firecrawl MCP for a structural clone; Build clones in a framework, not plain HTML
- Tools: Cursor, Gemini (canvas feature), Claude artifacts, ChatGPT, Chrome DevTools (command runner, full-size screenshot), React, Next.js, bash (integrate.sh script), Figma MCP, git2doc, Firecrawl MCP (8 tools), Wallhaven (example site)

## [Google A2A Protocol Explained: Tutorial, Demo, & How It Works with MCP & AI Agents](../videos/GUozMSpnmcc.md)
`GUozMSpnmcc` · AI LABS · 2025-11-02 · q2 · intro · review · also: multi-agent

Explainer of Google's A2A (agent-to-agent) protocol: agent cards for discovery, how it complements MCP, a hiring demo, and a CrewAI sample repo to clone.

- Techniques: Select a remote agent by its card before delegating; Expose agent cards as MCP resources; Generate A2A client and server code from the docs; Quickstart with the sample agent repo
- Tools: A2A protocol (Google), MCP (Model Context Protocol), Google Agentspace (spoken as 'agent space'), Google Agent Development Kit (ADK), LangChain, CrewAI, Gemini API, Cursor (@docs feature), Google A2A GitHub repo (sample agents; name not stated)

## [Copilot Kit Made My React App Think For Itself Using AI](../videos/rYVbw1wSnMk.md)
`rYVbw1wSnMk` · Better Stack · 2025-11-02 · q2 · intro · review · also: product-ux, dev-tools

A 5-minute walkthrough of CopilotKit, which lets a React app expose its data to an LLM, let the model change app state, and call MCP tools, with a self-hosted Express runtime.

- Techniques: Server-side runtime endpoint for the LLM key; Expose app data to the model via a readable-context hook; Let the model change app state via an action hook; Self-hosted MCP through the Vercel AI SDK MCP client; Cloud-hosted MCP as a frontend-only change
- Tools: CopilotKit, React, Vite, Tailwind CSS, Next.js, Express, Anthropic API (Claude), Composio (MCP server), GitHub (via Composio MCP tools), Model Context Protocol SDK, Vercel AI SDK (experimental MCP client), LiteLLM (mentioned as a wish, unmet)

## [Does GitHub's New MCP Server KILL Git Commands? (w/ Cursor)](../videos/3ivTdBgzMMI.md)
`3ivTdBgzMMI` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, dev-tools

Better Stack runs one timed repo-and-PR task through the GitHub MCP server inside Cursor, finds it about twice as slow as Git aliases and the GitHub CLI, and advises against it for simple Git work.

- Techniques: Run the GitHub MCP server in Cursor; Manual Git and PR flow with aliases (baseline); Fall back to direct git when the agent stalls
- Tools: GitHub MCP server (new, Docker-based; the older server ran via npx), Cursor (IDE with MCP settings), Docker, Git, GitHub CLI / Git aliases (baseline), NeoVim, macOS dictation feature, Supabase MCP server, Figma MCP server, Playwright MCP server

## [Agno AI Agent Tutorial: Build & Run AI Agents with Agent UI + MCP + CrewAI (Best Tutorial)](../videos/RWQv6JV7rKw.md)
`RWQv6JV7rKw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: multi-agent, agent-architecture

A short tutorial on Agent UI, an open-source Next.js chat front-end for agents. It shows swapping Agno's playground for a FastAPI backend and routing between specialist agents over A2A.

- Techniques: Install Agent UI via the docs' npx template; Swap the Agno Playground for your own backend; Main-agent router over specialist endpoints; Cap reply length with the system prompt
- Tools: Agent UI, Agno, Agno Playground, Next.js, npx, FastAPI, OpenAI SDK, A2A (agent-to-agent protocol), Cursor, LangChain, gpt-4o-mini, Gemini 2.5 Pro (mentioned in the demo answer, not used by the presenter's own setup)

## [The WhatsApp Trick That’s Running My Business for Me](../videos/BjqR3Ddb71k.md)
`BjqR3Ddb71k` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: voice-multimodal

A 6-minute setup tutorial for a local WhatsApp MCP server plus the ElevenLabs MCP in Claude Desktop, so an agent can read WhatsApp chats and reply with a synthesized voice note.

- Techniques: Local WhatsApp MCP setup in Claude Desktop; Adding the ElevenLabs MCP with one env var; Prompt the agent with an explicit contact name; Windows build fix for the WhatsApp bridge
- Tools: Claude Desktop, WhatsApp MCP server (Go bridge + MCP), ElevenLabs MCP, ElevenLabs voice cloning, uv / uvx, Go, Cursor, Windsurf, Blender MCP, Swift (planned app), MCP

## [Zapier MCP: The Only MCP Server That Cursor Needs](../videos/tFFsX97HzEk.md)
`tFFsX97HzEk` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, security-guardrails

Zapier's hosted MCP server replaces a pile of local MCP servers with one endpoint, per-action tool selection and fixed-argument control. Useful setup detail, but a vendor walkthrough with a hype title.

- Techniques: Consolidate local MCP servers into one hosted endpoint; Add only the specific tool actions an agent needs; Fix routing fields, leave content fields to the model; Override model-sent arguments on the server side; Connect a Postgres database for read and write actions
- Tools: Zapier MCP server, WebParse by Zapier, Cursor, mcp.json, Postgres, Official Postgres MCP server (read-only, per presenter), Supabase MCP server (noted as missing from Zapier), Composio (compared; manual auth grants), Slack, Jira, GitHub, GitLab

## [Time to SWITCH...Claude Code vs Cursor debate just ended](../videos/tCy5cJRErTg.md)
`tCy5cJRErTg` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, coding-agents, dev-tools

Walkthrough of Claudia, a build-from-source desktop GUI over Claude Code with custom agents, per-prompt checkpoints, a preview pane and GUI MCP setup, pitched as a reason to leave Cursor. Hype title; single-tool demo.

- Techniques: Read-only research subagent; Checkpoint before a risky AI change; Visual bug loop with a preview pane; Add MCP servers through a form; Build Claudia from source
- Tools: Claudia, Claude Code, Cursor, Rust, Bun, git, Next.js, shadcn/ui, Claude Pro plan ($20), MCP (stdio and SSE servers), CLAUDE.md, HTML

## [The #1 Open Source AI Agent to Stop Overloading Cursor AI (Cursor MCP + ACI.dev Unified Server)](../videos/eWvaItBefYw.md)
`eWvaItBefYw` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: coding-agents

Setup walkthrough for ACI.dev's unified MCP server, which exposes search and execute meta-tools so Cursor or Windsurf can reach many MCP apps without loading each one; the speaker's performance and context claims are anecdotal.

- Techniques: Unified MCP server with search and execute meta-tools; Pasting the ACI usage prompt as a Cursor project rule; Recovering from 'user isn't authenticated' errors; Smoke-testing the connection
- Tools: ACI.dev unified MCP server, ACI App Store / agent playground, Cursor, Windsurf, Claude Desktop, Brave Search API, Archive (research papers app), Google Calendar integration, Figma MCP, GitHub MCP, Firecrawl MCP

## [Cursor AI Had a BIG PROBLEM — I Just Found the FIX](../videos/UngBxJ9uy70.md)
`UngBxJ9uy70` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, context-engineering, multi-agent

AI LABS walkthrough of GitMCP, which turns any GitHub repo into a hosted MCP docs server, shown as an alternative to Context7 for keeping Cursor grounded in current docs, with a three-agent A2A demo.

- Techniques: Per-repo hosted MCP docs via URL swap; Scope docs to one repo instead of a broad doc index; Use the hosted repo chat as a post-build spec check; Router agent plus domain specialist agents over A2A; Routing check by server log
- Tools: Cursor, Gemini 2.5, GitMCP (gitmcp.io), Context7 MCP, MCP (Model Context Protocol), A2A (Google Agent-to-Agent protocol), Claude Desktop, Windsurf, VS Code, Claude, LangGraph (docs example), Three.js (demo project)

## [Mastra: The AI Framework That Changes Everything](../videos/_dG8iZgmicQ.md)
`_dG8iZgmicQ` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: agent-architecture, memory

Beginner walkthrough of Mastra, a TypeScript agent framework: build an agent, add a tool, memory, working memory, an MCP server, and call it via API.

- Techniques: Minimal Mastra agent; Custom tool with zod output schema; Persistent chat memory; Working memory template; Adding MCP server tools to an agent; Calling a Mastra agent from code
- Tools: Mastra (TypeScript agent framework) and Mastra Core, Mastra CLI, Mastra playground and dev script, Mastra memory (Memory class, working memory), Mastra LibSQL storage store, Mastra MCP client, Firecrawl MCP server, zod (output schemas), Mastra Swagger API docs and Mastra client, Mastra 101 course (source of the system prompt, per the presenter), Whisper Flow (dictation, named as Whisperflow in captions), Claude Agent SDK (mentioned as the presenter's earlier video topic)

## [ChatGPT Apps vs n8n vs AgentKit: The Future of AI Automation](../videos/lcqlgif2hFA.md)
`lcqlgif2hFA` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, product-ux

Walkthrough of building a ChatGPT app as a self-hosted MCP server (Express, Google Places API) exposed through ngrok and registered in ChatGPT developer mode. Title promises an n8n/AgentKit comparison that never appears.

- Techniques: Prompt-driven MCP server scaffold for a ChatGPT app; Reuse an existing MCP server as a ChatGPT app; Expose localhost with ngrok for ChatGPT; Register the MCP endpoint in ChatGPT developer mode; Widget output over plain text, polished with ShadCN
- Tools: ChatGPT apps (OpenAI), OpenAI apps SDK, MCP (Model Context Protocol) SDK, Express, Google Places API, ngrok, ShadCN, Cursor, Codex, Claude Code, Make.com (sponsor), n8n (named in title only)

## [Shadcn Isn’t Just a Library Anymore… Here’s How to 10x Your UI](../videos/V8rGgwQ-VJ0.md)
`V8rGgwQ-VJ0` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, vibe-coding-app-building

Shows how a shadcn/ui MCP server (component demos and blocks) plus Cursor rule files and a plan-first workflow produces better React UI, then how TweakCN restyles the result.

- Techniques: Fetch-before-build loop with the shadcn MCP; Rule file that forces the MCP lookup order; Plan first, with components named and no code; Theme with TweakCN after the structure is done
- Tools: shadcn/ui, shadcn UI MCP server (GitHub repo), Cursor, Claude (chat, used for the initial plan), Claude desktop MCP configuration, Windsurf, Claude Code, TweakCN, GitHub personal access token

## [OpenAI Agent Builder... n8n Killer?](../videos/RBlHcHUvFKY.md)
`RBlHcHUvFKY` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: agent-architecture, pr-code-review

Hands-on walkthrough of OpenAI's new drag-and-drop Agent Builder, used to build a GitHub PR code-review agent; covers guardrails, structured outputs, MCP, widgets and evals, with bugs noted and a verdict that it does not yet replace n8n.

- Techniques: Input guardrail with a fail branch; Structured extraction gate before tool calls; Transform node to flatten nested outputs for a tool; Isolated reviewer context; Natural-language graders over traces; Widget output from a final agent; Adding a custom MCP server
- Tools: OpenAI Agent Builder, ChatKit, Agents SDK, Apps SDK, GitHub MCP server, Context7 MCP server, GPT-5, GPT-4.1, OpenAI vector store (file search), web search tool, code interpreter, n8n

## [SDKs, Stealth Models, and LLM Myths | Better Stack Podcast Ep. 2](../videos/w8x5Kdv-Za8.md)
`w8x5Kdv-Za8` · Better Stack · 2025-11-02 · q2 · practitioner · panel · also: models-research, dev-tools, security-guardrails

Better Stack panel (Aug 2025) on the Vercel AI SDK, stealth models like Sonic, OpenAI GPT Realtime, and Anthropic's model-behavior research, with much opinion and few verified numbers.

- Techniques: AI SDK backend core plus UI hooks; Per-provider reasoning option pass-through; Explicit stack pinning in prompts; Smell-test models with known-hard setup tasks; Scenario-based goal-conflict red-teaming; Jailbreak testing with non-English or fictional framing
- Tools: Vercel AI SDK, AI Elements, Next.js, Turborepo, React Server Components, OpenRouter, vLLM, Ollama, Mastra, Sonic (stealth model; hosts suspect Grok Code Fast 1), Horizon Alpha (stealth model), GPT-5

## [3 Ways to Make GENUINELY Stunning Websites Using Claude Code](../videos/McJluKfjVGk.md)
`McJluKfjVGk` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, claude-code, coding-agents

A walkthrough of three Claude Code workflows for building polished UIs: SuperDesign for iterative design canvases, ShadCN MCP for component-library builds, and Firecrawl or Figma MCPs for cloning existing designs.

- Techniques: SuperDesign canvas setup; Layout-then-theme-then-polish staging; Targeted correction round; ShadCN MCP plus a saved usage-rule slash command; Theme import from tweakcn; Site cloning with Firecrawl MCP; Figma MCP selection import; Animation snippet import from Animatopy
- Tools: Claude Code, SuperDesign (superdesign.dev, VS Code / Cursor extension), Cursor, VS Code, ShadCN UI, ShadCN MCP server, Firecrawl MCP, Figma MCP server, tweakcn, Animatopy, Colors (palette generator website), Next.js

## [Figma MCP Tutorial: The Best Way to Clone a Front-End](../videos/FJBLhd23f80.md)
`FJBLhd23f80` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, vibe-coding-app-building

A 5-minute tutorial on connecting an open-source Figma MCP server to Cursor, then having the agent generate HTML/CSS from a Figma page link instead of a screenshot.

- Techniques: Run a Figma MCP server over SSE and attach it to Cursor; Copy a link to a Figma selection and hand it to the agent; Force the agent to the node tool when it picks the wrong one; Combine the Figma link with a screenshot for corrections
- Tools: Figma MCP server (glips, open source, run via npx and pnpm), Figma API / personal access tokens, Cursor (MCP client), pnpm, npx, git, HTML/CSS (generation target)

## [Sonnet 4.5 Just Unlocked a New Breed of Agents](../videos/t7VuWwukO3I.md)
`t7VuWwukO3I` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: claude-code, coding-agents, agent-architecture

AI LABS walkthrough of running Claude Code as a scheduled GitHub Actions agent (model-news monitor to Slack) and as an issue-triggered background coder, with two rules learned from failed runs: auto-approve tools and test MCP servers first.

- Techniques: Install the Claude Code GitHub app into a repo; Scheduled news monitor on GitHub Actions; Whitelist all tools for headless runs (Rule 1); Verify MCP servers before automation (Rule 2); Post to Slack via incoming webhook with curl; Hand off a background coding task via a GitHub issue; Paste SDK documentation into the task; Verify auth end to end on a branch
- Tools: Claude Code (version 2 announced with Sonnet 4.5), Claude Sonnet 4.5, Claude Code GitHub app, GitHub Actions, GitHub, Slack (incoming webhook via curl), Supabase (auth), Supabase MCP server, Claude Agent SDK (TypeScript and Python docs), BMAD method (referenced), OpenAI Codex (referenced as inspiration for cloud agents), Cursor (referenced for code rewind), GPT-5 (mentioned in the opening)

## [The Only Guide You Need to Build MCP Server.](../videos/kfTDFkhNDFU.md)
`kfTDFkhNDFU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering

Walkthrough of building a minimal Python MCP server with the official SDK, wiring it into Cursor, and using docs and AI generation to wrap a web crawler and a Figma API.

- Techniques: Minimal Python MCP server; Register a local MCP server in Cursor; Feed SDK docs to the coding agent; gitingest to turn a repo into LLM context; Wrap an existing script as an MCP tool; API-to-tool generation from endpoint docs
- Tools: MCP Python SDK (mcp, installed with pip; no version stated), Cursor (agent, Composer, docs feature, MCP settings), Crawl4AI (open-source web crawler and data extractor), Figma REST API (get file endpoint), gitingest (gitingest.com, GitHub URL swap), GitHub (SDK repo, README)

## [Build A RAG AI System in 5 Minutes with Cloudflare + Firecrawl!](../videos/YxC1zEz5TDY.md)
`YxC1zEz5TDY` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: rag-retrieval

Four-minute tutorial wiring Firecrawl-scraped docs into R2, indexing them with Cloudflare AutoRAG, and exposing the index to Cursor through Cloudflare's MCP server.

- Techniques: Crawl a docs site to Markdown with page metadata; Use R2 as the S3-compatible document store for RAG; Index an R2 bucket with AutoRAG using the auto models; Expose an AutoRAG index to Cursor as a global MCP server
- Tools: Firecrawl (Node package, crawl-URL method, Markdown export), Cloudflare R2 (S3-compatible object storage), Bun S3 client, Cloudflare AutoRAG (beta), Cloudflare vector database (used by AutoRAG; not named in the video), Cloudflare Workers, Cloudflare MCP servers (AutoRAG server, one of about 30 released recently), Cursor, Claude (comparison point only), Tailwind CSS (only referenced as an example doc set and a separate video)

## [How Claude Solved AI's Biggest Problem](../videos/Z9glbip8pZc.md)
`Z9glbip8pZc` · AI LABS · 2025-11-02 · q3 · intro · review · also: claude-code, skills-self-improvement, context-engineering

Walkthrough of Claude Skills: SKILL.md folders loaded on demand, how they differ from MCP, building one with skill-creator, and HTML visualization widgets. Mostly demo, with one sponsor segment.

- Techniques: Skill folder layout; Keep the description one line; push detail into referenced files; Install shared skills into Claude Code; Bootstrap a skill with skill-creator; Visualization widget skill
- Tools: Claude Skills, Claude Desktop app, Claude Code, skill-creator skill (Anthropic skills repo), MCP builder skill, MCP, Figma MCP server, Figma API, PDF Extractor skill, Algorithm art skill, Canvas design skill, Word, PDF, Excel and PowerPoint document skills

## [I Made MCP AI Agents That Automate Every App I Build.](../videos/23ykmgvaSmM.md)
`23ykmgvaSmM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, vibe-coding-app-building

Tutorial on wrapping an existing FastAPI to-do app with the FastAPI MCP server so Cursor, Windsurf, Claude Desktop, or a Python MCP-client agent can call its endpoints as tools. Covers setup, tool naming, and a registration gotcha.

- Techniques: Expose a FastAPI app as MCP tools; Name MCP tools with operation IDs; Register MCP after all endpoints are declared; Add the MCP server to an IDE client; Drive the MCP server from a custom Python agent
- Tools: FastAPI, fastapi-mcp (FastAPI MCP package), Next.js, Cursor, Windsurf, Claude Desktop, pip, uv, MCP use framework (Python MCP client library, name as spoken), mcp.json, config.json

## [Firecrawl MCP = Effortless Web Scraping](../videos/2GHRDoFquOo.md)
`2GHRDoFquOo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, coding-agents

Tutorial on wiring the Firecrawl MCP server into Cursor so an agent can scrape a live URL and generate a near-copy of a Notion landing page in Next.js. Shows setup and a single demo run, with the output's flaws called out.

- Techniques: Register Firecrawl MCP in Cursor; Name the MCP tool in the prompt and use agent mode; Scrape, then generate by component; Pick scrape vs extract by goal
- Tools: Firecrawl MCP server (scrape and extract tools, npx command, API key), Cursor (agent mode, MCP settings), Windsurf (same MCP config pattern, mentioned as an alternative), Claude 3.7 Sonnet (model selected in Cursor), Next.js (blank starter app used as the target), Notion landing page (the site being cloned)

## [3 More Ways To ACTUALLY Build Beautiful Websites with Cursor IDE](../videos/U1_nzjWUpL4.md)
`U1_nzjWUpL4` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: vibe-coding-app-building, coding-agents, context-engineering

Three practical ways to turn website designs into working Next.js UI in Cursor: a structured front-end spec prompt, a design.json built from screenshots, Browser MCP for cloning structure, and stagewise for precise element-level edits.

- Techniques: Structured front-end spec prompt; Screenshot to design.json style profile; Clone a site's structure with Browser MCP; Element-level UI edits with stagewise
- Tools: Cursor, Claude, ChatGPT, Claude Code, Next.js, Tailwind CSS, Browser MCP, stagewise, mcp.json, design.json

## [Connect any LLM to any MCP server without any MCP client.](../videos/QZ6AreMxMKA.md)
`QZ6AreMxMKA` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: agent-architecture, coding-agents

A beginner walkthrough of a Python MCP client library that runs an agent over any LLM and any MCP server, so no desktop client is needed. Shows setup, a single-file Airbnb example, multi-server config and Cursor tips.

- Techniques: Provider-agnostic MCP agent from a config file; Cap agent steps and filter results in the prompt; Multi-server config with a service manager; Give a coding assistant the library docs; Flatten a repo for LLM questions (gitingest)
- Tools: MCP (Model Context Protocol), Python, pip3, LangChain, LangChain OpenAI integration, LangChain Anthropic integration, OpenAI, Anthropic, Cursor, Windsurf, Claude Desktop, Airbnb MCP server

## [The GPT-5 Backlash, AI CLI Tools & AI Agent Protocols | Better Stack Podcast Ep 1](../videos/no8ijoB4qxM.md)
`no8ijoB4qxM` · Better Stack · 2025-11-02 · q2 · intro · other · also: coding-agents, claude-code, evals

Better Stack podcast on GPT-5's messy rollout, Claude Code's lead among CLI coding tools, benchmark contamination, and why MCP won while rival agent protocols stalled. Opinion-heavy, little hard data.

- Techniques: Benchmark contamination check; Plan with the strong model, execute with the cheaper one; Turn an existing REST API into an MCP server; Convert web pages to Markdown before sending them to the model; Pair a strong general model with a browser MCP server; Custom Claude Code status line
- Tools: GPT-5, GPT-5 medium, GPT-5 high, OpenAI Codex (Codex CLI), Claude Code, Claude Sonnet, Claude Opus (4.1), Cursor, GitHub Copilot, VS Code, Goose, OpenCode (SST)

## [Claude Code Is an MCP Now?...3 CRAZY Things You Never Saw Coming](../videos/diTuQaSJ3nI.md)
`diTuQaSJ3nI` · AI LABS · 2025-11-02 · q3 · practitioner · review · also: claude-code, multi-agent, token-cost-efficiency

Community tools that extend Claude Code: calling it as an MCP server from Cursor, routing it to other models (Kimi K2 via OpenRouter), a multi-agent "hive mind" mode, and a dedicated Claude Code Chat extension.

- Techniques: Expose Claude Code as an MCP server and call it from another client; Canvas-to-code handoff from Claude Desktop; Route Claude Code to OpenRouter models with Claude Code Router; Hive mind multi-agent sessions in Claude Flow; Dedicated Claude Code Chat window in the editor
- Tools: Claude Code, Claude Code SDK, Claude Code MCP server (community wrapper, unnamed in video), Claude Code Router (ccr), Cursor, Claude Desktop, Claude 3, OpenRouter, Kimi K2, Gemini, OpenAI models, DeepSeek

## [3 Things I Wish I Knew Before using Claude Code](../videos/_9T-6dw-CZs.md)
`_9T-6dw-CZs` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, coding-agents, context-engineering

A beginner-level walkthrough of five Claude Code features: custom slash commands, Cursor integration with multi-line input, adding MCP servers (Sentry example), plan mode with CLAUDE.md, and the "ultrathink" keyword.

- Techniques: Custom slash command as a prompt file; Claude Code inside Cursor; Add an MCP server from an existing Cursor or Windsurf JSON config; Use MCP server commands from slash commands; Plan first, then save rules to CLAUDE.md; Add 'ultrathink' to a prompt for hard problems
- Tools: Claude Code, Cursor, Windsurf, Sentry, Sentry MCP server, Seer (Sentry AI agent), Claude Agent SDK, Claude GitHub app

## [This New MCP Client Lets You Integrate So Many MCP Servers!!](../videos/xEyKT5iY0W0.md)
`xEyKT5iY0W0` · AI LABS · 2025-11-02 · q2 · intro · review · also: security-guardrails

Walkthrough of an open-source general-purpose MCP client that runs an agent over MCP servers outside coding IDEs, using Composio-hosted servers with agent-driven auth; the local install is slow.

- Techniques: Adding a remote MCP server to a generic client; Agent-driven auth for hosted MCP servers; Running the open client locally
- Tools: Open MCP client (open-source MCP client app, hosted on Vercel, source on GitHub), Composio (composio.dev, hosted MCP server catalog with auth), Google Tasks MCP server, Hacker News MCP server, Gmail MCP server, Google Drive MCP server, Notion MCP server, Google Meet MCP server, Cursor, Windsurf, LangSmith, OpenAI models

## [Replits NEW AI Agents Are INSANE](../videos/v1jLYiW0AWc.md)
`v1jLYiW0AWc` · AI LABS · 2025-11-02 · q3 · intro · review · also: product-ux, vibe-coding-app-building

Hands-on beta test of Replit Agent 3's Agents and Automations builder: guided setup via Slack, Telegram or scheduled triggers, OAuth connectors, and automatic app testing, with real gaps in memory, integrations and Slack deployment.

- Techniques: Least-privilege Notion OAuth; Test memory after deployment; Ask the agent to explain a missing action; Telegram publishing setup; Verify side effects end to end
- Tools: Replit Agent 3, Replit Agents and Automations, Replit app testing, Replit Stripe integration, OpenAI API, Notion (connector), Outlook (connector), OneDrive (connector), Spotify (connector), Linear (connector), Slack (connector and deployment target), Telegram (deployment target)

## [I Found a Tool That Breaks MCP (In a Good Way)](../videos/6R7CoIKKkDE.md)
`6R7CoIKKkDE` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

Tempo Labs' MCP app store packages third-party APIs as MCP servers with docs built in; the host builds an ElevenLabs quotes app by installing integrations and prompting. Promotional, single happy-path demo.

- Techniques: Connect the backend before the integrations; Install an integration from the MCP app store; PRD and user flow as the build spec; Describe the full behavior in one feature prompt; Add error logging before debugging a broken integration
- Tools: Tempo (Tempo Labs app builder, with its MCP app store), Model Context Protocol (MCP), Supabase, Firecrawl, ElevenLabs (Eleven Labs API), Google Gemini, OpenAI, Anthropic (auto-caption reads 'Tropic'), Next.js (starter template kit), shadcn/ui (auto-caption reads 'Shadzian'), Mermaid, React

## [Vibe Coding Debugging: The Only Tutorial You Need for 10X Fast Debugging](../videos/2h8WSChA1-o.md)
`2h8WSChA1-o` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: observability, coding-agents

A Sentry MCP walkthrough: an agent in Cursor creates a Sentry project, installs the Next.js SDK, wires the DSN, triggers test errors, then reads an issue's trace and proposes a fix. Vendor-led, with a paid SEER feature.

- Techniques: Let the agent provision Sentry through the MCP; Install the Sentry MCP into a client; Debug an error from its issue data, not the raw code; Set a verification step after the agent wires monitoring
- Tools: Sentry, Sentry MCP server, Sentry SDK, Next.js, Python SDK, Cursor, Claude Code, SEER, mcp.json

## [Claude Engineer is INSANE... Upgrade Your Claude Code Workflow](../videos/6Rg5M69bMgQ.md)
`6Rg5M69bMgQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, context-engineering, coding-agents

A walkthrough of two free add-ons for Claude Code: the SuperClaude configuration framework (slash commands, flags, personas, MCP-wired workflows) and a basic browser web UI for reaching Claude Code from other devices on the LAN.

- Techniques: Install SuperClaude from its GitHub repo; Have an AI write a usage guide from the framework's own config; Turn a phase into a runnable slash command plus prompt; Wire MCPs yourself, then reference them through flags; Reach Claude Code from a phone on the same LAN
- Tools: SuperClaude (configuration framework for Claude Code; no version stated), Claude Code, Cursor (used to read config and generate docs.md), Context7 MCP, Sequential MCP, Magic UI MCP, Puppeteer MCP, React, Next.js (spoken as 'xjs'), ElevenLabs API, OpenAI API, Warp (terminal, used to get the LAN IP)

## [Wait.. Claude Code is MADE Slow on Purpose? Heres How to Fix It](../videos/wYWyJNs1HVk.md)
`wYWyJNs1HVk` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, context-engineering, token-cost-efficiency

Walkthrough of installing the Serena MCP (semantic code retrieval over a project index) and a Claude Code usage monitor, to keep Claude's context window focused and token use lower; the title's "made slow on purpose" claim is not supported in the video.

- Techniques: Per-project Serena MCP install; Index the project before using Serena; Prime Claude with Serena's instructions; Use the Serena dashboard for logs and clean shutdown; Track plan-window usage in a terminal tab
- Tools: Serena (MCP server for semantic code retrieval and indexing), Context7 (MCP for up-to-date library documentation), Claude Code, Cursor, Windsurf, uv (Python package runner used to install Serena), Claude Code usage monitor (terminal tool; name not stated in the transcript), Next.js, Python, Claudia and the Claude Code web UI (mentioned as alternatives)

## [Context7 MCP Tutorial: Get Instant RAG for Your AI Coders](../videos/323l56VqJQw.md)
`323l56VqJQw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering

Tutorial on wiring the Context7 MCP server into Cursor so the agent pulls current, targeted library docs instead of stale training data or whole doc files; the evidence is one informal before/after build.

- Techniques: Add Context7 as an MCP server in Cursor; Recover missing MCP tools; Pull targeted doc sections instead of attaching whole docs; Keep API keys out of agent context
- Tools: Cursor, Context7 MCP server (context7.com), mcp-use (auto-caption 'mcpus'; the Python agent framework built in the demo), Playwright MCP, Claude 3.7 (model named by the speaker), shadcn/ui (example library), Next.js (example framework), Windsurf, VS Code with GitHub Copilot agent, .cursorignore

## [Supabase MCP Cursor Integration (Step by Step)](../videos/b_hr1TB2GYQ.md)
`b_hr1TB2GYQ` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, context-engineering

Step-by-step setup of Supabase's MCP server in Cursor so the agent can see the live database schema, with a connection-string walkthrough and a bash-wrapper trick. Anecdotal, short, and light on verification data.

- Techniques: Add Supabase MCP to Cursor via the command type; Wrap the MCP command in a bash script; Make the agent verify schema before and after each DB step
- Tools: Supabase, Supabase MCP server, Supabase CLI (`supabase status`, local instances), Cursor, Windsurf, Claude Desktop, GitHub MCP server, bash

## [Integrate Cursor/Windsurf into Apple Ecosystem with This Cursor MCP Setup!](../videos/htbzu9s189E.md)
`htbzu9s189E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents

Walkthrough of connecting the open-source apple-mcp server to Cursor so an agent can read and act on Apple Contacts, Notes, Messages and Reminders; mostly setup steps, with a useful note on restructuring a tool's navigation.

- Techniques: Register a local MCP server in Cursor; Get the absolute entry path for an MCP server; Use agent mode to call MCP tools; Extend an MCP server by having the agent copy existing modules; Restructure a search-everything tool into hierarchical navigation
- Tools: Cursor, apple-mcp (GitHub repo, MCP server for Apple apps), Claude Desktop, Windsurf, Docker MCP server (already added in Cursor, unrelated to the Apple setup), Claude 3.5 Sonnet, GPT-4, bun, realpath, Apple Notes, Apple Contacts, Apple Messages

## [MCP Servers are Security Nightmares...](../videos/CRKYNyMc4PM.md)
`CRKYNyMc4PM` · Better Stack · 2025-11-02 · q3 · practitioner · demo · also: security-guardrails, coding-agents

Demo of MCP tool poisoning, tool shadowing, rug-pull mutation and command injection in MCP servers. Main takeaway: treat tool descriptions and server code as untrusted input.

- Techniques: Pin and diff tool definitions; Review full tool descriptions and arguments before approval; Treat tool descriptions as untrusted input; Avoid shell interpolation in MCP tool handlers; Probe your own MCP servers directly; Limit what a server can reach
- Tools: Cursor, MCP (Model Context Protocol), WhatsApp MCP server (community project, named as legitimate), MCP client libraries (used to call server tools directly)

## [This n8n mcp is INSANE... Let AI Create your Entire Automation](../videos/xf2i6Acs1mI.md)
`xf2i6Acs1mI` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

A walkthrough of an n8n MCP server that lets Claude or Cursor research n8n nodes, build a workflow JSON, validate it and push it into an n8n workspace, shown with a deep-search agent demo and setup steps.

- Techniques: Register the n8n MCP in Claude Desktop; Register the n8n MCP in Cursor; Enforce tool-call order with a rulebook; Full management mode: API key and URL; Deep-search agent pattern in n8n
- Tools: n8n, n8n MCP server, Claude (Desktop, Projects, Artifacts), Claude Code, Cursor, Docker, npx, OpenAI API, SERP API, DuckDuckGo search node, Wikipedia search node, Reddit search node

## [Warp Code Tutorial: Save 90% of Time with Warp AI Agents (vs Claude Code) Agentic Development](../videos/STd07QswCpk.md)
`STd07QswCpk` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering, multi-agent

Sponsored walkthrough of building a full-stack notes app with Warp's agentic development environment, covering PRD planning, parallel agents split by API contract, saved prompts and rules, and MCP context.

- Techniques: PRD-first, then API contract, then fan out; Saved prompts as reusable commands; Templated workflows for known-hard setup steps; Rules to pin dependency and library behavior; Notebooks as context documents; Explicit task list for long runs; Parallel agent tabs with completion monitoring
- Tools: Warp (agentic development environment and terminal, with a built-in AI agent), Warp Drive (saved prompts, rules, MCP servers, workflows, notebooks), Context7 MCP, Playwright MCP, ChatGPT, Express Validator, Zod, Next.js, SWE-bench (vendor claim: 75.8%), Terminal Bench (vendor claim: #1)

## [Connect to Anything with This Cursor MCP Setup](../videos/brhs5DogIf8.md)
`brhs5DogIf8` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents

Walkthrough of adding community MCP servers to Cursor as stdio commands (Docker, YouTube summarizer), with a YOLO-mode caveat; mostly screen-recorded clicks, thin on specifics.

- Techniques: Add a stdio MCP server in Cursor; Verify tool access with a small agent-mode task; Use YOLO mode only with monitoring; Summarize a YouTube video through MCP
- Tools: Cursor, Model Context Protocol (MCP), Claude Desktop app, Claude, Composer (Cursor agent), uvx, Docker MCP server, Jira MCP server, Spotify MCP server, Shopify MCP server, YouTube MCP server, yt-dlp

## [NEW OpenAI AI Agents SDK – Multi-Agent AI Made Simple](../videos/ZvvQKie3X70.md)
`ZvvQKie3X70` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: agent-architecture, multi-agent, observability

Better Stack walkthrough of OpenAI's new Python Agents SDK: agents, handoffs via a router agent, function and built-in tools, local context, input guardrails, and built-in tracing.

- Techniques: Router/triage agent with handoff descriptions; Function tool from a Python function; Typed local context object; Guardrail as a classifier agent; Inspecting run steps with new_items
- Tools: OpenAI Agents SDK (Python), OpenAI web search tool, Pydantic, OpenAI platform traces

## [Claude code vs Codex vs Cursor: Who gets the cake?](../videos/_Xbe7MQ2NxI.md)
`_Xbe7MQ2NxI` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, coding-agents, agent-architecture

Argues Claude Code and other AI CLIs are "portable agent engines": terminal agents can call each other via bash, run headless (-p), deploy to GitHub Actions and act as MCP servers. Opinion-heavy, with a sponsor segment.

- Techniques: Headless single-shot invocation; Cross-agent delegation through bash; Scheduled agent via GitHub Actions; Claude Code GitHub app for PR review; Mixed local and remote MCP servers
- Tools: Claude Code, Claude Code GitHub app, Claude Code for Chrome, Claude for Excel, Agent SDK (formerly Claude Code SDK), Codex CLI, Gemini CLI, Qwen Code (transcript: QuenCode), Cursor CLI, gitingest, GitHub Actions, Slack

## [This MCP Setup is the Best Way to Add 3D Models to Your Frontend](../videos/srsst0L51RE.md)
`srsst0L51RE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, vibe-coding-app-building

Short tutorial on connecting the Sketchfab MCP server to Cursor so an agent can search, download and place a 3D model into a Three.js landing page from one prompt.

- Techniques: Install the Sketchfab MCP server from source; Get a Sketchfab API token; Get the absolute path to the built server entry point; Register the server in Cursor via mcp.json; Prompt for a 3D hero section and iterate on the model
- Tools: Sketchfab MCP server (community server listed on mcp.so), Sketchfab, Cursor, Windsurf, Claude Desktop, Three.js (3JS), git, npm, Claude 3.7 (mentioned for 3D game generation)

## [Develop Faster using the browser tools MCP Cursor/Windsurf.](../videos/G25UyWfYogQ.md)
`G25UyWfYogQ` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, testing-verification

Walkthrough of the browser-tools MCP server, which lets Cursor's agent run accessibility/SEO/performance audits, read screenshots and selected DOM elements from Chrome, and iterate on front-end fixes.

- Techniques: Install browser-tools MCP into Cursor; Load the Chrome extension and start the connector; Accessibility audit and fix loop; Configure screenshot folder and auto-paste; Select-element targeting; Voice mode for prompting
- Tools: browser-tools MCP server (browser-tools-mcp, GitHub repo linked in the description), Cursor (IDE and agent), Windsurf (mentioned for its select-element feature), Chrome browser extension (browser-tools), Chrome DevTools (Browser Tools MCP tab for settings and screenshot folder), mcp.json (Cursor MCP config file), React (demo app's calendar component)

## [GitHub MCP Server: Let AI Handle Your GitHub](../videos/TrDW2Puhw0Y.md)
`TrDW2Puhw0Y` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, dev-tools

Step-by-step setup of the GitHub MCP server in Cursor, then a live demo of an agent creating a repo, pushing a file, cloning and searching GitHub from the chat.

- Techniques: Wrap the GitHub token in a shell script for Cursor's MCP command; Create a GitHub classic personal access token for the MCP server; Register the script as a command-type MCP server in Cursor; Smoke-test the MCP connection with a read-only query
- Tools: GitHub MCP server (GitHub's official MCP server, run through npx), Cursor (IDE, agent mode, MCP settings), npx, bash, nano, realpath, GitHub classic personal access tokens, Claude Desktop (mentioned as the server's reference client), Archon (another creator's agent-building repo, mentioned in passing)

## [Better Stack MCP Server | Changelog #12](../videos/JkpEd2xUwxk.md)
`JkpEd2xUwxk` · Better Stack · 2025-11-02 · q2 · intro · review · also: observability

Better Stack's changelog demo of its MCP server, letting Claude Desktop manage incidents, on-call, status pages and query ClickHouse telemetry, plus the setup steps and credential scoping.

- Techniques: Incident triage loop via MCP prompts; Schema-first text-to-query over logs; Remote MCP setup for Claude Desktop; Separate the uptime token from telemetry scope
- Tools: Better Stack MCP server, Better Stack uptime (monitors, heartbeats, status pages, incidents, escalation policies), Better Stack telemetry (logs, spans, metrics), ClickHouse (HTTP client connection), Claude Desktop, remote MCP config (mcp-remote style client)

## [I Built 5 Websites Without Touching HTML:  Here's How (Kibo UI)](../videos/6odlDS7-G8k.md)
`6odlDS7-G8k` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, coding-agents, context-engineering

Tutorial on wiring the shadcn MCP server and a custom 1100-component Kibo UI registry into a coding agent, plus TweakCN's live-embed theming flow for building Next.js UIs.

- Techniques: Wire the shadcn MCP into a Next.js or React project; Host a custom component registry from shadcn's registry template; Category-guided component selection for very large catalogs; Two-command design-first workflow (init once, build per session); Embed a TweakCN live theme preview into a Next.js app
- Tools: shadcn, shadcn CLI, shadcn MCP server, shadcn registry template, Kibo UI (patterns registry, ~1100 components), TweakCN, TweakCN MCP server, Next.js, React, Claude Code, Cursor, components.json

## [SAVE Your 20$ by using Cursor AI for FREE!](../videos/Nm2Lhe0-6To.md)
`Nm2Lhe0-6To` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, token-cost-efficiency

Walkthrough of Desktop Commander, a free MCP server that gives Claude Desktop file, terminal and edit tools, demoed by building a Next.js and FastAPI image editor from one prompt.

- Techniques: Replace an AI IDE with an MCP server in an existing chat client; One prompt with a target path and an objective; Search-and-replace edits instead of full-file rewrites; Read and change the MCP server's config through its own tools; Run-and-verify loop with bug reports in chat; Side-by-side IDE view with agent edits
- Tools: Desktop Commander MCP, Claude Desktop, File system MCP server, Claude Code, Cursor, Windsurf, VS Code, Cline (transcribed as 'Klein'), Roo Code (transcribed as 'RuCode'), Claude 3.7 Sonnet, Claude 3.5 Sonnet, Next.js

## [All My AI Apps Are Connected to One MIND — With Open Memory](../videos/Y2XI2nk44WE.md)
`Y2XI2nk44WE` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: memory

Tutorial on Open Memory, a self-hosted shared memory server that several MCP clients (Claude Desktop, Cursor) can read and write, with setup steps and the failure modes the host hit.

- Techniques: Run Open Memory locally; Install the MCP server via generated client commands; Ingest a whole plan as one memory add; End-of-session progress checkpoint; Scope retrieval with specific project wording; Store plain-text memories, not structure
- Tools: Open Memory (Mem0 repo), Mem0, Claude Desktop, Claude, Cursor, Docker, make, OpenAI API, MCP, Next.js, React, TypeScript

## [I've Been Using the n8n MCP WRONG - The Correct Workflow](../videos/jUfpYmN9q6Y.md)
`jUfpYmN9q6Y` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: coding-agents, claude-code, context-engineering

Driving the n8n MCP from Claude Code works better with a phased, file-based workflow: plan, research, build and validate in separate sessions, delete-and-recreate on update, and OAuth instead of API keys.

- Techniques: Phased file-based workflow pipeline; Clear context between phases; Put standing rules in CLAUDE.md; Pre-build version and health check; Delete-and-recreate instead of in-place update; OAuth-first credentials; Single-node isolation debugging; Documentation re-check prompt
- Tools: n8n, n8n MCP server, Claude Code, Claude Desktop, Claude.md (CLAUDE.md), OpenAI node in n8n, Google Calendar node, Gmail, Google Cloud Platform, Brave Search (from the previous video), Gamma (sponsor segment)

## [How to Use Figma AI To Make Sites 10X More Beautiful](../videos/_-FEgdQ_L4I.md)
`_-FEgdQ_L4I` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, context-engineering

A walkthrough of a prompt-chained Figma Make workflow for planning and generating a React app, then converting it with a coding agent and feeding Figma designs to agents through the Dev Mode MCP server.

- Techniques: Plan-first prompt chain for Figma Make; Universal full-stack conversion prompt; Figma Dev Mode MCP setup; Implementation-rules configuration file; Screen triage before implementation; Add shadcn MCP for component context
- Tools: Figma Make, Figma desktop app (Dev Mode), Figma Dev Mode MCP server (local and remote variants), ChatGPT (web interface, for planning and prompt outputs), Warp (Warp Code agent, referred to as Warpcode in captions), Supabase, React, Next.js, GitHub, shadcn MCP server, shadcn/ui, Aceternity UI

## [These Hidden Cursor Features Will Make You 10x More Productive](../videos/A9BiNPf34Z4.md)
`A9BiNPf34Z4` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, context-engineering

A feature tour of Cursor's hidden productivity tools: global and project rules, notepads, indexed docs, MCP servers (Docker example), and YOLO mode for auto-running tools.

- Techniques: Global behaviour rules; Scoped project rules as .mdc files; Borrowing rule sets; Notepads as prompt templates; Web and indexed-doc references in Composer; Adding an MCP server in Cursor; YOLO mode with allow and deny lists
- Tools: Cursor, Cursor Rules (.cursor/rules, .mdc files), cursor.directory, Supabase (Postgres rule examples on GitHub), Tailwind CSS v4, Next.js, Better Stack docs, Model Context Protocol (MCP), Claude desktop app, docker-mcp (Docker MCP server, run with uvx), uv / uvx, npx

## [Automation Testing Tutorial Using Cursor AI + Operative.sh & Claude 4 (Setup + Demo)](../videos/GuKdinu64Z0.md)
`GuKdinu64Z0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: testing-verification, coding-agents

Walkthrough of installing operative.sh's web-eval MCP agent into Cursor and using plain-English test cases, including edge cases, to drive a Playwright browser against a local login page. Vendor-specific, thin on evidence.

- Techniques: Install operative.sh web-eval MCP into Cursor; Call the web eval agent with url, task and headless; Save an authenticated session once with setup-browser-state; Generate test cases to a file, then run them sequentially and write results back
- Tools: operative.sh (web eval agent, setup-browser-state tool, MCP installer, API key), Cursor (IDE, MCP host), Playwright (browser automation, installed by the setup), Claude 4 (Anthropic model; the presenter says it was released 2-3 days before recording and praises it), Aceternity UI (the demo site's UI library; auto-caption reads it as 'as eternity ui'), MCP (Model Context Protocol, the integration path)

## [Codex CLI Has Just Got WAY Better!](../videos/Szi4SHB4nNs.md)
`Szi4SHB4nNs` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, sandboxing-execution, claude-code

Better Stack tours the late-2025 Codex CLI update (Rust rewrite, ChatGPT login, sandbox and approval modes, config profiles) and candidly compares it with Claude Code.

- Techniques: Separate sandbox from approval when setting agent autonomy; Named config profiles in config.toml run with -p; Audit an agent run via the transcript view; Tune model and reasoning effort per task; Point Codex at an OpenAI-compatible endpoint for non-OpenAI models; Notify script for event alerts; Everyday workflow commands
- Tools: Codex CLI (OpenAI terminal coding agent), GPT-5, GPT-OSS, DeepSeek (tested, errored), AGENTS.md, config.toml, Ink (previous TypeScript UI), Ratatui (Rust TUI library), ChatGPT login, Codex VS Code plugin, Claude Code (comparison), Better Stack MCP (host plug)

## [Postman MCP Server Tutorial: Build & Run AI Agents with APIs (Postman MCP Generator + Cursor)](../videos/QDz4htGbOC4.md)
`QDz4htGbOC4` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents

Tutorial on Postman's MCP generator: turn selected API requests into a locally run MCP server, then register it in Cursor and call it from the chat. Thin on depth, but the steps are reproducible.

- Techniques: Generate a local MCP server from API docs in Postman; Put secrets in the generated .env file; Register a local MCP server in Cursor; Test an MCP server through Postman; Build an agent from an MCP server in code with mcp-use
- Tools: Postman MCP generator, Postman, Model Context Protocol (MCP), FastAPI MCP library, mcp-use, Cursor, Claude Desktop, Windsurf, Node.js, npm, OpenWeatherMap API

## [Time to UPGRADE… Unified AI Agents Are Finally Here](../videos/VDql5GzoSoc.md)
`VDql5GzoSoc` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, rag-retrieval

Walkthrough of ACI.dev, a hosted platform that connects apps to agents via an app store, an agent playground and a unified MCP server with search and execute tools; the hype title outruns the unbenchmarked speed claims.

- Techniques: Attach apps to an agent in ACI's playground; Unified MCP server in Cursor; Separate agents with separate tool sets
- Tools: ACI.dev, ACI unified MCP server, ACI app MCP server, Agent Playground (ACI), Google Calendar, YouTube, Google Maps, Gmail, Brave Search, Archive (app named in video), Cursor, Claude Desktop

## [Claude Code SDK: Build Real AI Apps with Python & MCP](../videos/h1AGjM9IeBM.md)
`h1AGjM9IeBM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, coding-agents, pr-code-review

A short walkthrough of the Claude Code SDK (Python, with the docs' example script and a GitHub Actions demo) that frames Claude Code as a programmable subprocess. The example broke for the speaker, and the video shows no working SDK run beyond that.

- Techniques: Run Claude Code as a subprocess from Python; Cap agent iterations with max_turns; Attach external MCP servers to programmatic Claude Code; Mention-triggered issue-to-PR workflow in GitHub Actions
- Tools: Claude Code, Claude Code SDK (Python, TypeScript, CLI), ClaudeCodeOptions, query(), Cursor, GitHub Actions, Claude Code GitHub Actions workflow, Jira MCP server, Slack MCP server, pip

## [ShadCN Dropped Something to FINALLY Fix Your UI](../videos/mSMflOx5pq8.md)
`mSMflOx5pq8` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, multi-agent, context-engineering

Tutorial on shadcn's official registry MCP: add extra community component registries, then run a multi-subagent workflow (requirements, component research, implementation) to build UIs without unnecessary components.

- Techniques: Install the shadcn registry MCP; Add third-party component registries; Preview a registry's visual style before using it; Three-stage subagent workflow for UI builds; Express agent for small changes; Port the commands to Cursor; Apply a TweakCN theme
- Tools: shadcn (CLI and registry MCP server), Claude Code, Cursor, VS Code, Next.js, React, npm, components.json, mcp.json, Aceternity UI, Origin UI, Neo Brutalism (registry, failed)

## [Stack Overflow for your LLMs (and you!)](../videos/IYyyiA5eWEo.md)
`IYyyiA5eWEo` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, rag-retrieval

A short Better Stack tool walkthrough of grep.app, a fast regex code search over GitHub, and its MCP server, which lets Claude Code or Cursor pull real library usage into context instead of hallucinating APIs.

- Techniques: Add grep.app as an MCP server in Cursor or Claude Code; Literal and regex code search with filters; Version-specific search for new packages; Regex to detect committed secrets (defensive use)
- Tools: grep.app, GitHub, Claude Code, Cursor, MCP, Lexical, Next.js, React Router, Payload CMS

## [Agents Can FINALLY See the Frontend (Chrome DevTools MCP)](../videos/zaXKZjJvaAs.md)
`zaXKZjJvaAs` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, testing-verification

Walkthrough of Chrome's DevTools MCP server, which lets a coding agent open, inspect, audit, and automate pages in a real Chrome instance. Mostly a prompt-driven demo with little setup detail.

- Techniques: Attach Chrome DevTools MCP to a coding agent; Prompt for a performance audit targeting LCP; Repeat the audit under network throttling; End-to-end flow and API check through the browser; Debug console errors and failed network requests
- Tools: Chrome DevTools MCP (Chrome's MCP server for coding agents), GitHub Copilot (agent used in the demo), Recommendoo (demo app built by the host with vibe-coding), OpenAI API (used by the demo app for suggestions), Watch Mode API (used by the demo app for title data)

## [Cursor 1.0 is their BEST update yet... (Agents, BugBot, Memories and more)](../videos/Ig-cfiqWJCs.md)
`Ig-cfiqWJCs` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, pr-code-review, sandboxing-execution

Feature tour of Cursor 1.0 covering BugBot PR review, remote background agents, per-project memories and one-click MCP install with OAuth, plus the security caveats of background agents.

- Techniques: BugBot on GitHub PRs with trigger control; Launching a background agent from a prompt; Background agent environment via snapshot or environment.json; Saving persistent project rules as memories; One-click MCP install with OAuth
- Tools: Cursor 1.0, Cursor BugBot, Cursor Agent, Cursor background agents, Cursor memories, Cursor dashboards, GitHub, GitHub Copilot, Claude Code (transcribed as 'clawed code'), Notion MCP server, Bun / bunx, Create React App (npx)

## [Google won't STOP... They Just Upped the Gemini CLI Again](../videos/A3AOeX1s7yw.md)
`A3AOeX1s7yw` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: coding-agents, context-engineering

A walkthrough of Gemini CLI's recent updates: free-tier quotas, MCP setup via settings.json, slash commands, VS Code inline diffs, and "extensions" as shareable bundles of context, MCP servers and commands.

- Techniques: Custom slash commands as TOML files for page and component generation; Adding MCP servers by editing settings.json; YOLO mode toggle for uninterrupted runs; Reviewing agent edits in VS Code via the IDE companion; Built-in session helpers; Packaging a team extension
- Tools: Gemini CLI, Gemini 2.5 Pro, ShadCN MCP (shadcn), Gemini CLI companion extension (VS Code), VS Code, Claude Code (compared, not demoed), Cursor (compared, not demoed), ChatGPT (used to draft the to-do app), TweakCN (theme source), Qwen (named as a competing free agent, no version), Skywork Super Agents (sponsor, not demoed)

## [Qwen 3 ACTUALLY Made Me Quit Claude Code](../videos/lXWazKnuZNQ.md)
`lXWazKnuZNQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, token-cost-efficiency

Walkthrough of using Qwen Code's free OAuth tier and Claude Code Router to run cheap Qwen3 Coder backends, with a single anecdotal DaisyUI build comparing it to Claude Code.

- Techniques: Qwen Code OAuth sign-in for free runs; Routing Claude Code through Claude Code Router; Context7 MCP for libraries models do not know well; Give the agent a PRD before building
- Tools: Qwen Code, Qwen3 Coder, Claude Code, Claude Code Router (ccr), Gemini CLI, Context7 MCP, DaisyUI, OpenRouter, ModelScope, Claude Sonnet 4, Cursor, CLAUDE.md

## [MCP-UI could be the future - Here's Why](../videos/aziRV2DAWew.md)
`aziRV2DAWew` · Better Stack · 2025-11-02 · q3 · intro · review · also: product-ux

Better Stack demos MCP-UI, an add-on that lets MCP tools return sandboxed UI components (mainly iframes) instead of text, and argues it could shape how chat apps handle commerce and brand-controlled UI.

- Techniques: Return an iframe UI resource from an MCP tool; Extract one component into its own route; Auto-size the iframe from the page; Send component actions back to the host as messages; Pick the content type by complexity
- Tools: MCP-UI, Model Context Protocol (MCP) SDK (Anthropic), Goose (client), ChatGPT, Remote DOM (Shopify), React, TanStack Router, iframe / window.postMessage

## [Google I/O in 6 Minutes (Developer Focused)](../videos/Da275bLi_-4.md)
`Da275bLi_-4` · Better Stack · 2025-11-02 · q2 · intro · news · also: coding-agents, models-research, local-ai

A 6-minute developer-focused roundup of Google I/O 2025 announcements: Jules, Gemini Code Assist, Stitch, Colab, Gemini Diffusion, 2.5 Pro/Flash API features, Gemma 3N, Chrome AI APIs and Android agents.

- Techniques: Async function calling for long-running tools; URL context instead of search for known pages; Thinking budgets for cost control on 2.5 Pro; Sketch or wireframe to UI to code loop (Stitch)
- Tools: Jules, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini Code Assist, VS Code, JetBrains IDEs, Stitch, Figma, Google Colab, Gemini Diffusion, DeepThink

## [AI Agent Protocols Explained: MCP, A2A, ACP and More](../videos/tb0c70DROYE.md)
`tb0c70DROYE` · Better Stack · 2025-11-02 · q3 · intro · review · also: multi-agent, agent-architecture

Better Stack walks through MCP, A2A, ACP and ANP: what each protocol does, where it fits, and short local demos of MCP (Goose), A2A (two agents on Ollama) and ACP (story writer). Practical orientation, no benchmarks.

- Techniques: Add an MCP server to Goose as a command-line extension; Chain MCP servers in one agent task; Build a standalone A2A agent (summarizer / ideator pattern); Serve several ACP agents from one server and call them over HTTP
- Tools: MCP (Model Context Protocol, Anthropic), JSON-RPC 2.0, A2A (Agent2Agent, Google) and its SDK, ACP (Agent Communication Protocol, IBM), ANP (Agent Network Protocol), AITP, ACONP / ACOMP, Coral, Agora, agents.json, WAP push, Goose

## [Warp CLI: Access the Latest AI Models Anywhere For FREE](../videos/dxvowd5bdoI.md)
`dxvowd5bdoI` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, dev-tools

A short walkthrough of Warp CLI, which runs Warp's saved prompts, agent profiles and MCP servers from any terminal, including headless one-shot runs for scripts and CI.

- Techniques: Headless one-shot agent run; Reuse a saved Warp Drive prompt from the CLI; Run a saved workflow with arguments; Pin model and permissions with an agent profile; Attach an MCP server to a single run; Chain prompts in a shell script
- Tools: Warp CLI (warp command, beta), Warp agent profiles, Warp Drive (saved prompts, workflows, notebooks, rules), Warp MCP servers, GPT-5, Context7 MCP server, Better Stack MCP server, WezTerm, Ghostty, iTerm, Next.js, OpenCode

## [AI Coding with Cursor & Claude: Build Apps That People Keep Using in 5 Simple Steps](../videos/i_31WoayEIo.md)
`i_31WoayEIo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, context-engineering, product-ux

Tutorial on building a photo-cleaner iOS app with Cursor and Claude: user journey saved in a markdown file, HTML prototype, palette, fonts, icon, Swift port and animations guided by Context7 docs.

- Techniques: Persistent context files in the repo; Specify the user journey first, then build an HTML prototype; Palette-from-elements prompt sequence; Google Fonts embed into the HTML prototype; App icon via ChatGPT image model with palette constraint; Context7 MCP for framework docs; Fresh chat per task plus Cursor to-do list; Two-stage animation pipeline; Screenshot-driven bug fixing
- Tools: Cursor, Windsurf, Lovable, bolt.new, Claude Code, Gemini CLI, Claude, ChatGPT, ChatGPT image model (called ChatGPT 4 image model in the video), Context7 MCP, Google Fonts, HTML

## [How I Built a ChatGPT Powered Voice Agent with MCP + LiveKit](../videos/jRk63S3v-UQ.md)
`jRk63S3v-UQ` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: voice-multimodal

Tutorial on building a voice agent with a LiveKit + Cartesia + OpenAI base, then wiring a local WhatsApp MCP server into it so speech can trigger tool calls.

- Techniques: Clone, install with uv, and run the voice agent locally; Change the LLM and the system prompt in the main agent file; Wire an MCP server into the voice agent through the MCP-use library
- Tools: LiveKit (voice agent transport and dashboard), OpenAI GPT-4o mini (LLM; transcribed as GPT-40 mini), OpenAI Whisper (speech-to-text), Cartesia Sonic preview (TTS), MCP-use library (MCP tool-use agent), WhatsApp MCP server (local), Brave Search MCP, Airbnb MCP (mentioned as a possible example), uv (Python package manager), Cursor (editor), git

## [RAG Just Got Updated…](../videos/EgXOaH-ZqfU.md)
`EgXOaH-ZqfU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, rag-retrieval, coding-agents

Setup and demo of Archon, a beta self-hosted tool that gives Claude Code or Cursor project docs, a task backlog, and on-demand RAG over crawled docs via MCP. Includes a sponsor segment and an oversold title.

- Techniques: Local Archon stack setup; Project docs and backlog from a feature description; Rules-file-driven on-demand RAG; Crawl vendor docs into a knowledge base
- Tools: Archon, Claude Code, Cursor, Supabase, Docker, Docker Compose, MCP (Model Context Protocol), OpenAI API (embeddings), Google Gemini API (embeddings, free tier), SwiftUI, Xcode, Liquid Glass (Apple UI design)

## [MCP UI, Large Behavioral Models & The Future of AI Interfaces | Better Stack Podcast Ep. 4](../videos/XfuiRayO8fY.md)
`XfuiRayO8fY` · Better Stack · 2025-11-02 · q2 · intro · panel · also: token-cost-efficiency, models-research

Better Stack podcast: hosts discuss MCP-UI (server-supplied UI in chat clients), large behavioral models for robotics, cheap alternative coding models like GLM, and some phone and laptop security tips. Mostly opinion, with little hands-on detail.

- Techniques: MCP-UI iframe component from a tool result; Model hopping in a multi-model editor; GPT-5 at high reasoning effort for code; Family passphrase against voice-clone scams; iOS call screening for unknown numbers; Find My Lock Mode for a lost Mac
- Tools: MCP-UI, Remote DOM, Goose, ChatGPT, Claude, Claude Code, Cursor, T3 Chat, GLM coding plan (Z.ai), GPT-5, Grok 4, Code Supernova

## [Building Custom AI Agents Just Got EASIER - Claude Agent SDK](../videos/NsROagHaKxA.md)
`NsROagHaKxA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: claude-code, agent-architecture, coding-agents

Better Stack walkthrough of the Claude Code SDK (now also called the Agent SDK): a single-prompt query, a streaming-input REPL, replacing the system prompt, and adding a custom MCP tool, all in one short TypeScript file.

- Techniques: One-shot query; Streaming-input REPL; Full system-prompt replacement; Appending to the system prompt; In-process custom MCP tool; Combined demo structure
- Tools: Claude Code SDK (the video also calls it the Claude Agent SDK in its title), Claude Code CLI, Claude Haiku (model option example), TypeScript, zod, MCP (createSdkMcpServer, tool), Bash tool (built-in), Glob tool (built-in)

## [OpenAI Agent Builder vs Claude: Who Wins Multi-Agent Workflows? (Complete Comparison)](../videos/sLiVXlIlSBQ.md)
`sLiVXlIlSBQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: agent-architecture, product-ux, coding-agents

A walkthrough of OpenAI's AgentKit (Agent Builder, ChatKit, widgets), with a Speechmatics sponsor segment up front; practical for seeing the visual workflow and ChatKit setup, thin as a head-to-head comparison.

- Techniques: Classifier-then-route agent workflow; Human approval gate in a workflow; Remote MCP server registration per agent; ChatKit starter quickstart; Theme via Playground, then hand off to a coding agent; Prompt-to-widget, then pin the format in the agent prompt; Custom widgets with Claude Code and agents.md
- Tools: OpenAI Agent Builder, OpenAI AgentKit, OpenAI ChatKit, ChatKit Playground, OpenAI Widget Builder, OpenAI vector store / file search, OpenAI guardrails node, ChatGPT apps, Zapier (MCP servers), Pipedream (MCP servers), n8n (comparison only), Next.js

## [I Built an MCP Server with a Single Prompt!](../videos/yLAmw4oL-6A.md)
`yLAmw4oL-6A` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents

A walkthrough of a hosted prompt-to-MCP-server generator, shown building a weather server and a Figma server, with practical lessons on testing before deploy and wiring the result into Cursor.

- Techniques: Prompt-to-MCP generation with env-var credentials; Test the raw API call before deploying; Declare the plan limits up front; Recover from drift by restarting from the original prompt; Wire a hosted MCP server into Cursor; Split tools by data type; Export and run locally
- Tools: MCP (Model Context Protocol), SSE-based MCP servers, Figma MCP server (get Figma node data tool), OpenWeather API, Cursor, Claude Desktop, Windsurf, mcp.json

## [AI Memory Explained: SuperMemory MCP for Cursor, Claude & Windsurf](../videos/mKXzPVIMFYE.md)
`mKXzPVIMFYE` · AI LABS · 2025-11-02 · q2 · intro · review · also: memory, context-engineering

Walkthrough of SuperMemory MCP: one hosted memory store shared across Cursor, Claude Desktop and Windsurf through add and search MCP tools, plus an IDE rule that auto-saves project changes.

- Techniques: Cross-client memory via a hosted MCP server; Milestone summary saved to memory; Auto-sync rule for memory updates; Resume by searching memory first
- Tools: SuperMemory MCP, SuperMemory API, Cursor, Claude Desktop, Windsurf, Next.js, React

## [I'm Never Vibe Coding Without Next JS Agents Anymore](../videos/yJv2JRM--ws.md)
`yJv2JRM--ws` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, vibe-coding-app-building

A walkthrough of building a full-stack Next.js agent marketplace with Claude Code and three MCP servers (Supabase, ShadCN, Stripe), driven by a PRD and per-MCP prompts. The reusable parts live in linked resources, not on screen.

- Techniques: One-command MCP wiring with a /mcp health check; PRD to converter prompts, one per MCP; Dependency-ordered single-session build; Component-grounded UI with a theme and a usage slash command; Static UI first, then a separate wiring pass; Mock-then-real payment verification
- Tools: Claude Code, Cursor, Next.js, Supabase (MCP server), ShadCN MCP, shadcn/ui, TweakCN, Stripe (MCP server, Stripe checkout), ChatGPT (used for the PRD brainstorm)

## [This Free Tool Makes Cursor 10x Smarter](../videos/52FC3qObp9E.md)
`52FC3qObp9E` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, context-engineering

Better Stack demo: Cursor's built-in docs indexing misses newer APIs, so adding "use context7" to a prompt fetches current library docs through an MCP server. Install is a single npx entry.

- Techniques: Install Context7 as a global MCP server in Cursor; Trigger doc retrieval with 'use context7' in the prompt; Manual doc snippet pull without MCP
- Tools: Cursor, Context7 (MCP server, run via npx; maintained by Upstash), Next.js 15.3 (onNavigate handler), Claude 3.5 Sonnet (model used in Cursor), MCP (Model Context Protocol), npx

## [Build FRONTEND Faster Than Ever with This Cursor MCP Setup!](../videos/DpdM4xei5fw.md)
`DpdM4xei5fw` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents

A 6-minute walkthrough of the 21st.dev / Magic UI MCP server inside Cursor, showing component generation, logo search and catalog install for frontend work.

- Techniques: Install an MCP UI server into the IDE; Prompt for a self-contained component, then let the IDE agent place it; Use logo search to fill in brand or icon assets; Install a catalog component by copying the command
- Tools: 21st.dev (Magic component builder, logo search, component inspiration, UI catalog), Magic UI, Cursor, Windsurf, Cline (called "Klein" in the auto-captions), VS Code, React, TypeScript, MCP (Model Context Protocol), WSL, v0 (mentioned as the comparison point for the component builder), ChatCN (named by the host as a UI library source; spelling from auto-captions, not verified)

## [The EASIEST way to build AI apps – AI SDK Overview](../videos/TbjBzopteO4.md)
`TbjBzopteO4` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: agent-architecture, dev-tools

Better Stack's tour of Vercel's AI SDK for TypeScript: it builds a Next.js chat app with streaming, file input, reasoning display, manual, provider and MCP tools, and streamed structured output, all in about 17 minutes.

- Techniques: Streaming chat endpoint; Per-provider options for reasoning; Manual tool with zod schema; External search and page-fetch tools; Provider-defined tools plus source output; MCP server as tools; Agent loop step cap; Smooth streaming; Streamed structured output; Local dev with an AI gateway
- Tools: AI SDK (Vercel), Next.js, React, Svelte, Angular, Zod, Vercel AI Gateway, OpenAI GPT-5, GPT-5 nano, gpt-image-1, Anthropic Claude Sonnet 4, Google Gemini 2.5 Flash

## [Build ANYTHING with MCP Servers - Coding Tutorial](../videos/sMqlObpNz64.md)
`sMqlObpNz64` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: coding-agents

Builds a TypeScript MCP server wrapping Better Stack's monitors API, then wires it into Cursor and Claude Desktop. Covers tools, resources, prompts, stdio vs SSE, and env-var wrapper scripts.

- Techniques: Minimal TypeScript MCP server skeleton; Register a tool with name, description, zod schema and async callback; Return errors so the model can self-correct; Pick the transport by where the server runs; Cursor setup with an env-var wrapper script; Claude Desktop setup via config file; Static and dynamic resources; Generate the API client from docs with an AI editor
- Tools: Model Context Protocol (MCP) TypeScript SDK (@modelcontextprotocol/sdk), zod, pnpm, shx, Node.js, Cursor, Claude Desktop, Cline (spoken as 'Klein'), Better Stack monitors API, FastMCP (Python wrapper mentioned), Model Context Protocol Python, Java, Kotlin, Rust SDKs (mentioned)

## [6 INSANE Repos I Wish I Knew Before...](../videos/tmj4_HhX7jI.md)
`tmj4_HhX7jI` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, context-engineering, vibe-coding-app-building

Six-repo roundup for Claude Code and MCP: awesome-claude-code, BMAD agile agents, UI component libraries, GitMCP, FastAPI-MCP and mcp-use. Mostly quick pitches plus a mid-video sponsor segment.

- Techniques: Repo to remote MCP server via GitMCP; Expose FastAPI endpoints as MCP tools (fastapi_mcp); Use an MCP server from code with mcp-use; Repo dump into markdown as Claude Code context; BMAD staged agile agents; Pick UI components with the agent; Parallel Claude Code sessions and usage monitoring
- Tools: Claude Code, Claude Desktop, Claude Squad, Claude Code usage monitor, awesome-claude-code, BMAD method, Cursor, shadcn/ui (ShadCN), awesome-ui-component-library, Ant Design, Recharts, Next.js

