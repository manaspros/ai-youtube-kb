# The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `L173Z8DpaJg` · [watch](https://youtu.be/L173Z8DpaJg) · **date:** 2026-09-18 · **length:** 20:51 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Safia Abdalla · **orgs:** Warp, Microsoft, Project Jupyter
- **topics:** software-factory, pr-code-review, multi-agent, sandboxing-execution · **tags:** warp, oz, cloud-agents, sandboxes, self-hosted, multi-harness, orchestration, agent-gated-review, issue-triage, open-source, api-first, software-factory-critique

> Safia Abdalla (Warp) on building the Oz cloud agent platform: hide infra complexity, allow any harness, expose everything via API, and run the open-source repo with agent-gated triage and PR review.

## Summary
Safia Abdalla of Warp explains why and how the team built Oz, its cloud agent platform. The core principle is that the platform should absorb infrastructure complexity so users never see it, which leads to managed and self-hosted sandboxes, a harness-agnostic layer with shared guardrails, and an API covering agents, sub-agents, environments and artifacts. She describes multi-agent work where research, implementation and validation run as separate agents, possibly on different harnesses and models, coordinated by an orchestrator. The most concrete part is Warp's open-source repo, where agents triage new issues, draft specs, and review every PR through several iterations before any human reviewer is pinged. She argues that "software factory" is the wrong name and prefers a workshop framing that keeps people in the loop, with observability, event-driven automations and cost control as requirements. The talk has little hard data or implementation detail, and it closes with a booth pitch.

## Key ideas
- **Platforms should absorb infrastructure complexity before it reaches the user.** — The speaker's guiding rule is that a good experience should not expose the messy infrastructure underneath. Every primitive in Oz is modeled to hide that complexity, so the user only sees the work. ([1:20](https://youtu.be/L173Z8DpaJg?t=80))
- **Cloud agents need both managed and self-hosted sandboxes.** — Managed sandboxes are an easy on-ramp, but serious teams have their own infra and security rules. So agent workloads must also run on infrastructure the customer brings. ([3:38](https://youtu.be/L173Z8DpaJg?t=218))
- **Support many harnesses, but enforce one platform structure around them.** — Users bring Claude Code, Codex, or their own harness. Without structure, the experience fragments, so the platform standardizes conversation state, rehydration, and outputs such as PRs, issues and files for every harness. ([5:40](https://youtu.be/L173Z8DpaJg?t=340))
- **Split real engineering work across specialised agents.** — One agent researches and plans, another implements, and a third validates. Each can use a different harness or model to get an adversarial check. An orchestrator agent handles delegation, messages between sub-agents, and tracking. ([6:44](https://youtu.be/L173Z8DpaJg?t=404))
- **Expose every component through an API so others can build on it.** — Agents, sub-agents, environments and artifacts are all reachable by API. Non-engineering staff at Warp used the SDK to build Slack bots for social-mention triage and product Q&A. ([8:01](https://youtu.be/L173Z8DpaJg?t=481))
- **Agents triage issues and gate PRs in the open-source repo.** — After open-sourcing, an agent triages each new issue by researching the codebase and asking clarifying questions, and drafts specs. Every PR passes an agent review over several iterations, and humans are pinged only after the agent approves. ([12:10](https://youtu.be/L173Z8DpaJg?t=730))
- **Structure lets non-developers ship software by turning intent into implementation.** — Domain experts who are not developers can bring ideas through the agent-run intake process. The speaker argues that most software is built by developers for people who lack domain expertise, so this structure matters. ([13:13](https://youtu.be/L173Z8DpaJg?t=793))
- **The speaker prefers a workshop framing to the term software factory.** — She uses a potter's workshop as the model: repeatable process, verification at each step, staff who watch and refine the process, and a loop with the people in it. A system should be observable, react to events, improve over time, and stay cheap in tokens. ([17:59](https://youtu.be/L173Z8DpaJg?t=1079))

## Techniques
- **Managed plus self-hosted sandboxes behind one model** — Run each agent in an isolated cloud sandbox. Offer a managed option for ease, and let teams plug in their own infrastructure, with the same abstraction for both. *When:* Teams with their own security, deployment, or internal-service constraints that rule out fully managed compute.
- **Harness-agnostic layer with platform guardrails** — Let any agent harness run, but route conversation state, rehydration, and all outputs (PRs, issues, generated files) through common platform structures so the experience stays consistent. *When:* You support several coding agents and want one review, storage, and artifact flow regardless of which one runs.
- **Orchestrator with mixed-model sub-agents** — A parent agent, triggered by a prompt or an API call, delegates to sub-agents for research/plan, implement, and validate. It mediates their messages and tracks progress. Each sub-agent can use a different harness or model. *When:* Non-trivial tasks where a single prompt does not fit, and you want adversarial checking between roles.
- **Agent-gated PR review before human review** — Every PR goes through repeated agent review rounds. Humans are notified only after the agent approves, so reviewers see only the higher-signal PRs. *When:* High PR volume on a repo where human reviewer time is the bottleneck.
- **Agent-driven issue intake** — On a new issue, an agent searches the codebase, asks the reporter follow-up questions if the request is vague, and drafts a spec or task before any implementation. *When:* Open-source or cross-functional repos where bug reports and feature requests arrive underspecified.
- **API-first primitives for agents, sub-agents, environments and artifacts** — Expose each part of the stack through an API and SDK, so teams outside engineering can build their own bots and workflows on top. *When:* A platform that must support custom internal tooling without a custom UI for each use case.

## Numbers
- GitHub stars on the Warp repo rose from about 20,000 to over 60,000 after the open-source release. ([10:47](https://youtu.be/L173Z8DpaJg?t=647))
- The open-source release brought thousands of PRs and hundreds of contributors. ([10:47](https://youtu.be/L173Z8DpaJg?t=647))
- Warp open-sourced the repo about three months before this talk. ([9:25](https://youtu.be/L173Z8DpaJg?t=565))

## Hot takes
- 'Software factory' is a poor term because it leaves the people out. A workshop, where humans watch and refine the process, is a better model.
- Platforms should absorb infrastructure complexity so users never see it.
- Most software is written by developers for people with domain expertise, so agent intake that lets non-developers express intent matters more than faster coding.

## Tools mentioned
Warp, Oz, Claude Code, Codex, GitHub, Slack

## Relevance to our work
- **prosharness** (2/3): Multi-agent research, implementation and validation with different harnesses and models, plus an agent review gate before humans, closely match ProsHarness's plan, critique and debate loop. → *Read the orchestration and review-gate sections of this talk against the plan, critique and debate loop, and consider a stage where an agent must approve a plan or PR before the human is pinged.*
- **agentos** (1/3): Its sandbox point (managed plus bring-your-own infra behind one abstraction) is relevant to Crucible's celld and Cloudflare backends, though the talk gives no implementation detail. → *When designing the Crucible backend choice, support a self-hosted sandbox target alongside managed ones behind one interface, as the speaker argues teams need.*
- **general** (1/3): Agent-driven issue triage and PR gating are a concrete, real-world case from a large open-source repo. → *Look at the Warp open-source repo's triage and review setup as a reference for an agent-gated intake and review workflow.*
