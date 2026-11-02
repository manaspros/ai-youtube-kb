# Can AI Agents Finally Automate the Web? (BrowserOS Review)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `rIZ8OBHL7Zo` · [watch](https://youtu.be/rIZ8OBHL7Zo) · **date:** 2025-11-02 · **length:** 8:05 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andres · **orgs:** Better Stack, BrowserOS, Perplexity, OpenAI, Opera, Fellow AI, Google, Ollama, Brave, Arc, Dia, Amazon
- **topics:** voice-multimodal, local-ai, dev-tools · **tags:** agentic-browser, browseros, ollama, local-llm, browser-agent, open-source, gemini, gemma, mcp

> Better Stack reviews BrowserOS, an open-source Chromium-based agentic browser; the built-in agent works on Gemini, but local Ollama models mostly failed the Amazon cart task.

## Summary
The video surveys agentic browsers (Perplexity Comet, Opera Neon, Fellow AI, OpenAI Operator, BrowserOS) and reviews BrowserOS, a free, open-source, Chromium-based browser pitched as privacy-first with bring-your-own API keys and local Ollama support. The UI adds three buttons (LLM Chat, LLM Hub, Agent); the reviewer judges the first two as thin wrappers and the Agent as the real feature. The agent added two items to an Amazon cart, but it took several minutes, was slower than doing it by hand, and ran on Gemini 2.5 credits from the makers. Setting up Ollama takes a few steps (pull a model, run ollama serve, set the origins variable, point the provider settings at the model). In the reviewer's tests, most local models failed the Amazon task, some lacked browser-tool support, and even Gemma 3 failed, which he attributes to an instruction set tuned for Gemini with no easy way to change it. The only workaround he names is rebuilding from source per the repo's build readme. The verdict is that the project is promising but early for web automation.

## Key ideas
- **Agentic browsers are a crowded new category: the reviewer counts about five (Perplexity Comet, Opera Neon, Fellow AI, OpenAI Operator, BrowserOS), with an embedded agent that automates navigation tasks like forms, bookings and shopping.** — Framing only; he positions Operator as not quite a browser on its own. BrowserOS is distinguished by being fully open source. ([0:00](https://youtu.be/rIZ8OBHL7Zo?t=0))
- **BrowserOS pitch: a free, open-source Chromium-based AI browser with privacy framing, bring-your-own API keys (OpenAI, Gemini, Anthropic), local models via Ollama, and claimed MCP support.** — He contrasts it with Chrome (little evolution), Brave (spread across crypto, search, VPN), and Comet (search/ad business model). These are the project's own arguments, relayed by him. ([1:16](https://youtu.be/rIZ8OBHL7Zo?t=76))
- **The UI is Chrome plus three buttons: LLM Chat (side panel for ChatGPT, Claude, Grok, Gemini or Perplexity, with page-copy to clipboard), LLM Hub (three chatbots side by side), and Agent (the real feature).** — He calls LLM Chat handy but unremarkable and LLM Hub a flex. Only the Agent button is treated as the substantive capability. ([2:38](https://youtu.be/rIZ8OBHL7Zo?t=158))
- **The agent is slow: adding AirPods and an iPad mini to an Amazon cart took several minutes, slower than doing it manually. It scrapes the page, detects elements and reasons about which to click.** — Out of the box it uses Gemini 2.5 through the makers' account, which includes free starter credits that can run out quickly with heavy use. ([3:45](https://youtu.be/rIZ8OBHL7Zo?t=225))
- **Local Ollama models were mostly unusable for this agent: most failed the simple Amazon task, some could not interact with the page because they lack browser-tool support, and Gemma 3 (the open model family behind Gemini) also failed.** — He blames the agent's instruction set, which he says is tuned to Gemini and cannot be swapped easily in the UI. Users have requested this on the Discord. ([5:59](https://youtu.be/rIZ8OBHL7Zo?t=359))
- **The escape hatch is changing the agent behavior at source level: rebuild the project from the repo's build readme. He still calls the project promising, citing its open-source status and active Discord community.** — Verdict: early days for web automation, with a fixed prompt/instruction set as the main barrier to running local models. ([7:00](https://youtu.be/rIZ8OBHL7Zo?t=420))

## Techniques
- **Run BrowserOS's agent on a local Ollama model** — 1) Install Ollama. 2) Use the Ollama CLI to download the model you want. 3) Start the server with `ollama serve`, with the OLLAMA_ORIGINS environment variable set to a wildcard so BrowserOS can query it (the speaker says 'empty wildcard'). 4) In BrowserOS, open Settings, click BrowserOS, and open the AI provider settings. 5) Set the provider to Ollama and enter the exact model name you are serving. *When:* When you want the agent fully local and private. Expect poor task success with most open models; see the next technique.
- **Evaluate candidate models on a browser-agent task before relying on them** — Use a concrete multi-step task (add specific items to an Amazon cart) and check whether the model supports browser tools at all. Test sibling models too; he tried Gemma 3 to see whether a Gemini-family model worked, and it did not. *When:* Before routing an agent to a local or cheaper model. Tool-call and browser-tool support can fail outright, separately from reasoning quality.
- **Customize an agent's instructions by rebuilding from source** — Follow the build readme in the BrowserOS repo to rebuild from source, then modify the agent's instruction set in code. The reviewer says this is the only way to change it, since the UI offers no option. *When:* When the default agent prompt is tuned to one model and you need it to work with another. This is a developer-level change, not a settings toggle.

## Numbers
- About five agentic browsers exist (Comet, Opera Neon, Fellow AI, OpenAI Operator, BrowserOS), per the reviewer's count. ([0:00](https://youtu.be/rIZ8OBHL7Zo?t=0))
- BrowserOS adds three buttons to Chrome: LLM Chat, LLM Hub and Agent. ([2:38](https://youtu.be/rIZ8OBHL7Zo?t=158))
- The Amazon cart task (two items) took several minutes, which is slower than doing it by hand. ([3:45](https://youtu.be/rIZ8OBHL7Zo?t=225))
- The default agent runs on Gemini 2.5 via the makers' account with free starter LLM credits that can be used up quickly. ([3:45](https://youtu.be/rIZ8OBHL7Zo?t=225))
- Most tested Ollama models failed the Amazon task, some lacked browser-tool support, and Gemma 3 also failed. ([5:59](https://youtu.be/rIZ8OBHL7Zo?t=359))

## Hot takes
- Agentic browsers for web automation are still very early: a simple cart task took minutes and was slower than manual.
- The LLM Hub side-by-side view is 'a flex' and probably not useful to most users.
- The default agent's instruction set is tied to Gemini, so swapping in another model may require rebuilding the project from source.
- Open-source and privacy positioning is a real differentiator versus Comet, but the local-model story did not work in this test.

## Tools mentioned
BrowserOS, Chromium, Chrome, Perplexity Comet, Opera Neon, Fellow AI, OpenAI Operator, Brave, Arc, Dia, Ollama, Gemini 2.5, Gemma 3, ChatGPT, Claude, Grok, Perplexity, MCP

## Relevance to our work
- **agentos** (1/3): Per-model instruction tuning and tool-call support gaps matter if AgentOS routes agent traffic across models, including local ones served by vLLM or Ollama. → *When adding strategy routing, add a per-model capability check (tool or browser-tool calling) and a small fixed task suite before a model is eligible to route.*
- **general** (1/3): The reviewer's test method (fixed multi-step task across models, noting failures and latency) is a reusable quick eval for agent models. → *Keep a short set of end-to-end agent tasks, such as a cart add, and run candidate local models through them before adopting one.*
