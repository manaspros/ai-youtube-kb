# Sora 2 Cameos & Jailbreaks & Claude Agent SDK | Better Stack Podcast Ep. 5

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `YjdMscni2CI` · [watch](https://youtu.be/YjdMscni2CI) · **date:** 2025-11-02 · **length:** 44:19 · **format:** panel · **quality:** 2/5 · **depth:** intro
- **speakers:** James, Richard, Andres · **orgs:** Better Stack, OpenAI, Anthropic, ByteDance, Firecrawl, Tencent, Stripe, Etsy, Shopify, Cloudflare
- **topics:** claude-code, agent-architecture, voice-multimodal, context-engineering · **tags:** sora-2, veo, claude-agent-sdk, claude-code, claude-code-hooks, custom-tools, system-prompt, mcp, context-management, memory-tool, jailbreaks, copyright, training-data, model-benchmarks, comfyui, glm-4-6, typescript, podcast

> Better Stack podcast: hosts riff on Sora 2's cameo feature, memorized training data and weak guardrails, then on the Claude Agent SDK for custom agents with their own prompts, tools and hooks. Mostly opinion.

## Summary
Three Better Stack hosts discuss OpenAI's Sora 2 video model, which launched as a TikTok-style feed with a "cameo" feature that lets users insert their face and voice into generated clips. Their informal tests suggest the model reproduces well-known characters and viral clips and that its filters are easy to get around, and they call the feature overhyped. The second half covers the Claude Agent SDK, which the hosts describe as the programmatic layer behind Claude Code: you can replace its default system prompt, register your own tools, and use hooks that inspect tool output before it reaches the user. They also cover context trimming, a memory tool that stores memories outside the context window, and the view that frontier coding models have converged, so benchmarks matter less than trying a model on a real project. Nearly all claims are anecdotal or opinion, with no code, benchmarks or sources shown.

## Key ideas
- **The Claude Agent SDK is presented as the programmatic layer behind Claude Code, and the speakers say it is the only route that lets you replace Claude Code's default system prompt entirely (output styles only append to it).** — Build a custom agent on the same engine as Claude Code but with your own system prompt. This is a speaker claim that should be checked against the SDK docs. ([25:41](https://youtu.be/YjdMscni2CI?t=1541))
- **A speaker reports that MCP tools are inconsistently chosen by the model, so custom tools written into the codebase with clear trigger conditions are more dependable.** — Tell the agent when to call a specific local function instead of hoping it picks the right MCP tool. Anecdotal, from one speaker's experience. ([27:04](https://youtu.be/YjdMscni2CI?t=1624))
- **The SDK release included a memory tool that stores memories on your own infrastructure outside the context window, plus a context-management feature that automatically removes context judged irrelevant.** — Memory lives outside the prompt and is retrieved as needed, and the runtime prunes stale context. Only mentioned in passing, with no details. ([28:30](https://youtu.be/YjdMscni2CI?t=1710))
- **Context relevance is treated as the main lever on output quality. The speakers say a large window still degrades when filled with irrelevant material, so trimming matters more than window size.** — Keep context focused on the current task. Claimed trend, with no measurements. ([29:55](https://youtu.be/YjdMscni2CI?t=1795))
- **Hooks can read a tool's output before it is shown, so they can enforce conventions. The example is rejecting npm and requiring bun, which makes the model notice the mistake and redo the call.** — Hooks can also cover linting and function style. The example is continued at 31:13. ([29:55](https://youtu.be/YjdMscni2CI?t=1795))
- **Benchmarks do not predict which coding model suits your project, so the speakers recommend trying each model for about a week on a real, large codebase.** — Differences between frontier coding models are now small and mostly a matter of feel. Opinion, not measured. ([33:31](https://youtu.be/YjdMscni2CI?t=2011))
- **Basic coding is treated as solved across models. The next difficulty is keeping a large, multi-file project coherent, and that is where models still differ.** — Cheap models such as GLM 4.6 are described as good enough for many users. This is the speakers' general view. ([37:21](https://youtu.be/YjdMscni2CI?t=2241))
- **Sora 2 appears to have memorized popular IP (SpongeBob, a Rickroll, a Charlie bit my finger video) and its filters are described as weak, based on the hosts' own prompt tests.** — Prompts asking for a TV showing a cartoon produced SpongeBob, and a different prompt produced a near copy of a Rickroll. Not verified, and the speakers note the same prompt can behave differently across runs. ([9:56](https://youtu.be/YjdMscni2CI?t=596))

## Techniques
- **Custom agent on the Claude Agent SDK with an owned system prompt** — Start an SDK agent and supply your own system prompt in place of Claude Code's default. The speakers say output styles only append, so this is the way to get full control. Verify this claim in the SDK docs first. *When:* You want a Claude Code-like loop with your own behavior and instructions rather than the stock prompt.
- **Local functions as agent tools in place of MCP tools** — Write a function in your own codebase, register it as a tool, and write a clear rule for when the agent should call it (for example, a specific task and its deterministic implementation). *When:* The model picks MCP tools inconsistently and you need a specific action to run reliably.
- **Hook-based output enforcement with automatic redo** — Attach a hook that inspects each tool output before it is displayed. The example checks for npm calls and asks for bun. When the check fails, the model is told about its mistake and redoes the call. The same pattern could cover lint rules or function style. *When:* You have repository conventions the model keeps missing and want them enforced mechanically instead of by prompt alone.
- **Coaching agent that withholds answers** — Configure the agent to ask the learner for their own solution, check it, and point to resources you have programmed in. It gives hints or verdicts rather than the answer. *When:* Building an educational or tutoring agent in place of a tutorial video.

## Numbers
- Sora 2 gives 100 free generations per day, currently only for users in the US or Canada. Clips are 10 seconds. ([2:33](https://youtu.be/YjdMscni2CI?t=153))
- Clips are 10 seconds long. ([11:22](https://youtu.be/YjdMscni2CI?t=682))
- Claude Sonnet 4.5 is claimed by its vendor to be the best coding model in the world. The hosts say the gap is small. ([32:14](https://youtu.be/YjdMscni2CI?t=1934))
- GLM 4.6 is described as costing about $2 per month, with good results for coding. ([37:21](https://youtu.be/YjdMscni2CI?t=2241))

## Hot takes
- Sora 2's appeal comes from the cameo and social features, not from model quality, which the speakers call overhyped.
- Sora 2 seems to have memorized popular IP, and its guardrails are weak. This rests on the hosts' informal tests and is unverified.
- Claude Code being closed source is its main moat, according to the hosts.
- Coding models have converged, so benchmark rankings should be ignored in favor of a week of real-project use.
- TypeScript is winning the AI SDK space, according to one host.
- Sora's viral spread owes more to people re-uploading clips to other platforms than to its own feed.

## Tools mentioned
Sora 2, VO3, Claude Agent SDK, Claude Code, Claude Code hooks, MCP, Claude Sonnet 4.5, Claude Opus, GPT-5, GPT-5 Codex, Codex, Grok 4, Grok Code Fast, GLM 4.6, ComfyUI, Wan video models (Tencent), Firecrawl, LangChain, LangGraph, Mastra, Bun, npm, TypeScript

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI. The Agent SDK exposes the same engine with programmatic control of the system prompt, custom tools and hooks that can check output and force a redo. The speakers' claim that it is the only way to replace the default prompt is unverified. → *Spike a ProsHarness run on the Claude Agent SDK. Verify whether the SDK is the only way to replace the default system prompt, and test a hook that rejects a disallowed command and forces a redo.*
- **agentos** (1/3): The speakers mention a memory tool that stores memories outside the context window and automatic context pruning, but give no detail. Only a passing pointer that overlaps with MemoryMesh's tiered memory. → *Read the Claude Agent SDK memory and context-management docs and compare them with MemoryMesh's cross-session tiers.*
