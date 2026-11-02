# How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Ok6QdZHCcI8` · [watch](https://youtu.be/Ok6QdZHCcI8) · **date:** 2026-10-29 · **length:** 11:47 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** David Abitbol · **orgs:** Revolut, Anthropic, OpenAI, Google
- **topics:** token-cost-efficiency, inference-serving, sandboxing-execution, governance-compliance · **tags:** self-hosted-open-models, glm, b200, blackwell, fp4, tensor-parallelism, kv-cache, prefix-cache, ttft, cost-reduction, sandbox, data-residency, zero-retention, opentelemetry, human-in-the-loop, claude-code, codex, opencode

> Revolut's AI ops lead explains how self-hosting GLM on dedicated GPUs cut its coding-AI invoice to about a tenth, and which serving metrics and tuning levers mattered.

## Summary
David Abitbol, who leads AI operations at Revolut, describes how the bank moved about 2,000 engineers from strict-budget frontier-model coding tools to self-hosted open-weight GLM models on dedicated GPUs. He argues the real gain is in lead time (feature pickup to merge) rather than raw coding time, and that flat-cost open models make unlimited use affordable. The talk gives concrete serving targets: time-to-first-token under about 3 seconds, roughly 200 tokens per second per user, and 56 B200 GPUs for the whole population. The same GPUs went from about 3 requests per second with over 10 seconds TTFT in April to over 7 requests per second with about 1.6 seconds TTFT by August, through tuning rather than added hardware. Tuning levers he lists are capping context at 256K, FP4 precision on Blackwell, tensor parallelism of 8 when KV cache is short, and a prefix-cache hit rate above 90 percent for coding workloads. For production he recommends a local router to send image tasks to a vision model, exposing OpenAI-compatible Responses endpoints to tools like OpenCode and Codex, and a sandbox with per-command allow and deny rules so coding stays human-in-the-loop for regulators. The talk is a short, first-hand internal case study with few methodology details.

## Key ideas
- **Measure AI coding by lead time (feature pickup to merge), not coding time. Lead time improved more than coding time because the bottleneck is inbox, Jira and Confluence overhead.** — Revolut's sample of 2,000 engineers: Gemini gave about 10% lead-time and 20% coding-time gains. Self-hosted GLM 5.1 (April) gave about 60% coding-time and 70% lead-time gains. ([3:20](https://youtu.be/Ok6QdZHCcI8?t=200))
- **Cost control drove the switch. Per-engineer spend of 1,000 to 10,000 a month with weak ROI led to strict budgets first, then self-hosting for flat-cost, effectively unlimited tokens.** — Currency is not stated in the talk. The stated goal is that engineers stop rationing tokens for the end of the quarter or the hardest task. ([2:18](https://youtu.be/Ok6QdZHCcI8?t=138))
- **Judge self-hosted serving by time-to-first-token and per-user speed, not peak throughput. Users run tasks in parallel and check in at completion, so ~200 tokens/s is enough.** — Target TTFT under 3 s. Complaints start above 5 s. Off-peak, some engineers reach about 800 tokens/s. ([4:24](https://youtu.be/Ok6QdZHCcI8?t=264))
- **Tuning, not hardware, produced the big gain. The same 56 GPUs went from ~3 req/s and >10 s TTFT (April) to >7 req/s and ~1.6 s TTFT (August).** — Speaker's summary: 88% performance improvement for 76% more demand. The point is to resist scaling out until parameters are tuned. ([5:28](https://youtu.be/Ok6QdZHCcI8?t=328))
- **Parameter checklist: cap context at 256K even if 1M is servable; use FP4 on Blackwell; use TP8 when KV cache is the constraint; target >90% prefix-cache hits for coding.** — Speaker says going from FP4 to FP8 costs about 40% more GPU footprint for no measurable precision gain. Speculative decoding and prefill optimisations are mentioned but not unpacked. ([6:32](https://youtu.be/Ok6QdZHCcI8?t=392))
- **For a text-only model, route image requests through a local router to a vision model and keep the main model for coding.** — He names a local router (caption reads 'OpenCodex') as one option. A smaller Gemini Flash-class model is used for UI design work with images. ([7:39](https://youtu.be/Ok6QdZHCcI8?t=459))
- **Expose the endpoints as OpenAI-compatible Responses APIs so existing coding harnesses work unchanged.** — He says this works in OpenCode, Codex and the Codex app. ([8:45](https://youtu.be/Ok6QdZHCcI8?t=525))
- **Compliance framing for a regulated EU bank: host the open weights on US/EU/UK-type infrastructure with zero retention. Keep coding tasks human-in-the-loop, enforced by a sandbox with per-command rules (allow grep, deny gradle). Use OpenTelemetry for incident forensics.** — He distinguishes downloaded weights from the China-hosted inference endpoint. He says a sandbox also guards against insider misuse. Prompt injection is called a smaller concern given model quality. ([9:50](https://youtu.be/Ok6QdZHCcI8?t=590))

## Techniques
- **Lead-time-first AI adoption metric** — Track per-engineer lead time (pickup to merge) and coding time in parallel, using a before/after cohort chart over model rollouts. Lead time is the headline metric. *When:* When justifying AI tooling spend or comparing models for an engineering org.
- **Latency-led GPU capacity planning** — Plot requests per second (demand) against TTFT (the optimised metric) over time on a fixed GPU count. Set an SLO of TTFT under 3 s, alert above 5 s, and tune before adding GPUs. *When:* Self-hosting a large model for an internal coding-agent population.
- **Serving parameter sweep** — Cap max context at 256K. Serve at FP4 on Blackwell (FP8 as fallback). Test TP8 vs TP4 against KV-cache headroom. Measure prefix-cache hit rate, targeting above 90% for coding. Evaluate speculative decoding and prefill optimisations. No config keys or flags are shown in the talk. *When:* Tuning an open-weight model on Blackwell GPUs for agentic coding traffic with long shared prefixes.
- **Local router for multimodal fallback** — Put a local OpenAI-compatible router in front of the text model. Send image-bearing requests to a vision model (Gemini or another vision model) and keep the main model for everything else. *When:* The primary coding model is text-only but users sometimes send screenshots or UI images.
- **Harness-agnostic OpenAI-compatible endpoint** — Expose the self-hosted model via OpenAI-compatible Responses API. Point OpenCode, Codex or the Codex app at it. *When:* You want to reuse existing coding-agent harnesses on a self-hosted model.
- **Sandbox with per-command allow/deny rules** — Run coding agents in a sandbox with an approval policy. Allow read-only tools like grep, deny build or deploy tools like gradle, and treat the agent as human-supervised rather than autonomous. *When:* Working in a regulated environment where auditors need evidence of human-in-the-loop control.
- **Compliance and telemetry baseline** — Host weights only in data-adequacy jurisdictions (US, EU, UK, Israel as named). Require zero data retention from GPU and inference providers. Instrument everything with OpenTelemetry so incidents can be traced. *When:* Deploying an AI coding tool for EU-regulated staff.

## Numbers
- Sample of 2,000 engineers analysed over the last year. ([1:16](https://youtu.be/Ok6QdZHCcI8?t=76))
- Gemini rollout: ~10% lead-time improvement and ~20% coding-time improvement. ([2:18](https://youtu.be/Ok6QdZHCcI8?t=138))
- Early Claude Code spend of roughly 1,000 to 10,000 a month per engineer with weak ROI (currency not stated). ([2:18](https://youtu.be/Ok6QdZHCcI8?t=138))
- Self-hosted GLM 5.1 (April): ~60% coding-time improvement and ~70% lead-time improvement. ([3:20](https://youtu.be/Ok6QdZHCcI8?t=200))
- 56 B200 GPUs serve about 2,000 engineers (GLM 5.x). The stated parameter count is garbled in captions and not reported here. ([4:24](https://youtu.be/Ok6QdZHCcI8?t=264))
- TTFT target under 3 s; complaints start above 5 s. Interactive speed about 200 tokens/s per user; about 800 tokens/s off-peak. ([4:24](https://youtu.be/Ok6QdZHCcI8?t=264))
- Blended cost of self-hosted GLM tokens is about $0.30 per million tokens. The invoice is about 1/10 of prior Anthropic and OpenAI spend. ([5:28](https://youtu.be/Ok6QdZHCcI8?t=328))
- On the same 56 GPUs: April ~3 req/s and TTFT over 10 s; August over 7 req/s and TTFT ~1.6 s. ([5:28](https://youtu.be/Ok6QdZHCcI8?t=328))
- Result: 88% performance improvement for 76% increased demand. ([6:32](https://youtu.be/Ok6QdZHCcI8?t=392))
- FP4 to FP8 costs about 40% more GPU footprint, with no measurable precision loss (speaker's claim). ([6:32](https://youtu.be/Ok6QdZHCcI8?t=392))
- Servable context is 1M tokens, but 256K is what the workload needs. ([6:32](https://youtu.be/Ok6QdZHCcI8?t=392))
- Prefix-cache hit rate for coding should be above 90%. ([7:39](https://youtu.be/Ok6QdZHCcI8?t=459))

## Hot takes
- The 90% headline is an invoice comparison (about 1/10 of prior Anthropic and OpenAI spend). It is not a like-for-like per-token or per-task comparison, and the baseline mix and utilisation are not disclosed.
- Lead-time gains are attributed to the model, but the talk gives no control group. Other process changes during the same period are not accounted for.
- Open models are presented as the cost-driven default, with frontier models kept as an exception. That is a cost and policy stance, not a quality claim.
- The China-data concern is dismissed on the basis that the weights are hosted on US infrastructure. That is the speaker's assessment, not a legal opinion, and it is aimed at a CIO audience.
- Caption errors in model names and parameter counts were not corrected where the intended value was unclear. Treat the GLM parameter count and the exact model versions as unverified.
- The talk is a 12-minute first-hand case study. It is valuable for real numbers, but it gives no hardware configs, flags or benchmark harness.

## Tools mentioned
GLM (GLM 5.1 and a later GLM 5.x model; caption reads 'GLM 5.3'), GLM-5 Flash (caption reads 'Glam5G Flash'), Gemini, Claude Code, Codex, Codex app, OpenCode (caption reads 'OpenCodex'), Anthropic API, OpenAI API, OpenAI Responses API (compatible endpoints), NVIDIA B200 GPUs, Blackwell GPUs, FP4 / FP8 precision, tensor parallelism (TP4, TP8), OpenTelemetry, gradle, grep, Jira, Confluence, Stack Overflow

## Relevance to our work
- **agentos** (2/3): InferCraft (L2B) runs vLLM on one RTX 5090. This talk gives the TTFT/RPS framing, the FP4 and TP tuning levers and the >90% prefix-cache target that InferCraft's benchmarks should measure. Scale and hardware differ. → *Add TTFT and requests/sec under a fixed-GPU load test, plus prefix-cache hit rate, as the InferCraft benchmark pass criteria. Compare TP4 and TP8 and FP4 and FP8 on the 5090.*
- **prosharness** (1/3): The harness wraps Claude Code and handles approvals. The talk's per-command allow/deny sandbox idea is a relevant but small addition. → *Review the harness approval policy so read-only commands like grep are auto-allowed and build or deploy commands like gradle require explicit approval.*
