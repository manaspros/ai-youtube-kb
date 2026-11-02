# Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `OV56RddyFuU` · [watch](https://youtu.be/OV56RddyFuU) · **date:** 2026-05-18 · **length:** 19:11 · **format:** demo · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Merve Noyan · **orgs:** Hugging Face
- **topics:** local-ai, training-finetuning-rl, mcp-and-tools, coding-agents · **tags:** open-weights, hugging-face, hermes-agent, local-inference, gguf, agent-driven-training, traces-dataset, ocr-batch, skills, mcp

> Hugging Face's Merve Noyan demos open-model agent workflows: picking and serving open models, Hermes Agent, pushing agent traces to the Hub, HF MCP server and skills that let coding agents launch fine-tuning and batch OCR jobs.

## Summary
Merve Noyan of Hugging Face argues that open weights and open harnesses give visibility, privacy and control, and that open models now compete with closed ones (she cites GLM 5.1 on the Artificial Analysis index). She walks through Hub features for choosing models: benchmark datasets, Inference Providers for comparing hosts on cost and speed, and "Use this model" buttons that show local serving commands. For local agents she demos Pi on llama.cpp and Hermes Agent with open models, and she says a new Hub "traces" dataset type can host coding-agent session logs (Claude Code, Codex, Pi) for exploration or later training. The main pitch is HF skills and the HF MCP server: the agent asks a few questions, estimates VRAM and cost, and launches a remote training or OCR job whose output lands back on the Hub. The talk is largely product tour, with some concrete workflow detail and a few unverified anecdotes.

## Key ideas
- **Open weights and open harnesses make agent behavior auditable** — She argues that with open weights and an open harness you notice silent quality changes (she alludes to a recent reported Claude performance drop), can quantize or fine-tune, and can run on edge or in-browser for privacy. ([0:56](https://youtu.be/OV56RddyFuU?t=56))
- **Open models are presented as now competitive with closed ones** — Her claim is that open models are catching up; she points to GLM 5.1 on the Artificial Analysis index and says she uses it in her own coding setup. ([2:17](https://youtu.be/OV56RddyFuU?t=137))
- **Vision-language models are arriving day zero with vision built in** — Recent labs release multimodal models at launch (she names Gemma 4, Qwen 3.5, Kimi K2.5). Serving them takes only a few lines with vLLM, MLX or llama.cpp. ([3:31](https://youtu.be/OV56RddyFuU?t=211))
- **Pick models by benchmark and by provider, not by guesswork** — Hub benchmark datasets show ranked scores (SWE-bench, HLE, AIME). Inference Providers route to hosts such as Groq, Cerebras and Novita, and you can compare cheapest or fastest. ([4:40](https://youtu.be/OV56RddyFuU?t=280))
- **Local coding agents run from a Hub ID with little setup** — Pi can consume a model served by llama.cpp. llama.cpp also ships a built-in agent binary that starts a model directly from a Hugging Face Hub ID. ([6:41](https://youtu.be/OV56RddyFuU?t=401))
- **Agent session traces can be published as a dataset** — A new Hub dataset type called traces accepts uploaded session logs from coding agents. The dataset viewer parses them, and the logs can later be used for training. She says Hermes Agent support is coming. ([8:57](https://youtu.be/OV56RddyFuU?t=537))
- **Agents can pick a model, estimate resources and launch the job** — For the OCR case, the agent picks a model, writes the processing script, estimates instance size and cost, and launches the run on Hugging Face infrastructure. The skill sets up the serving instance without the user doing the sizing by hand. ([16:21](https://youtu.be/OV56RddyFuU?t=981))
- **Benchmark leaders may not be the right fine-tuning base** — The top OLMOCR-Bench entry is not automatically the best choice to fine-tune. A dedicated skill answers which OCR model to start from, including smaller options. ([17:31](https://youtu.be/OV56RddyFuU?t=1051))

## Techniques
- **Hub-ID local serving for coding agents** — Serve the model with llama.cpp (or use its built-in agent binary by pointing it at a Hub ID), then point Pi at the local endpoint. *When:* You want a fully local coding agent on your own GPU without writing serving config.
- **GGUF hardware-fit check before download** — On the Hub model page, read the GGUF section and hardware compatibility table to see whether a quantized variant fits your VRAM. She gives the example of a larger Gemma 4 at 4-bit fitting a 24 GB L4. *When:* Choosing a quantization level for a fixed GPU budget.
- **Agent-driven fine-tuning via skills** — Install the LLM trainer skill, then tell the coding agent to train a named model on a named dataset. The agent asks for details such as validation split, works out VRAM and batch size, launches the remote job, and the result appears on the Hub. *When:* You want a fine-tune run kicked off from a chat-style request, with the agent handling sizing and launch.
- **Session traces pushed to a Hub dataset** — Upload Claude Code, Codex or Pi session directories to a traces dataset repo. The viewer parses the sessions so they can be explored and later used as training data. *When:* You want a shareable corpus of your agent sessions for inspection or future training.
- **Corpus OCR via prompted batch job** — Pick a cheap OCR model from a benchmark, have the agent write the processing script, let it compute instance cost, then run the job remotely and write results back for indexing. *When:* You need to convert a large set of PDFs or papers to Markdown in one batch with a small model.
- **HF MCP server for catalog access** — Connect the Hub MCP server to get search and access over models, datasets, Spaces and jobs. Spaces can be called as tools, for example an image-generation Space. Enable the experimental dynamic-spaces setting for wider Space access. *When:* An agent needs to discover or invoke Hub resources during a task.

## Numbers
- Hugging Face Hub hosts close to 3 million models (speaker's estimate, she says she should have updated the figure) ([2:17](https://youtu.be/OV56RddyFuU?t=137))
- A larger Gemma 4 quantized to 4-bit fits on an L4 GPU with 24 GB VRAM ([10:15](https://youtu.be/OV56RddyFuU?t=615))
- GLM 5.1 is currently top of the open-model list on the SWE-bench benchmark dataset view on the Hub ([4:40](https://youtu.be/OV56RddyFuU?t=280))
- Corpus of roughly 30,000 AI papers used as the OCR batch-job example (transcript reads '30 30 000 papers', so the count is approximate) ([16:21](https://youtu.be/OV56RddyFuU?t=981))

## Hot takes
- Open models are now roughly at parity with closed ones, and the gap keeps closing.
- Open weights and open harnesses are the only way to be sure nothing changes without you knowing.
- Vision-language capability will arrive at launch for most new models.
- Top-ranked OCR benchmark entries should not be trusted as the default base for fine-tuning.

## Tools mentioned
Hugging Face Hub, Hugging Face MCP server, Hugging Face skills (hub CLI, LLM trainer, Gradio, dataset), Inference Providers, Hermes Agent, Pi, llama.cpp, vLLM, MLX, LM Studio, Claude Code, Codex, Gradio, OLMOCR-Bench, Qwen, GLM 5.1, Gemma 4

## Relevance to our work
- **general** (2/3): Cheap open OCR model plus agent-written script plus cost estimate matches our cheap-model batch pipeline interest. → *Run a small open OCR or extraction model against Haiku on a sample of our document inputs and log per-document cost and accuracy.*
- **agentos** (1/3): Traces-as-dataset and GGUF/llama.cpp serving touch InferCraft and SkillForge telemetry, but the talk gives no benchmarks or internals. → *Export one of our own agent session logs into a traces-style schema and check whether it covers the fields SkillForge needs for skill mining.*
- **prosharness** (1/3): Remote jobs billed by runtime, with launch from an agent, overlap with checkpoint/resume of long runs. → *Read the HF jobs docs on status and resume before deciding whether a remote-run step belongs in a ProsHarness loop.*
