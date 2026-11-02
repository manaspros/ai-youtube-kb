# Qwen 3 ACTUALLY Made Me Quit Claude Code

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `lXWazKnuZNQ` · [watch](https://youtu.be/lXWazKnuZNQ) · **date:** 2025-11-02 · **length:** 7:52 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** unnamed host · **orgs:** Qwen, Anthropic, Google, OpenRouter, ModelScope
- **topics:** coding-agents, token-cost-efficiency, mcp-and-tools · **tags:** qwen-code, qwen3-coder, claude-code-router, openrouter, free-tier, model-routing, oauth, context7, daisyui, gemini-cli

> Walkthrough of using Qwen Code's free OAuth tier and Claude Code Router to run cheap Qwen3 Coder backends, with a single anecdotal DaisyUI build comparing it to Claude Code.

## Summary
The host presents Qwen Code, a terminal coding agent built on the Gemini CLI codebase, and its free tier of 2,000 runs per day via "OAuth with Qwen" sign-in. He argues the Qwen3 Coder model is strong enough to matter for users on cheaper Claude plans, citing an LM Arena placement he describes as on par with Claude Sonnet 4. He runs one side-by-side test: both agents build a DaisyUI music-player prototype with the Context7 MCP server for docs, and Claude Code produces the more complete result while Qwen Code builds only the player screen. In a second iteration, both follow the requested layout but neither implements DaisyUI components correctly, which he attributes to the models' training data. The second half covers Claude Code Router, which lets Claude Code call other providers, and lists free tiers (Qwen OAuth, ModelScope in mainland China, OpenRouter for Qwen3 Coder). He walks through the router's config file and UI setup, adding an OpenRouter model name, and launching with `ccr code`. The evidence is one anecdotal comparison with no measured quality, latency or cost data.

## Key ideas
- **Qwen Code is a terminal coding agent whose sign-in offers free 'OAuth with Qwen' access, announced by the speaker as 2,000 runs per day.** — Install via npm (the easiest route per the speaker), then choose the OAuth option at the sign-in screen; the browser login returns you to the terminal automatically. ([0:00](https://youtu.be/lXWazKnuZNQ?t=0))
- **The speaker says Qwen Code is built on the Gemini CLI base and keeps its feature set and context-file convention, so it lacks Claude Code's hooks, slash commands and subagents.** — He notes it reuses the Gemini CLI MCP setup process unchanged. He says Claude Code has more features, including hooks, slash commands and subagents, that he credits only Claude with right now. ([2:17](https://youtu.be/lXWazKnuZNQ?t=137))
- **The value of the free tier rests on the Qwen3 Coder model, which the speaker says performs on par with Claude Sonnet 4 on LM Arena.** — He says he used the model in his own workflows before the announcement. He frames the offer as most valuable to people on the $20 Claude plan or with no plan, not Max subscribers. ([2:17](https://youtu.be/lXWazKnuZNQ?t=137))
- **Context7 MCP supplies current library docs, which the speaker treats as necessary for a library models were not trained on.** — He connected Context7 in both agents and told them to use it for DaisyUI, which he says is not a native library LLMs know well. Claude Code produced a functional, colorful player; Qwen Code built only the main player screen. ([3:28](https://youtu.be/lXWazKnuZNQ?t=208))
- **In a second round with a detailed flow spec, both agents followed the requested layout but neither implemented DaisyUI components correctly.** — The speaker attributes this to missing DaisyUI training data, comparing it to better coverage of shadcn components and plain HTML. He says he should have given a proper PRD in the first round. ([4:55](https://youtu.be/lXWazKnuZNQ?t=295))
- **Claude Code Router (CCR) makes Claude Code call non-Anthropic providers through an API, so free tiers can back the same agent.** — He lists OpenRouter, the DeepSeek API, local Llama models and Gemini as options. The free-tier comparison he gives: Qwen OAuth at 2,000 requests per day with no token limit, ModelScope at 2,000 per day in mainland China, and OpenRouter at up to 1,000 per day with Qwen3 Coder listed as free. ([5:37](https://youtu.be/lXWazKnuZNQ?t=337))
- **CCR is configured through a JSON file or a UI mode; you add a provider and a model by pasting the model name from OpenRouter, then launch with `ccr code`.** — He opens the config file in Cursor using the `cursor` command, adds the API key, and says the UI mode lets you add a provider without editing JSON. The provider and model setup commands appear on screen but are not spoken. ([6:53](https://youtu.be/lXWazKnuZNQ?t=413))

## Techniques
- **Qwen Code OAuth sign-in for free runs** — Install Qwen Code from npm, start it, and at the sign-in screen pick 'OAuth with Qwen'. Complete login in the browser; the terminal session is authorized automatically. The speaker says this gives 2,000 runs per day. *When:* When you want a no-cost coding agent for light work and do not need Claude-level feature depth (hooks, subagents, slash commands).
- **Routing Claude Code through Claude Code Router** — Install Claude Code Router after Claude Code is installed (the exact npm command is shown on screen, not spoken). Edit the router's config file (opened in Cursor via the `cursor` command) or use its UI mode to add a provider and its API key. Add a model by copying its name from OpenRouter, pasting it into the router, and saving. Start the session with `ccr code` instead of `claude`. *When:* When you want Claude Code's workflow but a cheaper or free model backend, such as Qwen3 Coder via OpenRouter, for routine tasks.
- **Context7 MCP for libraries models do not know well** — Connect the Context7 MCP server to the agent, then prompt the agent to pull current docs for the library before it writes code. The speaker used this for DaisyUI and says the same MCP setup works in both Claude Code and Qwen Code. *When:* When building with a UI or framework that is newer or less common than the model's training data, where the model would otherwise guess at APIs and class names.
- **Give the agent a PRD before building** — Write a product requirements document describing the app and its flows, then ask the agent to implement it. The speaker's first round used a loose prompt and he says a PRD would have produced a better result. *When:* Before a multi-screen UI build, to avoid the agent's guessing about scope and layout. The speaker names this as a lesson learned, not a measured result.

## Numbers
- Claude Code plan cost quoted as $100 a month; Cursor Pro described as too expensive. Speaker's framing, no source. ([0:00](https://youtu.be/lXWazKnuZNQ?t=0))
- Qwen Code free tier: 2,000 runs per day via Qwen OAuth, which the speaker says was announced August 8. ([1:06](https://youtu.be/lXWazKnuZNQ?t=66))
- Qwen3 Coder, released July, is said to be on par with Claude Sonnet 4 on LM Arena. The speaker reports this from the leaderboard; no score is given. ([2:17](https://youtu.be/lXWazKnuZNQ?t=137))
- Qwen OAuth: 2,000 requests per day, described as having no token limits (speaker claim, not verified in the video). ([5:37](https://youtu.be/lXWazKnuZNQ?t=337))
- ModelScope (mainland China): 2,000 free API calls per day. ([5:37](https://youtu.be/lXWazKnuZNQ?t=337))
- OpenRouter: up to 1,000 free API calls per day; Qwen3 Coder listed as free at 1,000 requests per day. ([5:37](https://youtu.be/lXWazKnuZNQ?t=337))

## Hot takes
- The title says Qwen 3 'made me quit Claude Code', but the speaker keeps recommending Claude Code as the better option and never switches away from it.
- The only comparison is one DaisyUI prototype with n=1, judged by eye, with no measured quality, latency or cost data.
- The 2,000-runs-per-day free tier is a launch promotion the speaker presents as lasting. Its terms could change, and the video does not check that.
- Qwen Code's feature gap versus Claude Code (hooks, slash commands, subagents) is a bigger practical issue for agent workflows than the free request count.
- Claims that Qwen3 Coder is on par with Sonnet 4 rest on a leaderboard reference, with no benchmark numbers shown.
- Quality is capped at 2 because the title is hype and the substance is one anecdotal test. The setup steps are concrete, though.

## Tools mentioned
Qwen Code, Qwen3 Coder, Claude Code, Claude Code Router (ccr), Gemini CLI, Context7 MCP, DaisyUI, OpenRouter, ModelScope, Claude Sonnet 4, Cursor, CLAUDE.md, GEMINI.md, shadcn/ui, LM Arena

## Relevance to our work
- **agentos** (1/3): Routing one agent client across several model providers is the same pattern as the proxy-level model routing AgentOS already does, applied at the client instead of the proxy. → *Compare CCR's provider and model config with Govrix Scout's strategy routing to see whether any routing config shape is worth copying.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, and CCR changes which backend that CLI talks to. Harness behavior like checkpoint/resume could break under a different backend. → *Test one ProsHarness checkpoint/resume run with Claude Code pointed at a non-Anthropic backend through a router, to see what breaks.*
- **general** (1/3): Free-tier models could serve as cheap-model pipeline candidates, but the video gives no measured quality data for that use. → *Run a few real Haiku-style pipeline tasks (entity extraction or classification) against Qwen3 Coder through a free tier and compare output to Haiku before trusting it.*
