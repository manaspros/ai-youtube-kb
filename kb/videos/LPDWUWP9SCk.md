# Run Claude Code with Ollama for 99% Cheaper AI

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `LPDWUWP9SCk` · [watch](https://youtu.be/LPDWUWP9SCk) · **date:** 2026-08-02 · **length:** 5:37 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Warren · **orgs:** Better Stack, Ollama, Anthropic, Apple
- **topics:** local-ai, claude-code, token-cost-efficiency · **tags:** ollama, local-llm, claude-code, opencode, open-weight-models, gemma-4, qwen-3.6, vram, mlx, docker, base-url-override

> Better Stack setup walkthrough for pointing Claude Code and OpenCode at a local Ollama server to run open models such as Gemma 4 and Qwen 3.6. Setup only: the "99% cheaper" claim is never measured.

## Summary
Warren from Better Stack shows how Ollama, a local LLM server, can stand in for Anthropic's API in Claude Code by changing the base URL and auth token environment variables. He launches Claude Code and OpenCode through the Ollama CLI, runs Gemma 4 as the default model, and sends a "hello" and an image question to confirm the setup works. He notes that Ollama can pull many open models (Qwen 3.6, DeepSeek, GLM, MiniMax are named), that local hardware limits context length by VRAM tier, and that Ollama has MLX support on Apple silicon and a Docker path. He briefly compares Ollama with vLLM (better for hosted serving) and LM Studio (closer to Ollama, with a GUI). The video gives no cost calculation, benchmark or output-quality comparison, so the title's "99% cheaper" is not supported by anything shown.

## Key ideas
- **Ollama is a headless local LLM server; any tool that lets you set an API base URL can be pointed at it.** — The speaker cites over 176,000 GitHub stars and says Ollama works with Claude Code, Codex and OpenClaw. It can manage local models or route traffic to hosted ones. Tools keep working the same way, but the model behind them changes. ([0:00](https://youtu.be/LPDWUWP9SCk?t=0))
- **Claude Code can be redirected to Ollama with environment variables, with no Ollama CLI in the loop.** — The speaker says to change the base URL and auth token variables so Claude Code talks to the Ollama server. The exact variable names are not shown on screen in the transcript. Claude Code's UI is unchanged, and the reply still says it is Claude Code, even while running Gemma 4. ([1:15](https://youtu.be/LPDWUWP9SCk?t=75))
- **The ollama CLI can launch coding harnesses directly.** — Running the ollama command opens a menu of agents and harnesses, including Claude Code and OpenCode, plus a model picker. The demo uses OpenCode with Gemma 4 and Claude Code with Gemma 4 as the default model. ([0:00](https://youtu.be/LPDWUWP9SCk?t=0))
- **Model choice is open-ended: any model in the Ollama library can be pulled with one command.** — The speaker names Qwen 3.6, MiniMax, and DeepSeek-family models. ollama run <model> downloads the model on first use, which takes a while for large models. ([2:38](https://youtu.be/LPDWUWP9SCk?t=158))
- **Local hardware sets the usable context length, according to the speaker's VRAM tiers.** — He says under 24 GB VRAM gets about 4k context, 28 to 48 GB about 32k, and over 48 GB about 256k. The 24 GB and 28 GB boundary is unclear in the transcript. No source is given for the figures. ([2:38](https://youtu.be/LPDWUWP9SCk?t=158))
- **Ollama can run on Apple silicon through MLX and inside Docker.** — He says Ollama moved to MLX in March, which uses unified memory and the GPU neural accelerators to speed up first-token and generation time. Docker is covered in the docs for CPU-only and for NVIDIA or AMD GPUs; the demo shows only curl calls to the API. ([3:56](https://youtu.be/LPDWUWP9SCk?t=236))
- **Positioning: vLLM for hosted serving, LM Studio for a local GUI workflow.** — He calls vLLM far more suited to serving models as services, with better throughput and memory management. He says LM Studio is closest to Ollama for local use and has a GUI, but Ollama also has an official GUI. These comparisons are stated, not measured. ([3:56](https://youtu.be/LPDWUWP9SCk?t=236))

## Techniques
- **Redirect Claude Code to a local Ollama server** — Set the base URL environment variable to the Ollama server address and set the auth token variable, then start claude as usual. The speaker says Claude Code then works as before but runs the local model. Exact variable names and values are not shown in the transcript. *When:* Use when you want Claude Code's workflow for low-stakes or high-volume work and can accept a weaker local model. Verify the output yourself before trusting it.
- **Launch a harness through the Ollama CLI** — Run `ollama` in a terminal. Pick Claude Code or OpenCode from the menu, then pick the model (the demo default is gemma 4). This avoids setting environment variables by hand. *When:* Use for a quick local test of a harness with a local model.
- **Pull and run a model from the CLI** — `ollama run qwen3.6` downloads the model on first use and then starts a chat. For images, the demo runs `ollama run gemma 4` with a quoted question followed by an image path. *When:* Use to check that a model is installed and responds, or to test vision input with a single image.
- **Match the model to VRAM when choosing context length** — The speaker's rule of thumb: under 24 GB VRAM, about 4k context; 28 to 48 GB, about 32k; over 48 GB, about 256k. Check the actual context setting in your Ollama configuration for your model before relying on it. *When:* Use when deciding whether a local model can handle long coding sessions on your hardware.
- **Run Ollama in Docker and call its API** — The speaker points to the Ollama docs for a container guide covering CPU-only and NVIDIA or AMD GPU setups. He starts the model inside Docker and sends curl requests to the API. Container commands are not shown on screen. *When:* Use when a local model needs to back your own service, not just an interactive CLI.

## Numbers
- Ollama has over 176,000 GitHub stars. ([0:00](https://youtu.be/LPDWUWP9SCk?t=0))
- Pointing Claude Code at Ollama gives access to hundreds of models instead of the few Anthropic models. The speaker names GLM and DeepSeek as examples of models accessible this way. ([0:00](https://youtu.be/LPDWUWP9SCk?t=0))
- Claude Code shows 'API usage billing' while running the local model. The speaker says it costs nothing, because the model is local. The title's '99% cheaper' is never calculated. ([1:15](https://youtu.be/LPDWUWP9SCk?t=75))
- Context length by VRAM: under 24 GB gives about 4k; 28 to 48 GB gives about 32k; over 48 GB gives about 256k. The 24 to 28 GB boundary is unclear in the transcript. ([2:38](https://youtu.be/LPDWUWP9SCk?t=158))
- The image-caption test returned a correct tabby-cat description on the first run. Latency is described as 'very quick' with no measurement. ([2:38](https://youtu.be/LPDWUWP9SCk?t=158))

## Hot takes
- The title's '99% cheaper' claim is not supported. The video shows no cost calculation and no comparison with the Anthropic API.
- Quality is untested. The only checks are a 'hello' reply and one image caption, so the video cannot say whether a local model can do real coding work.
- The speaker presents the model still calling itself Claude Code as a 'trick'. That shows the harness's identity, not the model's capability, so it is not evidence of quality.
- Context-length tiers are stated without a source, and the boundary between the first two tiers is inconsistent in the transcript (24 GB vs 28 GB).
- The vLLM and LM Studio comparisons are one-line opinions with no benchmarks.

## Tools mentioned
Ollama, Claude Code, OpenCode, Codex, OpenClaw, Gemma 4, Qwen 3.6, MiniMax, DeepSeek, GLM, vLLM, LM Studio, MLX, Docker, EverythingLLM

## Relevance to our work
- **agentos** (2/3): The base-URL swap is the same pattern AgentOS relies on (point an OpenAI-compatible client at one proxy URL). Ollama is an alternative local backend to the vLLM path in InferCraft for cheap open-model traffic. → *Add a local-model backend (Ollama or a vLLM endpoint) to the routing table, then compare cost and tool-call success against a cheap hosted model on one of our agent eval tasks. The video has no measurements, so run the test ourselves.*
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI, and this shows the CLI can run on a different backend through environment variables. A cheaper model could suit scheduled or looped runs, but the video does not show whether tool use or long sessions survive a weaker model. → *Run one non-critical ProsHarness loop with the Claude Code base URL pointed at a local Ollama model. Check whether checkpoint/resume and skill invocations still work.*
