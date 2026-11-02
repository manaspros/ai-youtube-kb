# The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `spNAUEgq_A8` · [watch](https://youtu.be/spNAUEgq_A8) · **date:** 2026-07-18 · **length:** 30:38 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Justin Schroeder · **orgs:** Standard Agents, Vercel
- **topics:** multi-agent, context-engineering, agent-architecture, infra-cost-scaling · **tags:** domain-specific-agents, composition-over-inheritance, subagents, mcp-critique, skills, token-cost, small-language-models, agent-portability, permissions, hooks, stealth-product-pitch

> Justin Schroeder (Standard Agents) argues that small, isolated domain-specific agents composed under a coordinator beat ever-growing context-stuffed general agents on cost, scope, portability and scaling.

## Summary
The speaker says agents are deterministic software wrapped around non-deterministic model output, and that "agent" and "harness" are effectively the same thing. He argues the real problem is integration: businesses want their data inside AI, but building robust agents is hard, and MCP has mostly become a tool-distribution mechanism. He says stacking skills and MCP servers onto one general agent is inheritance, which degrades as the count grows, and proposes composition instead: small full agents, each with its own system prompt, tools, message history and loop, coordinated by a parent that talks to them in plain English. He claims this gives large token savings (over 80% per task at his company), lets cheap or non-LLM models handle narrow tasks, enforces tighter permissions, and scales by running many small sandboxed instances. He sketches an ideal agent anatomy (functions, prompt tools, sub-agent tools, hooks, rules, a filesystem and sandboxed execution) and recursive sub-agent trees. He is candid that these agents are not yet public, and the talk closes with predictions for late 2026 and 2027, plus a claim that token prices are rising.

## Key ideas
- **Agents are deterministic software that harnesses non-deterministic model output toward an objective; agent and harness can be treated as the same thing.** — The speaker defines an agent this way and says the agent/harness distinction is pedantic. He uses this framing for the rest of the talk. ([2:24](https://youtu.be/spNAUEgq_A8?t=144))
- **The real bottleneck is integration of business data into AI, and MCP has mainly served as a tool-distribution layer.** — Businesses build custom agents to get their data integrated. Agents are hard to build (agentic loop, provider abstraction, durable execution, validation, stop conditions), and telemetry, portability and composability are poor. He says MCP clients mostly support tools only, and that tools alone are not enough. ([7:19](https://youtu.be/spNAUEgq_A8?t=439))
- **Almost everything an agent runs on is context: system prompt, tools, skills, MCP, and messages. Skills are markdown documentation that can hurt performance when used in large numbers.** — He cites research (not shown) that many skills make an agent substantially worse. He frames the stack as model, system prompt, tools, skills, MCP, then messages, and says current progress happens in the context and model layers. ([9:30](https://youtu.be/spNAUEgq_A8?t=570))
- **Stacking capabilities onto one agent is inheritance, and it breaks down. Composition is the alternative.** — Five skills work fine on a general agent, but at 100 or 1,000 skills returns diminish. The alternative is a small agent per domain (for example, Figma) with its own tight system prompt, precise tools, and small message history. ([12:57](https://youtu.be/spNAUEgq_A8?t=777))
- **Sub-agents talk to the coordinator in natural language, and the coordinator sends only a narrow request so each sub-agent keeps minimal context.** — Example: the primary agent asks the Gmail agent for the latest email from a named person, and the only context passed is the system message, its tools, and that request. Each sub-agent is a full agent with its own loop, not a server with tools. ([14:13](https://youtu.be/spNAUEgq_A8?t=853))
- **Domain-specific agents claim gains in token cost, model choice, permissions and scaling.** — He lists four benefits: token efficiency (over 80% per task at his company), cheap small or non-LLM models for narrow tasks, enforceable capability limits that help with IT approval, and parallel scaling because each agent is its own small execution environment. He says none of these are proven publicly. ([15:37](https://youtu.be/spNAUEgq_A8?t=937))
- **Ideal agent anatomy: functions, prompt tools, sub-agent tools, hooks, rules, a filesystem and sandboxed code execution.** — Hooks can mutate or side-effect the loop. For example, a hook can inject an artificial message or tool call carrying the current time, since LLMs do not know the time. Rules cover turn limits and validation requirements. Each agent gets its own file system and sandbox. ([25:01](https://youtu.be/spNAUEgq_A8?t=1501))
- **Sub-agents can be nested into a tree, with one coordinator delegating to domain agents that delegate further.** — Example: a coordinator calls a Salesforce agent, which calls Google Workspace and asset-generation sub-agents. A legal-team agent checks output and calls GDPR and OSHA compliance agents, so no single agent carries all the context. ([28:18](https://youtu.be/spNAUEgq_A8?t=1698))

## Techniques
- **Composition of isolated domain agents** — Give each domain (e.g. Gmail, Figma, Salesforce) its own system prompt, narrow tools, small message history and own agent loop. The coordinator sends short natural-language requests and gets short natural-language answers back. *When:* When one general agent is accumulating skills and MCP servers and context bloat or tool confusion is growing.
- **Scoped delegation requests** — The coordinator does not forward the full conversation to a sub-agent. It sends one targeted request (e.g. get the last email from a named sender) so the sub-agent sees only its system message, tools and that request. *When:* When sub-agent calls are cheap or narrow tasks and token cost matters.
- **Per-task model routing** — Route tasks picked for them to small or cheap models, and to non-LLM models such as image generation or diffusion, while the coordinator uses a frontier model. *When:* When a task is narrow and well defined, and retries are rare enough that the cheaper model still wins on total cost.
- **Hook-injected runtime facts** — Insert a synthetic message or tool call into the message history that supplies facts the model lacks, such as the current time, instead of putting them in the system prompt. *When:* When the model needs live state that it cannot know, such as time, and you want it to stay out of the static prompt.
- **Capability scoping per agent** — Limit each agent to explicitly approved tools and actions, so the permission model is the set of tools the sub-agent has rather than dialog prompts on a general agent. *When:* When IT or security review needs a bounded, auditable capability set for an agent.
- **Recursive sub-agent tree** — Let sub-agents call their own sub-agents (e.g. a legal agent calling GDPR and OSHA agents), each with a minimal context window. *When:* When one domain has its own large body of rules or tools that would otherwise swamp the parent context.

## Numbers
- Domain-specific agents reach over 80% token efficiency per task (the speaker's company's observation; no published data). ([15:37](https://youtu.be/spNAUEgq_A8?t=937))
- DeepSeek V4 Flash is about 137 times cheaper per task than Fable 5, with the caveat that cost advantage disappears if the cheap model retries repeatedly. ([18:14](https://youtu.be/spNAUEgq_A8?t=1094))
- Speaker's own price tracker: token cost per unit of intelligence (IQ-adjusted) rose about 29% in the first half of 2026, which he says reversed the cost-decline trend. ([22:37](https://youtu.be/spNAUEgq_A8?t=1357))
- Unadjusted token prices are up about 76% in 2026 so far, per the speaker. ([22:37](https://youtu.be/spNAUEgq_A8?t=1357))
- Illustrative only: a GDPR context of about 45 megabytes would be too large to keep in the main agent. ([29:19](https://youtu.be/spNAUEgq_A8?t=1759))

## Hot takes
- An agent and a harness are the same thing, and the distinction is pedantic.
- MCP has become a tool-distribution mechanism and has not delivered much other value.
- Stacking skills and MCP servers onto one agent is inheritance, and it breaks down. Composition over inheritance is the answer.
- Token prices are going up in 2026, not down, even adjusted for capability.
- Prediction: late 2026 will see a sharp rise in domain-specific agents, and 2027 will be the year of multi-agent orchestration.

## Tools mentioned
Claude, Codex, OpenClaw, Hermes, MCP, Vercel AI SDK, Vercel Eve, Figma, Playwright, Gmail, Google Sheets, Google Workspace, Salesforce, DeepSeek V4 Flash, Fable 5, GLM 5.2, Nano Banana, DMUX, Arrow.js

## Relevance to our work
- **agentos** (2/3): The talk's cost and small-model argument maps onto AgentOS's routing and budget pillars, and it makes a claim about per-agent scoped context that AgentOS could test on its own pipelines. → *Benchmark one narrow AgentOS task (e.g. a classification or extraction step) run as a sub-agent with minimal context and a small model against the same step in the full agent, measuring cost, retries and success rate.*
- **general** (1/3): General signal that composition beats stacking context, though the talk's evidence is anecdotal.
