# Llama-Swap: This Fixes The Most Annoying Local LLM Problem

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `GtTzO5ZOQr4` · [watch](https://youtu.be/GtTzO5ZOQr4) · **date:** 2026-06-02 · **length:** 6:09 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** local-ai, infra-cost-scaling · **tags:** llama-swap, llama.cpp, local-llm, model-swapping, ttl-unload, openai-compatible, anthropic-compatible, reverse-proxy, ollama, lm-studio, vllm, tabbyapi, cursor, open-webui

> Better Stack walkthrough of llama-swap, a single Go proxy that exposes one OpenAI/Anthropic-compatible endpoint and starts, swaps and TTL-unloads local model backends based on the request's model field.

## Summary
The host argues that once you outgrow Ollama or LM Studio and move to raw llama-server for control over flags and GPU layers, you end up killing and restarting servers and changing base URLs whenever you switch models. llama-swap puts one stable endpoint in front of several backends: the client changes only the model field, and the proxy waits for the right backend to be healthy, stops whatever must yield, and forwards the request. Each model in its YAML config has its own launch command, model file, context size and TTL, and an idle model is unloaded after its TTL so VRAM is freed. It is a single Go binary with a YAML config, proxies OpenAI- and Anthropic-compatible APIs, and can front llama.cpp, vLLM and TabbyAPI. The host is clear that it is not a model store, downloader or GUI, and that the setup (model files, backend knowledge, YAML, GPU flags) is heavier than Ollama. The video is a short, demo-level overview with no benchmarks, and the exact YAML keys are not shown on screen.

## Key ideas
- **One stable endpoint, many local models: clients keep the same base URL and switch models by changing the model field in the request.** — The proxy checks the model field, waits for that backend to be healthy, or starts it, and stops any model that must yield before forwarding. ([2:02](https://youtu.be/GtTzO5ZOQr4?t=122))
- **Raw llama-server tuning forces you to kill and restart servers and rewire clients on every model change, and that is the problem the proxy solves.** — The host says the wait, reconnect or silent wrong-model failures are the real cost of bouncing between models, not the model choice itself. ([0:59](https://youtu.be/GtTzO5ZOQr4?t=59))
- **Per-model config holds the launch command, model file, context size and TTL, so the config remembers what should run.** — An idle model past its TTL is unloaded to free VRAM, which matters when you have more models on disk than VRAM to hold them. ([2:02](https://youtu.be/GtTzO5ZOQr4?t=122))
- **TTL-based unloading addresses the case of many models on disk but only enough VRAM for one or two loaded at once.** — Idle models are unloaded so the GPU is not stuck holding a model nobody is using. ([3:11](https://youtu.be/GtTzO5ZOQr4?t=191))
- **Positioning: llama-swap is server-first control, not a beginner tool. It is not a model store, downloader or GUI, unlike Ollama and LM Studio.** — You bring your own llama.cpp build and flags. It fits a dev box, homelab, Docker or shared machine where tools need a stable API. ([4:19](https://youtu.be/GtTzO5ZOQr4?t=259))
- **The setup cost is real: you need model files, backend knowledge, YAML and GPU-appropriate flags.** — The host recommends it for people who know exactly which model they want and are tired of rewiring, and for users of Cursor, Continue, custom agents or scripts. ([5:26](https://youtu.be/GtTzO5ZOQr4?t=326))

## Techniques
- **Single front-door proxy for multiple local model servers** — Run the llama-swap binary with one YAML config. Each model entry gets its own launch command, model file, context size and TTL. Point every OpenAI-compatible or Anthropic-compatible client at the proxy's port and select a model by setting the model field in the request. The video does not show exact YAML key names or the port flag, so check the project README for those. *When:* You run several local models of different sizes (for example a large coding model and a small chat or embedding model) on one GPU and want clients to stay unchanged while you switch models.
- **TTL-based idle unloading** — Set a TTL on each model entry. When a model has been idle longer than its TTL, the proxy unloads it and frees its VRAM. The next request for that model starts it again and waits until it is healthy. *When:* Your models are on disk in larger number than your VRAM can hold, and bursts of use are separated by idle periods.
- **Per-model backend control** — Put the exact llama-server (or vLLM or TabbyAPI) command, flags, GPU layer placement and context size in each model's entry, rather than relying on a model store to choose them. *When:* You need precise control over how each model launches and do not want a GUI or an automatic downloader.

## Numbers
- Example config defines two models, each with its own command, model file, context size and TTL. ([2:02](https://youtu.be/GtTzO5ZOQr4?t=122))

## Hot takes
- The video is a short demo with no benchmarks, so swap or cold-start latency is not quantified.
- The host says llama-swap is not for beginners, and the setup cost is high compared with Ollama or LM Studio.
- The video runs about 6 minutes and shows the config at a high level only, without the exact YAML keys.

## Tools mentioned
llama-swap, llama.cpp (llama-server), Ollama, LM Studio, vLLM, TabbyAPI, Open WebUI, Cursor, Continue, Qwen coder (transcript: 'quen-coder'), small-lm2 (name as spoken in the config example)

## Relevance to our work
- **agentos** (1/3): AgentOS's L2B InferCraft is a vLLM plus Ray Serve setup on one RTX 5090. llama-swap's single endpoint with per-model TTL unload is a local multi-model pattern worth comparing against that setup, but it does not change the design. → *Compare llama-swap's per-model TTL unload and single-endpoint model switching with the current vLLM and Ray Serve setup before adding any model-switching code.*
