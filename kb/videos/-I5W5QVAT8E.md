# Notion's Token Town — Sarah Sachs, Notion

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-I5W5QVAT8E` · [watch](https://youtu.be/-I5W5QVAT8E) · **date:** 2026-08-18 · **length:** 23:55 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sarah Sachs · **orgs:** Notion, Parallel, Decagon, Vercel, Semi Analysis, Citadel
- **topics:** token-cost-efficiency, infra-cost-scaling, enterprise-adoption, security-guardrails · **tags:** token-cost, model-routing, model-agnostic, open-weight, trajectory-evals, lethal-trifecta, software-factory, cpu-over-gpu, governance, vendor-lock-in

> Notion's head of AI engineering on keeping AI costs sustainable: stay model-agnostic, route traffic by task difficulty, use open-weight and plain code for simple steps, and evaluate whole trajectories instead of single calls.

## Summary
Sarah Sachs, who leads AI engineering at Notion, argues that the main barrier to running agent systems at scale is token cost, and that companies should not tie themselves to one model vendor. She says buying tokens through resellers adds surcharges, and that a model upgrade can quietly raise cost through more output tokens or a new tokenizer. Her proposed fix is a model-agnostic harness with an auto-router that sends most traffic (she says about 75% at Notion) to cheaper models and reserves frontier models for hard tasks. She recommends judging models on cost per capability per second across whole task trajectories, using open-weight models for moderate tasks, and running deterministic steps as code or CLI calls instead of LLM calls. For the next phase, she names security (the lethal trifecta) and orchestration of multi-agent software factories as the hard problems, and she demos a Notion flow where an agent scopes a task into a shared doc, asks teammates questions, then hands off to Claude for a PR and Codex for review. Much of the talk is Notion positioning, and her numbers are mostly unsourced anecdotes.

## Key ideas
- **Token cost is a structural barrier, and buying from resellers is a bad deal** — A model vendor that builds its own product sells first-party tokens cheaply, while a reseller pays a surcharge and resells at another markup. Tying a product to one provider leaves no exit when prices or capability shift. ([5:18](https://youtu.be/-I5W5QVAT8E?t=318))
- **Model upgrades can raise cost without a visible price change** — She gives two examples: a reasoning model with the same per-token price that emits about 3x more output tokens, and a new model with a different tokenizer that uses about 40% more tokens for the same text. Auto-upgrading without measuring cost makes the customer or the vendor pay more. ([5:18](https://youtu.be/-I5W5QVAT8E?t=318))
- **Do not send all traffic to the most capable model** — Most tasks, such as triaging an inbox, do not need the top model. Price does not track capability, so the frontier is a narrow tier and most of the market sits in cheaper tiers. The product team should define what counts as frontier for its own work. ([9:09](https://youtu.be/-I5W5QVAT8E?t=549))
- **Optionality is the leverage, and lab discounts rarely justify losing it** — Her advice is to stay model-agnostic so the product can switch providers when pricing or quality changes. She sees heavy marketing around a single lab as a warning sign. Early access and eval data can be traded to labs in place of large spend commitments. ([11:36](https://youtu.be/-I5W5QVAT8E?t=696))
- **Evaluate whole trajectories, not single calls** — For web search, one provider may look worse on single-call latency or cost but better across a full search trajectory. Her team's evals measure the whole path so that routing decisions reflect end-to-end cost and quality. ([14:07](https://youtu.be/-I5W5QVAT8E?t=847))
- **Open-weight models set a cost floor and give negotiation leverage** — She says open-weight models, including reinforcement-learning-tuned ones, now handle moderate tasks that used to need frontier models. Judge them on your own tool errors and latency, not external benchmarks. Her claim is that the gap closes within about six months, so prepare now. ([15:35](https://youtu.be/-I5W5QVAT8E?t=935))
- **Deterministic steps should not use an LLM** — Converting a CSV to PDF, making Notion tool calls through a CLI, and running SQL queries are discrete code tasks. Her team launched a Workers product that runs such jobs on CPUs, which avoids token cost for them. ([16:37](https://youtu.be/-I5W5QVAT8E?t=997))
- **The next hard problem is security and orchestration, not capability** — A system with private data, exposure to untrusted content, and an external communication channel carries the lethal-trifecta risk, and the risk grows with autonomy. Her team also finds that orchestrating multi-agent factories is hard. Most engineering time goes into babysitting them. ([17:38](https://youtu.be/-I5W5QVAT8E?t=1058))
- **Active spec docs let agents ask for missing information from people** — In a demo, an agent scopes a task into a collaborative Notion document and asks questions. It tags a PM and a support agent (Decagon) for customer data, then hands the spec to Claude to open a PR, and Codex reviews the PR. ([20:06](https://youtu.be/-I5W5QVAT8E?t=1206))

## Techniques
- **Model-agnostic harness with an auto-router** — Keep several providers behind one harness with a default router that picks a model per request, and let users or customers override it. Build for multimodal inputs, and accept that switching models mid-thread costs cache, so switch at thread boundaries if needed. *When:* When a product must survive vendor price or quality changes and most traffic is routine (Notion says the auto model covers about 75%).
- **Traffic tiering by task difficulty** — Split work into three tiers. Frontier models for hard, high-value tasks. Mid-tier or open-weight models, optionally RL-tuned, for moderate tasks. Code or CPU jobs for deterministic steps. Define each tier from your own product's expertise. *When:* When a product's request mix is mostly routine and the cost per task matters.
- **Trajectory-level eval of cost, latency and success** — Measure a whole multi-call run (for example, one web search task from query to answer) on cost, latency and outcome, then compare models on that. Do not rank models on single-call numbers. *When:* When choosing a provider for a multi-step tool workflow, or when a cheaper model may need more calls to finish.
- **Open-weight evaluation on your own system** — Test open-weight models on your real tool-call error rate and latency requirements. Use this as evidence in vendor negotiations, not only as a cost play. *When:* Before committing to a vendor contract, or when a frontier model upgrade changes cost.
- **Code and CLI for deterministic steps** — Replace LLM calls with code when the step is fixed, such as file conversion, SQL queries, or tool calls that a CLI already exposes. *When:* When a workflow step has a known input-output mapping and no judgment is needed.
- **Cross-vendor review chain for agent PRs** — One coding agent writes a PR, a different vendor's agent reviews it, and humans route feedback to teams. Agents take the first pass on feedback before people do. *When:* When you run a software factory and want review from a different model family than the author.
- **Lethal trifecta check on agent systems** — Audit each system for three conditions together: access to private data, exposure to untrusted content (ingestion, MCP, email, web), and a way to send data outward. Treat having all three as a risk to mitigate. Autonomy makes it worse, so keep a human in the loop where it matters. *When:* Before giving an agent with private data a path to the web, email, or external APIs.

## Numbers
- Reasoning model upgrade: same per-token price but about 3x as many output tokens (speaker's example) ([5:18](https://youtu.be/-I5W5QVAT8E?t=318))
- New model with a different tokenizer uses about 40% more tokens than its predecessor, which is deprecated within four months (speaker's example) ([5:18](https://youtu.be/-I5W5QVAT8E?t=318))
- 88% of people have not got past AI as an assistant (speaker's figure, no source given) ([3:50](https://youtu.be/-I5W5QVAT8E?t=230))
- Auto model handles about 75% of Notion's traffic ([13:04](https://youtu.be/-I5W5QVAT8E?t=784))
- Customers save more than 3 minutes per task from the software factory flow (speaker's figure) ([21:48](https://youtu.be/-I5W5QVAT8E?t=1308))

## Hot takes
- Do not win the token economics game with resold tokens; win on product, data flywheels and understanding customers.
- Bet on the frontier, not on a single lab.
- Lab discounts are rarely worth the loss of optionality.
- Most products should not send everything to the most capable model; doing so is a disservice to customers.
- Open-weight models are no longer only good for small SFT tasks and will likely cover today's gaps in about six months.
- The challenge of the next six months is security, not capability.

## Tools mentioned
Claude Code, Claude, Codex, Decagon, Parallel (web search provider), Notion Workers, Notion AI Manage Agent, Kimi 2.6 (as transcribed), GLM 5.2 (as transcribed), GPT 5.2 (as transcribed)

## Relevance to our work
- **agentos** (2/3): AgentOS already has strategy routing and budgets at the L1 proxy. The talk's per-trajectory cost view and tiered routing map onto that layer. → *Add a benchmark to the routing strategy that measures cost and success per completed multi-call task, not per call, and compare a cheap open-weight tier against the frontier tier on it.*
- **prosharness** (1/3): ProsHarness already runs a Codex critique step. The lethal-trifecta check is a light fit for its phone-driven approvals and credential handling, but the talk adds little beyond that. → *Read the lethal-trifecta framing (private data, untrusted input, outbound channel) and check whether a ProsHarness run can hold all three at once without approval.*
