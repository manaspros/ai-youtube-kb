# Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `uiP88SpCi1Q` · [watch](https://youtu.be/uiP88SpCi1Q) · **date:** 2026-07-18 · **length:** 5:55 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Erik Hanchett · **orgs:** AWS
- **topics:** token-cost-efficiency, infra-cost-scaling, context-engineering, agent-architecture · **tags:** token-cost, prompt-caching, model-routing, sliding-window, tool-result-offload, tool-loop-cap, strands-agents, observability

> An AWS developer advocate lists five ways to cut agent token spend: cache the system prompt, route by task difficulty, offload large tool results, cap tool loops, and trim conversation history, with per-tool observability to check each one.

## Summary
Erik Hanchett (AWS) gives a six-minute lightning talk on reducing token costs for agents, using the Strands Agents SDK in his examples. His five tips are to cache the system prompt (and ideally tool definitions and messages), route requests to cheaper or stronger models by difficulty, store large tool results outside the context and send only a summary, cap the number of agent loop iterations, and trim history with a sliding window plus summarization of older turns. He also recommends running observability on every tool to see how long each call takes and how often it loops before deploying. The talk has no benchmarks or measured savings; the value is a checklist of cheap, concrete levers. Code shown is pseudocode, so the patterns are the takeaway rather than an implementation.

## Key ideas
- **Cache the system prompt so only the first call sends it in full** — With prompt caching turned on (shown as a cache_prompt setting in Strands), later calls send a much smaller system prompt. The speaker says tool definitions and messages can be cached too. ([0:00](https://youtu.be/uiP88SpCi1Q?t=0))
- **Route each request to a model sized to its difficulty** — Use a frontier model for hard tasks and a cheap model such as Claude Haiku for simple ones, with Sonnet in between. Routing can be an if-statement or a very cheap model that picks the model. His advice: do not use the most expensive model for everything. ([1:25](https://youtu.be/uiP88SpCi1Q?t=85))
- **Keep large tool results out of the context on every loop** — Store big tool outputs locally or in the cloud, then pass a summary back to the model. Without this, the full result is re-sent on each agent loop iteration. ([1:25](https://youtu.be/uiP88SpCi1Q?t=85))
- **Cap the number of tool loop iterations** — Agents sometimes call the same tool 10 or 20 times, or loop without end. Set a max-iterations limit on the agent loop. ([2:47](https://youtu.be/uiP88SpCi1Q?t=167))
- **Measure tool calls with observability before deploying** — Track each tool's duration and how many times it is called in a loop, so inefficient tools can be found and tuned. ([2:47](https://youtu.be/uiP88SpCi1Q?t=167))
- **Trim history with a sliding window and summarize what falls out** — Strands has a sliding window conversation manager that keeps only the last N messages (10 in the example). The trade-off is losing early history, so the speaker suggests summarizing dropped turns into the context. ([2:47](https://youtu.be/uiP88SpCi1Q?t=167))

## Techniques
- **System prompt and tool caching** — Enable prompt caching on the agent (cache_prompt set to default in Strands). The first call sends the full system prompt, and later calls reuse the cached copy. Tool definitions and messages can be cached as well. *When:* A stable system prompt or tool set is sent on many calls in a row.
- **Difficulty-based model routing** — Add a routing step that picks the model per request, using an if-statement on task type or a cheap model that classifies difficulty. Easy tasks go to a small model such as Haiku, harder ones to Sonnet or a frontier model. *When:* The workload mixes simple and hard requests and the expensive model is not needed for most of them.
- **Tool result offload and summarization** — When a tool returns a large result, save it to local or cloud storage and put only a summary in the agent context. Strands offers APIs for this, but the speaker showed a manual version. *When:* A large tool result would otherwise be re-sent on every iteration of the agent loop.
- **Max-iteration cap on tool loops** — Set a fixed maximum number of agent loop iterations so a repeated tool call cannot run unbounded. *When:* Any agent that decides its own tool calls, to prevent runaway loops and unexpected token spend.
- **Per-tool loop and latency observability** — Before shipping, run observability tooling to record each tool's run time and how many times it is called in a loop. Use the data to find and tune the least efficient tools. *When:* Pre-deployment review of an agent's tool usage.
- **Sliding window history with summarization** — Use a conversation manager that sends only the last N messages (10 in the example, configurable). When the window slides, summarize the dropped history and place the summary in context. *When:* Long multi-turn conversations where full history is re-sent on every turn.

## Numbers
- Sliding window conversation manager keeps only the last 10 messages (configurable) ([2:47](https://youtu.be/uiP88SpCi1Q?t=167))
- A tool can be called 10 or 20 times in a loop when the tool call is not capped ([2:47](https://youtu.be/uiP88SpCi1Q?t=167))
- Full conversation history re-sent on every call can cost hundreds, if not thousands, of tokens (qualitative, no measured figure) ([2:47](https://youtu.be/uiP88SpCi1Q?t=167))
- Talk length is 5:55 and lists five techniques; no benchmarks or measured savings are given ([0:00](https://youtu.be/uiP88SpCi1Q?t=0))

## Hot takes
- Do not use the most expensive model for everything you do.
- Always set a max-iterations limit on the agent loop; an uncapped tool loop can run 10 to 20 times or never stop.
- Tool results need not be re-sent to the model on every loop iteration; summarize them instead.

## Tools mentioned
Strands Agents, Claude Haiku, Claude Sonnet

## Relevance to our work
- **agentos** (2/3): AgentOS L1 Govrix Scout already has budgets and strategy routing; the talk's difficulty routing and per-tool loop caps map onto that layer. → *Use Govrix Scout strategy routing to send simple requests to a cheap model and harder ones to a stronger model, and log the chosen model per request so savings can be measured.*
- **prosharness** (2/3): ProsHarness runs long Claude Code agent loops with checkpoint and resume, so uncapped loops and unbounded history carry real token cost there. → *Add a max-iteration cap and a per-run tool call counter to ProsHarness agent loops, and use the counts in checkpoint logs to spot runaway tools.*
