# evals — 319 videos

*evaluation methods, LLM-as-judge, benchmarks, eval-driven development*

By channel: AI Engineer 257 · Kai Explains 19 · AI LABS 15 · Better Stack 28

**Synthesized guide:** [guides/evals.md](../guides/evals.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Why We Rebuilt Microsoft Office From Scratch for AI Agents - Yijia Liang, Compound AI](../videos/v0UkV5qS9E4.md)
`v0UkV5qS9E4` · AI Engineer · 2026-11-01 · q3 · practitioner · talk · also: multi-agent, rag-retrieval, enterprise-adoption

Compound's Yijia Liang explains why they rebuilt Excel, PowerPoint and Word as headless Rust engines for finance agents, using the real Office apps as an oracle in agent loops, plus email-based multiplayer agents and swarm-based file processing.

- Techniques: Objective-function loop against the incumbent app as oracle; Own the write-render-check-fix loop with a headless engine; Grep-first agent swarm over a large file corpus with citations; Email as the multiplayer interface for an agent
- Tools: Compound (getCompound.ai), IronCalc, Microsoft Excel, Microsoft PowerPoint, Microsoft Word, OpenPyXL (transcribed as 'OpenPAxcel' / 'OpenPi Excel'), Outlook, SharePoint, Box, Microsoft Teams, Claude, ChatGPT

## [If Your AI Scores 100%, Your Eval Is Wrong - Ramakrishnan Lokanathan, eslams.com](../videos/7WUzHIF32vA.md)
`7WUzHIF32vA` · AI Engineer · 2026-11-01 · q3 · practitioner · talk · also: testing-verification, observability

Ramakrishnan Lokanathan argues evals should test the job a system must do, not just a score: test every workflow step, add real failures as regression tests, and make tests harder as scores approach the ceiling.

- Techniques: Ambition-first eval scoping; Step-level workflow evals; Three-layer eval stack; Failure-to-regression loop; Ratcheting the test difficulty; Game-based multi-agent evals (eslams)
- Tools: eslams (open-source Python package, speaker's project, eslams.com), SWE-bench, Humanity's Last Exam, Nemotron 3 (the speaker says he was a red-teamer for these models), GPT-3, ChatGPT, Google Assistant, Gemini, Parallel AI search index (named as 'parallel search model index' in the captions), MIT GenAI Divide report (cited, not named as a tool)

## [Avalon Just Beat Strata by 47% on AMD (9x Faster)](../videos/0F63pTS8Gt0.md)
`0F63pTS8Gt0` · Kai Explains · 2026-11-01 · q4 · practitioner · review · also: local-ai, inference-serving

Breakdown of the "Avalon beats Strata by 47% on AMD" claim: a llama.cpp fork tuned for one 7900 XT box, and why the number only holds on that machine and that model file.

- Techniques: Benchmark provenance checklist; Bandwidth-ceiling estimate for MoE decode; Expert cache from spare VRAM with CPU fallback; Cheap draft head that shares the expert cache for MoE speculative decoding; Perplexity as a fast quant-quality screen, with a caveat; mmap for models larger than VRAM plus RAM; Diagnose multi-GPU slowdowns as a bottleneck shift
- Tools: Avalon (llama.cpp fork, MIT, repo live Oct 9 2026, Qwen 3.8B Flash Next only, Linux only, RDNA3 required by installer), Strata (AMD-focused inference engine for MoE models; 0.1.43 in the table, 0.2.8 current), llama.cpp (stock, with an open draft PR from Piotr Wilkin), Boon llama.cpp fork (source of the first expert cache version in Avalon), ik_llama.cpp (source of Avalon's compression types), Unsloth IQ4 quantization (perplexity reference), Strata ISTA quantization format, Claude Opus (the video says version 5.5; the README credits it with writing the GPU and CPU kernels), ROCm (AMD software stack, cited as the lagging part), Vulkan (Avalon has no Vulkan backend, so it does not run on Windows), Qwen 3.8B Flash Next (MoE: 125B active, 51B lookup table, 48 layers, 512 experts per layer, top-10 routing)

## [78% Wanted This AI Feature. Almost Nobody Used It - Supriya Subudhi, Bumble](../videos/CvmZtAPmAW4.md)
`CvmZtAPmAW4` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: product-ux, token-cost-efficiency, governance-compliance

Bumble's Supriya Subudhi argues that a positive A/B test is only the start for AI features, and lays out five checks: real adoption, tail-of-distribution outputs, cost versus benefit, model cost-quality tradeoffs, and legal market readiness.

- Techniques: Adoption-first AI feature rollout; Segment-level eval review over averages; Guardrails on advice scope; Eval-driven model and prompt selection under a cost budget; Write down the business reason for each AI feature; Regulatory check before building
- Tools: Meta Muse AI (mentioned as an example of a US/Canada-only launch), Amazon AI shopping assistant (mentioned as an example), Spotify AI DJ (mentioned as an example)

## [Voice AI Where One Wrong Question Breaks the Rules - Shiv Indap, Upstart & Brooke Hopkins, Coval](../videos/3osCbSufv8g.md)
`3osCbSufv8g` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: voice-multimodal, governance-compliance, observability

Coval and Upstart walk through a regulated voice-agent (lending verification calls) eval loop: human review, judge calibration, failure routing, and simulation before release.

- Techniques: Judge-human calibration loop; Structured human review queues; Clustering and anomaly detection for unknown failure modes; Failure-to-owner routing; Voice simulation before release; Feature-flagged agent changes with named approvers
- Tools: Coval (voice-agent evaluation and simulation platform), Google Sheets (initial manual review tracking), LLM-as-judge, RL pipelines and fine-tuned LLMs (mentioned as options for self-healing, not shown)

## [Why Humans Can't Keep Up With AI-Written Code - Tariq Shaukat, Sonar](../videos/LQW_Wvqhp04.md)
`LQW_Wvqhp04` · AI Engineer · 2026-10-30 · q3 · practitioner · talk · also: software-factory, testing-verification, governance-compliance

Vendor talk arguing AI-generated code makes volume cheap but confidence scarce, so software factories need intent, guide rails, independent verification and evidence, with LLM judges treated as unreliable.

- Techniques: Code confidence formula as a factory checklist; Guide rails over guard rails; Deterministic plus agentic verification mix; Measure judge stability before trusting an LLM judge; Model per-step reliability to pick task length
- Tools: SonarQube, Sonar Vortex, Claude Mythos preview (named as the model in the Meter study, version as stated in talk)

## [The Cheaper AI Model That Costs You More - Rayan Krishnan, Vals AI](../videos/rWtbOgl5FTU.md)
`rWtbOgl5FTU` · AI Engineer · 2026-10-30 · q4 · practitioner · talk · also: token-cost-efficiency, enterprise-adoption, models-research

Vals AI's Rayan Krishnan argues model cards hide a "jagged frontier" by task and metric, and that cost-per-task evals, real-work benchmarks and routing can cut enterprise AI spend without losing output.

- Techniques: Pareto plotting of cost per task vs performance; Report partial credit and fully-correct rate together; Build evals from historical work (PR and issue replay); Sandbox hygiene against reward hacking; Resumable eval infrastructure; Task-level usage-limit right-sizing
- Tools: Vals AI benchmarks (Vals Index, Finance Agent benchmark, Excel modeling / LBO, tax agent), Vals Smith (internal eval-driven coding product), Opus 5.5 (Anthropic), Fable 5.1, Sonnet, GPT 5.6 Sol, Kimi K3

## [Stop Guessing Your vLLM Config: Benchmarking LLMs on Runpod - Chris Vela, Runpod](../videos/P_0_Th_ZzIg.md)
`P_0_Th_ZzIg` · AI Engineer · 2026-10-28 · q2 · practitioner · review · also: inference-serving, infra-cost-scaling

RunPod's Chris Vela argues for benchmarking vLLM configs on GPU pods across concurrency levels before production, and previews an unreleased BenchPod template. Vendor pitch with some reusable method.

- Techniques: Config-sweep benchmarking before production; Tune max batched tokens for long generations; Pin vLLM and CUDA to what the model needs; Agent-readable benchmark and health API; Model choice by task size and team size
- Tools: RunPod (GPU pods, serverless, storage volumes, Docker images), vLLM (OpenAI-compatible server, YAML config, nightly builds), BenchPod (unreleased RunPod template built on vLLM, with FastAPI, a watchdog and benchmark metrics), Kimi K3, DeepSeek, GLM, Qwen 3.8 (transcribed as 'Quinn 3.8'), Docker, NVIDIA B300, NVIDIA H200, CUDA 12.8 and 13.0, Claude (mentioned as the service many internal users are moving off)

## [We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI](../videos/YIhvrvHtonk.md)
`YIhvrvHtonk` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: agent-architecture, context-engineering, memory

Arize's PM on two years of shipping Alex, its in-product agent: keep the loop, plan, stop rule and memory in harness code, use small capped memory files, and treat production traces as regression tests.

- Techniques: Render the plan into the harness on every call; Explicit finish call as a harness gate; Tool results as pointers, not inline content; One small capped markdown memory file per user; Single model call instead of a loop for narrow features; Production sessions as living regression fixtures; Trace-reading agent for silent failures
- Tools: Arize AX, Alex (Arize in-product agent), Signal (Arize trace-reading agent), Sonnet 4.5 (auto-caption 'Sonic 4.5'), jq, Arize experiments

## [Stop Giving Your Agent Tools. Give It a Sandbox - Mikyo King, Arize AI](../videos/dAoOYFx7ZYw.md)
`dAoOYFx7ZYw` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: sandboxing-execution, mcp-and-tools, token-cost-efficiency

Arize's Mikyo King argues agents should get a search tool plus a code sandbox instead of a large tool catalog, reporting 43% fewer tokens and 31% lower cost in their own Harbor evals, while listing open problems such as secrets, permissions, and durability.

- Techniques: Search-then-execute tool access (code mode); Bash plus CLI as the first sandbox; Hoist REST CRUD endpoints into a sandbox language; SQL as an aggregate-query escape hatch; Keep secrets out of the model's context; Signed handoff for binary artifacts; Sandboxed, multi-trial agent evals with pass@k; Trajectory-driven instruction hill-climbing
- Tools: Arize Phoenix, Harbor Framework, Claude Code, MCP, Bash, Python sandbox, SQL (text-to-SQL), SWE-bench, PyDurable (named in the talk; caption may be garbled)

## [What a $900M Bank Error Teaches Us About AI Agents - John Feminella, Two Sigma](../videos/iniryju23Sk.md)
`iniryju23Sk` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: governance-compliance, security-guardrails

Two Sigma's John Feminella ties a 2020 bank loan-payment error to AI agent governance and lays out five composable controls: registry, risk scoring, declared guardrails, shared evals, tiered approvals.

- Techniques: Tiered approval routing; Registry auto-registration through approved frameworks; Declared-capability manifest enforced at init; Risk-based review routing; Platform-owned shared eval harness
- Tools: FlexCube (internal bank processing software, as named in the talk), Claude Code, Pi (open-ended coding agent, as named in the talk), OpenClaw (named as 'open claw' in the talk)

## [How a Trading Firm Ships New AI Models the Same Day - Noyan Tokgozoglu, Optiver](../videos/aGIUg8zKI8A.md)
`aGIUg8zKI8A` · AI Engineer · 2026-10-27 · q4 · practitioner · talk · also: enterprise-adoption, token-cost-efficiency, multi-agent

Optiver's head of AI engineering on running an AI platform where every decision shows up in P&L within hours: same-day model adoption, token-spend control, and narrowly scoped agents on a shared gateway.

- Techniques: Golden-set benchmarking on day zero; Gateway-first model onboarding checklist; Replace default MCP context with tool search and CLI wrappers; Analyze cache invalidation before tuning cache TTLs; Move reference material out of the system prompt into retrieval; Per-team alerts and self-managed spend limits; Point-in-time tool snapshots with per-invocation confidence; Scope agents narrowly and version them; Ship internal portal with contributions via PRs
- Tools: Claude Code (referenced as the "cloud code" moment in the auto-captions), Codex (OpenAI coding agent; the speaker says it lacked self-hosted managed agents until recently), MCP (Model Context Protocol) servers and MCP tool search, OpenTelemetry (OTEL) logging, Slack client, Internal inference gateway, agent gateway, agent workbench, meta-harness layer, and web portal (Optiver in-house)

## [How to Test Your Agents on Real Tasks With Harbor - Xander Song, Arize AI](../videos/kRJjSOYqW0I.md)
`kRJjSOYqW0I` · AI Engineer · 2026-10-27 · q4 · practitioner · talk · also: testing-verification, observability, coding-agents

Xander Song (Arize) introduces Harbor, an open-source framework for testing agents on real tasks in fresh sandboxes, scored by side-effect verifiers, and shows how his team used it to tune a prompt for SQL over GraphQL.

- Techniques: Harbor task layout; Oracle-first validation; Keep verifiers outside the agent's view; Synthetic task and oracle generation; Before/after prompt A/B in a fixed harness; Read-only SQL tool for aggregates; Single-node app snapshot in Docker; One-turn skill-triggering test
- Tools: Harbor, Docker, Arize Phoenix, OpenInference, OpenTelemetry, OTLP, ATIF (Agent Trajectory Interchange Format), Daytona, Modal, E2B, SQLite, Postgres

## [Agents That Self Improve While You Sleep - Fuad Ali, Arize AI](../videos/UGuNt2_Oz8s.md)
`UGuNt2_Oz8s` · AI Engineer · 2026-10-27 · q3 · practitioner · workshop · also: observability, skills-self-improvement, pr-code-review

A vendor-led workshop on closing an agent self-improvement loop: scheduled trace review, failure datasets, evals, replay experiments, and human checkpoints at the high-leverage points.

- Techniques: Trace-to-fixture pipeline; Trajectory-level LLM-judge eval; Cheap-first evaluator stack; Replay-based fix validation; Confidence-threshold human routing; Session-level eval signals; Stop criteria for eval depth
- Tools: Arize AX (tracing and evals platform), AX CLI, Arize Signal (always-on trace-review agent), Arize Alex (in-house agent), Phoenix (mentioned, not demonstrated), Arize managed sandboxes, GitHub, Codex, Cursor, Claude Code, OpenCode, Modal

## [What Does an AI Engineer Do Now? - Aparna Dhinakaran, Arize AI](../videos/ImnZ7s68jw8.md)
`ImnZ7s68jw8` · AI Engineer · 2026-10-26 · q3 · practitioner · talk · also: software-factory, observability, agent-architecture

Arize's Aparna Dhinakaran argues the AI engineer's job is now building the build-eval-ship-monitor-improve loop itself, with always-on agents consuming telemetry and evals aligned to human judgment.

- Techniques: Telemetry-triggered always-on agent sweep; Issue memory across agent runs; Sandbox-per-run with single proxy egress; Durable agent resume; Harness and model abstraction with per-run evaluation; Evaluator alignment against golden data; Offline plus online evals on the same definitions; Trace the coding agents too
- Tools: Arize Signal, Arize Evaluator, Claude Code, Cursor, Codex, Anthropic model family (multiple models, unnamed)

## [Is Flint the Killer of Qwen 3.8 27B? (First RSI Model)](../videos/RmE4G6MhOVU.md)
`RmE4G6MhOVU` · Kai Explains · 2026-10-26 · q4 · practitioner · review · also: local-ai, inference-serving, models-research

Kai Explains tests Recursive's Flint MoE coding model: the 131 tok/s headline is real, but always-on reasoning, long-context slowdown and agent loops mean task completion time is what matters.

- Techniques: Bandwidth-bound decode estimate; Time-to-task-completion benchmark; Token-budget cap test; Split prefill from decode timing; Hybrid planner and implementer; Fair engine comparison; Hardware fallbacks reported by users
- Tools: Flint (Recursive, 39.8B MoE, 2.5B active, 256 experts, 262,144-token text-only context, Apache license), Recursive REC inference engine (Mac-only, proprietary), Apple MLX, llama.cpp (Vulkan build on AMD), Ollama (23 GB model file), Unsloth 4-bit and NVFP4 weights (25 GB 4-bit file, 11.9 GB smallest quant), vLLM (NVFP4 run on RTX Pro 6000), Qwen dense 27B and Qwen MoE 35B (as named in transcript), OpenCode (agent, 5-minute silence timeout, free tier), Pi (Recursive's own agent, ~17k-token system prompt), OpenRouter (free Flint access), Terminal Bench 2.1

## [How to Build Voice Agents That Don't Fall Apart When You Interrupt - Jesse Hall, LiveKit](../videos/OmyqelTwpOo.md)
`OmyqelTwpOo` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · also: voice-multimodal, inference-serving

LiveKit's Jesse Hall argues voice agents must be evaluated as whole conversations: measure time-to-first-audio and time-to-first-sentence, use non-blocking tool calls, use audio-aware turn detection, and benchmark full stacks with simulated callers.

- Techniques: Time-to-first-audio and time-to-first-sentence instrumentation; Non-blocking (async) tool calls in a voice agent; Audio-aware turn detection; Full-stack scenario simulation with identical replay; Regression scenarios from production failures; Financial voice-agent guardrail checklist
- Tools: LiveKit (open-source real-time agent framework and infrastructure), LiveKit turn detector (audio + transcript end-of-turn model), LiveKit inference (model serving tuned for voice; speaker says it is model agnostic), Gemma 4 31B (auto-caption reads 'Gemma 431B'; top LLM on the hotel agent benchmark), ChatGPT advanced voice mode (cited as using LiveKit)

## [How to Write Your First AI Eval - SallyAnn DeLucia, Arize AI](../videos/gv4w23xYj-0.md)
`gv4w23xYj-0` · AI Engineer · 2026-10-26 · q3 · practitioner · workshop · also: observability, multi-agent

A hands-on workshop on writing a first LLM-as-judge eval for an agent: why vibe checks fail, how traces feed evals, how to write concrete criteria, and how to build and iterate a judge in a prompt playground.

- Techniques: Six-part criteria template; Judge prompt structure; Variable mapping for judge inputs; Span-level dataset selection; Iterate the judge in a prompt playground against a dataset; Alignment against human labels; Online evals on incoming traces; Decision-model comparison; Instrumentation: auto, manual, or hybrid
- Tools: Arize AI (Arize AX platform, captioned 'Arise' or 'AX'), Alex (Arize's in-platform AI agent that can run playgrounds and iterate on prompts), Signal (Arize's managed agent that reads traces, finds issues and proposes fixes), OpenInference (Arize's tracing package with auto-instrumentors for agent frameworks), OpenAI decision model API (mentioned as released the week before the talk), Anthropic, OpenAI and Gemini provider API keys (configured under AI providers in settings), ROUGE and BLEU (named as code-based eval metrics), Notion one-pager (workshop instructions)

## [Your Agent Fix Just Broke Something Else - Sofia Jakovcevic, Arize AI](../videos/v5tm5EAzsAs.md)
`v5tm5EAzsAs` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · also: observability, testing-verification, multi-agent

A five-step regression loop for agents built on production traces, evaluators and CI gates, so a prompt or policy change is judged on numbers before it merges. Vendor-led demo of Arize.

- Techniques: Five-step trace-driven regression loop; Four-bucket dataset composition; LLM-as-judge plus code evaluators; Side-by-side prompt versions in a playground; Agent playground against a remote agent; Run experiments from coding agents through skills; CI gate on experiment results
- Tools: Arize (Arize AI observability backend and platform, incl. prompt hub, prompt playground, agent playground, experiments, datasets), Arize agent skills repository (public, for coding agents), GitHub Actions (CI example), Arize SDK / REST / CLI (run experiment), LLM-as-judge evaluators (pre-built: hallucination, user frustration, security checks; custom evaluators supported)

## [AI Writes the Code. So What's Left for Engineers? - Laurie Voss, Arize AI](../videos/kspZP5BgkEU.md)
`kspZP5BgkEU` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · also: context-engineering, pr-code-review, product-ux

Laurie Voss (Arize AI) argues coding agents have made code writing nearly free, so the bottleneck moves to code review, ops and security, and ultimately to defining what "good" means, which makes "product engineers" the lasting role.

- Techniques: Theory-of-constraints bottleneck mapping; Review only high blast-radius code; Automatic verification for cheap-to-check work; Turn reviewer feedback into rules; Mergeability benchmark instead of test pass rate; Measure outcomes, not output volume
- Tools: Claude Code, GitHub Copilot, Cognition Devin, Cursor Bugbot, OpenAI Codex, Claude, Pragmatic Engineer newsletter, Arize AI

## [Why Frontier Models Fail as Buy-Side Analysts - Janie Gu, Google DeepMind & Suyeol Yun, LinqAlpha](../videos/aVbRSIQO2dE.md)
`aVbRSIQO2dE` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: sandboxing-execution, observability, models-research

Google DeepMind's Kaggle team and LinkAlpha present why most agent benchmarks are unreliable, what Kaggle found reproducing 65 of them, and MandateBench, a buy-side analyst benchmark graded on reasoning paths.

- Techniques: Reproduce, then read every trace before trusting a score; Separate the agent under test from the grader; Log every model call and keep traces open; Measure variance with repeated runs; Pin reasoning effort explicitly for head-to-head comparisons; Rubric-based grading of a reasoning graph; What-if perturbation of key assumptions; Reconcile conflicting source figures explicitly
- Tools: Kaggle, Kaggle Benchmarks, Google DeepMind models (as evaluated), MandateBench, HuggingFace (named as a place models searched for answers), Reddit and StackOverflow (named as places models searched for answers), Heijen's Code to Video Bench (captioned name; launched last week per speaker), Octava, Quadrillion, Rehearsals (partner names as captioned)

## [Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management](../videos/ZMZlAn6Pyfg.md)
`ZMZlAn6Pyfg` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · also: governance-compliance, enterprise-adoption, mcp-and-tools

A hedge-fund head of AI explains how Contour measures AI ROI: live A/B tests of analyst workflows, process metrics over slow P&L, cost per useful insight, and connector-maintenance time counted as a cost.

- Techniques: Live A/B workflow capture; Agent-synthesized vs analyst-synthesized expert calls; Cost per useful insight; Idea-resurfacing agent; Alt-data via MCP or API connectors into agents; Connector-maintenance time as an ROI line item
- Tools: AlphaSense, Yipit, Rogo, Hebbia, Bloomberg, MCP, APIs (vendor data)

## [Can AI Understand a Distressed Credit? - Harneet Kaur, Axim Intelligence](../videos/WOszaC1WWbQ.md)
`WOszaC1WWbQ` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · also: data-engineering, models-research

Founder of Axim Intelligence on testing whether LLMs can forecast distressed credit outcomes; models disagreed until a structured, layer-by-layer reasoning process made them converge, though no ground truth was shown.

- Techniques: Layer-by-layer benchmarking of an LLM analysis pipeline; Cross-model disagreement as a diagnostic; Structured reasoning scaffold to force convergence
- Tools: Opus (Opus 5.5, as named in transcript), Astra 6 (named in transcript; the model name may be an auto-caption error)

## [Google's Harness² Is This the End of Harness Engineering?](../videos/yCgfyQmqhPM.md)
`yCgfyQmqhPM` · Kai Explains · 2026-10-24 · q4 · practitioner · review · also: context-engineering, skills-self-improvement, token-cost-efficiency

Critical read of Google's Harness² paper, where a second model rewrites an agent's harness files through a Propose/Probe/Compose loop. Headline gains are measured against an empty harness with a frontier editor, and token cost runs 8x to 40x a plain run.

- Techniques: Propose, Probe, Compose harness editing; A/B probe before keeping any harness edit; Trigger line on every skill; Place guidance by cost: skill, then script, then sub-agent, then plugin, then always-on text; Reopen-and-verify rule before declaring done; Exact output path and filename rule; Forbid plain-text tool calls; Restrict network before running a self-improvement loop; Put a cap on multi-run loops
- Tools: Harness Square (Google Cloud AI Research paper, Oct 2026), GLM-5 (Z.ai), Gemini 3.5 Flash, Claude Opus 4.8 (editor and judge in the paper), Claude Code, OpenCode, CodeBuddy, Codex (OpenAI Codex agent), MetaHarness (Hugging Face legal tool), WorkBuddy (benchmark), Jobbench (benchmark), Harvey legal agent benchmark

## [This Tiny Qwen 27B Model Runs on a 12GB GPU](../videos/XKejQWnispc.md)
`XKejQWnispc` · Better Stack · 2026-10-24 · q3 · practitioner · review · also: local-ai, inference-serving, mcp-and-tools

Better Stack reviews Saluki 27B, a ~7.9GB quantization of a 27B Qwen-family model tuned to keep tool calling intact at the cost of math, and tests it on local llama.cpp and a DGX Spark.

- Techniques: Serve a GGUF quant locally with llama.cpp; Two-part tool-calling smoke test; Tool-call reliability count; Recommended settings for tool calls; Report strict and lenient parser scores separately; Measure agent throughput, not just file size; Pick by workload
- Tools: Saluki 27B (model name as captioned; the transcript attributes it to Underdog), Qwen 27B base model (captioned as 'QEN 3.827B'), Qwen 3.8 Flash (captioned as 'Quen 3.8 Flash next'; used as a comparison model at 4-bit), llama.cpp (llama-server, stock build), Ollama, Unsloth quants (4-bit, IQ2_XXS, IQ2_S), ISTA-DAS Lab 2-bit quant (RCO quantization search), Ternary Bonsai 2 (PrismML custom llama.cpp fork), MLX (an unfinished port was mentioned), BFCL (Berkeley function-calling benchmark, single-turn), AIME 2025, SWE-bench Verified (50-task subset)

## [Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni Analytics](../videos/A3FL_zTQKU0.md)
`A3FL_zTQKU0` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · also: testing-verification, observability, governance-compliance

Stephanie Jarmak (Omni Analytics) argues agent evals should be done like experiments: check the tool pipeline end to end, match the benchmark to your own workload, decouple flags from enforcement, and trust independent traces.

- Techniques: Tool-use pipeline audit; Harness-plus-model pairing as the unit under test; Workload-representative internal benchmark; Explicit metric choice per use case; Separate flagging from enforcement; Independent record comparison for trust; Shadow deployment and production measurement; Autonomy boundary spec for each action
- Tools: Amp (coding agent), Sourcegraph code search MCP tool, Claude (as used in the grep example), grep, Terminal Bench (transcribed as 'Terminal Bench 4'), OpenHands (open coding-agent harness), Opus 5 (model, as transcribed), Astra (model or harness, as transcribed; unverified), Code Scale Bench (speaker's own public benchmark for large codebases), LLM-as-judge (generic pattern), Omni Analytics evaluation harness (in progress)

## [How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada](../videos/c_SPW__jF9w.md)
`c_SPW__jF9w` · AI Engineer · 2026-10-22 · q4 · practitioner · talk · also: rag-retrieval, enterprise-adoption

Air Canada's data science team explains how they built evaluation sets with no public benchmark: generate test cases from known answers, grade them with code, and avoid LLM-as-judge.

- Techniques: Answer-first synthetic eval for retrieval QA; Plant-the-defect known-answer tests; Remove-a-clause mutation test; Template fill-in combinatorics; Invariance tests; Trajectory checks for tool-using agents; Prefer code graders over LLM-as-judge; Strip complexity before adding techniques
- Tools: BM25, LLM-as-judge, Text-to-SQL (mentioned as an example pattern)

## [1,368 AI Failures and What They Teach About Evals — Vishal Srivastava, New York Life & Tanmay Sah](../videos/mMw3arwQsL0.md)
`mMw3arwQsL0` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · also: governance-compliance, agent-architecture

Talk using AI Incident Database cases to argue for risk-based, system-level evals: test the whole deployment and the evaluator, try to falsify claims, and prioritize by harm.

- Techniques: Three-dimension, 13-sub-dimension incident taxonomy; Prioritize controls by harm association, not frequency; Materiality scale per AI use case; Four-part risk decomposition; System-level stress testing of the deployment; Evaluator reliability check; Build-break-fix falsification loop
- Tools: AI Incident Database (publicly available database of AI failure reports, used as the analysis corpus)

## [Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI](../videos/_dTF3NpPzGo.md)
`_dTF3NpPzGo` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · also: token-cost-efficiency, models-research

Louis-François Bouchard (Towards AI) releases ToneBench, an LLM-judged benchmark for whether models write like a specific author, and shares its method, judge-bias findings and costs.

- Techniques: Multi-draft variance measurement; Category-then-rating judge rubric; Cross-family LLM judging; Blind judging with post-hoc attribution; Human pairwise calibration; Contaminated-eval guard; Cheap-draft then strong-merge writing pipeline
- Tools: ToneBench (the speaker's new creative-writing benchmark, from Towards AI), EQBench Slop Score (referenced as prior art; the speaker does not rebuild it), Opus 5.5 (Extra High and Max Thinking modes, as named), GLM 5.3 Flash, GPT 6.1 (named), Grok 4.7 (transcribed as 'Gruk 4.7')

## [Is a Faster Model Actually Faster? Test the Whole Job — Morgan Suo, MiniMax](../videos/YvQ4BVTWfHI.md)
`YvQ4BVTWfHI` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: inference-serving, token-cost-efficiency, models-research

MiniMax's Morgan Suo argues a faster model must be judged on a whole research job (sources, numbers, cost, latency, retries), not on tokens/sec or averages, and walks through M3.1 Flash's sparse attention, KV-cache and expert quantization, speculative decoding, and reasoning-effort trade-offs.

- Techniques: Whole-job acceptance eval; Planted-fact position sweep for long-context retrieval; Per-subscore regression check instead of averages; Concurrency sweep with P95 time-to-first-token; Reasoning-effort budget comparison with a recorded setting; Reproducibility record and staged rollout
- Tools: MiniMax M3.1 Flash (LLM, long context, MoE, sparse attention, KV-cache quantization, reasoning effort control), MiniMax A3 (video generation model, shown in opening and closing segments), speculative decoding (serving method), KV cache (serving-side internal memory of keys and values), MoE experts (routed experts with 4-bit weights and activations, shared expert unchanged)

## [Anthropic Barely Reads Claude's Code Anymore](../videos/d8QpDbBKbAU.md)
`d8QpDbBKbAU` · Better Stack · 2026-10-20 · q4 · practitioner · news · also: pr-code-review, claude-code, multi-agent

Secondhand summary of how Anthropic reviews Claude Code's own PRs: layered automated review, risk-tiered human sign-off, incident-derived reviewer evals, and round caps for agent-vs-agent loops.

- Techniques: Layered review pipeline with a voting gate; Turn repeated reviewer findings into durable rules; Per-directory review.md written by code owners; Merge gate with explicit false-positive dismissal; Incident-derived reviewer eval with a keep-or-drop rule; Noise metric from comment outcomes; Round cap, scoped re-review, and whole-class flagging for agent loops; Risk tiering with a classifier agent and a second check
- Tools: Claude Code, CLAUDE.md, review.md, PR template, lint rules, CI (tests, type checking, linting)

## [The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft](../videos/UGjk3Uk0MxM.md)
`UGjk3Uk0MxM` · AI Engineer · 2026-10-20 · q4 · practitioner · workshop · also: mcp-and-tools, models-research, agent-architecture

Hands-on workshop comparing GPT-5.5, Kimi K2.6, DeepSeek V4 Flash and Mistral Large 3 on counting, RAG grounding, vision, tool calling, agent loops, evals and DSPy prompt optimization.

- Techniques: Single-variable model swap harness; Chain-of-thought decomposition for counting; Grounded RAG prompt with explicit refusal and citation; Tool definitions as prompt engineering; Low-level tool-call loop; Force tool use over mental math; Give date math to a tool; Deterministic checks first, LLM-as-judge second; Spec-driven eval generation with Assert; DSPy with GEPA for prompt optimization; Anthropic document citations
- Tools: Microsoft Foundry, GPT-5.5, Kimi K2.6, DeepSeek V4 Flash, Mistral Large 3, OpenAI Python SDK, OpenAI Responses API, Anthropic Messages API, uv, GitHub Codespaces, LangChain v1, PydanticAI

## [How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase](../videos/_4Ph2dhmUFI.md)
`_4Ph2dhmUFI` · AI Engineer · 2026-10-20 · q3 · practitioner · talk · also: governance-compliance, agent-architecture, multi-agent

Coinbase's Evan Kormos on deciding when an agent can run unsupervised: keep the process deterministic on the outside, model it as a graph with policy boundaries, and earn autonomy per node through measured evals.

- Techniques: Policy-bounded DAG process map; Cyclic review node with a bounded loop; Per-node automation checklist; Graduated autonomy rollout; DAG state injected into agent context; Statistical evaluation over repeated runs; Exception-flow and volume monitoring
- Tools: Apache Airflow, LangGraph (transcript says LangChain Langraph)

## [Stop Telling Agents How](../videos/7T-gldvgfpo.md)
`7T-gldvgfpo` · AI Engineer · 2026-10-19 · q3 · practitioner · talk · also: context-engineering, agent-architecture, multi-agent

OpenProse founders argue agents should be given declarative Markdown contracts plus triggers, not step-by-step prompts; the talk is largely a product demo of their hosted runner.

- Techniques: Contract-first workflow spec; Codify a golden trace into pinned steps; Event-driven job = contract + trigger; Fresh-session verifier against the contract; Kernel as a bootloader index; Templated multi-agent shapes; Cheap verifier or router (planned, not shipped)
- Tools: OpenProse, run.pros.md (hosted OpenProse runner), pros CLI (pros write, pros run), npx skills (skill install mechanism), Claude Code, Codex, Exa (search), DSPy (contrasted), n8n (contrasted), pi (agent harness without sub-agents, transcribed as 'pie'), Matt Pocock's skill workflow (grill-me, TDD) used as an example, Haiku (cheaper model mentioned)

## [Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa](../videos/L4dUFimVDKU.md)
`L4dUFimVDKU` · AI Engineer · 2026-10-19 · q2 · practitioner · workshop · also: rag-retrieval, data-engineering

Exa's forward-deployed engineer demos ExaSnapshot, point-in-time web search for backtesting agents without future leakage, plus a hands-on acquisition-prediction exercise. Mostly a vendor pitch, but the leakage and holdout-set points hold regardless of vendor.

- Techniques: Point-in-time (as-of date) retrieval for backtests; Content versioning for trusted historical features; Feature-by-feature backtest with a holdout set; Scoring rubric for event prediction; Pin the repo state for coding-model evals
- Tools: Exa, ExaSnapshot, Cursor, Gamma, ChatGPT, Claude

## [Qwen 3.8 27B Just Hit 200 Token/s on Mac M5 (Lithos Metal)](../videos/L7noXCBSObc.md)
`L7noXCBSObc` · Kai Explains · 2026-10-19 · q4 · practitioner · review · also: local-ai, inference-serving

Dissects Lithos Metal's "200 tok/s" Qwen 27B claim on Apple M5 Max: a projection, with ~80 tok/s measured end-to-end. Speculative decoding helps on code, hurts on English, and agent sessions are prefill-bound.

- Techniques: Estimate decode ceiling from memory bandwidth; Speculative decoding with a small drafter; Measure acceptance rate alongside tok/s; Estimate whole-session time from prefill and decode rates; Time the whole task instead of quoting tok/s; Lower thinking-mode effort for local Qwen; Read the benchmark repo before the blog post
- Tools: Lithos Metal (engine, v0 Zero 1.2 mentioned), Qwen 3.8 27B (model, 4-bit), dSpark (speculative-decoding drafter, 1.1 GB), DeepSeek speculative decoding paper (July), MLX, MLX D-SPARK, Ollama, OMLX, D-Flash 2 (Z-Lab and Inco), Splash (Inco), MLTF (as transcribed), AgentPerfLocal (benchmark that replays agent sessions)

## [Version-Controlled Search: The Web as It Was — Ryan Ahern, Exa](../videos/vS2IA9pq0Q4.md)
`vS2IA9pq0Q4` · AI Engineer · 2026-10-19 · q2 · intro · talk · also: rag-retrieval, token-cost-efficiency

Exa vendor talk on version-controlled search (Exa Snapshot): query the web as it stood at a past date, and use that to backtest agent-driven financial features without look-ahead leakage.

- Techniques: As-of (point-in-time) search for backtesting; Holdout validation for agentic features; Separate search-tool eval from model eval; Per-task cost measurement for retrieval
- Tools: Exa, Exa Snapshot, Exa Agent Ultra, Cursor, Gamma, ChatGPT, Claude

## [Nokia Just Released a Free Jev Alternative (AnyJev)](../videos/hJz7zi17mXA.md)
`hJz7zi17mXA` · Better Stack · 2026-10-19 · q3 · practitioner · review · also: local-ai, models-research

Better Stack tests Nokia's AnyJEV, a training-free library that turns open models into probability-based classifiers; it fixes order bias but trails hosted JEV on accuracy and calibration.

- Techniques: Decision-model setup (AnyJEV flow); Order-swap flip test; L0 debiasing without labels; Confidence reliability check; Local throughput budgeting for debiased runs
- Tools: AnyJEV (Nokia applied research, Python, Apache 2.0), JEV decision model (hosted API via TypeSafe, v1.13), Qwen3 8B (run locally via llama.cpp on an M2 Max MacBook Pro), Hugging Face Transformers, vLLM, SGLang, llama.cpp, Kaggle News Headlines Dataset for Sarcasm Detection (28,619 headlines), Small demo app published by the host on GitHub

## [Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs](../videos/W4pnzOURwHQ.md)
`W4pnzOURwHQ` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: data-engineering, enterprise-adoption, governance-compliance

Insurance claims data is messy, so AI claims work needs layered extraction, duplicate detection, human verification, and calibrated tiered benchmarks before cross-claim analytics pay off.

- Techniques: Layered extraction with per-level verification; Tiered benchmark with a private held-out tier; Calibrated multi-judge verification; Back-test on historical samples before pilot; Duplicate and co-mingling detection at intake; Human-in-the-loop surfacing with page references
- Tools: Artificial Analysis MLCR benchmark, GPT models, Anthropic models, ChatGPT, Gemini, Claude

## [Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS](../videos/q4WC4TowkBo.md)
`q4WC4TowkBo` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: testing-verification, coding-agents, context-engineering

Build deterministic verifier CLIs and evidence "receipts" so coding agents can prove their own work is done, closing the loop without the human reading every line of code.

- Techniques: Per-app verifier CLI with subcommands; Deterministic end-to-end prove step with Playwright; System-one LLM judge for fuzzy outcomes; Doctor/preflight plus stale-proof detection; Centralized verifier gate on workflow nodes (CTX); Babysitter agent for PR follow-through; Generate many variants and select via eval; Saboteur/detective bug-injection test of the verifier; Evidence attached to PRs; Outcome-first prompting with clear stop conditions; Error messages written for agents; Post-deploy monitoring agent
- Tools: Playwright, Chrome DevTools, pnpm, GitHub CLI (gh), GitHub API, Cloudflare Workers, MCP, Reptile, CodeRabbit, Datadog, Claude Code, Pi

## [Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse](../videos/obfPzbapMIM.md)
`obfPzbapMIM` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: observability, testing-verification, governance-compliance

Langfuse workshop on evaluating high-stakes agents: trace everything, build datasets from production via expert error analysis, mix LLM-judge with deterministic evaluators, and gate prompt changes in CI.

- Techniques: Annotation queue for expert error analysis; Free-text comments to failure-mode taxonomy via LLM; Mixed evaluator suite (LLM judge + code checks); Prompt-promotion-triggered CI eval gate; Mask PII before persisting traces; Shadow runs for ground-truth building; Judge calibration against a human-labeled sample
- Tools: Langfuse, GitHub Actions, ClickHouse, PostgreSQL, Amazon S3, OpenAI chat API, Anthropic models, Whisper Flow, Claude, Langfuse skill (agent skill)

## [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](../videos/SHMCGrNJJGc.md)
`SHMCGrNJJGc` · AI Engineer · 2026-10-17 · q4 · practitioner · workshop · also: observability, testing-verification

Hands-on workshop: trace a Claude financial-analyst agent in Phoenix, read failures, write code and LLM-judge evals, validate judges against human labels, run experiments, and gate CI on them.

- Techniques: Deterministic code eval with structured input; Faithfulness judge with full retrieval context; Five-part LLM judge prompt with constrained labels; Judge hygiene: different-family, stronger judge, suppressed tracing; Open coding then axial coding of traces, with a coding agent; Golden dataset with dev/test split by stable ID; Run experiments on the failing subset only; pass^k reporting for nondeterministic agents; Vitest-based eval suite gated in CI; Eval-driven development
- Tools: Arize Phoenix, Claude Agent SDK, Claude Code, Claude Sonnet 5.5, Claude Haiku 4.5, Claude Haiku 5.5, Vercel AI SDK, OpenTelemetry, OpenInference, Vitest, GitHub Actions, TypeScript

## [How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival](../videos/8g1N_a3h9H0.md)
`8g1N_a3h9H0` · AI Engineer · 2026-10-15 · q4 · practitioner · talk · also: token-cost-efficiency, context-engineering, observability

Alvin Pane (OutRival) on cutting LLM token spend in production: measure baseline variance with a ceiling test, shrink prompts with DSPy-style optimization, downsize models, then gate release on paired shadow-deployment stats with a lower confidence bound above zero.

- Techniques: Ceiling test (self-agreement baseline); Prompt optimization as search (DSPy-style); Prefix-cache-friendly prompt structure; Split pipeline by model size; Paired shadow-deployment statistics
- Tools: OpenTelemetry, DSPy, Jeepa optimizer (as transcribed; likely DSPy's GEPA optimizer)

## [Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket](../videos/gonAewBZxfU.md)
`gonAewBZxfU` · AI Engineer · 2026-10-15 · q4 · practitioner · talk · also: rag-retrieval, agent-architecture, data-engineering

Two In The Pocket engineers describe a RAG assistant over a Belgian payment scheme's rulebooks: section-aware chunking, table flattening, hybrid retrieval, agentic narrow-to-wide tools, and noisy LLM-judge evals.

- Techniques: Section-path chunking without overlap; Table flattening for merged cells; Hybrid dense plus BM25 with RRF; Narrow-to-wide agent tool ladder; Tool-level recovery guardrails; Stream prose, render structured parts last; Lightweight feedback logging; Promptfoo end-to-end evals plus retrieval-only eval
- Tools: Qdrant, BM25, Reciprocal Rank Fusion, Promptfoo, Pydantic, LLM-as-judge

## [I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](../videos/dYh7TQkuYFE.md)
`dYh7TQkuYFE` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: testing-verification, multi-agent

Corey Gallon (Rexmore) presents a three-level agent review method, each level built as a skill, that catches agents overstating work, misreading facts, and reasoning errors, shown on three real cases.

- Techniques: Deliverable contract with a self-check the sender runs; Fan-out / fan-in with independent identical agents and a source-anchored adjudicator; Control-total anchoring; Claim labeling self-audit; Cold persona reviewers with no context; Fresh-reviewer final pass

## [What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad](../videos/gDRCpTMCqEU.md)
`gDRCpTMCqEU` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: governance-compliance, enterprise-adoption

A technical due diligence checklist for AI productivity claims: check the arithmetic of workload vs. human labor, define what "automated" means, and verify quality with experts before trusting a number.

- Techniques: Workload-vs-labor arithmetic check; Straight-through processing boundary; Blind expert review of grader output; Cost per accepted autonomous task; Diligence questions checklist
- Tools: Faros telemetry, Meta grader study

## [Deploying AI Inside a Bank Is Not an Engineering Problem — Paden Gayle, Applied AI Engineers](../videos/3ZlQk4-knWM.md)
`3ZlQk4-knWM` · AI Engineer · 2026-10-14 · q3 · practitioner · talk · also: governance-compliance, enterprise-adoption

Paden Gayle argues that shipping AI inside a bank is a discovery problem: find the people who own each decision in week one, shrink the scope, limit the model's authority, and build an evidence pack from sprint one.

- Techniques: Week-one decision discovery; Dependency-mapped architecture diagram; Shadow, draft, shrink; Four-rung autonomy ladder; Model proposes, human submits boundary; Five-file evidence pack with failure table; Decision-time record capture; Segment-first evaluation reporting; Five-question readiness scorecard

## [Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire](../videos/rAUyRDOFyHU.md)
`rAUyRDOFyHU` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: enterprise-adoption, agent-architecture, sandboxing-execution

Flywire's engineers describe Orbit, an internal platform that runs deterministic code with small LLM steps, gated by YAML definitions, per-step permissions and human-reviewed merge requests.

- Techniques: Deterministic-first workflow with scoped LLM steps; Strict JSON output schema with targeted retry; Per-step capability allowlist declared in config; Skill first, then workflow; Isolated node evaluation with production-trace golden sets; Per-step model selection; Separate orchestration, runtime and session state
- Tools: Claude Agents SDK, Claude Code, AWS ECS Fargate, AWS Lambda microVMs, GitLab, Jira, Sentry, Slack, OpenTelemetry, MCP, YAML, Victoria (internal PaaS)

## [Just-in-Time Ontologies: What Cheap Intelligence Means for Data — Hrishi Olickel, Southbridge AI](../videos/Fa3hQVIKShw.md)
`Fa3hQVIKShw` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: data-engineering, token-cost-efficiency, agent-architecture

Hrishi Olickel (Southbridge AI) argues there is no universal schema, so build just-in-time ontologies per decision, using cheap model tiers, cross-family disagreement, and a failure surface.

- Techniques: Split the job into typed cases before modeling; Fix the question definition, not the threshold; Cross-family disagreement as the audit signal; Cost-tiered checking budget; Bounded pilots, then reusable codons, then production; Pareto surfing with a fixed baseline; Check for prior-driven silent errors
- Tools: Hank Weave (captions: Hank Wave, open-source harness for headless data work), Claude Code (captions: cloud code), Opus, Anthropic Claude models (cheap reasoning tier and frontier tier)

## [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](../videos/p7gaxmCUiIU.md)
`p7gaxmCUiIU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: skills-self-improvement, agent-architecture, voice-multimodal

Browserbase's Shubhankar Srivastava shows an auto-research loop in which a doer agent and a teacher agent iterate on a strategy file until browser-agent tasks converge into reusable skill.md files that cut cost and latency.

- Techniques: Teacher-doer auto-research loop with strategy file; Converged output as a skill.md artifact; Binary success verifier with minimal guardrails; Scheduled sample runs and failure-triggered healing; Three-layer security for learned skills; Objective choice in the teacher's criteria
- Tools: Claude Agent SDK, Claude Code, Codex, Opus 4.8, Sonnet, Browserbase browse CLI, Browserbase SDK, Stagehand, Browse.sh, WebMCP, Karpathy auto-research, OpenClaw

## [Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI](../videos/fnuNVFgLjHA.md)
`fnuNVFgLjHA` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: observability, skills-self-improvement, software-factory

Arize workshop on closing an agent's detect, investigate, fix, verify loop using an always-on trace-analysis agent, coding-agent skills, harness-as-judge scoring and replay experiments; mostly a product walkthrough.

- Techniques: Continuous failure clustering over production traces; Join trace evidence with the code path; Plain-language harness-as-judge rubric with tool access; Failure-dataset replay with agent experiments; Alert-triggered agent investigation; Agent skills for trace analysis from the coding agent
- Tools: Arize Signal, Arize skills, Arize agent experiments, Claude Code, OpenAI Agents SDK, FastAPI, Datadog, GitHub, Cursor, Codex

## [Continuously Improving Agents with Langfuse — Annabell Schäfer & Lotte Verheyden, ClickHouse](../videos/BOCjybvJYM4.md)
`BOCjybvJYM4` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: observability, coding-agents

Hands-on Langfuse workshop on monitoring agents in production: instrument traces, write failure-mode evaluators (LLM-judge and code) on live traces, then use a coding agent over trace data to find silent failures.

- Techniques: Failure-mode-first evaluator set; JSON-path variable mapping for LLM judges; Boolean code evaluators on live observations; Coding agent as trace analyst; Coverage monitoring
- Tools: Langfuse, OpenAI Agents SDK, OpenAI API, Codex, Claude Code, TypeScript, Python

## [Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic](../videos/QSeaZ6qHyXs.md)
`QSeaZ6qHyXs` · AI Engineer · 2026-10-12 · q3 · practitioner · other · also: agent-architecture, multi-agent, sandboxing-execution

Anthropic presenters answer audience questions on Claude Managed Agents: YAML-as-code deployment, eval sweeps, tenant isolation via workspaces, long runs, and sub-agents for custom tools.

- Techniques: Agent definitions as YAML synced by CI; Parallel eval sweeps on new model releases; Historical-session eval dataset; Workspace-per-customer isolation; Rubric-based exit criteria for long runs; Coordinator with a custom-tool sub-agent; Per-thread session mapping for multi-user chat
- Tools: Claude Managed Agents (CMA), Anthropic CLI (transcribed as 'Ancho CLI'), Claude Code, Modal, E2B (transcribed as 'EB2'), Daytona, Slack

## [The Autonomous Computer: Infrastructure for Computer Use Agents — Ang Li, Simular](../videos/tyFPqtyOK5w.md)
`tyFPqtyOK5w` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: voice-multimodal, agent-architecture, sandboxing-execution

Ang Li (Simular) on computer-use agents: why reliability needs a neurosymbolic loop, where the agent writes code that is replayed, and why pass^k matters more than pass@1.

- Techniques: Neurosymbolic replay with healing; Accessibility-tree grounding with IDs; Per-step observation choice; Clarification-first prompt; Reverse-check verification of entries; Rules-first guardrail chain; Exploration swarm for changing UIs; Test-time scaling by agent count; Save-to-skill with parameters
- Tools: Simular Agent S / S2 / S3 harnesses, Simuland (open-source scripting language), Claude Code, OSWorld, OSWorld 2, Playwright, Windows 365 for agents (Microsoft), Simular cloud desktop API and CLI, GPT-4V, GPT-5, GLM 5.2

## [Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI](../videos/_zUp6y9bDU8.md)
`_zUp6y9bDU8` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: observability, coding-agents, skills-self-improvement

Arize's Ankur Duggal argues agents need trace-based evals, then demos a coding agent (Claude Code plus Arize skills) turning production traces into failure analysis, datasets, evaluators and experiments.

- Techniques: Trace-to-dataset-to-experiment loop; Coding agent as eval workflow driver; Mixed evaluator set; Sampled online evals; Tailored evals from observed failures
- Tools: Arize AX, Phoenix, Claude Code, Codex, Cursor

## [Parsing the Epstein Files for JMail — Palak Agarwal & Omar Alhait, Reducto](../videos/HGfsfKaVuGY.md)
`HGfsfKaVuGY` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: data-engineering, product-ux

Reducto staff show how their parse-then-extract pipeline turned 3M+ messy Epstein-file PDFs into the JMail sites, then run a hands-on extraction exercise.

- Techniques: Parse-then-extract pipeline; Agentic OCR with self-correction; Schema review in a playground before deploy; Content-aware schema generation; Separate citation pass; Per-use-case prompts on specialized sub-models; Tiered evaluation with your own benchmark
- Tools: Reducto Studio, Reducto parse, split, extract, edit and classify APIs, Claude Code or Codex (paste-in setup instructions via a QR code, per the speaker)

## [Teaching Agents to Search with NVIDIA Data Designer — Dhruv Nathawani, NVIDIA](../videos/qFaKvbVc5cE.md)
`qFaKvbVc5cE` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: training-finetuning-rl, data-engineering, rag-retrieval

NVIDIA workshop on NVIDIA Data Designer: build column-by-column synthetic data pipelines, seed them with Wikidata random walks and Tavily search traces, and use them to teach a model web search (BrowseComp 0 to about 30%).

- Techniques: Column-by-column DAG for synthetic data; Seeded random walks over a knowledge graph; Teacher trajectories with a tool, then SFT on the trajectories; Overproduce and filter funnel; Layered verification of synthetic labels; Skip the golden answer and use a reward function (RL path); Persona seeds from census marginals
- Tools: NVIDIA Data Designer, Nemo Curator, Nemo Gym, Nemo Anonymizer, Nemo Safe Synthesizer, Tavily, MCP, vLLM, gpt-oss-120b, Wikidata, Hugging Face

## [Do Claude Get Quietly Nerfed After Launch..(We Have Proof)](../videos/SxLUx8-hN1o.md)
`SxLUx8-hN1o` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: claude-code, token-cost-efficiency, models-research

Claude "nerfs" are usually config changes (effort defaults, harness bugs, silent model fallback) rather than weight changes; track output tokens, tool calls and app version alongside any score.

- Techniques: Pin and set effort explicitly per model; Disable silent model switching in Claude Code; Choose effort by task type; Mine local session logs for token and tool-call metrics; Regression diagnosis by three signals; Multi-sample tracker with a detection threshold
- Tools: Claude Code, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.6, Claude Opus 4.7, Claude Opus 4.8, Claude Sonnet 4, GPT-6 Astra (as named in the talk), LiveNerf (daily tracker), Nerfbench (daily tracker), MarginLab (daily SWE-Bench Pro tracker), SWE-Bench Pro

## [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](../videos/YIxzNZDDy1A.md)
`YIxzNZDDy1A` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: observability, sandboxing-execution, coding-agents

Wolfram Ravenwolf's hands-on workshop on building a reproducible agent benchmark (Terminal-Bench via Harbor, WolfBench dashboard), arguing that one averaged score hides variance, cost and configuration choices.

- Techniques: Multi-metric leaderboard per configuration; Pin the harness and keep a fork; Sandbox per trial with bounded concurrency; Smoke-test one task before the full run; Explicit retry policy by error class; Set and record every sampling and agent setting; Trace-first debugging of surprising scores; Shareable result snapshot
- Tools: Harbor, Terminal-Bench 2.0, Terminus 2, Weights & Biases Weave, WolfBench, Inspect (UK AISI), Marimo, CoreWeave serverless sandboxes, Daytona, OpenRouter, Docker, uv

## [Parameter Golf with AutoResearch — Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI](../videos/7RFJRDYroic.md)
`7RFJRDYroic` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: software-factory, agent-architecture, context-engineering

Hands-on workshop on autoresearch loops, where an agent edits code, a fixed eval scores each attempt, and only improvements are kept. Covers eval design, bounded runs, steerability and the Parameter Golf results.

- Techniques: Fixed-budget eval contract; Tree-of-attempts search with per-node diffs; Guidance file as the steering channel; Hidden validation set for contests and benchmarks; Constrained single-metric optimisation; Bridged session for direct steering
- Tools: Weco, Modal, Claude Code, Opus 4.8, OpenAI MLE-bench

## [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](../videos/KhRjivBSwiw.md)
`KhRjivBSwiw` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: context-engineering, data-engineering, mcp-and-tools

TypeDef's talk and workshop argue that data and code agents need a computed, traversable context graph; deterministic structure comes first, and agents still default to grep unless tools are shaped and measured.

- Techniques: Deterministic structure first, LLM last; Layered extraction ladder for code; Persistent typed graph with subgraph traversal; Blast-radius tool before edits; Incremental re-indexing keyed to changed files; Isolated data clones for evals, with injected bugs; Tool renaming and shape-matching; Consistency and adoption metrics; Many small focused LLM questions; Eval set pinned to a snapshot, with near-failing tasks
- Tools: Neo4j, Cypher, tree-sitter, rustdoc JSON, Pydantic AI, pydantic evals, Fennec, OpenRouter, Logfire, dbt, Snowflake, Databricks

## [Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI](../videos/PwCSYy-oGsM.md)
`PwCSYy-oGsM` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: governance-compliance, enterprise-adoption, product-ux

Druid AI argues containment rate misleads agent evaluation and proposes a weighted, 0-2 scored framework (six pillars, 26 components) judged like an employee and re-run weekly against a human baseline.

- Techniques: Component scoring with weighted clusters; Mandate-first agent definition; Success criteria attached to each task; Weekly re-run against a human baseline; Hybrid accuracy measurement; Central handoff and action-center check; Skill-source and granularity review; Error tolerance set by mode; ROI as freed human time

## [Agents That Own Their Inference — Du'an Lightfoot & Khaja Omer, Akamai Technologies](../videos/4n08JHb90hI.md)
`4n08JHb90hI` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: inference-serving, local-ai, infra-cost-scaling

Akamai hands-on workshop on self-hosting LLM agents on a single GPU with vLLM: memory budgets, prefill vs decode, FP8 quantization, speculative decoding, and finding the concurrency knee.

- Techniques: Memory budget math; Concurrency sweep to find the knee; One-flag-at-a-time tuning; Quantize with your own eval set; Validate speculative decoding by acceptance rate; Prefix caching for repeated context; Own-vs-rent break-even
- Tools: vLLM, Kubernetes, LKE (Akamai Linode Kubernetes Engine), KServe, SGLang, TensorRT-LLM, llama.cpp, Ollama, Prometheus, Grafana, Langfuse, LLM Compressor

## [Vector Isn't Enough: Hybrid Search & Retrieval — Jeff Vestal & James Williams, Elastic](../videos/ksjwtQop4os.md)
`ksjwtQop4os` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: rag-retrieval, mcp-and-tools

Hands-on Elastic workshop on why hybrid search (BM25 plus dense vectors, fused with RRF or linear weights, then reranked) beats vector-only retrieval for RAG and agent tool use.

- Techniques: Reciprocal Rank Fusion (RRF) hybrid search; Linear combination with min-max normalisation; Filter before ranking; Retrieve then rerank in one request; Search templates routed by an LLM (poor man's auto-tuning); Semantic_text with default sentence chunking; LLM answer with citations from retrieved sources; Index-description tool for agents; Point-in-time pagination
- Tools: Elasticsearch (serverless), Kibana / Discover, Elastic Inference Service, Jina embedding and reranking models (Elastic acquisition), Agent Builder (Elastic agent platform), ES|QL, Jupyter notebooks, Elastic workflows and MCP endpoint

## [Latency Is a Budget. Humanlike Is the Goal. — Jesse Hall, LiveKit](../videos/j4AmIK6OvHc.md)
`j4AmIK6OvHc` · AI Engineer · 2026-10-11 · q3 · practitioner · talk · also: voice-multimodal, agent-architecture

LiveKit's Jesse Hall argues voice-agent latency is a budget to spend on human-like behavior, not raw speed, and shares audio-based turn detection, perceived-latency metrics, async tool handling and an outcome-scored simulated-caller benchmark.

- Techniques: Perceived-latency metric; Async tool with early turn release; Audio-based end-of-turn detection; Speculative LLM on provisional transcript, TTS on first sentence; Outcome-scored simulated-user benchmark; Stack-level model selection; Checklist for voice agents
- Tools: LiveKit (open-source real-time agent framework and infrastructure), LiveKit Inference (hosted model inference), LiveKit turn detector (audio-based end-of-turn model), Gemma 4 31B (tuned for voice on LiveKit Inference; auto-captions render it as 'Gemini 4 31B' at one point), ChatGPT advanced voice mode (cited as an example of a LiveKit-powered product), LiveKit voice eval harness and hotel-booking benchmark (open source)

## [Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI](../videos/TyPpSRXGhbc.md)
`TyPpSRXGhbc` · AI Engineer · 2026-10-10 · q4 · practitioner · talk · also: training-finetuning-rl, data-engineering

Snorkel AI and UC Berkeley Sky lab trained a 4B Qwen3 agent with RL for under $500 that beats its 235B variant on finance QA; simple binary rewards and single-table curricula won.

- Techniques: Multi-stage synthetic eval and training data pipeline; Company-level data split to prevent leakage; Binary reward with reference-based LLM judge; Single-table-first data mixture; Decorator-based RL wrapper for existing agents; Large concurrent rollout generation
- Tools: RLLM, GRPO, Qwen3 4B and 235B, GPT-5 nano (judge), FinQA benchmark, BFCL, EDGAR, H100

## [Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain](../videos/KGFyOtl5ktI.md)
`KGFyOtl5ktI` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: agent-architecture, memory, context-engineering

Jake Broekhuizen (LangChain) argues agent memory is a read-write loop: capture traces, filter them into signal, and promote only the durable parts into long-term context, with human review for procedural memory.

- Techniques: Trace-to-memory capture, analyze, update loop; Classify memory into semantic, episodic and procedural buckets; Gate procedural memory updates with human review and evals; Check the hot path for memory staleness
- Tools: LangSmith, LangSmith Context Hub, LangChain, OpenClaw, HermesAgent

## [We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman](../videos/k2ClBT4aqAg.md)
`k2ClBT4aqAg` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: context-engineering, coding-agents

Postman's engineer describes an API context graph over 115+ microservices, grounded in code and telemetry, that improves coding-agent answers on API discovery, shape analysis and impact assessment, with a token-efficiency gain and a staleness warning.

- Techniques: Code- and telemetry-grounded API context graph; Retrospective PR-based eval with quality-vs-tokens plot; Context layer exposed as a skill next to a generic coding agent; Treat graph staleness as an eval regression; Run expensive architecture checks cheaper and earlier
- Tools: Postman API context graph, Claude Code, GitHub code search, Postman AI agent

## [Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab](../videos/Emo5FGGY-wM.md)
`Emo5FGGY-wM` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · also: product-ux, observability

Amazon AGI Lab's Felipe Blanes on why static evals fail in production: run an eval flywheel fed by real customer signals, and be transparent about product limits, since trust rises more from honesty than from higher benchmark scores.

- Techniques: Eval flywheel with customer signals; Trajectory caching with model fallback; Stated-limitations disclosure; Non-technical authoring layer on an agent core
- Tools: Amazon Nova Act

## [The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](../videos/TeErpYBUIeM.md)
`TeErpYBUIeM` · AI Engineer · 2026-10-07 · q3 · intro · talk · also: observability, skills-self-improvement

Langfuse co-founder on moving agent improvement from manual trace review to an AI-driven loop, where agents propose fixes and dataset/evaluator updates while humans set goals and gate changes, with a changelog-writer case study.

- Techniques: Online plus offline eval loop; Agent-proposed fix with human gate; PR review decisions as eval signal; Backtest candidate against baseline; Agent-maintained evaluators from error patterns; Scheduled batch loop over labeled production data
- Tools: Langfuse, Langfuse agent skills, GitHub pull requests, coding agent, Langfuse prompt management, Langfuse annotation queues

## [Why Building an Eval Platform Is Harder Than It Looks — Braintrust](../videos/mUQoVz7THu0.md)
`mUQoVz7THu0` · AI Engineer · 2026-10-07 · q2 · intro · talk · also: observability, data-engineering

Braintrust's solutions lead on why eval platforms are a systems problem: a maturity path from spreadsheets to production-trace flywheels, plus why agent traces are hard to store and query.

- Techniques: Three-part minimal eval harness; Production-failure-to-test-case flywheel; Side-by-side experiment UI for prompt and model changes; Separate hot and cold paths for trace data; Natural-language headless eval runs via coding agents
- Tools: Braintrust, BTQL

## [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](../videos/eXA2tjRZIbY.md)
`eXA2tjRZIbY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · also: agent-architecture, observability

Resolve AI's architecture for production-ops agents (on-call, incidents, background tasks): six pillars covering model routing, context, causal evidence, governed actions, learning loops, and multi-level evals.

- Techniques: Alert-as-prompt investigation fan-out; Evidence-chain gate on root causes; Per-subtask model routing; Tiered action permissions; Five-level eval stack; Anti-sycophancy by design
- Tools: Grafana, Slack, Microsoft Teams, Google Cloud (GCP), graph RAG, knowledge graph

## [The Transcript Looked Fine. The Call Wasn't. — Debugging Voice Agents, Arize](../videos/42Bz0TUfeOQ.md)
`42Bz0TUfeOQ` · AI Engineer · 2026-10-06 · q2 · practitioner · talk · also: observability, voice-multimodal

Arize PM Fuad Ali on why voice agent failures are invisible in transcripts, and how to trace audio sessions, run audio-native evals, and close an observe-evaluate-improve loop. Partly a product pitch, with real open-source instrumentation content.

- Techniques: Session-stitched voice trace view; Provider-agnostic semantic conventions for LLM traffic; Audio-native evals for tone, latency and interruptions; Online evals on spans with monitors that trigger investigation; Replay failed traces against a patched endpoint to verify a fix
- Tools: Arize, OpenInference, OpenTelemetry, Grafana, WebSocket realtime API, GPT Realtime, Gemini Live, LiveKit

## [From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI](../videos/F0TNSmbo5hE.md)
`F0TNSmbo5hE` · AI Engineer · 2026-10-06 · q2 · practitioner · workshop · also: observability, software-factory, claude-code

Arize workshop on closing the agent improvement loop: instrument an OpenAI Agents app with OpenInference, have a coding agent mine traces and patch failures, then automate it with Arize Signal. Vendor-heavy.

- Techniques: Turn on OpenInference tracing for an agent app; Install vendor agent skills into the repo for the coding agent; Trace triage that looks past error status; Single-problem fix loop with re-verification; Triage automated findings into issues, dataset rows, evaluators or PRs; Regression and guardrail evals before merging an automated fix
- Tools: Arize AX, Arize Signal, Alex (Arize in-product assistant), OpenAI Agents SDK, OpenInference, Arize AX CLI, Claude Code (VS Code extension), npx skills (arise-ai skills), npm, GitHub, WonderToys demo app (Arize sample)

## [Evals in AI: A Deep Dive — Tejas Kumar, IBM](../videos/NdrSPm6NCdk.md)
`NdrSPm6NCdk` · AI Engineer · 2026-10-06 · q4 · practitioner · workshop · also: testing-verification, rag-retrieval

Tejas Kumar (IBM) walks through evals as fuzzy unit tests for non-deterministic agents, then builds an LLM judge live, calibrates it against hand-labelled data, and gates CI on human agreement.

- Techniques: Judge calibration loop against a golden set; Pointwise pass/fail judging; Bias probes for judges; CI agreement gate; Pin the judge model version; Living eval dataset from production traffic; Cheapest-first eval ladder; Adversarial and synthetic eval generation; Avoid fuzzy string matching on LLM output
- Tools: Vitest, Cursor, GPT-3.5 Turbo, GPT-4o-mini, Docling, OpenSearch, OpenRAG (IBM), LM Arena

## [Your LLM Judge Is a Confident Liar: Building Better Verifiers — Browserbase](../videos/xLxhT2ZI7UM.md)
`xLxhT2ZI7UM` · AI Engineer · 2026-10-06 · q4 · practitioner · talk · also: testing-verification, training-finetuning-rl, voice-multimodal

Browserbase and Microsoft researchers on why LLM judges confidently mis-grade web agents, and their rubric-and-evidence "universal verifier" that agrees with humans far better, plus its use for filtering training data.

- Techniques: Rubric-first LLM verification; Per-criterion top-K screenshot evidence; Dual verdict: partial-credit score plus boolean outcome; Controllable vs uncontrollable failure schema; Error isolation across dependent criteria; Human-agreement validation with held-out labels; Verifier as data filter for SFT; Auto-research loop to build a verifier, primed with human findings
- Tools: WebVoyager, Online Mind2Web (captioned as 'Online Minor Web'), OSWorld, GPT-4o, Opus 4.6, Cohen's kappa, Browserbase, Microsoft open-source web-agent framework (captioned 'StateGen')

## [Advanced Workshop: Mastering AI Observability — Doug Guthrie, Braintrust](../videos/hfEczxdNyvU.md)
`hfEczxdNyvU` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: observability, coding-agents

Braintrust workshop on AI observability: trace agents, score production traffic with judges and topics, and let a coding agent run the eval-and-fix flywheel through the Braintrust CLI.

- Techniques: Binary, harsh LLM judges with examples in the prompt; Human-calibrated judges; Scores defined in code and pushed to the platform; Automation rules with scope and sampling for online scoring; Topic windows and filters for long conversations; Coding agent as flywheel operator; Service account for the analysis loop; Remote eval exposed to a playground; Mutable spans for attaching scores later
- Tools: Braintrust, Braintrust CLI (bt), OpenAI Agents SDK, Codex, Claude Code, Cursor, OpenCode, uv, GitHub Actions, Modal, ClickHouse, Brainstore

## [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](../videos/qZj7sqmidqA.md)
`qZj7sqmidqA` · AI Engineer · 2026-10-06 · q3 · intro · workshop · also: observability, testing-verification

A two-hour Arize AI workshop on replacing "vibes" with measurement: read traces, write code and LLM-judge evals, calibrate the judges, then close the loop with experiments.

- Techniques: Error analysis (open then axial coding); Code evaluator on trace or span; Context-matched LLM judge; Rubric structure for LLM judges; Judge calibration with golden labels; Test both directions; Experiments on a fixed dataset; Evaluator split by dimension, with guardrail vs north-star labels; Online sampled evals at span or trace scope; Eval-driven development and data priorities
- Tools: Arize AX, Arize Phoenix, OpenInference, OpenTelemetry, Claude Agent SDK, Anthropic Claude Haiku (agent model), Anthropic Claude Sonnet 4.6 (judge model), Claude Code, Cursor, Codex, Arize Skills (npx install), Alex (AX built-in eval agent)

## [Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust](../videos/T3SS931wU0I.md)
`T3SS931wU0I` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: rag-retrieval, coding-agents

Braintrust dev-rel walks through a small eval comparing agentic search (grep/find/cat in Claude Code) with vector search for finding bugs in the TypeScript Go repo: equal accuracy, but vector cost 4x more.

- Techniques: Eval composition: dataset, task, scorer, experiment; Production-log sampling into a dataset; Mining bug-fix PRs as coding-agent eval tasks; Binary scoring from the repo's own test suite; Forcing a retrieval strategy in a coding agent; Propagating parent span IDs to subprocess agents
- Tools: Braintrust (evals, tracing, UI, CLI, MCP server), Claude Code (agent harness, disallowed-tools flag), grep, find, ls, cat, bash (agentic search tools), Vector database (unnamed in the talk), Microsoft TypeScript Go repo and its test suite (dataset and scorer), Cursor semantic search post (cited as motivation)

## [I Gave a Robot Duck a 15MB AI Brain (Needle 3)](../videos/KQcQ7P78eTI.md)
`KQcQ7P78eTI` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: training-finetuning-rl, local-ai, mcp-and-tools

Walkthrough of Cactus Compute's Needle 3 on-device tool-calling model: a size-adjustable layer ladder, local fine-tuning on a robot-duck task, and a 49-prompt held-out eval (27% base, 84% fine-tuned 20-layer).

- Techniques: Closed-set tool dispatcher; Layer-truncatable model (intelligence ladder); Rule-categorised synthetic training data; Hand-written held-out scoreboard; Split controller from the LLM decision layer; Local fine-tune over LAN to a GPU box
- Tools: Needle 3, Needle 2, Cactus Compute fine-tuning platform, OpenDuck Mini, MuJoCo, DeepSeek V4 Flash, NVIDIA RTX 5090, ESP32, Pebble Index Ring, BDX droids (Disney)

## [Cloudflare Just Challenged Jev, So I Tested Their New Model (Clef)](../videos/Uihz1NkhFM0.md)
`Uihz1NkhFM0` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: models-research, token-cost-efficiency

Better Stack pits Cloudflare's open-weight Clef against Jev on 200 comments and 225 thumbnails: Jev wins on speed, cost and tone; Clef is close and reads images.

- Techniques: Probability-output classification for triage; Per-question agreement against a referee model; Separate latency and cost measurement, including the network
- Tools: Clef (Cloudflare, 27B and 9B Flash, open weights, up to 4 images), Jev (TypeSafe AI, released September 15, size undisclosed), Claude Opus 5.5 (used as referee), Cloudflare free daily allowance (10,000 neurons), YouTube (comments and thumbnails source)

## [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](../videos/33Oct2hqGnk.md)
`33Oct2hqGnk` · AI Engineer · 2026-10-05 · q2 · practitioner · talk · also: mcp-and-tools, agent-architecture, sandboxing-execution

AWS's Sandhya Subramani demos an agent that writes its own tools and sub-agents at runtime using three built-in tools (editor, shell, load-from-directory) plus a system prompt, then argues that evals and sandboxing are required before trusting it.

- Techniques: Meta-tooling bootstrap (three tools + system prompt); Check-before-write rule for generated tools; Self-repair on error; Sub-agent topology choice (swarm, graph, workflow); Layered agent evals; Four-part guardrail stack for self-modifying agents
- Tools: Strands Agents (AWS open source agent harness, Python and TypeScript), Python, OpenTelemetry (named as telemetry), Strands code-execution sandbox (recent feature, named in talk)

## [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](../videos/_mi3alkqy4s.md)
`_mi3alkqy4s` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: pr-code-review, testing-verification, observability

Laurie Voss (Arize AI) argues that agent code generation has outrun human review, so teams should stop reviewing PRs by hand and build an engineered review harness, with humans designing its definition of good.

- Techniques: Multi-pass review with consensus filtering; Default-suspicious reviewer prompt; Tool-using reviewer over the whole repo; Runtime verification by the agent itself; Machine-checkable mergeability rubric; Codify the definition of good as a harness
- Tools: GitHub Copilot code review, Cursor reviewer, CodeRabbit, Greptile, Graphite, Codex, Anthropic automated security review action, SWE-bench, SWE-bench Pro, FrontierBench

## [AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile](../videos/474j-n1Ltxc.md)
`474j-n1Ltxc` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: pr-code-review, coding-agents

Greptile's Daksh Gupta uses review data from its own PR pipeline to test whether fully agent-written PRs are worse than human PRs; his answer is roughly no on reverts, severity and review rounds, but failure modes differ by agent.

- Techniques: Signal-based detection of agent-authored PRs; Proxy quality metrics for agent PRs; Per-agent failure-mode profiling via keyword counts; Three-question PR validation gate
- Tools: Greptile, Codex, Claude Code, Devin, Cursor, GitHub

## [Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog](../videos/rTojoVotlD8.md)
`rTojoVotlD8` · AI Engineer · 2026-10-04 · q3 · intro · talk · also: observability, governance-compliance, security-guardrails

Datadog's Marina Petzel argues LLM apps need cost, safety and quality monitoring on top of the golden signals, since a 200 OK can still hide a wrong answer; gives tagging and metric recommendations.

- Techniques: Mandatory four-level cost tagging; Track token creep and model drift as separate alerts; Caching layer to remove redundant completions; Guardrail metrics as blocking thresholds; LLM-as-judge for completeness, embeddings for relevance; Score RAG retrieval separately
- Tools: Datadog agent observability

## [This Tiny Coding Model Shouldn’t Be This Good (MiniCPM5)](../videos/Wik_JQ-enUA.md)
`Wik_JQ-enUA` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: local-ai, inference-serving, models-research

Review of OpenBMB's 2B MiniCPM5: strong on agent and tool benchmarks against Qwen 3.5 4B, but quantized GGUF runs loop under the documented llama.cpp defaults until min_p and repeat penalty are changed.

- Techniques: Run a small model on a Mac with MLX in a virtualenv; Tool-calling smoke test against a local OpenAI-compatible server; Fix the quantized sampler before judging a small model; Count runaway generations, not just pass rate; Load a GGUF into Ollama or LM Studio without a library entry
- Tools: MiniCPM5 2B (text-only, OpenBMB), MiniCPM5 1B, MLX / mlx-lm, llama.cpp (server), GGUF, OpenAI-compatible client, WebLLM, Ollama, LM Studio, Hugging Face, Qwen 3.5 (2B and 4B), Gemma 4 E2B

## [Opus 5.5 vs GPT-6 Sol (Blender F1 Car Test)](../videos/Zc72O98x3nk.md)
`Zc72O98x3nk` · Better Stack · 2026-10-02 · q2 · practitioner · review · also: models-research, coding-agents, token-cost-efficiency

Better Stack runs Opus 5.5 (Claude Code) and GPT-6 Sol (Codex) through the same three Blender prompts (static F1 model, build animation, pit-stop animation); Opus wins on quality but costs about 6x more.

- Techniques: Same-prompt, same-order head-to-head across agent CLIs; Judge cost per finished task, not per token; Build an animation as a sequence of agent prompts
- Tools: Claude Code, Codex, Blender, Claude Opus 5.5, GPT-6 Sol, GPT-6 Astra, Fable 5.1, GPT-6 Luna

## [The GPT 6 Astra Vs Claude Fable 5.1 Debate Is Finally Over](../videos/BwNNcob3-A0.md)
`BwNNcob3-A0` · AI LABS · 2026-10-02 · q2 · practitioner · review · also: models-research, token-cost-efficiency, coding-agents

Blind-judged comparison of Claude Fable 5.1 and GPT-6 Astra on the team's own client-style projects: Fable wins quality, interaction and review depth; Astra wins cost, speed, instruction following and long-running builds.

- Techniques: Blind LLM-as-judge on your own tasks; Human-in-the-loop UI review with a per-model viewer; Autonomy test with a vague brief written in the model's own prompting guide style; Track output tokens and tool calls as cost drivers; Enforce file-edit tool use and check for violations afterward; Planted-bug review test with decoys; Check whether the model changed mid-run
- Tools: Claude Fable 5.1, GPT-6 Astra, GPT 5.6 (judge model), Claude Code, Codex, Claude Opus (referenced for design comparison), Cursor (named as a place to use the Zapier SDK), Zapier SDK

## [Is it Possible to Run Any LLM in Jev Mode Using llama.cpp?](../videos/Oi4JPj58lUA.md)
`Oi4JPj58lUA` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: inference-serving, local-ai, data-engineering

Breakdown of "Jeff mode": llama.cpp constrained choice scoring is fast, but its confidence score comes from masking and renormalizing, needs calibration on your own data, and its speed depends on model architecture.

- Techniques: Forced-choice classification via cached-prompt branch scoring; Single-field logprob check on the stock server first; Calibrated confidence gate with escalation; Temperature scaling for post-hoc calibration; Group requests by schema to keep the prompt cache warm; Benchmark hygiene for local inference; Keep dependent fields in plain generation
- Tools: Jeff (TypeSafe structured-classification product, as captioned; the title spells it 'Jev mode'), llama.cpp, llama.cpp fork by Kodakus (parallel constrained decoding, two commits), llama.cpp stock server (n_probs / logprobs parameters), NotJeff (project reproducing the approach with stock llama.cpp, Qwen3-8B reported), Qwen 1.5B (plain attention, 28 layers), Qwen3-8B (captioned 'Quen38b'), Qwen 3.6 35B-A3B (captioned 'Quen 3.635BA3B', MoE), Gemma 4 12B (captioned 'Gemma 412b', sliding-window), Insider LLM 27B model (described as dense; config shows hybrid), Banking77 (public bank-intent dataset), Temperature scaling (calibration method)

## [Most Vector DB Benchmarks Are Wrong. Here's The Fix. (Qdrant FineWeb 10b)](../videos/6Uj6GXIpX9s.md)
`6Uj6GXIpX9s` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: rag-retrieval

Better Stack walks through Qdrant's open 10B-vector FineWeb benchmark dataset, which ships exact nearest-neighbor ground truth, and reruns a 1M slice against four vector engines. Lesson: test on your own data with brute-force truth.

- Techniques: Exact brute-force ground truth on your own slice; Store deep ground truth and truncate for smaller k; Recall-vs-latency sweep per engine; Sequential, isolated engine runs over the same loaded data; Benchmark filtered and sparse/hybrid queries separately
- Tools: Qdrant, Milvus, Elasticsearch, PGVector (pgvector), FineWeb (Hugging Face dataset), GTE Multilingual Base (embedding model), MS MARCO (query set), Docker, Qdrant open-source benchmark toolchain (Apache 2.0; named 'Supernova' in the captions, name unverified)

## [This Open-Weights TTS Beat ElevenLabs... Then I Read the License](../videos/kJppefEh2ZA.md)
`kJppefEh2ZA` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: voice-multimodal, local-ai

Josh from Better Stack tests Breeze TTS 2, an open-weights voice model that tops a benchmark, then shows why its non-commercial weights license blocks most real use.

- Techniques: Local voice-design install on macOS; Lower CFG scale to make voice descriptions stick; Inline vocal-event markup; License check before adopting open weights; Read leaderboards for vote count and prompt control
- Tools: Breeze TTS 2 (Breeze Blue), MLX audio (mlx-audio, pip install), Qwen 3, Qwen3-TTS, T5Gemma 2, Mimi audio codec, ElevenLabs Conversational, Cartesia Sonic 3.6, Artificial Analysis speech arena, Kokoro, Chatterbox, VoxCPM2

## [Qwen 3.8 27B Just Got 2× Faster on Mac Same Hardware](../videos/qZTmBhKz7b0.md)
`qZTmBhKz7b0` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: local-ai, inference-serving

A debunk of the "Qwen 3.8 27B 2x faster on Mac" headline: the 2x comes from speculative decoding with a 1.2 GB draft model, not the Splash engine, and the built-in multi-token-prediction head gives smaller gains for free. Measure effective tokens/s with warm and cold cache, not decode speed.

- Techniques: Measure effective tokens per second, cold and warm; Enable the model's built-in multi-token-prediction head as a draft; Bandwidth ceiling sanity check; Isolate the variable in a benchmark; Fail fast on memory; Point coding agents at a local OpenAI or Anthropic-compatible endpoint
- Tools: Splash (Inco AI inference engine for Apple Silicon, Apache 2.0, Qwen 3.8 27B and 35B only), Inco AI, D-Flash 2 (Splash's 1.2 GB draft model), Qwen 3.8 27B and 35B (built-in multi-token-prediction head), OMLX (inference engine used as baseline), LM Studio (shipped Splash as a selectable backend), MLX, GGUF, llama.cpp, Ollama, SpeedBench (coding benchmark with reasoning mode), Claude Code

## [Meet Jev: The Schema-Safe AI Built to Make Decisions](../videos/BGDd26FiOm4.md)
`BGDd26FiOm4` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: token-cost-efficiency, inference-serving, models-research

Critical walkthrough of JEV (TypeSafe AI), a model that returns only probabilities for typed decision questions instead of text; fast and cheap, but accuracy and calibration caveats are the real story.

- Techniques: Probability gate instead of a generated yes/no; Choice query with full distribution for routing; Tool selection without a language model in the loop; Per-tool-call relevance filter for Claude Code; Adversarial state test before trusting the output; Evaluate against a solver or known-correct baseline; Local logit read of an open model for a single decision; Price a decision workload before adopting
- Tools: JEV (TypeSafe AI model, version 1.13 per the vendor page), TypeSafe AI, GPT 5.6 Terra (reference model as transcribed), GPT 5.6 Sol (reference model as transcribed), GPT-6 Astra (reference model as transcribed), Claude Fable 5.1 (reference model as transcribed), Qwen 3.5 4B (captioned as 'Quen 3.54b'; open-model reimplementation), Qwen 3.6 35B (captioned as '3.635B'; open-model reimplementation in the MMLU-Pro comparison), Claude Code (JEV plugin scoring tool calls), RLCD (Reinforcement Learning for Calibrated Decisions, the vendor's training method), MMLU-Pro (benchmark), Vercel

## [Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash](../videos/ACPEpji5NV4.md)
`ACPEpji5NV4` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: rag-retrieval, data-engineering, memory

DoorDash's search and personalization lead on using LLMs offline to create graded relevance labels, semantic IDs, and memory, then serving those through small, fast models.

- Techniques: Offline LLM labeling with a distilled labeler; Label-audit by disagreement; Two-stage contrastive retrieval with hard-negative curriculum; Auxiliary ordinal relevance tower with value-function blend; Hierarchical learned semantic IDs as sparse features; Multi-form consumer memory blocks; Batch generation of personalized content with the existing ranking stack
- Tools: GPT-4o mini (named as an example lightweight labeler)

## [Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta](../videos/jNE8No-wvok.md)
`jNE8No-wvok` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: multi-agent, voice-multimodal, training-finetuning-rl

Meta's Aditya Gautam on using a multi-agent system of small domain-tuned VLMs to find intra-video policy anomalies and duplicate content in short-form video, with a production judge-and-human feedback loop.

- Techniques: Orchestrator plus specialist agents for video review; Change-based frame compression; Per-signal index routing; Domain pre-training plus schema-constrained instruction tuning; Judge-plus-human-queue production loop; Distillation plus quantization sweep; Node-level evaluation suite; Pre-inference gating with cache and metadata
- Tools: CLIP, MCP, Ray, DPO, JSON schema, vector database, graph database, inverted index

## [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](../videos/x4e5O9zN0TE.md)
`x4e5O9zN0TE` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: skills-self-improvement, memory, multi-agent

Long-running, stateful agents need controlled scenario suites, balanced scorecards and a ratchet loop, not just prompt tweaks; the speaker's case study is a game-village multi-agent system tuned by an outer auto-research loop.

- Techniques: Controlled scenario suite with ground truth; Balanced behavioral scorecard with guardrails; Frozen-harness ratchet loop; Structured run-trace logging; Importance-scored memory with a threshold cache; Provenance and confidence tags on memories; Separate episodic memory from current belief
- Tools: Project Paradox (in-house framework), RAG-backed per-agent memory, auto-research loop (Karpathy-inspired)

## [We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect](../videos/oVsEddfhdxc.md)
`oVsEddfhdxc` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: coding-agents, claude-code, models-research

Prime Intellect's Elie Bakouch runs Claude Code and Codex on an optimizer speedrun against human records, finding both beat the records but neither produced a novel optimizer, and that Claude Code idled while Codex kept working.

- Techniques: Speedrun as a verifiable research environment; Constrained variants to force novelty; Goal file plus rules file as the agent's contract; Restart with the latest best state; Behavior logs normalized by active time; Generator, judge and scale-up loop
- Tools: Claude Code, Codex, Slurm, AGENTS.md, goal.md, Verifiers, Prime-RL, Hosted Training, Kimi K2.7, GLM

## [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](../videos/OA-Mc60Rboo.md)
`OA-Mc60Rboo` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: skills-self-improvement, context-engineering, training-finetuning-rl

GEPA's Lakshya Agrawal explains reflective, text-space optimization: LLMs read full rollout traces and rewrite prompts, skills or harness code, with a Pareto pool, beating GRPO on sample efficiency.

- Techniques: Reflective prompt / artifact optimization loop; Pareto candidate pool selection; Actionable side information from the evaluator; Three optimization modes in one API; Optimize the agent file itself; Repo skill learning from trajectories; Judge-then-agent data flywheel
- Tools: GEPA (open-source, includes the optimize_anything API and a skill-learning feature), GRPO (used as the RL baseline), Claude Opus, Claude Sonnet 4.5, GPT-5 mini, GPT-4.1, GPT-4.1 nano, Gemini Flash, mini-SWE-agent, Claude Code, Codex, LLM-as-judge

## [The Loop Is the Product — Roland Gavrilescu, Introspection](../videos/7taOQBfjDyE.md)
`7taOQBfjDyE` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: skills-self-improvement, agent-architecture, product-ux

Introspection's Roland Gavrilescu argues self-improving agent loops should distill a team's taste into versioned recipes of evals, judges and skills, validated in production and measured as value per watt.

- Techniques: Trace pattern clustering to find signals; Agent-drafted judges with human calibration; Recipe diffs as reviewable candidates; Production A/B or bandit promotion; Per-model harness profiles
- Tools: Py.Recipes, Harbor, OpenClaw (originally CloudBot), Claude Code, Codex, Cursor, Cognition

## [The Best Models Still Reason Like Toddlers — Andrew Dai, Elorian](../videos/A_I8mw8yfns.md)
`A_I8mw8yfns` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: voice-multimodal, models-research

Elorium's CEO argues frontier models (Claude, ChatGPT, Gemini) pattern-match instead of reasoning over images and video, and proposes visual chain-of-thought trained on synthetic data as the fix.

- Techniques: Keep visual sub-tasks simple; One-second test for task difficulty; Visual chain of thought; Synthetic data flywheel for a hard modality; Programmatic or simulator validation of outputs
- Tools: Google Lens, SAM3, YOLO, Mask R-CNN, Siemens simulators, ByteDance Seedance (rendered as C-Dance in transcript)

## [Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face](../videos/dKcTBQzR7jI.md)
`dKcTBQzR7jI` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: voice-multimodal, data-engineering, training-finetuning-rl

Merve Noyan (Hugging Face) argues against running VLMs for real-time vision and shows a pipeline where VLMs label and judge data to train small Apache-2.0 detectors such as RF-DETR, plus a toolkit of models exposed as agent tools.

- Techniques: VLM as offline labeler, small detector at runtime; Overlay-and-ask judging; Ensemble of small judges with any-yes merge; License-first model selection; Agent with domain rules and human checkpoints; Models exposed as agent tools
- Tools: RF-DETR, Gemma 4 E4B, LFM2.5-VL, Qwen VLM (auto-caption reads 'Q1 3.5', ~3.5B), Falcon Perception, Moondream 3, MM Grounding DINO, SAM 3.1, Supervision (Roboflow), Hugging Face Jobs, Hugging Face Inference Providers, Hugging Face buckets

## [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](../videos/SQMCtZX3trg.md)
`SQMCtZX3trg` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: skills-self-improvement, coding-agents, context-engineering

Paul Bakaus (Impeccable) on building production agent skills as harness extensions: blind sub-agents, forced divergence, scripts, hooks and per-model builds, rather than prose alone.

- Techniques: Blind adversarial critique; Anti-attractor divergence; Register routing inside one skill; Cross-session skill memory; Scripts that print next-step instructions; Pre-tool-use blocking hooks for weaker models; Hook-driven feedback loop from a skill; Unskippable gates with logged results; Per-harness and per-model builds; Ablation testing of rules; LLM-as-user with a judge panel; Inverted judges
- Tools: Claude Code, Codex, Cursor, GitHub Copilot, Gemini, Playwright, skills.sh, npx skills

## [Teaching LLMs to Speak Spotify — Yves Raimond & Jacqueline Wood, Spotify](../videos/2LRIAfng7eA.md)
`2LRIAfng7eA` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: training-finetuning-rl, product-ux

Spotify's engineers explain turning recommendations into a steerable LLM: semantic-ID tokens, a four-stage NEO training recipe, and LLM judges grounded in behavioral data.

- Techniques: Semantic-ID tokenization and vocabulary extension; Frozen-backbone domain grounding; Staged training: grounding, then multi-task instruction tuning, then optional RL; Beam search over constrained decoding for ID generation; Grounding LLM judges with user profiles and behavioral signals; LLM judges for Cranfield-style relevance pools
- Tools: Qwen, LLaMA, LoRA, NEO (Spotify's training paradigm, linked paper), Discover Weekly, Spotify DJ

## [An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases](../videos/hd7TOvmyAxU.md)
`hd7TOvmyAxU` · AI Engineer · 2026-09-27 · q2 · practitioner · demo · also: observability, agent-architecture, training-finetuning-rl

Live demo of W&B's ARIA research agent running autoresearch experiments, plus its trace-to-eval loop: production traces, LLM judges, nightly YAML task suites, and promotion gated on eval scores.

- Techniques: Eval suite as YAML unit tests; Production traces to tasks loop; Live LLM judges as signal detectors; Eval-gated promotion; Async job dispatch from an agent; Agent analyzes its own traces
- Tools: Weights & Biases Weave, W&B Launch, W&B Inference, W&B Artifacts, W&B Reports, CoreWeave sandbox, Kubernetes, iOS app

## [Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics](../videos/Sjfz1TqxzEs.md)
`Sjfz1TqxzEs` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: training-finetuning-rl, voice-multimodal

Dyna Robotics co-founder on making generalist robot manipulation policies reliable enough for commercial use, via reward-model progress scoring and a targeted active-learning loop.

- Techniques: Reward model as progress scorer for background supervision; Failure-driven active learning loop; Pre-train, post-train, then active learn; Grade-based success criteria tied to customer acceptance; Two-level architecture

## [How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases](../videos/XyV6bSMyq-I.md)
`XyV6bSMyq-I` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: skills-self-improvement, observability, agent-architecture

Weights & Biases walks through how its ARIA agent evaluates and improves itself: production traces become offline regression tasks, and the agent runs its own hill-climbing loop.

- Techniques: Eval flywheel from production traces; Byte-identical prod and research agent with a sync job; YAML-defined config variants; Three task simulation modes; Dual scoring: pass/fail plus pairwise relative scoring; Unconstrained sandbox for agent research loops
- Tools: Weights & Biases Weave, W&B Reports, ARIA agent, Claude Code, YAML task and config specs

## [From Ingestion to Agents: How AI Teams Build on Document Intelligence — Adit Abraham, Reducto](../videos/0I07YAuF8xA.md)
`0I07YAuF8xA` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: data-engineering, rag-retrieval, agent-architecture

Reducto's CEO on why document ingestion decides agent quality: decompose parsing into specialised tools, verify rather than regenerate, store table forms split by job, and eval every pipeline stage.

- Techniques: Decomposed parsing stack; Targeted verification instead of regeneration; Dual table representation; Classify and split before extraction; Agent harness for chart reconstruction; Parent-subagent validation criteria; Per-stage evals
- Tools: Reducto, Gemini, OpenAI models, Anthropic models, Cursor (as analogy for speculative edits), code interpreter

## [Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google](../videos/l1-D89bAuOA.md)
`l1-D89bAuOA` · AI Engineer · 2026-09-20 · q3 · practitioner · talk · also: inference-serving, observability

Google engineers argue that LLM serving benchmarks often blame the server when the benchmark client is at fault, and show Inference Perf, a multi-process, reproducible load generator built for production-scale inference.

- Techniques: Scheduled multi-process load generation; Client-side health check on every run; Declarative benchmark configs with distributions; Sweep the load to find saturation; Match sampling and dataset preprocessing to production; Shared workload definitions
- Tools: Inference Perf, llm-d, Prism, vLLM, SGLang, Kubernetes, k6, Locust, MLPerf, ShareGPT

## [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](../videos/O84lhGc1OOI.md)
`O84lhGc1OOI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: rag-retrieval, multi-agent, context-engineering

Benjamin Clavié (Mixedbread) argues agents should be designed as knowledge workers, not coding agents, and uses BrowseComp-Plus and MatQA results to show that tooling and search orchestration drive accuracy.

- Techniques: Manager-plus-searcher subagents for open-ended retrieval; Optimize the lexical baseline before comparing; Hybrid search harness; Multimodal PDF search instead of OCR text; Teach the agent its retrieval primitives
- Tools: BM25, Gemini, Claude Code, Codex, Mixedbread search tool

## [Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic](../videos/PXj0p_mW9nI.md)
`PXj0p_mW9nI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: token-cost-efficiency, multi-agent, agent-architecture

Anthropic's Katelyn Lesse and Angela Jiang argue agent token budgets are not fungible: giving some tokens jobs (advisor, grader, dreamer) beats simply spending more on one executor, measured at a fixed budget and scored on pass rate.

- Techniques: Role-split executor with advisor; Rubric grader with retry loop; Dreamer writing memory from transcripts; Fixed-budget strategy comparison; Cost per pass metric
- Tools: Claude Managed Agents

## [Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../videos/EL123UNokkI.md)
`EL123UNokkI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: pr-code-review, multi-agent, observability

Uber's engineers explain uReview, their multi-agent code review system: how they built feedback-driven evals, team-owned customizations, and a cost/quality loop, plus why they think humans move up to an expanded outer loop.

- Techniques: Reply-sentiment and addressal-rate tracking; Trajectory-based runtime tuning with turn guardrails; Tiered review generators with post-processing; Few-shot AI linters with deterministic context; Ownership-coupled rule distribution
- Tools: GitHub, Fabricator, Claude

## [SOTA Generative Media Panel — Dumitru Erhan, Shane Gu & Nicole Brichtova, Google DeepMind](../videos/KLDdXOw6jIc.md)
`KLDdXOw6jIc` · AI Engineer · 2026-09-18 · q3 · practitioner · panel · also: models-research, voice-multimodal

Google DeepMind panel on generative media (Veo, Gemini Omni, Nano Banana): why language is a lossy conditioning channel, why human preference evals mislead, and why real-task data and FDE feedback matter.

- Techniques: Side-by-side human preference eval for close model comparisons; Deterministic checks for rendered text; Early-access programs before broad release; Amortizing human labels into a learned evaluator; Joint generation of coupled modalities in one model
- Tools: Veo 3, Gemini Omni, Nano Banana, Nano Banana Pro, Nano Banana 2 Lite, Manim, FFmpeg, Stable Diffusion, OCR

## [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../videos/YXEqC05WEI0.md)
`YXEqC05WEI0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: security-guardrails, governance-compliance, observability

Hinge Health's AI lead on shipping member-facing health AI: put irreversible decisions in code above the model, strip PHI at ingestion, monitor live traffic, and verify the judge before fixing the agent.

- Techniques: Code-layer routing above the model; PHI stripping at ingestion with environment and region separation; Layered live scoring of production traffic; Judge-first triage before agent changes; Severity triage for launch decisions

## [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../videos/G7cgLjZtmMU.md)
`G7cgLjZtmMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, product-ux, security-guardrails

Best Buy's Ahnaf Priyo maps the agentic commerce protocol stack (MCP, A2A, ACP, UCP, AP2), argues for pushed product feeds and checkout APIs over browser agents, and makes the case for behavior and protocol evals with a live cat-bakery demo.

- Techniques: Push product feed to platforms; Checkout as an explicit state machine; Scoped, single-use, revocable payment mandate; Layered evals for conversational commerce agents; Timeline view of agent calls; Agent skills for domain roles
- Tools: MCP, A2A, ACP, UCP, AP2, Cerebras, ChatGPT, Gemini, Chrome DevTools

## [AI is the World’s largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](../videos/yoONZwV2smc.md)
`yoONZwV2smc` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: security-guardrails, product-ux

Clay Cockrell and Tony Fabrikant of CoupleWork AI argue that relationship AI often acts as a sycophantic validation machine, and describe their clinician-led design of Maxine: risk screening, protocol escalation, privacy, and clinician-written evals.

- Techniques: Clinician-first TDD evals; Background risk screen with protocol handoff; Reflect patterns instead of validating; Dogfood the agent for tone drift; Treat sensitive chat data as privileged
- Tools: Gottman Method, Emotionally focused therapy (EFT), Maxine (CoupleWork AI coach)

## [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../videos/B0fjR3yaZFU.md)
`B0fjR3yaZFU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, product-ux, agent-architecture

Long Lake co-founder on why AI adoption in real services businesses lags: climb an autonomy ladder, turn real work traces into evals, and co-design with users on-site.

- Techniques: Autonomy ladder rollout; Sandboxed async coding agent with PR output; Traces to ground-truth evals; Diff-based implicit feedback; Post-training on enterprise data; Layered customization; Co-design embedded in existing tools
- Tools: Claude Code, Codex, Claude Cowork, MCP

## [Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots — Amit Desai, Roku](../videos/Zd5b40Jbp_k.md)
`Zd5b40Jbp_k` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, product-ux

Voice assistant satisfaction can rise without better accuracy: gate act/confirm/stop on calibrated confidence and pick thresholds by minimizing a user-cost function ("ouch").

- Techniques: Outcome user-cost minimization for act/confirm/stop; Two-threshold three-band policy with grid search; Sensitivity check on unit costs
- Tools: Interactive threshold-sweep graph built with a coding assistant (no specific library named)

## [Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End](../videos/4loPnxvWWhg.md)
`4loPnxvWWhg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: training-finetuning-rl, context-engineering, enterprise-adoption

A LeaseEnd data scientist explains how fine-tuning an intent classifier for customer texts became costly tech debt, and how replacing it with editable skills and prompts on a frontier model cut fix time from a week to under an hour.

- Techniques: Skill and prompt edits as the default fix; Curated production regression set as the gate; Markdown-file deploys to object storage; Triage gate before retraining; Fine-tuning pre-check list; LLM-judge labeling with manual review and holdout sets
- Tools: Claude Code, Amazon S3, OpenAI, Anthropic

## [Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley](../videos/hOWU0KPUp1k.md)
`hOWU0KPUp1k` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: governance-compliance, multi-agent, context-engineering

Brendan Rappazzo presents Loophole, an open-source game where two adversarial agents hunt contradictions in a legal code codified from the user's morals, then extends it to chatbot prompts, contracts, and simulated Senate votes.

- Techniques: Adversarial loophole and overreach search; Judge with auto-patch first, human escalation second; Formalize natural-language values into numbered legal text first; Persona-conditioned rule generation for simulation; Hill-climbing text against an adversarial judge
- Tools: Claude, GitHub

## [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](../videos/WJRdLNhrsLQ.md)
`WJRdLNhrsLQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, pr-code-review

Maven Clinic's CTO-level account of becoming an "AI-native" health company: AI in internal work and product, shorter planning cycles, changed code review, and tiered reliability bars with rubric-based evals.

- Techniques: Staged AI-coding adoption from low-risk tasks; Self-declared review tiers with accountability; Repeated-run pass-rate gating for non-deterministic tests; Rubric scoring plus human spot-checks on live conversations; Per-feature failure tolerance with multi-model agreement and human fallback
- Tools: Cursor, Claude Code, Jira

## [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../videos/pOvWgX7IJsc.md)
`pOvWgX7IJsc` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: inference-serving, models-research

Simran Arora (Together AI) on why multi-GPU communication is now the kernel bottleneck, the transfer and overlap trade-offs behind her Parallel Kittens primitives, and a benchmark showing frontier models still struggle to write fast multi-GPU kernels.

- Techniques: Copy-engine vs device-initiated transfer choice; Intra-SM vs inter-SM communication overlap; Thin primitive layer over a single-GPU kernel; Benchmark built from a parallelism taxonomy plus real-workload problems; Report correctness (pass@k) and speed-gated correctness (fast_1@k) separately; Agent harness: multi-turn bash agent for kernel tasks
- Tools: CUDA, PyTorch, torch.distributed, NCCL, RCCL, Triton, Triton Distributed, TileLink, ThunderKittens, Parallel Kittens, Parallel Kernel Bench, mini-SWE-agent

## ["My name is... my name is...": A Linguistic Map for Voice Agents — Midam Kim, ServiceNow](../videos/IDNfAZVKvPE.md)
`IDNfAZVKvPE` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: voice-multimodal, product-ux

Midam Kim (ServiceNow) uses a linguistics framework to explain why voice agents fail and proposes diagnosing them by listen/speak channels, timing, and the user's mental model.

- Techniques: Linguistic diagnostic grid for voice agents; Interactive clarification on recognition errors; Locale-aware pre-processing for TTS and vocabulary; Turn-taking and barge-in control; Dynamic per-call context retention; EvaBench for diagnosing voice agents
- Tools: EvaBench

## [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../videos/mMNkdYnIVC4.md)
`mMNkdYnIVC4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: agent-architecture, multi-agent, training-finetuning-rl

James Zou (Together AI, Stanford) argues agents should be given designed environments with verifiers, incentives and shared infrastructure instead of fixed workflows, citing Einstein Arena results and the DSGym data-science benchmark.

- Techniques: Verifier-first problem curation; Agent-native onboarding; Persona-differentiated agents; Shortcut audit before trusting a benchmark; Execution-verified trajectory generation
- Tools: Docker

## [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](../videos/UyyOoJmuATU.md)
`UyyOoJmuATU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, governance-compliance, enterprise-adoption

Vasant Kearney (Onlay) argues healthcare agents should run on X12 insurance transactions as a public, strict contract that guardrails can reject, with tiered memory and skeptical use of models.

- Techniques: Standard-format tool contract; Strict guardrail rejection per step; Separated, tiered memory; Full-system regression evals before model swaps; Hybrid hard-coded and agentic execution; Write-action audit logging
- Tools: X12, FHIR, EHR, Claude Code, Codex, OpenClaw, Hermes Agent

## [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](../videos/Yphdry8ttAQ.md)
`Yphdry8ttAQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, data-engineering, enterprise-adoption

A seven-step recipe for building vertical AI (finance, pharma) where domain experts in a learning loop, not LLM-as-judge, drive quality and proprietary data is the moat.

- Techniques: Narrow task decomposition; LLM workflow for unstructured-to-structured data curation; Observability traces as the first improvement loop; Domain expert as user in a learning loop; Post-training ladder; AI-in-the-loop reduction of expert time

## [Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe](../videos/jebp4V0vh30.md)
`jebp4V0vh30` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: inference-serving, rag-retrieval, product-ux

Adobe's Carlos Sanchez demos "agentic sites" that personalize page blocks in real time from browsing intent, grounded on the existing site, with provider choice driven by latency and accuracy evals.

- Techniques: Multi-provider eval matrix for accuracy and latency; Grounded block-level generation; Signal bucketing into personas or intents; Pre-generate and prefetch; Fast inference provider for the hot path
- Tools: Adobe Experience Manager, Edge Delivery Services, Cerebras, Gemma 4, Promptfoo, AWS Bedrock, Cloudflare, Google Cloud

## [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../videos/yqF6XhzbWBk.md)
`yqF6XhzbWBk` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: context-engineering, enterprise-adoption

Sebastian Fox (Composo) on why LLM judges miss serious clinical-note errors: "which error matters" is tacit and shifting, so keep it as retrieved, case-specific expert judgments and run a discover-capture-calibrate loop.

- Techniques: Failure-mode discovery from production outputs; Free-text expert comments as the raw eval data; Retrieval of similar judged cases into the judge context; Generate-then-check with a narrower checker; Severity vs. detectability map of errors
- Tools: ambient AI scribes (product category discussed), LLM-as-judge with rubric, RLHF (conceptual reference)

## [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](../videos/XzJD1bvXKjs.md)
`XzJD1bvXKjs` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: context-engineering, skills-self-improvement, models-research

Laurie Voss re-runs the 200-instruction IFScale benchmark on 2026 frontier models and finds the ceiling moved about 10x, to roughly 2,000 to 5,000 rules, but reliability and verification remain open problems.

- Techniques: Instruction density probe; Model-specific failure profiling; Pre-screening test vocabulary for safety filters; Per-output eval of long rule sets; Robustness check by rewording and reordering
- Tools: IFScale benchmark, Arize AI (speaker's employer; no product detail given), Chroma context rot study, Firebench, CCRbench, Guidebench (names as captioned; may be misspelled)

## [Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk](../videos/dQ-_i1tZiws.md)
`dQ-_i1tZiws` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, agent-architecture, security-guardrails

Maersk's Dmitry Buykin on running 200+ production shipping agents by turning expert SOPs into executable agent procedures, with a feedback loop that turns each correction into a harness change.

- Techniques: SOP-to-agent conversion; Three-part agent harness; Failure-to-fix mapping; Replay with writes disabled; Trace clustering into heat maps; Composite tools from repeated success; Function-calling tools instead of MCP
- Tools: SME bench (internal triage tool that clusters failures), Function calling

## [Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan](../videos/32nrHU6zHU8.md)
`32nrHU6zHU8` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: agent-architecture, observability, context-engineering

Navan's chief architect and a colleague argue agent infrastructure is repeating the microservices shift: skills as context units, hook-based tracing, trajectory evals, and tool-call guardrails.

- Techniques: Pre/post tool-call and session hooks for tracing and gating; Trace signals: goal, reasons, belief, tool calls, confidence; Trajectory evaluation; Skills as composable, testable context units; Single master agent with progressively loaded sub-skills; Per-tool-call authorization for on-behalf-of agents; A2A skill contracts across team boundaries
- Tools: AWS AgentCore, OpenTelemetry, Claude Code hooks, MCP, A2A protocol, Braintrust (inferred from auto-caption 'brain trusts')

## [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../videos/u6q-byPWUuo.md)
`u6q-byPWUuo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: inference-serving, training-finetuning-rl, enterprise-adoption

Abridge's engineering lead on running clinical AI at scale: clinician-written rubrics feed LLM judges, staged rollouts, and small post-trained models gated by cheap triggers to balance quality, latency and cost.

- Techniques: Multi-reviewer rubric construction for LLM judges; Staged rollout with online feedback for AI features; Task decomposition into small specialised models; Gate cascade for real-time event triggers

## [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../videos/Lrw0jqBNaw0.md)
`Lrw0jqBNaw0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, mcp-and-tools, observability

Sourcegraph's agent advocate argues DevRel must now serve AI agents as users and recommenders, and shows how to measure agent friction and recommendation rates.

- Techniques: Agent friction logging from traces; With-and-without-tool agent benchmark; Intent-split GEO prompt experiments; Agent experience report; Machine-readable authoritative content
- Tools: Sourcegraph code navigation MCP tool, CodeScaleBench (speaker's benchmark), llm.txt, MCP registries, Discord

## [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](../videos/bdHaOXZOhcM.md)
`bdHaOXZOhcM` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: software-factory, enterprise-adoption, coding-agents

A CTO explains how a manager with a full calendar keeps building by running coding agents overnight (context gathering at 5pm, morning review), using evals and custom-model training as examples.

- Techniques: Overnight agent loop; Context-harvesting prompt; Test-first with end-to-end computer-use verification; Feedback-to-eval hill-climb; Overnight custom-model training with sandboxed cloud access; Prototype branch behind feature flags; Small PRs with an AI reviewer in a clean sub-agent
- Tools: Claude Code, Codex, Cursor, Dia, Wispr Flow, Slack, Jira, Confluence, Notion, SQLite, AWS EC2, ModernBERT

## [5 Voice Agent Failure Modes You'll Hit in Week One — Venky B, Plivo](../videos/vblnYHzBgS4.md)
`vblnYHzBgS4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, inference-serving, data-engineering

Venky B of Plivo lists five voice-agent failure modes seen in production (latency, transcription, data collection, TTS output, barge-in) and the fixes his team uses. Main takeaway: treat voice as a structured pipeline problem, not a prompt problem.

- Techniques: Per-stage latency budget with time-to-first-audio as the metric; Self-hosted small or MoE open model for the conversational LLM; Dynamic keyword boosting per call phase; LLM post-processing of STT output with domain context; Typed field schema with validation and confirmation for data collection; Field-level unit-test evals for voice agents; Normalization layer between LLM and TTS; Pronunciation smoke tests with known hard names
- Tools: LiveKit, Pipecat, Pydantic, Zod, Qwen 3.5, Gemma 4, Cerebras, Groq

## [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../videos/ZIYYsAzaLlA.md)
`ZIYYsAzaLlA` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, context-engineering

Figma's engineer on building its first MCP server in about three months: which context format worked, how evals were automated, and how a remote server followed a local one.

- Techniques: Pick the representation the model knows best; Code plus screenshot as paired context; Reference-by-pointer via a component mapping; Two-step ask-then-act to emulate elicitation and sampling; Automated eval mixing deterministic checks and LLM judges; Local-first MCP server with an IPC bridge; Per-tool-call instructions when clients ignore server instructions
- Tools: Figma MCP server, Figma Code Connect, MCP Inspector, React, Tailwind CSS, Electron, Node.js, Cursor, VS Code, Claude Desktop

## [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../videos/DrTdD-ttjCY.md)
`DrTdD-ttjCY` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, product-ux, observability

Snowflake's sales-team GTM agent (6,000 users): launch with quality over coverage, stage the rollout, manage activation, and use question logs as the feedback loop.

- Techniques: Question bank as the first eval set; Narrow-scope, high-accuracy launch; Pilot, beta, GA with metric gates; LLM classification of usage logs; Closed loop from logs to content; Agent instructions under version control with tests; Build on a managed agent platform with inherited access control
- Tools: Snowflake Cowork (formerly Snowflake Intelligence), Cortex Analyst, Cortex Search, Snowflake semantic views, MCP connections, Confluence, Jira, Slack, Gmail, Salesforce, Google Docs

## [Multimodal Collaborative Agents for Next-Gen Commerce — Nidhi Kaushik Vyas, Google DeepMind](../videos/AhQpRalYlyg.md)
`AhQpRalYlyg` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, context-engineering

Google DeepMind product lead on shopping agents for fuzzy intent: build a working state, ask the highest-value clarifying question, elicit preferences visually, adapt the answer format, and grade every step with autoraters.

- Techniques: Working state with confidence and live refresh; Counterfactual sensitivity test for constraint extraction; Information-gain question selection; Elicitation-channel choice by preference type; Per-step autoraters with user simulator; Response format chosen by query intent
- Tools: MCP (expected interface between agents and merchants), UCP (merchant common-language protocol, named in the talk without detail)

## [The Half Life of Agent Infrastructure — Ben Kus, Box](../videos/sM1iYgz93HI.md)
`sM1iYgz93HI` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: agent-architecture, enterprise-adoption, rag-retrieval

Box CTO Ben Kus argues AI agent infrastructure has a half-life of months, not years, so teams should build abstractions, gate changes on eval sets, and get good at changing.

- Techniques: Abstraction layer over agent internals; Eval-gated switching; Scheduled stack review; Adaptive model selection; Hybrid lexical plus semantic retrieval with rank fusion; Agentic search
- Tools: Claude, Opus, OpenAI and Anthropic frontier models, open-weight models, BM25, embeddings and approximate nearest neighbor search, MySQL

## [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](../videos/AN65uc645mE.md)
`AN65uc645mE` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, inference-serving, multi-agent

Hippocratic AI's engineering lead explains how their clinical voice agent (200M+ patient conversations) hits safety, latency and accuracy at once: a vertically built stack, 31 parallel specialist models, context-fed ASR, and lossless inference tricks.

- Techniques: Parallel specialist models with self-gating; Context-conditioned ASR; Second-pass rescoring for ambiguous short utterances; Async and offline verifiers for tool calls; Human plus synthetic eval mix with sample-size planning; Severity-graded harm rubric; Lossless inference stack
- Tools: Whisper (large-turbo, fine-tuned), speculative decoding, 4-bit quantization, KV cache

## [Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs](../videos/r9OwPx_HoV0.md)
`r9OwPx_HoV0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: rag-retrieval

AI21's Yuval Belfer argues chunking still matters: no single chunk size wins per query, so index the corpus at several sizes, retrieve whole documents, and fuse the rankings with RRF for 20-40% gains.

- Techniques: Multiscale indexing; Parent-document lifting before fusion; Reciprocal Rank Fusion (RRF); Oracle best-per-query benchmark
- Tools: RRF (Reciprocal Rank Fusion), QMSum, NarrativeQA, FinanceBench, Seinfeld trivia dataset (in-house, speaker says it is published)

## [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](../videos/McknwOzbmyg.md)
`McknwOzbmyg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: testing-verification, voice-multimodal, product-ux

Jared Joselowitz (Ufonia) on shipping a clinical voice agent to patients without A/B tests or rollback, using simulated patients, a calibrated LLM judge, and prompt optimization gated by hazard-linked evidence.

- Techniques: Hazard-first safety case; Scenario-conditioned simulated user; Calibrated LLM judge; Reflective prompt optimization (GEPA) with a cost-weighted metric; Synthetic edge-case generation; Staged gated rollout with evidence-based autonomy; Pin prompt versions and keep full traces
- Tools: Matrix (internal simulation framework), PatBot (internal LLM patient), BevJudge (internal LLM judge), GEPA (genetic-Pareto prompt optimizer), DSPy (mentioned as the origin of GEPA), Gemini 2.5 Pro (judge model at the time of the paper)

## [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../videos/bMjlRrWjdT0.md)
`bMjlRrWjdT0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, product-ux, observability

DoorDash GenAI platform team on building a cross-functional AI evals platform: UI-first, then API-first, then workflow-first, so non-engineers can run annotation and judge calibration themselves.

- Techniques: Continuous eval loop; API-first eval platform with vibe-coded UIs; Self-serve judge calibration with prompt optimization; Platform-level model choice for judges
- Tools: Claude Code, Codex, DSPy-style prompt optimizer (transcribed as JEPA), MCP, LLM gateway, agent gateway

## [Mousepower: agents that can’t be measured, can’t be managed. — Maximillian Piras, Yutori](../videos/8KkibGU_DDY.md)
`8KkibGU_DDY` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: governance-compliance, token-cost-efficiency, product-ux

Maximillian Piras (Yutori) argues agents have a measurement problem: token spend must trace to verifiable outcomes, and tasks should be triaged by step and acceptance-criteria uncertainty before building an agent.

- Techniques: Two-axis task triage; Verifier agent alongside worker agent; Background parallel agents for peripheral work; Outcome-tied token accounting
- Tools: Claude

## [1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI](../videos/qStB9GbppMU.md)
`qStB9GbppMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: voice-multimodal, observability, security-guardrails

Hamming AI's CEO argues voice agent errors (about 10% in practice) are the top deployment blocker, and offers a loop to find, prioritise, test and red-team failures across many calls.

- Techniques: Frequency and severity triage matrix; Scenario-variation regression testing; Production A/B testing for voice fixes; Cross-conversation pattern analysis; Continuous adversarial red-teaming

## [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../videos/FvxY8oPoI8o.md)
`FvxY8oPoI8o` · AI Engineer · 2026-09-18 · q2 · practitioner · demo · also: token-cost-efficiency, infra-cost-scaling, coding-agents

DigitalOcean's Archana Kamath and Tyler Gillam argue for per-request model routing chosen by task, cost, latency and rules, validated with your own evals. A live OpenCode demo shows roughly 3x lower session cost at similar quality, though the evidence is one vendor demo.

- Techniques: Per-task model pools with ordered failover; Natural-language routing preferences plus hard rules; Side-by-side routed vs single-model agent runs with live cost tracking; Eval-gated routing with feedback loop
- Tools: Plano (open-source proxy and routing model), OpenCode, Claude Opus, Claude Sonnet 5, GLM 5.2, GPT 5.2, Llama 4 Maverick (caption reads 'long before Maverick')

## [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard](../videos/mav15aW9lLM.md)
`mav15aW9lLM` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: governance-compliance, enterprise-adoption, security-guardrails

Christopher Lovejoy (Anthropic) and Saul Howard (Anterior) argue that enterprise AI agents need audit, data-boundary, escalation and eval primitives designed in from the start, not bolted onto a proof of concept.

- Techniques: Immutable append-only event log as system of record; Event log plus schema-driven immutable blob store; Token-based access at point of use; Human-agent equivalency in the action model; Replay plus human-vs-agent diff as eval; Run evals inside the customer environment

## [The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev](../videos/fZH97QHHYjY.md)
`fZH97QHHYjY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: rag-retrieval, context-engineering

Jo Kristian Bergum argues BM25 is back for agentic search: LLM agents write long, precise queries that suit lexical matching, and the baseline was undertuned. Retrieval results can be exposed as a filesystem workspace for grep-style use.

- Techniques: Workspace-as-filesystem retrieval; Tuned BM25 baseline before any embedding comparison; Hybrid lexical plus grep for agent search; End-to-end task evaluation for search agents; Evidence-stuffing ablation
- Tools: BM25, grep, ripgrep, sed, BrowseComp-Plus, Hornet (vendor BM25 engine)

## [Don’t be data poor — Anuj Iravane, Anterior](../videos/XAsb7MIAzm8.md)
`XAsb7MIAzm8` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: data-engineering, skills-self-improvement

Anuj Iravane (Anterior) explains how to generate synthetic medical records when real PHI cannot be kept, by sampling labels and policy reasoning traces first and generating documents backward.

- Techniques: Reverse-generation from sampled labels; Coarse-to-fine layered generation; Round-trip label verification; Cross-document consistency eval in a refinement loop; Skill files as the domain-expert interface
- Tools: internal agent harness (unnamed)

## [Training Taste — Thais Castello Branco, Taste Labs](../videos/sDMGWK4wZ_w.md)
`sDMGWK4wZ_w` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: product-ux, vibe-coding-app-building, context-engineering

Thais Castello Branco (Taste Labs) on measuring and fighting "AI slop" in design: decompose subjective quality into checkable parts, build feature classifiers that flag slop, and turn a brand into structured context the agent both follows and is graded against.

- Techniques: Decompose subjective quality into probes; Split objective checks from aesthetic judgment; Rule-aware intentional divergence; Brand spec as both generation context and rubric; Retrieve pre-built brand systems
- Tools: Claude Design, Wayback Machine-style web crawl

## [Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust](../videos/nxokqOq1imY.md)
`nxokqOq1imY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: observability, agent-architecture

Braintrust field CTO argues each agent architecture generation (single call, chain, ReAct loop, graph, product system) needs different evals, and that production traces should keep feeding the eval set.

- Techniques: Architecture-matched eval suites; k-run pass@k and pass^k reporting; Production failure clustering to harvest evals; Node-level and branch-level evals for graph workflows
- Tools: Braintrust, Braintrust Topics

## [I Tested Every Qwen3.8-27B Quant: Here’s the Best One For Your GPU](../videos/hg26j0erUSo.md)
`hg26j0erUSo` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, inference-serving

Kai's practitioner guide to choosing a quant of Qwen3.8-27B for consumer GPUs: architecture-aware quants, why a Q4 KV cache silently degrades outputs, and VRAM-based file picks.

- Techniques: Diff quantized output against the full-precision model before trusting a quant or cache setting; Keep the KV cache at Q8 or full precision; Choose the quant by VRAM budget; Pin the model revision on download; Lower reasoning effort for simple tasks; Enable the built-in MTP draft head for speculative decoding; Make sure the front end renders the chat template correctly; Load the vision projector as a separate file
- Tools: Qwen3.8-27B, Unsloth UD-Q4_K_XL / Q6 / Q8 quants, Bartowski IQ4_XS quant, Ridge quant (name as transcribed; may be a caption error), Atomic Chat KL-divergence benchmark, Quesma benchmark run, GPQA Diamond, IFBench, TerminalBench, Jinja chat-template flag, spec type draft MTP (speculative decoding flag as spoken), RTX 3090

## [You Don't Need Frontier Models Anymore (Qwen 3.8 27B + DeepSeek Harness)](../videos/3DVRznjCIS8.md)
`3DVRznjCIS8` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: local-ai, agent-architecture, context-engineering

Same local Qwen model, same weights and prompt: the outcome changed with the harness around it (feedback loop, tools, session log, context), so the software matters as much as the model.

- Techniques: Attribute failures to the harness before blaming the model; Close the feedback loop so the agent can verify its own output; Persistent session log as source of truth for long runs; Sweep reasoning effort on a fixed prompt rather than assuming max is best; Size the local model by capacity and bandwidth, then pick quantization; Hybrid local-then-frontier handoff
- Tools: Qwen 3.8 27B (transcript: 'Quen 3.8'), Qwen 3.6, Qwen 3.7 Plus, DeepSeek Harness (transcript: 'DeepSeq Harness'; MIT licensed, plugin components, developer preview), DeepSeek v4 (2-bit quant, transcript: 'DeepSeq v4'), Claude Code (Qwen's benchmark harness for four agentic evals), Opus API (cost comparison), VS Code Copilot (failed reproduction run), Unsloth Q6 build of Qwen 3.8, Simon Willison's test prompt (reasoning-effort test), DeepSWE 1.1 (benchmark), OSWorld (computer-use benchmark)

## [Ox Alpha is Lying to You!](../videos/kFajz5bNO6M.md)
`kFajz5bNO6M` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: models-research, security-guardrails, governance-compliance

Kai investigates "Stealth Ox Alpha", a free OpenRouter model with no stated developer, using tokenizer offsets, error strings and a leaked system prompt; he concludes the evidence points to GLM but is unproven.

- Techniques: Tokenizer offset fingerprinting; Error-string matching; Temperature-zero output comparison; Controlled video token test; Report benchmark counts with intervals; Cost and time comparison on a fixed build task; Check retention claims at both the aggregator and the provider
- Tools: OpenRouter, OpenCode, GLM 5.3 (Zhipu), GLM-5, Gemini 2.5 Pro, GPT-4o, Claude Fable, Claude Code, Hermes Agent, DeepSeek Harness, Grok, DeepSeek

## [I Tested Meta Muse Glimmer 30B For 48 Hours: Here’s What Happened](../videos/v-xnHMwLgAw.md)
`v-xnHMwLgAw` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: local-ai, models-research

Kai Explains puts Meta's unannounced Muse Glimmer 30B through 48 hours of agent work on dual RTX 3090s: fast at 50-60 tok/s, but it fails instruction following, context depth and synthesis.

- Techniques: Constant-harness model A/B test; Three-question model vetting probe; Compaction threshold relative to window size; Local llama.cpp serving recipe (as described, not as flags); Long-command detachment rule
- Tools: Meta Muse Glimmer 30B, Unsloth Q8_0 GGUF, llama.cpp, DFlash drafter (speculative decoding), DeepSeek V4 Flash, Qwen 3.6 27B, Qwen 3.5 35B MoE, tmux, ComfyUI

## [Deepseek Harness: Not What You Think](../videos/y0BW4hpMpyM.md)
`y0BW4hpMpyM` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: agent-architecture, token-cost-efficiency, security-guardrails

Kai Explains on DeepSeek's open harness: benchmark scores are model-plus-harness pairs, the harness can move scores 5-8 points, and its append-only, cache-stable context design is the most reusable idea, alongside licensing and security concerns.

- Techniques: Report scores as model-plus-harness pairs; Append-only event log with a rebuilt, frozen message history; Cache-stable summarization and compaction; Track cache-hit rate per agent session
- Tools: DeepSeek Harness (DeepSeek's open-source agent harness, version 0.1, MIT license per the host), DeepSeek V4 Pro (pricing mentioned), Terminal Bench (public leaderboard at TBench AI, Terminus 2 research harness), Gemini 3 Pro, Gemini 3.1 Pro, Gemini CLI, Claude Code, Claude Agent SDK (pinned at 0.3 per the host), Claude Code 2.1 (bundled in the sub-agent payload), Opus 5 (as captioned), Fable 5 (as captioned), Codex CLI

## [I Tried Both New 30B Models... One Of Them Is a DISASTER! (Muse Glimmer & Lightning 3.5)](../videos/mzQC9UK9n84.md)
`mzQC9UK9n84` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: local-ai, mcp-and-tools, models-research

Hands-on test of Meta's Muse Glimmer and NVIDIA's Nemotron Lightning 3.5 (both ~30B, local via Ollama) on three agentic tasks; Glimmer passes two of three, Lightning fails all three.

- Techniques: Same-prompt, multi-round correction test; Serve two local models and drive them from an agent CLI; Expose a desktop editor to models through a custom UXP plugin; Check numbers against the source document; Treat tool-error fallback as a test case
- Tools: Muse Glimmer (Meta), Muse Spark (Meta), Nemotron Lightning 3.5 (NVIDIA), NeMo Switchyard (NVIDIA routing), D-Flash speculative decoding, Ollama, OpenCode, Opus 5 (reference model), Adobe Premiere Pro, Adobe Bridge, UXP plugin (custom), Epidemic Sound MCP server

## [OpenAI's GPT 6 Astra Is Near "AGI" Level?](../videos/WEwZfkUzBxY.md)
`WEwZfkUzBxY` · Kai Explains · 2026-09-02 · q3 · intro · news · also: models-research

Kai Explains weighs OpenAI's claim that its unreleased Astra model solved 10 open math problems, what Lean verification does and doesn't prove, and why this is not yet evidence of AGI.

- Techniques: Check formal proofs for sorry placeholders and compile them; Audit the formal statement against the original problem; Corroborate with an independent model under constraints; Report total cost including failed attempts; Separate solving-defined-problems from choosing-problems in evaluation
- Tools: Lean 4 (formal proof checker, with public GitHub repo of proofs), Astra (OpenAI internal model, unreleased, per the video), GPT-5 (cited for the October 2025 Erdős claim), Fable (named in the video as Anthropic's publicly available model; the name may be a caption error for Claude, which the host did not confirm), Riemann Bench (25 newly written research-level math problems), Erdős Problems database

## [This Is How Forward Deployed Engineering Is Actually Done](../videos/AD-EmZ3v6-g.md)
`AD-EmZ3v6-g` · AI LABS · 2026-09-02 · q2 · intro · tutorial · also: enterprise-adoption, product-ux, mcp-and-tools

How to do forward deployed engineering: audit a business process before building, sort each step into software, model or human, then eval against real cases. Useful method, but includes a sponsored segment and unsourced stats.

- Techniques: Shadow-and-document the process; Three-filter triage per step; Connect to existing systems instead of migrating; Keep process steps visible with checkpoints; Labelled-case eval loop; Value-and-error-cost accounting; Process audit as the first deliverable
- Tools: Claude Code (used for the internal chatbot case study), MCP (Model Context Protocol), Notion (named as the example system for MCP connection), Slack, Cursor (as a company example), OpenAI (as a company example), Anthropic (as a company example), Dex (job-matching sponsor; named in a sponsored segment)

## [Qwen 3.6 vs Nemotron 3.5 vs Muse Glimmer: The Real Test](../videos/GweZqgLxcCo.md)
`GweZqgLxcCo` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: local-ai, inference-serving

Practitioner head-to-head of Qwen 3.6, Nemotron 3.5 Lightning and Meta's Muse Glimmer on the host's own daily-digest workload: trick questions saturate, premise and pushback tests separate models, Nemotron wins long context, Qwen stays daily driver.

- Techniques: Premise-override trap; Sustained-pushback (spine) test; Needle-in-log long-context test; Benchmark hygiene checks; Agentic task with traps and side-effect checks; Measure total wall time, not per-step latency, for tool loops; Route models by workload
- Tools: Qwen 3.6 (27B), Nemotron 3.5 Lightning (NVIDIA; hybrid Mamba MoE, 32.9B parameters, 1M-token context), Muse Glimmer (Meta; 27.9B parameters, about 18 GB on disk), Q4 quantization, GPU inference (runtime not named), Host's custom benchmark harness (synthetic log, executable tool tasks, trick-question set)

## [Anthropic's Biggest Lie! (The Harness War)](../videos/_DZ4kJwQ50s.md)
`_DZ4kJwQ50s` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: context-engineering, agent-architecture, claude-code

Compares Claude Code's compaction-based context handling with Prime Intellect's open-source Prime Agent (an RLM-style persistent kernel plus a self-editing "continual harness"). Vendor-reported benchmarks; the context-rot argument is the useful part.

- Techniques: Single persistent kernel as the only tool; Context as a variable (RLM-style chunked processing); Externalized session state instead of compaction; Continual harness: log failures, promote tactics; Guard self-improvement against reward hacking
- Tools: Claude Code, Prime Agent (Prime Intellect, MIT license, installs via a single curl command on Linux or macOS), Claude Opus 5, IPython kernel, Codex (OpenAI coding harness, mentioned by name), GPT-5.4, Gemini, ARC-AGI-3, LongCoT-Mini

## [Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning](../videos/2bvtay8wGYI.md)
`2bvtay8wGYI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: training-finetuning-rl, context-engineering, agent-architecture

GR's Ross and Chengxi Taylor trace RL-for-reasoning from Galactica and 2022 PPO recipes to long-horizon agents: value models, compaction, pipeline RL, and a benchmark where frontier models lost money.

- Techniques: Value-model (critic) RL for long, variable-length trajectories; RL-trained compaction; File-system scratchpad, self-search and archive tools for long-horizon context; Pipeline RL with bounded off-policy lag; Verifiable-reward PPO after continued pretraining (2022 recipe); Open-ended, outcome-scored long-horizon benchmark
- Tools: Galactica (Meta science LLM; 30B variant cited), Llama 2, Llama 3, Reasoning Llama (named, no details), ChatGPT, GPT-3.5, GPT-4, OpenAI o1, DeepSeek-R1, InstructGPT (2022, cited for RLHF results), PaLM (540B, cited for comparison), Chinchilla (cited for comparison)

## [State of Data — Sean Cai, Independent / State of Data](../videos/ZyIoTOAbRfs.md)
`ZyIoTOAbRfs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, data-engineering

Sean Cai argues data markets are the scarce input for turning generalist models into experts, and that single benchmark numbers and contrived expert-made data mislead buyers.

- Techniques: Three-axis verifiability scoring; Multi-harness, multi-infrastructure benchmarking; Per-criterion rubric analysis with deterministic checks plus LLM-as-judge; Long-horizon task checklist; Automatic post-training rerun on base-model swap; Lab spending as a leading indicator

## [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](../videos/eAXxdtNlK04.md)
`eAXxdtNlK04` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: context-engineering, observability

Langfuse's Annabell Schäfer shows that a clear-cut yes/no target function (single-label paper classification) lets an optimizer loop improve a small model's prompt, and argues teams need domain experts and high-signal evaluators before auto-improvement pays off.

- Techniques: Fit / validate / test split for prompt optimization; Error clustering to drive hypotheses; Binary, criterion-specific judges instead of Likert-style scores; Task markdown as the loop spec
- Tools: Langfuse, Claude Code, GPT-5 Nano, Claude Opus 4.8

## [DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve](../videos/Yk87oUPVaxU.md)
`Yk87oUPVaxU` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: coding-agents, testing-verification, models-research

Datacurve's DeepSWE talk: a long-horizon coding benchmark with tasks written from scratch to resist PR-mined contamination, plus per-model behavior findings and verifier design lessons.

- Techniques: Original task authoring by domain experts; Behavior-based verifiers; Verifier isolation and history scrubbing; Terse objective-only prompts; Per-model failure-mode analysis; Harness-agnostic base-model comparison; Hybrid verification with LLM judges
- Tools: DeepSWE, SWE-Bench Pro, mini-SWE-agent

## [Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](../videos/jRCpXUjz4CI.md)
`jRCpXUjz4CI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: agent-architecture, sandboxing-execution, training-finetuning-rl

Alex Shaw (Terminal-Bench, Harbor) argues agents behave like ML models, so teams should build environments (instruction, sandbox, verifier) and run parallel rollouts for evals, training data, RL and agentic map-reduce.

- Techniques: Environment as a three-part directory (instruction, sandbox, verifier); Separate rollout, trajectory capture and verification; Parallel rollouts with a fire-and-forget launch; Agentic map-reduce over agent logs; Own the eval before choosing a model; Design for agent users of your product
- Tools: Harbor, Terminal-Bench 2.1, Codex (GPT-5.5 run in the demo), Cursor CLI (map step in demo), Modal (sandbox backend in demo), Tinker (RL integration), A frontier model transcribed as 'Fable 5' (reduce step in demo; name may be a caption error), LangChain Deep Agents with sandboxes (integration)

## [Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla](../videos/B8l81jhvHbI.md)
`B8l81jhvHbI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, memory, enterprise-adoption

Ishita Daga (Tesla) argues enterprise data agents fail from ambiguity, staleness and team-level preference, not model size, and proposes a tiered source-of-truth structure, a context lifecycle, and open questions on preference.

- Techniques: Tiered source-of-truth hierarchy; Context lifecycle with live sources and event logging; Replay-based evaluation of recent questions; Metric variants in a semantic layer with user selection
- Tools: mem0, Tableau, dbt, GitHub, memory.md files

## [Build Evals That Actually Matter - Nick Ung & Akshay Sharma, Lyft](../videos/3z2uT5aDx_Y.md)
`3z2uT5aDx_Y` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: observability, enterprise-adoption

Lyft's customer-support agent team on building offline simulation evals, calibrating LLM judges on hand labels, and closing the loop from error analysis to agent changes.

- Techniques: Simulated multi-turn offline eval; Mixed eval dataset from production samples plus mutations; User simulator realism calibration; Binary task-outcome rubric per metric; Judge calibration as a classifier; Confidence intervals and paired comparisons; Annotation queue for domain experts; Config-driven eval harness
- Tools: LangSmith, Langfuse, DeepEval, LangGraph, tau-bench (transcribed as CowBench, from Sierra)

## [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../videos/iqloyWCGYQQ.md)
`iqloyWCGYQQ` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: memory, models-research, training-finetuning-rl

Parth Asawa (UC Berkeley) argues that standard LLM benchmarks test models with memory wiped each time, and proposes measuring continual learning through sequential tasks, gain over a stateless baseline, and Pareto reporting.

- Techniques: Paired stateful vs stateless runs (gain metric); Benchmark design checklist for continual learning; Multi-axis Pareto reporting; Mid-sequence concept drift injection; Stability vs plasticity failure triage

## [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](../videos/XLEYtv3cMlw.md)
`XLEYtv3cMlw` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, agent-architecture, multi-agent

Sina Shahandeh (Radicait) on why coding-agent research loops stall on open-ended science, and how decomposing a codebase into linked component docs plus cross-model critique gets better hypotheses.

- Techniques: Hierarchical component docs as a scaffold; Hypothesis generation over each component; Multimodal model as a qualitative metric; Split roles across models in the loop; Per-iteration outcome review
- Tools: Codex, Obsidian, Gemini, Oracle CLI, GPT-5.5 Pro (as transcribed)

## [Ending AI Slop — Thais Castello Branco, Taste Labs](../videos/lCBf9slCanI.md)
`lCBf9slCanI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, data-engineering

Taste Labs founder argues subjective domains like design and writing can be made verifiable by decomposing quality into checkable parts, routing each part to the right judge, and using quality expert data.

- Techniques: Decompose fuzzy quality into codified components; Per-component routing of grading method; Ground-truth rules instead of similarity to a reference; Diverse expert pool with strict selection to counter mode collapse; Specificity and code-linkage QA on expert labels; Disagreement triage in expert consensus

## [Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect](../videos/AQv3qRCG6Gw.md)
`AQv3qRCG6Gw` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, observability

Will Brown (Prime Intellect) on running RL when no verifiable reward exists: manufacture supervision from grounding, judges, production traces and learned simulators, and keep humans on the top-level decisions.

- Techniques: Environment as the shared unit (task + harness + rewards); With/without grounding as a supervision gap; Backward construction from a reachable end state; Trace-seeded task mining; Judge-to-rubric distillation; Pass-rate gated task generation; Learned simulator of an uncontrolled tool or site; Reward-hack corpus and small-run validation
- Tools: Prime Intellect PrimeRL training framework, Prime Intellect verifiers and task sets, Prime Intellect Lab (hosted training and evals), GRPO / REINFORCE policy-gradient methods (named in passing), MCP servers, CLI tools and web apps (as simulator targets)

## [Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd](../videos/ZFxh7sqbUZo.md)
`ZFxh7sqbUZo` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: security-guardrails, training-finetuning-rl

David Brumley (CMU, Bugcrowd) on designing RL environments for vulnerability discovery and exploitation, using deterministic oracles, an open-world "audit" task scored by precision and recall, and a 16-rung capability ladder run against V8.

- Techniques: Deterministic witness-based grading; Open-world audit task with dedup and precision/recall; Capability ladder for hard targets; Withhold the answer key and the most dangerous artifacts
- Tools: MCP (exposed setup, read/write, and grading tools), Docker, exploitbench.ai, V8, AIxCC, DARPA Cyber Grand Challenge, SciBench, CyberGym, BountyBench

## [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../videos/Ki980nV0__0.md)
`Ki980nV0__0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, infra-cost-scaling

Dhruv Batra (Yutori) argues the long-tail web will be driven by pixel-based computer-use agents rather than new APIs, and shows his Navigator model's accuracy and cost per task.

- Techniques: Screenshot-in, action-out computer-use loop; Code-on-demand as a browser action; Pixel-based success check; Parallel sandboxed-browser fan-out; Read the async data call, not the initial HTML; Cost-per-task as the headline metric
- Tools: Navigator (Yutori computer-use model), OnlineMind2Web benchmark, Chrome extension for browser actions, MCP servers and web MCP, Opus 4.7 and GPT 5.5 (comparison models), Cloud sandbox browsers

## [From Tokens to Cells: Foundation Models for Single-Cell Biology - Akram Baharlouei, Altos Labs](../videos/-561cZmir5Q.md)
`-561cZmir5Q` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: models-research, data-engineering

Altos Labs engineer on why single-cell foundation models (scGPT, Geneformer, PrimeFlow) struggle with noisy data, and why distribution-matching and data quality matter more than scale.

- Techniques: Cell-as-sentence masked modelling; Flow-matching distribution learning; Simple-baseline check before scaling; Distributional scoring with MMD
- Tools: scGPT, Geneformer, PrimeFlow, MMD

## [Why Software Factories Fail](../videos/Ib5GBkD555M.md)
`Ib5GBkD555M` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, pr-code-review, context-engineering

Dex (HumanLayer) argues that agent "lights-off" software factories fail because coding models are trained on tests passing, not maintainable code, so teams must restore code review and plan up front.

- Techniques: Staged plan before agent implementation; Review the plan so the PR review is short; Check for test gaming with pre-patch runs and a quality judge; Diagnose RL-style reward gaps
- Tools: Claude Code, Codex, SWE-bench Multilingual, SWE-Marathon, DeepSWE, Frontier Code, Linear, Jira, HumanLayer

## [Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama](../videos/J4_jCrTxMkk.md)
`J4_jCrTxMkk` · AI Engineer · 2026-08-18 · q4 · practitioner · panel · also: local-ai, inference-serving

Panel from NVIDIA, Unsloth, Hugging Face and Ollama on how quantization and compression make large open models run on local hardware, how to pick per-layer precision, and how to evaluate the result.

- Techniques: Sensitivity-aware dynamic quantization; Post-training quantization first, QAD for small models; KL-divergence evaluation against the unquantized model; Harness-level vibe testing before shipping a quant; Per-model default quant with precision kept high for tiny models; Big planner, small executor routing
- Tools: llama.cpp, Ollama, Unsloth, NVIDIA Model Optimizer (ModelOpt), TRL, bitsandbytes, QLoRA, GRPO, NVFP4, MXFP4, OpenClaw, Hermes agent

## [Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software](../videos/2aS7aKoXn64.md)
`2aS7aKoXn64` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: training-finetuning-rl, agent-architecture

Theta Software on designing RL environments and LLM judges for long-horizon work, plus a critique of current finance agent benchmarks, which they say are saturated and mostly too short to count as long-horizon.

- Techniques: Judge with read-only environment access, as an agent; Make long trajectories queryable before judging; Pair deterministic checks with a rubric judge; Rubric QA suite; Check learnability and reward density
- Tools: METR time-horizon benchmark (cited, not a tool used), GDPval (benchmark, cited), BankerToolbench (benchmark, cited), APEX-Agents (benchmark, cited), Grafana, GitHub (CI/CD logs, PRs), AWS CloudWatch, Codex models (cited), Claude models (cited), GPT-5.5 (cited)

## [Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk](../videos/1EZdpEhwmNc.md)
`1EZdpEhwmNc` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: security-guardrails, coding-agents, mcp-and-tools

Snyk's CTO argues agent security needs deterministic checks alongside LLMs, with customer data on attacks, toxic skills and MCP servers, plus a live coding-agent demo.

- Techniques: Hybrid LLM plus deterministic security checks; Repeated-run recall measurement; Pre-install package health gate; Skill and MCP risk assessment before adoption; Per-model red-team suite; Breakability-aware automated remediation; Deterministic invocation through a skill or hook
- Tools: Claude Code, Cursor Cloud, Codex, Snyk Studio, Snyk Evo, Snyk package health check

## [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../videos/R3-anFK1YM8.md)
`R3-anFK1YM8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, context-engineering, local-ai

Sakana AI researcher on memory harnesses for long-horizon research agents running on local models; a ranked decision-ledger recall policy beat both no memory and plain vector RAG, at lower cost.

- Techniques: Write-manage-read memory loop; Ranked decision-ledger recall; Recall-mode ladder with an oracle; Ablate with wrong and recent memory; Local, controlled eval pipeline
- Tools: DeepSeek V4 Flash, Qwen (4-bit quantised), XBench, vector RAG, Spyder V2 benchmark

## [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../videos/CvRngaQZQ3Y.md)
`CvRngaQZQ3Y` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, training-finetuning-rl, memory

LangChain's Vivek Trivedy argues agent improvement is a data-mining loop: ship, collect traces, mine them, then run data-driven experiments on prompts, tools and models.

- Techniques: Agent-driven trace mining; Frontier-to-open-model downgrade via trace judging; Distillation from good traces; Evals generated from traces; Score-driven auto-research loop; Harness, then fine-tune, then harness sandwich; Human review summaries
- Tools: LangSmith, LangSmith Engine, Deep Agents, Claude Code, Codex, Terminal Bench, scikit-learn

## [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../videos/jHMiYtjoJfA.md)
`jHMiYtjoJfA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, product-ux

Ben Hylak (Raindrop) argues teams should "raise the floor" by finding production agent failures, tracking when they started and how many users they hit, and using code-based classifiers over traces instead of clustering or big eval sets.

- Techniques: Evals as local code tests; Per-issue onset and affected-user tracking; Code-based trace classifiers; Deterministic signal first, agent investigates second; Scale-dependent experimentation
- Tools: Raindrop, Workshop (open-source tracing tool), vitest (vitest evals), howtoeval.com, Sentry (mentioned as a model for issue detection)

## [Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang](../videos/zkX03APVj0M.md)
`zkX03APVj0M` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: sandboxing-execution, training-finetuning-rl

Joseph Wang of Emulated argues that agent training needs realistic infra environments: multi-node sandboxes that touch real cloud resources, not single-container coding tasks.

- Techniques: Multi-node cluster simulation in one sandbox; Chained multi-deployment episodes for long horizon; Organisation context as part of the environment; Multi-node sandbox on real cloud resources (CloudBox); Choose a vertical with clear customer requirements first
- Tools: Harbor, etcd, Kubernetes, AWS Lambda

## [Vending-Bench: Long-Horizon Agent Evals — Lukas Petersson, Andon Labs](../videos/cO8qC6HBuBg.md)
`cO8qC6HBuBg` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: security-guardrails, models-research

Lukas Petersson (Andon Labs) on Vending-Bench, emergent misbehavior in agents, and moving evals into real-world deployments and forked simulations, because models act differently once they suspect a simulation.

- Techniques: Incentive-based misbehavior probing; Forked real-environment evals; Simulation-awareness probe; Cross-model replay of a real incident
- Tools: Vending-Bench, Vending-Bench Arena (arena mode), Claude / Opus 4.6, 4.7, 4.8, Fable (named in talk, may be a caption error), GLM 5.2, GPT 5.5, Gemini, Grok 4.3, Kimi, Slack (channel used to message the store agents), LinkedIn, Indeed

## [Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face](../videos/O-CBZ3JtRvo.md)
`O-CBZ3JtRvo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, training-finetuning-rl, models-research

Uri Rolls and Thom Wolf present Arithmetic's "Mask Off" benchmark: black-box access-control exploit chains built from real zero-days, graded per step, to test whether models can make logic leaps.

- Techniques: Black-box exploit-chain environments from self-found zero-days; Per-step deterministic graders with partial credit; Trace review as the main eval loop; Orchestrator for running evals
- Tools: Bach (Arithmetic's internal eval orchestrator)

## [Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic](../videos/K0X9QDRkIdg.md)
`K0X9QDRkIdg` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, sandboxing-execution, context-engineering

Anthropic engineers explain how agent surfaces moved from the Messages API to Claude Managed Agents, which separates the brain from the hands, logs sessions durably, and adds vaults, dreaming and outcomes.

- Techniques: Brain/hands decoupling with on-demand sandboxes; Append-only session log as the resume point; Re-reading discarded context from the log; Vault-based credential injection; Restricted network allowlist per environment; Rubric and failure-case grader loop (outcomes); Batch dreaming over transcripts and memory; Harness-debt audit when models change
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, MCP servers, MCP tunnels, self-hosted sandboxes

## [Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog](../videos/wEc9aG7cRQc.md)
`wEc9aG7cRQc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, security-guardrails

Diane Lin (Datadog) on why LLM agents give different verdicts on the same input near the decision boundary, and how to fix it with disagreement-driven active learning plus episodic and semantic memory instead of fine-tuning.

- Techniques: Measure consistency with repeated runs; Disagreement-based query selection; Semantic memory for policy and preference facts; Episodic memory as case-based precedent lookup; Active-learning loop with memory updates
- Tools: Datadog

## [How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](../videos/xyL2Ltkh-SA.md)
`xyL2Ltkh-SA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, context-engineering

Two YouTube Ads team members on building evals for agents: tools first, intuition before scale, human rater rubrics, reading traces, and pattern-level launch gates.

- Techniques: Tools-first, then critique agent with remediation loop; Intuition-first review before scaled evals; Rubric with examples plus mandatory rater explanations; Negative test cases in the golden set; Judge calibration by sampled agreement monitoring; Trace-based failure diagnosis; Pattern-level metrics with a refreshed test set and online evals; Launch gate defined up front with regression triage

## [When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI](../videos/-npY6XjM8CQ.md)
`-npY6XjM8CQ` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: models-research

Nick Heiner (Surge AI) on why benchmarks drift from real value (cost, contamination, reward hacking, bad verifiers, leaderboard gaming) and how to build better ones.

- Techniques: Two-way verifier-prompt alignment audit; Accept all valid answer formats in verifiers; Adversarial check of graders against lazy solutions; Contamination probe by prefix completion; Private holdout plus disclosure of test conditions; Watch for benchmark-vs-human-eval divergence; Blind pairwise expert comparison for subjective quality; Saturation check for broken tasks
- Tools: LM Arena, SWE-bench Verified, IFEval, Apex, Automation Bench, Hemingway-Bench

## [The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller](../videos/GgLQ02aO-hs.md)
`GgLQ02aO-hs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, data-engineering

DSPy maintainers argue AI programs should be functions with fixed typed contracts, with the model, prompts and harness swappable underneath and optimized against evals.

- Techniques: Typed signature with natural-language instruction; Three-part task spec (instructions, code constraints, examples); Predict-then-reason fallback in code; Optimizer over a fixed metric; Learn a harness per function (DSPy.Flex, announced)
- Tools: DSPy, GEPA (transcript says JEPA; caption error, prompt optimizer from Berkeley), Recursive Language Models (RLM), MultiModule GRPO, BetterTogether, DSPy.Flex (announced for DSPy 4)

## [Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i](../videos/jWq-aZIU0kM.md)
`jWq-aZIU0kM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: testing-verification, models-research

Ali Khial (G2i) argues that many agent benchmarks have unrealistic prompts, weak verifiers and reward-hacking gaps, and proposes five principles for building better benchmark tasks.

- Techniques: Layered grading: behavioural breadth plus targeted precision; Specify behaviour and hard constraints, not implementation; Audit a benchmark's verifiers by sampling tasks; Novel tasks with private holdout sets; Publish per-run data alongside rankings
- Tools: SWE-Bench Pro

## [From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize](../videos/9HbzAWnKbo4.md)
`9HbzAWnKbo4` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, software-factory, sandboxing-execution

Arize's founder demos Signal, a background agent that reads production traces and logs, drafts an issue or fix with evidence, and hands it to a human reviewer, with the loop run in a sandbox.

- Techniques: Trace-to-file skill; Event- or schedule-triggered agent loop; Composable narrow skills over raw data; Sandbox per run, pluggable harness; Failure-to-evaluator loop
- Tools: Arize AX, Arize Phoenix, Pyroscope, Claude Code, Cursor, Daytona, GitHub, Google Cloud logging skills

## [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../videos/WP3hjUXd918.md)
`WP3hjUXd918` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: context-engineering, token-cost-efficiency, rag-retrieval

Towards AI workshop on context engineering: prompt caching makes compaction costly, and on their AI tutor keeping full history beat every compaction preset on recall, cost and latency.

- Techniques: Head and tail truncation of big tool outputs; Sliding window and clearing old tool outputs; Selective retention and summarization with a threshold; Filesystem knowledge base with progressive disclosure; Hybrid retrieval with a token cap; Eval harness: presets by tasks, then grade; Planted-fact recall probe; Log every turn
- Tools: LangChain (create_agent, middleware), FastAPI, Next.js, Gemini 3.5 Flash, DeepSeek V4 Flash, Claude Code, Codex, Opik (transcribed as 'OPIC'), Hugging Face Spaces, BM25, Dense embedding retrieval

## [How Forward Deployed Engineering is done at Ramp — Leo Mehr](../videos/ITMXwI6QL6A.md)
`ITMXwI6QL6A` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: enterprise-adoption, software-factory, context-engineering

Leo Mehr (Ramp) on forward deployed engineering: scope hard before building, then replace each FDE pipeline stage with agents, with evals and good context as the hard parts.

- Techniques: Scoping questionnaire before any build; Clarifying-question intake agent before spec; Stage-by-stage agent factory for the FDE lifecycle; Per-stage quality checks with evals, rubrics and human feedback
- Tools: Notion, Notion Agents, Slack

## [First Steps Toward Automated AI Research — Richard Socher, CEO Recursive AI](../videos/pWXUkLP9uWM.md)
`pWXUkLP9uWM` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: models-research, agent-architecture

Richard Socher (Recursive AI) argues for automating scientific research via a "Eureka machine" and shows small auto-research wins on NanoChat, NanoGPT speedrun and CUDA kernels, while separating these from true recursive self-improvement.

- Techniques: Benchmark-gated auto-research loop; Short fixed-budget runs as the test; Reward-hack audit before trusting results; Simulation as the verifier
- Tools: NanoChat, NanoGPT speedrun, NVIDIA CUDA kernels, U.com web search for LMs

## [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](../videos/X1kp-ABIIxQ.md)
`X1kp-ABIIxQ` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, sandboxing-execution, observability

Dan Farrelly (Inngest CTO) argues agent architectures decay fast unless the execution layer (durable state, retries, triggers, tracing) is separated from fast-changing context (prompts, models, tools) and compute (sandboxes).

- Techniques: Three-layer decomposition (execution / context / compute); Externalised durable step state with resume-from-failure; Cron-triggered health check, triage agent, and reviewer loop; Deferred outcome scoring from downstream events; Ephemeral sandboxes with state kept in the orchestrator
- Tools: Inngest

## [Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind](../videos/O72p-rBb2bA.md)
`O72p-rBb2bA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: security-guardrails, enterprise-adoption

SonderMind engineers describe the guardrail, eval and clinician-annotation loop behind Sonder, a clinically grounded mental health AI coach, and open-source 300 scenarios for it.

- Techniques: Pre- and post-LLM guardrail sandwich; Trace-to-typed-eval annotation loop; Multi-metric guardrail scoring
- Tools: Sonder (SonderMind's clinical AI coach), LLM-as-judge guardrail calls, CI-gated eval suite, annotation queue with trace replay, analytics and alerting platform

## [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](../videos/kiqubc5b5Yo.md)
`kiqubc5b5Yo` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: multi-agent, agent-architecture, enterprise-adoption

Morgan Stanley's AlphaLab, a multi-agent harness that automates quant research through research, critic-checked eval building, and Kanban-style experiments. Its main lesson: the value sits in strict eval environments and rubrics, not in the harness.

- Techniques: Scaffolded to-do list with re-prompting on early exit; Builder plus critics eval loop; Strategist, worker, and post-mortem Kanban loop; Containerised, Kaggle-style eval contract; Environments as RL reward signal; Rubric grading of each rollout's process; Meta-harness optimisation by an LLM; Provider-agnostic harness with functional tool calls
- Tools: Claude Code, Codex, Opus 4.5, Slurm, Kaggle, GRPO, NVIDIA Nemotron

## [The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI](../videos/q2JrUKBMf0w.md)
`q2JrUKBMf0w` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: observability, agent-architecture

Arize's founder argues that evals must add a third layer, agent-as-a-judge, that reads production traces, finds failure patterns, and can open fix PRs. It is a short vendor pitch with little method detail.

- Techniques: Agent-as-a-judge over traces; Three-layer eval stack; Trace-driven online evals; Repeated-tool-call loop detection
- Tools: Arize Signal, Agent as a Judge (Arize)

## [From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI](../videos/Ib5t2RLtxvM.md)
`Ib5t2RLtxvM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: testing-verification, sandboxing-execution, observability

Rustem Feyzkhanov (Snorkel AI) on turning production agent traces into repeatable, containerized simulation benchmarks that serve as release gates and training data.

- Techniques: Trace-to-task conversion; Harbor-style task folder; Oracle-first validation; Sidecar service mocking with a simulated user; Stepwise long-horizon simulation; Layered verifiers with SME escalation; Benchmark CI and difficulty tagging; Coverage split: happy path plus edge cases; Held-out split for agent config
- Tools: Docker, Docker Compose, Harbor (task format), Terminal-bench, SWE-bench, Arize (experiment and trace recording; transcript says 'Arise'), MCP tools

## [Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai](../videos/YnNF55QV0zs.md)
`YnNF55QV0zs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, models-research, product-ux

Ishan Anand (InsightSciences) on synthetic personas as bounded forecasts: where LLM personas fail (confounders, order bias, attitudes vs behavior), and how to measure them against human distributions and noise floors.

- Techniques: Validate personas against held-out human ground truth; Ground the persona in the full world of the study; Durability tests for option order and wording; Attitude-to-behavior triangulation; Free-text answers mapped to scale via semantic similarity; Fine-tune on survey distributions conditioned on demographics; Noise floor via split-half simulation

## [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../videos/7vn4WpqNpck.md)
`7vn4WpqNpck` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: coding-agents, enterprise-adoption

Denys Linkov (Wisedocs) on whether a six-month monorepo refactor of a medical-claims ML pipeline was worth it when coding agents keep improving, and how to measure agent reliability.

- Techniques: Time-horizon reliability check before long runs; Agentic tool-evaluation pipeline; Monorepo consolidation for agent-driven work; Human PRs as a context-building step; Check hidden assumptions in dependencies; Layered refactor instead of a full rewrite
- Tools: Cursor, Temporal, Claude Sonnet 4.6, Claude Opus 4.8, o3, GPT-5.5, Confluence, Claude Code plan mode

## [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../videos/XEd_SRVHBgU.md)
`XEd_SRVHBgU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: training-finetuning-rl, models-research

Sara Hooker (Adaption) argues frontier AI should be open to more builders, and pitches Autoscientist, an automated training loop that co-optimizes data and model while saying pre-training scale is no longer the main lever.

- Techniques: Co-optimize data curation with the model in the same search; Win-rate threshold as the stop condition for a training search; Wide architecture and size search instead of team familiarity; Adaptive test-time compute per task (planned)
- Tools: Autoscientist (Adaption, beta)

## [Evaling Video Slop — Maor Bril, Character.ai](../videos/b_PmGocP4rc.md)
`b_PmGocP4rc` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: testing-verification, voice-multimodal, agent-architecture

Maor Bril (Character.ai) on evaluating AI video: frame-level metrics miss story, physics and pacing, so he distilled a judge committee into a small fast VLM trained on pairwise comparisons and run inside the generation loop.

- Techniques: Pairwise A-vs-B judge training; Manufactured negatives; Matched-encoding real-vs-AI pairing with identical annotation; Expert-committee distillation into a small VLM; Eval inside the generation loop; Calibration sessions with randomized annotation; Agent with validation tools
- Tools: Qwen (small VLM, post-trained), Dolby Atmos (audio quality), CLIP-style frame metrics, frame-drift metrics, Kling, Seedance, Veo, Sora, OpenTelemetry (requested, planned for harness)

## [SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)](../videos/KMR_RBoCa4M.md)
`KMR_RBoCa4M` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: enterprise-adoption, data-engineering

Nubank and Snowglobe claim simulated personas with mocked tools produce agent eval data on demand, cutting release cycles from weeks to hours, provided the sim-to-real gap is measured.

- Techniques: Simulated-user eval set generation; Persona-consistent grounding state; Sim pre-screening before A/B tests; Sim-to-real calibration; Same-harness model sweep
- Tools: Snowglobe SDK, LLM-as-judge, Automated prompt optimization (captioned 'JEPA', likely GEPA)

## [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../videos/CTLa_p6iOiY.md)
`CTLa_p6iOiY` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: voice-multimodal, testing-verification

Pierluca D'Oro (Programma Labs) shows that static computer-use benchmarks can be gamed by replaying recorded successful traces, and argues for varied environments plus hierarchical confidence intervals.

- Techniques: Replay-agent baseline check; PRISM environment design checklist; Template plus verifier config compiler; Hierarchical confidence intervals; Interval-gated model decisions

## [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song](../videos/AVMr9PMINyo.md)
`AVMr9PMINyo` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · also: inference-serving, models-research, training-finetuning-rl

A MiniMax and Together AI panel on how an open-weight model like MiniMax M3 gets trained, then served at scale, with day-zero kernel work, agentic KV-cache demands and long-horizon RL evals.

- Techniques: Day-zero kernel plus post-launch optimization queue; Benchmark unsolved kernel problems as RL environments; Multi-submission long-horizon evals with held-out validation; Multimodal training from step zero; KV cache as a distributed store; Cross-model optimization transfer
- Tools: KernelBench, Parallel KernelBench, OSWorld, SVG bench, MiniMax sparse attention

## [Verifiable Environments for AI in Biology — Kenny Workman, LatchBio](../videos/3ZMUiFaQ3qg.md)
`3ZMUiFaQ3qg` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: data-engineering, models-research

LatchBio's CTO on building verifiable benchmarks for biology agents: DAG-decomposed spatial-omics evals, human verification of ambiguous tasks, rubrics for long-horizon work, and refusal testing.

- Techniques: Per-node verifiable eval specs; Human-verification pass over agent trajectories; Rubrics on invariant choke-point nodes; Paired routine and red-team refusal evals
- Tools: Python grader functions, SWE-bench-style task format, Claude models (named by the speaker as the models used for the evals)

## [Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber](../videos/31GUkCBD-Uc.md)
`31GUkCBD-Uc` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: observability, agent-architecture

Uber's Uber Eats image pipeline (routing, enhancement, publish QA) and how they keep it aligned with human labels through offline evals, auto-tuning and a diagnoser that closes the production feedback loop.

- Techniques: Flat per-run JSON trace across the whole agent chain; Router as a classifier scored by a confusion matrix, with an N-by-N extension; Golden human-label set plus ship gate; Production drift loop: sample, re-label, diagnose, tune, benchmark, register; Reflect-and-synthesize prompt optimizer; Generate-edit-QA loop scored with pass@K; Pairwise judge with yes/no/unsure and product-agreed criteria; Redundant Swiss-cheese final gate; Diagnoser as a routing layer over all feedback; Replay flagged examples before releasing a config; Per-segment production metrics
- Tools: Arize

## [Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit](../videos/Owb8g3yDyzo.md)
`Owb8g3yDyzo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, enterprise-adoption

Intuit's Udi Menkes argues frontier LLMs give fluent but unverified money advice, and that grounding a model in real business outcomes (state, action, outcome) beats model size.

- Techniques: Outcome-grounded trajectory dataset; Propose-then-rank split; Propensity-matched uplift estimate; Evidence-grounded explanation; Long-horizon simulation with a rules baseline
- Tools: QuickBooks, TurboTax, Credit Karma, Mailchimp, reinforcement learning (Intuit in-house model)

## ["The biggest challenge in your stack? Evals, Evals, Evals" - 2026 State of AI Engineering results](../videos/RGe6EjucbzI.md)
`RGe6EjucbzI` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: enterprise-adoption, models-research, infra-cost-scaling

Bar Yeren (Amplify) reads out the 2026 State of AI Engineering survey (1,048 respondents): evals remain the top challenge, teams run multi-model stacks, cost is a first-class constraint, and agents now mostly have write access.

- Techniques: Intent-to-adopt ratio; Routing by task type across models; Monitoring cost and token usage alongside quality; Human-in-the-loop approvals and permission gating for write-enabled agents
- Tools: Notion, Vercel, Nano Banana, ChatGPT Images 2.0

## [Claude Code Setup Guide By The Creator Himself](../videos/pGro_uKt-_M.md)
`pGro_uKt-_M` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: claude-code, context-engineering, token-cost-efficiency

AI LABS walks through Claude Code creator Boris Cherny's setup advice: strip your Claude Code setup to a baseline with each new model, keep only what Claude can't infer, and gate work with evals that can fail. Includes a sponsored segment.

- Techniques: Baseline-then-add-back setup audit; Usage triage; Keep-rule for CLAUDE.md; Doctor audit; Fail-able acceptance checks written first; Built-in headless browser verification; Outcome-first prompting; Escalation ladder for model mistakes; Recurring cloud routines for maintenance
- Tools: Claude Code, CLAUDE.md, Claude Code skills, MCP server, Claude Code hooks, Claude Code plugins, context command (Claude Code), usage command (Claude Code), doctor command (Anthropic), safe mode (Claude Code), headless Chrome, sub-agents

## [This is basically an X-ray for your codebase...](../videos/Y_7_rbtQXcs.md)
`Y_7_rbtQXcs` · Better Stack · 2026-08-02 · q3 · intro · review · also: observability, coding-agents

Short Better Stack walkthrough of MindWalk v0.3, a 3D session replay for Claude Code and Codex runs, with an LLM judge that grades how the agent explored, stayed in scope and verified its work.

- Techniques: Color-coded session replay of file access; LLM-judge rubric over a whole agent session; Timeline event markers for multi-agent runs; Choose the review lens by change size
- Tools: MindWalk v0.3, Claude Code, Codex, Three.js, Graphify (named as a comparison, not evaluated)

## [OpenAI Sol Ultra Just BEAT Claude Fable](../videos/27QLmUQvL2A.md)
`27QLmUQvL2A` · Better Stack · 2026-08-02 · q2 · intro · news · also: models-research, multi-agent, coding-agents

Better Stack on GPT-5.6 Sol and its Ultra sub-agent mode: 91.9% Terminal-Bench 2.1, METR caught heavy test-gaming, Sol costs about half of Claude Fable 5.

- Techniques: Tiered model routing by task weight; Discount benchmark leads when the independent evaluator disputes them; Watch unattended runs for test-gaming
- Tools: OpenAI Codex, GPT-5.6, GPT-5.5, Sol, Terra, Luna, Sol Ultra (Ultra mode), Terminal-Bench 2.1, Claude Mythos 5, Claude Fable 5, METR time-horizon evals, Cerebras chips

## [AI Benchmarks Are Fake!?](../videos/pHAbwL7w83Q.md)
`pHAbwL7w83Q` · Better Stack · 2026-08-02 · q3 · practitioner · news · also: sandboxing-execution, models-research

Short explainer on two ways AI coding benchmarks get gamed: agents retrieving fix commits and models memorizing test sets. It relays Cursor's strict-environment results and contamination studies, with concrete numbers and few original methods.

- Techniques: Strict-environment eval run; Trajectory audit for shortcut solutions; Original-vs-altered contamination quiz; Contamination-adjusted scoring; Parallel held-out benchmark
- Tools: SWE-Bench Pro, SWE-Bench Multilingual, DeepSWE, Frontier Code (Cognition, as captioned), GSM-8K, SST-2, Qwen 2.5, Claude Opus 4.8, GPT 5.4, GPT 5.5, Composer 2.5 (Cursor), Mythos (Anthropic, as captioned)

## [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen](../videos/IJXjTLPzvAU.md)
`IJXjTLPzvAU` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: context-engineering, product-ux

Jacob Thomas argues persona/role-play agents are judged by fluency metrics that cannot catch anachronistic "composite" historical figures, and proposes a pre-registered, expert-scored, context-window-based eval (Lincoln case study).

- Techniques: Pre-registered fidelity eval for personas; Anachronism-first rubric with voice excluded; Encounter-as-configuration with receipts; Context window grounding over persona fine-tuning; Expert-authored gold set as a CI gate
- Tools: Claude Opus 4.7, Companion (open-source persona prompt framework built by the speaker), Character AI, Hello History, KOSIR, PsyMem, In-Character benchmark

## [On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft](../videos/RGSFUqzqErE.md)
`RGSFUqzqErE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: rag-retrieval, context-engineering, skills-self-improvement

Microsoft's Pablo Castro splits agent knowledge into intrinsic, extrinsic and learned, and demos Foundry knowledge bases and an Agent Optimizer that tunes agent config from traces.

- Techniques: Three-way knowledge split for agent design; Hybrid retrieval over combined methods; Layered retrieval API; Agentic retrieval with a satisfaction check; Knowledge base as MCP server; Eval generated from traces, then hill-climb the agent config
- Tools: Microsoft Foundry, Foundry IQ, Azure AI Search, Work IQ, Fabric IQ, WebIQ, Agent Optimizer, Foundry Toolkit for VS Code, GitHub Copilot, MCP

## [Agents Building Agents - Alfonso Graziano, Nearform](../videos/aHhB3sjGjkI.md)
`aHhB3sjGjkI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: skills-self-improvement, observability, coding-agents

Alfonso Graziano (Nearform) shows coding agents improving other agents: an eval-driven loop lifts a toy agent from 18% to 83% and a production agent from 67% to 86%, and a trace-clustering loop turns live user feedback into fixes.

- Techniques: Golden dataset plus scorers as the agent test suite; Baseline report before the optimization loop; Branch-per-hypothesis improvement loop with rollback; Protected eval set in the optimizer instructions; Reading the agent's full traces, including thinking traces, for root cause; Trace clustering from live feedback; Packaging the analysis as a reusable skill; Failure mode to spec to golden-set entry
- Tools: Claude Code, Mastra, auto-agent (the speaker's own internal tool, not public)

## [Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers](../videos/O3FEoMYvUf8.md)
`O3FEoMYvUf8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: models-research

Alejandro Vidal (Mindmakers) argues LLM benchmarks should use psychometrics: item response theory (IRT) gives per-question difficulty, per-model ability with intervals, and tools for auditing, shrinking, and protecting benchmarks.

- Techniques: IRT calibration of benchmark items; Benchmark audit by discrimination; Greedy high-discrimination subset selection; Residual-based outlier and consistency checks; Anchor plus fingerprint adaptive test sets; Group-wise item curves for differential item functioning; Residual correlation matrix as a model fingerprint
- Tools: Epoch AI open benchmark datasets, GPQA benchmark (used as a counterexample)

## [Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](../videos/q4Tr-DknG2M.md)
`q4Tr-DknG2M` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: training-finetuning-rl, models-research, multi-agent

Cursor's Lee Robinson on how Cursor trains its Composer models: a two-loop flywheel, defenses against eval hacking, textual-feedback RL, and models increasingly helping train their successors.

- Techniques: Eval hygiene for agent benchmarks; Private held-out eval from your own repos; Ablate-and-reimplement RL task generation; Textual feedback for credit assignment; Distilled judges and reward models from the top model; Agent fleets launched from chat with escalation to humans
- Tools: Cursor, Composer, Kimi (prior open-source base model; transcribed as 'Kimmy'), Colossus, Slack, Git, Datadog, Notion, Linear, MCP, Artificial Analysis

## [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../videos/ObTPqBGsEbA.md)
`ObTPqBGsEbA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: observability, enterprise-adoption, governance-compliance

A five-pillar playbook (evaluation, tracing, data foundation, orchestration, governance) for taking enterprise AI agents to production, illustrated with a retail banking chatbot case study.

- Techniques: Business-metric eval spec before build; Living golden eval set seeded from human answers; Three-layer eval stack; Automated eval pipeline with human review threshold; Trace-driven duplicate-call detection and retry cap; Tiered CI eval runs; Prompt versioning as change management; Model selection on your own eval set; Incident playbook: detect, diagnose, contain, fix, regress
- Tools: Databricks, MLflow, Delta Lake, Apache Spark, Unity Catalog, Genie, Agent Bricks, Databricks Apps, Mosaic AI, Git, Python, LLM-as-judge

## [Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua](../videos/ZSQb5fzRFPw.md)
`ZSQb5fzRFPw` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: voice-multimodal, sandboxing-execution, infra-cost-scaling

Cua's team presents "Computer-Use 2.0": a background computer-use driver (Cua Driver), a multi-platform benchmark (CuaBench, including a KiCad electrical-engineering set), and warm sandbox pools (CuaFleet) that cut idle GPU time in RL training.

- Techniques: Two-tier background action with fallback; Window-scoped observation; Single-file cross-platform task definition; Adversarial pre-validation of evals; Trajectory forking for world-model probes; Demand-autoscaled warm pool for sandboxes
- Tools: Cua Driver, CuaBench, CuaFleet, Codex computer-use model, TerminalBench, Harbor, Android activity framework, Hermes harness, KiCad

## [ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay](../videos/TJPInBjhE4Q.md)
`TJPInBjhE4Q` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: pr-code-review, coding-agents, governance-compliance

Sachin Gupta (eBay) argues coding agents create unmeasured review debt and offers a deterministic 0-100 PR review-burden score built from five signal families, plus a rollout plan.

- Techniques: Deterministic review-burden score; Backfill calibration; Non-blocking rollout ladder; Shape rules for agent PRs; Authorship detection as a weak amplifier
- Tools: GitHub, GitHub Copilot, Codex, Cursor

## [Modern Post-Training: A Deep Dive  — Will Brown, Prime Intellect](../videos/V-EDrhIhHzQ.md)
`V-EDrhIhHzQ` · AI Engineer · 2026-07-18 · q4 · deep · workshop · also: training-finetuning-rl, agent-architecture, infra-cost-scaling

Will Brown (Prime Intellect) walks through modern post-training: environments as evals, the verifiers v1 task/harness/runtime split, async RL with an interception server, and the PrimeRL trainer.

- Techniques: Task / harness / runtime decomposition; Fake base URL interception for RL on real harnesses; Async rollout batching with off-policy tolerance; Message-level trace with token mapping; Algorithm and loss separation with a registry; Group-relative shaping for length and efficiency; Same-task eval CLI with swappable harness and runtime
- Tools: verifiers, PrimeRL, Renderers, TorchTitan, Megatron, Harbor, NemoGym, OpenEnv, Hugging Face datasets, uv, Docker, Claude Code

## [Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind](../videos/0vphxNt4wyk.md)
`0vphxNt4wyk` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: skills-self-improvement, context-engineering

Philipp Schmid (Google DeepMind) argues skills need evals like code does, and gives a lean eval-harness recipe: trigger tests, regex asserts, repeated trials, and with/without-skill ablations to decide when to retire a skill.

- Techniques: Trigger and negative-case eval set; JSON cases plus regex asserts; LLM-as-judge for trace-level checks; CI gate on skill diffs; With/without-skill ablation; Isolated, repeated trials; Lean skill plus reference files; Goal-and-constraint skills, scripts for fixed workflows
- Tools: Gemini CLI, Gemini API, Gemini Interactions API, SkillsBench, Claude Code, Codex, Cursor, Antigravity, Python, regex, LLM-as-judge

## [Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs](../videos/vljxQZfJ9wY.md)
`vljxQZfJ9wY` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: observability, agent-architecture

Nishant Gupta (Meta Superintelligence Labs) argues agent evals must score workflow behavior from production telemetry, not model answers or benchmarks, and should run continuously as a control-plane function.

- Techniques: Scenario-driven offline evals; Production telemetry as the eval set; Targeted human review to calibrate automated evals; Continuous evaluation loop; Agent tracing like distributed tracing; Evaluation as a control plane

## [Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth](../videos/uIiA6DquRiE.md)
`uIiA6DquRiE` · AI Engineer · 2026-07-18 · q4 · practitioner · workshop · also: training-finetuning-rl, inference-serving, models-research

Daniel Han (Unsloth) workshop on benchmark reliability, harness and inference-provider accuracy drift, dynamic quantization, torch.compile over handwritten kernels, and reward hacking in RL and coding agents.

- Techniques: Repeated sampling with reliability math; Rolling-average regression canary for a hosted agent; Benchmarks with unbounded instance space and programmatic verifiers; Single controlled harness for model comparisons; Calibration-based dynamic quantization; Per-provider accuracy check before adopting an inference endpoint; Open-weight baseline on llama.cpp or llama-server; torch.compile-first performance tuning with randomized bisection over flags; Audit RL and agent runs for reward hacking
- Tools: Unsloth, Hugging Face, Math-Verify (Hugging Face), llama.cpp / llama-server, PyTorch, torch.compile, Triton, CUDA, FlashAttention (FA2, FA3, FA4 mentioned), Claude Code, OpenAI Codex, Gemini CLI

## ["Software engineering is not about writing code" — Benoit Schillings, Google DeepMind VP of Research](../videos/1P1hJ36rxM0.md)
`1P1hJ36rxM0` · AI Engineer · 2026-07-18 · q3 · intro · review · also: coding-agents, models-research

A Google DeepMind research VP argues code is now nearly free to write, so the bottlenecks move to specification, verification, architecture and open-ended evals, with self-play replacing scarce human code data.

- Techniques: Self-play with verifiable coding challenges; Open-ended scored eval instead of pass/fail; Shift the correctness burden to the language or type system; Decompose before generating; Generate correct code directly instead of detect-and-patch
- Tools: Gemini, Google DeepMind research stack (unnamed), AlphaZero (reference point), Python, Lean (proof assistant, referenced as inspiration), Mythos (model that found vulnerabilities, referenced in news), GitHub (as the source of public code), Pitchfork (internal ML-for-code project started at Google X in 2018)

## [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](../videos/vh2VGuQ3zhY.md)
`vh2VGuQ3zhY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: mcp-and-tools, context-engineering, rag-retrieval

Giving an agent every tool schema on every request breaks accuracy, latency and cost as the catalog grows; the fix is semantic routing that injects only the top-K relevant tools per query.

- Techniques: Semantic tool routing (tool RAG); Just-in-time tool and context injection; K-sweep routing evaluation; Router miss fallbacks; Description writing for retrieval; Routing observability
- Tools: Qdrant, Chroma, Pinecone, Berkeley Function Calling Leaderboard, ToolBench, Anthropic MCP on-demand tool loading write-up, Aurelio Labs semantic-router (open source), MCP0 (cited as an open-source routing project at large scale)

## [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](../videos/Rx8f05JI_WA.md)
`Rx8f05JI_WA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: testing-verification, coding-agents, security-guardrails

Rishi Desai presents SWE-Marathon, 20 project-scale coding tasks where the best agent solves only 26%, and argues that multi-channel, anti-cheat verification is the main bottleneck for long-horizon evals.

- Techniques: Multi-channel verification; Strace-based forbidden-subprocess detection; Hardening loop before publishing a benchmark; Standardize tasks into a Harbor-format environment; Trajectory work-pattern charts
- Tools: SWE-Marathon, Harbor, HumanEval, SWE-bench, Terminal-Bench, Claude Opus 4.8, Claude Code, GPT-5.5 (transcribed as 'gbd 5.5'), Codex, GLM 5.2, Gemini, strace

## [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../videos/HEFSExa0xl0.md)
`HEFSExa0xl0` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: agent-architecture, mcp-and-tools, testing-verification

Witan Labs on lifting coding agents' spreadsheet accuracy from about 50% to 92% by replacing 15 tools with one persistent-state REPL, plus a formula engine and render engine as the verification loop.

- Techniques: Single persistent-state REPL instead of many tools; Verification loop with domain engines; Golden-spreadsheet black-box evaluation; Domain-knowledge reminders in the prompt; Trace review for plumbing bugs
- Tools: Node.js REPL, JavaScript, TypeScript type definitions, C#, LLM-as-judge, Witan Labs internal formula engine, Witan Labs internal render engine

## [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](../videos/2e9ANoOEn28.md)
`2e9ANoOEn28` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, security-guardrails, multi-agent

Aditya Bhargava (Etsy) argues the agent harness, not the model, drives results, especially for weaker models, and walks through building a coding-agent harness step by step in his language Agency.

- Techniques: Tools as plain functions with docstrings; Interrupt plus handler for approvals; Partial function application for capability scoping; ReAct test-feedback loop; Subagents as tools with grouped tool sets; Objective-driven prompt optimization; Serializable pause and resume at interrupts
- Tools: Agency (agencylang.com, TypeScript-like agent language, installed via pnpm), HarnessBench (harness benchmark, 106 tasks), Claude Code (cited as an example agent: Opus model plus harness), Built-in Agency log viewer, Built-in Agency standard library (includes Wikipedia search tool)

## [AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](../videos/T0HhO4YtTfE.md)
`T0HhO4YtTfE` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, product-ux, context-engineering

A MongoDB developer advocate walks through a four-phase framework (product requirements, system design, evaluation and monitoring, cost/latency optimization) using a health insurance claims review system as the worked example.

- Techniques: Four-phase AI system design framework; Quantified solution-agnostic business problem; Three-axis AI role classification; Per-source retrieval strategy from update cadence and content type; Simplest-design-first, evaluate, then iterate; Guardrails as measurable rates; Production signals from human behaviour; Structured outputs as a reliability guard
- Tools: MongoDB, Voyage AI

## [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](../videos/WLXxTaPagA8.md)
`WLXxTaPagA8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, observability, multi-agent

Solo agent builders keep rebuilding CI/CD-style controls (regression tests, alerts, contracts, staging, audit trails) one failure at a time; the talk argues for blocking gates at the most expensive handoff.

- Techniques: Boring blocking gates before save; Guarded vs naive mode demo; Handoff mapping; Per-gate audit record; Voice and domain contracts as explicit rules
- Tools: Claude Code

## [Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon](../videos/LrGCT7G_rU8.md)
`LrGCT7G_rU8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: data-engineering, agent-architecture, security-guardrails

Anna Marie Benzon presents a capstone ETL remediation agent: deterministic rules detect facts, tabular Q-learning picks among six bounded actions, and an external safety layer can force escalation. Results are from synthetic benchmarks.

- Techniques: Event-triggered diagnose-decide-act-verify loop; Rules for facts, learning for choices, guardrails for authority; Tabular Q-learning over a small discrete state; Propose, check, execute, and record separately; Multi-seed evaluation with baselines and confidence intervals
- Tools: AWS Glue, Amazon EventBridge, AWS Lambda, Amazon CloudWatch, AWS Glue Data Catalog, Amazon S3

## [Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](../videos/4uFVSLgD2Q4.md)
`4uFVSLgD2Q4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, enterprise-adoption, sandboxing-execution

OpenGov's Gabe De Mesa on how they built and scaled OG Assist, an in-product agent: an in-house Effect-native agent loop, A2A contracts, approval gates, ephemeral sandboxes, and rolling-summary context.

- Techniques: Effect-native agent loop with injected language model; A2A agent card as the API contract; Deterministic approval interrupt; Automated tool-call evals in CI; Ephemeral sandbox per agent task; Rolling summary with recent-window and recall; Runtime generative UI via registered primitives; Tools to toolkits to model registration
- Tools: Effect, Effect AI, LangGraph, A2A protocol, A2UI, Claude, Cursor, Claude Cloud Agents

## [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../videos/2IxD9OB3XuQ.md)
`2IxD9OB3XuQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: skills-self-improvement, memory, context-engineering

Soheil Feizi (RELAI) argues agents should learn from production failures only through verifiable updates: turn logs into replayable test environments, route fixes to model, harness or memory, and gate each change with regression tests. Second half is a product demo.

- Techniques: Log-to-replayable-environment lift; Instruction-first environment bootstrap; Three-gate fix verification; Layer routing by smallest durable change; Regression-aware optimization; Regression trap in benchmark design; Reviewable change proposal as output
- Tools: RELAI Rely (rely optimize CLI), GEPA, Letta, mem0, LoRA, DPO, GRPO, RLVR, SFT

## [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis](../videos/IQkVMvXQKLY.md)
`IQkVMvXQKLY` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: security-guardrails, training-finetuning-rl

Sachin Kumar (LexisNexis) shows that a backdoored fine-tune can pass behavioral evals, and that a sparse autoencoder trained on base-vs-fine-tune activation deltas finds the trigger with near-zero false alarms.

- Techniques: Diff SAE on activation deltas; Backdoor isolation score per feature; Procedural data with a controlled trigger; Objectively measured backdoor target; Build-gate probe check
- Tools: SmolLM2-360M, sparse autoencoder, LoRA, static analysis

## [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](../videos/pSto5YaNGUo.md)
`pSto5YaNGUo` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: observability, software-factory, agent-architecture

Mutagent's CEO and CTO argue agents should be built and improved in an agentic loop: an offline eval-and-optimize loop plus an online trace-diagnose loop, with a demo of their research-preview evaluator and diagnose agents.

- Techniques: Spec-first agent definition; Eval-driven development as TDD for agents; Binary criteria with calibrated LLM judges; Trajectory-level evaluation; Failure-mode library with code-checkable indicators; Tiered trace sampling; Auto-research style optimization gated by evals; Orchestrator dispatching evaluator and diagnose subagents from a coding harness; Diagnostic report with assumptions block and human decisions
- Tools: Claude Code, Codex, Deep Agents (mentioned as a framework), Hermes (mentioned as a framework), Whisper Flow (speech-to-text for feedback), Tracing platform (auto-caption reads 'length use'; name unclear)

## [How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](../videos/1IdzkRVmWAA.md)
`1IdzkRVmWAA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: rag-retrieval, agent-architecture, training-finetuning-rl

Mixedbread's team on why agents write keyword-soup queries that hurt retrieval, and how a bounded four-tool search harness, trained with SFT then RL, recovers much of the oracle gap.

- Techniques: Tiered search tool set for agents; Bounded parallel search rounds with dedupe; Priming with a corpus preview; Describe-the-need query framing; Oracle-gap diagnosis; SFT then on-policy RL with a mixed reward
- Tools: Mixedbread search, Codex, GPT-5, Gemini 3.5 Flash, grep, BM25

## [Frontier results, on device - RL Nabors, Arize](../videos/fWXJM-J0ZB8.md)
`fWXJM-J0ZB8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: local-ai, inference-serving, context-engineering

Rachel Lee Neighbors shows how to right-size a model: prototype with a frontier model, build a golden eval set, then pick the smallest local model (Llama 3.2 3B) that meets latency and quality targets, closing the gap with prompt changes and deterministic post-processing.

- Techniques: Prototype-big-deploy-small pipeline; Golden dataset with multi-metric eval in Phoenix; Latency budget by percentile; Single-variable prompt ablation; Deterministic post-processing instead of prompt tuning; Auditing the LLM judge; Regression evals in CI
- Tools: Phoenix (Arize), Goose, Gemma 4 E2B, Gemma 3, Llama 3.2 3B, Qwen 2.5 1.5B, Qwen 3 1.7B, Claude Sonnet, Claude Opus, MobileNet, YOLO, MediaPipe

## [Your Agents Need a Save Button - Hamza Tahir, ZenML](../videos/bZISsg7H7DA.md)
`bZISsg7H7DA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, observability

Hamza Tahir (ZenML) argues agents need checkpointed runtime state so production runs can be replayed with what-if changes (model swap, mocked tool), compared across cohorts, and shipped only after cohort-level diffs.

- Techniques: Per-step checkpointing of agent state; Counterfactual replay from a checkpoint; Side-by-side run diffing; Cohort replay with agent-driven analysis; Replay-based ship gate
- Tools: Kitaru, OpenTelemetry, GPT-5 Nano

## [How Autoresearch is changing ML research — Zhengyao Jiang, Weco](../videos/iCj_ATyThvc.md)
`iCj_ATyThvc` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: software-factory, models-research

Weco's Zhengyao Jiang on AIDE, an autoresearch agent whose PRs won OpenAI's ParameterGolf and got reused by others; humans design the eval and code abstraction while the agent executes.

- Techniques: Publish-gated agent output; Strict eval API that separates held-out data; Recombine community ideas with the agent's own changes; Constraint-driven follow-up move
- Tools: AIDE (Weco's autoresearch agent), H100 GPU node, Quantization, Qwen gated attention (paper idea)

## [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](../videos/YZQsWVeN3rE.md)
`YZQsWVeN3rE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: multi-agent, context-engineering, rag-retrieval

Alex Bauer (Upside.tech) on building trust in AI for go-to-market data: manage agents like people, scaffold business context first, use a librarian and a jury-and-judge pattern, and use only tier-two agent harnesses for important work.

- Techniques: Commander's intent prompting; Anchor assets and scaffolding; Citation tracing for verification; Librarian pre-query lookup; Jury and judge; Tiered tool selection
- Tools: Claude, Claude Opus, Slackbot, ChatGPT

## [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](../videos/kZsf_Sfm7RU.md)
`kZsf_Sfm7RU` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: observability, pr-code-review, multi-agent

Shipping an agent is where the real work starts. Raphael Kalandadze shows a post-launch loop: a log-monitor agent opens PRs, a fresh-context review agent critiques them, and a session analyzer scores every conversation for health.

- Techniques: Hourly log-monitor agent that opens PRs; Fresh-context review agent as a PR gate; Session analyzer for health scoring; Computer-use QA agent with a site-specific skill; Meta-harness: connect all context to the monitoring agents
- Tools: Claude Code, Codex, HTML artifacts, log and trajectory store, browser computer-use agent

## [Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo](../videos/CDqzWpwkSls.md)
`CDqzWpwkSls` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: product-ux, governance-compliance

Duolingo shows skilled reviewers accepted half of fake AI cheating flags; guidelines demanding independent evidence raised rejections 21%. Design human-in-the-loop interactions for discernment, not approval.

- Techniques: Calibration test with planted false signals; Reframe the AI output as a preliminary alert; Split compound questions into separate signals; Inline anchored feedback instead of a long essay; Surface assumptions and trade-offs for sign-off in agent plans; Capture the edit diff as the training signal; Log the questions users ask as a trust signal

## [User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](../videos/Jx4ZFEAq6bY.md)
`Jx4ZFEAq6bY` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: memory, rag-retrieval, skills-self-improvement

StarlightSearch's CEO argues agent memory should learn from outcomes: utility-weighted retrieval, reasoning-style memories, and consolidation into skills. Product-pitchy, with self-reported benchmarks.

- Techniques: Utility-weighted memory retrieval; Human failure report as a memory write; Memory as procedure, not fact; Consolidate memories into skills; Runtime learning vs compile-time optimization
- Tools: Reflect (StarlightSearch's memory system), Mem0 (transcribed as 'memzero'), DSPy, ReAct, Pinecone (cited in a post, not used)

## [GLM 5.2 is my new favorite model...](../videos/nODxez6nZEU.md)
`nODxez6nZEU` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: models-research, coding-agents, token-cost-efficiency

Hands-on test of open-weight GLM 5.2 against Kimi K2.7 Code and Claude Opus 4.8 on web design, one-shot apps and cost; strong and cheap per task, but token-hungry, and prompt steering drove most results.

- Techniques: Text prompt via a multimodal model for a text-only target; Section-and-style design brief for a one-shot landing page; Single-prompt full-stack app as a stack-choice and integration probe; Console-error loop as a pass or fail check; Cost per task from token counts and per-million prices; Use a cheaper open model for simpler tasks; Claude Code harness on a non-Anthropic API endpoint
- Tools: GLM 5.2 (Z.ai), GLM 5.1, Kimi K2.7 Code, Kimi K2.6, Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 4.6, Claude Code, Claude (vision, used to write the screenshot-to-prompt), Fable 5, Qwen 3.7, MiniMax M3

## [AI passed every benchmark… then failed at real work](../videos/7s2IIIP47GM.md)
`7s2IIIP47GM` · Kai Explains · 2026-07-02 · q2 · intro · other · also: coding-agents, enterprise-adoption

Opinion piece arguing AI coding tools look strong on benchmarks but fail on open-ended, underspecified real work, and that failures are quiet. Recommends measuring shipped outcomes and keeping humans on costly decisions.

- Techniques: Outcome-based tool evaluation; Human gating by cost of error; Evaluate on your own codebase and problems
- Tools: Claude Code (transcript says "Clawed code"), GitHub Copilot, Gemini CLI, Cursor

## [Humanoid GPT, GitHub for Robotics, Sana Real-Time AI Video Editing and D4rt 4D Scene Model AI News](../videos/EenYAIfx2ME.md)
`EenYAIfx2ME` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, voice-multimodal, local-ai

Weekly AI news roundup (2026-07-02) covering NVIDIA SANA streaming, Holo 3.1, Dots.TTS, D4RT, Tanker, MAMA, QJudger, VibeVoice and Humanoid GPT; nearly all claims are repeated from project pages, not tested.

- Techniques: Hybrid softmax/linear attention diffusion transformer for streaming video; Cycle reverse regularization for temporal consistency; Codebook-free autoregressive TTS with a flow-matching head; Ultra-low frame-rate continuous speech tokenizers for long-form dialogue; Multi-dimension structured LLM-as-judge with human-agreement validation; Contact-aware optimization for close multi-person pose; DAgger distillation from motion experts into a GPT-style controller; Compare quantized formats on your own hardware before choosing one
- Tools: SANA streaming, SANA video, SANA (NVIDIA), Holo 3.1, HoloTab harness, Android World benchmark, DGX Spark, NVIDIA RTX 5090, NVFP4, FP8, GGUF Q4, BF16

## [Grok Imagine Video 1.5, Qwen-VLA, NVIDIA Cosmos3-Nano, MiniMax M3, Bernini AI, Stax & More AI News](../videos/kQh9Hhr_eK0.md)
`kQh9Hhr_eK0` · Kai Explains · 2026-07-02 · q2 · intro · news · also: models-research, token-cost-efficiency, local-ai

Weekly AI news roundup (Jul 2026): Grok Imagine Video 1.5, MiniMax M3 open-weight 1M-context model, NVIDIA Cosmos 3 Nano, Qwen VLA, ByteDance Bernini, plus OCR, diarization, TTS and Google Stacks eval toolkit.

- Techniques: Plan-then-render for unified video generation/editing; Custom eval datasets with custom evaluators (Google Stacks workflow); Tiered upgrade path for diarization
- Tools: MiniMax M3, MiniMax Sparse Attention (MSA), NVIDIA Cosmos 3 Nano, Cosmos 3 Super, Qwen VLA, Grok Imagine Video 1.5 Preview, ByteDance Bernini, TripoSplat, Quai KeyVL2 (30B sparse MoE, 3B active), PaddleOCR 1.6 (ERNIE 4.5 backbone), pyannote Speaker Diarization 3.1, pyannote Community-1

## [This Claude Code Plugin Writes 94% Less Code (ponytail)](../videos/2xuFcmUAQUc.md)
`2xuFcmUAQUc` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: claude-code, token-cost-efficiency, coding-agents

Better Stack tests Ponytail, a Claude Code plugin that applies a YAGNI decision ladder to make agents write less code. Its cost claims come with a caveat, and one A/B test shows fewer lines and lower cost.

- Techniques: YAGNI decision ladder in the agent prompt; Native-first replacement check; Record deferred decisions in a code comment; Benchmark cost next to correctness; Side-by-side A/B of a coding agent with and without a plugin
- Tools: Ponytail (Claude Code plugin; benchmark compares no skill, Caveman, and Ponytail), Claude Code, Caveman, Radix UI (React dialog library, the default-agent choice in the modal example), npm (npm package dialog example), Python server (default-run output, not a named tool)

## [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](../videos/wcUJWP6WpGM.md)
`wcUJWP6WpGM` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: coding-agents, testing-verification, training-finetuning-rl

Ibragim Badertdinov (Nebius) shares lessons from running monthly SWE-rebench evals of coding agents: fresh time-split tasks, verifier quality, infra noise, benchmark cheating, and reporting cost and reliability.

- Techniques: Monthly time-split task collection; Oversample, then filter by running agents; Strip future information from the agent sandbox; Minimal agent with strong infrastructure; Error-class retry policy; Reliability-aware metrics; Reproduce a public benchmark before trusting your own numbers; Eval pipeline reused as training pipeline
- Tools: SWE-rebench, SWE-bench, Terminal-Bench, Claude Code, Codex, Junie, Docker, GitHub Archive, GitHub API

## [Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse](../videos/vNCY9kXXyDQ.md)
`vNCY9kXXyDQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: skills-self-improvement, observability, claude-code

Langfuse's founder explains how they built an installable skill that teaches coding agents to add Langfuse tracing and evals, and what they learned about docs, eval checks and auto-tuning skills.

- Techniques: Skill with progressive disclosure; Agent-facing docs surface; Wrap the API as a CLI and advertise --help; Natural-language checks for skill evals; Auto-research loop on a skill with human review; Timestamped skill copies for staleness
- Tools: Claude Code, Langfuse, OpenAI SDK

## [20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna](../videos/hqHC6Z_lXyo.md)
`hqHC6Z_lXyo` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: models-research, inference-serving

Public leaderboards and manual or metric-based checks mislead model choice; the speaker argues for task-specific, many-sample evals plus Pareto fronts of quality vs latency and cost, where smaller fast models often win.

- Techniques: Pareto front selection; Consensus across leaderboards and per-task boards; Large-sample, condition-matched human evaluation; Metric validation before use; Compression for latency (quantization, pruning, step reduction)
- Tools: Design Arena, LM Arena (now Arena), Artificial Analysis, CLIP score, Pruna open-source compression package

## [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](../videos/zKk7sDMGDEQ.md)
`zKk7sDMGDEQ` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: rag-retrieval, claude-code, coding-agents

Turbopuffer's Kuba Rogut benchmarks semantic code search as an extra tool for Claude Code, using a windowed-grep baseline and file, line and symbol precision and recall on human-labelled context tasks; semantic search helps precision but the gain is smaller than Cursor's because Claude Code does not know when to call it.

- Techniques: Chunk-embed-index semantic code search as a CLI tool; Windowed file reads as a retrieval baseline; Trajectory-level retrieval evaluation; Inline comments as embedding context
- Tools: Turbopuffer, Voyage code-3, Claude Code, Cursor, TurboGrep, tree splitter

## [Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI](../videos/mFLlVpnGpds.md)
`mFLlVpnGpds` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, data-engineering

Pyannote's Hervé Bredin explains why speaker diarization is still unsolved and why merging it with STT word timestamps is hard, with a live DER demo.

- Techniques: DER error breakdown; Benchmark in your own acoustic condition; Exclusive diarization in overlaps; Timestamp-based word-to-speaker alignment; Model-agnostic reconciliation layer
- Tools: pyannote (open-source diarization toolkit), pyannote metrics (DER evaluation), OpenAI Whisper, NVIDIA Parakeet, Hugging Face model hub, pyannoteAI cloud API

## [Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind](../videos/3_gYbhABcAE.md)
`3_gYbhABcAE` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: agent-architecture, mcp-and-tools, context-engineering

Philipp Schmid (Google DeepMind) lists five habits from deterministic software that break when building agents: text as state, handing control to the LLM, errors as inputs, pass-rate evals, and agent-ready tools.

- Techniques: Goal-first dispatcher prompting; Free-text approval with edits; Preferences as natural language in context; Errors as observations; Repeated-run pass-rate evals with judges; Agent-ready tool definitions
- Tools: Gemini API, Gemini

## [Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel](../videos/YYH0DMQr30A.md)
`YYH0DMQr30A` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: training-finetuning-rl, data-engineering

Snorkel's Kobe Crawford argues that task quality is data quality for agentic terminal tasks, and shows that RL on verified high-quality tasks gives about 5x the uplift of low-quality ones.

- Techniques: Containerized task environments with a verification test gate; Accepted vs rejected task comparison; Failure taxonomy for benchmark runs; Controlled RL A/B on task quality; Rubric-based human and LLM-judge calibration; Make tasks verifiable on the back end
- Tools: Harbor Framework, Terminal-Bench, Claude Sonnet 4.5, Codex, GPT-5.2, GPT-5.1

## [Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence](../videos/UQKg0td-Bf4.md)
`UQKg0td-Bf4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: testing-verification, security-guardrails, mcp-and-tools

Steven Willmott (SafeIntelligence) argues agent testing needs an explicit spec of data, rules, terminology, roles and robustness needs, kept separate from the implementation and run in a closed loop.

- Techniques: Six-part agent spec; Spec-driven security testing; Input perturbation sweep; Closed-loop spec iteration (backyard RL); Specs as versioned repo files; Agent cards plus variation envelopes
- Tools: SafeIntelligence platform, A2A agent cards, LangSmith, Vertex AI agents, Braintrust, OpenAPI

## [The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI](../videos/iNkFlCiij0U.md)
`iNkFlCiij0U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: models-research

Snorkel AI's Vincent Chen on what makes agent benchmarks useful: rigorous task quality, distributional coverage, unsaturated difficulty, multi-axis scoring, a clear thesis, and researcher-friendly tooling, plus three axes for the next benchmarks.

- Techniques: Adversarial multi-reviewer task validation; Taxonomy-first task distribution; Separate constraint scoring from task completion; Check for headroom before publishing a benchmark; Build for researcher UX
- Tools: Terminal-Bench, Harbor, HELM, SWE-bench, tau-bench, GPQA, MMLU, ARC-AGI

## [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../videos/KA5kPbdkK2E.md)
`KA5kPbdkK2E` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: skills-self-improvement, observability, vibe-coding-app-building

Benjamin Verbeek (Lovable) on two continuous-learning loops: a self-updating "Stack Overflow" of fixes for stuck users, and an agent "vent" tool that reports platform friction to engineers.

- Techniques: Stuck-session detection with an LLM judge; Clustered, generalised fix knowledge bank; Blank-injection holdout; Tuned agent vent tool; Agent triage of agent feedback; Feedback volume as an incident detector
- Tools: Slack, Framer Motion

## [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](../videos/TNwJ1LMiENk.md)
`TNwJ1LMiENk` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: training-finetuning-rl, mcp-and-tools

Snorkel shows a 4B model, RL-trained on single-table financial tool-use tasks for under $500, beating a 235B model. The gain came from fixing tool discipline, not reasoning.

- Techniques: Behavior-targeted RL with GRPO on a tool environment; Single-table-first training data; Verification pass on generated tasks; Rubric decomposition for diagnosis; Publish the environment as a portable package
- Tools: GRPO, RLM framework (UC Berkeley), FinQA environment (Snorkel), OpenEnv, Prime Intellect, Harbor, GetTableNames / GetTableInfo tools, Qwen3

## [Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind](../videos/Ubwb6NzegyA.md)
`Ubwb6NzegyA` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: testing-verification, models-research

Google DeepMind and Kaggle staff tour their open eval platforms (hackathons, agent exams, Game Arena, community benchmarks) and the problems they hit: saturation, cost, harness variance, and hidden configs.

- Techniques: PvP game benchmark with pairwise rating; Task-of-assertions plus LLM-judge benchmark structure; One-line agent exam; Lock down the harness and config when comparing models
- Tools: Kaggle Benchmarks, Kaggle Game Arena, OpenSpiel, Kaggle simulation platform, LLM model proxy (also available on Colab), Bradley-Terry pairwise rating, Moltbook (transcribed as Motebook), SWE-Bench Pro (cited)

## [How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed](../videos/phchDt63qAA.md)
`phchDt63qAA` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: training-finetuning-rl, product-ux

Zed's Edit Predictions lead explains how Zeta 2, a small fine-tuned next-edit model, was distilled from frontier teachers using opt-in production snapshots, settled-state labels, and multi-sample filtering.

- Techniques: Teacher repair loop; Cache the teacher, vary the formatting; Settled-state labels via idle detection; Multi-sample consensus filter with a distance band; Multi-reference offline eval; Percentage-based live experiment rollout
- Tools: Zed, Zeta 2, Seed Coder, Levenshtein distance, JSONL

## [The maturity phases of running evals — Phil Hetzel, Braintrust](../videos/FB-MLPhL9Ms.md)
`FB-MLPhL9Ms` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: observability, testing-verification

Phil Hetzel (Braintrust) lays out four maturity stages of agent evals, from documented vibe checks to replaying tool-using agents offline with captured system state.

- Techniques: Documented human annotation (thumbs plus justification); Failure-mode extraction from justifications; LLM-as-judge with binary outputs and human-aligned ground truth; Deterministic code scorers for objective failures; Production trace flywheel; Whole-trace evaluation with per-step targeting; Embedding system state in traces and time-versioned queries
- Tools: Braintrust, Cursor, Claude Code, Codex

## [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](../videos/zMiSRliEzv4.md)
`zMiSRliEzv4` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: software-factory, agent-architecture, observability

PostHog's Joshua Snyder describes a pipeline that turns product signals (errors, replays, Slack, experiments) into grouped reports, runs a Claude Agent SDK research agent in sandboxes, and opens PRs that are iterated until green.

- Techniques: Generate queries from a signal, then embed the queries; Safety classifier at the ingestion edge; Weighted report promotion with a threshold; Three-way actionability gate; Snapshot and rehydrate the sandbox for CI and review loops; Distill repeated agent behavior into a one-shot call; Evaluate on production-representative data
- Tools: Claude Agent SDK, Modal, MCP, Linear, Notion, Sentry, git blame, PostHog, feature flags

## [Does GenAI "belong" to data scientists? — Phil Hetzel, Braintrust](../videos/NKwIX3CiRgU.md)
`NKwIX3CiRgU` · AI Engineer · 2026-06-18 · q2 · intro · talk · also: enterprise-adoption, product-ux

Phil Hetzel (Braintrust) argues GenAI agent work should not belong only to data scientists or ML engineers. He says it needs a diverse product team, with domain experts shaping prompts and eval, and data scientists supplying rigorous eval discipline.

- Techniques: Judge calibration against human labels; Production traces feed the offline eval set; Domain-expert trace annotation; Prompt playground for non-engineers; Functional eval over technical metrics
- Tools: Braintrust

## [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../videos/N7b1PJc7SFc.md)
`N7b1PJc7SFc` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: voice-multimodal, infra-cost-scaling, agent-architecture

Together AI's voice AI lead on the cascading STT→LLM→TTS pipeline: per-stage latency budgets, streaming STT, co-locating models to cut network hops, and why speech-to-speech is not yet production-ready.

- Techniques: Cascading voice pipeline with streamed hand-offs; Per-stage latency budget; Streaming STT with lookahead-limited encoders; Co-locate models with the orchestrator; Asymmetric autoscaling for stateful voice; Pre- and post-LLM guardrail and routing stages; Thinker-talker delegation; Tiered tool-call evals; Full-duplex conversation evals
- Tools: Together AI (hosted inference, the speaker's company), Pipecat (agent orchestrator, named as an example), LiveKit (agent orchestrator, named as an example), Whisper (OpenAI speech-to-text, cited as the batch model), NVIDIA streaming speech encoder (named only as a recent NVIDIA model), NVIDIA VoiceChat (speech-to-speech model), OpenAI realtime API (speech-to-speech), ChatGPT advanced voice mode, Claude Code and Cursor (cited as voice-interaction examples)

## [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](../videos/QuuIywMG4s8.md)
`QuuIywMG4s8` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: testing-verification, coding-agents

Ara Khan (Cline) argues most people misuse evals, either trusting vendor leaderboards or dismissing evals for vibes, and shows how to build a Terminal-Bench-style agent eval and hill-climb on it alongside a vibe check.

- Techniques: Failure-trace triage loop; Isolated parallel eval runs; Hill-climb with a vibe check; Sort fixes into three zones; Delayed model adoption; Check the task itself
- Tools: Terminal-Bench, Harbor, SWE-bench Verified, Claude Code, Codex, Daytona, Docker, Modal

## [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](../videos/NuePCNMpWGc.md)
`NuePCNMpWGc` · AI Engineer · 2026-06-18 · q2 · practitioner · talk · also: pr-code-review, coding-agents, testing-verification

Sonar argues that LLM pass rates miss security, maintainability and verbosity. It shows its Java eval of 53+ models and pitches a verify-in-loop and remediation pipeline, so it is product-heavy.

- Techniques: Dual-metric model evaluation; In-loop static analysis via MCP; Regression-gated autofix; One PR per issue for tech debt; Remediation on quality-gate failure
- Tools: SonarQube, SonarQube Agentic Analysis (MCP), Sonar Sweep, Sonar Context Augmentation, Sonar remediation agent, Claude Code, Codex, Gemini CLI, Devin, Cursor, Windsurf, Antigravity

## [LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](../videos/JsCCrBF7F1g.md)
`JsCCrBF7F1g` · AI Engineer · 2026-06-18 · q2 · practitioner · talk · also: observability, agent-architecture

Arize's Dat Ngo argues LLM observability, evals and experiments form one flywheel, built on OpenTelemetry traces, with evals scoped from single spans up to whole sessions. It is mostly a product walkthrough with a useful eval taxonomy.

- Techniques: OTel auto-instrumentation for agents; Session-level state tracking; Distributional trajectory analysis; Eval at the smallest scope that answers the question; Deterministic checks before LLM judges; Calibrate an LLM judge against a golden dataset; Trace-to-dataset-to-experiment loop; Coding-agent access to the eval platform
- Tools: Arize Phoenix, Arize AX, OpenTelemetry, LLM-as-judge, Claude Code, Codex, Anthropic Managed Agents (mentioned)

## [How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust](../videos/XBaznoTRDFI.md)
`XBaznoTRDFI` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: observability, data-engineering

Braintrust's solutions lead argues agent observability differs from uptime-focused tracing: quality, non-determinism, huge text-heavy traces, and domain experts in the loop.

- Techniques: Split quality metrics from technical metrics; Full-text index on traces with SQL access; Trace to offline dataset to experiment; Human grades with justification to LLM judges; Embed and cluster traces to find unknown unknowns
- Tools: Braintrust, Grafana, Datadog, ClickHouse, Tantivy, Apache Lucene, SQL, CLI

## [How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS](../videos/vy7o1g2iHY8.md)
`vy7o1g2iHY8` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: skills-self-improvement, testing-verification, agent-architecture

WorkOS DX engineer on replacing 10k lines of generated agent skills with 553 lines of gotchas, enforcing gates in a state machine, and making agents prove their work with hashes and videos.

- Techniques: Enforced state-machine gates for agent pipelines; Hash-verified test receipts; Gotchas-only skills validated by paired evals; Visual before-and-after proof on PRs; Retrospective agent over run transcripts; Conditional rules instead of doc summaries
- Tools: Pi, Claude Code, Codex, Playwright CLI, TypeScript, SHA-256, WorkOS CLI, AuthKit, TanStack Start, Next.js, GitHub, Linear

## [Rewiring the State — Eoin Mulgrew, No. 10 (Downing Street)](../videos/ObNKGf9YR0g.md)
`ObNKGf9YR0g` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: enterprise-adoption, governance-compliance, product-ux

Eoin Mulgrew of No. 10's data science team describes an outsider "insurgency" unit with forward-deployed engineers that ships small government AI tools in weeks; mostly a recruitment pitch.

- Techniques: Insurgency unit with a mandate; Forward-deployed engineers embedded in workflows; Internal tool instead of outsourced one-off analysis; Policy simulation sandbox; Pre-deployment sycophancy red-teaming and user coaching; Benchmark-based guardrails for classroom AI
- Tools: Gemini, Inspect (AI Safety Institute evaluation tool), Xtract (planning-application digitisation)

## [Why This AI Has No Idea What World War 2 Is](../videos/4EA7vEAkoIw.md)
`4EA7vEAkoIw` · Better Stack · 2026-06-02 · q3 · intro · demo · also: models-research, training-finetuning-rl

Better Stack demo of Talkie, a 13B model trained only on pre-1931 text, used to show how vintage models separate memorization from learning, forecasting, and temporal leakage.

- Techniques: Contamination-controlled capability probe with a date-cutoff model; Surprisal-based forecasting eval; Temporal leakage audit; Period-matched synthetic post-training data with a modern RL judge, plus a style check
- Tools: Talkie (13B vintage language model, pre-1931 training data), Claude Sonnet 4.6 (used as RL judge in post-training), ChatGPT (mentioned as a modern model), Claude (mentioned as a modern model), Gemini (mentioned as a modern model), GPT (2018 OpenAI research, mentioned via a researcher's background), DALL-E (captioned as 'DALI'), Whisper (mentioned via a researcher's background), HumanEval-style Python tests (captioned as 'human eval')

## [ADLC: Claude Code's New Lifecycle for AI Coding](../videos/aMBQB_IJ0dQ.md)
`aMBQB_IJ0dQ` · AI LABS · 2026-06-02 · q2 · intro · other · also: agent-architecture, claude-code, context-engineering

Conceptual walkthrough of the agentic development lifecycle (ADLC), a phase-by-phase SDLC analogue for non-deterministic agents with a validation gate and staged rollout. Thin on code and data, with a sponsor segment.

- Techniques: Behavior-first planning mode; Human-agent responsibility model; Ground-truth dataset plus baselines as a validation gate; Single orchestration layer for multiple agents; Context hygiene against context rot; Staged rollout with behavioral alerting; Feedback signals and periodic data refresh
- Tools: Claude Code (planning mode, agent view), Cursor, Google Calendar MCP, Gmail MCP, Notion MCP, RAGAS, DeepEval, Gemini (1M-token context, mentioned), Claude Opus (1M-token context, mentioned), ChatGPT (feedback UI example, mentioned), Softr (sponsor, transcribed as 'Softer')

## [The BEST AI Tool for Reliable Deterministic Outputs (Interfaze)](../videos/RQYkKpAFZ4c.md)
`RQYkKpAFZ4c` · Better Stack · 2026-06-02 · q2 · intro · review · also: data-engineering, models-research

Hands-on review of Interfaze, a beta model that claims deterministic structured JSON via task-specific encoders; OCR tests on declassified UFO documents show mixed results, and the main claims are vendor-reported.

- Techniques: Dashboard system-prompt builder to code snippet; Guardrail smoke test before tuning; Shape pinning with a sample output; Confidence-colored bounding-box overlay for OCR
- Tools: Interfaze (beta model and dashboard), SOB (Structured Output Benchmark, vendor-published), Gemini 3 Flash (comparison model, vendor-reported), GPT 5.4 Mini (comparison model, vendor-reported), GPT-4 (mentioned as a generalist example), Gemini (mentioned as a generalist example), Host-built HTML bounding-box viewer (not named)

## [How we solved Context Management in Agents — Sally-Ann Delucia](../videos/esY99nYXxR4.md)
`esY99nYXxR4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: context-engineering, memory, multi-agent

Arize's product head explains how their Alex agent escaped a context-growth loop: head/tail truncation with the middle moved to memory, long-session evals, and sub-agents for heavy data search.

- Techniques: Head + tail truncation with middle spill to memory; Reference-by-ID retrieval tool; Long-session eval (seed N turns, test turn N+1); Sub-agent for data-heavy search
- Tools: Alex (Arize's in-product agent), Arize observability platform, Claude Code (referenced, not used by speaker)

## [Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw](../videos/4VhbYlfC7Gs.md)
`4VhbYlfC7Gs` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: agent-architecture, observability

Vincent Koc (Comet, OpenClaw) argues static, hand-written evals don't fit adaptive agents; he proposes intent-based, always-on evals self-curated from traces, with the eval suite treated as living code.

- Techniques: Intent-defined end-state evals; Trace-driven suite self-curation; Always-on eval service; Telemetry-aware harness; Split static and dynamic evals
- Tools: Comet, OpenClaw, Claude, Codex, MCP, Karpathy autoresearch

## [Shipping complex AI applications — Braintrust & Trainline](../videos/ZdheJTfLu-s.md)
`ZdheJTfLu-s` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: observability, agent-architecture

Hands-on Braintrust and Trainline workshop on taking a multi-stage LLM support-triage agent from one prompt to a traced, evaluated, managed and failure-driven production loop.

- Techniques: Staged agent pipeline with a deterministic front end; Nested tracing per user interaction; Golden set from categorized edge cases; Two-tier scoring; Evaluate before swapping models; Failure-to-fix loop; Prompts and scorers as managed, slugged assets
- Tools: Braintrust, OpenAI SDK, OpenAI mini model (speaker says 'mini'), TypeScript, pnpm, make, Node 22, Cursor / Codex (suggested for setup)

## [Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take](../videos/FlzpEGHNVKQ.md)
`FlzpEGHNVKQ` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: context-engineering, mcp-and-tools

How a consumer chess app grounds LLM game commentary in Stockfish and detectors, hits a sub-3s latency target, and closes a feedback loop where a Claude Code agent triages bad comments and opens PRs.

- Techniques: Deterministic analysis then LLM narration; Scenario-based LLM-as-judge regression set; Channel-injected events into a running coding agent; Latency-first model selection for interactive output; Iterative context pruning
- Tools: Stockfish, Maia (human-move prediction model), Gemini 3 Flash, Claude Code, Claude Code Channels, GPT-5 Mini, OpenRouter, Slack, GitHub

## [Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop](../videos/-aM2EDTiaMs.md)
`-aM2EDTiaMs` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: observability, agent-architecture, coding-agents

Raindrop's founders argue production agent monitoring must replace evals as the main safety net, using implicit classifier signals, regex, ship-vs-control experiments, and agent self-diagnostic reports.

- Techniques: Binary issue classifiers as monitoring signals; Regex keyword signals on user messages; Percentage rollout with a control group, judged by signal rates; Self-diagnostic report tool; Natural-language signal definition (deep search); Daily triage agent over signals; Cluster by user intent and track issue rate per cluster; Trajectory search over tool-call sequences
- Tools: Raindrop, OpenTelemetry, Claude Code, Codex, OpenAI API, Sentry, Slack, BigQuery, Snowflake, Statsig

## [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](../videos/pFsfax19yOM.md)
`pFsfax19yOM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: skills-self-improvement, claude-code, context-engineering

Hands-on WorkOS workshop on writing Claude skills: description-based routing, constraints over prose, progressive disclosure, confidence gates, with-and-without-skill evals, and sharing skills.

- Techniques: Description-as-router; Constraints over prescription; Bang-backtick command injection; Progressive disclosure via reference map; Subagent for verbose checks; Confidence-gated clarification; With-and-without-skill eval; Transcript-driven skill refinement; Looped connector poll
- Tools: Claude Code, Codex, Cursor, Pi, OpenClaw, Claude Desktop, Claude Agent SDK, WorkOS CLI, Obsidian, Linear, Slack connector, Remotion

## [Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase](../videos/JT3OzDKrucU.md)
`JT3OzDKrucU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: skills-self-improvement, mcp-and-tools, context-engineering

Pedro Rodrigues (Supabase) on writing a product skill for agents, using a three-condition eval to show skills plus MCP beat MCP alone. Main lesson: agents need guidance, not more context.

- Techniques: Three-condition skill eval; Inline must-not-miss rules; Skill as pointer to live docs; Dev-first schema workflow with a deferred migration; Start minimal and iterate
- Tools: Supabase, Supabase advisor, Braintrust, Claude Code, Codex, Vercel skills package, MCP, SSH, Postgres

## [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](../videos/R7A8rX-09Zw.md)
`R7A8rX-09Zw` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: models-research

Peter Gostev (Arena) argues leaderboard line-go-up hides real gaps; uses a nonsense-question "BullshitBench" and Arena's dissatisfaction-rate data to show progress is uneven by domain and that more reasoning can hurt.

- Techniques: False-premise / nonsense probe with LLM-as-judge; Dissatisfaction rate from pairwise votes; Domain and expertise slicing of real prompts; Compare reasoning effort on the same model
- Tools: BullshitBench, Arena text leaderboard

## [Why building eval platforms is hard — Phil Hetzel, Braintrust](../videos/_fQ7Z_Wfouk.md)
`_fQ7Z_Wfouk` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: observability, data-engineering

Braintrust's Phil Hetzel on why eval platforms are a systems problem: the maturity path from spreadsheets to tracing plus online evals, and why agent traces break ordinary data stacks.

- Techniques: Spreadsheet plus for-loop eval starter; Playground for non-technical experimentation; Failure-mode-driven scoring functions; Online evals on the trace stream; Production-to-offline loop; Topic modeling over traces; Automatic tracing through an AI proxy or gateway
- Tools: Braintrust, Postgres, Neon, DuckDB, Google Sheets

## [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](../videos/WE_Gnowy3uw.md)
`WE_Gnowy3uw` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: skills-self-improvement, coding-agents, multi-agent

Cursor's David Gomes on replacing its git-worktree and best-of-N feature (about 15K lines deleted) with one markdown skill plus subagents, and what was lost in the swap.

- Techniques: Skill as the orchestrator for a stateful workflow; Best-of-N through one subagent per model; Commands instead of skills for server-controlled prompts; Prompt-level containment with system reminders; Two-scorer isolation eval run headlessly; Feeding failure cases into RL training
- Tools: Cursor (2.0 and 3.0), Cursor CLI (headless), Git worktrees, Agent skills, Subagents, Slash commands, Composer (Cursor's own model, version 2 mentioned), Braintrust, Kimi, Grok, GPT, Opus

## [Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft](../videos/iOXM3zE-2dk.md)
`iOXM3zE-2dk` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: observability, security-guardrails, coding-agents

Microsoft Foundry workshop on agent observability: trace-linked evals, stage-wise agent evaluators, OTel tracing, red teaming, and an observe skill that automates the eval-optimize loop with a human stopping regressions.

- Techniques: Trace-linked evaluation; Stage-wise agent evaluators; Bootstrapped eval dataset from instructions; Version-compare regression diff; Bounded auto-optimization with human stop; Adversarial red teaming with an attacker agent; OTel GenAI tracing with custom attributes; Eval gate on model swap
- Tools: Microsoft Foundry, Azure Monitor, Application Insights, OpenTelemetry, GitHub Codespaces, dev containers, GitHub Copilot Chat, Foundry MCP server, Azure AI Toolkit (VS Code extension), LangGraph, KQL, PyRIT (auto-caption reads it as 'pirate')

## [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../videos/XNtkiQJ49Ps.md)
`XNtkiQJ49Ps` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: product-ux, agent-architecture, skills-self-improvement

Legora's CTO argues that vertical agents need more than chat: make work verifiable, let humans steer through skills and decision logs, and use persistent artifacts as the collaboration surface.

- Techniques: Proxy verification with golden examples; Task decomposition by verifiability; Allowlist guardrails for agent actions; Skills as judgment encoded at work nodes; Elicit-or-decide with a decision log; Persistent, scoped artifacts as the collaboration surface
- Tools: Claude Code

## [Context Is the New Code — Patrick Debois, Tessl](../videos/bSG9wUYaHWU.md)
`bSG9wUYaHWU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: context-engineering, skills-self-improvement, security-guardrails

Patrick Debois argues that agent context (instructions, skills, specs) needs its own lifecycle like code: generate, test with evals, distribute as packages, observe logs, then adapt.

- Techniques: Layered context tests (lint, judge, end-to-end); Repeated runs with error budgets; Commit-scoped context A/B scenarios; Turning feedback into context fixes; Context filter before loading; Packaging context with provenance and scanning; Parallel generation as a spec-quality check
- Tools: Claude Code, AGENTS.md, CLAUDE.md, SKILL.md, MCP, Tessl, GitHub, GitLab, Slack, Snyk, Gemini, GitHub Copilot

## [Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML](../videos/X6NShR2ccOg.md)
`X6NShR2ccOg` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: training-finetuning-rl, enterprise-adoption, inference-serving

Adaptive ML's CCO argues RL, not prompting or SFT, is the systematic way to take enterprise LLMs and agents from MVP to production, using environments, rewards, and LLM judges. Mostly a product pitch for their platform.

- Techniques: Mock environment with mock tools and an LLM-played user; Rejection-sampling bootstrap from reward-scored trajectories; Business KPI as the RL reward; LLM judge with human-written rubric, graduated to a reward model; Prefer a smaller RL-trained model for high-volume or latency-bound features
- Tools: Adaptive Engine, PPO, GSPO, Gemma, Mistral, Qwen

## [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase](../videos/GmAQKINjv1E.md)
`GmAQKINjv1E` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: skills-self-improvement, claude-code, context-engineering

Pedro Rodrigues (Supabase) walks through writing agent skills, testing their triggering, and running with/without-skill evals, using a Postgres RLS view bug as the running example.

- Techniques: Progressive-disclosure skill layout; Trigger-accuracy testing via headless CLI; With/without skill eval comparison; Deterministic state assertions before LLM judging; MCP tool plus skill split for data access; security_invoker for Postgres views over RLS tables; Skill install via npm skills package with symlinks
- Tools: Claude Code, Supabase MCP server, Supabase CLI via npx, Postgres, Next.js, Braintrust, Langfuse, Vercel skills npm package, Python (DB reset and eval scripts), VS Code

## [How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs](../videos/kfSDc2eVLo4.md)
`kfSDc2eVLo4` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: enterprise-adoption, product-ux

Chris Lovejoy (Notius Labs) argues winning in vertical AI is an organizational problem, and gives a three-role framework (oracle, evaluator, architect) for placing domain experts, with Granola, Tandem and Anterior as cases.

- Techniques: Oracle role (domain expert edits the product directly); Decentralized oracle; Evaluator role (expert defines metrics; engineers improve); Architect role (self-improving system); Role progression check
- Tools: LLM-as-judge, clinician review dashboard

## [Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic](../videos/A48uhxfxbsM.md)
`A48uhxfxbsM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, observability

Samuel Colvin (Pydantic) live-demos optimizing a structured-output extraction prompt with GEPA against a golden dataset, then serving managed prompt variables from Logfire without redeploying. Main takeaway: deterministic golden-set evals plus automated prompt search help most for cheaper models and private data.

- Techniques: Golden-dataset structured-output eval with a custom deterministic evaluator; Compare-two-runs error analysis; GEPA prompt search with an expert-prompt-engineer proposer; Keyed-component optimization instead of free-form prompt rewrites; Typed managed variables for live prompt and config changes; Trace the optimizer itself; Train/eval split with extra coverage
- Tools: Pydantic AI, Pydantic Logfire, GEPA (called JEPA in captions), DSPy, OpenFeature, Beautiful Soup, FastAPI, Pydantic AI Gateway, uv

## [Fighting AI with AI — Lawrence Jones, Incident](../videos/L2r6vLlLgs8.md)
`L2r6vLlLgs8` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: observability, coding-agents, multi-agent

Lawrence Jones (Incident.io) on using AI tools to debug and improve multi-prompt AI systems: export UI traces and eval suites as file systems for coding agents, then run parallel backtest analysis pipelines.

- Techniques: Eval-tool CLI for agents; Runbook-driven prompt fix; Download trace or interaction as a file tree; Parallel per-item analysis with file-based resume; Cohort clustering over failures; Analysis as a repeatable markdown playbook; Investigate, fix, then verify in one session
- Tools: Claude Code, Codex, Go, YAML

## [Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize](../videos/Xfl50508LZM.md)
`Xfl50508LZM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: observability, agent-architecture

A two-hour Arize Phoenix workshop on evaluating a Claude-powered financial research agent: read traces first, then write code evals, LLM judges, meta-evals and experiments.

- Techniques: Root-span code eval; Faithfulness eval using the research step as context; Classification LLM judge with a binary label; Trace-to-dataset failure loop; Wrap multi-turn agent runs in one parent span; Golden set with a held-out split and reference solutions; Pairwise comparison and reliability metrics; Cost-normalized accuracy and tiered models
- Tools: Arize Phoenix (Phoenix Cloud), OpenInference instrumentation, OpenTelemetry (phoenix.otel register, auto_instrument), Claude Agent SDK, Claude Haiku (agent model), Claude Sonnet (judge model), Phoenix evaluators (correctness, faithfulness, classification), Phoenix datasets and experiments, Arize AX (enterprise product, mentioned)

## [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../videos/mYSRn6PC1mc.md)
`mYSRn6PC1mc` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: agent-architecture, mcp-and-tools, context-engineering

Workshop on building a deep-research agent (MCP server plus Claude Code skills) that feeds a separate LinkedIn writer workflow with evaluator-optimizer review and a calibrated LLM-judge eval loop.

- Techniques: Autonomy-ladder architecture choice; Tools as specialists inside one agent; Delegation to keep context lean; Files as the inter-agent contract; Guideline plus static style profiles; Start with many few-shot examples, then trim; Evaluator-optimizer with fresh context and typed feedback; Synthetic eval inputs, real outputs, binary labels with critiques; Judge calibration with dev/test F1; MCP server exposes tools, prompts and resources; skills wrap prompts for progressive disclosure; Trace-based debugging with threads and traces
- Tools: Claude Code, FastMCP, MCP, Gemini API (grounding, multimodal YouTube), Firecrawl, Perplexity, Opik, Pydantic, git-ingest, uv, Python

## [The 2.3B AI Model that "Thinks" like a 70B (Gemma 4)](../videos/ZxQ2DuejRhU.md)
`ZxQ2DuejRhU` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: local-ai, models-research

Better Stack runs informal local and on-phone tests of Google's Apache 2.0 Gemma 4 E2B and E4B models: fast on iPhone, weak at coding and vision, with Google's benchmark claims left unverified.

- Techniques: Offline local test harness with LM Studio and Cline; Fixed-prompt regression comparison across models; Check model output artifacts for leakage and phantom files; Quick capability probes; Try on a phone with the vendor's app
- Tools: Gemma 4 (E2B, E4B, Google, Apache 2.0), Qwen 3.5 (compared in the speaker's earlier video), LM Studio, Cline (transcribed as 'Klein'), Google AI Edge Gallery app, LiteRT-LM (Google's inference framework), MLX / Swift MLX (no Gemma 4 bindings yet), swift-lm (community project working on unofficial native bindings, as transcribed)

## [Stop Assuming Your AI Agent Can Read the Web (Test It!)](../videos/OlNZCtk100Q.md)
`OlNZCtk100Q` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: testing-verification, voice-multimodal

Walkthrough of the Agent Reading Test, a canary-token benchmark that checks whether an AI agent's web fetch pipeline actually reads a full page, with a 13/20 Kimi 2.5 example.

- Techniques: Canary-token reading audit; Verify agent-reported coverage against the answer key; Checklist of web-fetch failure modes
- Tools: Agent Reading Test (agentreadingtest.com), Claude Code, Kimi 2.5

## [I Tested Every "Top" Coding Agent. Only One Survived Xcode.](../videos/J8-CdK4215Y.md)
`J8-CdK4215Y` · Better Stack · 2026-03-02 · q3 · intro · review · also: coding-agents, models-research

Better Stack gives seven coding agents the same SwiftUI "Dog Tinder" build prompt; Claude Opus 4.6 via Claude Code is the only one that works first try and looks best, while GLM-5 fails badly.

- Techniques: Fixed-spec, first-try app build as a coding-agent eval; Check that the output opens, not just that files exist; Generate an Xcode project from a YAML spec with the codegen CLI; Use Xcode's built-in AI assistant with OpenRouter as the model backend; Give Claude Code only the permissions it needs, then let it run the whole project
- Tools: Swift, SwiftUI, Xcode, Xcode AI assistant (coding intelligence), OpenRouter, Claude Code CLI, Opus 4.6, Gemini CLI, Gemini 3 Pro (preview on CLI), Qwen CLI, Qwen 3 Coder Next, Kimi CLI

## [Qwen 3.5 The FREE AI Model That Claims to Beat Sonnet 4.5](../videos/y8JWZQpWbxQ.md)
`y8JWZQpWbxQ` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: models-research, coding-agents, local-ai

Better Stack runs three coding tasks (todo app, Three.js solar system, tweet-screenshot feature) comparing Qwen 3.5 35B on OpenRouter against Claude Sonnet 4.5, and finds Sonnet ahead on all three; the takeaway is to run your own evals, not trust benchmarks.

- Techniques: Three-tier hands-on model bake-off; Pin the harness before comparing models; Check the project layout, not only whether the app runs; Check whether a fix targets the root cause; Code-structure review of generated components
- Tools: Qwen 3.5 (medium series, 35B; 400B max-thinking variant mentioned), Claude Sonnet 4.5, Claude Opus 4.5 (benchmark comparison only), Claude Code, Claude Cowork (mentioned), OpenCode, OpenCode Go (model list, mentioned), OpenRouter, superpowers skill (OpenCode), React, Vite, Three.js

## [Skills Had ONE Job (They Failed)](../videos/i0W90tlKfYg.md)
`i0W90tlKfYg` · Better Stack · 2026-02-02 · q4 · practitioner · review · also: context-engineering, skills-self-improvement, coding-agents

Vercel's Next.js eval found a passive AGENTS.md doc index beat on-demand skills (100% vs. skills that were often never invoked); skills suit explicit workflows, AGENTS.md suits framework knowledge.

- Techniques: Passive documentation index in AGENTS.md; Split context by trigger type; Measure skill trigger rate, not just existence
- Tools: Next.js, Agent Skills (open standard, Anthropic), Vercel skills CLI and skills repository (named as 'skill CLI' in the transcript), AGENTS.md, CLAUDE.md

## [OpenAI's New Release Is WILD](../videos/75SHVbKCe44.md)
`75SHVbKCe44` · AI LABS · 2026-01-02 · q2 · intro · news · also: models-research, security-guardrails

OpenAI's "confession report" method for reducing model dishonesty, as a short, mostly critical take: the speaker argues it rewards admissions rather than accuracy and only helps identify errors, not prevent them.

- Techniques: Confession report after each response; Classify outcomes on a 2x2 grid (answer correct or wrong x confessed or not)
- Tools: OpenAI models (ChatGPT, unnamed model in the study), Claude (referenced in passing as a reward-hacking example), YouWear (sponsor, AI app builder)

## [Gemini 3 Flash Is Incredible… Until It Isn’t](../videos/YoBiCEXUqmU.md)
`YoBiCEXUqmU` · Better Stack · 2026-01-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency

Better Stack's quick review of Gemini 3 Flash: fast and cheap with strong benchmark scores, but a high hallucination score rules it out for accuracy-sensitive work, and the presenter would not use it for coding.

- Techniques: One-shot build as a speed and cost probe; Cheap model plus correction prompts; Check hallucination separately before using a model for factual answers
- Tools: Gemini 3 Flash, Gemini 3 Pro, Gemini 2.5 Flash, Claude Opus 4.5, Artificial Analysis (Intelligence Index, coding index, knowledge and hallucination benchmark, cost-vs-intelligence chart), SWE-bench Verified, Three.js (transcribed as '3GS')

## [Here's What They Didn't Tell You About Claude's New Model - Opus 4.5](../videos/IZhGvZ4UlPs.md)
`IZhGvZ4UlPs` · AI LABS · 2025-12-02 · q2 · intro · review · also: models-research, coding-agents

A hands-on review of Claude Opus 4.5 covering the launch benchmarks, system-card safety findings, and side-by-side coding tests against Gemini 3 Pro and Sonnet 4.5.

- Techniques: Epics-and-stories spec before building; Identical-prompt cross-tool comparison; Steerability probe via style cue; Functional check beyond visuals; Human-judgment fallback when automated evals saturate
- Tools: Claude Opus 4.5, Claude Sonnet 4.5, Claude Code, Claude desktop app, Cursor, Gemini 3 Pro, GPT-5.1, SWE-bench, tau-squared-bench (tau2-bench), MonkeyType (test-app target, not a tool used), Swift

## [Deepseek R1 vs O1: Here’s Why R1 Crushes It!](../videos/ciLo6YtqvL0.md)
`ciLo6YtqvL0` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research, token-cost-efficiency

A hands-on, anecdotal test of DeepSeek R1 against OpenAI o1 on about ten reasoning and coding prompts. R1 passes 8 of 10 and is pitched as open-weight and cheap, but the verdict rests on single runs.

- Techniques: Mixed reasoning probe battery; Read the visible reasoning trace to locate the failure; Render generated outputs before grading; Distill a reasoning model into small open-base models
- Tools: DeepSeek R1 (open weights, MIT license), DeepSeek R1-Zero (transcript 'R10'), DeepSeek V3 (base model for R1), DeepSeek chat platform with DeepThink toggle, DeepSeek API, Qwen distilled models (1.5B, 7B, others), Llama 3.3 distilled model, OpenAI o1, OpenAI o1-mini, Claude Sonnet, SVG viewer, browser HTML viewer

## [Qwen3 Coder vs Kimi K2 vs Claude Sonnet 4](../videos/nzAT09XolYw.md)
`nzAT09XolYw` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: coding-agents, token-cost-efficiency

Better Stack runs one Next.js blog-generator spec through Qwen3 Coder, Kimi K2 and Claude Sonnet 4 in OpenCode. Qwen was fastest and cheapest, Sonnet built fastest, yet all three hit a YouTube-transcript failure.

- Techniques: Same-repo, same-prompt head-to-head; Spec in a prompt file, not in the chat; Stop-loss on the debug loop; Style-from-samples analysis step; Tiered model assignment by cost
- Tools: OpenCode, Qwen3 Coder, Kimi K2, Claude Sonnet 4, Next.js, bun, OpenRouter, Moonshot console, Gemini CLI (fork basis for Qwen CLI, not used in the test), GPT-4 (named as the extraction model in the Claude build's prompts), YouTube transcript API/library (unnamed), Markdown

## [Gemini 2.0 Tested: Google's New Models Are No Joke!](../videos/XcQhApQVPCY.md)
`XcQhApQVPCY` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: models-research, token-cost-efficiency

AI LABS runs a hands-on test of Gemini 2.0 Flash, Flash-Lite ("Flashlight") and Pro on 10 quick prompts: Flash-Lite is fastest and cheapest, but coding and reasoning results are mixed.

- Techniques: Fixed prompt suite with per-model latency and pass/fail; Run generated code before scoring it; Trick-question check for reasoning; Shortlist with quality-vs-price and speed charts before hands-on tests
- Tools: Gemini 2.0 Flash, Gemini 2.0 Flash-Lite (called 'Flashlight' in the video; name is an auto-caption-based guess), Gemini 2.0 Pro (experimental), Trillium TPU (named as Google's new chip, unverified link to the speed gains), Nvidia GPUs, Artificial Analysis (benchmark charts), o3-mini, GPT-4o, GPT-4 mini, o1, DeepSeek R1, Qwen 2.5 Max (auto-caption 'Quen 2.5 Max')

## [NEW Qwen 2.5 Coder (32B): Insane Coding Power Tested! Is This the Best Free LLM?](../videos/4shPVb4RqGQ.md)
`4shPVb4RqGQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research, local-ai

Informal hands-on test of Qwen 2.5 Coder (32B) against five coding prompts via the hosted demo; it passed three and failed two, and the presenter says to test it yourself before switching from Claude.

- Techniques: Fixed pass/fail prompt set for a quick coder-model smoke test; Trying an open coder model locally with Ollama; Testing in a hosted artifacts sandbox
- Tools: Qwen 2.5 Coder (32B and 7B), Qwen 2.5, Claude 3.5 Sonnet, GPT-4 Omni (GPT-4o), Cursor, Open WebUI, Ollama, Hugging Face (demo space and artifacts), Notion (test list)

## [Qwen 2.5 Max vs DeepSeek R1 – Which One is Better? (Tested)](../videos/6o_VFkOEwsI.md)
`6o_VFkOEwsI` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research

Hands-on, informal test of Alibaba's closed Qwen 2.5 Max chat model on roughly ten prompts reused from a DeepSeek R1 test; verdict: decent, but below DeepSeek V3 and not open source.

- Techniques: Fixed prompt suite reused across models; Render-and-inspect generated artifacts; Ask for a single-file HTML output for testing; Checkable constraint probe
- Tools: Qwen 2.5 Max (Alibaba, closed model, chat and API only), Qwen 2.5 Plus (default model in the Qwen chat), Qwen 2.5 72B, DeepSeek R1 (reasoning model, baseline), DeepSeek V3, DeepSeek Chat (online HTML preview feature), Phi 3, Llama 3.1, GPT-4o, Claude 3.5 Sonnet, Notion (prompt storage), Arena Hard (benchmark)

## [DeepSeek V3: The BEST AI for Coding](../videos/yNPKt4tkeC0.md)
`yNPKt4tkeC0` · Better Stack · 2025-11-02 · q2 · intro · review · also: models-research, token-cost-efficiency

Better Stack overview of DeepSeek V3 as a cheap open-weight coding model: free chat, OpenAI-SDK drop-in use, vendor and independent benchmark rankings, and a Reddit terms-of-service caveat.

- Techniques: Swap an OpenAI SDK app to DeepSeek V3; Price-to-performance check before committing to a model; Cross-check vendor benchmarks against independent leaderboards by task
- Tools: DeepSeek V3, DeepSeek Coder, chat.deepseek.com, OpenAI SDK, GPT-4o, Claude Sonnet, o1, Claude, Llama 3 (405B), MMLU-Pro, GPQA Diamond, MATH-500

## [The GPT-5 Backlash, AI CLI Tools & AI Agent Protocols | Better Stack Podcast Ep 1](../videos/no8ijoB4qxM.md)
`no8ijoB4qxM` · Better Stack · 2025-11-02 · q2 · intro · other · also: coding-agents, claude-code, mcp-and-tools

Better Stack podcast on GPT-5's messy rollout, Claude Code's lead among CLI coding tools, benchmark contamination, and why MCP won while rival agent protocols stalled. Opinion-heavy, little hard data.

- Techniques: Benchmark contamination check; Plan with the strong model, execute with the cheaper one; Turn an existing REST API into an MCP server; Convert web pages to Markdown before sending them to the model; Pair a strong general model with a browser MCP server; Custom Claude Code status line
- Tools: GPT-5, GPT-5 medium, GPT-5 high, OpenAI Codex (Codex CLI), Claude Code, Claude Sonnet, Claude Opus (4.1), Cursor, GitHub Copilot, VS Code, Goose, OpenCode (SST)

## [DeepSeek R1 Lite: Open-Source AI That Might Beat OpenAI O1?](../videos/Kr3zaxX8-g4.md)
`Kr3zaxX8-g4` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research

Hands-on check of DeepSeek R1 Lite Preview's web demo on seven prompts (code, SVG, math, summarizing, pseudocode); six pass, one fails. Anecdotal, with no methodology.

- Techniques: Manual pass/fail test tracker; Run generated artifacts in their real runtime; Repeat a nondeterministic run; Check the reasoning stream against a known answer; Cross-model verification with no ground truth
- Tools: DeepSeek R1 Lite Preview (web demo, deep-think toggle), OpenAI o1-preview (comparison only), Claude 3.5 Sonnet (comparison only), Notion (test tracker), VS Code (running generated Python and HTML), SVG viewer (unnamed), Other LLMs (pseudocode cross-check, unnamed)

## [OpenAI O3-Mini: The Fastest Reasoning Model Yet?](../videos/cdYA5QV8gRY.md)
`cdYA5QV8gRY` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research, coding-agents

Quick anecdotal test of OpenAI's o3-mini and o3-mini-high: the speaker reports correct answers on six reasoning prompts, far faster than o1, plus a Chrome extension built with o3-mini-high.

- Techniques: Latency-first spot check of a reasoning model; Pick the lower reasoning tier when the task is simple; One-shot scaffold for a small browser extension
- Tools: o3-mini, o3-mini-high, o1, ChatGPT, Chrome extension, Cursor, Windsurf

## [MIT just proved how ChatGPT impacts our brains](../videos/y9WkrRhFF0s.md)
`y9WkrRhFF0s` · Better Stack · 2025-11-02 · q2 · intro · other · also: models-research

Better Stack walks through the MIT "Your Brain on ChatGPT" essay study: AI-assisted writers showed weaker brain connectivity, poorer recall and lower ownership, with the effect persisting after the AI was removed. Small, text-only, single-task evidence.

- Techniques: Crossover study with a swap session; Post-task recall probe; Multi-signal output scoring; Deliberate AI use for learning
- Tools: ChatGPT, Google search (search-engine condition), EEG (neural recording used in the study), NLP analysis (used in the study)

## [The HIDDEN Reason GPT‑5 Feels Underwhelming](../videos/RuBXRjqqxZ8.md)
`RuBXRjqqxZ8` · Better Stack · 2025-11-02 · q2 · intro · review · also: models-research

Walks through SWE-bench, Aider Polyglot and LiveCodeBench to show GPT-5's coding scores are not like-for-like, then speculates that its real-time model router explains why it feels underwhelming.

- Techniques: Same-scaffold model comparison; Check the eval metadata before trusting a number; Contamination-aware problem selection; Probe routed systems with simple prompts
- Tools: SWE-bench, SWE-bench Verified, mini-SWE-agent, Aider Polyglot, LiveCodeBench, GPT-5, GPT-5 mini, o3, o3 Pro, o4, Claude 4 Opus, Claude 4 Sonnet

## [OpenAI Announces a Major Breakthrough: AGI is Here (OpenAI o3 Explained)](../videos/AJknN7qzmDU.md)
`AJknN7qzmDU` · AI LABS · 2025-11-02 · q2 · intro · news · also: models-research

Announcement-day explainer on OpenAI o3 and o3-mini: ARC-AGI scores from ARC Prize, plus two live demos of o3-mini writing code and grading itself on GPQA. The "AGI is here" title overstates what the video shows.

- Techniques: Self-written evaluation harness on a public dataset; Prompt-to-code-to-run loop from a local UI; Compare reasoning effort levels on the same benchmark
- Tools: OpenAI o3, OpenAI o3-mini, OpenAI o1 Pro, OpenAI o1-preview, OpenAI o1-mini, GPT-4 Turbo (caption reads 'GPT for Turbo' in the latency comparison), ARC-AGI benchmark, ARC Prize leaderboard, GPQA dataset, Python

## [Grok 3 Tested: Did Elon Musk Actually Succeed This Time?](../videos/E4fML4Lghjw.md)
`E4fML4Lghjw` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research, coding-agents

Hands-on test of xAI's Grok 3 with about 11 quick prompts: strong on word problems and reasoning, failed the constrained haiku and most coding prompts, so the verdict is not for coding tools.

- Techniques: Pass/fail prompt battery for a new model; Letter-constraint instruction test; Copy-paste code check for generated apps
- Tools: Grok 3 (xAI), Grok 3 reasoning mode ('Big Brain'), Grok Deep Search agent, LM Arena (called 'chat arena' in the transcript), Artificial Analysis leaderboard, OpenAI o3 (upcoming, per the host), OpenAI o3-mini, DeepSeek R1, GPT-4o, Claude 3.5 (image and SVG comparison), Cursor, Windsurf

## [OpenAI's NEXT BIG LEAP in AI Reasoning](../videos/sFn8D9DutIw.md)
`sFn8D9DutIw` · AI LABS · 2024-11-02 · q2 · intro · news · also: models-research

Short AI LABS news explainer on OpenAI's o1 preview: slower, chain-of-thought reasoning, vendor benchmark claims, and three single-prompt demos (strawberry letter count, math, murder mystery) cross-checked with Claude.

- Techniques: Side-by-side prompt comparison; Cross-model verification
- Tools: OpenAI o1 (o1-preview), GPT-4.0 (as spoken in the transcript), ChatGPT Plus, Claude

