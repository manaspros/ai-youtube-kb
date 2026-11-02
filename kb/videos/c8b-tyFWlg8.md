# GPT-5.4: The Pros & Cons

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `c8b-tyFWlg8` · [watch](https://youtu.be/c8b-tyFWlg8) · **date:** 2026-04-02 · **length:** 5:41 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Unnamed Better Stack host · **orgs:** OpenAI, Artificial Analysis, Anthropic, Google, Design Arena
- **topics:** models-research, coding-agents, token-cost-efficiency, mcp-and-tools · **tags:** gpt-5.4, openai, codex, computer-use, playwright, tool-search, fast-mode, long-context-pricing, mcp, model-review

> Better Stack's 5-minute review of OpenAI's GPT-5.4: native computer use, tool search and a fast mode on the upside; slower output, a long-context price cliff and a generic UI style on the downside.

## Summary
The host summarizes OpenAI's GPT-5.4 release (2026-04-02) as an all-rounder that combines Codex 5.3 coding with GPT-5.2 knowledge-work and web-search skills, citing Artificial Analysis rankings. The most interesting feature is native computer use, with an experimental Playwright skill. In one Codex test (a 3D Tower Bridge scene), the model ran for about 30 minutes per prompt, opened a browser, screenshotted its work, and fixed issues in a loop, finishing in roughly 1.5 hours over three prompts. The new "fast mode" is presented as the same model served at up to 1.5x token speed for 2x usage billing. Tool search is the other headline change: the prompt carries a lightweight tool list and the model fetches full definitions on demand, with OpenAI claiming up to 47% fewer tokens on a 36-MCP-server benchmark at equal accuracy. The cons are slower time-to-first-token and time-to-500-tokens on Artificial Analysis (the host is unsure whether model or provider is to blame), API pricing of $2.50/$15 per million input/output tokens for the base model and $30/$180 for the pro model, input beyond 272K tokens billed at double, and a UI style the host finds repetitive. The host says he will daily-drive it despite these points.

## Key ideas
- **GPT-5.4 is positioned as a general-purpose all-rounder: Codex 5.3 coding strength merged with GPT-5.2 knowledge-work and web-search skills, with a 1M-token context window.** — Host cites Artificial Analysis ranking it top for coding and agentic work and roughly tied with Gemini for overall intelligence. These are third-party benchmark claims the host relays, not his own tests. ([0:00](https://youtu.be/c8b-tyFWlg8?t=0))
- **Native computer use is the most notable change: the model can write code to drive a browser through Playwright or issue mouse and keyboard actions from screenshots.** — OpenAI released an experimental Playwright skill. The host used it in Codex with high reasoning and an image-generation skill to build a 3D Tower Bridge scene. ([0:56](https://youtu.be/c8b-tyFWlg8?t=56))
- **In the hands-off Playwright loop, the agent opens the browser, clicks around the scene, spots visual bugs (e.g. a background not blending in), edits the code, and repeats.** — The first iteration took about 30 minutes from one prompt. Follow-ups for boats facing the wrong way and road clipping each ran about 30 minutes; the total was roughly 1.5 hours across three prompts. The result is imperfect but was produced hands-off. ([1:54](https://youtu.be/c8b-tyFWlg8?t=114))
- **Tool search replaces loading every tool definition into the prompt with a lightweight tool list plus an on-demand lookup.** — The model appends a full definition to the conversation only when it needs that tool. OpenAI claims up to 47% fewer tokens on a 36-MCP-server benchmark with the same accuracy. The host frames large MCP setups as a context-bloat problem that can hurt output quality. ([1:54](https://youtu.be/c8b-tyFWlg8?t=114))
- **Fast mode is the same model and intelligence with up to 1.5x faster token output, billed at 2x usage, so it works as a priority tier rather than a different model.** — The host noticed the product suggesting fast mode would have saved about an hour during a two-hour session. ([1:54](https://youtu.be/c8b-tyFWlg8?t=114))
- **Speed is a con: GPT-5.4 has among the longest time-to-first-token and time-to-500-tokens on Artificial Analysis, and the host is unsure whether the cause is the model or the provider.** — The host speculates the model may think longer than needed, and suggests fast mode as the workaround. ([3:22](https://youtu.be/c8b-tyFWlg8?t=202))
- **Long-context pricing has a cliff: input beyond 272,000 tokens is billed at double the normal rate, so the host suggests compacting context before crossing that point.** — Pro-tier API pricing is $30 per million input tokens and $180 per million output tokens, against $2.50 and $15 for the base model. ([4:25](https://youtu.be/c8b-tyFWlg8?t=265))
- **UI generation is a weakness in the host's single test: GPT-5.4 gave a frosted-card look with gradients, which he found similar across GPT models, and he preferred Opus 4.6's cafe website.** — The host says Design Arena ranking is also weak for OpenAI on design. He calls this subjective and based on one test. ([4:25](https://youtu.be/c8b-tyFWlg8?t=265))

## Techniques
- **Tool search (deferred tool definitions)** — Keep a lightweight list of available tools in the system prompt. Expose a tool-search capability so the model fetches a tool's full definition and appends it to the conversation only when it needs that tool. OpenAI reports up to 47% fewer tokens on a 36-MCP-server benchmark at equal accuracy. The video shows only OpenAI's built-in version and gives no implementation details. *When:* When many tools or MCP servers are attached and their definitions are bloating the prompt and hurting output quality.
- **Playwright self-verification loop for front-end work** — Give the coding agent a browser-driving skill (here OpenAI's experimental Playwright skill). Let it open the app, click around, screenshot and find visual issues, then edit the code and repeat without supervision. The host ran it for about 30 minutes per prompt. *When:* For visual or interactive web/3D work where the agent has to check its own output in a real browser.
- **Compact context before the long-context price cliff** — Track input token count and compact or trim context before it passes 272K tokens, since input beyond that is billed at double. The video suggests this as a cost guard but shows no tooling. *When:* When using a model with a 1M context window and tiered pricing on long inputs.
- **Fast mode as a priority tier** — Switch to the priority tier to get up to 1.5x token speed at 2x usage billing, with the same model and output quality, when latency matters more than cost. *When:* For long interactive coding sessions where waiting on tokens costs more time than the extra usage.

## Numbers
- 1M-token context window ([0:00](https://youtu.be/c8b-tyFWlg8?t=0))
- First iteration of the 3D Tower Bridge scene took about 30 minutes from one prompt; three prompts totaled about 1.5 hours ([0:56](https://youtu.be/c8b-tyFWlg8?t=56))
- Fast mode: up to 1.5x faster token speed, billed at 2x usage ([1:54](https://youtu.be/c8b-tyFWlg8?t=114))
- Tool search: up to 47% token reduction on a 36-MCP-server benchmark, same accuracy (OpenAI claim) ([1:54](https://youtu.be/c8b-tyFWlg8?t=114))
- Base model API price $2.50 per 1M input tokens and $15 per 1M output tokens ([4:25](https://youtu.be/c8b-tyFWlg8?t=265))
- Pro model API price $30 per 1M input tokens and $180 per 1M output tokens ([4:25](https://youtu.be/c8b-tyFWlg8?t=265))
- Input beyond 272,000 tokens is billed at double the normal rate ([4:25](https://youtu.be/c8b-tyFWlg8?t=265))

## Hot takes
- The host calls GPT-5.4 a 'no-brainer upgrade' over Codex 5.3 for Codex users, based on one 3D-scene test.
- The host says the fast mode is 'the exact same model' with a priority tier, so it is not a different model.
- The host suspects GPT-5.4's slowness may be a provider problem rather than a model problem, and says that may improve over time.
- The host says GPT models share a 'very similar UI' style (frosted cards, gradients) and that OpenAI is not strong at design at the moment, based on one prompt.

## Tools mentioned
GPT-5.4, Codex (5.3 referenced as the prior default), GPT-5.2 (referenced), Playwright (experimental skill), image generation skill (unnamed), Opus 4.6, Gemini, Artificial Analysis (benchmarks), Design Arena (design ranking)

## Relevance to our work
- **agentos** (2/3): Long-context tiered pricing (2x above 272K input) and per-model token-speed-vs-cost tradeoffs are inputs for L1 budget enforcement and strategy routing in Govrix Scout. → *Add a pricing-tier-aware check to the budget/routing layer so requests crossing a long-context threshold are flagged, compacted or re-routed before billing doubles.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, which faces the same MCP tool-definition bloat that tool search addresses; the video describes OpenAI's feature only. → *Measure how many prompt tokens MCP tool definitions consume in a ProsHarness run, and check whether Claude Code's deferred tool loading covers that case before building anything custom.*
