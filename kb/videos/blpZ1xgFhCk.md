# This Is What Voice Coding Was Supposed to Be (Qwen Audio Agent)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `blpZ1xgFhCk` · [watch](https://youtu.be/blpZ1xgFhCk) · **date:** 2026-10-02 · **length:** 9:34 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh (Better Stack host) · **orgs:** Better Stack, Alibaba Cloud, Anthropic, OpenAI
- **topics:** voice-multimodal, agent-architecture, coding-agents, multi-agent · **tags:** voice-coding, full-duplex, acp, agent-client-protocol, interruption-handling, barge-in, claude-code, qwen, dashscope, mlx, local-voice, async-task-handoff

> Hands-on review of Qwen Audio Agent, an open-source voice runtime that keeps a voice conversation alive while Claude Code does slow coding work in the background over ACP. The main lesson is that voice coding is a concurrency problem, not a transcription problem.

## Summary
Josh from Better Stack demos Qwen Audio Agent, a desktop runtime with no model weights of its own. A lightweight front-end voice agent holds the conversation and answers quick questions itself, while Claude Code runs as a back-end worker over the Agent Client Protocol (ACP) and handles file edits, tool runs and tests. Long tasks are handed off as async jobs, the user can keep talking and ask for status mid-task, and the result is injected back into the live conversation when it finishes. Interruption is implemented as an explicit state machine that cancels in-flight audio and transcripts. The backend is swappable via ACP (Claude Code, Codex, OpenCode named). The speaker is candid about the caveats: the good voice path depends on a paid Alibaba DashScope key, a fully local MLX mode exists but its docs are Chinese-only, and no latency numbers are published. He closes with the claim that transcription is solved and the real problem is whether the system can keep talking while it is busy.

## Key ideas
- **Dictation-style voice coding (Whisper, then paste) only replaces typing. The useful part is full duplex, where the conversation keeps running while work happens elsewhere.** — The speaker argues the real gain comes from the voice side staying responsive while the agent works, not from faster transcription. ([0:00](https://youtu.be/blpZ1xgFhCk?t=0))
- **Interruption is a state machine, not a single event.** — Steps: detect user speech, mark an interruption, emit an interrupt signal, actively cancel audio and transcripts still in flight, then start the new turn. The speaker says the 'still hearing another second and a half' gap is what makes voice assistants feel broken. ([5:27](https://youtu.be/blpZ1xgFhCk?t=327))
- **Two-lane architecture: a fast voice layer and a slow coding worker.** — The front-end voice agent answers simple questions immediately (status, cancel, 'never mind'). The back-end coding agent, Claude Code, is connected over ACP and does file edits, tool calls and tests. Slow work becomes an async task whose result is injected back into the live conversation. ([4:11](https://youtu.be/blpZ1xgFhCk?t=251))
- **Route trivial questions away from the expensive agent.** — A simple arithmetic question (19 x 24) was answered by the voice agent without touching the repo or spending Claude API credits. ([2:14](https://youtu.be/blpZ1xgFhCk?t=134))
- **Status queries work mid-task without blocking on the worker.** — The user asked how the refactor was going and got an answer that it was editing and running tests, while a second request ran in parallel. ([3:32](https://youtu.be/blpZ1xgFhCk?t=212))
- **The backend is swappable because the integration is a protocol (ACP), not a vendor-specific integration.** — Claude Code, Codex, OpenCode and others are named as possible workers. ([5:27](https://youtu.be/blpZ1xgFhCk?t=327))
- **The open-source claim needs qualifying. The runtime is Apache 2.0, but the best-sounding voice depends on a paid cloud API.** — The default path runs through Alibaba DashScope with a paid key (free credits included). There is no self-hosted version of the high-quality audio generation. A fully local mode exists (Hugging Face speech-to-text with an MLX backend on Apple Silicon, MPS), but the tuned profile docs are Chinese-only. ([6:11](https://youtu.be/blpZ1xgFhCk?t=371))
- **No published latency numbers were found on any hardware.** — The speaker says he looked and found none, which matters given that the product is sold on responsiveness. ([7:14](https://youtu.be/blpZ1xgFhCk?t=434))
- **Thesis: the hard problem is concurrency, not speech.** — Transcription is treated as solved. Whether the system can keep talking while busy is the differentiator, and the speaker says almost nobody treats it that way. ([9:17](https://youtu.be/blpZ1xgFhCk?t=557))

## Techniques
- **Voice front-end + async coding back-end over ACP** — Run a lightweight voice agent that owns conversation, interruptions and cancel/status commands. Hand real coding work to a separate agent over the Agent Client Protocol as an async task. Inject the result back into the live conversation when the task completes. The protocol keeps the backend swappable (Claude Code, Codex, OpenCode). *When:* Any long-running agent task where the user must keep interacting, such as voice, phone, or chat front-ends over a slow coding agent.
- **Interruption as an explicit state machine** — On user speech: (1) detect speech, (2) mark an interruption, (3) emit an interrupt signal, (4) cancel in-flight audio and transcript output, (5) start the new turn. Do not treat barge-in as a single event. *When:* Voice UIs where barge-in must not leave stale audio or a second of trailing speech playing after the user starts talking.
- **Local fast-path for trivial questions** — Let the cheap voice-side model answer simple queries itself (arithmetic, status, cancel) and only escalate tasks that touch files or tools to the expensive coding agent. *When:* To cut API spend and avoid turning every quick question into a full agent task.
- **Setup (as demonstrated)** — Install the signed universal macOS DMG (no CUDA, Python or compile step). Create an Alibaba Cloud (DashScope) API key from the English site, enter it in the desktop UI for the front-end voice agent. Add Anthropic API credits for the back-end Claude Code worker. The speaker estimates 10-15 minutes to integrate everything. Local-only mode requires a second Python install and an MLX setup (docs in Chinese). *When:* Trying the runtime on Apple Silicon; the local-only route is the only one that avoids a cloud key.

## Numbers
- Video length 9:34. Setup estimated at 10-15 minutes (speaker's estimate). ([8:10](https://youtu.be/blpZ1xgFhCk?t=490))
- Repo stars about 2,400 (auto-caption reads '23, 2,400 stars'), versus about 4,000 monthly package downloads, so stars are running ahead of usage. ([8:10](https://youtu.be/blpZ1xgFhCk?t=490))
- On the latest release, the Mac build downloaded about 90 times versus about 502 for Windows (auto-caption is unclear on these figures, so treat them as approximate). ([8:10](https://youtu.be/blpZ1xgFhCk?t=490))
- No latency numbers published for any hardware; the speaker looked and found none. ([7:14](https://youtu.be/blpZ1xgFhCk?t=434))
- Model claims 100+ languages for recognition and a few dozen for speech (vendor claim, as relayed by the speaker). ([7:14](https://youtu.be/blpZ1xgFhCk?t=434))

## Hot takes
- The runtime is open source but the best voice path is cloud-only and paid. The fully local path is real but undocumented in English and has no latency data.
- Transcription is solved. The differentiator is whether the system can keep talking to you while it is busy.
- Interruption handling (cancel in-flight audio and transcripts) matters more to perceived quality than response speed.
- The project is described as Chinese-first: the wake word, the full-duplex design article and the tuned voice profile are all Chinese-only.

## Tools mentioned
Qwen Audio Agent (open-source voice runtime, Apache 2.0; no model weights shipped), Claude Code (back-end coding agent), Codex, OpenCode, ACP (Agent Client Protocol), Alibaba DashScope (paid cloud voice API), OpenAI Realtime API (mentioned as comparison), PipeCat (mentioned as comparison), LiveKit Agents (mentioned as comparison), Whisper (dictation baseline), Hugging Face speech-to-text pipeline, MLX (Apple Silicon local backend), MPS (Apple Silicon GPU backend)

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps Claude Code with checkpoint/resume, approvals and loops. The voice runtime shows the pattern of answering status and cancel requests from a separate front-end while the worker is still running. → *If ProsHarness adds phone or voice approvals, treat status and cancel as a fast path that reads checkpoint state and never blocks on the worker. Skim the ACP docs to see whether ProsHarness can talk to Claude Code through the same protocol.*
