# DeepClaude: The Combined Power of Deepseek R1 & Claude 3.5 Sonnet!

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `ymunCZzgzeg` · [watch](https://youtu.be/ymunCZzgzeg) · **date:** 2025-11-02 · **length:** 4:43 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** DeepSeek, Anthropic, Aider
- **topics:** models-research, coding-agents · **tags:** deepclaude, deepseek-r1, claude-3.5-sonnet, reasoning-model, multi-model, chat-ui, rust, api-keys, react, tool-review

> A short walkthrough of DeepClaude, an open-source chat UI that calls DeepSeek R1 and Claude 3.5 Sonnet through their APIs; the presenter installs it, runs one React prompt, and finds it weak as a standalone chat app.

## Summary
The presenter introduces DeepClaude, a tool found on X that pairs DeepSeek R1's chain of thought with Claude 3.5 Sonnet's output through both providers' APIs. The GitHub README describes it as a high-performance LLM inference API with a chat UI, and shows an Aider Polyglot benchmark where R1 plus Sonnet beats R1 alone. The presenter says those benchmarks are not a fully accurate source and gives no figures. Setup needs Rust 1.75, a DeepSeek key and an Anthropic key, a backend build and run, then npm install and npm run dev for the frontend. In the test, a React quote-generator prompt produced working fade animations and favorites, but there was no artifact rendering and a small arrow overlap. The verdict is that the concept is solid but the standalone chat UI is more complicated than convenient, and the presenter suggests it would be more useful as an extension in Cursor or VS Code. The video is a single anecdotal test with no latency, cost or quality measurements.

## Key ideas
- **DeepClaude combines DeepSeek R1's chain of thought with Claude 3.5 Sonnet's response by calling both providers' APIs from one chat UI.** — The presenter describes it as a tool found on X. The GitHub README calls it a high-performance LLM inference API with a chat UI that integrates R1's chain of thought. ([0:00](https://youtu.be/ymunCZzgzeg?t=0))
- **The README's Aider Polyglot benchmark claims R1 plus Sonnet beats R1 alone, but the presenter does not trust it as a full picture.** — No scores are read out on screen. The presenter says the benchmarks are not a fully accurate source of information. ([0:00](https://youtu.be/ymunCZzgzeg?t=0))
- **Setup is a Rust backend plus a Node frontend, and it needs both API keys before anything works.** — Requires Rust 1.75, a DeepSeek API key and an Anthropic API key. The backend is built and started first, then the frontend is installed and started and opened on localhost. ([0:00](https://youtu.be/ymunCZzgzeg?t=0))
- **API requests are configurable in the code, and a chat UI picks the Claude model per chat.** — Keys, system prompts and per-provider settings are entered in the UI. Starting a new chat gives a dropdown of Claude models; the presenter uses the updated Claude 3.5 Sonnet entry. ([1:22](https://youtu.be/ymunCZzgzeg?t=82))
- **The test prompt worked as code generation, but the UI lacks artifact rendering, so the presenter had to wire up display himself.** — The prompt asked for a React quote-generator with fetch, fade-in and fade-out. The model returned full code and dependency notes. There was a minor arrow-over-text overlap, and the quote source is a predefined list rather than an API. ([2:49](https://youtu.be/ymunCZzgzeg?t=169))
- **Verdict: useful concept, weak as a standalone chat app; the presenter suggests an editor extension instead.** — Without artifacts or deeper integration, the presenter finds it more complicated than convenient, and thinks Cursor or VS Code integration would make it practical. ([3:52](https://youtu.be/ymunCZzgzeg?t=232))

## Techniques
- **Dual-provider chat setup** — Clone the DeepClaude repo, build the Rust backend, run it, then cd into the frontend folder, run npm install and npm run dev, open the localhost URL, and enter the DeepSeek and Anthropic API keys in the settings panel. The exact build and run commands are not spelled out in the transcript; they are shown on screen in the README. *When:* Trying side-by-side reasoning-model plus chat-model output in one UI without writing glue code.
- **Single-prompt comparison test** — Paste one concrete UI-generation prompt (a React component with a fetch, a fade-in and fade-out animation, and specific behaviors), then check whether the code runs and whether the interface supports the expected features such as artifact rendering. *When:* A quick smoke test of a new model wrapper before trusting it on real work. The presenter used it to judge both code quality and UI fit.
- **Per-chat model switching** — Start a new chat from the sidebar and pick a different Claude model from the dropdown; system prompts and keys are set per configuration in the settings section. *When:* Comparing Claude model versions or prompt configs without leaving the UI.

## Numbers
- Rust 1.75 is the minimum toolchain version the README calls for. ([0:00](https://youtu.be/ymunCZzgzeg?t=0))
- Benchmark claim (no numbers shown or quoted): R1 plus Sonnet outperforms R1 on Aider's Polyglot benchmark. ([0:00](https://youtu.be/ymunCZzgzeg?t=0))
- Test run: one React component prompt, one arrow-overlap visual bug, and no artifact rendering; no latency, token or cost figures given. ([2:49](https://youtu.be/ymunCZzgzeg?t=169))

## Hot takes
- The concept of pairing a reasoning model with a chat model is solid, but the standalone chat UI is not useful; an editor extension would be better.
- The GitHub benchmark is not a reliable source of evidence, according to the presenter.
- Hype title ('Combined Power') with thin substance: one anecdotal prompt and no measurements, so quality is capped at 2.

## Tools mentioned
DeepClaude, DeepSeek R1, Claude 3.5 Sonnet, Rust 1.75, npm, React, Aider Polyglot benchmark

## Relevance to our work
- **agentos** (1/3): Mixing a reasoning model with a chat model is a routing pattern AgentOS's strategy routing could care about, but this video gives no measurements. → *Only if the Govrix strategy router is ever tested with a reasoning-model plus chat-model pair: compare output quality and cost on a fixed prompt set, not on a single anecdote.*
- **prosharness** (1/3): ProsHarness already runs plan, critique (Codex) and debate across models; this is another two-model pattern, but the video is a single anecdotal test. → *Read the R1 chain-of-thought plus Sonnet pairing as a cheap comparison point for the plan-critique step; do not change the harness based on this video.*
