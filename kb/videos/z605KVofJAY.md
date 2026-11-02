# 10 Best Local Coding Models Right Now 2026

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `z605KVofJAY` · [watch](https://youtu.be/z605KVofJAY) · **date:** 2026-09-02 · **length:** 13:11 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed host (Kai Explains channel) · **orgs:** Z.ai (ZAI), Moonshot AI, DeepSeek, Alibaba (Qwen), Mistral AI, OpenAI, AMD, Continue, Ollama, LM Studio, llama.cpp, GitHub
- **topics:** local-ai, models-research, coding-agents, inference-serving · **tags:** local models, open-weight, coding models, hardware sizing, VRAM, quantization, fill-in-the-middle, autocomplete, tool calling, Apache 2.0, SWE-bench, Continue.dev, Ollama, cheap API pricing

> Kai Explains lists 10 open coding models split by hardware tier and task type, and argues that picking a model for your own hardware and job matters more than leaderboard rank.

## Summary
The host opens with a failed attempt to run a 37 GB model on a 24 GB GPU, then argues that the best coding model and the best model you can actually run are different questions. He says to answer two questions first: what hardware you have (a 24 GB consumer card, a 64/96 GB Apple Silicon machine, a 128 GB Strix Halo box, or a laptop that stays on API), and what kind of work you do (sub-second autocomplete, multi-step agentic issue fixing, or large-context refactoring). The frontier-class open models (GLM 5.3, Kimi K2.7, DeepSeek V4 Pro and Flash, Qwen3-Coder 480B, Kimi K3) are presented as API-only for most people, with pricing and context-window claims. The locally runnable picks are Qwen3-Coder-Next, Qwen3.6 27B (his daily driver), Devstral Small 2 (for strict tool calling), and GPT-OSS-20B. He then makes the key point that autocomplete needs fill-in-the-middle training, not chat or agent models, and recommends Codestral 2 wired into Continue.dev, with Qwen 2.5 Coder 14B for smaller hardware. The numbers are the speaker's own recollections and leaderboard quotes, with no benchmark method shown.

## Key ideas
- **Pick a model by hardware first. A top leaderboard model is often too big to run locally; the speaker's 37 GB model did not load on a 24 GB GPU.** — Split the question into what you can run (VRAM or unified memory ceiling) and what is best overall. The speaker says these answers have little overlap. ([0:00](https://youtu.be/z605KVofJAY?t=0))
- **Hardware tiers set the ceiling. A consumer 24 GB card is the local ceiling for most people, Apple Silicon is capped at 64/96 GB, and 128 GB unified memory means Strix Halo (Ryzen AI Max+ 395) at about $3,999.** — Anything bigger than these tiers, or a laptop, means API use. Multi-GPU clusters are for corporate accounts. ([1:20](https://youtu.be/z605KVofJAY?t=80))
- **Autocomplete, agentic issue fixing and large-context refactoring need different models. Autocomplete needs sub-second first-token latency, agentic work needs planning and tool reliability, and refactoring needs a long context that does not forget early files.** — A deep-reasoning model is too slow for tab completion, and a fast completion model is too shallow for system design. ([2:30](https://youtu.be/z605KVofJAY?t=150))
- **Frontier open models are cheap to rent. GLM 5.3 gains come from post-training, not a new base model, and Kimi K2.7 was trained on compiler and test-failure trajectories so that errors become signals to retry.** — The speaker cites GLM 5.3 Deep SWE going from 46.2 to 66.9 and SWE Marathon from 19.4 to 42.5. He claims Kimi K2.7 is a trillion-parameter, 32B-active model. ([3:42](https://youtu.be/z605KVofJAY?t=222))
- **Pricing is the reason to use DeepSeek V4 for bulk work. Flash is cheap enough for high-volume log, documentation and CI analysis, and both Pro and Flash have 1M context under MIT.** — Quoted prices: Pro $0.435 per million input tokens; Flash $0.14 input and $0.28 output. ([5:09](https://youtu.be/z605KVofJAY?t=309))
- **License matters for shipping commercially. Qwen3-Coder (480B, 69.6% SWE-bench Verified) is Apache 2.0, so there is no custom license or revenue-threshold clause to review.** — The speaker contrasts it with open-weight models that restrict commercial use. ([6:12](https://youtu.be/z605KVofJAY?t=372))
- **The local daily driver is a single-card dense model. Qwen3.6 27B (Apache 2.0, April 2026) needs about 17 GB at Q4 and runs through Ollama with community GGUF quants. Vision needs a separate mmproj file served via llama.cpp or LM Studio.** — Qwen3-Coder-Next runs at about 46 GB at 4-bit on a 64/96 GB Mac or 128 GB Strix Halo, with 3B active parameters per token. ([7:39](https://youtu.be/z605KVofJAY?t=459))
- **Tool-call reliability is a separate choice. Devstral Small 2 (24B dense, 256K context, fits 24 GB at Q4) is picked for strict JSON and function calling in scripts and agent frameworks, not for raw capability.** — Ollama can serve it the same way as the Qwen models. ([9:00](https://youtu.be/z605KVofJAY?t=540))
- **Autocomplete needs fill-in-the-middle (FIM) training, not chat or agent training. FIM sees the code above and below the cursor. The open answer is Codestral 2 (Apache 2.0, April 2026) in Continue.dev, with Qwen 2.5 Coder 14B (about 9.5 GB at Q4) for smaller hardware.** — The speaker says his local setup matches GitHub Copilot in quality with lower latency and no subscription, after two years on Copilot. This is anecdotal. ([10:02](https://youtu.be/z605KVofJAY?t=602))

## Techniques
- **Hardware-first model sizing** — Measure VRAM or unified memory first. Check the weight size at the quantization you plan to use (speaker's figures: about 17 GB for Qwen3.6 27B at Q4, about 46 GB for Qwen3-Coder-Next at 4-bit, about 14 GB for GPT-OSS-20B) and leave room for context before you download anything. *When:* Before downloading any local model, and before picking from a leaderboard.
- **Route models by job, not one model for everything** — Use a small FIM model for editor autocomplete (latency in milliseconds), a reasoning or agent model for multi-step issue-to-fix loops, a long-context model for large refactors, and an API model for the hardest architecture work. *When:* When setting up a mixed workflow across editor, agent and batch use.
- **Local tab completion with Continue.dev and a FIM model** — Install Continue, an open-source VS Code and JetBrains extension. Point it at a local FIM-trained model such as Codestral 2 for autocomplete. Use Qwen 2.5 Coder 14B if the hardware is smaller (about 9.5 GB at Q4). *When:* Replacing a subscription tab-completion tool such as GitHub Copilot with a local setup.
- **Running Qwen3.6 27B on one 24 GB card** — Pull a community GGUF build with Ollama for text coding work. For native vision, load the separate mmproj file and serve the model through llama.cpp or LM Studio instead, since the speaker says Ollama does not handle the vision file. *When:* Solo development on a single 24 GB consumer GPU, for refactoring, tests, code review and explaining unfamiliar code.
- **Pick for tool-call reliability** — For a local model that must emit strict JSON or call functions from a script or agent framework, choose Devstral Small 2 over a higher-capability model of similar size. *When:* Building agentic pipelines that depend on schema-compliant output.
- **Filter by license before commercial use** — Shortlist Apache 2.0 or MIT models (the speaker names Qwen3-Coder, Qwen3.6 27B, Codestral 2, DeepSeek V4) before any legal review. *When:* Choosing a model for a product you will ship commercially.
- **Cheap hosted model for bulk processing** — Send high-volume logs, documentation and CI pipeline text to DeepSeek V4 Flash through the API, where the speaker's quoted per-token prices make the cost small. *When:* Offline batch jobs where volume matters more than frontier reasoning.

## Numbers
- A 37 GB model would not load on a 24 GB GPU (the speaker's own failed attempt). ([0:00](https://youtu.be/z605KVofJAY?t=0))
- Consumer RTX 4090 or 5090 gives about 24 GB VRAM. Apple Silicon Mac Studio capped at 64/96 GB unified memory. Strix Halo 128 GB at about $3,999. ([1:20](https://youtu.be/z605KVofJAY?t=80))
- GLM 5.3: 743B total parameters, 40B active per token, 1M context. Deep SWE 46.2 to 66.9; SWE Marathon 19.4 to 42.5. ([3:42](https://youtu.be/z605KVofJAY?t=222))
- Kimi K2.7: about a trillion total parameters, 32B active per token. ([5:09](https://youtu.be/z605KVofJAY?t=309))
- DeepSeek V4 Pro $0.435 per million input tokens. V4 Flash $0.14 input and $0.28 output per million tokens. Both have 1M context under MIT. ([5:09](https://youtu.be/z605KVofJAY?t=309))
- Qwen3-Coder (480B): 69.6% on SWE-bench Verified, Apache 2.0. ([6:12](https://youtu.be/z605KVofJAY?t=372))
- Kimi K3: 2.8 trillion total parameters, 1M context, weights released July 26, 2026 (speaker's date). ([6:12](https://youtu.be/z605KVofJAY?t=372))
- Qwen3-Coder-Next: about 46 GB unified memory at 4-bit; 3B active parameters per token (described as an 80B-class model). ([7:39](https://youtu.be/z605KVofJAY?t=459))
- Qwen 3.6 27B: about 17 GB at Q4, released April 2026 under Apache 2.0, 27B dense. ([7:39](https://youtu.be/z605KVofJAY?t=459))
- Devstral Small 2: 24B dense parameters, 256K context, fits a 24 GB card at Q4. ([9:00](https://youtu.be/z605KVofJAY?t=540))
- GPT-OSS-20B: 21B total parameters, 3.6B active per token, about 14 GB VRAM. ([10:02](https://youtu.be/z605KVofJAY?t=602))
- Qwen 2.5 Coder 14B: about 9.5 GB at Q4 (autocomplete alternative). ([11:28](https://youtu.be/z605KVofJAY?t=688))
- Codestral 2: released April 2026 under Apache 2.0 with native FIM support. Speaker says it matches Copilot quality locally, based on his own use. ([11:28](https://youtu.be/z605KVofJAY?t=688))
- Conclusion cites Qwen 3 Coder Next at 70.6 on SWE-bench, which differs from the 69.6 quoted for Qwen3-Coder (480B) earlier. ([12:42](https://youtu.be/z605KVofJAY?t=762))

## Hot takes
- The most useful idea is the split of hardware tier and job type, with fill-in-the-middle training for autocomplete. The model roster is a snapshot that will age quickly.
- Most numbers are speaker-quoted leaderboard figures with no benchmark method shown. The SWE-bench figures for Qwen3-Coder (69.6) and Qwen3-Coder-Next (70.6) are not reconciled.
- The claim that Codestral 2 matches Copilot and that Qwen3.6 handles 80% of daily tasks is one developer's anecdote, not a measurement.
- Several model names and specs come from auto-captions and need checking against primary sources before use (for example Kimi K2.7 vs K3 naming and the Qwen3.6 27B details). Quality is capped by this, though the framing is practitioner-grade.

## Tools mentioned
GLM 5.3, Kimi K2.7, Kimi K3, DeepSeek V4 Pro, DeepSeek V4 Flash, Qwen3-Coder (480B), Qwen3-Coder-Next, Qwen 3.6 27B, Qwen 2.5 Coder 14B, Devstral Small 2, GPT-OSS-20B, Codestral 2, Ollama, llama.cpp, LM Studio, Continue.dev, GitHub Copilot, VS Code, JetBrains IDEs, AMD Ryzen AI Max+ 395 (Strix Halo), SWE-bench Verified, Deep SWE, SWE Marathon

## Relevance to our work
- **agentos** (2/3): InferCraft runs on a single RTX 5090 and needs model choices by job. The video's hardware-tier framing and its split between FIM, agentic and long-context models fit that. Its tool-call reliability pick (Devstral Small 2) matters for InferCraft, and the job-based routing idea maps to Govrix strategy routing (L1). The speaker's figures are unverified. → *Run a tool-call JSON reliability eval on our RTX 5090 comparing Devstral Small 2 and Qwen3.6 27B at Q4 (plus GPT-OSS-20B), using our own evals rather than the video's numbers.*
