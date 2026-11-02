# oMLX Best Way to Run Local AI on A MAC

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `j557WxWtdZk` · [watch](https://youtu.be/j557WxWtdZk) · **date:** 2026-09-02 · **length:** 14:13 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Narrator (Kai Explains channel host) · **orgs:** Apple, Hugging Face, LM Studio, GitHub, Anthropic, Cursor, OpenAI
- **topics:** local-ai, inference-serving, coding-agents, token-cost-efficiency · **tags:** oMLX, MLX, Apple Silicon, KV cache, prefix caching, SSD cache tier, time to first token, Claude Code, Cursor, OpenCode, Codex, local coding agent, Mac Studio, GLM, Minimax, Qwen

> Kai Explains walks through OMLX, an open-source local inference server for Apple Silicon Macs that keeps a two-tier (RAM + SSD) KV cache so near-identical prefixes in long coding-agent sessions are reused instead of recomputed, mainly cutting time-to-first-token.

## Summary
The speaker argues that slowdown in long local coding-agent sessions on a Mac is a caching problem, not a hardware problem. Standard MLX servers treat a near-identical prompt prefix (new tool result appended) as a full mismatch and recompute from token 0. OMLX keeps a hot in-memory cache tier and a cold SSD tier (safetensors, block-based, prefix sharing, copy-on-write) so warm prefixes are reloaded rather than recomputed. The benefit is to time-to-first-token only; generation speed and model capacity are unchanged. Setup covers the signed DMG (recommended, since pip installs skip custom kernels), Homebrew, and Claude Code, Cursor, OpenCode, Codex and other integrations. Published benchmarks are first-party, and the one third-party number (about 20 s down to a fast warm response on an 8.7K context) is a single anecdote. The speaker recommends checking the dashboard's hot/cold panels to confirm cache hits.

## Key ideas
- **Slow turns in long local agent sessions come from cache misses, not hardware. Coding agents resend almost the same prefix each turn, and standard MLX servers discard the KV cache on any mismatch.** — A new tool result appended at the end makes the prefix a near-match, which standard servers treat as total mismatch and recompute from position 0. This cost grows with session length. ([0:00](https://youtu.be/j557WxWtdZk?t=0))
- **OMLX uses a two-tier KV cache: a hot in-memory tier and a cold SSD tier in safetensors format, with block-based management, prefix sharing and copy-on-write.** — Evicted blocks are read back from SSD on a later prefix match instead of being recomputed. The cache also survives server restarts. ([3:58](https://youtu.be/j557WxWtdZk?t=238))
- **The win is time to first token only. Generation speed and the model that fits your hardware do not change.** — Cold first turns are no faster than raw MLX. Gains concentrate in warm, repeated-prefix turns, which is most of a coding-agent session. ([4:20](https://youtu.be/j557WxWtdZk?t=260))
- **Pick the DMG install for most people. Pip installs silently skip native kernels for GLM 5.2, Minimax M3 and Qwen 3.5, which then fall back to a much slower path.** — The speaker reports the fused prefill kernel is about 30x faster on an M3 Ultra for those models. Building the kernels needs full Xcode, not just command line tools. ([6:39](https://youtu.be/j557WxWtdZk?t=399))
- **Claude Code gets a native Anthropic-compatible endpoint, and OMLX adds Claude-Code-specific context scaling and SSE keep-alive.** — Context scaling reports token counts so autocompact fires correctly for a smaller local window. Keep-alive prevents read timeouts during long prefill. Configuration is via environment variables set before launch. ([9:03](https://youtu.be/j557WxWtdZk?t=543))
- **Sizing: leave 4 to 5 GB headroom for macOS, then budget for weights plus KV cache growth.** — Example: a 9B model at 4-bit fits a real session on 16 GB. 30-40B coding models suit 64 GB. ([7:40](https://youtu.be/j557WxWtdZk?t=460))
- **Verify the cache is working by watching the dashboard's hot and cold panels during a session.** — Blocks should accumulate. A full reset every turn usually means system prompt or tool schema content is being reordered, because prefix matching is exact. ([11:22](https://youtu.be/j557WxWtdZk?t=682))
- **Benchmark evidence is thin. Published numbers are first-party on an M3 Ultra 512GB; the only independent data point is one developer's anecdote.** — First-party: about 45-59 tok/s generation for an 8-bit Qwen3 Coder model, and about 4.14x generation speedup at 8-way batching. Third-party: about 20 s down to a fast warm response on an 8.7K-token context. The speaker says to reproduce this yourself. ([10:12](https://youtu.be/j557WxWtdZk?t=612))

## Techniques
- **Diagnose slow agent turns as a prefix-cache miss** — Watch whether time-to-first-token grows with turn count while generation speed stays flat. If it does, check whether the server reuses the KV cache across turns. Keep the system prompt and tool schema byte-identical and in the same order between calls, because prefix matching is exact. *When:* Local or self-hosted coding agents that feel fast at turn 1 and crawl by turn 20+.
- **Install OMLX via the signed DMG** — Download the signed, notarized DMG from GitHub releases, drag it to Applications, launch it, and set the model directory in the welcome screen. The app ships a CLI shim. Confirm with a curl against the server. Requirements: macOS 15 Sequoia or later, Python 3.11-3.13, M1-M4 chip. Homebrew is three commands, but needs full Xcode for custom kernels. *When:* First install on a Mac. Preferred over pip for models with custom kernels (GLM 5.2, Minimax M3, Qwen 3.5).
- **Point Claude Code at OMLX** — Set three environment variables before launching Claude Code. OMLX serves an Anthropic-compatible endpoint at /v1/messages, so no translation proxy is needed. The speaker does not name the variables in the transcript. Check the OMLX docs. *When:* Running Claude Code against a local model on a Mac.
- **Point Cursor at a local OpenAI-compatible server** — Settings > Models > OpenAI API: enable Override base URL and set it to the OMLX address. Put any non-empty string in the API key field. Add the loaded model under Custom Models using its exact OMLX name. Disable Cursor's default models so it does not validate against OpenAI. *When:* Using Cursor with a local model. The labels may have changed between versions.
- **One-command agent configuration with OMLX's CLI launcher** — Run OMLX's launcher for OpenCode, Codex or PyAgent. It updates the tool config and starts the agent. The existing config is backed up to a timestamped .back file first, so you can restore it. *When:* Wiring OpenCode, Codex or PyAgent to a local model without hand-editing config.
- **Browse and reuse Hugging Face and LM Studio model caches** — Point OMLX's model directory at existing folders. It reads the Hugging Face cache and LM Studio folders directly. The admin dashboard is at /admin and includes a Hugging Face model browser. *When:* You already have models downloaded for other tools and want to avoid re-downloading.

## Numbers
- OMLX has over 18,600 GitHub stars (first-party, as of the video) ([0:00](https://youtu.be/j557WxWtdZk?t=0))
- Typical symptom: 20-30 s per tool call by about turn 12, and about 90 s per response by turn 20 ([0:00](https://youtu.be/j557WxWtdZk?t=0))
- Fused prefill kernel for GLM 5.2 / Minimax M3 / Qwen 3.5 reportedly about 30x faster on M3 Ultra (project-reported) ([6:39](https://youtu.be/j557WxWtdZk?t=399))
- Leave 4-5 GB of RAM headroom for macOS ([7:40](https://youtu.be/j557WxWtdZk?t=460))
- First-party benchmark, M3 Ultra 512GB: about 45-59 tok/s generation for an 8-bit Qwen3 Coder Next model across 1K-32K contexts ([10:12](https://youtu.be/j557WxWtdZk?t=612))
- First-party: continuous batching about 4.14x generation speedup at 8 concurrent requests vs single ([10:12](https://youtu.be/j557WxWtdZk?t=612))
- Third-party single writeup: about 20 s to process an 8,700-token context on raw MLX, reduced to a fast warm response with OMLX (unverified, one developer) ([11:22](https://youtu.be/j557WxWtdZk?t=682))

## Hot takes
- Reaching for more RAM or a bigger model is the wrong fix for slow long agent sessions. The bottleneck is recomputing the cache.
- Pip installs of MLX-based models silently fall back to a much slower path when custom kernels are missing. A DMG install avoids this.
- The Copilot integration listed in OMLX's README is doubtful, since GitHub Copilot Chat uses OAuth and does not accept an arbitrary base URL. The speaker says to verify it in the dashboard first.
- Warm-cache gains are the entire point. Turn 1 is no faster, and generation speed is unchanged.

## Tools mentioned
OMLX (Apache 2.0, about 18.6k GitHub stars, by one developer), Apple MLX / MLX server, Claude Code, Cursor, OpenCode, Codex, PyAgent, Pi, Hugging Face cache, LM Studio, safetensors, Qwen3 Coder Next (8-bit, benchmark model), GLM 5.2, Minimax M3, Qwen 3.5, Xcode

## Relevance to our work
- **agentos** (2/3): AgentOS already fronts local vLLM serving with KV-cache strategies (InferCraft, including CPU offload). OMLX's hot/cold two-tier prefix cache with SSD spill is the same idea on Apple Silicon, and it is a useful reference for the L2B KV-cache design and its warm-prefix metrics. → *Read the OMLX repo's cache design (block-based prefix sharing, SSD tier, copy-on-write) and compare it with the InferCraft CPU-offload strategy. Add a warm-prefix hit-rate metric to the InferCraft benchmark.*
- **prosharness** (1/3): ProsHarness wraps long-running Claude Code runs. Keeping the system prompt and tool schema byte-stable between calls preserves prefix cache hits, which matters for checkpoint/resume and long loops. → *Check that ProsHarness keeps the system prompt and tool-schema ordering byte-identical across turns and resumes, so prefix caching is not silently invalidated.*
