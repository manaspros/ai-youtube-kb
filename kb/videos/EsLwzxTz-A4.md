# This Is The Best Local Model Runner For Apple Silicon (oMLX)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `EsLwzxTz-A4` · [watch](https://youtu.be/EsLwzxTz-A4) · **date:** 2026-06-02 · **length:** 10:16 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andrus · **orgs:** Better Stack, Apple, LM Studio
- **topics:** local-ai, inference-serving, token-cost-efficiency · **tags:** oMLX, Apple Silicon, MLX, local inference, KV cache, SSD offload, prefix cache, LM Studio, Codex CLI, Qwen 3.6, M2 MacBook Pro, 32k context

> Hands-on review of oMLX, an MLX-based local inference server for Apple Silicon with SSD-paged KV cache; one Qwen 3.6 35B coding run beats LM Studio on speed, with 400 errors at context overflow as the trade-off.

## Summary
The Better Stack host reviews oMLX, a runtime built on Apple's MLX framework that targets unified-memory Macs. Its main claim is a two-tier KV cache: recent context stays in RAM while older prefix material such as system prompts and tool definitions is paged to SSD. The host runs one coding task with Qwen 3.6 35B (4-bit) through the Codex CLI on an M2 MacBook Pro, first on oMLX and then on LM Studio with the same model, context window and prompt. oMLX reportedly finished in about 20 minutes at roughly 47 tokens/s, against about 35 minutes at 16 tokens/s on LM Studio, and the machine stayed usable during the oMLX run. oMLX hit two or three 400 errors when prompts exceeded the 32k window, while LM Studio hit none. After a session clear, oMLX rehydrated the cached prefix from disk and reported 89% cache efficiency over the run. The host calls the result very impressive but admits it is one unrepeated run and the outputs look similar, so the evidence is anecdotal.

## Key ideas
- **oMLX is a runtime on Apple's MLX framework, built for unified memory rather than generic GPU support.** — MLX uses zero-copy arrays, since CPU and GPU share memory, and lazy evaluation, so the graph is optimized before execution. The host frames memory as the main bottleneck on local hardware. ([0:00](https://youtu.be/EsLwzxTz-A4?t=0))
- **oMLX uses a two-tier KV cache that pages older context to SSD.** — Recent context stays in unified memory for speed. Older parts of the conversation, such as large system prompts and tool definitions, are frozen and swapped to disk. The host compares this to LM Studio, which keeps the full history hot in RAM. ([1:04](https://youtu.be/EsLwzxTz-A4?t=64))
- **Claude Code carries a large fixed prompt overhead in small context windows.** — The host reports about 16.2k tokens of system prompt and tool definitions on a blank session. In a 32k window that leaves about 16k for the project, so he used Codex CLI, which he says has a leaner base prompt. ([3:30](https://youtu.be/EsLwzxTz-A4?t=210))
- **Persistent SSD caching lets a cleared session resume without re-prefilling.** — After /clear, oMLX still held the computed state of the project on disk. When a new prompt continued the same prefix, the model's state was reloaded from disk rather than rebuilt, and the model continued the work instead of hallucinating. ([4:31](https://youtu.be/EsLwzxTz-A4?t=271))
- **In the same-model comparison, oMLX was about 3x faster and kept the machine responsive.** — oMLX averaged about 47 tokens/s and finished in about 20 minutes. LM Studio averaged about 16 tokens/s and took about 35 minutes. On LM Studio the host could not watch video on a second monitor because of RAM pressure. ([7:03](https://youtu.be/EsLwzxTz-A4?t=423))
- **The trade-off is 400 errors at context overflow, and LM Studio's context handling was more stable.** — oMLX returned two or three 400 errors when the prompt exceeded the 32k limit, requiring a manual clear. LM Studio produced no such errors. The host says this makes oMLX a hands-on tool. ([8:20](https://youtu.be/EsLwzxTz-A4?t=500))
- **The results come from a single unrepeated run, and output quality looked similar.** — The host says he is not drawing firm conclusions, and the two final apps looked nearly identical. The oMLX app lost its watchlist on page refresh, which he attributed to incomplete database persistence. ([7:03](https://youtu.be/EsLwzxTz-A4?t=423))

## Techniques
- **Serve a local model through an OpenAI-compatible endpoint and point a coding CLI at it** — Launch the oMLX server from its window, choose the server location and set an API key. Download a model from the dashboard (Qwen 3.6 35B, 4-bit). Copy the ready-made harness snippet from the dashboard for Codex CLI. The exact command was not read on screen, so check the dashboard snippet directly. *When:* Running a local coding agent on a Mac with limited RAM, where you want the model to run in the background while you keep using the machine.
- **Same-model, same-context head-to-head benchmark for local runtimes** — Use the same model, the same context window and limits, and the same startup prompt that points to an agent-instructions file in an empty repo. Measure wall-clock time, average tokens/s and the cache-efficiency panel (cached tokens / total tokens) reported by the CLI. Count 400 context-limit errors. *When:* Comparing local inference runtimes on realistic agent coding workloads rather than synthetic prompts. Repeat runs before drawing conclusions, since this review uses one run per runtime.
- **Keep the stable prefix on disk and reuse it after a session clear** — The host relies on oMLX's SSD cache: after /clear, a new prompt that shares the earlier prefix reloads the stored state from disk. Order the stable material (system prompt, tool definitions, project context) at the start of the prompt so it can match the cached prefix. *When:* Long agent sessions on constrained memory, where clearing context to recover from overflow would otherwise force a full recompute.
- **Pick a lean harness when the context window is small** — Measure the fixed token overhead of each agent harness before the first task (the host reads Claude Code's context stats: about 16.2k tokens on a blank session). With a 32k window, choose the harness that leaves the most room for project work. *When:* Working with a small local context window, such as 32k on a laptop.

## Numbers
- Claude Code uses about 16.2k tokens for system prompt and tool definitions on a blank session, leaving about 16k of a 32k window. ([3:30](https://youtu.be/EsLwzxTz-A4?t=210))
- oMLX finished the coding task in about 20 minutes. LM Studio took about 35 minutes. ([4:31](https://youtu.be/EsLwzxTz-A4?t=271))
- oMLX processed about 1.78M tokens, of which about 1.59M were cached, giving 89% cache efficiency. ([5:44](https://youtu.be/EsLwzxTz-A4?t=344))
- Average throughput was about 47 tokens/s on oMLX versus 16 tokens/s on LM Studio, which the host describes as roughly 3x faster. ([7:03](https://youtu.be/EsLwzxTz-A4?t=423))
- oMLX hit two or three 400 errors when prompts exceeded the 32k context window. LM Studio had none. ([5:44](https://youtu.be/EsLwzxTz-A4?t=344))
- Model under test: Qwen 3.6 35B parameters at 4-bit quantization, run on a 32k context window on an M2 MacBook Pro. ([2:14](https://youtu.be/EsLwzxTz-A4?t=134))

## Hot takes
- The title ('the best local model runner for Apple Silicon') is stronger than the evidence: one unrepeated run of one model on one task, which the host himself calls inconclusive.
- The 89% cache efficiency and the 3x speed gap are the most useful numbers, but they are single-run measurements with no variance reported.
- Reliability trade-off: the speed win comes with context-overflow 400 errors that need manual /clear, which matters more for unattended agent runs than for interactive use.
- Apple-Silicon-specific: the unified-memory and SSD-paging ideas don't transfer directly to a discrete-GPU box, but the prefix-cache-after-clear behavior is a general pattern.
- Auto-caption artifacts: the model name 'Quen' is read as Qwen, and 'the 30k2 context limit' is read as the 32k window. The movie-database API is transcribed as 'MubiDB' and may be a different service.

## Tools mentioned
oMLX, Apple MLX, Qwen 3.6 35B (4-bit), Codex CLI, Claude Code, LM Studio, Apple Silicon (M2 MacBook Pro)

## Relevance to our work
- **agentos** (2/3): InferCraft plans CPU offload and KV-cache strategies on one RTX 5090. oMLX's two-tier cache (hot context in memory, older prefix paged to SSD, prefix rehydration after a clear) is a concrete comparison point for that design. The reported cache-efficiency metric is also a usable KPI for benchmarks. → *Add a benchmark to the InferCraft KV-offload work that replays a long agent session with a mid-run clear and reports cached tokens / total tokens and re-prefill time, so the SSD-paged strategy can be compared with a plain reset under the same workload.*
- **prosharness** (1/3): Checkpoint/resume of long Claude Code runs depends on what context survives a reset. The host's observation that a cleared session can reuse a disk-cached prefix suggests resume prompts should keep the stable prefix byte-identical. → *Check that ProsHarness's resume prompt keeps the system prompt and tool definitions byte-identical and first, so a resumed run can reuse a prefix cache instead of re-prefilling.*
