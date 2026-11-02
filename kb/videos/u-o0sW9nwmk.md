# From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `u-o0sW9nwmk` · [watch](https://youtu.be/u-o0sW9nwmk) · **date:** 2026-10-08 · **length:** 18:31 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Rafal Wilinski · **orgs:** Runlayer, Zapier
- **topics:** skills-self-improvement, mcp-and-tools, security-guardrails · **tags:** agent skills, skill distillation, self-improving agents, MCP distribution, Voyager, procedural memory, skill library, prompt injection scanning, organizational knowledge, Runlayer

> Rafal Wilinski (Runlayer) argues agents should distill successful and failed runs into skills, serve them via MCP as a governed company-wide library, and reports a 36% to 100% success jump after one distilled skill.

## Summary
The speaker frames skills as progressive-disclosure playbooks that narrow an agent's search space, and says most company know-how is lost when a session closes. He lists three problems with today's skills: they are local and developer-centric, nobody writes down hard-won procedures, and many non-developer clients do not support skills. His answer is to serve skills through a remote MCP server as the distribution layer, using tools rather than resources because resource support is inconsistent across clients. He credits the Voyager Minecraft paper for the idea of turning exploration into a reusable skill library. Runlayer's pipeline takes traces from runs, distills a skill with an LLM, and treats failed runs as the richest signal for refining it. Before a skill enters the shared library, it passes checks for prompt injection and PII. He reports a Chromium-in-Lambda task going from 36% to 100% success with Sonnet 4.6 after one distilled skill, a single anecdote with no sample size given. He closes by arguing that a company's distilled internal procedures are a moat and a hedge against model deprecation.

## Key ideas
- **Skills are playbooks loaded by progressive disclosure** — The client first sees only a short skill description, then reads the full playbook into context when it judges the skill relevant. The speaker says this changes the agent's trajectory and narrows the search space. ([1:41](https://youtu.be/u-o0sW9nwmk?t=101))
- **Skills have three problems: dev-centric and local, no capture of tacit knowledge, and uneven client support** — Skills live as markdown, JSON, CLI commands and git repos, which suits developers but not marketing, HR, legal or finance. Most people never write down the playbook after solving a hard problem. Some clients do not support skills at all. ([4:15](https://youtu.be/u-o0sW9nwmk?t=255))
- **MCP can serve as the distribution layer for skills** — A remote MCP server becomes the source of truth. Clients search for skills, and the server applies policy by query and role. The speaker chose tools over resources because resource support is mixed across clients, and notes a Skills Over MCP working group. ([7:58](https://youtu.be/u-o0sW9nwmk?t=478))
- **Turn exploration into reusable procedural knowledge (Voyager)** — Voyager saved each discovered recipe as code in a skill library and retrieved it later instead of rediscovering it. The speaker adopts this as the core idea for his team's pipeline. ([10:16](https://youtu.be/u-o0sW9nwmk?t=616))
- **Failed runs are the richest signal for sharpening skills** — Successful runs make a skill more trustworthy. Failed runs expose missing guardrails, missing libraries and edge cases, so each pass or fail feeds the distiller. The loop runs asynchronously with no human in it. ([11:40](https://youtu.be/u-o0sW9nwmk?t=700))
- **Gate skills before they reach the shared library** — Distilled skills are checked for prompt injection and PII before they are published. A central MCP gateway then serves the approved library to every client and agent in the company. ([15:17](https://youtu.be/u-o0sW9nwmk?t=917))
- **Internal distilled procedures as a moat and a hedge against model churn** — The speaker argues that models become commodities and can be deprecated or degrade, so a company's compounding library of its own procedures is harder to copy and lowers cost without switching models. ([16:42](https://youtu.be/u-o0sW9nwmk?t=1002))

## Techniques
- **Trace-to-skill distillation** — After an agent run that succeeds or looks interesting, send the tool-call trace to an LLM and ask it to write a reusable skill. Store the skill for future runs. *When:* Multi-step agent tasks where the same procedure recurs, such as a deploy, rollback or a customer-handling playbook.
- **Learn from failures too** — Feed failed runs into the same distiller so a failure adds the missing guardrail, library or edge case to the skill. Successes raise trust in the skill and failures make it more robust. *When:* Any skill loop where you can tell success from failure, such as a verifiable task outcome.
- **Checks before publishing a skill** — Scan each distilled skill for prompt injection and PII before it enters the shared library. *When:* Any setup where agents write content that other agents will later load into context.
- **Remote MCP skill registry with tool-based access** — Expose skill search and retrieval as MCP tools on a central server, with policy applied per role or query, so any MCP client can use the skills. *When:* Mixed client fleets where some clients (non-developer chat apps) cannot load local skill files or do not support MCP resources.
- **Group similar runs before distilling** — Cluster similar runs first, then distill one skill from the group rather than from a single run. *When:* When many runs cover the same problem and you want a more general skill.

## Numbers
- Success rate on a Chromium-fork-in-AWS-Lambda task rose from 36% to 100% after one distilled skill was added to future runs (Sonnet 4.6). Single anecdote, no sample size given. ([12:31](https://youtu.be/u-o0sW9nwmk?t=751))
- Runlayer scans thousands of skills every day and reports unsafe content in them. ([5:40](https://youtu.be/u-o0sW9nwmk?t=340))
- METR-style time-horizon chart cited for longer agent task horizons. No numeric value given in the talk. ([3:02](https://youtu.be/u-o0sW9nwmk?t=182))
- Speaker reports skills cut tool calls, explored branches and token/money spend. Qualitative, no figures. ([13:50](https://youtu.be/u-o0sW9nwmk?t=830))

## Hot takes
- MCP is not dead. It is the best distribution layer for skills, because it works across almost every client.
- Failed runs are more valuable than successful ones for building skills.
- The moat is not the model. It is the company's own distilled library of how work gets done.
- Installing skills with npx is a security hazard, since skills can carry prompt injections and scripts.

## Tools mentioned
MCP, Claude Sonnet 4.6, Voyager, Chromium, AWS Lambda, npx skills

## Relevance to our work
- **agentos** (3/3): Maps directly onto L2D SkillForge (mine agent telemetry into governed, reusable skills). The talk answers SkillForge's open question about the success signal, saying success and failure both count and a failed run is the richest signal. It also offers a concrete gate (injection and PII checks) before a skill is published, which lines up with Govrix scanning. → *Add a SkillForge distillation job that reads traces from both successful and failed runs, emits a candidate skill, and gates it with the existing Govrix injection and PII scanner before it enters the library. Measure success rate before and after on one fixed task.*
- **prosharness** (2/3): ProsHarness already has skill ranking and checkpoint/resume around Claude Code runs. Distilling a skill from each completed or failed harness run would be a cheap extension of that. → *After each ProsHarness run ends, distill a candidate skill from the trace (pass or fail) and store it as a draft that skill ranking can score before promotion.*
- **general** (1/3): Progressive disclosure of playbooks and the Voyager-style skill library are a useful framing for context engineering, though the talk gives no implementation detail.
