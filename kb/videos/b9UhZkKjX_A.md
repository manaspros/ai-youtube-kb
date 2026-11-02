# From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `b9UhZkKjX_A` · [watch](https://youtu.be/b9UhZkKjX_A) · **date:** 2026-10-11 · **length:** 19:39 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Jose Palafox · **orgs:** GitHub, GitHub Next, Microsoft
- **topics:** coding-agents, software-factory, observability, multi-agent · **tags:** github-copilot, copilot-cli, agentic-workflows, github-actions, agent-marketplace, cross-repo, otel, cost-optimization, headless-agents, human-in-the-loop

> GitHub's Jose Palafox walks through the Copilot agent surfaces: local agents you steer, reusable shared agents, cross-repo orchestration, and headless agents in CI that get cost and trace visibility through OTel.

## Summary
The speaker, a GitHub field-facing security and AI person, splits agents into two modes: local agents driven from an IDE or CLI, and autonomous pipeline agents that run off the laptop. Every interface (IDE, CLI, SDK, GitHub.com delegation, mobile remote) goes through one Copilot API harness that handles chunking, model routing, auth, metrics and audit logging. The CLI ships embedded agents such as a Haiku-backed Explorer for codebase reading and a Rubber Duck agent that audits a plan with a different model family. Custom agents can be scaffolded from a one-line description through an agent builder, scoped to project or user level. Sharing is handled by a marketplace (a repo with a JSON marker that gives versioning and vulnerability notices) or a .github-private repo, and the speaker argues reuse raises cache-hit rates and so lowers cost. Orchestrate fans a set of GitHub issues out to sub-agents that each run inside their target repo, so permissions stay with that repo. Headless Copilot CLI runs (-p) in GitHub Actions cover scheduled maintenance, with human approval as issue-comment slash commands between phases. The speaker says GitHub's own agentic-workflows framework has about 200 agents and its team develops from a phone, and argues that moving agents into CI is what makes per-agent OTel cost and tool-call metrics visible enough to optimise.

## Key ideas
- **Two modes of agent use** — Local agents you drive interactively, and autonomous pipeline agents that run in CI without you, so work survives a closed laptop or lost network. ([0:12](https://youtu.be/b9UhZkKjX_A?t=12))
- **One harness behind every surface** — IDE, CLI, SDK and GitHub.com delegation all route into a single Copilot API layer that does chunking, model routing, auth, metrics and audit logging, then filters output on the way back. ([2:02](https://youtu.be/b9UhZkKjX_A?t=122))
- **Small-model subagents and cross-model audit** — Built-in agents set their own model. A cheap Haiku-based explorer reads codebases, and a second-provider agent audits a plan written by another model because the training data and weights differ. ([4:08](https://youtu.be/b9UhZkKjX_A?t=248))
- **Scaffold agents from a one-line prompt** — An agent builder generates front matter, description, success criteria and a method from a rough description, at project or user scope. You then edit the result. ([5:32](https://youtu.be/b9UhZkKjX_A?t=332))
- **Share agents through a marketplace or a private repo** — A marketplace is a repo with a JSON marker that adds versioning, bulk updates and security notices to downstream users. An org can also expose agents from a .github-private repo. ([8:06](https://youtu.be/b9UhZkKjX_A?t=486))
- **Reuse agents to raise cache hits and lower cost** — The speaker argues cheapest usage comes from exact matches between turns on common data, so standard shared agents that people call the same way drive down the bill. ([9:20](https://youtu.be/b9UhZkKjX_A?t=560))
- **Cross-repo work by spawning agents inside each repo** — Orchestrate takes a set of GitHub issues as goals and starts a sub-agent in each target repo, since an agent started in one repo often lacks permission in another. ([10:41](https://youtu.be/b9UhZkKjX_A?t=641))
- **Headless CLI in CI with human gates** — copilot -p runs a one-shot prompt inside GitHub Actions on a cron or repo event, using the repo's budget and identity. Developers advance each phase by typing a slash command on an issue. ([11:48](https://youtu.be/b9UhZkKjX_A?t=708))
- **Move agents into CI to make cost visible** — Instrumenting every pipeline agent with OTel lets you pivot token use by agent and repo, alert when a run exceeds its P90 cost, and A/B test front matter or models for cheaper output. ([17:39](https://youtu.be/b9UhZkKjX_A?t=1059))

## Techniques
- **Headless one-shot agent in CI** — Call the Copilot CLI with -p and a single prompt inside a GitHub Actions job triggered by cron or repo events, so the agent runs on the repo's budget and identity. *When:* Recurring maintenance such as doc refresh, context-file updates, or periodic code scans.
- **Slash-command phase gates on issues** — A cron agent opens issues with proposed items. A developer comments a slash command to advance an issue, which triggers the next agent (PRD/plan, then implementation), and a final human acceptance review. *When:* Pipelines where spending on the next phase needs a human decision.
- **Scaffold agents from a one-line description** — Use the built-in agent builder to generate front matter, description, success criteria and method from a short prompt, then edit the source order or sources by hand. *When:* Creating repeat-task agents quickly without writing agent files from scratch.
- **Marketplace or private-repo distribution** — Keep agent files in one repo with a marketplace JSON marker, or in an org .github-private repo, so clients sync and get updates and vulnerability notices. *When:* Several teams need the same agents and nobody owns a central catalog yet.
- **Orchestrate: issues as goals, agents per repo** — Write one GitHub issue per cross-repo task. The orchestrator spawns a sub-agent in each target repo so each runs with that repo's permissions. *When:* A change in one service, such as an API change, has to be carried into downstream repos.
- **Cross-model plan audit** — Write the plan with one model, then pass the document to an agent backed by a different model provider to validate it before implementation. *When:* Before implementing a plan, to catch errors one model family might miss.
- **Small-model codebase explorer** — Route read-only codebase investigation to a small model subagent instead of the largest model. *When:* Exploration tasks where cost matters more than maximum reasoning.
- **OTel per-agent cost monitoring** — Instrument each agent run with OpenTelemetry, then chart token use per agent and repo, flag runs above the P90 cost, and inspect failing tool calls or verbose runs. *When:* Many agents run in CI and you need to find cost or reliability outliers.

## Numbers
- The agentic-workflows framework repo contains about 200 agents, all running parts of a pipeline and built by agents (speaker's rough count: 'I don't know. 200'). ([15:03](https://youtu.be/b9UhZkKjX_A?t=903))
- GitHub Next's Agentix project has about 30 pipeline agents for code deduplication, review, QA and similar tasks. ([16:15](https://youtu.be/b9UhZkKjX_A?t=975))
- In the example cron agent, the first stage flags three improvement items for the developer to approve. ([13:52](https://youtu.be/b9UhZkKjX_A?t=832))

## Hot takes
- Cost optimisation depends on being able to see agent behaviour, and agents running in CI are what make that visibility possible.
- Reusable, standardised agents are the cheapest way to use a coding agent, because cache hits come from identical prompts across people.
- GitHub's own agentic-workflows team builds its project only from a phone, using slash commands on issues.

## Tools mentioned
GitHub Copilot CLI, GitHub Copilot SDK, GitHub Actions, GitHub Agentic Workflows, Awesome Copilot, OpenTelemetry, Slack, Microsoft Teams

## Relevance to our work
- **prosharness** (2/3): The headless one-shot CLI in CI with issue-comment slash-command gates is a concrete pattern for scheduled runs with phone-style approvals, close to ProsHarness's loops/schedules and phone-driven approvals. The speaker's approach to gating spend between phases is useful for checkpoint and resume design. → *Compare ProsHarness's phone-driven approval flow with the issue-comment gate (a human command advances the next phase) and decide whether ProsHarness should model phase advance as an explicit, resumable approval step.*
- **agentos** (1/3): The per-agent OTel cost monitoring with P90 alerting and A/B tests on models and front matter is a small addition to the L4 observability stack (Prometheus/Grafana, OTel). It is a method, not a new component. → *Consider a P90 cost-per-agent-run alert in the L4 Prometheus/Grafana stack, with a link from each alert to the run's trace.*
