# Laguna S 2.1: The Best Local Model? Beats GLM 5.2

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `YRlM9V_3mR8` · [watch](https://youtu.be/YRlM9V_3mR8) · **date:** 2026-08-02 · **length:** 9:54 · **format:** review · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kai (host of Kai Explains; name not stated in the transcript) · **orgs:** Poolside, NVIDIA, Anthropic, DeepSeek, GitHub (Jason Warner's former employer, mentioned)
- **topics:** local-ai, models-research, inference-serving, token-cost-efficiency · **tags:** laguna-s-2.1, poolside, mixture-of-experts, open-weights, local-llm, dgx-spark, llama-cpp, expert-offload, gguf, iq4_xs, swe-bench, coding-agents, openmdw-license, glm-5.2, benchmarks

> Kai reviews Poolside's Laguna S 2.1, an open-weight 118B MoE model with 8B active that runs on one desktop-class box; it beats GLM 5.2 on some coding benchmarks but not all, and the launch numbers are unverified.

## Summary
The video reviews Poolside's Laguna S 2.1, a 118B-parameter mixture-of-experts model that activates about 8B parameters per token and has a 1M-token context. The speaker reports it leads open models on SWE-Bench Multilingual (78.5%) and a hard agentic benchmark (40%, or 16% without max thinking), and beats a 1.6T DeepSeek model on that agentic benchmark and on code-QA. It does not beat GLM 5.2 across the board: GLM wins the terminal-tasks and "WE Pro" benchmarks by a few points each. The local pitch is that a 4-bit build (about 59 GB) fits on one NVIDIA DGX Spark at 50 to 77 tokens/s, and an IQ4_XS GGUF can run on 64 GB RAM plus a 12 GB GPU by pushing expert layers to system RAM with llama.cpp. The speaker frames local hosting as a fixed hardware cost versus per-token API pricing, with code staying on-premises. Caveats he stresses: every number is Poolside's own and was not independently reproduced at launch, Claude still leads on terminal tasks (88 vs 70), and the model must be tested on your own codebase before trust. He also covers the company's funding and a fast training run (under nine weeks on about 4,000 H200s, the first Poolside run with RL and 8-bit training).

## Key ideas
- **Open-weight models finally offer frontier-adjacent coding quality that you can self-host; the speaker argues the West is back in the open race by going small.** — Previously the best downloadable models came from Chinese labs (GLM, DeepSeek, Qwen, Kimi). Laguna S 2.1 is pitched as Western, self-hostable, and under the OpenMDW license, which permits shipping products. ([0:00](https://youtu.be/YRlM9V_3mR8?t=0))
- **The small-active-parameter trick is mixture of experts: a router wakes about 8B of 118B parameters per generated token.** — Only about 7% of weights fire per token, so the model carries the memory of a large model but pays the running cost of a small one. It also reads a 1M-token context in one shot, so a whole repo can be held at once. ([2:47](https://youtu.be/YRlM9V_3mR8?t=167))
- **On multilingual bug fixing and some agentic and code-QA benchmarks, Laguna beats much larger open models, including a 1.6T DeepSeek.** — Reported: SWE-Bench Multilingual 78.5% (first among open models tested, GLM included); hard agentic 40% vs DeepSeek 9%; code-QA 46 vs DeepSeek 27. The speaker says the small model keeps winning when the task rewards understanding over raw size. ([2:47](https://youtu.be/YRlM9V_3mR8?t=167))
- **It is a split decision with GLM 5.2, not a knockout: GLM wins the two benchmarks people quote first by a few points.** — Terminal tasks GLM 81 vs Laguna 70; the 'WE Pro' benchmark GLM 62 vs Laguna 59. GLM is about 740B total with roughly five times the active parameters. Laguna does reach within a few points of a model six times its size. ([4:13](https://youtu.be/YRlM9V_3mR8?t=253))
- **Max thinking mode is a tunable quality-vs-token trade: hard agentic score rises from 16% to 40% at roughly 2.5x the tokens.** — The speaker presents this as a second gear for hard tasks; the cost is the token burn. ([4:13](https://youtu.be/YRlM9V_3mR8?t=253))
- **Local hosting is framed as a one-time hardware cost against per-token API pricing and rate limits, and the code never leaves the machine.** — The speaker's example is a DGX Spark (about $4,000, 128 GB unified memory) running the 4-bit model at 50 to 77 tokens/s with room left for a large context. He also says 16 GB of system RAM is not enough for the RAM-offload route. ([5:33](https://youtu.be/YRlM9V_3mR8?t=333))
- **Honest caveats: every benchmark is self-reported and unreproduced at launch, the model trails the closed frontier, and a benchmark is not your codebase.** — Claude beats it on terminal tasks (88 vs 70). He recommends running it on your own work for a week before trusting it with anything important. ([8:13](https://youtu.be/YRlM9V_3mR8?t=493))

## Techniques
- **Run a MoE model that exceeds VRAM by offloading expert layers to system RAM (llama.cpp)** — Use the IQ4_XS GGUF (57.6 GB file). Set the llama.cpp MoE CPU-offload option to 46 (the caption reads 'ncpmo set to 46', most likely --n-cpu-moe 46), which keeps 46 expert layers in system RAM and the rest on the GPU. Budget about 62 GB usable system RAM plus about 12 GB VRAM. VRAM also holds the KV cache and compute buffers, so leave headroom. The speaker does not show the full command line. *When:* You have a 12 GB-class GPU and about 64 GB of RAM and want to avoid buying a 128 GB box. Not viable with 16 GB RAM.
- **Single-box 4-bit serving on unified memory** — Quantize to 4-bit (about 59 GB for Laguna S 2.1) and serve on a 128 GB unified-memory machine (DGX Spark). Day-one runtimes named: Ollama (captioned 'Alama'), vLLM, SGLang, plus hosted OpenRouter. *When:* You want a fully offline coding model with a large context on one desk-sized machine.
- **Enable max thinking only for hard agentic tasks** — Turn on the max thinking mode for hard tasks and expect roughly 2.5x the tokens; keep the default mode for routine edits. *When:* Per-task selection when quality on hard agentic work matters more than token cost.
- **Test an open model on your own repo before adopting it** — Run the candidate on a week of real work (your frameworks and conventions) and compare against your current model rather than trusting leaderboard numbers. *When:* Before using any new model, especially for work where a faceplant matters.

## Numbers
- Laguna S 2.1: 118B total parameters, about 8B active per token (about 7%), 1M-token context. ([0:00-2:47](https://youtu.be/YRlM9V_3mR8?t=0))
- SWE-Bench Multilingual 78.5%, first among open models tested, including GLM. ([2:47](https://youtu.be/YRlM9V_3mR8?t=167))
- Hard agentic benchmark 40% (vs DeepSeek 1.6T at 9%). 16% without max thinking; max thinking uses about 2.5x tokens. ([2:47-4:13](https://youtu.be/YRlM9V_3mR8?t=0))
- Code-QA 46 for Laguna vs 27 for the 1.6T DeepSeek. ([2:47](https://youtu.be/YRlM9V_3mR8?t=167))
- Terminal tasks: GLM 5.2 81 vs Laguna 70. 'WE Pro': GLM 62 vs Laguna 59. Claude terminal tasks 88 vs Laguna 70. ([4:13 and 8:13](https://youtu.be/YRlM9V_3mR8?t=0))
- GLM 5.2 about 740B total, about 5x Laguna's active parameters. ([4:13](https://youtu.be/YRlM9V_3mR8?t=253))
- DGX Spark about $4,000, 128 GB unified memory; 4-bit Laguna about 59 GB; 50 to 77 tokens/s. ([5:33](https://youtu.be/YRlM9V_3mR8?t=333))
- IQ4_XS GGUF file 57.6 GB; needs about 62 GB usable system RAM and 12 GB VRAM for the offload route. ([5:33](https://youtu.be/YRlM9V_3mR8?t=333))
- Training: under nine weeks on roughly 4,000 H200 GPUs, 30T tokens; first run with RL and 8-bit precision. ([6:49](https://youtu.be/YRlM9V_3mR8?t=409))
- Poolside raised over $600M; NVIDIA put in up to $1B more, valuation around $12B (last October). ([6:49](https://youtu.be/YRlM9V_3mR8?t=409))

## Hot takes
- The West is back in the open-weight race, and going small is the winning design choice.
- For agent-heavy users, a local model's fixed hardware cost beats per-token API pricing and rate limits.
- Launch benchmarks are a claim, not a result, until third parties reproduce them (speaker's own caveat).
- The honest verdict is a split decision with GLM 5.2, not a clean win.

## Tools mentioned
Laguna S 2.1 (Poolside, open weights, OpenMDW license), Laguna XS (tinier sibling; captioned 'XS5'), GLM 5.2 (Chinese open model, about 740B), DeepSeek (largest model cited, about 1.6T), Qwen and Kimi (named as Chinese open-model families), Claude (Anthropic, closed frontier comparison), NVIDIA DGX Spark (128 GB unified memory desktop), llama.cpp (GGUF, IQ4_XS quant, expert-layer offload), Ollama (captioned 'Alama'), vLLM, SGLang, OpenRouter (hosted)

## Relevance to our work
- **agentos** (2/3): InferCraft (L2B) already serves local models with vLLM on one RTX 5090. This video gives a concrete open-weight MoE candidate and an expert-offload recipe, which fits InferCraft's serving and scheduler work. → *Add Laguna S 2.1 to the InferCraft vLLM benchmark matrix, and measure expert-offload throughput on the 32 GB RTX 5090 (the 59 GB 4-bit build does not fit there without offload; the speaker's numbers were on a 128 GB box).*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, so a local model would only help cheap side steps (summaries, classification) if it ever runs non-Claude steps. This is a weak fit. → *Note Laguna S 2.1 as a zero-token local option for cheap sub-steps; verify tool calling on one of our repos before any use.*
