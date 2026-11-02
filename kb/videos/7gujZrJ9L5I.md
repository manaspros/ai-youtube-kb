# How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7gujZrJ9L5I` · [watch](https://youtu.be/7gujZrJ9L5I) · **date:** 2026-06-18 · **length:** 25:13 · **format:** panel · **quality:** 3/5 · **depth:** intro
- **speakers:** Ian Ballantyne, KP Sawhney · **orgs:** Google DeepMind, Google
- **topics:** agent-architecture, coding-agents, skills-self-improvement, infra-cost-scaling · **tags:** antigravity, agent-harness, shared-workspace, token-cost, quota, skills-sprawl, trajectory-store, agent-observability, pr-review, mock-tpu, mcp-vs-cli, model-fallback

> A Google DeepMind panel on running coding and research agents at Google scale, covering shared workspaces, quota and cost control, skill sprawl, internal observability, and PR review.

## Summary
Ian Ballantyne (DeepMind developer relations) and KP Sawhney (DeepMind AI platform team) open with a live demo of Antigravity, the agent-manager IDE. The agent reads a spec, plans with built-in to-dos, drives a browser, inspects the DOM, and writes notes and a final report, and the user can edit the plan before saying "proceed." Sawhney says the team is moving the deep-research pipeline onto this harness, with stages collaborating through a shared file system rather than passing large text blobs. The main scaling worries are token cost and per-user quota, which Google currently handles by brute force, and power users who spin up many agents. Internally, Google uses a custom UI that traces each agent request down to the raw model call, plus a trajectory store for finding where a coding run started looping. On skills, the speakers describe a large internal library that risks sprawl, so the best skills are kept through a Darwinian process. They also discuss evals, which are hard to build for skills, and automated PR review, which uses a per-language review model fine-tuned on style guides.

## Key ideas
- **Antigravity is an agent platform, not just an IDE** — It has an agent manager that spawns several agents across projects, built-in to-dos and planning, browser control, DOM inspection, and screenshot or video capture. At the end it writes a report of what was done. ([1:09](https://youtu.be/7gujZrJ9L5I?t=69))
- **Human-in-the-loop plan editing before execution** — The agent writes an implementation plan that shows what it intends to change. The user can edit single lines or redirect it, then says proceed. The scratchpad notes give a trace the user can review or interrupt. ([3:52](https://youtu.be/7gujZrJ9L5I?t=232))
- **Pipeline stages should share a workspace, not pass text blobs** — For deep research, the speaker wants stages to collaborate in a shared file system. Passing large search outputs between steps is expensive and eats context. Each element should act more like a collaborator in a workspace. ([4:53](https://youtu.be/7gujZrJ9L5I?t=293))
- **Token cost and quota are the top scaling problem** — Agents are very token hungry, so per-user and per-team quota management is central. The speakers expect pricing to change, since subscription models do not fit agentic usage. They mention Anthropic blocking OpenClaw-style use as an example. ([8:13](https://youtu.be/7gujZrJ9L5I?t=493))
- **Mix cheap local models with frontier models by component** — Gemma 4 can run on your own GPUs or TPUs with no quota cost, and it can handle bulk work. Stronger models are reserved for specific components of the agent system. ([8:13](https://youtu.be/7gujZrJ9L5I?t=493))
- **Skills need curation to avoid sprawl** — A large internal skill library helps people do their jobs, but skills can sprawl out of control. The team wants only the best skills to survive, a Darwinian selection process. ([6:09](https://youtu.be/7gujZrJ9L5I?t=369))
- **Evaluating agent workflows is hard, and test data is the bottleneck** — Spinning up sandboxed environments for each problem set is mechanically hard. The trickiest part is building new datasets. Skill authors are expected to write their own tests, and agents are being tried at designing those tests too. ([18:12](https://youtu.be/7gujZrJ9L5I?t=1092))
- **Observability needs drill-down from request to raw model call** — One internal backend shows every agent query in a web UI. You can drill from the top level down to the raw model request. A trajectory store lets you find the exact step where looping or going off the rails began. ([13:33](https://youtu.be/7gujZrJ9L5I?t=813))
- **Quota exhaustion should fall back seamlessly, not stop the job** — The goal is for the harness to move work to a cheaper model or a local model when quota runs out, without interrupting the task. A user should not come back to find the job idle for an hour. ([21:15](https://youtu.be/7gujZrJ9L5I?t=1275))

## Techniques
- **Shared file-system workspace between agent stages** — Each stage writes its outputs to files in a common workspace and passes references or paths onward, not large text payloads in the prompt. Stages can read and extend each other's artifacts. *When:* Multi-stage research or coding pipelines where inter-stage context is large and costly to pass through the model.
- **Editable plan gate before execution** — The agent drafts an implementation plan and shows it to the user. The user edits individual lines or redirects it, then approves with a proceed step before any changes are made. *When:* Agent edits to real codebases where the user wants to correct intent before work starts.
- **Scratchpad notes as a reviewable trace** — The agent keeps running notes on its reasoning and actions. The user can read them mid-run and interrupt if the agent is heading the wrong way. *When:* Long autonomous runs that need human oversight without constant prompting.
- **Mock compute for harness testing** — Replace the expensive model or hardware layer with mocks to test the harness flow and control logic, and save real compute for final checks. *When:* Testing complex agent workflows where the orchestration logic is what needs verifying, and compute is scarce.
- **Trajectory store plus hierarchical drill-down** — Record every step of an agent run, then view it in a UI that drills from the request down to each model call. Use it to locate the first step where a loop or failure started. *When:* Debugging long coding-agent runs or loops, and per-user spend investigations.
- **Per-language fine-tuned review model plus per-product review prompts** — A review model is fine-tuned on each language's style guides and good past examples. Each product adds its own specialized instructions and prompts so the other reviewers get a stronger signal. *When:* Automated PR review at large scale, where generic reviewers give weak feedback.
- **Transparent model fallback under the harness** — When one model or tier hits its limit, the harness moves the work to another model, for example Pro to Flash or to a local model. The user is told clearly what happened, but the task keeps running. *When:* Long agent jobs on tiered or quota-limited model access.
- **Skills plus guardrailed CLI over MCP for internal tools** — Package domain knowledge as skills that wrap a guarded CLI. The speaker keeps MCP for its auth model but prefers skills and CLI for daily work. *When:* Internal agent tooling where experts contribute reusable skills and the agent needs safe, scoped command access.

## Numbers
- Audience hands-up: about four or five people had used Antigravity before the demo. ([0:00](https://youtu.be/7gujZrJ9L5I?t=0))
- Google engineers submitting around 100,000 lines of code, with agents adding more, which increases the review load. ([23:05](https://youtu.be/7gujZrJ9L5I?t=1385))
- The speaker needed to click about 100 times to keep the agent going, because Google accounts get lower limits than customers. ([21:15](https://youtu.be/7gujZrJ9L5I?t=1275))
- Example user scenario: one power user runs a team of 100 agents, which raises per-user abuse and quota concerns. ([11:31](https://youtu.be/7gujZrJ9L5I?t=691))
- A speaker cites GitHub receiving trillions of lines generated by agents (second-hand, not verified). ([24:17](https://youtu.be/7gujZrJ9L5I?t=1457))

## Hot takes
- MCP may be a flash in the pan. Its auth model is powerful, but skills plus a guardrailed CLI work better day to day.
- Subscription pricing does not fit token-hungry agentic systems, so agent pricing will change.
- Skill libraries inside large orgs need Darwinian pruning or they sprawl out of control.
- The trickiest part of agent evals is making new datasets, not spinning up sandboxes.

## Tools mentioned
Antigravity, Gemini, Gemma 4, Deep Research, Jules, MCP, OpenClaw

## Relevance to our work
- **agentos** (2/3): Per-user quota and fallback routing map onto L1 budgets and strategy routing. The trajectory store and drill-down observability map onto L4. Skill sprawl maps onto SkillForge curation. → *Add a per-user or per-team token quota with a fallback chain (frontier, then cheap model, then local Gemma) to the L1 proxy. Also add a trajectory view that finds the first step of a loop in a run.*
- **prosharness** (2/3): The editable plan gate before proceed matches ProsHarness's plan step. Shared workspace files between stages match checkpoint and resume design. → *Compare ProsHarness's plan step with an editable plan and explicit proceed gate. Consider writing stage outputs to files in a shared workspace and passing paths, not text, between plan, critique and debate stages.*
- **general** (2/3): Context engineering: large inter-stage payloads are expensive, and the speakers name file-based collaboration as the fix. Evals are hard for skills, and the speakers say skill authors must write their own tests. → *Read the speakers' argument for file-based inter-stage communication, then test a pipeline that passes file paths in place of text blobs and measure context and cost.*
