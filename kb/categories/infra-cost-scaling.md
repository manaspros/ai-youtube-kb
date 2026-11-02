# infra-cost-scaling — 182 videos

*infra architecture, gateways/proxies, cost, scaling, reliability*

By channel: AI Engineer 96 · Kai Explains 20 · Better Stack 66

**Synthesized guide:** [guides/infra-cost-scaling.md](../guides/infra-cost-scaling.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [This Gateway Makes Claude Code 30% Cheaper (Context Mode)](../videos/Afm-GNrJbEQ.md)
`Afm-GNrJbEQ` · Better Stack · 2026-11-01 · q3 · practitioner · review · also: token-cost-efficiency, claude-code, security-guardrails

Better Stack tests Context Mode's hosted Claude Code gateway: same answers, about 31% lower cost on log-heavy sessions, a command firewall, but all prompts pass through vendor servers.

- Techniques: Route Claude Code through a proxy gateway by base URL; Fold bulky tool output and keep an archive; Command-rule firewall with a preset; Side-by-side cost benchmark for a proxy or optimizer
- Tools: Claude Code, Context Mode gateway (hosted), Context Mode open-source plugin, Anthropic API, Claude Max plan, Opus 5.5 (as named in the video), NASA Kennedy Space Center web server logs, July 1995 (test data)

## [When Running Your Own AI Models Beats Paying for APIs - Steven Latré, imec](../videos/9-Y_oS9OBLc.md)
`9-Y_oS9OBLc` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: inference-serving, token-cost-efficiency, local-ai

imec's AI lead benchmarks coding agents on open-weight models vs. APIs and finds that concurrency, GPU utilization and harness choice, not just accuracy, decide when self-hosting pays off.

- Techniques: GPU-utilization break-even check for API vs self-host; Concurrency ramp test on a single inference box; Task-level benchmark grid across harness, model and hardware; Measure harness token output and wall time on a paid GPU; Map model choice to hardware tiers
- Tools: Codex, Pi (transcribed as 'Py'), Claude Code, SWE-Bench Pro, Qwen, DeepSeek, GLM, Kimi K3, Claude Opus (mentioned as a reference point), NVIDIA B200-class GPU (transcribed as 'A times B 200')

## [Stop Guessing Your vLLM Config: Benchmarking LLMs on Runpod - Chris Vela, Runpod](../videos/P_0_Th_ZzIg.md)
`P_0_Th_ZzIg` · AI Engineer · 2026-10-28 · q2 · practitioner · review · also: inference-serving, evals

RunPod's Chris Vela argues for benchmarking vLLM configs on GPU pods across concurrency levels before production, and previews an unreleased BenchPod template. Vendor pitch with some reusable method.

- Techniques: Config-sweep benchmarking before production; Tune max batched tokens for long generations; Pin vLLM and CUDA to what the model needs; Agent-readable benchmark and health API; Model choice by task size and team size
- Tools: RunPod (GPU pods, serverless, storage volumes, Docker images), vLLM (OpenAI-compatible server, YAML config, nightly builds), BenchPod (unreleased RunPod template built on vLLM, with FastAPI, a watchdog and benchmark metrics), Kimi K3, DeepSeek, GLM, Qwen 3.8 (transcribed as 'Quinn 3.8'), Docker, NVIDIA B300, NVIDIA H200, CUDA 12.8 and 13.0, Claude (mentioned as the service many internal users are moving off)

## [Can Your AI Analyst Keep a Secret? - Aaron Linsky, Bridgewater & Nikhil Benesch, turbopuffer](../videos/u_jvuCjuvEk.md)
`u_jvuCjuvEk` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · also: rag-retrieval, security-guardrails

Bridgewater and turbopuffer explain how to run vector search over 100M documents with per-document permissions, using cluster-pruned "native filtering" to keep recall and latency acceptable.

- Techniques: Cluster-pruned native filtering for ACL-restricted vector search; Avoid fixed top-K then post-filter for access control; Express permissions as filter predicates on documents; Napkin math before choosing an index; Object-storage-first tiering for large, bursty corpora
- Tools: turbopuffer, Amazon S3, Google Cloud Storage, Azure Blob Storage, Bridgewater DeLorean (internal bitemporal macro time-series database, mentioned), Bridgewater Vault (internal unstructured document store, about 100M docs)

## [Why Compute Still Trades in Group Chats — Affaan Mustafa & Alejandro Soumah Fernandez, Jump Trading](../videos/GCse4OMzY8U.md)
`GCse4OMzY8U` · AI Engineer · 2026-10-24 · q3 · intro · talk · also: token-cost-efficiency, governance-compliance

Jump Trading's compute leads explain how GPU capacity trades bilaterally over chats, why cheaper tokens still raise compute demand, and how prepayments and financing gate startup capacity.

- Techniques: Prepayment step-function capacity model; On-demand bridge versus financed prepayment comparison; Build-vs-rent by utilization curve; Decompose a quote into fungible and non-fungible parts; Risk-first structure selection
- Tools: H100, H200, B300, CoreWeave, Slack, Telegram, Bloomberg chat, ICE chat

## [Why Rust Is The New GOAT For AI](../videos/R-tLX37Xgx8.md)
`R-tLX37Xgx8` · Better Stack · 2026-10-24 · q3 · intro · other · also: dev-tools, coding-agents

Better Stack argues Rust is taking over AI tooling: memory safety, no GC pauses, and single native binaries, with GitHub Copilot, Codex CLI and Bun as examples. Mostly company anecdotes.

- Techniques: Rust core behind a Python API; Ship a native library instead of a helper process; Feed compiler errors back into the agent loop; Ownership-based memory for latency-critical services
- Tools: Rust, Cargo, GitHub Copilot, Copilot SDK, Bun, Zig, Claude Code, Codex CLI, Node.js, TypeScript, Go, Python

## [Buying GPUs Should Work Like Buying Stocks — Carmen Li, Compute Exchange](../videos/laQ8wMysnkk.md)
`laQ8wMysnkk` · AI Engineer · 2026-10-24 · q2 · intro · talk · also: token-cost-efficiency, product-ux

Carmen Lee (Compute Exchange / Silicon Data) pitches a neutral GPU-procurement exchange and GPU term-structure and residual-value indices; useful market context, but mostly a company talk with few reusable engineering techniques.

- Techniques: Forward-curve reading from GPU rental indices; Discounted-cash-flow residual valuation of GPU servers; Neutral exchange model for compute procurement
- Tools: NVIDIA DGX, InferenceX, MLPerf, CME futures

## [Why AI Startups Will Disappear Without Compute Markets — Evan Conrad, San Francisco Compute](../videos/Wk2bUUGFC_o.md)
`Wk2bUUGFC_o` · AI Engineer · 2026-10-23 · q3 · intro · talk · also: product-ux

Evan Conrad (San Francisco Compute) argues AI startups need compute markets because credit, deposits and forecasting risk make GPU capacity unfinanceable without liquidity; physical settlement requires operating the clusters too.

- Techniques: Build-then-sell capacity financing; Physically settled forward contracts; Take-or-pay contracts for AI capacity
- Tools: San Francisco Compute (company, compute market and operator), Junlark (former company name, as transcribed; an AI music lab), Suno and Udio (as transcribed 'Suno or UDO'; music generation products named as context), Kubernetes (via CNCF Infrastructure Group, mentioned as background)

## [Same GPU, 50% More Output: Why the Operator Matters — Oliver Kennon, SemiAnalysis](../videos/3axY1wz2OvA.md)
`3axY1wz2OvA` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: inference-serving, token-cost-efficiency, governance-compliance

Oliver Kennan (SemiAnalysis) argues GPU cost per useful token depends on the operator's serving software and ops discipline, not just the chip, and that cost positions are relative to competitors, which matters for compute futures and rental price hedges.

- Techniques: Cost per acceptable token; Compare on the same chip at a fixed interactivity target; Assess the operator, not just the hardware; Safe update and rollback process for serving
- Tools: SemiAnalysis inference calculator (public), ClusterMax 3.0 (SemiAnalysis operator rating; a 4.0 is mentioned as upcoming), NVIDIA B200 GPU

## [Can 9 year old GPU beats today's latest GPUs?](../videos/eckOsa0kBkY.md)
`eckOsa0kBkY` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: local-ai, inference-serving, token-cost-efficiency

Kai Explains tests whether four 2017 Tesla V100s can beat 2025 DGX Sparks and RTX Pro 6000 boxes on local LLM inference; the answer is yes for decode speed, but the software and power economics are the real constraints.

- Techniques: Split inference cost into prefill and decode; Check interconnect before adding GPUs; Break-even math for owned GPUs versus hosted tokens; Pick a fork that still targets your hardware generation
- Tools: NVIDIA Tesla V100 (SXM2, Volta), NVIDIA DGX Spark (GB10, Blackwell, NVFP4), NVIDIA RTX 5090, NVIDIA RTX 5060, NVIDIA GTX 1080 Ti, NVIDIA RTX Pro 6000 Blackwell Server Edition, Qwen 3.8 Flash (model; the speaker gives it as a 125B model and also uses other names), vLLM, OneCat vLLM fork (v1.50, v1.5.1), V100 Skinny (community project built on OneCat), llama.cpp, NVFP4

## [The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI](../videos/Ti-BmGU1_mQ.md)
`Ti-BmGU1_mQ` · AI Engineer · 2026-10-17 · q4 · practitioner · workshop · also: token-cost-efficiency, governance-compliance, models-research

Eugene Cheah (Featherless AI) walks through "tokenomics" in four moves (measure, right-size, buy capacity, check processes) to cut inference spend, with per-key tracking, model labels per department, and a warning that tokens are not work done.

- Techniques: Per-team and per-use-case API key split; Speed tier per workload; Planner-worker model split; Eval-driven model downsizing; Department-level model labels; Dedicated capacity for base load, burst to public cloud
- Tools: Claude Code, Pi coding agent harness, simple-classifier (open source, speaker's project), tokenomics tracking tool (open-sourced by speaker's company)

## [I Spent Two Years Building the Median — Hariprasad Sudharshan](../videos/0JZy5AuuQzc.md)
`0JZy5AuuQzc` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: product-ux, agent-architecture

Hariprasad Sudharshan argues that with rented models and harnesses, most AI-built products converge on a "median," so durable value needs a deliberate novelty, a strong opinion, and distribution.

- Techniques: Novelty budget; Three-question pre-build check; Separate model, harness and product in comparisons; Treat agent done as a median baseline; Self-hosting break-even calculator
- Tools: Claude Code, Codex, Cursor, Lovable, Replit, LlamaIndex, vLLM, Max plan

## [Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, Sonar](../videos/7b9tov5Uc5s.md)
`7b9tov5Uc5s` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: pr-code-review, software-factory, governance-compliance

Gautam Korlam (Sonar/QAR, ex-Uber) on why CI, merge queues and review were built for human speed, and how to keep agent-scale commits green, fast and auditable in regulated teams.

- Techniques: Parallel speculative merge queue; Move checks left and offload expensive checks; Cache, shard and reduce compiler churn; Layered AI review with a fast first pass; Policy-based auto-approval with escalation; Durable decision record on the PR
- Tools: Rust, GitHub, Next.js (captioned 'next text'), Uber SubmitQueue (captioned 'summit cube')

## [Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI](../videos/_naLJOqVOEI.md)
`_naLJOqVOEI` · AI Engineer · 2026-10-12 · q2 · intro · talk · also: inference-serving, models-research

A FriendliAI engineer argues open-weight models now rival frontier ones, so the inference provider's speed, reliability and cost decide the outcome. Covers prefix-cache routing, tiered KV cache and hybrid speculative decoding. Mostly a sales pitch.

- Techniques: Cache-aware request routing; Tiered KV cache offload; Hybrid speculative decoding; Provider bake-off on your own workload
- Tools: OpenRouter (provider stats snapshot), Code Arena leaderboard

## [Taming the AI Hardware Cambrian Explosion — Abdul Dakkak, Modular](../videos/7BcQdtRA3Tc.md)
`7BcQdtRA3Tc` · AI Engineer · 2026-10-12 · q2 · intro · talk · also: inference-serving

Modular's pitch for a single portable stack (Mojo language, MAX inference engine, Modular Cloud) across NVIDIA, AMD and other accelerators, backed by vendor-run speed and cost benchmarks.

- Techniques: Heterogeneous prefill/decode split; Price-normalized hardware comparison; Portable kernel development with an open benchmark; AI-assisted porting of kernels; Tuning serving parameters on a Pareto frontier
- Tools: Mojo, MAX, Modular Cloud, vLLM, SGLang, TensorRT-LLM, llama.cpp, PyTorch, Triton, CUDA, ROCm, OpenCL

## [AI Apps in a Flash: Ship to GPUs Without Docker — Dean Quiñanola, Runpod](../videos/XczFLWEntiE.md)
`XczFLWEntiE` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: inference-serving, dev-tools

RunPod's Dean Quiñanola demos RunPod Flash, a Python-first way to run and deploy GPU functions on serverless endpoints without writing a Docker image; the main takeaway is that the Docker build-push loop is the bottleneck for AI app iteration.

- Techniques: Docker-free function iteration with a local dev server; Dependencies installed at worker start-up instead of baked into an image; Endpoint-to-endpoint function calls; Network volumes for warm caches across scale-ups; Teardown of dev endpoints on cancel; Spreadsheet-driven experiment fan-out
- Tools: RunPod Flash, RunPod serverless endpoints, Docker, Docker Hub, FastAPI, PyTorch, Hugging Face, Python, GitHub

## [Deno Is Over (Cloudflare Shut It Down)](../videos/W_g7WKMwNeo.md)
`W_g7WKMwNeo` · Better Stack · 2026-10-12 · q3 · intro · news · also: dev-tools, agent-architecture

Deno's team is joining Cloudflare. The Deno runtime gets one more year of monthly fixes, Deno Deploy shuts after six months, and Cloudflare is mainly buying the team and CellD, a self-hostable durable-objects runtime.

- Techniques: Durable objects as per-entity state; Open-source the runtime to remove lock-in fear
- Tools: Deno, Deno Deploy, JSR, Cloudflare Workers, Durable Objects, workerd (WorkerD), CellD, SQLite, RustyV8 (auto-caption 'RustyVA'), Node.js, Supabase Edge Functions, Netlify Edge Functions

## [OpenRouter is Quietly Giving Nerfed AI Model (STOP Using Wrong Endpoint)](../videos/ZsnFX5mEJ4s.md)
`ZsnFX5mEJ4s` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: token-cost-efficiency, inference-serving

Kai argues that OpenRouter "nerfed model" complaints are mostly not quantization. The real causes are price-sorted provider routing, silent context and output caps, tool-call failures and cache pricing. Fix them by pinning providers and logging which endpoint served each request.

- Techniques: Pin trusted providers with provider.order; Require supported parameters and set max_tokens explicitly; Set a precision floor with quantizations; Leave tool-call requests on default AutoExacto; Audit the served provider per request; Check endpoint caps before choosing a provider; Rank providers by effective cost, not listed price
- Tools: OpenRouter, DeepSeek V4 Pro, DeepSeek V4.1 Flash, Kimi K3, GLM 5.2, GLM 5.3, GLM-5, GPT-OSS-120B, Llama 3.3 70B, Novita, DeepInfra, Together

## [Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands](../videos/iH_wV8BbS24.md)
`iH_wV8BbS24` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: sandboxing-execution, security-guardrails, coding-agents

Robert Brennan (OpenHands CEO) compares four ways to sandbox coding agents, from Docker on a laptop to one Kubernetes pod per session, and argues least privilege should set the blast radius.

- Techniques: Container per agent conversation with selective mounts; Least-privilege sandbox spec; Ephemeral pod per agent session; Event- or schedule-triggered cloud agents; Matching environment to job
- Tools: OpenHands, OpenHands Agent Canvas, Claude Code, Codex, Docker, Kubernetes, GitHub Actions, Cursor, GitHub Copilot, Twilio, Slack, Datadog

## [Agents That Own Their Inference — Du'an Lightfoot & Khaja Omer, Akamai Technologies](../videos/4n08JHb90hI.md)
`4n08JHb90hI` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: inference-serving, local-ai, evals

Akamai hands-on workshop on self-hosting LLM agents on a single GPU with vLLM: memory budgets, prefill vs decode, FP8 quantization, speculative decoding, and finding the concurrency knee.

- Techniques: Memory budget math; Concurrency sweep to find the knee; One-flag-at-a-time tuning; Quantize with your own eval set; Validate speculative decoding by acceptance rate; Prefix caching for repeated context; Own-vs-rent break-even
- Tools: vLLM, Kubernetes, LKE (Akamai Linode Kubernetes Engine), KServe, SGLang, TensorRT-LLM, llama.cpp, Ollama, Prometheus, Grafana, Langfuse, LLM Compressor

## [How Inference Keeps Up with Our Insatiable Need for Tokens — Cerebras & Gimlet Labs](../videos/_cRgl3maiT8.md)
`_cRgl3maiT8` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: inference-serving

Cerebras and Gimlet Labs walk through LLM inference optimizations, from paged KV cache and chunked prefill to prefill/decode and attention/FFN disaggregation across mixed hardware, plus agent-generated GPU kernels.

- Techniques: Paged KV cache; Prefix / prompt caching; Chunked prefill; Prefill/decode disaggregation; Speculative decoding; Attention/FFN disaggregation; Agent-driven kernel search
- Tools: Cerebras CS3, AWS Trainium, AWS EFA, NVIDIA H100, AMD GPUs, Kforge (Gimlet agent for kernel generation)

## [AI Agents Don't Read Your Policy Docs. They Hit Your APIs — Gravitee](../videos/7v2myBde05o.md)
`7v2myBde05o` · AI Engineer · 2026-10-11 · q2 · practitioner · review · also: security-guardrails, governance-compliance, mcp-and-tools


- Techniques: Per-task scoped agent identity via token exchange; Gateway-level rate limiting on agent requests; Semantic cache keyed on prompt similarity; Pre-request prompt size and relevance policies; Narrowing MCP servers to a per-agent tool subset; Export gateway telemetry to existing observability stack
- Tools: Gravitee AI Gateway, Anthropic Claude (Sonnet), Groq (inference), Databricks, Redis (built-in semantic cache), MCP (Model Context Protocol), A2A (agent-to-agent protocol), OpenTelemetry, Datadog, Splunk, Prometheus, Kubernetes

## [Zero Cold Starts: Serverless AI Agents on Akamai Functions — Thorsten Hans](../videos/Zf_e45GiNCE.md)
`Zf_e45GiNCE` · AI Engineer · 2026-10-11 · q3 · intro · demo · also: mcp-and-tools, sandboxing-execution

Thorsten Hans (Akamai) demos building MCP servers and a Vercel AI SDK agent as WebAssembly apps on Spin, deployed to Akamai Functions for near-zero cold starts and global distribution.

- Techniques: Compose MCP servers from Wasm components; Snapshot a pre-initialized interpreter into the Wasm artifact; Edge-deployed agent using a Wasm framework with a remote model; Local-to-cloud parity via Spin abstractions
- Tools: Spin, WasmTime, WASI, wasmcp, Akamai Functions, StarlingMonkey, Vercel AI SDK, Ollama, MCP Inspector, SQLite, OCI registries

## [An AI Future Without the Lock-In — Remy Guercio, Tailscale](../videos/s-glGHAa1a4.md)
`s-glGHAa1a4` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: governance-compliance, mcp-and-tools

Tailscale's Remy Guercio argues for "ROI maxing" over token maxing: keep choice at every AI layer through an identity-aware AI gateway (Aperture) to avoid lock-in. Mostly a product pitch.

- Tools: Tailscale, Aperture (Tailscale AI gateway), WireGuard, TSNet, Entra, Okta, Anthropic API, OpenAI API, Vercel AI gateway, AWS Bedrock, Codex, Claude Code

## [From 15% to 90% GPU Utilization: Fix the Data Pipeline, Not the Model](../videos/tNAV259UhCM.md)
`tNAV259UhCM` · AI Engineer · 2026-10-10 · q4 · practitioner · talk · also: data-engineering, training-finetuning-rl

Fixing a multimodal SFT data pipeline on Ray (concurrency, prefetch, zero-copy, scheduling) took GPU utilization from 15% to about 90%. The lesson: profile the data path, not the model.

- Techniques: Wait time ratio as the pipeline health metric; Async IO for object-store fetches, process pool for CPU preprocessing; Background prefetch queue; Pass object references instead of data; Spread scheduling and zero-copy retrieval at scale; Scaling-ladder ablation
- Tools: Ray, Ray actors, Ray object store, Megatron, Qwen3-VL (auto-caption reads as "QN3VL"), PIL, NumPy, Hugging Face Transformers tokenizers, pandas, S3, JSONL, asyncio

## [Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg](../videos/cf2IhzqeQH4.md)
`cf2IhzqeQH4` · AI Engineer · 2026-10-07 · q3 · intro · talk · also: governance-compliance, product-ux

Stigg's CEO argues AI usage pricing needs bank-style runtime controls: synchronous entitlement checks before consumption, hold-and-settle for concurrency, and layered credit pools, not invoice-time reconciliation.

- Techniques: Synchronous pre-consumption check with async settlement; Hold, settle, and idempotency for concurrent draws; Ordered draw-down across credit sources; Deterministic decision waterfall; Metering ledger inside the customer VPC
- Tools: Stigg, OpenClaw, Claude Max, GitHub Copilot

## [Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell — Akamai](../videos/XTpyNrEgJQ4.md)
`XTpyNrEgJQ4` · AI Engineer · 2026-10-07 · q3 · practitioner · demo · also: inference-serving

Akamai's Sheila explains when speculative decoding pays off on vLLM: spare GPU memory and structured, low-temperature workloads, measured by acceptance rate and tokens/s on a single Blackwell GPU.

- Techniques: Draft-model speculative decoding; Acceptance-rate-first benchmarking; Draft model selection checklist; Side-by-side A/B on one GPU; Workload triage before enabling
- Tools: vLLM, Llama 70B, NVIDIA Blackwell GPU, EAGLE, Medusa, n-gram speculative decoding

## [Move Fast and Don't Break Things: Scaling Databases for the AI Era — PlanetScale](../videos/uKUA1a0Kdfc.md)
`uKUA1a0Kdfc` · AI Engineer · 2026-10-07 · q3 · intro · talk · also: dev-tools, governance-compliance

PlanetScale's Ben argues that agent-driven change can be safe if databases are isolated, sharded, back-pressured, and branched like code, with agents given the same primitives humans use.

- Techniques: Per-segment traffic budgets with graceful degradation; Shard with a routing proxy plus per-shard replicas; Declarative sharding config as JSON for agent drafting; Schema branch, deploy request, one-click revert; Isolation by failure domain
- Tools: PlanetScale, Vitess, VTGate, MySQL, Postgres, SQLite, MCP server, CLI, VSchema

## [How I Learned to Stop Worrying and Love the Sandbox — Matt Brockman, E2B](../videos/fz6-NS7qpZc.md)
`fz6-NS7qpZc` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: sandboxing-execution, agent-architecture

E2B engineer runs a hands-on sandbox capture-the-flag, covering resource limits, snapshot/resume, templates, lifecycle timeouts, orphan processes, and per-user sandbox assignment.

- Techniques: Snapshot-and-resume sandboxes; Warm template with processes already running; Fork a sandbox for parallel experiments; Task-scoped lifetime with a short idle timeout; Orphan process inventory and reaping; Per-user sandbox assignment map; Separate read-only and writable paths; Egress rules when secrets are present
- Tools: E2B, Firecracker, Nomad, Kubernetes, Claude Code, Codex, Python SDK, JavaScript SDK

## [What Is an Inference Engine, Anyway? — Charles Frye, Modal](../videos/woIYJYd_etI.md)
`woIYJYd_etI` · AI Engineer · 2026-10-06 · q4 · deep · workshop · also: inference-serving, observability

Charles Frye (Modal) explains what runs inside an LLM inference engine: workloads, prefill vs decode, process layout, scheduler bottlenecks, KV cache, CUDA graphs, speculative decoding, and production debugging.

- Techniques: Phase-split serving metrics; Keep host work off the GPU critical path; Speculative decoding with exact-output verification; Prefix and radix KV-cache reuse; Treat queueing and cache thrash as alerts; Correctness logging and post-deploy evals; Profile for per-GPU or per-host anomalies
- Tools: SGLang, vLLM, TensorRT-LLM, PyTorch, Hugging Face transformers, FlashAttention, FlashInfer, CUTLASS, Triton, DeepGEMM, DeepEP, Marlin

## [Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI](../videos/48YUYDjwfYY.md)
`48YUYDjwfYY` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: token-cost-efficiency, coding-agents, sandboxing-execution

Cast.ai's Kimchi team argues for routing each task to the cheapest model that still meets a quality bar, judged by cost per task, with long-running sessions kept alive in remote sandboxes.

- Techniques: Per-task cost-at-quality model comparison; Outcome-scored harness with a grade gate; Milestone-based long-run planning with up-front questions; Remote sandbox session that outlives the client; Team review board for agent sessions
- Tools: Kimchi, Ferment, Teleport, Studio, pi-mono SDK (captioned as 'PyMono SSDK'), Claude

## [Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI](../videos/FQwTqUmcbRg.md)
`FQwTqUmcbRg` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: data-engineering, training-finetuning-rl, inference-serving

Datology's CTO on running trillion-token synthetic pretraining data jobs: rephrase seeded documents, batch S3 metadata calls, checkpoint for GPU failures, schedule CPU and GPU pools atomically, and sweep vLLM flags.

- Techniques: Seed-based document rephrasing for synthetic pretraining data; Batched S3 metadata listing at maximum page size; Right-sized partitions with checkpointing and idempotent retries; Atomic CPU and GPU scheduling with dedicated pools; Grid search over vLLM and SGLang serving parameters for batch inference; One workflow for research and product in the same infrastructure
- Tools: Ray, KubeRay, vLLM, SGLang, Apache Spark, Kubernetes, Amazon EKS on HyperPod, Slurm, Amazon S3, Parquet, Beyond Web (DatologyAI synthetic data recipe), Nemotron Synth

## [GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe](../videos/bRGyYaE0lxI.md)
`bRGyYaE0lxI` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: training-finetuning-rl, inference-serving

Crusoe engineers explain how they run Slurm on Kubernetes so failed GPU nodes are cordoned, replaced and the training job resumes from checkpoint with no user action, with a live demo.

- Techniques: Automated GPU failure remediation loop; Opt-out label check before node replacement; Checkpoint on SIGTERM grace window; Slurm operator on Kubernetes (Slinky pattern); Shared GPU pool across training and inference
- Tools: Slurm, Kubernetes, Slinky (SchedMD), sbatch, srun, PyTorch, Crusoe Managed Kubernetes (CMK), Crusoe AutoClusters, Crusoe Slurm operator

## [What Makes Open Models Fast in Production — Sujee Maniyam, Nebius](../videos/TRe1u7dHYiA.md)
`TRe1u7dHYiA` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: inference-serving

Nebius Token Factory explains the serving optimizations behind fast open-model inference: cache-aware routing, speculative decoding, KV-cache offload, and prefill/decode separation. It is mostly a product pitch with few measured results.

- Techniques: Cache-aware request routing; Speculative decoding with a self-trained draft model; KV-cache offload to host memory; Prefill/decode disaggregation; Per-model engine and precision selection
- Tools: Cursor, OpenCode

## [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](../videos/vGCJ7diEtrw.md)
`vGCJ7diEtrw` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: software-factory, testing-verification, context-engineering

Factory's engineer defines a "software factory" as a full autonomous lifecycle, not coding agents. Covers model routing for cost, verifiable done-criteria, sequential worker and validator missions, deferred tool loading, and codebase readiness.

- Techniques: Difficulty-classified model routing; Validation contract written before coding; Sequential workers with fresh context per handoff; Two-tier validation; Deferred tool loading; Codebase readiness audit; Codify tacit rules as skills or plugins
- Tools: Factory (software factory platform), Factory missions (orchestrator, worker and validator agents), Automatic model routing, Deferred context engine, Agent readiness framework, Plugins, Auto-wiki, Slack, GitHub, Figma, Notion, Gmail

## [Why DeepSeek Ditched Its Own Flagship (And Then Didn't)](../videos/u00vNoI2iQc.md)
`u00vNoI2iQc` · Kai Explains · 2026-10-02 · q3 · practitioner · news · also: token-cost-efficiency, models-research, inference-serving

Kai Explains on DeepSeek briefly retiring V4 Pro for V4.1 Flash, reversing within a day, and why agent teams should cost-model and test their own prompts before switching models.

- Techniques: Cost agent turns by cache-hit vs cache-miss input; Pin model identifiers and track vendor changelogs; Run candidate models on your own traffic before switching; Route by task type across model tiers; Use concurrency limits as a capacity signal in model choice; Rank models by cost per solved task
- Tools: DeepSeek V4 Pro, DeepSeek V4.1 Flash, DeepSeek V4.1 Pro (named as roadmap, not released), Claude Opus 5, GPT 5.6 Sol, DeepSWE benchmark (as captioned), Humanity's Last Exam, ProgramBench, Terminal Bench (hardest version), Cybergym, GitHub issues (developer feedback channel)

## [Columnar Databases Are Incredibly Fast. Here's Why.](../videos/mR06J55fLvo.md)
`mR06J55fLvo` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: data-engineering, dev-tools

Better Stack compares Postgres, ClickHouse and DuckDB on 100M rows: columnar stores win big on aggregations, but lose on point lookups and single-row updates.

- Techniques: Split workloads by access pattern; Choose the ClickHouse sort key for the dominant filter; Insert in key order to make min/max skipping work; Avoid per-row updates on columnar stores; Benchmark with identical SQL on the same data
- Tools: PostgreSQL, ClickHouse (open-source server, shown as local server), DuckDB (embedded, single-file library)

## [Lovable Rewrote Vite in Rust... (kind of)](../videos/msSZ4CL_sNg.md)
`msSZ4CL_sNg` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: dev-tools, vibe-coding-app-building

Better Stack tests Lovable's claim that OJ, a Rust rewrite of Vite's dev server, is 4x lighter and 2x faster to start, finds small gains on a small app and larger gains on a 5000-component app, and summarizes Evan You's critique.

- Techniques: Benchmark a dev server by time-to-deepest-component plus process-tree memory; Check fast refresh state preservation with a counter component; Coalesce agent write bursts into one hot update
- Tools: OJ (Orange Juice, Lovable's Rust dev server), Vite (8.1 per the transcript; Bundle Dev Mode is experimental), Rolldown (VoidZero), Oxc (VoidZero), Rust, React, TanStack Start, Tailwind CSS, esbuild (mentioned, not used), Vite Plugin Checker, Google Chrome (benchmark harness)

## [Oracle’s $288B Lease: The Debt They Can’t Escape](../videos/mNozPwLvJIY.md)
`mNozPwLvJIY` · Kai Explains · 2026-10-02 · q3 · intro · news · also: governance-compliance, models-research

Kai Explains argues Oracle's Project Jupiter force majeure notice is not an exit signal; the real constraint on AI capacity is power and permits, not demand.

- Techniques: Read the contract and filing before the headline; Trace cash flow by layer and strip out one-off inflows; Compare market timestamps with news timestamps
- Tools: Oracle Cloud Infrastructure, OpenAI, Bloom Energy fuel cells, GE Vernova gas turbines, Energy Transfer pipeline, Blue Owl Capital, Stack Infrastructure

## [AI just hits its Tipping Point (Outage)](../videos/e0NvEaJT7cY.md)
`e0NvEaJT7cY` · Kai Explains · 2026-10-02 · q3 · practitioner · other · also: models-research

Commentary on the Sept 3 2026 outages that hit Claude, ChatGPT and Grok in one window; argues the shared hidden dependency is who owns the data center, so fallbacks should be chosen by landlord, not logo.

- Techniques: Fallback landlord audit; Skip failover when the risk is small; Test the fallback regularly; Monitor every provider's status feed
- Tools: Claude, ChatGPT, Grok, Gemini, Claude Code, Cowork, Codex, Claude.ai, VS Code extension, NVIDIA GPUs (H100, H200, GB200), Colossus One, Cloudflare

## [Cloudflare Just Saved 100TB of Memory](../videos/RTmTebnxwKc.md)
`RTmTebnxwKc` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: dev-tools

Cloudflare cut DNS cache memory per entry by 56% with five Rust data-layout changes (Vec to Box, flattened lists, deduped owner names, boxed enum variants, raw wire-format bytes), freeing about 100TB fleet-wide.

- Techniques: Swap growable Vec/String for Box<[T]> / Box<str> on write-once data; Flatten parallel same-length-lifecycle lists into one list plus small offsets; Store a field only when it differs from a value already stored; Box rare large enum variants, keep common small ones inline; Keep cached payloads in the wire or serialized format; Audit per-entry footprint and allocated bytes separately
- Tools: Rust, Cloudflare 1.1.1.1 (public DNS resolver), Big Pineapple (Cloudflare's DNS resolver software, Rust), gemmalloc (allocator, as transcribed; may be an auto-caption error), DNS wire format

## [Mac Studio vs AMD AI PC: Don't Buy Before Watching This](../videos/dlyic4oco4s.md)
`dlyic4oco4s` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, inference-serving

Mac Studio M5 vs Ryzen AI Max+ 395 for local AI: prefill, not tokens/sec, dominates wait time, MoE models shrink Apple's lead, and cheap AMD mini PCs can be misconfigured traps.

- Techniques: Measure prefill and decode separately, at your real context length; Pick hardware by model architecture; Check that the GPU math library is actually in use; Tune the AMD unified-memory box (documented steps as described); Run a constellation of small resident models under an orchestrator; Vet mini-PC SKUs before buying; Use newer open-source attention kernels on the AMD iGPU
- Tools: Mac Studio M5, Apple M5 Ultra, Apple M5 Max, Apple M4 Max, Apple M1 Max, AMD Ryzen AI Max Plus 395, Framework Desktop, Minis Forum MS-S1 Max, Gemma 4 (12B, dense), gpt-oss-120b (~116B total, ~5.1B active), Qwen 3.6 (35B-class MoE, about 3B active), a 122B model (name not given)

## [DeepSeek's $1 Billion Is a Price Hike, Not Growth](../videos/dXieY9PwvJg.md)
`dXieY9PwvJg` · Kai Explains · 2026-10-02 · q4 · practitioner · news · also: token-cost-efficiency, models-research

Breaks down DeepSeek's reported $1B annualized revenue: most of the jump came from an August price hike, not volume growth, and cache-hit rates drive real agent bills.

- Techniques: Decompose spend into price x volume before trusting a revenue or cost trend; Measure your cache-hit (cached input) ratio per provider and per model; Pin a specific provider in the router config, not just a model name; Use time-of-day or peak/off-peak tiers to shift batch or background work
- Tools: DeepSeek V4 Flash, DeepSeek V4 Pro, DeepSeek V4.1 Flash, DeepSeek API, OpenRouter, OpenCode, Huawei Ascend 950 Supernodes, Ascend 950DT, MIT-licensed DeepSeek weights, Nebius, Together, Parasail

## [Mac Studio vs DGX Spark: Which Is Better for Local AI?](../videos/_NZeV2uOVnk.md)
`_NZeV2uOVnk` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, inference-serving

Kai Explains compares a Mac Studio (M3 Ultra, with M5 Ultra prices and specs) and an NVIDIA DGX Spark for local LLM inference, and argues the answer depends on whether the workload is decode-bound, prefill-bound, or CUDA-shaped.

- Techniques: Benchmark prefill and decode separately; Estimate decode ceiling from bandwidth; Size memory as usable, not nominal; Test concurrency, not just one stream; Disaggregated prefill and decode across two machines; Rent before buying
- Tools: Mac Studio (M3 Ultra, 819 GB/s; M5 Ultra for specs and pricing, 1.2 TB/s), NVIDIA DGX Spark (GB10, 128 GB LPDDR5X, 273 GB/s), llama.cpp, MXFP4, Ollama, vLLM, TensorRT-LLM, SGLang, CUDA, cuDNN, NCCL, Triton

## [Why LLM Recommenders Will Be AI's Biggest Consumer App — Devansh Tandon, Meta](../videos/lIgdnF0s0kQ.md)
`lIgdnF0s0kQ` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: models-research, product-ux

Devansh Tandon (Meta) argues recommenders scale like LLMs, lays out four recommender S-curves, gives a three-step recipe for LLM recommenders built on semantic IDs, and claims feeds are far more token-efficient than chat apps.

- Techniques: Semantic ID tokenization of content; Bilingual LLM pre-training on semantic IDs; Post-training LLM rerankers with chain of thought; Shared base model with thin per-surface fine-tuning; Agentic recommendation loop
- Tools: Semantic IDs, HSTU, Tiger, Plum, Gemini, Claude Code, Codex

## [One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio](../videos/2wgPHvW0mG8.md)
`2wgPHvW0mG8` · AI Engineer · 2026-09-27 · q3 · intro · talk · also: multi-agent, voice-multimodal, agent-architecture

Skydio's Suchet Bargoti on running fleets of docked drones as agent-commanded infrastructure: tool-based VLM control, edge/cloud latency tiers, a shared map that the fleet updates, and a learning flywheel.

- Techniques: Tool-exposed primitives for a VLM agent; Latency-tiered edge and cloud split; Fleet-shared map with sync-back; Bandwidth-aware video encoding for cloud agents; Hybrid end-to-end versus hand-engineered decomposition; Log, sanitize, retrain, redeploy loop
- Tools: Vision-language model (VLM), Reinforcement learning, Drone APIs exposed as agent tools, Cloud GPUs and inference engines, Map merging and sync service

## [The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI](../videos/Hvb2LfMH58c.md)
`Hvb2LfMH58c` · AI Engineer · 2026-09-20 · q2 · intro · talk · also: inference-serving, agent-architecture

FriendliAI's CEO argues agent workloads need task-level (end-to-end) latency optimization, not per-request speed, and pitches prefix caching, KV cache management and cache-aware routing on an open-weight inference cloud.

- Techniques: Prefix KV caching for agent steps; Tiered KV cache with quantization and cross-replica sharing; Cache-aware routing with load-aware fallback; Optimize end-to-end task latency as the target metric; Agent-aware scheduling (described as future work)
- Tools: vLLM, GLM 5.2, Kilo Code, Claude Opus 4.8, MiniMax, Kimi

## [Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI](../videos/sOB3HSiG8vo.md)
`sOB3HSiG8vo` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: inference-serving

OpenAI's inference team explains how its inference load balancer moved from a feedback-loop weight controller to a control-plane/data-plane design that optimizes end-to-end latency, plus retry budgets, outlier penalties and load shedding for production stability.

- Techniques: Control-plane / data-plane routing split; Latency-minimizing routing weights; Outlier penalty by weight reduction; Utilization-dependent retry budget; Proactive load shedding

## [Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave](../videos/cQQbJqvZkpo.md)
`cQQbJqvZkpo` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · also: inference-serving

CoreWeave's inference platform talk: how serverless, dedicated and batch consumption models share one stack, with KV-cache-aware routing, cache offload and quantization/speculative decoding as the main performance levers.

- Techniques: KV-cache-aware request routing; KV-cache offload to high-bandwidth storage; Provisioned throughput on a shared serverless tier; Time-scheduled reuse of reserved GPUs for batch; Async speculator training on customer data; Metering without retaining content
- Tools: vLLM, SGLang, TensorRT-LLM, LMCache, Mooncake, NVFP4, Artificial Analysis, OpenRouter

## [Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta](../videos/7c9FSUVcXR0.md)
`7c9FSUVcXR0` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · also: inference-serving, agent-architecture

Two Meta infra engineers argue LLM inference is now a distributed-systems and orchestration problem, so teams should optimize cost per successful task and build a control plane, not just faster tokens.

- Techniques: Four-quadrant optimization check; Workflow-aware scheduling and retries; Cascade breakers: queue-depth shedding, circuit breakers and retry budgets; Cost per successful task as the KPI; Telemetry-driven control loop; Latency, cost and throughput trade-off triangle
- Tools: vLLM, SGLang, TensorRT, Triton, Kubernetes, Mesos

## [Large clusters for small models — Daniel Svonava, Superlinked](../videos/g4SsanB0gMc.md)
`g4SsanB0gMc` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: inference-serving, local-ai, training-finetuning-rl

Daniel Svonava (Superlinked) on serving fleets of small open models on your own GPUs: why top-down routers fail for many small requests, and how a centralized pull-based queue, a thin Rust gateway and a runtime sidecar fix it.

- Techniques: Centralized pull-based batching queue; Thin gateway with annotation, not full parsing; Runtime sidecar behind a socket; Knee-based benchmarking; Pin plus lazy-load model placement; Per-task model selection with evals, then cheap adaptation; Autoresearch loop for serving tuning
- Tools: vLLM, SGLang, PyTorch, Candle, NATS JetStream, MessagePack, Rust, AWS Bedrock, LoRA, Hugging Face

## [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../videos/XsvUhpnHepE.md)
`XsvUhpnHepE` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: voice-multimodal, mcp-and-tools, token-cost-efficiency

Oxylabs' Giedrius Šteimantas argues web-using agents need a scraping infrastructure layer: use browsers only when required, validate content before it reaches the LLM, and fix the failing discovery and purchase stages of a shopping agent.

- Techniques: Validate page content before the LLM sees it; Search API for discovery, not a browser; Tiered web access: API first, browser last; Markdown and geolocated output from the scraper; Drop-in managed browser for Playwright MCP
- Tools: Playwright MCP, Oxylabs Fast Search API, Oxylabs Web Scraper API, Oxylabs Headless Browser

## [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../videos/zrZ1amZBSPw.md)
`zrZ1amZBSPw` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: governance-compliance, security-guardrails

Principal engineer at Twilio on running an LLM gateway in production: per-request fallbacks, per-route latency timeouts, guardrail fail-open/closed choices, load shedding, and centralizing governance without centralizing traffic.

- Techniques: Per-request provider fallback; Cool-down for failing providers; Per-route P99 and timeouts; Hedged requests for the tail; Guardrail time budget and explicit fail mode; Guardrail placement by output type; Bounded queues and load shedding with priorities; Per-route API key segregation; Decentralized traffic, centralized governance

## [Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS](../videos/gxVZ_1tuuq4.md)
`gxVZ_1tuuq4` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: agent-architecture, memory

AWS's Mike Chambers argues that an agent minus its model is the harness, and that agents built for many users should split the loop, memory, identity and tools into separately scaled parts, demoed on Bedrock AgentCore.

- Techniques: Split agent components for independent scaling; Session manager for cross-invocation state; Local dev loop that mirrors production; Declarative harness config; Agent-generated infrastructure as code
- Tools: Amazon Bedrock AgentCore, AgentCore CLI, Strands Agents SDK, Kiro, Claude Code, Cursor, MCP, AG-UI, AWS agent toolkit, Sonnet 4.5

## [Generative Video at the Speed of Light — Keegan McCallum, uRun](../videos/Xln-On3syJk.md)
`Xln-On3syJk` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: voice-multimodal, inference-serving

Keegan McCallum (uRun) argues generative video is improving on efficiency and long-horizon generation as well as quality, and describes the infra needed for real-time interactive video apps.

- Techniques: Distill a large video model for real-time serving; Real-time steering instead of prompt-and-reroll; Multi-model streaming pipeline with per-frame control sync; Wrap real-time video as a React component plus Python runtime; Agent-facing access via CLI and MCP server
- Tools: Helios, Wan 2.1 14B, WebRTC, ICE, TURN, React, Python async runtime, MCP, CLI, Sora, Sora 2, Seedance

## [Homa: The End of TCP for AI Clusters — John Ousterhout, Stanford](../videos/eZ8WWZzoaR0.md)
`eZ8WWZzoaR0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: inference-serving

Ousterhout argues AI inference and agentic workloads now send many small latency-sensitive messages, which TCP and RDMA handle badly, and presents Homa, a receiver-driven transport with about 13x lower short-message P99 in his benchmark.

- Techniques: Message-framed transport (RPC unit); Receiver-driven grant scheduling; Unscheduled first-RTT send; SRPT via switch priority queues; Percentile sweep by message size
- Tools: Homa (Linux kernel module), TCP, RDMA over Converged Ethernet (RoCE), ECN marking

## [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../videos/YXowceUKYJI.md)
`YXowceUKYJI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: inference-serving, agent-architecture

Red Hat engineers explain why agentic multi-turn traffic breaks classic LLM serving, and how llm-d uses KV-cache-aware routing and prefill/decode disaggregation on Kubernetes, with benchmark data and a GLM 5.2 case study.

- Techniques: KV-cache-aware pod routing; Prefill/decode disaggregation with KV transfer; Tiered KV offload with session pinning; Distribution-based capacity planning and trace replay; Decision matrix before choosing PD
- Tools: llm-d, vLLM, Kubernetes, NIXL, DeepEP, Mooncake, inference-perf, LeaderWorkerSet, RDMA/RoCE

## [Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher](../videos/y2W4FNAuPEA.md)
`y2W4FNAuPEA` · AI Engineer · 2026-09-18 · q3 · practitioner · workshop · also: inference-serving, agent-architecture

Two-hour LLM inference workshop covering KV-cache memory math, prefill vs decode, attention variants, quantization, vLLM/SGLang serving optimizations, and benchmark caveats.

- Techniques: KV-cache capacity planning; Fix one dimension, then solve the rest for cost; Weight quantization for KV headroom; Attention variant selection; Radix-tree prefix caching for agent loops; Speculative decoding variants; Engine benchmarking loop
- Tools: vLLM, SGLang, TensorRT-LLM, NVIDIA Dynamo, Hugging Face Transformers, FlashAttention, EAGLE, Medusa, Molab, Google Colab, Mistral 7B, GPT-OSS-120B

## [Why Your AI Agent Needs a Wallet: USDC and Nanopayments — Harshal Bhangale, Circle](../videos/xKzU_3riL6s.md)
`xKzU_3riL6s` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: governance-compliance, mcp-and-tools

Circle engineer argues agents need wallets: x402 pay-per-request with USDC nanopayments and wallet-enforced spend caps, shown in a live Claude Code demo. Vendor pitch with a real but partly failed demo.

- Techniques: Wallet-enforced spend caps; HTTP 402 pay-per-request (x402); Off-chain signed authorizations with later settlement
- Tools: Claude Code, Circle Agent Wallet, x402, USDC, Circle Gateway, Nanopayments, Gmail, Blockrun (data provider), Polymarket data

## [The Search Engine for the Agentic Web — Will Bryk, Exa](../videos/59AA5kIoqjA.md)
`59AA5kIoqjA` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: rag-retrieval, product-ux

Exa's CEO pitches Exa as a search engine built for AI agents rather than humans, covering its history, API features (fast endpoint, token extraction, structured output) and a data marketplace.

- Techniques: Hybrid embedding plus keyword retrieval; Token-budget extraction before the LLM; Schema-based structured search output; Per-tenant search configuration; Latency tiers by consumer type
- Tools: Exa search API, Exa Connect, Cursor, HubSpot, Similarweb, GPT-3, ChatGPT

## [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](../videos/cI7zfqusmFU.md)
`cI7zfqusmFU` · AI Engineer · 2026-09-18 · q3 · practitioner · demo · also: agent-architecture, multi-agent

Giselle van Dongen (Restate) argues long-running agents need a durable infrastructure layer, and demos journaled retries, human-approval suspension, keyed sessions and mid-run signal or cancel.

- Techniques: Wrap every side-effecting agent step in a durable run call; Durable promise for human-in-the-loop approval; Keyed virtual object per session for serialized agent state; Classify mid-run input, then signal or cancel-and-restart; Central LLM gateway as its own durable handler
- Tools: Restate, Slack, LiteLLM, Python

## [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](../videos/byn9PURoBNY.md)
`byn9PURoBNY` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: training-finetuning-rl, inference-serving

Krea's infra engineer on training the from-scratch Krea 2 diffusion transformer at scale: which metrics matter, why to let crashing runs restart, frequent checkpoints, and bursting training and inference across clusters and rented GPUs.

- Techniques: Let crashing jobs restart instead of debugging each crash; Hard GPU health gate on temperature; Checkpoint every 20 to 30 minutes to a high-throughput file system; Two-tier priority queue in front of Kubernetes; Overflow to external GPUs with a virtual node
- Tools: Kubernetes, Virtual Kubelet, Kubernetes descheduler, Kubernetes taints and tolerations, Queue system (captioned as 'Q') for gang scheduling, Prometheus, NVIDIA DCGM, Weka (parallel file system), Ceph, InfiniBand, NVLink, Hugging Face

## [When AI Agents Pay and Sellers Monetize: Building x402 Apps on AWS — Anil Nadiminti, AWS](../videos/qTZirYu9pr0.md)
`qTZirYu9pr0` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: governance-compliance, security-guardrails, mcp-and-tools

AWS walkthrough of letting AI agents pay for content via the x402 HTTP 402 protocol, with AgentCore Payments on the buy side and WAF bot pricing on the sell side. Mostly product pitch, with some useful architecture.

- Techniques: Payment session spend caps with expiry; Deterministic payment layer decoupled from the agent loop; Key custody behind KMS, with agent-level capability only; x402 request/402/pay/retry flow; Edge bot classification and differential pricing
- Tools: AgentCore Payments, Bedrock AgentCore Gateway, Bedrock AgentCore Runtime, AWS WAF, Amazon CloudFront, AWS KMS, x402, Coinbase wallets, Stripe wallets, Base (L2 chain)

## [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../videos/5dCAmSDOAjI.md)
`5dCAmSDOAjI` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: voice-multimodal, inference-serving, product-ux

Ahmed Ahres (Reactor) argues real-time interactive video and world models will change how content is made and consumed, then describes the infra gaps: streaming, session memory, and sub-100 ms global latency. Mostly a company pitch.

- Techniques: Stream frames over a live session instead of returning a file; Regional GPU routing for a latency budget; Session memory to keep generated worlds consistent; Multi-GPU serving plus quantization for cost and speed; Human-in-the-loop evaluation for real-time output
- Tools: Reactor API (real-time world model platform, roughly 10 lines to integrate per the speaker), Helios (ByteDance, interactive video model), LingBot (Alibaba, world model), LongLive 2 (NVIDIA, multi-shot film model), StreamDiffusion (NVIDIA, video-to-video; transcript reads 'SoundCloud Streaming', likely a caption error), Veo, Sora, Genie 3 (mentioned as comparisons)

## [Connect AI to Billions of Legal Documents — Simon Eskildsen, turbopuffer & Jacob Lauritzen, Legora](../videos/V-isu4eTHgw.md)
`V-isu4eTHgw` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: rag-retrieval, security-guardrails, enterprise-adoption

Legora (legal AI) walks through moving project and legal-research search from one Elasticsearch, to Postgres/pgvector, to turbopuffer, one namespace per project on object storage, and why that fits regulated multi-tenant workloads.

- Techniques: Namespace-per-tenant isolation with per-namespace keys and buckets; Partition by access temperature, not by hash; Object-storage-native write path; Round-trip budgeting over object storage; Memory-only cache for encrypted multi-tenant data; Clustered centroid tree for vector search; Two-round-trip inverted index for full text; Fan-out with hierarchy and validity filters for legal research
- Tools: turbopuffer, Elasticsearch, PostgreSQL, pgvector (DiskANN index, transcribed as 'disk NN'), Postgres tsvector, BM25, Amazon S3 (object storage), Google Cloud Storage, Azure Blob Storage, NVMe SSD cache

## [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../videos/FvxY8oPoI8o.md)
`FvxY8oPoI8o` · AI Engineer · 2026-09-18 · q2 · practitioner · demo · also: token-cost-efficiency, evals, coding-agents

DigitalOcean's Archana Kamath and Tyler Gillam argue for per-request model routing chosen by task, cost, latency and rules, validated with your own evals. A live OpenCode demo shows roughly 3x lower session cost at similar quality, though the evidence is one vendor demo.

- Techniques: Per-task model pools with ordered failover; Natural-language routing preferences plus hard rules; Side-by-side routed vs single-model agent runs with live cost tracking; Eval-gated routing with feedback loop
- Tools: Plano (open-source proxy and routing model), OpenCode, Claude Opus, Claude Sonnet 5, GLM 5.2, GPT 5.2, Llama 4 Maverick (caption reads 'long before Maverick')

## [How America Turned Against the AI Industry?](../videos/xu-i-Zeu46s.md)
`xu-i-Zeu46s` · Kai Explains · 2026-09-02 · q2 · intro · other · also: governance-compliance, product-ux

Kai Explains essay on why US public opinion turned against AI and data centers: broken promises, local costs, and water as the proxy grievance. Opinion piece, not a technical talk.

- Techniques: Tangible-unit framing for infrastructure costs; Treat stated concerns as evidence before explaining; Cost-locality check on advocacy
- Tools: ChatGPT

## [ChatGPT is in big Trouble (AI Bubble)!](../videos/EK8y8O5st_M.md)
`EK8y8O5st_M` · Kai Explains · 2026-09-02 · q3 · intro · news · also: models-research, enterprise-adoption

Kai Explains argues that leaked 2025 OpenAI financials, huge compute commitments, and lost enterprise and coding share make ChatGPT's position structurally weak. The figures are reported second-hand, not audited.

- Techniques: Route each job to the cheapest model that meets its quality bar; Judge AI vendor health by unit economics, not user count
- Tools: ChatGPT, GPT-5, GPT-5.4, Gemini, Gemini 3, Claude, DeepSeek, Kimi, AWS Bedrock, Azure AI Foundry, Google Vertex, Sora

## [MCP Was Wrong From The Start (They Just Fixed It)](../videos/f4mI3d-nTrI.md)
`f4mI3d-nTrI` · Better Stack · 2026-09-02 · q3 · practitioner · news · also: mcp-and-tools, agent-architecture

Walkthrough of the MCP 2026-07-28 spec, which makes the protocol stateless: no handshake, no session IDs, explicit state handles, input-required round trips, and official tasks for long-running calls.

- Techniques: Stateless MCP tool calls; Explicit state handle; Input-required round trip; Async tasks for slow tools; Gateway routing on MCP headers; Cache hints on list calls; SDK migration
- Tools: MCP (spec version 2026-07-28), MCP TypeScript SDK v2 (separate server and client packages), MCP SDK codemod, Cloudflare Workers, Cloudflare Durable Objects, Google Cloud Run, Redis

## [Can a Local LLM Actually Replace Claude or Codex for Coding?](../videos/uefMWJ1GBWg.md)
`uefMWJ1GBWg` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: local-ai, coding-agents, token-cost-efficiency

Kai Explains on whether a local open-weight model can replace Claude Code or Codex for coding. Verdict: memory and tool-calling decide it, the hybrid and free-tier route wins on cost for most people, and local is a daily driver only for bounded work.

- Techniques: Test the harness on a trivial task before a big job; Size hardware as weights plus context; Prefer higher quantization on a smaller model for tool use; Rewire a cloud CLI to a local endpoint; Hybrid routing: frontier plans, local executes; Sandbox any local agent that can run shell commands; Break-even math for local versus cloud; Price agent API usage on cached input
- Tools: Claude Code, Codex, ChatGPT, Ollama, llama.cpp, MLX, LM Studio, Aider, OpenCode, Cline (transcribed as Klein), Qwen Code (transcribed as QuenCode; model not named), OpenRouter

## [Xiaomi AI Cube vs DGX Spark! The prototype that can change local AI](../videos/SeQ8qou_i-E.md)
`SeQ8qou_i-E` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, inference-serving

Xiaomi AI Cube vs DGX Spark: headline specs measure different things. Batch size, concurrency, serving config and the network decide real throughput; the Cube is still unshipped.

- Techniques: Normalize vendor throughput claims before comparing; Benchmark a box at several concurrency levels; Check the serving stack's defaults before judging hardware; Test network sensitivity before scaling out; Fit check and payback arithmetic for a purchase
- Tools: Xiaomi AI Cube (D100 chip, prototype, unannounced), NVIDIA DGX Spark, Xiaomi MIMO (3B model at the batch-one lab result), MIMO 2.5 (Xiaomi flagship, over 300B parameters), llama.cpp, vLLM, X-ring backend (name as spoken in the transcript, unverified), HBM4 (memory in data-center GPUs), NVIDIA H200 (comparison reference), Xiaomi phone processor (113 GB/s memory bandwidth, not the Cube chip)

## [Best Hardware for Running Local LLMs in 2026: Mac vs NVIDIA vs Cloud](../videos/gQ7iJuciMg0.md)
`gQ7iJuciMg0` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, inference-serving, token-cost-efficiency

Compares Mac Mini M5 Pro, DGX Spark, RTX 5090 and rented GPUs for local LLMs at current prices, arguing that prefill and decode need different hardware and that renting usually wins on cost.

- Techniques: Evaluate hardware separately for prefill (TTFT) and decode (tokens/sec); Split prefill and decode across machines; Budget memory headroom, not just model fit; Measure real memory bandwidth, not spec sheet bandwidth; Rent-vs-buy break-even calculation; Size for the model you run this week; Route by workload
- Tools: Mac Mini M5 / M5 Pro (Apple), Mac Mini M4 Pro (Apple, prior generation), Mac Studio, M3 Ultra (Apple), M5 Ultra (Apple), NVIDIA DGX Spark, NVIDIA RTX 5090, NVIDIA H100 (rental), Strix Halo (AMD, 128GB box), vLLM, DeepSeek V4 Flash (304B parameters), speculative decoding (on the 5090 owner's 27B setup)

## [The Study NVIDIA Doesn't Want You to See](../videos/5TFzJ38ae1s.md)
`5TFzJ38ae1s` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, inference-serving, token-cost-efficiency

Kai Explains reads the "Dumpster Cluster" paper (128 used V100s serving Llama models) past its viral 35x tokens-per-dollar claim. Capex-only, 8B-only numbers flip at 70B once electricity, failures and software support are counted.

- Techniques: Lifetime cost-per-token accounting; Operational failure budgeting for used GPU fleets; Track software support as a separate lifecycle
- Tools: Dumpster Cluster paper (128x V100 SXM2 cluster study), NVIDIA V100, NVIDIA A100, NVIDIA H100, NVIDIA B200, vLLM (0.17 for B200 runs, 0.6 for H100/A100 runs, per the video), PyTorch 2.11 (dropped Volta from CUDA 12.8/12.9 pre-built binaries), CUDA (compute capability 7.0 = Volta), CoreWeave Vera Rubin (vendor tokens-per-MW claim)

## [4 Billion Free LLM Tokens… One API (FreeLLMAPI)](../videos/sHOwbyMbun0.md)
`sHOwbyMbun0` · Better Stack · 2026-09-02 · q3 · intro · review · also: token-cost-efficiency, dev-tools

Better Stack walkthrough of FreeLLM API, a self-hosted gateway that pools free LLM tiers from about 28 providers behind one OpenAI-compatible endpoint with failover. Useful for cheap prototyping; the speaker warns free-tier quality and availability drift.

- Techniques: Single OpenAI-compatible endpoint over pooled free tiers; Choose a routing strategy in the dashboard; Smoke-test in the Playground before wiring tools; Check monthly token usage per model before long runs; Reserve the pool for latency-tolerant work
- Tools: FreeLLM API (Free LLM API), Docker, Docker Compose, Git, OpenAI-compatible client SDK, OpenRouter, LiteLLM, Grok (xAI), Cerebras, Google models, Mistral, NVIDIA (free models mentioned as 'open route')

## [I replaced my entire tech stack with Postgres](../videos/MZfhhl6ej-k.md)
`MZfhhl6ej-k` · Better Stack · 2026-09-02 · q3 · intro · tutorial · also: dev-tools, rag-retrieval

Better Stack walks through replacing separate cache, vector DB, search, geo, cron and document-store services with Postgres features, framed for small apps rather than scale.

- Techniques: Postgres as a cache using UNLOGGED tables; pgvector for embeddings and similarity search; Full-text search with a generated tsvector column and a GIN index; Geospatial radius and polygon queries with PostGIS; Scheduled SQL with pg_cron; Document storage with JSONB, a GIN index and containment queries
- Tools: PostgreSQL, pgvector, PostGIS, pg_cron, JSONB, DocumentDB, Redis, Memcached, Pinecone, Qdrant, Elasticsearch, MongoDB

## [Best Hardware for Running Local LLMs in 2026: Mac vs NVIDIA vs Cloud](../videos/sR8sJ2mybQU.md)
`sR8sJ2mybQU` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, inference-serving, token-cost-efficiency

Kai Explains on picking local-LLM hardware in 2026 (Mac Studio vs RTX vs rented cloud GPUs), with measured vLLM vs llama.cpp and multi-GPU scaling results and a budget-based buying guide.

- Techniques: Pick the serving framework by VRAM headroom; Estimate decode speed from memory bandwidth, then confirm with your own benchmark; Pair MoE models with bandwidth-limited hardware; Cap consumer multi-GPU at two cards, or run one server per GPU; Breakeven check before renting or buying; Split work between local and frontier models
- Tools: Qwen3 Coder Next (80B MoE, Q4 about 46 GB, 70.6 SWE-bench as stated), Qwen 3.6 27B dense (16 GB, 77.2 SWE-bench as stated; transcript spells it 'Quen 3.627B'), Claude Sonnet 4.6, Claude Opus, GPT-4 (mentioned only as an example of a frontier API), vLLM, llama.cpp, Apple MLX, CUDA graphs, NVLink, PCIe, Mac Studio M4 Max 128 GB

## [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../videos/maRzp4kImJ4.md)
`maRzp4kImJ4` · AI Engineer · 2026-08-18 · q4 · deep · talk · also: training-finetuning-rl, inference-serving

Nan Jiang (Modal) argues RL rollouts can run on scattered, elastic GPUs across regions if the trainer syncs only a bit-exact sparse diff of serving-precision weights instead of full checkpoints.

- Techniques: Decoupled rollout islands; Bit-exact sparse weight diff; Versioned request contract; Sidecar version gate; Floor-based update-visibility check
- Tools: Modal, SGLang, vLLM, Adam, BF16, FP8, NVFP4, RDMA, Stitch

## [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../videos/CoEIs6Xm8m8.md)
`CoEIs6Xm8m8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: token-cost-efficiency, models-research, security-guardrails

Cline's founder argues open-weight models plus verification-heavy agent harnesses will win on cost as closed labs subsidize subscriptions for lock-in, citing a supply-chain attack and spend data.

- Techniques: Put quality in the harness, not the model; Default route to cheaper open-weight models in an internal gateway; Head-to-head test on a real bug from your own repo; Set usage limits per user on the provider dashboard
- Tools: Claude Code, Codex, Cursor, Cline, LiteLLM, GLM, Kimi, DeepSeek, Opus, Open Compute

## [Security Firewall for Agents — Ryan Dahl, Deno](../videos/MkRYPFIMCSA.md)
`MkRYPFIMCSA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: security-guardrails, governance-compliance

Ryan Dahl (Deno) on Claw Patrol, an open-source byte-level egress proxy that gates what production agents send to databases, Kubernetes and SaaS, with rules, credential injection and human or LLM approval.

- Techniques: Byte-level egress proxy for agents; Credential injection at the proxy; Policy-as-code in HCL with Git review; Chained verdicts: rule, LLM judge, then human approval; Network-level placement with existing identity
- Tools: OpenClaw, Claw Patrol, Deno Deploy, PostgreSQL, Kubernetes, ClickHouse, AWS (Sigv4), GitHub, Slack, PagerDuty, HCL, Terraform

## [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../videos/Ki980nV0__0.md)
`Ki980nV0__0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, evals

Dhruv Batra (Yutori) argues the long-tail web will be driven by pixel-based computer-use agents rather than new APIs, and shows his Navigator model's accuracy and cost per task.

- Techniques: Screenshot-in, action-out computer-use loop; Code-on-demand as a browser action; Pixel-based success check; Parallel sandboxed-browser fan-out; Read the async data call, not the initial HTML; Cost-per-task as the headline metric
- Tools: Navigator (Yutori computer-use model), OnlineMind2Web benchmark, Chrome extension for browser actions, MCP servers and web MCP, Opus 4.7 and GPT 5.5 (comparison models), Cloud sandbox browsers

## [MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal](../videos/s4r6nk5WsZw.md)
`s4r6nk5WsZw` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: mcp-and-tools, agent-architecture

Cornelia Davis (Temporal) explains why no MCP clients support MCP Tasks (async long-running tools) in v1, shows live demos of durable purchase-order and invoice workflows, and walks through the v2 changes that make tasks stateless and extension-based.

- Techniques: Map task lifecycle onto a domain state machine; Signal into a long-running workflow for approvals; Client-side task tracker workflow; Parallel back-office steps beside an async tool call
- Tools: MCP Tasks, FastMCP, Temporal

## [Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs](../videos/Bck7ABCZRZI.md)
`Bck7ABCZRZI` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: token-cost-efficiency, local-ai, governance-compliance

Thiyagarajan Maruthavanan (Kalmantic Labs) argues teams should rent inference to learn and own it to earn, using his own runaway-cost incident and enterprise objections to self-hosting as evidence.

- Techniques: Per-key spend monitoring with a cutoff; Input compression and context management in agent loops; Rent-to-own decision gate; Small local inference box for personal agents
- Tools: DGX Spark, Headroom, JustTokenMax, JustInfo, Suno, NemoClaw

## [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face](../videos/lyL5QhgIOxc.md)
`lyL5QhgIOxc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: rag-retrieval, data-engineering


- Techniques: Insert-time search tokens in a denormalized read collection; Lucene-backed autocomplete instead of regex scans; Read-replica routing by consistency class; Hidden analytics replica; Two-layer autoscaling with event-driven pod scaling
- Tools: MongoDB Atlas, Atlas Search, Apache Lucene, Kubernetes, Horizontal Pod Autoscaler, KEDA, Cast.ai, AWS S3, AWS Redshift

## [Notion's Token Town — Sarah Sachs, Notion](../videos/-I5W5QVAT8E.md)
`-I5W5QVAT8E` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: token-cost-efficiency, enterprise-adoption, security-guardrails

Notion's head of AI engineering on keeping AI costs sustainable: stay model-agnostic, route traffic by task difficulty, use open-weight and plain code for simple steps, and evaluate whole trajectories instead of single calls.

- Techniques: Model-agnostic harness with an auto-router; Traffic tiering by task difficulty; Trajectory-level eval of cost, latency and success; Open-weight evaluation on your own system; Code and CLI for deterministic steps; Cross-vendor review chain for agent PRs; Lethal trifecta check on agent systems
- Tools: Claude Code, Claude, Codex, Decagon, Parallel (web search provider), Notion Workers, Notion AI Manage Agent, Kimi 2.6 (as transcribed), GLM 5.2 (as transcribed), GPT 5.2 (as transcribed)

## [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](../videos/1UmZHb_E_SM.md)
`1UmZHb_E_SM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: rag-retrieval, data-engineering

Oxylabs' product manager on how public web data infrastructure feeds AI systems: how a video API, a sub-second SERP API and a 60k-rps scraper grew out of repeated client requests, latency cuts and load tests.

- Techniques: Iterate from client requests into an internal library; Narrow the response to what the AI consumer needs; Stage-by-stage latency audit; Realistic load testing with gradual ramp-up; Account for observability as load
- Tools: Oxylabs Fast Search API, headless browsers, proxy network

## [Designing Voice Agents for Real Conversations - Chintan Agrawal & Daniel Wirjo, AWS](../videos/hMlLw1LeIK8.md)
`hMlLw1LeIK8` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: voice-multimodal

AWS solutions architects walk through turn-taking in voice agents: three levels from Silero VAD silence timers to Smart Turn, plus latency budgets and production issues. Includes live Pipecat demos.

- Techniques: Hybrid VAD + learned end-of-turn model with timer fallback; Interruption classification at barge-in; Per-stage latency budget with P50 and P95 tracking; Co-location to remove network hops; Session pruning or reset for long voice sessions; Config-only swap between turn-detection strategies for A/B tests
- Tools: Pipecat, Silero VAD, Smart Turn v3, Cartesia (STT and Sonic TTS), Deepgram Nova 3, Claude Haiku, GPT-4.1, Nemotron 3 Ultra

## [The State of Model Routing — NVIDIA, Cognition, OpenRouter](../videos/QHBjufYK8TA.md)
`QHBjufYK8TA` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · also: token-cost-efficiency, multi-agent, inference-serving

Panel from Cognition, NVIDIA and OpenRouter on model routing: frontier models plan and delegate to cheaper models, and the hard parts are detecting when a small model is out of depth and keeping cache costs low.

- Techniques: Frontier-planner, cheap-executor split; Frontier watcher with escalation; Persistent sidekick sub-agent; Reference-based handoff; Piggyback checks on cache refresh; Hidden-state probes for lost-ness; Routing from production signals; Ask the model why, then regression-test the prompt; Privacy-aware local/cloud split
- Tools: Devin, Cognition Fusion, OpenRouter Fusion, OpenRouter Pareto Code, NVIDIA Nemotron, NVIDIA Dynamo, NVIDIA DGX Spark, OpenClaw, TerminalBench, LMArena

## [Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft](../videos/fnLBmfsI_Fg.md)
`fnLBmfsI_Fg` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: voice-multimodal, agent-architecture

Microsoft's ACE live voice tutor uses a small model (Haiku 4.5) for speech only, moving reasoning, lesson state and planning into a code state machine to hit about 900ms response time.

- Techniques: Externalised state machine for a small speaking model; Per-turn summary handoff; Strict rules to keep small models on track; Model selection by latency budget
- Tools: Claude Opus 4.7, Claude Haiku 4.5

## [Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA](../videos/XjI-AR4pt7Y.md)
`XjI-AR4pt7Y` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: security-guardrails, governance-compliance

Production ML breaches are mostly boring misconfigurations, not AI attacks; the talk argues for layered infra security, a maturity model, and budgeting guardrails by latency overhead tier.

- Techniques: Tiered guardrail budget; Maturity self-assessment with overhead budgets; Least privilege with short-lived credentials; Segment by service identity, not network location; Secrets and model artifacts hygiene; Treat ML infra like a database
- Tools: Ray, NIST AI RMF

## [AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix](../videos/CgsWxRUY5Eo.md)
`CgsWxRUY5Eo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: coding-agents, pr-code-review, context-engineering

Netflix's playbook for using coding agents on production profiling data to find CPU hot spots, open reviewed fixes, and grow a shared pattern catalog, with a canary gate and an autonomy ladder.

- Techniques: Profile-to-PR agent pipeline; Central anti-pattern catalog in git; Cross-repo sweep for recurring patterns; Canary-gated review; Shift-left catalog injection; Scheduled fixed workflow before autonomy
- Tools: Continuous profilers (sampled call stacks with CPU time), Git and code search across repos, Canary deployment infrastructure, TorchFix (public PyTorch anti-pattern catalog), Spectator (metrics library, named as the source of the counter-object pattern)

## [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../videos/jQDXzEVHMSE.md)
`jQDXzEVHMSE` · AI Engineer · 2026-08-18 · q3 · practitioner · interview · also: rag-retrieval, testing-verification

Gergely Orosz interviews Simon Eskildsen, founder of Turbopuffer, on his path from Shopify infrastructure to building an S3-backed search engine, napkin-math habits, CPU scarcity and startup financing. Mostly origin story, little AI content.

- Techniques: Napkin-math latency and cost estimate before benchmarking; Proxy-based fault injection in CI; Object storage as the system of record with an HTTP cache in front; Design for tail latency and round trips; Batch durable writes; Ship simplest version then probe demand
- Tools: Toxiproxy, NGINX, Amazon S3, MySQL, Rails, Postgres, pgAnalyze, Docker, Rust, GDB, Redis, NVMe SSD

## [Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase](../videos/u1yaOeEX4e8.md)
`u1yaOeEX4e8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, data-engineering

JPMorgan payments lead on modeling each API request as a short-lived execution DAG, then using per-segment baselines and drift categories to detect anomalies with fewer false alarms.

- Techniques: Request-as-DAG from traces; Tiered detection; Segmented baselines; Drift classification before action; Async telemetry to hot and recon paths; Staged automated remediation; Synthetic training data for detectors
- Tools: OpenTelemetry, Kafka, Neo4j (mentioned as contrast), KL divergence, MMD, EWMA (exponential moving average)

## [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../videos/Ot4OPrPH4xY.md)
`Ot4OPrPH4xY` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: rag-retrieval, data-engineering

Bright Data's product lead argues that web data is becoming agent context, that repeated queries to paid context services get expensive, and that owning the data can beat renting it past a volume tipping point.

- Techniques: Field-by-field enrichment agent loop; Hybrid search plus direct scrapers; Basic heuristic entity merge; Break-even analysis for build vs rent; Self-healing scrapers
- Tools: Bright Data, Scraper Studio, Exa, Parallel, Tavily, New.com, Amazon AgentCore, Microsoft WebIQ, ZoomInfo / gtm.ai, SERP API, Claude native web search, Opus 4.8

## ["The biggest challenge in your stack? Evals, Evals, Evals" - 2026 State of AI Engineering results](../videos/RGe6EjucbzI.md)
`RGe6EjucbzI` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: evals, enterprise-adoption, models-research

Bar Yeren (Amplify) reads out the 2026 State of AI Engineering survey (1,048 respondents): evals remain the top challenge, teams run multi-model stacks, cost is a first-class constraint, and agents now mostly have write access.

- Techniques: Intent-to-adopt ratio; Routing by task type across models; Monitoring cost and token usage alongside quality; Human-in-the-loop approvals and permission gating for write-enabled agents
- Tools: Notion, Vercel, Nano Banana, ChatGPT Images 2.0

## [This Free Go Alternative to Firebase is Just One File](../videos/WZoC1HA1vec.md)
`WZoC1HA1vec` · Better Stack · 2026-08-02 · q3 · intro · review · also: dev-tools

Walkthrough of PocketBase, a single Go binary with embedded SQLite giving realtime DB, auth and file storage, tested on a React bug tracker, with a VPS deployment and pre-v1 caveats.

- Techniques: Singleton SDK client module; Auth state from the auth store; Load-then-subscribe for live lists; Multipart create with a file attachment; Collection API rules for access control; Hooks for server-side side effects; Single-VPS deployment with persistent data
- Tools: PocketBase, SQLite, Go, JavaScript, TypeScript, React, Supabase, Firebase, Render, Railway, OpenCode, Claude Code

## [WebAssembly 3.0: It's Not Just for Browsers Anymore](../videos/McB108-FExg.md)
`McB108-FExg` · Kai Explains · 2026-08-02 · q3 · intro · news · also: sandboxing-execution, dev-tools

Kai Explains argues WebAssembly 3.0 (component model plus WASI) makes Wasm a cross-language, server and edge runtime, while JavaScript keeps the DOM and is not being replaced.

- Techniques: Polyglot components via the component model; Wasm instead of containers for short-lived edge or per-request execution; Split UI from logic across the JS/Wasm boundary
- Tools: WebAssembly 3.0, Wasm component model, WASI, Spin framework, Cloudflare Workers, Fastly Compute, Docker, Chrome DevTools, npm, React, Figma, Photoshop

## [OmniRoute + Claude Code is INSANE (Why I Cancelled My Claude Code Subscription)](../videos/k26fT4athQs.md)
`k26fT4athQs` · Kai Explains · 2026-08-02 · q2 · intro · review · also: token-cost-efficiency, coding-agents

A host explains dropping a Claude Code subscription for OmniRoute, a self-run gateway that routes Claude Code to many providers with fallback, token compression and free tiers, and says when to keep a paid Opus key.

- Techniques: Local OpenAI-compatible gateway in front of a coding agent; Mid-request provider fallback; Tool-output compression before the model call; Per-task model routing with a paid escape hatch; Semantic cache for repeated questions
- Tools: OmniRoute (also captioned as OmniRoot; self-hosted LLM gateway, version not stated), Claude Code (agent CLI), Anthropic Claude Opus (paid model for hard tasks), RTK (token-compression pass), Caveman (token-compression pass), MCP (gateway ships about 94 built-in tools over Model Context Protocol)

## [What Would It Cost to Run Claude Fable 5 Locally?](../videos/fXWFSTSvnVM.md)
`fXWFSTSvnVM` · Kai Explains · 2026-08-02 · q3 · intro · other · also: local-ai, inference-serving

Back-of-envelope memory and concurrency math on what it would take to self-host a frontier-scale open model (Kimi K3 as a stand-in for Claude Fable 5): a Mac Studio or 4xH100 cannot hold it, and serving 100 people is a data-center sizing problem.

- Techniques: Weight memory floor estimate; Concurrency sizing from arrival rate and service time; Hybrid local and cloud routing; Rent-before-buy pilot
- Tools: Claude Fable 5 (Anthropic model; weights not public, used only as the question), Kimi K3 (open-weight model, 2.8T parameters, MXFP4 weights as stated; used as the sizing example), NVIDIA DGX B200 (8x B200 GPUs, 1.44 TB GPU memory), NVIDIA DGX B300 (8x B300 GPUs, about 2.3 TB GPU memory), NVIDIA H100 (80 GB each, 4 units discussed), Apple Mac Studio (up to 512 GB unified memory), MXFP4 (4-bit weight format, called MXFFP4 in the auto-captions)

## [What Would It Cost to Run Kimi K3 Locally?](../videos/ni5P3gT8OXo.md)
`ni5P3gT8OXo` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: local-ai, inference-serving

Napkin math for running Kimi K3 locally: ~1.5 TB of 4-bit weights rules out Mac Studio and 4xH100, 8xB200 is barely enough, and serving 100 users is a data-center project.

- Techniques: Weight memory estimate for a quantized model; Headroom budget for a serving node; Concurrency sizing instead of user counting; Peak-moment plus prompt-length sizing; Hybrid routing: local for routine, cloud for hard; Rent before you buy
- Tools: Kimi K3, Hugging Face, Mac Studio, NVIDIA H100, NVIDIA B200, NVIDIA B300, NVIDIA DGX B200, NVIDIA DGX B300, MXFP4 (4-bit format, as named in transcript), Claude, GPT

## [MCP Is Getting Its Biggest Update Ever (No One's Ready)](../videos/k5f1uID3GcU.md)
`k5f1uID3GcU` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: mcp-and-tools, agent-architecture, security-guardrails

MCP's July 28 rewrite drops the handshake and session ID so any replica can serve any request; state moves into owner-checked handles, and auth fragmentation across clients is the bigger unresolved problem.

- Techniques: Make stateful MCP tools own their handles; Round-trip state through the client as a sealed blob; Split pure tools from stateful tools in deployment; Gateway and proxy checklist for the MCP change; Test each server against every major client; Load tool definitions on demand in the client
- Tools: MCP (Model Context Protocol), July 28 spec revision, OAuth 2.1, Claude Code, Claude.ai, Anthropic API, ChatGPT, Google Cloud, VS Code, Redis, Salesforce, JIRA, Snowflake

## [The Guy Who Coined "Event Gateways" Explains Why Webhooks Are Dying | Better Stack Podcast Ep. 17](../videos/ElaEGr2t9XQ.md)
`ElaEGr2t9XQ` · Better Stack · 2026-08-02 · q3 · practitioner · interview · also: agent-architecture, product-ux, dev-tools

Hookdeck's founder explains why he built an event gateway and the open-source Outpost to replace fragile webhook handling with queuing, replay, push-based rate control and per-vendor latency monitoring. Substantive but vendor-led.

- Techniques: Push-based webhook intake in front of your endpoint; Respond fast, queue the work; Per-vendor delivery latency baseline and alerting; Per-tenant queues with a shared push consumer; Event destinations instead of HTTP webhook transport; Open-source-first with a managed twin; Verify agent-written contributions against real APIs
- Tools: Hookdeck (Event Gateway), Outpost (Apache 2.0, open source), Hookdeck Radar, Kafka, RabbitMQ, Amazon SQS, Google Cloud Pub/Sub, AWS EventBridge, Azure Event Grid, Kong event gateway, Cloudflare Queues, BullMQ

## [Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua](../videos/ZSQb5fzRFPw.md)
`ZSQb5fzRFPw` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: voice-multimodal, sandboxing-execution, evals

Cua's team presents "Computer-Use 2.0": a background computer-use driver (Cua Driver), a multi-platform benchmark (CuaBench, including a KiCad electrical-engineering set), and warm sandbox pools (CuaFleet) that cut idle GPU time in RL training.

- Techniques: Two-tier background action with fallback; Window-scoped observation; Single-file cross-platform task definition; Adversarial pre-validation of evals; Trajectory forking for world-model probes; Demand-autoscaled warm pool for sandboxes
- Tools: Cua Driver, CuaBench, CuaFleet, Codex computer-use model, TerminalBench, Harbor, Android activity framework, Hermes harness, KiCad

## [Modern Post-Training: A Deep Dive  — Will Brown, Prime Intellect](../videos/V-EDrhIhHzQ.md)
`V-EDrhIhHzQ` · AI Engineer · 2026-07-18 · q4 · deep · workshop · also: training-finetuning-rl, evals, agent-architecture

Will Brown (Prime Intellect) walks through modern post-training: environments as evals, the verifiers v1 task/harness/runtime split, async RL with an interception server, and the PrimeRL trainer.

- Techniques: Task / harness / runtime decomposition; Fake base URL interception for RL on real harnesses; Async rollout batching with off-policy tolerance; Message-level trace with token mapping; Algorithm and loss separation with a registry; Group-relative shaping for length and efficiency; Same-task eval CLI with swappable harness and runtime
- Tools: verifiers, PrimeRL, Renderers, TorchTitan, Megatron, Harbor, NemoGym, OpenEnv, Hugging Face datasets, uv, Docker, Claude Code

## [The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab](../videos/sum9DgexFRQ.md)
`sum9DgexFRQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: mcp-and-tools, multi-agent, security-guardrails

Ramesh Raskar and Maria of MIT's Project Nanda outline an open infrastructure for a web of AI agents: a signed discovery index, agent hosting, and NandaTown, a simulator for testing agent networks before they go live.

- Techniques: Signed agent facts record and agent card; Message box in front of the agent runtime; Adaptive endpoint resolution; Sleep and wake hosting; Tiered simulation with scripted agents, then LLM agents; Onboarding in three tiers
- Tools: Nanda index, NandaTown, OpenClaw, Maritime, AWS, DNS, YAML

## [When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis](../videos/XovaGv4f39A.md)
`XovaGv4f39A` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: rag-retrieval, context-engineering, multi-agent

Luis Romero-Sevilla (Orbis) on Extended Cache Augmented Generation (ECAG): for large, frequently replaced, densely interrelated document collections, split docs across parallel KV-cached context buckets and let a supervisor model interrogate them, instead of RAG or GraphRAG.

- Techniques: Parallel context buckets with a supervisor (ECAG); Dropping topical sharding for bucketing; Caching KV state per context bucket
- Tools: GraphRAG, vector database, KV cache

## [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](../videos/uiP88SpCi1Q.md)
`uiP88SpCi1Q` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: token-cost-efficiency, context-engineering, agent-architecture

An AWS developer advocate lists five ways to cut agent token spend: cache the system prompt, route by task difficulty, offload large tool results, cap tool loops, and trim conversation history, with per-tool observability to check each one.

- Techniques: System prompt and tool caching; Difficulty-based model routing; Tool result offload and summarization; Max-iteration cap on tool loops; Per-tool loop and latency observability; Sliding window history with summarization
- Tools: Strands Agents, Claude Haiku, Claude Sonnet

## [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](../videos/spNAUEgq_A8.md)
`spNAUEgq_A8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: multi-agent, context-engineering, agent-architecture

Justin Schroeder (Standard Agents) argues that small, isolated domain-specific agents composed under a coordinator beat ever-growing context-stuffed general agents on cost, scope, portability and scaling.

- Techniques: Composition of isolated domain agents; Scoped delegation requests; Per-task model routing; Hook-injected runtime facts; Capability scoping per agent; Recursive sub-agent tree
- Tools: Claude, Codex, OpenClaw, Hermes, MCP, Vercel AI SDK, Vercel Eve, Figma, Playwright, Gmail, Google Sheets, Google Workspace

## [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](../videos/OqM67QG_Ikk.md)
`OqM67QG_Ikk` · AI Engineer · 2026-07-18 · q4 · deep · talk · also: sandboxing-execution, security-guardrails, agent-architecture

A first-principles tour of why agent code needs sandboxes, comparing fork/exec, containers, gVisor and microVMs, then how to add disk snapshots, restore and multi-node scheduling for OpenAI-scale agent sandboxes.

- Techniques: Isolation ladder for untrusted tool execution; Driving a microVM through its VMM API; Per-device jailing for emulated devices; Incremental block-level disk snapshot; Acknowledge snapshot before upload completes; Tiered always-on block storage; Snapshot-aware scheduling; Startup latency hybrid
- Tools: gVisor, Firecracker, Cloud Hypervisor, CrossVM, QEMU, KVM, virtio, vsock, seccomp, VFIO, NBD, FIEMAP

## [Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs](../videos/65X0pQ6Lmbg.md)
`65X0pQ6Lmbg` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: voice-multimodal, product-ux

Allen Pike (Forestwalk Labs) on why voice input with visual output beats voice-to-voice for AI now, and the latency tactics (fast small model, eager short inference turns, stable prompt prefixes) that make it feel responsive.

- Techniques: Two-tier model split (fast responder plus async thinker); Eager short-interval inference; Prefix-stable context layout for caching; Visual response envelope
- Tools: Linear, Slack, GPT-5 Mini, Haiku

## [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](../videos/APh1Vx0oLmQ.md)
`APh1Vx0oLmQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: agent-architecture, security-guardrails, observability

Nishant Gupta (Meta Superintelligence Labs) argues that agent reliability is an infrastructure problem: treat models as probabilistic, keep the platform deterministic, and let infrastructure validate and enforce what the model proposes.

- Techniques: Propose, validate, enforce split; Tool isolation with circuit breakers; Controlled recovery instead of open retries; Decision-chain tracing; Per-agent limits and cost quotas; Layered defence for agent actions; Humans as exception handlers

## [Big Tech Is Buying Up Open Source... Vite Is Next](../videos/wxKRGs7FS6s.md)
`wxKRGs7FS6s` · Better Stack · 2026-07-02 · q2 · intro · news · also: dev-tools

Better Stack's take on Cloudflare buying VoidZero (Vite, Vitest, Rolldown, Oxc): what the deal promises, why it happened, and the consolidation risk for open source.

- Techniques: Vet a dependency after a vendor acquisition
- Tools: Vite, Vitest (called 'Vite for Test' in the captions), Rolldown, Oxc, Vite+ ('Vite Plus' in the captions), Vue, Void (VoidZero deployment platform), Cloudflare Vite plugin, Cloudflare CLI (cfdev, cfdeploy, announced), Astro, Bun, uv

## [I Turned Cheap Cloud Storage Into a 1PB Local Drive (With JuiceFS)](../videos/ZoBEQWxosGg.md)
`ZoBEQWxosGg` · Better Stack · 2026-07-02 · q3 · intro · tutorial · also: dev-tools, observability

Walkthrough of JuiceFS, a POSIX file system that stores data in cheap S3-style object storage with metadata in Redis and a local SSD cache, plus wiring its Prometheus metrics into Better Stack.

- Techniques: JuiceFS volume with Redis metadata and S3 data; Cold vs warm read benchmark with dd; Scraping JuiceFS metrics into a hosted dashboard
- Tools: JuiceFS, Redis, PostgreSQL, TiKV, Amazon S3, Google Cloud Storage, Backblaze B2, Docker, macFUSE, dd, ngrok, Prometheus

## [Reachy Mini: the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face](../videos/0jeZfjJMfmo.md)
`0jeZfjJMfmo` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, inference-serving

Hugging Face's Andres Marafioti on the open-source $300-450 Reachy Mini robot, its voice pipeline, and how a streaming TTS model was made fast enough for real-time voice agents.

- Techniques: Stream TTS audio instead of generating full utterances; Static KV cache plus graph capture for autoregressive audio models; Partial STT every 150 ms; Separate scaling of LLM inference from stateful conversation nodes; Measure the whole latency path, not just the model; Codex-driven hardware app development
- Tools: Reachy Mini, Raspberry Pi, Codex, Parakeet, Qwen3-TTS, Qwen 3.5 27B, Kokoro, Voxtral, Hugging Face Inference Endpoints, speech-to-speech pipeline, GPT Realtime

## [Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat](../videos/F1DYkY1BlfM.md)
`F1DYkY1BlfM` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: sandboxing-execution, security-guardrails

Red Hat's Sally Ann O'Malley runs OpenClaw agents in Podman containers, keeps API keys as secret refs, and lifts the same setup to Kubernetes; the talk is a live demo with a pitch for containers as the default agent sandbox.

- Techniques: Podman secrets + secret-ref indirection for agent API keys; Container as the agent sandbox with explicit host grants; Mount the agent's tool directory at startup; Named volume for runtime state with scheduled backup; Local-to-Kubernetes lift with the same image; Company baseline image with per-user layer; SSH sandbox for remote execution; Installer that converts env vars to secret refs and sets providers
- Tools: OpenClaw, Podman, Podman secrets, Docker, Kubernetes, OpenShift, kind, systemd, OpenRouter, Anthropic, Gemma, OpenTelemetry

## [Run Frontier AI at Home — Alex Cheema, EXO Labs](../videos/ESbWpPT_9-o.md)
`ESbWpPT_9-o` · AI Engineer · 2026-06-18 · q3 · deep · talk · also: local-ai, inference-serving

EXO Labs' Alex Cheema argues decode is memory-bound, so local frontier inference is a memory, bandwidth and energy problem. He demos Mac clusters over Thunderbolt RDMA and a Mac plus DGX Spark prefill/decode split.

- Techniques: Kernel fusion of redundant launches; Cache-stable prompt prefix in the harness; Prefill/decode disaggregation across devices; Tensor parallelism over RDMA; Full-replica weights with append-only event logs for cluster state; Expose each node over HTTP and reach it through a mesh VPN; Budget-based Pareto benchmarking; Hypothesis-driven auto-research
- Tools: EXO, Claude Code, OpenCode, OpenClaw, Tailscale, MLX, llama.cpp, Thunderbolt 5 RDMA, 10GbE

## [How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind](../videos/7gujZrJ9L5I.md)
`7gujZrJ9L5I` · AI Engineer · 2026-06-18 · q3 · intro · panel · also: agent-architecture, coding-agents, skills-self-improvement

A Google DeepMind panel on running coding and research agents at Google scale, covering shared workspaces, quota and cost control, skill sprawl, internal observability, and PR review.

- Techniques: Shared file-system workspace between agent stages; Editable plan gate before execution; Scratchpad notes as a reviewable trace; Mock compute for harness testing; Trajectory store plus hierarchical drill-down; Per-language fine-tuned review model plus per-product review prompts; Transparent model fallback under the harness; Skills plus guardrailed CLI over MCP for internal tools
- Tools: Antigravity, Gemini, Gemma 4, Deep Research, Jules, MCP, OpenClaw

## [RAG is dead, right?? — Kuba Rogut, Turbopuffer](../videos/UM6sFg_jdlE.md)
`UM6sFg_jdlE` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: rag-retrieval, coding-agents, context-engineering

Kuba Rogut (Turbopuffer) argues that "RAG is dead" misreads the problem: retrieval should be a toolbox (vector, BM25, grep, filters) used in iterative agent loops, and embeddings work best as precomputed cache compute.

- Techniques: Multi-modal retrieval toolbox for agents; Iterative search-read-assess loop; Index once, query at runtime; Merkle-tree index reuse across near-identical corpora; Staged narrowing before the context window
- Tools: Claude Code, Codex, Cursor, Turbopuffer, BM25, Merkle trees

## [Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI](../videos/TUnPNY4E2fw.md)
`TUnPNY4E2fw` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: training-finetuning-rl

Together AI's Max Ryabinin walks through stacking memory optimizations (Ulysses context parallelism, checkpointing, CPU offload, tiling, and the UPipe head-chunking method) to train with multi-million-token context.

- Techniques: Staged memory accounting; Head-based context parallelism (DeepSpeed Ulysses); Activation checkpointing plus CPU offload of block inputs; Sequence tiling of element-wise ops; UPipe head chunking with buffer reuse; Profile with PyTorch profiler first
- Tools: PyTorch profiler, FSDP, DeepSpeed Ulysses, FlashAttention

## [GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod](../videos/zDGHt0LB-dA.md)
`zDGHt0LB-dA` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: inference-serving

RunPod's Audrey Hsu demos Flash, a Python SDK that runs a decorated async function on a cloud GPU with hot reload from the local dev loop, plus a multi-model image pipeline and a pods-vs-serverless cost note.

- Techniques: Decorator-based remote GPU execution with hot reload; LLM prompt expansion before image generation; Chained model pipeline with separate endpoints per stage; Start small, then scale: pods for experiments, serverless for fan-out
- Tools: RunPod Flash (Python SDK), RunPod Serverless, RunPod Pods, RunPod Clusters, RunPod Hub, Stable Diffusion XL Turbo, DreamShaper, Qwen3, Google image composition model (Nano Banana 2), PyTorch, FastAPI, Docker

## [Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod](../videos/ILdE7FaAjVA.md)
`ILdE7FaAjVA` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: inference-serving

RunPod's intro walkthrough of deploying an open LLM (Qwen via vLLM) as a serverless GPU endpoint from its Hub in under five minutes; mostly a product pitch, with a useful look at cold starts and autoscaling settings.

- Techniques: Serverless GPU autoscaling with warm workers; Deploy a model from a pre-vetted Hub listing; Cold-start awareness in latency budgets
- Tools: RunPod, vLLM, Hugging Face, Docker

## [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](../videos/SKDJo2CopRs.md)
`SKDJo2CopRs` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: sandboxing-execution, agent-architecture, mcp-and-tools

Two Cloudflare engineers tour Durable Objects, dynamic workers and code mode as a stateful, sandboxed runtime for agents. Mostly product pitch, with a few reusable architecture ideas.

- Techniques: One Durable Object per entity ID as the session or agent; Resumable stream held by the agent object; Deny-by-default capability sandbox for generated code; Code mode for large API surfaces; Scheduled work inside the agent class; Plugins as isolated dynamic workers
- Tools: Cloudflare Durable Objects, Cloudflare Workers, Cloudflare Dynamic Workers, Cloudflare Agents SDK, Vercel AI SDK, MCP, Cloudflare Sandbox SDK, Daytona, SQLite, R2, Zig (via Wasm), Next.js on Workers

## [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../videos/N7b1PJc7SFc.md)
`N7b1PJc7SFc` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, evals, agent-architecture

Together AI's voice AI lead on the cascading STT→LLM→TTS pipeline: per-stage latency budgets, streaming STT, co-locating models to cut network hops, and why speech-to-speech is not yet production-ready.

- Techniques: Cascading voice pipeline with streamed hand-offs; Per-stage latency budget; Streaming STT with lookahead-limited encoders; Co-locate models with the orchestrator; Asymmetric autoscaling for stateful voice; Pre- and post-LLM guardrail and routing stages; Thinker-talker delegation; Tiered tool-call evals; Full-duplex conversation evals
- Tools: Together AI (hosted inference, the speaker's company), Pipecat (agent orchestrator, named as an example), LiveKit (agent orchestrator, named as an example), Whisper (OpenAI speech-to-text, cited as the batch model), NVIDIA streaming speech encoder (named only as a recent NVIDIA model), NVIDIA VoiceChat (speech-to-speech model), OpenAI realtime API (speech-to-speech), ChatGPT advanced voice mode, Claude Code and Cursor (cited as voice-interaction examples)

## [What Lies Beneath the API — Benjamin Cowen, Modal](../videos/HvZXAOZ3iv8.md)
`HvZXAOZ3iv8` · AI Engineer · 2026-06-18 · q2 · intro · talk · also: training-finetuning-rl, inference-serving

Modal forward-deployed engineer argues that once a product is differentiated, fine-tuning becomes worth it, and that serverless compute and open-source libraries now make it accessible without a cluster team. Sales-leaning, with a few concrete signals and code-size claims.

- Techniques: Signal-based fine-tuning decision; Harness outcomes as RL training data; Parallel hyperparameter sweep with early kill; Sandbox-fanned RL rollouts; Autoscaled serving of custom models
- Tools: Modal, vLLM, SGLang, Triton Inference Server, Python

## [Bun.Image Makes Your Entire Image Pipeline Obsolete](../videos/Tnmyb_pdM10.md)
`Tnmyb_pdM10` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: dev-tools

Short walkthrough of Bun.Image, the built-in image API in Bun 1.3.14, with resize, WebP conversion and ThumbHash placeholders, and a claim that it is faster than Sharp.

- Techniques: Resize, convert and compress with Bun.Image; Optional image operations; ThumbHash blur placeholders; Progressive JPEG for a loading effect
- Tools: Bun 1.3.14 (Bun.Image / image API), Sharp, libvips, WebP, ThumbHash, Waku, Next.js, Bun SQLite, Bun S3, Bun Postgres, Vercel Zero (referenced, not discussed)

## [Developers Finally Got an Open-Source Voice AI Platform (Dograh)](../videos/xD9JEvfCH9k.md)
`xD9JEvfCH9k` · Better Stack · 2026-06-02 · q3 · intro · review · also: voice-multimodal, observability

Short hands-on look at Dograh, a self-hostable open-source voice agent platform with a visual workflow builder, per-call traces and recordings, as an alternative to hosted tools like Vapi.

- Techniques: Local spin-up of a self-hosted voice agent stack; Lead-qualification voice flow as a node graph; Per-call debugging via transcript, trace and recording; Swap providers at the runtime layer
- Tools: Dograh, Docker Compose, Git, Vapi, Bland, Retell, Pipecat, Vocode, LiveKit

## [Deno Just Open Sourced Their Agent Firewall (Claw Patrol)](../videos/ZiFoTw6doGI.md)
`ZiFoTw6doGI` · Better Stack · 2026-06-02 · q3 · intro · review · also: security-guardrails, governance-compliance

Walkthrough of Claw Patrol, an open-source agent firewall from the Deno team: a gateway injects real credentials into agent requests, enforces per-action rules, and logs every request.

- Tools: Claw Patrol (Deno, open source), Deno, Tailscale, WireGuard, OpenClaw, Claude (Claude Code CLI; transcript spells it "Clawed"), Codex, Postgres, ClickHouse, Slack, GitHub, Kubernetes

## [Llama-Swap: This Fixes The Most Annoying Local LLM Problem](../videos/GtTzO5ZOQr4.md)
`GtTzO5ZOQr4` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: local-ai

Better Stack walkthrough of llama-swap, a single Go proxy that exposes one OpenAI/Anthropic-compatible endpoint and starts, swaps and TTL-unloads local model backends based on the request's model field.

- Techniques: Single front-door proxy for multiple local model servers; TTL-based idle unloading; Per-model backend control
- Tools: llama-swap, llama.cpp (llama-server), Ollama, LM Studio, vLLM, TabbyAPI, Open WebUI, Cursor, Continue, Qwen coder (transcript: 'quen-coder'), small-lm2 (name as spoken in the config example)

## [Stop Overpaying for LLMs... This Router Cut My Costs 70% (Manifest)](../videos/BXme4u4uoyA.md)
`BXme4u4uoyA` · Better Stack · 2026-06-02 · q3 · intro · review · also: token-cost-efficiency, mcp-and-tools

Better Stack walkthrough of Manifest, a self-hostable LLM router that scores each request across 23 dimensions and sends it to the cheapest capable model; the speaker claims up to 70% cost cuts with no agent code changes.

- Techniques: Drop-in LLM router in front of agents; Deterministic request scoring for model routing; Route to subscriptions and local models before paid API tokens; Failover on provider errors; Per-agent cost tracking and budgets
- Tools: Manifest, Docker, Docker Compose, OpenAI API (base_url change), Anthropic API, Ollama, OpenRouter, LiteLLM, llama.cpp, Python (demo agent script)

## [Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI](../videos/P_RI1kCkRbo.md)
`P_RI1kCkRbo` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: voice-multimodal, models-research

Gradium's CEO argues voice AI is not yet at the "Her" moment: cascaded pipelines hit latency limits, full-duplex speech models lack reliability and tools, and TTS cost dominates. He pitches on-device TTS as the fix.

- Techniques: Filler speech while a tool call runs; Stress-test full-duplex and interruption behaviour; On-device TTS for cost and privacy; Keep the cascade as the default for reliable agents
- Tools: Moshi, Gradium Phonon, NVIDIA PersonaPlex, Kokoro, ElevenLabs, OpenRouter

## [The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked](../videos/qdh_x-uRs9g.md)
`qdh_x-uRs9g` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: inference-serving, rag-retrieval

Superlinked's Filip Makraduli on why small models (embeddings, rerankers, NER) need their own inference layer, and the open-source SIE engine built to serve them on shared GPUs.

- Techniques: Hot-swap many small models on one GPU with LRU eviction; Re-implement the forward pass per model family; Small-model preprocessing in front of the agent; Models as config, cluster as code
- Tools: vLLM, Prometheus, Grafana, Terraform, Helm, Docker, Hugging Face, FlashAttention, Chroma, Qdrant, Weaviate (transcribed as VV8), LanceDB (transcribed as LensDB)

## [Gateways are All You Need — Karan Sampath, Anthropic](../videos/CD6R4Wf3jnY.md)
`CD6R4Wf3jnY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: mcp-and-tools, security-guardrails, governance-compliance

Anthropic forward-deployed engineer Karan Sampath argues enterprises should put one gateway in front of all MCP servers for auth, access control, observability and credentials, so teams build only business logic.

- Tools: MCP, Claude Code, Claude Agent SDK, claude.ai, Claude managed agents

## [Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev](../videos/svCnShDvgQg.md)
`svCnShDvgQg` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, sandboxing-execution

Eric Allam (Trigger.dev) argues that replay-based durable execution breaks for long-running agent loops, and proposes splitting agent durability into an append-only context log plus VM snapshot/restore of the execution state.

- Techniques: Two-layer agent durability; Snapshot on idle, restore on next message; Recovery by failure class; Seekable compression with lazy page restore; Whole-VM snapshot instead of process checkpoint
- Tools: Trigger.dev, Firecracker, CRIU (captioned as "Cree"), Docker, fcrun

## [Mastering AI Pricing — Mayank Pant, Stripe](../videos/CrqPcIZOOXA.md)
`CrqPcIZOOXA` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: product-ux, governance-compliance

Stripe's billing architect on AI pricing: treat the first price as a hypothesis, use base-plus-usage hybrid pricing with credits, add usage guardrails, and choose billing infrastructure that lets you change prices quickly.

- Techniques: Credit abstraction layer; Base fee plus usage fee (hybrid); Usage guardrail stack; Value-to-metric mapping; Grandfathered pricing versions; Per-event rating with explainable invoices
- Tools: Stripe Billing, Metronome

## [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @The Pragmatic Engineer](../videos/CS5Cmz5FssI.md)
`CS5Cmz5FssI` · AI Engineer · 2026-05-18 · q3 · practitioner · interview · also: enterprise-adoption, coding-agents, governance-compliance

Gergely Orosz (Pragmatic Engineer) on "token maxing": how usage leaderboards get gamed, why individual gains do not yet show up as team gains, and why big companies build their own agent infrastructure.

- Techniques: Enable non-engineers to build with coding agents; Keep agent count small and treat orchestration like tech lead mentoring; Single MCP gateway tied to service discovery; Risk-tiered code review for agent-written changes; Trade early access for structured feedback
- Tools: Claude Code, Cursor, GitHub Copilot, MCP gateway

## [Run S3 on Your Laptop? This Changes Everything (MinIO)](../videos/GHeLgENOBb4.md)
`GHeLgENOBb4` · Better Stack · 2026-05-02 · q2 · intro · review · also: dev-tools

Short intro to running MinIO, an S3-compatible object store, on a laptop for local dev and prototypes, with the caveats that the repo is archived and the project is moving to a paid AI Store.

- Techniques: Run a local S3-compatible store in Docker; Register the local server with the MinIO client (mc) as an alias; Keep the S3 SDK code and only change the endpoint; Tiered environments behind one S3 API; Browse and preview objects in the MinIO web console
- Tools: MinIO, MinIO AI Store, mc (MinIO client), Docker, boto3, Python, Kubernetes, Ceph, Garage, AWS S3

## [This Tiny 82M Model Just Beat Most TTS APIs (Runs Locally)](../videos/bdf6BxyxCnQ.md)
`bdf6BxyxCnQ` · Better Stack · 2026-05-02 · q3 · intro · review · also: voice-multimodal, local-ai

Better Stack tries Kokoro 82M, a small open TTS model, on a Mac M4 Pro and weighs its speed, privacy and cost against its missing voice cloning and emotion control.

- Techniques: Run a small local TTS model as a drop-in for cloud TTS; Pick a small TTS model when time-to-first-audio matters; Evaluate TTS by listening to your own text per language and voice
- Tools: Kokoro 82M (TTS model, Apache 2.0), StyleTTS2 (architecture the model is based on), Misaki (text processing library named by the host), XTTS, CosyVoice, F5-TTS, ElevenLabs (cloud TTS), OpenAI TTS (cloud TTS), Python, pip, conda, Mac M4 Pro (test hardware)

## [Stop Using Docker for GPUs! (RunPod Flash is INSANE!)](../videos/Biv4fKGsTcE.md)
`Biv4fKGsTcE` · Better Stack · 2026-04-02 · q2 · intro · review · also: dev-tools

Walkthrough of RunPod Flash, which turns decorated Python functions into on-demand serverless GPU endpoints without Docker, shown via a two-stage CPU-resize then RTX 5090 video-generation pipeline.

- Techniques: Split a pipeline by hardware class; Expose each heavy step as an on-demand endpoint; Local setup sequence; Budget for the cold first run; Monitor through the analytics tab
- Tools: RunPod Flash, Flash SDK, RunPod serverless, uv, Python, CogVideoX ("cog video X", 5B parameters), NVIDIA RTX 5090, Docker (contrasted, not used), Discord (example trigger)

## [1 Million Sandboxes Per Second?! Dynamic Workers Are INSANE](../videos/7Re3HReM5SQ.md)
`7Re3HReM5SQ` · Better Stack · 2026-04-02 · q3 · practitioner · tutorial · also: sandboxing-execution, agent-architecture

Better Stack walks through Cloudflare Dynamic Workers, V8-isolate workers created at runtime by a parent Worker, as a faster, lighter alternative to container sandboxes for running AI-generated code. The catch is JavaScript only, with no filesystem.

- Techniques: Per-request sandboxed child Worker with network disabled; Stable-name reuse for warm sandboxes; Custom bindings and RPC into the child; Bundling npm dependencies into a child; Egress interception for credential injection; Agent code-execution loop with artifact persistence; Scripted bulk spawn with create-or-reuse
- Tools: Cloudflare Dynamic Workers, Cloudflare Workers, Wrangler, V8 isolates, Cloudflare Sandboxes, Cloudflare Durable Objects, Cloudflare R2, Cap'n Web, Hono, Anthropic SDK, Claude Sonnet 4.6, Claude Sonnet 3.5

## [The Open-Source Firebase Alternative Might Be Better (AppWrite)](../videos/PuH4Wq5Smwg.md)
`PuH4Wq5Smwg` · Better Stack · 2026-04-02 · q2 · intro · tutorial · also: dev-tools

Better Stack walkthrough of self-hosting Appwrite, an open-source Firebase alternative, with a Docker Compose setup, a to-do app sync demo, and trade-offs versus Supabase and Firebase.

- Techniques: Self-host Appwrite with Docker Compose; Register a localhost web platform; Per-role collection permissions; Wire the client through env variables
- Tools: Appwrite, Docker, Docker Compose, Firebase, Supabase, Cloudflare, MariaDB, PostgreSQL, React, Flutter, Better Stack

## [I Replaced Vercel with Dokploy](../videos/v6fn0KMCtEo.md)
`v6fn0KMCtEo` · Better Stack · 2026-04-02 · q2 · intro · review · also: dev-tools

Better Stack's 4-minute walkthrough of Dokploy, a self-hosted, Docker-native PaaS that turns a rented VPS into a Vercel/Heroku-style deploy target with HTTPS, logs, rollback and optional Swarm scaling.

- Techniques: Self-hosted push-to-deploy on a cheap VPS; Docker Swarm for multi-server scaling via Dokploy; Built-in ops bundle instead of extra tools
- Tools: Dokploy, Docker, Docker Compose, Docker Swarm, Traefik, Hetzner VPS, GitHub, Next.js, Vercel, Railway, Heroku, Coolify

## [Headscale - The Tool That Made Me DELETE My Tailscale Subscription!](../videos/8t8FZaBamqA.md)
`8t8FZaBamqA` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: dev-tools

Walkthrough of Headscale, a self-hosted open-source control plane for Tailscale clients: Docker setup, pre-auth keys, a permissive ACL, and an honest verdict that setup is involved and the web UI is buggy.

- Techniques: Dockerized Headscale control plane with a reverse proxy; User-scoped pre-auth keys for joining nodes; Permissive starter ACL plus SSH rule; Checking reachability from inside and outside the tailnet
- Tools: Headscale, Tailscale (client and reference control plane), Docker / Docker Compose, Caddy, SQLite, PostgreSQL (optional backend), Headscale web UI (community, unnamed), Cloudflare (DNS), Ubuntu (test servers), Claude Opus (mentioned as a tool for building a UI), OpenClaw (mentioned as a possible offline local-LLM target)

## [Cloudflare Just Killed Mac Minis? OpenClaw Runs Serverless – Here's How!](../videos/DQdYE02TkIQ.md)
`DQdYE02TkIQ` · Better Stack · 2026-03-02 · q2 · practitioner · tutorial · also: sandboxing-execution, agent-architecture

Walkthrough of running the OpenClaw agent gateway serverlessly on Cloudflare Workers, Sandboxes, Browser Rendering and R2, with setup steps and a serverless-versus-VPS verdict. Ends with a Better Stack sponsor read.

- Techniques: Prerequisites checklist before deploying OpenClaw on Cloudflare; Verify Durable Object, R2 and browser bindings after deploy; Enable Cloudflare Access and set two Wrangler secrets; Clear a stale sandbox container before redeploying; Pair the device and authenticate the browser; Persist state in R2, not the sandbox disk
- Tools: OpenClaw (captioned as Clawdbot / MoltBot / MaltBot), Cloudflare Workers, Cloudflare Sandboxes (Docker-based), Cloudflare Browser Rendering (headless Chromium), Cloudflare R2, Cloudflare Durable Objects, Cloudflare Access, Cloudflare AI Gateway, Wrangler, Hono, Chrome DevTools Protocol, Docker

## [I Replaced Notion, Linear, and Slack With One Tool (Huly)](../videos/gGKtoykrNYA.md)
`gGKtoykrNYA` · Better Stack · 2026-03-02 · q2 · intro · review · also: dev-tools

Walkthrough of Huly, a self-hosted open-source all-in-one workspace (tasks, docs, chat, calendar, GitHub sync) pitched as a replacement for Notion, Linear, Slack and GitHub. Short, shallow demo; the speaker judges it good but flags RAM and setup costs.

- Techniques: Self-host an all-in-one workspace in Docker; Two-way GitHub issue sync into a project board; Link specs, tasks and code in one place
- Tools: Huly (captioned as Hooli), GitHub, Docker, Notion, Linear, Slack, TypeScript

## [The Internet Is Full of Zombies and Nobody Is Talking About It](../videos/3yR45A3EGOU.md)
`3yR45A3EGOU` · Better Stack · 2026-02-02 · q2 · intro · other · also: —

Explains BGP "zombie" routes that stay in some routers' tables after withdrawal, citing Cloudflare's observations and their make-before-break fix. Networking background, not AI.

- Techniques: Make-before-break route handoff; Rely on TTL-style expiry as a backstop for stale state
- Tools: BGP (Border Gateway Protocol)

## [This Tool Turns Claude Into an Automation Engine (ActivePieces)](../videos/K_6IYK2cIqs.md)
`K_6IYK2cIqs` · Better Stack · 2026-01-02 · q2 · intro · review · also: mcp-and-tools, dev-tools

Quick review of ActivePieces, a self-hostable, MIT-licensed Zapier/Make alternative whose integrations are also exposed as MCP servers; shallow demo, with the Claude angle mostly asserted rather than shown.

- Techniques: Self-host ActivePieces with Docker; Start from a template in New flow; Build a flow from scratch: trigger, AI step, sink; Expose automation pieces to Claude Desktop through their MCP URL
- Tools: ActivePieces, Docker, Claude Desktop, Claude, Cursor, MCP, Zapier, Make.com, Gmail, OpenAI, Notion, VPS

## [Building a One-Man Empire with AI & the Future of Developer Education | Better Stack Podcast Ep. 9](../videos/XG6ToBSg2HU.md)
`XG6ToBSg2HU` · Better Stack · 2026-01-02 · q3 · practitioner · interview · also: dev-tools, coding-agents, data-engineering

Better Stack podcast with solo developer David Flanagan (Raw Code Academy) on running a one-person, AI-assisted business: Cloudflare automation, LLM transcript correction, Kubernetes vs serverless cost trade-offs, QEnv and Dagger.

- Techniques: LLM-assisted transcript correction loop; Cron-driven content publishing on Cloudflare Workers; Spec-first delegation to coding agents; Hierarchical env with secret references (QEnv); Per-package CI definitions in a monorepo; Dagger pipelines in TypeScript; Cost-inflection planning for hosting; Reproducible machine via NixOS config
- Tools: Cloudflare Workers, Cloudflare R2, Cloudflare D1, Cloudflare service bindings, Gemini 3, Claude Code, Codex, Droid (multi-model agent CLI), Deepgram Nova 3, Whisper, ElevenLabs, Bluesky

## [This Tiny Linux Setting Fixed My Next.js Builds (Swap)](../videos/HU5CV64vLg4.md)
`HU5CV64vLg4` · Better Stack · 2026-01-02 · q3 · intro · tutorial · also: dev-tools

Tutorial on fixing out-of-memory Next.js builds on a 1 GB DigitalOcean droplet by adding swap files and capping the Node heap, instead of upscaling the server.

- Techniques: Diagnose swap and disk before creating a swap file; Create and activate a swap file; Stack extra swap files to reach a larger total; Lower the Node heap cap to match swap; Set a swap budget against steady-state use
- Tools: Next.js, Node.js, pnpm, npm, create-payload-app (pnpx create payload app@latest), Payload CMS, SQLite, DigitalOcean droplet, Ubuntu, fallocate, mkswap, swapon

## [Your VPN Is Probably FAKE! (85% Exposed in Investigation)](../videos/5kgkcsiPB-o.md)
`5kgkcsiPB-o` · Better Stack · 2026-01-02 · q2 · intro · review · also: security-guardrails

Better Stack summarizes an IPinfo investigation finding that most VPN providers list server countries that are virtual, with traffic exiting elsewhere; the speaker says the core problem is transparency, not encryption.

- Techniques: Latency-based location verification; Do not trust declared IP geolocation
- Tools: IPinfo ProbeNet, OpenVPN

## [Goodbye AI Cloud Bills... Exo Runs AI on Your Own Devices](../videos/L8468vMTX2s.md)
`L8468vMTX2s` · Better Stack · 2026-01-02 · q2 · intro · review · also: local-ai, inference-serving

Short Better Stack overview of EXO, an open-source tool that auto-discovers devices on a LAN and shards one model across them; the demo runs on a single Mac, so the multi-device claims are unverified.

- Techniques: Zero-config LAN cluster for local inference; Shard the model by measured node capacity; Thunderbolt 5 RDMA between Macs
- Tools: EXO (open-source peer-to-peer inference cluster, ExoLabs), Apple MLX, OpenAI-style chat endpoint (served by EXO), Thunderbolt 5 RDMA, DeepSeek V3 671B (cited community run), Qwen3 235B (cited community run), MacBook Pro M4 Pro (demo machine), Mac Studio M3 Ultra (cited benchmark), Mac mini M4 (cited ExoLabs run), Raspberry Pi (CPU node)

## [How AWS S3 Hit 1PB/s Using Hard Drives… This Is WILD!](../videos/J1vEUTe4gi0.md)
`J1vEUTe4gi0` · Better Stack · 2025-12-02 · q3 · intro · review · also: data-engineering

Explains how AWS S3 runs on hard drives at petabyte-per-second scale, using parallel erasure-coded reads, randomized placement, rebalancing and workload decorrelation to avoid hot drives.

- Techniques: Erasure-coded striping for parallel reads; Power of two random choices for placement; Proactive rebalancing by data age and new capacity; Workload aggregation to smooth bursts
- Tools: Amazon S3, Apache Kafka (referenced as an example of log-structured writes)

## [OpenTelemetry Collector - Explanation & Setup](../videos/4ACQhkJBKyA.md)
`4ACQhkJBKyA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability, dev-tools

Beginner tutorial on the OpenTelemetry Collector: receivers, processors and exporters, why to put it between apps and an observability backend, and a Docker setup that adds host and self-metrics and ships data to Better Stack.

- Techniques: Minimal collector config.yaml with OTLP in, batch, OTLP out; Per-signal pipelines with different processors; Adding a backend source token with the attributes processor; Host and self-metrics via receivers
- Tools: OpenTelemetry Collector, OpenTelemetry SDK (Node.js), OTLP (OpenTelemetry Protocol), Docker, Better Stack, Prometheus, Prometheus Remote Write exporter, Jaeger, Zipkin, VS Code, hostmetrics receiver, batch processor

## [Running Docker on Cloudflare is FINALLY possible...](../videos/c6TEXxpUEUw.md)
`c6TEXxpUEUw` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: sandboxing-execution, dev-tools

Better Stack walkthrough of Cloudflare Containers: deploying a Bun + ffmpeg container behind a Worker with a Durable Object, then reviewing limits, beta pricing and a Rivet/Fly cost comparison.

- Techniques: Container server behind a Worker; Durable Object container class; wrangler config for containers; Monitoring containers
- Tools: Cloudflare Containers (beta), Cloudflare Workers, Durable Objects, Wrangler CLI, Docker, Bun, ffmpeg, Rivet containers, Fly Machines (Fly.io), index.html static assets

## [SLAs, SLOs, and SLIs EXPLAINED in 7 Minutes (2025)](../videos/pouVbehfnqQ.md)
`pouVbehfnqQ` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: observability

Beginner explainer distinguishing SLAs (customer contracts with penalties), SLOs (internal targets) and SLIs (measured metrics), using a rice-farmer analogy and AWS EC2 uptime math. Main takeaway: derive SLOs from measured SLIs and monitor your own services rather than trusting vendor status pages.

- Techniques: Derive the SLO from measured SLI history; Keep the internal SLO stricter than the external SLA; Turn an uptime percentage into a minute budget; Monitor your own endpoints, not only the vendor status page
- Tools: AWS, Amazon EC2

## [Neon: The FUTURE of Postgres? Branching, HTTP Queries, and More!](../videos/7KglfRnIlfc.md)
`7KglfRnIlfc` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

Short Better Stack review of Neon serverless Postgres, covering scale-to-zero compute, copy-on-write branches, time travel, and an HTTP driver for edge runtimes; mostly feature claims with one Cloudflare Worker demo.

- Techniques: Per-PR or per-environment database branches; Scale-to-zero for idle databases; Query Postgres from edge runtimes over HTTP/WebSocket; Point-in-time restore and time travel
- Tools: Neon (serverless Postgres), Neon CLI, Neon serverless driver (HTTP/WebSocket to TCP proxy), Cloudflare Workers, Hono, GitHub integration, Vercel edge functions (caption reads 'cell edge functions'; the host does not name a provider)

## [OpenTelemetry Sampling with Go - Simplify Chaos and Get Better Insights](../videos/WtX3Nlnjffs.md)
`WtX3Nlnjffs` · Better Stack · 2025-11-02 · q2 · practitioner · tutorial · also: observability, dev-tools

Walkthrough of OpenTelemetry sampling for logs and traces in a local Go app: collector probabilistic sampling, SDK trace samplers, and tail-based sampling with error and probabilistic policies.

- Techniques: Probabilistic log sampling in the collector; Consistent sampling across multiple collectors; Trace-correlated logs in a Go app; SDK head-based trace sampling; Collector probabilistic trace sampling; Tail-based trace sampling with policies; Error-only policy with context; Memory guard for tail sampling
- Tools: OpenTelemetry Collector, OpenTelemetry Go SDK (traces, logs), OTel slog bridge (Go log/slog), OTLP exporter, Probabilistic sampling processor (logs and traces), Tail sampling processor, Memory limiter processor, Go, FNV hash, Better Stack (sponsor, logs UI)

## [Vercel goes ALL IN on AI (Vercel Ship Recap)](../videos/idBEifQwlGI.md)
`idBEifQwlGI` · Better Stack · 2025-11-02 · q2 · intro · news · also: sandboxing-execution, dev-tools

Better Stack's 5-minute recap of Vercel Ship: AI Gateway and AI SDK v5 betas, a hosted sandbox for untrusted code with active-CPU billing, BotID, rolling releases, and several limited-beta features.

- Tools: Vercel AI Gateway, AI SDK v5, Vercel Sandbox, Fluid compute, Active CPU billing, BotID, CheckBotID, Rolling Releases, Microfrontends, Vercel Queues, Vercel Agent, Amazon Linux 2023

## [Why You NEED to Try Cloudflare's Sandbox SDK Today](../videos/0bkeZOXNJBg.md)
`0bkeZOXNJBg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: sandboxing-execution

Short walkthrough of Cloudflare's Sandbox SDK for running AI-generated code in isolated containers from a Worker, with a Claude Haiku-to-sandbox example and a positioning take against Daytona.

- Techniques: Worker + Durable Object sandbox wiring; Generate-then-execute loop; Local dev with Docker before deploy
- Tools: Cloudflare Sandbox SDK, Cloudflare Workers, Cloudflare Durable Objects, Cloudflare Containers, Wrangler, Docker Desktop, Bun, Node 20, Python 3.11, Ubuntu 22, Anthropic AI SDK, Claude Haiku

## [Docker Image BEST Practices - From 1.2GB to 10MB](../videos/t779DVjCKCs.md)
`t779DVjCKCs` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: dev-tools

Better Stack walkthrough that shrinks a React/Node Docker image from 1.2 GB to 10 MB using Alpine bases, layer ordering, .dockerignore, single-RUN cleanup, multi-stage builds and the slim tool.

- Techniques: Switch to a minimal base image variant; Dependency-first layer ordering; .dockerignore to trim the build context; Do cleanup in the same RUN as the install or build; Multi-stage build: build in one stage, serve from a small stage; Inspect layers and minify with Dive and slim
- Tools: Docker, Dockerfile, Node.js (node:latest, node alpine variant), npm, React, Nginx, Alpine Linux, Distroless (Google), Python, Kubernetes, Dive, Slim (slim build, x-ray, lint)

## [Meta Just Changed Data Compression FOREVER (OpenZL Explained)](../videos/_BsjI3IUtlg.md)
`_BsjI3IUtlg` · Better Stack · 2025-11-02 · q2 · intro · review · also: data-engineering, dev-tools

Better Stack explainer of Meta's open-source OpenZL: format-aware compression with a per-format plan and one universal decoder. The claimed gains are on structured data, from a single Meta test.

- Techniques: Schema-first format description with SDDL; Offline plan training over reversible transforms; Evolve the compression plan without redeploying the decoder
- Tools: OpenZL (Meta, open source, no version stated), SDDL (Simple Data Description Language, OpenZL schema format), ZStandard (ZSTD, used as the fallback backend and as the speed baseline), GZip (named as a general-purpose baseline)

## [WebAssembly vs AWS Lambda vs Cloudflare Workers: Which Actually Performs Best?](../videos/5vCGMrYadBI.md)
`5vCGMrYadBI` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: sandboxing-execution, dev-tools

Better Stack runs one TypeScript app on Fermyon Spin (WebAssembly), Cloudflare Workers and AWS Lambda, comparing latency, recursion limits, sandbox behavior and resource use. Workers win on JS speed, Wasm has the smallest footprint, and the test is small and single-region.

- Techniques: Per-minute uptime probe for latency distribution; Local warm-up timing with repeated curl; Recursion vs iteration as a stress test; Eval-injection sandbox probe; Host-level resource sampling per process; OpenTelemetry trace export from a Spin app
- Tools: Fermyon Spin (captioned 'Thermian Spin'), Fermyon Cloud (captioned 'Thermian Cloud'), Cloudflare Workers, Wrangler, workerd, esbuild, Node.js, V8 / V8 isolates, QuickJS, AWS Lambda, Better Stack uptime monitors, OpenTelemetry

## [Leaving AWS to Build a Better Redis w/ Roman Gershman (Dragonfly Co-Founder)](../videos/tXdDddCgGnE.md)
`tXdDddCgGnE` · Better Stack · 2025-11-02 · q3 · intro · interview · also: dev-tools

Founder interview with Dragonfly's co-founder and CTO Roman Gershman on why he left AWS ElastiCache to rewrite Redis from scratch, plus the license and language choices behind it.

- Techniques: Rewrite the core instead of forking when the bottleneck is architectural; Keep the wire API for ecosystem compatibility; Time-delayed source-available license; Stay hands-on with the community
- Tools: DragonflyDB, Dragonfly Cloud, Dragonfly Swarm (announced by host, not detailed), Redis, Redis API, AWS ElastiCache, KeyDB (captions read it as KDB; the reference is inferred, not stated), Lua scripting, C++, Rust, Visual Studio Code, GitHub Copilot

## [Dokku - Is This FREE Heroku Clone Better Than The Original?](../videos/J8gPLpcgUOs.md)
`J8gPLpcgUOs` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

Walkthrough of Dokku, a Docker-based single-server Heroku alternative: create a $6 DigitalOcean droplet, git-push deploy a Node app, add subdomain routing and a linked Postgres database.

- Techniques: Provision a Dokku droplet from the DigitalOcean marketplace; Create the app and deploy with git push; Enable subdomains on an IP with nip.io and vhost routing; Add a linked Postgres database; Inspect and debug with Docker commands
- Tools: Dokku, Docker, Heroku buildpacks, Procfile, DigitalOcean droplet, Nginx, Let's Encrypt (Dokku plugin), nip.io, PostgreSQL, Dokku Postgres plugin, Node.js, node-postgres client

## [Docker + Django: Containerize the Right Way with Nginx, Postgresql & Gunicorn](../videos/1v3lqIITRJA.md)
`1v3lqIITRJA` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: dev-tools

Better Stack tutorial on running Django in production with Docker: gunicorn instead of runserver, nginx serving static files, a multi-stage non-root Dockerfile, and Postgres wired together with docker-compose.

- Techniques: gunicorn as the app server with entrypoint script; Environment-driven settings.py with two env files; Static file serving through a shared volume and nginx; nginx config with mime types, static alias and reverse proxy; Multi-stage Dockerfile with cache-friendly ordering and non-root user; docker-compose three-service stack; .dockerignore with env files first
- Tools: Django, Docker, Docker Compose, Gunicorn (version 23 as stated), Nginx, PostgreSQL, Python 3.13-slim (base image), python-dotenv (load_dotenv for local dev)

## [Watchtower -The PERFECT Docker Automation Tool?](../videos/GHeZaoUpVcQ.md)
`GHeZaoUpVcQ` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

A short walkthrough of Watchtower, a Docker tool that auto-updates and restarts containers, with the host's view that it suits homelabs but not production, where monitor-only alerting is safer.

- Techniques: Watchtower as a sidecar compose service; Excluding Watchtower from itself; Monitor-only mode with Slack alerts; Digest-based change detection
- Tools: Watchtower, Docker, Docker Compose, Docker Hub, Slack (webhook notifications)

## [Take Back Your PRIVACY and Run DeepSeek on EC2 in 5 Minutes!](../videos/DCWtyd9AW4w.md)
`DCWtyd9AW4w` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: local-ai, dev-tools

Step-by-step tutorial for running distilled DeepSeek (Qwen-based) models on a CPU-only AWS EC2 instance using Ollama, Open WebUI in Docker, and an Nginx reverse proxy, framed around keeping prompts private.

- Techniques: Run Ollama in Docker with a persistent volume and a published port; Open WebUI as a front end for a Docker-hosted Ollama; Nginx reverse proxy from port 80 to a local app port; Pick a quantization level by tradeoff
- Tools: AWS EC2, Amazon Linux, Docker, Ollama, Open WebUI, Nginx, Caddy (mentioned, not used), DeepSeek (distilled models, Qwen-based per the speaker), Qwen (distilled base for the 1.5B and 7B models), vim / nano

## [Cloudflare Just Made AI Agents WAY Easier (Agents SDK)](../videos/l4tHKJFQvRg.md)
`l4tHKJFQvRg` · Better Stack · 2025-11-02 · q3 · intro · review · also: agent-architecture, dev-tools

Better Stack demos Cloudflare's Agents SDK starter: durable-object agents that persist state, sync across browsers, schedule tasks and pause for human approval. Demo-driven, with no benchmarks.

- Techniques: Single shared agent for multi-window sync; Per-user or per-workflow agent routing; Chat agent setup; Persisting UI state; Human-in-the-loop tool approval; Scheduling tasks from chat
- Tools: Cloudflare Agents SDK (starter template), Cloudflare Durable Objects, Cloudflare Workers AI, AI SDK (used for tools and model calls), AIChatAgent (Agents SDK base class for chat), useAgent (React hook from the SDK), React, WebSocket, Hono (official middleware mentioned), OpenAI-compatible API schema (for model choice)

## [STOP Using Docker Compose. Switch to Kubernetes in 6 Mins (With Kompose)](../videos/cyGF_PLBx4c.md)
`cyGF_PLBx4c` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

Tutorial that converts a two-container Docker Compose app to Kubernetes manifests with Kompose, runs it on a local kind cluster, and fixes two first-deploy failures (image pull policy and ClusterIP).

- Techniques: Convert Compose to Kubernetes manifests with Kompose; Create a local kind cluster with exposed ports; Load a locally built image into kind; Inspect a kind node's images with docker exec; Fix pulls of :latest-tagged local images by setting imagePullPolicy; Expose a Service on a fixed host port with NodePort; Check cluster state with kubectl get all
- Tools: Docker Compose, Kompose (auto-caption reads it as 'Compose'), kubectl, kind, Kubernetes, Docker, nginx, Bun, Minikube, Docker Desktop, Homebrew, Docker Swarm

## [MASTER Apache Kafka in just 8 minutes to Build Real-Time Apps](../videos/feKBnsvO2Pk.md)
`feKBnsvO2Pk` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: data-engineering, dev-tools

Beginner Kafka tutorial: topics and pub/sub, disk-backed replayable events, brokers and KRaft, then a two-producer, two-consumer Python log demo run through Docker Compose and uv.

- Techniques: Local single-node Kafka via Docker Compose in KRaft mode; Minimal Python producer writing to a topic; Minimal Python consumer printing a topic; Replay a topic from the beginning; Run Python producers and consumers with uv in separate tabs
- Tools: Apache Kafka, Docker Compose, Python, uv, ZooKeeper (named as the replaced component), KRaft (Kafka Raft, Kafka's built-in metadata management), A Python Kafka client library (not named in the transcript), WebSockets (comparison only), Amazon SQS (comparison only), RabbitMQ (comparison only), Prometheus 3 (plug for another Better Stack video)

## [12 Logging BEST Practices in 12 minutes](../videos/I2mWnh66Bkg.md)
`I2mWnh66Bkg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability, dev-tools, security-guardrails

A generic logging best-practices list: plan what to log, use levels and structured fields, sample high-volume logs, emit one canonical line per request, centralize, set retention, redact secrets, and watch logging overhead.

- Techniques: Canonical log line per request; Selective sampling; Redaction in the pipeline; Tiered retention policy; Load test logging overhead
- Tools: OpenTelemetry, OpenTelemetry Collector, Vector, Go slog (log/slog), Logrus (transcribed as Logris), Go

## [Redis vs DragonflyDB - A Faster, Modern, Drop-In Replacement?](../videos/OlsENj_LpEQ.md)
`OlsENj_LpEQ` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: dev-tools

Better Stack benchmarks DragonflyDB against Redis on one node and as Redis Cluster, finds Dragonfly several times faster on a single node, but cluster Redis closes most of the gap.

- Techniques: Single-node memtier_benchmark comparison; Redis Cluster baseline for fair comparison; Drop-in migration trial by endpoint swap
- Tools: Redis (single-node and cluster mode, redis-cli), DragonflyDB (single binary or Docker container), memtier_benchmark (load-testing tool described as Redis's), Docker, AWS EC2 (benchmark hosts, 8-core 32GB and 16-core 64GB)

## [K9s | The BEST Terminal UI for Kubernetes (2025)](../videos/AMUQzyPvO04.md)
`AMUQzyPvO04` · Better Stack · 2025-11-02 · q3 · intro · review · also: dev-tools

A 5-minute walkthrough of K9s, a terminal UI for Kubernetes, covering navigation, per-resource shortcuts, port-forwarding, live edits, aliases and skins. The speaker keeps kubectl for applying manifests.

- Techniques: Port-forward a pod from K9s; Edit a deployment's image or replica count live; Open a shell in a container; Command mode and filtering; Custom aliases and config; Enable image vulnerability scans (preview)
- Tools: K9s, kubectl, Kubernetes metrics server, MongoDB shell, Tokyo Night skin (community variant, linked in the video description), Dracula skin (from the official K9s skins repo)

## [Google’s Golden Signals with the OpenTelemetry Demo and Grafana](../videos/QWmU9Y_zKsw.md)
`QWmU9Y_zKsw` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: observability

A short walkthrough of Google's four golden signals (latency, errors, traffic, saturation) on the OpenTelemetry demo app in Grafana, then a feature-flag fault-injection demo showing how failures ripple across services. Sponsored segment in the middle.

- Techniques: Golden-signal dashboard per service; Span-derived RED-style metrics cross-checked against traces; Feature-flag fault injection to map dependencies; Load generation to produce realistic traffic before reading signals
- Tools: OpenTelemetry demo app, OpenTelemetry Collector, Grafana, PromQL, Prometheus, Jaeger, Locust, Valkey (cache), Docker, Kubernetes, EC2, Better Stack

## [Build Docker Images 40x FASTER with This Tool (depot.dev)](../videos/Xdhtmqd8gHs.md)
`Xdhtmqd8gHs` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

Better Stack walkthrough of Depot, a remote Docker build service with cloud machines and shared caching, cutting one project's rebuild from 7m44s to 12s with depot build and depot bake.

- Techniques: Offload Docker builds to a remote builder with a shared cache; Point the build at a non-root Dockerfile with the file flag; Build all compose services in one remote run with depot bake
- Tools: Depot (depot.dev) CLI, depot build, depot bake, Docker, Docker Compose, Dockerfile, VS Code

## [Deploying your Own Vercel in MINUTES (open-source alternative)](../videos/pjrEaRSSQck.md)
`pjrEaRSSQck` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: dev-tools

A 7-minute walkthrough of self-hosting Appwrite Sites on a DigitalOcean droplet as an open-source Vercel alternative: Git deploys, branch previews, and bundled auth, database and storage.

- Techniques: Self-host Appwrite Sites with Docker Compose; Connect Git to self-hosted Appwrite via a GitHub App; Create a site from a Git repo with framework presets; Preview-then-promote with Activate
- Tools: Appwrite (Sites, Auth, Databases, Storage, Functions, Messaging, Appwrite Cloud), Vercel (comparison baseline), Docker Compose, DigitalOcean droplet, GitHub App, React (framework preset), npm, Better Stack (logging), .env file

## [Observability vs Monitoring - Whats the difference?](../videos/ytx6jr2TyxI.md)
`ytx6jr2TyxI` · Better Stack · 2025-11-02 · q2 · intro · other · also: observability

Beginner explainer distinguishing monitoring (known thresholds, the "what and when") from observability (logs, metrics and traces for the "how and why"), with a plug for Better Stack at the end.

- Techniques: Layered monitoring then observability; Tiered data collection for cost control
- Tools: Better Stack

## [Is Kafka OUTDATED? Could RedPanda Be the Future of Event Streaming?](../videos/tHXWAkJeWmA.md)
`tHXWAkJeWmA` · Better Stack · 2025-11-02 · q2 · intro · review · also: data-engineering, dev-tools

Better Stack compares Kafka and Redpanda: Redpanda wins architecture and deployment, Kafka wins ecosystem and licensing, and performance depends on the workload, per conflicting benchmarks.

- Techniques: Test Kafka-compatible brokers with existing clients; Minimal Docker Compose deployment for comparison; Benchmark on your own workload with OpenMessaging Benchmark
- Tools: Apache Kafka, Redpanda, Redpanda Console, Redpanda Connect, Kafka Connect, Kafka Streams, MirrorMaker, ZooKeeper, Docker, Docker Compose, Kafka Python client, OpenMessaging Benchmark framework

## [This Framework DESTROYS Next.js With 7x Faster Performance!](../videos/7gTj5RLyMXw.md)
`7gTj5RLyMXw` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

Better Stack benchmarks Fastify with React (Vite SSR) against Next.js and finds a 5x gap on a local hello-page test, but only about 4% on a realistic to-do app once Vercel hosting is included. The "7x" headline comes from one maintainer benchmark.

- Techniques: Fastify + Vite SSR wiring for React; Confirm SSR before benchmarking; AutoCannon 10-second load test; Separate warm and cold start numbers
- Tools: Fastify, Fastify React (fastify-react renderer), Vite, React, Next.js, AutoCannon, Vercel, DigitalOcean, Webpack, React Server Components (discussed, not adopted by Fastify React), Nuxt, Vue

## [How to Setup Redis Caching in Node](../videos/QqTB97aMa4c.md)
`QqTB97aMa4c` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

A beginner Node.js tutorial that adds Redis caching to an Express endpoint, load-tests before and after with Artillery, and briefly compares cache-aside, write-through, write-behind and refresh-ahead.

- Techniques: Redis server setup on Ubuntu (systemd-supervised); Node client connection with error, ready and connect handling; Cache-aside (lazy loading) on an HTTP search endpoint; Normalizing cache keys; Before and after load test with Artillery; Write-through; Write-behind (write-back); Refresh-ahead; Deciding what to cache
- Tools: Redis (server, default port 6379), redis (npm client for Node.js), Node.js, Express, npm, Artillery (load testing, installed globally), redis-cli, Ubuntu (apt-get, systemd), VS Code, PM2 (npx pm2), Git (used to diff benchmark results), Hacker News API (external upstream in the demo)

## [Unmasking hidden costs of microservices with Vojtech Vondra](../videos/nw2oVC3ycd4.md)
`nw2oVC3ycd4` · Better Stack · 2024-11-02 · q3 · practitioner · talk · also: governance-compliance

A Microsoft identity engineer argues microservices carry hidden costs that multiply with each service, and that teams should stay small (about five services) unless they are very large.

- Techniques: Count n before splitting into services; Cross-cutting concerns checklist; Design interfaces and communication first; Measure boilerplate ratio
- Tools: Azure

## [Docker with Node.js: Build, Run, and Manage Containers](../videos/ozFFCrMedFM.md)
`ozFFCrMedFM` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: dev-tools, observability

Beginner Docker tutorial for a Node.js app: write a Dockerfile and .dockerignore, run on a custom network with a Postgres container, bind 0.0.0.0, orchestrate with Docker Compose and healthchecks, then ship logs to Better Stack.

- Techniques: Dockerfile skeleton for a Node app; .dockerignore for Node projects; Build and run with a tag, env file and network; Point the DB host at the container name; Bind the HTTP server to 0.0.0.0 (Fastify); docker-compose.yml with healthcheck gating; Container log and resource inspection; Vector log shipping to Better Stack
- Tools: Docker, Docker Compose, Docker Hub, Node.js (20.16 LTS base image, node:20.16-alpine3.19), npm, Alpine Linux, Fastify, Express, PostgreSQL, Vector, Better Stack

## [Introduction to Node Clustering](../videos/Nz0OfV2L5m0.md)
`Nz0OfV2L5m0` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: dev-tools

Better Stack tutorial on Node.js's cluster module: fork one worker per CPU core to get past single-threaded Node, benchmark the gain with autocannon (22k to 61k requests in 10s), then do the same with PM2 and note the state and logging caveats.

- Techniques: Hand-rolled cluster primary with respawn; Benchmark before and after with autocannon; PM2 cluster mode; Move shared state out of workers
- Tools: Node.js, cluster module (node:cluster), os.availableParallelism, Express, autocannon, PM2, Pino, Winston, Better Stack

## [How to Setup Uptime Kuma - Self Hosted Monitoring](../videos/t4Nb-09oZSw.md)
`t4Nb-09oZSw` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: dev-tools, observability

Walkthrough of self-hosting Uptime Kuma with Docker to monitor sites, then building public status pages and incidents. The back half pitches Better Stack's managed service.

- Techniques: Uptime Kuma Docker install; HTTP(s) monitor settings; Keyword check; Status page setup; Better Stack escalation and recovery
- Tools: Uptime Kuma, Docker, Node.js, PM2, Better Stack, Playwright, Plausible, Google Analytics, Discord, Slack

