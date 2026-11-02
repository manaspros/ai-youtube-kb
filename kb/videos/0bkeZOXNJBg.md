# Why You NEED to Try Cloudflare's Sandbox SDK Today

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `0bkeZOXNJBg` · [watch](https://youtu.be/0bkeZOXNJBg) · **date:** 2025-11-02 · **length:** 5:17 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cloudflare, Daytona, Vercel, Anthropic
- **topics:** sandboxing-execution, infra-cost-scaling · **tags:** cloudflare, sandbox-sdk, durable-objects, containers, workers, wrangler, code-execution, daytona, claude-haiku, bun

> Short walkthrough of Cloudflare's Sandbox SDK for running AI-generated code in isolated containers from a Worker, with a Claude Haiku-to-sandbox example and a positioning take against Daytona.

## Summary
Cloudflare released a Sandbox SDK for executing code, managing files and running processes in an isolated environment, aimed at untested code produced by AI agents. The speaker questions whether it is late given Daytona and Vercel already offer sandboxes, then explains the layering: a Worker runs the application code, a Durable Object receives RPC calls and manages the sandbox lifecycle, and a container executes commands and returns output back up the chain. The walkthrough builds a Bun project with Wrangler config declaring the container, a Durable Object binding and a storage migration, plus a Dockerfile based on the Cloudflare sandbox image that exposes the Durable Object port. A minimal Worker calls sandbox.exec to run Python and returns the exit code, output and command. A second example sends a question to Claude Haiku via the Anthropic SDK, writes the generated code to code.js in the sandbox and runs it with node. The speaker says deployment requires a Workers paid plan and that the SDK also covers process management, git clones and terminal-like sessions. The verdict: strongest for teams already on Cloudflare Workers who want a TypeScript API, while Daytona is the pick for a cheaper option with a Python SDK and more features.

## Key ideas
- **Sandbox SDK is positioned for running untested, AI-generated code: execute commands, manage files and run processes in an isolated environment.** — Framed as the answer to agent-generated code that should not run on the host. The speaker asks whether it arrives late given Daytona and Vercel sandboxes, and treats the Cloudflare-specific answer as the main reason to pick it. ([0:00](https://youtu.be/0bkeZOXNJBg?t=0))
- **Three-layer architecture: Worker, Durable Object, container.** — The Worker runs application code. A Durable Object receives RPC calls and manages sandbox lifecycle (create, activate, delete). It routes commands to the container, which executes them and captures output; responses flow back through the same layers. ([0:00](https://youtu.be/0bkeZOXNJBg?t=0))
- **Container image is a full Linux environment with Node 20, Python 3.11, latest Bun on Ubuntu 22.** — Full Linux capabilities, but local runs need Docker Desktop or another Docker runtime because the container image is built and pulled first. ([1:24](https://youtu.be/0bkeZOXNJBg?t=84))
- **Minimal Worker: getSandbox plus sandbox.exec, with the Durable Object class exported so the runtime registers it.** — Code runs Python through exec, logs stdout and stderr, and returns the result from a default fetch handler. The Sandbox class must be re-exported from the entry file or the Durable Object is not registered; the Durable Object namespace is typed on env. ([1:24](https://youtu.be/0bkeZOXNJBg?t=84))
- **Responses carry exit code, output and the command that ran, and the same output appears in the local console.** — Local dev with Docker builds the image on first run before the port is reachable, so the first request is slow. ([2:43](https://youtu.be/0bkeZOXNJBg?t=163))
- **LLM-to-sandbox pattern: model writes code, sandbox runs it.** — The example sends the user question to Claude Haiku with a prompt asking for simple, cleaned-up code, writes the output to code.js in a sandbox named after a demo user, and executes it with node (the speaker notes Bun would also work). Errors are handled and the result returned. ([2:43](https://youtu.be/0bkeZOXNJBg?t=163))
- **Deployment needs a Workers paid plan; the SDK goes beyond exec.** — Also mentioned: process management, cloning git repos, and sessions that behave like terminal tabs. The speaker says long-running containers beyond the limits of other options are a reason to choose it, but the duration figure is garbled in the captions. ([4:06](https://youtu.be/0bkeZOXNJBg?t=246))
- **Decision rule: Cloudflare Sandbox for Workers shops wanting a TypeScript API; Daytona for cheaper with a Python SDK and more features.** — A comparison given in one paragraph with no benchmarks or pricing numbers. Treat it as the speaker's opinion from a short hands-on, not a measured evaluation. ([4:06](https://youtu.be/0bkeZOXNJBg?t=246))

## Techniques
- **Worker + Durable Object sandbox wiring** — Wrangler JSONC declares the container, a Durable Object binding for the Sandbox class, and a migration for its storage. A Dockerfile uses the Cloudflare sandbox base image (Node 20, Python 3.11, Bun on Ubuntu 22) and exposes the Durable Object port. In the Worker, call getSandbox(env, id) to create or reuse a sandbox by ID, run sandbox.exec(command), and re-export the Sandbox class from the entry module so the runtime registers the Durable Object. *When:* Use when you want per-user or per-session isolated execution from a Cloudflare Worker, with sandbox identity tied to an ID you control.
- **Generate-then-execute loop** — Send the user question to an LLM (the example uses Claude Haiku through the Anthropic SDK) with a prompt that asks for a single, minimal code file. Write the returned code into the sandbox with the sandbox file-write call, execute it with node (or bun) via exec, and return the stdout, stderr, exit code and generated code to the caller. Handle errors on the generation and execution paths separately. *When:* Use for agent features that must run model-written code (data transforms, calculations, quick scripts) without touching the host or the main worker process.
- **Local dev with Docker before deploy** — Run the Worker locally with Docker running so the sandbox image builds and pulls on first request, then hit the local endpoint to confirm exec output. Deploy after that; the account needs a Workers paid plan. *When:* Use to validate the container image and Durable Object wiring before paying for a deploy.

## Numbers
- Container image includes Node 20, Python 3.11, latest Bun, on Ubuntu 22. ([1:24](https://youtu.be/0bkeZOXNJBg?t=84))
- Deploying requires a Workers paid plan. ([4:06](https://youtu.be/0bkeZOXNJBg?t=246))
- Speaker says containers can run for a long time (captions read 'more than 45 minutes or five hours'), which is ambiguous and not verified; check the official docs before relying on it. ([4:06](https://youtu.be/0bkeZOXNJBg?t=246))
- Video length is 5:17; no benchmarks, latency or pricing figures are given. ([0:00](https://youtu.be/0bkeZOXNJBg?t=0))

## Hot takes
- Cloudflare's sandbox is a no-brainer for teams already on Workers who want a TypeScript API (speaker's view).
- The title ('You NEED to try') oversells a short intro; the substance is a basic exec example and a one-paragraph comparison.
- Lateness vs Daytona and Vercel is raised as a question and not answered in depth.

## Tools mentioned
Cloudflare Sandbox SDK, Cloudflare Workers, Cloudflare Durable Objects, Cloudflare Containers, Wrangler, Docker Desktop, Bun, Node 20, Python 3.11, Ubuntu 22, Anthropic AI SDK, Claude Haiku, Daytona, Vercel sandbox

## Relevance to our work
- **agentos** (2/3): Crucible (L2C) is opt-in sandboxed code execution with a Cloudflare backend. This talk shows the concrete Cloudflare primitives (Worker, Durable Object per sandbox, exec and file-write API) that such a backend would sit on. → *Compare the Cloudflare Sandbox SDK's Durable Object lifecycle and exec/write-file API with the planned celld Cloudflare backend in Crucible, and check the container lifetime limits in Cloudflare's docs before committing to it.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI for long runs; an isolated sandbox could matter later if it runs untrusted generated code, but the talk does not address checkpoint/resume or harness design. → *If ProsHarness ever needs isolated execution for Claude Code runs, add Cloudflare Sandbox and Daytona to the candidate list and compare their exec/session APIs.*
