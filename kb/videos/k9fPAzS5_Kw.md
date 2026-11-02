# Here Is How to Vibe Code Large Scale Projects

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `k9fPAzS5_Kw` · [watch](https://youtu.be/k9fPAzS5_Kw) · **date:** 2025-11-02 · **length:** 6:58 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed) · **orgs:** Plandex, OpenRouter, OpenAI, Cursor, Google, Apple
- **topics:** coding-agents, context-engineering, vibe-coding-app-building · **tags:** plandex, cli-coding-agent, large-codebase, tree-sitter, openrouter, docker, multi-model-routing, sandboxed-changes, full-auto-mode, swift, swiftui, xcode, gemini-2.5

> AI LABS walkthrough of Plandex, a self-hosted CLI coding agent aimed at large projects: local Docker setup, chat-then-tell workflow, reviewable sandboxed changes, and one Swift app demo. Context-size claims are unverified.

## Summary
The host introduces Plandex as a command-line coding agent meant to get around the context limits of tools like Cursor, claiming it can use up to 2M tokens of context and index directories of 20M+ tokens through Tree-sitter project maps. He walks through three deployment modes (Plandex Cloud, Cloud with your own keys, and self-hosted local with Docker and your own keys) and sets up the local mode: start the Docker server, install the CLI, sign in, export OpenRouter and OpenAI keys, and initialize a repo. The workflow is chat mode for brainstorming and reading the project, then tell mode, where Plandex breaks the task into single-goal steps and runs them in a sandbox. Changes are only applied after an explicit review. When a command fails, it offers a debug-once or full-auto debug option, and he warns that full auto burns API credits quickly. In the demo, Plandex reads a Swift/SwiftUI macOS menu bar app, builds a build script, runs it, fixes errors, and adds an accent-color setting that the host confirms in Xcode. The video is a single hands-on run with no benchmarks.

## Key ideas
- **Plandex is pitched as a CLI agent for large projects: up to 2M tokens of direct context and indexing of directories above 20M tokens, using Tree-sitter project maps. These are the creator's claims, repeated from the project's marketing and not measured in the video.** — Claimed capacity is the main selling point, contrasted with Cursor's context limit. No test on a large repo is shown. ([0:00](https://youtu.be/k9fPAzS5_Kw?t=0))
- **Three deployment modes: Plandex Cloud (no separate keys), Cloud with your own API keys, and self-hosted local mode (Docker server plus your own keys). Windows needs WSL.** — The demo uses local mode. Docker must be installed and running before the server starts, or setup throws an error. ([1:25](https://youtu.be/k9fPAzS5_Kw?t=85))
- **Two-phase workflow: chat mode to brainstorm and have the project read and summarized, then tell mode to implement. The task is split into single-goal steps that run one by one.** — On the Swift app, chat mode produced an architecture, key components and user-flow overview before any code was written. ([2:51](https://youtu.be/k9fPAzS5_Kw?t=171))
- **Changes are staged in a sandbox and kept separate from the working files until the user reviews them after each tell session (apply or reject). Commands it runs are part of that staged set.** — The speaker presents this as the way to test what was built before accepting it. ([4:15](https://youtu.be/k9fPAzS5_Kw?t=255))
- **Full auto debug mode retries failing commands on its own and uses many tokens, which can get expensive across OpenRouter and OpenAI credits. The speaker explicitly warns about cost.** — Failing commands offer a menu: debug once, or debug in full auto. The demo uses the debug path to fix a build script error. ([4:15](https://youtu.be/k9fPAzS5_Kw?t=255))
- **Demo: a SwiftUI menu bar app. Plandex built a build script, ran it, read the logs and fixed the errors, then added an accent-color setting that the host confirmed in Xcode.** — The host says a previous Gemini 2.5 video was the only model that could handle this app, and he credits Plandex's multi-model routing for the success. That is an untested inference from one run. ([5:43](https://youtu.be/k9fPAzS5_Kw?t=343))

## Techniques
- **Self-host Plandex in local mode** — 1) Make sure Docker is installed and running. 2) Clone the Plandex GitHub repo and start the server with the command from the local-mode quick start in the repo (command not shown in the video). 3) In a new terminal, install the Plandex CLI with the install command from the guide (it uses sudo). 4) Run the sign-in command, pick local mode when asked, and accept the default host (the port the server prints). This creates a local user. *When:* You want Plandex with your own OpenRouter/OpenAI keys and no Plandex Cloud account. Windows users need WSL.
- **Set keys and initialize a repo** — Export your OpenRouter API key and OpenAI API key in the shell before initializing. Run `plandex` to open the REPL in the project directory, then run the init command (the video says the short form works too; the exact name is not spoken). Settings and auto mode are changed through other REPL commands. *When:* Each new repo. Keys must be exported before init, or Plandex has nothing to call.
- **Chat to brainstorm and understand, then tell to implement** — Stay in chat mode and describe the feature, or ask Plandex to read the existing project so it can summarize architecture, components and user flow. Switch to tell mode when ready. It asks whether to send another prompt or begin implementation, then builds a plan of single-goal steps and runs them in order. *When:* Larger or unfamiliar codebases, or any change that needs a plan you can read before code is written.
- **Review before applying, and debug failed commands** — After a tell session, review the staged changes, then press A to apply or reject. When a command fails, pick 'debug once' for a single fix attempt or 'debug in full auto' to let Plandex retry on its own. Full auto costs more tokens. *When:* Use review gates on any change you have not tested. Reserve full auto for cases where you accept the spend, because it burns API credits fast.

## Numbers
- Claimed direct context window of up to 2 million tokens (creator's statement, not measured) ([0:00](https://youtu.be/k9fPAzS5_Kw?t=0))
- Claimed index capacity of 20 million tokens or more for a directory (creator's statement, not measured) ([0:00](https://youtu.be/k9fPAzS5_Kw?t=0))
- Three deployment modes: Plandex Cloud, Cloud with own keys, self-hosted local with Docker and own keys ([1:25](https://youtu.be/k9fPAzS5_Kw?t=85))
- Full auto debug uses a lot of tokens and burns OpenRouter/OpenAI credits; no dollar figure given ([4:15](https://youtu.be/k9fPAzS5_Kw?t=255))

## Hot takes
- The title says 'large scale projects', but the only demo is a small single-app SwiftUI menu bar project. No large repo is tested.
- The 2M-token context and 20M-token index figures are the vendor's claims, repeated without verification. Nothing shows how much of a large codebase actually makes it into the model's working context.
- The credit for success going to multi-model routing through OpenRouter rests on one run and a comparison with an earlier video. It is speculation, not a measured result.
- The full-auto cost warning is the most practical point in the video.
- Not a sponsored segment. The end has a donation request, not a product pitch.

## Tools mentioned
Plandex, Docker, OpenRouter API, OpenAI API, Tree-sitter, Cursor, Xcode, Swift, SwiftUI, Gemini 2.5

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code with plan → critique (Codex) → debate and phone-driven approvals. Plandex separates a plan-building chat phase from an implementation phase, then gates application behind an explicit review. That is the same shape, and it is a competing harness to compare against. → *Compare Plandex's chat-plan / tell-implement / apply-or-reject flow with ProsHarness's plan → critique → approval loop, and check whether ProsHarness needs an explicit review-before-apply gate and a full-auto token budget cap.*
- **agentos** (1/3): Plandex sandboxes agent file changes until the user approves them, which is related to Crucible's exec-gate and sandboxed execution. It also routes across models via OpenRouter, which is related to L1 strategy routing. Both are shallow mentions in a single demo. → *Read Plandex's sandbox-then-apply flow in its repo and note whether a review-before-commit step fits the Crucible exec-gate design. No code change needed yet.*
