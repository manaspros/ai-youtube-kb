# OpenAI Swarm Hype Explodes: AgentKit Drives Multi-Agent AI Revolution

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `oV3IjJSXQyM` · [watch](https://youtu.be/oV3IjJSXQyM) · **date:** 2026-01-02 · **length:** 6:07 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Narrator (unnamed Better Stack host) · **orgs:** OpenAI, Anthropic, Klarna, Ramp, Dropbox, Microsoft Teams, Meta, DeepSeek, McKinsey
- **topics:** multi-agent, agent-architecture, mcp-and-tools · **tags:** openai-swarm, agentkit, agent-builder, chatkit, agents-sdk, multi-agent, handoffs, mcp, vendor-lock-in, agent-tracing, latency, hype-check

> Better Stack argues OpenAI's deprecated Swarm is not back and that AgentKit (Oct 2025) is the real multi-agent upgrade, but the video gives few technical details and mostly unsourced claims.

## Summary
The video responds to social-media hype about OpenAI's Swarm framework, stating that Swarm was a 2024 experimental, stateless handoff framework under 100 lines, deprecated in March 2025 in favor of the Agents SDK. The speaker presents AgentKit, launched at DevDay on October 6, 2025, as the production successor, describing its visual Agent Builder, ChatKit embedding, a connector registry of 200+ integrations, and built-in guardrails and evals. He cites customer results (Klarna, Ramp) and model claims (o4-mini token efficiency, RFT beta) without links or methodology. The main technical caveat is that multi-agent systems produce large traces, handoffs, retries and planning steps, so latency grows quickly. The debate over vendor lock-in (AgentKit) versus open standards (MCP) is raised but not analyzed. Overall it is a news-style hype piece with a few verifiable product facts and little reproducible detail.

## Key ideas
- **OpenAI Swarm is not being updated; it was a 2024 experimental framework for linking stateless agents (under 100 lines on the chat completions API) and was deprecated in March 2025.** — Swarm lacked memory, tracing and guardrails, so it was never built for production. OpenAI pointed users to the Agents SDK as the upgrade path. ([0:00](https://youtu.be/oV3IjJSXQyM?t=0))
- **AgentKit (launched at DevDay, Oct 6, 2025) is presented as the production-grade successor, not Swarm reborn.** — Components named: Agent Builder (visual drag-and-drop chaining of planners, executors and retrievers), ChatKit (embed agents in apps), and a connector registry of 200+ integrations. ([1:17](https://youtu.be/oV3IjJSXQyM?t=77))
- **AgentKit's claimed safety and evaluation features are masking (likely PII masking), jailbreak detection, and built-in trace and scoring evals.** — The speaker contrasts these with Swarm's bare handoffs. No detail is given on how the evals or guardrails are configured. ([1:17](https://youtu.be/oV3IjJSXQyM?t=77))
- **Customer results are cited without sources: Klarna automating about two-thirds of support tickets and Ramp cutting iteration cycles by 70%.** — Treat as unverified vendor-adjacent claims. No links, dates or methodology are given. ([2:34](https://youtu.be/oV3IjJSXQyM?t=154))
- **The real technical caveat is cost and latency in multi-agent systems: traces grow with handoffs, sub-decisions, retries and planning steps, so latency blows up.** — This is the only operational point in the video. It is stated in one sentence with no measurements. ([3:45](https://youtu.be/oV3IjJSXQyM?t=225))
- **Vendor lock-in (AgentKit's defined design) versus open standards (MCP's open ecosystem) is the main ongoing developer debate.** — The speaker says the MCP ecosystem has 200+ open tools in six months but offers no comparison or evidence. The transcript misspells MCP as 'MPC'. ([3:45](https://youtu.be/oV3IjJSXQyM?t=225))
- **The video's broad conclusion is that 2025-2026 is an agent-tooling race and developers should start experimenting now.** — Claims such as 10x developer productivity and agent economies with no downtime are asserted, not supported. ([3:45](https://youtu.be/oV3IjJSXQyM?t=225))

## Techniques
- **Migrate off Swarm-style stateless handoffs to a framework with state and tracing** — The speaker's only concrete guidance is to move from Swarm to the Agents SDK or AgentKit, which add memory, tracing and guardrails that Swarm lacked. No steps, code or config are shown. *When:* When evaluating whether an old multi-agent prototype needs production features such as state, tracing or guardrails.
- **Budget multi-agent traces for latency and retries** — Count handoffs, sub-decisions, retries and planning steps per run, since these inflate trace size and latency. The video does not specify a measurement method. *When:* Before shipping any multi-agent workflow, to set latency budgets and catch retry loops.
- **Built-in trace-and-score evals for agent performance** — Attach evals to each agent run to trace and score its performance, as AgentKit claims to do. The video does not show the eval setup. *When:* When you need a repeatable quality signal for agent workflows; check the platform docs for the actual mechanism.

## Numbers
- Swarm is under 100 lines of code, built on the old chat completions API, and was deprecated in March 2025. ([0:00](https://youtu.be/oV3IjJSXQyM?t=0))
- AgentKit's connector registry lists over 200 plug-and-play integrations. ([1:17](https://youtu.be/oV3IjJSXQyM?t=77))
- o4-mini is claimed to be about 30% more token efficient, tested alongside the RFT beta (November). ([1:17](https://youtu.be/oV3IjJSXQyM?t=77))
- Klarna is said to automate about two-thirds of its support tickets (unsourced). ([2:34](https://youtu.be/oV3IjJSXQyM?t=154))
- Ramp cut iteration cycles by 70% (unsourced). ([2:34](https://youtu.be/oV3IjJSXQyM?t=154))
- A swarm-sampling approach is claimed to boost quant trading rewards by 94% (unsourced, attributed to 'Jensen' in the transcript). ([2:34](https://youtu.be/oV3IjJSXQyM?t=154))
- The MCP ecosystem has over 200 open tools within six months (unsourced). ([3:45](https://youtu.be/oV3IjJSXQyM?t=225))
- Meta's reported $70 billion CapEx is cited as evidence of agent-driven investment (unsourced). ([5:04](https://youtu.be/oV3IjJSXQyM?t=304))
- Agents are said to be on track to 10x developer productivity (unsourced). ([3:45](https://youtu.be/oV3IjJSXQyM?t=225))

## Hot takes
- AgentKit is the upgrade, and Swarm is not coming back.
- Multi-agent systems blow up latency through huge traces of handoffs, retries and planning steps.
- Agents will supercharge developers rather than replace them.
- Agents are on track to deliver 10x developer productivity (asserted without evidence).

## Tools mentioned
OpenAI Swarm (deprecated March 2025), OpenAI Agents SDK, OpenAI AgentKit (Agent Builder, ChatKit, connector registry), OpenAI Chat Completions API, RFT (reinforcement fine-tuning) beta, o4-mini (transcribed 'O4 Mini'), GPT-5 (multi-model stack, mentioned without detail), MCP (Model Context Protocol; transcribed 'MPC'), DeepSeek (transcribed 'DeepSeq'), Llama (transcribed 'Ulma 3')

## Relevance to our work
- **agentos** (1/3): The multi-agent trace-growth and latency point, and AgentKit's guardrail list (masking, jailbreak detection), touch the L1 scan and L4 observability ideas, but nothing is concrete. → *Add per-handoff spans and retry counters to the AgentOS trace plan before any multi-agent feature lands, and benchmark the latency impact.*
