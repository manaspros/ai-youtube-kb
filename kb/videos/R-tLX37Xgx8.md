# Why Rust Is The New GOAT For AI

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `R-tLX37Xgx8` · [watch](https://youtu.be/R-tLX37Xgx8) · **date:** 2026-10-24 · **length:** 6:24 · **format:** other · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** GitHub, Microsoft, Google, Discord, Mozilla, Anthropic, OpenAI, xAI, NVIDIA, Hugging Face, Stack Overflow
- **topics:** dev-tools, coding-agents, infra-cost-scaling · **tags:** rust, memory-safety, garbage-collection, copilot, native-binaries, compiler-feedback-for-agents, python-rust-extensions, gpu-kernels, bun, codex-cli

> Better Stack argues Rust is taking over AI tooling: memory safety, no GC pauses, and single native binaries, with GitHub Copilot, Codex CLI and Bun as examples. Mostly company anecdotes.

## Summary
The speaker argues that teams building AI tools are rewriting them in Rust, citing GitHub's Copilot runtime, xAI, Bun (which Claude Code runs on) and Codex CLI. The case rests on memory safety: the speaker says roughly 70% of Microsoft's CVE-assigned bugs in 2019 and about 70% of Chrome's high-severity bugs were memory bugs, and that Android's memory-bug share fell from 76% in 2019 to under 20% after switching new code to Rust. Rust's ownership model is presented as avoiding both manual frees and garbage-collector pauses, using a Discord Go service as the example. The main concrete case is GitHub's Copilot runtime: moving from a per-app Node process to an in-process native library cut session start-to-reply from about 5.25 s to 292 ms. The speaker also says compiler error messages help coding agents self-correct, and that GitHub's TypeScript-to-Rust port took about 14.5 weeks. The closing point is that Python developers do not need to switch, since libraries like Hugging Face tokenizers, tiktoken, pydantic v2 and uv already have Rust cores, while people building CLIs and agent harnesses are the ones the speaker says should consider Rust. Most evidence is vendor self-reporting, and the 'GOAT' title is hype.

## Key ideas
- **Major AI tooling is being rewritten in Rust** — The speaker names GitHub (Copilot runtime), xAI, Bun (the JS runtime Claude Code runs on, moved from Zig to Rust this summer) and OpenAI's Codex CLI (said to be 97% Rust) as examples. These are the speaker's claims, not verified here. ([0:00](https://youtu.be/R-tLX37Xgx8?t=0))
- **Memory bugs dominate security bug counts** — Speaker cites Microsoft (~70% of CVE-assigned security bugs in 2019 were memory-safety bugs), Chrome (~70% of high-severity bugs were memory bugs), and Android (memory bugs fell from 76% of security bugs in 2019 to under 20% last year after new Android code moved to Rust). ([0:58](https://youtu.be/R-tLX37Xgx8?t=58))
- **Garbage collectors cause uncontrolled pauses; Rust avoids them** — A Discord Go service had latency and CPU spikes roughly every two minutes from the garbage collector; the Rust rewrite had none. Rust instead frees each value when its single owner goes out of scope, and the compiler checks these rules before the program runs. ([2:03](https://youtu.be/R-tLX37Xgx8?t=123))
- **Copilot speedup came from removing a per-app Node process as much as from Rust** — The old runtime was TypeScript, and every app using GitHub's SDK started its own Node process (about 100 MB minimum each). The Rust version compiles to one native file that the app loads in-process like a plugin, cutting session start-to-reply from 5.25 s to 292 ms. ([3:09](https://youtu.be/R-tLX37Xgx8?t=189))
- **Compiler errors let coding agents self-correct** — When an agent writes broken Rust, the compiler points at the line and states the failure, so the agent fixes it and retries. GitHub's port went from about 430k lines of TypeScript to 832k lines of Rust plus about 470k lines of tests in about 14.5 weeks. Memory-rule errors were only about 1.7% of the agent's compile errors. ([4:09](https://youtu.be/R-tLX37Xgx8?t=249))
- **Python AI libraries already run Rust underneath** — Hugging Face tokenizers ships a ~9.6 MB compiled Rust core, and tiktoken, pydantic (v2+) and uv (pip replacement) are also Rust-backed. The speaker's advice: Python users need not switch; CLI and agent-harness builders should consider Rust. ([4:09](https://youtu.be/R-tLX37Xgx8?t=249))
- **Google reports fewer rollbacks and faster reviews for Rust changes** — Speaker says Rust changes in Android get rolled back about four times less often than C++ changes, and take about 25% less time in code review. ([4:09](https://youtu.be/R-tLX37Xgx8?t=249))
- **NVIDIA is exploring Rust for GPU kernels** — Speaker says NVIDIA announced last month a way to write GPU kernels in Rust, which the post says is not production-ready yet. Kernels are still mostly CUDA C++. ([5:25](https://youtu.be/R-tLX37Xgx8?t=325))

## Techniques
- **Rust core behind a Python API** — Keep the Python surface small and readable and put the number-crunching in a compiled Rust library underneath, as Hugging Face tokenizers, tiktoken, pydantic and uv do. *When:* When a Python library has a CPU-heavy hot path (tokenization, validation, package resolution) and the users should not have to change language.
- **Ship a native library instead of a helper process** — Compile the component to a single native file and load it in the host process as a plugin, instead of spawning a separate runtime per app and passing messages (the Copilot SDK change). *When:* When many client apps each start a heavy runtime (a Node process at about 100 MB each) and per-session startup latency or memory is the bottleneck.
- **Feed compiler errors back into the agent loop** — When an agent writes code in a strict compiled language, return the compiler's line-level errors to the agent and let it retry until the build passes. *When:* For agent-written code in a strongly typed language where compile errors are precise and actionable.
- **Ownership-based memory for latency-critical services** — Use single-owner values that free at scope exit, with no tracing GC, so latency does not depend on background collection pauses. *When:* For long-running services where GC pauses show up as periodic latency or CPU spikes (the Discord example).

## Numbers
- Rust 1.0 released May 2015; 72% of 2025 Stack Overflow Rust users want to keep using it ([0:58](https://youtu.be/R-tLX37Xgx8?t=58))
- Microsoft 2019: about 70% of CVE-assigned security bugs were memory-safety bugs; Chrome team: about 70% of high-severity bugs were memory bugs ([0:58](https://youtu.be/R-tLX37Xgx8?t=58))
- Android memory bugs: 76% of security bugs in 2019, below 20% last year (first time) ([0:58](https://youtu.be/R-tLX37Xgx8?t=58))
- Android Rust code has about 1000x fewer memory bugs per line than Android C/C++ (speaker's figure) ([2:03](https://youtu.be/R-tLX37Xgx8?t=123))
- Copilot start-to-reply: 5.25 s to 292 ms; each Node process used about 100 MB minimum ([3:09](https://youtu.be/R-tLX37Xgx8?t=189))
- GitHub port: about 430,000 lines TypeScript to 832,000 lines Rust plus about 470,000 test lines, in about 14.5 weeks ([4:09](https://youtu.be/R-tLX37Xgx8?t=249))
- Memory-rule errors were about 1.7% of agent compile errors ([4:09](https://youtu.be/R-tLX37Xgx8?t=249))
- Android Rust changes rolled back about 4x less often than C++; about 25% less code review time ([4:09](https://youtu.be/R-tLX37Xgx8?t=249))
- Hugging Face tokenizers compiled Rust file is about 9.6 MB ([4:09](https://youtu.be/R-tLX37Xgx8?t=249))

## Hot takes
- The 'GOAT' title overstates the case. The evidence is almost all vendor self-reporting or secondhand anecdote (GitHub, Google, Discord, Microsoft, Chrome) with no independent measurement shown.
- The Copilot 5.25 s to 292 ms gain is presented as a Rust win, but the speaker's own explanation attributes most of it to removing a per-app Node process and runtime. Rust is one part of that, not the whole cause.
- 'GitHub, OpenAI, xAI and Anthropic are all moving to Rust' is a broad generalization. The speaker gives no sources for the xAI and OpenAI claims.
- The most practical point is the compiler-feedback loop for coding agents: GitHub's port reportedly leaned on compiler errors, and only about 1.7% of those errors were memory-rule errors.

## Tools mentioned
Rust, Cargo, GitHub Copilot, Copilot SDK, Bun, Zig, Claude Code, Codex CLI, Node.js, TypeScript, Go, Python, C, C++, CUDA, Hugging Face tokenizers, tiktoken, pydantic, uv, pip, Chrome, Android

## Relevance to our work
- **agentos** (1/3): Govrix Scout (L1 proxy) is already Rust. The speaker's compiler-errors-in-the-agent-loop point could apply when agents edit it, but the talk gives no new data on proxies or gateways. → *When agents edit the Rust proxy, return cargo check/clippy output to the agent loop and count how many fix attempts it takes to get a green build.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, and the speaker says Claude Code now runs on Bun, which moved to Rust. Per-process memory and startup cost matter if the harness spawns many CLI processes. → *Measure per-process memory and startup time for the claude CLI when ProsHarness runs several loops in parallel, to see whether process count is the bottleneck.*
