# What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `vGCJ7diEtrw` · [watch](https://youtu.be/vGCJ7diEtrw) · **date:** 2026-10-04 · **length:** 22:49 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Tereza Tížková · **orgs:** Factory, EY, Adobe, Coinbase
- **topics:** software-factory, infra-cost-scaling, testing-verification, context-engineering · **tags:** software factory, autonomous agents, missions, orchestrator, validators, validation contract, model routing, prompt caching, verifiable done criteria, deferred tool loading, agent readiness, codebase hygiene, auto-wiki, plugins, long-running agents

> Factory's engineer defines a "software factory" as a full autonomous lifecycle, not coding agents. Covers model routing for cost, verifiable done-criteria, sequential worker and validator missions, deferred tool loading, and codebase readiness.

## Summary
The speaker, from the vendor Factory, argues that a software factory is the whole autonomous loop (signals, prioritisation, orchestration, execution, validation, production testing, iteration), not just code generation. She names three principles: stay agnostic to models and tools, run autonomously for long periods, and keep improving the codebase and the agents' knowledge. On cost, she describes automatic model routing that classifies task difficulty and picks the cheapest model above a threshold, with escalation on failure, and says caching is a pricing choice rather than a technical limit. On autonomy, she says the hard part of loops is writing verifiable done-criteria, and that her team's "missions" use an orchestrator that writes a validation contract, sequential workers, and validators that judge code they did not write, including a validator that drives the running app in a VM. For context, she describes deferred tool loading, where only short tool descriptions are exposed until a full schema is needed, and a readiness checklist for codebase hygiene. Many claims are product-specific and lack shown data, so the talk is best read as a practitioner's description of one vendor's design.

## Key ideas
- **A software factory is the whole autonomous loop, not code generation** — She defines it as collecting signals and user feedback, prioritising, orchestrating, executing, validating, testing in production and iterating. She says writing code is the easy part and that engineers spend little time on it. ([1:34](https://youtu.be/vGCJ7diEtrw?t=94))
- **Three principles: be agnostic, be autonomous, always improve** — Agnostic means independent of LLM choice and of how the org already works (Slack, GitHub, existing subscriptions). Autonomous means giving agents permissions, governance and trust to run for long periods. Always improving means documenting the codebase so agents, like new hires, can learn and share knowledge. ([4:13](https://youtu.be/vGCJ7diEtrw?t=253))
- **Model routing can cut spend without cutting usage** — She describes a Coinbase CEO chart where token use kept rising but spend flattened. Levers were per-role default models, caching, spend visibility, and routing. The speaker says routing can also help speed and reliability, for example by switching providers when one fails. ([5:39](https://youtu.be/vGCJ7diEtrw?t=339))
- **Routing = classify difficulty, then pick the cheapest model over a threshold** — The router reads the prompt structure, codebase, and tools to estimate task difficulty. It picks the cheapest model predicted to succeed, and escalates to a stronger model if the task fails. She says the hard part is classifying well and avoiding frequent switches. ([8:14](https://youtu.be/vGCJ7diEtrw?t=494))
- **Caching is a pricing decision, not a technical barrier** — Anyone can cache. Open models on dedicated compute can get the same benefit. What the user pays is a business choice and depends on deals with API providers. ([9:39](https://youtu.be/vGCJ7diEtrw?t=579))
- **The hard part of a loop is defining verifiable done** — Coding loops had clear pass/fail criteria. Open-world tasks (such as 3D printing a logo) do not, so the criteria must be checkable. Without them, agents can game the tests and pass without solving the real problem. ([10:38](https://youtu.be/vGCJ7diEtrw?t=638))
- **Missions: orchestrator writes done-criteria, workers run in sequence, validators judge** — A long-running mission has an orchestrator that writes a validation contract before any code exists. Workers run one after another so each gets a fresh context, and each may spawn parallel subagents. Validators review code they did not write and send feedback back. In one 16-hour customer mission, validation took about 40% of the process. ([11:59](https://youtu.be/vGCJ7diEtrw?t=719))
- **Two kinds of validator: static checks and a clicking user-test agent** — The scrutiny validator runs linters, type checks and tests. The user-testing validator runs in its own VM, clicks through the product, and checks it works. She says this caught dummy UIs that looked fine in code. ([14:25](https://youtu.be/vGCJ7diEtrw?t=865))
- **Deferred context: expose short tool lists and load full schemas on demand** — Enterprises can have hundreds of tools, and their schemas can bloat context or confuse the agent. The deferred context engine lists only short descriptions, and loads a tool's full schema when it is actually needed. Nothing is removed. The claimed saving is about 50% of tokens or more at scale. ([15:51](https://youtu.be/vGCJ7diEtrw?t=951))
- **AI amplifies both good and bad codebases, so check readiness first** — She says adopting AI on an unstructured codebase can make the code worse, and that the productivity gap between early adopters and careful adopters is growing. Her readiness framework checks reproducible dev environments, tests, documentation, style and linters, and gives follow-up actions. ([17:14](https://youtu.be/vGCJ7diEtrw?t=1034))
- **Codify tacit team rules as plugins and auto-generated docs** — Repeating preferences to agents is a sign that rules live only in people's heads. Her team packages reusable skills and context as plugins, and uses an auto-wiki that updates documentation automatically. ([19:53](https://youtu.be/vGCJ7diEtrw?t=1193))

## Techniques
- **Difficulty-classified model routing** — Assign each task to a role-default model, classify its difficulty from prompt structure, codebase and tool use, set a threshold, pick the cheapest model above it, and escalate on failure. Track cost, speed and failure rate. *When:* When token spend grows faster than value and many tasks are easy enough for cheaper models.
- **Validation contract written before coding** — The orchestrator writes explicit pass/fail conditions for the mission before any worker starts. Validators check the output against that contract. *When:* For long-running, open-ended agent tasks where done must be verifiable and not self-declared.
- **Sequential workers with fresh context per handoff** — Each worker finishes its piece and passes the result to the next agent in a chain. Workers may spawn parallel subagents for research or file-building subtasks. *When:* For long missions where accumulated context degrades quality. She says fresh heads help, like a colleague reviewing code.
- **Two-tier validation** — Run a static validator (linters, types, tests) and a user-testing validator that drives the running app in a VM and clicks through it. *When:* When tests pass but the product may still be a non-working UI, or when the output needs interaction-level checks.
- **Deferred tool loading** — Show only short tool names and descriptions up front. Load the full schema when the agent calls or needs that tool. Keep all tools reachable. *When:* When many tools (for example many MCP servers) bloat context or cause the wrong tool to be picked.
- **Codebase readiness audit** — Check the repo for reproducible dev setup, tests, docs, style rules and linters, and act on the gaps before expanding agent use. *When:* Before rolling out coding agents to a codebase that is poorly documented or inconsistent.
- **Codify tacit rules as skills or plugins** — Capture repeated instructions as packaged skills and context, and generate docs automatically so new agents inherit team conventions. *When:* When you keep correcting agents on the same team preferences.

## Numbers
- Routing can save about 25% on AI spend in a conservative benchmark. She says the real figure is probably higher. ([7:00](https://youtu.be/vGCJ7diEtrw?t=420))
- Coinbase CEO chart: token usage kept growing while cost was flattened. No figures are given. ([5:39](https://youtu.be/vGCJ7diEtrw?t=339))
- A customer mission ran for 16 hours. Missions can run for weeks. ([11:59](https://youtu.be/vGCJ7diEtrw?t=719))
- Validation takes about 40% of the whole mission process. ([11:59](https://youtu.be/vGCJ7diEtrw?t=719))
- Deferred tool loading saves about 50% of tokens or more at scale, per the speaker. ([15:51](https://youtu.be/vGCJ7diEtrw?t=951))
- Agent runs of a year or more without a human in the loop are predicted. She calls this ambitious but says her team's missions already run for weeks. ([4:13](https://youtu.be/vGCJ7diEtrw?t=253))

## Hot takes
- A software factory is not a coding agent or a swarm of thousands of them; the code-writing step is the easy part.
- You cannot buy a software factory from a consultancy. Rebuild the organisation from the ground up.
- Caching is a pricing choice, not a technical problem.
- AI adoption follows a power law: it can make a messy codebase much worse.
- Humans should decide what to build, and agents should decide how to build it.

## Tools mentioned
Factory (software factory platform), Factory missions (orchestrator, worker and validator agents), Automatic model routing, Deferred context engine, Agent readiness framework, Plugins, Auto-wiki, Slack, GitHub, Figma, Notion, Gmail, Google Drive

## Relevance to our work
- **agentos** (2/3): Model routing (difficulty classification, cheapest-model threshold, escalation on failure) maps onto AgentOS L1 strategy routing and L2B cost and scheduling work, but the talk gives no measured data. → *Prototype a difficulty-classified routing strategy in the L1 proxy and compare its cost and failure rate against the current strategy on a fixed prompt set.*
- **prosharness** (2/3): A validation contract written before execution, plus a separate validator that runs the app, fits ProsHarness's plan, critique and checkpoint flow. → *Add a validation contract step to the plan phase that is written before the first Claude Code run, and add a run-the-app validator as a separate check.*
- **general** (1/3): Deferred tool loading is a context-engineering pattern for large tool sets. Useful background, but no measured figures were given. → *Read the deferred-context idea against the current Claude Code tool-loading behaviour before using it in a harness.*
