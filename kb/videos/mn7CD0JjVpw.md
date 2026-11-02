# Best Local AI Models For Every VRAM Tier

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `mn7CD0JjVpw` · [watch](https://youtu.be/mn7CD0JjVpw) · **date:** 2026-09-02 · **length:** 10:20 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kai Explains host (name not stated in the transcript) · **orgs:** Microsoft, Google, Mistral, Anthropic, Hugging Face
- **topics:** local-ai, inference-serving, token-cost-efficiency · **tags:** local-llm, vram, quantization, ollama, lm-studio, kv-cache, context-length, moe, phi-4-mini, qwen, gemma, mistral, llama, hardware-tiers

> Tier-by-tier guide to local LLMs by GPU VRAM (4GB to 24GB+). Pick the biggest quantized model that fits with context headroom, and set the context length explicitly to avoid KV-cache crashes.

## Summary
The host argues that GPU VRAM, not model fame, decides which local model you can run, and walks through recommendations for 4GB, 6GB, 8GB, 16GB and 24GB cards. He frames the runtime (Ollama or LM Studio) as the software layer that matters, and explains quantization (Q4, Q8) as the trade that lets a 7B model fit in roughly 4.5GB instead of 14GB. Each tier lists one safe pick and one or two alternatives, with anecdotes about what failed (a 7B model spilling out of VRAM on 4GB, a small coder model hallucinating outdated SQLAlchemy APIs, Ollama crashing when the KV cache grew). The 8GB pick, Qwen 3.5 9B at Q4_K_M, is backed by his own benchmarks on an RTX 3070 and an Artificial Analysis index score. The video closes with a rule of thumb (run the biggest model that fits with room left for context) and an admission that local models still trail closed frontier models on coding tests.

## Key ideas
- **VRAM sets the model. Pick the model by memory tier, since a model that does not fit will choke regardless of its quality.** — The host says the one number that matters is GPU memory and organizes the video into 4GB, 6GB, 8GB, 16GB and 24GB tiers, each with a recommended model and a list of what fails. ([0:00](https://youtu.be/mn7CD0JjVpw?t=0))
- **The runtime is the software layer that determines the experience.** — A model is just a file on disk. Ollama wraps inference in a simple CLI (pull, then run), while LM Studio offers a GUI. He says either works and to pick one. ([0:00](https://youtu.be/mn7CD0JjVpw?t=0))
- **Quantization makes big models fit, with a quality cost. Prefer a smaller model at higher precision over a bigger one squeezed to Q2.** — A 7B model in 16-bit needs about 14GB just to load. Its Q4 version runs at around 4.5GB. He advises a small model at Q8 on weak machines, because a sharp small model beats a degraded big one. ([1:15](https://youtu.be/mn7CD0JjVpw?t=75))
- **At 4GB, small models are useful for summarization and simple code help, but larger models are not.** — Phi-4-mini (3.8B) is the main pick. He says it handles basic completion, explaining code and small bug fixes. He tried Mistral 7B at Q3 on a 4GB card, and it ran at 4-5 tokens per second and spilled from VRAM into RAM. ([2:29](https://youtu.be/mn7CD0JjVpw?t=149))
- **At 6GB, a 7B model is possible but context length is the constraint. Small coding models can confidently use outdated APIs.** — Phi-4-mini at Q5 is the no-risk pick at 15-30 tokens per second. Mistral 7B at Q3_K_M suits writing docs and commit messages. Qwen 2.5 7B at Q3_K_S was fine for boilerplate but hallucinated old SQLAlchemy methods while debugging a Flask app. ([4:52](https://youtu.be/mn7CD0JjVpw?t=292))
- **Set the context length explicitly when pulling a model. The default can grow the KV cache until the runtime crashes.** — He recommends capping context at 8k on 6GB cards. Pushing to 32k overflowed to RAM or crashed Ollama mid-session. He says this cost him several failed sessions to diagnose. ([4:52](https://youtu.be/mn7CD0JjVpw?t=292))
- **At 8GB, a 7-9B model at Q4_K_M is where local coding becomes practical. Qwen 3.5 9B is his pick based on his own tests.** — He benchmarked five models on an RTX 3070. Qwen 3.5 9B at Q4_K_M is about 6.6GB and stays fully in GPU memory at 32K context in his test. Llama 8B is the balanced alternative, and a Mistral Small model is the speed pick. ([6:14](https://youtu.be/mn7CD0JjVpw?t=374))
- **Use a separate small model for autocomplete, and keep the large chat model out of the editor's tab completion path.** — At 16GB he runs Qwen 3.6 27B at Q4_K_M for chat and a dedicated code-completion model for tab completion, with max prompt tokens set to 1024. Using the 27B model for autocomplete made his editor too slow. ([7:34](https://youtu.be/mn7CD0JjVpw?t=454))
- **Mixture-of-experts models make large coding models fit on bigger-memory machines, and the gap to a closed model is smaller than expected on SWE-bench.** — Qwen3-Coder-Next is an 80B MoE with about 3B active parameters. He says it needs roughly 45GB across RAM and GPU at 4-bit and gives a 256K context window. He cites 58.7% on SWE-bench Verified against 62.4% for Claude Sonnet 4.6. ([8:48](https://youtu.be/mn7CD0JjVpw?t=528))
- **Rule of thumb: run the biggest model that fits in memory with room left for context. He says the floor is rising fast.** — He acknowledges that the closed frontier sits around 90 on these coding tests, so local models still trail it. The message is that the best you can own is much better than what fit the same box six months earlier. ([8:48](https://youtu.be/mn7CD0JjVpw?t=528))

## Techniques
- **Pick the biggest model that fits with context headroom** — Compute the model's quantized size (e.g. 7B at Q4 is about 4.5GB, 9B at Q4_K_M is about 6.6GB), subtract the memory needed for your context window, and choose the largest model that still fits fully in GPU memory. Avoid spilling into RAM. *When:* Choosing a local model for a given GPU, before pulling anything.
- **Prefer a smaller model at higher precision** — On constrained hardware, use a small model at Q8 or Q5 rather than a larger model at Q2 or Q3. The host treats heavy quantization below Q4 as a noticeable quality loss. *When:* Machines with 4-8GB VRAM, where a 7B model at Q3 is the only way to fit a big model.
- **Set the context length explicitly at model load** — Do not rely on the runtime default. Specify the context length when pulling or loading the model, and cap it lower on small cards (he suggests 8k on 6GB). Larger contexts grow the KV cache and can overflow to RAM or crash the runtime. *When:* Any local-model session where the runtime might crash or slow down mid-session.
- **Split chat and autocomplete models** — Run a large model in the chat sidebar and a small dedicated code-completion model for tab completion. Cap the autocomplete prompt at about 1024 tokens to keep the editor responsive. *When:* Editor integration on a 16GB or larger GPU.
- **Use an MoE model on large-memory machines** — On a Mac Studio with large unified memory or a multi-GPU rig, load a mixture-of-experts coder model. Only a few billion parameters are active per token, so it is faster than a dense model of the same total size. *When:* Serious local coding on hardware with roughly 45GB or more of combined RAM and GPU memory.

## Numbers
- A 7B model in 16-bit needs about 14GB of RAM to load; its Q4 version runs at about 4.5GB. ([1:15](https://youtu.be/mn7CD0JjVpw?t=75))
- Phi-4-mini (3.8B) scores about 68% on MMLU and 70% on HumanEval (as stated by the host). ([2:29](https://youtu.be/mn7CD0JjVpw?t=149))
- Mistral 7B at Q3 on a 4GB card ran at 4-5 tokens per second and spilled out of VRAM. ([2:29](https://youtu.be/mn7CD0JjVpw?t=149))
- Phi-4-mini at Q5 on 6GB gives about 15-30 tokens per second. ([3:33](https://youtu.be/mn7CD0JjVpw?t=213))
- Pushing context to 32k on a 6GB tier overflowed to RAM or crashed Ollama; the host recommends an 8k cap. ([4:52](https://youtu.be/mn7CD0JjVpw?t=292))
- Qwen 3.5 9B at Q4_K_M is about 6.6GB and stays fully in GPU memory even at 32K context on an RTX 3070 (host's test). ([6:14](https://youtu.be/mn7CD0JjVpw?t=374))
- Qwen 3.5 9B scores 32.4 on the Artificial Analysis Intelligence Index, 38% above the runner-up at the 8GB tier. ([6:14](https://youtu.be/mn7CD0JjVpw?t=374))
- A Llama 8B fine-tune at Q4_K_M scores MMLU 73.0 and HumanEval 72.6 (as stated; uses slightly more RAM than Qwen 3.5 9B). ([6:14](https://youtu.be/mn7CD0JjVpw?t=374))
- Mistral Small scores 8.0 on MT-Bench (as stated by the host). ([6:14](https://youtu.be/mn7CD0JjVpw?t=374))
- Qwen3-Coder-Next (80B MoE, ~3B active) needs roughly 45GB across RAM and GPU at 4-bit, with a 256K context window and 58.7% on SWE-bench Verified. ([8:48](https://youtu.be/mn7CD0JjVpw?t=528))
- Claude Sonnet 4.6 scores 62.4% on SWE-bench Verified (as cited by the host). The closed frontier is said to sit around 90 on these coding tests. ([8:48](https://youtu.be/mn7CD0JjVpw?t=528))

## Hot takes
- The small-model failure mode (hallucinating outdated library APIs with confidence) matters more for coding than any benchmark score the video quotes.
- The 8GB pick rests on the host's own benchmarks on one RTX 3070, and the 16GB and 24GB tiers rest mainly on his personal setup. Treat the specific numbers as anecdotal until reproduced.
- Model names and version numbers are garbled in the auto-captions (e.g. 'QN 3.59B', 'Alama', 'Fi4mini', 'Kadastral'). Verify exact names and quantization tags on Hugging Face or in Ollama before pulling anything.
- The 'floor is rising' and 'run the biggest model that fits' framing is practical advice rather than a new technique, and the video is light on methodology for the benchmark claims.

## Tools mentioned
Ollama, LM Studio, llama.cpp (spoken as 'llama'; context-length crash anecdote), Phi-4-mini, Gemma 4 E2B (Gemma 4 family, ~April 2026 per the host), Qwen 2.5 7B, Qwen 3.5 9B, Qwen 3.6 27B, Qwen3-Coder-Next (80B MoE, ~3B active), Mistral 7B, Mistral Small, Llama 8B (captions read 'Llama 3.38b'), Hugging Face, Flask, SQLAlchemy, RTX 3070, RX 9060 XT (16GB, the host's own card), RTX 4090 / RTX 4080 (24GB), Mac Studio (unified memory), Artificial Analysis Intelligence Index, MT-Bench, MMLU, HumanEval, SWE-bench Verified, Claude Sonnet 4.6

## Relevance to our work
- **agentos** (1/3): Local inference and KV-cache sizing are relevant to InferCraft on a single RTX 5090. The video's point is that context length must be an explicit setting, and that a default can crash the runtime. Only tangentially relevant, since the video targets much smaller GPUs. → *Make max context length an explicit, budgeted config value in InferCraft's serving setup (not a runtime default), and log KV-cache growth against it, since the video reports crashes from unbudgeted KV-cache growth.*
