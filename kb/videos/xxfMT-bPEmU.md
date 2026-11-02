# From coding to Knowledge work agents — Karan Vaidya, Composio

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `xxfMT-bPEmU` · [watch](https://youtu.be/xxfMT-bPEmU) · **date:** 2026-09-18 · **length:** 20:42 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Karan Vaidya · **orgs:** Composio, Meta Superintelligence Labs (mentioned in an anecdote)
- **topics:** governance-compliance, agent-architecture, sandboxing-execution, memory · **tags:** knowledge-work-agents, agent-governance, reversibility, sandboxing, action-logging, skill-distillation, composio, tool-access-control

> Composio CTO on why coding agents work and knowledge-work agents don't: six missing primitives (centralization, history, context, verification, governance, reversibility), enforced with walls and sandboxes rather than prompts.

## Summary
Composio's CTO argues that coding agents succeeded because the infrastructure around code (repo, git history, CI, linters, revert) was built for agents, while knowledge-work agents lack that base. He names six primitives coding had and knowledge work lacks: centralization, history, context, verification, governance and reversibility. Centralization means one place for all app connections and logins, since a single deal is spread across Salesforce, Notion, Gmail, Slack and Zendesk. Logging every agent action across apps gives the agent memory, lets people audit it, and over time yields distilled skills about how the organization works. For verification he suggests pre-send style checks and sandboxes that mock real tools. For governance he argues that access limits and behavior policies must sit outside the agent, because prompt instructions get forgotten or compacted. Reversibility is the hardest gap, since sent emails, wires and hard deletes cannot be undone, so irreversible actions should be rehearsed in a sandbox and reviewed first. The speaker frames infrastructure, not models, as the bottleneck, and the talk closes with a recruiting and product pitch for Composio.

## Key ideas
- **Coding agents succeeded because of the surrounding infrastructure, not only the models** — Repo, commit history, CI/CD, review, linters and revert were already in place for code. Knowledge work (support, finance, sales) has none of these, so agents there work blind. ([1:18](https://youtu.be/xxfMT-bPEmU?t=78))
- **Centralization: one place for all connections and logins** — A single deal is scattered across Salesforce, Notion, Gmail, Slack and Zendesk, each with its own login. The agent should start from one hub that holds the apps and access, as a coding agent starts from the repo. ([2:47](https://youtu.be/xxfMT-bPEmU?t=167))
- **A record of every agent action gives memory and trust** — Logging what the agent touched, skipped, succeeded at and failed at lets it reuse how similar tasks were done. It also lets humans check the actions rather than trust the agent's own report of success. ([4:49](https://youtu.be/xxfMT-bPEmU?t=289))
- **Context has two kinds: platform shape and company style** — Shape means how the data and systems connect, which a senior engineer holds in their head. Style means what good looks like locally, such as linters or idioms. Both can be read from the code in coding, and from logs in knowledge work. ([6:53](https://youtu.be/xxfMT-bPEmU?t=413))
- **Distill skills from the action log at three levels** — Patterns in logged runs can become skills about how a tool works in general, how a company operates, and how a particular person prefers to work. The agent can then query them instead of guessing. ([8:21](https://youtu.be/xxfMT-bPEmU?t=501))
- **Verification must check whether an action should happen, not only whether it is valid** — In his example, a mass outreach email passed every validity check (real addresses, valid format), but nothing asked if it should be sent at all. He proposes checking drafts against the user's past sent emails for style, and running destructive steps against mocked tools first. ([10:23](https://youtu.be/xxfMT-bPEmU?t=623))
- **Governance must be enforced outside the agent, in two layers** — A deterministic access layer limits what the agent can reach (e.g. read-only, or draft but not send). A policy layer limits what it can do with that access (e.g. never delete more than 10 emails without permission, never email outside a domain). He says prompting is fragile because instructions get compacted away. ([14:40](https://youtu.be/xxfMT-bPEmU?t=880))
- **Reversibility is the hardest gap, so irreversible actions need trust before they run** — Code has revert and bisect. Knowledge work often has no undo for sent emails, wires or hard deletes. He recommends undo where it exists (such as removing a label) and a sandbox-then-review flow for actions that cannot be undone. ([17:03](https://youtu.be/xxfMT-bPEmU?t=1023))

## Techniques
- **Single connection hub for agents** — Route all app connections and logins through one place, so the agent starts with the full set of systems and does not have to stitch together threads itself. *When:* Multi-app knowledge-work agents such as support, sales or finance agents that touch several SaaS tools.
- **Cross-app action record** — Log every action the agent takes, with what it touched, what it skipped, and the outcome. Use the log for memory of past similar tasks, for audit, and for checking claims about success. *When:* Any agent that writes to business systems, from the first run onward.
- **Skill distillation from run logs** — Mine the action log for recurring patterns about which approaches worked and which failed, and store them as skills at tool, company and personal levels. *When:* After enough logged runs exist to show repeatable patterns.
- **Pre-send style check against past outputs** — Before an agent sends outbound text, compare the draft with the user's previously sent messages for tone and fit, and add a check on whether the send should happen at all. *When:* Agents that send emails or messages to people outside the team.
- **Sandbox mirror of production tools** — Mock the real tools in a sandbox. The agent performs the destructive step there, a human reviews the result, and only then the action runs for real. *When:* Hard deletes, sends, payments or any action with no undo.
- **Two-layer walls: access scope plus behavior policy** — Put deterministic access scopes (read-only, draft-only) at a boundary the agent cannot change, then add declarative policies on top, such as count thresholds for deletes or an allowlist of recipient domains. *When:* Any agent with write access to email, CRM or other systems where a prompt-only rule is not enough.
- **Tiered gates scaled to blast radius** — Use several gates of different strength: agents work on branches but cannot merge to main, code owners review critical files, and agents deploy to previews but not production. Strictness rises with the damage a bad action could do. *When:* Coding agents, to allow fast autonomous work where errors are cheap and human review where they are not.
- **Undo for reversible actions, sandbox for the rest** — Give the agent a reverse button for reversible actions (e.g. removing a label it added). For irreversible actions, run them in a sandbox first and ask the user to confirm the outcome. *When:* When designing the set of actions an agent is allowed to take.

## Numbers
- Composio has powered over a billion tool calls in total ([18:29](https://youtu.be/xxfMT-bPEmU?t=1109))
- Composio handles about 300 million tool calls per month ([18:29](https://youtu.be/xxfMT-bPEmU?t=1109))
- A junior engineer takes around three months to build the architecture map that a senior engineer carries in their head (analogy, not a measurement) ([6:53](https://youtu.be/xxfMT-bPEmU?t=413))
- In the Meta alignment anecdote, an agent deleted about 200 emails before it was stopped by physically running to the machine ([13:19](https://youtu.be/xxfMT-bPEmU?t=799))
- Example policy: never delete more than 10 emails without permission ([15:43](https://youtu.be/xxfMT-bPEmU?t=943))
- Example sandbox notification: an agent is about to delete 1,200 emails ([18:29](https://youtu.be/xxfMT-bPEmU?t=1109))

## Hot takes
- Prompt instructions are not governance: they get forgotten or compacted, so the boundary must sit outside the agent.
- For knowledge work, trust has to come before the action, because mistakes like sent emails or wires cannot be rolled back as code can.
- Passing validity checks is not enough, since a check can confirm an email is well-formed and still not ask whether it should be sent.
- The bottleneck has moved from models to the infrastructure around them, at least for non-coding work.

## Tools mentioned
Composio, Claude Code, Codex, Cursor, OpenClaw, Git, Salesforce, Notion, Gmail, Slack, Zendesk, bugbot.md (named in passing)

## Relevance to our work
- **agentos** (2/3): The two-layer wall (access scope plus policy) and the action log map onto L1 Govrix Scout budgets, scanning and the Merkle audit log. The talk also raises the reversibility question, which the proxy does not yet handle. → *Add a reversibility tag to tool/action classes in the L1 proxy so irreversible calls are routed to a sandbox or approval step, and check that the Merkle audit log records attempted and skipped actions, not only completed ones.*
- **prosharness** (2/3): ProsHarness already has phone-driven approvals and checkpoint/resume. The talk's undo versus sandbox split maps onto which Claude Code actions need approval. → *Classify Claude Code actions in ProsHarness as reversible (file edits under git) or irreversible (push, deletes, external sends), and require phone approval only for the irreversible class. Log each run's actions so they can later be mined into skills.*
- **general** (1/3): The idea of distilling run logs into skills at tool, company and personal levels is relevant to the context-engineering interest. The talk gives no implementation detail. → *Read the talk's skill-distillation section (8:21) for framing only; no build step is needed yet.*
