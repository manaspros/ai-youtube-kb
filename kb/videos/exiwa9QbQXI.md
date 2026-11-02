# The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `exiwa9QbQXI` · [watch](https://youtu.be/exiwa9QbQXI) · **date:** 2026-10-08 · **length:** 18:32 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Davis Palmie · **orgs:** Factory, Lumetric, Slalom, Y Combinator, Uber, Microsoft
- **topics:** software-factory, governance-compliance, context-engineering · **tags:** software factory, agent readiness, autonomous agents, incident triage, model routing, agent governance, outcome metrics, vendor pitch, DORA

> Factory's Davis Palmie argues engineers should build a "software factory" of agents that turns signals like bug reports into production code, starting narrow, measuring outcomes, and staying model- and surface-agnostic.

## Summary
Davis Palmie, a member of technical staff at Factory, frames AI coding as moving through three eras: autocomplete, whole-file generation, and tool-using agents, with engineers now governing agents rather than typing code. He describes a "software factory" as a system of agents that takes input signals (bug reports, Sentry alerts, user feedback) to production deployment across support, planning, testing, review, rollout and monitoring. He argues coding was never the real bottleneck; review time, bug reproduction, doc drift and cross-team context dominate lead time. His advice is to start with one narrow, verifiable pillar such as incident triage, keep humans reviewing, and only close the loop once outputs can be tied back to input signals. He proposes three principles (model-agnostic, sovereign deployment, integrated across the SDLC) plus surface-agnostic agents sharing one harness. He offers an eight-pillar "agent readiness" checklist and recommends measuring outcomes (signal-to-production time, human intervention count, median time to repair, code shelf life, cost per PR) rather than token counts. Much of the talk is a vendor pitch for Factory, and concrete data is thin.

## Key ideas
- **Three eras of AI coding and the engineer's role shift** — Progression went from tab autocomplete, to whole-file generation, to agents that gather context, call tools and debug their own output. Engineers move from typing code to governing agents, which are then organised into a system (the software factory). ([0:08](https://youtu.be/exiwa9QbQXI?t=8))
- **Coding is not the bottleneck** — Median PR review time, bug reproduction, doc currency and test upkeep take far longer than writing code. Lead time from code written to production is said to dwarf the coding time. Teams are siloed, and agents suffer more from that siloing than humans do. ([4:42](https://youtu.be/exiwa9QbQXI?t=282))
- **Start narrow and verifiable, then loop** — Begin with something like incident triage: the agent reads a Sentry alert, pulls traces and posts a diagnosis in Slack for an engineer to review. Trust grows as correct diagnoses accumulate. Only after outputs can be tied back to input signals should the pipeline be allowed to loop, which is where organisational self-improvement starts. ([7:11](https://youtu.be/exiwa9QbQXI?t=431))
- **Three principles: model-agnostic, sovereign, integrated** — Pick the model per task for cost and performance rather than locking to one lab. Deployment should range from fully managed to bring-your-own machine to air-gapped. Docs, code, planning and testing should be linked, since a weakness in one pillar weakens the whole factory. ([7:11](https://youtu.be/exiwa9QbQXI?t=431))
- **Surface-agnostic agents with one shared harness and context** — The same agents should run from remote machines, the CLI or Slack, so teams keep their own tools. Humans and agents may use different surfaces but should share the same harness and context. ([12:41](https://youtu.be/exiwa9QbQXI?t=761))
- **Agent readiness is a precursor to effective engineering** — Eight pillars are assessed: validation (linters and formatters), documented CI build commands, feedback loops (unit and integration tests), docs such as READMEs and AGENTS.md, reproducible dev environments, modular code with clear boundaries, observability, and proactive security scanning. Paving these roads helps humans and agents alike. ([13:45](https://youtu.be/exiwa9QbQXI?t=825))
- **Govern once, auditable actions, roll out incrementally** — Guardrails, agents, docs and test policies are defined once and applied across the org, so the standard rises to the highest bar. Actions should be auditable under RBAC and least privilege, and automation should be rolled out pillar by pillar before it becomes a loop. Humans stay in the loop for architecture and strategy. ([14:48](https://youtu.be/exiwa9QbQXI?t=888))
- **Measure outcomes, not tokens (Goodhart's law)** — Token and lines-of-code metrics are gameable, and token leaderboards encourage wasteful spend. Suggested outcome metrics are signal-to-production time, human intervention count, median time to repair, shelf life of code, and cost per PR. ([15:51](https://youtu.be/exiwa9QbQXI?t=951))

## Techniques
- **Narrow-first, verifiable agent pillar** — Automate one pillar end to end, such as an agent that reads a Sentry alert, pulls traces and drafts a Slack diagnosis, while an engineer reviews every output. Track correct versus incorrect diagnoses before widening scope. *When:* When introducing agents into an incident or ops workflow, and the team has not yet built trust in the system.
- **Close the loop only after tying outputs to input signals** — Make sure each agent output can be traced back to the signal that caused it (for example, a bug report or alert). Only then let the pipeline act without a human gate, and use that traceability for self-improvement. *When:* Before turning a human-reviewed agent pipeline into an autonomous loop.
- **Agent readiness checklist (eight pillars)** — Score a repo on validation (linters, formatters), CI build docs, test feedback loops, agent-facing docs (README, AGENTS.md), reproducible dev environments, modular boundaries, observability, and security scanning. Fix the gaps before deploying coding agents. *When:* Before pointing coding agents at a codebase, or when onboarding a repo into an agent workflow.
- **Per-task model routing for cost versus quality** — Route each task to the cheapest model that reaches the required quality (for example, code review on a cheaper frontier model, or open-source models where they are good enough). Do not lock the workflow to one provider. *When:* When agent costs grow and tasks vary in difficulty.
- **Single harness and context shared across surfaces** — Run the same agent harness and context whether the work starts from the CLI, Slack or a remote machine, so teams do not have to change their own tools to use the agents. *When:* When several teams use different tools and need consistent agent behaviour.
- **Outcome-based agent metrics** — Track signal-to-production time, human intervention count, median time to repair, code shelf life and cost per PR, instead of tokens spent or lines generated. *When:* When reporting on or budgeting for agent-driven development.

## Numbers
- Code review achieves the same performance with GPT 5.2 as with the latest Opus models, at half the price (speaker's internal finding). ([7:11](https://youtu.be/exiwa9QbQXI?t=431))
- Open-source alternatives are said to be 10 to 30 times cheaper. ([8:39](https://youtu.be/exiwa9QbQXI?t=519))
- Agent readiness is assessed across eight pillars. ([13:45](https://youtu.be/exiwa9QbQXI?t=825))
- Managing N teams is said to drop from O(N) to O(1) with a shared factory, conservatively. ([10:41](https://youtu.be/exiwa9QbQXI?t=641))

## Hot takes
- Coding was never the bottleneck; review, debugging, docs and cross-team context are the real lead-time costs.
- Token and lines-of-code leaderboards are Goodhart's law in practice and encourage wasteful spend.
- Engineers will not be replaced, but judgment and prioritisation now beat mechanical implementation skill.
- Engineers will end up building and maintaining the system that builds production code, which blurs product and engineering.
- Agents need the same governance as engineers (tooling, access levels, review), and should not be turned loose in the codebase.

## Tools mentioned
Sentry, Slack, AGENTS.md, Factory

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs loops and schedules around Claude Code, and it has checkpoint/resume and phone approvals. The talk's narrow-first rollout, auditable actions and the rule to close the loop only after outputs are traceable to input signals apply directly. → *Gate any ProsHarness autonomous loop behind a narrow first use (for example, a single incident-triage or bug-triage job with human approval), and require each run record to link its output back to the triggering signal before the loop is allowed to run unattended.*
- **agentos** (1/3): AgentOS already has budgets and strategy routing (L1). The talk's outcome metrics (cost per PR, median time to repair, human intervention count) and per-task model choice are a useful lens for its observability and governance pillars, but the talk gives no technical design details. → *Add an outcome dashboard in L4 (Prometheus/Grafana) with cost per task and median time to repair alongside token metrics, to test whether the budget pillar optimises for outcomes or just spend.*
