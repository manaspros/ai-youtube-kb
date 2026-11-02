# Realtime multiplayer, automation, and you! — Idan Gazit, GitHub

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `iQ5xldZ9StU` · [watch](https://youtu.be/iQ5xldZ9StU) · **date:** 2026-08-18 · **length:** 21:41 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Idan Gazit · **orgs:** GitHub, Microsoft
- **topics:** software-factory, security-guardrails, coding-agents, sandboxing-execution · **tags:** agentic-workflows, github-actions, markdown-as-source, prompt-injection, guardrails, secrets-broker, safe-outputs, multiplayer, cloud-sandbox, shared-plans, background-automation, dependency-upgrades

> GitHub Next demos Agentic Workflows (markdown playbooks compiled to Actions with deterministic guardrails) and ACE, a cloud multiplayer dev environment where humans and agents share chat and plans.

## Summary
Idan Gazit, who leads GitHub Next (the labs team), argues that AI now automates tasks that need judgment, not just heuristics, so teams can spend the time saved on craft. He shows Agentic Workflows: a natural-language playbook written in markdown, with a small YAML front matter block, that compiles into a GitHub Actions workflow and runs in the background, such as an Astro dependency upgrader that edits code and opens a single PR. The security argument is that guardrails must be enforced deterministically (tool, read/write, and network allowlists, a cap on safe outputs, an explicit "do nothing" option) because prompting guardrails can be overridden by prompt injection. Secrets stay outside the agent, which asks a broker to call services on its behalf, and all writes are staged and logged. The second half demos ACE, where each session is a cloud microVM checked out to a branch, and teammates and the agent share one chat and one markdown plan that both can edit. He closes with the point that typing is only about 5% of developer time, so AI should help with the rest.

## Key ideas
- **Background automations, not interactive chat, may be the bigger category** — The speaker expects automations that run in the background while people sleep to be a bigger category than interactive AI. Agentic Workflows was announced in public preview in this talk. ([13:01](https://youtu.be/iQ5xldZ9StU?t=781))
- **Markdown is the source; the Actions YAML is a compiled artifact** — A playbook is written in plain English, as if briefing a junior dev. It is compiled into a GitHub Actions workflow that nobody needs to read. To change behavior, you edit the English and it recompiles. ([9:37](https://youtu.be/iQ5xldZ9StU?t=577))
- **Guardrails must be deterministic config, not prompts** — Telling the agent not to do something in the prompt fails under prompt injection. Permissions, tool access, network domains and write types are declared in YAML front matter that the runtime enforces. ([7:31](https://youtu.be/iQ5xldZ9StU?t=451))
- **Cap the agent's writes to prevent noise and denial of service** — Safe outputs list the only things the agent may write, such as a single pull request. A prompt-injected agent that opens 500 PRs would be a denial of service, and the agent is also allowed to do nothing, which keeps notification noise low when many automations run. ([7:31](https://youtu.be/iQ5xldZ9StU?t=451))
- **Defense in depth and never give agents secrets** — Treat any secret an agent can see as already compromised. Secrets sit outside the agent's sandbox, and when a call is needed the agent asks a broker to make it. All writes are staged for vetting and everything is logged for audit. ([11:47](https://youtu.be/iQ5xldZ9StU?t=707))
- **Shared documents and chat become the interface when code is cheap** — When writing code costs little, planning and review are iterative and collaborative. Facts that are not in code, such as political or vendor considerations, are best surfaced in a shared surface, not in Slack or Word docs. ([13:01](https://youtu.be/iQ5xldZ9StU?t=781))
- **Each agent session is a cloud branch with the team's chat as context** — In ACE, every session is a repo branch in a cloud microVM, not on a laptop. The agent reads the whole team chat and can act on the final decision the group reached, instead of asking the human to restate it. ([14:26](https://youtu.be/iQ5xldZ9StU?t=866))
- **Make the document true instead of editing code** — Plans are markdown that humans and the agent edit together. The speaker imagines a future where a change is made by editing the doc and telling the AI to make the document true. ([17:12](https://youtu.be/iQ5xldZ9StU?t=1032))
- **Typing is a small share of developer time** — Citing a longitudinal study of 100 developers over thousands of hours, the speaker says hands-on typing is about 5% of the job, so AI tools that only speed typing miss most of the work. ([19:34](https://youtu.be/iQ5xldZ9StU?t=1174))

## Techniques
- **Markdown playbook compiled to CI workflow** — Write the automation as a plain-English task list (check for releases, read changelog and docs, apply upgrade, open a PR, and so on) plus a short YAML front matter. A compiler turns it into an Actions workflow. Iterate by editing the markdown. *When:* Recurring background maintenance: dependency upgrades, issue triage, CI failure triage, repo status summaries, and tasks that a PM can also write.
- **Declarative guardrail front matter** — Declare allowed tools, read and write scopes, network domain allowlist, and a safe-outputs list with counts (for example, one PR). Let the runtime enforce these, not the prompt. Include an explicit do-nothing outcome. *When:* Any agent that reads untrusted input such as issues or web pages and has write access to a repo or service.
- **Secret brokering outside the agent sandbox** — Keep credentials in a broker. The agent sends a request, the broker checks it and performs the call, and the result is logged. The agent never holds the secret. *When:* Agents that call authenticated external services and could be prompt-injected into leaking credentials.
- **Staged, logged writes** — Route all agent writes through a staging step that is vetted and logged before it takes effect. *When:* Auditable automation in production repos or shared systems.
- **Swarm of role-specific workflows** — Run several small agentic workflows that cover different maintenance jobs, such as issue triage, low-hanging-fruit fixes, nudging stale tickets, and CI diagnosis, rather than one large agent. *When:* Keeping a busy repo maintained continuously.
- **Shared cloud session per branch with team chat as context** — Give each task a cloud sandbox checked out to a branch. Keep the discussion in a shared thread, then ask the agent to act on the agreed outcome rather than restating it. *When:* Team work where decisions happen in chat and the agent should follow the group's final decision.
- **Shared markdown plan as contract** — Have the agent write the plan as a markdown file in the repo. Teammates edit it directly, then ask the agent to act on the edited plan. *When:* Feature planning where humans and agents must agree before code is written.
- **Automation triage by stack trace origin** — For each incoming issue, have the agent walk the stack trace to decide whether the failing code is first-party or third-party, then close or route the issue accordingly. *When:* Large open-source projects with high issue volume, as used by Home Assistant.

## Numbers
- Hands-on typing is about 5% of developer time, per a longitudinal study of 100 developers over thousands of hours (cited by the speaker). ([19:34](https://youtu.be/iQ5xldZ9StU?t=1174))
- Astro upgrade example jumped two major versions, from 5 to 7, with the agent fixing breaking changes and verifying the build. ([9:37](https://youtu.be/iQ5xldZ9StU?t=577))
- Astro ships about 50 releases a month, which motivates automated dependency upgrades. ([4:12](https://youtu.be/iQ5xldZ9StU?t=252))
- Agentic Workflows is in public preview; ACE is expected in technical preview later in the month of the talk. ([13:01](https://youtu.be/iQ5xldZ9StU?t=781))

## Hot takes
- Prompting guardrails into an agent is letting the fox loose in the henhouse; real guardrails have to be deterministic.
- Background automations that run while you sleep will be a bigger category than interactive AI.
- The markdown is the source code and the YAML is a compiled artifact you never look at.
- Since typing is about 5% of dev time, tools that only speed up typing miss most of the work.

## Tools mentioned
GitHub Copilot, GitHub Actions, Dependabot, Astro, Cloudflare, ACE (GitHub Next prototype)

## Relevance to our work
- **agentos** (2/3): Declarative tool, network and write allowlists plus a per-run write cap, enforced by the runtime rather than the prompt, map onto the Govrix proxy and Crucible exec-gate guardrails. → *Add a manifest-level allowlist with a max-writes cap, enforced in the proxy layer, and test that a prompt-injected agent cannot exceed it.*
- **prosharness** (2/3): ProsHarness already runs loops and schedules and needs approvals. The shared markdown plan that humans and the agent co-edit, and the cap on safe outputs, are both directly relevant. → *Store the ProsHarness plan as an editable markdown file that the user can change and the agent re-reads before each step, and add a safe-outputs cap to scheduled runs.*
- **general** (1/3): Markdown-as-source for automations and the make-the-document-true pattern are useful for context engineering, but the talk is a product demo with little detail on how it works. → *Read the GitHub Agentic Workflows documentation and library examples to compare the front matter schema with the ProsHarness and AgentOS manifest designs.*
