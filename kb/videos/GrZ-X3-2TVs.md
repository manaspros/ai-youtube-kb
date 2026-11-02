# YC Just Open-Sourced Its Multiplayer Harness

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `GrZ-X3-2TVs` · [watch](https://youtu.be/GrZ-X3-2TVs) · **date:** 2026-09-02 · **length:** 5:45 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Y Combinator, Better Stack
- **topics:** agent-architecture, security-guardrails, enterprise-adoption, coding-agents · **tags:** multiplayer-agents, agent-harness, self-hosted, slack-bot, permissions, command-policy, shell-sandbox, per-workspace-containers, open-source

> Better Stack's hands-on tour of YC's open-source "multiplayer" agent harness (QM): a self-hosted, multi-user web app with Slack access, per-workspace containers, a seven-tool surface and org-level approval modes. Promising but two weeks old.

## Summary
The presenter walks through QM, an open-source agent harness from Y Combinator, which the auto-captions render as "QM". Unlike a laptop CLI such as Claude Code, it is a full-stack web app that a company deploys on its own infrastructure, with a headless backend running agent loops, Postgres storing session history, and access through Slack or the web UI. Each user gets an isolated workspace backed by a container with persistent storage, so installed packages and cloned repos survive across sessions. Shared projects let a team share files, apps, connectors, memory and skills, while a personal space is private by default. The admin picks which harnesses (default "pi", and Claude Code if configured) users may choose, and the presenter had to add Claude Code through an API call because the admin panel has no control for it. The agent gets only seven tools (execute, read, write, publish, memory, history, background) and does everything else as shell commands inside its sandbox. An org-wide posture (strict, auto, dangerous) sets approval behaviour, and a command policy blocks risky commands like recursive deletes and destructive SQL even in dangerous mode. The presenter sees real value for teams but calls the UI and UX immature, with no clear indicator of which context is active.

## Key ideas
- **QM is a deployed multi-user web app, not a local terminal tool.** — The company runs it on its own infrastructure. A headless backend runs the agent loops, Postgres holds session history, and people reach it through Slack or the web UI. Each org member gets an isolated workspace. ([0:00](https://youtu.be/GrZ-X3-2TVs?t=0))
- **Each workspace is a persistent machine.** — Every workspace has its own container and attached storage, so a Python environment installed on Monday and files or clones from earlier are still there on Friday. The presenter presents this as the main difference from ephemeral agent runs. ([0:51](https://youtu.be/GrZ-X3-2TVs?t=51))
- **Projects are the sharing boundary.** — Each user gets a private personal space, which is effectively a private project. Team projects share tools, files, apps, connectors, memory and skills. Credentials can stay private or be shared on purpose. The presenter notes the web UI gives no persistent indicator of which context the user is configuring in. ([1:59](https://youtu.be/GrZ-X3-2TVs?t=119))
- **The harness is pluggable, but admins gate the list.** — The default is the pi harness and Claude Code can be enabled to run in the cloud. Out of the box only the harness the deployment booted with is available, and the admin panel has no control for changing that list. ([3:05](https://youtu.be/GrZ-X3-2TVs?t=185))
- **The agent gets a deliberately small tool surface.** — Only seven tools are exposed: execute, read, write, publish, memory, history and background. Everything else is a shell command inside the agent's sandbox, the same approach the presenter attributes to Claude Code, instead of many MCP servers. ([3:05](https://youtu.be/GrZ-X3-2TVs?t=185))
- **Approval is an org-wide ceiling with a command floor.** — Three org postures: strict pauses almost every tool call for human approval; auto (default) runs a classifier over external data and tool results before the model sees them; dangerous performs no screening. Teams can tighten the posture for their scope but not loosen it past the org setting. A command policy blocks recursive deletes and destructive SQL in every posture. ([3:05](https://youtu.be/GrZ-X3-2TVs?t=185))
- **Verdict: promising, not mature.** — The presenter calls it worth a look and a powerful option for teams sharing company context, but the project is two weeks old, has about 13,000 GitHub stars, and still has UI and UX gaps. It is open source, so the code can be changed. ([4:31](https://youtu.be/GrZ-X3-2TVs?t=271))

## Techniques
- **Minimal primitive tool surface plus shell sandbox** — Expose a handful of generic primitives (execute, read, write, publish, memory, history, background) and let the agent run everything else as shell commands in its own per-user machine, instead of wiring one MCP server per capability and hoping the model picks correctly. *When:* When giving a general agent broad capability on a shared platform and wanting to avoid tool-selection noise and MCP sprawl.
- **Org ceiling with per-team tightening and a posture-independent command deny list** — Set an org-wide approval posture (strict, auto or dangerous). Let team scopes only tighten it. Keep a command policy that always blocks patterns such as recursive deletes and destructive SQL, even when screening is off. In auto mode, run a classifier over external data and tool outputs before they reach the model. *When:* When rolling an agent out company-wide and the risk of one bad action has to stay bounded regardless of how permissive a team is.
- **Enable extra harnesses through the admin API** — As admin, send a PUT to the harnesses endpoint with the IDs of the harnesses to allow (the presenter used two, pi and Claude Code), then refresh. The video does not show the endpoint path, so check the repo docs. *When:* When the admin UI lacks a harness allowlist control and you need a specific harness, such as Claude Code, available to users.
- **Share context through a team project, keep credentials private by default** — Use each user's private personal space by default. Put shared tools, files, memory, credentials and skills into a team project only when they should be shared. Credentials stay private unless the admin deliberately shares them. *When:* When several people need the same connectors and docs without leaking personal secrets.

## Numbers
- About 13,000 GitHub stars at the time of the video. ([4:31](https://youtu.be/GrZ-X3-2TVs?t=271))
- Seven agent tools: execute, read, write, publish, memory, history, background. ([3:05](https://youtu.be/GrZ-X3-2TVs?t=185))
- Three org-wide approval postures: strict, auto (default), dangerous. ([3:05](https://youtu.be/GrZ-X3-2TVs?t=185))
- The project is about two weeks old. ([4:31](https://youtu.be/GrZ-X3-2TVs?t=271))
- Only the harness the deployment booted with is enabled out of the box, which the presenter saw as only pi in the dropdown. ([3:05](https://youtu.be/GrZ-X3-2TVs?t=185))

## Hot takes
- The presenter says the UI and UX are still weak and the web UI gives no clear indicator of which context the user is in.
- The presenter thinks a company-wide agent needs a posture-independent command policy and a classifier, and says this is not something you get when everyone runs agents locally.
- The admin panel has no harness allowlist control, so the presenter had to use an API call to enable Claude Code.
- The video is thin on architecture: it does not show how the classifier, command policy or workspace isolation are implemented.

## Tools mentioned
QM (YC open-source multiplayer agent harness; the caption spelling may be off, and the repo was about two weeks old at the video date), pi (the default agent harness in QM), Claude Code (can be enabled as a harness inside QM), Slack (integration surface), PostgreSQL (session history), GitHub (repo linked in the description)

## Relevance to our work
- **agentos** (2/3): The three-level approval posture, classifier over tool results, and posture-independent command deny list overlap with AgentOS's Crucible exec-gate guardrails and governance pillar. → *Compare QM's command policy (recursive deletes and destructive SQL blocked even in dangerous mode) with Crucible's exec-gate rules, and consider a posture-independent deny floor for AgentOS.*
- **prosharness** (2/3): QM runs a Claude Code harness in cloud containers where installed packages and clones persist per workspace, and admins gate which harnesses users may choose. Both are close to ProsHarness's checkpoint/resume and harness-around-Claude-Code design. → *Compare QM's per-workspace persistent-state model with ProsHarness checkpoint/resume to decide which state belongs at workspace level and which at run level.*
