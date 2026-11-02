# Orchestras, Not Factories: How the Fastest Builders Work — Charlie Holtz, Conductor

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `TRfzFJCJ7ZE` · [watch](https://youtu.be/TRfzFJCJ7ZE) · **date:** 2026-10-04 · **length:** 17:45 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Charlie Holtz · **orgs:** Conductor
- **topics:** multi-agent, software-factory, coding-agents, sandboxing-execution · **tags:** conductor, claude-code, git-worktrees, slot-free-zones, cloud-sandbox, agent-collaboration, claude-md, skills, feed-the-beast, orchestration, openclaw, software-factory-critique

> Charlie Holtz (Conductor co-founder) lists six principles for fast agent-driven building: stay near the frontier, don't beat the market, mark slot-free zones, feed a central store, run free-range cloud agents, and orchestrate rather than run a factory.

## Summary
Charlie Holtz, co-founder of Conductor (a desktop app for running many coding agents at once), gives six principles drawn from watching strong builders work. He argues for staying near the frontier of new tools, but only optimizing a workflow when the team has private information the models lack, which he calls the "don't beat the market" test. He describes "slot-free zones": parts of the codebase, such as the migrations file, that always need strict human review, while other parts are reviewed loosely. He says teams should invest heavily in CLAUDE.md and skill files, which work like a daily briefing loaded into every agent session. Conductor's internal agent ingests Slack, Discord, and meeting data into Postgres so agents can query it with SQL. He describes moving agents into cloud sandboxes that keep running when the laptop closes, with shared live workspaces and APIs that let agents spawn other workspaces. He closes by rejecting the "software factory" framing and wanting builders to feel like a conductor of an orchestra. The talk is practitioner-level but partly a product pitch for Conductor's new cloud and collaboration features.

## Key ideas
- **Stay near the frontier, not at it** — Conductor started as a side workflow when the team were heavy Claude Code users, cloning the repo several times and then discovering worktrees; the product grew out of that. Social-graph tips now lag by 3 to 6 months, so builders should try new releases close to launch, but avoid spending all their time on workflow tinkering (what he calls 'midwit memeing'). ([2:38](https://youtu.be/TRfzFJCJ7ZE?t=158))
- **Don't beat the market** — Before customizing a workflow, ask why it is not already the default. Only invest in custom tooling when you have private 'alpha' the models lack, such as knowledge of your users or codebase. Example: their chat app needs fast rendering of long chats, which justifies heavy React query tuning. ([3:52](https://youtu.be/TRfzFJCJ7ZE?t=232))
- **Slot-free zones need strict human review** — Conductor is careful about some parts of its code and loose about others, which he says is unusual. Any change to the migrations file needs a human reviewer enforced in CI. They treat Slack-written content as human-authored and slot-free. Being careless here forced them to rewrite the app a couple of times. ([5:11](https://youtu.be/TRfzFJCJ7ZE?t=311))
- **Invest in CLAUDE.md and skills like an onboarding whisper** — CLAUDE.md or AGENTS.md is loaded into the agent's context at every session start, so it works like a daily briefing you would give a new intern. The best builders he has observed spend unusual effort on these files and on their skills. ([6:35](https://youtu.be/TRfzFJCJ7ZE?t=395))
- **Feed the beast: one central database for org context** — Conductor's internal agent (nicknamed the CIA) saves every Slack message, Discord bug request, and recorded meeting into Postgres. The point is that agents work better when they have the company's real context. The recommended pattern is to store everything in one database and give the agent a SQL tool. ([7:55](https://youtu.be/TRfzFJCJ7ZE?t=475))
- **Free-range agents live in cloud sandboxes, not on the laptop** — Until recently every Conductor task ran in a git worktree on the laptop. Now tasks run in cloud sandboxes that keep going when the laptop lid closes. He argues longer-running, more numerous agents need this, and that it enables collaboration and agents creating more agents. ([9:19](https://youtu.be/TRfzFJCJ7ZE?t=559))
- **Collaboration in shared live agent workspaces** — Teammates can see each other's agent workspaces in real time, chat inside them, and review each other's agent changes, for example asking for tabs instead of spaces. He calls collaboration one of the most important interface changes coming in this space. ([10:38](https://youtu.be/TRfzFJCJ7ZE?t=638))
- **Agents spawning agents through an API** — A separate agent (an OpenClaw-style bot) with access to Conductor's API receives requests from Telegram or Slack and creates new workspaces that start work on its own, so the user can start tasks away from the desk. ([13:21](https://youtu.be/TRfzFJCJ7ZE?t=801))
- **Orchestras, not factories** — He rejects the software-factory framing used by the rest of the program, saying factory language pushes people toward line-manager roles. He wants builders to conduct a team of humans and agents, zooming in on details when needed and out most of the time, and he argues tool builders should use words that make people feel capable. ([14:55](https://youtu.be/TRfzFJCJ7ZE?t=895))

## Techniques
- **Don't-beat-the-market test** — Ask whether a workflow is already the default in the harness. Only put effort into customizing it if you have private knowledge about your users or codebase that the models lack. *When:* Deciding whether to build custom tooling or prompts around a fast-moving agent feature such as a new loop mode.
- **Slot-free zones with CI-enforced human review** — Mark specific paths (migrations, for example) so that any change to them in CI requires a named human reviewer. Treat other paths, and human-written content such as Slack, as loosely reviewed. *When:* Agent-written code touches schema, data, or other high-blast-radius areas, and you want to move fast elsewhere.
- **CLAUDE.md / AGENTS.md and skills as onboarding material** — Keep the always-loaded instruction file and skill files carefully written, and treat them as a briefing you would give a new hire every day. *When:* Every agent session starts with little context about your team's conventions.
- **Central event store with a SQL tool for agents** — Ingest Slack, bug reports, and meeting recordings into one Postgres database, then give the agent a SQL tool so it can answer questions from company context. *When:* You want agents to know how your organization works, not only the repository.
- **Cloud sandboxes per task with lifecycle independent of the laptop** — Run each agent task in its own sandbox that keeps running when the client disconnects, and show the sandbox state in the UI. *When:* Tasks are long or numerous and you want agents to run while you are away.
- **Agents calling the product API to create work** — Expose the product's workspace-creation API to an agent that can be reached from chat apps, so it can start tasks itself. *When:* You want to start or manage agent runs from a phone or chat without opening the desktop app.

## Numbers
- Team has been power users of Claude Code since February of the prior year, which is when their workflow started forming ([2:38](https://youtu.be/TRfzFJCJ7ZE?t=158))
- Relying on social-graph tips means being 3 to 6 months behind the frontier ([2:38](https://youtu.be/TRfzFJCJ7ZE?t=158))
- Conductor rewrote its whole app a couple of times after mishandling slot-free zones ([5:11](https://youtu.be/TRfzFJCJ7ZE?t=311))
- Speaker says Conductor is not a pure token-maxer shipping 30,000-line PRs; reviews are strict in some areas and loose in others ([5:11](https://youtu.be/TRfzFJCJ7ZE?t=311))

## Hot takes
- The term 'software factory' is the wrong frame for AI coding tools, and builders should avoid it for their own sake.
- Most teams should wait for the default harness to ship a workflow rather than optimizing their own version of it.
- Teams should spend heavy effort on CLAUDE.md and skill files, not only on prompts.
- Collaboration on shared live agent workspaces will be one of the most important interface changes this year.

## Tools mentioned
Conductor, Claude Code, Codex, git worktrees, Postgres, Slack, Discord, Telegram, OpenClaw, React

## Relevance to our work
- **prosharness** (2/3): Checkpoint/resume plus phone-driven control already exist in ProsHarness; the talk's cloud-sandbox survival and agent-spawns-run API patterns map directly onto that design, and the slot-free-zone idea maps onto its approval gates. → *Check whether ProsHarness runs survive the laptop closing and whether a phone-triggered start-and-status path exists; add a required human-review gate for high-risk paths such as migrations.*
- **agentos** (1/3): The central store of org events with SQL access is close to the MemoryMesh and storage layers, and the reviewed-skills point bears on SkillForge, but the talk gives no measured results. → *Read the CIA ingestion idea against MemoryMesh: consider whether SkillForge's output skills should go through a human-review tier before they are loaded.*
