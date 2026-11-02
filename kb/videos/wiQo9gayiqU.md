# No API Key. No Cloud. Just Mac AI (Apfel)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `wiQo9gayiqU` · [watch](https://youtu.be/wiQo9gayiqU) · **date:** 2026-08-02 · **length:** 6:48 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Apple, Better Stack
- **topics:** local-ai, token-cost-efficiency, dev-tools · **tags:** apfel, apple-foundation-models, apple-intelligence, on-device-ai, macos, openai-compatible, local-llm, ollama-comparison, shell-tools, context-window-limits

> Better Stack demos Apfel, an MIT-licensed macOS CLI that exposes Apple's built-in ~3B on-device model through a terminal prompt, shell workflows and an OpenAI-compatible localhost server, and is candid about its limits.

## Summary
The presenter introduces Apfel, a small open-source (MIT) Swift binary that lets you call the ~3B-parameter on-device language model Apple ships with Apple Intelligence on macOS, with no API key and no download. It offers three interfaces: a streaming CLI, a chat prompt, and an OpenAI-compatible server on localhost. He demonstrates installing via Homebrew, streaming a response with Wi-Fi off, saving generated code to a file, and pointing an unmodified OpenAI Python SDK script at the local server. He explains that Apfel does not host a model itself but translates requests to Apple's Foundation Models framework, so unlike Ollama or MLX you cannot choose, swap or fine-tune the model. He then lists the ceilings: under roughly 5,000 tokens of total context, no memory between calls, weak math and multi-step reasoning, Apple's safety guardrails, and availability only on Apple hardware. His suggested use is small, frequent tasks such as shell one-liners, commit messages from diffs, tagging and short summaries, with the cloud kept for serious reasoning. The promised Ollama comparison is mostly verbal; no benchmarks are shown.

## Key ideas
- **Apple's built-in on-device model can be reached from the terminal, a chat prompt, or a local OpenAI-style server, with no API key and no per-token bill.** — Apfel (transcribed as Appful) is a tiny MIT-licensed Swift binary that exposes the ~3B on-device model behind Apple's Foundation Models framework. It was previously only reachable by writing a Swift app. ([0:00](https://youtu.be/wiQo9gayiqU?t=0))
- **Apfel is a translator, not a model host: nothing is downloaded and no model can be chosen.** — Ollama and MLX pull open-weight models you can swap, shrink or fine-tune. Apfel wraps the one model Apple already installed, so there is no download and almost no disk use, but also no choice and no updates to manage. ([3:15](https://youtu.be/wiQo9gayiqU?t=195))
- **Its best fit is the high volume of small, low-stakes prompts, not agent work.** — He lists shell one-liners, commit messages from a diff, quick tagging and classification, and short summaries. He suggests building an app offline against the OpenAI-style API and switching to a cloud endpoint only at ship time. ([4:22](https://youtu.be/wiQo9gayiqU?t=262))
- **The OpenAI-compatible server makes existing SDK code work offline with only a base URL change.** — The demo reuses an OpenAI Python script, changes the base URL to localhost, and passes a dummy API key, which the server ignores. The data stays on the machine. ([2:05](https://youtu.be/wiQo9gayiqU?t=125))
- **The binding constraint is the context window: under about 5,000 tokens total for prompt plus answer.** — He says that is roughly one page, so logs cannot be fed in, and a real coding sub-agent would exhaust the budget reading a single small file. He tells viewers to know this number before building anything on it. ([5:40](https://youtu.be/wiQo9gayiqU?t=340))
- **The model is weak at math, multi-step tasks and remembering context, and Apple's guardrails cannot be turned off.** — He estimates it handles about 75-80% of simple shell one-liners and then fails on math, multi-step work and follow-ups. A permissive mode softens the safety guardrails, but he says the model still belongs to Apple. ([4:22](https://youtu.be/wiQo9gayiqU?t=262))
- **Free local AI here is tied to Apple hardware and cannot be moved elsewhere.** — The app is open source, but the model lives inside macOS and cannot be downloaded or run on other machines. He frames it as a free tier for tiny prompts, with real reasoning and long documents left to the cloud or a bigger local model. ([5:40](https://youtu.be/wiQo9gayiqU?t=340))

## Techniques
- **Install and one-shot streaming prompt** — Install with `brew install apfel` (as spoken; the transcript auto-captions the name). Run `apfel stream "<prompt>"`. Output streams token by token and works with Wi-Fi off because no model is fetched at runtime. *When:* Quick offline questions or one-liners where no memory of earlier turns is needed.
- **Generate code straight into a file** — Prompt apfel with the function spec and redirect or direct the output to a target file. The output includes extra wrapper text that must be removed by hand, as the presenter notes. *When:* Scaffolding small snippets offline. Review the output before use, because the model is small.
- **Feed an existing file for feedback** — Use the file-input flag (shown as `-f` followed by the file name) and then ask a question about the file. Keep the file well under the roughly 5,000-token total context. *When:* Quick review of a short script. Logs and large files will not fit.
- **Drop-in OpenAI SDK replacement for local dev** — Start Apfel's OpenAI-compatible server on localhost. In an existing OpenAI SDK script, change the base URL to the localhost address and pass any placeholder API key. The server ignores the key. Switch the base URL back to the cloud endpoint when shipping. *When:* Building and testing an app offline or at zero cost before using a real cloud model. The port is not stated in the video.
- **Tiered routing for cheap tasks** — Send classification, tagging, short summaries and commit-message generation to the local model, and send multi-step reasoning, math and long-document work to a cloud or larger local model. The presenter describes this split verbally and does not show an implementation. *When:* High-volume small prompts where cloud cost matters more than model quality.

## Numbers
- On-device model is about 3 billion parameters. ([0:38](https://youtu.be/wiQo9gayiqU?t=38))
- Presenter's test machine was an M4 Max Mac. Install with Homebrew was described as very quick because no model downloads. ([0:38](https://youtu.be/wiQo9gayiqU?t=38))
- Total context window (prompt plus answer) is under 5,000 tokens, about one page of text. ([5:40](https://youtu.be/wiQo9gayiqU?t=340))
- Estimated success on simple shell one-liners is roughly 75-80%. This is an anecdotal estimate, not a benchmark. ([4:22](https://youtu.be/wiQo9gayiqU?t=262))

## Hot takes
- Free local AI on a Mac is only useful for tiny prompts, given the 5k-token context and 3B model.
- Apfel is best understood as a free offline utility, not as an alternative to Ollama or MLX, because the model cannot be chosen.
- The Ollama comparison is promised in the intro but is mostly verbal. No benchmarks or side-by-side outputs are shown, so the comparison is unsupported.
- The 75-80% shell one-liner figure and the claim about remembering context are the presenter's own impressions, not measured results.

## Tools mentioned
Apfel (transcribed as Appful; MIT-licensed CLI and local server), Apple Foundation Models framework, Apple Intelligence (on-device ~3B model), Homebrew (brew), OpenAI SDK (Python, used unchanged), Ollama (transcribed as Olama; comparison only), MLX (comparison only), Llama and Qwen (open-weight models named in comparison)

## Relevance to our work
- **agentos** (1/3):  → *Benchmark a tiny local model against Haiku on classification and commit-message-style tasks before adding any free-tier route to the strategy routing in Govrix Scout.*
- **prosharness** (1/3): ProsHarness drives Claude Code, which needs far more context than 5k tokens. The only fit is cheap side tasks such as generating commit messages. → *Only if ProsHarness spends tokens on trivial sub-steps, consider a local model for them. Do not plan on it for agent loops or checkpoint summaries.*
