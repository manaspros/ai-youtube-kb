# Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `gxVZ_1tuuq4` · [watch](https://youtu.be/gxVZ_1tuuq4) · **date:** 2026-09-18 · **length:** 20:46 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Mike Chambers · **orgs:** AWS, Amazon, Linux Foundation, Agentic AI Foundation, LangChain
- **topics:** agent-architecture, infra-cost-scaling, memory · **tags:** harness engineering, agent harness, AgentCore, Strands Agents, session manager, multi-tenant, infrastructure as code, managed harness, live demo, AWS

> AWS's Mike Chambers argues that an agent minus its model is the harness, and that agents built for many users should split the loop, memory, identity and tools into separately scaled parts, demoed on Bedrock AgentCore.

## Summary
Mike Chambers (AWS) separates two kinds of agents: the coding agents people use (Claude Code, Cursor, Kiro) and the agents teams build for others, and says the second kind needs more care. He defines a harness as everything in an agent except the model, covering memory, skills, tools/MCP and standards. For agents deployed to thousands of users, he argues each component (loop, memory, identity, runtime, context management) should scale on its own rather than sitting in one container. Observability and evals are named as the most important parts, but the talk barely covers how to do them. The bulk of the 20-minute session is a live demo of the Strands Agents SDK, a session manager that rehydrates history between invocations, and an AgentCore CLI that scaffolds, runs locally in a browser, and deploys agents via infrastructure as code. He ends by claiming a simple agent can be defined by a JSON config (model plus system prompt) and that many agentic use cases need little more than that, with AgentCore pieces usable on their own. The content is mostly a product walkthrough.

## Key ideas
- **Two separate kinds of agents: the ones you use (coding agents, productivity tools) and the ones you build for others. Each needs its own way of thinking.** — The speaker says the two chain together, since you might build an agent that others use. Building for an audience means designing for that audience, not for personal use. ([2:13](https://youtu.be/gxVZ_1tuuq4?t=133))
- **A harness is what is left of an agent once the model is removed.** — For a coding agent the harness holds memory, chosen skills, tools and MCP servers, and team standards. He suggests teams now need harness standards as well as coding standards. ([4:37](https://youtu.be/gxVZ_1tuuq4?t=277))
- **Agents built for scale need each part scaled on its own, not packed into one container.** — Loop, memory, identity, skills, tools, runtime and context management each have separate scaling needs. Observability and evals are called the most important, though he mentions them last. ([7:46](https://youtu.be/gxVZ_1tuuq4?t=466))
- **A session manager gives short-term and medium-term state between invocations.** — It rehydrates conversation history on the next call. A remember tool writes long-term facts to files. He admits it is not full long-term memory. In the demo, the agent answered a question using facts from earlier sessions. ([10:25](https://youtu.be/gxVZ_1tuuq4?t=625))
- **Avoid click ops and slop ops: have an agent write infrastructure as code rather than clicking in a console or asking an agent to create resources directly.** — He says the agent should build infrastructure as code so the team still owns its deployments. He presents an AWS agent toolkit for this, available free on GitHub. ([5:43](https://youtu.be/gxVZ_1tuuq4?t=343))
- **A managed harness can cover many agents with no custom code.** — The config is a small JSON file with a model and a system prompt, deployed with the CLI. He argues that a system prompt, a few tools and MCP connections cover around 80% of agentic use cases. He hedges the figure with 'maybe'. ([17:39](https://youtu.be/gxVZ_1tuuq4?t=1059))
- **Harness capabilities are composable and can be used one at a time.** — Memory, runtime, identity and other parts can be lifted out and added to a running production agent without moving the whole stack. ([18:54](https://youtu.be/gxVZ_1tuuq4?t=1134))

## Techniques
- **Split agent components for independent scaling** — Run the agent loop, memory, identity, tools and runtime as separate services that scale individually, with per-user isolation handled by the platform. *When:* When one agent must serve thousands of users and one container cannot scale to that load.
- **Session manager for cross-invocation state** — Store the conversation history and rehydrate it when the user returns, plus a remember tool that writes facts to files for later recall. *When:* When an agent must pick up a conversation from an earlier session without full long-term memory infrastructure.
- **Local dev loop that mirrors production** — Run the agent locally in a browser UI that updates live as code changes, then deploy the same code to the cloud with infrastructure as code and switch between local and deployed versions. *When:* When iterating on an agent before a production deploy, to shorten the feedback loop.
- **Declarative harness config** — Describe an agent as a JSON file with model and system prompt, deploy it without agent code, and add code only where the defaults fall short. *When:* For simple agents where the system prompt and a few tools are enough.
- **Agent-generated infrastructure as code** — Have a coding agent scaffold cloud resources as IaC instead of asking the agent to create resources directly or clicking in a console. *When:* When you want agents to help with cloud deployments but keep the deployment reviewable and owned by the team.

## Numbers
- An MCP Lambda handler he made in 2025 is downloaded about 35,000 times a month. ([1:24](https://youtu.be/gxVZ_1tuuq4?t=84))
- A three-week generative AI course with Andrew Ng is approaching half a million enrollments. ([0:16](https://youtu.be/gxVZ_1tuuq4?t=16))
- He estimates that maybe 80% of agentic use cases can be covered by a system prompt, some tools and MCP connections. This is an unmeasured guess. ([17:39](https://youtu.be/gxVZ_1tuuq4?t=1059))
- The demo agent runs on Sonnet 4.5 by default. ([14:08](https://youtu.be/gxVZ_1tuuq4?t=848))

## Hot takes
- Agents we use and agents we build are separate categories and should be designed differently.
- Avoid slop ops: agents should write infrastructure as code, not click in consoles or create cloud resources directly.
- Most agentic use cases may be solved by a system prompt plus tools and MCP, with no custom code.
- Observability and evals matter more than anything else for agents built for scale.

## Tools mentioned
Amazon Bedrock AgentCore, AgentCore CLI, Strands Agents SDK, Kiro, Claude Code, Cursor, MCP, AG-UI, AWS agent toolkit, Sonnet 4.5

## Relevance to our work
- **prosharness** (2/3): Its session-state rehydration and declarative harness config overlap with ProsHarness checkpoint/resume and the harness it wraps around Claude Code. → *Compare ProsHarness checkpoint/resume with the session-manager rehydration pattern. Try a declarative JSON harness config (model, system prompt, tools) to define ProsHarness runs.*
- **agentos** (1/3): The talk's split of loop, memory, identity and tools into separately scaled parts matches AgentOS's pillar layout, but it offers no benchmarks or failure data. → *Compare AgentOS's per-pillar layout with this talk's separately scaled components when reviewing how the proxy, memory and sandbox pillars scale apart.*
- **general** (1/3): Treating the harness (everything except the model) as the unit to version and scale is a reusable framing for any agent build. → *Read the Langchain and martinfowler harness-engineering articles the speaker cites for alternate definitions of a harness.*
