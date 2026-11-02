# training-finetuning-rl — 94 videos

*fine-tuning, RL / RLVR, post-training, small/open models, distillation*

By channel: AI Engineer 79 · Kai Explains 6 · Better Stack 9

**Synthesized guide:** [guides/training-finetuning-rl.md](../guides/training-finetuning-rl.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [What Really Happens Inside ChatGPT (AI Explained)](../videos/ZTmZOdB5o0U.md)
`ZTmZOdB5o0U` · Better Stack · 2026-10-12 · q3 · intro · other · also: models-research, rag-retrieval, mcp-and-tools

An eight-minute beginner tour of LLM internals (tokens, weights, transformers, training, LoRA, quantization, RAG, tool calling, MCP, agent loops) with no product pitch, pitched at newcomers rather than builders.

- Techniques: Stateless chat memory via replay; Tool-calling loop; Agent loop with task handoff; Retrieval-augmented generation (RAG); LoRA fine-tuning; Weight quantization for local models; Reinforcement learning with a programmatic checker
- Tools: ChatGPT, GitHub, Slack, Better Stack, Model Context Protocol (MCP)

## [Stop Renting Intelligence: The Train-to-Deploy Loop for Specialized AI — Fireworks AI](../videos/13YZ1EB9hjU.md)
`13YZ1EB9hjU` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: inference-serving, product-ux

Fireworks AI talk on the train-to-deploy loop: moving from closed models to open-source models by fine-tuning (SFT, RFT, DPO) on the same platform used for hosting, with hot-loading and a training agent. Mostly a product pitch, with a few usable workflow ideas.

- Techniques: Continuous train-deploy-monitor-retrain loop; RFT with a vendor-built evaluator function; Training agent with plan approval gate; Draft model training for speculative decoding; Clone-and-compare training runs
- Tools: Fireworks AI platform, FireAttention, Weights & Biases, Qwen3 8B

## [Teaching Agents to Search with NVIDIA Data Designer — Dhruv Nathawani, NVIDIA](../videos/qFaKvbVc5cE.md)
`qFaKvbVc5cE` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: data-engineering, rag-retrieval, evals

NVIDIA workshop on NVIDIA Data Designer: build column-by-column synthetic data pipelines, seed them with Wikidata random walks and Tavily search traces, and use them to teach a model web search (BrowseComp 0 to about 30%).

- Techniques: Column-by-column DAG for synthetic data; Seeded random walks over a knowledge graph; Teacher trajectories with a tool, then SFT on the trajectories; Overproduce and filter funnel; Layered verification of synthetic labels; Skip the golden answer and use a reward function (RL path); Persona seeds from census marginals
- Tools: NVIDIA Data Designer, Nemo Curator, Nemo Gym, Nemo Anonymizer, Nemo Safe Synthesizer, Tavily, MCP, vLLM, gpt-oss-120b, Wikidata, Hugging Face

## [From 15% to 90% GPU Utilization: Fix the Data Pipeline, Not the Model](../videos/tNAV259UhCM.md)
`tNAV259UhCM` · AI Engineer · 2026-10-10 · q4 · practitioner · talk · also: data-engineering, infra-cost-scaling

Fixing a multimodal SFT data pipeline on Ray (concurrency, prefetch, zero-copy, scheduling) took GPU utilization from 15% to about 90%. The lesson: profile the data path, not the model.

- Techniques: Wait time ratio as the pipeline health metric; Async IO for object-store fetches, process pool for CPU preprocessing; Background prefetch queue; Pass object references instead of data; Spread scheduling and zero-copy retrieval at scale; Scaling-ladder ablation
- Tools: Ray, Ray actors, Ray object store, Megatron, Qwen3-VL (auto-caption reads as "QN3VL"), PIL, NumPy, Hugging Face Transformers tokenizers, pandas, S3, JSONL, asyncio

## [Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI](../videos/TyPpSRXGhbc.md)
`TyPpSRXGhbc` · AI Engineer · 2026-10-10 · q4 · practitioner · talk · also: evals, data-engineering

Snorkel AI and UC Berkeley Sky lab trained a 4B Qwen3 agent with RL for under $500 that beats its 235B variant on finance QA; simple binary rewards and single-table curricula won.

- Techniques: Multi-stage synthetic eval and training data pipeline; Company-level data split to prevent leakage; Binary reward with reference-based LLM judge; Single-table-first data mixture; Decorator-based RL wrapper for existing agents; Large concurrent rollout generation
- Tools: RLLM, GRPO, Qwen3 4B and 235B, GPT-5 nano (judge), FinQA benchmark, BFCL, EDGAR, H100

## [Your LLM Judge Is a Confident Liar: Building Better Verifiers — Browserbase](../videos/xLxhT2ZI7UM.md)
`xLxhT2ZI7UM` · AI Engineer · 2026-10-06 · q4 · practitioner · talk · also: evals, testing-verification, voice-multimodal

Browserbase and Microsoft researchers on why LLM judges confidently mis-grade web agents, and their rubric-and-evidence "universal verifier" that agrees with humans far better, plus its use for filtering training data.

- Techniques: Rubric-first LLM verification; Per-criterion top-K screenshot evidence; Dual verdict: partial-credit score plus boolean outcome; Controllable vs uncontrollable failure schema; Error isolation across dependent criteria; Human-agreement validation with held-out labels; Verifier as data filter for SFT; Auto-research loop to build a verifier, primed with human findings
- Tools: WebVoyager, Online Mind2Web (captioned as 'Online Minor Web'), OSWorld, GPT-4o, Opus 4.6, Cohen's kappa, Browserbase, Microsoft open-source web-agent framework (captioned 'StateGen')

## [I Gave a Robot Duck a 15MB AI Brain (Needle 3)](../videos/KQcQ7P78eTI.md)
`KQcQ7P78eTI` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: local-ai, mcp-and-tools, evals

Walkthrough of Cactus Compute's Needle 3 on-device tool-calling model: a size-adjustable layer ladder, local fine-tuning on a robot-duck task, and a 49-prompt held-out eval (27% base, 84% fine-tuned 20-layer).

- Techniques: Closed-set tool dispatcher; Layer-truncatable model (intelligence ladder); Rule-categorised synthetic training data; Hand-written held-out scoreboard; Split controller from the LLM decision layer; Local fine-tune over LAN to a GPU box
- Tools: Needle 3, Needle 2, Cactus Compute fine-tuning platform, OpenDuck Mini, MuJoCo, DeepSeek V4 Flash, NVIDIA RTX 5090, ESP32, Pebble Index Ring, BDX droids (Disney)

## [GLM-5.2: Open Weights, Near-Frontier Intelligence — Zixuan Li, Z.ai](../videos/9JFGohx4E7U.md)
`9JFGohx4E7U` · AI Engineer · 2026-10-04 · q2 · intro · keynote · also: models-research, coding-agents

Z.ai's Zixuan Li introduces GLM 5.2, an open-weight model he says is near frontier on coding and agentic tasks, and explains why Z.ai opens its weights, plus its Zcode harness.

- Techniques: Open-weight release for on-premise deployment; Vertical fine-tuning on an open base model; Tiered thinking budget; Own harness with bring-your-own-key and compaction
- Tools: GLM-5.2, Zcode, Hugging Face, Codex, Claude Code, OpenCode, Terminal Bench 2.1, Artificial Analysis Intelligence Index

## [Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI](../videos/FQwTqUmcbRg.md)
`FQwTqUmcbRg` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: data-engineering, infra-cost-scaling, inference-serving

Datology's CTO on running trillion-token synthetic pretraining data jobs: rephrase seeded documents, batch S3 metadata calls, checkpoint for GPU failures, schedule CPU and GPU pools atomically, and sweep vLLM flags.

- Techniques: Seed-based document rephrasing for synthetic pretraining data; Batched S3 metadata listing at maximum page size; Right-sized partitions with checkpointing and idempotent retries; Atomic CPU and GPU scheduling with dedicated pools; Grid search over vLLM and SGLang serving parameters for batch inference; One workflow for research and product in the same infrastructure
- Tools: Ray, KubeRay, vLLM, SGLang, Apache Spark, Kubernetes, Amazon EKS on HyperPod, Slurm, Amazon S3, Parquet, Beyond Web (DatologyAI synthetic data recipe), Nemotron Synth

## [GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe](../videos/bRGyYaE0lxI.md)
`bRGyYaE0lxI` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: infra-cost-scaling, inference-serving

Crusoe engineers explain how they run Slurm on Kubernetes so failed GPU nodes are cordoned, replaced and the training job resumes from checkpoint with no user action, with a live demo.

- Techniques: Automated GPU failure remediation loop; Opt-out label check before node replacement; Checkpoint on SIGTERM grace window; Slurm operator on Kubernetes (Slinky pattern); Shared GPU pool across training and inference
- Tools: Slurm, Kubernetes, Slinky (SchedMD), sbatch, srun, PyTorch, Crusoe Managed Kubernetes (CMK), Crusoe AutoClusters, Crusoe Slurm operator

## [Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava](../videos/qflLT3SoVbw.md)
`qflLT3SoVbw` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: context-engineering, rag-retrieval, memory

Anant Srivastava argues enterprise teams should decide deliberately whether knowledge lives in the prompt, in retrieval/memory, or in fine-tuned weights, using rate of change, scope, and behavior-vs-facts as the test.

- Techniques: Knowledge placement diagnostic; Retrieval-first debugging; Fine-tune the stable center, keep humans on the edge; Code-aware chunking with denormalized metadata; Promote-and-prune memory loop; Small fine-tuned model for cost

## [This Tiny AI Never Stops Learning (mini-AGI)](../videos/L-6O7R71CCg.md)
`L-6O7R71CCg` · Better Stack · 2026-10-02 · q2 · intro · review · also: local-ai, models-research

Better Stack walkthrough of "Mini-AGI," a toy mixture-of-experts model trained from zero on a MacBook to keep learning continuously; the author's retention and forgetting claims are single-run anecdotes.

- Techniques: Ordered streaming training with a small step per chunk; Expert-per-file paging for models larger than VRAM; Two-speed learning rates to limit forgetting; Held-out script as a memorization detector; Fixed probe prompt during training; Pause and resume across sessions
- Tools: Mini-AGI (toy continual-learning mixture-of-experts model; repo tested only on Nvidia GPUs; weights not yet released, per the speaker), TinyStories dataset (short children's stories), Screenplay corpus: Pulp Fiction, Jackie Brown, Inglourious Bastards, Django Unchained, Four Rooms, Kill Bill, Reservoir Dogs (held out), Apple M2 Max MacBook Pro, 32 GB RAM, Author's custom screenplay chat web app (not named)

## [Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta](../videos/jNE8No-wvok.md)
`jNE8No-wvok` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: multi-agent, voice-multimodal, evals

Meta's Aditya Gautam on using a multi-agent system of small domain-tuned VLMs to find intra-video policy anomalies and duplicate content in short-form video, with a production judge-and-human feedback loop.

- Techniques: Orchestrator plus specialist agents for video review; Change-based frame compression; Per-signal index routing; Domain pre-training plus schema-constrained instruction tuning; Judge-plus-human-queue production loop; Distillation plus quantization sweep; Node-level evaluation suite; Pre-inference gating with cache and metadata
- Tools: CLIP, MCP, Ray, DPO, JSON schema, vector database, graph database, inverted index

## [World Models Need Causality, Not Pretty Pixels — Christopher Manning, Moonlake AI](../videos/4Gqg0HVe-AY.md)
`4Gqg0HVe-AY` · AI Engineer · 2026-09-27 · q3 · intro · talk · also: voice-multimodal, models-research

Christopher Manning of Moonlake AI argues that world models for physical AI need abstracted, causal, editable representations rather than beautiful pixels, and proposes code-based neurosymbolic simulators that can be verified and used for sim-to-real transfer.

- Techniques: Action-conditioned semantic world model; Code as the controllable scene representation; Render-compare-revise loop; Retrieval to fill unobserved state; Task-driven fidelity budgeting; Neural sim-to-real gap reduction
- Tools: Genie 3, Marble, JEPA, Claude, physics engines, diffusion models, RAG over web search

## [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](../videos/OA-Mc60Rboo.md)
`OA-Mc60Rboo` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: skills-self-improvement, evals, context-engineering

GEPA's Lakshya Agrawal explains reflective, text-space optimization: LLMs read full rollout traces and rewrite prompts, skills or harness code, with a Pareto pool, beating GRPO on sample efficiency.

- Techniques: Reflective prompt / artifact optimization loop; Pareto candidate pool selection; Actionable side information from the evaluator; Three optimization modes in one API; Optimize the agent file itself; Repo skill learning from trajectories; Judge-then-agent data flywheel
- Tools: GEPA (open-source, includes the optimize_anything API and a skill-learning feature), GRPO (used as the RL baseline), Claude Opus, Claude Sonnet 4.5, GPT-5 mini, GPT-4.1, GPT-4.1 nano, Gemini Flash, mini-SWE-agent, Claude Code, Codex, LLM-as-judge

## [Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face](../videos/dKcTBQzR7jI.md)
`dKcTBQzR7jI` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: voice-multimodal, data-engineering, evals

Merve Noyan (Hugging Face) argues against running VLMs for real-time vision and shows a pipeline where VLMs label and judge data to train small Apache-2.0 detectors such as RF-DETR, plus a toolkit of models exposed as agent tools.

- Techniques: VLM as offline labeler, small detector at runtime; Overlay-and-ask judging; Ensemble of small judges with any-yes merge; License-first model selection; Agent with domain rules and human checkpoints; Models exposed as agent tools
- Tools: RF-DETR, Gemma 4 E4B, LFM2.5-VL, Qwen VLM (auto-caption reads 'Q1 3.5', ~3.5B), Falcon Perception, Moondream 3, MM Grounding DINO, SAM 3.1, Supervision (Roboflow), Hugging Face Jobs, Hugging Face Inference Providers, Hugging Face buckets

## [From VLM/VLA's to Embodied Agents — Armen Aghajanyan, Perceptron AI](../videos/ZZcE0HeO-Hc.md)
`ZZcE0HeO-Hc` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: voice-multimodal, models-research

Perceptron's CEO argues VLMs, VLAs and world models should merge into one "embodied foundation model," and shares sparsity, token-routing and data-mix findings with public benchmarks but few hard details.

- Techniques: Data-sparse MoE token routing; Agentic detection with zoom, tiling and contrast; Orchestrator plus low-level control policy; Self-verifying video annotation; Online augmentation for robustness; Patch averaging for token compression
- Tools: Gemini 3.1 Pro, Gemini Embodied Reasoning, Perceptron models (Mark 1)

## [Teaching LLMs to Speak Spotify — Yves Raimond & Jacqueline Wood, Spotify](../videos/2LRIAfng7eA.md)
`2LRIAfng7eA` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: evals, product-ux

Spotify's engineers explain turning recommendations into a steerable LLM: semantic-ID tokens, a four-stage NEO training recipe, and LLM judges grounded in behavioral data.

- Techniques: Semantic-ID tokenization and vocabulary extension; Frozen-backbone domain grounding; Staged training: grounding, then multi-task instruction tuning, then optional RL; Beam search over constrained decoding for ID generation; Grounding LLM judges with user profiles and behavioral signals; LLM judges for Cranfield-style relevance pools
- Tools: Qwen, LLaMA, LoRA, NEO (Spotify's training paradigm, linked paper), Discover Weekly, Spotify DJ

## [An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases](../videos/hd7TOvmyAxU.md)
`hd7TOvmyAxU` · AI Engineer · 2026-09-27 · q2 · practitioner · demo · also: evals, observability, agent-architecture

Live demo of W&B's ARIA research agent running autoresearch experiments, plus its trace-to-eval loop: production traces, LLM judges, nightly YAML task suites, and promotion gated on eval scores.

- Techniques: Eval suite as YAML unit tests; Production traces to tasks loop; Live LLM judges as signal detectors; Eval-gated promotion; Async job dispatch from an agent; Agent analyzes its own traces
- Tools: Weights & Biases Weave, W&B Launch, W&B Inference, W&B Artifacts, W&B Reports, CoreWeave sandbox, Kubernetes, iOS app

## [Robotics Has Been Stuck for 70 Years — Deepak Pathak, Skild AI](../videos/jFHteJjRl8A.md)
`jFHteJjRl8A` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: voice-multimodal, models-research, data-engineering

Deepak Pathak (Skild AI) argues robotics lacks internet-scale data, so the answer is one omnibodied brain pretrained on diverse data, post-trained on teleop, and improved by a deployment data flywheel.

- Techniques: Pretrain on diverse, scalable data, post-train on small high-quality teleop; Deployment data flywheel; End-to-end camera-to-motor policy with only a low-level PID loop; Learn from human video, then adapt with minimal robot data; Cross-embodiment zero-shot transfer

## [Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics](../videos/Sjfz1TqxzEs.md)
`Sjfz1TqxzEs` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: evals, voice-multimodal

Dyna Robotics co-founder on making generalist robot manipulation policies reliable enough for commercial use, via reward-model progress scoring and a targeted active-learning loop.

- Techniques: Reward model as progress scorer for background supervision; Failure-driven active learning loop; Pre-train, post-train, then active learn; Grade-based success criteria tied to customer acceptance; Two-level architecture

## [From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam](../videos/T72nqdC92PM.md)
`T72nqdC92PM` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: data-engineering, models-research, voice-multimodal

Sarvam's Krishna Prasad Srinivasan on training Servam Vision, a 3B state-space document-OCR model built from scratch for English and 22 Indian languages, using block-level OCR, a four-stage curriculum and RL with machine-checkable rewards.

- Techniques: Block-level OCR with layout and reading-order modules; Four-stage training curriculum for a domain VLM; RLVR with unit-test rewards; Real complex documents as RL reward sources, synthetic documents for SFT; Human-in-the-loop workbench with confidence scores and block grounding
- Tools: Servam Vision, Akshar (agentic document workbench), OlmOCR-Bench, OmniDocBench, Qwen, Gemma

## [Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer](../videos/btxG75rNJC4.md)
`btxG75rNJC4` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: inference-serving, observability

Two AI21 engineers walk through two silent vLLM bugs for hybrid Mamba models, one a scheduler ordering error and one a 32-bit index overflow, and the debugging method that found them.

- Techniques: Logprob comparison against a reference forward pass; Reproduce under pressure with determinism; Thread identity through the forward context; Bisect by forcing one code path; Check whether a fix is causal and watch for overflow
- Tools: vLLM, Hugging Face Transformers, NVIDIA compute-sanitizer, FSDP, Jamba (hybrid Mamba plus attention model)

## [What's New in Inference Engineering — Philip Kiely, Baseten](../videos/75ckHC2LU_0.md)
`75ckHC2LU_0` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: inference-serving, models-research

Philip Kiely (Baseten) updates his inference book with post-February 2026 developments: why TurboQuant lost on data-center throughput, learned KV compaction, DFlash diffusion-style drafting, and continuous speculator retraining.

- Techniques: Continuous speculator retraining; DFlash block drafting; Learned KV compaction (Still); Stay on NVFP4 weight quantization for production; Local-first versus data-center-first sequencing
- Tools: vLLM, NVIDIA Dynamo, NIXL (transcribed as 'Nickel'), EAGLE-3, DFlash, DSpark, Medusa, TurboQuant, NVFP4, Still (Base10 KV compaction), attention matching, cartridges

## [Large clusters for small models — Daniel Svonava, Superlinked](../videos/g4SsanB0gMc.md)
`g4SsanB0gMc` · AI Engineer · 2026-09-20 · q4 · practitioner · talk · also: inference-serving, local-ai, infra-cost-scaling

Daniel Svonava (Superlinked) on serving fleets of small open models on your own GPUs: why top-down routers fail for many small requests, and how a centralized pull-based queue, a thin Rust gateway and a runtime sidecar fix it.

- Techniques: Centralized pull-based batching queue; Thin gateway with annotation, not full parsing; Runtime sidecar behind a socket; Knee-based benchmarking; Pin plus lazy-load model placement; Per-task model selection with evals, then cheap adaptation; Autoresearch loop for serving tuning
- Tools: vLLM, SGLang, PyTorch, Candle, NATS JetStream, MessagePack, Rust, AWS Bedrock, LoRA, Hugging Face

## [Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End](../videos/4loPnxvWWhg.md)
`4loPnxvWWhg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: context-engineering, evals, enterprise-adoption

A LeaseEnd data scientist explains how fine-tuning an intent classifier for customer texts became costly tech debt, and how replacing it with editable skills and prompts on a frontier model cut fix time from a week to under an hour.

- Techniques: Skill and prompt edits as the default fix; Curated production regression set as the gate; Markdown-file deploys to object storage; Triage gate before retraining; Fine-tuning pre-check list; LLM-judge labeling with manual review and holdout sets
- Tools: Claude Code, Amazon S3, OpenAI, Anthropic

## [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../videos/mMNkdYnIVC4.md)
`mMNkdYnIVC4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: agent-architecture, evals, multi-agent

James Zou (Together AI, Stanford) argues agents should be given designed environments with verifiers, incentives and shared infrastructure instead of fixed workflows, citing Einstein Arena results and the DSGym data-science benchmark.

- Techniques: Verifier-first problem curation; Agent-native onboarding; Persona-differentiated agents; Shortcut audit before trusting a benchmark; Execution-verified trajectory generation
- Tools: Docker

## [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../videos/-tviRdpmHvs.md)
`-tviRdpmHvs` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: models-research, data-engineering

Krea's Sangwoo Lee on training the Krea 2 image model: data curation for stylistic diversity, cascaded dedup and classifier filters, and an LLM-style post-training pipeline with RL.

- Techniques: Cascaded dedup; VLM-judge distillation into a small classifier; SAE feature tagging for data hygiene; Two-pass captioning with OCR; Concept coverage via external importance ranking; Progressive resolution pretraining; Prompt expansion model
- Tools: Krea 2, pHash, MD5, SSCD, SigLIP, CLIP, sparse autoencoder, GRPO, OCR, VLM

## [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../videos/u6q-byPWUuo.md)
`u6q-byPWUuo` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, inference-serving, enterprise-adoption

Abridge's engineering lead on running clinical AI at scale: clinician-written rubrics feed LLM judges, staged rollouts, and small post-trained models gated by cheap triggers to balance quality, latency and cost.

- Techniques: Multi-reviewer rubric construction for LLM judges; Staged rollout with online feedback for AI features; Task decomposition into small specialised models; Gate cascade for real-time event triggers

## [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](../videos/byn9PURoBNY.md)
`byn9PURoBNY` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: infra-cost-scaling, inference-serving

Krea's infra engineer on training the from-scratch Krea 2 diffusion transformer at scale: which metrics matter, why to let crashing runs restart, frequent checkpoints, and bursting training and inference across clusters and rented GPUs.

- Techniques: Let crashing jobs restart instead of debugging each crash; Hard GPU health gate on temperature; Checkpoint every 20 to 30 minutes to a high-throughput file system; Two-tier priority queue in front of Kubernetes; Overflow to external GPUs with a virtual node
- Tools: Kubernetes, Virtual Kubelet, Kubernetes descheduler, Kubernetes taints and tolerations, Queue system (captioned as 'Q') for gang scheduling, Prometheus, NVIDIA DCGM, Weka (parallel file system), Ceph, InfiniBand, NVLink, Hugging Face

## [Where RL Will Take Search — Maximilian-David Rumpf, SID.ai](../videos/iJVxxxHM_Oc.md)
`iJVxxxHM_Oc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: rag-retrieval, multi-agent, context-engineering

Founder of SID.ai argues search should move from fixed retrieval pipelines to one RL-trained model, reporting about 20x faster and 100x cheaper than frontier-model search agents.

- Techniques: Search as a delegated RL-trained sub-agent; Verifiable retrieval reward for RL; Mixed reward with latency; Learned loop in place of a fixed pipeline; Parallel sub-agent searches
- Tools: BM25, PageRank, vector search, rerankers

## [Did This Open Source Model Just Fix AI Reasoning? (ThinkingCap)](../videos/byfjZvrYRH0.md)
`byfjZvrYRH0` · Better Stack · 2026-09-02 · q2 · intro · review · also: token-cost-efficiency, local-ai

Better Stack tests ThinkingCap, a Qwen3.6-27B fine-tune trained to reason less: about 46% fewer thinking tokens with flat accuracy by vendor numbers, backed by one RTX 5090 demo.

- Techniques: Efficiency-aware reward during fine-tuning; Separate reasoning and answer token counts; Single-answer A/B probe on fixed hardware
- Tools: Qwen3.6-27B (27B parameters, quantized, base for ThinkingCap), ThinkingCap (fine-tune of Qwen3.6-27B), Step 3.5 Flash (reasoning model used as the overthinking example), GPT-3, GPT-3.5, GPT-4, OpenAI thinking model (Sept 2024, unnamed in transcript), DeepSeek R1, NVIDIA RTX 5090 (64 GB RAM test machine), GSM8K benchmark, Hugging Face (model distribution, Apache 2.0)

## [DeepSeek Did What Other Labs Won’t Even Try](../videos/7C0DDDec3A8.md)
`7C0DDDec3A8` · Kai Explains · 2026-09-02 · q4 · practitioner · news · also: models-research, inference-serving, token-cost-efficiency

Explainer on DeepSeek V4: how two new compressed attention mechanisms (CSA and HCA) cut long-context KV cache and compute, why that makes $0.435 per million input tokens possible, and what the 58-page report implies for other labs.

- Techniques: Learned KV compression over fixed token blocks (CSA); Heavy block compression with dense attention for global context (HCA); Three-timescale memory layout; Specialist post-training then distillation; FP4 quantization-aware training on MoE experts; Spend thinking tokens as a default when inference is cheap
- Tools: DeepSeek V4 Pro (1.6T total / 49B active), DeepSeek V4 Flash (284B total / 13B active), DeepSeek V3.2, Kimi K3 (2.8T, July 2026), Kimi K2.6, GLM 5.1, Claude Opus 5, GPT 5.4, GPT 5.2, Gemini 3.1 Pro, Gemini 3.0 Pro, Muon optimizer

## [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../videos/maRzp4kImJ4.md)
`maRzp4kImJ4` · AI Engineer · 2026-08-18 · q4 · deep · talk · also: inference-serving, infra-cost-scaling

Nan Jiang (Modal) argues RL rollouts can run on scattered, elastic GPUs across regions if the trainer syncs only a bit-exact sparse diff of serving-precision weights instead of full checkpoints.

- Techniques: Decoupled rollout islands; Bit-exact sparse weight diff; Versioned request contract; Sidecar version gate; Floor-based update-visibility check
- Tools: Modal, SGLang, vLLM, Adam, BF16, FP8, NVFP4, RDMA, Stitch

## [Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning](../videos/2bvtay8wGYI.md)
`2bvtay8wGYI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: context-engineering, agent-architecture, evals

GR's Ross and Chengxi Taylor trace RL-for-reasoning from Galactica and 2022 PPO recipes to long-horizon agents: value models, compaction, pipeline RL, and a benchmark where frontier models lost money.

- Techniques: Value-model (critic) RL for long, variable-length trajectories; RL-trained compaction; File-system scratchpad, self-search and archive tools for long-horizon context; Pipeline RL with bounded off-policy lag; Verifiable-reward PPO after continued pretraining (2022 recipe); Open-ended, outcome-scored long-horizon benchmark
- Tools: Galactica (Meta science LLM; 30B variant cited), Llama 2, Llama 3, Reasoning Llama (named, no details), ChatGPT, GPT-3.5, GPT-4, OpenAI o1, DeepSeek-R1, InstructGPT (2022, cited for RLHF results), PaLM (540B, cited for comparison), Chinchilla (cited for comparison)

## [State of Data — Sean Cai, Independent / State of Data](../videos/ZyIoTOAbRfs.md)
`ZyIoTOAbRfs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, data-engineering

Sean Cai argues data markets are the scarce input for turning generalist models into experts, and that single benchmark numbers and contrived expert-made data mislead buyers.

- Techniques: Three-axis verifiability scoring; Multi-harness, multi-infrastructure benchmarking; Per-criterion rubric analysis with deterministic checks plus LLM-as-judge; Long-horizon task checklist; Automatic post-training rerun on base-model swap; Lab spending as a leading indicator

## [Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](../videos/jRCpXUjz4CI.md)
`jRCpXUjz4CI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, agent-architecture, sandboxing-execution

Alex Shaw (Terminal-Bench, Harbor) argues agents behave like ML models, so teams should build environments (instruction, sandbox, verifier) and run parallel rollouts for evals, training data, RL and agentic map-reduce.

- Techniques: Environment as a three-part directory (instruction, sandbox, verifier); Separate rollout, trajectory capture and verification; Parallel rollouts with a fire-and-forget launch; Agentic map-reduce over agent logs; Own the eval before choosing a model; Design for agent users of your product
- Tools: Harbor, Terminal-Bench 2.1, Codex (GPT-5.5 run in the demo), Cursor CLI (map step in demo), Modal (sandbox backend in demo), Tinker (RL integration), A frontier model transcribed as 'Fable 5' (reduce step in demo; name may be a caption error), LangChain Deep Agents with sandboxes (integration)

## [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../videos/ZTA0GwpAUak.md)
`ZTA0GwpAUak` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: coding-agents, enterprise-adoption

Samuel Denton (Applied Compute) lays out a 2x2 of offline/online hints and traces for distilling production agents, with SWE-bench and hyperlink-format results showing online hints win on on-policy behavior.

- Techniques: Offline hint on offline production traces; Turn-budget nudge hint; One-step on-policy rollout from an offline trace; Online hint from each rollout; Judge-chosen hint placement with next-step distillation; Relevance-mass token selection (self-distillation)
- Tools: SWE-bench, Qwen 3.5 (thinking model)

## [The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside](../videos/KhYifX22yhE.md)
`KhYifX22yhE` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: data-engineering, models-research

Poolside's data and training leads on synthetic data at scale, the modular generation pipelines behind Laguna M.1 and XS.2, and the silent-corruption bugs (broken GPU, BF16 accumulation, FP8 kernel race) they found training Laguna S.

- Techniques: Modular six-part synthetic data pipeline; Seed-heavy cheap rephrasing; Staged decomposition of hard generation; Cross-domain porting and judge-evolver loops; Orchestrated agent queue (Hive); Cross-replica weight hash checks; FP32 accumulation for growing activations; Test recipes on a small model before scaling
- Tools: Hugging Face, DeepGEMM (FP8 kernels), Hive (poolside internal generation orchestrator)

## [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../videos/iqloyWCGYQQ.md)
`iqloyWCGYQQ` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, memory, models-research

Parth Asawa (UC Berkeley) argues that standard LLM benchmarks test models with memory wiped each time, and proposes measuring continual learning through sequential tasks, gain over a stateless baseline, and Pareto reporting.

- Techniques: Paired stateful vs stateless runs (gain metric); Benchmark design checklist for continual learning; Multi-axis Pareto reporting; Mid-sequence concept drift injection; Stability vs plasticity failure triage

## [The Base Model Is Dead — Varun Singh, Arcee AI](../videos/xbPriQWXtWM.md)
`xbPriQWXtWM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: models-research, data-engineering

Varun Singh (Arcee AI) argues base models have shifted from storing general web knowledge to priming RL for reasoning and agentic behavior, and explains the data-mix changes this requires.

- Techniques: Rephrase-based synthetic upsampling; Early injection of post-training-format data; Mid-training on post-training and long-context traces; Atomic-skill check before RL; Warm-up on test-time compute formats; Monitor MoE expert utilization under data shift
- Tools: Claude Code

## [Ending AI Slop — Thais Castello Branco, Taste Labs](../videos/lCBf9slCanI.md)
`lCBf9slCanI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, data-engineering

Taste Labs founder argues subjective domains like design and writing can be made verifiable by decomposing quality into checkable parts, routing each part to the right judge, and using quality expert data.

- Techniques: Decompose fuzzy quality into codified components; Per-component routing of grading method; Ground-truth rules instead of similarity to a reference; Diverse expert pool with strict selection to counter mode collapse; Specificity and code-linkage QA on expert labels; Disagreement triage in expert consensus

## [Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect](../videos/AQv3qRCG6Gw.md)
`AQv3qRCG6Gw` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, observability

Will Brown (Prime Intellect) on running RL when no verifiable reward exists: manufacture supervision from grounding, judges, production traces and learned simulators, and keep humans on the top-level decisions.

- Techniques: Environment as the shared unit (task + harness + rewards); With/without grounding as a supervision gap; Backward construction from a reachable end state; Trace-seeded task mining; Judge-to-rubric distillation; Pass-rate gated task generation; Learned simulator of an uncontrolled tool or site; Reward-hack corpus and small-run validation
- Tools: Prime Intellect PrimeRL training framework, Prime Intellect verifiers and task sets, Prime Intellect Lab (hosted training and evals), GRPO / REINFORCE policy-gradient methods (named in passing), MCP servers, CLI tools and web apps (as simulator targets)

## [Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd](../videos/ZFxh7sqbUZo.md)
`ZFxh7sqbUZo` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: security-guardrails, evals

David Brumley (CMU, Bugcrowd) on designing RL environments for vulnerability discovery and exploitation, using deterministic oracles, an open-world "audit" task scored by precision and recall, and a 16-rung capability ladder run against V8.

- Techniques: Deterministic witness-based grading; Open-world audit task with dedup and precision/recall; Capability ladder for hard targets; Withhold the answer key and the most dangerous artifacts
- Tools: MCP (exposed setup, read/write, and grading tools), Docker, exploitbench.ai, V8, AIxCC, DARPA Cyber Grand Challenge, SciBench, CyberGym, BountyBench

## [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../videos/Cc0_nyxROBA.md)
`Cc0_nyxROBA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, agent-architecture, security-guardrails

Gaurav Mishra (Amazon AGI Lab) on why RL-trained computer-use agents break on real login screens, ads, and expired sessions, and how to adapt training and the harness to real-world messiness.

- Techniques: Simulated messy environments for agent RL; Recovery as a native model action; Process reward model over the trajectory; Action risk classifier in the harness; Harness-level credential and loop guardrails; Checkpoint, rollback, and audit trail; Forced human handoff; Adversarial tasks in mainstream training; Design-partner failure loop
- Tools: Playwright, WebMCP, MCP, web search APIs, PPO, GRPO

## [Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google](../videos/hacEQHHhu2Q.md)
`hacEQHHhu2Q` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: local-ai, inference-serving

Google's Cormac Brick on running tiny (50M to 500M) and small (1 to 4B) models on phones, browsers and robots, and why fine-tuning on synthetic data beats bigger models for narrow tasks.

- Techniques: Synthetic-data fine-tuning of a tiny model for one task; Voice-to-function-calling pipeline; Two-stage on-device dictation pipeline; Memory budgeting for on-device LLMs; Multi-token prediction (MTP) for decode speed; Frame budgeting for NPU vision; Side-task tiny model
- Tools: LiteRT-LM, LiteRT / MediaPipe, Gemma 3, Gemma E2B, FunctionGemma, Gemma 4, AI Edge Gallery app, Apple FastVLM, Hugging Face (Mobile Actions dataset), Raspberry Pi, Jetson Nano, Qualcomm IoT boards (NPU)

## [Scaling up Continual Learning — Ronak Malde, Trajectory](../videos/zL1kLftVTlo.md)
`zL1kLftVTlo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, skills-self-improvement

Ronak Malde (Trajectory) on scaling continual learning: on-policy self-distillation with privileged hints as a step past GRPO, plus fixes for long tool-calling runs (step-level weighting, hint-leakage control).

- Techniques: On-policy self-distillation (OPSD); Step-level divergence weighting for long trajectories; Residual guidance via linear combination of hint strengths; LLM-filtered hints to prevent leakage; Inspect rollouts for hint leakage
- Tools: GRPO, OPSD, OpenClaw RL, LiveCodeBench, Mercor APEX-Agents

## [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](../videos/l0FLhNqBOic.md)
`l0FLhNqBOic` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: enterprise-adoption, product-ux, rag-retrieval

Varick Agents explain why process understanding, not model execution, is now the bottleneck, and describe the forward-deployed engineering agent they built for it.

- Techniques: Failure-path process interviews; Per-step autonomy split; Dependency graph as shared state; Post-training an open model for analysis style; RL environment with domain traversal tools; Assistant embedded in the authoring tool
- Tools: Varick OS (in-house platform), Claude, Codex, Granola, Kimi (open-source base model, named as K2.6), NetSuite, Microsoft Dynamics, SAP, Salesforce

## [Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software](../videos/2aS7aKoXn64.md)
`2aS7aKoXn64` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, agent-architecture

Theta Software on designing RL environments and LLM judges for long-horizon work, plus a critique of current finance agent benchmarks, which they say are saturated and mostly too short to count as long-horizon.

- Techniques: Judge with read-only environment access, as an agent; Make long trajectories queryable before judging; Pair deterministic checks with a rubric judge; Rubric QA suite; Check learnability and reward density
- Tools: METR time-horizon benchmark (cited, not a tool used), GDPval (benchmark, cited), BankerToolbench (benchmark, cited), APEX-Agents (benchmark, cited), Grafana, GitHub (CI/CD logs, PRs), AWS CloudWatch, Codex models (cited), Claude models (cited), GPT-5.5 (cited)

## [Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute](../videos/k35LeKZEhiE.md)
`k35LeKZEhiE` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, enterprise-adoption

Raymond Feng (Applied Compute) on post-training agents that learn on the job: how RL loops break when you do not own the harness, and the environment-fidelity failures that teach models bad habits.

- Techniques: Replayable sandbox for multi-rollout RL; Graded chats as the only training interface; Audit the environment for infrastructure failures before trusting a run; Log model requests and responses as the training source; Mine traces for failure modes, then build the dataset

## [Data Quality Is the Compute Multiplier — Ari Morcos, DatologyAI](../videos/_PdK6x7PQNM.md)
`_PdK6x7PQNM` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: data-engineering, models-research

Ari Morcos (Datology AI) argues data quality is an under-used compute multiplier, showing curated-data gains in VLMs, multilingual and legal models, and a small-budget frontier-scale run.

- Techniques: Four-C data pipeline (clean, curate, create, compose); Selective synthetic rephrasing into many formats; Domain mid-training with a representative mix; Small-run scaling check under token scarcity; Repeat high-quality data under token limits

## [Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs](../videos/ewtOo0scUh0.md)
`ewtOo0scUh0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: data-engineering, sandboxing-execution

Bespoke Labs on curating data and RL environments for post-training: OpenThoughts and OpenThoughts-Agent recipes, counterintuitive sampling and teacher findings, and a tag-based SFT fix for numeric hallucinations.

- Techniques: Stage-wise ablation of a data curation pipeline; Multi-sample answers per question; Teacher model selection by measurement; Structural tags in fine-tuning data; Reflection-based prompt optimization
- Tools: Curator, Bespoke Stratos, OpenThoughts, Terminal-Bench, Tinker, Fireworks

## [Local Models: Trust, Control, Optimization — Carter Abdallah, NVIDIA](../videos/FWMJQDH3iK0.md)
`FWMJQDH3iK0` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · also: local-ai, models-research, governance-compliance

A panel from NVIDIA, Prime Intellect and Arcee argues open-weight models give trust, cost control and data ownership, and that post-training them on your own harness and traces beats generalist frontier APIs for narrow work.

- Techniques: Harness-specific post-training of an open base model; RL environment, then deploy, then train on production traces; Trace capture as a fine-tuning dataset; Specialize a small model to one or two tasks; Verify open weights and inference code before trusting them
- Tools: vLLM, SGLang, PrimeRL, NeMo RL, NeMo Gym (captioned as 'Nemo Jim'), verifiers, Hugging Face, Nemotron, Trinity (Arcee model), Hermes (harness), Pi (harness), OpenMDW license

## [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../videos/CvRngaQZQ3Y.md)
`CvRngaQZQ3Y` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: observability, evals, memory

LangChain's Vivek Trivedy argues agent improvement is a data-mining loop: ship, collect traces, mine them, then run data-driven experiments on prompts, tools and models.

- Techniques: Agent-driven trace mining; Frontier-to-open-model downgrade via trace judging; Distillation from good traces; Evals generated from traces; Score-driven auto-research loop; Harness, then fine-tune, then harness sandwich; Human review summaries
- Tools: LangSmith, LangSmith Engine, Deep Agents, Claude Code, Codex, Terminal Bench, scikit-learn

## [Scaling Compute on Context — Jack Morris, Engram](../videos/WiqDvX6isc4.md)
`WiqDvX6isc4` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: memory, models-research, context-engineering

Jack Morris (Engram) frames "scaling compute on context": with a fixed private dataset and a pretrained model, the only scaling axis left is compute, and he surveys why naive, compaction, distillation, synthetic-data and RL approaches all saturate.

- Techniques: Naive continued training on a private corpus; KV compaction of in-context data; On-policy distillation toward in-context behaviour; Self-study (generated QA conditioned on the corpus); Synthetic continued pretraining; Unsupervised RL environments over the corpus; Gradually harder self-generated curriculum
- Tools: Cartridges (self-study paper, named on slide), On-policy distillation, GRPO (named as an RL loss example), KV cache compaction (named approach)

## [Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang](../videos/zkX03APVj0M.md)
`zkX03APVj0M` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: sandboxing-execution, evals

Joseph Wang of Emulated argues that agent training needs realistic infra environments: multi-node sandboxes that touch real cloud resources, not single-container coding tasks.

- Techniques: Multi-node cluster simulation in one sandbox; Chained multi-deployment episodes for long horizon; Organisation context as part of the environment; Multi-node sandbox on real cloud resources (CloudBox); Choose a vertical with clear customer requirements first
- Tools: Harbor, etcd, Kubernetes, AWS Lambda

## [Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face](../videos/O-CBZ3JtRvo.md)
`O-CBZ3JtRvo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, evals, models-research

Uri Rolls and Thom Wolf present Arithmetic's "Mask Off" benchmark: black-box access-control exploit chains built from real zero-days, graded per step, to test whether models can make logic leaps.

- Techniques: Black-box exploit-chain environments from self-found zero-days; Per-step deterministic graders with partial credit; Trace review as the main eval loop; Orchestrator for running evals
- Tools: Bach (Arithmetic's internal eval orchestrator)

## [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../videos/XEd_SRVHBgU.md)
`XEd_SRVHBgU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: models-research, evals

Sara Hooker (Adaption) argues frontier AI should be open to more builders, and pitches Autoscientist, an automated training loop that co-optimizes data and model while saying pre-training scale is no longer the main lever.

- Techniques: Co-optimize data curation with the model in the same search; Win-rate threshold as the stop condition for a training search; Wide architecture and size search instead of team familiarity; Adaptive test-time compute per task (planned)
- Tools: Autoscientist (Adaption, beta)

## [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song](../videos/AVMr9PMINyo.md)
`AVMr9PMINyo` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · also: inference-serving, models-research, evals

A MiniMax and Together AI panel on how an open-weight model like MiniMax M3 gets trained, then served at scale, with day-zero kernel work, agentic KV-cache demands and long-horizon RL evals.

- Techniques: Day-zero kernel plus post-launch optimization queue; Benchmark unsolved kernel problems as RL environments; Multi-submission long-horizon evals with held-out validation; Multimodal training from step zero; KV cache as a distributed store; Cross-model optimization transfer
- Tools: KernelBench, Parallel KernelBench, OSWorld, SVG bench, MiniMax sparse attention

## [Jev CEO: I made ChatGPT, now I'm building what's next](../videos/cJ0EOzey--o.md)
`cJ0EOzey--o` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: models-research, product-ux

Former OpenAI post-training lead Diego Almeida argues RLHF models are built for assistance, not automation, and pitches a new post-training objective (calibrated decision making) at his stealth startup TypeSafe.

- Techniques: Assistance vs automation diagnostic; Cost-shifting to the user as a deployment pattern; Name the optimization target before choosing a post-training method
- Tools: Claude Code

## [Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit](../videos/Owb8g3yDyzo.md)
`Owb8g3yDyzo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, enterprise-adoption

Intuit's Udi Menkes argues frontier LLMs give fluent but unverified money advice, and that grounding a model in real business outcomes (state, action, outcome) beats model size.

- Techniques: Outcome-grounded trajectory dataset; Propose-then-rank split; Propensity-matched uplift estimate; Evidence-grounded explanation; Long-horizon simulation with a rules baseline
- Tools: QuickBooks, TurboTax, Credit Karma, Mailchimp, reinforcement learning (Intuit in-house model)

## [Model Distillation: How to Steal a Billion-Dollar AI](../videos/gacMZf5rqYA.md)
`gacMZf5rqYA` · Kai Explains · 2026-08-02 · q3 · practitioner · other · also: models-research, local-ai, security-guardrails

Explainer on model distillation: how small students copy frontier models via API outputs, the DeepSeek R1 and budget-reasoning examples, the capability gaps that remain, and reported extraction campaigns.

- Techniques: White-box soft-label distillation; Black-box distillation via API sampling; Reasoning-trace fine-tuning of an open base; Small curated dataset recipe (S1-style); Append 'Wait' to extend reasoning at inference; Paraphrase robustness check for memorization; Size the local student to the GPU
- Tools: DeepSeek-R1, Qwen (32B, 14B, 7B distilled variants), OpenAI o1-mini, OpenAI o1-preview, OpenAI ChatGPT, Google Gemini, Sky-T1 (Berkeley), S1 (Stanford / University of Washington), Alma (local model runner, as named), OpenRouter, Hugging Face model cards, AIME 2024 benchmark

## [Inkling: This Open-Weight Model Wants To Be Fine Tuned](../videos/YAcIUCjsRnU.md)
`YAcIUCjsRnU` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: models-research, voice-multimodal

Better Stack walks through Thinking Machines' open-weight "Inkling" model: a MoE that takes raw audio and image patches, positioned as a base for fine-tuning on Tinker rather than a general frontier model.

- Techniques: Decide fine-tune vs retrieval by failure type; Distill a narrow task from a general model into a small fine-tuned model; Let the model generate its own fine-tuning dataset via Tinker; Feed raw audio directly to the model for tasks needing prosody or delivery; Tune reasoning depth with the thinking-effort slider
- Tools: Inkling (Thinking Machines open-weight MoE model), Tinker (fine-tuning platform), LoRA, Hugging Face, GLM 5.2, GPT-OSS, GPT-4.0, Kimi K3, Qwen, DeepSeek, NVIDIA Nemotron

## [SeFI image, Leanstral Beats Every Math AI, Hy3 Challenges GPT, Agents A1 & Bytedance AI News](../videos/rVwK1fuzKJU.md)
`rVwK1fuzKJU` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, local-ai, inference-serving

Weekly Kai Explains roundup of late-July 2026 open-model releases: Mistral Leanstral 1.5 (Lean 4 prover), Tencent HY3, InternScience Agents A1, CeFi Image, ByteDance Depth Anything 3 and GenRecon. Mostly release-announcement content with a few concrete numbers.

- Techniques: Test-time compute scaling for formal provers; Property-generation plus formal proof as a bug finder; Semantic-first two-stream diffusion
- Tools: Leanstral 1.5, Lean 4, Lean language server, CISPO, Mistral Vibe, Hugging Face, Tencent HY3, Hunyuan 3, CodeBuddy, WorkBuddy, Tencent Cloud, OpenRouter

## [State of the Union: Why Local, Why Now — NVIDIA, Osmantic, Roboflow, EXO Labs, @matthew_berman](../videos/KB41dTlX1Uc.md)
`KB41dTlX1Uc` · AI Engineer · 2026-07-18 · q3 · intro · panel · also: local-ai, inference-serving, models-research

Panel on why local AI is now practical: multi-model setups, frontier-plans/local-executes splits, distilling big-model consensus into small specialized models, and the remaining UX and openness gaps.

- Techniques: Plan with frontier, execute with local; Consensus distillation; Drop open-vocabulary machinery when classes are fixed; Trace-driven model routing; Retune existing configs for small hardware; Hardware-aware model selection; Frontier bootstrap then open model
- Tools: vLLM, SGLang, Local.ai, ODS (open-source deployment system), DGX Spark, DGX Station, Brev, Segment Anything 3 (SAM3), Cursor, Codex, Llama, Qwen 3.5 / 3.6

## [Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](../videos/q4Tr-DknG2M.md)
`q4Tr-DknG2M` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, models-research, multi-agent

Cursor's Lee Robinson on how Cursor trains its Composer models: a two-loop flywheel, defenses against eval hacking, textual-feedback RL, and models increasingly helping train their successors.

- Techniques: Eval hygiene for agent benchmarks; Private held-out eval from your own repos; Ablate-and-reimplement RL task generation; Textual feedback for credit assignment; Distilled judges and reward models from the top model; Agent fleets launched from chat with escalation to humans
- Tools: Cursor, Composer, Kimi (prior open-source base model; transcribed as 'Kimmy'), Colossus, Slack, Git, Datadog, Notion, Linear, MCP, Artificial Analysis

## [Modern Post-Training: A Deep Dive  — Will Brown, Prime Intellect](../videos/V-EDrhIhHzQ.md)
`V-EDrhIhHzQ` · AI Engineer · 2026-07-18 · q4 · deep · workshop · also: evals, agent-architecture, infra-cost-scaling

Will Brown (Prime Intellect) walks through modern post-training: environments as evals, the verifiers v1 task/harness/runtime split, async RL with an interception server, and the PrimeRL trainer.

- Techniques: Task / harness / runtime decomposition; Fake base URL interception for RL on real harnesses; Async rollout batching with off-policy tolerance; Message-level trace with token mapping; Algorithm and loss separation with a registry; Group-relative shaping for length and efficiency; Same-task eval CLI with swappable harness and runtime
- Tools: verifiers, PrimeRL, Renderers, TorchTitan, Megatron, Harbor, NemoGym, OpenEnv, Hugging Face datasets, uv, Docker, Claude Code

## [Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth](../videos/uIiA6DquRiE.md)
`uIiA6DquRiE` · AI Engineer · 2026-07-18 · q4 · practitioner · workshop · also: evals, inference-serving, models-research

Daniel Han (Unsloth) workshop on benchmark reliability, harness and inference-provider accuracy drift, dynamic quantization, torch.compile over handwritten kernels, and reward hacking in RL and coding agents.

- Techniques: Repeated sampling with reliability math; Rolling-average regression canary for a hosted agent; Benchmarks with unbounded instance space and programmatic verifiers; Single controlled harness for model comparisons; Calibration-based dynamic quantization; Per-provider accuracy check before adopting an inference endpoint; Open-weight baseline on llama.cpp or llama-server; torch.compile-first performance tuning with randomized bisection over flags; Audit RL and agent runs for reward hacking
- Tools: Unsloth, Hugging Face, Math-Verify (Hugging Face), llama.cpp / llama-server, PyTorch, torch.compile, Triton, CUDA, FlashAttention (FA2, FA3, FA4 mentioned), Claude Code, OpenAI Codex, Gemini CLI

## [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis](../videos/IQkVMvXQKLY.md)
`IQkVMvXQKLY` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: security-guardrails, evals

Sachin Kumar (LexisNexis) shows that a backdoored fine-tune can pass behavioral evals, and that a sparse autoencoder trained on base-vs-fine-tune activation deltas finds the trigger with near-zero false alarms.

- Techniques: Diff SAE on activation deltas; Backdoor isolation score per feature; Procedural data with a controlled trigger; Objectively measured backdoor target; Build-gate probe check
- Tools: SmolLM2-360M, sparse autoencoder, LoRA, static analysis

## [How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](../videos/1IdzkRVmWAA.md)
`1IdzkRVmWAA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: rag-retrieval, agent-architecture, evals

Mixedbread's team on why agents write keyword-soup queries that hurt retrieval, and how a bounded four-tool search harness, trained with SFT then RL, recovers much of the oracle gap.

- Techniques: Tiered search tool set for agents; Bounded parallel search rounds with dedupe; Priming with a corpus preview; Describe-the-need query framing; Oracle-gap diagnosis; SFT then on-policy RL with a mixed reward
- Tools: Mixedbread search, Codex, GPT-5, Gemini 3.5 Flash, grep, BM25

## [Ideogram 4.0 image model, ByteDance Ditches Nvidia GPU, Google's 16GB Multimodal Beast AI News](../videos/12_TXXeI4uE.md)
`12_TXXeI4uE` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, voice-multimodal

Roundup of late-June/early-July 2026 open-model releases: Ideogram 4.0 (open-weight, describe-to-structure training), Reve 2.0, Joy AI Echo long-video generation, Gemma 4 12B unified multimodal model, Magenta RealTime 2, ByteDance CUDA Agent, LFM 2.5 VL 450M, Molmo 2, MDA depth, Nemotron ASR, NVIDIA Artifixer.

- Techniques: Describe-to-structure-to-recreate training; Mixture-density depth output; Agentic kernel optimization loop; Unified decoder-only multimodal input without encoders
- Tools: Ideogram 4.0, Reve 2.0, Joy AI Echo, Gemma 4 (12B), Magenta RealTime 2 (MRT2), CUDA Agent, CUDA Agent Ops 6K, torch.compile, KernelBench, LFM 2.5 VL 450M, Molmo 2, MDA (Modeling Depth Ambiguity)

## [Claude Fable 5, Grok imagine 1.5, Gemini Live Translate, HumanEgo Robot, Mirage World Model AI News](../videos/ibGW_YqQmLg.md)
`ibGW_YqQmLg` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, inference-serving, voice-multimodal

Kai Explains weekly AI news roundup (2026-07-02): Claude Fable 5 and Mythos 5, Grok Imagine 1.5, N2 Pro, Quasar, LeVar, vLLM-Omni, HumanEgo, SCAIL 2, Gemini 3.5 Live Translate, Mirage. Mostly vendor and paper claims relayed without testing.

- Techniques: Adaptive thinking gate; Sensitive-category model routing; Persistent file-based memory for long agent runs; Latent-space scene memory (Mirage); Interaction-centric tokens for cross-embodiment policies (HumanEgo); Skeleton-free motion transfer (SCAIL 2); Geometry from a 4D reconstruction model as a video-diffusion condition (LeVar)
- Tools: Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, Claude Mythos Preview, Project Glasswing, Grok Imagine 1.5, xAI API, N2 Pro (SII), N2 Mini, Qwen 3.5, OpenRouter

## [OpenAI GPT 5.6 launch, Realtime Video avatar, HappyHorse 1.1, Nvidia & More AI News](../videos/odlkEMloedA.md)
`odlkEMloedA` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, voice-multimodal

Weekly AI news roundup: GPT-5.6 Sol/Terra/Luna and its gated release, Happy Horse 1.1 video, Ornith 1.0 open coding models, WanStreamer, NVIDIA's video inference engine, Fine VLA and SURF. Mostly vendor-reported claims.

- Techniques: Self-scaffolding RL training (Ornith 1.0); Tiered model family routing; Automatic per-model acceleration stack selection; Single-transformer streaming for conversational avatars; Fine-grained instruction relabeling for robot data
- Tools: GPT-5.6 (Sol, Terra, Luna), OpenAI Preparedness Framework, Terminal Bench 2.1, GeneBench V1, ExploitBench, ExploitGym, Happy Horse 1.1, Happy Horse 1.0, Arena AI Video Arena, Ornith 1.0 (9B dense, 31B dense, 35B MoE, 397B MoE), Claude Opus 4.7, MiniMax M3

## [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](../videos/wcUJWP6WpGM.md)
`wcUJWP6WpGM` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: evals, coding-agents, testing-verification

Ibragim Badertdinov (Nebius) shares lessons from running monthly SWE-rebench evals of coding agents: fresh time-split tasks, verifier quality, infra noise, benchmark cheating, and reporting cost and reliability.

- Techniques: Monthly time-split task collection; Oversample, then filter by running agents; Strip future information from the agent sandbox; Minimal agent with strong infrastructure; Error-class retry policy; Reliability-aware metrics; Reproduce a public benchmark before trusting your own numbers; Eval pipeline reused as training pipeline
- Tools: SWE-rebench, SWE-bench, Terminal-Bench, Claude Code, Codex, Junie, Docker, GitHub Archive, GitHub API

## [Your Coding Agent Should Do AI System Engineering — Ben Burtenshaw, Hugging Face](../videos/JomVvNDjGb8.md)
`JomVvNDjGb8` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: coding-agents, skills-self-improvement, multi-agent

Ben Burtenshaw (Hugging Face) argues coding agents can take on AI systems work: writing CUDA kernels, fine-tuning models, and running a multi-agent automated research lab, using open skills, open Hub repos and an open dashboard data layer.

- Techniques: Skill-as-few-shot-examples with bundled benchmark scripts; Skill eval across models (Upskill); Role-split autoresearch loop; Git and bucket as agent shared state; Open-format dashboard as an agent data source; Verifiable-experiment precondition
- Tools: CUDA, Hugging Face kernels library, Upskill, Hugging Face Skills repo, HF Papers CLI, HF Jobs, OpenCode, Codex, Claude Code, Trackio, Parquet, Unsloth

## [Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel](../videos/YYH0DMQr30A.md)
`YYH0DMQr30A` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: evals, data-engineering

Snorkel's Kobe Crawford argues that task quality is data quality for agentic terminal tasks, and shows that RL on verified high-quality tasks gives about 5x the uplift of low-quality ones.

- Techniques: Containerized task environments with a verification test gate; Accepted vs rejected task comparison; Failure taxonomy for benchmark runs; Controlled RL A/B on task quality; Rubric-based human and LLM-judge calibration; Make tasks verifiable on the back end
- Tools: Harbor Framework, Terminal-Bench, Claude Sonnet 4.5, Codex, GPT-5.2, GPT-5.1

## [Personalization in the Era of LLMs - Shivam Verma, Spotify](../videos/5YSJEP0HWzM.md)
`5YSJEP0HWzM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: context-engineering, enterprise-adoption

Spotify's AI Foundation tech lead explains how it personalizes recommendations with user embeddings, semantic IDs for catalog items, and soft user tokens fed into a fine-tuned open-weight LLM.

- Techniques: Semantic ID tokenization of item embeddings; Soft user token injection; Tokenized listening-history prompting for domain adaptation; Daily batch user-embedding generation; User-editable text profile as a steering signal
- Tools: Llama, Qwen

## [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](../videos/TNwJ1LMiENk.md)
`TNwJ1LMiENk` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: evals, mcp-and-tools

Snorkel shows a 4B model, RL-trained on single-table financial tool-use tasks for under $500, beating a 235B model. The gain came from fixing tool discipline, not reasoning.

- Techniques: Behavior-targeted RL with GRPO on a tool environment; Single-table-first training data; Verification pass on generated tasks; Rubric decomposition for diagnosis; Publish the environment as a portable package
- Tools: GRPO, RLM framework (UC Berkeley), FinQA environment (Snorkel), OpenEnv, Prime Intellect, Harbor, GetTableNames / GetTableInfo tools, Qwen3

## [Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI](../videos/TUnPNY4E2fw.md)
`TUnPNY4E2fw` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: infra-cost-scaling

Together AI's Max Ryabinin walks through stacking memory optimizations (Ulysses context parallelism, checkpointing, CPU offload, tiling, and the UPipe head-chunking method) to train with multi-million-token context.

- Techniques: Staged memory accounting; Head-based context parallelism (DeepSpeed Ulysses); Activation checkpointing plus CPU offload of block inputs; Sequence tiling of element-wise ops; UPipe head chunking with buffer reuse; Profile with PyTorch profiler first
- Tools: PyTorch profiler, FSDP, DeepSpeed Ulysses, FlashAttention

## [How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed](../videos/phchDt63qAA.md)
`phchDt63qAA` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: evals, product-ux

Zed's Edit Predictions lead explains how Zeta 2, a small fine-tuned next-edit model, was distilled from frontier teachers using opt-in production snapshots, settled-state labels, and multi-sample filtering.

- Techniques: Teacher repair loop; Cache the teacher, vary the formatting; Settled-state labels via idle detection; Multi-sample consensus filter with a distance band; Multi-reference offline eval; Percentage-based live experiment rollout
- Tools: Zed, Zeta 2, Seed Coder, Levenshtein distance, JSONL

## [From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google](../videos/-TiET_K-E_g.md)
`-TiET_K-E_g` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: local-ai, inference-serving, skills-self-improvement

Google's Cormac Brick on on-device agents: a prompt-based skill harness on Gemma 4, and fine-tuning FunctionGemma on synthetic data to lift function-calling success from about 46% to 90%+ on most functions.

- Techniques: Progressive skill disclosure; In-app JavaScript rendering from a skill; Coding agent writes the skills; Synthetic-data fine-tune for fixed function calling; Export and deploy pipeline for small models; Chained tiny models for a pipeline
- Tools: LiteRT-LM, LiteRT, MediaPipe, Gemma 4, FunctionGemma, Gemma 3, Gemini Nano, Android AICore, Gemini CLI, Gemini Flash, litert-torch, transformers

## [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../videos/gHs5ZiY80PM.md)
`gHs5ZiY80PM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: inference-serving, voice-multimodal

NVIDIA's Ziv Ilan on making diffusion image and video models fast enough for real use: quantization, step caching and step distillation, stacked incrementally, with distillation as the biggest win.

- Techniques: Post-training quantization with dynamic ranges for diffusion; Step caching (TeaCache-style and chunk-based); Trajectory vs distribution step distillation; Incremental optimization ladder
- Tools: TensorRT-LLM Visual Gen, FastGen, vLLM-Omni, SGLang Diffusion, TeaCache, Blackwell GPUs (B200), Hugging Face checkpoints

## [What Lies Beneath the API — Benjamin Cowen, Modal](../videos/HvZXAOZ3iv8.md)
`HvZXAOZ3iv8` · AI Engineer · 2026-06-18 · q2 · intro · talk · also: inference-serving, infra-cost-scaling

Modal forward-deployed engineer argues that once a product is differentiated, fine-tuning becomes worth it, and that serverless compute and open-source libraries now make it accessible without a cluster team. Sales-leaning, with a few concrete signals and code-size claims.

- Techniques: Signal-based fine-tuning decision; Harness outcomes as RL training data; Parallel hyperparameter sweep with early kill; Sandbox-fanned RL rollouts; Autoscaled serving of custom models
- Tools: Modal, vLLM, SGLang, Triton Inference Server, Python

## [Why This AI Has No Idea What World War 2 Is](../videos/4EA7vEAkoIw.md)
`4EA7vEAkoIw` · Better Stack · 2026-06-02 · q3 · intro · demo · also: models-research, evals

Better Stack demo of Talkie, a 13B model trained only on pre-1931 text, used to show how vintage models separate memorization from learning, forecasting, and temporal leakage.

- Techniques: Contamination-controlled capability probe with a date-cutoff model; Surprisal-based forecasting eval; Temporal leakage audit; Period-matched synthetic post-training data with a modern RL judge, plus a style check
- Tools: Talkie (13B vintage language model, pre-1931 training data), Claude Sonnet 4.6 (used as RL judge in post-training), ChatGPT (mentioned as a modern model), Claude (mentioned as a modern model), Gemini (mentioned as a modern model), GPT (2018 OpenAI research, mentioned via a researcher's background), DALL-E (captioned as 'DALI'), Whisper (mentioned via a researcher's background), HumanEval-style Python tests (captioned as 'human eval')

## [Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face](../videos/OV56RddyFuU.md)
`OV56RddyFuU` · AI Engineer · 2026-05-18 · q2 · practitioner · demo · also: local-ai, mcp-and-tools, coding-agents

Hugging Face's Merve Noyan demos open-model agent workflows: picking and serving open models, Hermes Agent, pushing agent traces to the Hub, HF MCP server and skills that let coding agents launch fine-tuning and batch OCR jobs.

- Techniques: Hub-ID local serving for coding agents; GGUF hardware-fit check before download; Agent-driven fine-tuning via skills; Session traces pushed to a Hub dataset; Corpus OCR via prompted batch job; HF MCP server for catalog access
- Tools: Hugging Face Hub, Hugging Face MCP server, Hugging Face skills (hub CLI, LLM trainer, Gradio, dataset), Inference Providers, Hermes Agent, Pi, llama.cpp, vLLM, MLX, LM Studio, Claude Code, Codex

## [How Transformers Finally Ate Vision – Isaac Robinson, Roboflow](../videos/VhfAVA3BG2I.md)
`VhfAVA3BG2I` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: models-research, inference-serving

Isaac Robinson (Roboflow) traces how plain ViTs beat CNN and hybrid backbones, crediting massive ViT-specific pretraining, borrowed LLM speedups, and NAS over one foundation model for deployable vision.

- Techniques: Benchmark attention variants against a FlashAttention baseline; Masked-patch pretraining to instill inductive bias; Linear-probe check for frozen features; NAS over a pretrained foundation model; Transfer benchmark for foundation models
- Tools: SAM, SAM2, SAM3, MobileSAM, TinyViT, Hiera, ConvNeXt, Swin Transformer, ViT, MAE, DINOv2, DINOv3

## [Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs](../videos/UsB70Tf5zcE.md)
`UsB70Tf5zcE` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: models-research

Hands-on workshop on building and training a tiny GPT-2-style character-level LLM from scratch in PyTorch on a laptop or Colab, covering tokenizer, transformer blocks, training loop, and decoding.

- Techniques: Character-level tokenizer via stoi/itos dictionaries; Decoder-only transformer with pre-norm residual blocks; Offset-by-one next-token targets with cross-entropy; Linear warmup then cosine decay with AdamW; Validation-loss checkpointing and overfit detection; Loss-curve triage; Temperature and top-k sampling for generation; Seed-pinned, prompt-logged output for reproducibility; Encoder-to-embedding injection for multimodal inputs; Modality-specific losses for audio and distillation
- Tools: PyTorch, uv, NumPy, tqdm, tiktoken, Google Colab, Python 3.12, Karpathy nanoGPT (referenced)

## [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google](../videos/BKWpYIWvAo4.md)
`BKWpYIWvAo4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: local-ai, inference-serving, skills-self-improvement

Google AI Edge on running small Gemma models on-device via LiteRT-LM, the on-device agent-skills pattern (progressive disclosure, constrained tool calls), and fine-tuning tiny models with synthetic data.

- Techniques: Progressive disclosure for skills; Three-primitive orchestrator; Constrained decoding scoped to tool calls; Synthetic data then fine-tune then quantize; Modular pipeline of small models; LoRA hot-swap on one base model; Skill testing loop with a coding agent and a device; Build-once, deploy-everywhere model file with AOT for NPU
- Tools: LiteRT-LM, LiteRT (formerly TensorFlow Lite), LiteRT-Torch, Google AI Edge Gallery, MediaPipe, Gemma 4 (E2B, E4B), Function Gemma (270M), Gemma 3 270M, EmbeddingGemma (300M), FastVLM (500M, Apple), Qwen 0.6B, Gemini CLI

## [Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML](../videos/X6NShR2ccOg.md)
`X6NShR2ccOg` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: evals, enterprise-adoption, inference-serving

Adaptive ML's CCO argues RL, not prompting or SFT, is the systematic way to take enterprise LLMs and agents from MVP to production, using environments, rewards, and LLM judges. Mostly a product pitch for their platform.

- Techniques: Mock environment with mock tools and an LLM-played user; Rejection-sampling bootstrap from reward-scored trajectories; Business KPI as the RL reward; LLM judge with human-written rubric, graduated to a reward model; Prefer a smaller RL-trained model for high-volume or latency-bound features
- Tools: Adaptive Engine, PPO, GSPO, Gemma, Mistral, Qwen

## [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../videos/xOP1PM8fwnk.md)
`xOP1PM8fwnk` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: models-research, inference-serving, voice-multimodal

Google DeepMind's Sander Dieleman walks through training image and video diffusion models at scale: learned latents, how denoising works, guidance, step-count distillation, and control signals added in post-training.

- Techniques: Two-stage latent diffusion with a learned autoencoder; Guidance by amplifying the conditional-minus-unconditional difference; Deterministic sampling as a distillation teacher; Consistency distillation restricted to sampling intervals; Injecting conditioning via extra tokens or broadcast; Data-parallel first, then model-parallel sharding with JAX pjit
- Tools: JAX, pjit, TPU, Stable Diffusion, GLIDE, EQVAE, Veo, Genie

## [Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI](../videos/fLUtUkqYHnQ.md)
`fLUtUkqYHnQ` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: inference-serving, models-research, local-ai

Liquid AI's Maxime Labonne on training 350M to 24B edge models: small models have their own constraints, narrow targeting and doom-loop fixes via DPO and RL.

- Techniques: On-policy DPO pairs for doom-loop suppression; Repetition penalty inside RLVR; Fix training stage by diagnosis; Profile architecture on target hardware; Tool and environment offload for small models
- Tools: Hugging Face, Python

## [ChatGPT is OBSESSED with Goblins (Here’s Why)](../videos/RGIrw2G70wE.md)
`RGIrw2G70wE` · Better Stack · 2026-05-02 · q3 · intro · news · also: models-research, context-engineering

Explains OpenAI's investigation into why ChatGPT kept inserting goblins and gremlins: a reward signal for the nerdy persona rewarded those words, and the habit spread through training and self-generated data.

- Techniques: Spurious-reward audit via matched pairs; Track lexical quirk frequency across releases, personas and training steps; Break self-generated training feedback loops; Negative system-prompt rule with a relevance condition as a stopgap
- Tools: ChatGPT, Codex, GPT-5.1, GPT-5.4, GPT-5.5

## [How Big Models Fit on Small GPUs (DeepSpeed)](../videos/OM-DJuwweE0.md)
`OM-DJuwweE0` · Better Stack · 2026-02-02 · q3 · intro · tutorial · also: local-ai

Better Stack's short tutorial on using Microsoft's DeepSpeed ZeRO stages to fit training workloads into limited GPU memory, run on Colab from a Mac.

- Techniques: Run the DeepSpeed environment check before training; Begin with a ZeRO stage 2 config.json copied from the official docs; Change one config knob per run; Escalate ZeRO stage only when memory still fails; Use a hosted GPU runtime when the local machine has no NVIDIA GPU; Scale to multiple GPUs through Accelerate
- Tools: DeepSpeed, PyTorch, Hugging Face (transformers), Accelerate, Google Colab, CUDA, DSReport (DeepSpeed environment check), ZeRO / ZeRO-Infinity (DeepSpeed features)

## [Figure 03 and the Future of Robotics](../videos/NL2zbYhC5Z4.md)
`NL2zbYhC5Z4` · Better Stack · 2025-11-02 · q2 · intro · news · also: models-research, agent-architecture

Better Stack's overview of Figure 03's claimed actuators, balance control, sensing, cooling and Helix model, plus speculative stack guesses from GitHub repo names; few reproducible details.

- Techniques: Physics-first balance with a learned layer; Layered real-time control stack; Sim-to-real RL with massively parallel environments; Latency budgeting as a first-class metric; Thermal co-design with structure; Fleet-wide offload for centralized training
- Tools: Figure 03, Helix (Figure's large behavior model), NVIDIA Isaac Lab, NVIDIA Isaac Sim, MuJoCo, Brax, nvblox (transcribed as NV Blocks), LightGlue ONNX

