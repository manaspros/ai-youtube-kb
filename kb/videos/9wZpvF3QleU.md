# 500 Skills, Zero Fine-Tuning: LinkedIn's Playbook for AI Agents — Ajay Prakash, LinkedIn

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `9wZpvF3QleU` · [watch](https://youtu.be/9wZpvF3QleU) · **date:** 2026-09-18 · **length:** 20:25 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Ajay Prakash · **orgs:** LinkedIn
- **topics:** skills-self-improvement, mcp-and-tools, context-engineering, coding-agents · **tags:** playbooks, MCP, progressive-discovery, meta-tools, tribal-knowledge, self-improving-docs, central-vs-local-playbooks, enterprise-coding-agents

> LinkedIn's Ajay Prakash on an internal MCP server that serves tools plus self-contained markdown "playbooks" teaching coding agents company workflows, kept current by a PR-based self-update loop.

## Summary
Ajay Prakash (LinkedIn) explains why generic coding agents failed on LinkedIn's internal stack and how the company fixed it. Adding MCP tools helped, but agents still could not finish jobs reliably end-to-end because the needed tribal knowledge sat in stale docs, wikis and Slack, tool outputs bloated context, and nothing persisted between sessions. The fix was "playbooks": instruction documents served through the same MCP server as tools, which an agent invokes by name and receives as tool output. Playbooks should be self-contained for one task and reference smaller playbooks, which gives reuse and progressive discovery. Agents are asked to note outdated or missing content at session end and open a PR to update the playbook after approval. The MCP server is pre-installed on every laptop and auto-updates hourly, with central (cross-repo) and repo-local playbooks. The speaker says MCP degrades past roughly 30 to 40 tools, so the catalogue is hidden behind three meta tools (search, get schema, execute). He reports 8,000+ daily users, 1,300+ tools and 600+ playbooks, but gives no benchmarks or controlled comparisons.

## Key ideas
- **Generic coding agents fail in large enterprises because they lack internal context.** — LinkedIn has 1,000+ repos plus internal frameworks, databases, experimentation and config systems. Agents hallucinated or invented APIs, and engineers spent more time prompting than coding. Engineers also go through a week-long bootcamp to learn these systems. ([3:08](https://youtu.be/9wZpvF3QleU?t=188))
- **More MCP tools compound value but do not make agents reliable end-to-end.** — Code search was the first internal MCP tool, then docs, Jira, Slack, data platforms and feature flags. Complex jobs still failed because the needed knowledge was tribal and scattered across outdated docs, duplicate wikis and Slack threads. ([6:43](https://youtu.be/9wZpvF3QleU?t=403))
- **Three failure modes: lost on tribal knowledge, context overload, and no durable memory.** — Every tool output consumes context, which forces compaction and loses information mid-task. Agents also keep no durable memory, so each engineer's request starts from scratch. ([9:11](https://youtu.be/9wZpvF3QleU?t=551))
- **Playbooks are instructions served over MCP that look like ordinary tools.** — Each playbook has a name and description, and the agent can choose to invoke it. The playbook's content comes back as tool output, so the agent gets both how-to instructions and the tools to carry them out (e.g. setting up an Airflow DAG). ([10:37](https://youtu.be/9wZpvF3QleU?t=637))
- **Keep playbooks self-contained for one task and compose larger ones by reference.** — Small single-task playbooks can be reused by many others. The agent reads sub-playbooks only when needed, which is progressive discovery. The speaker says this is close to the skills concept, but LinkedIn built it before skills existed. ([12:48](https://youtu.be/9wZpvF3QleU?t=768))
- **A session-end self-update loop keeps playbooks from going stale.** — The agent is asked to record discrepancies, missing or outdated steps at the end of a session, then check out the repo, edit the playbook and open a PR. Human approval merges it, which creates a flywheel. ([14:13](https://youtu.be/9wZpvF3QleU?t=853))
- **Split playbooks into central (cross-repo) and repo-local, served by one local MCP server.** — The server is pre-installed on all laptops and updates hourly. Repo-local playbooks are checked into their repo and only load when agents work in that repo, so repo owners do not need changes to a central repo. The single server also centralises auth and telemetry. ([15:13](https://youtu.be/9wZpvF3QleU?t=913))
- **Replace a large tool catalogue with three meta tools to scale past MCP's practical limit.** — The speaker says MCP degrades past about 30 to 40 tools. Instead of exposing everything, the agent uses search (keywords and tags), get schema, then execute. Coding agents get pre-configured system instructions on how to use these meta tools. ([16:13](https://youtu.be/9wZpvF3QleU?t=973))
- **Quality and infrastructure, not model access, are the takeaways.** — The speaker says the system worked because quality and reliability were designed in from day one. He argues that enterprises need the right infrastructure for agents, since giving everyone the latest models is not enough. ([19:08](https://youtu.be/9wZpvF3QleU?t=1148))

## Techniques
- **Playbooks as MCP-served instruction docs** — Store markdown how-to instructions, expose each one as an MCP tool with a name and description, and return its content as tool output when invoked. Keep each playbook focused on one task. *When:* Repeatable internal workflows that need company-specific knowledge the model lacks.
- **Compose playbooks by reference** — Break large playbooks into small self-contained ones and have larger playbooks point to them. The agent reads sub-playbooks only when it reaches that step. *When:* Many overlapping tasks where reuse and limited upfront context both matter.
- **Session-end playbook self-update PR** — Instruct the agent to note outdated or missing content at session end, edit the playbook in its repo, and open a PR. Human approval merges it. *When:* Any knowledge base that decays, where agents hit the gaps during real work.
- **Three meta tools for large tool catalogues** — Expose search (keywords and tags), get schema, and execute instead of every tool. Pre-configure the coding agent's system prompt to use the search-then-fetch-then-run pattern. *When:* Tool or playbook counts exceed roughly 30 to 40, which the speaker says degrades performance.
- **Central plus repo-local instruction split** — Cross-cutting playbooks live in a central repo. Repo-specific ones are checked into the repo and loaded only when an agent works there. *When:* Scaling ownership of agent instructions across many repos without a central bottleneck.
- **Single pre-installed local MCP server with hourly auto-update** — Ship one local MCP server to every laptop that auto-refreshes its tools and playbooks, and route auth and telemetry through it. *When:* Rolling out agent tooling org-wide and needing consistent auth, telemetry and updates.

## Numbers
- Over 1,000 repos making up thousands of microservices and apps at LinkedIn. ([4:09](https://youtu.be/9wZpvF3QleU?t=249))
- Week-long bootcamp for new engineers to learn internal systems. ([5:37](https://youtu.be/9wZpvF3QleU?t=337))
- Speaker says MCP degrades beyond about 30 to 40 tools (his claim, no data shown). ([16:13](https://youtu.be/9wZpvF3QleU?t=973))
- MCP server auto-installed on all laptops and updated every hour. ([15:13](https://youtu.be/9wZpvF3QleU?t=913))
- Over 8,000 daily users of the tools and playbooks system. ([17:40](https://youtu.be/9wZpvF3QleU?t=1060))
- Over 1,300 tools and over 600 playbooks in the system. ([17:40](https://youtu.be/9wZpvF3QleU?t=1060))
- Speaker's anecdote: an on-call incident that would take hours by hand finishes in minutes with the agent (anecdotal, not measured). ([2:07](https://youtu.be/9wZpvF3QleU?t=127))

## Hot takes
- Playbooks are essentially skills, and LinkedIn built the concept before skills existed.
- Past about 30 to 40 MCP tools, adding more tools hurts rather than helps, so use meta tools for discovery.
- Stale internal docs are best kept fresh by letting the agent open PRs against them at the end of each session.
- Enterprise value comes from agent infrastructure (auth, telemetry, instructions), not from giving everyone the newest model.

## Tools mentioned
MCP, Claude Code, GitHub Copilot, Cursor, Airflow, Jira, Slack

## Relevance to our work
- **agentos** (2/3): SkillForge mines telemetry into governed reusable skills; this talk's single-task playbooks, composition by reference, and session-end update PRs map onto that design. → *Compare SkillForge's skill format against single-task, reference-composed units, and test a session-end 'update the skill via PR' step as a source of the skill-worthiness signal.*
- **general** (2/3): Concrete context-engineering pattern for coding agents in a large internal codebase, with a clear progressive-discovery rule. → *Adopt the rule of one self-contained, single-task instruction doc per workflow, referenced from larger docs rather than inlined.*
- **prosharness** (1/3): ProsHarness does skill ranking and checkpointed runs, and this talk covers how agents discover and invoke instructions, which is adjacent but not a direct change. → *Read the playbook self-update PR loop as a pattern for keeping ProsHarness skills current; no change needed yet.*
