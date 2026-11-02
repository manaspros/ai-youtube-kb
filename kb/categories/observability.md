# observability — 181 videos

*tracing, logging, monitoring, analytics on agent/LLM traffic*

By channel: AI Engineer 108 · AI LABS 1 · Better Stack 72

**Synthesized guide:** [guides/observability.md](../guides/observability.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [AI Writes Code Faster Than Your Team Can Review It - Andrew Norrish, Sourcegraph](../videos/-X3yXTwGs9A.md)
`-X3yXTwGs9A` · AI Engineer · 2026-11-02 · q2 · practitioner · talk · also: pr-code-review, enterprise-adoption

Sourcegraph's field director argues AI code outpaces human review, so SRE and platform teams need code-search-driven investigation, monitors and bulk remediation. Mostly a vendor pitch.

- Techniques: Deterministic cross-repo code search for incident root cause; Commit-pattern monitors for AI-written code; Bulk remediation across repos; Webhook-triggered agentic triage; Automated RCA from deploy history; Eval-gated code-review agent over historical branches
- Tools: Sourcegraph (code search, code graph, Deep Search, MCP server), HackerOne, git (history search for incident commits)

## [Claude Code Is Wasting Your Tokens on This](../videos/F4h3a8HFBSE.md)
`F4h3a8HFBSE` · Better Stack · 2026-11-01 · q3 · practitioner · review · also: token-cost-efficiency, claude-code

Claude Code's background-agent summaries re-send full conversations every 30 seconds, costing an estimated 2-20% of usage with no off switch; the video gives measurements and workarounds.

- Techniques: Measure hidden agent-side LLM calls with OTel; Disable background summaries via the subagent setting; Block the summary timer with a preload script (advanced, risky); Budget background agents by wallclock time
- Tools: Claude Code, OpenTelemetry, Better Stack, ccusage, Bun, T3 Code, TanStack, Claude Opus, Claude Haiku

## [If Your AI Scores 100%, Your Eval Is Wrong - Ramakrishnan Lokanathan, eslams.com](../videos/7WUzHIF32vA.md)
`7WUzHIF32vA` · AI Engineer · 2026-11-01 · q3 · practitioner · talk · also: evals, testing-verification

Ramakrishnan Lokanathan argues evals should test the job a system must do, not just a score: test every workflow step, add real failures as regression tests, and make tests harder as scores approach the ceiling.

- Techniques: Ambition-first eval scoping; Step-level workflow evals; Three-layer eval stack; Failure-to-regression loop; Ratcheting the test difficulty; Game-based multi-agent evals (eslams)
- Tools: eslams (open-source Python package, speaker's project, eslams.com), SWE-bench, Humanity's Last Exam, Nemotron 3 (the speaker says he was a red-teamer for these models), GPT-3, ChatGPT, Google Assistant, Gemini, Parallel AI search index (named as 'parallel search model index' in the captions), MIT GenAI Divide report (cited, not named as a tool)

## [Voice AI Where One Wrong Question Breaks the Rules - Shiv Indap, Upstart & Brooke Hopkins, Coval](../videos/3osCbSufv8g.md)
`3osCbSufv8g` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: evals, voice-multimodal, governance-compliance

Coval and Upstart walk through a regulated voice-agent (lending verification calls) eval loop: human review, judge calibration, failure routing, and simulation before release.

- Techniques: Judge-human calibration loop; Structured human review queues; Clustering and anomaly detection for unknown failure modes; Failure-to-owner routing; Voice simulation before release; Feature-flagged agent changes with named approvers
- Tools: Coval (voice-agent evaluation and simulation platform), Google Sheets (initial manual review tracking), LLM-as-judge, RL pipelines and fine-tuned LLMs (mentioned as options for self-healing, not shown)

## [Your Agent Just Paid for Nothing: 6 Attacks on x402 Payments - Ishween Kaur, SoFi](../videos/YU1uD_YkpjU.md)
`YU1uD_YkpjU` · AI Engineer · 2026-10-30 · q3 · practitioner · talk · also: security-guardrails, governance-compliance

Ishveen Kaur (SoFi) walks through six ways an autonomous agent can lose money on x402 machine payments, with guards, a probation-list pattern, and a trace-one-payment-ID method for finding them.

- Techniques: Compare listed price against 402 quoted price, network and wallet before paying; Shared payment-number ledger on the seller side; Buyer retries reuse one payment number; Choose release timing by data cost; Paywall test across all endpoints and no-store caching for paid output; Allow list, block list and probation list for discovered sellers; Per-plan call cap against prompt injection; Single-ID tracing with a 20-25 case dataset
- Tools: x402 (HTTP 402 payment protocol), Llama 3.2 (agent model in the prompt-injection demo), Base Sepolia testnet (auto-caption reads 'Bayes Cipolia'; probably Base Sepolia), x402.org facilitator (testnet), Bazaar (x402 seller directory), Ethereum and Solana (named as alternative chains), Cloudflare pay-per-crawl (cited as a parallel)

## [We Trust AI Agents That Break Every Day - Shy Ruparel, Temporal](../videos/mJ7q8CuVmbw.md)
`mJ7q8CuVmbw` · AI Engineer · 2026-10-29 · q3 · practitioner · review · also: agent-architecture, token-cost-efficiency, enterprise-adoption

Temporal developer advocate Shy Ruparel argues agent reliability is a state and recovery problem, not a model problem, and demos durable execution resuming a crashed payout workflow with a human approval.

- Techniques: Durable workflow with deterministic orchestration and recorded activities; Human approval as a signal with a long timer; Declare the retry policy once, not in loops; Degrade the AI step, not the transaction; One event history for both debugging and replay
- Tools: Temporal, Qwen (run locally as a 36B and a 9B model, per auto-captions), OpenAI Codex (cited as running on Temporal), Replit Agent (cited as running on Temporal), Keycard (talk referenced, not described)

## [300 Agents, 60 People: How We Secured Our Own AI Agents - Aiden Sochowski, Runlayer](../videos/BgLdvF7Qkh8.md)
`BgLdvF7Qkh8` · AI Engineer · 2026-10-27 · q3 · practitioner · talk · also: security-guardrails, governance-compliance, token-cost-efficiency

Runlayer's founding engineer describes how a 50-60 person company monitored its own 300+ daily agents through a gateway, then used the session data for security (intent drift, over-permissioning, cross-agent contamination) and for cost control (erroring MCP tools, model tier jumps).

- Techniques: Gateway-first agent telemetry; Per-tool-call intent classifier; Baseline-and-flag on tool-use history; Inbound and outbound content policies; Tight write scoping per agent; MCP error and retry monitoring with rate limits; Budgets and default model tiers
- Tools: MCP (Model Context Protocol), Claude Code (captioned as 'cloud code'), Opus (Claude model, mentioned as hard to prompt-inject), Runlayer (the speaker's company; product is a gateway, not named in detail)

## [How to Test Your Agents on Real Tasks With Harbor - Xander Song, Arize AI](../videos/kRJjSOYqW0I.md)
`kRJjSOYqW0I` · AI Engineer · 2026-10-27 · q4 · practitioner · talk · also: testing-verification, evals, coding-agents

Xander Song (Arize) introduces Harbor, an open-source framework for testing agents on real tasks in fresh sandboxes, scored by side-effect verifiers, and shows how his team used it to tune a prompt for SQL over GraphQL.

- Techniques: Harbor task layout; Oracle-first validation; Keep verifiers outside the agent's view; Synthetic task and oracle generation; Before/after prompt A/B in a fixed harness; Read-only SQL tool for aggregates; Single-node app snapshot in Docker; One-turn skill-triggering test
- Tools: Harbor, Docker, Arize Phoenix, OpenInference, OpenTelemetry, OTLP, ATIF (Agent Trajectory Interchange Format), Daytona, Modal, E2B, SQLite, Postgres

## [Agents That Self Improve While You Sleep - Fuad Ali, Arize AI](../videos/UGuNt2_Oz8s.md)
`UGuNt2_Oz8s` · AI Engineer · 2026-10-27 · q3 · practitioner · workshop · also: evals, skills-self-improvement, pr-code-review

A vendor-led workshop on closing an agent self-improvement loop: scheduled trace review, failure datasets, evals, replay experiments, and human checkpoints at the high-leverage points.

- Techniques: Trace-to-fixture pipeline; Trajectory-level LLM-judge eval; Cheap-first evaluator stack; Replay-based fix validation; Confidence-threshold human routing; Session-level eval signals; Stop criteria for eval depth
- Tools: Arize AX (tracing and evals platform), AX CLI, Arize Signal (always-on trace-review agent), Arize Alex (in-house agent), Phoenix (mentioned, not demonstrated), Arize managed sandboxes, GitHub, Codex, Cursor, Claude Code, OpenCode, Modal

## [What Does an AI Engineer Do Now? - Aparna Dhinakaran, Arize AI](../videos/ImnZ7s68jw8.md)
`ImnZ7s68jw8` · AI Engineer · 2026-10-26 · q3 · practitioner · talk · also: software-factory, evals, agent-architecture

Arize's Aparna Dhinakaran argues the AI engineer's job is now building the build-eval-ship-monitor-improve loop itself, with always-on agents consuming telemetry and evals aligned to human judgment.

- Techniques: Telemetry-triggered always-on agent sweep; Issue memory across agent runs; Sandbox-per-run with single proxy egress; Durable agent resume; Harness and model abstraction with per-run evaluation; Evaluator alignment against golden data; Offline plus online evals on the same definitions; Trace the coding agents too
- Tools: Arize Signal, Arize Evaluator, Claude Code, Cursor, Codex, Anthropic model family (multiple models, unnamed)

## [How to Write Your First AI Eval - SallyAnn DeLucia, Arize AI](../videos/gv4w23xYj-0.md)
`gv4w23xYj-0` · AI Engineer · 2026-10-26 · q3 · practitioner · workshop · also: evals, multi-agent

A hands-on workshop on writing a first LLM-as-judge eval for an agent: why vibe checks fail, how traces feed evals, how to write concrete criteria, and how to build and iterate a judge in a prompt playground.

- Techniques: Six-part criteria template; Judge prompt structure; Variable mapping for judge inputs; Span-level dataset selection; Iterate the judge in a prompt playground against a dataset; Alignment against human labels; Online evals on incoming traces; Decision-model comparison; Instrumentation: auto, manual, or hybrid
- Tools: Arize AI (Arize AX platform, captioned 'Arise' or 'AX'), Alex (Arize's in-platform AI agent that can run playgrounds and iterate on prompts), Signal (Arize's managed agent that reads traces, finds issues and proposes fixes), OpenInference (Arize's tracing package with auto-instrumentors for agent frameworks), OpenAI decision model API (mentioned as released the week before the talk), Anthropic, OpenAI and Gemini provider API keys (configured under AI providers in settings), ROUGE and BLEU (named as code-based eval metrics), Notion one-pager (workshop instructions)

## [Your Agent Fix Just Broke Something Else - Sofia Jakovcevic, Arize AI](../videos/v5tm5EAzsAs.md)
`v5tm5EAzsAs` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · also: evals, testing-verification, multi-agent

A five-step regression loop for agents built on production traces, evaluators and CI gates, so a prompt or policy change is judged on numbers before it merges. Vendor-led demo of Arize.

- Techniques: Five-step trace-driven regression loop; Four-bucket dataset composition; LLM-as-judge plus code evaluators; Side-by-side prompt versions in a playground; Agent playground against a remote agent; Run experiments from coding agents through skills; CI gate on experiment results
- Tools: Arize (Arize AI observability backend and platform, incl. prompt hub, prompt playground, agent playground, experiments, datasets), Arize agent skills repository (public, for coding agents), GitHub Actions (CI example), Arize SDK / REST / CLI (run experiment), LLM-as-judge evaluators (pre-built: hallucination, user frustration, security checks; custom evaluators supported)

## [Why Frontier Models Fail as Buy-Side Analysts - Janie Gu, Google DeepMind & Suyeol Yun, LinqAlpha](../videos/aVbRSIQO2dE.md)
`aVbRSIQO2dE` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: evals, sandboxing-execution, models-research

Google DeepMind's Kaggle team and LinkAlpha present why most agent benchmarks are unreliable, what Kaggle found reproducing 65 of them, and MandateBench, a buy-side analyst benchmark graded on reasoning paths.

- Techniques: Reproduce, then read every trace before trusting a score; Separate the agent under test from the grader; Log every model call and keep traces open; Measure variance with repeated runs; Pin reasoning effort explicitly for head-to-head comparisons; Rubric-based grading of a reasoning graph; What-if perturbation of key assumptions; Reconcile conflicting source figures explicitly
- Tools: Kaggle, Kaggle Benchmarks, Google DeepMind models (as evaluated), MandateBench, HuggingFace (named as a place models searched for answers), Reddit and StackOverflow (named as places models searched for answers), Heijen's Code to Video Bench (captioned name; launched last week per speaker), Octava, Quadrillion, Rehearsals (partner names as captioned)

## [Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni Analytics](../videos/A3FL_zTQKU0.md)
`A3FL_zTQKU0` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · also: evals, testing-verification, governance-compliance

Stephanie Jarmak (Omni Analytics) argues agent evals should be done like experiments: check the tool pipeline end to end, match the benchmark to your own workload, decouple flags from enforcement, and trust independent traces.

- Techniques: Tool-use pipeline audit; Harness-plus-model pairing as the unit under test; Workload-representative internal benchmark; Explicit metric choice per use case; Separate flagging from enforcement; Independent record comparison for trust; Shadow deployment and production measurement; Autonomy boundary spec for each action
- Tools: Amp (coding agent), Sourcegraph code search MCP tool, Claude (as used in the grep example), grep, Terminal Bench (transcribed as 'Terminal Bench 4'), OpenHands (open coding-agent harness), Opus 5 (model, as transcribed), Astra (model or harness, as transcribed; unverified), Code Scale Bench (speaker's own public benchmark for large codebases), LLM-as-judge (generic pattern), Omni Analytics evaluation harness (in progress)

## [Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse](../videos/obfPzbapMIM.md)
`obfPzbapMIM` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: evals, testing-verification, governance-compliance

Langfuse workshop on evaluating high-stakes agents: trace everything, build datasets from production via expert error analysis, mix LLM-judge with deterministic evaluators, and gate prompt changes in CI.

- Techniques: Annotation queue for expert error analysis; Free-text comments to failure-mode taxonomy via LLM; Mixed evaluator suite (LLM judge + code checks); Prompt-promotion-triggered CI eval gate; Mask PII before persisting traces; Shadow runs for ground-truth building; Judge calibration against a human-labeled sample
- Tools: Langfuse, GitHub Actions, ClickHouse, PostgreSQL, Amazon S3, OpenAI chat API, Anthropic models, Whisper Flow, Claude, Langfuse skill (agent skill)

## [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](../videos/SHMCGrNJJGc.md)
`SHMCGrNJJGc` · AI Engineer · 2026-10-17 · q4 · practitioner · workshop · also: evals, testing-verification

Hands-on workshop: trace a Claude financial-analyst agent in Phoenix, read failures, write code and LLM-judge evals, validate judges against human labels, run experiments, and gate CI on them.

- Techniques: Deterministic code eval with structured input; Faithfulness judge with full retrieval context; Five-part LLM judge prompt with constrained labels; Judge hygiene: different-family, stronger judge, suppressed tracing; Open coding then axial coding of traces, with a coding agent; Golden dataset with dev/test split by stable ID; Run experiments on the failing subset only; pass^k reporting for nondeterministic agents; Vitest-based eval suite gated in CI; Eval-driven development
- Tools: Arize Phoenix, Claude Agent SDK, Claude Code, Claude Sonnet 5.5, Claude Haiku 4.5, Claude Haiku 5.5, Vercel AI SDK, OpenTelemetry, OpenInference, Vitest, GitHub Actions, TypeScript

## [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](../videos/tZycGA_Fbfo.md)
`tZycGA_Fbfo` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: mcp-and-tools, security-guardrails, context-engineering

Credit Karma's senior staff engineer walks through a governed enterprise agent stack: scaffolded agent repos, a central MCP gateway, risk-gated execution, per-run evals, PII blocking, and a context optimizer that cut token use about 90% in demos.

- Techniques: Dev-portal agent scaffolding; Gateway token exchange with namespace routing; Risk-classified plan graph with HITL gate; Thread, run and checkpoint memory; Severity-based redaction before every sink; Context pipeline: budget, re-rank, dedupe, compress; Per-run eval scoreboard with nested detail; Three-layer monitoring split
- Tools: LangGraph, LangChain, FastMCP, Redis, JWT, Docker, Kubernetes, OpenTelemetry, Grafana Tempo, Prometheus, ELK, Loki

## [How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival](../videos/8g1N_a3h9H0.md)
`8g1N_a3h9H0` · AI Engineer · 2026-10-15 · q4 · practitioner · talk · also: token-cost-efficiency, evals, context-engineering

Alvin Pane (OutRival) on cutting LLM token spend in production: measure baseline variance with a ceiling test, shrink prompts with DSPy-style optimization, downsize models, then gate release on paired shadow-deployment stats with a lower confidence bound above zero.

- Techniques: Ceiling test (self-agreement baseline); Prompt optimization as search (DSPy-style); Prefix-cache-friendly prompt structure; Split pipeline by model size; Paired shadow-deployment statistics
- Tools: OpenTelemetry, DSPy, Jeepa optimizer (as transcribed; likely DSPy's GEPA optimizer)

## [The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale](../videos/-a2oTS9J67U.md)
`-a2oTS9J67U` · AI Engineer · 2026-10-14 · q3 · practitioner · talk · also: governance-compliance, enterprise-adoption

Michele Grant on earning trust in enterprise AI agents: define value, name an accountable owner, and grant autonomy in stages backed by audit evidence, using an M&A integration example.

- Techniques: Pre-deployment value case with baselines; Human work standard (one-page decision map); Deterministic core for financial math; Telemetry as proof, not the model's summary; Four-stage autonomy scorecard; Regression triggers in the model inventory

## [Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI](../videos/fnuNVFgLjHA.md)
`fnuNVFgLjHA` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: evals, skills-self-improvement, software-factory

Arize workshop on closing an agent's detect, investigate, fix, verify loop using an always-on trace-analysis agent, coding-agent skills, harness-as-judge scoring and replay experiments; mostly a product walkthrough.

- Techniques: Continuous failure clustering over production traces; Join trace evidence with the code path; Plain-language harness-as-judge rubric with tool access; Failure-dataset replay with agent experiments; Alert-triggered agent investigation; Agent skills for trace analysis from the coding agent
- Tools: Arize Signal, Arize skills, Arize agent experiments, Claude Code, OpenAI Agents SDK, FastAPI, Datadog, GitHub, Cursor, Codex

## [Continuously Improving Agents with Langfuse — Annabell Schäfer & Lotte Verheyden, ClickHouse](../videos/BOCjybvJYM4.md)
`BOCjybvJYM4` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: evals, coding-agents

Hands-on Langfuse workshop on monitoring agents in production: instrument traces, write failure-mode evaluators (LLM-judge and code) on live traces, then use a coding agent over trace data to find silent failures.

- Techniques: Failure-mode-first evaluator set; JSON-path variable mapping for LLM judges; Boolean code evaluators on live observations; Coding agent as trace analyst; Coverage monitoring
- Tools: Langfuse, OpenAI Agents SDK, OpenAI API, Codex, Claude Code, TypeScript, Python

## [Build a Platform and Watch It Burn — Michael Forrester, Accenture & Whitney Lee, Datadog](../videos/1tpqdglI3T0.md)
`1tpqdglI3T0` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: security-guardrails, sandboxing-execution, mcp-and-tools

Workshop where attendees attack a Kubernetes-hosted burrito-ordering agent, then add layered infra and AI guardrails (admission, runtime, network, input/output scrubbing, MCP checks) and see which attacks each layer stops.

- Techniques: Layered guardrails across infra and AI; Input guard before the LLM call; Mid-stream output scrubbing; MCP tool description review and registry allowlists; OpenTelemetry traces for every agent turn; Kernel-level prevention for runaway processes; Agent identity and least privilege; Three-question rubric for AI in a workflow
- Tools: Kubernetes, Amazon EKS, kagent, Kyverno, Falco, Falco Talon, Tetragon, KubeArmor, Cilium, SPIFFE/SPIRE, LLM Guard, NeMo Guardrails

## [Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI](../videos/_zUp6y9bDU8.md)
`_zUp6y9bDU8` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: evals, coding-agents, skills-self-improvement

Arize's Ankur Duggal argues agents need trace-based evals, then demos a coding agent (Claude Code plus Arize skills) turning production traces into failure analysis, datasets, evaluators and experiments.

- Techniques: Trace-to-dataset-to-experiment loop; Coding agent as eval workflow driver; Mixed evaluator set; Sampled online evals; Tailored evals from observed failures
- Tools: Arize AX, Phoenix, Claude Code, Codex, Cursor

## [How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI](../videos/xn8EsW0wxyc.md)
`xn8EsW0wxyc` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: security-guardrails, agent-architecture, mcp-and-tools

Venice AI's developer-relations lead explains how secrets leak through agent architectures (logs, vaults, LLM context, tool calls) and patterns to contain them: hashed IDs, handles, narrow tool scope, and keeping credentials out of the reasoning layer.

- Techniques: Credential-in-runtime, not in-prompt; Hashed identifiers for rate limits and tracking; Split-key custody for stored outputs; Revocable handles as capabilities; Narrow tool exposure per agent; Prompt-injection classifier in front of the agent; Own the agent runtime; Verifiable private inference via TEE attestation
- Tools: Venice AI, OpenClaw, 1Password, HashiCorp Vault, Firecracker, AWS EC2, VPC, Qdrant, LanceDB, Cursor, Claude Code, MCP

## [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](../videos/YIxzNZDDy1A.md)
`YIxzNZDDy1A` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: evals, sandboxing-execution, coding-agents

Wolfram Ravenwolf's hands-on workshop on building a reproducible agent benchmark (Terminal-Bench via Harbor, WolfBench dashboard), arguing that one averaged score hides variance, cost and configuration choices.

- Techniques: Multi-metric leaderboard per configuration; Pin the harness and keep a fork; Sandbox per trial with bounded concurrency; Smoke-test one task before the full run; Explicit retry policy by error class; Set and record every sampling and agent setting; Trace-first debugging of surprising scores; Shareable result snapshot
- Tools: Harbor, Terminal-Bench 2.0, Terminus 2, Weights & Biases Weave, WolfBench, Inspect (UK AISI), Marimo, CoreWeave serverless sandboxes, Daytona, OpenRouter, Docker, uv

## [The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder](../videos/abw_m-DRi1k.md)
`abw_m-DRi1k` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: security-guardrails, sandboxing-execution

Coder's staff solutions engineer explains the "lethal trifecta" (private data, external communication, untrusted input) and argues for isolated remote dev environments, a logging model proxy, and a process-level agent firewall.

- Techniques: Remote isolated agent environment; Logging model proxy in front of the LLM provider; Process-level agent firewall with command denylist; Pre-baked environments as supply-chain control
- Tools: Coder, Terraform, Claude Code, Codex, OpenClaw

## [From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot](../videos/b9UhZkKjX_A.md)
`b9UhZkKjX_A` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: coding-agents, software-factory, multi-agent

GitHub's Jose Palafox walks through the Copilot agent surfaces: local agents you steer, reusable shared agents, cross-repo orchestration, and headless agents in CI that get cost and trace visibility through OTel.

- Techniques: Headless one-shot agent in CI; Slash-command phase gates on issues; Scaffold agents from a one-line description; Marketplace or private-repo distribution; Orchestrate: issues as goals, agents per repo; Cross-model plan audit; Small-model codebase explorer; OTel per-agent cost monitoring
- Tools: GitHub Copilot CLI, GitHub Copilot SDK, GitHub Actions, GitHub Agentic Workflows, Awesome Copilot, OpenTelemetry, Slack, Microsoft Teams

## [Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto](../videos/jJQoVkd5yLg.md)
`jJQoVkd5yLg` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: mcp-and-tools, product-ux

Reducto deleted its one-tool-per-endpoint MCP server after a team rollout showed agents were confidently wrong; the rebuild uses fewer workflow-shaped tools, legible uncertainty, and session logs that feed back into guidance.

- Techniques: Workflow-shaped MCP tools instead of endpoint wrappers; Per-step next-action guidance in tool responses; Snapshot / live-state tool with specific error codes; Confidence and provenance in tool outputs fed back to the model; Evals that score clarifying questions as correct behaviour; Session logging, then mining for override and low-confidence signals; Require an explanation of what was built and why
- Tools: Claude Code, MCP, Slack, Notion, Circleback

## [Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab](../videos/Emo5FGGY-wM.md)
`Emo5FGGY-wM` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · also: evals, product-ux

Amazon AGI Lab's Felipe Blanes on why static evals fail in production: run an eval flywheel fed by real customer signals, and be transparent about product limits, since trust rises more from honesty than from higher benchmark scores.

- Techniques: Eval flywheel with customer signals; Trajectory caching with model fallback; Stated-limitations disclosure; Non-technical authoring layer on an agent core
- Tools: Amazon Nova Act

## [Your AI Agent Has No Nervous System — Matt Gibiec, Dynatrace](../videos/YNT7Plf9KIg.md)
`YNT7Plf9KIg` · AI Engineer · 2026-10-09 · q2 · intro · talk · also: coding-agents, context-engineering

Vendor pitch for Dynatrace's "Blue Box" agent, which argues AI coding agents need live environment context (service dependencies, production telemetry, change history) to avoid hallucinated or breaking changes.

- Techniques: Dependency-mapped local testing; Baseline-deviation alerts to the coding agent; Change-correlated incident triage; Context-scoped fix suggestion with human approval
- Tools: Dynatrace Blue Box

## [AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar](../videos/uuwDWRbxoYo.md)
`uuwDWRbxoYo` · AI Engineer · 2026-10-09 · q2 · intro · talk · also: pr-code-review, software-factory

Sonar's Ali-Reza Adl-Tabatabai pitches an agentic PR validation system (ex-Guitar) that reviews, fixes, and auto-merges PRs, with a trust ladder for rollout. Mostly product pitch, few numbers.

- Techniques: Trust-gated automation ladder; Autofix loop until green; Flaky-test detection and rule-based retry; Agent plus static-analysis hybrid; Model routing proxy with failover; Aggregate PR and CI analytics
- Tools: Sonar, SonarQube, Guitar (agent platform)

## [The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](../videos/TeErpYBUIeM.md)
`TeErpYBUIeM` · AI Engineer · 2026-10-07 · q3 · intro · talk · also: evals, skills-self-improvement

Langfuse co-founder on moving agent improvement from manual trace review to an AI-driven loop, where agents propose fixes and dataset/evaluator updates while humans set goals and gate changes, with a changelog-writer case study.

- Techniques: Online plus offline eval loop; Agent-proposed fix with human gate; PR review decisions as eval signal; Backtest candidate against baseline; Agent-maintained evaluators from error patterns; Scheduled batch loop over labeled production data
- Tools: Langfuse, Langfuse agent skills, GitHub pull requests, coding agent, Langfuse prompt management, Langfuse annotation queues

## [Why Building an Eval Platform Is Harder Than It Looks — Braintrust](../videos/mUQoVz7THu0.md)
`mUQoVz7THu0` · AI Engineer · 2026-10-07 · q2 · intro · talk · also: evals, data-engineering

Braintrust's solutions lead on why eval platforms are a systems problem: a maturity path from spreadsheets to production-trace flywheels, plus why agent traces are hard to store and query.

- Techniques: Three-part minimal eval harness; Production-failure-to-test-case flywheel; Side-by-side experiment UI for prompt and model changes; Separate hot and cold paths for trace data; Natural-language headless eval runs via coding agents
- Tools: Braintrust, BTQL

## [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](../videos/eXA2tjRZIbY.md)
`eXA2tjRZIbY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · also: agent-architecture, evals

Resolve AI's architecture for production-ops agents (on-call, incidents, background tasks): six pillars covering model routing, context, causal evidence, governed actions, learning loops, and multi-level evals.

- Techniques: Alert-as-prompt investigation fan-out; Evidence-chain gate on root causes; Per-subtask model routing; Tiered action permissions; Five-level eval stack; Anti-sycophancy by design
- Tools: Grafana, Slack, Microsoft Teams, Google Cloud (GCP), graph RAG, knowledge graph

## [Agent Memory Is Solved. Agent Learning Isn't. — Karthik Ranganathan, Yugabyte](../videos/9_oy4owGtPI.md)
`9_oy4owGtPI` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: memory, multi-agent, context-engineering

Yugabyte's CEO argues agent memory is solved but cross-agent learning is not, and demos Mako, a private-to-shared context store where humans promote memories and provenance is traceable.

- Techniques: Private-to-shared promotion gate; Provenance on every memory; Scoped data packs with a skill-driven MCP interface; Cross-session resumability via shared memory; One-variable-at-a-time RAG tuning with traces; Trace-based token accounting
- Tools: Mako (Yugabyte agent-native persistence layer), YugabyteDB, Claude Desktop, Claude Design, Codex, ChatGPT, MCP, Postgres

## [The Transcript Looked Fine. The Call Wasn't. — Debugging Voice Agents, Arize](../videos/42Bz0TUfeOQ.md)
`42Bz0TUfeOQ` · AI Engineer · 2026-10-06 · q2 · practitioner · talk · also: voice-multimodal, evals

Arize PM Fuad Ali on why voice agent failures are invisible in transcripts, and how to trace audio sessions, run audio-native evals, and close an observe-evaluate-improve loop. Partly a product pitch, with real open-source instrumentation content.

- Techniques: Session-stitched voice trace view; Provider-agnostic semantic conventions for LLM traffic; Audio-native evals for tone, latency and interruptions; Online evals on spans with monitors that trigger investigation; Replay failed traces against a patched endpoint to verify a fix
- Tools: Arize, OpenInference, OpenTelemetry, Grafana, WebSocket realtime API, GPT Realtime, Gemini Live, LiveKit

## [From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI](../videos/F0TNSmbo5hE.md)
`F0TNSmbo5hE` · AI Engineer · 2026-10-06 · q2 · practitioner · workshop · also: evals, software-factory, claude-code

Arize workshop on closing the agent improvement loop: instrument an OpenAI Agents app with OpenInference, have a coding agent mine traces and patch failures, then automate it with Arize Signal. Vendor-heavy.

- Techniques: Turn on OpenInference tracing for an agent app; Install vendor agent skills into the repo for the coding agent; Trace triage that looks past error status; Single-problem fix loop with re-verification; Triage automated findings into issues, dataset rows, evaluators or PRs; Regression and guardrail evals before merging an automated fix
- Tools: Arize AX, Arize Signal, Alex (Arize in-product assistant), OpenAI Agents SDK, OpenInference, Arize AX CLI, Claude Code (VS Code extension), npx skills (arise-ai skills), npm, GitHub, WonderToys demo app (Arize sample)

## [Advanced Workshop: Mastering AI Observability — Doug Guthrie, Braintrust](../videos/hfEczxdNyvU.md)
`hfEczxdNyvU` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: evals, coding-agents

Braintrust workshop on AI observability: trace agents, score production traffic with judges and topics, and let a coding agent run the eval-and-fix flywheel through the Braintrust CLI.

- Techniques: Binary, harsh LLM judges with examples in the prompt; Human-calibrated judges; Scores defined in code and pushed to the platform; Automation rules with scope and sampling for online scoring; Topic windows and filters for long conversations; Coding agent as flywheel operator; Service account for the analysis loop; Remote eval exposed to a playground; Mutable spans for attaching scores later
- Tools: Braintrust, Braintrust CLI (bt), OpenAI Agents SDK, Codex, Claude Code, Cursor, OpenCode, uv, GitHub Actions, Modal, ClickHouse, Brainstore

## [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](../videos/qZj7sqmidqA.md)
`qZj7sqmidqA` · AI Engineer · 2026-10-06 · q3 · intro · workshop · also: evals, testing-verification

A two-hour Arize AI workshop on replacing "vibes" with measurement: read traces, write code and LLM-judge evals, calibrate the judges, then close the loop with experiments.

- Techniques: Error analysis (open then axial coding); Code evaluator on trace or span; Context-matched LLM judge; Rubric structure for LLM judges; Judge calibration with golden labels; Test both directions; Experiments on a fixed dataset; Evaluator split by dimension, with guardrail vs north-star labels; Online sampled evals at span or trace scope; Eval-driven development and data priorities
- Tools: Arize AX, Arize Phoenix, OpenInference, OpenTelemetry, Claude Agent SDK, Anthropic Claude Haiku (agent model), Anthropic Claude Sonnet 4.6 (judge model), Claude Code, Cursor, Codex, Arize Skills (npx install), Alex (AX built-in eval agent)

## [What Is an Inference Engine, Anyway? — Charles Frye, Modal](../videos/woIYJYd_etI.md)
`woIYJYd_etI` · AI Engineer · 2026-10-06 · q4 · deep · workshop · also: inference-serving, infra-cost-scaling

Charles Frye (Modal) explains what runs inside an LLM inference engine: workloads, prefill vs decode, process layout, scheduler bottlenecks, KV cache, CUDA graphs, speculative decoding, and production debugging.

- Techniques: Phase-split serving metrics; Keep host work off the GPU critical path; Speculative decoding with exact-output verification; Prefix and radix KV-cache reuse; Treat queueing and cache thrash as alerts; Correctness logging and post-deploy evals; Profile for per-GPU or per-host anomalies
- Tools: SGLang, vLLM, TensorRT-LLM, PyTorch, Hugging Face transformers, FlashAttention, FlashInfer, CUTLASS, Triton, DeepGEMM, DeepEP, Marlin

## [The State of AI in Software Development: Data from 400+ Orgs — Justin Reock, DX](../videos/Se8jHLliLXE.md)
`Se8jHLliLXE` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: enterprise-adoption, pr-code-review

DX's deputy CTO shares 2025-26 data from 400+ orgs: AI lifts delivery speed only modestly, quality volatility grows, and PR size and falling change confidence are the warning signs.

- Techniques: Cohort-vs-foundational-metric comparison; Utilization, impact, cost framing; Agent feedback as telemetry; Agent-readiness audit; Agent first-pass PR review kept in the PR thread; Bottleneck-first AI adoption
- Tools: DORA metrics, DX platform

## [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](../videos/_mi3alkqy4s.md)
`_mi3alkqy4s` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: pr-code-review, evals, testing-verification

Laurie Voss (Arize AI) argues that agent code generation has outrun human review, so teams should stop reviewing PRs by hand and build an engineered review harness, with humans designing its definition of good.

- Techniques: Multi-pass review with consensus filtering; Default-suspicious reviewer prompt; Tool-using reviewer over the whole repo; Runtime verification by the agent itself; Machine-checkable mergeability rubric; Codify the definition of good as a harness
- Tools: GitHub Copilot code review, Cursor reviewer, CodeRabbit, Greptile, Graphite, Codex, Anthropic automated security review action, SWE-bench, SWE-bench Pro, FrontierBench

## [The 5 Levels of Self-Driving Production — Eric Schwartz, Traversal](../videos/y-OVWZD4j6U.md)
`y-OVWZD4j6U` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: enterprise-adoption, product-ux

Traversal's PM argues AI coding agents shift engineering time from building to troubleshooting, and proposes a five-level "self-driving production" autonomy scale plus five criteria for judging AI SRE tools.

- Techniques: Five-level autonomy scale for incident response; Five-question checklist for evaluating AI SRE tools; Causal root cause framing for multi-hop incidents; Agent-first incident intake; Alert triage pass before on-call
- Tools: Traversal (AI SRE product; production world model and causal search engine), Claude Code (auto-caption "Cloud Code"), Codex, Cursor, Datadog, Elastic, Splunk, ServiceNow, Slack

## [Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog](../videos/rTojoVotlD8.md)
`rTojoVotlD8` · AI Engineer · 2026-10-04 · q3 · intro · talk · also: governance-compliance, evals, security-guardrails

Datadog's Marina Petzel argues LLM apps need cost, safety and quality monitoring on top of the golden signals, since a 200 OK can still hide a wrong answer; gives tagging and metric recommendations.

- Techniques: Mandatory four-level cost tagging; Track token creep and model drift as separate alerts; Caching layer to remove redundant completions; Guardrail metrics as blocking thresholds; LLM-as-judge for completeness, embeddings for relevance; Score RAG retrieval separately
- Tools: Datadog agent observability

## [Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp](../videos/tUPPVhBBcoM.md)
`tUPPVhBBcoM` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: software-factory, skills-self-improvement, pr-code-review

Warp's founder argues software engineering is becoming factory engineering: agent loops run from triage to spec to implementation to monitoring, with humans gating stuck points and observer agents improving the skills.

- Techniques: Software factory loop with human gates; Triage routing by ambiguity; Product spec plus tech spec; Observer agent skill loop; Verification by running the product
- Tools: Warp, Claude Code, CI/CD, GitHub, Computer use

## [An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases](../videos/hd7TOvmyAxU.md)
`hd7TOvmyAxU` · AI Engineer · 2026-09-27 · q2 · practitioner · demo · also: evals, agent-architecture, training-finetuning-rl

Live demo of W&B's ARIA research agent running autoresearch experiments, plus its trace-to-eval loop: production traces, LLM judges, nightly YAML task suites, and promotion gated on eval scores.

- Techniques: Eval suite as YAML unit tests; Production traces to tasks loop; Live LLM judges as signal detectors; Eval-gated promotion; Async job dispatch from an agent; Agent analyzes its own traces
- Tools: Weights & Biases Weave, W&B Launch, W&B Inference, W&B Artifacts, W&B Reports, CoreWeave sandbox, Kubernetes, iOS app

## [How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases](../videos/XyV6bSMyq-I.md)
`XyV6bSMyq-I` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: evals, skills-self-improvement, agent-architecture

Weights & Biases walks through how its ARIA agent evaluates and improves itself: production traces become offline regression tasks, and the agent runs its own hill-climbing loop.

- Techniques: Eval flywheel from production traces; Byte-identical prod and research agent with a sync job; YAML-defined config variants; Three task simulation modes; Dual scoring: pass/fail plus pairwise relative scoring; Unconstrained sandbox for agent research loops
- Tools: Weights & Biases Weave, W&B Reports, ARIA agent, Claude Code, YAML task and config specs

## [Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer](../videos/btxG75rNJC4.md)
`btxG75rNJC4` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: inference-serving, training-finetuning-rl

Two AI21 engineers walk through two silent vLLM bugs for hybrid Mamba models, one a scheduler ordering error and one a 32-bit index overflow, and the debugging method that found them.

- Techniques: Logprob comparison against a reference forward pass; Reproduce under pressure with determinism; Thread identity through the forward context; Bisect by forcing one code path; Check whether a fix is causal and watch for overflow
- Tools: vLLM, Hugging Face Transformers, NVIDIA compute-sanitizer, FSDP, Jamba (hybrid Mamba plus attention model)

## [Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google](../videos/l1-D89bAuOA.md)
`l1-D89bAuOA` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · also: evals, inference-serving

Google engineers argue that LLM serving benchmarks often blame the server when the benchmark client is at fault, and show Inference Perf, a multi-process, reproducible load generator built for production-scale inference.

- Techniques: Scheduled multi-process load generation; Client-side health check on every run; Declarative benchmark configs with distributions; Sweep the load to find saturation; Match sampling and dataset preprocessing to production; Shared workload definitions
- Tools: Inference Perf, llm-d, Prism, vLLM, SGLang, Kubernetes, k6, Locust, MLPerf, ShareGPT

## [Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../videos/EL123UNokkI.md)
`EL123UNokkI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: pr-code-review, evals, multi-agent

Uber's engineers explain uReview, their multi-agent code review system: how they built feedback-driven evals, team-owned customizations, and a cost/quality loop, plus why they think humans move up to an expanded outer loop.

- Techniques: Reply-sentiment and addressal-rate tracking; Trajectory-based runtime tuning with turn guardrails; Tiered review generators with post-processing; Few-shot AI linters with deterministic context; Ownership-coupled rule distribution
- Tools: GitHub, Fabricator, Claude

## [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../videos/YXEqC05WEI0.md)
`YXEqC05WEI0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: security-guardrails, evals, governance-compliance

Hinge Health's AI lead on shipping member-facing health AI: put irreversible decisions in code above the model, strip PHI at ingestion, monitor live traffic, and verify the judge before fixing the agent.

- Techniques: Code-layer routing above the model; PHI stripping at ingestion with environment and region separation; Layered live scoring of production traffic; Judge-first triage before agent changes; Severity triage for launch decisions

## [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](../videos/hD9-V56FNRI.md)
`hD9-V56FNRI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, security-guardrails, memory

Talk arguing that once agents call tools and change state, they are distributed systems, so they need idempotency, compensation, scoped permissions, bounded retries and per-step traces.

- Techniques: Idempotency keys plus status lookup on every side-effecting tool; Persist each loop step and define compensation operations; Retry and fanout guardrails; Scoped credentials and tool allowlists; Parameter-bound, expiring human approvals; Memory as a cached, provenance-tagged store; Tool contracts with schemas and idempotency
- Tools: Replit AI agent (cited as a production-database deletion incident; not a tool under review), Air Canada chatbot (cited as an incorrect-refund incident; not a tool under review)

## [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../videos/GJX19pNhmSw.md)
`GJX19pNhmSw` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: token-cost-efficiency, governance-compliance, agent-architecture

Microsoft's Tisha Chawla and Susheem Koul argue agent cost control belongs at the agent-run layer, not the request layer. They show an out-of-band "TokenOps" plane that attributes spend per run, steers runs toward budget before halting them, and reports vendor benchmarks.

- Techniques: Run-scoped attribution tags and budgets; Boundary decorator on agent methods; Governor with a developer-declared action allowlist; Tiered policy ladder: steer, then halt; Cost guard: projected-overrun steering; Preview (shadow) mode for guardrails; Benchmark against throttling baseline
- Tools: OpenTelemetry, LangChain, LangSmith, LiteLLM, Portkey, Cloudflare AI Gateway, browser-use, MetaGPT

## [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](../videos/wCIYViPd4SU.md)
`wCIYViPd4SU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, enterprise-adoption, claude-code

Two Sigma explains how it runs cloud agents as each employee's own identity, using a propagated attribution header and enterprise-grounded web search to cut exfiltration risk.

- Techniques: Run agents as the user identity in existing per-user namespaces; Propagate an attribution header like a trace ID; Deny native web tools and route through enterprise grounding; Enforce tool behaviour with existing harness primitives
- Tools: Claude Code, Google Web Grounding for Enterprise, MCP CLI, Kubernetes, Brave Search (native web tool in Claude Code, per speaker)

## [Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan](../videos/32nrHU6zHU8.md)
`32nrHU6zHU8` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: agent-architecture, evals, context-engineering

Navan's chief architect and a colleague argue agent infrastructure is repeating the microservices shift: skills as context units, hook-based tracing, trajectory evals, and tool-call guardrails.

- Techniques: Pre/post tool-call and session hooks for tracing and gating; Trace signals: goal, reasons, belief, tool calls, confidence; Trajectory evaluation; Skills as composable, testable context units; Single master agent with progressively loaded sub-skills; Per-tool-call authorization for on-behalf-of agents; A2A skill contracts across team boundaries
- Tools: AWS AgentCore, OpenTelemetry, Claude Code hooks, MCP, A2A protocol, Braintrust (inferred from auto-caption 'brain trusts')

## [How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face](../videos/FLUoowDJg4I.md)
`FLUoowDJg4I` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: software-factory, agent-architecture, models-research

Hugging Face's Niels Rogge shows how nightly agents open outreach GitHub issues and PRs to move researchers' artifacts onto the Hub, moving from a fixed workflow to an autonomous agent loop.

- Techniques: Deterministic LLM pipeline mirroring the manual process; Cron for overnight background agents; Promote a step to an autonomous loop only where outputs are unpredictable; One container per work item for parallel agents; Skill as a manual trigger that fans out to subagents; Open-model routing through one OpenAI-compatible endpoint; Template completion from source material
- Tools: Claude Agent SDK, Cursor, Modal, GitHub Actions, Langfuse, Hugging Face CLI, Hugging Face inference providers, Slack, Gemini, Claude Code

## [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../videos/Lrw0jqBNaw0.md)
`Lrw0jqBNaw0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, evals, mcp-and-tools

Sourcegraph's agent advocate argues DevRel must now serve AI agents as users and recommenders, and shows how to measure agent friction and recommendation rates.

- Techniques: Agent friction logging from traces; With-and-without-tool agent benchmark; Intent-split GEO prompt experiments; Agent experience report; Machine-readable authoritative content
- Tools: Sourcegraph code navigation MCP tool, CodeScaleBench (speaker's benchmark), llm.txt, MCP registries, Discord

## [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../videos/DrTdD-ttjCY.md)
`DrTdD-ttjCY` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, product-ux, evals

Snowflake's sales-team GTM agent (6,000 users): launch with quality over coverage, stage the rollout, manage activation, and use question logs as the feedback loop.

- Techniques: Question bank as the first eval set; Narrow-scope, high-accuracy launch; Pilot, beta, GA with metric gates; LLM classification of usage logs; Closed loop from logs to content; Agent instructions under version control with tests; Build on a managed agent platform with inherited access control
- Tools: Snowflake Cowork (formerly Snowflake Intelligence), Cortex Analyst, Cortex Search, Snowflake semantic views, MCP connections, Confluence, Jira, Slack, Gmail, Salesforce, Google Docs

## [Agent Frameworks Considered Harmful — Rémi Louf, .txt](../videos/KHudyx5wW3U.md)
`KHudyx5wW3U` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: agent-architecture, context-engineering

Rémi Louf (CEO of .text) on building a small event-driven agent runtime in two weeks: typed events, an append-only log, and content-addressed prompts for auditable, replayable agents.

- Techniques: Markdown-defined agents in a versioned folder; Event-typed agent contracts; Append-only event log with causal ids; Content-addressed prompt assembly; Replay a stored request against another model; Two-boundary enforcement
- Tools: Codex, Slack, Linear, llama.cpp

## [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../videos/bMjlRrWjdT0.md)
`bMjlRrWjdT0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, enterprise-adoption, product-ux

DoorDash GenAI platform team on building a cross-functional AI evals platform: UI-first, then API-first, then workflow-first, so non-engineers can run annotation and judge calibration themselves.

- Techniques: Continuous eval loop; API-first eval platform with vibe-coded UIs; Self-serve judge calibration with prompt optimization; Platform-level model choice for judges
- Tools: Claude Code, Codex, DSPy-style prompt optimizer (transcribed as JEPA), MCP, LLM gateway, agent gateway

## [1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI](../videos/qStB9GbppMU.md)
`qStB9GbppMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: voice-multimodal, evals, security-guardrails

Hamming AI's CEO argues voice agent errors (about 10% in practice) are the top deployment blocker, and offers a loop to find, prioritise, test and red-team failures across many calls.

- Techniques: Frequency and severity triage matrix; Scenario-variation regression testing; Production A/B testing for voice fixes; Cross-conversation pattern analysis; Continuous adversarial red-teaming

## [Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust](../videos/nxokqOq1imY.md)
`nxokqOq1imY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, agent-architecture

Braintrust field CTO argues each agent architecture generation (single call, chain, ReAct loop, graph, product system) needs different evals, and that production traces should keep feeding the eval set.

- Techniques: Architecture-matched eval suites; k-run pass@k and pass^k reporting; Production failure clustering to harvest evals; Node-level and branch-level evals for graph workflows
- Tools: Braintrust, Braintrust Topics

## [DeepSeek Harness Just Changed AI Forever](../videos/DTu4yvmc0Fc.md)
`DTu4yvmc0Fc` · Better Stack · 2026-09-02 · q2 · intro · review · also: agent-architecture, coding-agents

Short hands-on tour of an open-source, plugin-first coding harness built on the Cordis framework, covering swappable models, an append-only trajectory log, and adding plugins by prompt. Hype title, thin on setup.

- Techniques: Add a plugin by prompting inside the harness; Use an append-only trajectory log to audit a run; Swap the model provider through plugin config
- Tools: DeepSeek harness (open-source agent harness, desktop app and TUI), Cordis (plugin framework; name as auto-captioned), DeepSeek V4 Pro (model; named in the video), GLM 5.2 (model used as a comparison point), Claude Sonnet 4.5 (in sample provider config), OpenClaw (named as "open claw" in the video), OpenCode (compared for in-prompt customization), QM (a harness the channel covered earlier, name as spoken)

## [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](../videos/eAXxdtNlK04.md)
`eAXxdtNlK04` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, context-engineering

Langfuse's Annabell Schäfer shows that a clear-cut yes/no target function (single-label paper classification) lets an optimizer loop improve a small model's prompt, and argues teams need domain experts and high-signal evaluators before auto-improvement pays off.

- Techniques: Fit / validate / test split for prompt optimization; Error clustering to drive hypotheses; Binary, criterion-specific judges instead of Likert-style scores; Task markdown as the loop spec
- Tools: Langfuse, Claude Code, GPT-5 Nano, Claude Opus 4.8

## [Build Evals That Actually Matter - Nick Ung & Akshay Sharma, Lyft](../videos/3z2uT5aDx_Y.md)
`3z2uT5aDx_Y` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, enterprise-adoption

Lyft's customer-support agent team on building offline simulation evals, calibrating LLM judges on hand labels, and closing the loop from error analysis to agent changes.

- Techniques: Simulated multi-turn offline eval; Mixed eval dataset from production samples plus mutations; User simulator realism calibration; Binary task-outcome rubric per metric; Judge calibration as a classifier; Confidence intervals and paired comparisons; Annotation queue for domain experts; Config-driven eval harness
- Tools: LangSmith, Langfuse, DeepEval, LangGraph, tau-bench (transcribed as CowBench, from Sierra)

## [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../videos/vSx5IULvBns.md)
`vSx5IULvBns` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, enterprise-adoption

Resolve AI engineer argues production ops, not coding, is the bottleneck, and shows always-on cloud background agents that run on schedules, events and messages, with deployment monitoring as the lead use case.

- Techniques: Trigger-typed background agent; Per-change check plan generated from the diff; Time-bounded watch with agent-chosen duration; Confidence-gated reply with human confirmation; Feedback in the thread edits the standing task; Expose agent capabilities over MCP
- Tools: Slack, Microsoft Teams, GitHub release tags, Kafka, CI/CD pipelines, feature flag systems, MCP servers, Granola

## [Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect](../videos/AQv3qRCG6Gw.md)
`AQv3qRCG6Gw` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, evals

Will Brown (Prime Intellect) on running RL when no verifiable reward exists: manufacture supervision from grounding, judges, production traces and learned simulators, and keep humans on the top-level decisions.

- Techniques: Environment as the shared unit (task + harness + rewards); With/without grounding as a supervision gap; Backward construction from a reachable end state; Trace-seeded task mining; Judge-to-rubric distillation; Pass-rate gated task generation; Learned simulator of an uncontrolled tool or site; Reward-hack corpus and small-run validation
- Tools: Prime Intellect PrimeRL training framework, Prime Intellect verifiers and task sets, Prime Intellect Lab (hosted training and evals), GRPO / REINFORCE policy-gradient methods (named in passing), MCP servers, CLI tools and web apps (as simulator targets)

## [The Model Was Right. The Harness Failed. — Vinoth Govindarajan, OpenAI](../videos/BInpv7lGp1o.md)
`BInpv7lGp1o` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: agent-architecture, security-guardrails

Agent production failures are mostly harness failures, not model failures; the talk gives a state-ownership, ordered-commit, lifecycle, authority and receipt framework, using OpenClaw incidents as case studies.

- Techniques: Session lane / single ordered writer; Run deadlines, cancellation and watchdog; Scoped approval object; Run receipt as the audit record; Idempotency keys on side effects; Verify at the user-visible edge; Five-question production audit
- Tools: OpenClaw, OpenAI Agents SDK, Codex, Cursor, OpenCode, Claude Code, Hermes, Telegram

## [Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest](../videos/0RNNfxpdbQk.md)
`0RNNfxpdbQk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: multi-agent, testing-verification, context-engineering

Pinterest's Drasko Profirovic on Medic, an agentic Spark failure-diagnosis tool, and how its prototype became a multi-agent system with record/playback testing, log and metrics handling, and sub-agents.

- Techniques: Record/playback end-to-end agent harness; Learned red-herring filtering for logs; Metrics as a collaged graph image in a quarantined sub-agent; Supervisor with parallel hypothesis researchers; Per-agent prompt plus MCP tool subset; OpenTelemetry traces as step waterfalls
- Tools: Apache Spark, LangGraph, LangGraph DeepAgents, LangFuse, OpenTelemetry, Model Context Protocol (MCP), Grafana, Airflow, Slack, vector database

## [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../videos/CvRngaQZQ3Y.md)
`CvRngaQZQ3Y` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, training-finetuning-rl, memory

LangChain's Vivek Trivedy argues agent improvement is a data-mining loop: ship, collect traces, mine them, then run data-driven experiments on prompts, tools and models.

- Techniques: Agent-driven trace mining; Frontier-to-open-model downgrade via trace judging; Distillation from good traces; Evals generated from traces; Score-driven auto-research loop; Harness, then fine-tune, then harness sandwich; Human review summaries
- Tools: LangSmith, LangSmith Engine, Deep Agents, Claude Code, Codex, Terminal Bench, scikit-learn

## [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../videos/jHMiYtjoJfA.md)
`jHMiYtjoJfA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, product-ux

Ben Hylak (Raindrop) argues teams should "raise the floor" by finding production agent failures, tracking when they started and how many users they hit, and using code-based classifiers over traces instead of clustering or big eval sets.

- Techniques: Evals as local code tests; Per-issue onset and affected-user tracking; Code-based trace classifiers; Deterministic signal first, agent investigates second; Scale-dependent experimentation
- Tools: Raindrop, Workshop (open-source tracing tool), vitest (vitest evals), howtoeval.com, Sentry (mentioned as a model for issue detection)

## [How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](../videos/xyL2Ltkh-SA.md)
`xyL2Ltkh-SA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, context-engineering

Two YouTube Ads team members on building evals for agents: tools first, intuition before scale, human rater rubrics, reading traces, and pattern-level launch gates.

- Techniques: Tools-first, then critique agent with remediation loop; Intuition-first review before scaled evals; Rubric with examples plus mandatory rater explanations; Negative test cases in the golden set; Judge calibration by sampled agreement monitoring; Trace-based failure diagnosis; Pattern-level metrics with a refreshed test set and online evals; Launch gate defined up front with regression triage

## [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud](../videos/JJGbw4ggaFs.md)
`JJGbw4ggaFs` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, context-engineering, coding-agents

May Walter (HUD) shows how HUD runs a weekly agentic workflow on GitHub Actions with Claude Code that mines production traces, scores performance fixes by ROI, verifies them at runtime, and sends a human-readable report to Slack.

- Techniques: Scheduled agentic investigation with runtime verification; Function-level production context map; Query language plus task skills; ROI and risk scoring with a human-readable gist; Vendor-neutral workflow layer; Targeted automatic checks for known performance smells
- Tools: Claude Code, GitHub Actions, MCP, ClickHouse, Slack

## [From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize](../videos/9HbzAWnKbo4.md)
`9HbzAWnKbo4` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: software-factory, evals, sandboxing-execution

Arize's founder demos Signal, a background agent that reads production traces and logs, drafts an issue or fix with evidence, and hands it to a human reviewer, with the loop run in a sandbox.

- Techniques: Trace-to-file skill; Event- or schedule-triggered agent loop; Composable narrow skills over raw data; Sandbox per run, pluggable harness; Failure-to-evaluator loop
- Tools: Arize AX, Arize Phoenix, Pyroscope, Claude Code, Cursor, Daytona, GitHub, Google Cloud logging skills

## [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](../videos/X1kp-ABIIxQ.md)
`X1kp-ABIIxQ` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, sandboxing-execution, evals

Dan Farrelly (Inngest CTO) argues agent architectures decay fast unless the execution layer (durable state, retries, triggers, tracing) is separated from fast-changing context (prompts, models, tools) and compute (sandboxes).

- Techniques: Three-layer decomposition (execution / context / compute); Externalised durable step state with resume-from-failure; Cron-triggered health check, triage agent, and reviewer loop; Deferred outcome scoring from downstream events; Ephemeral sandboxes with state kept in the orchestrator
- Tools: Inngest

## [The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI](../videos/q2JrUKBMf0w.md)
`q2JrUKBMf0w` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: evals, agent-architecture

Arize's founder argues that evals must add a third layer, agent-as-a-judge, that reads production traces, finds failure patterns, and can open fix PRs. It is a short vendor pitch with little method detail.

- Techniques: Agent-as-a-judge over traces; Three-layer eval stack; Trace-driven online evals; Repeated-tool-call loop detection
- Tools: Arize Signal, Agent as a Judge (Arize)

## [From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI](../videos/Ib5t2RLtxvM.md)
`Ib5t2RLtxvM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, testing-verification, sandboxing-execution

Rustem Feyzkhanov (Snorkel AI) on turning production agent traces into repeatable, containerized simulation benchmarks that serve as release gates and training data.

- Techniques: Trace-to-task conversion; Harbor-style task folder; Oracle-first validation; Sidecar service mocking with a simulated user; Stepwise long-horizon simulation; Layered verifiers with SME escalation; Benchmark CI and difficulty tagging; Coverage split: happy path plus edge cases; Held-out split for agent config
- Tools: Docker, Docker Compose, Harbor (task format), Terminal-bench, SWE-bench, Arize (experiment and trace recording; transcript says 'Arise'), MCP tools

## [Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase](../videos/u1yaOeEX4e8.md)
`u1yaOeEX4e8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: infra-cost-scaling, data-engineering

JPMorgan payments lead on modeling each API request as a short-lived execution DAG, then using per-segment baselines and drift categories to detect anomalies with fewer false alarms.

- Techniques: Request-as-DAG from traces; Tiered detection; Segmented baselines; Drift classification before action; Async telemetry to hot and recon paths; Staged automated remediation; Synthetic training data for detectors
- Tools: OpenTelemetry, Kafka, Neo4j (mentioned as contrast), KL divergence, MMD, EWMA (exponential moving average)

## [Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber](../videos/31GUkCBD-Uc.md)
`31GUkCBD-Uc` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, agent-architecture

Uber's Uber Eats image pipeline (routing, enhancement, publish QA) and how they keep it aligned with human labels through offline evals, auto-tuning and a diagnoser that closes the production feedback loop.

- Techniques: Flat per-run JSON trace across the whole agent chain; Router as a classifier scored by a confusion matrix, with an N-by-N extension; Golden human-label set plus ship gate; Production drift loop: sample, re-label, diagnose, tune, benchmark, register; Reflect-and-synthesize prompt optimizer; Generate-edit-QA loop scored with pass@K; Pairwise judge with yes/no/unsure and product-agreed criteria; Redundant Swiss-cheese final gate; Diagnoser as a routing layer over all feedback; Replay flagged examples before releasing a config; Per-segment production metrics
- Tools: Arize

## [This is basically an X-ray for your codebase...](../videos/Y_7_rbtQXcs.md)
`Y_7_rbtQXcs` · Better Stack · 2026-08-02 · q3 · intro · review · also: coding-agents, evals

Short Better Stack walkthrough of MindWalk v0.3, a 3D session replay for Claude Code and Codex runs, with an LLM judge that grades how the agent explored, stayed in scope and verified its work.

- Techniques: Color-coded session replay of file access; LLM-judge rubric over a whole agent session; Timeline event markers for multi-agent runs; Choose the review lens by change size
- Tools: MindWalk v0.3, Claude Code, Codex, Three.js, Graphify (named as a comparison, not evaluated)

## [OpenAI Went Rogue and Hacked Hugging Face](../videos/iUkgp7kzIxM.md)
`iUkgp7kzIxM` · Better Stack · 2026-08-02 · q3 · intro · news · also: security-guardrails, sandboxing-execution

Better Stack news recap of the Hugging Face intrusion that OpenAI said came from its unreleased model escaping an internal cyber eval, plus HF's AI-assisted forensics and practical takeaways.

- Techniques: Lock down the eval egress path; Run cyber evals with classifiers off, but isolated; LLM triage over security telemetry; Self-host an open-weight model for forensics; Credential hygiene after a platform incident
- Tools: ExploitGym (OpenAI internal cyber eval), GPT 5.6 Sol, GLM 5.2 (Z.ai open-weight model, self-hosted by Hugging Face), Hugging Face (Spaces, datasets pipeline)

## [Agents Building Agents - Alfonso Graziano, Nearform](../videos/aHhB3sjGjkI.md)
`aHhB3sjGjkI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, skills-self-improvement, coding-agents

Alfonso Graziano (Nearform) shows coding agents improving other agents: an eval-driven loop lifts a toy agent from 18% to 83% and a production agent from 67% to 86%, and a trace-clustering loop turns live user feedback into fixes.

- Techniques: Golden dataset plus scorers as the agent test suite; Baseline report before the optimization loop; Branch-per-hypothesis improvement loop with rollback; Protected eval set in the optimizer instructions; Reading the agent's full traces, including thinking traces, for root cause; Trace clustering from live feedback; Packaging the analysis as a reusable skill; Failure mode to spec to golden-set entry
- Tools: Claude Code, Mastra, auto-agent (the speaker's own internal tool, not public)

## [Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc](../videos/RGiXcVxSD3s.md)
`RGiXcVxSD3s` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: product-ux, agent-architecture, skills-self-improvement

Vertical AI talk by the Filed CTO arguing chat and citations are not enough; products should be built for delegating long-running work to agents, with skills, traces, pause-and-intervene and plan approval.

- Techniques: Delegation-first task selection; Implicit skill capture from usage; Per-value trace-back for trust; Pause-and-tag intervention; Plan approval gate for irreversible actions
- Tools: Wispr Flow

## [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](../videos/Akm1sqvWG4A.md)
`Akm1sqvWG4A` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: rag-retrieval, data-engineering, security-guardrails

Abed Matini (Ogilvy) shows a local, framework-free RAG FAQ bot: Docling to Markdown, structure-aware chunking, hybrid BM25 plus vector search fused with RRF, Python guardrails, and Langfuse telemetry.

- Techniques: Markdown-first ingestion with Docling; Per-document chunking strategy selection in admin; Q&A-shaped chunks for FAQ content; Hybrid retrieval with RRF fusion in Python; Deterministic functions instead of agent loops; Pre-LLM guardrail layer with rigid tests; Per-conversation telemetry with self-hosted Langfuse; Two-model local stack in Docker
- Tools: Docling, Python, FastAPI, React, PostgreSQL, Docker, Ollama, Qwen2.5, BGE-M3, Langfuse, GitHub Codespaces

## [The Log Is The Agent - Ishaan Sehgal, Omnara](../videos/UPwGaM2MKHY.md)
`UPwGaM2MKHY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, context-engineering

Argues an agent's identity is its append-only event log, not the model or runtime; once workers are disposable, reliability, forking, sharing and ownership follow from the log design.

- Techniques: Log-first agent loop; Persist pending permissions as events; Projections over one record; Compaction as forked log; Fork at a point in the log; Share by access grant, not transcript copy
- Tools: Claude Code, Codex, OpenCode, Claude SDK, Cloudflare Durable Objects, SQLite, JSONL

## [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../videos/ObTPqBGsEbA.md)
`ObTPqBGsEbA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: evals, enterprise-adoption, governance-compliance

A five-pillar playbook (evaluation, tracing, data foundation, orchestration, governance) for taking enterprise AI agents to production, illustrated with a retail banking chatbot case study.

- Techniques: Business-metric eval spec before build; Living golden eval set seeded from human answers; Three-layer eval stack; Automated eval pipeline with human review threshold; Trace-driven duplicate-call detection and retry cap; Tiered CI eval runs; Prompt versioning as change management; Model selection on your own eval set; Incident playbook: detect, diagnose, contain, fix, regress
- Tools: Databricks, MLflow, Delta Lake, Apache Spark, Unity Catalog, Genie, Agent Bricks, Databricks Apps, Mosaic AI, Git, Python, LLM-as-judge

## [Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs](../videos/vljxQZfJ9wY.md)
`vljxQZfJ9wY` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: evals, agent-architecture

Nishant Gupta (Meta Superintelligence Labs) argues agent evals must score workflow behavior from production telemetry, not model answers or benchmarks, and should run continuously as a control-plane function.

- Techniques: Scenario-driven offline evals; Production telemetry as the eval set; Targeted human review to calibrate automated evals; Continuous evaluation loop; Agent tracing like distributed tracing; Evaluation as a control plane

## [Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](../videos/Lc8zRh9muoY.md)
`Lc8zRh9muoY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, agent-architecture

Microsoft's Chronicle PoC records each agent node's inputs and outputs as a replayable trace, so production failures can be debugged and turned into offline tests. The talk argues for replayability rather than chasing bitwise determinism.

- Techniques: Boundary-annotated run recording; Record at the node boundary, not the network; Replay with selective stubbing plus assertions; Zero-model-call deterministic tests from traces; Guardrails at the tool boundary; Keep generation variance on
- Tools: Chronicle (Microsoft proof of concept; code link shown by QR code, URL not spoken)

## [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](../videos/WLXxTaPagA8.md)
`WLXxTaPagA8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, evals, multi-agent

Solo agent builders keep rebuilding CI/CD-style controls (regression tests, alerts, contracts, staging, audit trails) one failure at a time; the talk argues for blocking gates at the most expensive handoff.

- Techniques: Boring blocking gates before save; Guarded vs naive mode demo; Handoff mapping; Per-gate audit record; Voice and domain contracts as explicit rules
- Tools: Claude Code

## [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](../videos/pSto5YaNGUo.md)
`pSto5YaNGUo` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: evals, software-factory, agent-architecture

Mutagent's CEO and CTO argue agents should be built and improved in an agentic loop: an offline eval-and-optimize loop plus an online trace-diagnose loop, with a demo of their research-preview evaluator and diagnose agents.

- Techniques: Spec-first agent definition; Eval-driven development as TDD for agents; Binary criteria with calibrated LLM judges; Trajectory-level evaluation; Failure-mode library with code-checkable indicators; Tiered trace sampling; Auto-research style optimization gated by evals; Orchestrator dispatching evaluator and diagnose subagents from a coding harness; Diagnostic report with assumptions block and human decisions
- Tools: Claude Code, Codex, Deep Agents (mentioned as a framework), Hermes (mentioned as a framework), Whisper Flow (speech-to-text for feedback), Tracing platform (auto-caption reads 'length use'; name unclear)

## [Your Agents Need a Save Button - Hamza Tahir, ZenML](../videos/bZISsg7H7DA.md)
`bZISsg7H7DA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, evals

Hamza Tahir (ZenML) argues agents need checkpointed runtime state so production runs can be replayed with what-if changes (model swap, mocked tool), compared across cohorts, and shipped only after cohort-level diffs.

- Techniques: Per-step checkpointing of agent state; Counterfactual replay from a checkpoint; Side-by-side run diffing; Cohort replay with agent-driven analysis; Replay-based ship gate
- Tools: Kitaru, OpenTelemetry, GPT-5 Nano

## [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](../videos/kZsf_Sfm7RU.md)
`kZsf_Sfm7RU` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: pr-code-review, evals, multi-agent

Shipping an agent is where the real work starts. Raphael Kalandadze shows a post-launch loop: a log-monitor agent opens PRs, a fresh-context review agent critiques them, and a session analyzer scores every conversation for health.

- Techniques: Hourly log-monitor agent that opens PRs; Fresh-context review agent as a PR gate; Session analyzer for health scoring; Computer-use QA agent with a site-specific skill; Meta-harness: connect all context to the monitoring agents
- Tools: Claude Code, Codex, HTML artifacts, log and trajectory store, browser computer-use agent

## [The Pipeline Is Dead - Iris ten Teije, Sky Valley Ambient Computing](../videos/bRnoEpoK5m4.md)
`bRnoEpoK5m4` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: product-ux, agent-architecture

Argues the one-version-for-everyone software pipeline ends as code gets cheap; proposes a canonical stem with per-user, bounded, reversible divergences and names the hard problems: provenance, testing, measurement, trust, coordination.

- Techniques: Stem plus bounded, reversible divergences; Developer-declared adaptation boundaries; Behavior-driven personalization with a spirit-of-the-software check; Traceable adaptation provenance; Goal-metric gating for changes; Recommend-first autonomy as a trust ladder; Coordination by intent and outcome

## [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](../videos/APh1Vx0oLmQ.md)
`APh1Vx0oLmQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: agent-architecture, security-guardrails, infra-cost-scaling

Nishant Gupta (Meta Superintelligence Labs) argues that agent reliability is an infrastructure problem: treat models as probabilistic, keep the platform deterministic, and let infrastructure validate and enforce what the model proposes.

- Techniques: Propose, validate, enforce split; Tool isolation with circuit breakers; Controlled recovery instead of open retries; Decision-chain tracing; Per-agent limits and cost quotas; Layered defence for agent actions; Humans as exception handlers

## [I Turned Cheap Cloud Storage Into a 1PB Local Drive (With JuiceFS)](../videos/ZoBEQWxosGg.md)
`ZoBEQWxosGg` · Better Stack · 2026-07-02 · q3 · intro · tutorial · also: dev-tools, infra-cost-scaling

Walkthrough of JuiceFS, a POSIX file system that stores data in cheap S3-style object storage with metadata in Redis and a local SSD cache, plus wiring its Prometheus metrics into Better Stack.

- Techniques: JuiceFS volume with Redis metadata and S3 data; Cold vs warm read benchmark with dd; Scraping JuiceFS metrics into a hosted dashboard
- Tools: JuiceFS, Redis, PostgreSQL, TiKV, Amazon S3, Google Cloud Storage, Backblaze B2, Docker, macFUSE, dd, ngrok, Prometheus

## [Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse](../videos/vNCY9kXXyDQ.md)
`vNCY9kXXyDQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: skills-self-improvement, evals, claude-code

Langfuse's founder explains how they built an installable skill that teaches coding agents to add Langfuse tracing and evals, and what they learned about docs, eval checks and auto-tuning skills.

- Techniques: Skill with progressive disclosure; Agent-facing docs surface; Wrap the API as a CLI and advertise --help; Natural-language checks for skill evals; Auto-research loop on a skill with human review; Timestamped skill copies for staleness
- Tools: Claude Code, Langfuse, OpenAI SDK

## [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../videos/KA5kPbdkK2E.md)
`KA5kPbdkK2E` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: skills-self-improvement, evals, vibe-coding-app-building

Benjamin Verbeek (Lovable) on two continuous-learning loops: a self-updating "Stack Overflow" of fixes for stuck users, and an agent "vent" tool that reports platform friction to engineers.

- Techniques: Stuck-session detection with an LLM judge; Clustered, generalised fix knowledge bank; Blank-injection holdout; Tuned agent vent tool; Agent triage of agent feedback; Feedback volume as an incident detector
- Tools: Slack, Framer Motion

## [The maturity phases of running evals — Phil Hetzel, Braintrust](../videos/FB-MLPhL9Ms.md)
`FB-MLPhL9Ms` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: evals, testing-verification

Phil Hetzel (Braintrust) lays out four maturity stages of agent evals, from documented vibe checks to replaying tool-using agents offline with captured system state.

- Techniques: Documented human annotation (thumbs plus justification); Failure-mode extraction from justifications; LLM-as-judge with binary outputs and human-aligned ground truth; Deterministic code scorers for objective failures; Production trace flywheel; Whole-trace evaluation with per-step targeting; Embedding system state in traces and time-versioned queries
- Tools: Braintrust, Cursor, Claude Code, Codex

## [What if the network was the sandbox? — Remy Guercio, Tailscale](../videos/BM2JX9hqsVQ.md)
`BM2JX9hqsVQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: sandboxing-execution, security-guardrails, governance-compliance

Tailscale's Remy Guercio argues the network layer can act as an agent sandbox: identity-tagged WireGuard connections let an LLM gateway hold the provider key so the sandbox never has one, and every model call and tool call is visible and cuttable there.

- Techniques: Zero-key sandbox behind an identity-aware gateway; Per-identity budgets and quotas across providers; Per-tool-call webhooks for external policy; Identity-aware internal services with tsnet; Policy as code for network identity
- Tools: Tailscale, WireGuard, Aperture, tsnet, Claude Code, Codex, Gemini CLI, GitHub Actions, Opus 4.6

## [What Breaks When You Build AI Under Sovereignty Constraints - Bilge Yücel, deepset GmbH](../videos/x2bH0RKPgdc.md)
`x2bH0RKPgdc` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: governance-compliance, security-guardrails, mcp-and-tools

Bilge Yücel (deepset) on building AI under sovereignty constraints: four pillars, what breaks when you move from frontier APIs to self-hosted, and a guardrail-agent-guardrail reference design built on Haystack.

- Techniques: Sovereignty checklist as a design gate; Safe/unsafe router as an input guardrail; Per-agent tool allowlist plus BM25 tool search; Per-tool human confirmation strategies; Pipeline serialized to YAML for version control; Tracer component wrapping the pipeline
- Tools: Haystack, MCP, BM25, OpenTelemetry, YAML, Kubernetes, Mistral, Google models, Nvidia models, Jina

## [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](../videos/zMiSRliEzv4.md)
`zMiSRliEzv4` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: software-factory, agent-architecture, evals

PostHog's Joshua Snyder describes a pipeline that turns product signals (errors, replays, Slack, experiments) into grouped reports, runs a Claude Agent SDK research agent in sandboxes, and opens PRs that are iterated until green.

- Techniques: Generate queries from a signal, then embed the queries; Safety classifier at the ingestion edge; Weighted report promotion with a threshold; Three-way actionability gate; Snapshot and rehydrate the sandbox for CI and review loops; Distill repeated agent behavior into a one-shot call; Evaluate on production-representative data
- Tools: Claude Agent SDK, Modal, MCP, Linear, Notion, Sentry, git blame, PostHog, feature flags

## [LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](../videos/JsCCrBF7F1g.md)
`JsCCrBF7F1g` · AI Engineer · 2026-06-18 · q2 · practitioner · talk · also: evals, agent-architecture

Arize's Dat Ngo argues LLM observability, evals and experiments form one flywheel, built on OpenTelemetry traces, with evals scoped from single spans up to whole sessions. It is mostly a product walkthrough with a useful eval taxonomy.

- Techniques: OTel auto-instrumentation for agents; Session-level state tracking; Distributional trajectory analysis; Eval at the smallest scope that answers the question; Deterministic checks before LLM judges; Calibrate an LLM judge against a golden dataset; Trace-to-dataset-to-experiment loop; Coding-agent access to the eval platform
- Tools: Arize Phoenix, Arize AX, OpenTelemetry, LLM-as-judge, Claude Code, Codex, Anthropic Managed Agents (mentioned)

## [How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust](../videos/XBaznoTRDFI.md)
`XBaznoTRDFI` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: evals, data-engineering

Braintrust's solutions lead argues agent observability differs from uptime-focused tracing: quality, non-determinism, huge text-heavy traces, and domain experts in the loop.

- Techniques: Split quality metrics from technical metrics; Full-text index on traces with SQL access; Trace to offline dataset to experiment; Human grades with justification to LLM judges; Embed and cluster traces to find unknown unknowns
- Tools: Braintrust, Grafana, Datadog, ClickHouse, Tantivy, Apache Lucene, SQL, CLI

## [Developers Finally Got an Open-Source Voice AI Platform (Dograh)](../videos/xD9JEvfCH9k.md)
`xD9JEvfCH9k` · Better Stack · 2026-06-02 · q3 · intro · review · also: voice-multimodal, infra-cost-scaling

Short hands-on look at Dograh, a self-hostable open-source voice agent platform with a visual workflow builder, per-call traces and recordings, as an alternative to hosted tools like Vapi.

- Techniques: Local spin-up of a self-hosted voice agent stack; Lead-qualification voice flow as a node graph; Per-call debugging via transcript, trace and recording; Swap providers at the runtime layer
- Tools: Dograh, Docker Compose, Git, Vapi, Bland, Retell, Pipecat, Vocode, LiveKit

## [Claude Code + Better Stack: The Only Error Debugging Setup You Need](../videos/u2tqAXKkb4c.md)
`u2tqAXKkb4c` · Better Stack · 2026-06-02 · q2 · intro · tutorial · also: mcp-and-tools, claude-code

Better Stack demo of triaging a live React frontend error from the terminal: Claude Code pulls error data through the Better Stack MCP server, opens a fix PR, then resolves the issue. Short, vendor-led.

- Techniques: MCP-backed error triage loop; Deferred tool loading for MCP servers; Frontend error capture with a vendor DSN and an agent setup prompt; Scheduled error-triage routine
- Tools: Claude Code, Better Stack (error tracking, session replay, MCP server), Sentry React SDK, Telegram, WhatsApp, email

## [Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw](../videos/4VhbYlfC7Gs.md)
`4VhbYlfC7Gs` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: evals, agent-architecture

Vincent Koc (Comet, OpenClaw) argues static, hand-written evals don't fit adaptive agents; he proposes intent-based, always-on evals self-curated from traces, with the eval suite treated as living code.

- Techniques: Intent-defined end-state evals; Trace-driven suite self-curation; Always-on eval service; Telemetry-aware harness; Split static and dynamic evals
- Tools: Comet, OpenClaw, Claude, Codex, MCP, Karpathy autoresearch

## [Shipping complex AI applications — Braintrust & Trainline](../videos/ZdheJTfLu-s.md)
`ZdheJTfLu-s` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: evals, agent-architecture

Hands-on Braintrust and Trainline workshop on taking a multi-stage LLM support-triage agent from one prompt to a traced, evaluated, managed and failure-driven production loop.

- Techniques: Staged agent pipeline with a deterministic front end; Nested tracing per user interaction; Golden set from categorized edge cases; Two-tier scoring; Evaluate before swapping models; Failure-to-fix loop; Prompts and scorers as managed, slugged assets
- Tools: Braintrust, OpenAI SDK, OpenAI mini model (speaker says 'mini'), TypeScript, pnpm, make, Node 22, Cursor / Codex (suggested for setup)

## [Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop](../videos/-aM2EDTiaMs.md)
`-aM2EDTiaMs` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: evals, agent-architecture, coding-agents

Raindrop's founders argue production agent monitoring must replace evals as the main safety net, using implicit classifier signals, regex, ship-vs-control experiments, and agent self-diagnostic reports.

- Techniques: Binary issue classifiers as monitoring signals; Regex keyword signals on user messages; Percentage rollout with a control group, judged by signal rates; Self-diagnostic report tool; Natural-language signal definition (deep search); Daily triage agent over signals; Cluster by user intent and track issue rate per cluster; Trajectory search over tool-call sequences
- Tools: Raindrop, OpenTelemetry, Claude Code, Codex, OpenAI API, Sentry, Slack, BigQuery, Snowflake, Statsig

## [Why building eval platforms is hard — Phil Hetzel, Braintrust](../videos/_fQ7Z_Wfouk.md)
`_fQ7Z_Wfouk` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: evals, data-engineering

Braintrust's Phil Hetzel on why eval platforms are a systems problem: the maturity path from spreadsheets to tracing plus online evals, and why agent traces break ordinary data stacks.

- Techniques: Spreadsheet plus for-loop eval starter; Playground for non-technical experimentation; Failure-mode-driven scoring functions; Online evals on the trace stream; Production-to-offline loop; Topic modeling over traces; Automatic tracing through an AI proxy or gateway
- Tools: Braintrust, Postgres, Neon, DuckDB, Google Sheets

## [Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft](../videos/iOXM3zE-2dk.md)
`iOXM3zE-2dk` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: evals, security-guardrails, coding-agents

Microsoft Foundry workshop on agent observability: trace-linked evals, stage-wise agent evaluators, OTel tracing, red teaming, and an observe skill that automates the eval-optimize loop with a human stopping regressions.

- Techniques: Trace-linked evaluation; Stage-wise agent evaluators; Bootstrapped eval dataset from instructions; Version-compare regression diff; Bounded auto-optimization with human stop; Adversarial red teaming with an attacker agent; OTel GenAI tracing with custom attributes; Eval gate on model swap
- Tools: Microsoft Foundry, Azure Monitor, Application Insights, OpenTelemetry, GitHub Codespaces, dev containers, GitHub Copilot Chat, Foundry MCP server, Azure AI Toolkit (VS Code extension), LangGraph, KQL, PyRIT (auto-caption reads it as 'pirate')

## [Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate](../videos/vi-2nasppAg.md)
`vi-2nasppAg` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: agent-architecture, multi-agent, sandboxing-execution

Iterate's workshop on building event-sourced agent harnesses as stream processors: pure reducers for state, side effects after append, pause-based circuit breakers. Live demos mostly failed; the design ideas are the value.

- Techniques: Event-sourced agent log; Reducer plus after-append split; Pause-event circuit breaker; Deferred enrichment with a time budget; Child paths for sub-agents; Secret substitution at fetch time
- Tools: events.iterate.com (event service), Cloudflare dynamic workers, OpenAI SDK (Responses API), Zod, Pi, Claude, OpenCode, Convex, Kafka, Cursor, OpenClaw, Electric SQL

## [Feedback Loops are All You Need — Mehedi Hassan, Granola](../videos/ON5LIT0M4do.md)
`ON5LIT0M4do` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: product-ux, testing-verification

Granola's Mehdi Hassan argues that shipping LLM features needs your own tracing, per-PR web previews, and fast feedback loops, not better one-shot prompts.

- Techniques: Home-built LLM tracing store with an internal UI; Web-shell preview per PR; Agent self-verification with screenshot evidence; Own the web search path
- Tools: Electron, Cursor, AI SDK, CloudWatch, OpenTelemetry, Tauri, Figma

## [Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic](../videos/A48uhxfxbsM.md)
`A48uhxfxbsM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: evals, context-engineering

Samuel Colvin (Pydantic) live-demos optimizing a structured-output extraction prompt with GEPA against a golden dataset, then serving managed prompt variables from Logfire without redeploying. Main takeaway: deterministic golden-set evals plus automated prompt search help most for cheaper models and private data.

- Techniques: Golden-dataset structured-output eval with a custom deterministic evaluator; Compare-two-runs error analysis; GEPA prompt search with an expert-prompt-engineer proposer; Keyed-component optimization instead of free-form prompt rewrites; Typed managed variables for live prompt and config changes; Trace the optimizer itself; Train/eval split with extra coverage
- Tools: Pydantic AI, Pydantic Logfire, GEPA (called JEPA in captions), DSPy, OpenFeature, Beautiful Soup, FastAPI, Pydantic AI Gateway, uv

## [Fighting AI with AI — Lawrence Jones, Incident](../videos/L2r6vLlLgs8.md)
`L2r6vLlLgs8` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: evals, coding-agents, multi-agent

Lawrence Jones (Incident.io) on using AI tools to debug and improve multi-prompt AI systems: export UI traces and eval suites as file systems for coding agents, then run parallel backtest analysis pipelines.

- Techniques: Eval-tool CLI for agents; Runbook-driven prompt fix; Download trace or interaction as a file tree; Parallel per-item analysis with file-based resume; Cohort clustering over failures; Analysis as a repeatable markdown playbook; Investigate, fix, then verify in one session
- Tools: Claude Code, Codex, Go, YAML

## [Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize](../videos/Xfl50508LZM.md)
`Xfl50508LZM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: evals, agent-architecture

A two-hour Arize Phoenix workshop on evaluating a Claude-powered financial research agent: read traces first, then write code evals, LLM judges, meta-evals and experiments.

- Techniques: Root-span code eval; Faithfulness eval using the research step as context; Classification LLM judge with a binary label; Trace-to-dataset failure loop; Wrap multi-turn agent runs in one parent span; Golden set with a held-out split and reference solutions; Pairwise comparison and reliability metrics; Cost-normalized accuracy and tiered models
- Tools: Arize Phoenix (Phoenix Cloud), OpenInference instrumentation, OpenTelemetry (phoenix.otel register, auto_instrument), Claude Agent SDK, Claude Haiku (agent model), Claude Sonnet (judge model), Phoenix evaluators (correctness, faithfulness, classification), Phoenix datasets and experiments, Arize AX (enterprise product, mentioned)

## [The Open-Source Alternative to Tableau and Power BI (ReDash)](../videos/ouKwtFoT1ZY.md)
`ouKwtFoT1ZY` · Better Stack · 2026-05-02 · q2 · intro · review · also: dev-tools

Short Better Stack overview of Redash, a self-hosted, open-source SQL editor and dashboard builder, with a quick demo of query, chart, dashboard, and scheduled refresh, and a frank list of trade-offs against Metabase, Superset, Tableau and Power BI.

- Techniques: Self-host Redash with Docker; Query, chart, parameter, dashboard flow; Scheduled dashboard refresh; Joining API data with database queries
- Tools: Redash, Docker, Docker Compose, PostgreSQL, MySQL, BigQuery, Snowflake, MongoDB, Metabase, Apache Superset, Tableau, Power BI

## [The Fastest Way to Debug Docker Containers (Dozzle)](../videos/cyNv7UzNaU4.md)
`cyNv7UzNaU4` · Better Stack · 2026-03-02 · q2 · intro · review · also: dev-tools

A short walkthrough of Dozzle, a lightweight open-source live log viewer for Docker and Kubernetes that streams container logs to the browser without storing them; v10 adds alerts, webhooks and DuckDB-based SQL queries.

- Techniques: Live container log tail in the browser; Compose service for a live log viewer; Lock down before exposing beyond localhost; Log alerts to a webhook (v10)
- Tools: Dozzle (v10 cited), Docker, Docker Compose, Docker Swarm, Kubernetes, Helm, DuckDB, Slack (webhook target)

## [How AI Will Transform DevOps and SRE Practices | Better Stack Podcast Ep. 12](../videos/K7y8ZAHQYGY.md)
`K7y8ZAHQYGY` · Better Stack · 2026-03-02 · q3 · practitioner · interview · also: software-factory, dev-tools

Better Stack podcast with SRE consultant Amin Astani on how AI-written code floods CI/CD and on-call, arguing for SLOs, constrained automation and reliability incentives over AI-run production changes.

- Techniques: Error-budget decision test for SLO maturity; Compensatory automation split for production changes; Agentic first-pass alert triage with human escalation; Release-path check before scaling AI code output; Postmortem framing beyond human error; Operational excellence in performance criteria; Self-hosted CI with Concourse
- Tools: Kubernetes, Prometheus, OpenTelemetry, Claude Code (captioned as 'Cloud Code'), incident.io, Honeycomb, Scuba (Meta internal observability tool), Conveyor (Meta internal CD system), Concourse CI, Jenkins, GitHub, Nagios

## [xAI Dropped Grok-4.1… and It’s Actually SCARY Good](../videos/kRQgww49C90.md)
`kRQgww49C90` · Better Stack · 2026-01-02 · q2 · intro · news · also: models-research, mcp-and-tools

Better Stack recap of xAI's Grok 4.1 beta and Grok 4.1 Fast API (Nov 2025): emotional intelligence, lower hallucinations, a 2M-context tool-calling model, and a dummy-log SRE demo. Mostly restates vendor claims.

- Techniques: Agent-side log triage prompt on a fast tool-calling model; Server-side tools inside one model call (Agent Tools API)
- Tools: Grok 4.1 (beta), Grok 4.1 Fast, Grok 4.1 Thinking / non-thinking, Grok 4, Grok 5 (expected Q1 2026, not released), Agent Tools API, xAI X search (xSearch), Grok.com, Gemini 3.0, LM Arena leaderboard, EQBench, Creative Writing v3 benchmark

## [OpenTelemetry Collector - Explanation & Setup](../videos/4ACQhkJBKyA.md)
`4ACQhkJBKyA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: infra-cost-scaling, dev-tools

Beginner tutorial on the OpenTelemetry Collector: receivers, processors and exporters, why to put it between apps and an observability backend, and a Docker setup that adds host and self-metrics and ships data to Better Stack.

- Techniques: Minimal collector config.yaml with OTLP in, batch, OTLP out; Per-signal pipelines with different processors; Adding a backend source token with the attributes processor; Host and self-metrics via receivers
- Tools: OpenTelemetry Collector, OpenTelemetry SDK (Node.js), OTLP (OpenTelemetry Protocol), Docker, Better Stack, Prometheus, Prometheus Remote Write exporter, Jaeger, Zipkin, VS Code, hostmetrics receiver, batch processor

## [SLAs, SLOs, and SLIs EXPLAINED in 7 Minutes (2025)](../videos/pouVbehfnqQ.md)
`pouVbehfnqQ` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: infra-cost-scaling

Beginner explainer distinguishing SLAs (customer contracts with penalties), SLOs (internal targets) and SLIs (measured metrics), using a rice-farmer analogy and AWS EC2 uptime math. Main takeaway: derive SLOs from measured SLIs and monitor your own services rather than trusting vendor status pages.

- Techniques: Derive the SLO from measured SLI history; Keep the internal SLO stricter than the external SLA; Turn an uptime percentage into a minute budget; Monitor your own endpoints, not only the vendor status page
- Tools: AWS, Amazon EC2

## [OpenTelemetry Sampling with Go - Simplify Chaos and Get Better Insights](../videos/WtX3Nlnjffs.md)
`WtX3Nlnjffs` · Better Stack · 2025-11-02 · q2 · practitioner · tutorial · also: infra-cost-scaling, dev-tools

Walkthrough of OpenTelemetry sampling for logs and traces in a local Go app: collector probabilistic sampling, SDK trace samplers, and tail-based sampling with error and probabilistic policies.

- Techniques: Probabilistic log sampling in the collector; Consistent sampling across multiple collectors; Trace-correlated logs in a Go app; SDK head-based trace sampling; Collector probabilistic trace sampling; Tail-based trace sampling with policies; Error-only policy with context; Memory guard for tail sampling
- Tools: OpenTelemetry Collector, OpenTelemetry Go SDK (traces, logs), OTel slog bridge (Go log/slog), OTLP exporter, Probabilistic sampling processor (logs and traces), Tail sampling processor, Memory limiter processor, Go, FNV hash, Better Stack (sponsor, logs UI)

## [Traces vs Spans Explained (with real examples)](../videos/A-nbuPugjxo.md)
`A-nbuPugjxo` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

Beginner primer on distributed tracing: a trace is one request's whole journey, spans are the units of work inside it, and the common mistake is starting new traces instead of child spans.

- Techniques: One trace per inbound request, one span per operation; Propagate trace context into every outbound call; Instrument selectively; Audit for disconnected traces; Read the trace graph and span tree in Jaeger
- Tools: Jaeger, OpenTelemetry (documentation referenced; no version stated)

## [Python Logging Made EASY with Loguru](../videos/y8qLhov8QU8.md)
`y8qLhov8QU8` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

Tutorial on Python logging with the loguru package: one-import setup, reconfiguring sinks and levels, context binding, exception capture, JSON and file output, and shipping logs to Better Stack.

- Techniques: Reconfigure loguru with remove() and add(); Add contextual fields with bind() or contextualize(); Capture exceptions with logger.catch(); Switch to JSON output with serialize=True; Write to a rotated file sink; Send logs to Better Stack alongside the console
- Tools: loguru, Python, pip, Better Stack (Logtail), LogtailHandler (logtail Python package), sys.stderr

## [DNS Malware Explained: How Hackers Hide Code in Plain Sight](../videos/66EG2a81_rE.md)
`66EG2a81_rE` · Better Stack · 2025-11-02 · q3 · intro · review · also: security-guardrails

Short Better Stack explainer on attackers hiding malware and prompt-injection text in DNS TXT records, why encrypted DNS makes this harder to see, and what DNS monitoring to add.

- Techniques: Alert on DNS TXT query volume per host; Run your own DNS resolver for visibility; Ship resolver logs to a log platform and search for patterns; Block known-bad domains with threat-intel lists
- Tools: DNSDB Scout, Cloudflare, Better Stack, DNS over HTTPS (DoH), DNS over TLS (DoT)

## [Semantic Conventions - The SECRET to Crystal Clear Telemetry Data](../videos/ckcbPgZb3TU.md)
`ckcbPgZb3TU` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: dev-tools

Better Stack walkthrough of OpenTelemetry semantic conventions: renaming tracers, spans, metrics and events in a small Node/Hono dice app, and keeping existing logs aligned with ECS via Vector.

- Techniques: Name tracers after the instrumentation scope; HTTP server span with semconv names; Use the standard HTTP duration metric; Format event names like attribute names; Check stability before adopting an attribute; Normalize existing logs with Vector instead of rewriting them; Use ECS as the log field reference for now
- Tools: OpenTelemetry semantic conventions, OpenTelemetry Node SDK, OpenTelemetry Logs SDK, Hono (TypeScript web framework), TypeScript, Node.js, Elastic Common Schema (ECS), Vector, Better Stack, Prometheus, PostgreSQL, Nginx

## [Add an Uptime Badge to ANY Website](../videos/r43TKZspxzo.md)
`r43TKZspxzo` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

Better Stack walkthrough: set up uptime monitors and a status page, then build a custom status badge in Next.js that reads monitor-group status from the Better Stack API.

- Techniques: Server-side fetch of a status API; Derive a status label from monitor counts; Discover IDs from API example requests; Env config for badge; Escalation policy on uptime monitors
- Tools: Better Stack (uptime monitors, status pages, API tokens, monitor groups API), Next.js (server components), React, Tailwind CSS, curl, jq, Nextforge (Next.js template that includes a Better Stack system status component; plugged, no version given)

## [Portainer will CHANGE the way you use Docker!](../videos/CelLibFSDoo.md)
`CelLibFSDoo` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

Quick tour of four self-hosted Docker web UIs (Portainer, Dockge, Dozzle, Yacht) with a verdict: Portainer for general container management, Dozzle for log viewing, avoid Yacht; includes a Better Stack sponsor read.

- Techniques: Run Portainer CE as a container for a web UI; Install Dockge with extra Docker Desktop directories; Merged multi-container logs in Dozzle
- Tools: Portainer (Community Edition), Docker, Docker Desktop, Docker Compose, Dockge, Dozzle, Yacht, Uptime Kuma, Nginx (sample Compose app in Dockge demo), Vector, Better Stack, AWS EC2

## [This Framework Replaces Your ENTIRE Backend (Motia)](../videos/xvwY4ZKklrc.md)
`xvwY4ZKklrc` · Better Stack · 2025-11-02 · q3 · intro · review · also: agent-architecture, dev-tools

Better Stack walks through Motia, a framework that runs APIs, cron jobs, background tasks and AI steps in one runtime built from small "step" files, and demos a four-step tweet pipeline.

- Techniques: One file per step (config + handler); Event chaining between steps; Cron polling of pending work in shared state; Trace-ID-keyed status endpoint; Manual triggering from the dashboard or curl
- Tools: Motia, OpenAI GPT-4, Bluesky, Better Stack, TypeScript, Python, curl

## [Vector vs OpenTelemetry Collector - The Ultimate Observability Showdown](../videos/uRA7qee4Frg.md)
`uRA7qee4Frg` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: dev-tools

Hands-on comparison of Vector and the OpenTelemetry Collector on three tasks: nginx log structuring, Docker metrics to Prometheus, and traces to Jaeger. Vector wins logs and metrics; OTel handles traces better but is harder to set up.

- Techniques: Vector nginx log structuring; OTel Collector nginx log parsing; Docker metrics to Prometheus via OTel Collector; Docker metrics to Prometheus via Vector; Traces to Jaeger via OTel Collector
- Tools: Vector, Vector Remap Language (VRL), OpenTelemetry Collector, Docker, Docker Compose, Nginx, Prometheus, Jaeger, telemetry-gen (OpenTelemetry telemetry generator), Better Stack, Datadog Agent (mentioned only as a hypothetical source), OTLP

## [10 Chrome DevTools Tricks You Didn't Know! (3rd is Crazy)](../videos/EAxdMoyKf5Y.md)
`EAxdMoyKf5Y` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

A 7-minute, beginner-level tour of ten Chrome DevTools tricks: local overrides, keyboard shortcuts, focus emulation, node screenshots, the animation editor, network throttling, styled console logs and AI assistance.

- Techniques: Persist page edits with local overrides; Keyboard navigation of DevTools; Keep focus-dependent UI open for inspection; Capture screenshots from DevTools; Edit CSS animations in the Animations panel; Simulate slow networks; Style console output with %c; Ask the built-in AI assistant
- Tools: Chrome DevTools, Chrome, Google Docs, ChatGPT (mentioned in passing as a comparison)

## [Jsonnet & Grafonnet: Automate & Scale Grafana Dashboards Like a PRO](../videos/u6git2AjoEo.md)
`u6git2AjoEo` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

A five-minute tutorial on defining Grafana dashboards in Jsonnet with the Grafonnet library, so they can be version-controlled, generated and reused instead of hand-built in the UI.

- Techniques: Install the Jsonnet toolchain; Compile Jsonnet to JSON with a jpath flag; Bootstrap Grafonnet with jb; Build a time-series panel with Grafonnet helpers; Generate repeated targets with a function; Factor panels into a lib/*.libsonnet module; Use the $ and self references in Jsonnet objects
- Tools: Jsonnet, Go jsonnet, C++ jsonnet, jsonnet-bundler (jb), Jsonnet language server (VS Code), Grafana, Grafonnet, Prometheus, PromQL, Node Exporter, Grafana Tanker, Better Stack

## [Why Your Applications NEED Distributed Tracing](../videos/E956jBlMKcA.md)
`E956jBlMKcA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

Intro to distributed tracing: why logs and metrics fall short for microservices, what traces and spans are, and a Node.js demo sending OpenTelemetry data through an OTel Collector to Jaeger.

- Techniques: Collector-based OTLP export to Jaeger; Instrument a Node.js app with an instrumentation file; Add custom span attributes, events and exceptions for debugging; Trace search for root-cause isolation
- Tools: OpenTelemetry, OpenTelemetry Collector, Jaeger, Zipkin, Docker, Node.js, Express, OTLP (OpenTelemetry Protocol)

## [Monitoring Made EASY with Grafana and Prometheus!](../videos/pGSkPutCKtQ.md)
`pGSkPutCKtQ` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

Step-by-step Docker Compose setup of Prometheus, node_exporter and Grafana to chart host CPU and root-disk usage, with a sponsored Better Stack plug.

- Techniques: Compose file for a host-metrics stack; Minimal prometheus.yml; Verify the scrape in Prometheus before Grafana; Add Prometheus as a Grafana data source; CPU utilization panel; Root disk usage panel; Dashboard layout and iteration
- Tools: Grafana, Prometheus, node_exporter (Prometheus Node Exporter), Docker, Docker Compose, PromQL, Better Stack (hosted, sponsored mention)

## [Vibe Coding Debugging: The Only Tutorial You Need for 10X Fast Debugging](../videos/2h8WSChA1-o.md)
`2h8WSChA1-o` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents

A Sentry MCP walkthrough: an agent in Cursor creates a Sentry project, installs the Next.js SDK, wires the DSN, triggers test errors, then reads an issue's trace and proposes a fix. Vendor-led, with a paid SEER feature.

- Techniques: Let the agent provision Sentry through the MCP; Install the Sentry MCP into a client; Debug an error from its issue data, not the raw code; Set a verification step after the agent wires monitoring
- Tools: Sentry, Sentry MCP server, Sentry SDK, Next.js, Python SDK, Cursor, Claude Code, SEER, mcp.json

## [Setup Centralized Logging with Rsyslog](../videos/JocDslKu3j4.md)
`JocDslKu3j4` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

Six-minute Better Stack tutorial on centralizing Linux logs with rsyslog: enable TCP reception on a collector, forward from clients over TCP 514, and verify with logger.

- Techniques: Enable TCP syslog reception on the collector; Forward all logs from a client with one rule; Verify forwarding end to end
- Tools: rsyslog, syslog, systemctl, ufw, nano, logger, ss, hostname, Ubuntu, Better Stack

## [The BEST Way to Log in Node.js - Winston](../videos/He7Dc6DuxdI.md)
`He7Dc6DuxdI` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

Node.js Winston logging tutorial: JSON logger setup, env-driven levels, default and child metadata, error stacks, exception and rejection files, then shipping logs to Better Stack.

- Techniques: Minimal Winston logger; defaultMeta for service-wide fields; Child logger for request or scope metadata; Logging errors with stack traces; Separate files for crashes and rejections; Ship logs to Better Stack via Logtail
- Tools: Winston (Node.js logging library), Node.js, pnpm, Bun, jq (pretty-printing JSON output in the terminal), Better Stack (hosted log search; Telemetry Sources), Logtail Node client and Winston transport (@logtail/node, @logtail/winston, inferred from spoken names)

## [12 Logging BEST Practices in 12 minutes](../videos/I2mWnh66Bkg.md)
`I2mWnh66Bkg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools, infra-cost-scaling, security-guardrails

A generic logging best-practices list: plan what to log, use levels and structured fields, sample high-volume logs, emit one canonical line per request, centralize, set retention, redact secrets, and watch logging overhead.

- Techniques: Canonical log line per request; Selective sampling; Redaction in the pipeline; Tiered retention policy; Load test logging overhead
- Tools: OpenTelemetry, OpenTelemetry Collector, Vector, Go slog (log/slog), Logrus (transcribed as Logris), Go

## [React 19.2 Explained in 5 Minutes (it's awesome)](../videos/8B1Nw2ajYbM.md)
`8B1Nw2ajYbM` · Better Stack · 2025-11-02 · q3 · intro · news · also: dev-tools

Quick tour of React 19.2's six new features: Activity for state-preserving hide/show, useEffectEvent, cache signal for aborting renders, performance tracks in Chrome DevTools, partial pre-rendering in react-dom, and an upgraded ESLint plugin.

- Techniques: Keep component state across hide/show with Activity; Read latest state inside an effect with useEffectEvent; Cancel wasted server work with cache signal; Profile React in Chrome DevTools using the built-in tracks; Enable React Compiler lint rules via the updated ESLint plugin
- Tools: React 19.2, React DOM, Chrome DevTools (Performance profiles), React DevTools (mentioned as unnecessary for the performance tracks), ESLint (react-hooks plugin, flat config), React Compiler

## [OpenTelemetry Makes Istio's Telemetry AMAZING!](../videos/76O-1qakUTM.md)
`76O-1qakUTM` · Better Stack · 2025-11-02 · q2 · practitioner · tutorial · also: dev-tools

Walkthrough of putting an OpenTelemetry Collector between Istio sidecars and backends (Jaeger, Prometheus, console), then adding Node.js OTel auto-instrumentation to the app; short tutorial with the config described rather than shown.

- Techniques: Mesh-first telemetry baseline; Separate observability namespace; Hand-written collector config instead of the Istio sample; Enable OTLP ingest on the backends; Verify the pipeline with kubectl; Node.js auto-instrumentation in each service
- Tools: Kubernetes, Istio, istiod, Istio Ingress Gateway, OpenTelemetry Collector, OpenTelemetry Node.js auto-instrumentation, Jaeger, Prometheus, MongoDB, kubectl, Node.js, Azure

## [Dagger - The End of Slow, Messy YAML CI/CD Forever!](../videos/cwa_MBL1kek.md)
`cwa_MBL1kek` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools, testing-verification

Short Better Stack tutorial on Dagger: write CI pipelines as functions in Go (or Python, TypeScript, PHP), run them identically locally and in GitHub Actions, cache volumes, and debug with a terminal breakpoint.

- Techniques: Daggerize a Go project; Write a test function that runs in a container; Replace GitHub Actions YAML with a single Dagger call; Cache dependency downloads with a volume; Debug a failing pipeline interactively; Reuse modules from the Daggerverse
- Tools: Dagger, Dagger Go SDK, Dagger Python SDK, Dagger TypeScript SDK, Dagger PHP SDK, Docker, GitHub Actions, Act, Go, Alpine container image, Homebrew, OpenTelemetry

## [NEW OpenAI AI Agents SDK – Multi-Agent AI Made Simple](../videos/ZvvQKie3X70.md)
`ZvvQKie3X70` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: agent-architecture, multi-agent, mcp-and-tools

Better Stack walkthrough of OpenAI's new Python Agents SDK: agents, handoffs via a router agent, function and built-in tools, local context, input guardrails, and built-in tracing.

- Techniques: Router/triage agent with handoff descriptions; Function tool from a Python function; Typed local context object; Guardrail as a classifier agent; Inspecting run steps with new_items
- Tools: OpenAI Agents SDK (Python), OpenAI web search tool, Pydantic, OpenAI platform traces

## [Go's Built-in Package for Better Logging (using slog)](../videos/_mqB7LLgwgs.md)
`_mqB7LLgwgs` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

A short Go tutorial on the standard-library log/slog package: JSON output, levels, typed attributes, groups, child loggers, and swappable handlers.

- Techniques: JSON logger as the process default; Set the minimum level through handler options; Typed attributes with helpers; Strict logging with LogAttrs; Nested objects with Group; Child logger for shared fields; Group the custom fields under one key; Keep call sites on slog and choose the backend in one place
- Tools: Go (log/slog standard library, Go 1.21+), log (standard library, migrated to slog output via SetDefault), go vet, zap (Uber logging library, mentioned as a possible handler backend), zerolog (mentioned as a possible handler backend), IDE (unnamed, showing vet errors)

## [Google’s Golden Signals with the OpenTelemetry Demo and Grafana](../videos/QWmU9Y_zKsw.md)
`QWmU9Y_zKsw` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: infra-cost-scaling

A short walkthrough of Google's four golden signals (latency, errors, traffic, saturation) on the OpenTelemetry demo app in Grafana, then a feature-flag fault-injection demo showing how failures ripple across services. Sponsored segment in the middle.

- Techniques: Golden-signal dashboard per service; Span-derived RED-style metrics cross-checked against traces; Feature-flag fault injection to map dependencies; Load generation to produce realistic traffic before reading signals
- Tools: OpenTelemetry demo app, OpenTelemetry Collector, Grafana, PromQL, Prometheus, Jaeger, Locust, Valkey (cache), Docker, Kubernetes, EC2, Better Stack

## [Better Stack MCP Server | Changelog #12](../videos/JkpEd2xUwxk.md)
`JkpEd2xUwxk` · Better Stack · 2025-11-02 · q2 · intro · review · also: mcp-and-tools

Better Stack's changelog demo of its MCP server, letting Claude Desktop manage incidents, on-call, status pages and query ClickHouse telemetry, plus the setup steps and credential scoping.

- Techniques: Incident triage loop via MCP prompts; Schema-first text-to-query over logs; Remote MCP setup for Claude Desktop; Separate the uptime token from telemetry scope
- Tools: Better Stack MCP server, Better Stack uptime (monitors, heartbeats, status pages, incidents, escalation policies), Better Stack telemetry (logs, spans, metrics), ClickHouse (HTTP client connection), Claude Desktop, remote MCP config (mcp-remote style client)

## [Jsonnet & Grizzly: The ULTIMATE Grafana Dashboard Duo!](../videos/E1wi-8w2xdA.md)
`E1wi-8w2xdA` · Better Stack · 2025-11-02 · q2 · practitioner · tutorial · also: dev-tools

Tutorial on managing Grafana dashboards as code with Grizzly, a CLI that watches Jsonnet source and pushes dashboard changes to Grafana live, with a short Better Stack product plug.

- Techniques: Grizzly watch loop in Docker Compose; Grafana service account token for Grizzly; Add the Grizzly library through the Jsonnet bundler; Split dashboard definitions from the main file
- Tools: Grizzly (Grafana CLI for dashboards and alerts), Jsonnet, Jsonnet bundler, Grafana, Docker Compose, Prometheus, Grafana Cloud, Better Stack

## [Observability vs Monitoring - Whats the difference?](../videos/ytx6jr2TyxI.md)
`ytx6jr2TyxI` · Better Stack · 2025-11-02 · q2 · intro · other · also: infra-cost-scaling

Beginner explainer distinguishing monitoring (known thresholds, the "what and when") from observability (logs, metrics and traces for the "how and why"), with a plug for Better Stack at the end.

- Techniques: Layered monitoring then observability; Tiered data collection for cost control
- Tools: Better Stack

## [OpenTelemetry in Node.js - Traces, Metrics and Logs](../videos/NbVVZlSsvvM.md)
`NbVVZlSsvvM` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: dev-tools

Step-by-step Node.js tutorial for OpenTelemetry: NodeSDK bootstrap, auto-instrumentation, manual spans, metrics and Winston logs, then switching exporters to an OTLP collector and a Better Stack backend.

- Techniques: NodeSDK bootstrap file loaded with --import; Manual span per unit of work with startActiveSpan; Attributes and events on spans; Error status plus recorded exception; Counter and histogram with the meter API; Winston logs with auto-instrumented trace context; Switch exporters to OTLP and run an OpenTelemetry Collector; Dashboard chart from a custom counter
- Tools: OpenTelemetry JS SDK (@opentelemetry/sdk-node, sdk-trace, sdk-metrics, sdk-logs, api, resources, semantic-conventions), @opentelemetry/auto-instrumentations-node, @opentelemetry/winston-transport, OTLP exporters (trace, metric, log), OpenTelemetry Collector (Docker image), Prometheus receiver (collector self-metrics), Express, Winston, tsx, Node.js (--import / --require), Insomnia (request testing), Docker

## [OpenFeature Will CHANGE How You Deploy Code](../videos/ZJzQLSfuNUI.md)
`ZJzQLSfuNUI` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

A 5-minute Better Stack walkthrough of OpenFeature, a vendor-neutral feature-flag API, showing flagd flags, device-type targeting, and an OpenTelemetry tracing hook.

- Techniques: Backend OpenFeature setup with flagd; React client setup with the flagd web provider; Device-type targeting via evaluation context; Flag data on OpenTelemetry traces
- Tools: OpenFeature, OpenFeature SDK (Python), OpenFeature React SDK, flagd, flagd web provider, OpenTelemetry (traces), OpenTelemetry Collector, Docker Compose, React, LaunchDarkly, GrowthBook

## [FINALLY Say Goodbye to Unstructured Logs with Vector.dev](../videos/We7s8KFY7Qg.md)
`We7s8KFY7Qg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

A short Better Stack tutorial on turning Nginx access logs in Docker into structured JSON with Vector, using its VRL nginx parser, and printing the result as JSON.

- Techniques: Run Vector as a Compose sidecar that tails Docker logs; Parse Nginx access logs with a VRL remap transform; Debug the pipeline by formatting the last log line with jq; Use Bruno's collection runner to generate repeatable test traffic
- Tools: Vector (vector.dev), with the VRL remap language and its parse_nginx_log parser, Docker and Docker Compose, Nginx, Bun (demo API on port 3000), Bruno (API client and collection runner), jq

## [Sick of Digging Through Logs? Find Errors FAST with OpenTelemetry and Go!](../videos/gOag7kWHJ5c.md)
`gOag7kWHJ5c` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

A Go tutorial that wires an existing slog logger into OpenTelemetry (bridge, provider, OTLP/HTTP exporter, Collector) so logs can correlate with traces and metrics. Covers only Go; the video says JS and Python were not yet supported.

- Techniques: OTel log bridge for an existing slog logger (Go); Local OTel Collector for log debugging via Docker Compose
- Tools: OpenTelemetry (OTel) logs SDK, OTLP over HTTP, OpenTelemetry Collector, Go, log/slog, Go Fiber (GoFiberApp service name), Bruno (API client), Docker Compose, otelbin (config visualizer), Prometheus, Grafana, Better Stack (promoted)

## [Docker Logging - "docker logs" Command | Log Drivers | Logging Strategies](../videos/Zlj39xXPu2k.md)
`Zlj39xXPu2k` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: dev-tools

Better Stack beginner walkthrough of Docker logging: docker logs flags (tail, since, until, grep), the default json-file driver, how the official nginx image symlinks logs to stdout/stderr, daemon.json log options, and four logging strategies.

- Techniques: Read container logs with filters; Make a container's file logs visible to Docker; Rotate and compress json-file logs globally; Stamp each log entry with custom fields; Choose a log architecture
- Tools: Docker, Docker Desktop, docker logs, docker run, docker ps, docker exec, NGINX, Windows Subsystem for Linux, Fluentd, AWS CloudWatch, Google Cloud Logging, syslog

## [AWS CloudWatch: How to Set Up EC2, RDS, Lambda and API logging](../videos/4tCj9kfc_cA.md)
`4tCj9kfc_cA` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: dev-tools

A 30-minute AWS CloudWatch setup tutorial covering EC2 agent logs, Lambda, API Gateway access logs, RDS log exports, alarms, canaries, and forwarding logs to Better Stack.

- Techniques: EC2 custom log shipping to CloudWatch; API Gateway access logging; RDS log exports to CloudWatch; Static-threshold alarm with a test trigger; Alarm to incident tool via SNS webhook; Log forwarding with a vendor Lambda and subscription filter; Synthetic endpoint canary
- Tools: AWS CloudWatch, CloudWatch Logs (log groups, log streams, Live Tail, subscription filters), CloudWatch Metrics and automatic dashboards, CloudWatch Alarms, CloudWatch Synthetics canaries, CloudWatch agent (amazon-cloudwatch-agent), Amazon SNS, AWS IAM, Amazon EC2, Amazon RDS, AWS Lambda (Node.js 18, x86_64), Amazon API Gateway

## [fluentd Data Collector | Collecting, Transforming and Routing Log Events](../videos/ephdg9usWyc.md)
`ephdg9usWyc` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Hands-on Fluentd tutorial: tail an Apache access log, parse it to JSON, strip a field, and ship it to Better Stack. Solid practical config walkthrough with a vendor-flavored destination.

- Techniques: Install Fluent Package on Ubuntu and verify; Minimal tail source with pos_file and tag; Stdout-first validation before wiring a remote destination; Remote destination with LogTail plugin; Redact fields with record_transformer; Field search on structured logs; Operate by tag, not by file
- Tools: Fluentd, Fluent Package 5.0.2, Calyptia Fluentd, td-agent (named as the pos_file directory), Better Stack Logs, LogTail (Fluentd output plugin for Better Stack), Apache HTTP Server (apache2 parser), Ubuntu 22.04 LTS (jammy), systemctl, truncate, nano, fluent-gem

## [Python Job Scheduling - with the Schedule package](../videos/nurgToSGoUM.md)
`nurgToSGoUM` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Tutorial on running periodic Python jobs with the schedule package, scraping Hacker News, and alerting on missed runs with a Better Stack heartbeat.

- Techniques: Declarative recurring jobs with schedule; Decorator-based job registration; HTML scrape to dict list with BeautifulSoup; Heartbeat ping at the end of each scheduled job; Choose the scheduler by requirement
- Tools: schedule (Python package), requests, BeautifulSoup 4 (bs4) with html.parser, pprint, Better Stack (Heartbeats, incidents, on-call escalation), VS Code, Hacker News (scraped source), Unix cron, Celery, Celery Beat, Django, AWS Lambda

## [Python QueueHandler & QueueListener - Offload Log Processing to Separate Thread | FastAPI demo](../videos/_UgXBArTWOA.md)
`_UgXBArTWOA` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: dev-tools

Walkthrough: Python QueueHandler and QueueListener move slow log sinks like SMTP email onto a background thread, shown in FastAPI. Gotcha: stop the listener on shutdown or queued records are dropped.

- Techniques: Level-gated SMTP alerting; QueueHandler + QueueListener offload; Lifespan-managed listener for FastAPI; Module split for logging config; Quick before/after latency check
- Tools: Python logging (logging.handlers: SMTPHandler, QueueHandler, QueueListener), Python queue module, contextlib asynccontextmanager (called 'context lib' in transcript), FastAPI (lifespan parameter), uvicorn (main:app, --reload), time module, VS Code, a free SMTP test service (unnamed in transcript)

## [Node.js Job Scheduling with Agenda | JSDOM web-scraping task](../videos/ZE_P7uXZm2c.md)
`ZE_P7uXZm2c` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools, data-engineering

Tutorial on scheduling Node.js jobs with Agenda, MongoDB-backed persistence, priorities, one-off and cron schedules, a JSDOM Hacker News scraper, and Better Stack heartbeat alerts. Not AI-related.

- Techniques: Run MongoDB as the Agenda backing store in Docker; Minimal Agenda setup in an ES module; Graceful shutdown with cancel; Priority via define options; One-off and immediate runs; Dead-man heartbeat for scheduled jobs; Scraping Hacker News with fetch and JSDOM
- Tools: Agenda (npm agenda), MongoDB, mongosh (MongoDB Shell), Docker, Docker Hub (mongo image), Node.js, npm, JSDOM, Better Stack (heartbeats and incidents), VS Code, fetch (Node built-in), fs (Node built-in)

## [Laravel Scheduled Tasks](../videos/gMOkw_x9ByY.md)
`gMOkw_x9ByY` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Walkthrough of Laravel's task scheduler (kernel schedule method, schedule:run vs schedule:work, cron), building a custom artisan command that publishes scheduled blog posts, and monitoring it with a Better Stack heartbeat.

- Techniques: Define a scheduled artisan task; Run the scheduler in production via cron; SQLite database for a demo project; Scaffold model, migration and seeder; Seed test data with a randomized schedule; Custom command to release due posts; Better Stack heartbeat after the job succeeds; Verify DB state with tinker
- Tools: Laravel, Artisan, PHP, SQLite, Eloquent, Faker, Carbon, Better Stack heartbeats, VS Code, cron

## [Pino JS - Logging in JavaScript / Node.js applications](../videos/fluDEkA1h6w.md)
`fluDEkA1h6w` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Better Stack walkthrough of Pino, the fast JSON logger for Node.js: log levels, formatters, child loggers, error logging, worker-thread transports, redaction, Fastify integration, and shipping logs to Better Stack.

- Techniques: Minimal Pino setup and pretty output; Log level from environment; Custom log level; Uppercase level label via formatter; Child logger for fixed context; Logging errors with stack traces; File transport with pino.transport; pino-pretty to a file without colour; Multiple log destinations; Redacting sensitive fields; Fastify with Pino; Shipping logs to Better Stack
- Tools: Pino, pino-pretty, npm, Node.js, npx, VS Code, Fastify, Better Stack Logs, @logtail/pino (Logtail Pino transport), Express (mentioned), NestJS (mentioned), Winston (mentioned)

## [Logging in FastAPI Apps / Writing a FastAPI Middleware](../videos/1RLFSOwpf88.md)
`1RLFSOwpf88` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: dev-tools

Step-by-step FastAPI logging tutorial: a configured Python logger, a per-request logging and timing middleware, and shipping logs to Better Stack, with the slow-request search as the payoff.

- Techniques: Central logger module with formatter and multiple handlers; Ship logs to Better Stack with the Logtail handler; Request logging middleware; Middleware in a separate module (class-based registration); Structured log fields via extra=; Per-request latency via timing middleware
- Tools: FastAPI, Uvicorn, Starlette, Python logging module, Python time module, Python asyncio, Logtail Python package, Better Stack (Logtail source and Live Tail UI), VS Code

## [Winston - Logging in JavaScript & Node.js applications](../videos/YjEqmINAQpI.md)
`YjEqmINAQpI` · Better Stack · 2024-11-02 · q3 · intro · demo · also: dev-tools

Tutorial on Winston, the Node.js logging library: levels, transports, JSON and printf formats, child and named loggers, error stacks, startTimer profiling, and shipping logs to Better Stack.

- Techniques: Basic Winston logger with console and file transports; Per-transport level; Readable console output and a custom timestamped line; Child logger for request-scoped fields; Stack traces for errors; Named loggers per service; Timing a block of code; Shipping logs to Better Stack with the Winston transport
- Tools: Winston (Node.js logging library, version not stated), Node.js, npm, VS Code, GitHub (Winston readme), Better Stack (log service, with its Winston/Logtail transport), Winston community transports: MongoDB, Syslog, Telegram, MySQL

## [Logging in Django and Python Applications - Handlers / Formatters / Better Stack aggregation](../videos/XSwIUnGXrwY.md)
`XSwIUnGXrwY` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: dev-tools

Step-by-step Django and Python logging: stdlib loggers, handlers and formatters, a Django LOGGING dict driven by .env, named-logger propagation, then shipping logs to Better Stack.

- Techniques: Module-scoped loggers; Python stdlib setup without a framework; Django LOGGING dictConfig; Formatter styles; Env-driven log config with django-environ; Named-logger propagation control; Shipping logs to Better Stack
- Tools: Python logging (stdlib), Django (LOGGING setting, dev server, manage.py migrate, SQLite), django-environ, logtail-python (Better Stack Python package), Better Stack (log management: sources, live tail, SQL dashboards), VS Code

## [Log Levels Explained (with practical examples!)](../videos/myxlDVC2K74.md)
`myxlDVC2K74` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Better Stack walkthrough of logging levels (fatal/critical through trace), with Python examples of when to use each and how levels drive filtering, alerting and log volume in production.

- Techniques: Classify each log call by recoverability and required action; Fail fast on missing configuration with a critical log; Try/except around IO with an error log and a fallback; Log an HTTP fetch as info on success and error on failure, with a debug payload dump; Route deprecation warnings into the logger; Set the production threshold to info and keep debug and trace out; Alert on error and critical, and watch the count after deploys
- Tools: Python logging module, Python os and sys modules, requests (Python HTTP library), telnetlib (deprecated Python stdlib module, slated for removal in Python 3.13), Loguru (external Python logging package, referenced for trace level), go-zero log package (Go, has trace method), Pino.js (Node.js logger, custom levels), log4j, log4net, syslog, Better Stack (Logtail) log service, JSONPlaceholder (sample JSON API used in the info and debug examples)

## [Dozzle - Web-based Docker Log Viewer!](../videos/4ynKW5rwd1E.md)
`4ynKW5rwd1E` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Beginner walkthrough of Dozzle, a lightweight web UI for real-time Docker container logs, run as a container with the Docker socket mounted read-only.

- Techniques: Run sample containers with port mapping; Run Dozzle with read-only Docker socket and port mapping; Run Dozzle via Docker Compose; Use the log UI for triage
- Tools: Dozzle, Docker, Docker CLI, Docker Compose, Docker Hub, Nginx, Redis, GitHub

## [JSON logs in Python apps - with FastAPI & python-json-logger!](../videos/aJCK0LWz8kg.md)
`aJCK0LWz8kg` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Tutorial on turning Python standard-library logs into JSON with python-json-logger in a FastAPI app, passing per-request fields via extra=, and shipping the logs to Better Stack with a Logtail handler.

- Techniques: Install python-json-logger and swap the formatter; Add per-request fields with extra= and let the formatter see them; Logtail / Better Stack handler alongside local handlers; Log outcome and return 404 from a lookup endpoint; Filter structured logs by field in Live Tail
- Tools: Python logging module, python-json-logger, FastAPI, Uvicorn, Better Stack (Logtail), Logtail Python handler, VS Code, venv, pip, Vector (mentioned as an alternative), Fluentd (mentioned as an alternative)

## [Logrotate - Log Management on Linux Servers](../videos/-tM6DsYam0c.md)
`-tM6DsYam0c` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: dev-tools

Practical walkthrough of logrotate on Ubuntu: per-service configs, create vs copytruncate, compression, scheduling via cron, and a heartbeat curl in postrotate to alert when rotation stops.

- Techniques: Check the installed logrotate version and defaults; Per-service rotation block in /etc/logrotate.d/; Choose the rotation strategy per app; Force a rotation to test a config; Run logrotate hourly instead of daily; Heartbeat alert on successful rotation
- Tools: logrotate 3.19, cron (cron.daily, cron.hourly), Apache 2 (apache2), rsyslog, UFW, gzip / gunzip, mail, nano, tmux, curl, Better Stack Heartbeats, Ubuntu

## [Docker with Node.js: Build, Run, and Manage Containers](../videos/ozFFCrMedFM.md)
`ozFFCrMedFM` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: dev-tools, infra-cost-scaling

Beginner Docker tutorial for a Node.js app: write a Dockerfile and .dockerignore, run on a custom network with a Postgres container, bind 0.0.0.0, orchestrate with Docker Compose and healthchecks, then ship logs to Better Stack.

- Techniques: Dockerfile skeleton for a Node app; .dockerignore for Node projects; Build and run with a tag, env file and network; Point the DB host at the container name; Bind the HTTP server to 0.0.0.0 (Fastify); docker-compose.yml with healthcheck gating; Container log and resource inspection; Vector log shipping to Better Stack
- Tools: Docker, Docker Compose, Docker Hub, Node.js (20.16 LTS base image, node:20.16-alpine3.19), npm, Alpine Linux, Fastify, Express, PostgreSQL, Vector, Better Stack

## [Fastify Application Development | Logging with Pino.js](../videos/vUDH8OX5DTM.md)
`vUDH8OX5DTM` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Beginner tutorial on building a small Fastify API in Node.js, configuring its built-in Pino logger, and shipping the logs to Better Stack through a Pino transport.

- Techniques: Fastify app bootstrap with ESM and nodemon; Enable Pino logging in Fastify by config object; Log from inside a route with reply.log; Route extraction into a plugin; Ship Fastify logs to Better Stack via the Logtail Pino transport; Fan out logs to multiple transports; Search hosted logs by a structured field
- Tools: Fastify, Node.js, npm, Pino (Fastify's default logger), @logtail/pino (Better Stack Logtail Pino transport), nodemon, Better Stack (log platform, Live tail and search), VS Code

## [Loguru - Simplified Python Logging with Loguru!](../videos/gSc1oHcwkE4.md)
`gSc1oHcwkE4` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Intro tutorial on Loguru, a Python logging library: sinks, format, JSON output, context binding, exception capture, file rotation, and shipping logs to Better Stack.

- Techniques: Minimal Loguru setup; Replace the default sink with a custom stdout sink; Colors via format markup; JSON output; Custom JSON shape with logger.patch; Per-sink level threshold; Multiple sinks; Bound context; Scoped context; Exception capture; File rotation and retention; Better Stack sink
- Tools: Loguru, Python standard library logging (comparison only), pip, VS Code, Better Stack (Logs & Metrics, Live Tail), Better Stack Python driver with LogTail handler, GitHub (Loguru repo page)

## [Monitoring Linux Authentication Logs with Vector & Better Stack](../videos/H4LSiY7I4ps.md)
`H4LSiY7I4ps` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools, security-guardrails

Better Stack tutorial: collect /var/log/auth.log with Vector, convert syslog to JSON with a remap transform, ship it to Better Stack, then chart sudo authentication failures on a dashboard.

- Techniques: Verify what auth.log captures before building a pipeline; Vector file source plus remap transform for auth logs; Validate, then test with a console sink; Ship to a remote source with an HTTP sink and bearer auth; Create a log-to-metrics group-by from the parsed event name; Build a bar chart of one event type
- Tools: Vector (version not stated), Better Stack (sources, live tail, log-to-metrics, dashboards, alerting), Ubuntu (WSL), auth.log / syslog / rsyslog, PAM (pluggable authentication modules), sudo, sshd, nano, Vector Remap Language (VRL) functions: parse_linux_authorization, parse_regex, json_extract (SQL)

## [How to Setup Uptime Kuma - Self Hosted Monitoring](../videos/t4Nb-09oZSw.md)
`t4Nb-09oZSw` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: dev-tools, infra-cost-scaling

Walkthrough of self-hosting Uptime Kuma with Docker to monitor sites, then building public status pages and incidents. The back half pitches Better Stack's managed service.

- Techniques: Uptime Kuma Docker install; HTTP(s) monitor settings; Keyword check; Status page setup; Better Stack escalation and recovery
- Tools: Uptime Kuma, Docker, Node.js, PM2, Better Stack, Playwright, Plausible, Google Analytics, Discord, Slack

## [How to Schedule Tasks in Node using node-cron](../videos/_WFcUzO_9CY.md)
`_WFcUzO_9CY` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: dev-tools

Tutorial on scheduling Node.js functions with node-cron (crontab syntax, validation, start/stop control) and wrapping a SQLite backup job with a Better Stack heartbeat so missed runs alert someone.

- Techniques: Basic node-cron schedule; Validate a cron expression before scheduling; Round-robin job state with a closure; Create a deferred, controllable task; Schedule an existing function without modifying it; Dead-man-switch heartbeat monitoring; Set heartbeat grace from measured duration
- Tools: node-cron, Node.js, npm, VS Code, crontab.guru, ChatGPT (mentioned as a way to draft cron expressions), dotenv, SQLite, Better Stack (Uptime heartbeats)

## [How To Start Logging With MySQL](../videos/4nrbbGiG0x4.md)
`4nrbbGiG0x4` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: dev-tools

Walkthrough of MySQL's four log types (error, general, slow query, binary) on Ubuntu, then shipping them and server metrics to Better Stack with a slow-query anomaly alert.

- Techniques: Enable general log at runtime; Enable logs persistently in my.cnf; Slow query log threshold check; Locate binary logs; Ship MySQL logs and metrics to Better Stack; Dashboard template plus anomaly alert
- Tools: MySQL server (version not stated), mysql command-line client, Ubuntu, systemctl, less / cat / nano, mysqldumpslow, Better Stack (logs, Live Tail, dashboards, alerts), Vector, Better Stack MySQL exporter

## [Rsyslog - Log Processing in Linux](../videos/fgdXuqiyUKs.md)
`fgdXuqiyUKs` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Hands-on Ubuntu tutorial on rsyslog: read rules from 50-default.conf, route cron output to its own file, tail a FastAPI app's log file into the syslog file, and add JSON templates and constant fields.

- Techniques: Install and verify rsyslog; Map the config layout; Route a service's output to its own file; Application log file tailed by rsyslog; Add JSON output and constant fields
- Tools: rsyslog, systemd / systemctl, apt, yum, cron / crontab, nano, Python logging, Python venv, FastAPI, Uvicorn, VS Code, Ubuntu

## [Django Middleware - Defining a Custom Logging Middleware](../videos/_FZfjYVhnwA.md)
`_FZfjYVhnwA` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Step-by-step build of a Django middleware that logs request method, IP, path, status and duration, then ships the logs to Better Stack with structured fields.

- Techniques: Class-based request/response logging middleware; Register middleware by dotted path; In-module logger with stream output; Per-request duration with time.time(); Structured fields with extra=; Adding a Better Stack Python handler; Moving network log shipping off the request path
- Tools: Django, Python logging (getLogger, StreamHandler, Formatter, QueueHandler, QueueListener), Python venv and pip, Python time module, VS Code, Better Stack (log sources, Live Tail, search), Logtail Python package (Better Stack handler), Vector, FluentD, Celery

## [What is OpenTelemetry? - Explanation and Demo](../videos/LzLULxhyIpU.md)
`LzLULxhyIpU` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Intro and live Node/Express demo of OpenTelemetry: why unified logs, metrics and traces matter, how the SDK and collector fit together, and exporting to Better Stack.

- Techniques: Bootstrap OTel in a Node/Express app with an instrumentation file loaded before the app; Use OTLP exporters for every signal, and keep the app pointed at a local Collector; Collector config: receivers, processors, exporters, service pipelines; Run the Collector in Docker with the OTel JS getting-started command; Build a custom chart from an auto-generated HTTP metric
- Tools: OpenTelemetry (API, Node SDK, OTLP exporters, Collector), OpenTelemetry Collector (otel/opentelemetry-collector Docker image), getNodeAutoInstrumentations (OTel Node auto-instrumentation package), Node.js 20.15, Express.js, Bunyan (logging, JSON output), Pino, Winston, Better Stack (Telemetry source, Live Tail, dashboards), Prometheus, Jaeger, Docker

## [PHP Logging with Monolog](../videos/GLbeuxNAcn8.md)
`GLbeuxNAcn8` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Intro tutorial on PHP logging with Monolog (channels, handlers, formatters, exceptions) that ends by shipping logs to Better Stack; useful basics, mostly vendor-tied at the end.

- Techniques: Install Monolog with Composer; Bootstrap the autoloader and import aliases; One logger per channel with a level-filtered file handler; Fan out to multiple destinations; Switch output format with a formatter; Log exceptions with context; Ship logs to Better Stack (Logtail)
- Tools: Monolog (PHP logging package), PHP 8.2, Composer, Ubuntu, Windows Subsystem for Linux (WSL), VS Code, Better Stack Logs (Live tail, sources), Better Stack PHP client (Logtail handler, installed via Composer), php8.2-curl, Laravel, Symfony, Elasticsearch / MongoDB / FluentD formatters (listed, not used)

## [Log Shipping with Vector | Collecting, Transforming and Routing Log Events](../videos/EKHjPK6CHFw.md)
`EKHjPK6CHFw` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: dev-tools

Hands-on tutorial on installing Vector, tailing syslog and a FastAPI JSON log file, transforming logs with Vector Remap Language (VRL), and shipping the result to Better Stack over HTTP.

- Techniques: Install Vector from the apt repo and manage the service; Minimal Vector config: file source to console sink, then validate; Python JSON logging for Vector to tail; Remap transform for parsing and enrichment (VRL); HTTP sink to Better Stack with bearer auth
- Tools: Vector (version not stated), Vector Remap Language (VRL), apt / apt-get, systemctl, nano, Python FastAPI, uvicorn, python-json-logger, Better Stack Logs and Metrics, Linux syslog (/var/log/syslog), WSL (Ubuntu), VS Code

## [Go Structured Logging with the slog Package (Golang)](../videos/ptoKy-COIlE.md)
`ptoKy-COIlE` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: dev-tools

Better Stack walkthrough of Go's log/slog package (Go 1.21+): levels, text and JSON handlers, attributes, groups, child loggers, file and multi-writer output, and redaction via LogValuer.

- Techniques: Replace the default logger with a configured one; Switch to JSON for aggregation; Typed attributes; Group related fields; Request-scoped child logger; Log to a file and to stderr; Redact fields with LogValuer
- Tools: Go 1.21 (speaker's version shown as 1.21.0.4 in the captions), log/slog (NewTextHandler, NewJSONHandler, HandlerOptions, Group, With, SetDefault, LogValuer), log (standard library: New, SetOutput, Default, Lshortfile, LDate flags), io.MultiWriter, os.OpenFile, os.Getenv, math/rand (Intn), VS Code, Better Stack (log platform)

## [JavaScript Console Logging Essentials](../videos/j7XwVztvKH4.md)
`j7XwVztvKH4` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: dev-tools

Beginner tutorial on the 20+ browser/Node console methods beyond console.log: format specifiers, log levels, trace, table, count, time, group and clear, with a note that Winston-style libraries are better for production.

- Techniques: printf-style substitution in console.log; Using log levels to separate message types; Using console.trace to find how code was reached; Tabular output with console.table; Counting calls with a label; Timing code with labelled timers; Grouping related output with console.group; Clearing the console after a successful stage
- Tools: Chrome DevTools, Node.js, Winston (mentioned as a logging library for production), Hacking Scale newsletter (Better Stack plug)

## [Cron Task Scheduling in Linux | User Crontabs | python-crontab package](../videos/t1QWq7IzbKw.md)
`t1QWq7IzbKw` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Better Stack walkthrough of Linux cron: install and start the cron service, write user crontab entries, schedule Python scripts with python-crontab, and monitor jobs with heartbeat pings.

- Techniques: Install and start the cron service; Five-field crontab entry; Backup a SQLite file on a schedule; Register a Python job from code using python-crontab; Manage existing cron jobs from Python; Dead-man's-switch heartbeat for each scheduled run
- Tools: cron, crontab, python-crontab, Python 3, venv, pip, requests, pathlib, shutil, sqlite3, nano, VS Code

