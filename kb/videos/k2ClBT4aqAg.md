# We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `k2ClBT4aqAg` · [watch](https://youtu.be/k2ClBT4aqAg) · **date:** 2026-10-09 · **length:** 17:26 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kamalakannan Nandagopal · **orgs:** Postman
- **topics:** context-engineering, coding-agents, evals · **tags:** API context graph, microservices, coding agents, grounding, eval design, token efficiency, staleness, impact analysis, API discovery, architecture review

> Postman's engineer describes an API context graph over 115+ microservices, grounded in code and telemetry, that improves coding-agent answers on API discovery, shape analysis and impact assessment, with a token-efficiency gain and a staleness warning.

## Summary
Kamalakannan Nandagopal (Postman) argues that coding agents struggle in distributed systems because the context they need is spread across many repos and services, and that API definitions are the natural context layer. Postman built an API context graph covering its 115+ microservices and thousands of endpoints, linking each endpoint to its implementing code line, service-to-service calls, data stores and client apps. A rule keeps every node grounded in either code or production telemetry. The team evaluated with eval cases mined from real PRs and design discussions, scored 0 to 5, and plotted quality against tokens, comparing Postman's agent, Claude Code with plain GitHub code search, and Claude Code with the graph exposed as a skill. The graph helped most on impact assessment and API shape analysis, where it used roughly half to a third of the baseline's tokens. A failure case showed that a stale graph (new consumers added after the eval was written) hurts results and erodes developer trust, so syncing and removals matter as much as initial population. Across the top 10 repos, about 75% of PRs touched API surface. Running the agent over the whole graph produced a 21-page architecture report covering dependency cycles, risky migrations, single points of failure and telemetry blind spots. The speaker says cheaper runs let teams move these checks earlier, to PR time and the local dev loop. The talk is a vendor-hosted case study with limited published numbers.

## Key ideas
- **Coding agents do well on greenfield work or single-repo fixes but struggle with production systems split across many microservices, repos, and environments.** — The speaker traces the path from autocomplete to refactors to autonomous agents, then says the real limit is cross-service context, not code generation. ([0:12](https://youtu.be/k2ClBT4aqAg?t=12))
- **Human-written docs and per-user agent memory both fall short for teams; the speaker says purely LLM-written docs degrade over time (citing research, not verified here).** — He says no standard exists yet for sharing agent memory across a team or org, and skills and MCPs are only as good as the context behind them. ([2:55](https://youtu.be/k2ClBT4aqAg?t=175))
- **In microservices, APIs define each service's responsibility, so they are the best context layer for agents.** — API calls between systems reveal workflows and user journeys that span several services, so the team built the graph around endpoints and their calls. ([4:23](https://youtu.be/k2ClBT4aqAg?t=263))
- **Every node in the graph must be grounded in a hard source: a code line or a production trace.** — This rule is the basis for trusting the graph; LLM-indexed summaries without a code or telemetry anchor were not accepted. ([5:34](https://youtu.be/k2ClBT4aqAg?t=334))
- **Evals were built from real merged PRs and design-review decisions, with the retrospective outcome as ground truth.** — Each case is scored 0 to 5 and tokens are recorded, then plotted as quality versus cost. The comparison includes a generic coding agent using plain code search, and the same agent with the graph exposed as a skill. ([6:44](https://youtu.be/k2ClBT4aqAg?t=404))
- **The graph helps most on impact and shape questions, where plain code search does poorly.** — For API shape analysis, a schema property that grew to 15 attributes was traced across consumers with the graph. For impact assessment, the agent reached similar quality with roughly half to a third of the tokens. ([9:25](https://youtu.be/k2ClBT4aqAg?t=565))
- **A stale graph causes visible failures, so keeping it in sync with ground truth is a core requirement.** — New consumers added after the eval was written produced a failure where the agent used many tokens and got the answer wrong. Removed APIs and dependencies matter as much as new ones. ([12:08](https://youtu.be/k2ClBT4aqAg?t=728))
- **Whole-ecosystem analysis is a payoff of the graph: a 21-page architecture review with actions per role.** — The report flagged dependency cycles, long migrations, single points of failure, and telemetry blind spots. It is one example that the speaker presents as a sign of the approach's value, not as a measured result. ([14:27](https://youtu.be/k2ClBT4aqAg?t=867))

## Techniques
- **Code- and telemetry-grounded API context graph** — Catalog each production service and every endpoint, link each endpoint to its implementing code line, map service-to-service calls and data-store access, and reject any node not backed by code or a trace. *When:* Multi-service systems where agents must answer cross-repo questions such as who calls this API and what breaks if it changes.
- **Retrospective PR-based eval with quality-vs-tokens plot** — Mine real PRs and design decisions for developer intent and actual outcome, use the outcome as ground truth, score each run 0 to 5, record tokens, and plot results with a pass line. *When:* Comparing agent setups (plain search, MCP, skill, context layer) on realistic engineering tasks rather than synthetic benchmarks.
- **Context layer exposed as a skill next to a generic coding agent** — Package the graph as a skill for a generic coding agent and run the same eval cases with and without it, so the context layer is the only variable. *When:* Testing whether a shared context source helps an existing coding agent without building a custom agent.
- **Treat graph staleness as an eval regression** — When an eval fails, check whether the ground truth changed after the eval was written (new consumers, removed APIs) before blaming the agent. *When:* Any context store that is populated once and then drifts from the codebase.
- **Run expensive architecture checks cheaper and earlier** — Reduce tokens per query with a graph so the same check can run per PR or in the local dev environment instead of only on demand. *When:* When cost per check limits how often a quality check can run.

## Numbers
- More than 115 microservices and thousands of REST endpoints power Postman's cloud features. ([0:12](https://youtu.be/k2ClBT4aqAg?t=12))
- Across the top 10 repos, about 75% of PRs had some effect on API surface or added an API integration. ([13:27](https://youtu.be/k2ClBT4aqAg?t=807))
- On impact assessment, the graph-equipped agent reached similar quality using roughly half to one third of the tokens of the code-search baseline (approximate, from the slide description). ([12:08](https://youtu.be/k2ClBT4aqAg?t=728))
- Evals are scored on a 0 to 5 scale and plotted against tokens per run; no absolute scores are stated. ([11:10](https://youtu.be/k2ClBT4aqAg?t=670))
- The whole-ecosystem architecture review produced a 21-page report. ([14:27](https://youtu.be/k2ClBT4aqAg?t=867))

## Hot takes
- Purely LLM-written documentation degrades over time, so human curation is needed.
- Agent memory is still limited to one individual user; no standard exists for sharing it across an engineering org.
- Every data point in an agent's context graph should trace back to a line of code or a production trace, not to an LLM summary.

## Tools mentioned
Postman API context graph, Claude Code, GitHub code search, Postman AI agent

## Relevance to our work
- **agentos** (1/3): SkillForge and MemoryMesh need provenance; the grounding rule is a useful design check, but the talk does not cover AgentOS-style infra. → *Read the grounding and staleness section (5:34 and 12:08) before deciding how MemoryMesh provenance should trace each fact to its source.*
- **prosharness** (1/3): The quality-vs-tokens scatter with a pass line is a simple way to compare harness setups on cost and quality. → *Adopt the quality-versus-tokens plot for comparing ProsHarness plan-critique-debate runs, using PR-derived ground truth.*
- **general** (1/3): The retrospective PR-based eval design and the note that stale context causes failures apply to any agent evaluation. → *Build eval cases from real merged PRs with outcomes as ground truth, and log whether context was current at the time each eval ran.*
